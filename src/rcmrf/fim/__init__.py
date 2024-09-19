from src.rcmrf.fim import generators

class FragilityInformationModel(generators.OpsModel):

    def __init__(self, design:dict, modelling_settings:dict=None):
        """Builds numerical model for the given design in OpenSeesPy

        Args:
            design (_type_): dictionary containing necessary design information for generating numerical models
            settings (_type_): modeling settings
        """
        self.py_files = {} # Populate this dictionary with file names and coresponding string inputs
        self.tcl_files = {} # Populate this dictionary with file names and coresponding string inputs
        self.beamX = design['beamX']
        self.beamY = design['beamY']
        self.beamStair = design['beamStair']
        self.column = design['column']
        self.general = design['general']
        self.joint = design['joint']

        if modelling_settings:
            # TODO: discuss these options with Hossam and Xavier
            self.infill = modelling_settings['infill'] # Included or not ("yes", "no")
            self.plasticity = modelling_settings['plasticity'] # plasticity along the element ("concentrated", "distributed")
            self.hinge = modelling_settings['hinge'] # modelling of plastic hinge section ("uniaxial", "fibre") 
        else:
            self.infill = 'no'
            self.plasticity = 'concentrated'
            self.hinge = 'uniaxial'

    def get_writable(self, scripting_language:str):
        """ 
        Save opensees models for the selected scripting language
        """
        if scripting_language.lower() == 'tcl': # save OpenSees model for tcl
            generator = generators.TclGenerator()

        elif scripting_language.lower() == 'python':
            generator = generators.PyGenerator() # save OpenSees model for python         
        else:
            raise ValueError(f'Invalid scripting language: {scripting_language}')

        generator.compile_opensees_model(self.general, self.joint, self.column, self.beamX, self.beamStair, self.beamY)
        writable = generator.get_writable_opensees_model()

        return writable
