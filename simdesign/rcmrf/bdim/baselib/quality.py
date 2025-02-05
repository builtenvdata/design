# Imports from installed packages
from abc import ABC
import numpy as np
from scipy.stats import lognorm, uniform
import json
from pathlib import Path
from pydantic import BaseModel
from typing import Literal, Optional, List

# Imports from bdim base library
from .beam import BeamBase
from .column import ColumnBase


class ModelData(BaseModel):
    """Construction quality model data.

    Attributes
    ----------
    joint : Literal["inelastic", "elastic", "rigid"]
        Joint modelling option considered in nonlinear models.
    bondslip_factor : float
        Bondslip factor considered for nonlinear beam-column elements.
    sigma_fck : float
        Logarithmic standard deviation of concrete strength ratio.
    sigma_fsyk : float
        Logarithmic standard deviation of steel yield strength ratio.
    sigma_cover : float
        Logarithmic standard deviation of concrete cover ratio.
    uniform_low_sbh : float
        Lower boundary of uniform stirrup spacing ratio distribution.
    uniform_up_sbh : float
        Upper boundary of uniform stirrup spacing ratio distribution.
    """
    joint: Literal["inelastic", "elastic", "rigid"]
    """Joint modelling option considered in nonlinear models."""
    bondslip_factor: float
    """Bondslip factor considered for nonlinear beam-column elements."""
    sigma_fck: float
    """Logarithmic standard deviation of concrete strength ratio."""
    sigma_fsyk: float
    """Logarithmic standard deviation of steel yield strength ratio."""
    sigma_cover: float
    """Logarithmic standard deviation of concrete cover ratio."""
    uniform_low_sbh: float
    """Lower boundary of uniform stirrup spacing ratio distribution."""
    uniform_up_sbh: float
    """Upper boundary of uniform stirrup spacing ratio distribution."""


class QualityData(BaseModel):
    """Data of all construction quality models (high, moderate, low).

    Attributes
    ----------
    high : ModelData
        High construction quality model.
    moderate : ModelData
        Moderate construction quality model.
    low : ModelData
        Low construction quality model.
    """
    high: ModelData
    """High construction quality model."""
    moderate: ModelData
    """Moderate construction quality model."""
    low: ModelData
    """Low construction quality model."""


