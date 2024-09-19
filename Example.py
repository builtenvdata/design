from src import rcmrf
from test import Tester
from time import time
from src.utils import run_time

if __name__ == '__main__':
    start_time = time()
    # Initialize the framework engine for the RC-MRF buildings in specified region
    buildings = rcmrf.Engine(region='EU', output_directory='Outputs')

    # Generate taxonomy based on user-defined input
    buildings.generate_bcim(PSS1=0.5, PSS2=0.65, PWBa=0.5, Psquared=0.5, PQLow=0.1, PQModer=0.3, PQHigh=0.6, Nsimul=10,
                            DesignClass='CDL', Beta=0.15, Bcolfix=0.3, Bbeamfix_X=0.3, Bbeamfix_Y=0.3, Hstairs=0.15,
                            ppinfill=0.7, NStoreys=5)

    # Simulate building designs
    buildings.generate_bim(save='yes')

    # Generate numerical models
    buildings.generate_fim(save_model='python')

    # Test
    test = Tester()
    test.test_rcmrf_eu_bcim()
    test.test_rcmrf_eu_bim()

    run_time(start_time)
