from src import rcmrf
from time import time
from src.utils import run_time
import os
import pandas as pd
from pathlib import Path


if __name__ == '__main__':
    start_time = time()
    # Initialize the framework engine for the RC-MRF buildings in specified region
    buildings = rcmrf.Engine(region='EU', output_directory='python-openseestcl')

    # Generate taxonomy based on user-defined input
    path = Path(__file__).parent / "test"
    test_input_filename = path / 'rcmrf' / 'eu' / 'test_bcim.csv'
    test_dict = pd.read_csv(test_input_filename).to_dict('list')
    buildings.generate_bcim_test(test_dict)

    # Simulate building designs
    buildings.generate_bim()

    # Generate numerical models
    buildings.generate_fim(save_model='tcl')

    # Run models
    cwd = os.getcwd()
    for i in range(1, 181):
        os.chdir(buildings.output_directory / f"Building_{i}" / "Numerical_Model")
        path_x = "GoX.tcl"
        path_y = "GoY.tcl"
        os.system(f'opensees.exe {path_x}')
        os.system(f'opensees.exe {path_y}')
        os.chdir(cwd)

    run_time(start_time)
