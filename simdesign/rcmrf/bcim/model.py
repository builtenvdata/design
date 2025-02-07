"""
Building Class Information Model (BCIM) and its main components.

The current implementation is limited to the generation of building portfolio
with fixed floor layouts and single staircase throughout buildings.
"""

# Imports from installed packages
import json
import pandas as pd
from pathlib import Path
from typing import Dict, List, Literal, Optional, Union

# Imports from bcim library
from .parametrization import ArchetypeData, InputData
from .randomization import Sampler

# Imports from bdim common library
from ..bdim.baselib.building import TaxonomyData

# Imports from geometry library
from ..geometry import StandardFrame


class Archetypes:
    """Controls the building archetypes data loaded from layouts file.

    Attributes
    ----------
    available_tags : List[ArchetypeData]
        List of available archetype tags.
    file_path : Path
        Path to the CSV file containing archetype data.
    all_data : List[ArchetypeData]
        List containing all archetype data loaded from the CSV file.

    Methods
    -------
    get_data_for_given_tag
        Retrieves archetype data for the given tag.
    get_data_for_given_tags
        Retrieves archetype data for the given list of tags.
    get_geometry
        Retrieves the geometry of a building archetype specified by the given
        tag.
    """
    available_tags: List[ArchetypeData]
    """List of available archetype tags."""
    file_path: Path = Path(__file__).parent / 'data' / 'layouts.csv'
    """Path to the CSV file containing archetype data."""
    all_data: List[ArchetypeData]
    """List containing all archetype data loaded from the CSV file."""

    def __init__(self) -> None:
        """
        Initialize the Archetype instance by loading data from the CSV file.
        """
        csv_data = pd.read_csv(self.file_path)
        self.all_data = []
        for _, row in csv_data.iterrows():
            self.all_data.append(ArchetypeData(**row.to_dict()))

    @property
    def available_tags(self) -> List[ArchetypeData]:
        """
        Returns
        -------
        List[ArchetypeData]
            List of available archetype tags.
        """
        return [archetype.tag for archetype in self.all_data]

    def get_data_for_given_tag(self, tag: str) -> Optional[ArchetypeData]:
        """
        Retrieves archetype (floor layout) data for the given tag.

        Parameters
        ----------
        tag : str
            The tag of the archetype (floor layout) for which data is
            requested.

        Returns
        -------
        ArchetypeData | None
            Archetype data (floor layout) if found, None otherwise.
        """
        if tag in self.available_tags:
            index = self.available_tags.index(tag)
            return self.all_data[index]

    def get_data_for_given_tags(
        self, tags: List[str]
    ) -> Optional[List[ArchetypeData]]:
        """
        Retrieves archetype data for the given list of tags.

        Parameters
        ----------
        tags : List[str]
            The list of tags for which archetype (floor layout) data is
            requested.

        Returns
        -------
        List[ArchetypeData] | None
            List of archetype data for the requested tags.
        """
        data_list = []
        for tag in tags:
            data = self.get_data_for_given_tag(tag)
            if data:
                data_list.append(data)
        # Return data for requested archetypes
        if any(data_list):
            return data_list

    def get_geometry(
        self, tag: str, num_storeys: int, storey_height: float,
        ground_storey_height: float, bay_width_x: float,
        bay_width_y: float, stairs_width_x: float
    ) -> StandardFrame:
        """Retrieves the geometry of a building archetype specified by the
        given tag.

        Parameters
        ----------
        tag : str
            The tag of the archetype (layout) for which geometry is requested.
        num_storeys : int
            Number of storeys in the building.
        storey_height : float
            Height of each storey.
        ground_storey_height : float
            Height of the ground storey.
        bay_width_x : float
            Width of the bays along the x-axis.
        bay_width_y : float
            Width of the bays along the y-axis.
        stairs_width_x : float
            Width of the stairs along the x-axis.

        Returns
        -------
        StandardFrame
            StandardFrame object representing the geometry of the building
            archetype.
        """
        data = self.get_data_for_given_tag(tag)
        # Grid ID of left bottom point (or bay ID in x and y)
        stair_loc = (data.stairs_grid_x, data.stairs_grid_y)
        # Initialise the frame object
        regular_frame = StandardFrame(
            num_storeys, storey_height, data.num_bays_x, bay_width_x,
            data.num_bays_y, bay_width_y, tag)
        # Set stairs location
        regular_frame.set_continuous_stairs_rectangles(
            stair_loc, stairs_width_x)
        # Modifying a floor height (ground floors are usually modified)
        ground_storey_id = 1
        regular_frame.modify_floor_height(ground_storey_id,
                                          ground_storey_height)
        # Add the new lines and points for stairs (For now do this in the end)
        regular_frame.add_new_lines_and_points_for_stairs()

        return regular_frame


