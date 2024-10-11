"""
Pydantic models used for parametrizing BCIM inputs.
"""

# Imports from installed packages
from pydantic import BaseModel
from typing import List, Union, Literal


class GroundStoreyHeight(BaseModel):
    """Parameters used to define ground storey heights.

    Sampled typical storey heights are factored by the `factor` based on their
    `probability` to obtain ground storey heights.  If the factored storey
    height is larger than `maximum` it will be set to `maximum`.

    Attributes
    ----------
    maximum: float
        Maximum possible ground storey height.
    factor: List[float]
        Factors applied on typical storey heights to obtain
        ground storey heights.
    probability: List[float]
        Corresponding probabilities of factors
        Sum should be equal to 1.0.
    """
    maximum: float
    """Maximum possible ground storey height."""
    factor: List[float]
    """Factors applied on typical storey heights to obtain
    ground storey heights."""
    probability: List[float]
    """Corresponding probabilities of factors.
    Sum should be equal to 1.0."""


class ConstructionQuality(BaseModel):
    """Construction quality IDs and their occurrence probability in
    the generated building portfolio.

    Attributes
    ----------
    quality: List[int]
        Construction quality identifiers, IDs.
    probability: List[float]
        Probability values for each quality ID.
    """
    quaility: List[int] = [1, 2, 3]
    """Construction quality identifiers, IDs.
    1: High quality
    2: Moderate quality
    3: Low quality"""
    probability: List[float]
    """Probability values for each quality ID."""


class SlabProperty(BaseModel):
    """Extra parameters required in slab property sampling.

    Attributes
    ----------
    one_to_one_and_comp_ratio : float
        Ratio of the number of buildings with one-way solid slabs to
        the total number of buildings with one-way solid or composite
        slabs when:
            minimum span length <= `max_solid_length` and
            max-min span length ratio >= 2.0
        Should be less than 1.0.
    two_to_two_and_comp_ratio : float
        Ratio of number of buildings with two-way solid slabs to
        the total number of buildings with two-way solid or one-way
        composite slabs when:
            minimum span length <= `max_solid_length` and
            max-min span length ratio < 2.0
        Should be less than 1.0.
    max_thickness : float
        Maximum possible slab thickness.
    max_solid_length : float
        Maximum possible length of solid slabs (type 1 and 2).
    staircase_slab_depth: float
       Depth of the slabs of the staircase.
    """
    one_to_one_and_comp_ratio: float
    """Ratio of the number of buildings with one-way solid slabs to
    the total number of buildings with one-way solid or composite
    slabs when:
        minimum span length <= `max_solid_length` and
        max-min span length ratio >= 2.0
    Should be less than 1.0."""
    two_to_two_and_comp_ratio: float
    """Ratio of number of buildings with two-way solid slabs to
    the total number of buildings with two-way solid or one-way
    composite slabs when:
        minimum span length <= `max_solid_length` and
        max-min span length ratio < 2.0
    Should be less than 1.0."""
    max_thickness: float
    """Maximum possible slab thickness."""
    max_solid_length: float
    """Maximum possible length of solid slabs (type 1 and 2)."""
    staircase_slab_depth: float
    """Depth of the slabs of the staircase."""


class TypicalStoreyHeight(BaseModel):
    """Parameters for the typical storey heights which are represented with
    truncated log-normal distribution.

    Attributes
    ----------
    cv : float
        Coefficient of variation, s/mu.
    mu : float
        Mean value for the typical storey heights.
    lower_bound : float
        Lower bound value.
    upper_bound : float
        Upper bound value.
    """
    cv: float
    """Coefficient of variation, s/mu."""
    mu: float
    """Mean value for the typical storey heights."""
    lower_bound: float
    """Lower bound value."""
    upper_bound: float
    """Upper bound value."""


class StaircaseBayWidth(BaseModel):
    """Parameters for the uniform distribution representing the staircase bay
    width.

    Attributes
    ----------
    lower_bound : float
        The lower bound value.
    upper_bound : float
        The upper bound value.
    """
    lower_bound: float
    """The lower bound value."""
    upper_bound: float
    """The upper bound value."""


