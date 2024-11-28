# Imports from installed packages
import openseespy.opensees as ops
from typing import Optional, List

# Imports from utils library
from ...utils.misc import round_list


class Node:
    """Class for defining nodes of the structure in OpenSees.

    Attributes
    ----------
    tag : int
        Unique identifier for the node.
    coordinates : List[float]
        Node coordinates (x, y, z).
    masses : List[float]
        Nodal masses (Mx, My, Mz, RMx, RMy, RMz).
    nodal_mass: bool = True
        Flag to define masses as nodal masses in the numerical model.
    """
    tag: int
    """Unique identifier for the node."""
    coordinates: List[float]
    """Node coordinates (x, y, z)."""
    masses: List[float]
    """Nodal masses (Mx, My, Mz, RMx, RMy, RMz)."""
    nodal_mass: bool = True
    """Flag to define masses as nodal masses in the numerical model."""

    def __init__(self, tag: int, coordinates: List[float],
                 masses: Optional[List[float]] = None) -> None:
        """Initialize the Node object.

        Parameters
        ----------
        tag : int
            Unique identifier for the node.
        coordinates : List[float]
            Node coordinates (x, y, z).
        masses : Optional[List[float]], optional
            Nodal masses (Mx, My, Mz, RMx, RMy, RMz), by default None.
        """
        self.tag = tag
        self.coordinates = round_list(coordinates)
        if masses is None:
            masses = [0.0] * 6
        self.masses = masses

    def add_to_ops(self) -> None:
        """Adds the node object to OpenSees domain.
        """
        if self.nodal_mass and any(self.masses):
            ops.node(self.tag, *self.coordinates, '-mass', *self.masses)
        else:
            ops.node(self.tag, *self.coordinates)

    def to_py(self) -> str:
        """Gets the python command to construct the node object in OpenSees.

        Returns
        -------
        str
            Python command for constructing the node object in OpenSees.
        """
        coordinates = ', '.join(map(str, self.coordinates))
        if self.nodal_mass and any(self.masses):
            masses = ', '.join(map(str, self.masses))
            return f"ops.node({self.tag}, {coordinates}, '-mass', {masses})"
        else:
            return f"ops.node({self.tag}, {coordinates})"

    def to_tcl(self) -> str:
        """Gets the Tcl command to construct the node object in OpenSees.

        Returns
        -------
        str
            Tcl command for constructing the node object in OpenSees.
        """
        coordinates = ' '.join(map(str, self.coordinates))
        if self.nodal_mass and any(self.masses):
            masses = ' '.join(map(str, self.masses))
            return f"node {self.tag} {coordinates} -mass {masses}"
        else:
            return f"node {self.tag} {coordinates}"
