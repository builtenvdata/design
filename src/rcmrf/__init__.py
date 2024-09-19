"""The framework engine for RC buildings with MRF systems
"""

from pathlib import Path
import pandas as pd
import shutil

import src.rcmrf.eu as eu
# import src.rcmrf.it as it
# import src.rcmrf.tr as tr
# import src.rcmrf.pt as pt
from src.rcmrf.fim import FragilityInformationModel
from src.utils import make_dir, check_parameters


class Engine:

    AVAILABLE_REGIONS = ('EU') # Extend this as upon adding BCIM and BIM modules for other regions
    REQUIRED_PARAMETERS_EU = ('PSS1', 'PSS2', 'PWBa', 'Psquared', 'PQLow', 'PQModer', 'PQHigh', 'Nsimul', 'DesignClass', 'Beta', 'Bcolfix', 'Bbeamfix_X', 'Bbeamfix_Y', 'Hstairs', 'ppinfill', 'NStoreys')

    def __init__(self, region:str, output_directory:str):
        """_summary_

        Args:
            region (str): design region or country

        Raises:
            ValueError: If the country is not listed in AVAILABLE_REGIONS
        """
        # Make a clean output directory if it does not exist
        self.output_directory = Path(output_directory)
        make_dir(self.output_directory)
        # if not Path.exists(self.output_directory):

        if region in self.AVAILABLE_REGIONS:
            self.bcim = None
            self.bim = None
            self.parameters = None
            self.region = region.upper()

        else:
            raise ValueError('Invalid Country.')

    def generate_bcim_test(self, test_dict):
        self.bcim = eu.generate_bcim(test_taxonomy=test_dict)

    def generate_bcim(self, **parameters):
        """Generates building class information model

        Args:
            **parameters :
                PSS1 (float) : ratio of buildings that have one-way solid slabs when the span is less than 6 m
                PSS2 (float) : ratio of buildings that have two-way solid slabs
                PWBa (float) : ratio of buildings that have wide beams for slab type 3
                Psquared (float) : ratio of buildings that have square columns
                PQLow (float) : ratio of buildings that have low quality
                PQModer (float) :  ratio of buildings that have moderate quality
                PQHigh (float) : ratio of buildings that have high quality
                Nsimul (int) : number of buildings to be designed
                DesignClass (string) : design class selected for the design load factor (CDN, CDL, CDM, CDH)
                Beta (float) : lateral load factor (0.0 to 0.35)
                Bcolfix (float) : minimum dimension of the column width or depth
                Bbeamfix_X (float) : minimum width of the beams in the X direction
                Bbeamfix_Y (float) : minimum width of the beams in the Y direction
                Hstairs (float) : depth of the slabs of the staircase
                ppinfill (float) : linear load corresponding to the weight of the infills
                NStoreys (int) : number of storey
                    
        Raises:
            ValueError: If any of the required simulation parameters is not provided.
        """

        if self.region == 'EU': # for Europe
            check_parameters(parameters, self.REQUIRED_PARAMETERS_EU) # Check entries
            self.bcim = eu.generate_bcim(parameters)
        # elif self.region == 'IT': # for Italy
        #     self.taxonomy = it.get_building_taxonomy(parameters)
        # elif self.region == 'PT': # for Portugal
        #     self.taxonomy = pt.get_building_taxonomy(parameters)
        # elif self.region == 'TR': # for Türkiye
        #     self.taxonomy = tr.get_building_taxonomy(parameters)

        self.parameters = parameters

    def generate_bim(self, save:str=None):
        """Simulate designs for the generated portfolio based on the design region
        """

        if self.region == 'EU': # for Europe
            self.bcim, self.bim = eu.generate_bim(taxonomy=self.bcim)     
        # elif self.region == 'IT': # for Italy
        #     self.taxonomy, self.design = it.get_simulated_designs(taxonomy=self.taxonomy)     
        # elif self.region == 'PT': # for Portugal
        #     self.taxonomy, self.design = pt.get_simulated_designs(taxonomy=self.taxonomy)     
        # elif self.region == 'TR': # for Türkiye
        #     self.taxonomy, self.design = tr.get_simulated_designs(taxonomy=self.taxonomy)     

        if save:

            bcim_file = self.output_directory / "Building_Class_Information.csv"
            df = pd.DataFrame(self.bcim.__dict__)
            df.to_csv(bcim_file, index=False)
            info_file_src = ((Path(__file__).parent).parent).parent / 'static' / 'layouts_and_variables.xlsx'
            info_file_dst = self.output_directory / 'layouts_and_variables.xlsx'
            shutil.copy(info_file_src, info_file_dst)

            for i in range(len(self.bcim.NStoreys)):

                if self.bim[i].final_design:
                    building_folder = self.output_directory / f"Building_{i+1:d}"
                    bim_folder = building_folder / f"Building_Information"

                    make_dir(bim_folder)
                    for key in ['beamX', 'beamY', 'beamStair', 'column']:
                        file_path = bim_folder / (key+'.csv')
                        df = pd.DataFrame(self.bim[i].final_design[key])
                        df.to_csv(file_path, index=False)

    def generate_fim(self, save_model:str=None, modelling_settings:dict=None, do_nspa:str=None, num_eigen:int=None):

        for i in range(len(self.bcim.NStoreys)):

            if self.bim[i].final_design:
                building_folder = self.output_directory / f"Building_{i+1:d}"
                results_folder = building_folder / f"Analysis_Results"
                model_folder = building_folder / f"Numerical_Model"
                model = FragilityInformationModel(self.bim[i].final_design, modelling_settings)

                # Save model files
                if save_model:
                    make_dir(model_folder)
                    writable = model.get_writable(save_model)
                    for key, item in writable.items():
                        with open(model_folder / key, 'w') as file:
                            file.write(item)

                # Run analysis and save results
                if num_eigen or do_nspa:
                    make_dir(results_folder)
                    if num_eigen:
                        model.do_modal(results_folder, num_eigen)
                    if do_nspa:
                        model.do_nspa(results_folder, 'X')
                        model.do_nspa(results_folder, 'Y')
