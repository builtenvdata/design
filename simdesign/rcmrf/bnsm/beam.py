# Imports from installed packages
import numpy as np
import openseespy.opensees as ops
from typing import Tuple, List, Literal, Dict

# Imports from bnsm library
from .node import Node
from .constants import RIGID_MAT, LINEAR_TRANSF_X, LINEAR_TRANSF_Y

# Imports from bdim base library
from ..bdim.baselib.beam import BeamBase, Array3

# Imports from utils library
from ...utils.units import MPa
from ...utils.misc import PRECISION, round_list


class Beam:
    """Beam class which can be used to define beam elements
    in OpenSees.

    Attributes
    ----------
    design : BeamBase
        Instance of beam design information model.
    bondslip_factor : float
        Bondslip factor considered while defining plastic hinges.
    ele_node_i : Node
        Element node at the start of beam.
    ele_node_j : Node
        Element node at the end of beam.
    ele_load : float
        Uniformly distributed gravity load along the beam.
    hinge_node_i : Node
        Extra node considered for hinge definition at the start of beam.
    hinge_node_j : Node
        Extra node considered for hinge definition at the end of beam.
    """

    design: BeamBase
    """Instance of beam design information model."""
    bondslip_factor: float
    """Bondslip factor considered while defining plastic hinges."""
    ele_node_i: Node
    """Element node at the start of beam."""
    ele_node_j: Node
    """Element node at the end end of beam."""
    ele_load: float
    """Uniformly distributed gravity load along the beam."""
    hinge_node_i: Node
    """Extra node considered for hinge definition at the start of beam."""
    hinge_node_j: Node
    """Extra node considered for hinge definition at the start of end."""

    @property
    def ele_tag(self) -> int:
        """
        Returns
        -------
        int
            Tag of beam-column element representing elastic part of the beam.
        """
        return self.design.line.tag

    @property
    def hinge_i_tag(self) -> int:
        """
        Returns
        -------
        int
            Tag of hinge element at the start of the beam.
        """
        return self.ele_node_i.tag

    @property
    def hinge_j_tag(self) -> int:
        """
        Returns
        -------
        int
            Tag of hinge element at the end of the beam.
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

    def __init__(self, design: BeamBase, bondslip_factor: float,
                 load_factors: Dict[Literal['G', 'Q'], float]) -> None:
        """Initialize the Beam object.

        Parameters
        ----------
        design : BeamBase
            Instance of beam design information model.
        bondslip_factor : float
            Bondslip factor considered while defining plastic hinges.
        load_factors : Dict[Literal['G', 'Q'], float]
            Load factors used to compute uniformly distributed gravity load on
            the beam.
        """
        self.design = design
        self.bondslip_factor = bondslip_factor
        self.ele_load = round(
            float(design.wg_total * load_factors['G'] +
                  design.wq_total * load_factors['Q']),
            PRECISION)

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
        """Adds beam objects to the OpenSees domain
        (i.e, plastic hinges, elastic beam element and nodes).
        """
        # Create beam element nodes
        self.ele_node_i.add_to_ops()
        self.ele_node_j.add_to_ops()

        # Create elastic beam element
        ele_inputs = self._get_elastic_ele_inputs()
        ops.element('elasticBeamColumn', *ele_inputs)

        # Create hysteretic materials for plastic hinges at both ends
        hinge_i_mat_inputs, hinge_j_mat_inputs = self._get_hinge_mat_inputs()
        ops.uniaxialMaterial('Hysteretic', *hinge_i_mat_inputs)
        ops.uniaxialMaterial('Hysteretic', *hinge_j_mat_inputs)

        # Create plastic hinge elements at both ends
        (hinge_i_tag, hinge_i_nodes, hinge_i_mats,
         hinge_j_tag, hinge_j_nodes, hinge_j_mats,
         orientation, mat_dirs) = self._get_hinge_ele_inputs()
        ops.element('zeroLength', hinge_i_tag, *hinge_i_nodes,
                    '-mat', *hinge_i_mats, '-dir', *mat_dirs,
                    '-orient', *orientation)
        ops.element('zeroLength', hinge_j_tag, *hinge_j_nodes,
                    '-mat', *hinge_j_mats, '-dir', *mat_dirs,
                    '-orient', *orientation)

    def to_py(self) -> List[str]:
        """Gets the Python commands to construct beam components in OpenSees
        domain (i.e, plastic hinges, elastic beam element and nodes).

        Returns
        -------
        List[str]
            List of Python commands for constructing the components of beam
            object in OpenSees.
        """
        # Create beam element nodes
        content = ['# Create elastic beam element nodes']
        content.append(self.ele_node_i.to_py())
        content.append(self.ele_node_j.to_py())

        # Create elastic beam element
        content.append('# Create elastic beam element')
        ele_inputs = self._get_elastic_ele_inputs()
        ele_inputs = ', '.join([f"{item}" for item in ele_inputs])
        content.append(f"ops.element('elasticBeamColumn', {ele_inputs})")

        # Create hysteretic materials for plastic hinges at both ends
        content.append(
            '# Create hysteretic materials for plastic hinges at both ends')
        hinge_i_mat_inputs, hinge_j_mat_inputs = self._get_hinge_mat_inputs()
        hinge_i_mat_inputs = ', '.join(
            [f"{item}" for item in hinge_i_mat_inputs])
        hinge_j_mat_inputs = ', '.join(
            [f"{item}" for item in hinge_j_mat_inputs])
        content.append(
            f"ops.uniaxialMaterial('Hysteretic', {hinge_i_mat_inputs})")
        content.append(
            f"ops.uniaxialMaterial('Hysteretic', {hinge_j_mat_inputs})")

        # Create plastic hinge elements at both ends
        content.append('# Create plastic hinge elements at both ends')
        (hinge_i_tag, hinge_i_nodes, hinge_i_mats,
         hinge_j_tag, hinge_j_nodes, hinge_j_mats,
         orientation, mat_dirs) = self._get_hinge_ele_inputs()
        hinge_i_nodes = ', '.join([f"{item}" for item in hinge_i_nodes])
        hinge_i_mats = ', '.join([f"{item}" for item in hinge_i_mats])
        hinge_j_nodes = ', '.join([f"{item}" for item in hinge_j_nodes])
        hinge_j_mats = ', '.join([f"{item}" for item in hinge_j_mats])
        orientation = ', '.join([f"{item}" for item in orientation])
        mat_dirs = ', '.join([f"{item}" for item in mat_dirs])
        content.append(
            f"ops.element('zeroLength', {hinge_i_tag}, {hinge_i_nodes}, "
            f"'-mat', {hinge_i_mats}, '-dir', {mat_dirs}, "
            f"'-orient', {orientation})"
            )
        content.append(
            f"ops.element('zeroLength', {hinge_j_tag}, {hinge_j_nodes}, "
            f"'-mat', {hinge_j_mats}, '-dir', {mat_dirs}, "
            f"'-orient', {orientation})"
            )

        return content

    def to_tcl(self) -> List[str]:
        """Gets the Tcl commands to construct beam components in OpenSees
        domain (i.e, plastic hinges, elastic beam element and nodes).

        Returns
        -------
        List[str]
            List of Tcl commands for constructing the components of beam
            object in OpenSees.
        """
        # Create beam element nodes
        content = ['# Create elastic beam element nodes']
        content.append(self.ele_node_i.to_tcl())
        content.append(self.ele_node_j.to_tcl())

        # Create elastic beam element
        content.append('# Create elastic beam element')
        ele_inputs = self._get_elastic_ele_inputs()
        ele_inputs = ' '.join([f"{item}" for item in ele_inputs])
        content.append(f"element elasticBeamColumn {ele_inputs}")

        # Create hysteretic materials for plastic hinges at both ends
        content.append(
            '# Create hysteretic materials for plastic hinges at both ends')
        hinge_i_mat_inputs, hinge_j_mat_inputs = self._get_hinge_mat_inputs()
        hinge_i_mat_inputs = ' '.join(
            [f"{item}" for item in hinge_i_mat_inputs])
        hinge_j_mat_inputs = ' '.join(
            [f"{item}" for item in hinge_j_mat_inputs])
        content.append(
            f"uniaxialMaterial Hysteretic {hinge_i_mat_inputs}")
        content.append(
            f"uniaxialMaterial Hysteretic {hinge_j_mat_inputs}")

        # Create plastic hinge elements at both ends
        content.append('# Create plastic hinge elements at both ends')
        (hinge_i_tag, hinge_i_nodes, hinge_i_mats,
         hinge_j_tag, hinge_j_nodes, hinge_j_mats,
         orientation, mat_dirs) = self._get_hinge_ele_inputs()
        hinge_i_nodes = ' '.join([f"{item}" for item in hinge_i_nodes])
        hinge_i_mats = ' '.join([f"{item}" for item in hinge_i_mats])
        hinge_j_nodes = ' '.join([f"{item}" for item in hinge_j_nodes])
        hinge_j_mats = ' '.join([f"{item}" for item in hinge_j_mats])
        orientation = ' '.join([f"{item}" for item in orientation])
        mat_dirs = ' '.join([f"{item}" for item in mat_dirs])
        content.append(
            f"element zeroLength {hinge_i_tag} {hinge_i_nodes} "
            f"-mat {hinge_i_mats} -dir {mat_dirs} -orient {orientation}"
            )
        content.append(
            f"element zeroLength {hinge_j_tag} {hinge_j_nodes} "
            f"-mat {hinge_j_mats} -dir {mat_dirs} -orient {orientation}"
            )

        return content

    def add_grav_loads_to_ops(self) -> None:
        """Adds gravity load objects to the OpenSees domain
        (i.e, uniformly distrubted loads).
        """
        ops.eleLoad('-ele', self.ele_tag, '-type', '-beamUniform',
                    -self.ele_load, 0.0)

    def to_py_grav_loads(self) -> str:
        """Gets the Python commands to construct beam gravity load object in
        OpenSees domain (i.e, uniformly distrubted loads).

        Returns
        -------
        str
            Python command for constructing beam gravity load object
            in OpenSees.
        """
        return (
                f"ops.eleLoad('-ele', {self.ele_tag}, '-type', "
                f"'-beamUniform', {-self.ele_load}, 0.0)"
            )

    def to_tcl_grav_loads(self) -> str:
        """Gets the Tcl commands to construct beam gravity load object in
        OpenSees domain (i.e, uniformly distrubted loads).

        Returns
        -------
        str
            Tcl command for constructing beam gravity load object
            in OpenSees.
        """
        return (
                f"eleLoad -ele {self.ele_tag} -type "
                f"-beamUniform {-self.ele_load} 0.0"
            )

    def _get_hinge_ele_inputs(self) -> Tuple[int, List[int], List[int],
                                             int, List[int], List[int],
                                             List[float], List[int]]:
        """Retrieves plastic hinge element inputs.

        Returns
        -------
        hinge_i_tag : int
            Tag of hinge element at the start section.
        hinge_i_nodes : List[int]
            Nodes of hinge element at the start section.
        hinge_i_mats : List[int]
            Material tags associated with hinge element at the start section.
        hinge_j_tag : int
            Tag of hinge element at the end section.
        hinge_j_nodes : List[int]
            Nodes of hinge element at the end section.
        hinge_j_mats : List[int]
            Material tags associated with hinge element at the end section.
        orientation : List[float]
            Orientation of hinge element (ZeroLength element).
        mat_dirs : List[int]
            Directions of each hinge material.
        """
        hinge_i_mat = self.ele_node_i.tag
        hinge_i_nodes = [self.hinge_node_i.tag, self.ele_node_i.tag]
        hinge_j_mat = self.ele_node_j.tag
        hinge_j_nodes = [self.ele_node_j.tag, self.hinge_node_j.tag]

        if self.design.direction == 'x':
            vecx = [1.0, 0.0, 0.0]
            vecyp = [0.0, 1.0, 0.0]
            # cross product is vecz = [0, 0, 1]
        elif self.design.direction == 'y':
            vecx = [0.0, 1.0, 0.0]
            vecyp = [-1.0, 0.0, 0.0]
            # cross product is vecz = [0, 0, 1]

        orientation = vecx + vecyp
        hinge_i_mats = [RIGID_MAT, RIGID_MAT, RIGID_MAT,
                        RIGID_MAT, hinge_i_mat, RIGID_MAT]
        hinge_j_mats = [RIGID_MAT, RIGID_MAT, RIGID_MAT,
                        RIGID_MAT, hinge_j_mat, RIGID_MAT]
        mat_dirs = [1, 2, 3, 4, 5, 6]

        return (self.hinge_i_tag, hinge_i_nodes, hinge_i_mats,
                self.hinge_j_tag, hinge_j_nodes, hinge_j_mats,
                orientation, mat_dirs)

    def _get_hinge_mat_inputs(self) -> Tuple[List[float],
                                             List[float]]:
        """Gets the plastic hinge material properties, i.e.,
        Hysteresis material model inputs.

        Returns
        -------
        mat_inputs_i : List[float]
            Hysteretic material model inputs for hinge at the start section.
        mat_inputs_j : List[float]
            Hysteretic material model inputs for hinge at the end section.

        References
        ---------
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

        Dolšek, M. and Fajfar, P. (2005). Post-test analyses of the SPEAR test
        building. University of Ljubljana.
        """
        h = self.design.h
        ln = self.design.L
        fc_mpa = self.design.fc_q / MPa
        fsyl_mpa = self.design.fsyl_q / MPa
        dbl_t1 = self.design.dbl_t1
        sbh = self.design.sbh_q
        rhol = self.design.rhol
        rhoh = self.design.rhoh_y

        # Shear span, assuming equal to 50% of the free length of the element
        ls = ln/2  # NOTE: Could be varied with intensity of loading, but ok.
        niu = 0.0  # Axial load ratio, assuming beams do not have any
        # Post-yield hardening stiffness - Haselton et al. 2008 - Equation 3.17
        Mc_My = 1.25 * (0.89**niu) * (0.91**(0.01*fc_mpa))
        #  Residual strength to capping strength ratio - assumed
        Mr_Mc = 0.1  # 10%
        # Reinforcing bar buckling coefficient, by Dhakal and Maekawa 2002
        sn = (sbh[0] / dbl_t1) * (fsyl_mpa / 100)**0.5
        # Shear cracking is expected to precede flexural yield EC8-3 pp 41
        av = 1.0
        z = 0.9 * (0.9*h)  # lever arm
        # NOTE: av.z is the tension shift of the bending diagram see:
        # EN 1992-1-1: 2004, 9.2.1.3(2)

        # Compute yield moments in positive and negative directions at both
        # end sections of the beam (i and j) - Panagiotakos and Fardis (2001)
        My_neg, fiy_neg = self._get_my('negative')
        My_pos, fiy_pos = self._get_my('positive')
        # Maximum moment capacity
        Mc_neg = Mc_My * My_neg
        Mc_pos = Mc_My * My_pos
        # Residual moment capacity
        Mr_neg = Mr_Mc*Mc_neg
        Mr_pos = Mr_Mc*Mc_pos

        # Plastic Rotation capacity by Haselton et al. 2016 - Equation 5
        c_u = 1.0  # Unit conversion coefficient 1.0 for MPa, 6.9 for ksi
        theta_cap_pl_pos = 0.12 * (1 + 0.55 * self.bondslip_factor) * \
            (0.16**niu) * ((0.02 + 40*rhoh)**0.43) * \
            (0.54**(0.01*c_u*fc_mpa)) * (0.66**(0.1*sn)) * (2.27**(10.0*rhol))
        # Non-symmetric beam section - Equation 7
        # NOTE: This is different than MATLAB implementation
        ratio_pos_neg = np.maximum(
            0.01, self.design.rhol_top / self.design.rhol_bot) ** 0.225
        theta_cap_pl_neg = ratio_pos_neg * theta_cap_pl_pos
        # Post-capping rotation capacity by Haselton et al. 2016 - Equation 8
        theta_pc_neg = 0.76 * (0.031**niu) * ((0.02 + 40*rhoh)**1.02)
        theta_pc_neg[theta_pc_neg >= 0.10] = 0.10
        theta_pc_pos = 0.76 * (0.031**niu) * ((0.02 + 40*rhoh)**1.02)
        theta_pc_pos[theta_pc_pos >= 0.10] = 0.10

        # Yield rotation capacity - EN 1998-3:2004 - Equation A.10b
        theta_y1_neg = fiy_neg * ((ls + (av*z))/3)
        theta_y1_pos = fiy_pos * ((ls + (av*z))/3)
        theta_y2 = 0.0014 * (1 + 1.5*h/ls)
        theta_y3_neg = 0.125*fiy_neg*dbl_t1 * (fsyl_mpa / (fc_mpa**0.50))
        theta_y3_bot = 0.125*fiy_pos*dbl_t1 * (fsyl_mpa / (fc_mpa**0.50))
        theta_y_pos = (
            theta_y1_neg + theta_y2 + self.bondslip_factor * theta_y3_neg)
        theta_y_bot = (
            theta_y1_pos + theta_y2 + self.bondslip_factor * theta_y3_bot)

        # Elastic stiffness multiplier
        # Ibarra and Krawinkler (2005), Zareian and Medina (2010)
        n_factor = 10

        # Strain values e1p, e2p, e3p, e1n, e2n, e3n  (hysteretic material)
        # Rotation values for monotonic loading
        theta_1_neg = theta_y_pos / n_factor
        theta_2_neg = (theta_y_pos / n_factor) + theta_cap_pl_neg
        theta_3_neg = (theta_y_pos / n_factor) + theta_cap_pl_neg + \
            theta_pc_neg
        theta_1_pos = theta_y_bot / n_factor
        theta_2_pos = (theta_y_bot / n_factor) + theta_cap_pl_pos
        theta_3_pos = (theta_y_bot / n_factor) + theta_cap_pl_pos + \
            theta_pc_pos
        # NOTE: rotation values needs to be adjusted for cyclic loading
        # theta_cap_pl needs to be factored by 0.7
        # theta_pc needs to be factored by 0.5

        # Pinching factor for strain (or deformation) during reloading
        pinchx = 0.8  # TODO: Reference
        # Pinching factor for stress (or force) during reloading
        pinchy = 0.2  # TODO: Reference
        # Damage due to ductility: D1(mu-1)
        damage1 = 0.0  # TODO: Reference
        # Damage due to energy: D2(Eii/Eult)
        damage2 = 0.0  # TODO: Reference
        # Power used to determine the degraded unloading stiffness based on
        # ductility, mu-beta (optional, default=0.0)
        beta = 0.85  # Reference: Dolšek and Fajfar 2005

        # NOTE: This part is different than original implementation
        # The negative ones are based on top (compression) reinforcement
        # The positive ones are based on bottom (tension) renforcement
        mat_tag_i = self.ele_node_i.tag
        mat_inputs_i = [
            mat_tag_i,
            My_pos[0], theta_1_pos[0],
            Mc_pos[0], theta_2_pos[0],
            Mr_pos[0], theta_3_pos[0],
            -My_neg[0], -theta_1_neg[0],
            -Mc_neg[0], -theta_2_neg[0],
            -Mr_neg[0], -theta_3_neg[0],
            pinchx, pinchy, damage1, damage2, beta
                 ]
        mat_tag_j = self.ele_node_j.tag
        mat_inputs_j = [
            mat_tag_j,
            My_pos[-1], theta_1_pos[-1],
            Mc_pos[-1], theta_2_pos[-1],
            Mr_pos[-1], theta_3_pos[-1],
            -My_neg[-1], -theta_1_neg[-1],
            -Mc_neg[-1], -theta_2_neg[-1],
            -Mr_neg[-1], -theta_3_neg[-1],
            pinchx, pinchy, damage1, damage2, beta
                 ]

        # Rounding to precision
        mat_inputs_i = round_list(mat_inputs_i)
        mat_inputs_j = round_list(mat_inputs_j)

        return mat_inputs_i, mat_inputs_j

    def _get_elastic_ele_inputs(self) -> List[float]:
        """Retrieves elastic beam element inputs.

        Returns
        -------
        List[float]
            List of elastic beam element inputs.
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
            self.ele_tag, self.ele_node_i.tag, self.ele_node_j.tag,
            self.design.Ag, self.Ecm_q, self.Gcm_q,
            self.design.J, Iy_mod, Iz_mod
            ]
        # Append geometric transformation
        if self.design.direction == 'x':
            ele_inputs.append(LINEAR_TRANSF_X)
        elif self.design.direction == 'y':
            ele_inputs.append(LINEAR_TRANSF_Y)

        # Rounding to precision
        ele_inputs = round_list(ele_inputs)

        return ele_inputs

    def _get_my(self, direction: Literal['negative', 'positive']
                ) -> Tuple[Array3[np.float64], Array3[np.float64]]:
        """
        Computes yield moment of the section in the given direction.

        Parameters
        ----------
        direction : Literal['negative', 'positive']
            Moment capacity direction.

        Returns
        -------
        My : np.ndarray
            Yield moment of beam in the specified `direction`.
            Computed for start, mid, end beam sections.
        fiy : np.ndarray
            Yield curvature of beam in the specified `direction`.
            Computed for start, mid, end beam sections.

        References
        ----------
        Panagiotakos, T. B., & Fardis, M. N. (2001).
        Deformations of reinforced concrete members at yielding and ultimate.
        Structural Journal, 98(2), 135-148.
        """
        h = self.design.h
        b = self.design.b
        fc = self.design.fc_q
        fsyl = self.design.fsyl_q
        cover = self.design.cover_q
        nbl_b1 = self.design.nbl_b1
        nbl_b2 = self.design.nbl_b2
        dbl_b1 = self.design.dbl_b1
        dbl_b2 = self.design.dbl_b2
        nbl_t1 = self.design.nbl_t1
        nbl_t2 = self.design.nbl_t2
        dbl_t1 = self.design.dbl_t1
        dbl_t2 = self.design.dbl_t2
        dbh = self.design.dbh

        # Set direction dependent parameters
        if direction == 'positive':  # positive direction case
            # Longitudinal reinforcement area under tension
            As_tens = (nbl_b1 * ((0.25 * np.pi) * dbl_b1**2) +
                       nbl_b2 * ((0.25 * np.pi) * dbl_b2**2))
            # Longitudinal reinforcement area under compression
            As_comp = (nbl_t1 * ((0.25 * np.pi) * dbl_t1**2) +
                       nbl_t2 * ((0.25 * np.pi) * dbl_t2**2))
        elif direction == 'negative':  # negative direction case
            # Longitudinal reinforcement area under tension
            As_tens = (nbl_t1 * ((0.25 * np.pi) * dbl_t1**2) +
                       nbl_t2 * ((0.25 * np.pi) * dbl_t2**2))
            # Longitudinal reinforcement area under compression
            As_comp = (nbl_b1 * ((0.25 * np.pi) * dbl_b1**2) +
                       nbl_b2 * ((0.25 * np.pi) * dbl_b2**2))

        # Concrete crushing strain used for computing section capacity
        EPS_CU = 0.0035
        # Stress-block coefficient used to compute section capacity
        # TODO: Reference
        if fc < 27.6 * MPa:
            betac = 0.85
        elif fc > 55.17 * MPa:
            betac = 0.65
        else:
            betac = 1.05 - 0.05 * fc / (6.9 * MPa)
        # Concrete modulus of elasticity
        Ec = self.Ecm_q
        # Steel modulus of elasticity
        Es = self.design.Es
        nyoung = Es / Ec
        # Yield strain of steel bars
        esy = fsyl / Es
        # Dist. from concrete fiber in compression to the rebars in tension
        dd = h - cover - dbh - 0.5 * dbl_b1
        # Distance from ext. concrete fiber (comp.) to the rebars (comp.)
        dd_prime = h - dd
        # Balanced c value: dist. to neutral axis from ext. conc. fiber (comp.)
        cb = (EPS_CU * dd) / (EPS_CU + esy)
        # Tension and compression longitudinal reinforcement ratio values
        rhol_tens = As_tens / (b * dd)
        rhol_comp = As_comp / (b * dd)
        # Compute distance to neutral axis with outer faces (simplification)
        c = (As_tens * fsyl - As_comp * fsyl) / (0.85 * fc * b * betac)
        # Decide whether yielding is controlled by tension or compression zone
        # Panagiotakos and Fardis 2001 - Equation 4 & 5
        Acomp_cntrl = rhol_tens + rhol_comp
        Atens_cntrl = rhol_tens + rhol_comp
        Bcomp_cntrl = rhol_tens + rhol_comp*(dd_prime/dd)
        Btens_cntrl = rhol_tens + rhol_comp*(dd_prime/dd)
        # Yielding is controlled by the tension steel
        control = np.ones_like(dd)
        A_to_use = Atens_cntrl
        B_to_use = Btens_cntrl
        # Yielding is controlled by the compression zone
        control[c >= cb] = 0
        A_to_use[c >= cb] = Acomp_cntrl[c >= cb]
        B_to_use[c >= cb] = Bcomp_cntrl[c >= cb]
        # The compression zone depth: Panagiotakos and Fardis 2001 - Equation 3
        ky = (((nyoung**2) * (A_to_use**2) + (2*nyoung*B_to_use))**0.5
              - nyoung*A_to_use)
        # Panagiotakos and Fardis 2001 - Equation 1
        fiy1 = fsyl / (Es * (1 - ky) * dd)
        # Panagiotakos and Fardis 2001 - Equation 2
        fiy2 = (1.8 * (fc) / (Ec * ky * dd))
        # Yield curvature
        fiy = fiy1
        fiy[control == 0] = fiy2[control == 0]
        # Yield Moment: Panagiotakos and Fardis 2001 - Equation 6
        rhol_int = 0.0  # Beams do not have web-reinforcement
        term1 = (Ec * (ky**2)/2) * (
            0.5 * (1 + (dd_prime / dd)) - (ky / 3))
        term2 = (Es/2) * (
                (1 - ky) * rhol_tens +
                (ky - (dd_prime / dd)) * rhol_comp +
                (rhol_int / 6) * (1 - (dd_prime / dd))
                ) * (1 - (dd_prime / dd))
        My = (b * (dd**3)) * fiy * (term1 + term2)

        return My, fiy
