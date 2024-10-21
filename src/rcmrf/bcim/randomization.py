"""
Samplers used for randomization in building portfolio generation process.
"""

# Imports from installed packages
from scipy.stats import norm, uniform
import numpy as np
from typing import List, Tuple, Literal, Union

# Imports from utils library
from ...utils.stats import multivariate_normal, random_choice
from ...utils.stats import log_normal_truncated_cdf_inv, log_normal_truncated
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
    slab_thickness : np.ndarray
        Slab thickness.
    slab_type : np.ndarray
        Slab typology
            1: Two-way solid slab
            2: One-way solid slab
            3: One-way composite slab with ceramic blocks and RC joists or
            pre-stressed beams
    slab_orient : np.ndarray
        Slab unloading orientation
            1: Unloading in beams along X direction
            2: Unloading in beams along Y direction
            3: Unloading in beams along both directions
    slab_weight : np.ndarray
        Slab self-weights per unit area.
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
    slab_thickness: np.ndarray
    """Slab thickness."""
    slab_type: np.ndarray
    """Slab typology.
        1: Two-way solid slab.
        2: One-way solid slab.
        3: One-way composite slab with ceramic blocks and RC joists or
    pre-stressed beams."""
    slab_orient: np.ndarray
    """Slab unloading orientation.
        1: Unloading in beams along X direction.
        2: Unloading in beams along Y direction.
        3: Unloading in beams along both directions.
    """
    slab_weight: np.ndarray
    """Self-weight of slabs per surface."""
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
        # astair = np.random.uniform(lower_bound, upper_bound, num_sample)
        loc = lower_bound
        scale = upper_bound - lower_bound
        prob = np.random.rand(self.sample_size)
        astair = uniform.ppf(prob, loc=loc, scale=scale)
        staircase_span_length_x = 0.05 * np.round(20 * astair)
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
        # Mean of the multivariate normal or Gaussian distribution
        mu = np.array([0, 0])
        # Covariance matrix
        # TODO: This could be named as correlation matrix as well
        cov = np.array([[1, corr_coeff], [corr_coeff, 1]])
        # Realisations
        # Z = np.random.multivariate_normal(mu, cov, size=num_sample)
        z = multivariate_normal(mu, cov, self.sample_size)
        u = norm.cdf(z, loc=0.0, scale=1.0)
        # Log-normal truncated distribution
        mu_ln = np.log(np.array(theta))
        rx = log_normal_truncated_cdf_inv(
            u[:, 0], mu=mu_ln[0], sigma=std_ln[0],
            lower=lower_bound[0], upper=upper_bound[0])
        ry = log_normal_truncated_cdf_inv(
            u[:, 1], mu=mu_ln[1], sigma=std_ln[1],
            lower=lower_bound[1], upper=upper_bound[1])
        # Rounding
        typical_span_length_x = 0.05 * np.round(20 * rx)
        typical_span_length_y = 0.05 * np.round(20 * ry)
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

        # layouts = np.random.choice(layouts, size=self.sample_size)
        sample = random_choice(layouts, size=self.sample_size)
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
        typical_storey_heights = log_normal_truncated(
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
        max_h_ground: float
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
            Sum should be equal to 1.0.
        max_h_ground : float
            Maximum possible ground storey height.

        Returns
        -------
        List[float]
            Randomised ground storey heights.

        Notes
        -----
        1. `ground_storey_height = min(factor * typical_storey_heights,
        max_h_ground)`
        2. Factors have different probabilities

        Example Inputs
        --------------
        >>> factors = [1.0, 1.1, 1.2, 1.3, 1.4]
        >>> probability = [0.55, 0.10, 0.20, 0.10, 0.05]
        >>> max_h_ground = 4.20
        """
        # Generate sample for factors
        factors = np.random.choice(
            factors, size=self.sample_size, p=probabilities)
        # Set ground storey heights as factored storey heights
        ground_storey_height = 0.05 * np.round(
            20 * self.typical_storey_height * factors)
        # Check against the maximum
        ground_storey_height = np.minimum(ground_storey_height, max_h_ground)
        # Set precision
        ground_storey_height = np.round(ground_storey_height, PRECISION)
        # Store
        self.ground_storey_height = ground_storey_height
        # Return
        return ground_storey_height.tolist()

    def set_slab_properties(
        self, ratio1_1c: float, ratio2_2c: float, max_thickness: float,
        max_solid_length: float
    ) -> Tuple[Union[List[float], List[Literal[1, 2, 3]]]]:
        """
        Sets slab properties following a span length based decision tree.

        Parameters
        ----------
        ratio1_1c : float
            Ratio of the number of buildings with one-way solid slabs to
            the total number of buildings with one-way solid or composite
            slabs when:
                minimum span length <= `max_solid_length` and
                max-min span length ratio >= 2.0
            Should be less than 1.0.
        ratio2_2c : float
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

        Returns
        -------
        Tuple[Union[List[float], List[Literal[1, 2, 3]]]]
            slab thickness values,
            slab types,
            slab loading orientations,
            slab unit weight per surface area.

        Notes
        -----
        1. One-way slab directions are always in the direction of the longer
        span.
        2. If minimum span length is greater than max_solid_length
        (minimum span length <= `max_solid_length`), always one-way composite
        slab is assigned.
        3. Otherwise (minimum span length > `max_solid_length`), if the ratio
        between max and min span length is greater or equal to 2 (max-min span
        length ratio >= 2.0), sample has one-way solid or composite slabs
        based on ratio1 and randomly generated value.
        4. Otherwise (max-min span length ratio < 2.0), sample has two-way
        solid or composite slabs based on ratio2 and randomly generated value.
        5. If slab thickness computed based on minimum span length is greater
        than `max_thickness`, it is set as `max_thickness`.

        References
        ----------
        http://www.presdouro.pt/12/pdf/DT_PD2016.pdf

        Example Inputs
        --------------
        >>> ratio1_1c = 0.50
        >>> ratio2_2c = 0.65
        >>> max_thickness = 0.85  # m
        >>> max_solid_length = 6.0  # m

        TODO
        ----
        All the output parameters depend on slab_type that randomly obtained
        and span lengths. Maybe it is time to move orientation, thickness and
        weight elsewhere (they can be defined inside slab objects)
        """
        slab_thickness = np.zeros(self.sample_size)
        slab_type = np.zeros(self.sample_size, dtype='int')
        slab_orient = np.zeros(self.sample_size, dtype='int')
        slab_weight = np.zeros(self.sample_size)

        max_span_length = np.maximum(self.typical_span_length_x,
                                     self.typical_span_length_y)
        min_span_length = np.minimum(self.typical_span_length_x,
                                     self.typical_span_length_y)
        max_min_span_ratio = max_span_length / min_span_length
        x_y_span_ratio = (self.typical_span_length_x /
                          self.typical_span_length_y)

        for i in range(self.sample_size):
            if x_y_span_ratio[i] > 1.0:
                slab_orient[i] = 1
            else:
                slab_orient[i] = 2

            if min_span_length[i] > max_solid_length:
                slab_type[i] = 3
            else:
                random_value = np.random.rand()
                if max_min_span_ratio[i] >= 2.0:
                    if random_value <= ratio1_1c:
                        slab_type[i] = 2
                    else:
                        slab_type[i] = 3
                else:
                    if random_value <= ratio2_2c:
                        slab_type[i] = 1
                        slab_orient[i] = 3
                    else:
                        slab_type[i] = 3
            # Standard solid slab
            if slab_type[i] == 1 or slab_type[i] == 2:
                slab_thickness[i] = min(
                    round(100 * min_span_length[i]/30) / 100,
                    max_thickness)
                slab_weight[i] = 24 * slab_thickness[i]
            # Composite slabs ceramic blocks and pre-stressed joists
            elif slab_type[i] == 3:
                slab_thickness[i] = min(
                    round(100 * (0.032 * min_span_length[i] + 0.065)) / 100,
                    max_thickness)
                slab_weight[i] = \
                    2.20 * np.log(slab_thickness[i]) + 6.50
        # Set precision
        slab_thickness = np.round(slab_thickness, PRECISION)
        slab_weight = np.round(slab_weight, PRECISION)
        # Store
        self.slab_thickness = slab_thickness
        self.slab_type = slab_type
        self.slab_orient = slab_orient
        self.slab_weight = slab_weight
        # Return
        return (slab_thickness.tolist(), slab_type.tolist(),
                slab_orient.tolist(), slab_weight.tolist())

    def set_beam_type(self, composite_slab_wb_ratio: float
                      ) -> List[Literal[1, 2]]:
        """
        Sets beam types.

        Parameters
        ----------
        composite_slab_wb_ratio : float
            Ratio of number of buildings with composite slab that have wide
            beams to the total number of buildings with composite slab.
            Should be less than 1.0.

        Returns
        -------
        List[Literal[1, 2]]
            Beam typologies.

        Notes
        -----
        1. If slabs are solid slabs, beams are set as emergent beams (2).
        2. Otherwise, randomly assign wide (1) or emergent beam (2) based on
        the user-defined `composite_slab_wb_ratio` parameter.

        Example Inputs
        --------------
        >>> composite_slab_wb_ratio = 0.50
        """
        beam_type = np.zeros(self.sample_size, dtype='int')
        # Solid slab cases (can only be emergent)
        mask = self.slab_type != 3
        # beam_type[mask] = 2
        # Composite slab cases (can be either wide or emergent)
        beam_types = [1, 2]
        probs = [composite_slab_wb_ratio, 1.0 - composite_slab_wb_ratio]
        # beam_type[~mask] = np.random.choice(
        #     beam_types, size=sum(~mask), p=probs)
        beam_type = np.random.choice(beam_types, size=self.sample_size,
                                     p=probs)
        beam_type[mask] = 2
        # Store
        self.beam_type = beam_type
        # Return
        return beam_type.tolist()

    def set_column_type(self, square_column_ratio: float
                        ) -> List[Literal[1, 2]]:
        """
        Sets the type of column type or cross-section geometry.

        Parameters
        ----------
        square_column_ratio : float
            Ratio of buildings that have square columns to the
            total number of buildings (square + rectangle columns).
            Should be less than 1.0.

        Returns
        -------
        List[Literal[1, 2]]
            Randomly assigned column types for each building,
            square (1) or rectangular (2).

        Example Inputs
        --------------
        >>> square_column_ratio = 0.50
        """
        probability = [square_column_ratio, 1.0 - square_column_ratio]
        sections = [1, 2]
        # column_section = np.random.choice(sections, size=self.sample_size,
        #                                   p=probability)
        column_section = random_choice(sections, size=self.sample_size,
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
        # sample = np.random.choice(
        #     material_class, size=self.sample_size, p=probability)
        sample = random_choice(
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
        # quality = np.random.choice(
        #     quality_ids, size=self.sample_size, p=probabilities)
        quality = random_choice(
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