class DefaultInputs:
    """Loads and manages the default input data from json files.

    The data include the statistical distribution parameters required
    to perform random sampling, the parameters required to define building
    geometries per realization (e.g., num_storeys) and those required to
    perform simulated designs (e.g., beta).

    Attributes
    ----------
    available_classes : List[str]
        List of available design classes.
    defaults : Dict[str, ParametersData]
        Private attribute representing data from all JSON files.
    data_path : Path
        Private attribute representing the path to the folder containing JSON
        files of the parameters.

    Methods
    -------
    get
        Returns the parameters data for the specified design_class.
    available_classes
        Returns the available design classes.
    """
    available_classes: List[str]
    """List of available design classes."""
    defaults: Dict[str, InputData]
    """Private attribute representing data from all JSON files."""
    data_path: Path = Path(__file__).parent / 'data'
    """Private attribute representing the path to the folder containing JSON
    files of the parameters."""

    def __init__(self):
        """Initialise parameters object.

        It loads all the JSON data as default parameters which can be
        retrieved.
        """
        json_files = list(self.data_path.glob('*.json'))
        self.defaults = {}
        for file in json_files:
            with open(file, 'r') as json_file:
                # Load the JSON data into a Python dictionary
                data = json.load(json_file)
                # Initiate the InputData object and store with its filename
                self.defaults[file.name] = InputData(**data)

    def get(self, design_class: str) -> InputData:
        """Returns the parameters data for the specified design_class.

        Parameters
        ----------
        design_class : str
            The design class for which the parameters will be returned.

        Returns
        -------
        ParametersData
            The parameters defined for the specified design_class.
        """
        index = self.available_classes.index(design_class)
        filename = list(self.defaults.keys())[index]
        return self.defaults[filename]

    @property
    def available_classes(self) -> List[str]:
        """
        Returns
        -------
        List[str]
            List of available design classes.
        """
        return [item.design_class for _, item in self.defaults.items()]


