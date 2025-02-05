"""
Base module for defining stairs in buildings.

Plan view of mesh objects (rectangle) representing stairs.

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
from abc import ABC

# Imports from bdim base library
from .loads import PermanentBase, VariableBase

# Imports from geometry library
from ...geometry.base import Rectangle


class StairsBase(ABC):
    """
    Abstract base class for stairs.

    Must be inherited by design class specific stairs.
    """
    _thickness: float = 0.15
    """Private attribute for stairs slab thickness (depth), by default 0.15m.
    """
    rectangle: Rectangle
    """Geometric mesh representation of the stairs (tag, points, lines)."""
    gamma_rc: float
    """Unit weight of reinforced concrete."""
    pg: float
    """Permanent loads per unit stairs slab area."""
    pq: float
    """Variable loads per unit stairs slab area."""
    roof: bool
    """ Flag for checking if rectangle is located at roof level or not."""

    def __init__(self, rectangle: Rectangle, thickness: float = None) -> None:
        """Initializes the stairs object.

        Parameters
        ----------
        rectangle : Rectangle
            Geometric mesh representation of the stairs (tag, points, lines).
        thickness : float
           Stairs slab thickness (depth), by default None.
        """
        self.rectangle = rectangle
        self.t = thickness

    @property
    def t(self) -> float:
        """
        Returns the default value or the specified value in TaxonomyData.

        Returns
        -------
        float
            Stairs slab thickness (depth).
        """
        return self._thickness

    @t.setter
    def t(self, value=None) -> None:
        """Setter for stairs slab thickness (depth)."""
        self._thickness = value or self._thickness

    @property
    def lx(self) -> float:
        """
        Returns
        -------
        float
            Stairs slab (rectangle) length along global X-axis.
        """
        return self.rectangle.lines[1].length

    @property
    def ly(self) -> float:
        """
        Returns
        -------
        float
            Stairs slab (rectangle) length along global Y-axis.
        """
        return self.rectangle.lines[0].length

    @property
    def area(self) -> float:
        """
        Returns
        -------
        float
            Stairs slab (rectangle) area.
        """
        return self.rectangle.area

    @property
    def pself(self) -> float:
        """Stairs self-weight per unit area.

        Returns
        -------
        float
            Stairs self-weight per unit area.
        """
        return self.gamma_rc * self.t

    @property
    def beam_influence_areas(self) -> float:
        """
        Returns
        -------
        float
            Tributary areas for the beams supporting the stairs.

        Notes
        -----
        The supporting two beams are along x direction.
        One is located at mid-storey level, while the other is located at
        floor level.
        """
        return self.lx*self.ly/2

    def set_loads(
        self, permanent_loads: PermanentBase, variable_loads: VariableBase
    ) -> None:
        """Sets the values of permanent and variable loads on stairs.

        Parameters
        ----------
        permanent_loads : PermanentBase
            Permanent loads.
        variable_loads : VariableBase
            Variable loads.
        """
        self.gamma_rc = permanent_loads.gamma_rc
        self.pg = self.pself + permanent_loads.staircase
        self.pq = variable_loads.staircase
