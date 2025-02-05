"""
Base module for defining applied loads in buildings.
"""

# Imports from installed packages
from abc import ABC
import json
import numpy as np
from pathlib import Path
from pydantic import BaseModel
from typing import List, Literal, Type, Tuple, Dict, Optional


class VariableBase(BaseModel, ABC):
    """Abstract base class representing live loads (Q).

    Attributes
    ----------
    floor : float
        Live load on the floor.
    roof : float
        Live load on the roof.
    staircase : float
        Live load on the staircase.
    """
    floor: float
    """Live load on the floor."""
    roof: float
    """Live load on the roof."""
    staircase: float
    """Live load on the staircase."""


class PermanentBase(BaseModel, ABC):
    """Abstract base class representing superimposed dead loads (G).

    Attributes
    ----------
    floor : float
        Superimposed dead load on the floor.
    roof : float
        Superimposed dead load on the roof.
    staircase : float
        Superimposed dead load on the staircase.
    infill : float
        Superimposed dead load due to infill walls.
    gamma_rc : float
        Unit weight of reinforced concrete.
    """
    floor: float
    """Superimposed dead load on the floor."""
    roof: float
    """Superimposed dead load on the roof."""
    staircase: float
    """Superimposed dead load on the staircase."""
    infill: float
    """Superimposed dead load due to infill walls."""
    gamma_rc: float
    """Unit weight of reinforced concrete."""


class CombinationBase(BaseModel, ABC):
    """Abstract base class representing a load combination.

    Attributes
    ----------
    tag : str
        Tag identifying the load combination.
    loads : Dict[Literal["G", "Q", "E+X", "E-X", "E+Y", "E-Y"], float]
        Dictionary containing load tags and factors corresponding to
        each load type in the load combination.
    masses : Dict[Literal["G", "Q"], float]
        Dictionary containing mass sources and factors used to compute
        seismic loads considered in the load combination.
        Default is None.
    """
    tag: str
    """Tag identifying the load combination."""
    loads: Dict[Literal["G", "Q", "E+X", "E-X", "E+Y", "E-Y"], float]
    """Dictionary containing load tags and factors corresponding to
    each load type in the load combination."""
    masses: Optional[Dict[Literal["G", "Q"], float]] = None
    """Dictionary containing mass sources and factors used to compute
    seismic loads considered in the load combination."""


class LoadsDataBase(BaseModel, ABC):
    """Abstract base class representing the format of loads data.

    Attributes
    ----------
    variable : VariableBase
        Object representing variable (live) loads.
    permanent : PermanentBase
        Object representing permanent (dead) loads.
    combinations : List[CombinationBase]
        List of load combination objects.
    """
    variable: VariableBase
    """Object representing variable (live) loads."""
    permanent: PermanentBase
    """Object representing permanent (dead) loads."""
    combinations: List[CombinationBase]
    """List of load combination objects."""


class LoadsBase(ABC):
    """Abstract base class for loading loads data from a file.

    Attributes
    ----------
    variable : VariableBase
        Object representing variable (live) loads.
    permanent : PermanentBase
        Object representing permanent (dead) loads.
    combinations : List[CombinationBase]
        List of load combinations.
    _data_path : Path
        Path to the file containing loads data.
    _data_model : LoadsDataBase
        Pydantic model used for loading data format.
    """
    variable: VariableBase
    """Object representing variable (live) loads."""
    permanent: PermanentBase
    """Object representing permanent (dead) loads."""
    combinations: List[CombinationBase]
    """List of load combination objects."""
    _data_path: Path | str
    """Path to the file containing loads data."""
    _data_model: Type[LoadsDataBase]

    def __init__(self) -> None:
        """Initialize a new instance of LoadsBase.
        """
        with open(self._data_path, 'r') as json_file:
            # Load the JSON data into a Python dictionary
            data = json.load(json_file)
            # Initiate the InputData object and store with its filename
            loads_data = self._data_model(**data)

        self.permanent = loads_data.permanent
        self.variable = loads_data.variable
        self.combinations = loads_data.combinations
        # Check for mass sources
        self._set_mass_sources()

    def get_seismic_load_combos(self) -> List[CombinationBase]:
        """Returns load combinations containing seismic loading.

        Returns
        -------
        List[CombinationBase]
            List of seismic load combinations.
        """
        seismic_combos = []
        seismic_strs = ["E+X", "E-X", "E+Y", "E-Y"]
        for combo in self.combinations:
            if any(item in seismic_strs for item in combo.loads.keys()):
                seismic_combos.append(combo)

        return seismic_combos

    def get_gravity_load_combos(self) -> List[CombinationBase]:
        """Returns load combinations containing only gravity loads.

        Other gravity loads such as snow (S) can be added. In that case,
        this method should be overwritten for the specific design class.

        Returns
        -------
        List[CombinationBase]
            List of gravity load combinations.
        """
        grav_combos = []
        grav_strs = ["G", "Q"]  # permanent, variable
        for combo in self.combinations:
            if all(item in grav_strs for item in combo.loads.keys()):
                grav_combos.append(combo)

        return grav_combos

    def _set_mass_sources(self) -> None:
        """Checks for mass sources and assigns the defaults if they're
        not defined.

        If other gravity loads such as snow (S) are added,
        this method should be overwritten.
        """
        # Check for mass sources
        for combo in self.get_seismic_load_combos():
            if combo.masses:
                continue
            else:
                combo.masses = {}
                if 'G' in combo.loads.keys():
                    combo.masses["G"] = combo.loads["G"]
                else:
                    combo.masses["G"] = 0.0
                if 'Q' in combo.loads:
                    combo.masses["Q"] = combo.loads["Q"]
                else:
                    combo.masses["Q"] = 0.0

    def get_seismic_loads(
        self, beta: float, weights: np.ndarray, heights: np.ndarray
    ) -> Tuple[np.float64, np.ndarray]:
        """Calculate and return seismic loads (E).

        Parameters
        ----------
        beta : float
            Design lateral load factor (in g).
        weights : np.ndarray
            Array of weights.
        heights : np.ndarray
            Array of heights corresponding to each mass.

        Returns
        -------
        Tuple[np.float64, np.ndarray]
            Base shear and seismic forces acting at each mass.
        """
        base_shear = np.sum(beta * weights)
        forces = base_shear * (weights * heights) / np.sum(weights * heights)

        return base_shear, forces
