# Imports from installed packages
from abc import ABC
import json
import numpy as np
from pathlib import Path
from pydantic import BaseModel
from typing import List, Literal

# Imports from bdim base library
from .materials import ConcreteBase, SteelBase

# Imports from utils library
from ....utils.units import mm, inch
from ....utils.misc import PRECISION


class RebarData(BaseModel):
    """Abstract base class representing a steel material.

    Attributes
    ----------
    beam_long_bar_diameters : List[float]
        Possible beam longitudinal bar diameters.
    beam_trans_bar_diameters : List[float]
        Possible beam transverse bar diameters.
    beam_trans_bar_spacings : List[float]
        Possible beam transverse bar spacings.
    column_long_bar_diameters : List[float]
        Possible column longitudinal bar diameters.
    column_trans_bar_diameters : List[float]
        Possible column transverse bar diameters.
    column_trans_bar_spacings : List[float]
        Possible column transverse bar spacings.
    units : Literal['mm', 'in']
        Units of bar diameters and spacing.
    """
    beam_longitudinal_bar_diameters: List[float]
    """Possible beams longitudinal bar diameters (nominal)."""
    beam_transverse_bar_diameters: List[float]
    """Possible beams transverse bar diameters (nominal)."""
    beam_transverse_bar_spacings: List[float]
    """Possible beams transverse bar spacings."""
    column_longitudinal_bar_diameters: List[float]
    """Possible columns longitudinal bar diameters (nominal)."""
    column_transverse_bar_diameters: List[float]
    """Possible columns transverse bar diameters (nominal)."""
    column_transverse_bar_spacings: List[float]
    """Possible columns transverse bar spacings."""
    units: Literal['mm', 'in']
    """Units of bar diameters and spacing."""


