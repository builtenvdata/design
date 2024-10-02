"""
Specific routines for defining and designing eu_cdm joints.
"""
# Imports from installed packages
from typing import Optional

# Imports from bdim base library
from ..baselib.joint import JointBase

# Imports from the design class (eu_cdm) library
from .beam import Beam
from .column import Column
from .materials import Steel, Concrete


class Joint(JointBase):
    """Joint object for design class: eu_cdm.
    """
    left_beam: Optional[Beam]
    """Beam located on the left side of the joint (along global x-axis)."""
    right_beam: Optional[Beam]
    """Beam located on the right side of the joint (along global x-axis)."""
    front_beam: Optional[Beam]
    """Beam located in front of the joint (along global y-axis)."""
    rear_beam: Optional[Beam]
    """Beam located behind the joint (along global y-axis)."""
    top_column: Optional[Column]
    """Column located on top of the joint (along global z-axis)."""
    bottom_column: Optional[Column]
    """Column located under the joint(along global z-axis)."""
    steel: Steel
    """Steel material."""
    concrete: Concrete
    """Concrete material."""
