from src import rcmrf
from time import time
from src.utils import run_time
import os
import pandas as pd
from pathlib import Path


if __name__ == '__main__':
    start_time = time()
    # Initialize the framework engine for the RC-MRF buildings in specified region
    buildings = rcmrf.Engine(region='EU', output_directory='python-openseespy')

    # Generate taxonomy based on user-defined input
    path = Path(__file__).parent / "test"
    test_input_filename = path / 'rcmrf' / 'eu' / 'test_bcim.csv'
    test_dict = pd.read_csv(test_input_filename).to_dict('list')
    buildings.generate_bcim_test(test_dict)

    # Simulate building designs
    buildings.generate_bim()

    # Generate numerical models
    buildings.generate_fim(save_model='python')

    # Run models
    for i in range(1, 181):
        file_x = buildings.output_directory / f"Building_{i}" / "Numerical_Model" / "run_push_x.py"
        path_x = file_x.as_posix()
        file_y = buildings.output_directory / f"Building_{i}" / "Numerical_Model" / "run_push_y.py"
        path_y = file_y.as_posix()
        file_modal = buildings.output_directory / f"Building_{i}" / "Numerical_Model" / "run_modal.py"
        path_modal = file_modal.as_posix()
        os.system(f'python {path_modal}')
        os.system(f'python {path_x}')
        os.system(f'python {path_y}')

    run_time(start_time)
