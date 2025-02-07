"""
Samplers used for randomization in building portfolio generation process.
"""

# Imports from installed packages
import numpy as np
from typing import List, Tuple, Literal

# Imports from utils library
from ...utils.stats import (
    random_truncated_lognormal,
    random_multivariate_truncated_lognormal,
)
from ...utils.misc import PRECISION


class Sampler:
    """
    Sampler class for regular moment resisting frame structures.

    Parameters
    ----------
    num_sample : int
        Number of samples to be generated.
    seed : int
        Seed number considered in random number generators.

    Attributes
    ----------
    sample_size : int
        Number of samples to be generated.
    staircase_span_length_x : np.ndarray
        Staircase span length in x direction.
    typical_span_length_x : np.ndarray
        Typical span length in x direction.
    typical_span_length_y : np.ndarray
        Typical span length in y direction.
    layout: np.ndarray
        Building floor layouts.
    typical_storey_height : np.ndarray
        Typical storey heights.
    ground_storey_height : np.ndarray
        Ground storey heights.
    slab_type : np.ndarray
        Slab typology
            1: Two-way solid slab
            2: One-way solid slab
            3: One-way composite slab with ceramic blocks and RC joists or
            pre-stressed beams
    beam_type : np.ndarray
        Beam typology
            1: Wide beams
            2: Emergent beams
    column_section : np.ndarray
        Column cross-section
            1: square solid section
            2: rectangular solid section
    steel_mat_class : np.ndarray
        Steel material class ID, e.g., S400
    concrete_mat_class : np.ndarray
        Concrete material class ID, e.g., C20
    quality : np.ndarray
        Construction quality
            1: High quality
            2: Moderate quality
            3: Low quality

    Methods
    -------
    set_stair_span_length_x
        Sets staircase span lengths.
    set_typical_span_length
        Sets typical span lengths in x and y directions in a random fashion.
    set_layout
        Sets plan layout IDs for buildings.
    set_typical_storey_height
        Sets typical storey heights in a random fashion.
    set_ground_storey_height
        Sets ground storey heights.
    set_slab_properties
        Sets slab properties following a span length based decision tree.
    set_beam_type
        Sets beam types.
    set_column_type
        Sets the type of column type or cross-section geometry.
    set_material_class
        Randomly assigns material classes to the buildings given their
        occurrence probabilities.
    set_construction_quality
        Sets construction quality in a randomised fashion.
    """
    sample_size: int
    """Number of samples to be generated."""
    staircase_span_length_x: np.ndarray
    """Staircase span length in x direction."""
    typical_span_length_x: np.ndarray
    """Typical span length in x direction."""
    typical_span_length_y: np.ndarray
    """Typical span length in y direction."""
    layout: np.ndarray
    """Building floor layouts."""
    typical_storey_height: np.ndarray
    """Typical storey heights."""
    ground_storey_height: np.ndarray
    """Ground storey heights."""
    slab_type: np.ndarray
    """Slab typology.
        1: Two-way solid slab.
        2: One-way solid slab.
        3: One-way composite slab with ceramic blocks and RC joists or
    pre-stressed beams."""
    beam_type: np.ndarray
    """Beam typology.
        1: Wide beams.
        2: Emergent beams."""
    column_section: np.ndarray
    """Column cross-section.
        1: square solid section.
        2: rectangular solid section."""
    steel_grade: np.ndarray
    """Steel material class ID, e.g., S400."""
    concrete_grade: np.ndarray
    """Concrete material class ID, e.g., C20."""
    quality: np.ndarray
    """Construction quality.
        1: High quality.
        2: Moderate quality.
        3: Low quality."""

    def __init__(self, num_sample: int, seed: int | None = None) -> None:
        """
        Initialise the sampler object for regular moment resisting frame
        structures.

        Parameters
        ----------
        num_sample : int
            Number of samples to be generated.
        seed : int | None
            Seed number considered in random number generators,
            by default None.

        Example Inputs
        --------------
        >>> num_sample = 150
        >>> seed = 1993
        """
        # Set the sample size
        self.sample_size = num_sample
        # Set the seed for random number generator
        if seed:
            np.random.seed(seed)

    def set_stair_span_length_x(self, lower_bound: float, upper_bound: float
                                ) -> List[float]:
        """
        Sets staircase span lengths.

        Staircase span lengths are represented by uniform distribution.

        Parameters
        ----------
        lower_bound : float
            Lower boundary of the output interval.
            All values generated will be greater than or equal to lower bound.
        upper_bound : float
            Upper boundary of the output interval.
            All values generated will be less than or equal to upper bound.

        Returns
        -------
        List[float]
            Staircase span lengths.

        Example Inputs
        --------------
        >>> lower_bound = 2.8
        >>> upper_bound = 3.2
        """
        sample = np.random.uniform(lower_bound, upper_bound, self.sample_size)
        staircase_span_length_x = 0.05 * np.round(20 * sample)
        # Set precision
        staircase_span_length_x = np.round(staircase_span_length_x, PRECISION)
        self.staircase_span_length_x = staircase_span_length_x
        # Return
        return staircase_span_length_x.tolist()

    def set_typical_span_length(
        self, corr_coeff: float, lower_bound: Tuple[float],
        upper_bound: Tuple[float], theta: Tuple[float], std_ln: Tuple[float],
    ) -> Tuple[List[float]]:
        """
        Sets typical span lengths in x and y directions in a random fashion.

        Typical span lengths are represented with truncated log-normal
        distribution. It is assumed that span lengths are correlated.
        The samples are generated from multivariate truncated lognormal
        distribution.

        Parameters
        ----------
        corr_coeff : float
            Correlation coefficient (between span lengths x and y).
        lower_bound : Tuple[float]
            Lower bound for truncated log-normal distribution (x, y).
        upper_bound : Tuple[float]
            Upper bound for truncated log-normal distribution (x, y).
        theta : Tuple[float]
            Median of log-normal distribution.
        sigma : Tuple[float]
            Logarithmic standard deviation of the log-normal
            distribution (x, y).

        Notes
        -----
        ~LN(ln(theta), sigma)

        Returns
        -------
        Tuple[List[float]]
            Span lengths (x, y).

        Example Inputs
        --------------
        >>> corr_coeff = -0.92
        >>> lower_bound = (3.5, 3.5)
        >>> upper_bound = (7.5, 6.0)
        >>> theta = (4.5, 4.5)
        >>> std_ln = (0.35, 0.35)
        """
        # Correlation Matrix
        rho = np.array([
            [1.0, corr_coeff],
            [corr_coeff, 1.0]
        ])
        # Generate samples from multivarite truncated lognormal distribution
        samples = random_multivariate_truncated_lognormal(
            self.sample_size, rho,
            np.array(lower_bound), np.array(upper_bound),
            np.array(theta), np.array(std_ln)
        )
        # Rounding
        typical_span_length_x = 0.05 * np.round(20 * samples[:, 0])
        typical_span_length_y = 0.05 * np.round(20 * samples[:, 1])
        # Set precision
        typical_span_length_x = np.round(typical_span_length_x, PRECISION)
        typical_span_length_y = np.round(typical_span_length_y, PRECISION)
        # Store
        self.typical_span_length_x = typical_span_length_x
        self.typical_span_length_y = typical_span_length_y

        return typical_span_length_x.tolist(), typical_span_length_y.tolist()

    def set_layout(self, layouts: List[str]) -> List[str]:
        """Sets plan layout IDs for buildings.

        Parameters
        ----------
        layouts : List[str]
            Building layouts

        Returns
        -------
        np.ndarray
           Random building layout assignments

        Example Inputs
        --------------
        >>> layouts = ["B01", "B02", "B03", "B04", "B04b", "B05", "B06",
        "B07", "B08", "B09", "B10"]
        """

        sample = np.random.choice(layouts, size=self.sample_size)
        # Store
        self.layout = sample
        # Return
        return sample.tolist()

    def set_typical_storey_height(
        self, cv: float, mu: float, lower_bound: float, upper_bound: float
    ) -> List[float]:
        """
        Sets typical storey heights in a random fashion.

        Typical storey heights are represented with truncated log-normal
        distribution.

        Parameters
        ----------
        cv : float
            Coefficient of variation, s/mu.
        mu : float
            Mean of normal distribution.
        lower_bound : float
            Lower bound of truncated log-normal distribution.
        upper_bound : float
            Upper bound of truncated log-normal distribution.

        Returns
        -------
        List[float]
            Generated typical storey heights.

        Example Inputs
        --------------
        >>> cv = 0.07
        >>> mu = 2.90
        >>> lower_bound = 2.3
        >>> upper_bound = 3.8
        """
        std_ln = (np.log(1 + cv ** 2)) ** 0.5
        mu_ln = np.log(mu) - 0.5 * std_ln ** 2
        # Realisations
        typical_storey_heights = random_truncated_lognormal(
            self.sample_size, mu_ln, std_ln, lower_bound, upper_bound)
        # Rounding
        typical_storey_height = (.05 * np.round(20 * typical_storey_heights))
        # Set precision
        typical_storey_height = np.round(typical_storey_height, PRECISION)
        # Store
        self.typical_storey_height = typical_storey_height

        return typical_storey_height.tolist()

    def set_ground_storey_height(
        self, factors: List[float], probabilities: List[float],
        max_height: float
    ) -> List[float]:
        """
        Sets ground storey heights.

        Parameters
        ----------
        factors : List[float]
            Factors applied on typical storey heights to obtain
            ground storey heights.
        probabilities : List[float]
            Corresponding probabilities of factors
        max_height : float
            Maximum considered ground storey height.

        Returns
        -------
        List[float]
            Randomised ground storey heights.

        Notes
        -----
        1. `ground_storey_height = min(factor * typical_storey_heights,
        max_height)`
        2. Factors have different probabilities

        Example Inputs
        --------------
        >>> factors = [1.0, 1.1, 1.2, 1.3, 1.4]
        >>> probability = [0.55, 0.10, 0.20, 0.10, 0.05]
        >>> max_height = 4.20
        """
        # Generate sample for factors
        factors = np.random.choice(
            factors, size=self.sample_size, p=probabilities)
        # Set ground storey heights as factored storey heights
        ground_storey_height = 0.05 * np.round(
            20 * self.typical_storey_height * factors)
        # Check against the maximum
        ground_storey_height = np.minimum(ground_storey_height, max_height)
        # Set precision
        ground_storey_height = np.round(ground_storey_height, PRECISION)
        # Store
        self.ground_storey_height = ground_storey_height
        # Return
        return ground_storey_height.tolist()

    def set_slab_type(
        self, ss1_prob_given_ss1_or_hs: float,
        ss2_prob_given_ss2_or_hs: float,
        max_ss_short_span: float,
        max_ss2_aspect_ratio: float
    ) -> List[Literal[1, 2, 3]]:
        """
        Sets slab typology following a span length based decision tree.

        Parameters
        ----------
        ss1_prob_given_ss1_or_hs : float
            Probability of having SS1 type slab given that the slab type
            is either SS1 or HS.
        ss2_prob_given_ss2_or_hs : float
            Probability of having SS2 type slab given that the slab type
            is either SS2 or HS.
        max_ss_short_span : float
            Upper limit for the shorter span length in solid slabs (SS1, SS2).
        max_ss2_aspect_ratio : float
            Upper limit for the ratio of maximum to minimum span lengths
            (aspect ratio) in SS2 slabs.

        Returns
        -------
        List[Literal[1, 2, 3]]
            Slab typologies.

        Notes
        -----
        1. Slab typologies:
        Solid two-way cast-in-situ slabs (1: SS2),
        Solid one-way cast-in-situ slabs (2: SS1),
        Composite slabs with pre-fabricated joists and ceramic blocks (3: HS).
        2. Slab type is assigned as HS, if minimum span length is greater than
        the upper limit for minimum solid slab span length
        (minimum span length <= `max_ss_short_span`).
        3. Otherwise, if the ratio of maximum to minimum span lengths is
        greater or equal to `max_ss2_aspect_ratio`, slab type is
        randomly as SS1 or HS based on `ss1_prob_given_ss1_or_hs`.
        4. Otherwise, slab type is determined randomly as SS2 or HS based on
        `ss2_prob_given_ss2_or_hs`.

        Example Inputs
        --------------
        >>> ss1_prob_given_ss1_or_hs = 0.50
        >>> ss2_prob_given_ss2_or_hs = 0.65
        >>> max_ss_short_span = 6.0  # in meters
        >>> max_ss2_aspect_ratio = 2.0
        """
        # Set the storage array
        slab_type = np.zeros(self.sample_size, dtype='int')
        # Parameters for decision tree
        max_span_length = np.maximum(self.typical_span_length_x,
                                     self.typical_span_length_y)
        min_span_length = np.minimum(self.typical_span_length_x,
                                     self.typical_span_length_y)
        max_span_ratio = max_span_length / min_span_length
        # Parameters for random sampling from discrete probability distribution
        ids_ss1_hs = [2, 3]
        probs_ss1_hs = [ss1_prob_given_ss1_or_hs, 1 - ss1_prob_given_ss1_or_hs]
        ids_ss2_hs = [1, 3]
        probs_ss2_hs = [ss2_prob_given_ss2_or_hs, 1 - ss2_prob_given_ss2_or_hs]
        # Decision Tree
        for i in range(self.sample_size):
            if min_span_length[i] > max_ss_short_span:
                slab_type[i] = 3
            else:
                if max_span_ratio[i] >= max_ss2_aspect_ratio:
                    slab_type[i] = np.random.choice(ids_ss1_hs, p=probs_ss1_hs)
                else:
                    slab_type[i] = np.random.choice(ids_ss2_hs, p=probs_ss2_hs)
        # Store the typologies
        self.slab_type = slab_type
        # Return
        return slab_type.tolist()

    def set_beam_type(self, wb_prob_given_hs: float) -> List[Literal[1, 2]]:
        """
        Sets beam types.

        Parameters
        ----------
        wb_prob_given_hs : float
            Probability of having wide beams (WB) given slab type is HS

        Returns
        -------
        List[Literal[1, 2]]
            Beam typologies.

        Notes
        -----
        1. If slabs are solid slabs, beams are set as emergent beams (2).
        2. Otherwise, randomly assign wide (1) or emergent beam (2) based on
        the user-defined `wb_prob_given_hs` parameter.

        Example Inputs
        --------------
        >>> wb_prob_given_hs = 0.50
        """
        # Set the storage array
        beam_type = np.zeros(self.sample_size, dtype='int')
        # Solid slab cases (can only be emergent)
        mask = self.slab_type != 3
        # Composite slab cases (can be either wide or emergent)
        beam_types = [1, 2]
        probs = [wb_prob_given_hs, 1.0 - wb_prob_given_hs]
        beam_type = np.random.choice(
            beam_types, size=self.sample_size, p=probs)
        beam_type[mask] = 2
        # Store
        self.beam_type = beam_type
        # Return
        return beam_type.tolist()

    def set_column_type(self, square_prob: float) -> List[Literal[1, 2]]:
        """
        Sets the type of column or cross-section geometry.

        Parameters
        ----------
        square_prob : float
            Probability of having square columns.

        Returns
        -------
        List[Literal[1, 2]]
            Randomly assigned column types for each building,
            square (1) or rectangular (2).

        Example Inputs
        --------------
        >>> square_prob = 0.50
        """
        probability = [square_prob, 1.0 - square_prob]
        sections = [1, 2]
        column_section = np.random.choice(sections, size=self.sample_size,
                                          p=probability)
        # Store
        self.column_section = column_section
        # Return
        return column_section.tolist()

    def set_material_class(
        self, material_class: List[str], probability: List[float],
        material: Literal["steel", "concrete"]
    ) -> List[str]:
        """
        Randomly assigns material classes to the buildings given
        their occurrence probabiities.

        Parameters
        ----------
        material_class : List[str]
            List of defined material classes.
        probability : List[float]
            Probabilities of having different material classes.
            Sum should be equal to 1.0.
        material : Literal["steel", "concrete"]
            Type of material, which can be either "steel" or "concrete".

        Returns
        -------
        List[str]
            Randomly assigned material classes for building.

        Example Inputs
        --------------
        >>> material_class = ["S240", "S400"]
        >>> probabilities = [0.60, 0.40]
        """
        sample = np.random.choice(
            material_class, size=self.sample_size, p=probability)
        if material == "steel":
            self.steel_grade = sample
        elif material == "concrete":
            self.concrete_grade = sample
        # Return
        return sample.tolist()

    def set_construction_quality(self, quality_ids: List[int],
                                 probabilities: List[float]) -> List[int]:
        """
        Sets construction quality in a randomised fashion.

        Parameters
        ----------
        quality_ids : List[int]
            Quality identifiers, IDs.
        probabilities : List[float]
            Corresponding probabilities for construction qualities.
            Sum should be equal to 1.0.

        Returns
        -------
        List[int]
            Construction quality sample.

        Example Inputs
        --------------
        >>> quality_ids = [1, 2, 3]
        >>> probabilities = [0.6, 0.3, 0.1]
        """
        quality = np.random.choice(
            quality_ids, size=self.sample_size, p=probabilities)
        # Store
        self.quality = quality
        # Return
        return quality.tolist()

    def reset(self) -> None:
        """Resets all the attributes of the Sampler class instance.
        """
        # Reset
        attrs = list(self.__dict__.keys())
        for attr in attrs:
            delattr(self, attr)
