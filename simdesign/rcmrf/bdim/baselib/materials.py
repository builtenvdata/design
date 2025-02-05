"""
Base module for defining materials in buildings.
"""

# Imports from installed packages
from abc import ABC, abstractmethod
import json
from pathlib import Path
from pydantic import BaseModel, model_validator, ValidationError
from typing import List, Optional, Type

# Imports from units library
from ....utils.units import GPa


class SteelBase(BaseModel, ABC):
    """Abstract base class representing a steel material.

    Attributes
    ----------
    grade : str
        Grade of the steel material.
    fsyk : float
        Characteristic value of steel yield strength (in MPa).
    fsyd : float
        Design value of steel yield strength (in MPa).
    fsym : float
        Mean value of steel yield strength (in MPa).
    Es : float
        Steel elastic youngs' modulus (in base units, kPa),
        by default 200 * GPa.
    PARTIAL_FACTOR : float
        Partial factor for steel, by default 1.0.
    """
    grade: str
    """Grade of the steel material."""
    fsyk: float
    """Characteristic value of steel yield strength (in MPa)."""
    fsyd: float | None = None
    """"Design value of steel yield strength (in MPa)."""
    fsym: float | None = None
    """Mean value of steel yield strength (in MPa)."""
    Es: float | None = None
    """Steel elastic youngs' modulus (in base units, kPa)."""
    PARTIAL_FACTOR: float = 1.0
    """Partial factor for steel, by default 1.0."""

    @model_validator(mode='after')
    def set_fsyd(cls: Type['SteelBase'], instance: 'SteelBase'
                 ) -> 'SteelBase':
        """
        If not provided, sets the design value of yield strength (fsyd).
        """
        if instance.fsyd is None:
            instance.fsyd = instance.fsyk / instance.PARTIAL_FACTOR
        return instance

    @model_validator(mode='after')
    def set_fsym(cls: Type['SteelBase'], instance: 'SteelBase'
                 ) -> 'SteelBase':
        """
        If not provided, sets the mean value of yield strength (fsym)

        References
        ----------
        Table 4.10 and table 4.14 from Wisniewski D (2007) PhD thesis.
        """
        if instance.fsym is None:
            instance.fsym = 1.2 * instance.fsyk
        return instance

    @model_validator(mode='after')
    def set_youngs_modulus(cls: Type['SteelBase'], instance: 'SteelBase'
                           ) -> 'SteelBase':
        """
        If not provided, sets Young's modulus (E).
        """
        if instance.Es is None:
            instance.Es = 200 * GPa
        return instance


