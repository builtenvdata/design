# Imports from installed packages
from abc import ABC
from typing import Optional

# Imports from bdim base library
from .beam import BeamBase
from .column import ColumnBase
from .materials import ConcreteBase, SteelBase

# Imports from geometry library
from ... geometry.base import Point

# Imports from utils library
from ....utils.units import MPa


class JointBase(ABC):
    """Abstract base class for joints.

    Must be inherited by design class specific joints.
    """
    elastic_node: Point
    """Joint node (point) in the linear elastic numerical model."""
    steel: SteelBase
    """Steel material."""
    concrete: ConcreteBase
    """Concrete material."""
    left_beam: Optional[BeamBase]
    """Beam located on the left side of the joint (along global x-axis)."""
    right_beam: Optional[BeamBase]
    """Beam located on the right side of the joint (along global x-axis)."""
    front_beam: Optional[BeamBase]
    """Beam located in front of the joint (along global y-axis)."""
    rear_beam: Optional[BeamBase]
    """Beam located behind the joint (along global y-axis)."""
    top_column: Optional[ColumnBase]
    """Column located on top of the joint (along global z-axis)."""
    bottom_column: Optional[ColumnBase]
    """Column located under the joint(along global z-axis)."""

    def __init__(
        self,
        elastic_node: Point,
        left_beam: Optional[BeamBase],
        right_beam: Optional[BeamBase],
        front_beam: Optional[BeamBase],
        rear_beam: Optional[BeamBase],
        top_column: Optional[ColumnBase],
        bottom_column: Optional[ColumnBase]
    ) -> None:
        """Initialises the joint object.

        Parameters
        ----------
        elastic_node : Point
            Joint node (point) in the linear elastic numerical model.
        left_beam : Optional[BeamBase]
            Beam located on the left side of the joint (along global x-axis).
        right_beam : Optional[BeamBase]
            Beam located on the right side of the joint (along global x-axis).
        front_beam : Optional[BeamBase]
            Beam located in front of the joint (along global y-axis)
        rear_beam : Optional[BeamBase]
            Beam located behind the joint (along global y-axis).
        top_column : Optional[ColumnBase]
            Column located on top of the joint (along global z-axis).
        bottom_column : Optional[ColumnBase]
            Column located under the joint (along global z-axis).
        """
        self.elastic_node = elastic_node
        self.left_beam = left_beam
        self.right_beam = right_beam
        self.front_beam = front_beam
        self.rear_beam = rear_beam
        self.top_column = top_column
        self.bottom_column = bottom_column

    def __str__(self) -> str:
        """
        Returns
        -------
        str
            String representation of the joint object.
        """
        joint_rep = self.elastic_node.__str__()
        joint_rep = joint_rep.replace('Point', 'Joint-')
        return joint_rep

    @property
    def fcm(self) -> float:
        """
        Returns
        -------
        float
            Mean value of concrete compressive strength (in base units).
        """
        return self.concrete.fcm * MPa
