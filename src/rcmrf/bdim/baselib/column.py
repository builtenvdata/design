"""
Base routines for defining and designing columns in buildings.

Section view of columns.
y
|__x
    --------------    ----
    |     y      |    |
    |     |      |    |
    |     +--x   |    by
    |            |    |
    |            |    |
    --------------    ----
    |---- bx ----|
"""

# Imports from installed packages
from abc import ABC, abstractmethod
from dataclasses import dataclass
from math import ceil
import numpy as np
from typing import Literal, List, Dict

# Imports from bdim base library
from .materials import SteelBase, ConcreteBase

# Imports from geometry library
from ...geometry.base import Point, Line

# Imports from utils library
from ....utils.units import MPa, m


@dataclass
class ColumnForces:
    """Data class for storing element forces.
    """
    N1: float
    """Axial force at 1st gauss point (start-section)."""
    Mx1: float
    """Moment around local-x at 1st gauss point (start-section)."""
    Vy1: float
    """Shear in local-y at 1st gauss point (start-section)."""
    My1: float
    """Moment around local-y at 1st gauss point (start-section)."""
    Vx1: float
    """Shear in local-x at 1st gauss point (start-section)."""
    N9: float
    """Axial force at 9th gauss point (end-section)."""
    Mx9: float
    """Moment around local-x at 9th gauss point (end-section)."""
    Vy9: float
    """Shear in local-y at 9th gauss point (end-section)."""
    My9: float
    """Moment around local-y at 9th gauss point (end-section)."""
    Vx9: float
    """Shear in local-x at 9th gauss point (end-section)."""
    case: Literal['gravity', 'seismic', None] = None
    """If forces are computed for load combo, defines the type of
    load combination, otherwise, None. By default None."""

    def __add__(self, other: 'ColumnForces') -> 'ColumnForces':
        """The addition operator “+” (object is left operand).

        Parameters
        ----------
        other : ColumnForces
            Other ColumnForces object.

        Returns
        -------
        ColumnForces
            Addition of the other two `ColumnForces` objects.

        Raises
        ------
        TypeError
            Unsupported operand type.
        """
        if isinstance(other, ColumnForces):
            return ColumnForces(
                self.N1 + other.N1,
                self.Mx1 + other.Mx1,
                self.Vy1 + other.Vy1,
                self.My1 + other.My1,
                self.Vx1 + other.Vx1,
                self.N9 + other.N9,
                self.Mx9 + other.Mx9,
                self.Vy9 + other.Vy9,
                self.My9 + other.My9,
                self.Vx9 + other.Vx9
            )
        else:
            raise TypeError("Unsupported operand type(s) for +: ",
                            "'{}' and '{}'".format(type(self), type(other)))

    def __sub__(self, other: 'ColumnForces') -> 'ColumnForces':
        """The substraction operator “-” (object is left operand).

        Parameters
        ----------
        other : ColumnForces
            Other ColumnForces object.

        Returns
        -------
        ColumnForces
            Substraction of the other two `ColumnForces` objects.

        Raises
        ------
        TypeError
            Unsupported operand type.
        """
        if isinstance(other, ColumnForces):
            return ColumnForces(
                self.N1 - other.N1,
                self.Mx1 - other.Mx1,
                self.Vy1 - other.Vy1,
                self.My1 - other.My1,
                self.Vx1 - other.Vx1,
                self.N9 - other.N9,
                self.Mx9 - other.Mx9,
                self.Vy9 - other.Vy9,
                self.My9 - other.My9,
                self.Vx9 - other.Vx9
            )
        else:
            raise TypeError("Unsupported operand type(s) for -: ",
                            "'{}' and '{}'".format(type(self), type(other)))

    def __mul__(self, factor: float | int) -> 'ColumnForces':
        """The multiplication operator “*” (object is left operand).

        Parameters
        ----------
        factor : float | int
            Factor used for multiplying the force quantities.

        Returns
        -------
        ColumnForces
            Product of factor and ColumnForces object.
        """
        return ColumnForces(
            self.N1 * factor,
            self.Mx1 * factor,
            self.Vy1 * factor,
            self.My1 * factor,
            self.Vx1 * factor,
            self.N9 * factor,
            self.Mx9 * factor,
            self.Vy9 * factor,
            self.My9 * factor,
            self.Vx9 * factor
        )

    def __rmul__(self, factor: float | int) -> 'ColumnForces':
        """The multiplication operator “*” (object is right operand).

        Parameters
        ----------
        factor : float | int
            Factor used for multiplying the force quantities.

        Returns
        -------
        ColumnForces
            Product of factor and ColumnForces object.
        """
        return self.__mul__(factor)

    def __truediv__(self, factor: float | int) -> 'ColumnForces':
        """The division operator “/” (object is left operand).

        Parameters
        ----------
        factor : float | int
            Factor used for dividing the force quantities.

        Returns
        -------
        ColumnForces
            Quotient of division operation: ColumnForces/factor.
        """
        return ColumnForces(
            self.N1 / factor,
            self.Mx1 / factor,
            self.Vy1 / factor,
            self.My1 / factor,
            self.Vx1 / factor,
            self.N9 / factor,
            self.Mx9 / factor,
            self.Vy9 / factor,
            self.My9 / factor,
            self.Vx9 / factor
        )


