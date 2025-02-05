import openseespy.opensees as ops
from pathlib import Path

from .model import build_model


def do_modal(num_modes: int = 3) -> dict:
    """Perform modal analysis for built OpenSees model.

    Parameters
    ----------
    num_modes : int, optional
        Number of modes considered for modal analysis.
        By default 3.

    Return
    ------
    dict
        Dictionary containing modal properties.
    """
    # Set output directory
    output_directory = Path(__file__).parent / 'Modal-Results'
    if not Path.exists(output_directory):
        Path.mkdir(output_directory)
    # Build the numerical model
    build_model()

    # Perform eigen value analysis
    ops.eigen(num_modes)
    # Save eigen vectors for retained floor nodes
    nodes = [91000, 92000, 93000, 94000]
    for i in range(1, num_modes+1):
        modal_disps = []
        for node in nodes:
            disps = ', '.join([f'{disp}' for disp in ops.nodeEigenvector(node, i)])
            modal_disps.append(f'{node}, {disps}')
        modal_disps = '\n'.join(modal_disps)
        report_file_path = (output_directory / f'EigenVectors_Mode{i}.txt').as_posix()
        with open(report_file_path, 'w') as file:
            file.write(modal_disps)

    # Perform modal analysis and save results
    report_file_path = (output_directory / 'ModalProperties.txt').as_posix()
    results = ops.modalProperties('-print', '-return', '-file', report_file_path, '-unorm')

    return results
