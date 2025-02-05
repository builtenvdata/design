import openseespy.opensees as ops
from pathlib import Path

from .model import build_model


def _set_algorithm(ok: int, tol: float, iter: int = 100) -> None:
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
        ops.algorithm('NewtonLineSearch')
        ok = ops.analyze(1)
    # Try Broyden algorithm
    if ok != 0:
        ops.test('NormDispIncr', tol, iter)
        ops.algorithm('Broyden', 50)
        ok = ops.analyze(1)
    # Try Broyden-Fletcher-Goldfarb-Shanno (BFGS) algorithm
    if ok != 0:
        ops.test('NormDispIncr', tol, iter)
        ops.algorithm('BFGS')
        ok = ops.analyze(1)
    # Return the analysis result
    return ok


def do_nspa_x(max_drift: float = 0.1, dincr: float = 0.001) -> tuple[list[float], list[float]]:
    """Performs nonlinear static pushover analysis (NSPA) in x direction.

    Parameters
    ----------
    max_drift : float, optional.
        Maximum considered drift value for the control node.
        By default 0.1
    dincr : float, optional.
        First displacement increment considered during the analysis.
        By default 0.001.

    Return
    ------
    ctrl_disp : list[float]
        Displacement values of control node.
    base_shear : list[float]
        Base shear value obtained as sum of the reaction forces.
    """
    # Set output directory
    output_directory = Path(__file__).parent / 'NSPA-Results'
    if not Path.exists(output_directory):
        Path.mkdir(output_directory)
    reaction_file_path = (output_directory / 'support_reactions_x.out').as_posix()
    disp_file_path = (output_directory / 'storey_displacements_x.out').as_posix()
    storey_heights_file_path = (output_directory / 'storey_heights.out').as_posix()

    # Build the numerical model
    build_model()

    # Add NSPA time-series and load pattern to ops domain
    ops.timeSeries('Linear', 2)
    ops.pattern('Plain', 2, 2)
    # Add lateral nspa loads to ops domain
    ops.load(91000, 0.08482564604055667, 0, 0, 0, 0, 0)
    ops.load(92000, 0.2061352861498299, 0, 0, 0, 0, 0)
    ops.load(93000, 0.3638100049443609, 0, 0, 0, 0, 0)
    ops.load(94000, 0.3452290628652525, 0, 0, 0, 0, 0)

    # Set the recorders
    ctrl_node = 94000  # Control node
    ctrl_dof = 1  # Control dof
    supports = [70001, 70007, 70013, 70019, 70002, 70008, 70014, 70020, 70003, 70009, 70015, 70021, 70004, 70010, 70016, 70022, 70005, 70011, 70017, 70023, 70006, 70012, 70018, 70024]  # Foundation nodes
    floors = [91000, 92000, 93000, 94000]  # Retained floor nodes
    ops.recorder('Node', '-file', disp_file_path, '-node', *floors, '-dof', ctrl_dof, 'disp')
    ops.recorder('Node', '-file', reaction_file_path, '-node', *supports, '-dof', ctrl_dof, 'reaction')

    # Base level coordinate
    base_level = min([ops.nodeCoord(node, 3) for node in supports])
    # Save storey heights
    with open(storey_heights_file_path, 'w') as file:
        for node in floors:
            file.write(f'{ops.nodeCoord(node, 3) - base_level}\n')

    # Set some analysis parameters
    max_disp = max_drift * (ops.nodeCoord(ctrl_node, 3) - base_level)
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
    base_shear = [0]
    ctrl_disp = [0]
    ok = 0
    cont = True
    while ok == 0 and cont:
        ops.test('NormDispIncr', tol_init, iter_init)
        ops.integrator('DisplacementControl', ctrl_node, ctrl_dof, dincr)
        ops.algorithm('Newton', '-initialThenCurrent')
        ok = ops.analyze(1)
        if ok != 0:  # try other algorithms
            ok = _set_algorithm(ok, tol_init)
        if ok != 0:  # reduce dincr to an half
            ops.integrator('DisplacementControl', ctrl_node, ctrl_dof, 0.5*dincr)
            ok = _set_algorithm(ok, tol_init)
        if ok != 0:  # reduce dincr to a quarter
            ops.integrator('DisplacementControl', ctrl_node, ctrl_dof, 0.25*dincr)
            ok = _set_algorithm(ok, tol_init)
        if ok != 0:  # increase tolerance by factor of 10
            ok = _set_algorithm(ok, 10*tol_init)
        if ok != 0:  # increase tolerance by factor of 100
            ok = _set_algorithm(ok, 100*tol_init)

        # Get the base shear force
        ops.reactions()
        current_disp = ops.nodeDisp(ctrl_node, ctrl_dof)
        current_shear = abs(sum([ops.nodeReaction(node, ctrl_dof) for node in supports]))
        # Set continue flag
        cont = current_disp < max_disp and current_shear < 50000 and current_shear >= 0.2*max(base_shear)
        # Append base shear and control node displacement
        if ok == 0 and cont:
            base_shear.append(current_shear)
            ctrl_disp.append(current_disp)

    # Wipe the model
    ops.wipe()
    # Return base shear and control node displacement history
    return ctrl_disp, base_shear