class ConcreteBase(BaseModel, ABC):
    """Abstract base class representing a concrete material.

    Attributes
    ----------
    grade : str
        Grade of the concrete material.
    fck : float
        Characteristic value of the compressive strength of concrete
        cylinders (in MPa).
    fcd : float
        Design value of concrete compressive strength (in MPa).
    fcm : float
        Mean value of the compressive strength of concrete cylinders (in MPa).
    Ecm : float
        Mean value of concrete elastic youngs' modulus (in base units, kPa).
    Gcm : float
        Mean value of concrete elastic shear modulus (in base units, kPa).
    Ecd : float
        Design value of concrete elastic youngs' modulus (in base units, kPa).
    Gcd : float
        Design value of concrete elastic shear modulus (in base units, kPa).
    PARTIAL_FACTOR : float
        Partial factor for concrete, by default 1.0.
    POISSONS_RATIO : float
        Poisson's ratio for concrete, by default 0.2.
    """
    grade: str
    """Grade of the concrete material."""
    fck: float
    """Characteristic value of the compressive strength of concrete
    cylinders (in MPa)."""
    fcd: float | None = None
    """Design value of concrete compressive strength (in MPa)."""
    fcm: float | None = None
    """Mean value of the compressive strength of concrete cylinders (in MPa).
    """
    Ecm: float | None = None
    """Mean value of concrete elastic youngs' modulus (in base units, kPa)."""
    Gcm: float | None = None
    """Mean value of Concrete elastic shear modulus (in base units, kPa)."""
    Ecd: float | None = None
    """Design value of concrete elastic youngs' modulus (in base units, kPa).
    """
    Gcd: float | None = None
    """Design value of Concrete elastic shear modulus (in base units, kPa)."""
    POISSONS_RATIO: float = 0.2
    """Poisson's ratio for concrete, by default 0.2."""
    PARTIAL_FACTOR: float = 1.0
    """Partial factor for concrete, by default 1.0."""

    @model_validator(mode='after')
    def set_fcd(cls: Type['ConcreteBase'], instance: 'ConcreteBase'
                ) -> 'ConcreteBase':
        """
        If not provided, set the design value of compressive strength (fcd).
        """
        if instance.fcd is None:
            instance.fcd = instance.fck / instance.PARTIAL_FACTOR
        return instance

    @model_validator(mode='after')
    def set_fcm(cls: Type['ConcreteBase'], instance: 'ConcreteBase'
                ) -> 'ConcreteBase':
        """
        If not provided, set the mean value of compressive strength (fcm).
        """
        if instance.fcm is None:
            instance.fcm = instance.fck + 8
        return instance

    @model_validator(mode='after')
    def validate_poissons_ratio(
        cls: Type['ConcreteBase'], instance: 'ConcreteBase'
    ) -> 'ConcreteBase':
        """
        Checks if Poisson's ratio is within a reasonable range.
        """
        if not (0 < instance.POISSONS_RATIO < 0.5):
            raise ValueError("Poisson's ratio must be between 0 and 0.5.")
        return instance

    @model_validator(mode='after')
    def set_youngs_modulus(
        cls: Type['ConcreteBase'], instance: 'ConcreteBase'
    ) -> 'ConcreteBase':
        """
        If not provided, sets Young's modulus (E).
        """
        if instance.Ecm is None:
            if instance.fcm is None:
                raise ValidationError(
                    "Cannot calculate Young's modulus (E) without fcm.")
            instance.Ecm = 9.5 * (instance.fcm ** (1/3)) * GPa

        if instance.Ecd is None:
            if instance.fcd is None:
                raise ValidationError(
                    "Cannot calculate Young's modulus (E) without fcd.")
            instance.Ecd = ((57 * ((instance.fcd) * 145)**0.5) / 145) * GPa

        return instance

    @model_validator(mode='after')
    def set_shear_modulus(cls: Type['ConcreteBase'], instance: 'ConcreteBase'
                          ) -> 'ConcreteBase':
        """
        If not provided, sets shear modulus (G).
        """
        if instance.Gcm is None:
            if instance.Ecm is None:
                raise ValidationError(
                    "Cannot calculate shear modulus (G) without E.")
            instance.Gcm = instance.Ecm / (2 * (1 + instance.POISSONS_RATIO))

        if instance.Gcd is None:
            if instance.Ecd is None:
                raise ValidationError(
                    "Cannot calculate shear modulus (G) without E.")
            instance.Gcd = instance.Ecd / (2 * (1 + instance.POISSONS_RATIO))

        return instance


class MaterialDataBase(BaseModel, ABC):
    """Abstract base class representing materials data.

    Attributes
    ----------
    concrete : List[ConcreteBase]
        List of concrete materials.
    steel : steel: List[SteelBase]
        List of steel materials.
    """
    concrete: List[ConcreteBase]
    """List of concrete material instances."""
    steel: List[SteelBase]
    """List of steel material instances."""