@dataclass
class ColumnEnvelopeForces:
    """Data class for storing element forces.
    """
    N1_neg: float
    """Negative axial force envelope (maximum compression force) at
    1st gauss point (start-section)."""
    N1_pos: float
    """Positive axial force envelope (maximum tension force) at
    1st gauss point (start-section)."""
    Mx1_neg: float
    """Negative moment envelope around local-x at 1st gauss point
    (start-section)."""
    Mx1_pos: float
    """Positive moment envelope around local-x at 1st gauss point
    (start-section)."""
    Vy1: float
    """Shear force envlope in local-y at 1st gauss point (start-section)."""
    My1_neg: float
    """Negative moment envelope around local-y at 1st gauss point
    (start-section)."""
    My1_pos: float
    """Positive moment envelope around local-y at 1st gauss point
    (start-section)."""
    Vx1: float
    """Shear force envlope in local-x at 1st gauss point (start-section)."""
    N9_neg: float
    """Negative axial force envelope (maximum compression force) at
    9th gauss point (end-section)."""
    N9_pos: float
    """Positive axial force envelope (maximum tension force) at
    9th gauss point (end-section)."""
    Mx9_neg: float
    """Negative moment envelope around local-x at
    9th gauss point (end-section)."""
    Mx9_pos: float
    """Positive moment envelope around local-x at
    9th gauss point (end-section)."""
    Vy9: float
    """Shear force envlope in local-y at 9th gauss point (end-section)."""
    My9_neg: float
    """Negative moment envelope around local-y at
    9th gauss point (end-section)."""
    My9_pos: float
    """Positive moment envelope around local-y at
    9th gauss point (end-section)."""
    Vx9: float
    """Shear force envlope in local-x at 9th gauss point (end-section)."""


