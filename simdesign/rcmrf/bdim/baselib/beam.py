"""
Base routines for defining and designing beams in buildings.

Section view of beams along X direction.
z
|__y
    --------------    ----
    |     y      |    |
    |     |      |    |
    |     +--x   |    h
    |            |    |
    |            |    |
    --------------    ----
    |---- b -----|

Section view of beams along Y direction.
z
|__x
    --------------    ----
    |     y      |    |
    |     |      |    |
    |     +--x   |    h
    |            |    |
    |            |    |
    --------------    ----
    |---- b -----|
"""

# Imports from installed packages
from abc import ABC, abstractmethod
from dataclasses import dataclass
from math import ceil
import numpy as np
import numpy.typing as npt
from typing import Annotated, Literal, List, Optional, Dict, TypeVar

# Imports from bdim base library
from .materials import SteelBase, ConcreteBase
from .column import ColumnBase

# Imports from geometry library
from ...geometry.base import Line, Point

# Imports from utils library
from ....utils.misc import dot, PRECISION
from ....utils.units import kN, MPa, m, cm

# Numpy Typing with specific shape and datatype
DType = TypeVar("DType", bound=np.generic)

Array3 = Annotated[npt.NDArray[DType], Literal[3]]


@dataclass
class BeamForces:
    """Data class for storing element forces."""
    M1: float
    """Moment around local-x at 1st gauss point (start-section)."""
    M5: float
    """Moment around local-x at 5th gauss point (mid-section)."""
    M9: float
    """Moment around local-x at 9th gauss point (end-section)."""
    V1: float
    """Shear in local-y at 1st gauss point (start-section)."""
    V5: float
    """Shear in local-y at 5th gauss point (mid-section)."""
    V9: float
    """Shear in local-y at 9th gauss point (end-section)."""
    case: Literal['gravity', 'seismic', None] = None
    """If forces are computed for load combo, defines the type of
    load combination, otherwise, None. By default None."""

    def __add__(self, other: 'BeamForces') -> 'BeamForces':
        """The addition operator “+” (object is left operand).

        Parameters
        ----------
        other : BeamForces
            Other BeamForces object.

        Returns
        -------
        BeamForces
            Addition of the other two `BeamForces` objects.

        Raises
        ------
        TypeError
            Unsupported operand type.
        """
        if isinstance(other, BeamForces):
            return BeamForces(
                self.M1 + other.M1,
                self.M5 + other.M5,
                self.M9 + other.M9,
                self.V1 + other.V1,
                self.V5 + other.V5,
                self.V9 + other.V9
            )
        else:
            raise TypeError("Unsupported operand type(s) for +: ",
                            "'{}' and '{}'".format(type(self), type(other)))

    def __sub__(self, other: 'BeamForces') -> 'BeamForces':
        """The substraction operator “-” (object is left operand).

        Parameters
        ----------
        other : BeamForces
            Other BeamForces object.

        Returns
        -------
        BeamForces
            Substraction of the other two `BeamForces` objects.

        Raises
        ------
        TypeError
            Unsupported operand type.
        """
        if isinstance(other, BeamForces):
            return BeamForces(
                self.M1 - other.M1,
                self.M5 - other.M5,
                self.M9 - other.M9,
                self.V1 - other.V1,
                self.V5 - other.V5,
                self.V9 - other.V9
            )
        else:
            raise TypeError("Unsupported operand type(s) for +: ",
                            "'{}' and '{}'".format(type(self), type(other)))

    def __mul__(self, factor: float | int) -> 'BeamForces':
        """The multiplication operator “*” (object is left operand).

        Parameters
        ----------
        factor : float | int
            Factor used for multiplying the force quantities.

        Returns
        -------
        BeamForces
            Product of factor and BeamForces object.
        """
        return BeamForces(
            self.M1 * factor,
            self.M5 * factor,
            self.M9 * factor,
            self.V1 * factor,
            self.V5 * factor,
            self.V9 * factor
        )

    def __rmul__(self, factor: float | int) -> 'BeamForces':
        """The multiplication operator “*” (object is right operand).

        Parameters
        ----------
        factor : float | int
            Factor used for multiplying the force quantities.

        Returns
        -------
        BeamForces
            Product of factor and BeamForces object.
        """
        return self.__mul__(factor)

    def __truediv__(self, factor: float | int) -> 'BeamForces':
        """The division operator “/” (object is left operand).

        Parameters
        ----------
        factor : float | int
            Factor used for dividing the force quantities.

        Returns
        -------
        BeamForces
            Quotient of division operation: BeamForces/factor.
        """
        return BeamForces(
            self.M1 / factor,
            self.M5 / factor,
            self.M9 / factor,
            self.V1 / factor,
            self.V5 / factor,
            self.V9 / factor
        )


