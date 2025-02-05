# Imports from installed packages
from typing import List
import openseespy.opensees as ops

# Imports from bnsm library
from .node import Node

# Imports from bdim base library
from ..bdim.baselib.joint import JointBase, Point


class Foundation:
    """Class for defining foundations of the structure in OpenSees.

    Attributes
    ----------
    fixed_node : Node
        Fixed node.
    foundation_node : Node
        Foundation node.
    design : JointBase
        Instance of support joint design information model.

    Notes
    -----
    The ssi can be defined by means of ground springs.
    However, the soil information is not known and the foundation
    design is not performed. Therefore, the soil-structure interaction,
    SSI, is ignored and `equalDOF` constraints are defined between fixed
    node and foundation node.
    """

    fixed_node: Node
    """Fixed node."""
    foundation_node: Node
    """Foundation node."""
    design: JointBase
    """Design information of support joint."""

    def __init__(self, design: JointBase, mass: float):
        """Initialize the Foundation object.

        Parameters
        ----------
        design : JointBase
            Reference design information of support joint.
        mass : float
            Total mass assigned to support joint.
        """
        # Save reference design information of joint
        self.design = design
        # Set reference node properties
        ref_tag = self.ref_point.tag
        ref_coords = self.ref_point.coordinates
        # Initialize fixed node
        self.fixed_node = Node(ref_tag, ref_coords)
        # Initialize foundation node
        masses = [mass, mass, mass, 0.0, 0.0, 0.0]
        self.foundation_node = Node(ref_tag + 70000, ref_coords, masses)

    @property
    def ref_point(self) -> Point:
        """
        Returns
        -------
        Point
            Reference point in joint of basic geometry.
        """
        return self.design.elastic_node

    def add_to_ops(self) -> None:
        """Adds all the objects that are necessary for defining foundation
        into the OpenSees domain.
        """
        self.fixed_node.add_to_ops()
        self.foundation_node.add_to_ops()
        ops.fix(self.fixed_node.tag, 1, 1, 1, 1, 1, 1)
        ops.equalDOF(
            self.fixed_node.tag, self.foundation_node.tag, 1, 2, 3, 4, 5, 6)

    def to_py(self) -> List[str]:
        """Gets the Python commands to define all the objects that are
        necessary for defining foundation in the OpenSees domain.

        Returns
        -------
        List[str]
            List of Python commands for constructing the components of
            foundation in OpenSees.
        """
        col = self.design.top_column.line.tag
        content = [f'# Foundation or support under the column {col}']
        content.append("# Fixed node")
        content.append(self.fixed_node.to_py())
        content.append(f"ops.fix({self.fixed_node.tag}, 1, 1, 1, 1, 1, 1)")
        content.append("# Foundation node")
        content.append(self.foundation_node.to_py())
        content.append(f"ops.equalDOF({self.fixed_node.tag}, "
                       f"{self.foundation_node.tag}, 1, 2, 3, 4, 5, 6)")

        return content

    def to_tcl(self) -> List[str]:
        """Gets the Tcl commands to define all the objects that are
        necessary for defining foundation in the OpenSees domain.

        Returns
        -------
        List[str]
            List of Tcl commands for constructing the components of
            foundation in OpenSees.
        """
        col = self.design.top_column.line.tag
        content = [f'# Foundation or support under the column {col}']
        content.append("# Fixed node")
        content.append(self.fixed_node.to_tcl())
        content.append(f"fix {self.fixed_node.tag} 1 1 1 1 1 1")
        content.append(self.foundation_node.to_tcl())
        content.append("# Foundation node")
        content.append(f"equalDOF {self.fixed_node.tag} "
                       f"{self.foundation_node.tag} 1 2 3 4 5 6")

        return content