class QualityBase(ABC):
    """Abstract base class for adjusting properties of structural members
    based on construction quality or deterioration level.

    Attributes
    ----------
    data_path : Path | str
        Path to the json file containing all the construction quality data.
    data : QualityData
        All the construction quality data considered for the design class.
    _model : ModelData
        Internal attribute for selected construction quality model.
    seed : Optional[int], optional
        Seed number considered for generating random values, by default None.
    """
    data_path: Path | str
    """Path to the json file containing all the construction quality data."""
    data: QualityData
    """All the construction quality data considered for the design class."""
    _model: ModelData
    """Internal attribute for selected construction quality model."""
    seed: Optional[int] = None
    """Seed number considered for generating random values, by default None."""

    def __init__(self) -> None:
        """Initialize a new instance of Quality class.
        """
        # Load quality model data
        with open(self.data_path, 'r') as json_file:
            # Load the JSON data into a Python dictionary
            data = json.load(json_file)
            # Store the quality model
            self.data = QualityData(**data)
        # Set the seed to use
        if self.seed:
            np.random.seed(self.seed)

    @property
    def model(self) -> ModelData:
        """Gets the selected construction quality model.

        Returns
        -------
        ModelData
            Construction quality model.
        """
        return self._model

    @model.setter
    def model(self, identifier: Literal[1, 2, 3]) -> None:
        """Selects construction quality model based on its identifier.

        Parameters
        ----------
        identifier : Literal[1, 2, 3]
            Construction quality identifier
            1. High construction quality.
            2. Moderate  construction quality.
            3. Low construction quality.
        """
        mapper = {
            1: self.data.high,
            2: self.data.moderate,
            3: self.data.low
        }
        self._model = mapper.get(identifier)

    def set_new_seed(self, seed: int) -> None:
        """
        Set a new random seed for reproducibility.

        This method updates the object's seed attribute and sets the global
        NumPy random seed to ensure deterministic behavior in random
        operations.

        Parameters
        ----------
        seed : int
            The new seed value to set.
        """
        self.seed = seed
        np.random.seed(self.seed)

    def set_adjusted_properties(self, beams: List[BeamBase],
                                columns: List[ColumnBase]) -> None:
        """Sets the quality adjusted properties of beams and columns:

        - Concrete compressive strength
        - Longitudinal reinforcement yield strength
        - Transverse reinforcement yield strength
        - Concrete cover
        - Stirrup spacing

        Parameters
        ----------
        beams : List[BeamBase]
            List of beams whose properties will be adjusted.
        columns : List[ColumnBase]
            List of columns whose properties will be adjusted.
        """
        # Initialize some parameters
        sigma_fck = self.model.sigma_fck
        sigma_fsyk = self.model.sigma_fsyk
        sigma_cover = self.model.sigma_cover
        uniform_low_sbh = self.model.uniform_low_sbh
        uniform_up_sbh = self.model.uniform_up_sbh
        num_columns = len(columns)
        num_beams = len(beams)
        # Mean concrete compressive strength ratio
        """
        TODO: Why do we use randomised mean ratio?
        Shouldn't we lower the mean_fc_ratio maybe?
        Based on the quality? Or just use 1.0?
        """
        # 1. Compute property modifiers (ratio of design value to in-situ)
        mu = np.log(1.0)  # (Logarithmic mean of ratio values)
        # Concrete compressive strength
        mu_fc = np.log(lognorm.ppf(np.random.rand(),
                                   s=sigma_fck,
                                   scale=np.exp(mu)))
        col_fc_ratio = lognorm.ppf(np.random.rand(num_columns),
                                   s=sigma_fck,
                                   scale=np.exp(mu_fc))
        beam_fc_ratio = lognorm.ppf(np.random.rand(num_beams),
                                    s=sigma_fck,
                                    scale=np.exp(mu_fc))
        # Longitudinal steel yield strength
        col_fsyl_ratio = lognorm.ppf(np.random.rand(num_columns),
                                     s=sigma_fsyk,
                                     scale=np.exp(mu))
        beam_fsyl_ratio = lognorm.ppf(np.random.rand(num_beams),
                                      s=sigma_fsyk,
                                      scale=np.exp(mu))
        # Transverse steel yield strength
        col_fsyh_ratio = lognorm.ppf(np.random.rand(num_columns),
                                     s=sigma_fsyk,
                                     scale=np.exp(mu))
        beam_fsyh_ratio = lognorm.ppf(np.random.rand(num_beams),
                                      s=sigma_fsyk,
                                      scale=np.exp(mu))
        # Concrete cover
        col_cover_ratio = lognorm.ppf(np.random.rand(num_columns),
                                      s=sigma_cover,
                                      scale=np.exp(mu))
        beam_cover_ratio = lognorm.ppf(np.random.rand(num_beams),
                                       s=sigma_cover,
                                       scale=np.exp(mu))
        # Stirrup spacing
        col_sbh_ratio = uniform.ppf(
            np.random.rand(num_columns),
            loc=uniform_low_sbh,
            scale=uniform_up_sbh-uniform_low_sbh
            )
        beam_sbh_start_ratio = uniform.ppf(
            np.random.rand(num_beams),
            loc=uniform_low_sbh,
            scale=uniform_up_sbh - uniform_low_sbh
            )
        beam_sbh_end_ratio = uniform.ppf(
            np.random.rand(num_beams),
            loc=uniform_low_sbh,
            scale=uniform_up_sbh - uniform_low_sbh
            )
        beam_sbh_mid_ratio = uniform.ppf(
            np.random.rand(num_beams),
            loc=uniform_low_sbh,
            scale=uniform_up_sbh - uniform_low_sbh
            )
        # Store adjusted properties of columns
        for i, col in enumerate(columns):
            col.fc_q = col.fcm * col_fc_ratio[i]
            col.fsyl_q = col.fsym * col_fsyl_ratio[i]
            col.fsyh_q = col.fsym * col_fsyh_ratio[i]
            col.cover_q = col.cover * col_cover_ratio[i]
            col.sbh_q = col.sbh * col_sbh_ratio[i]
        # Store adjusted properties of beams
        for i, beam in enumerate(beams):
            beam.fc_q = beam.fcm * beam_fc_ratio[i]
            beam.fsyl_q = beam.fsym * beam_fsyl_ratio[i]
            beam.fsyh_q = beam.fsym * beam_fsyh_ratio[i]
            beam.cover_q = beam.cover * beam_cover_ratio[i]
            sbh_start = beam.sbh[0] * beam_sbh_start_ratio[i]
            sbh_mid = beam.sbh[1] * beam_sbh_mid_ratio[i]
            sbh_end = beam.sbh[2] * beam_sbh_end_ratio[i]
            beam.sbh_q = np.array([sbh_start, sbh_mid, sbh_end])
