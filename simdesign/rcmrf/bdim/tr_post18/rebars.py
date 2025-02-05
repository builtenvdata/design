"""
The model used for detailing the structural members of tr_post18 buildings.
"""

# Imports from installed packages
import numpy as np
from pathlib import Path

# Imports from bdim base library
from ..baselib.rebars import RebarsBase
from .materials import Concrete, Steel

# Imports from utils library
from ....utils.units import mm


class Rebars(RebarsBase):
    """The class used for determining rebar solutions tr_post18 beams
    and columns.

    The functions within Rebars are very important because this is
    the place where the final solutions are obtained before uniformisation.
    The assumptions considered can have significant impact on the final
    solutions.

    Attributes
    ----------
    _data_path : Path | str
        Path to the json file containing rebar data.
    beam_long_bar_dias : List[float]
        Possible beam longitudinal bar diameters.
    beam_trans_bar_diams : List[float]
        Possible beam transverse bar diameters.
    beam_trans_bar_spacings : List[float]
        Possible beam transverse bar spacings.
    col_long_bar_diams : List[float]
        Possible column longitudinal bar diameters.
    col_trans_bar_diams : List[float]
        Possible column transverse bar diameters.
    col_trans_bar_spacings : List[float]
        Possible column transverse bar spacings.
    concrete : ConcreteBase
        Concrete material instance considered in design of beams and columns.
    steel : SteelBase
        Steel material instance considered in design of beams and columns.
    beam_max_sbl : float
        Maximum spacing between longitudinal bars (reinforcement) for beams.
    beam_min_sbl : float
        Minimum spacing between longitudinal bars (reinforcement) for beams.
    beam_max_leg_dist : float
        For beams, maximum distance between longitudinal bars within a beam
        section that can be considered to be confined without the need to have
        an extra stirrup leg around them.
    beam_cover : float
        Concrete cover for beams.
    col_max_sbl : float
        Maximum spacing between longitudinal bars (reinforcement) for columns.
    col_min_sbl : float
        Minimum spacing between longitudinal bars (reinforcement) for columns.
    col_max_leg_dist : float
        Maximum distance between longitudinal bars within a column
        section that can be considered to be confined without the need to have
        an extra stirrup leg around them.
    col_cover : float
        Concrete cover for columns.
    """

    _data_path = Path(__file__).parent / "data" / "rebars.json"
    """Path to the json file containing rebar data."""
    concrete: Concrete
    """Concrete material instance considered in design of beams and columns."""
    steel: Steel
    """Steel material instance considered in design of beams and columns."""
    beam_min_sbl: float = 35 * mm
    """For beams, minimum spacing between longitudinal bars (reinforcement).
    TS500-Section9.5.2"""
    col_min_sbl: float = 35 * mm
    """For columns, minimum spacing between longitudinal bars (reinforcement).
    TS500-Section9.5.2"""
    col_max_leg_dist: float = 150 * mm
    """For columns, maximum distance between longitudinal bars within a section
    that can be considered to be confined without the need to have
    an extra stirrup leg around them.
    """

    def _get_min_beam_dbh(self, **kwargs) -> float | np.ndarray:
        """Gets the minimum transverse reinforcement diameter in beams.

        Returns
        -------
        float | np.ndarray
            Minimum transverse reinforcement diameter.
        """
        return 8 * mm * np.ones(np.size(kwargs["dbl"]))

    def _get_min_col_dbh(self, **kwargs) -> float | np.ndarray:
        """Gets the minimum transverse reinforcement diameter in columns.

        References
        ----------
        Section-7.4.1 in TS500 and Section-7.3.4 in TBEC2018

        Returns
        -------
        float | np.ndarray
            Minimum transverse reinforcement diameter.
        """
        dbl = kwargs["dbl"]
        return np.maximum(dbl / 3, 8 * mm)

    def _get_beam_max_sbh(self, **kwargs) -> float | np.ndarray:
        """Gets maximum spacing between horizontal bars
        (transverse reinforcement) for beams.

        References
        ----------
        Section 7.4.4 in TBEC-2018

        Returns
        -------
        float | np.ndarray
            Maximum spacing between transverse reinforcement.
        """
        # maximum allowed spacing in current iteration
        d = kwargs["h"] - kwargs["cover"] - 0.5 * kwargs["dbh"]  # beam depth
        dbl = kwargs["dbl"]  # long. reinf. diameter
        max_sbh = np.minimum(np.minimum(150 * mm, d / 4), 8 * dbl)
        return max_sbh

    def _get_col_max_sbh(self, **kwargs) -> float | np.ndarray:
        """Gets maximum spacing between horizontal bars
        (transverse reinforcement) for columns.

        References
        ----------
        Section-7.3.4.1 in TBEC-2018

        Returns
        -------
        float | np.ndarray
            Maximum spacing between transverse reinforcement.
        """
        # maximum allowed spacing in current iteration
        by = kwargs["by"]  # column width along y
        bx = kwargs["bx"]  # column width along x
        b0 = np.minimum(by, bx)
        dbl = kwargs["dbl"]  # long. reinf. diameter
        max_sbh = np.minimum(np.minimum(150 * mm, b0 / 3), 6 * dbl)
        return max_sbh
