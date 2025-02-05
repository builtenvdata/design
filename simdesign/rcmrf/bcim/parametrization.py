"""
Pydantic models used for parametrizing BCIM inputs.
"""

# Imports from installed packages
from pydantic import BaseModel
from typing import List, Union, Literal, Optional


class GroundStoreyHeight(BaseModel):
    """Parameters used to define ground storey heights.

    Sampled typical storey heights are factored by the `factor` based on their
    `probability` to obtain ground storey heights. If the factored storey
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


class SlabTypology(BaseModel):
    """Parameters required for slab typology sampling or decision tree.

    Attributes
    ----------
    ss1_prob_given_ss1_or_hs : float
        Probability of having SS1 type slab given that the slab type
        is either SS1 or HS.
    ss2_prob_given_ss2_or_hs : float
        Probability of having SS2 type slab given that the slab type
        is either SS2 or HS.
    upper_lim_for_min_ss_span_length : float
        Upper limit for the minimum span length in solid slabs (SS1, SS2).
    upper_lim_for_max_ss2_span_ratio : float
        Upper limit for the ratio of maximum to minimum span lengths in
        SS2 slabs.
    staircase_slab_depth: float | None
       Depth of the staircase slabs, by default None.
    floor_slab_thickness: float | None
       Depth of the floor slabs, by default None.

    Notes
    -----
    1. SS2 refers to solid two-way cast-in-situ slabs.
    2. SS1 refers to solid one-way cast-in-situ slabs.
    3. HS refers to composite slabs with pre-fabricated joists and ceramic
    blocks.
    """
    ss1_prob_given_ss1_or_hs: float
    """Probability of having SS1 type slab given that the slab type
    is either SS1 or HS."""
    ss2_prob_given_ss2_or_hs: float
    """Probability of having SS2 type slab given that the slab type
    is either SS2 or HS."""
    max_ss_short_span: float = 6.0
    """Upper limit for the short span length in solid slabs (SS1, SS2),
    by default 6.0 meters."""
    max_ss2_aspect_ratio: float = 2.0
    """Upper limit for the ratio of maximum to minimum span lengths
    (aspect ratio) in SS2 slabs, by default 2.0"""
    staircase_slab_depth: Optional[float] = None
    """Depth of the staircase slabs, by default None."""
    floor_slab_thickness: Optional[float] = None
    """Thickness of the floor slabs, by default None."""


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
        Parameters required for sampling typical storey heights.
    staircase_bay_width : StaircaseBayWidth
        Parameters required for sampling staircase bay widths.
    standard_bay_width : StandardBayWidth
        Parameters required for sampling standard bay widths.
    steel : Material
        Parameters required for sampling steel grades.
    concrete : Material
        Parameters required for sampling concrete grades.
    ground_storey_height : GroundStoreyHeight
        Parameters required for ground storey height sampling or decision tree
        operations.
    construction_quality : ConstructionQuality
        Parameters required for sampling construction quality levels.
    slab_typology : SlabTypology
        Parameters required for slab typology sampling or decision tree
        operations.
    wb_prob_given_hs : float
        Probability of having wide beams (WB) given the slab type is HS.
    square_column_prob : float
        Probability of having square columns.
    layout : Union[Literal["all"], List[str]]
        Layout IDs considered for the building generation process.
        It can be either "all" to include all layouts or a list of specific
        layouts.
    beta : float
        Design lateral load factor.
    num_storeys : int
        Number of storeys in the building.
    design_class : str
        Building seismic design class.
    sample_size : int
        Size of the sample to be generated.
    seed : int
        Seed value for the random number generator to ensure reproducibility.
    """
    typical_storey_height: TypicalStoreyHeight
    """Parameters required for typical storey height sampling."""
    staircase_bay_width: StaircaseBayWidth
    """Parameters required for staircase storey height sampling."""
    standard_bay_width: StandardBayWidth
    """Parameters required for standard bay width sampling."""
    steel: Material
    """Parameters required for steel grade sampling."""
    concrete: Material
    """Parameters required for concrete grade sampling."""
    ground_storey_height: GroundStoreyHeight
    """Parameters required for ground storey height sampling/decision tree."""
    construction_quality: ConstructionQuality
    """Parameters required for sampling construction quality levels."""
    slab_typology: SlabTypology
    """Parameters required for slab typology sampling/decision tree."""
    wb_prob_given_hs: float
    """Probability of having wide beams (WB) given slab type is HS."""
    square_column_prob: float
    """Probability of having square columns."""
    layout: Union[Literal["all"], List[str]]
    """Layout considered layout ids for the building generation process.
    It can be either "all" or a list of specific layout."""
    beta: float
    """Design lateral load factor."""
    num_storeys: int
    """Number of storeys."""
    design_class: str
    """Building seismic design class."""
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
