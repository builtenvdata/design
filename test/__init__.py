"""
Testing
"""

import src.rcmrf as rcmrf
# import src.rcdual as rcdual
# import src.rcwall as rcwall
from pathlib import Path
import pandas as pd
import pickle
import numpy as np

class Tester:

    def __init__(self):
        self.path = Path(__file__).resolve().parent

    def test_rcmrf_eu_bcim(self):
        # For error computations see: https://numpy.org/doc/stable/reference/generated/numpy.isclose.html#numpy.isclose
        rtol = 1e-5 # The relative tolerance parameter
        atol = 1e-8 # The absolute tolerance parameter

        # Get designs for test taxonomy
        control_filename = self.path / 'rcmrf' / 'eu' / 'expected_bcim.pkl'
        with open(control_filename, 'rb') as file:
            control_taxonomies = pickle.load(file)
        test_input_filename = self.path / 'rcmrf' / 'eu' / 'test_parameters.csv'
        test_parameters = pd.read_csv(test_input_filename).to_dict('index')
        number_of_tests = len(test_parameters.keys())
        test_log = []
        test_flag = 0

        for i in range(number_of_tests):
            flag = 0
            simulated_taxonomy = rcmrf.eu.generate_bcim(parameters=test_parameters[i])
            simulated_taxonomy = pd.DataFrame(simulated_taxonomy.__dict__)
            simulated_taxonomy = simulated_taxonomy.reindex(sorted(simulated_taxonomy.columns), axis=1)
            expected_taxonomy = control_taxonomies[i]
            expected_taxonomy = expected_taxonomy.reindex(sorted(expected_taxonomy.columns), axis=1)
            # Check string arguments
            mask1 = expected_taxonomy['DesignClass'] == simulated_taxonomy['DesignClass']
            if np.all(mask1) == False:
                test_log.append(['DesignClass', np.where(~mask1)])
                print(f'failed to pass the test for design {i} - check DesignClass')
                flag = 1

            mask2 = expected_taxonomy['Layout'] == simulated_taxonomy['Layout']
            if np.all(mask2) == False:
                test_log.append(['Layout', np.where(~mask2)])
                print(f'failed to pass the test for design {i} - check Layout')
                flag = 1

            # Check values
            simulated_taxonomy = simulated_taxonomy.drop(columns=['DesignClass', 'Layout'])
            expected_taxonomy = expected_taxonomy.drop(columns=['DesignClass', 'Layout'])
            mask3 = np.isclose(simulated_taxonomy.to_numpy(), expected_taxonomy.to_numpy(), rtol=rtol, atol=atol, equal_nan=True)
            if np.all(mask3) == False:
                test_log.append(['values', np.where(~mask3)])
                print(f'BCIM module failed to pass the test for simulation {i} - check values {simulated_taxonomy.columns[np.unique(np.where(~mask3)[1])]}')
                flag = 1

            test_flag += flag

        print('------------------------------------')
        if test_flag == 0:
            print('BCIM module passed the test!')
        else:
            print(f'BCIM module failed to pass the test for {test_flag} simulations!')
            with open('test_log_bcim.pkl', 'wb') as file:
                pickle.dump(test_log, file)
        print('------------------------------------')

    def test_rcmrf_eu_bim(self):
        # For error computations see: https://numpy.org/doc/stable/reference/generated/numpy.isclose.html#numpy.isclose
        rtol = 1e-4 # The relative tolerance parameter
        atol = 1e-8 # The absolute tolerance parameter

        # Get designs for test taxonomy
        control_filename = self.path / 'rcmrf' / 'eu' / 'expected_bim.pkl'
        with open(control_filename, 'rb') as file:
            control_designs = pickle.load(file)
        test_input_filename = self.path / 'rcmrf' / 'eu' / 'test_bcim.csv'
        test_dict = pd.read_csv(test_input_filename).to_dict('list')
        taxonomy = rcmrf.eu.generate_bcim(test_taxonomy=test_dict)
        taxonomy, test_designs = rcmrf.eu.generate_bim(taxonomy)

        # Start performing the closeness tests for designs
        components = ['beamX', 'beamY', 'beamStair', 'column']
        test_log = {}
        test_flag = 0
        for i, design in enumerate(test_designs):
            flag = 0
            test_log[i] = {}
            # Check design solutions
            for comp in components:
                test_log[i][comp] = None
                expected_design = control_designs[i]['final_design'][comp].to_numpy()
                simulated_design = pd.DataFrame(design.final_design[comp]).to_numpy()
                mask = np.isclose(expected_design, simulated_design, rtol=rtol, atol=atol, equal_nan=True)

                if np.all(mask) == False:
                    test_log[i][comp] = np.where(~mask)
                    print(f'BIM module failed to pass the test for design {i} - {comp}')
                    flag = 1

            # Check general
            expected_general=control_designs[i]['general']
            simulated_general = test_designs[i].general.__dict__
            for key in expected_general.keys():
                if key in simulated_general.keys():
                    if key not in ['BuildingTYPE', 'designlevel']:
                        bool = np.all(np.isclose(expected_general[key], simulated_general[key], rtol=rtol, atol=atol, equal_nan=True))
                    else:
                        bool = expected_general[key] == simulated_general[key]
                    if not bool:
                        print(f'BIM module failed to pass the test for design {i} - general: {key}')
                        flag = 1                        

            # Check joint
            expected_joint = control_designs[i]['joint']
            simulated_joint = test_designs[i].joint.__dict__
            for key in expected_joint.keys():
                if key in simulated_joint.keys():
                    bool = np.allclose(expected_joint[key], simulated_joint[key], rtol=rtol, atol=atol, equal_nan=True)
                    if not bool:
                        print(f'BIM module failed to pass the test for design {i} - joint: {key}')
                        flag = 1     

            test_flag += flag

        print('------------------------------------')
        if test_flag == 0:
            print('BIM module passed the test!')
        else:
            print(f'BIM module failed to pass the test for {test_flag} designs!')
            with open('test_log_bim.pkl', 'wb') as file:
                pickle.dump(test_log, file)
        print('------------------------------------')