@dataclass
class BeamEnvelopeForces:
    """Data class for storing element envelope forces."""
    M1_neg: float
    """Negative moment envelope around local-x at 1st gauss point
    (start-section)."""
    M5_neg: float
    """Negative moment envelope around local-x at 5th gauss point
    (mid-section)."""
    M9_neg: float
    """Negative moment envelope around local-x at 9th gauss point
    (end-section)."""
    M1_pos: float
    """Positive moment envelope around local-x at 1st gauss point
    (start-section)."""
    M5_pos: float
    """Positive moment envelope around local-x at 5th gauss point
    (mid-section)."""
    M9_pos: float
    """Positive moment envelope around local-x at 9th gauss point
    (end-section)."""
    V1: float
    """Shear envelope in local-y at 1st gauss point (start-section)."""
    V5: float
    """Shear envelope in local-y at 5th gauss point (mid-section)."""
    V9: float
    """Shear envelope in local-y at 9th gauss point (end-section)."""


class BeamBase(ABC):
    """Abstract base class for beams.

    Must be inherited by design class specific beams.
    """
    ok: bool
    """Flag to check section adequacy."""
    line: Line
    """Line representation of beam (tag and points)."""
    h: float
    """Beam height (depth)."""
    b: float
    """Beam breadth (width)."""
    __h: float
    """Private attribute for restoring `h` attribute."""
    __b: float
    """Private attribute for restoring `b` attribute."""
    steel: SteelBase
    """Steel material."""
    concrete: ConcreteBase
    """Concrete material."""
    typology: Literal[1, 2]
    """Beam typology
    1: Wide beams.
    2: Emergent beams."""
    exterior: bool
    """True if the beam is exterior."""
    slab_wg: List[float]
    """Uniformly distributed permanent loads transferred from slabs."""
    slab_wq: List[float]
    """Uniformly distributed variable loads transferred from slabs."""
    slab_alpha: List[float]
    """Beam load distribution coefficients, alpha."""
    stairs_wg: float
    """Uniformly distributed permanent loads transferred from stairs."""
    stairs_wq: float
    """Uniformly distributed variable loads transferred from stairs."""
    infill_wg: float
    """Infill loading on beams."""
    gamma_rc: float
    """Reinforced concrete unit weight."""
    pre_Md: float
    """Bending moment for preliminary design."""
    pre_Vd: float
    """Shear force for preliminary design."""
    forces: Dict[str, BeamForces]
    """Dictionary containing forces obtained from unique load cases
    (in load combos), e.g., 'G', 'Q', 'E+X', 'E-X', 'E+Y', 'E-Y'."""
    design_forces: List[BeamForces]
    """List of forces obtained each load combination (design forces)."""
    pre_h: float
    """Preliminary design beam height."""
    pre_b: float
    """Preliminary design beam breadth (width)."""
    cover: float
    """Concrete cover."""
    columns: List[ColumnBase | None]
    """List of columns connected to beam end nodes, i and j
    [Ci_top, Ci_bot, Cj_top, Cj_end].
    Columns which are not found are equal to None.
    """
    Asl_top_req: Array3[np.float64]
    """Required longitudinal reinforcement area at top."""
    Asl_bot_req: Array3[np.float64]
    """Required longitudinal reinforcement area at bottom."""
    Ash_sbh_req: Array3[np.float64]
    """Required transverse reinforcement area to spacing ratio."""
    dbl_t1: Array3[np.float64]
    """Diameter of top corner longitudinal bars (reinforcement)."""
    nbl_t1: Array3[np.int64]
    """Number of top corner longitudinal bars (reinforcement)."""
    dbl_t2: Array3[np.float64]
    """Diameter of top internal longitudinal bars (reinforcement)."""
    nbl_t2: Array3[np.int64]
    """Number of top internal longitudinal bars (reinforcement)."""
    dbl_b1: Array3[np.float64]
    """Diameter of bottom corner longitudinal bars (reinforcement)."""
    nbl_b1: Array3[np.int64]
    """Number of bottom corner longitudinal bars (reinforcement)."""
    dbl_b2: Array3[np.float64]
    """Diameter of bottom internal longitudinal bars (reinforcement)."""
    nbl_b2: Array3[np.int64]
    """Number of bottom internal longitudinal bars (reinforcement)."""
    dbh: Array3[np.float64]
    """Diameter of horizontal bars (transverse reinforcement)."""
    sbh: Array3[np.float64]
    """Spacing of horizontal bars (transverse reinforcement)."""
    nbh_b: Array3[np.int64]
    """Number of horizontal bars (stirrup legs) parallel to section width."""
    nbh_h: Array3[np.int64]
    """Number of horizontal bars (stirrup legs) parallel to section height."""
    MIN_H_EB: float = 30 * cm
    """The default minimum height (depth) of emergent beams."""
    MIN_B_EB: float = 20 * cm
    """The default minimum breadth (width) of emergent beams."""
    MAX_B_EB: float = 1.0 * m
    """The default maximum value of beam breadth (width) for emergent beams."""
    MAX_H_EB: float = 1.0 * m
    """The default maximum value of beam height (depth) for emergent beams."""
    MIN_H_WB: float = 15 * cm
    """The default minimum height (depth) of wide beams."""
    MIN_B_WB: float = 30 * cm
    """The default minimum breadth (width) of wide beams."""
    MAX_B_WB: float = 80 * cm
    """The default maximum value of beam breadth (width) for wide beams."""
    MAX_H_WB: float = 1.0 * m
    """The default maximum value of beam height (depth) for wide beams."""
    B_INCR_EB: float = 5 * cm
    """Controls amount of `b` increase for emergent beams
    in each design iteration."""
    H_INCR_EB: float = 5 * cm
    """Controls amount of `h` increase for emergent beams
    in each design iteration."""
    B_INCR_WB: float = 5 * cm
    """Controls amount of `b` increase for wide beams
    in each design iteration."""
    H_INCR_WB: float = 5 * cm
    """Controls amount of `h` increase for wide beams
    in each design iteration."""
    MAX_ASPECT_RATIO_EB: float = 2.0
    """Controls the maximum aspect ratio (height to breadth)
    for emergent beams."""
    MAX_ASPECT_RATIO_WB: float = 3.0
    """Controls the maximum aspect ratio (breadth to height)
    for wide beams."""
    fc_q: float
    """In-situ concrete compressive strength (quality adjusted)."""
    fsyl_q: float
    """In-situ longitudinal reinforcement yield strength (quality adjusted)."""
    fsyh_q: float
    """In-situ transverse reinforcement yield strength (quality adjusted)."""
    sbh_q: Array3[np.float64]
    """In-situ spacing of transverse reinforcement (quality adjusted)."""
    cover_q: float
    """In-situ concrete cover (quality adjusted)."""

    def __init__(
        self, line: Line, typology: Literal[1, 2], gamma_rc: float
    ) -> None:
        """Initialises the beam object.

        Parameters
        ----------
        line : Line
            Geometric mesh representation of beam.
        typology : Literal[1, 2]
            Beam typology
                1: Wide beams.
                2: Emergent beams.
        gamma_rc : float
            Reinforced concrete unit weight.
        """
        # Save inputs
        self.line = line
        self.gamma_rc = gamma_rc
        self.typology = typology
        # Initialize some parameters
        if self.typology == 1:
            self.b = self.MIN_B_WB
            self.h = self.MIN_H_WB
        elif self.typology == 2:
            self.b = self.MIN_B_EB
            self.h = self.MIN_H_EB
        self.exterior = False
        self.ok = True
        self.slab_wg = []
        self.slab_wq = []
        self.slab_alpha = []
        self.forces = {}
        self.stairs_wg = 0.0
        self.stairs_wq = 0.0
        self.infill_wg = 0.0

    def __str__(self) -> str:
        """
        Returns
        -------
        str
            String representation of the beam object.
        """
        beam_rep = self.line.__str__()
        beam_rep = beam_rep.replace('Line', 'Beam')
        beam_rep = beam_rep.replace('Point', 'Node-')
        return beam_rep

    @property
    def fck(self) -> float:
        """
        Returns
        -------
        float
            Characteristic concrete compressive strength (in base units).
        """
        return self.concrete.fck * MPa

    @property
    def fsyk(self) -> float:
        """
        Returns
        -------
        float
            Characteristic steel yield strength (in base units).
        """
        return self.steel.fsyk * MPa

    @property
    def fsym(self) -> float:
        """
        Returns
        -------
        float
            Mean steel yield strength (in base units).
        """
        return self.steel.fsym * MPa

    @property
    def fcd(self) -> float:
        """
        Returns
        -------
        float
            Design value of concrete compressive strength (in base units).
        """
        return self.concrete.fcd * MPa

    @property
    def fcm(self) -> float:
        """
        Returns
        -------
        float
            Mean value of concrete compressive strength (in base units).
        """
        return self.concrete.fcm * MPa

    @property
    def fsyd(self) -> float:
        """
        Returns
        -------
        float
            Design value of steel yield strength (in base units).
        """
        return self.steel.fsyd * MPa

    @property
    def Ecm(self) -> float:
        """
        Returns
        -------
        float
            Mean value of elastic young's modulus of concrete (in base units).
        """
        return self.concrete.Ecm

    @property
    def Ecd(self) -> float:
        """
        Returns
        -------
        float
            Design value of elastic young's modulus of concrete
            (in base units).
        """
        return self.concrete.Ecd

    @property
    def Gcm(self) -> float:
        """
        Returns
        -------
        float
            Mean value of elastic shear modulus of concrete (in base units).
        """
        return self.concrete.Gcm

    @property
    def Gcd(self) -> float:
        """
        Returns
        -------
        float
            Design value of elastic shear modulus of concrete (in base units).
        """
        return self.concrete.Gcd

    @property
    def Es(self) -> float:
        """
        Returns
        -------
        float
            Elastic young's modulus of steel (in base units).
        """
        return self.steel.Es

    @property
    def Ag(self) -> float:
        """
        Returns
        -------
        float
            Gross cross sectional area of the beam.
        """
        return self.b * self.h

    @property
    def Iy(self) -> float:
        """
        Returns
        -------
        float
            Moment of inertia around y-axis of the beam.
        """
        return (self.h * self.b**3) / 12

    @property
    def Ix(self) -> float:
        """
        Returns
        -------
        float
            Moment of inertia around x-axis of the beam.
        """
        return (self.b * self.h**3) / 12

    @property
    def Iy_eff(self) -> float:
        """
        Returns
        -------
        float
            Moment of inertia around y-axis of the beam.
        """
        return 0.5 * self.Iy

    @property
    def Ix_eff(self) -> float:
        """
        Returns
        -------
        float
            Moment of inertia around x-axis of the beam.
        """
        return 0.5 * self.Ix

    @property
    def J(self) -> float:
        """
        Returns
        -------
        float
            Second polar moment of area of the beam.
        """
        hbmin = np.minimum(self.b, self.h)
        hbmax = np.maximum(self.b, self.h)
        return (hbmax * hbmin**3) * (
            1/3 - 0.21 * (hbmin / hbmax) * (1 - (hbmin**4 / (12*hbmax**4))))

    @property
    def L(self) -> float:
        """
        Returns
        -------
        float
            Beam length.
        """
        return round(self.line.length, PRECISION)

    @property
    def elastic_nodes(self) -> List[Point]:
        """
        Returns
        -------
        List[Point]
            Beam nodes (points) in elastic model.
        """
        return self.line.points

    @property
    def self_wg(self) -> float:
        """
        Returns
        -------
        float
            Beam unit weight per length.
        """
        return self.gamma_rc * self.Ag

    @property
    def wg_total(self) -> float:
        """
        Returns
        -------
        float
            Summation of uniformly distributed permanent loads (G).
        """
        return sum(self.slab_wg) + self.stairs_wg + \
            self.infill_wg + self.self_wg

    @property
    def wg_total_alpha(self) -> float:
        """
        Returns
        -------
        float
            Summation of equivalent uniformly distributed permanent loads (G).

        Notes
        -----
        Differently from `wg_total`, in this case,
        the slab loads are factored by alpha coefficient.
        """
        return dot(self.slab_wg, self.slab_alpha) + \
            self.stairs_wg + self.infill_wg + self.self_wg

    @property
    def wq_total(self) -> float:
        """
        Returns
        -------
        float
            Summation of uniformly distributed variable loads (Q).
        """
        return sum(self.slab_wq) + self.stairs_wq

    @property
    def wq_total_alpha(self) -> float:
        """
        Returns
        -------
        float
            Summation of equivalent uniformly distributed variable loads (Q).

        Notes
        -----
        Differently from `wq_total`, in this case,
        the slab loads are factored by alpha coefficient.
        """
        return dot(self.slab_wq, self.slab_alpha) + self.stairs_wq

    @property
    def simple_Mg(self) -> float:
        """
        Returns
        -------
        float
            Expected bending moment at mid-span of simply-support beam due to
            permanent loads.
        """
        return self.wg_total_alpha * (self.L**2) / 8

    @property
    def simple_Mq(self) -> float:
        """
        Returns
        -------
        float
            Expected bending moment at mid-span of simply-support beam due to
            variable loads.
        """
        return self.wq_total_alpha * (self.L**2) / 8

    @property
    def simple_Vg(self) -> float:
        """
        Returns
        -------
        float
            Expected shear force at mid-span of simply-support beam due to
            permanent loads.
        """
        return self.wg_total * self.L / 2

    @property
    def simple_Vq(self) -> float:
        """
        Returns
        -------
        float
            Expected shear force at mid-span of simply-support beam due to
            variable loads.
        """
        return self.wq_total * self.L / 2

    @property
    def direction(self) -> Optional[Literal['x', 'y']]:
        """
        Returns
        -------
        Literal['x', 'y'] | None
            Global axis which is parallel to the beam's line (its direction).
        """
        if all(self.line.unit_vector == np.array([1.0, 0.0, 0.0])):
            return 'x'
        elif all(self.line.unit_vector == np.array([0.0, 1.0, 0.0])):
            return 'y'

    @property
    def envelope_forces(self) -> BeamEnvelopeForces:
        """
        Returns
        -------
        BeamEnvelopeForces
            Returns the envelope forces computed from `combo_forces`.
        """
        # Get a list of all attributes
        attributes = ['M1', 'M5', 'M9', 'V1', 'V5', 'V9']

        # Find minimum and maximum for each attribute
        min_values = [min(getattr(force, attr) for force in self.design_forces)
                      for attr in attributes]
        max_values = [max(getattr(force, attr) for force in self.design_forces)
                      for attr in attributes]
        return BeamEnvelopeForces(
            M1_neg=min(min_values[0], 0.0),
            M5_neg=min(min_values[1], 0.0),
            M9_neg=min(min_values[2], 0.0),
            M1_pos=max(max_values[0], 0.0),
            M5_pos=max(max_values[1], 0.0),
            M9_pos=max(max_values[2], 0.0),
            V1=max(max_values[3], abs(min_values[3])),
            V5=max(max_values[4], abs(min_values[4])),
            V9=max(max_values[5], abs(min_values[5])),
        )

    @property
    def rhol_top(self) -> Array3[np.float64]:
        """
        Returns
        -------
        Array3[np.float64]
            Top longitudinal reinforcement ratio.
        """
        Acorner = self.nbl_t1 * (np.pi * self.dbl_t1**2 / 4)
        Ainterior = self.nbl_t2 * (np.pi * self.dbl_t2**2 / 4)
        # return (Acorner + Ainterior) / ((self.h-self.cover) * self.b)
        return (Acorner + Ainterior) / self.Ag

    @property
    def rhol_bot(self) -> Array3[np.float64]:
        """
        Returns
        -------
        Array3[np.float64]
            Bottom longitudinal reinforcement ratio.
        """
        Acorner = self.nbl_b1 * (np.pi * self.dbl_b1**2 / 4)
        Ainterior = self.nbl_b2 * (np.pi * self.dbl_b2**2 / 4)
        # return (Acorner + Ainterior) / ((self.h-self.cover) * self.b)
        return (Acorner + Ainterior) / self.Ag

    @property
    def rhol(self) -> Array3[np.float64]:
        """
        Returns
        -------
        Array3[np.float64]
            Total longitudinal reinforcement ratio.
        """
        return self.rhol_top + self.rhol_bot

    @property
    def rhol_max_tens(self) -> float:
        """
        Returns
        -------
        float
            Maximum longitudinal reinforcement ratio in tens. and comp. zones
        """
        return 1.0

    @property
    def rhoh_x(self) -> Array3[np.float64]:
        """
        Returns
        -------
        Array3[np.float64]
            Horizontal (transverse) reinforcement ratio in local-x.
        """
        Ash = self.nbh_b * np.pi*self.dbh**2/4
        return Ash / (self.h * self.sbh)

    @property
    def rhoh_y(self) -> Array3[np.float64]:
        """
        Returns
        -------
        Array3[np.float64]
            Horizontal (transverse) reinforcement ratio in local-y.
        """
        Ash = self.nbh_h * np.pi*self.dbh**2/4
        return Ash / (self.b * self.sbh)

    @property
    def max_b(self) -> float:
        """
        Returns
        -------
        float
            Computed maximum allowed section breadth (width).
        """
        if self.direction == 'x':  # Beam is along x
            bc = max(col.by for col in self.columns if col)
        elif self.direction == 'y':  # Beam is along y
            bc = max(col.bx for col in self.columns if col)
        # EC8 5.4.1.2.1 (3) width limit
        b_max_code = min(bc + self.h, 2*bc)
        # Masks for finding emergent beams
        bool1 = self.typology == 2
        bool2 = self.exterior
        bool3 = self.stairs_wg != 0.0
        if bool1 or bool2 or bool3:
            return min(b_max_code, self.MAX_B_EB)
        else:
            return min(b_max_code, self.MAX_B_WB)

    @property
    def max_h(self) -> float:
        """
        Returns
        -------
        float
            Computed maximum allowed section height (depth).
        """
        # Masks for finding emergent beams
        bool1 = self.typology == 2  # Emergent by default
        bool2 = self.exterior  # Forces exterior beams to emergent
        bool3 = self.stairs_wg != 0.0  # Forces stairs beams to be emergent
        if bool1 or bool2 or bool3:
            return self.MAX_H_EB
        else:
            return self.MAX_H_WB

    @property
    def min_b(self) -> float:
        """
        Returns
        -------
        float
            Computed minimum allowed section breadth (width).
        """
        # Masks for finding emergent beams
        bool1 = self.typology == 2  # Emergent by default
        bool2 = self.exterior  # Forces exterior beams to emergent
        bool3 = self.stairs_wg != 0.0  # Forces stairs beams to be emergent
        if bool1 or bool2 or bool3:
            return self.MIN_B_EB
        else:
            return self.MIN_B_WB

    @property
    def min_h(self) -> float:
        """
        Returns
        -------
        float
            Computed minimum allowed section height (depth).
        """
        # Masks for finding emergent beams
        bool1 = self.typology == 2  # Emergent by default
        bool2 = self.exterior  # Forces exterior beams to emergent
        bool3 = self.stairs_wg != 0.0  # Forces stairs beams to be emergent
        if bool1 or bool2 or bool3:
            return self.MIN_H_EB
        else:
            return self.MIN_H_WB

    @property
    def mrd_pos(self) -> Array3[np.float64]:
        """
        Returns
        -------
        Array3[np.float64]
            Design resistance moment of beam in positive direction.
            Computed for start, mid, end beam sections.

        Notes
        -----
        Required for capacity design of columns.
        """
        return self._get_mrd('pos')

    @property
    def mrd_neg(self) -> Array3[np.float64]:
        """
        Returns
        -------
        Array3[np.float64]
            Design resistance moment of beam in negative direction.
            Computed for start, mid, end beam sections.

        Notes
        -----
        Required for capacity design of columns.
        """
        return self._get_mrd('neg')

    def _get_mrd(self, direction: Literal['neg', 'pos']) -> Array3[np.float64]:
        """
        Computes yield moment of the section in the given direction.

        Parameters
        ----------
        direction : Literal['neg', 'pos']
            Moment capacity direction (based on the sign convention).

        Returns
        -------
        My : np.ndarray
            Yield moment of beam in the specified `direction`.
            Computed for start, mid, end beam sections.

        References
        ----------
        Panagiotakos, T. B., & Fardis, M. N. (2001).
        Deformations of reinforced concrete members at yielding and ultimate.
        Structural Journal, 98(2), 135-148.

        Notes
        -----
        - Positive direction indicates that
        bottom section is tension zone and top section is compression zone.
        - Negative direction indicates that
        top section is tension zone and bottom section is compression zone.

        TODO
        ----
        Might need to switch to practice equations
        rather than using those in research paper.
        """
        # Set direction dependent parameters
        if direction == 'pos':  # positive direction case
            # Longitudinal reinforcement area under tension
            As_tens = (self.nbl_b1 * ((0.25 * np.pi) * self.dbl_b1**2) +
                       self.nbl_b2 * ((0.25 * np.pi) * self.dbl_b2**2))
            # Longitudinal reinforcement area under compression
            As_comp = (self.nbl_t1 * ((0.25 * np.pi) * self.dbl_t1**2) +
                       self.nbl_t2 * ((0.25 * np.pi) * self.dbl_t2**2))
        elif direction == 'neg':  # negative direction case
            # Longitudinal reinforcement area under tension
            As_tens = (self.nbl_t1 * ((0.25 * np.pi) * self.dbl_t1**2) +
                       self.nbl_t2 * ((0.25 * np.pi) * self.dbl_t2**2))
            # Longitudinal reinforcement area under compression
            As_comp = (self.nbl_b1 * ((0.25 * np.pi) * self.dbl_b1**2) +
                       self.nbl_b2 * ((0.25 * np.pi) * self.dbl_b2**2))

        # Dist. from concrete fiber in compression to the rebars in tension
        if hasattr(self, 'dbh'):
            dd = self.h - self.cover - self.dbh - 0.5 * self.dbl_t1
        else:
            dd = 0.9 * self.h  # Assume
        # Concrete crushing strain used for computing section capacity
        EPS_CU = 0.0035
        # Stress-block coefficient used to compute section capacity
        # TODO: Reference
        if self.fcd < 27.6 * MPa:
            betac = 0.85
        elif self.fcd > 55.17 * MPa:
            betac = 0.65
        else:
            betac = 1.05 - 0.05 * self.fcd / (6.9 * MPa)
        # Yield strain of steel bars
        esy = self.fsyk / self.Es
        # Concrete modulus of elasticity
        Ec = self.Ecd
        # Steel modulus of elasticity
        Es = self.Es
        # Modular ratio
        nyoung = Es / Ec
        # Distance from ext. concrete fiber (comp.) to the rebars (comp.)
        dd_prime = self.h - dd
        # Balanced c value: dist. to neutral axis from ext. conc. fiber (comp.)
        cb = (EPS_CU * dd) / (EPS_CU + esy)
        # Tension and compression longitudinal reinforcement ratio values
        rhol_tens = As_tens / (self.b * dd)
        rhol_comp = As_comp / (self.b * dd)
        # Compute distance to neutral axis with outer faces (simplification)
        c = (As_tens * self.fsyd - As_comp * self.fsyd) \
            / (0.85 * self.fcd * self.b * betac)
        # Decide whether yielding is controlled by tension or compression zone
        # Panagiotakos and Fardis 2001 - Equation 4 & 5
        Acomp_cntrl = rhol_tens + rhol_comp
        Atens_cntrl = rhol_tens + rhol_comp
        Bcomp_cntrl = rhol_tens + rhol_comp * (dd_prime / dd)
        Btens_cntrl = rhol_tens + rhol_comp * (dd_prime / dd)
        # Yielding is controlled by the tension steel
        control = np.ones_like(self.dbl_t1)
        A_to_use = Atens_cntrl
        B_to_use = Btens_cntrl
        # Yielding is controlled by the compression zone
        control[c >= cb] = 0
        A_to_use[c >= cb] = Acomp_cntrl[c >= cb]
        B_to_use[c >= cb] = Bcomp_cntrl[c >= cb]
        # The compression zone depth: Panagiotakos and Fardis 2001 - Equation 3
        ky = (((nyoung**2) * (A_to_use**2) + (2*nyoung*B_to_use))**0.5
              - nyoung*A_to_use)
        # Panagiotakos and Fardis 2001 - Equation 1
        fiy1 = self.fsyd / (Es * (1 - ky) * dd)
        # Panagiotakos and Fardis 2001 - Equation 2
        fiy2 = (1.8 * (self.fcd) / (Ec * ky * dd))
        # Yield curvature
        fiy = fiy1
        fiy[control == 0] = fiy2[control == 0]
        # Yield Moment: Panagiotakos and Fardis 2001 - Equation 6
        rhol_int = 0.0  # Beams do not have web-reinforcement
        term1 = (Ec * (ky**2)/2) * (
            0.5 * (1 + (dd_prime / dd)) - (ky / 3))
        term2 = (Es/2) * (
                (1 - ky) * rhol_tens +
                (ky - (dd_prime / dd)) * rhol_comp +
                (rhol_int / 6) * (1 - (dd_prime / dd))
                ) * (1 - (dd_prime / dd))
        My = (self.b * (dd**3)) * fiy * (term1 + term2)

        return My

    def restore_dimensions(self) -> None:
        """Restore beam dimension attributes.

        `b, h`
        """
        self.b = self.__b
        self.h = self.__h

    def set_restore_point(self):
        """Set the restore point for specific beam attributes.

        `b, h`
        """
        self.__b = self.b
        self.__h = self.h

    def increase_dimensions(self) -> None:
        """Method used for increasing dimensions of inadequate sections.

        Used in design iterations.
        Can be overwritten for each design class.

        Notes
        -----
        Usually, the beam aspect ratio is between 1.5-2.0.
        Hence, added aspect ratio limit for emergent beams.
        """
        if not self.ok:
            aspect_ratio = self.h / self.b
            # Masks for finding emergent beams
            bool1 = self.typology == 2  # Emergent by default
            bool2 = self.exterior  # Forces exterior beams to emergent
            bool3 = self.stairs_wg != 0.0  # Forces stairs beams to be emergent
            # Emergent beam cases
            if bool1 or bool2 or bool3:
                if aspect_ratio < self.MAX_ASPECT_RATIO_EB:
                    self.h += self.H_INCR_EB
                else:
                    self.b += self.B_INCR_EB
            # Wide beam cases
            else:
                if self.b / self.h <= self.MAX_ASPECT_RATIO_WB:
                    self.b += self.B_INCR_WB
                    if self.b > self.max_b:
                        self.b = self.pre_b
                        self.h += self.H_INCR_WB
                else:
                    self.h += self.H_INCR_WB

    def predesign_section_dimensions(self, slab_h: float) -> None:
        """Does preliminary design of beam.

        This method makes initial guess for section dimensions.

        Parameters
        ----------
        slab_h : float
            Slab thickness.

        Notes
        -----
        It can be overwritten for specific design classes.

        TODO
        ----
        Added aspect ratio limit for wide-beams. Discuss.
        """
        # Maximum mu value considered for the economic emergent beam design
        ECONOMIC_MU_EB = 0.25
        # Maximum mu value considered for the economic wide beam design
        ECONOMIC_MU_WB = 0.25
        # Unit conversions
        Md = self.pre_Md * kN * m
        # Emergent beam cases
        bool1 = self.typology == 2  # Emergent by default
        bool2 = self.exterior  # Forces exterior beams to emergent
        bool3 = self.stairs_wg != 0.0  # Forces stairs beams to be emergent
        if bool1 or bool2 or bool3:
            # Set section breadth to minimum
            self.b = self.min_b
            # Compute height for economic section, assuming d = 0.1h
            mu_h = ((Md / (ECONOMIC_MU_EB * self.fcd * self.b))**0.5) / 0.9
            # Compute height to control deformations
            if self.stairs_wg != 0.0 or sum(self.slab_wg) != 0.0:
                # The beam carries a slab (stairs or floor slab)
                def_h = self.L / 12
            else:  # The beam is secondary gravity beam
                def_h = self.L / (0.9 * 18)
            # Get the maximum slab computed from all
            self.h = max(self.min_h, slab_h, mu_h, def_h)
            # Iterate for aspect ratio consideration
            while self.h / self.b > self.MAX_ASPECT_RATIO_EB:
                # Increase breadth
                self.b += self.B_INCR_EB
                # Compute height for economic section, assuming d = 0.1h
                mu_h = ((Md / (ECONOMIC_MU_EB * self.fcd * self.b))**0.5) / 0.9
                # Compute height to control deformations
                if self.stairs_wg != 0.0 or sum(self.slab_wg) != 0.0:
                    # The beam carries a slab (stairs or floor slab)
                    def_h = self.L / 12
                else:  # The beam is secondary gravity beam
                    def_h = self.L / (0.9 * 18)
                # Get the maximum slab computed from all
                self.h = max(self.min_h, slab_h, mu_h, def_h)
        # Wide beam cases
        else:
            # Set section height (slab thickness or minimum)
            self.h = max(slab_h, self.min_h)
            # Section widths
            if sum(self.slab_wg) == 0.0:  # Secondary gravity beams
                self.b = self.min_b  # Use minimum dimension
            else:  # Primary gravity beams
                # Set width based on economic mu value and minimum allowed
                self.b = max(self.min_b,
                             (Md / (ECONOMIC_MU_WB*self.fcd*(0.9*self.h)**2))
                             )
                while (self.b > self.max_b or
                       self.b / self.h > self.MAX_ASPECT_RATIO_WB):
                    self.h += self.H_INCR_WB
                    self.b = Md / (ECONOMIC_MU_WB*self.fcd*(0.9*self.h)**2)
        # Round
        self.h = ceil(20 * self.h) / 20
        self.b = ceil(20 * self.b) / 20

    def validate_section_dimensions(self) -> None:
        """Method for validating section dimensions against maximum.
        """
        if self.b > self.max_b or self.h > self.max_h:
            self.ok = False

    def validate_longitudinal_reinforcement(self) -> None:
        """Method for validating longitudinal reinforcement against maximum.

        This method is intended to run after determining beam rebars.
        """
        # Adequacy check for maximum longitudinal reinforcement in tension
        rhol_tens = max(self.rhol_top.max(), self.rhol_bot.max())
        if rhol_tens > self.rhol_max_tens:
            self.ok = False

    def validate_transverse_reinforcement(self) -> None:
        """Method for validating transverse reinforcement.

        This method is intended to run after determining beam rebars.
        """
        pass

    @abstractmethod
    def verify_section_adequacy(self) -> None:
        """Abstract method for verifying adequacy of section dimensions.
        """
        pass

    @abstractmethod
    def compute_required_longitudinal_reinforcement(self) -> None:
        """Abstract method for computing required longitudinal reinforcement.

        Final solution is determined after finding rebar solution to meet
        the detailing requirements.
        """
        pass

    @abstractmethod
    def compute_required_transverse_reinforcement(self) -> None:
        """Abstract method for computing required transverse reinforcement.

        Final solution is determined after finding rebar solution to meet
        the detailing requirements.
        """
        pass