class MaterialsBase(ABC):
    """Abstract base class representing the collection of steel and concrete
    materials defined for a design class.

    Attributes
    ----------
    _data_blueprint: MaterialDataBase
        Subclass representing the blueprint for materials data.
    _data_path: Path
        Path to the json file containing material data.
    concrete : List[BaseConcrete]
        List of concrete material instances.
    steel : List[BaseSteel]
        List of steel material instances.

    Methods
    ----------
    __init__()
        Initialize a new instance of MaterialsBase.
    get_steel(grade: str) -> Optional[BaseSteel]
        Find and return the steel material instance with the specified grade.
    get_concrete(grade: str) -> Optional[BaseConcrete]
        Find and return the concrete material instance with the specified
        grade.
    get_next_concrete(concrete: ConcreteBase) -> ConcreteBase
        Returns the concrete material coming after the given.
    get_next_steel(steel: SteeBase) -> SteelBase
        Returns the concrete material coming after the given.
    """
    _data_blueprint: MaterialDataBase
    """Subclass representing the blueprint for materials data."""
    _data_path: Path | str
    """Path to the json file containing material data."""
    concrete: List[ConcreteBase]
    """List of concrete material instances."""
    steel: List[SteelBase]
    """List of steel material instances."""

    def __init__(self) -> None:
        """Initialize a new instance of Materials class.
        """
        with open(self._data_path, 'r') as json_file:
            # Load the JSON data into a Python dictionary
            data = json.load(json_file)
            # Initiate the InputData object and store with its filename
            loads_data: MaterialDataBase = self._data_blueprint(**data)
        self.concrete = loads_data.concrete
        self.steel = loads_data.steel

    def _get_steel(self, grade: str) -> Optional[SteelBase]:
        """Find and return the steel material instance with the specified
        grade.

        Parameters
        ----------
        grade : str
            grade or identifier of the steel material to find.

        Returns
        -------
        SteelBase or None
            The steel material instance with the specified grade, if found;
            otherwise None.
        """
        for steel in self.steel:
            if steel.grade == grade:
                return steel

    @abstractmethod
    def get_steel(self, grade: str) -> Optional[SteelBase]:
        """Find and return the steel material instance with the specified
        grade.

        Parameters
        ----------
        grade : str
            grade or identifier of the steel material to find.

        Returns
        -------
        SteelBase or None
            The steel material instance with the specified grade, if found;
            otherwise None.
        """
        pass

    def _get_concrete(self, grade: str) -> Optional[ConcreteBase]:
        """Find and return the concrete material instance with the specified
        grade.

        Parameters
        ----------
        grade : str
            grade or identifier of the concrete material to find.

        Returns
        -------
        ConcreteBase or None
            The concrete material instance with the specified grade, if found;
            otherwise None.
        """
        for concrete in self.concrete:
            if concrete.grade == grade:
                return concrete

    @abstractmethod
    def get_concrete(self, grade: str) -> Optional[ConcreteBase]:
        """Find and return the concrete material instance with the specified
        grade.

        Parameters
        ----------
        grade : str
            grade or identifier of the concrete material to find.

        Returns
        -------
        ConcreteBase or None
            The concrete material instance with the specified grade, if found;
            otherwise None.
        """
        pass

    def _get_next_concrete(self, concrete: ConcreteBase
                           ) -> Optional[ConcreteBase]:
        """Returns the concrete material coming after the given.

        Parameters
        ----------
        concrete : ConcreteBase
            Current concrete material.

        Returns
        -------
        ConcreteBase or None
            The next concrete material instance if the given is not
            the final option; otherwise None.
        """
        index = self.concrete.index(concrete)
        if index + 1 < len(self.concrete):
            return self.concrete[index + 1]

    @abstractmethod
    def get_next_concrete(self, concrete: ConcreteBase
                          ) -> Optional[ConcreteBase]:
        """Returns the concrete material coming after the given.

        Parameters
        ----------
        concrete : ConcreteBase
            Current concrete material.

        Returns
        -------
        ConcreteBase or None
            The next concrete material instance if the given is not
            the final option; otherwise None.
        """
        pass

    def _get_next_steel(self, steel: SteelBase) -> Optional[SteelBase]:
        """Returns the concrete material coming after the given.

        Parameters
        ----------
        steel : SteelBase
            Current steel material.

        Returns
        -------
        SteelBase or None
            The next steel material instance if the given is not
            the final option; otherwise None.
        """
        index = self.steel.index(steel)
        if index + 1 < len(self.steel):
            return self.steel[index + 1]

    @abstractmethod
    def get_next_steel(self, steel: SteelBase) -> Optional[SteelBase]:
        """Returns the concrete material coming after the given.

        Parameters
        ----------
        steel : SteelBase
            Current steel material.

        Returns
        -------
        SteelBase or None
            The next steel material instance if the given is not
            the final option; otherwise None.
        """
        pass