def do_nspa_y(max_drift: float = 0.1, dincr: float = 0.001) -> tuple[list[float], list[float]]:
    """Performs nonlinear static pushover analysis (NSPA) in y direction.

    Parameters
    ----------
    max_drift : float, optional.
        Maximum considered drift value for the control node.
        By default 0.1
    dincr : float, optional.
        First displacement increment considered during the analysis.
        By default 0.001.

    Return
    ------
    ctrl_disp : list[float]
        Displacement values of control node.
    base_shear : list[float]
        Base shear value obtained as sum of the reaction forces.
    """
    # Set output directory
    output_directory = Path(__file__).parent / 'NSPA-Results'
    if not Path.exists(output_directory):
        Path.mkdir(output_directory)
    reaction_file_path = (output_directory / 'support_reactions_y.out').as_posix()
    disp_file_path = (output_directory / 'storey_displacements_y.out').as_posix()
    storey_heights_file_path = (output_directory / 'storey_heights.out').as_posix()

    # Build the numerical model
    build_model()

    # Add NSPA time-series and load pattern to ops domain
    ops.timeSeries('Linear', 2)
    ops.pattern('Plain', 2, 2)
    # Add lateral nspa loads to ops domain
    ops.load(91000, 0, 0.0946240161898906, 0, 0, 0, 0)
    ops.load(92000, 0, 0.22343819244170032, 0, 0, 0, 0)
    ops.load(93000, 0, 0.3607018940005991, 0, 0, 0, 0)
    ops.load(94000, 0, 0.32123589736780983, 0, 0, 0, 0)

    # Set the recorders
    ctrl_node = 94000  # Control node
    ctrl_dof = 2  # Control dof
    supports = [70001, 70007, 70013, 70019, 70002, 70008, 70014, 70020, 70003, 70009, 70015, 70021, 70004, 70010, 70016, 70022, 70005, 70011, 70017, 70023, 70006, 70012, 70018, 70024]  # Foundation nodes
    floors = [91000, 92000, 93000, 94000]  # Retained floor nodes
    ops.recorder('Node', '-file', disp_file_path, '-node', *floors, '-dof', ctrl_dof, 'disp')
    ops.recorder('Node', '-file', reaction_file_path, '-node', *supports, '-dof', ctrl_dof, 'reaction')

    # Base level coordinate
    base_level = min([ops.nodeCoord(node, 3) for node in supports])
    # Save storey heights
    with open(storey_heights_file_path, 'w') as file:
        for node in floors:
            file.write(f'{ops.nodeCoord(node, 3) - base_level}\n')

    # Set some analysis parameters
    max_disp = max_drift * (ops.nodeCoord(ctrl_node, 3) - base_level)
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
    base_shear = [0]
    ctrl_disp = [0]
    ok = 0
    cont = True
    while ok == 0 and cont:
        ops.test('NormDispIncr', tol_init, iter_init)
        ops.integrator('DisplacementControl', ctrl_node, ctrl_dof, dincr)
        ops.algorithm('Newton', '-initialThenCurrent')
        ok = ops.analyze(1)
        if ok != 0:  # try other algorithms
            ok = _set_algorithm(ok, tol_init)
        if ok != 0:  # reduce dincr to an half
            ops.integrator('DisplacementControl', ctrl_node, ctrl_dof, 0.5*dincr)
            ok = _set_algorithm(ok, tol_init)
        if ok != 0:  # reduce dincr to a quarter
            ops.integrator('DisplacementControl', ctrl_node, ctrl_dof, 0.25*dincr)
            ok = _set_algorithm(ok, tol_init)
        if ok != 0:  # increase tolerance by factor of 10
            ok = _set_algorithm(ok, 10*tol_init)
        if ok != 0:  # increase tolerance by factor of 100
            ok = _set_algorithm(ok, 100*tol_init)

        # Get the base shear force
        ops.reactions()
        current_disp = ops.nodeDisp(ctrl_node, ctrl_dof)
        current_shear = abs(sum([ops.nodeReaction(node, ctrl_dof) for node in supports]))
        # Set continue flag
        cont = current_disp < max_disp and current_shear < 50000 and current_shear >= 0.2*max(base_shear)
        # Append base shear and control node displacement
        if ok == 0 and cont:
            base_shear.append(current_shear)
            ctrl_disp.append(current_disp)

    # Wipe the model
    ops.wipe()
    # Return base shear and control node displacement history
    return ctrl_disp, base_shear
