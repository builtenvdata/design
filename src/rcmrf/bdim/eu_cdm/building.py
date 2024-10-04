"""
Specific routines for defining and designing eu_cdm buildings.

Basic units are kN, m, sec
"""

# Imports from installed packages
from typing import List, Type

# Imports from the design class (eu_cdm) library
from .analysis import ElasticModel
from .beam import Beam
from .column import Column
from .joint import Joint
from .loads import Loads
from .materials import Materials, Concrete, Steel
from .quality import Quality
from .rebars import Rebars
from .slab import Slab
from .stairs import Stairs

# Imports from bdim base library
from ..baselib.building import BuildingBase, TaxonomyData

# Imports from units library
from ....utils.units import m


class Building(BuildingBase):
    """Building object for design class: eu_cdm.
    """
    beams: List[Beam]
    """List of beam instances."""
    columns: List[Column]
    """List of column instances."""
    joints: List[Joint]
    """List of joint instances."""
    slabs: List[Slab]
    """List of slab instances."""
    stairs: List[Stairs]
    """List of stairs instances."""
    steel: Steel
    """Steel material instance considered in design of beams and columns."""
    concrete: Concrete
    """Concrete material instance considered in design of beams and columns."""
    loads: Loads
    """Loads instance used to apply building loads."""
    materials: Materials
    """Materials instance used to set building materials."""
    rebars: Rebars
    """Rebars instance used to determine reinforcement arrangement."""
    quality: Quality
    """Quality instance used to adjust properties of structural elements."""
    ColumnClass: Type[Column]
    BeamClass: Type[Beam]
    JointClass: Type[Joint]
    SlabClass: Type[Slab]
    StairsClass: Type[Stairs]
    ElasticModelClass: Type[ElasticModel]
    COLUMN_UNIFORMIZATION_STEP = 2
    """Step size considered for section uniformization in column. For
    example, if equals to 2, the same column section might be varied at
    every two storeys from bottom to top. If None, a constant section is
    used at all storeys.

    If step size is only 1 storey lower than total number of stories in the
    building a constant section is used for column along the building.
    """

    def __init__(self, taxonomy: TaxonomyData) -> None:
        """Initializes building object.

        Parameters
        ----------
        taxonomy : TaxonomyData
            Taxonomy data required for performing simulated-designs.
        """
        # Set classes used define building components.
        self.ColumnClass = Column
        self.BeamClass = Beam
        self.JointClass = Joint
        self.SlabClass = Slab
        self.StairsClass = Stairs
        self.ElasticModelClass = ElasticModel
        # Set the available materials
        self.materials = Materials()
        # Set the design loads and combinations
        self.loads = Loads()
        # Set the rebar options considered for detailing
        self.rebars = Rebars()
        # Set the quality models considered for structural property adjusments
        self.quality = Quality()
        # Initialise the structure
        super().__init__(taxonomy=taxonomy)
        # Set the maximum column dimensions for full design routine
        self._set_maximum_column_dimensions()

    def _set_maximum_column_dimensions(self) -> None:
        """Sets the maximum column dimensions based on number of storeys.

        Notes
        -----
        The limitations based on engineering judgement. They can be changed.
        In case they are independent from number of storeys, these can be
        set within column object as similar to the minimum dimension.
        """
        for column in self.columns:
            if self.num_storeys <= 3:
                column.MAX_B_SQUARE = 0.60*m
                column.MAX_B_RECTANGLE = 0.80*m
            elif self.num_storeys <= 6:
                column.MAX_B_SQUARE = 0.80*m
                column.MAX_B_RECTANGLE = 1.00*m
            elif self.num_storeys <= 9:
                column.MAX_B_SQUARE = 0.80*m
                column.MAX_B_RECTANGLE = 1.30*m

    def _change_materials(self) -> None:
        """The method used for changing materials in iterative design
        algorithm.

        Notes
        -----
        It is overwritten for eu_cdm design class with following changes:
        - The method is modified such that steel and concrete materials
        is not updated simultaneously in the same iteration. Instead,
        first, the concrete material is updated, when the final concrete
        material is reached steel material is updated.
        """
        if self.next_concrete:
            self.concrete = self.next_concrete
        elif self.next_steel:
            self.steel = self.next_steel
