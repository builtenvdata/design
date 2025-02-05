# Imports from installed packages
import numpy as np
import openseespy.opensees as ops
from typing import Dict, List, Literal, Tuple

# Imports from bnsm library
from .node import Node
from .constants import (
    RIGID_SEC, RIGID_MAT,
    LINEAR_TRANSF_X, LINEAR_TRANSF_Y, LINEAR_TRANSF_Z)

# Imports from bdim base library
from ..bdim.baselib.joint import JointBase, Point

# Imports from utils library
from ...utils.misc import PRECISION, convert_numpy_types, round_list


class StairsJoint:
    """Class for defining stairs beam-column joint (at mid-storey level) in
    OpenSees.

    Attributes
    ----------
    design : JointBase
        Instance of joint design information model.
    center_node : Node
        Central joint node for connecting nodes at joint offset distances.
    left_node : Node | None
        The left joint node at offset distance along x-axis.
    right_node : Node | None
        The right joint node at offset distance along x-axis.
    bottom_node : Node | None
        The bottom joint node at offset distance along z-axis.
    top_node : Node | None
        The top joint node at offset distance along z-axis.
    """

    design: JointBase
    """Instance of joint design information model."""
    center_node: Node
    """Central joint node for connecting nodes at joint offset distances."""
    left_node: Node | None
    """The left joint node at offset distance along x-axis."""
    right_node: Node | None
    """The right joint node at offset distance along x-axis."""
    bottom_node: Node | None
    """The bottom joint node at offset distance along z-axis."""
    top_node: Node | None
    """The top joint node at offset distance along z-axis."""
    rigid_ele: List[int]
    """Tags of the rigid-like elements."""

    def __init__(self, design: JointBase, mass: float) -> None:
        """Initialize StairsJoint object.

        Parameters
        ----------
        design : JointBase
            Reference design information of joint.
        mass : float
            Total mass assigned to joint.
        """
        # Store rigid-like element tags
        self.rigid_ele = []
        # Save reference design information of joint
        self.design = design
        # Set reference node properties
        ref_tag = self.ref_point.tag
        ref_coords = self.ref_point.coordinates
        # Initialize center node
        masses = [mass, mass, mass, 0.0, 0.0, 0.0]
        self.center_node = Node(ref_tag, ref_coords, masses)
        # Initialize rigid offsets nodes
        if self.design.bottom_column:  # bottom
            coords = ref_coords.copy()
            coords[2] -= self.h/2
            self.bottom_node = Node(ref_tag + 20000, coords)
        else:
            self.bottom_node = None
        if self.design.right_beam:  # right
            coords = ref_coords.copy()
            coords[0] += self.bx/2
            self.right_node = Node(ref_tag + 30000, coords)
        else:
            self.right_node = None
        if self.design.left_beam:  # left
            coords = ref_coords.copy()
            coords[0] -= self.bx/2
            self.left_node = Node(ref_tag + 50000, coords)
        else:
            self.left_node = None
        if self.design.top_column:  # top
            coords = ref_coords.copy()
            coords[2] += self.h/2
            self.top_node = Node(ref_tag + 70000, coords)
        else:
            self.top_node = None

    @property
    def bx(self) -> float:
        """
        Returns
        -------
        float
            Joint width along global x-axis (based on columns' section widths).
        """
        bx = 0.0
        if self.design.top_column:
            bx = max(bx, self.design.top_column.bx)
        if self.design.bottom_column:
            bx = max(bx, self.design.bottom_column.bx)
        return bx

    @property
    def by(self) -> float:
        """
        Returns
        -------
        float
            Joint width along global y-axis (based on columns' section widths).
        """
        by = 0.0
        if self.design.top_column:
            by = max(by, self.design.top_column.by)
        if self.design.bottom_column:
            by = max(by, self.design.bottom_column.by)
        return by

    @property
    def h(self) -> float:
        """
        Returns
        -------
        float
            Joint height based on all beam section heights.

        Notes
        -----
        The largest of the beam heights is selected.
        """
        h = 0.0
        if self.design.left_beam:
            h = max(h, self.design.left_beam.h)
        if self.design.right_beam:
            h = max(h, self.design.right_beam.h)
        if self.design.rear_beam:
            h = max(h, self.design.rear_beam.h)
        if self.design.front_beam:
            h = max(h, self.design.front_beam.h)

        return h

    @property
    def ref_point(self) -> Point:
        """
        Returns
        -------
        Point
            Reference point in joint of basic geometry.
        """
        return self.design.elastic_node

    def add_to_ops(self) -> None:
        """Adds stairs joint model objects to the OpenSees domain (i.e,
        rigid joint offsets elements and nodes).
        """
        # Central joint node
        self.center_node.add_to_ops()
        # Rigid-joint offset elements
        if self.left_node:
            self.left_node.add_to_ops()
            ele_nodes = [self.left_node.tag, self.center_node.tag]
            ele_tag = self.left_node.tag
            ops.element('elasticBeamColumn', ele_tag, *ele_nodes,
                        RIGID_SEC, LINEAR_TRANSF_X)
            self.rigid_ele.append(ele_tag)
        if self.right_node:
            self.right_node.add_to_ops()
            ele_nodes = [self.center_node.tag, self.right_node.tag]
            ele_tag = self.right_node.tag
            ops.element('elasticBeamColumn', ele_tag, *ele_nodes,
                        RIGID_SEC, LINEAR_TRANSF_X)
            self.rigid_ele.append(ele_tag)
        if self.bottom_node:
            self.bottom_node.add_to_ops()
            ele_nodes = [self.bottom_node.tag, self.center_node.tag]
            ele_tag = self.bottom_node.tag
            ops.element('elasticBeamColumn', ele_tag, *ele_nodes,
                        RIGID_SEC, LINEAR_TRANSF_Z)
            self.rigid_ele.append(ele_tag)
        if self.top_node:
            self.top_node.add_to_ops()
            ele_nodes = [self.center_node.tag, self.top_node.tag]
            ele_tag = self.top_node.tag
            ops.element('elasticBeamColumn', ele_tag, *ele_nodes,
                        RIGID_SEC, LINEAR_TRANSF_Z)
            self.rigid_ele.append(ele_tag)

    def to_py(self) -> List[str]:
        """Gets the Python commands to define stairs joint model objects in
        the OpenSees domain (i.e, rigid joint offsets elements and nodes).

        Returns
        -------
        List[str]
            List of Python commands for constructing the components of stairs
            joint in OpenSees.
        """
        grids = ', '.join([f"{i}" for i in self.design.elastic_node.grid_ids])
        content = [f'# Joint grid ids (x, y, z): ({grids})']
        content.append("# Central joint node")
        content.append(self.center_node.to_py())
        content.append("# Rigid-joint offset elements")
        if self.left_node:
            content.append(self.left_node.to_py())
            ele_nodes = f"{self.left_node.tag}, {self.center_node.tag}"
            ele_tag = self.left_node.tag
            content.append(
                f"ops.element('elasticBeamColumn', {ele_tag}, {ele_nodes}, "
                f"{RIGID_SEC}, {LINEAR_TRANSF_X})"
            )
        if self.right_node:
            content.append(self.right_node.to_py())
            ele_nodes = f"{self.center_node.tag}, {self.right_node.tag}"
            ele_tag = self.right_node.tag
            content.append(
                f"ops.element('elasticBeamColumn', {ele_tag}, {ele_nodes}, "
                f"{RIGID_SEC}, {LINEAR_TRANSF_X})"
            )
        if self.bottom_node:
            content.append(self.bottom_node.to_py())
            ele_nodes = f"{self.bottom_node.tag}, {self.center_node.tag}"
            ele_tag = self.bottom_node.tag
            content.append(
                f"ops.element('elasticBeamColumn', {ele_tag}, {ele_nodes}, "
                f"{RIGID_SEC}, {LINEAR_TRANSF_Z})"
            )
        if self.top_node:
            content.append(self.top_node.to_py())
            ele_nodes = f"{self.center_node.tag}, {self.top_node.tag}"
            ele_tag = self.top_node.tag
            content.append(
                f"ops.element('elasticBeamColumn', {ele_tag}, {ele_nodes}, "
                f"{RIGID_SEC}, {LINEAR_TRANSF_Z})"
            )

        return content

    def to_tcl(self) -> List[str]:
        """Gets the Tcl commands to define stairs joint model objects in
        the OpenSees domain (i.e, rigid joint offsets elements and nodes).

        Returns
        -------
        List[str]
            List of Tcl commands for constructing the components of stairs
            joint in OpenSees.
        """
        grids = ', '.join([f"{i}" for i in self.design.elastic_node.grid_ids])
        content = [f'# Joint grid ids (x, y, z): ({grids})']
        content.append("# Central joint node")
        content.append(self.center_node.to_tcl())
        content.append("# Rigid-joint offset elements")
        if self.left_node:
            content.append(self.left_node.to_tcl())
            ele_nodes = f"{self.left_node.tag} {self.center_node.tag}"
            ele_tag = self.left_node.tag
            content.append(
                f"element elasticBeamColumn {ele_tag} {ele_nodes} "
                f"{RIGID_SEC} {LINEAR_TRANSF_X}"
            )
        if self.right_node:
            content.append(self.right_node.to_tcl())
            ele_nodes = f"{self.center_node.tag} {self.right_node.tag}"
            ele_tag = self.right_node.tag
            content.append(
                f"element elasticBeamColumn {ele_tag} {ele_nodes} "
                f"{RIGID_SEC} {LINEAR_TRANSF_X}"
            )
        if self.bottom_node:
            content.append(self.bottom_node.to_tcl())
            ele_nodes = f"{self.bottom_node.tag} {self.center_node.tag}"
            ele_tag = self.bottom_node.tag
            content.append(
                f"element elasticBeamColumn {ele_tag} {ele_nodes} "
                f"{RIGID_SEC} {LINEAR_TRANSF_Z}"
            )
        if self.top_node:
            content.append(self.top_node.to_tcl())
            ele_nodes = f"{self.center_node.tag} {self.top_node.tag}"
            ele_tag = self.top_node.tag
            content.append(
                f"element elasticBeamColumn {ele_tag} {ele_nodes} "
                f"{RIGID_SEC} {LINEAR_TRANSF_Z}"
            )

        return content