class BCIM:
    """This is the main class used to generate and process BCIM data.

    Attributes
    ----------
    inputs : InputData
        Input parameters used for BCIM data generation.
    __defaults: DefaultInputs
        DefaultInputs instance managing the parameters from json files.
    __archetypes: Archetypes
        An Archetypes instance processing layout data to generate frame mesh.
    staircase_span_length_x: List[float]
        Staircase span length in x direction.
    staircase_span_length_y: List[float]
        Staircase span length in y direction.
    typical_span_length_x: List[float]
        Typical span length in x direction.
    typical_span_length_y: List[float]
        Typical span length in y direction.
    layout: List[str]
        Building floor layouts.
    typical_storey_height: List[float]
        Typical storey height.
    ground_storey_height: List[float]
        Ground storey height.
    slab_type: List[float]
        Slab type.
        1: Two-way solid slab (SS2).
        2: One-way solid slab (SS1).
        3: Composite slabs with pre-fabricated joists and ceramic blocks (HS).
    beam_type: List[Literal[1, 2]]
        Beam typology
        1: Wide beams.
        2: Emergent beams.
    column_section: List[Literal[1, 2]]
        Column cross-section
        1: Square solid section.
        2: Rectangular solid section.
    steel_mat_class: List[str]
        Steel material class ID, or grade, e.g., 'S400'.
    concrete_mat_class: List[str]
        Concrete material class ID, or grade, e.g., 'C20'.
    quality: List[Literal[1, 2, 3]]
        Construction quality
        1: High quality.
        2: Moderate quality.
        3: Low quality.
    building_geometry: List[StandardFrame]
        List of building geometry instances.
    floor_width_x: List[float]
        Total floor width in x direction in floor layout.
    floor_width_y: List[float]
        Total floor width in y direction in floor layout.
    floor_area: List[float]
        Total floor area in floor layout.
    long_over_short_width: List[float]
        Ratio of longer to shorter floor widths in floor layout.
    beta: List[float]
        Design lateral load factor.
    num_storeys: List[int]
        Number of storeys.
    design_class: List[float]
        Building design class selected.

    Properties
    ----------
    available_design_classes : List[str]
        Available design classes to use.
    available_archetypes : List[str]
        Available building archetypes (layouts) to use.
    taxonomy : List[Taxonomy]
        Taxonomy information required for simulated-design.

    Methods
    -------
    configure
        Configure BCIM with sample size, design class, seed, and additional
        parameters.
    generate
        Generate BCIM data based on configured parameters.
    to_csv
        Saves the generated BCIM data into the specified .csv file path.

    TODO
    ----
    Visualize available layouts.
    """
    inputs: InputData
    """Input parameters used for BCIM data generation."""
    __defaults: DefaultInputs
    """DefaultInputs instance managing the parameters from json files."""
    __archetypes: Archetypes
    """An Archetypes instance processing layout data to generate frame mesh."""
    staircase_span_length_x: List[float]
    """Staircase span length in x direction."""
    staircase_span_length_y: List[float]
    """Staircase span length in y direction."""
    typical_span_length_x: List[float]
    """Typical span length in x direction."""
    typical_span_length_y: List[float]
    """Typical span length in y direction."""
    layout: List[str]
    """Building floor layouts."""
    typical_storey_height: List[float]
    """Typical storey height."""
    ground_storey_height: List[float]
    """Ground storey height."""
    slab_thickness: List[float | None]
    """Slab thickness."""
    slab_type: List[Literal[1, 2, 3]]
    """Slab typology
    1: Two-way solid slab (SS2).
    2: One-way solid slab (SS1).
    3: Composite slabs with pre-fabricated joists and ceramic blocks (HS)."""
    staircase_slab_dept: List[float | None]
    """Depth of the staircase slabs."""
    beam_type: List[Literal[1, 2]]
    """Beam typology
    1: Wide beams.
    2: Emergent beams."""
    column_section: List[Literal[1, 2]]
    """Column cross-section
    1: Square solid section.
    2: Rectangular solid section."""
    steel_grade: List[str]
    """Steel material class ID, or grade, e.g., 'S400'."""
    concrete_grade: List[str]
    """Concrete material class ID, or grade, e.g., 'C20'."""
    quality: List[Literal[1, 2, 3]]
    """Construction quality levels
    1: High quality.
    2: Moderate quality.
    3: Low quality."""
    geometry: List[StandardFrame]
    """List of bilding geometry instances."""
    floor_width_x: List[float]
    """Total floor width in x direction in floor layout."""
    floor_width_y: List[float]
    """Total floor width in y direction in floor layout."""
    floor_area: List[float]
    """Total floor area in floor layout."""
    long_over_short_width: List[float]
    """Ratio of longer to shorter floor widths in floor layout."""
    beta: List[float]
    """Design lateral load factor."""
    num_storeys: List[int]
    """Number of storeys."""
    design_class: List[float]
    """Building design class selected."""
    available_design_classes: List[str]
    """Available design classes to use."""
    available_archetypes: List[str]
    """Available building archetypes (layouts) to use."""
    taxonomy: List[TaxonomyData]
    """Taxonomy Information required for performing simulated-design."""

    def __init__(self) -> None:
        """Initialize BCIM object.
        """
        self.__defaults = DefaultInputs()
        """Object gets the parameters loaded from json files."""
        self.__archetypes = Archetypes()
        """Object generating the building archetypes data load from layouts
        file."""

    def generate(self, design_class: str, **inputs) -> None:
        """Upon setting model inputs, generates the BCIM data.

        It uses the parameters defined in json files for the specified
        design_class as the default inputs. If user would like to change
        any parameter, it can be specified as keyword argument. All possible
        inputs other than design_class are listed in the example inputs.

        Parameters
        ----------
        design_class : str
            Building design class.
        **inputs
            Contains input parameters required for data generation.
            These will replaced the defaults obtained for the specified
            `design_class`.

        Example Inputs
        --------------
        >>> design_class = "eu_cdh"
        >>> inputs = {
                "typical_storey_height": {
                    "cv": 0.07,
                    "mu": 2.90,
                    "lower_bound": 2.3,
                    "upper_bound": 3.8
                },
                "staircase_bay_width": {
                    "lower_bound": 2.8,
                    "upper_bound": 3.2
                },
                "standard_bay_width": {
                    "corr_coeff_xy": -0.92,
                    "lower_bound_x": 3.5,
                    "upper_bound_x": 7.5,
                    "theta_x": 4.5,
                    "sigma_x": 0.35,
                    "lower_bound_y": 3.5,
                    "upper_bound_y": 7.5,
                    "theta_y": 4.5,
                    "sigma_y": 0.35
                },
                "steel": {
                    "tag": ["S400", "S500"],
                    "probability": [0.10, 0.90]
                },
                "concrete": {
                    "tag": ["C20", "C25", "C30", "C35"],
                    "probability": [0.30, 0.45, 0.20, 0.05]
                },
                "ground_storey_height": {
                    "maximum": 4.20,
                    "factor": [1.0, 1.1, 1.2, 1.3, 1.4],
                    "probability": [0.55, 0.10, 0.20, 0.10, 0.05]
                },
                "construction_quality": {
                    "probability": [0.6, 0.3, 0.1]
                },
                "slab_typology": {
                    "ss1_prob_given_ss1_or_hs": 0.50,
                    "ss2_prob_given_ss2_or_hs": 0.65,
                    "upper_lim_for_min_ss_span_length": 6.0,
                    "upper_lim_for_max_ss2_span_ratio": 2.0,
                    "staircase_slab_depth": 0.15,
                    "floor_slab_thickness": 0.15
                },
                "wb_prob_given_hs": 0.50,
                "square_column_prob": 0.50,
                "layout": "all",
                "beta": 0.15,
                "num_storeys": 5,
                "seed": 1993,
                "sample_size": 150
            }
        """
        # Retrieve default input parameters for the design class
        defaults = self.__defaults.get(design_class).__dict__
        # Update the parameters based on user input
        for key in inputs.keys():
            if key in defaults.keys():
                bool1 = isinstance(inputs[key], dict)
                bool2 = isinstance(defaults[key], dict)
                if bool1 and bool2:
                    inputs_sub: dict = inputs[key]
                    defaults_sub: dict = defaults[key]
                    for subkey in inputs_sub:
                        if subkey in defaults_sub.keys():
                            defaults_sub[subkey] = inputs_sub[subkey]
                else:
                    defaults[key] = inputs[key]
        # Store the updated input parameters
        self.inputs = InputData(**defaults)
        # Add all floor layout names
        if self.inputs.layout == "all":
            self.inputs.layout = self.available_archetypes
        # Generate the model data
        self.__generate()

    def __generate(self) -> None:
        """Completes BCIM data generation process.
        """
        # Generate realisations
        self.__get_realisations()
        # Reset sampler and get the realisation as dictionary
        self.__get_geometries()
        # Add the rest
        self.beta = \
            [self.inputs.beta] * self.inputs.sample_size
        self.num_storeys = \
            [self.inputs.num_storeys] * self.inputs.sample_size
        self.design_class = \
            [self.inputs.design_class] * self.inputs.sample_size
        self.staircase_slab_depth = \
            [self.inputs.slab_typology.staircase_slab_depth] * \
            self.inputs.sample_size
        self.slab_thickness = \
            [self.inputs.slab_typology.floor_slab_thickness] * \
            self.inputs.sample_size
        # Bay with in y direction for staircases is the same as typical one
        self.staircase_span_length_y = self.typical_span_length_y.copy()

    def __get_realisations(self) -> None:
        """Generate realisations for BCIM data.
        """
        # Set the sampler to use
        sampler = Sampler(
            self.inputs.sample_size, self.inputs.seed)
        # Spans with staircase
        tmp = self.inputs.staircase_bay_width
        self.staircase_span_length_x = \
            sampler.set_stair_span_length_x(
                tmp.lower_bound, tmp.upper_bound)
        # Typical spans
        tmp = self.inputs.standard_bay_width
        self.typical_span_length_x, self.typical_span_length_y = \
            sampler.set_typical_span_length(
                tmp.corr_coeff_xy, (tmp.lower_bound_x, tmp.lower_bound_y),
                (tmp.upper_bound_x, tmp.upper_bound_y),
                (tmp.theta_x, tmp.theta_y), (tmp.sigma_x, tmp.sigma_y))
        # Layouts
        tmp = self.inputs.layout
        self.layout = sampler.set_layout(tmp)
        # Typical storey heights
        tmp = self.inputs.typical_storey_height
        self.typical_storey_height = \
            sampler.set_typical_storey_height(
                tmp.cv, tmp.mu, tmp.lower_bound, tmp.upper_bound)
        # Ground storey heights
        tmp = self.inputs.ground_storey_height
        self.ground_storey_height = \
            sampler.set_ground_storey_height(
                tmp.factor, tmp.probability, tmp.maximum)
        # Slab type
        tmp = self.inputs.slab_typology
        self.slab_type = \
            sampler.set_slab_type(
                tmp.ss1_prob_given_ss1_or_hs, tmp.ss2_prob_given_ss2_or_hs,
                tmp.max_ss_short_span,
                tmp.max_ss2_aspect_ratio)
        # Beam types
        tmp = self.inputs.wb_prob_given_hs
        self.beam_type = sampler.set_beam_type(tmp)
        # Column types
        tmp = self.inputs.square_column_prob
        self.column_section = sampler.set_column_type(tmp)
        # Steel materials
        tmp = self.inputs.steel
        self.steel_grade = sampler.set_material_class(
            tmp.grade, tmp.probability, 'steel')
        # Concrete materials
        tmp = self.inputs.concrete
        self.concrete_grade = sampler.set_material_class(
            tmp.grade, tmp.probability, 'concrete')
        # Construction quality
        tmp = self.inputs.construction_quality
        self.quality = sampler.set_construction_quality(
            tmp.quaility, tmp.probability)

    def __get_geometries(self) -> None:
        """Generate building geometries for BCIM data.
        """
        # Get geometries for the sample
        geometries = []
        area = []
        lx = []
        ly = []
        long_over_short = []
        for i in range(self.inputs.sample_size):
            geometry = self.__archetypes.get_geometry(
                self.layout[i], self.inputs.num_storeys,
                self.typical_storey_height[i],
                self.ground_storey_height[i],
                self.typical_span_length_x[i],
                self.typical_span_length_y[i],
                self.staircase_span_length_x[i])
            # Compute other attributes
            xs = geometry.system_grid_data.x.ordinates
            ys = geometry.system_grid_data.y.ordinates
            lx.append(max(xs) - min(xs))
            ly.append(max(ys) - min(ys))
            area.append(lx[i] * ly[i])
            long_over_short.append(max(lx[i], ly[i]) / min(lx[i], ly[i]))
            geometries.append(geometry)
        # Add the geometry attributes to bcim data
        self.geometry = geometries
        self.floor_width_x = lx
        self.floor_width_y = ly
        self.floor_area = area
        self.long_over_short_width = long_over_short

    def _update_geometries(self):
        """Updates building geometries if new data is provided.
        """
        self.__get_geometries()

    @property
    def available_design_classes(self) -> List[str]:
        """
        Returns
        -------
        List[str]
            List of available design classes that can be used for BCIM data
            generation.
        """
        return self.__defaults.available_classes

    @property
    def available_archetypes(self) -> List[str]:
        """
        Returns
        -------
        List[str]
            List of available archetype (layouts) tags that can be used for
            BCIM data generation.
        """
        return self.__archetypes.available_tags

    """TODO
    Might need to visualize available layouts.
    Maybe it is required to create a layout visualiser.
    This has to be another property, which can be used by GUI.
    So, instead of showing available archetypes tags, we can directly
    visualise them as well.
    """

    @property
    def taxonomy(self) -> List[TaxonomyData]:
        """
        Returns
        -------
        List[TaxonomyData]
            List of design inputs (taxonomy) for each building realisation.
        """
        names = ['slab_thickness', 'slab_type',
                 'staircase_slab_depth', 'beam_type', 'column_section',
                 'geometry', 'steel_grade', 'concrete_grade', 'quality',
                 'beta', 'design_class']
        taxonomy_list = []
        for i in range(self.inputs.sample_size):
            data = {name: getattr(self, name)[i] for name in names}
            taxonomy = TaxonomyData(**data)
            taxonomy_list.append(taxonomy)

        return taxonomy_list

    def to_csv(self, path: Union[str, Path]) -> None:
        """Saves the generated BCIM data into the specified .csv file path.

        Parameters
        ----------
        path : str | Path
            File path of the csv file.
            e.g., My/Path/To/The/File.csv
        """
        names = ['staircase_span_length_x', 'typical_span_length_x',
                 'typical_span_length_y', 'layout',
                 'typical_storey_height', 'ground_storey_height',
                 'slab_type', 'beam_type', 'column_section',
                 'steel_grade', 'concrete_grade', 'quality',
                 'floor_width_x', 'floor_width_y', 'floor_area',
                 'long_over_short_width', 'beta', 'num_storeys',
                 'design_class', 'staircase_span_length_y']
        data = {name: getattr(self, name) for name in names}
        data = pd.DataFrame(data)
        data.to_csv(path, index=False, float_format='%g')