class RebarsBase(ABC):
    """The abstract base class for RebarDetailer.

    The class is used to determine rebar solutions for elements.
    The functions within RebarDetailer are very important because this is
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
    _data_path: Path | str
    """Path to the json file containing rebar data."""
    beam_long_bar_diams: np.ndarray
    """Possible beam longitudinal bar diameters."""
    beam_trans_bar_diams: np.ndarray
    """Possible beam transverse bar diameters."""
    beam_trans_bar_spacings: np.ndarray
    """Possible beam transverse bar spacings."""
    col_long_bar_diams: np.ndarray
    """Possible column longitudinal bar diameters."""
    col_trans_bar_diams: np.ndarray
    """Possible column transverse bar diameters."""
    col_trans_bar_spacings: np.ndarray
    """Possible column transverse bar spacings."""
    concrete: ConcreteBase
    """Concrete material instance considered in design of beams and columns."""
    steel: SteelBase
    """Steel material instance considered in design of beams and columns."""
    beam_max_sbl: float = 2000*mm
    """Maximum spacing between longitudinal bars (reinforcement) for beams."""
    beam_min_sbl: float = 40*mm
    """Minimum spacing between longitudinal bars (reinforcement) for beams."""
    beam_max_leg_dist: float = 2000*mm
    """For beams, maximum distance between longitudinal bars within a beam
    section that can be considered to be confined without the need to have
    an extra stirrup leg around them."""
    beam_cover: float = 30*mm
    """Concrete cover for beams."""
    col_max_sbl: float = 2000*mm
    """Maximum spacing between longitudinal bars (reinforcement) for columns.
    """
    col_min_sbl: float = 35*mm
    """Minimum spacing between longitudinal bars (reinforcement) for columns.
    """
    col_max_leg_dist: float = 2000*mm
    """Maximum distance between longitudinal bars within a column
    section that can be considered to be confined without the need to have
    an extra stirrup leg around them."""
    col_cover: float = 30*mm
    """Concrete cover for columns."""

    def __init__(self) -> None:
        """Initialize the available bar diameters, and transf, bar spacing.
        """
        with open(self._data_path, 'r') as json_file:
            # Load the JSON data into a Python dictionary
            data = json.load(json_file)
        # Check data with pydantic model
        model = RebarData(**data)
        if model.units == 'mm':
            self.beam_long_bar_diams = mm * np.array(
                model.beam_longitudinal_bar_diameters)
            self.beam_trans_bar_diams = mm * np.array(
                model.beam_transverse_bar_diameters)
            self.beam_trans_bar_spacings = mm * np.array(
                model.beam_transverse_bar_spacings)
            self.col_long_bar_diams = mm * np.array(
                model.column_longitudinal_bar_diameters)
            self.col_trans_bar_diams = mm * np.array(
                model.column_transverse_bar_diameters)
            self.col_trans_bar_spacings = mm * np.array(
                model.column_transverse_bar_spacings)
        elif model.units == 'in':
            self.beam_long_bar_diams = inch * np.array(
                model.beam_longitudinal_bar_diameters)
            self.beam_trans_bar_diams = inch * np.array(
                model.beam_transverse_bar_diameters)
            self.beam_trans_bar_spacings = inch * np.array(
                model.beam_transverse_bar_spacings)
            self.col_long_bar_diams = inch * np.array(
                model.column_longitudinal_bar_diameters)
            self.col_trans_bar_diams = inch * np.array(
                model.column_transverse_bar_diameters)
            self.col_trans_bar_spacings = inch * np.array(
                model.column_transverse_bar_spacings)
        # Sort data
        self.beam_long_bar_diams.sort()
        self.beam_trans_bar_diams.sort()
        self.beam_trans_bar_spacings[::-1].sort()  # descending order
        self.col_long_bar_diams.sort()
        self.col_trans_bar_diams.sort()
        self.col_trans_bar_spacings[::-1].sort()  # descending order

    def _get_min_beam_dbh(self, **kwargs) -> float | np.ndarray:
        """Gets the minimum transverse reinforcement diameter in beams.

        Returns
        -------
        float | np.ndarray
            Minimum transverse reinforcement diameter.
        """
        dbl = kwargs['dbl']
        return np.maximum(dbl/4, 6*mm)

    def _get_min_col_dbh(self, **kwargs) -> float | np.ndarray:
        """Gets the minimum transverse reinforcement diameter in columns.

        Returns
        -------
        float | np.ndarray
            Minimum transverse reinforcement diameter.
        """
        dbl = kwargs['dbl']
        return np.maximum(dbl/4, 6*mm)

    def _get_col_max_sbh(self, **kwargs) -> float | np.ndarray:
        """Gets maximum spacing between horizontal bars
        (transverse reinforcement) for columns.

        Returns
        -------
        float | np.ndarray
            Maximum spacing between transverse reinforcement.
        """
        # maximum allowed spacing in current iteration
        by = kwargs['by']  # column width along y
        bx = kwargs['bx']  # column width along x
        dbl = kwargs['dbl']  # long. reinf. diameter
        max_sbh = np.minimum(
            np.minimum(by, bx), 12*dbl
        )
        return max_sbh

    def _get_beam_max_sbh(self, **kwargs) -> float | np.ndarray:
        """Gets maximum spacing between horizontal bars
        (transverse reinforcement) for beams.

        Returns
        -------
        float | np.ndarray
            Maximum spacing between transverse reinforcement.
        """
        # maximum allowed spacing in current iteration
        h = kwargs['h']  # beam depth
        dbh = kwargs['dbh']  # transverse reinf. diameter
        dbl = kwargs['dbl']  # long. reinf. diameter
        max_sbh = np.minimum(
            np.minimum(250*mm, h),
            np.minimum(24*dbh, 12*dbl)
        )
        return max_sbh

    def get_beam_long_rebars(
        self, Asl_top: np.ndarray, Asl_bot: np.ndarray, b: np.ndarray
    ) -> tuple[np.ndarray]:
        """Selects the longitudinal reinforcement solution for a generic
        beam with dimension `b` and `h` over an alignment with N sections.

        Parameters
        ----------
        Asl_top : np.ndarray
            Required longitudinal reinforcement area at top.
        Asl_bot : np.ndarray
            Required longitudinal reinforcement area at bottom.
        b : float
            Beam breadth (width).

        Returns
        -------
        dbl_t1 : np.ndarray
            Diameter of 1st type of longitudinal bars at top.
        nbl_t1 : np.ndarray
            Number of 1st type of longitudinal bars at top.
        dbl_t2 : np.ndarray
            Diameter of 2nd type of longitudinal bars at top.
        nbl_t2 : np.ndarray
            Number of 2nd type of longitudinal bars at top.
        dbl_b1 : np.ndarray
            Diameter of 1st type of longitudinal bars at bottom.
        nbl_b1 : np.ndarray
            Number of 1st type of longitudinal bars at bottom.
        dbl_b2 : np.ndarray
            Diameter of 2nd type of longitudinal bars at bottom.
        nbl_b2 : np.ndarray
            Number of 2nd type of longitudinal bars at bottom.

        Abbreviations for rebars
        ------------------------
        - b: rebar, bar, reinforcement
        - l: longitudinal
        - h: horizontal (transverse)
        - n: number of
        - d: diameter

        Assumptions
        -----------
        - Always starts with top reinforcement
        - At top or bottom of the beam sections at most two type of bars can
        be used (e.g., dbl_t1, dbl_t2, dbl_b1, dbl_b2).
        - The diameter of 1st type long. bar is always greater than or equal to
        the diameter of 2nd type long. bar (dbl1 >= dbl2). Even if 2nd diam is
        smaller, choose the closest one to dbl1 from the available bars.
        - dbl1's and dbl2's at bottom and top parts of the sections do not
        necessarily have to be the same. (e.g., dbl_t1=0.020, dbl_b1=0.025)
        - Along the beam which is continuous over the multiple spans maximum of
        two rebar diameter is allowed.
        - At the two ends of beam sections, the provided reinforcement could be
        different.
        - Number of 1st type longitudinal bars is equal for all the sections.
        Number of 1st type longitudinal bars at bottom and also at top
        can be minimum of two. Hence, at least four corner bars of 1st type
        are provided.

        Example section
        ---------------
                   Y
                   ^
                   |
        -----------------------     -------------
        | #t1  #t2   #t2  #t1 |     |   -- cover
        |                     |     |
        |                     |     |
        |          +          |     h
        |                     |     |
        |                     |     |
        | #b1 #b2 #b1 #b2 #b1 |     |   -- cover
        -----------------------     -------------  ----> X
        |--------- b ---------|

        Asl_top = 2.Ab_#t1 + 2.Ab_#t2
        Asl_bot = 3.Ab_#b1 + 2.Ab_#b2

        Number of unique diameter values at a section can be one or two
        unique(db_#t1), db_#t2), db_#b1), db_#b2)) = (dbl_1, dbl_2)
        OR
        unique(db_#t1), db_#t2), db_#b1), db_#b2)) = dbl

        TODO
        ----
        1. Allow use of 3rd diameter for longitudinal reinforcement
        2. Possibly limit the number of #t1's and #b1's to 2 (corner bars only)
        3. Enforce continuous #t1 and #b1 (corner bars) in all beam sections.
        """
        def get_two_type_long_bar_solution(
            Asl_req: np.ndarray, nbl_1: int, dbl_1: float, dbl_2: float,
            min_nbl_2: int | None = None
        ) -> tuple[np.ndarray]:
            """Determine the long. reinf. solution with two type of bars.

            Parameters
            ----------
            Asl_req : np.ndarray
                Required longitudinal reinforcement area.
            nbl_1 : int
                Number of 1st type longitudinal bars.
            dbl_1 : float
                Diameter of 1st type longitudinal bars.
            dbl_2 : float
                Diameter of 2nd type longitudinal bars.
            min_nbl_2 : int | None, optional
                Minimum number of 2nd type longitudinal bars, by default None.

            Returns
            -------
            nbl_2 : np.ndarray
                Number of 2nd type longitudinal bars per section.
            Asl_rat : np.ndarray
                Ratio of long. reinf. area to required area per section.
            """
            # Minimum transverse reinforcement diameter
            dbh_min = self._get_min_beam_dbh(dbl=max(dbl_1, dbl_2))
            # Assumed transverse reinf. diam. for long. bar arrangement
            diff = self.beam_trans_bar_diams - dbh_min
            dbh = self.beam_trans_bar_diams[np.where(diff >= 0)[0][0]]

            if min_nbl_2 is None:
                min_nbl_2 = nbl_1-1
            nbl_2 = np.maximum(
                np.ceil((Asl_req - nbl_1*Ab_dict[dbl_1]) / Ab_dict[dbl_2]),
                min_nbl_2)
            distx = np.round((b -
                             (nbl_1*dbl_1 + nbl_2*dbl_2 + 2*self.beam_cover
                              + 2*dbh)) / (nbl_1 + nbl_2 - 1), PRECISION)
            # Increase num rebars to not exceed max spacing limit
            for i in np.where(distx > self.beam_max_sbl)[0].tolist():
                while distx[i] > self.beam_max_sbl:
                    nbl_2[i] += 1
                    distx[i] = (b[i] - (nbl_1*dbl_1 + nbl_2[i]*dbl_2
                                        + 2*self.beam_cover + 2*dbh)
                                ) / (nbl_1 + nbl_2[i] - 1)
                    distx = np.round(distx, PRECISION)
            Asl = nbl_1*Ab_dict[dbl_1] + nbl_2*Ab_dict[dbl_2]
            Asl_rat = np.divide(Asl, Asl_req,
                                out=np.full_like(Asl, 1e2),
                                where=Asl_req != 0)
            Asl_rat[distx < self.beam_min_sbl] = 1000

            return nbl_2, Asl_rat

        """
        INITIALIZATION
        """
        # Number of beam sections
        num_sec = len(Asl_top)
        # Maximum number of #1 bars
        max_nbl_1 = 4
        # Rebar area for given longitudinal bar diameters
        Ab_dict = {db: np.pi * (db**2) * 0.25
                   for db in self.beam_long_bar_diams}

        """
        1) TOP LONGITUDINAL REBARS (TOP FLEXURAL REINFORCEMENT)
        """
        top_Asl_rat_dict = {}  # Ratio of top long. reinf. to required area
        nbl_t2_dict = {}  # Number of #t2 long. reinf. bars per solution
        # ...........................................................................
        # 1.A) Solutions with only one diameter (#1t)
        # ...........................................................................
        m = 2
        n_min = 0
        for dbl in self.beam_long_bar_diams:
            key = f"{m}dbl1{dbl}_dbl2{dbl}"
            n, Asl_rat = get_two_type_long_bar_solution(
                Asl_req=Asl_top, nbl_1=m, dbl_1=dbl, dbl_2=dbl,
                min_nbl_2=n_min)
            top_Asl_rat_dict[key] = Asl_rat
            nbl_t2_dict[key] = n
        # ...........................................................................
        # 1.B) Solutions with m #1t and n #2t bars with lower diameter
        # ...........................................................................
        for i, dbl_1 in enumerate(self.beam_long_bar_diams[1:], 1):
            # Using the previous one as lower bar diameter
            dbl_2 = self.beam_long_bar_diams[i-1]
            # TODO: Alternatively iterate for all lower rebars
            # for db2 in self.long_bar_diams[:i]:

            for m in range(2, max_nbl_1+1, 1):
                n, Asl_rat = get_two_type_long_bar_solution(
                    Asl_req=Asl_top, nbl_1=m, dbl_1=dbl_1, dbl_2=dbl_2)
                key = f"{m}dbl1{dbl_1}_dbl2{dbl_2}"
                nbl_t2_dict[key] = n
                top_Asl_rat_dict[key] = Asl_rat
        # ...........................................................................
        # 1.C) Find solutions based on ratio of available and required areas
        # ...........................................................................
        err_top = {key: np.sum(rat) for key, rat in top_Asl_rat_dict.items()}
        best_top: str = min(err_top, key=err_top.get)
        dbl_top1 = float(best_top.split('_')[0].split('dbl1')[1])
        dbl_top2 = float(best_top.split('_')[1].split('dbl2')[1])
        nbl_top1 = int(best_top.split('_')[0].split('dbl1')[0])
        dbl_t1 = dbl_top1 * np.ones(num_sec)
        nbl_t1 = np.full(num_sec, nbl_top1)
        dbl_t2 = dbl_top2 * np.ones(num_sec)
        nbl_t2 = nbl_t2_dict[best_top]

        """
        2) BOTTOM LONGITUDINAL REBARS (BOTTOM FLEXURAL REINFORCEMENT)
        """
        bot_Asl_rat_dict = {}  # Ratio of bot long. reinf. to required area
        nbl_b2_dict = {}  # Number of #b2 long. reinf. bars per solution

        # Add solutions with only one diameter
        m = 2
        n_min = 0
        for dbl in self.beam_long_bar_diams:
            # Must have maximum of two different rebar diameters
            bool1 = dbl_top1 == dbl_top2
            bool2 = dbl_top1 == dbl
            bool3 = dbl_top2 == dbl
            if bool1 or bool2 or bool3:
                key = f"{m}dbl1{dbl}_dbl2{dbl}"
                n, Asl_rat = get_two_type_long_bar_solution(
                    Asl_req=Asl_bot, nbl_1=m, dbl_1=dbl, dbl_2=dbl,
                    min_nbl_2=n_min)
                bot_Asl_rat_dict[key] = Asl_rat
                nbl_b2_dict[key] = n

        # Add solutions with two diameters
        dbl_1 = dbl_top1  # Use the same big bar (#1)
        if dbl_top1 != dbl_top2:  # no other rebar option
            dbl_2 = dbl_top2
            for m in range(2, max_nbl_1+1, 1):
                n, Asl_rat = get_two_type_long_bar_solution(
                    Asl_req=Asl_bot, nbl_1=m,
                    dbl_1=dbl_1, dbl_2=dbl_2)
                key = f"{m}dbl1{dbl_1}_dbl2{dbl_2}"
                nbl_b2_dict[key] = n
                bot_Asl_rat_dict[key] = Asl_rat
        else:   # no other rebar options are possible
            # Using the previous one as lower bar diameter
            i = np.where(self.beam_long_bar_diams == dbl_1)[0][0]
            dbl_2 = self.beam_long_bar_diams[i-1]
            # TODO: Alternatively iterate for all lower rebars
            # for db2 in self.long_bar_diams[:i]:

            for m in range(2, max_nbl_1+1, 1):
                n, Asl_rat = get_two_type_long_bar_solution(
                    Asl_req=Asl_bot, nbl_1=m,
                    dbl_1=dbl_1, dbl_2=dbl_2)
                key = f"{m}dbl1{dbl_1}_dbl2{dbl_2}"
                nbl_b2_dict[key] = n
                bot_Asl_rat_dict[key] = Asl_rat

        err_bot = {key: np.sum(rat)
                   for key, rat in bot_Asl_rat_dict.items()}
        best_bot: str = min(err_bot, key=err_bot.get)
        dbl_bot1 = float(best_bot.split('_')[0].split('dbl1')[1])
        dbl_bot2 = float(best_bot.split('_')[1].split('dbl2')[1])
        nbl_bot1 = int(best_bot.split('_')[0].split('dbl1')[0])
        dbl_b1 = dbl_bot1 * np.ones(num_sec)
        nbl_b1 = np.full(num_sec, nbl_bot1)
        dbl_b2 = dbl_bot2 * np.ones(num_sec)
        nbl_b2 = nbl_b2_dict[best_bot]

        return (dbl_t1, nbl_t1, dbl_t2, nbl_t2,
                dbl_b1, nbl_b1, dbl_b2, nbl_b2)

    def get_beam_transv_rebars(
        self, Ash_sbh: np.ndarray, nbl_t1: np.ndarray, nbl_t2: np.ndarray,
        nbl_b1: np.ndarray, nbl_b2: np.ndarray, dbl_t1: np.ndarray,
        dbl_b1: np.ndarray, b: np.ndarray, h: np.ndarray
    ) -> tuple[np.ndarray]:
        """
        Selects transverse reinforcement solution for a generic beam with
        dimension `b` and `h` over an alignment with N sections.

        Parameters
        ----------
        Ash_sbh : np.ndarray
            Required transverse reinforcement area to spacing ratio.
        nbl_t1 : np.ndarray
            Number of 1st type of longitudinal bars at top.
        nbl_t2 : np.ndarray
            Number of 2nd type of longitudinal bars at top.
        nbl_b1 : np.ndarray
            Number of 1st type of longitudinal bars at bottom.
        nbl_b2 : np.ndarray
            Number of 2nd type of longitudinal bars at bottom.
        dbl_t1 : np.ndarray
            Diameter of 1st type of longitudinal bars at top.
        dbl_b1 : np.ndarray
            Diameter of 1st type of longitudinal bars at bottom.
        b : float
            Beam breadth (width).
        h : float
            Beam height (depth).

        Returns
        -------
        dbh : np.ndarray
            Diameter of horizontal bars (transverse reinforcement).
        sbh : np.ndarray
            Spacing of horizontal bars (transverse reinforcement).
        nbh_parallel_b : np.ndarray
            Number of horizontal bars (stirrup legs) parallel to width.
        nbh_parallel_h : np.ndarray
            Number of horizontal bars (stirrup legs) parallel to height.

        Abbreviations for rebars
        ------------------------
        - The same of `get_beam_long_rebars`.

        Assumptions
        -----------
        - The same of `get_beam_long_rebars`.
        """
        # Initialization
        num_sec = len(Ash_sbh)  # Number of beam sections
        nbh_x = 2*np.ones(num_sec)  # no. of legs parallel to width (always 2)
        nbh_y = np.zeros(num_sec)  # no. of legs parallel to height
        sbh = np.zeros(num_sec)  # transverse reinforcement (bar) spacing
        dbh = np.zeros(num_sec)  # transverse reinforcement (bar) diameter
        # Maximum possible number of legs (bars) parallel to height
        max_nbh_y = np.minimum(nbl_t1+nbl_t2, nbl_b1+nbl_b2)
        # Minimum transverse reinforcement diameter
        dbh_min = self._get_min_beam_dbh(dbl=np.maximum(dbl_t1, dbl_b1))
        for j in range(num_sec):
            # Initial assumptions for number of legs and diameters
            nbh = 2  # start with closed stirrup
            leg_conf_dist = 0.9 * b[j] / (nbh - 1)
            while leg_conf_dist > self.beam_max_leg_dist:
                nbh += 1  # add stirrup
                leg_conf_dist = 0.9 * b[j] / (nbh - 1)
            # No. of stirrup legs parallel to height
            nbh_y[j] = nbh
            # Current transverse reinforcement diameter
            diff = self.beam_trans_bar_diams - dbh_min[j]
            dbh[j] = self.beam_trans_bar_diams[np.where(diff >= 0)[0][0]]
            # maximum allowed spacing in current iteration
            max_sbh = self._get_beam_max_sbh(
                b=b[j], h=h[j], dbh=dbh[j],
                dbl=dbl_t1[j], cover=self.beam_cover)
            max_sbh = np.round(max_sbh, PRECISION)

            # Iterate for a solution
            iterate = True
            while iterate:
                # total transverse reinforcement area along y
                Ashy = 0.25 * np.pi * nbh_y[j] * dbh[j]**2
                if Ash_sbh[j] == 0.0:
                    sbhy = self.beam_trans_bar_spacings[0]
                else:
                    sbhy = Ashy / Ash_sbh[j]
                sbh[j] = min(sbhy, max_sbh)  # current spacing
                for spacing in self.beam_trans_bar_spacings:
                    if sbh[j] >= spacing:
                        sbh[j] = spacing  # This spacing works for this section
                        iterate = False  # Stop iterating for this section
                        break  # break the for loop

                if iterate:
                    if sbh[j] == sbhy and np.all(nbh_y[j] <= max_nbh_y[j]):
                        # add a stirrup leg along y
                        nbh_y[j] += 1
                    elif iterate and dbh[j] < max(self.beam_trans_bar_diams):
                        # increase transverse reinforcement diameter
                        idx = np.where(
                            self.beam_trans_bar_diams == dbh[j])[0][0]
                        dbh[j] = self.beam_trans_bar_diams[idx+1]
                    elif iterate:
                        # Accept the underdesign, no solution is found.
                        nbh_y[j] = max_nbh_y[j]
                        sbh[j] = min(self.beam_trans_bar_spacings)
                        dbh[j] = max(self.beam_trans_bar_diams)
                        iterate = False

        return dbh, sbh, nbh_x, nbh_y

    def get_column_long_rebars(
            self, Aslx_req: np.ndarray, Asly_req: np.ndarray,
            rhol_min: np.ndarray, bx: np.ndarray, by: np.ndarray
    ) -> tuple[np.ndarray]:
        """Selects the longitudinal and transverse reinforcement solution for a
        generic column with dimension `bx` and `by` over an alignment with
        N sections.

        Parameters
        ----------
        Aslx_req : np.ndarray
            Required longitudinal reinforcement area at
            bottom or top side of the section, In other words,
            required area of bars distributed along -x on one side.
        Asly_req : np.ndarray
            Required longitudinal reinforcement area at
            left or right side of the section. In other words,
            required area of bars distributed along -y on one side.
        rhol_min : np.ndarray
            Minimum longitudinal reinforcement ratio.
        bx : np.ndarray
            Breadth (width) along global -x axis.
        by : np.ndarray
            Breadth (width) along global -y axis.

        Returns
        -------
        dbl_c : np.ndarray
            Diameter of corner longitudinal bars.
        dbl_i : np.ndarray
            Diameter of internal longitudinal bars
        nbl_ix : np.ndarray
            Number of internal longitudinal bars (reinforcement) at
            bottom or top side of the section. In other words,
            half of the total number of internal longitudinal bars
            distributed along X (on one side of the section).
        nbl_iy : np.ndarray
            Number of internal longitudinal bars (reinforcement) at
            left or right side of the section. In other words,
            half of the total number of internal longitudinal bars
            distributed along Y (on one side of the section).
        dbh : np.ndarray
            Diameter of horizontal bars (transverse reinforcement).
        sbh : np.ndarray
            Spacing of horizontal bars (transverse reinforcement).
        nbh_x : np.ndarray
            Number of horizontal bars (stirrup legs) along -x axis.
        nbh_y : np.ndarray
            Number of horizontal bars (stirrup legs) along -y axis.

        Abbreviations for rebars
        ------------------------
        b: rebar, bar, reinforcement
        l: longitudinal
        h: horizontal (transverse)
        n: number of
        d: diameter
        i: internal
        c: corner

        Assumptions
        -----------
        - All corner bars have the same diameter.
        - Corner bars are continuous over the sections.
        - All internal bars have the same diameter.
        - Internal bars may or may not be continuous.
        - Internal bars can have either the same diameters as corner bars or
        can have a smaller diameter which is still closest to the corner one.

        Example section
        ---------------
                   Y
                   ^
                   |
        -----------------------     -------------
        | #c    #i    #i   #c |     |  ---- cover
        |                     |     |
        | #i               #i |     |
        |                     |     |
        | #i       +       #i |     by
        |                     |     |
        | #i               #i |     |
        |                     |     |
        | #c    #i    #i   #c |     |  ---- cover
        -----------------------     -------------  ----> X
        |-------- bx ---------|

        Aslx_req = 2.Ab_#c + 2.Ab_#i
        Asly_req = 2.Ab_#c + 3.Ab_#i

        Number of unique diameter values at a section can be one or two
        unique(db_#c, db_#i) = (dbl_c, dbl_i)
        OR
        unique(db_#c, db_#i) = dbl_c
        """

        def get_two_type_long_bar_solution(
            Aslx_req: np.ndarray, Asly_req: np.ndarray,
            nbl_1x: int, nbl_1y: int, dbl_1: float, dbl_2: float,
            min_nbl_2: int
        ) -> tuple[np.ndarray]:
            """Determine the long. reinf. solution with two type of bars.

            Parameters
            ----------
            Aslx_req : np.ndarray
                Required longitudinal reinforcement area at
                bottom or top side of the section, In other words,
                required area of bars distributed along -x on one side.
            Asly_req : np.ndarray
                Required longitudinal reinforcement area at
                left or right side of the section. In other words,
                required area of bars distributed along -y on one side.
            nbl_1x : int
                Number of 1st type longitudinal bars at bottom or top side of
                the section.
            nbl_1y : int
                Number of 1st type longitudinal bars at left or right side of
                the section.
            dbl_1 : float
                Diameter of 1st type longitudinal bars.
            dbl_2 : float
                Diameter of 2nd type longitudinal bars.
            min_nbl_2 : int
                Minimum number of 2nd type longitudinal bars.

            Returns
            -------
            nbl_2x : int
                Number of 2nd type longitudinal bars at bottom or top side
                of the section.
            nbl_2y : int
                Number of 2nd type longitudinal bars at left or right side
                of the section.
            Asl : np.ndarray
                Total longitudinal reinforcement area per section.
            """
            # Minimum transverse reinforcement diameter
            dbh_min = self._get_min_col_dbh(dbl=dbl_c)
            # Assumed transverse reinf. diam. for long. bar arrangement
            diff = self.col_trans_bar_diams - dbh_min
            dbh = self.col_trans_bar_diams[np.where(diff >= 0)[0][0]]

            # Number of bars with 2nd diameter
            nbl_2x = np.maximum(
                np.ceil((Aslx_req - nbl_1x*Ab_dict[dbl_1]) / Ab_dict[dbl_2]),
                min_nbl_2)
            nbl_2y = np.maximum(
                np.ceil((Asly_req - nbl_1y*Ab_dict[dbl_1]) / Ab_dict[dbl_2]),
                min_nbl_2)
            # Bar spacing
            dist_x = np.round((bx -
                              (nbl_1x*dbl_1 + nbl_2x*dbl_2 + 2*self.col_cover +
                               2*dbh)) / (nbl_1x + nbl_2x - 1), PRECISION)
            dist_y = np.round((by -
                              (nbl_1y*dbl_1 + nbl_2y*dbl_2 + 2*self.col_cover +
                               2*dbh)) / (nbl_1y + nbl_2y - 1), PRECISION)

            # Increase num rebars along X to not exceed max spacing limit
            for i in np.where(dist_x > self.col_max_sbl)[0].tolist():
                while dist_x[i] > self.col_max_sbl[i]:
                    nbl_2x[i] += 1
                    dist_x[i] = (bx[i] - (nbl_1x*dbl_1 + nbl_2x[i]*dbl_2
                                          + 2*self.col_cover + 2*dbh)
                                 ) / (nbl_1x + nbl_2x[i] - 1)
                    dist_x = np.round(dist_x, PRECISION)
            # Increase num rebars along Y to not exceed max spacing limit
            for i in np.where(dist_y > self.col_max_sbl)[0].tolist():
                while dist_y[i] > self.col_max_sbl[i]:
                    nbl_2y[i] += 1
                    dist_y[i] = (by[i] - (nbl_1y*dbl_1 + nbl_2y[i]*dbl_2
                                          + 2*self.col_cover + 2*dbh)
                                 ) / (nbl_1y + nbl_2y[i] - 1)
                    dist_y = np.round(dist_y, PRECISION)

            # Compute total bar area
            Aslx = nbl_1x*Ab_dict[dbl_1] + nbl_2x*Ab_dict[dbl_2]
            Asly = nbl_1y*Ab_dict[dbl_1] + nbl_2y*Ab_dict[dbl_2]
            Asl = 2*(Aslx + Asly) - 4*Ab_dict[dbl_1]
            Asl_min = rhol_min * bx * by
            # Check for min. long. reinf. and increase reinf.
            for i in np.where(Asl_min > Asl)[0].tolist():
                while Asl_min[i] > Asl[i]:
                    if Aslx[i]/Asly[i] > bx[i]/by[i]:
                        nbl_2x[i] += 1
                        dist_x[i] = (bx[i] - (nbl_1x*dbl_1 + nbl_2x[i]*dbl_2
                                              + 2*self.col_cover + 2*dbh)
                                     ) / (nbl_1x + nbl_2x[i] - 1)
                        dist_x = np.round(dist_x, PRECISION)
                    else:
                        nbl_2y[i] += 1
                        dist_y[i] = (by[i] - (nbl_1y*dbl_1 + nbl_2y[i]*dbl_2
                                              + 2*self.col_cover + 2*dbh)
                                     ) / (nbl_1y + nbl_2y[i] - 1)
                        dist_y = np.round(dist_y, PRECISION)

                    Aslx[i] = nbl_1x*Ab_dict[dbl_1] + nbl_2x[i]*Ab_dict[dbl_2]
                    Asly[i] = nbl_1y*Ab_dict[dbl_1] + nbl_2y[i]*Ab_dict[dbl_2]
                    Asl[i] = 2*(Aslx[i] + Asly[i]) - 4*Ab_dict[dbl_1]

            # Penalize the solution if it does not respect the spacing limit
            Asl[dist_x < self.col_min_sbl] = 1e4
            Asl[dist_y < self.col_min_sbl] = 1e4
            # Return solutions
            return nbl_2x, nbl_2y, Asl

        """
        INITIALIZATION
        """
        # Number of column sections
        num_sec = len(Aslx_req)
        # Rebar area for given longitudinal bar diameters
        Ab_dict = {db: np.pi * (db**2) * 0.25
                   for db in self.col_long_bar_diams}
        Asl_dict = {}  # Longitudinal reinforcement area for solutions
        # Internal long. reinf. bars distributed along -x per solution
        nbl_ix_dict = {}
        # Internal long. reinf. bars distributed along -y per solution
        nbl_iy_dict = {}
        # Get rebar solutions
        # NOTE: Assume internal bars will have same diameter,
        # and only corner bars could be different (and bigger)
        nbl_cx = 2
        nbl_cy = 2
        min_nbl_i = 0
        for i, dbl_c in enumerate(self.col_long_bar_diams):
            for dbl_i in reversed(self.col_long_bar_diams[max(i-1, 0):i+1]):
                key = f"dblc{dbl_c}_dbli{dbl_i}"
                nbl_ix, nbl_iy, Asl = get_two_type_long_bar_solution(
                    Aslx_req, Asly_req, nbl_cx, nbl_cy, dbl_c, dbl_i,
                    min_nbl_i)
                Asl_dict[key] = Asl
                nbl_ix_dict[key] = nbl_ix
                nbl_iy_dict[key] = nbl_iy
        # Get the final soltuion based on the lowest total bar area
        # NOTE: The issue is that we do not really check the compatibility of
        # columns e.g., for lap-splices
        area = {key: np.sum(Asl) for key, Asl in Asl_dict.items()}
        best: str = min(area, key=area.get)
        dbl_c = float(best.split('_')[0].split('dblc')[1])
        dbl_i = float(best.split('_')[1].split('dbli')[1])
        dbl_c = dbl_c * np.ones(num_sec)
        dbl_i = dbl_i * np.ones(num_sec)
        nbl_ix = nbl_ix_dict[best]
        nbl_iy = nbl_iy_dict[best]

        return dbl_c, dbl_i, nbl_ix, nbl_iy

    def get_column_transv_rebars(
            self, bx: np.ndarray, by: np.ndarray,
            Ashx_sbh_req: np.ndarray, Ashy_sbh_req: np.ndarray,
            dbl_c: np.ndarray, nbl_ix: np.ndarray, nbl_iy: np.ndarray
    ) -> tuple[np.ndarray]:
        """Selects transverse (horizontal/shear) reinforcement solution
        for a generic column with dimension `bx` and `by` over an alignment
        with N sections.

        Parameters
        ----------
        bx : np.ndarray
            Breadth (width) along global -x axis.
        by : np.ndarray
            Breadth (width) along global -y axis.
        Ashx_sbh_req : np.ndarray
            Required ratio of transverse reinforcement area along -x
            axis (i.e., parallel to -x axis) to the bar spacing.
        Ashy_sbh_req : np.ndarray
            Required ratio of transverse reinforcement area along -y
            axis (i.e., parallel to -y axis) to the bar spacing.
        dbl_c : np.ndarray
            Diameter of corner longitudinal bars.
        nbl_ix : np.ndarray
            Number of internal longitudinal bars (reinforcement) at
            bottom or top side of the section. In other words,
            half of the total number of internal longitudinal bars
            distributed along X (on one side of the section).
        nbl_iy : np.ndarray
            Number of internal longitudinal bars (reinforcement) at
            left or right side of the section. In other words,
            half of the total number of internal longitudinal bars
            distributed along Y (on one side of the section).

        Returns
        -------
        dbh : np.ndarray
            Diameter of horizontal bars (transverse reinforcement).
        sbh : np.ndarray
            Spacing of horizontal bars (transverse reinforcement).
        nbh_x : np.ndarray
            Number of horizontal bars (stirrup legs) along -x axis.
        nbh_y : np.ndarray
            Number of horizontal bars (stirrup legs) along -y axis.

        Abbreviations for rebars
        ------------------------
        - The same of `get_column_long_rebars`.

        Assumptions
        -----------
        - The same of `get_column_long_rebars`.
        """
        # Initialization
        nbl_cy = 2  # Number of corner bars parallel to y-axis on one side
        nbl_cx = 2  # Number of corner bars parallel to x-axis on one side
        num_sec = len(Ashx_sbh_req)  # Number of column sections
        nbh_x = 2 * np.ones(num_sec)  # no. of legs parallel to x-axis
        nbh_y = 2 * np.ones(num_sec)  # no. of legs parallel to y-axis
        sbh = np.zeros(num_sec)  # transverse reinforcement (bar) spacing
        dbh = np.zeros(num_sec)  # transverse reinforcement (bar) diameter
        # Maximum possible number of legs (bars)
        max_nbh_x = nbl_cy + nbl_iy
        max_nbh_y = nbl_cx + nbl_ix
        # Minimum transverse reinforcement diameter
        dbh_min = self._get_min_col_dbh(dbl=dbl_c)
        for j in range(num_sec):
            # Initial no. of stirrup legs parallel to x-axis
            nbh_x[j] = 2  # start with closed stirrup
            leg_conf_dist_x = 0.9 * by[j] / (nbh_x[j] - 1)
            while leg_conf_dist_x > self.col_max_leg_dist:
                nbh_x[j] += 1  # add stirrup leg
                leg_conf_dist_x = 0.9 * by[j] / (nbh_x[j] - 1)
            # Initial no. of stirrup legs parallel to y-axis
            nbh_y[j] = 2  # start with closed stirrup
            leg_conf_dist_y = 0.9 * bx[j] / (nbh_y[j] - 1)
            while leg_conf_dist_y > self.col_max_leg_dist:
                nbh_y[j] += 1  # add stirrup leg
                leg_conf_dist_y = 0.9 * bx[j] / (nbh_y[j] - 1)
            # Initial transverse reinforcement diameter
            diff = self.col_trans_bar_diams - dbh_min[j]
            dbh[j] = self.col_trans_bar_diams[np.where(diff >= 0)[0][0]]
            # maximum allowed spacing in current iteration
            max_sbh = self._get_col_max_sbh(
                bx=bx[j], by=by[j], dbh=dbh[j], dbl=dbl_c[j],
                cover=self.col_cover)
            max_sbh = np.round(max_sbh, PRECISION)

            # Iterate for a solution
            iterate = True
            while iterate:
                # total transverse reinforcement area
                Ashx = 0.25 * np.pi * nbh_x[j] * dbh[j]**2  # along x
                Ashy = 0.25 * np.pi * nbh_y[j] * dbh[j]**2  # along y
                # initial spacing of stirrups along the member
                if Ashx_sbh_req[j] == 0.0:
                    sbhx = self.col_trans_bar_spacings[0]
                else:
                    sbhx = Ashx / Ashx_sbh_req[j]
                if Ashy_sbh_req[j] == 0.0:
                    sbhy = self.col_trans_bar_spacings[0]
                else:
                    sbhy = Ashy / Ashy_sbh_req[j]
                sbh[j] = min(sbhx, sbhy, max_sbh)
                for spacing in self.col_trans_bar_spacings:
                    if sbh[j] >= spacing:
                        sbh[j] = spacing  # This spacing works for this section
                        iterate = False  # Stop iterating for this section
                        break  # break the for loop

                if iterate:
                    if sbh[j] == sbhy and np.all(nbh_y[j] <= max_nbh_y[j]):
                        # add a stirrup leg along y
                        nbh_y[j] += 1
                    elif sbh[j] == sbhx and np.all(nbh_x[j] <= max_nbh_x[j]):
                        # add a stirrup leg along x
                        nbh_x[j] += 1
                    elif dbh[j] < max(self.col_trans_bar_diams):
                        # increase transverse reinforcement diameter
                        idx = np.where(
                            self.col_trans_bar_diams == dbh[j])[0][0]
                        dbh[j] = self.col_trans_bar_diams[idx+1]
                    else:
                        # Accept the underdesign, no solution is found.
                        nbh_y[j] = max_nbh_y[j]
                        nbh_x[j] = max_nbh_x[j]
                        sbh[j] = min(self.col_trans_bar_spacings)
                        dbh[j] = max(self.col_trans_bar_diams)
                        iterate = False

        return dbh, sbh, nbh_x, nbh_y
