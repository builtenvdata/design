# Imports from installed packages
import numpy as np
import openseespy.opensees as ops
from typing import List

# Imports from bnsm library
from .node import Node

# Imports from utils library
from ...utils.misc import PRECISION


class FloorDiaphragm:
    """Class for defining floor diaphragms of the structure in OpenSees.

    Attributes
    ----------
    cnodes : List[Node]
        Constrained floor nodes.
    rnode : Node
        Retained floor node.
    floor : int
        Floor id (e.g., storey no).
    masses: List[float]
        Total joint masses used for defining retained node location.
    """

    cnodes: List[Node]
    """Constrained floor nodes."""
    rnode: Node
    """Retained floor node."""
    floor: int
    """Floor id."""
    masses: List[float]
    """Total joint masses used for defining retained node location."""

    def __init__(self, cnodes: List[Node], floor: int,
                 masses: List[float]) -> None:
        """"Initialize FloorDiaphragm object.

        Parameters
        ----------
        cnodes : List[Node]
            Constrained floor nodes.
        floor : int
            Floor id (e.g., storey no).
        masses : List[float]
            Total joint masses used for defining retained node location.
        """
        self.cnodes = cnodes
        self.floor = floor
        self.masses = masses
        # Initializes floor retained node
        # Summation of masses
        sum_mass = 0  # summation of the masses
        sum_mass_moment = 0  # summation of the mass moments
        for i, node in enumerate(self.cnodes):
            mass = np.array(3*masses[i])
            coords = np.array(node.coordinates)
            sum_mass += mass
            sum_mass_moment += mass*coords
        # Center of mass
        cm = np.round(sum_mass_moment / sum_mass, PRECISION)
        tag = 90000 + self.floor * 1000
        self.rnode = Node(tag, cm)

    def add_to_ops(self) -> None:
        """Adds all of the floor diaphragm objects into the OpenSees domain
        (i.e, constrained floor nodes, retained floor node at center of mass
        and floor diaphragm).
        """
        # Constrained floor nodes
        for node in self.cnodes:
            node.add_to_ops()
        # Rigid floor diaphragm - Multi-point (mp) constraints
        self.rnode.add_to_ops()  # Retained floor node
        perp_dir = 3
        rnode_tag = self.rnode.tag
        cnode_tags = [node.tag for node in self.cnodes]
        ops.rigidDiaphragm(perp_dir, rnode_tag, *cnode_tags)
        ops.fix(rnode_tag, 0, 0, 1, 1, 1, 0)

    def to_py(self) -> List[str]:
        """Gets the Python commands to define floor diaphragm objects in
        the OpenSees domain (i.e, constrained floor nodes, retained floor
        node at center of mass and floor diaphragm).

        Returns
        -------
        List[str]
            List of Python commands for constructing the components of
            floor diaphragm in OpenSees.
        """
        content = [f"# Floor no. {self.floor}"]
        # Constrained floor nodes
        content.append("# Constrained floor nodes")
        for node in self.cnodes:
            content.append(node.to_py())
        # Rigid floor diaphragm - Multi-point (mp) constraints
        content.append("# Retained floor node")
        content.append(self.rnode.to_py())  # Retained floor node
        perp_dir = 3
        rnode_tag = self.rnode.tag
        cnode_tags = ', '.join([f"{node.tag}" for node in self.cnodes])
        content.append("# Rigid floor diaphragm - multi-point constraints")
        content.append(
            f"ops.rigidDiaphragm({perp_dir}, {rnode_tag}, {cnode_tags})")
        content.append("# Fix the floating dofs of the retained node")
        content.append(f"ops.fix({rnode_tag}, 0, 0, 1, 1, 1, 0)")

        return content

    def to_tcl(self) -> List[str]:
        """Gets the Tcl commands to define floor diaphragm objects in
        the OpenSees domain (i.e, constrained floor nodes, retained floor
        node at center of mass and floor diaphragm).

        Returns
        -------
        List[str]
            List of Tcl commands for constructing the components of
            floor diaphragm in OpenSees.
        """
        content = [f"# Floor no. {self.floor}"]
        # Constrained floor nodes
        content.append("# Constrained floor nodes")
        for node in self.cnodes:
            content.append(node.to_tcl())
        # Rigid floor diaphragm - Multi-point (mp) constraints
        content.append("# Retained floor node")
        content.append(self.rnode.to_tcl())  # Retained floor node
        perp_dir = 3
        rnode_tag = self.rnode.tag
        cnode_tags = ' '.join([f"{node.tag}" for node in self.cnodes])
        content.append("# Rigid floor diaphragm - multi-point constraints")
        content.append(
            f"rigidDiaphragm {perp_dir} {rnode_tag} {cnode_tags}")
        content.append("# Fix the floating dofs of the retained node")
        content.append(f"fix {rnode_tag} 0 0 1 1 1 0")

        return content
