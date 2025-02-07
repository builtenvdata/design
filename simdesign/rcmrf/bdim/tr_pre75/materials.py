"""
Pydantic models for defining materials in tr_pre75 buildings.
"""

# Imports from installed packages
from pathlib import Path
from typing import List, Optional

# Imports from bdim base library
from ..baselib.materials import (ConcreteBase, SteelBase,
                                 MaterialDataBase, MaterialsBase)


class Steel(SteelBase):
    """Pydantic model representing steel materials for design class tr_pre75.

    Attributes
    ----------
    grade : str
        Grade of the steel material.
    fsyk : float
        Characteristic value of steel yield strength (in MPa).
    fsym : float
        Mean value of steel yield strength (in MPa).
    fsyd: float
        Design value of steel yield strength (in MPa).
    E : float
        Steel elastic youngs' modulus (in base units, kPa),
        by default 200 * GPa.
    PARTIAL_FACTOR : float
        Partial factor for steel, by default 1.0.
    """


class Concrete(ConcreteBase):
    """Pydantic model representing concrete materials for design
    class tr_pre75.

    Attributes
    ----------
    grade : str
        Grade of the concrete material.
    fck : float
        Characteristic value of the compressive strength of concrete
        cylinders (in MPa).
    fck_cube : float
        Characteristic value of the compressive strength of concrete cubes
         (in MPa).
    fcd : float
        Design value of concrete compressive strength (in MPa).
    fcm : float
        Mean value of the compressive strength of concrete cylinders (in MPa).
    E : float
        Concrete elastic youngs' modulus (in base units, kPa).
    G : float
        Concrete elastic shear modulus (in base units, kPa).
    PARTIAL_FACTOR : float
        Partial factor for concrete, by default 1.0.
    POISSONS_RATIO : float
        Poisson's ratio for concrete, by default 0.2.
    """
    fck_cube: float
    """Characteristic value of the compressive strength of concrete
    cylinders (in MPa)."""


class MaterialData(MaterialDataBase):
    """Pydantic model representing materials data.

    Attributes
    ----------
    concrete : List[ConcreteBase]
        List of concrete materials.
    steel : steel: List[SteelBase]
        List of steel materials.
    """
    concrete: List[Concrete]
    """List of concrete materials."""
    steel: List[Steel]
    """List of steel materials."""


class Materials(MaterialsBase):
    """Collection of steel and concrete materials defined for
    design class tr_pre75.

    Attributes
    ----------
    _data_blueprint = MaterialData
        Subclass representing the blueprint for materials data.
    _data_path: Path
        Path to the json file containing material data.
    concrete : List[Concrete]
        List of concrete material instances.
    steel : List[Steel]
        List of steel material instances.

    Methods
    ----------
    __init__()
        Initialize a new instance of Materials.
    get_steel(grade: str) -> Optional[Steel]
        Find and return the steel material instance with the specified grade.
    get_concrete(grade: str) -> Optional[Concrete]
        Find and return the concrete material instance with the specified
        grade.
    get_next_concrete(concrete: Concrete) -> Concrete
        Returns the concrete material coming after the given.
    get_next_steel(steel: Steel) -> Steel
        Returns the concrete material coming after the given.
    """
    _data_blueprint: MaterialData = MaterialData
    """Subclass representing the blueprint for materials data."""
    _data_path = Path(__file__).parent / 'data' / 'materials.json'
    """Path to the json file containing material data."""
    concrete: List[Concrete]
    """List of concrete material instances."""
    steel: List[Steel]
    """List of steel material instances."""

    def get_steel(self, grade: str) -> Optional[Steel]:
        """
        Find and return the steel material instance with the specified grade.

        Parameters
        ----------
        grade : str
            grade or identifier of the steel material to find.

        Returns
        -------
        Steel or None
            The steel material instance with the specified grade, if found;
            otherwise None.
        """
        return super()._get_steel(grade)

    def get_concrete(self, grade: str) -> Optional[Concrete]:
        """
        Find and return the concrete material instance with the specified
        grade.

        Parameters
        ----------
        grade : str
            grade or identifier of the concrete material to find.

        Returns
        -------
        Concrete or None
            The concrete material instance with the specified grade, if found;
            otherwise None.
        """
        return super()._get_concrete(grade)

    def get_next_concrete(self, concrete: Concrete) -> Concrete:
        """
        Returns the concrete material coming after the given.

        Parameters
        ----------
        concrete : Concrete
            Current concrete material.

        Returns
        -------
        Concrete or None
            The next concrete material instance if the given is not
            the final option; otherwise None.
        """
        return super()._get_next_concrete(concrete)

    def get_next_steel(self, steel: Steel) -> Steel:
        """
        Returns the concrete material coming after the given.

        Parameters
        ----------
        steel : Steel
            Current steel material.

        Returns
        -------
        Steel or None
            The next steel material instance if the given is not
            the final option; otherwise None.
        """
        return super()._get_next_steel(steel)
