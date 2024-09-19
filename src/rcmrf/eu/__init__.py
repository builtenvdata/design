from src.rcmrf.eu.bcim import BuildingClassInformationModel
from src.rcmrf.eu.bim import BuildingInformationModel

def generate_bcim(parameters:dict=None, test_taxonomy:dict=None):
    # Generate building portfolio
    taxonomy = BuildingClassInformationModel()
    if parameters:
        taxonomy.generate_new(parameters)
    elif test_taxonomy:
        taxonomy.adapt_for_test(test_taxonomy)
    else:
        raise ValueError('Entries are not valied.')
    
    return taxonomy


def generate_bim(taxonomy:BuildingClassInformationModel):

    design = []
    # Simulate the designs of buildings
    for i in range(len(taxonomy.NStoreys)):
        taxonomy_i = {attribute: value[i] if isinstance(value[i], str) else round(value[i], 6) for attribute, value in taxonomy.__dict__.items()}
        # Initalise the ith building
        building_i = BuildingInformationModel()
        # Do the layout calculations given ith taxonomy
        building_i.make_layout(taxonomy_i)
        # Make the pre-design of the ith building
        building_i.make_predesign()
        # Make the final design of the ith building
        building_i.make_final_design()
        # If design solution is reached update taxonomy:
        if building_i.final_design:
            taxonomy.beamtype[i] = building_i.general.BeamType + 0
            taxonomy.fck[i] = building_i.general.fck + 0
            taxonomy.fcd[i] = building_i.general.fcd + 0
            taxonomy.fcd_EQ[i] = building_i.general.fcdEQ + 0
            taxonomy.fsyd[i] = building_i.general.fsyd + 0
            taxonomy.fsyk[i] = building_i.general.fsyk + 0
            print('------------------------------------')
            print(f'Design of building {i+1} was COMPLETED for beta = {100*building_i.general.ag:4.2f}!')
            print('------------------------------------')
        else:
            print('------------------------------------')
            print(f'Design of building {i+1} was TERMINATED for beta = {100*building_i.general.ag:4.2f}!')
            print('------------------------------------')
        # Append the design
        design.append(building_i)

    return taxonomy, design