class StandardBayWidth(BaseModel):
    """Parameters for the truncated lognormal distribution representing the
    standard bay width.

    Attributes
    ----------
    corr_coeff_xy : float
        Correlation coefficient between bay widths in two principal
        horizontal directions (-x and -y).
    lower_bound_x : float
        Lower bound of truncated log-normal distribution (-x).
    upper_bound_x : float
        Upper bound of truncated log-normal distribution (-x).
    theta_x : float
        Median of log-normal distribution (-x).
    sigma_x : float
        Logarithmic standard deviation of the lognormal distribution (-x).
    lower_bound_y : float
        Lower bound of truncated log-normal distribution (-y).
    upper_bound_y : float
        Upper bound of truncated log-normal distribution (-y).
    theta_y : float
        Median of log-normal distribution (-y).
    sigma_y : float
        Logarithmic standard deviation of the lognormal distribution (-y).
    """
    corr_coeff_xy: float
    """Correlation coefficient between bay widths in two principal
    horizontal directions (-x and -y)."""
    lower_bound_x: float
    """Lower bound of truncated log-normal distribution (-x)."""
    upper_bound_x: float
    """Upper bound of truncated log-normal distribution (-x)."""
    theta_x: float
    """Median of log-normal distribution (-x)."""
    sigma_x: float
    """Logarithmic standard deviation of the lognormal distribution (-x)."""
    lower_bound_y: float
    """Lower bound of truncated log-normal distribution (-y)."""
    upper_bound_y: float
    """Upper bound of truncated log-normal distribution (-y)."""
    theta_y: float
    """Median of log-normal distribution (-y)."""
    sigma_y: float
    """Logarithmic standard deviation of the lognormal distribution (-y)."""


class Material(BaseModel):
    """
    Material grades and their occurrence probabilities.

    Attributes
    ----------
    grade : List[str]
        Material tags, i.e., concrete strength classes or steel grades.
    probability : List[float]
        Occurrence probabilities for each material.
    """
    grade: List[str]
    """Material tags, i.e., concrete strength classes or steel grades."""
    probability: List[float]
    """Occurrence probabilities for each material."""


class InputData(BaseModel):
    """
    Input parameters obtained from JSON files to generate BCIM data.

    Attributes
    ----------
    typical_storey_height : TypicalStoreyHeight
        Parameters representing the typical storey height distribution.
    staircase_bay_width : StaircaseBayWidth
        Parameters representing the staircase bay width distribution.
    standard_bay_width : StandardBayWidth
        Parameters representing the standard bay width distribution.
    steel : Material
        Steel grades and their occurrence probabilities.
    concrete : Material
        Concrete strength classes and their occurrence probabilities.
    ground_storey_height : GroundStoreyHeight
        Parameters defining ground storey heights.
    construction_quality : ConstructionQuality
        IDs and occurrence probabilities for construction quality.
    slab_properties : SlabProperty
        Extra parameters required in slab property sampling.
    composite_slab_wb_ratio : float
        Ratio of number of buildings with composite slab that have wide
        beams to the total number of buildings with composite slab.
    square_column_ratio : float
        Ratio of square columns in the sample.
    layout : Literal["all"] | List[str]
        Layout options for the building generation process.
        It can be either "all" or a list of specific layout.
    beta : float
        Design lateral load factor.
    num_storeys : int
        Number of storeys.
    design_class : str
        Building design class.
    sample_size: int
        Size of the generate sample.
    seed: int
        Seed used in random number generator.
    """
    typical_storey_height: TypicalStoreyHeight
    """Parameters representing the typical storey height distribution."""
    staircase_bay_width: StaircaseBayWidth
    """Parameters representing the staircase bay width distribution."""
    standard_bay_width: StandardBayWidth
    """Parameters representing the standard bay width distribution."""
    steel: Material
    """Steel grades and their occurrence probabilities."""
    concrete: Material
    """Concrete strength classes and their occurrence probabilities."""
    ground_storey_height: GroundStoreyHeight
    """Parameters defining ground storey heights."""
    construction_quality: ConstructionQuality
    """IDs and occurrence probabilities for construction quality."""
    slab_properties: SlabProperty
    """Extra parameters required in slab property sampling."""
    composite_slab_wb_ratio: float
    """Ratio of number of buildings with composite slab that have wide
    beams to the total number of buildings with composite slab."""
    square_column_ratio: float
    """Ratio of square columns in the sample."""
    layout: Union[Literal["all"], List[str]]
    """Layout options for the building generation process.
    It can be either "all" or a list of specific layout."""
    beta: float
    """Design lateral load factor."""
    num_storeys: int
    """Number of storeys."""
    design_class: str
    """Building design class."""
    sample_size: int
    """Size of the generate sample."""
    seed: int
    """Seed used in random number generator."""


class ArchetypeData(BaseModel):
    """
    Model representing data for a specific building archetype.

    In this case, archetype is specified by floor layout properties
    since at each floor, the standard frame has the same plan with uniform
    bay widths along the same axis. The only exception is bay width along
    x-axis for stairs.

    Attributes
    ----------
    tag : str
        Unique identifier for the archetype.
    num_bays_x : int
        Number of bays along the x-axis.
    num_bays_y : int
        Number of bays along the y-axis.
    stairs_grid_x : int
        Grid position of stairs along the x-axis.
    stairs_grid_y : int
        Grid position of stairs along the y-axis.
    """
    tag: str
    """Unique identifier for the archetype (or floor layout)."""
    num_bays_x: int
    """Number of bays along the x-axis."""
    num_bays_y: int
    """Number of bays along the y-axis."""
    stairs_grid_x: int
    """Grid id of stairs along the x-axis."""
    stairs_grid_y: int
    """Grid id of stairs along the y-axis."""
