# Imports from installed packages
import numpy as np
from typing import Optional, List, Dict, Literal, Tuple
import openseespy.opensees as ops
from pathlib import Path

# Imports from bnsm library
from .constants import (
    RIGID_SEC, RIGID_MAT, BIG_VALUE,
    LINEAR_TRANSF_X, LINEAR_TRANSF_Y, LINEAR_TRANSF_Z,
    PDELTA_TRANSF_Z, VECXZ_X, VECXZ_Y, VECXZ_Z,
    GRAV_TS_TAG, GRAV_P_TAG, NSPA_TS_TAG, NSPA_P_TAG)
from .foundation import Foundation
from .joint import StairsJoint, FloorJoint
from .floor import FloorDiaphragm
from .beam import Beam, BeamBase
from .column import Column, ColumnBase

# Imports from bdim base library
from ..bdim.baselib.building import BuildingBase

# Imports from utils library
from ...utils.misc import make_dir
from ...utils import plotter as pl


class BNSM:
    """Building Nonlinear Structural Model (BNSM) class which can be used to
    define and run numerical models in OpenSees.

    Attributes
    ----------
    design : BuildingBase
        Instance of building design information model.
    foundations : List[Foundation]
        List of foundation instances.
    floors : List[FloorDiaphragm]
        List of floor instances.
    floor_joints : List[OpsFloorJoint]
        List of floor joints instances.
    stairs_joints : List[OpsStairsJoint]
        List of stairs joints instances.
    beams : List[Beam]
        List of beam instances.
    columns : List[Column]
        List of column instances.
    load_factors : Dict[Literal['G', 'Q'], float]
        Load factors used to compute gravity loads.
        'G': Permanent load factor
        'Q': Variable load factor
    mass_sources : Dict[Literal['G', 'Q'], float]
        Mass sources used to compute seismic masses.
        'G': Permanent mass factor
        'Q': Variable mass factor
    basic_masses : np.ndarray
        Point masses for the basic building geometry.
    scheme : Literal['FMP', 'EQL', 'MPP', 'TRI', 'UNI']
        The loading scheme considered for retriving pushover loads.
        'FMP': Fundamental-mode proportional loading.
        'EQL': Equivalent lateral loading.
        'MPP': Mass proportional loading.
        'TRI': Triangular or height propotional loading.
        'UNI': Uniform loading.
    max_drift : float
        The drift value used to calculate maximum disp. of control node.
    dincr: float
        First displacement increment considered during nspa.
    """

    design: BuildingBase
    """Instance of building design information model."""
    foundations: List[Foundation]
    """List of foundation (support) instances."""
    floors: List[FloorDiaphragm]
    """List of floor diaphragm instances."""
    floor_joints: List[FloorJoint]
    """List of floor joints instances."""
    stairs_joints: List[StairsJoint]
    """List of stairs joints instances."""
    beams: List[Beam]
    """List of beam instances."""
    columns: List[Column]
    """List of column instances."""
    load_factors: Dict[Literal['G', 'Q'], float]
    """Load factors used to compute gravity loads.
    'G': Permanent load factor.
    'Q': Variable load factor."""
    mass_sources: Dict[Literal['G', 'Q'], float]
    """Mass sources used to compute seismic masses.
    'G': Permanent mass factor.
    'Q': Variable mass factor."""
    basic_masses: np.ndarray
    """Point masses for the basic building geometry."""
    scheme: Literal['FMP', 'EQL', 'MPP', 'TRI', 'UNI']
    """The loading scheme considered for retriving pushover loads.
    - 'FMP': Fundamental-mode proportional loading.
    - 'EQL': Equivalent lateral loading.
    - 'MPP': Mass proportional loading.
    - 'TRI': Triangular or height propotional loading.
    - 'UNI': Uniform loading.
    """
    max_drift: float
    """The drift value used to calculate maximum disp. of control node."""
    dincr: float
    """First displacement increment considered during nspa."""

    def __init__(
        self, design: BuildingBase,
        load_factors: Dict[Literal['G', 'Q'], float] = {'G': 1.0, 'Q': 0.3},
        mass_factors: Dict[Literal['G', 'Q'], float] = {'G': 1.0, 'Q': 0.3},
        scheme: Literal['FMP', 'EQL', 'MPP', 'TRI', 'UNI'] = 'EQL',
        max_drift: float = 0.05, dincr: float = 0.001
    ) -> None:
        """Initialize BNSM object.

        Parameters
        ----------
        design : BuildingBase
            Instance of building design information model (BDIM)
        load_factors : Dict[Literal['G', 'Q'], float], optional
            Load factors used to compute gravity loads & seismic masses
            'G': Permanent load factor
            'Q': Variable load factor
            By default {'G': 1.0, 'Q': 0.3}.
        mass_sources : Dict[Literal['G', 'Q'], float]
            Mass sources used to compute seismic masses.
            'G': Permanent mass factor
            'Q': Variable mass factor
        scheme : Literal['FMP', 'EQL', 'MPP', 'TRI', 'UNI'], optional
            The loading scheme considered for retriving pushover loads.
            'FMP': Fundamental-mode proportional loading.
            'EQL': Equivalent lateral loading.
            'MPP': Mass proportional loading.
            'TRI': Triangular or height propotional loading.
            'UNI': Uniform loading.
            By default 'EQL'.
        max_drift : float, optional
            The drift value used to calculate maximum disp. of control node.
            By default 0.05.
        dincr: float
            First displacement increment considered during nspa.
            By default 0.001.
        """
        self.design = design
        self.load_factors = load_factors
        self.mass_sources = mass_factors
        self.scheme = scheme
        self.max_drift = max_drift
        self.dincr = dincr
        self.foundations = []
        self.floors = []
        self.floor_joints = []
        self.stairs_joints = []
        self.beams = []
        self.columns = []
        self.__set_basic_masses()
        self.__initialize_floor_joints()
        self.__initialize_stairs_joints()
        self.__initialize_foundations()
        self.__initialize_beams()
        self.__initialize_columns()

    def __initialize_beams(self) -> None:
        """Initialize beam models.
        """
        # Initialize the beam models
        bondslip_fact = self.design.quality.model.bondslip_factor
        self.beams = [Beam(beam, bondslip_fact, self.load_factors)
                      for beam in self.design.beams]
        # Initialize beam nodes at floor levels
        for joint in self.floor_joints:
            if joint.design.left_beam:
                design = joint.design.left_beam
                node_j = joint.left_node
                beam = self.__find_beam_by_design(design)
                if beam and node_j:
                    beam.hinge_node_j = node_j
                    beam.set_ele_node_j()
            if joint.design.right_beam:
                design = joint.design.right_beam
                node_i = joint.right_node
                beam = self.__find_beam_by_design(design)
                if beam and node_i:
                    beam.hinge_node_i = node_i
                    beam.set_ele_node_i()
            if joint.design.rear_beam:
                design = joint.design.rear_beam
                node_j = joint.rear_node
                beam = self.__find_beam_by_design(design)
                if beam and node_j:
                    beam.hinge_node_j = node_j
                    beam.set_ele_node_j()
            if joint.design.front_beam:
                design = joint.design.front_beam
                node_i = joint.front_node
                beam = self.__find_beam_by_design(design)
                if beam and node_i:
                    beam.hinge_node_i = node_i
                    beam.set_ele_node_i()
        # Initialize beam nodes at mid-storeys (stairs beams)
        for joint in self.stairs_joints:
            if joint.design.left_beam:
                design = joint.design.left_beam
                node_j = joint.left_node
                beam = self.__find_beam_by_design(design)
                if beam and node_j:
                    beam.hinge_node_j = node_j
                    beam.set_ele_node_j()
            if joint.design.right_beam:
                design = joint.design.right_beam
                node_i = joint.right_node
                beam = self.__find_beam_by_design(design)
                if beam and node_i:
                    beam.hinge_node_i = node_i
                    beam.set_ele_node_i()

    def __initialize_columns(self) -> None:
        """Initialize column models.
        """
        # Set bondslip factor
        bondslip_fact = self.design.quality.model.bondslip_factor
        # Check if capacity design is followed for shear
        if self.design.OVERSTRENGTH_FACTOR_COLUMN_SHEAR:
            capacity_des = True
        else:
            capacity_des = False

        # Initialize columns
        self.columns = [Column(column, bondslip_fact,
                               capacity_des, self.load_factors)
                        for column in self.design.columns]
        # Initialize column nodes at stairs and floor joints
        for joint in self.floor_joints + self.stairs_joints:
            if joint.design.bottom_column:
                design = joint.design.bottom_column
                node_j = joint.bottom_node
                column = self.__find_column_by_design(design)
                if column and node_j:
                    column.hinge_node_j = node_j
                    column.set_ele_node_j()
            if joint.design.top_column:
                design = joint.design.top_column
                node_i = joint.top_node
                column = self.__find_column_by_design(design)
                if column and node_i:
                    column.hinge_node_i = node_i
                    column.set_ele_node_i()

        # Initialize column nodes at foundations
        for foundation in self.foundations:
            if foundation.design.top_column:
                design = foundation.design.top_column
                node_i = foundation.foundation_node
                column = self.__find_column_by_design(design)
                if column and node_i:
                    column.hinge_node_i = node_i
                    column.set_ele_node_i()

    def __initialize_floor_joints(self) -> None:
        """initialize joint models at floor levels.
        """
        # Joint flexibility model
        if self.design.beam_type == 1:  # Wide beams are used.
            # Rigid joints are imposed in the case of wide beams to
            # force damage localization.
            """TODO: I am not sure if this should be done here.
            Exterior beams are always emergent in fact. We may still see
            joint damage. In the future, we may do this check inside, and
            determine the modelling option for each joint separately.
            Note that the modelling optional is then direction dependent."""
            flex_model = 'rigid'
        else:  # Based on quality and design class for emergent beam cases.
            flex_model = self.design.quality.model.joint
        floor_i = 0
        for points in self.design.geometry.floor_level_points:
            floor_i += 1
            cnodes = []
            joint_masses = []
            for point in points:
                point_i = self.design.geometry.points.index(point)
                mass = self.basic_masses[point_i]
                design = self.design._find_joint_by_point(point)
                joint = FloorJoint(design, mass, flex_model, self.load_factors)
                cnodes.append(joint.floor_node)
                joint_masses.append(mass)
                self.floor_joints.append(joint)
            # Initiate floor class and append to floors list
            self.floors.append(FloorDiaphragm(cnodes, floor_i, joint_masses))

    def __initialize_stairs_joints(self) -> None:
        """Initialize joint models of stairs (mid-storey level joints).
        """
        for point in self.design.geometry.points_at_mid_floor_levels:
            point_i = self.design.geometry.points.index(point)
            mass = self.basic_masses[point_i]
            design = self.design._find_joint_by_point(point)
            joint = StairsJoint(design, mass)
            self.stairs_joints.append(joint)

    def __initialize_foundations(self) -> None:
        """Initialize foundation models.
        """
        for point in self.design.geometry.ground_level_points:
            point_i = self.design.geometry.points.index(point)
            mass = self.basic_masses[point_i]
            design = self.design._find_joint_by_point(point)
            foundation = Foundation(design, mass)
            self.foundations.append(foundation)

    def __set_basic_masses(self) -> None:
        """Sets nodal masses of basic geometry based on mass factors.
        """
        elastic_model = self.design.ElasticModelClass(
            self.design.beams, self.design.columns, self.design.loads,
            self.design.geometry, self.design.beta)
        masses_g, masses_q = elastic_model._get_nodal_masses()
        self.basic_masses = np.array(masses_g) * self.mass_sources['G'] + \
            np.array(masses_q) * self.mass_sources['Q']

    def __find_beam_by_design(self, design: BeamBase) -> Optional[Beam]:
        """Finds the beam model by the given design.

        Parameters
        ----------
        design : BeamBase
            Beam design instance used for search.

        Returns
        -------
        BeamModel | None
            Returns BeamModel object if design attribute matches with
            given design, otherwise, returns None.
        """
        filtered_beams = filter(
            lambda beam: beam.design == design, self.beams)
        # Retrieve the first joint matching the condition
        matching_beam = next(filtered_beams, None)
        return matching_beam

    def __find_column_by_design(self, design: ColumnBase) -> Optional[Column]:
        """Finds the column model by the given design.

        Parameters
        ----------
        design : ColumnBase
            Column design instance used for search.

        Returns
        -------
        ColumnModel | None
            Returns ColumnModel object if design attribute matches with
            given design, otherwise, returns None.
        """
        filtered_columns = filter(
            lambda column: column.design == design, self.columns)
        # Retrieve the first joint matching the condition
        matching_column = next(filtered_columns, None)
        return matching_column

    def build(self) -> None:
        """Adds the numerical model to the OpenSees domain.
        """
        # Destroy any constructed OpenSees object
        ops.wipe()
        # Create ModelBuilder (with three-dimensions and 6 DOF/node)
        ops.model('basic', '-ndm', 3, '-ndf', 6)
        # Geometric transformations
        ops.geomTransf('Linear', LINEAR_TRANSF_X, *VECXZ_X)
        ops.geomTransf('Linear', LINEAR_TRANSF_Y, *VECXZ_Y)
        ops.geomTransf('Linear', LINEAR_TRANSF_Z, *VECXZ_Z)
        ops.geomTransf('PDelta', PDELTA_TRANSF_Z, *VECXZ_Z)
        # Rigid-like material and section
        ops.uniaxialMaterial('Elastic', RIGID_MAT, BIG_VALUE)
        ops.section(
            'Aggregator', RIGID_SEC,
            RIGID_MAT, 'P', RIGID_MAT, 'Vy',  RIGID_MAT, 'Vz',
            RIGID_MAT, 'My', RIGID_MAT, 'Mz', RIGID_MAT, 'T'
        )
        # Add foundations to ops domain (nodes and constraints)
        for foundation in self.foundations:
            foundation.add_to_ops()
        # Add floors to ops domain (nodes & diaphrams)
        for floor in self.floors:
            floor.add_to_ops()
        # Add stairs joints to ops domain (nodes and rigid offsets)
        for joint in self.stairs_joints:
            joint.add_to_ops()
        # Add floor joints to ops domain (nodes, joint offsets and flexibility)
        for joint in self.floor_joints:
            joint.add_to_ops()
        # Add beams to ops domain (plastic hinges, beam elements and nodes)
        for beam in self.beams:
            beam.add_to_ops()
        # Add columns to ops domain (plastic hinges, column elements and nodes)
        for column in self.columns:
            column.add_to_ops()

        # Add gravity time-series and load pattern to ops domain
        ops.timeSeries('Constant', GRAV_TS_TAG)
        ops.pattern('Plain', GRAV_P_TAG, GRAV_TS_TAG)
        # Add beam gravity loads to ops domain
        for beam in self.beams:
            beam.add_grav_loads_to_ops()
        # Add column gravity loads to ops domain
        for column in self.columns:
            column.add_grav_loads_to_ops()

        # Perform gravity analysis and save the model state
        ops.system('UmfPack')
        ops.numberer('RCM')
        ops.constraints('Transformation')
        ops.test('NormDispIncr', 1e-08, 1)
        ops.integrator('LoadControl', 1)
        ops.algorithm('Linear')
        ops.analysis('Static')
        ops.analyze(1)
        ops.loadConst('-time', 0.0)
        ops.wipeAnalysis()

    def do_modal(
        self, num_modes: int = 3, out_dir: Optional[str | Path] = None,
        print_screen: bool = False, normalisation: bool = True
    ) -> Dict[str, List[float]]:
        """Performs modal analysis.

        Parameters
        ----------
        num_modes : int, optional
            Number of modes for whose properties are calculated. By default 3.
        out_dir : bool, optional
            Output directory to save the modal properties and eigen vectors
            for the floor retained nodes. If None, these are not saved.
            By default None.
        print_screen : bool, optional
            Flag to print modal properties on the screen. By default False.
        normalisation : bool, optional
            Flag to compute the modal properties by using a
            displacement-normalized version of the eigenvectors.
            By default True.

        Returns
        -------
        Dict[str, List[float]]
            Dictionary containing modal properties.

        TODO
        ----
        For now print screen does not work.
        """
        # Build the model
        self.build()

        # Perform eigen value analysis
        list_solvers = ['-genBandArpack', '-fullGenLapack', '-symmBandLapack']
        ok = False
        for s in list_solvers:
            try:
                eigen_values = ops.eigen(s, num_modes)
                for i in range(num_modes):
                    if eigen_values[i] < 0 or eigen_values[i] > 1e+300:
                        ok = False
                    else:
                        ok = True
                if ok:
                    break
            except BaseException as e:
                print(f"Using {s[1:]} as solver... received an error: {e}")
        if not ok:
            raise UserWarning("Could not complete the eigenvalue analysis, " +
                              "something is wrong...\n" +
                              "Try to reduce number of modes to determine...")

        # Save eigen vectors for retained floor nodes
        if out_dir:
            # Create the output directory
            out_dir = Path(out_dir)
            make_dir(out_dir)
            # Modal properties directory
            modal_path = (out_dir / 'ModalProperties.txt').as_posix()
            # Save eigen vectors for retained floor nodes
            nodes = [floor.rnode.tag for floor in self.floors]
            for i in range(1, num_modes+1):
                modal_disps = []
                for node in nodes:
                    disps = ', '.join([
                        f'{disp}' for disp in ops.nodeEigenvector(node, i)
                        ])
                    modal_disps.append(f'{node}, {disps}')
                modal_disps = '\n'.join(modal_disps)
                eigen_path = (out_dir / f'EigenVectors_Mode{i}.txt').as_posix()
                with open(eigen_path, 'w') as file:
                    file.write(modal_disps)

        # Set modal analysis arguments
        args = []
        if print_screen:
            args.append('-print')
        if out_dir:
            args.extend(['-file', modal_path])
        if normalisation:
            args.append('-unorm')
        args.append('-return')

        # Perform modal analysis
        modal_properties = ops.modalProperties(*args)

        return modal_properties

    def do_nspa(
        self, ctrl_dof: Literal[1, 2],
        out_dir: Optional[str | Path] = None,
    ) -> Tuple[List[float], List[float]]:
        """Performs nonlinear static pushover analysis (NSPA).

        Parameters
        ----------
        ctrl_dof : Literal[1, 2]
            Control degrees of freedom for loading.
            1: X-direction.
            2: Y-direction.
        out_dir : bool, optional
            Output directory to save the modal properties and eigen vectors
            for the floor retained nodes. If None, these are not saved.
            By default None.

        Return
        ------
        ctrl_disp : List[float]
            Displacement values of control node.
        base_shear : List[float]
            Base shear value obtained as sum of the reaction forces.
        """

        # Get NSPA loading parameters
        nodes, loads, ctrl_node = \
            self.__get_nspa_loading_parameters(ctrl_dof)

        # Add NSPA time-series and load pattern to ops domain
        ops.timeSeries('Linear', NSPA_TS_TAG)
        ops.pattern('Plain', NSPA_P_TAG, NSPA_TS_TAG)
        # Add lateral nspa loads to ops domain
        for node, load_values in zip(nodes, loads):
            ops.load(node, *load_values)

        # Set foundation nodes
        supports = [
            found.foundation_node.tag for found in self.foundations
            ]
        # Set floor nodes
        floors = [floor.rnode.tag for floor in self.floors]
        # Base level coordinate
        base_level = min([ops.nodeCoord(node, 3) for node in supports])

        # Set the recorders
        if out_dir:
            # Create the output directory
            out_dir = Path(out_dir)
            make_dir(out_dir)
            # Directions per dof
            if ctrl_dof == 1:
                direction = 'x'
            elif ctrl_dof == 2:
                direction = 'y'
            if not Path.exists(out_dir):
                Path.mkdir(out_dir)
            reaction_file_path = (
                out_dir / f'support_reactions_{direction}.out'
                ).as_posix()
            disp_file_path = (
                out_dir / f'storey_displacements_{direction}.out'
                ).as_posix()
            storey_heights_file_path = (
                out_dir / f'storey_heights_{direction}.out'
                ).as_posix()
            ops.recorder('Node', '-file', disp_file_path, '-node', *floors,
                         '-dof', ctrl_dof, 'disp')
            ops.recorder('Node', '-file', reaction_file_path, '-node',
                         *supports, '-dof', ctrl_dof, 'reaction')
            # Save storey heights
            with open(storey_heights_file_path, 'w') as file:
                for node in floors:
                    file.write(f'{ops.nodeCoord(node, 3) - base_level}\n')

        # Set some analysis parameters
        max_disp = self.max_drift * (ops.nodeCoord(ctrl_node, 3) - base_level)
        dincr = self.dincr
        tol_init = 1.0e-6
        iter_init = 20
        ops.wipeAnalysis()
        ops.system('UmfPack')
        ops.numberer('RCM')
        ops.constraints('Penalty', 1e12, 1e12)
        ops.test('NormDispIncr', tol_init, iter_init)
        ops.integrator('DisplacementControl', ctrl_node, ctrl_dof, dincr)
        ops.algorithm('Newton', '-initialThenCurrent')
        ops.analysis('Static')

        # Start performing the analysis
        ctrl_disp = [0]
        base_shear = [0]
        ok = 0
        cont = True
        while ok == 0 and cont:
            # Perform the analysis for a single step with initial settings
            ops.test('NormDispIncr', tol_init, iter_init)
            ops.integrator('DisplacementControl', ctrl_node, ctrl_dof, dincr)
            ok = ops.algorithm('Newton', '-initialThenCurrent')
            # Try other algorithms with more iterations
            if ok != 0:
                ok = self.__set_nspa_algorithm(ok, tol_init)
            # Reduce dincr to an half
            if ok != 0:
                ops.integrator(
                    'DisplacementControl', ctrl_node, ctrl_dof, 0.5*dincr
                    )
                ok = self.__set_nspa_algorithm(ok, tol_init)
            # Reduce dincr to a quarter
            if ok != 0:
                ops.integrator(
                    'DisplacementControl', ctrl_node, ctrl_dof, 0.25*dincr
                    )
                ok = self.__set_nspa_algorithm(ok, tol_init)
            # Increase tolerance by factor of 10
            if ok != 0:
                ok = self.__set_nspa_algorithm(ok, 10*tol_init)
            # increase tolerance by factor of 100
            if ok != 0:
                ok = self.__set_nspa_algorithm(ok, 100*tol_init)

            # Get the base shear force
            ops.reactions()
            current_disp = ops.nodeDisp(ctrl_node, ctrl_dof)
            current_shear = abs(sum(
                [ops.nodeReaction(found.foundation_node.tag, ctrl_dof)
                    for found in self.foundations]))
            # current_shear = ops.getTime()
            # Set continue flag
            cont = (current_disp < max_disp and
                    current_shear < 50000 and
                    current_shear >= 0.2*max(base_shear))
            # Append base shear and control node displacement
            if ok == 0 and cont:
                base_shear.append(current_shear)
                ctrl_disp.append(current_disp)
            elif (
                max(base_shear) == 0.0 or  # Analysis did not even start
                base_shear[-1] / max(base_shear) > 0.8  # Not good enough
            ):
                ok = -1

        # Wipe the numerical model
        ops.wipe()
        # Return base shear and control node displacement history
        return ctrl_disp, base_shear, ok

    def __set_nspa_algorithm(self, ok: int, tol: float,
                             iter: int = 100) -> None:
        """Sets the solution algorithm for NSPA in ops domain.

        Parameters
        ----------
        ok : int
            Result of the last analysis step in OpenSees.
        tol : float
            The tolerance criteria used to check for convergence.
        iter : int, optional
            The max number of iterations to check before returning failure.
            By default 100.

        Return
        ------
        int
            Result of the new analysis step in OpenSees.
        """
        # Try KrylovNewton
        if ok != 0:
            ops.test('NormDispIncr', tol, iter)
            ops.algorithm('KrylovNewton')
            ok = ops.analyze(1)
        # Try NewtonLineSearch algorithm
        if ok != 0:
            ops.test('NormDispIncr', tol, iter)
            ops.algorithm('NewtonLineSearch', '-InitialInterpolated', 0.8)
            ok = ops.analyze(1)
        # Try Broyden algorithm
        if ok != 0:
            ops.test('NormDispIncr', tol, iter)
            ops.algorithm('Broyden')
            ok = ops.analyze(1)
        # Try Broyden–Fletcher–Goldfarb–Shanno (BFGS) algorithm
        if ok != 0:
            ops.test('NormDispIncr', tol, iter)
            ops.algorithm('BFGS')
            ok = ops.analyze(1)
        # Return the analysis result
        return ok

    def __get_nspa_loading_parameters(
        self, ctrl_dof: Literal[1, 2]
    ) -> Tuple[List[int], List[float], int]:
        """Gets the parameters required for nspa loading.

        Parameters
        ----------
        ctrl_dof : Literal[1, 2]
            Control degrees of freedom for loading.
            1: X-direction.
            2: Y-direction.

        Returns
        -------
        nodes : List[int]
            List containing tags of nodes which will be pushed.
        loads : List[float]
            List of loads which corresponds to each node deemed to be pushed.
        ctrl_node : int
            Tag of control node (determined based on max height).
        """
        # Find all required metrics for load computations.
        nodes = []
        masses = []
        heights = []
        modal_disps = []
        if self.scheme == 'FMP':  # Do Modal Analysis
            num_modes = round(len(self.basic_masses) / 2)
            modal_properties = self.do_modal(num_modes)
            if ctrl_dof == 1:
                mass_part_rat = np.array(modal_properties['partiMassRatiosMX'])
            elif ctrl_dof == 2:
                mass_part_rat = np.array(modal_properties['partiMassRatiosMY'])
            inds = mass_part_rat.argsort()[::-1]
            mode1 = int(inds[0] + 1)
        else:  # Just build the model
            self.build()
        for floor in self.floors:
            node = floor.rnode.tag
            nodes.append(node)
            masses.append(sum(floor.masses))
            heights.append(ops.nodeCoord(node, 3))
            if self.scheme == 'FMP':
                modal_disps.append(ops.nodeEigenvector(node, mode1, ctrl_dof))
        # Convert these lists to arrays for performing array operations
        masses = np.array(masses)
        heights = np.array(heights)
        modal_disps = np.array(modal_disps)
        # Loads for fundamental-mode proportional loading scheme
        if self.scheme == 'FMP':
            loads = (masses * modal_disps) / np.sum(masses * modal_disps)
        # Loads for equivalent lateral loading scheme
        elif self.scheme == 'EQL':
            loads = (masses * heights) / np.sum(masses * heights)
        # Loads for mass proportional loading scheme
        elif self.scheme == 'MPP':
            loads = masses / np.sum(masses)
        # Loads for triangular or height propotional loading scheme
        elif self.scheme == 'TRI':
            loads = heights / np.sum(heights)
        # Loads for uniform loading scheme
        elif self.scheme == 'UNI':
            loads = np.ones(len(nodes)) / len(nodes)
        # Make loading positive
        if np.sum(loads) < 0:
            loads = -1.0 * loads
        # Get control node
        inds = heights.argsort()[::-1]
        ctrl_node = nodes[inds[0]]
        loads = loads.tolist()
        if ctrl_dof == 1:
            loads = [[load, 0, 0, 0, 0, 0] for load in loads]
        elif ctrl_dof == 2:
            loads = [[0, load, 0, 0, 0, 0] for load in loads]

        return nodes, loads, ctrl_node

    def to_py(self, directory: Path | str) -> None:
        """Exports the numerical model files in Python format.

        Parameters
        ----------
        directory : Path | str
            Directory in which the files will be written.
        """
        # Create output directory
        directory = Path(directory)
        make_dir(directory)
        # Get each function as list of strings
        build_list = self.__get_build_py()
        foundations_list = self.__get_foundations_py()
        floors_list = self.__get_floors_py()
        joints_list = self.__get_joints_py()
        beams_list = self.__get_beams_py()
        columns_list = self.__get_columns_py()
        gravity_list = self.__get_gravity_py()
        modal_list = self.__get_modal_py()
        nspa_list = self.__get_nspa_py()
        run_list = self.__get_run_py()
        # Write __init__ file
        with open(directory / '__init__.py', 'w') as file:
            file.write('\n')
        # Write model source file
        with open(directory / 'model.py', 'w') as file:
            file.write('\n'.join(build_list))
        # Write foundations source file
        with open(directory / 'foundations.py', 'w') as file:
            file.write('\n'.join(foundations_list))
        # Write floors source file
        with open(directory / 'floors.py', 'w') as file:
            file.write('\n'.join(floors_list))
        # Write joints source file
        with open(directory / 'joints.py', 'w') as file:
            file.write('\n'.join(joints_list))
        # Write beams source file
        with open(directory / 'beams.py', 'w') as file:
            file.write('\n'.join(beams_list))
        # Write columns source file
        with open(directory / 'columns.py', 'w') as file:
            file.write('\n'.join(columns_list))
        # Write gravity analysis source file
        with open(directory / 'gravity.py', 'w') as file:
            file.write('\n'.join(gravity_list))
        # Write modal analysis source file
        with open(directory / 'modal.py', 'w') as file:
            file.write('\n'.join(modal_list))
        # Write nspa source file
        with open(directory / 'nspa.py', 'w') as file:
            file.write('\n'.join(nspa_list))
        # Write example run file
        with open(directory / 'run.py', 'w') as file:
            file.write('\n'.join(run_list))

    def to_tcl(self, directory: Path | str) -> None:
        """Exports the numerical model files in Tcl format.

        Parameters
        ----------
        directory : Path | str
            Directory in which the files will be written.
        """
        # Create output directory
        directory = Path(directory)
        make_dir(directory)
        # Get each function as list of strings
        build_list = self.__get_build_tcl()
        foundations_list = self.__get_foundations_tcl()
        floors_list = self.__get_floors_tcl()
        joints_list = self.__get_joints_tcl()
        beams_list = self.__get_beams_tcl()
        columns_list = self.__get_columns_tcl()
        gravity_list = self.__get_gravity_tcl()
        modal_list = self.__get_modal_tcl()
        nspa_list = self.__get_nspa_tcl()
        run_list = self.__get_run_tcl()
        # Write model source file
        with open(directory / 'model.tcl', 'w') as file:
            file.write('\n'.join(build_list))
        # Write foundations source file
        with open(directory / 'foundations.tcl', 'w') as file:
            file.write('\n'.join(foundations_list))
        # Write floors source file
        with open(directory / 'floors.tcl', 'w') as file:
            file.write('\n'.join(floors_list))
        # Write joints source file
        with open(directory / 'joints.tcl', 'w') as file:
            file.write('\n'.join(joints_list))
        # Write beams source file
        with open(directory / 'beams.tcl', 'w') as file:
            file.write('\n'.join(beams_list))
        # Write columns source file
        with open(directory / 'columns.tcl', 'w') as file:
            file.write('\n'.join(columns_list))
        # Write gravity analysis source file
        with open(directory / 'gravity.tcl', 'w') as file:
            file.write('\n'.join(gravity_list))
        # Write modal analysis source file
        with open(directory / 'modal.tcl', 'w') as file:
            file.write('\n'.join(modal_list))
        # Write nspa source file
        with open(directory / 'nspa.tcl', 'w') as file:
            file.write('\n'.join(nspa_list))
        # Write example run file
        with open(directory / 'run.tcl', 'w') as file:
            file.write('\n'.join(run_list))

    def __get_build_py(self) -> List[str]:
        """Generates a list of strings representing the Python function that
        constructs the components of the numerical model in OpenSees.

        Return
        ------
        List[str]
            List of lines which will be written into model.py file.
        """
        # Convert vectors strings
        vecxz_x = ', '.join([str(v) for v in VECXZ_X])
        vecxz_y = ', '.join([str(v) for v in VECXZ_Y])
        vecxz_z = ', '.join([str(v) for v in VECXZ_Z])
        # Add lines for setting build method
        content = [
            '"""Adds the numerical model to the OpenSees domain.',
            '"""',
            "ops.wipe()",
            "ops.model('basic', '-ndm', 3, '-ndf', 6)",
            "",
            "# Geometric transformations",
            f"ops.geomTransf('Linear', {LINEAR_TRANSF_X}, {vecxz_x})",
            f"ops.geomTransf('Linear', {LINEAR_TRANSF_Y}, {vecxz_y})",
            f"ops.geomTransf('Linear', {LINEAR_TRANSF_Z}, {vecxz_z})",
            f"ops.geomTransf('PDelta', {PDELTA_TRANSF_Z}, {vecxz_z})",
            "",
            "# Rigid-like material and section",
            f"ops.uniaxialMaterial('Elastic', {RIGID_MAT}, {BIG_VALUE})",
            f"ops.section('Aggregator', {RIGID_SEC}, {RIGID_MAT}, 'P', " +
            f"{RIGID_MAT}, 'Vy',  {RIGID_MAT}, 'Vz', {RIGID_MAT}, 'My', " +
            f"{RIGID_MAT}, 'Mz', {RIGID_MAT}, 'T')",
            "",
            "# Define components of foundations",
            "add_foundations()",
            "# Define components of floors",
            "add_floors()",
            "# Define components of joints",
            "add_joints()",
            "# Define components of beams",
            "add_beams()",
            "# Define components of columns",
            "add_columns()",
            "# Perform static analysis under gravity loads",
            "do_gravity()",
            ""
        ]
        # Add white spaces for method content
        content = ['    ' + item if item
                   else item
                   for item in content]
        # Add method definition
        method = ["def build_model() -> None:"]
        # Add imports
        imports = ["import openseespy.opensees as ops",
                   "",
                   "from .foundations import add_foundations",
                   "from .floors import add_floors",
                   "from .joints import add_joints",
                   "from .beams import add_beams",
                   "from .columns import add_columns",
                   "from .gravity import do_gravity",
                   "", ""]
        content = imports + method + content

        return content

    def __get_foundations_py(self) -> List[str]:
        """Generates a list of strings representing the Python function that
        constructs the components of the foundation in OpenSees.

        Return
        ------
        List[str]
            List of lines which will be written into foundations.py file.
        """
        # Initialize the content list - docstring
        content = [
            '"""Add foundation components to ops domain '
            '(nodes and constraints).',
            '"""'
        ]
        # Add lines for constructing the foundation objects
        for foundation in self.foundations:
            content.extend(foundation.to_py())
            content.append("")
        # Add white spaces for method content
        content = ['    ' + item if item
                   else item
                   for item in content]
        # Add method definition
        method = ["def add_foundations() -> None:"]
        # Add imports
        imports = ["import openseespy.opensees as ops",
                   "", ""]
        content = imports + method + content

        return content

    def __get_floors_py(self) -> List[str]:
        """Generates a list of strings representing the Python function that
        constructs the components of all floors in OpenSees.

        Return
        ------
        List[str]
            List of lines which will be written into floors.py file.
        """
        # Initialize the content list - docstring
        content = [
            '"""Add floors to ops domain (nodes & diaphrams).',
            '"""'
        ]
        # Add lines for constructing the floor objects
        for floor in self.floors:
            content.extend(floor.to_py())
            content.append("")
        # Add white spaces for method content
        content = ['    ' + item if item
                   else item
                   for item in content]
        # Add method definition
        method = ["def add_floors() -> None:"]
        # Add imports
        imports = ["import openseespy.opensees as ops",
                   "", ""]
        content = imports + method + content

        return content

    def __get_joints_py(self) -> List[str]:
        """Generates a list of strings representing the Python function that
        constructs the components of all joints in OpenSees.

        Return
        ------
        List[str]
            List of lines which will be written into joints.py file.
        """
        # Initialize the content list - docstring
        content = [
            '"""Add components of joints to ops domain.',
            '"""'
        ]
        # Add lines for constructing the stairs joint objects
        content.append('# -------------------------------------------------')
        content.append('# Add stairs joints to ops domain '
                       '(nodes and rigid offsets)')
        content.append('# -------------------------------------------------')
        for joint in self.stairs_joints:
            content.extend(joint.to_py())
            content.append("")
        # Add lines for constructing the floor joint objects
        content.append('# -------------------------------------------------')
        content.append('# Add floor joints to ops domain '
                       '(nodes, joint offsets and flexibility)')
        content.append('# -------------------------------------------------')
        for joint in self.floor_joints:
            content.extend(joint.to_py())
            content.append("")
        # Add white spaces for method content
        content = ['    ' + item if item
                   else item
                   for item in content]
        # Add method definition
        method = ["def add_joints() -> None:"]
        # Add imports
        imports = ["import openseespy.opensees as ops",
                   "", ""]
        content = imports + method + content

        return content

    def __get_beams_py(self) -> List[str]:
        """Generates a list of strings representing the Python function that
        constructs the components of all beams in OpenSees.

        Return
        ------
        List[str]
            List of lines which will be written into beams.py file.
        """
        # Initialize the content list - docstring
        content = [
            '"""Add components of all beams to ops domain '
            '(plastic hinges, beam elements and nodes)',
            '"""'
        ]
        # Add lines for constructing the beam objects
        for beam in self.beams:
            content.extend(beam.to_py())
            content.append("")
        # Add white spaces for method content
        content = ['    ' + item if item
                   else item
                   for item in content]
        # Add method definition
        method = ["def add_beams() -> None:"]
        # Add imports
        imports = ["import openseespy.opensees as ops",
                   "", ""]
        content = imports + method + content

        return content

    def __get_columns_py(self) -> List[str]:
        """Generates a list of strings representing the Python function that
        constructs the components of all columns in OpenSees.

        Return
        ------
        List[str]
            List of lines which will be written into columns.py file.
        """
        # Initialize the content list - docstring
        content = [
            '"""Add components of all columns to ops domain '
            '(plastic hinges, column elements and nodes)',
            '"""'
        ]
        # Add lines for constructing the beam objects
        for column in self.columns:
            content.extend(column.to_py())
            content.append("")
        # Add white spaces for method content
        content = ['    ' + item if item
                   else item
                   for item in content]
        # Add method definition
        method = ["def add_columns() -> None:"]
        # Add imports
        imports = ["import openseespy.opensees as ops",
                   "", ""]
        content = imports + method + content

        return content

    def __get_gravity_py(self) -> List[str]:
        """Generates a list of strings representing the Python function that
        constructs the components of the gravity analysis in OpenSees.

        Return
        ------
        List[str]
            List of lines which will be written into gravity.py file.
        """
        # Initialize the content list - docstring, load pattern, time-series
        content = [
            '"""Perform linear static analysis under gravity loads.',
            '"""',
            "# Add gravity time-series and load pattern to ops domain",
            f"ops.timeSeries('Constant', {GRAV_TS_TAG})",
            f"ops.pattern('Plain', {GRAV_P_TAG}, {GRAV_TS_TAG})",
            ""
        ]
        # Add lines for constructing the beam gravity load objects
        content.append("# Add beam gravity loads to ops domain")
        for beam in self.beams:
            content.append(beam.to_py_grav_loads())
        # Add lines for constructing the column gravity load objects
        content.append("")
        content.append("# Add column gravity loads to ops domain")
        for column in self.columns:
            content.extend(column.to_py_grav_loads())
        # Add lines for performing gravity analysis
        content.append("")
        content.append("# Perform gravity analysis and save the model state")
        content.append("ops.system('UmfPack')")
        content.append("ops.numberer('RCM')")
        content.append("ops.constraints('Transformation')")
        content.append("ops.test('NormDispIncr', 1e-08, 1)")
        content.append("ops.integrator('LoadControl', 1)")
        content.append("ops.algorithm('Linear')")
        content.append("ops.analysis('Static')")
        content.append("ops.analyze(1)")
        content.append("ops.loadConst('-time', 0.0)")
        content.append("ops.wipeAnalysis()")
        content.append("")
        # Add white spaces for method content
        content = ['    ' + item if item
                   else item
                   for item in content]
        # Add method definition
        method = ["def do_gravity() -> None:"]
        # Add imports
        imports = ["import openseespy.opensees as ops",
                   "", ""]
        content = imports + method + content

        return content

    def __get_modal_py(self) -> List[str]:
        """Generates a list of strings representing the Python function
        for modal analysis in OpenSees.

        Return
        ------
        List[str]
            List of lines which will be written into modal.py file.
        """
        # Retrained floor nodes
        nodes = ', '.join([f"{floor.rnode.tag}" for floor in self.floors])
        # Initialize the content list - docstring
        content = ['"""Perform modal analysis for built OpenSees model.',
                   "",
                   "Parameters",
                   "----------",
                   "num_modes : int, optional",
                   "    Number of modes considered for modal analysis.",
                   "    By default 3.",
                   "",
                   "Return",
                   "------",
                   "dict",
                   "    Dictionary containing modal properties.",
                   '"""',]
        # Add lines for setting the output directory
        content.append("# Set output directory")
        content.append(
            "output_directory = Path(__file__).parent / 'Modal-Results'")
        content.append("if not Path.exists(output_directory):")
        content.append("    Path.mkdir(output_directory)")
        # Add lines for building the numerical model
        content.append("# Build the numerical model")
        content.append("build_model()")
        # Add lines for performing eigenvalue analysis
        content.append("")
        content.append("# Perform eigen value analysis")
        content.append("ops.eigen(num_modes)")
        # Add lines for looping through eigenvectors and saving them
        content.append("# Save eigen vectors for retained floor nodes")
        content.append(f"nodes = [{nodes}]")
        content.append("for i in range(1, num_modes+1):")
        content.append("    modal_disps = []")
        content.append("    for node in nodes:")
        content.append(
            "        disps = "
            "', '.join([f'{disp}' for disp in ops.nodeEigenvector(node, i)])"
            )
        content.append("        modal_disps.append(f'{node}, {disps}')")
        content.append("    modal_disps = '\\n'.join(modal_disps)")
        content.append("    report_file_path = (output_directory / "
                       "f'EigenVectors_Mode{i}.txt').as_posix()")
        content.append("    with open(report_file_path, 'w') as file:")
        content.append("        file.write(modal_disps)")
        # Add lines for saving modal properties
        content.append("")
        content.append("# Perform modal analysis and save results")
        content.append("report_file_path = (output_directory / "
                       "'ModalProperties.txt').as_posix()")
        content.append("results = ops.modalProperties('-print', '-return', "
                       "'-file', report_file_path, '-unorm')")
        content.append("")
        # Add return statement
        content.append("return results")
        content.append("")
        # Add white spaces for method content
        content = ['    ' + item if item
                   else item
                   for item in content]
        # Add method definition
        method = ["def do_modal(num_modes: int = 3) -> dict:"]
        # Add imports
        imports = ["import openseespy.opensees as ops",
                   "from pathlib import Path",
                   "",
                   "from .model import build_model",
                   "", ""]
        content = imports + method + content

        return content

    def __get_nspa_dof_py(self, ctrl_dof: Literal[1, 2]) -> List[str]:
        """Generates a list of strings representing the Python function
        for nonlinear static pushover (NSPA) analysis in OpenSees.

        Parameters
        ----------
        ctrl_dof : Literal[1, 2]
            Control degrees of freedom for loading.
            1: X-direction.
            2: Y-direction.

        Return
        ------
        List[str]
            List of lines representing do_nspa_{direction} method.
        """
        # Get NSPA loading parameters
        nodes, loads, ctrl_node = \
            self.__get_nspa_loading_parameters(ctrl_dof)
        # Set support nodes
        supports = ', '.join([
            f"{found.foundation_node.tag}" for found in self.foundations
            ])
        # Set floor nodes
        floors = ', '.join([f"{floor.rnode.tag}" for floor in self.floors])
        # Directions per dof
        if ctrl_dof == 1:
            direction = 'x'
        elif ctrl_dof == 2:
            direction = 'y'
        # Initialize the content list - docstring
        content = [
            '"""Performs nonlinear static pushover analysis (NSPA) '
            f'in {direction} direction.',
            "",
            "Parameters",
            "----------",
            "max_drift : float, optional.",
            "    Maximum considered drift value for the control node.",
            f"    By default {self.max_drift}",
            "dincr : float, optional.",
            "    First displacement increment considered during the analysis.",
            f"    By default {self.dincr}.",
            "",
            "Return",
            "------",
            "ctrl_disp : list[float]",
            "    Displacement values of control node.",
            "base_shear : list[float]",
            "    Base shear value obtained as sum of the reaction forces.",
            '"""'
            ]
        # Add lines for setting the output directory
        content.append("# Set output directory")
        content.append(
            "output_directory = Path(__file__).parent / 'NSPA-Results'")
        content.append("if not Path.exists(output_directory):")
        content.append("    Path.mkdir(output_directory)")
        content.append("reaction_file_path = (output_directory / "
                       f"'support_reactions_{direction}.out').as_posix()")
        content.append("disp_file_path = (output_directory / "
                       f"'storey_displacements_{direction}.out').as_posix()")
        content.append("storey_heights_file_path = (output_directory / "
                       "'storey_heights.out').as_posix()")
        # Add lines for building the numerical model
        content.append("")
        content.append("# Build the numerical model")
        content.append("build_model()")
        # Add lines for setting the time-series and load pattern
        content.append("")
        content.append("# Add NSPA time-series and load pattern to ops domain")
        content.append(f"ops.timeSeries('Linear', {NSPA_TS_TAG})")
        content.append(f"ops.pattern('Plain', {NSPA_P_TAG}, {NSPA_TS_TAG})")
        # Add lines for setting the nspa loads
        content.append("# Add lateral nspa loads to ops domain")
        for node, load_values in zip(nodes, loads):
            values_str = ', '.join([f"{val}" for val in load_values])
            content.append(f"ops.load({node}, {values_str})")
        # Add lines for setting recorders
        content.append("")
        content.append("# Set the recorders")
        content.append(f"ctrl_node = {ctrl_node}  # Control node")
        content.append(f"ctrl_dof = {ctrl_dof}  # Control dof")
        content.append(f"supports = [{supports}]  # Foundation nodes")
        content.append(f"floors = [{floors}]  # Retained floor nodes")
        content.append("ops.recorder('Node', '-file', disp_file_path, '-node',"
                       " *floors, '-dof', ctrl_dof, 'disp')")
        content.append("ops.recorder('Node', '-file', reaction_file_path, "
                       "'-node', *supports, '-dof', ctrl_dof, 'reaction')")
        # Add lines for saving storey heights
        content.append("")
        content.append("# Base level coordinate")
        content.append(
            "base_level = min([ops.nodeCoord(node, 3) for node in supports])"
            )
        content.append("# Save storey heights")
        content.append("with open(storey_heights_file_path, 'w') as file:")
        content.append("    for node in floors:")
        content.append(
            "        file.write(f'{ops.nodeCoord(node, 3) - base_level}\\n')"
            )
        # Add lines for setting the analysis parameters
        content.append("")
        content.append("# Set some analysis parameters")
        content.append(
            "max_disp = max_drift * (ops.nodeCoord(ctrl_node, 3) - base_level)"
            )
        content.append("tol_init = 1.0e-6")
        content.append("iter_init = 20")
        content.append("ops.wipeAnalysis()")
        content.append("ops.system('UmfPack')")
        content.append("ops.numberer('RCM')")
        content.append("ops.constraints('Penalty', 1e12, 1e12)")
        content.append("ops.test('NormDispIncr', tol_init, iter_init)")
        content.append("ops.integrator('DisplacementControl', ctrl_node, "
                       "ctrl_dof, dincr)")
        content.append("ops.algorithm('Newton', '-initialThenCurrent')")
        content.append("ops.analysis('Static')")
        # Add lines for performing the analysis
        content.append("")
        content.append("# Start performing the analysis")
        content.append("base_shear = [0]")
        content.append("ctrl_disp = [0]")
        content.append("ok = 0")
        content.append("cont = True")
        content.append("while ok == 0 and cont:")
        content.append("    ops.test('NormDispIncr', tol_init, iter_init)")
        content.append("    ops.integrator('DisplacementControl', ctrl_node, "
                       "ctrl_dof, dincr)")
        content.append("    ops.algorithm('Newton', '-initialThenCurrent')")
        content.append("    ok = ops.analyze(1)")
        content.append("    if ok != 0:  # try other algorithms")
        content.append("        ok = _set_algorithm(ok, tol_init)")
        content.append("    if ok != 0:  # reduce dincr to an half")
        content.append("        ops.integrator('DisplacementControl', "
                       "ctrl_node, ctrl_dof, 0.5*dincr)")
        content.append("        ok = _set_algorithm(ok, tol_init)")
        content.append("    if ok != 0:  # reduce dincr to a quarter")
        content.append("        ops.integrator('DisplacementControl', "
                       "ctrl_node, ctrl_dof, 0.25*dincr)")
        content.append("        ok = _set_algorithm(ok, tol_init)")
        content.append("    if ok != 0:  # increase tolerance by factor of 10")
        content.append("        ok = _set_algorithm(ok, 10*tol_init)")
        content.append(
            "    if ok != 0:  # increase tolerance by factor of 100"
        )
        content.append("        ok = _set_algorithm(ok, 100*tol_init)")
        content.append("")
        content.append("    # Get the base shear force")
        content.append("    ops.reactions()")
        content.append("    current_disp = ops.nodeDisp(ctrl_node, ctrl_dof)")
        content.append("    current_shear = abs(sum([ops.nodeReaction(node, "
                       "ctrl_dof) for node in supports]))")
        content.append("    # Set continue flag")
        content.append("    cont = current_disp < max_disp and current_shear <"
                       " 50000 and current_shear >= 0.2*max(base_shear)")
        content.append("    # Append base shear and control node displacement")
        content.append("    if ok == 0 and cont:")
        content.append("        base_shear.append(current_shear)")
        content.append("        ctrl_disp.append(current_disp)")
        # Add lines for wiping the model
        content.append("")
        content.append("# Wipe the model")
        content.append("ops.wipe()")
        # Add lines for return statement
        content.append(
            "# Return base shear and control node displacement history"
        )
        content.append("return ctrl_disp, base_shear")
        content.append("")
        # Add white spaces for method content
        content = ['    ' + item if item
                   else item
                   for item in content]
        # Add method definition
        method = [
            f"def do_nspa_{direction}(max_drift: float = {self.max_drift}, "
            f"dincr: float = {self.dincr}) "
            "-> tuple[list[float], list[float]]:"
            ]
        content = method + content

        return content

    def __get_algorithm_py(self) -> List[str]:
        """Generates a list of strings representing the Python function
        for setting the algorithm during nspa in OpenSees.

        Return
        ------
        List[str]
            List of lines representing _set_algorithm method.
        """
        content = [
            '"""Sets the solution algorithm for NSPA in ops domain.',
            "",
            "Parameters",
            "----------",
            "ok : int",
            "    Result of the last analysis step in OpenSees.",
            "tol : float",
            "    The tolerance criteria used to check for convergence.",
            "iter : int, optional",
            "    The max number of iterations to check before returning "
            "failure.",
            "    By default 100."
            "",
            "Return",
            "------",
            "int",
            "    Result of the new analysis step in OpenSees.",
            '"""'
        ]
        # Add lines for setting nspa algorithm
        content.append("# Try KrylovNewton")
        content.append("if ok != 0:")
        content.append("    ops.test('NormDispIncr', tol, iter)")
        content.append("    ops.algorithm('KrylovNewton')")
        content.append("    ok = ops.analyze(1)")
        content.append("# Try NewtonLineSearch algorithm")
        content.append("if ok != 0:")
        content.append("    ops.test('NormDispIncr', tol, iter)")
        content.append("    ops.algorithm('NewtonLineSearch')")
        content.append("    ok = ops.analyze(1)")
        content.append("# Try Broyden algorithm")
        content.append("if ok != 0:")
        content.append("    ops.test('NormDispIncr', tol, iter)")
        content.append("    ops.algorithm('Broyden', 50)")
        content.append("    ok = ops.analyze(1)")
        content.append(
            "# Try Broyden-Fletcher-Goldfarb-Shanno (BFGS) algorithm"
            )
        content.append("if ok != 0:")
        content.append("    ops.test('NormDispIncr', tol, iter)")
        content.append("    ops.algorithm('BFGS')")
        content.append("    ok = ops.analyze(1)")
        content.append("# Return the analysis result")
        # Add lines for setting return statement
        content.append("return ok")
        content.append("")
        # Add white spaces for method content
        content = ['    ' + item if item
                   else item
                   for item in content]
        # Add method definition
        method = [
            "def _set_algorithm(ok: int, tol: float, iter: int = 100) -> None:"
            ]
        content = method + content

        return content

    def __get_nspa_py(self) -> List[str]:
        """Generates a list of strings representing Python functions for
        performing nonlinear static pushover (NSPA) analysis in OpenSees.

        Return
        ------
        List[str]
            List of lines which will be written into nspa.py file.
        """
        # Get all nspa methods
        algorithm_list = self.__get_algorithm_py() + [""]
        nspa_x_list = self.__get_nspa_dof_py(1) + [""]
        nspa_y_list = self.__get_nspa_dof_py(2)
        # Add imports
        imports = ["import openseespy.opensees as ops",
                   "from pathlib import Path",
                   "",
                   "from .model import build_model",
                   "", ""]
        content = imports + algorithm_list + nspa_x_list + nspa_y_list

        return content

    def __get_run_py(self) -> List[str]:
        """Generates a list of strings representing an example Python script
        for running nspa and modal analysis.

        Return
        ------
        List[str]
            List of lines which will be written into run.py.
        """
        content = [
            "# Import necessary modules using dynamic import",
            "import sys",
            "from pathlib import Path",
            "import importlib",
            "",
            "",
            "# Determine the package name dynamically",
            "current_dir = Path(__file__).resolve().parent",
            "parent_dir = current_dir.parent",
            "package_name = current_dir.name",
            "# Add the parent directory to sys.path",
            "sys.path.append(str(parent_dir))",
            "# Dynamically import modules from the determined package",
            "modal = importlib.import_module(f\"{package_name}.modal\")",
            "nspa = importlib.import_module(f\"{package_name}.nspa\")",
            "",
            "# Perform modal analysis",
            "results = modal.do_modal()",
            "# Perform nonlinear static pushover analysis in X direction",
            "dx, vx = nspa.do_nspa_x()",
            "# Perform nonlinear static pushover analysis in Y direction",
            "dy, vy = nspa.do_nspa_y()",
            ""
        ]

        return content

    def __get_build_tcl(self) -> List[str]:
        """Generates a list of strings representing the Tcl script that
        constructs the components of the numerical model in OpenSees.
        """
        vecxz_x = ' '.join([str(v) for v in VECXZ_X])
        vecxz_y = ' '.join([str(v) for v in VECXZ_Y])
        vecxz_z = ' '.join([str(v) for v in VECXZ_Z])

        content = [
            '# Adds the numerical model to the OpenSees domain',
            "",
            "wipe",
            "model BasicBuilder -ndm 3 -ndf 6",
            "",
            "# Geometric transformations",
            f"geomTransf Linear {LINEAR_TRANSF_X} {vecxz_x}",
            f"geomTransf Linear {LINEAR_TRANSF_Y} {vecxz_y}",
            f"geomTransf Linear {LINEAR_TRANSF_Z} {vecxz_z}",
            f"geomTransf PDelta {PDELTA_TRANSF_Z} {vecxz_z}",
            "",
            "# Rigid-like material and section",
            f"uniaxialMaterial Elastic {RIGID_MAT} {BIG_VALUE}",
            f"section Aggregator {RIGID_SEC} {RIGID_MAT} P " +
            f"{RIGID_MAT} Vy {RIGID_MAT} Vz {RIGID_MAT} My " +
            f"{RIGID_MAT} Mz {RIGID_MAT} T",
            "",
            "# Define components of foundations",
            "source foundations.tcl",
            "# Define components of floors",
            "source floors.tcl",
            "# Define components of joints",
            "source joints.tcl",
            "# Define components of beams",
            "source beams.tcl",
            "# Define components of columns",
            "source columns.tcl",
            "# Perform static analysis under gravity loads",
            "source gravity.tcl"
            ""
        ]

        return content

    def __get_foundations_tcl(self) -> List[str]:
        """Generates a list of strings representing the Tcl script that
        constructs the components of the foundation in OpenSees.
        """
        content = [
            '# Add foundation components to ops domain '
            '(nodes and constraints)\n'
        ]
        for foundation in self.foundations:
            content.extend(foundation.to_tcl())
            content.append("")

        return content

    def __get_floors_tcl(self) -> List[str]:
        """Generates a list of strings representing the Tcl script that
        constructs the components of all floors in OpenSees.
        """
        content = [
            '# Add floors to ops domain (nodes & diaphrams)\n'
        ]
        for floor in self.floors:
            content.extend(floor.to_tcl())
            content.append("")

        return content

    def __get_joints_tcl(self) -> List[str]:
        """Generates a list of strings representing the Tcl script that
        constructs the components of all joints in OpenSees.
        """
        content = [
            '# Add components of joints to ops domain\n'
        ]
        content.append('# -------------------------------------------------')
        content.append('# Add stairs joints to ops domain '
                       '(nodes and rigid offsets)')
        content.append('# -------------------------------------------------\n')
        for joint in self.stairs_joints:
            content.extend(joint.to_tcl())
            content.append("")

        content.append('# -------------------------------------------------')
        content.append('# Add floor joints to ops domain '
                       '(nodes, joint offsets and flexibility)')
        content.append('# -------------------------------------------------\n')
        for joint in self.floor_joints:
            content.extend(joint.to_tcl())
            content.append("")

        return content

    def __get_beams_tcl(self) -> List[str]:
        """Generates a list of strings representing the Tcl script that
        constructs the components of all beams in OpenSees.
        """
        content = [
            '# Add components of all beams to ops domain '
            '(plastic hinges, beam elements and nodes)\n'
        ]
        for beam in self.beams:
            content.extend(beam.to_tcl())
            content.append("")

        return content

    def __get_columns_tcl(self) -> List[str]:
        """Generates a list of strings representing the Tcl function that
        constructs the components of all columns in OpenSees.
        """
        content = [
            '# Add components of all columns to ops domain '
            '(plastic hinges, column elements and nodes)\n'
        ]
        for column in self.columns:
            content.extend(column.to_tcl())
            content.append("")

        return content

    def __get_gravity_tcl(self) -> List[str]:
        """Generates a list of strings representing the Tcl script that
        constructs the components of the gravity analysis in OpenSees.
        """

        content = [
            "# Perform linear static analysis under gravity loads",
            "",
            "# Add gravity time-series and load pattern to ops domain",
            f"timeSeries Constant {GRAV_TS_TAG}",
            f"pattern Plain {GRAV_P_TAG} {GRAV_TS_TAG}" + " {",
            ""
        ]

        content.append("    # Add beam gravity loads to ops domain")
        for beam in self.beams:
            content.append("    " + beam.to_tcl_grav_loads())

        content.append("")
        content.append("    # Add column gravity loads to ops domain")
        for column in self.columns:
            content.extend(["    " + i for i in column.to_tcl_grav_loads()])
        content.append("}")

        content.append("")
        content.append("# Perform gravity analysis and save the model state")
        content.append("system UmfPack")
        content.append("numberer RCM")
        content.append("constraints Transformation")
        content.append("test NormDispIncr 1e-08 1")
        content.append("integrator LoadControl 1")
        content.append("algorithm Linear")
        content.append("analysis Static")
        content.append("analyze 1")
        content.append("loadConst -time 0.0")
        content.append("wipeAnalysis")
        content.append("")

        return content

    def __get_modal_tcl(self) -> List[str]:
        """Generates a list of strings representing the Tcl procedure for
        modal analysis in OpenSees.

        Return
        ------
        List[str]
            List of lines which will be written into modal.tcl file.
        """
        # Retrained floor nodes
        nodes = ' '.join([f"{floor.rnode.tag}" for floor in self.floors])
        # Initialize the content list
        content = [
            "# Perform modal analysis for built OpenSees model",
            "#",
            "# Parameters",
            "# ----------",
            "# num_modes : int, optional",
            "#     Number of modes considered for modal analysis.",
            "#     By default 3."
            "#",
            "# Return",
            "# ------",
            "# dict",
            "#     Dictionary containing modal properties.",
            ]
        content.append("")
        # Add lines for setting the output directory
        content.append("# Set output directory")
        content.append('set output_directory "Modal-Results"')
        content.append("file mkdir $output_directory")
        # Add lines for building the numerical model
        content.append("# Build the numerical model")
        content.append("source model.tcl")
        # Add lines for performing eigenvalue analysis
        content.append("")
        content.append("# Perform eigenvalue analysis")
        content.append("set eigenVals [eigen $numModes]")
        # Add lines for looping through eigenvectors and saving them
        content.append("# Save eigen vectors for retained floor nodes")
        content.append(f'set nodes [list {nodes}]')
        content.append("# Loop through eigenvectors")
        content.append("for {set i 1} {$i <= $numModes} {incr i} {")
        content.append('    set modalDisps ""')
        content.append("    foreach node $nodes {")
        content.append("        # Get the eigenvector as a list of floats")
        content.append("        set eigenvector [nodeEigenvector $node $i]")
        content.append("        # Join the list into a comma-separated string")
        content.append('        set disps [join $eigenvector ", "]')
        content.append("        # Append the node tag and the comma-separated"
                       " eigenvector string")
        content.append('        append modalDisps "$node, $disps\\n"')
        content.append("    }")
        content.append(
            '    # Write the eigenvector data for the mode to a file')
        content.append(
            '    set report_file '
            '[open "$output_directory/EigenVectors_Mode${i}.txt" "w"]'
            )
        content.append("    puts $report_file $modalDisps")
        content.append("    close $report_file")
        content.append("}")
        # Add lines for saving modal properties
        content.append("")
        content.append("# Perform modal analysis and save results")
        content.append(
            'set report_file "$output_directory/ModalProperties.txt"'
            )
        content.append(
            'set results [modalProperties -print -return -file '
            '$report_file -unorm]'
            )
        # Add return statement
        content.append("")
        content.append("return $results")
        # Add Tcl procedure definition
        tmp = ["proc do_modal { {numModes 3} } {"]
        content = tmp + \
            ["    " + item if item
             else item
             for item in content]
        # End of procedure
        content.append("}")

        return content

    def __get_nspa_dof_tcl(self, ctrl_dof: Literal[1, 2]) -> List[str]:
        """Generates a list of strings representing the Tcl procedure
        for nonlinear static pushover (NSPA) analysis in OpenSees.

        Parameters
        ----------
        ctrl_dof : Literal[1, 2]
            Control degrees of freedom for loading.
            1: X-direction.
            2: Y-direction.

        Return
        ------
        List[str]
            List of lines representing do_nspa_{direction} procedure.
        """
        # Get NSPA loading parameters
        nodes, loads, ctrl_node = \
            self.__get_nspa_loading_parameters(ctrl_dof)
        # Set support nodes
        supports = ' '.join([
            f"{found.foundation_node.tag}" for found in self.foundations
            ])
        # Set floor nodes
        floors = ' '.join([f"{floor.rnode.tag}" for floor in self.floors])
        # Directions per dof
        if ctrl_dof == 1:
            direction = 'x'
        elif ctrl_dof == 2:
            direction = 'y'

        # Initialize the content list - docstring
        content = [
            "# Performs nonlinear static pushover analysis (NSPA) "
            f"in {direction} direction.",
            "#",
            "# Parameters",
            "# ----------",
            "# max_drift : float, optional.",
            "#    Maximum considered drift value for the control node.",
            f"#    By default {self.max_drift}",
            "# dincr : float, optional.",
            "#    First displacement increment considered during the "
            "analysis.",
            f"#    By default {self.dincr}.",
            "#",
            "# Return",
            "# ------",
            "# ctrl_disp : list[float]",
            "#    Displacement values of control node.",
            "# base_shear : list[float]",
            "#    Base shear value obtained as sum of the reaction forces.",
            ""
            ]
        # Add lines for setting the output directory
        content.append("# Set output directory")
        content.append("set output_directory \"NSPA-Results\"")
        content.append("file mkdir $output_directory")
        content.append(
            'set reaction_file_path "$output_directory'
            f'/support_reactions_{direction}.out"')
        content.append(
            'set disp_file_path "$output_directory'
            f'/storey_displacements_{direction}.out"')
        content.append(
            'set storey_heights_file_path '
            '"$output_directory/storey_heights.out"')
        # Add lines for building the numerical model
        content.append("")
        content.append("# Build the numerical model")
        content.append("source model.tcl")
        # Add lines for setting the time-series and load pattern
        content.append("")
        content.append("# Add NSPA time-series and load pattern to ops domain")
        content.append(f"timeSeries Linear {NSPA_TS_TAG}")
        content.append(f"pattern Plain {NSPA_P_TAG} {NSPA_TS_TAG} " + "{")
        # Add lines for setting the nspa loads
        for node, load_values in zip(nodes, loads):
            values_str = ' '.join([f"{val}" for val in load_values])
            content.append(f"    load {node} {values_str}")
        content.append("}")
        # Add lines for setting recorders
        content.append("")
        content.append("# Set recorders")
        content.append(f"set ctrl_node {ctrl_node}")
        content.append(f"set ctrl_dof {ctrl_dof}")
        content.append(f"set supports [list {supports}]")
        content.append(f"set floors [list {floors}]")
        content.append("recorder Node -file $disp_file_path -node {*}$floors "
                       "-dof $ctrl_dof disp")
        content.append("recorder Node -file $reaction_file_path -node "
                       "{*}$supports -dof $ctrl_dof reaction")
        # Add lines for saving storey heights
        content.append("")
        content.append("# Base level coordinate")
        content.append("set base_level 1.0e12")
        content.append("foreach node $supports {")
        content.append("    set zCoord [nodeCoord $node 3]")
        content.append("    if {$zCoord < $base_level} {")
        content.append("        set base_level $zCoord")
        content.append("    }")
        content.append("}")
        content.append("# Save storey heights")
        content.append('set file [open $storey_heights_file_path "w"]')
        content.append("foreach node $floors {")
        content.append(
            "    puts $file [expr {[nodeCoord $node 3] - $base_level}]"
            )
        content.append("}")
        content.append("close $file")
        # Add lines for setting the analysis parameters
        content.append("")
        content.append("# Set analysis parameters")
        content.append(
            "set max_disp "
            "[expr {$max_drift * [nodeCoord $ctrl_node 3] - $base_level}]"
            )
        content.append("set tol_init 1.0e-6")
        content.append("set iter_init 20")
        content.append("wipeAnalysis")
        content.append("system UmfPack")
        content.append("numberer RCM")
        content.append("constraints Penalty 1.0e12 1.0e12")
        content.append("test NormDispIncr $tol_init $iter_init")
        content.append("integrator DisplacementControl $ctrl_node $ctrl_dof "
                       "$dincr")
        content.append("algorithm Newton -initialThenCurrent")
        content.append("analysis Static")
        # Add lines for performing the analysis
        content.append("")
        content.append("# Start performing the analysis")
        content.append("set max_base_shear 0")
        content.append("set ok 0")
        content.append("set cont 1")
        content.append("set base_shear [list 0.0]")
        content.append("set ctrl_disp [list 0.0]")
        content.append("while { $ok == 0 && $cont == 1 } {")
        content.append("    test NormDispIncr $tol_init $iter_init")
        content.append("    integrator DisplacementControl $ctrl_node "
                       "$ctrl_dof $dincr")
        content.append("    algorithm Newton -initialThenCurrent")
        content.append("    set ok [analyze 1]")
        content.append("    # try other algorithms")
        content.append("    if { $ok != 0 } {")
        content.append("        set ok [_set_algorithm $ok $tol_init]")
        content.append("    }")
        content.append("    # reduce dincr to an half")
        content.append("    if { $ok != 0 } {")
        content.append("        integrator DisplacementControl $ctrl_node "
                       "$ctrl_dof [expr 0.5 * $dincr]")
        content.append("        set ok [_set_algorithm $ok $tol_init]")
        content.append("    }")
        content.append("    # reduce dincr to a quarter")
        content.append("    if { $ok != 0 } {")
        content.append("        integrator DisplacementControl $ctrl_node "
                       "$ctrl_dof [expr 0.25 * $dincr]")
        content.append("        set ok [_set_algorithm $ok $tol_init]")
        content.append("    }")
        content.append("    # increase tolerance by factor of 10")
        content.append("    if { $ok != 0 } {")
        content.append("        set ok [_set_algorithm $ok "
                       "[expr 10 * $tol_init]]")
        content.append("    }")
        content.append("    # increase tolerance by factor of 100")
        content.append("    if { $ok != 0 } {")
        content.append("        set ok [_set_algorithm $ok "
                       "[expr 100 * $tol_init]]")
        content.append("    }")
        content.append("")
        content.append("    # Get the base shear force")
        content.append("    reactions")
        content.append("    set current_disp [nodeDisp $ctrl_node $ctrl_dof]")
        content.append("    set current_shear 0")
        content.append("    foreach foundation_node $supports {")
        content.append(
            "        set reaction [nodeReaction $foundation_node $ctrl_dof]")
        content.append(
            "        set current_shear [expr $current_shear + abs($reaction)]")
        content.append("    }")
        content.append("    # Calculate the maximum encountered shear value")
        content.append(
            "    "
            "set max_base_shear [expr {max($max_base_shear, $current_shear)}]"
            )
        content.append("    # Set continue flag")
        content.append(
            "    "
            "set cont [expr {($current_disp < $max_disp) && "
            "($current_shear < 50000) && "
            "($current_shear >= 0.2 * $max_base_shear)}]")
        content.append("    # Append base shear and control node displacement")
        content.append("    if { $ok == 0 && $cont == 1 } {")
        content.append("        lappend base_shear $current_shear")
        content.append("        lappend ctrl_disp $current_disp")
        content.append("    }")
        content.append("}")
        # Add lines for wiping the model
        content.append("")
        content.append("# Wipe the model")
        content.append("wipe")
        # Add lines for return statement
        content.append(
            "# Return base shear and control node displacement history"
        )
        content.append("return [list $ctrl_disp $base_shear]")
        # Add white spaces for method content
        content = ['    ' + item if item
                   else item
                   for item in content]
        # Add method definition
        var1 = "{ max_drift " + f"{self.max_drift}" + " }"
        var2 = "{ dincr " + f"{self.dincr}" + " }"
        method = [f"proc do_nspa_{direction}" + " { " +
                  f"{var1} {var2}" + " }" + " { "]
        content = method + content
        # Add method closure bracket
        content = content + ["}", ""]

        return content

    def __get_algorithm_tcl(self) -> List[str]:
        """Generates a list of strings representing the Tcl procedure
        for setting the algorithm during nspa in OpenSees.

        Return
        ------
        List[str]
            List of lines representing Tcl proceudure _set_algorithm.
        """
        # Add the procedure content
        content = [
            "# Sets the solution algorithm for NSPA in OpenSees.",
            "#",
            "# Parameters",
            "# ----------",
            "# ok : int",
            "#     Result of the last analysis step in OpenSees.",
            "# tol : float",
            "#     The tolerance criteria used to check for convergence.",
            "# iter : float",
            "#     The max number of iterations to check before returning "
            "failure.",
            "#     By default 100.",
            "#",
            "# Return",
            "# ------",
            "# int",
            "#     Result of the new analysis step in OpenSees.",
            "",
            "# Try KrylovNewton",
            "if { $ok != 0 } {",
            "    test NormDispIncr $tol $iter",
            "    algorithm KrylovNewton",
            "    set ok [analyze 1]",
            "}",
            "# Try NewtonLineSearch algorithm",
            "if { $ok != 0 } {",
            "    test NormDispIncr $tol $iter",
            "    algorithm NewtonLineSearch",
            "    set ok [analyze 1]",
            "}",
            "# Try Broyden algorithm",
            "if { $ok != 0 } {",
            "    test NormDispIncr $tol 10",
            "    algorithm Broyden 50",
            "    set ok [analyze 1]",
            "}",
            "# Try Broyden-Fletcher-Goldfarb-Shanno (BFGS) algorithm",
            "if { $ok != 0 } {",
            "    test NormDispIncr $tol 10",
            "    algorithm BFGS",
            "    set ok [analyze 1]",
            "}",
            "# Return the analysis result",
            "return $ok"
        ]
        # Add white spaces for method content
        content = ['    ' + item if item
                   else item
                   for item in content]
        # Add method definition
        method = ["proc _set_algorithm { ok tol {iter 100} } {"]
        content = method + content
        # Add method closure bracket
        content = content + ["}", ""]

        return content

    def __get_nspa_tcl(self) -> List[str]:
        """Generates a list of strings representing Tcl procedures for
        performing nonlinear static pushover (NSPA) analysis in OpenSees.

        Return
        ------
        List[str]
            List of lines which will be written into nspa.tcl file.
        """
        # Get all nspa procedures
        algorithm_list = self.__get_algorithm_tcl() + [""]
        nspa_x_list = self.__get_nspa_dof_tcl(1) + [""]
        nspa_y_list = self.__get_nspa_dof_tcl(2)

        content = algorithm_list + nspa_x_list + nspa_y_list

        return content

    def __get_run_tcl(self) -> List[str]:
        """Generates a list of strings representing an example Python script
        for running nspa and modal analysis.

        Return
        ------
        List[str]
            List of lines which will be written into run.py.
        """
        content = [
            "source modal.tcl",
            "source nspa.tcl",
            "",
            "# Perform modal analysis",
            "set results [do_modal 5]",
            "# Perform nonlinear static pushover analysis in X direction",
            "lassign [do_nspa_x] dx vx",
            "# Perform nonlinear static pushover analysis in Y direction",
            "lassign [do_nspa_y] dy vy",
            ""
        ]

        return content

    def plot_model(
        self, show_nodes: Literal['no', 'yes'] = 'yes', line_width: float = 3,
        directory: Optional[str | Path] = None, show: bool = True
    ) -> None:
        """
        Plots the structural model, showing nodes and elements grouped by type
        (rigid elements, beams, and columns).

        Parameters
        ----------
        show_nodes : Literal['no', 'yes'], optional
            A flag to control whether to display the nodes in the plot.
            'yes' to show the nodes, 'no' to hide them. By default 'yes'.
        line_width : float, optional
            Specifies the line width used to draw the elements in the plot.
            By default 3.
        directory : str | Path | None, optional
            Directory to save an image of the model. If None, the image will
            not be saved. By default None.
        show : bool, optional
                Flag for showing the figure in an interactive window,
                by default True.
        """
        # Set the group elements
        rigid = []
        for joint in self.floor_joints:
            rigid.extend(joint.rigid_ele)
        for joint in self.stairs_joints:
            rigid.extend(joint.rigid_ele)
        beams = [beam.design.line.tag for beam in self.beams]
        columns = [column.design.line.tag for column in self.columns]
        groups = [
            [rigid, beams, columns],
            ["black", "red", "blue"]
        ]
        # Build the model
        self.build()
        # Path to the file (without the file extension)
        if directory:
            filename = str(Path(directory) / 'model_view.html')
        else:
            filename = None
        # Plot the model
        pl.plot_model(show_nodes=show_nodes, ele_groups=groups, show=show,
                      line_width=line_width, filename=filename)

    def plot_mode_shape(
        self, mode_number: int = 1, scale: float = 100, line_width: float = 3,
        contour: Optional[Literal['x', 'y', 'z']] = None,
        directory: Optional[str | Path] = None, show: bool = True
    ) -> None:
        """
        Plots the mode shape of the structure for a given mode number,
        scaled for visual clarity.

        Parameters
        ----------
        mode_number : int, optional
            Specifies the mode number to be plotted.
            By default 1.
        scale : float, optional
            A scaling factor to exaggerate the mode shape for better
            visualization. By default 100.
        line_width : float, optional
            Specifies the line width used to draw the mode shape.
            By default 3.
        contour : Literal['x', 'y', 'z'] | None, optional
            Contours of displacement in x, y, or z.
            By default None.
        directory : str | Path | None, optional
            Directory to save an image of the model. If None, the image will
            not be saved. By default None.
        show : bool, optional
                Flag for showing the figure in an interactive window,
                by default True.
        """
        # Build the model
        self.build()
        # Path to the file
        if directory:
            filename = str(Path(directory) / f'mode_{mode_number}_shape.html')
        else:
            filename = None
        # Plot the mode shape
        pl.plot_mode_shape(
            mode_number=mode_number, scale=scale, line_width=line_width,
            contour=contour, filename=filename, show=show
        )