class ColumnBase(ABC):
    """Abstract base class for columns.

    Must be inherited by design class specific columns.
    """
    steel: SteelBase
    """Steel material."""
    concrete: ConcreteBase
    """Concrete material."""
    bx: float
    """Breadth (width) along global x."""
    by: float
    """Breadth (width) along global y."""
    section: Literal[1, 2]
    """Column cross-section
    1: square solid section.
    2: rectangular solid section."""
    line: Line
    """Line representation of column (tag and points)."""
    gamma_rc: float
    """Reinforced concrete unit weight."""
    pre_Nq: float
    """Expected axial force due to variable loads."""
    pre_Ng: float
    """Expected axial force due to permanent loads."""
    pre_Nd: float
    """Expected preliminary design axial force."""
    orient: Literal['x', 'y', None]
    """Direction of greater dimension in global axis."""
    ok_x: bool
    """Flag to check section adequacy in x direction."""
    ok_y: bool
    """Flag to check section adequacy in y direction."""
    pre_bx: float
    """Preliminary design breadth (width) along global x."""
    pre_by: float
    """Preliminary design breadth (width) along global y."""
    cover: float
    """Concrete cover."""
    Aslx_req: float
    """Required longitudinal reinforcement area at
    bottom or top side of the section. In other words,
    required area of bars distributed along -x on one side."""
    Asly_req: float
    """Required longitudinal reinforcement area at
    left or right side of the section. In other words,
    required area of bars distributed along -y on one side."""
    Ashx_sbh_req: float
    """Required ratio of transverse reinforcement area along -x
    axis (i.e., parallel to -x axis) to the bar spacing."""
    Ashy_sbh_req: float
    """Required ratio of transverse reinforcement area along -y
    axis (i.e., parallel to -y axis) to the bar spacing."""
    dbl_cor: float
    """Diameter of corner longitudinal bars (reinforcement)."""
    dbl_int: float
    """Diameter of internal longitudinal bars (reinforcement)."""
    nblx_int: int
    """Number of internal longitudinal bars (reinforcement) at
    bottom or top side of the section. In other words,
    half of the total number of internal longitudinal bars (reinforcement)
    distributed along X (on one side of the section)."""
    nbly_int: int
    """Number of internal longitudinal bars (reinforcement) at
    left or right side of the section. In other words,
    half of the total number of internal longitudinal bars (reinforcement)
    distributed along Y (on one side of the section)."""
    dbh: float
    """Diameter of horizontal bars (transverse reinforcement)."""
    sbh: float
    """Spacing of horizontal bars (transverse reinforcement)."""
    nbh_x: float
    """Number of horizontal bars (stirrup legs) along -x axis."""
    nbh_y: float
    """Number of horizontal bars (stirrup legs) along -y axis."""
    MAX_B_SQUARE: float = 0.80 * m
    """The default maximum square column dimension."""
    MAX_B_RECTANGLE: float = 1.30 * m
    """The default maximum rectangular column dimension."""
    MIN_B_SQUARE: float = 0.25 * m
    """The default minimum square column dimension."""
    MIN_B_RECTANGLE: float = 0.25 * m
    """The default minimum rectangular column dimension."""
    BX_INCR: float = 0.05 * m
    """Controls amount of `bx` increase in design iterations."""
    BY_INCR: float = 0.05 * m
    """Controls amount of `by` increase in design iterations."""
    __bx: float
    """Private attribute for restoring `bx` attribute."""
    __by: float
    """Private attribute for restoring `by` attribute."""
    forces: Dict[str, ColumnForces]
    """Dictionary containing forces obtained from unique load cases
    (in load combos), e.g., 'G', 'Q', 'E+X', 'E-X', 'E+Y', 'E-Y'."""
    design_forces: List[ColumnForces]
    """List of forces obtained each load combination (design forces)."""
    fc_q: float
    """In-situ concrete compressive strength (quality adjusted)."""
    fsyl_q: float
    """In-situ longitudinal reinforcement yield strength (quality adjusted)."""
    fsyh_q: float
    """In-situ transverse reinforcement yield strength (quality adjusted)."""
    sbh_q: float
    """In-situ spacing of transverse reinforcement (quality adjusted)."""
    cover_q: float
    """In-situ concrete cover (quality adjusted)."""
    position_factor: float
    """Position factor considered to account for the column axial force
    increase during seismic loading. This will be used to increase the
    axial forces of columns which will be used for the computation of
    plastic hinge parameters in nonlinear opensees models."""

    def __init__(
        self, line: Line, section: Literal[1, 2], gamma_rc: float
    ) -> None:
        """Initialises the column object.

        Parameters
        ----------
        line : Line
            Geometric mesh representation of column.
        section : Literal[1, 2]
            Column cross-section type
            1: square solid section.
            2: rectangular solid section.
        gamma_rc : float
            Reinforced concrete unit weight.
        """
        # Save inputs
        self.line = line
        self.section = section
        self.gamma_rc = gamma_rc
        # Initialize some parameters
        self.bx = self.min_b
        self.by = self.min_b
        self.ok_x = True
        self.ok_y = True
        self.orient = None
        self.forces = {}

    def __str__(self) -> str:
        """
        Returns
        -------
        str
            String representation of the column object.
        """
        column_rep = self.line.__str__()
        column_rep = column_rep.replace('Line', 'Column')
        column_rep = column_rep.replace('Point', 'Node-')
        return column_rep

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
            Gross area of the column cross-section.
        """
        return self.bx * self.by

    @property
    def Ix(self) -> float:
        """
        Returns
        -------
        float
            Column moment of inertia around x-axis.
        """
        return (self.by * self.bx**3) / 12

    @property
    def Iy(self) -> float:
        """
        Returns
        -------
        float
            Column moment of inertia around y-axis.
        """
        return (self.bx * self.by**3) / 12

    @property
    def Ix_eff(self) -> float:
        """
        Returns
        -------
        float
            Effective column moment of inertia around x-axis.
        """
        return 0.5 * self.Ix

    @property
    def Iy_eff(self) -> float:
        """
        Returns
        -------
        float
            Effective column moment of inertia around y-axis.
        """
        return 0.5 * self.Iy

    @property
    def H(self) -> float:
        """
        Returns
        -------
        float
            Column height.
        """
        return self.line.length

    @property
    def J(self) -> float:
        """
        Returns
        -------
        float
            Column second polar moment of area.
        """
        hmin = np.minimum(self.bx, self.by)
        hmax = np.maximum(self.bx, self.by)
        return (hmax * hmin**3) * (
            1/3 - 0.21 * (hmin / hmax) * (1 - (hmin**4 / (12*hmax**4))))

    @property
    def self_wg(self) -> float:
        """
        Returns
        -------
        float
            Column unit weight per length.
        """
        return self.gamma_rc * self.Ag

    @property
    def elastic_nodes(self) -> List[Point]:
        """
        Returns
        -------
        List[Point]
            Column element nodes (points) in elastic model.
        """
        return self.line.points

    @property
    def max_b(self) -> float:
        """
        Returns
        -------
        float
            Computer maximum allowed column dimension.
        """
        if self.section == 1:  # Square columns
            return self.MAX_B_SQUARE
        elif self.section == 2:  # Rectangular columns
            return self.MAX_B_RECTANGLE

    @property
    def min_b(self) -> float:
        """
        Returns
        -------
        float
            Computer minimum allowed column dimension.
        """
        if self.section == 1:  # Square columns
            return self.MIN_B_SQUARE
        elif self.section == 2:  # Rectangular columns
            return self.MIN_B_RECTANGLE

    @property
    def rhol_max(self) -> float:
        """
        Returns
        -------
        float
            Maximum allowed longitudinal reinforcement ratio.
        """
        return 1.0

    @property
    def rhol_min(self) -> float:
        """
        Returns
        -------
        float
            Minimum longitudinal reinforcement ratio.
        """
        return 0.0

    @property
    def rhol(self) -> float:
        """
        Returns
        -------
        float
            Longitudinal reinforcement area ratio.
        """
        Abl_cor = (np.pi * self.dbl_int**2) / 4
        Abl_int = (np.pi * self.dbl_int**2) / 4
        nbl_int = 2 * (self.nbly_int + self.nblx_int)
        nbl_cor = 4
        return (nbl_cor*Abl_cor + nbl_int*Abl_int) / self.Ag

    @property
    def rhoh_x(self) -> float:
        """
        Returns
        -------
        float
            Transverse reinforcement area (in x) ratio.
        """
        Abh_x = self.nbh_x * (np.pi * self.dbh**2) / 4
        return Abh_x / (self.sbh * self.by)

    @property
    def rhoh_y(self) -> float:
        """
        Returns
        -------
        float
            Transverse reinforcement area (in y) ratio.
        """
        Abh_y = self.nbh_y * (np.pi * self.dbh**2) / 4
        return Abh_y / (self.sbh * self.bx)

    @property
    def envelope_forces(self) -> ColumnEnvelopeForces:
        """
        Returns
        -------
        ColumnEnvelopeForces
            Returns the envelope forces computed from `combo_forces`.
        """
        # Get a list of all attributes
        attributes = ['N1', 'Mx1', 'Vy1', 'My1', 'Vx1',
                      'N9', 'Mx9', 'Vy9', 'My9', 'Vx9']

        # Find minimum and maximum for each attribute
        min_values = [min(getattr(force, attr) for force in self.design_forces)
                      for attr in attributes]
        max_values = [max(getattr(force, attr) for force in self.design_forces)
                      for attr in attributes]
        return ColumnEnvelopeForces(
            N1_neg=min(min_values[0], 0.0),
            N1_pos=max(max_values[0], 0.0),
            Mx1_neg=min(min_values[1], 0.0),
            Mx1_pos=min(max_values[1], 0.0),
            Vy1=max(max_values[2], abs(min_values[2])),
            My1_neg=min(min_values[3], 0.0),
            My1_pos=min(max_values[3], 0.0),
            Vx1=max(max_values[4], abs(min_values[4])),
            N9_neg=min(min_values[5], 0.0),
            N9_pos=max(max_values[5], 0.0),
            Mx9_neg=min(min_values[6], 0.0),
            Mx9_pos=min(max_values[6], 0.0),
            Vy9=max(max_values[7], abs(min_values[7])),
            My9_neg=min(min_values[8], 0.0),
            My9_pos=min(max_values[8], 0.0),
            Vx9=max(max_values[9], abs(min_values[9]))
        )

    def restore_dimensions(self) -> None:
        """Restore column dimension attributes.

        `bx, by`
        """
        self.bx = self.__bx
        self.by = self.__by

    def set_restore_point(self) -> None:
        """Set the restore point for specific column attributes.

        `bx, by, steel, concrete`
        """
        self.__bx = self.bx
        self.__by = self.by

    def increase_dimensions(self) -> None:
        """Method used for increasing dimensions of inadequate sections.

        Used in design iterations.
        Can be overwritten for each design class.
        """
        # Modify dimension in global x
        if not self.ok_x:
            self.bx = ceil(20*(self.bx + self.BX_INCR)) / 20
        # Modify dimension in global y
        if not self.ok_y:
            self.by = ceil(20*(self.by + self.BY_INCR)) / 20
        # Make dimensions compatible with the section type (square, rect)
        self.apply_section_compatibility()

    def apply_section_compatibility(self) -> None:
        """Modifies the section dimensions for compatibility with section type.
        i.e., square (1), rectangle (2).

        Used in design iterations.
        Can be overwritten for each design class.
        """
        if self.section == 1:  # Square section
            # Make both dimensions equal to their maximum
            self.bx = ceil(20*max(self.bx, self.by)) / 20
            self.by = ceil(20*max(self.bx, self.by)) / 20
        elif self.section == 2:  # Rectangular section
            # Shorter dimension should be at least half of the longer dimension
            if self.orient == 'x':  # Longer dimension is bx
                self.by = ceil(20*max(self.by, 0.5*self.bx)) / 20
                self.by = ceil(20 * self.by) / 20
            elif self.orient == 'y':  # Longer dimension is by
                self.bx = ceil(20*max(self.bx, 0.5*self.by)) / 20
                self.bx = ceil(20 * self.bx) / 20

    def predesign_section_dimensions(self) -> None:
        """Does preliminary design of column.

        This method makes initial guess for section dimensions.

        Notes
        -----
        It can be overwritten for specific design classes.
        """
        # Initial guess for column concrete area
        min_area = self.pre_Nd / self.fcd
        # Determine initial dimensions
        if self.section == 1:  # Square section
            self.bx = (min_area**0.5)
            self.by = (min_area**0.5)
        elif self.section == 2:  # Rectangular section
            if self.orient == 'x':  # Longer dimension is bx
                self.bx = (2*min_area)**0.5
                self.by = 0.5*self.bx
            elif self.orient == 'y':  # Longer dimension is by
                self.by = (2*min_area)**0.5
                self.bx = 0.5*self.by
        # Check against minimum dimensions
        self.bx = max(ceil(20*self.bx)/20, self.min_b)
        self.by = max(ceil(20*self.by)/20, self.min_b)

    def validate_section_dimensions(self) -> None:
        """Method for validating section dimensions against maximum.
        """
        if self.bx > self.max_b:
            self.ok_x = False
        if self.by > self.max_b:
            self.ok_y = False

    def validate_longitudinal_reinforcement(self) -> None:
        """Method for validating longitudinal reinforcement against maximum.

        This method is intended to run after determining column rebars.
        """
        # Adequacy check for maximum longitudinal reinforcement
        if self.rhol > self.rhol_max:
            self.ok_x = False
            self.ok_y = False

    def validate_transverse_reinforcement(self) -> None:
        """Method for validating transverse reinforcement.

        This method is intended to run after determining column rebars.
        """
        pass

    def get_mrdx(self, **kwargs) -> float:
        """Computes the design value of moment of resistance around local x.

        This method can be overwritten for specific design class.

        Parameters
        ----------
        Ned : float
            Mean axial force on column.

        Returns
        -------
        float
            Design value of moment of resistance around local x.
        """
        # Make compression force positive
        return self._get_mrd(-1.0*kwargs['Ned'], 'x')

    def get_mrdy(self, **kwargs) -> float:
        """Computes the design value of moment of resistance around local y.

        This method can be overwritten for specific design class.

        Parameters
        ----------
        Ned : float
            Mean axial force on column.

        Returns
        -------
        float
            Design value of moment of resistance around local y.
        """
        # Make compression force positive
        return self._get_mrd(-1.0*kwargs['Ned'], 'y')

    def _get_mrd(self, Ned: float, axis=Literal['x', 'y']) -> float:
        """Computes the design value of moment of resistance around
        specified local axis.

        Parameters
        ----------
        Ned : float
            Mean axial force on column (compressive force has positive sign).

        Returns
        -------
        float
            Design value of moment of resistance around specified local axis.

        References
        ----------
        REBAP (1983) Regulamento de Estruturas de Betão Armado e PréEsforçado.
        Decreto-Lei N.° 349-C/83, Lisbon, Portugal
        """
        # Stress block coefficients for different axial load ratio (REBAP 1983)
        BETA_FC_VECTOR = [1.00, 0.93, 0.88, 0.88, 0.93]
        # Axial load ratio corresponding to each stress block coefficient
        NIU_VECTOR = [0.40, 0.50, 0.60, 0.70, 0.85]
        # Axis dependent section properties
        if axis == 'x':  # Around local x-axis
            h = self.bx
            b = self.by
            nbl_int = self.nblx_int
        elif axis == 'y':  # Around local y-axis
            b = self.by
            h = self.bx
            nbl_int = self.nbly_int
        # Total steel area, ignoring the intermediate steel
        Asl = 2*np.pi*0.25*(2*self.dbl_cor**2 + nbl_int*self.dbl_int**2)
        # Dimensionless omega (similar to reinf. ratio)
        omega = (Asl / self.Ag) * (self.fsyd / self.fcd)
        # Axial load ratio
        niu = Ned / (self.Ag * self.fcd)
        # Axial load ratio - 0.85
        niu_c = niu - 0.85
        # Stress block coefficient for given axial load ratio
        beta_c = np.interp(niu, NIU_VECTOR, BETA_FC_VECTOR)
        # Dimensionless lambda
        lambda_ = 0.5 - self.cover / h
        # Dimensionless mu
        if niu < 0.0:  # Axial force is tensile
            mu = (omega + niu) * (lambda_ * beta_c)
        elif niu <= 0.85:  # Axial force is compressive and lower than 0.85
            mu = (omega * lambda_ * beta_c) - (0.55 * niu * niu_c)
        else:  # Axial force is compressive and greater than 0.85
            mu = (omega - niu_c) * (lambda_ * beta_c)
        # Design moment of resistance
        Mrd = mu * b * (h**2) * self.fcd
        # Return
        return Mrd

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
