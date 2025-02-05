"""
Pydantic models for defining loads in tr_pre75 buildings.
"""

# Imports from installed packages
import numpy as np
from pathlib import Path
from typing import Tuple, List, Type


# Imports from bdim base library
from ..baselib.loads import VariableBase, PermanentBase
from ..baselib.loads import CombinationBase, LoadsDataBase, LoadsBase


class Variable(VariableBase):
    """
    Model representing live loads (Q) for design class tr_pre75.

    Attributes
    ----------
    floor : float
        Live load on the floor.
    roof : float
        Live load on the roof.
    staircase : float
        Live load on the staircase.
    """
    pass


class Permanent(PermanentBase):
    """
    Model representing superimposed dead loads (G) for design class tr_pre75.

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
    pass


class Combination(CombinationBase):
    """
    Model representing a load combination for design class tr_pre75.

    This combination includes:
    - Dead loads (G)
    - Live loads (Q)
    - Seismic loads (E+X, E-X, E+Y, E-Y)

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
    pass


class LoadsData(LoadsDataBase):
    """
    Model representing the format of loads data for design class eu_cdl.

    Attributes
    ----------
    variable : Variable
        Object representing variable (live) loads.
    permanent : Permanent
        Object representing permanent (dead) loads.
    combinations : List[Combination]
        List of load combination objects.
    """

    variable: Variable
    """Object representing variable (live) loads."""
    permanent: Permanent
    """Object representing permanent (dead) loads."""
    combinations: List[Combination]
    """List of load combination objects."""


class Loads(LoadsBase):
    """Class for retrieving loads data from a json file
    for design class tr_pre75.

    Attributes
    ----------
    variable : Variable
        Object representing variable (live) loads.
    permanent : Permanent
        Object representing permanent (dead) loads.
    combinations : List[Combination]
        List of load combinations.
    _data_path : Path
        Path to the file containing loads data.
    _data_model : LoadsData
        Pydantic model used for loading data format.
    """

    variable: Variable
    """Object representing variable (live) loads."""
    permanent: Permanent
    """Object representing permanent (dead) loads."""
    combinations: List[Combination]
    """List of load combinations."""
    _data_path = Path(__file__).parent / "data" / "loads.json"
    """Path to the file containing loads data."""
    _data_model: Type[LoadsData]

    def __init__(self) -> None:
        """Initializes Loads object."""
        self._data_model = LoadsData
        super().__init__()

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
        forces = beta * weights
        return base_shear, forces
