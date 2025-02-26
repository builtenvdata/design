"""
Base module for defining slabs in buildings.

Plan view of mesh objects (rectangle) representing slabs.

y
|__x
                l2(p2,p3)
   p2(x2,y2,z2) o------>o p3(x3,y3,z3)
                ^       ^
      l1(p1,p2) |       | l3(p4,p3)
                |       |
   p1(x1,y1,z1) o------>o p4(x4,y4,z4)
                l4(p1,p4)
pi: i'th Point
li: i'th Line
xi, yi, zi: Coordinates of i'th Point
"""

# Imports from installed packages
import numpy as np
from abc import ABC
from scipy.interpolate import interp1d
from typing import Literal, List

# Imports from bdim base library
from .loads import PermanentBase, VariableBase

# Imports from geometry library
from ...geometry.base import Rectangle

# Imports from utils library
from ....utils.misc import PRECISION


class SlabBase(ABC):
    """
    Abstract base class for slabs.

    Must be inherited by design class specific slabs.
    """
    rectangle: Rectangle
    """Geometric mesh representation of the slab (tag, points, lines)."""
    typology: Literal[1, 2, 3]
    """Slab typology
    1: Two-way solid slab.
    2: One-way solid slab.
    3: One-way composite slab with ceramic blocks and RC joists or
    pre-stressed beams."""
    _orientation: Literal[1, 2, 3]
    """Private attribute for slab unloading orientation."""
    _thickness: float
    """Private attribute for slab thickness (depth)."""
    gamma_rc: float
    """Unit weight of reinforced concrete."""
    pg: float
    """Permanent loads on unit slab area."""
    pq: float
    """Variable loads on unit slab area."""
    roof: bool
    """Flag for checking if located at roof level or not."""
    MAX_THICKNESS: float = 0.85
    """Maximum possible slab thickness, by default 0.85 m."""

    def __init__(
        self, rectangle: Rectangle, typology: Literal[1, 2, 3],
        thickness: float = None, orientation: Literal[1, 2, 3] = None
    ) -> None:
        """Initializes slab object.

        Parameters
        ----------
        rectangle : Rectangle
            Geometric mesh representation of the slab (tag, points, lines).
        typology : Literal[1, 2, 3]
            Slab typology
            1: Solid two-way cast-in-situ slabs (SS2)
            2: Solid one-way cast-in-situ slabs (SS1)
            3: Composite slabs with pre-fabricated joists and ceramic blocks
            (HS)
        thickness : float
            Slab thickness (depth), by default None.
        orientation : Literal[1, 2, 3], optional
            Orientation of slab load transfer to beams, by default None.
            1: Unloading in beams along X direction.
            2: Unloading in beams along Y direction.
            3: Unloading in beams along both directions.
        """
        self.rectangle = rectangle
        self.typology = typology
        self._thickness = thickness
        self._orientation = orientation

    @property
    def lx(self) -> float:
        """
        Returns
        -------
        float
            Slab length along global X-axis.
        """
        return self.rectangle.lines[1].length

    @property
    def ly(self) -> float:
        """
        Returns
        -------
        float
            Slab length along global Y-axis.
        """
        return self.rectangle.lines[0].length

    @property
    def area(self) -> float:
        """
        Returns
        -------
        float
            Total slab area.
        """
        return self.rectangle.area

    @property
    def pself(self) -> float:
        """
        Returns
        -------
        float
            Slab self-weight per unit area.

        Note
        ----
        The equation used for calculating the self-weight of HS slab is
        is obtained through regression analysis using the data provided
        by the manufacturers.

        References
        ----------
        https://presdouro.pt/wp-content/themes/presdouro/images/DT_PD2016_VALIDADO.pdf
        https://lajes.pavimir.pt/pdfs/DA%2060%20-%20Pavimentos%20Aligeirados.pdf
        """
        # Solid cast-in-situ slab
        if self.typology == 1 or self.typology == 2:
            return self.gamma_rc * self.t
        # Composite slab with pre-fabricated joists and ceramic blocks
        elif self.typology == 3:
            return 2.20 * np.log(self.t) + 6.50

    @property
    def beam_alpha_coeffs(self) -> List[float]:
        """
        Returns
        -------
        List[float]
            Alpha coefficients of four beams surrounding the slab.
        """
        if self.orientation == 3:
            long = max(self.lx, self.ly)
            short = min(self.lx, self.ly)
            ratio = float(short / long)
            alpha_l = self._get_alpha(ratio)
            alpha_s = self._get_alpha(1.0)
            if self.lx > self.ly:
                # Long span is along x
                return [alpha_s, alpha_l, alpha_s, alpha_l]
            else:
                # Long span is along y
                return [alpha_l, alpha_s, alpha_l, alpha_s]
        else:
            return [1.0, 1.0, 1.0, 1.0]

    @property
    def orientation(self) -> Literal[1, 2, 3]:
        """
        Returns
        -------
        Literal[1, 2, 3]
            Slab unloading orientation.
            1: Unloading in beams along X direction.
            2: Unloading in beams along Y direction.
            3: Unloading in beams along both directions.

        Notes
        -----
        One-way slab directions are always in the direction of the longer span.
        """
        if not self._orientation:
            if self.typology == 1:
                return 3
            elif self.lx / self.ly > 1.0:
                return 1
            else:
                return 2
        return self._orientation

    @orientation.setter
    def orientation(self, value=None) -> None:
        """Setter."""
        self._orientation = value

    @property
    def t(self) -> float:
        """
        Returns
        -------
        float
            Slab thickness (depth).

        Note
        ----
        The equation used for calculating the thickness of HS slab is
        is obtained through regression analysis using the data provided
        by the manufacturers.

        References
        ----------
        https://presdouro.pt/wp-content/themes/presdouro/images/DT_PD2016_VALIDADO.pdf
        https://lajes.pavimir.pt/pdfs/DA%2060%20-%20Pavimentos%20Aligeirados.pdf
        """
        if not self._thickness:
            min_span_length = min(self.lx, self.ly)
            if self.typology == 1 or self.typology == 2:
                return min(
                    round(100 * min_span_length/30) / 100,
                    self.MAX_THICKNESS)
            elif self.typology == 3:
                return min(
                    round(100 * (0.032 * min_span_length + 0.065)) / 100,
                    self.MAX_THICKNESS)
        return self._thickness

    @t.setter
    def t(self, value=None) -> None:
        """Setter for slab thickness (depth)."""
        self._thickness = value

    @property
    def beam_tributary_areas(self) -> List[float]:
        """
        Returns
        -------
        List[float]
            Tributary areas for four beams surrounding the slab.
        """
        # Loading along beam in x
        if self.orientation == 1:
            ax = self.lx*self.ly/2
            ay = 0
        # Loading along beam in y
        elif self.orientation == 2:
            ax = 0
            ay = self.lx*self.ly/2
        # Loading along beams on both sides
        elif self.orientation == 3:
            if self.lx > self.ly:
                # Trapezoid area
                ax = (((self.lx - self.ly) + self.lx) * self.ly) / 2
                # Triangle area
                ay = ((self.ly / 2) * self.ly) / 2
            else:
                # Triangle area
                ax = ((self.lx / 2) * self.lx) / 2
                # Trapezoid area
                ay = (((self.ly - self.lx) + self.ly) * self.lx) / 2

        ax = round(ax, PRECISION)
        ay = round(ay, PRECISION)
        return [ay, ax, ay, ax]

    def set_loads(
        self, permanent_loads: PermanentBase, variable_loads: VariableBase
    ) -> None:
        """Sets the values of permanent and variable loads on slabs.

        Parameters
        ----------
        permanent_loads : PermanentBase
            Permanent loads.
        variable_loads : VariableBase
            Variable loads.
        """
        self.gamma_rc = permanent_loads.gamma_rc
        if self.roof:
            self.pg = self.pself + permanent_loads.roof
            self.pq = variable_loads.roof
        else:
            self.pg = self.pself + permanent_loads.floor
            self.pq = variable_loads.floor

    def _get_alpha(self, ratio: float) -> float:
        """
        Computes correction factor for equivalent uniformly distributed load.

        Given the transferred load from slab for each beam will be either
        triangle or trapezoidal, the correction factor, alpha, needs to be
        applied to the equivalent uniformly distributed load to obtain the
        same maximum moment for these distributed loading shapes.

        Parameters
        ----------
        ratio : float
            Ratio of shorter slab width to longer slab width.

        Returns
        -------
        float
            The correction factor for equivalent uniformly distributed load.

        Notes
        -----
        In the mid-span of a beam with length L,
        the triangular load with height of wtr will result in max. moment of:
        Mmax = (L**2 * wtr) / 12
        On the other hand, the uniform load we for the same beam will result in
        maximum moment of:
        Mmax = (L**2 * we) / 8
        Assuming that the max. moment from both load distributions are equal,
        factor alpha=2/3 needs to be applied on wtr to obtain equivalent we
        values. In the case of trapezoidal loads, alpha factor varies between
        [2/3, 1.0].

        References
        ----------
        D'Arga e Lima, J., Monteiro, V., Mun,. M. (1997) Betão Armado, Esforços
        Normais e de Flexão, 3rd Ed. Laboratório Nacional de Engenharia Civil,
        Lisboa.
        """
        ratio = ratio / 2  # divided by half for compatibility with table.
        ratio_ref = np.arange(0, 0.55, 0.05)
        alpha_ref = np.array([1.000, 0.9967, 0.9867, 0.97, 0.9467, 0.9167,
                              0.88, 0.8367, 0.7867, 0.73, 0.6667])
        if ratio <= 0.50:
            alpha = interp1d(ratio_ref, alpha_ref)(ratio)
        else:
            alpha = ratio * alpha_ref[-1]

        return alpha
