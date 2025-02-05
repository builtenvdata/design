import openseespy.opensees as ops

from .foundations import add_foundations
from .floors import add_floors
from .joints import add_joints
from .beams import add_beams
from .columns import add_columns
from .gravity import do_gravity


def build_model() -> None:
    """Adds the numerical model to the OpenSees domain.
    """
    ops.wipe()
    ops.model('basic', '-ndm', 3, '-ndf', 6)

    # Geometric transformations
    ops.geomTransf('Linear', 88888, 0, -1, 0)
    ops.geomTransf('Linear', 77777, 1, 0, 0)
    ops.geomTransf('Linear', 99999, -1, 0, 0)
    ops.geomTransf('PDelta', 66666, -1, 0, 0)

    # Rigid-like material and section
    ops.uniaxialMaterial('Elastic', 99999, 1000000000.0)
    ops.section('Aggregator', 99999, 99999, 'P', 99999, 'Vy',  99999, 'Vz', 99999, 'My', 99999, 'Mz', 99999, 'T')

    # Define components of foundations
    add_foundations()
    # Define components of floors
    add_floors()
    # Define components of joints
    add_joints()
    # Define components of beams
    add_beams()
    # Define components of columns
    add_columns()
    # Perform static analysis under gravity loads
    do_gravity()