class FloorJoint(StairsJoint):
    """Class for defining floor beam-column joint (at floor levels) in
    OpenSees.

    Attributes
    ----------
    design : JointBase
        Instance of joint design information model.
    center_node : Node
        Central joint node for connecting nodes at joint offset distances.
    floor_node : Node
        Floor node which is constrained by floor diaphragm.
    left_node : Node | None
        The left joint node at offset distance along x-axis.
    right_node : Node | None
        The right joint node at offset distance along x-axis.
    bottom_node : Node | None
        The bottom joint node at offset distance along z-axis.
    top_node : Node | None
        The top joint node at offset distance along z-axis.
    rear_node : Node | None
        The rear joint node at offset distance along y-axis.
    front_node : Node | None
        The front joint node at offset distance along y-axis.
    flexibility_model : Literal['inelastic', 'elastic', 'rigid']
        Joint flexibility model.

    References
    ----------
    O'Reilly, G. J. (2016). Performance-based seismic assessment and
    retrofit of existing RC frame buildings in Italy
    (Doctoral dissertation, IUSS Pavia).

    O'Reilly, G. J., & Sullivan, T. J. (2019). Modeling techniques for
    the seismic assessment of the existing Italian RC frame structures.
    Journal of Earthquake Engineering, 23(8), 1262-1296.

    GitHub - gerardjoreilly/Numerical-Modelling-of-GLD-RC-Frames: Set of
    OpenSees procedures used to model RC frames designed prior to the 1970s
    in Italy, as outlined and calibrated in O'Reilly & Sullivan [2019].
    https://github.com/gerardjoreilly/Numerical-Modelling-of-GLD-RC-Frames.
    Accessed 21 Oct 2024.
    """

    floor_node: Node
    """Floor node which is constrained by floor diaphragm."""
    rear_node: Node | None
    """The rear joint node at offset distance along y-axis."""
    front_node: Node | None
    """The front joint node at offset distance along y-axis."""
    flexibility_model: Literal["inelastic", "elastic", "rigid"]
    """Joint flexibility model."""
    axial_force: float
    """Axial force acting on joint."""

    def __init__(self, design: JointBase, mass: float,
                 model: Literal["inelastic", "elastic", "rigid"],
                 load_factors: Dict[Literal['G', 'Q'], float]) -> None:
        """Initialize FloorJoint object.

        Parameters
        ----------
        design : JointBase
            Reference design information of joint.
        mass : float
            Total mass assigned to joint.
        model : Literal["inelastic", "elastic", "rigid"]
            Joint flexibility model.
        load_factors : Dict[Literal['G', 'Q'], float]
            Load factors used to compute axial load on joint.
        """
        # Save joint flexibility model option
        self.flexibility_model = model
        # Initialize the nodes in stairs joint
        super().__init__(design, mass)
        # Initialize the floor node to account for joint flexibility
        self.floor_node = Node(self.ref_point.tag + 10000,
                               self.ref_point.coordinates)
        # Initialize rigid offsets (in Y) nodes
        if self.design.front_beam:  # front
            coords = self.ref_point.coordinates.copy()
            coords[1] += self.by/2
            self.front_node = Node(self.ref_point.tag + 40000, coords)
        else:
            self.front_node = None
        if self.design.rear_beam:  # rear
            coords = self.ref_point.coordinates.copy()
            coords[1] -= self.by/2
            self.rear_node = Node(self.ref_point.tag + 60000, coords)
        else:
            self.rear_node = None
        # Axial force on the joint
        if self.design.bottom_column:
            # forces = (
            #     load_factors['G'] *
            #     self.design.bottom_column.forces['G/seismic'] +
            #     load_factors['Q'] *
            #     self.design.bottom_column.forces['Q/seismic']
            # )
            # self.axial_load = -forces.N9
            self.axial_force = (
                load_factors['G'] * self.design.bottom_column.pre_Nq +
                load_factors['Q'] * self.design.bottom_column.pre_Ng
                )
        else:
            raise ValueError(
                "Bottom column is missing, joint model won't work here.")

    def add_to_ops(self) -> None:
        """Adds floor joint model objects to the OpenSees domain (i.e, rigid
        joint offsets elements, nodes and joint flexibility element).
        """
        super().add_to_ops()
        # Rigid-joint offset elements along Y
        if self.rear_node:
            self.rear_node.add_to_ops()
            ele_nodes = [self.rear_node.tag, self.center_node.tag]
            ele_tag = self.rear_node.tag
            ops.element('elasticBeamColumn', ele_tag, *ele_nodes,
                        RIGID_SEC, LINEAR_TRANSF_Y)
            self.rigid_ele.append(ele_tag)
        if self.front_node:
            self.front_node.add_to_ops()
            ele_nodes = [self.center_node.tag, self.front_node.tag]
            ele_tag = self.front_node.tag
            ops.element('elasticBeamColumn', ele_tag, *ele_nodes,
                        RIGID_SEC, LINEAR_TRANSF_Y)
            self.rigid_ele.append(ele_tag)

        # Joint flexibility element
        ele_nodes = [self.center_node.tag, self.floor_node.tag]
        ele_tag = self.floor_node.tag

        if self.flexibility_model == 'rigid':  # Use rigid section
            sec_tag = RIGID_SEC
        else:  # Use new section with flexible rotation behaviour
            sec_tag = self.floor_node.tag
            mz_mat = 300000 + self.center_node.tag
            my_mat = 400000 + self.center_node.tag

            if self.flexibility_model == 'elastic':  # Elastic rotation
                krot_z, krot_y = self._get_elastic_joint_params()
                ops.uniaxialMaterial('Elastic', mz_mat, krot_z)
                ops.uniaxialMaterial('Elastic', my_mat, krot_y)

            elif self.flexibility_model == 'inelastic':  # Inelastic rotation
                inputs_rot_z, inputs_rot_y = self._get_inelastic_joint_params()
                ops.uniaxialMaterial('Hysteretic', mz_mat, *inputs_rot_z)
                ops.uniaxialMaterial('Hysteretic', my_mat, *inputs_rot_y)

            # Define the new section with flexible rotation behaviour
            ops.section('Aggregator', sec_tag,
                        RIGID_MAT, 'P', RIGID_MAT, 'Vy', RIGID_MAT, 'Vz',
                        my_mat, 'My', mz_mat, 'Mz', RIGID_MAT, 'T')

        # Define the joint flexibility element
        ops.element('zeroLengthSection', ele_tag, *ele_nodes,
                    sec_tag, '-orient', 0, 0, 1, 0, 1, 0)

    def to_py(self) -> List[str]:
        """Gets the Python commands to define floor joint model objects in
        the OpenSees domain (i.e, rigid joint offsets elements, nodes and joint
        flexibility element).

        Returns
        -------
        List[str]
            List of Python commands for constructing the components of floor
            joint in OpenSees.
        """
        content = super().to_py()
        # Rigid-joint offset elements along Y
        if self.rear_node:
            content.append(self.rear_node.to_py())
            ele_nodes = f"{self.rear_node.tag}, {self.center_node.tag}"
            ele_tag = self.rear_node.tag
            content.append(
                f"ops.element('elasticBeamColumn', {ele_tag}, {ele_nodes}, "
                f"{RIGID_SEC}, {LINEAR_TRANSF_Y})"
            )
        if self.front_node:
            content.append(self.front_node.to_py())
            ele_nodes = f"{self.center_node.tag}, {self.front_node.tag}"
            ele_tag = self.front_node.tag
            content.append(
                f"ops.element('elasticBeamColumn', {ele_tag}, {ele_nodes}, "
                f"{RIGID_SEC}, {LINEAR_TRANSF_Y})"
            )

        # Joint flexibility element
        ele_nodes = f"{self.center_node.tag}, {self.floor_node.tag}"
        ele_tag = self.floor_node.tag

        if self.flexibility_model == 'rigid':  # Use rigid section
            content.append("# Joint flexibility element: Rigid")
            sec_tag = RIGID_SEC
        else:  # Use new section with flexible rotation behaviour
            sec_tag = self.floor_node.tag
            mz_mat = 300000 + self.center_node.tag
            my_mat = 400000 + self.center_node.tag

            if self.flexibility_model == 'elastic':  # Elastic rotation
                content.append("# Joint flexibility element: Elastic")
                krot_z, krot_y = self._get_elastic_joint_params()
                content.append(
                    f"ops.uniaxialMaterial('Elastic', {mz_mat}, {krot_z})"
                    )
                content.append(
                    f"ops.uniaxialMaterial('Elastic', {my_mat}, {krot_y})"
                    )

            elif self.flexibility_model == 'inelastic':  # Inelastic rotation
                content.append("# Joint flexibility element: Inelastic")
                inputs_rot_z, inputs_rot_y = self._get_inelastic_joint_params()
                rot_z = ', '.join([f"{item}" for item in inputs_rot_z])
                rot_y = ', '.join([f"{item}" for item in inputs_rot_y])
                content.append(
                    f"ops.uniaxialMaterial('Hysteretic', {mz_mat}, {rot_z})"
                    )
                content.append(
                    f"ops.uniaxialMaterial('Hysteretic', {my_mat}, {rot_y})"
                    )

            # Define the new section with flexible rotation behaviour
            content.append(
                f"ops.section('Aggregator', {sec_tag}, "
                f"{RIGID_MAT}, 'P', {RIGID_MAT}, 'Vy', {RIGID_MAT}, 'Vz', "
                f"{my_mat}, 'My', {mz_mat}, 'Mz', {RIGID_MAT}, 'T')"
            )

        # Define the joint flexibility element
        content.append(
            f"ops.element('zeroLengthSection', {ele_tag}, {ele_nodes}, "
            f"{sec_tag}, '-orient', 0, 0, 1, 0, 1, 0)"
        )

        return content

    def to_tcl(self) -> List[str]:
        """Gets the Tcl commands to define floor joint model objects in
        the OpenSees domain (i.e, rigid joint offsets elements, nodes and joint
        flexibility element).

        Returns
        -------
        List[str]
            List of Tcl commands for constructing the components of floor
            joint in OpenSees.
        """
        content = super().to_tcl()
        # Rigid-joint offset elements along Y
        if self.rear_node:
            content.append(self.rear_node.to_tcl())
            ele_nodes = f"{self.rear_node.tag} {self.center_node.tag}"
            ele_tag = self.rear_node.tag
            content.append(
                f"element elasticBeamColumn {ele_tag} {ele_nodes} "
                f"{RIGID_SEC} {LINEAR_TRANSF_Y}"
            )
        if self.front_node:
            content.append(self.front_node.to_tcl())
            ele_nodes = f"{self.center_node.tag} {self.front_node.tag}"
            ele_tag = self.front_node.tag
            content.append(
                f"element elasticBeamColumn {ele_tag} {ele_nodes} "
                f"{RIGID_SEC} {LINEAR_TRANSF_Y}"
            )

        # Joint flexibility element
        ele_nodes = f"{self.center_node.tag} {self.floor_node.tag}"
        ele_tag = self.floor_node.tag

        if self.flexibility_model == 'rigid':  # Use rigid section
            content.append("# Joint flexibility element: Rigid")
            sec_tag = RIGID_SEC
        else:  # Use new section with flexible rotation behaviour
            sec_tag = self.floor_node.tag
            mz_mat = 300000 + self.center_node.tag
            my_mat = 400000 + self.center_node.tag

            if self.flexibility_model == 'elastic':  # Elastic rotation
                content.append("# Joint flexibility element: Elastic")
                krot_z, krot_y = self._get_elastic_joint_params()
                content.append(
                    f"uniaxialMaterial Elastic {mz_mat} {krot_z}"
                    )
                content.append(
                    f"uniaxialMaterial Elastic {my_mat} {krot_y}"
                    )

            elif self.flexibility_model == 'inelastic':  # Inelastic rotation
                content.append("# Joint flexibility element: Inelastic")
                inputs_rot_z, inputs_rot_y = self._get_inelastic_joint_params()
                rot_z = ' '.join([f"{item}" for item in inputs_rot_z])
                rot_y = ' '.join([f"{item}" for item in inputs_rot_y])
                content.append(
                    f"uniaxialMaterial Hysteretic {mz_mat} {rot_z}"
                    )
                content.append(
                    f"uniaxialMaterial Hysteretic {my_mat} {rot_y}"
                    )

            # Define the new section with flexible rotation behaviour
            content.append(
                f"section Aggregator {sec_tag} "
                f"{RIGID_MAT} P {RIGID_MAT} Vy {RIGID_MAT} Vz "
                f"{my_mat} My {mz_mat} Mz {RIGID_MAT} T"
            )

        # Define the joint flexibility element
        content.append(
            f"element zeroLengthSection {ele_tag} {ele_nodes} "
            f"{sec_tag} -orient 0 0 1 0 1 0"
        )

        return content

    @property
    def category_x(self) -> Literal['roof', 'exterior', 'interior']:
        """
        Returns
        -------
        Literal['roof', 'exterior', 'interior']
            Joint category along-x axis based on its location.
        """
        if self.design.top_column is None:
            return 'roof'
        else:
            beams = [self.design.left_beam, self.design.right_beam]
            if None in beams:
                return 'exterior'
            else:
                return 'interior'

    @property
    def category_y(self) -> Literal['roof', 'exterior', 'interior']:
        """
        Returns
        -------
        Literal['roof', 'exterior', 'interior']
            Joint category along-y axis based on its location.
        """
        if self.design.top_column is None:
            return 'roof'
        else:
            beams = [self.design.front_beam, self.design.rear_beam]
            if None in beams:
                return 'exterior'
            else:
                return 'interior'

    @property
    def fcm(self) -> float:
        """
        Returns
        -------
        float
            Mean value of concrete compressive strength (in base units).
        """
        return self.design.fcm

    @property
    def hstorey(self) -> float:
        """
        Returns
        -------
        float
            Itnernal storey height

        Notes
        -----
        The equations were derived using constant storey height.
        If possible the average one is used.
        """
        if self.design.top_column is None:
            return self.design.bottom_column.H
        elif self.design.bottom_column is None:
            return self.design.top_column.H
        else:
            return self.design.top_column.H

    @property
    def bb_x(self) -> float:
        """
        Returns
        -------
        float
            Maximum of beam section widths (view along x or in yz-plane).
        """
        bbx = 0.0
        if self.design.front_beam:
            bbx = max(bbx, self.design.front_beam.b)
        if self.design.rear_beam:
            bbx = max(bbx, self.design.rear_beam.b)
        return bbx

    @property
    def hc_x(self) -> float:
        """
        Returns
        -------
        float
            Maximum of column section heights (view along x or in yz-plane).
        """
        return self.bx

    @property
    def bc_x(self) -> float:
        """
        Returns
        -------
        float
            Maximum of column section widths (view along x or in yz-plane).
        """
        return self.by

    @property
    def hc_y(self) -> float:
        """
        Returns
        -------
        float
            Maximum of column section heights (view along y or in xz-plane).
        """
        return self.by

    @property
    def bc_y(self) -> float:
        """
        Returns
        -------
        float
            Maximum of column section widths (view along y or in xz-plane).
        """
        return self.bx

    @property
    def bb_y(self) -> float:
        """
        Returns
        -------
        float
            Maximum of beam section widths (view along y or in xz-plane).
        """
        bby = 0.0
        if self.design.right_beam:
            bby = max(bby, self.design.right_beam.b)
        if self.design.left_beam:
            bby = max(bby, self.design.left_beam.b)
        return bby

    @property
    def hb_x(self) -> float:
        """
        Returns
        -------
        float
            Maximum of beam section heights (view along x or in yz-plane).
        """
        hx = 0.0
        if self.design.left_beam:
            hx = max(hx, self.design.left_beam.h)
        if self.design.right_beam:
            hx = max(hx, self.design.right_beam.h)

        return hx

    @property
    def hb_y(self) -> float:
        """
        Returns
        -------
        float
            Maximum of beam section heights (view along y or in xz-plane).
        """
        hy = 0.0
        if self.design.rear_beam:
            hy = max(hy, self.design.rear_beam.h)
        if self.design.front_beam:
            hy = max(hy, self.design.front_beam.h)

        return hy

    def _get_elastic_joint_params(self) -> Tuple[float, float]:
        """Gets the parameters for elastic joint materials.

        Returns
        -------
        krot_y : float
            Stiffness of elastic spring representing rotational behaviour
            around global-y.
        krot_x : float
            Stiffness of elastic spring representing rotational behaviour
            around global-x.

        TODO
        ----
        Even though original implementation by Gerard O'Reilly used the
        expression for interior joints, I believe this was done for the
        sake of simplicity. Let's just use the corresponding equations.
        """
        # Get the hysteretic material inputs
        inputs_rot_y, inputs_rot_x = self._get_inelastic_joint_params()

        # Compute elastic stiffness values
        krot_y = inputs_rot_y[0] / inputs_rot_y[1]
        krot_x = inputs_rot_x[0] / inputs_rot_x[1]

        # Rounding to precision
        krot_y = round(float(krot_y), PRECISION)
        krot_x = round(float(krot_x), PRECISION)

        return krot_y, krot_x

    def _get_inelastic_joint_params(self) -> Tuple[List[float], List[float]]:
        """Gets the material properties for inelastic joint behaviour, i.e.,
        hysteretic material model parameters.

        Returns
        -------
        roty_mat_inputs : List[float]
            List of inputs for the material representing rotational behaviour
            around global y-axis.
        rotx_mat_inputs : List[float]
            List of inputs for the material representing rotational behaviour
            around global x-axis.

        Notes
        -----
        The constants slightly different than those in the references.
        The new calibrated values were directly provided by Gerard O'Reilly.

        TODO
        ----
        Due to the lack of data, equation described for roof was not validated.
        However, we rarely except nonlinearity for joints at the last floor.
        So, this has the least significance. Let's keep using it for now?
        """
        # Shear deformations for each limit state: cracking, peak, ultimate
        gamma_int = 2 * [0.0002, 0.0090, 0.0200]
        gamma_ext = 2 * [0.0002, 0.0132, 0.0270]
        gamma_roof = 2 * [0.0002, 0.0132, 0.0270]
        # Shear strength coefficients for each LS: cracking, peak, ultimate
        kappa_int = 2 * [0.29, 0.42, 0.42]
        kappa_ext = 2 * [0.132, 0.132, 0.053]
        kappa_roof = 2 * [0.132, 0.132, 0.053]
        # Hysteretic parameters (pinchx, pinchy, damage1, damage2, beta)
        if 'exterior' in [self.category_x, self.category_y] \
           or 'roof' in [self.category_x, self.category_y]:
            hyst_params = [0.6, 0.2, 0.0, 0.0, 0.3]  # exterior or roof joint
        else:
            hyst_params = [0.6, 0.2, 0.0, 0.01, 0.3]  # interior joint

        # Principle tensile stress values Equation 2.34 (O'Reilly, 2016)
        pt_ext = np.array(kappa_ext) * (self.fcm**0.5)
        pt_int = np.array(kappa_int) * (self.fcm**0.5)
        pt_roof = np.array(kappa_roof) * (self.fcm**0.5)

        # Joint width definition Equation 2.48 (O'Reilly, 2016)
        # Y direction
        if self.bc_y >= self.bb_y:
            bj_y = min(self.bc_y, self.bb_y + 0.5*self.hc_y)
        else:
            bj_y = min(self.bb_y, self.bc_y + 0.5*self.hc_y)
        # X direction
        if self.bc_x >= self.bb_x:
            bj_x = min(self.bc_x, self.bb_x + 0.5*self.hc_x)
        else:
            bj_x = min(self.bb_x, self.bc_x + 0.5*self.hc_x)

        # Lever arm, i.e., distance between comp. and tens. forces
        jd_y = 0.9 * (0.9 * self.hb_y)
        jd_x = 0.9 * (0.9 * self.hb_x)

        # Stress and strain values for material around global-y
        if self.category_y == 'exterior':  # Exterior joint
            # Equation 2.33 (O'Reilly, 2016)
            Mj_y = (pt_ext * bj_y * self.hc_y) * \
                (self.hstorey * jd_y) / (self.hstorey - jd_y) * (
                    (self.hb_y / (2*self.hc_y)) + (
                        (self.hb_y / (2*self.hc_y))**2 +
                        1 +
                        (self.axial_force / (pt_ext * bj_y * self.hc_y))
                    )**0.5
                 )
            # Strain values
            gamma_y = gamma_ext.copy()

        elif self.category_y == 'interior':  # Interior joint
            # Equation 2.55 (O'Reilly, 2016)
            Mj_y = (pt_int * bj_y * self.hc_y) * \
                (self.hstorey * jd_y) / (self.hstorey - jd_y) * \
                (1 + (self.axial_force / (pt_int * bj_y * self.hc_y)))**0.5
            # Strain values
            gamma_y = gamma_int.copy()

        elif self.category_y == 'roof':  # Roof joint
            # This equation comes from the model online.
            Mj_y = 2 * (pt_roof * bj_y * self.hc_y) * jd_y * (
                    (self.hb_y / (2*self.hc_y)) + (
                        (self.hb_y / (2*self.hc_y))**2 +
                        1 +
                        (self.axial_force / (pt_roof * bj_y * self.hc_y))
                    )**0.5
                 )
            # Strain values
            gamma_y = gamma_roof.copy()

        # Stress and strain values for material around global-x
        if self.category_x == 'exterior':  # Exterior joint
            # Equation 2.33 (O'Reilly, 2016)
            Mj_x = (pt_ext * bj_x * self.hc_x) * \
                (self.hstorey * jd_x) / (self.hstorey - jd_x) * (
                    (self.hb_x / (2*self.hc_x)) + (
                        (self.hb_x / (2*self.hc_x))**2 +
                        1 +
                        (self.axial_force / (pt_ext * bj_x * self.hc_x))
                    )**0.5
                 )
            # Strain values
            gamma_x = gamma_ext.copy()

        elif self.category_x == 'interior':  # Interior joint
            # Equation 2.55 (O'Reilly, 2016)
            Mj_x = (pt_int * bj_x * self.hc_x) * \
                (self.hstorey * jd_x) / (self.hstorey - jd_x) * \
                (1 + (self.axial_force / (pt_int * bj_x * self.hc_x)))**0.5
            # Strain values
            gamma_x = gamma_int.copy()

        elif self.category_x == 'roof':  # Exterior joint
            # This equation comes from the model online.
            Mj_x = 2 * (pt_roof * bj_x * self.hc_x) * jd_x * (
                    (self.hb_x / (2*self.hc_x)) + (
                        (self.hb_x / (2*self.hc_x))**2 +
                        1 +
                        (self.axial_force / (pt_roof * bj_x * self.hc_x))
                    )**0.5
                 )
            # Strain values
            gamma_x = gamma_roof.copy()

        # Inputs for material representing rotational behaviour around global-y
        roty_mat_inputs = []
        # Inputs for material representing rotational behaviour around global-x
        rotx_mat_inputs = []
        for i in range(6):
            if i < 3:
                roty_mat_inputs.extend([Mj_y[i], gamma_y[i]])
                rotx_mat_inputs.extend([Mj_x[i], gamma_x[i]])
            else:
                roty_mat_inputs.extend([-Mj_y[i], -gamma_y[i]])
                rotx_mat_inputs.extend([-Mj_x[i], -gamma_x[i]])

        # Add hysteretic parameters
        roty_mat_inputs.extend(hyst_params)
        rotx_mat_inputs.extend(hyst_params)

        # Rounding to precision
        roty_mat_inputs = round_list(convert_numpy_types(roty_mat_inputs))
        rotx_mat_inputs = round_list(convert_numpy_types(rotx_mat_inputs))

        return roty_mat_inputs, rotx_mat_inputs
