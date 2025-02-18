"""
The model used for detailing the structural members of tr_7599 buildings.
"""

# Imports from installed packages
import numpy as np
from pathlib import Path

# Imports from bdim base library
from ..baselib.rebars import RebarsBase

# Imports from utils library
from ....utils.units import mm


class Rebars(RebarsBase):
    """The class used for determining rebar solutions in beams and columns.

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
    beam_max_sbl : float
        For beams, maximum spacing between longitudinal bars (reinforcement).
    beam_min_sbl : float
        For beams, minimum spacing between longitudinal bars (reinforcement).
    beam_cover : float
        For beams, concrete cover.
    beam_max_sbh_over_dbl : float
        For beams, Maximum value of horizontal bar spacing to longitudinal bar
        diameter ratio.
    beam_max_sbh_over_dbh : float
        For beams, Maximum value of horizontal bar spacing to bar diameter
        ratio.
    beam_max_leg_dist : float
        For beams, maximum distance between longitudinal bars within a section
        that can be considered to be confined with
    """

    _data_path = Path(__file__).parent / "data" / "rebars.json"
    """Path to the json file containing rebar data."""
    beam_min_sbl: float = 35 * mm
    """For beams, min. spacing between longitudinal bars (reinforcement)."""
    col_min_sbl: float = 35 * mm
    """For columns, min. spacing between longitudinal bars (reinforcement)."""

    def _get_min_beam_dbh(self, **kwargs) -> float | np.ndarray:
        """Gets the minimum transverse reinforcement diameter in beams.

        References
        ----------
        Section-6.9.7 from TBEC-1975

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
        Section-6.6.5.1 from TBEC-1975 and Section-7.6 from TS500-1975

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
        Section-6.9.7 from TBEC-1975

        Returns
        -------
        float | np.ndarray
            Maximum spacing between transverse reinforcement.
        """
        # maximum allowed spacing in current iteration
        bw = kwargs["b"]  # beam width
        h = kwargs["h"]  # beam depth
        max_sbh = np.minimum(bw, h / 2)
        return max_sbh

    def _get_col_max_sbh(self, **kwargs) -> float | np.ndarray:
        """Gets maximum spacing between horizontal bars
        (transverse reinforcement) for columns.

        References
        ----------
        Section 6.6.5.1 in TBEC-1975

        Returns
        -------
        float | np.ndarray
            Maximum spacing between transverse reinforcement.
        """
        return 100 * mm
