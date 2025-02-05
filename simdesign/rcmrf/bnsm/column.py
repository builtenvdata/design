# Imports from installed packages
import numpy as np
import openseespy.opensees as ops
from typing import Dict, Literal, List, Tuple

# Imports from bnsm library
from .node import Node
from .constants import RIGID_MAT, PDELTA_TRANSF_Z

# Imports from bdim base library
from ..bdim.baselib.column import ColumnBase

# Imports from utils library
from ...utils.units import MPa, MN
from ...utils.misc import PRECISION, round_list


class Column:
    """Column class which can be used to define column elements
    in OpenSees.

    Attributes
    ----------
    design : ColumnBase
        Instance of column design information model.
    capacity_design : bool
        Flag to check whether capacity shear design is followed or not.
    bondslip_factor : float
        Bondslip factor considered while defining plastic hinges.
    axial_force: float
        Considered axial force on column for plastic hinge calculations.
    ele_node_i : Node
        Element node at the start of column.
    ele_node_j : Node
        Element node at the end of column.
    ele_load: float
        Uniformly distributed gravity load along the column.
    hinge_node_i : Node
        Extra node considered for hinge definition at the start of column.
    hinge_node_j : Node
        Extra node considered for hinge definition at the end of column.
    """

    design: ColumnBase
    """Instance of column design information model."""
    capacity_design: bool
    """Flag to check whether capacity shear design is followed or not."""
    bondslip_factor: float
    """Bondslip factor considered while defining plastic hinges."""
    axial_force: float
    """Considered axial force on column for plastic hinge calculations."""
    ele_node_i: Node
    """Element node at the start of column."""
    ele_node_j: Node
    """Element node at the end end of column."""
    ele_load: float
    """Uniformly distributed gravity load along the column."""
    hinge_node_i: Node
    """Extra node considered for hinge definition at the start of column."""
    hinge_node_j: Node
    """Extra node considered for hinge definition at the end of column."""

    @property
    def ele_tag(self) -> int:
        """
        Returns
        -------
        int
            Tag of beam-column element representing elastic part of the column.
        """
        return self.design.line.tag

    @property
    def hinge_i_tag(self) -> int:
        """
        Returns
        -------
        int
            Tag of hinge element at the start of the column.
        """
        return self.ele_node_i.tag

    @property
    def hinge_j_tag(self) -> int:
        """
        Returns
        -------
        int
            Tag of hinge element at the end of the column.
        """
        return self.ele_node_j.tag

    @property
    def Ecm_q(self) -> float:
        """
        Returns
        -------
        float
            Elastic young's modulus of concrete (in base units).

        Note
        ----
        Based on quality adjusted concrete strength.
        """
        # Use quality adjusted elastic youngs modulus
        fc_mpa = self.design.fc_q / MPa  # convert to MPa
        return (22000 * (fc_mpa / 10)**0.3) * MPa

    @property
    def Gcm_q(self) -> float:
        """
        Returns
        -------
        float
            Elastic shear modulus of concrete (in base units).

        Note
        ----
        Based on quality adjusted concrete strength.
        """
        return self.Ecm_q / (2 * (1 + self.design.concrete.POISSONS_RATIO))

    def __init__(
        self, design: ColumnBase, bondslip_factor: float,
        capacity_design: bool, load_factors: Dict[Literal['G', 'Q'], float]
    ) -> None:
        """Initialize the Column object.

        Parameters
        ----------
        design : ColumnBase
            Instance of column design information model.
        bondslip_factor : float
            Bondslip factor considered while defining plastic hinges.
        capacity_design : bool
            Flag to check whether capacity shear design is followed or not.
        load_factors : Dict[Literal['G', 'Q'], float]
            Load factors used to compute gravity loads/forces on the column.
        """
        self.design = design
        self.bondslip_factor = bondslip_factor
        self.capacity_design = capacity_design
        # forces = design.position_factor * (
        #     load_factors['G'] *
        #     self.design.forces['G/seismic'] +
        #     load_factors['Q'] *
        #     self.design.forces['Q/seismic']
        # )
        # self.axial_force = (forces.N1 + forces.N9) / 2
        self.axial_force = -(load_factors['G'] * design.pre_Nq +
                             load_factors['Q'] * design.pre_Ng)
        self.ele_load = float(design.self_wg * load_factors['G'])

    def set_ele_node_i(self) -> None:
        """Initialize and set ele_node_i based on hinge_node_i.
        """
        coords = self.hinge_node_i.coordinates.copy()
        tag = self.hinge_node_i.tag + 100000
        self.ele_node_i = Node(tag, coords)

    def set_ele_node_j(self) -> None:
        """Initialize and set ele_node_j based on hinge_node_j.
        """
        coords = self.hinge_node_j.coordinates.copy()
        tag = self.hinge_node_j.tag + 100000
        self.ele_node_j = Node(tag, coords)

    def add_to_ops(self) -> None:
        """Adds beam column to the OpenSees domain
        (i.e, plastic hinges, elastic column element and nodes).

        Notes
        -----
        Same hinge materials are used at both ends.
        """
        # Create column element nodes
        self.ele_node_i.add_to_ops()
        self.ele_node_j.add_to_ops()

        # Create elastic column element
        ele_inputs = self._get_elastic_ele_inputs()
        ops.element('elasticBeamColumn', *ele_inputs)

        # Get inputs for materials describing plastic hinge behaviour
        my_hys_mat_inputs, vy_limit_curve_inputs, vy_limit_state_mat_inputs = \
            self._get_hinge_mat_inputs(axis='y')
        mz_hys_mat_inputs, vz_limit_curve_inputs, vz_limit_state_mat_inputs = \
            self._get_hinge_mat_inputs(axis='x')

        # Create materials describing flexural behaviour of plastic hinge
        my_tag = my_hys_mat_inputs[0]
        mz_tag = mz_hys_mat_inputs[0]
        ops.uniaxialMaterial('Hysteretic', *my_hys_mat_inputs)
        ops.uniaxialMaterial('Hysteretic', *mz_hys_mat_inputs)

        # Create or set materials describing shear behaviour of plastic hinge
        if self.capacity_design:  # Use rigid material for shear behaviour
            vy_tag = RIGID_MAT
            vz_tag = RIGID_MAT
        else:  # Create shear hinge materials
            vy_tag = vy_limit_state_mat_inputs[0]
            vz_tag = vz_limit_state_mat_inputs[0]
            ops.limitCurve('ThreePoint', *vy_limit_curve_inputs)
            ops.uniaxialMaterial('LimitState', *vy_limit_state_mat_inputs)
            ops.limitCurve('ThreePoint', *vz_limit_curve_inputs)
            ops.uniaxialMaterial('LimitState', *vz_limit_state_mat_inputs)

        # Create plastic hinge sections at both ends
        sec_tag = self.design.line.tag
        ops.section('Aggregator', sec_tag,
                    RIGID_MAT, 'P', vy_tag, 'Vy', vz_tag, 'Vz',
                    my_tag, 'My', mz_tag, 'Mz', RIGID_MAT, 'T')

        # Create plastic hinge elements at both ends
        orientation = [0, 0, 1, 0, 1, 0]
        ele_i_tag = self.ele_node_i.tag
        ele_i_nodes = [self.hinge_node_i.tag, self.ele_node_i.tag]
        ele_j_tag = self.ele_node_j.tag
        ele_j_nodes = [self.ele_node_j.tag, self.hinge_node_j.tag]
        ops.element('zeroLengthSection', ele_i_tag, *ele_i_nodes, sec_tag,
                    '-orient', *orientation)
        ops.element('zeroLengthSection', ele_j_tag, *ele_j_nodes, sec_tag,
                    '-orient', *orientation)

    def to_py(self) -> List[str]:
        """Gets the Python commands to construct column components in OpenSees
        domain (i.e, plastic hinges, elastic column element and nodes).

        Returns
        -------
        List[str]
            List of Python commands for constructing the components of beam
            object in OpenSees.

        Notes
        -----
        Same hinge materials are used at both ends.
        """
        # Create column element nodes
        content = ['# Create elastic column element nodes']
        content.append(self.ele_node_i.to_py())
        content.append(self.ele_node_j.to_py())

        # Create elastic column element
        content.append('# Create elastic column element')
        ele_inputs = self._get_elastic_ele_inputs()
        ele_inputs = ', '.join([f"{item}" for item in ele_inputs])
        content.append(f"ops.element('elasticBeamColumn', {ele_inputs})")

        # Get inputs for materials describing plastic hinge behaviour
        my_hys_mat_inputs, vy_limit_curve_inputs, vy_limit_state_mat_inputs = \
            self._get_hinge_mat_inputs(axis='y')
        mz_hys_mat_inputs, vz_limit_curve_inputs, vz_limit_state_mat_inputs = \
            self._get_hinge_mat_inputs(axis='x')

        # Create materials describing flexural behaviour of plastic hinge
        content.append(
            '# Create materials describing flexural behaviour of plastic hinge'
            )
        my_tag = my_hys_mat_inputs[0]
        mz_tag = mz_hys_mat_inputs[0]
        my_hys_mat = ', '.join([f"{item}" for item in my_hys_mat_inputs])
        mz_hys_mat = ', '.join([f"{item}" for item in mz_hys_mat_inputs])
        content.append(f"ops.uniaxialMaterial('Hysteretic', {my_hys_mat})")
        content.append(f"ops.uniaxialMaterial('Hysteretic', {mz_hys_mat})")

        # Create or set materials describing shear behaviour of plastic hinge
        if self.capacity_design:  # Use rigid material for shear behaviour
            vy_tag = RIGID_MAT
            vz_tag = RIGID_MAT
            content.append(
                '# Use rigid material for shear behaviour of plastic hinge'
                )
        else:  # Create shear hinge materials
            content.append(
                '# Create new materials describing shear behaviour of plastic '
                'hinge'
                )
            vy_tag = vy_limit_state_mat_inputs[0]
            vz_tag = vz_limit_state_mat_inputs[0]
            vy_limit_curve = ', '.join(
                [f"{item}" for item in vy_limit_curve_inputs]
                )
            vy_limit_state_mat = ', '.join(
                [f"{item}" for item in vy_limit_state_mat_inputs]
                )
            vz_limit_curve = ', '.join(
                [f"{item}" for item in vz_limit_curve_inputs]
                )
            vz_limit_state_mat = ', '.join(
                [f"{item}" for item in vz_limit_state_mat_inputs]
                )
            content.append(f"ops.limitCurve('ThreePoint', {vy_limit_curve})")
            content.append(
                f"ops.uniaxialMaterial('LimitState', {vy_limit_state_mat})"
                )
            content.append(f"ops.limitCurve('ThreePoint', {vz_limit_curve})")
            content.append(
                f"ops.uniaxialMaterial('LimitState', {vz_limit_state_mat})"
                )

        # Create plastic hinge sections at both ends
        content.append('# Create plastic hinge sections at both ends')
        sec_tag = self.design.line.tag
        content.append(
            f"ops.section('Aggregator', {sec_tag}, "
            f"{RIGID_MAT}, 'P', {vy_tag}, 'Vy', {vz_tag}, 'Vz', "
            f"{my_tag}, 'My', {mz_tag}, 'Mz', {RIGID_MAT}, 'T')"
            )

        # Create plastic hinge elements at both ends
        content.append('# Create plastic hinge elements at both ends')
        orientation = "0, 0, 1, 0, 1, 0"
        ele_i_tag = self.ele_node_i.tag
        ele_i_nodes = f"{self.hinge_node_i.tag}, {self.ele_node_i.tag}"
        ele_j_tag = self.ele_node_j.tag
        ele_j_nodes = f"{self.ele_node_j.tag}, {self.hinge_node_j.tag}"
        content.append(
            f"ops.element('zeroLengthSection', {ele_i_tag}, {ele_i_nodes}, "
            f"{sec_tag}, '-orient', {orientation})"
            )
        content.append(
            f"ops.element('zeroLengthSection', {ele_j_tag}, {ele_j_nodes}, "
            f"{sec_tag}, '-orient', {orientation})"
            )

        return content

    def to_tcl(self) -> List[str]:
        """Gets the Tcl commands to construct column components in OpenSees
        domain (i.e, plastic hinges, elastic column element and nodes).

        Returns
        -------
        List[str]
            List of Tcl commands for constructing the components of beam
            object in OpenSees.

        Notes
        -----
        Same hinge materials are used at both ends.
        """
        # Create column element nodes
        content = ['# Create elastic column element nodes']
        content.append(self.ele_node_i.to_tcl())
        content.append(self.ele_node_j.to_tcl())

        # Create elastic column element
        content.append('# Create elastic column element')
        ele_inputs = self._get_elastic_ele_inputs()
        ele_inputs = ' '.join([f"{item}" for item in ele_inputs])
        content.append(f"element elasticBeamColumn {ele_inputs}")

        # Get inputs for materials describing plastic hinge behaviour
        my_hys_mat_inputs, vy_limit_curve_inputs, vy_limit_state_mat_inputs = \
            self._get_hinge_mat_inputs(axis='y')
        mz_hys_mat_inputs, vz_limit_curve_inputs, vz_limit_state_mat_inputs = \
            self._get_hinge_mat_inputs(axis='x')

        # Create materials describing flexural behaviour of plastic hinge
        content.append(
            '# Create materials describing flexural behaviour of plastic hinge'
            )
        my_tag = my_hys_mat_inputs[0]
        mz_tag = mz_hys_mat_inputs[0]
        my_hys_mat = ' '.join([f"{item}" for item in my_hys_mat_inputs])
        mz_hys_mat = ' '.join([f"{item}" for item in mz_hys_mat_inputs])
        content.append(f"uniaxialMaterial Hysteretic {my_hys_mat}")
        content.append(f"uniaxialMaterial Hysteretic {mz_hys_mat}")

        # Create or set materials describing shear behaviour of plastic hinge
        if self.capacity_design:  # Use rigid material for shear behaviour
            vy_tag = RIGID_MAT
            vz_tag = RIGID_MAT
            content.append(
                '# Use rigid material for shear behaviour of plastic hinge'
                )
        else:  # Create shear hinge materials
            content.append(
                '# Create new materials describing shear behaviour of plastic '
                'hinge'
                )
            vy_tag = vy_limit_state_mat_inputs[0]
            vz_tag = vz_limit_state_mat_inputs[0]
            vy_limit_curve = ' '.join(
                [f"{item}" for item in vy_limit_curve_inputs]
                )
            vy_limit_state_mat = ' '.join(
                [f"{item}" for item in vy_limit_state_mat_inputs]
                )
            vz_limit_curve = ' '.join(
                [f"{item}" for item in vz_limit_curve_inputs]
                )
            vz_limit_state_mat = ' '.join(
                [f"{item}" for item in vz_limit_state_mat_inputs]
                )
            content.append(f"limitCurve ThreePoint {vy_limit_curve}")
            content.append(f"uniaxialMaterial LimitState {vy_limit_state_mat}")
            content.append(f"limitCurve ThreePoint {vz_limit_curve}")
            content.append(f"uniaxialMaterial LimitState {vz_limit_state_mat}")

        # Create plastic hinge sections at both ends
        content.append('# Create plastic hinge sections at both ends')
        sec_tag = self.design.line.tag
        content.append(
            f"section Aggregator {sec_tag} "
            f"{RIGID_MAT} P {vy_tag} Vy {vz_tag} Vz "
            f"{my_tag} My {mz_tag} Mz {RIGID_MAT} T"
            )

        # Create plastic hinge elements at both ends
        content.append('# Create plastic hinge elements at both ends')
        orientation = "0 0 1 0 1 0"
        ele_i_tag = self.ele_node_i.tag
        ele_i_nodes = f"{self.hinge_node_i.tag} {self.ele_node_i.tag}"
        ele_j_tag = self.ele_node_j.tag
        ele_j_nodes = f"{self.ele_node_j.tag} {self.hinge_node_j.tag}"
        content.append(
            f"element zeroLengthSection {ele_i_tag} {ele_i_nodes} "
            f"{sec_tag} -orient {orientation}"
            )
        content.append(
            f"element zeroLengthSection {ele_j_tag} {ele_j_nodes} "
            f"{sec_tag} -orient {orientation}"
            )

        return content

    def add_grav_loads_to_ops(self) -> None:
        """Adds gravity load objects to the OpenSees domain
        (i.e, point loads at both ends).
        """
        point_load = round(self.ele_load * self.design.H / 2, PRECISION)
        load_values = [0.0, 0.0, -point_load, 0.0, 0.0, 0.0]
        ops.load(self.ele_node_i.tag, *load_values)
        ops.load(self.ele_node_j.tag, *load_values)

    def to_py_grav_loads(self) -> List[str]:
        """Gets the Python commands to construct column gravity load object in
        OpenSees domain (i.e, point loads at both ends).

        Returns
        -------
        List[str]
            List of Python commands for adding column gravity loads
            to OpenSees.
        """
        point_load = round(self.ele_load * self.design.H / 2, PRECISION)
        load_values = f"0.0, 0.0, {-point_load}, 0.0, 0.0, 0.0"
        return [
            f"ops.load({self.ele_node_i.tag}, {load_values})",
            f"ops.load({self.ele_node_j.tag}, {load_values})"
        ]

    def to_tcl_grav_loads(self) -> List[str]:
        """Gets the Tcl commands to construct column gravity load object in
        OpenSees domain (i.e, point loads at both ends).

        Returns
        -------
        List[str]
            List of Tcl commands for adding column gravity loads to OpenSees.
        """
        point_load = round(self.ele_load * self.design.H / 2, PRECISION)
        load_values = f"0.0 0.0 {-point_load} 0.0 0.0 0.0"
        return [
            f"load {self.ele_node_i.tag} {load_values}",
            f"load {self.ele_node_j.tag} {load_values}"
        ]

    def _get_elastic_ele_inputs(self) -> List[float]:
        """Retrieves elastic column element inputs.

        Returns
        -------
        List[float]
            List of elastic column element inputs.
        """
        # Elastic stiffness multiplier
        # Ibarra and Krawinkler (2005), Zareian and Medina (2010)
        stiffness_factor_1 = 10
        stiffness_factor_2 = (stiffness_factor_1 + 1) / stiffness_factor_1
        Iz_mod = self.design.Ix * stiffness_factor_2
        Iy_mod = self.design.Iy * stiffness_factor_2
        # EI_factor = 0.50

        # List of elasticBeamColumn element inputs
        ele_inputs = [
            self.design.line.tag, self.ele_node_i.tag, self.ele_node_j.tag,
            self.design.Ag, self.Ecm_q, self.Gcm_q,
            self.design.J, Iy_mod, Iz_mod, PDELTA_TRANSF_Z
            ]
        # Rounding
        ele_inputs = round_list(ele_inputs)

        return ele_inputs

    def _get_hinge_mat_inputs(self, axis=Literal['x', 'y']
                              ) -> Tuple[List[float]]:
        """Gets the plastic hinge material properties for given axis, i.e.,

        - Flexure material inputs (Hysteretic uniaxial material).
        - Shear limit curve inputs (ThreePoint LimitCurve).
        - Shear limit state material inputs (LimitState uniaxial material).

        Parameters
        ----------
        axis : Literal['x', 'y']
            The local axis considered for the calculations.

        Returns
        -------
        flex_hyst_mat : List[float]
            Hysteretic material model inputs for the plastic hinge describing
            behaviour in flexure around `axis`.
        shear_limit_curve_inputs : List[float]
            Inputs for limit curve used by the limit state material describing
            the shear behaviour in `axis`.
        shear_limit_state_mat : List[float]
            Inputs for the limit state material for describing the shear
            behaviour in `axis`.

        References
        ----------
        Haselton, C. B., Liel, A. B., Lange, S. T., & Deierlein, G. G. (2008).
        Beam-column element model calibrated for predicting flexural response
        leading to global collapse of RC frame buildings. Pacific Earthquake
        Engineering Research Center, University of California, Berkeley, CA.

        Haselton, C. B., Liel, A. B., Taylor-Lange, S. C., & Deierlein, G. G.
        (2016). Calibration of model to simulate response of reinforced
        concrete beam-columns to collapse. ACI Structural Journal, 113(6).

        Ibarra, L. F. and Krawinkler, H. (2005). Global collapse of frame
        structures under seismic excitations. Technical Report 152,
        Stanford University.

        Zareian, F. and Medina, R. A. (2010). A practical method for proper
        modeling of structural damping in inelastic plane structural systems,
        Computers & Structures, Vol. 88, 1-2, pp. 45-53.

        CEN (2005) Eurocode 8: Design of structures for earthquake resistance -
        Part 3: Assessment and retrofitting of existing buildings.
        Brussels, Belgium

        Panagiotakos, T. B., & Fardis, M. N. (2001).
        Deformations of reinforced concrete members at yielding and ultimate.
        Structural Journal, 98(2), 135-148.

        ASCE/SEI 41-17. (2017). Seismic rehabilitation of existing buildings.
        American Society of Civil Engineers.

        LeBorgne, M. R., & Ghannoum, W. M. (2014). Calibrated analytical
        element for lateral-strength degradation of reinforced concrete
        columns. Engineering Structures, 81, 35-48.

        Sezen, H. and Moehle, J.P. (2004). Shear Strength Model for Lightly
        Reinforced Concrete Columns. J Struct Eng 130:1692-1703.
        https://doi.org/10.1061/(asce)0733-9445(2004)130:11(1692)

        Elwood K. J., & Moehle J. P. (2003). Shake table tests and analytical
        studies on the gravity load collapse of reinforced concrete frames.
        PEER report 2003/01. Pacific Earthquake Engineering Research Center,
        College of Engineering,  University of California, Berkeley.
        """
        if axis == 'x':
            # Section height
            h = self.design.by  # along y
            # Section width
            b = self.design.bx  # along x
            # Number of internal web reinforcement (intermediate)
            nbl_v = self.design.nbly_int
            # Number of internal reinforcement (on a single side)
            nbl_int = self.design.nblx_int
            # Transverse reinforcement ratio
            rhoh = self.design.rhoh_y  # Stirrups are along -y axis
            # The integer tag for the material describing flexure behaviour
            # around local -x (corresponds to z in ops)
            flex_mat_tag = self.design.line.tag + 10000

        elif axis == 'y':
            # Section height
            h = self.design.bx  # along x
            # Section width
            b = self.design.by  # along y
            # Number of internal web reinforcement (intermediate)
            nbl_v = self.design.nblx_int
            # Number of internal reinforcement (on a single side)
            nbl_int = self.design.nbly_int
            # Transverse reinforcement ratio
            rhoh = self.design.rhoh_x  # Stirrups are along -x axis
            # The integer tag for the material describing flexure behaviour
            # around local -y axis (corresponds to y in ops)
            flex_mat_tag = self.design.line.tag + 20000

        # Number of corner reinforcement (on a single side)
        nbl_cor = 2
        # Diameter of corner reinforcement
        dbl_cor = self.design.dbl_cor
        # Diameter of internal reinforcement
        dbl_int = self.design.dbl_int
        # Concrete compressive strength in base units (quality adjusted)
        fc = self.design.fc_q
        # Longitudinal steel yield strength in base units (quality adjusted)
        fsyl = self.design.fsyl_q
        # Concrete cover
        cover = self.design.cover_q
        # Horizontal (stirrup) reinforcement diameter
        dbh = self.design.dbh
        # Concrete compressive strength in MPa (quality adjusted)
        fc_mpa = self.design.fc_q / MPa  # convert to MPa
        # Longitudinal steel yield strength in MPa (quality adjusted)
        fsyl_mpa = self.design.fsyl_q / MPa  # convert to MPa
        # Nominal length of column
        Ln = self.design.H
        # Stirrup spacing
        sbh = self.design.sbh_q
        # Longitudinal reinforcement ratio
        rhol = self.design.rhol
        # Concrete crushing strain used for computing section capacity
        eps_cu = 0.0035
        # Axial load
        Nu = max(-self.axial_force, 0)

        """PART 1: YIELD MOMENT AND CURVATURE CALCULATIONS
        MAIN REFERENCE: Panagiotakos and Fardis (2001)
        """
        # Stress-block coefficient used to compute section capacity
        # TODO: Reference
        if fc < 27.6 * MPa:
            betac = 0.85
        elif fc > 55.17 * MPa:
            betac = 0.65
        else:
            betac = 1.05 - 0.05 * fc_mpa / 6.9
        # Concrete modulus of elasticity
        Ec = self.Ecm_q
        # Steel modulus of elasticity
        Es = self.design.Es
        # Modular ratio
        nyoung = Es / Ec
        # Yield strain of steel bars
        esy = fsyl / Es
        # Distance from top fiber to bottom rebars
        dd = h - cover - dbh - 0.5 * dbl_cor
        # Distance from top fiber to top rebars
        dd_prime = h - dd
        # Balanced  value of c: distance to neutral axis from top fiber
        cb = (eps_cu * dd) / (eps_cu + esy)  # from compatibility
        # Tension and compression reinforcement
        As_tens = (nbl_cor * ((0.25 * np.pi) * dbl_cor**2) +
                   nbl_int * ((0.25 * np.pi) * dbl_int**2))
        rhol_tens = As_tens / (b * dd)
        As_comp = (nbl_cor * ((0.25 * np.pi) * dbl_cor**2) +
                   nbl_int * ((0.25 * np.pi) * dbl_int**2))
        rhol_comp = As_comp / (b * dd)
        # Web reinforcement (intermediate)
        As_int = 2 * nbl_v * (0.25*np.pi*dbl_int**2)
        rhol_int = As_int / (b * dd)
        # Compute distance to neutral axis with outer faces (simplification)
        c = (As_tens * fsyl - As_comp * fsyl + Nu) / (
            0.85 * fc * b * betac)
        # Decide whether yielding is controlled by tension or compression zone
        if c < cb:  # Yielding is controlled by the tension steel
            # Panagiotakos and Fardis 2001 - Equation 4
            A_to_use = (
                rhol_tens + rhol_comp + rhol_int + (Nu / (b*dd*fsyl))
                )
            B_to_use = (
                rhol_tens + rhol_comp*(dd_prime/dd) +
                0.5*rhol_int*(1 + (dd_prime/dd)) +
                (Nu / (b*dd*fsyl))
                )
            control = 1
        else:  # Yielding is controlled by the compression zone
            # Panagiotakos and Fardis 2001 - Equation 5
            A_to_use = (
                rhol_tens + rhol_comp + rhol_int - (Nu / (1.8*nyoung*b*dd*fc))
                )
            B_to_use = (
                rhol_tens + rhol_comp*(dd_prime/dd) +
                0.5*rhol_int*(1 + (dd_prime/dd))
                )
            control = 0
        # The compression zone depth: Panagiotakos and Fardis 2001 - Equation 3
        ky = (((nyoung**2) * (A_to_use**2) + (2*nyoung*B_to_use))**0.5
              - nyoung*A_to_use)
        # Yield curvature
        if control == 1:
            # Panagiotakos and Fardis 2001 - Equation 1
            fiy = fsyl / (Es * (1 - ky) * dd)
        else:
            # Panagiotakos and Fardis 2001 - Equation 2
            fiy = (1.8 * fc) / (Ec * ky * dd)
        # Yield Moment: Panagiotakos and Fardis 2001 - Equation 6
        term1 = (Ec * (ky**2)/2) * (
            0.5 * (1 + (dd_prime / dd)) - (ky / 3))
        term2 = (Es/2) * (
            (1 - ky) * rhol_tens +
            (ky - (dd_prime / dd)) * rhol_comp +
            (rhol_int / 6) * (1 - (dd_prime / dd))
            ) * (1 - (dd_prime / dd))
        My = (b * (dd**3)) * fiy * (term1 + term2)

        """PART 2: PLASTIC HINGE PROPERTY CALCULATIONS
        MAIN REFERENCE: Haselton et al. (2016)
        """
        # Shear span, assuming equal to 50% of the free length of the element
        Ls = Ln/2  # NOTE: Could be varied with intensity of loading, but ok.
        # Shear cracking is expected to precede flexural yield EC8-3 pp 41
        av = 1.0
        # Axial load ratio
        niu = Nu / (self.design.Ag * fc)
        # Unit conversion coefficient 1.0 for MPa, 6.9 for ksi (Haselton 2016)
        c_u = 1.0
        # Reinforcing bar buckling coefficient, by Dhakal and Maekawa 2002
        sn = (sbh / dbl_cor) * (fsyl_mpa / 100)**0.5
        # Effective depth: dist. between outer comp. fiber and tens. steel
        d = 0.9*h
        # Level arm: dist. between comp. and tens. forces
        z = 0.9*d

        # Post-yield hardening stiffness - Haselton et al. 2008 - Equation 3.17
        Mc_My = 1.25 * (0.89**niu) * (0.91**(0.01*fc_mpa))
        #  Residual strength to capping strength ratio - assumed
        Mr_Mc = 0.1  # 10%
        # Maximum moment capacity
        Mc = Mc_My * My
        # Residual moment capacity
        Mr = Mr_Mc * Mc

        # Plastic Rotation capacity by Haselton et al. 2016 - Equation 5
        # TODO: check if notation is consistent with directions
        theta_cap_pl = 0.12 * (1 + 0.55 * self.bondslip_factor) \
            * (0.16**niu) \
            * ((0.02 + 40*rhoh)**0.43) * (0.54**(0.01*c_u*fc_mpa)) \
            * (0.66**(0.1*sn)) * (2.27**(10.0*rhol))
        # Post-capping rotation capacity by Haselton et al. 2016 - Equation 8
        theta_pc = min(0.10,
                       0.76 * (0.031**niu) * ((0.02 + 40*rhoh)**1.02))

        # Yield rotation capacity - EN 1998-3:2004 - Equation A.10b
        theta_y1 = fiy * ((Ls + (av*z))/3)
        theta_y2 = 0.0014 * (1 + 1.5*h/Ls)
        theta_y3 = 0.125*fiy*dbl_cor * (fsyl_mpa / (fc_mpa**0.50))
        theta_y = theta_y1 + theta_y2 + (self.bondslip_factor * theta_y3)

        # Elastic stiffness multiplier
        # Ibarra and Krawinkler (2005), Zareian and Medina (2010)
        n_factor = 10
        # # Modified moment of inertia
        # EIfact = max(min(1.33 * (0.10+niu)**0.80, 0.80), 0.35)
        # Ig_mod = EIfact * Ig * (n_factor + 1.0) / n_factor
        # k0 = (n_factor + 1) * 3.0 * EIfact * E_mod * Ig_mod / Ln
        # k0 = My / theta_y
        # # strain hardening ratio of spring
        # a_mem = (n_factor + 1.0) * (My * (Mc_My - 1)) / (k0 * theta_cap_pl)
        # # modified strain hardening ratio of spring
        # # (Ibarra & Krawinkler 2005, note: Eqn B.5 is incorrect)
        # a_s = (a_mem) / (1.0 + n_factor*(1.0 - a_mem))

        # Rotation values for monotonic loading
        theta_1 = theta_y / n_factor
        theta_2 = (theta_y / n_factor) + theta_cap_pl
        theta_3 = (theta_y / n_factor) + theta_cap_pl + theta_pc
        # NOTE: rotation values needs to be adjusted for cyclic loading
        # theta_cap_pl needs to be factored by 0.7
        # theta_pc needs to be factored by 0.5

        # Pinching factor for strain (or deformation) during reloading
        pinchx = 1.0  # TODO: Reference
        # Pinching factor for stress (or force) during reloading
        pinchy = 1.0  # TODO: Reference
        # Damage due to ductility: D1(mu-1)
        damage1 = 0.0  # TODO: Reference
        # Damage due to energy: D2(Eii/Eult)
        damage2 = 0.0  # TODO: Reference
        # Power used to determine the degraded unloading stiffness based on
        # ductility, mu-beta (optional, default=0.0)
        beta = 0.0  # TODO: Reference
        # Material inputs other than tag and type
        flex_hyst_mat = [
            flex_mat_tag,
            My, theta_1, Mc, theta_2, Mr, theta_3,
            -My, -theta_1, -Mc, -theta_2, -Mr, -theta_3,
            pinchx, pinchy, damage1, damage2, beta
        ]

        """
        PART 3: SHEAR MATERIALS
        """
        if axis == 'x':
            # Number of horizontal bars (stirrup legs)
            nbh = self.design.nbh_x
            # # Gross moment of intertia
            # Ig = self.design.Ix
            # The integer tag for the Limit Curve defining the limit surface
            limit_curve_tag = self.design.line.tag + 10000
            # The integer tag for the material describing shear behaviour in
            # local -x (corresponds to z in ops)
            shear_mat_tag = self.design.line.tag + 30000

        elif axis == 'y':
            # Number of horizontal bars (stirrup legs)
            nbh = self.design.nbh_y
            # # Gross moment of intertia
            # Ig = self.design.Iy
            # The integer tag for the Limit Curve defining the limit surface
            limit_curve_tag = self.design.line.tag + 20000
            # The integer tag for the material describing shear behaviour in
            # local -y (corresponds to z in ops)
            shear_mat_tag = self.design.line.tag + 40000

        # Transverse reinforcement yield strength (quality adjusted)
        fsyh_mpa = self.design.fsyh_q / MPa  # in MPa
        fsyh = self.design.fsyh_q  # in base units
        # Gross corss-section area
        Ag = self.design.Ag
        # Axial load in Mega Newton (mN) - Positive in compression
        Nu_MN = max((-self.axial_force) / MN, 0)  # convert to mN
        # Transverse reinforcement area
        Av = nbh * np.pi * (dbh**2) / 4
        # Initial shear strength, see ASCE/SEI 41-17 - Equation 10-3si
        k = 1.0  # Degradation factor (1.0 for initial strength)
        lambda_ = 1.0  # Assuming normal weight concrete aggregate
        d = 0.8 * h  # Effective depth, permitted to assume by ASCE
        alpha = np.interp(sbh / d, [0.75, 1.0], [1.0, 0.0])
        M_V_rat = Ls  # Largest ratio of moment to shear, assumed
        M_Vd_rat = min(max(M_V_rat/d, 2), 4)  # Should satify: 2 <= M/Vd <= 4
        Vn = k * (alpha * (Av * fsyh_mpa * d / sbh) + lambda_ * (
            (fc_mpa**0.5) / (2 * M_Vd_rat)
            * (1 + (2 * Nu_MN) / ((fc_mpa**0.5) * Ag)) ** 0.5
        ) * (0.8 * Ag))
        # Convert from MPa units to based units
        Vn *= MN
        # Shear-spring elastic slope - LeBorgne and Ghannoum (2014) - Eqn. 1
        k_el = (5/6) * (self.Gcm_q * Ag / Ln)
        # Degrading slope of the shear-drift spring backbone
        # Shoraka and Elwood (2013) - Eqn. 20
        k_deg = (
            4.5 * Nu * (((Av * fsyh * 0.9 * h) / (Nu * sbh)) * 4.6 + 1) ** 2
        ) / Ln

        # # Commented for now, because these are not being used
        # # Maximum shear value (upon plastic hinge formation)
        # Vp = Mc / Ls
        # # Ratio of max. shear to nominal shear strength
        # V_ratio = Vp / Vn
        # # Elastic displacement, at nominal shear strength
        # delta_Vn = Vn / k_el
        # # TODO: Reference
        # delta_Vu = (4 - 12*Vn / (b*0.9*h*fc)) * delta_Vn
        # # TODO: Reference
        # delta_Au = max(
        #     0.04
        #     + (5.5989 / (2.1445 +
        #                  Nu_MN * sbh / (Av * fsyh_mpa * 0.90 * h * 2.1445))),
        #     delta_Vu + 0.001,
        # )
        # # Inputs for Hysteretic material model
        # # TODO: reference?
        # # Stress and strain (or force & deformation) at the three points of
        # # the envelope in the positive direction
        # s1p, e1p = 0.80*Vn, 0.80*Vn/k_el  # 1st
        # s2p, e2p = 1.0*Vn, Vn/k_el  # 2nd
        # s3p, e3p = 0.20*Vn, 0.80*Vn/k_deg  # 3rd (Optional)
        # # Stress and strain (or force & deformation) at the three points the
        # # envelope in the negative direction (all are negative values)
        # s1n, e1n = -0.80*Vn, -0.80*Vn/k_el  # 1st
        # s2n, e2n = -1.0*Vn, -Vn/k_el  # 2nd
        # s3n, e3n = -0.20*Vn, -0.80*Vn/k_deg  # 3rd (Optional)
        # # Pinching factor for strain (or deformation) during reloading
        # pinchX = 0.4
        # # Pinching factor for stress (or force) during reloading
        # pinchY = 0.3
        # # Damage due to ductility: D1(m-1)
        # damage1 = 0.0
        # # Damage due to energy: D2(Ei/Eult)
        # damage2 = 0.0
        # # Power used to determine the degraded unloading stiffness based on
        # # ductility, mu-beta (optional, default=0.0)
        # beta = 0.0
        # # Shear material inputs for hysteretic material model
        # shear_hyst_mat = [
        #     shear_mat_tag,
        #     s1p, e1p,
        #     s2p, e2p,
        #     s3p, e3p,
        #     s1n, e1n,
        #     s2n, e2n,
        #     s3n, e3n,
        #     pinchX, pinchY, damage1, damage2, beta
        # ]

        # Inputs for Three-Point Limit Curve - Elwood and Moehle 2003
        # integer element tag for the associated beam-column element
        eleTag = self.design.line.tag
        # Three-Point strength degradation model by Sezen and Moehle 2004
        k0, k1, k2 = 1.0, 1.0, 0.7  # Strength degradation factors
        mu_y0, mu_y1, mu_y2 = 0.0, 2.0, 6.0  # Displacement ductilities
        # The coordinates of points on the limit curve
        # x1, y1 = -10, Vn  # the first point
        x1, y1 = mu_y0*theta_y, k0*Vn  # the first point TODO: verify
        # x2, y2 = 0, Vn  # the second point
        x2, y2 = mu_y1*theta_y, k1*Vn  # the second point TODO: verify
        # x3, y3 = 10, Vn  # the third point
        x3, y3 = mu_y2*theta_y, k2*Vn  # the third point TODO: verify
        # Floating point value for the slope of the third branch in the
        # post-failure backbone, assumed to be negative
        Kdeg = -k_deg
        # Floating point value for the residual force capacity of the
        # post-failure backbone
        Fres = 0.05  # should be a small value - shear failure
        # Integer flag for type of deformation defining the abscissa
        # of the limit curve:
        # 1 = maximum beam-column chord rotations
        # 2 = drift based on displacement of nodes ndI and ndJ
        defType = 2
        # Integer flag for type of force defining the ordinate of the
        # limit curve:
        # 0 = force in associated limit state material
        # 1 = shear in beam-column element
        # 2 = axial load in beam-column element
        # Option 1 assumes no member loads
        forType = 0
        # Integer node tag for the first associated node
        # (normally node I of $eleTag beam-column element)
        ndl = self.hinge_node_i.tag
        # Integer node tag for the second associated node
        # (normally node J of $eleTag beam-column element)
        ndJ = self.hinge_node_j.tag
        # Nodal degree of freedom to monitor for drift
        if axis == 'x':
            dof = 1
        elif axis == 'y':
            dof = 2
        # Perpendicular global direction from which length is
        # determined to compute drift: 1 = X, 2 = Y, 3 = Z
        perpDirn = 3
        # Variable containing limit curve inputs
        shear_limit_curve_inputs = [
            limit_curve_tag, eleTag,
            x1, y1, x2, y2, x3, y3, Kdeg, Fres,
            defType, forType, ndl, ndJ, dof, perpDirn
            ]
        # Inputs for LimitState material model - Elwood and Moehle 2003
        # Stress and strain (or force & deformation) at the three points of
        # the envelope in the positive direction
        s1p, e1p = 0.25*Vn, 0.25*Vn/k_el  # 1st
        s2p, e2p = 0.75*Vn, 0.75*Vn/k_el  # 2nd
        s3p, e3p = 2.5*Vn, 2.5*Vn/k_el  # 3rd
        # Stress and strain (or force & deformation) at the three points the
        # envelope in the negative direction (all are negative values)
        s1n, e1n = -0.25*Vn, -0.25*Vn/k_el  # 1st
        s2n, e2n = -0.75*Vn, -0.75*Vn/k_el  # 2nd
        s3n, e3n = -2.5*Vn, -2.5*Vn/k_el  # 3rd
        # Pinching factor for strain (or deformation) during reloading
        pinchX = 0.4  # TODO: Reference
        # Pinching factor for stress (or force) during reloading
        pinchY = 0.3  # TODO: Reference
        # Damage due to ductility: D1(m-1)
        damage1 = 0.003  # TODO: Reference
        # Damage due to energy: D2(Ei/Eult)
        damage2 = 0.0  # TODO: Reference
        # Power used to determine the degraded unloading stiffness based on
        # ductility, mu-beta (optional, default=0.0)
        beta = 0.0  # TODO: Reference
        # The integer defining the type of LimitCurve (0 = no curve,
        # 1 = axial curve, all other curves can be any other integer)
        curveType = 2
        # Variable containing limit state material inputs
        shear_limit_state_mat = [
            shear_mat_tag,
            s1p, e1p,
            s2p, e2p,
            s3p, e3p,
            s1n, e1n,
            s2n, e2n,
            s3n, e3n,
            pinchX, pinchY, damage1, damage2, beta,
            limit_curve_tag, curveType
            ]

        # Rounding to precision
        flex_hyst_mat = round_list(flex_hyst_mat)
        shear_limit_curve_inputs = round_list(shear_limit_curve_inputs)
        shear_limit_state_mat = round_list(shear_limit_state_mat)

        return flex_hyst_mat, shear_limit_curve_inputs, shear_limit_state_mat
