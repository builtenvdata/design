"""
Base routines for defining and designing buildings.

x, y are horizontal directions whereas z is vertical.

Basic Units are kN, m, sec
"""

# Imports from installed packages
from abc import ABC
from dataclasses import dataclass
from typing import List, Type, Literal, Dict, Tuple, Optional, Union
import numpy as np
from math import ceil
from pathlib import Path
import pandas as pd

# Imports from bdim base library
from .analysis import ElasticModelBase
from .beam import BeamBase
from .column import ColumnBase
from .joint import JointBase
from .loads import LoadsBase
from .materials import MaterialsBase, ConcreteBase, SteelBase
from .quality import QualityBase
from .rebars import RebarsBase
from .slab import SlabBase
from .stairs import StairsBase

# Imports from geometry library
from ...geometry.base import FrameBase, Point, Line, Rectangle

# Imports from utils library
from ....utils.misc import make_dir
from ....utils.units import MPa, mm


@dataclass
class TaxonomyData:
    """Taxonomy data required for performing simulated-designs.
    """
    slab_type: Literal[1, 2, 3]
    """Slab typology
    1: Two-way solid slab (SS2).
    2: One-way solid slab (SS1).
    3: Composite slabs with pre-fabricated joists and ceramic blocks (HS)."""
    beam_type: Literal[1, 2]
    """Beam typology
    1: Wide beams.
    2: Emergent beams."""
    column_section: Literal[1, 2]
    """Column cross-section
    1: square solid section.
    2: rectangular solid section."""
    steel_grade: str
    """Steel material class ID, e.g., S400."""
    concrete_grade: str
    """Concrete material class ID, e.g., C20."""
    quality: Literal[1, 2, 3]
    """Construction quality levels
    1: High quality.
    2: Moderate quality.
    3: Low quality."""
    geometry: FrameBase
    """Building geometry instance."""
    beta: float
    """Design lateral load factor."""
    design_class: str
    """Building design class selected."""
    staircase_slab_depth: Optional[float] = None
    """Depth of the staircase slabs."""
    slab_thickness: Optional[float] = None
    """Slab thickness (depth)."""
    slab_orientation: Optional[Literal[1, 2, 3]] = None
    """Slab unloading orientation.
    1: Unloading in beams along X direction.
    2: Unloading in beams along Y direction.
    3: Unloading in beams along both directions."""


class BuildingBase(ABC):
    """
    Abstract base class for buildings.

    Must be inherited by design class specific buildings.
    """
    taxonomy: TaxonomyData
    """Building taxonomy data."""
    beams: List[BeamBase]
    """List of beam instances."""
    columns: List[ColumnBase]
    """List of column instances."""
    joints: List[JointBase]
    """List of joint instances."""
    slabs: List[SlabBase]
    """List of slab instances."""
    stairs: List[StairsBase]
    """List of stairs instances."""
    steel: SteelBase
    """Steel material instance considered in design of beams and columns."""
    concrete: ConcreteBase
    """Concrete material instance considered in design of beams and columns."""
    loads: LoadsBase
    """Loads instance used to apply building loads."""
    materials: MaterialsBase
    """Materials instance used to set building materials."""
    rebars: RebarsBase
    """Rebars instance used to determine reinforcement arrangement."""
    quality: QualityBase
    """Quality instance used to adjust properties of structural elements."""
    ColumnClass: Type[ColumnBase]
    BeamClass: Type[BeamBase]
    JointClass: Type[JointBase]
    SlabClass: Type[SlabBase]
    StairsClass: Type[StairsBase]
    ElasticModelClass: Type[ElasticModelBase]
    ok: bool
    """Decision flag for determining whether design is ok or not."""
    ITER_MAX: int = 100
    """Maximum number of iterations in the iterative design routine.
    By default 100."""
    COLUMN_UNIFORMIZATION_STEP: Optional[int] = None
    """Step size considered for section uniformization in column. For
    example, if equals to 2, the same column section might be varied at
    every two storeys from bottom to top. If None, a constant section is
    used at all storeys. By default None.

    If step size is only 1 storey lower than total number of stories in the
    building a constant section is used for column along the building."""
    OVERSTRENGTH_FACTOR_COLUMN_MOMENT: Optional[float] = None
    """Safety or overstrength factor considered in calculation of capacity
    design moments for columns (strong-column weak-beam principle).
    By default None.

    If None, column capacity design moments are not considered during
    the design."""
    OVERSTRENGTH_FACTOR_BEAM_SHEAR: Optional[float] = None
    """Safety or overstrength factor considered in calculation of capacity
    design shear forces for beams. By default None.

    If None, beam capacity design shear forces are not considered during
    the design."""
    OVERSTRENGTH_FACTOR_COLUMN_SHEAR: Optional[float] = None
    """Safety or overstrength factor considered in calculation of capacity
    design shear forces for columns. By default None.

    If None, column capacity design shear forces are not considered during
    the design."""

    @property
    def stairs_midstorey_beams(self) -> List[BeamBase]:
        """
        Returns
        -------
        List[BeamBase]
            List of stairs midstorey beams.
        """
        return self._get_stairs_midstorey_beams()

    @property
    def next_steel(self) -> SteelBase:
        """
        Returns
        -------
        SteelBase
            Next steel material.
        """
        return self.materials.get_next_steel(self.steel)

    @property
    def next_concrete(self) -> ConcreteBase:
        """
        Returns
        -------
        ConcreteBase
            Next concrete material.
        """
        return self.materials.get_next_concrete(self.concrete)

    @property
    def geometry(self) -> FrameBase:
        """
        Returns
        -------
        StandardFrame
            Frame building geometry instance.
        """
        return self.taxonomy.geometry

    @property
    def beta(self) -> float:
        """
        Returns
        -------
        float
            Design lateral load factor (in g).
        """
        return self.taxonomy.beta

    @property
    def beam_type(self) -> Literal[1, 2]:
        """
        Returns
        -------
        Literal[1, 2]
            Typology of beams.
            1: Wide beams are allowed.
            2: Emergent beams are used only.
        """
        return self.taxonomy.beam_type

    @beam_type.setter
    def beam_type(self, new_type: Literal[1, 2]) -> None:
        """Setter for `beam_type`."""
        for beam in self.beams:
            beam.typology = new_type
        self.taxonomy.beam_type = new_type

    @property
    def column_section(self) -> Literal[1, 2]:
        """
        Returns
        -------
        Literal[1, 2]
            Cross-section of columns.
            1: Square solid section.
            2: Rectangular solid section.
        """
        return self.taxonomy.column_section

    @column_section.setter
    def column_section(self, new_section: Literal[1, 2]) -> None:
        """Setter for `column_section`."""
        for column in self.columns:
            column.section = new_section
        self.taxonomy.column_section = new_section

    @property
    def design_class(self) -> str:
        """
        Returns
        -------
        str
            Building design class, e.g., 'eu_cdh'.
        """
        return self.taxonomy.design_class

    @property
    def slab_thickness(self) -> float | None:
        """
        Returns
        -------
        float | None
            Slab thickness (depth) considered in the building,
            if already set in the taxonomy, otherwise, None
        """
        if hasattr(self.taxonomy, 'slab_thickness'):
            return self.taxonomy.slab_thickness
        else:
            return None

    @slab_thickness.setter
    def slab_thickness(self, new_thickness: str) -> None:
        """Setter for `slab_thickness`."""
        self.taxonomy.slab_thickness = new_thickness

    @property
    def slab_type(self) -> Literal[1, 2, 3]:
        """
        Returns
        -------
        Literal[1, 2, 3]
            Slab typology considered in the building.
            1: Two-way solid slab.
            2: One-way solid slab.
            3: One-way composite slab with ceramic blocks and RC joists or
            pre-stressed beams.
        """
        return self.taxonomy.slab_type

    @property
    def staircase_slab_depth(self) -> float:
        """
        Returns
        -------
        float
            Building staircase slab thickness (depth).
        """
        if hasattr(self.taxonomy, 'staircase_slab_depth'):
            return self.taxonomy.staircase_slab_depth
        else:
            return None

    @staircase_slab_depth.setter
    def staircase_slab_depth(self, new_thickness: str) -> None:
        """Setter for `staircase_slab_depth`."""
        self.taxonomy.staircase_slab_depth = new_thickness

    @property
    def steel_grade(self) -> str:
        """
        Returns
        -------
        str
            The reinforcing steel material grade, e.g., 'S400'.
        """
        return self.taxonomy.steel_grade

    @steel_grade.setter
    def steel_grade(self, new_grade: str) -> None:
        """Setter for `steel_grade`."""
        self.taxonomy.steel_grade = new_grade

    @property
    def concrete_grade(self) -> str:
        """
        Returns
        -------
        str
            The concrete material grade, e.g., 'C20'.
        """
        return self.taxonomy.concrete_grade

    @concrete_grade.setter
    def concrete_grade(self, new_grade: str) -> None:
        """Setter for `concrete_grade`."""
        self.taxonomy.concrete_grade = new_grade

    @property
    def gamma_rc(self) -> float:
        """
        Returns
        -------
        float
            Reinforced concrete unit weight in building.
        """
        return self.loads.permanent.gamma_rc

    @property
    def continuous_columns(
        self
    ) -> Dict[Tuple[Union[float, int]], List[List[ColumnBase]]]:
        """
        Returns
        -------
        Dict[Tuple[Union[float, int]], List[List[ColumnBase]]]
            Lists of continuous columns at each grid on xy-plane.

        Notes
        -----
        Key of the returned dictionary corresponds to grid ids (x, y).
        Items contain nested list of continuous columns at corresponding grid.
        If there are discontinuous columns, the nested list will contain more
        than one list of continuous columns.
        """
        lines_dict = self.geometry.continuous_lines_along_z
        col_dict: Dict[Tuple[Union[float, int]], List[List[ColumnBase]]] = {}
        for grid_ids, lines in lines_dict.items():
            col_dict[grid_ids] = []
            columns = []
            for line in lines:
                if line is None:
                    if any(columns):
                        col_dict[grid_ids].append(columns.copy())
                        columns = []
                else:
                    column = self._find_column_by_line(line)
                    columns.append(column)
            col_dict[grid_ids].append(columns.copy())

        return col_dict

    @property
    def _continuous_columns(self) -> List[List[ColumnBase]]:
        """
        Returns
        -------
        List[List[ColumnBase]]
            All continuous columns in a single list
        """
        return [columns
                for _, columns_list in self.continuous_columns.items()
                for columns in columns_list]

    @property
    def continuous_beams_x(
        self
    ) -> Dict[Tuple[Union[float, int]], List[List[BeamBase]]]:
        """
        Returns
        -------
        Dict[Tuple[Union[float, int]], List[List[BeamBase]]]
            Lists of continuous beams at each grid on yz-plane.

        Notes
        -----
        Key of the returned dictionary corresponds to grid ids (y, z).
        Items contain nested list of continuous beams at corresponding grid.
        If there are discontinuous beams, the nested list will contain more
        than one list of continuous beams.
        """
        lines_dict = self.geometry.continuous_lines_along_x
        beam_dict: Dict[Tuple[Union[float, int]], List[List[BeamBase]]] = {}
        for grid_ids, lines in lines_dict.items():
            beam_dict[grid_ids] = []
            beams = []
            for line in lines:
                if line is None:
                    if any(beams):
                        beam_dict[grid_ids].append(beams.copy())
                        beams = []
                else:
                    beam = self._find_beam_by_line(line)
                    beams.append(beam)
            beam_dict[grid_ids].append(beams.copy())

        return beam_dict

    @property
    def continuous_beams_y(
        self
    ) -> Dict[Tuple[Union[float, int]], List[List[BeamBase]]]:
        """
        Returns
        -------
        Dict[Tuple[Union[float, int]], List[List[BeamBase]]]
            Lists of continuous beams at each grid on xz-plane.

        Notes
        -----
        Key of the returned dictionary corresponds to grid ids (x, z).
        Items contain nested list of continuous beams at corresponding grid.
        If there are discontinuous beams, the nested list will contain more
        than one list of continuous beams.
        """
        lines_dict = self.geometry.continuous_lines_along_y
        beam_dict: Dict[Tuple[Union[float, int]], List[List[BeamBase]]] = {}
        for grid_ids, lines in lines_dict.items():
            beam_dict[grid_ids] = []
            beams = []
            for line in lines:
                if line is None:
                    if any(beams):
                        beam_dict[grid_ids].append(beams.copy())
                        beams = []
                else:
                    beam = self._find_beam_by_line(line)
                    beams.append(beam)
            beam_dict[grid_ids].append(beams.copy())

        return beam_dict

    @property
    def _continuous_beams(self) -> List[List[BeamBase]]:
        """
        Returns
        -------
        List[List[BeamBase]]
            All continuous beams in a single list
        """
        # Get continuous beams as single list
        cont_beams_all: List[List[BeamBase]] = []
        for _, beams_list in self.continuous_beams_x.items():
            for beams in beams_list:
                cont_beams_all.append(beams)
        for _, beams_list in self.continuous_beams_y.items():
            for beams in beams_list:
                cont_beams_all.append(beams)
        return cont_beams_all

    @property
    def num_storeys(self) -> int:
        """
        Returns
        -------
        int
            Number of storeys in the building.

        Notes
        -----
        The results is correct if at least one column is fully
        continuous along the building.
        """
        max_level = 0  # This corresponds to storey
        all_stairs_columns = self._get_stairs_columns_agg()
        for _, column_lists in self.continuous_columns.items():
            tmp = 0
            for columns in column_lists:
                # Find the columns with equal sections
                steps = [0.5 if column in all_stairs_columns else 1.0
                         for column in columns]
                levels = np.cumsum(steps)
                tmp += max(levels)

            max_level = int(max(max_level, tmp))

        if max_level > 9:
            raise NotImplementedError('Frame buildings are not allowed to '
                                      'have more than 9 stories.')
        else:
            return max_level

    @property
    def dim_change(self) -> bool:
        """
        Returns
        -------
        bool
            Flag indicating whether it is possible to increase section
            dimensions or not.
        """
        # Beam breadth
        bool1 = all(beam.b <= beam.max_b for beam in self.beams)
        # Beam height
        bool2 = all(beam.h <= beam.max_h for beam in self.beams)
        # Column dimensions
        bool3 = all(max(col.bx, col.by) <= col.max_b for col in self.columns)

        # Return
        return all((bool1, bool2, bool3))

    @property
    def mat_change(self) -> bool:
        """
        Returns
        -------
        bool
            Flag for determining if it is possible change materials or not.
        """
        if self.next_concrete or self.next_steel:
            return True
        else:
            return False

    @property
    def beam_change(self) -> bool:
        """
        Returns
        -------
        bool
            Flag for determining if it is possible change `beam_type`
            or not.
        Notes
        -----
        Can be overwritten.
        """
        if self.beam_type == 1:
            return True
        else:
            return False

    @property
    def column_change(self) -> bool:
        """
        Returns
        -------
        bool
            Flag for determining if it is possible change `column_section`
            or not.
        Notes
        -----
        Can be overwritten.
        """
        if self.column_section == 2:
            return True
        else:
            return False

    @property
    def beams_fail(self) -> bool:
        """
        Returns
        -------
        bool
            Boolean indicating if beams failed to pass the design check or not.
        """
        return not all(beam.ok for beam in self.beams)

    @property
    def columns_fail(self) -> bool:
        """
        Returns
        -------
        bool
            Boolean indicating if columns failed to pass the design check or
            not.
        """
        return not all(col.ok_x and col.ok_y for col in self.columns)

    @property
    def elastic_nodes(self) -> List[Point]:
        """
        Returns
        -------
        List[Point]
            Nodes (points) in the linear elastic numerical model.
        """
        return self.geometry.points

    @property
    def elastic_nodes_ground(self) -> List[Point]:
        """_summary_

        Returns
        -------
        List[Point]
            Nodes (points) in the linear elastic numerical model.
        """
        return [cols[0][0].line.points[0]
                for _, cols in self.continuous_columns.items()]

    def __init__(self, taxonomy: TaxonomyData) -> None:
        """Initializes building object.

        Parameters
        ----------
        taxonomy : TaxonomyData
            Taxonomy data required for performing simulated-designs.
        """
        self.taxonomy = taxonomy
        self.beams = []
        self.columns = []
        self.joints = []
        self.slabs = []
        self.stairs = []
        self.ok = False
        self._initialize_columns()
        self._initialize_beams()
        self._initialize_joints()
        self._initialize_slabs()
        self._initialize_stairs()
        self._initialize_materials()
        self._set_beam_gravity_loads()
        self._set_restore_point()
        self._set_quality_model()

    def _initialize_beams(self) -> None:
        """Initializes building beams.
        """
        # Lines of exterior beams
        exterior_beam_lines = self.geometry.exterior_horizontal_lines
        # Beams along global x-axis
        for line in self.geometry.lines_x:
            beam = self.BeamClass(line=line, typology=self.beam_type,
                                  gamma_rc=self.gamma_rc)
            # Check if it is an exterior beam
            if line in exterior_beam_lines:
                beam.exterior = True
            # Set the beam cover
            beam.cover = self.rebars.beam_cover
            # Find end columns
            beam.columns = self._find_columns_by_beam(beam)
            # Append to beams list
            self.beams.append(beam)
        # Beams along global y-axis
        for line in self.geometry.lines_y:
            beam = self.BeamClass(line=line, typology=self.beam_type,
                                  gamma_rc=self.gamma_rc)
            # Check if it is an exterior beam
            if line in exterior_beam_lines:
                beam.exterior = True
            # Set the beam cover
            beam.cover = self.rebars.beam_cover
            # Find end columns
            beam.columns = self._find_columns_by_beam(beam)
            # Append to beams list
            self.beams.append(beam)

    def _initialize_columns(self) -> None:
        """Initializes building columns.
        """
        # Get facades
        facade_ids = self.geometry.lines_z_facades
        vertical_lines = self.geometry.lines_z
        # Start loop through each vertical line
        for line in vertical_lines:
            column = self.ColumnClass(line=line,
                                      section=self.column_section,
                                      gamma_rc=self.gamma_rc)
            line_idx = vertical_lines.index(line)
            facade_id = facade_ids[line_idx]
            # Set the longer dimension direction in global axis for
            # rectangular column.
            if facade_id in [2, 4, 12, 14, 32, 34]:
                column.orient = 'y'
            else:
                column.orient = 'x'
            # Set the column cover
            column.cover = self.rebars.col_cover
            # Append to the column list
            self.columns.append(column)

    def _initialize_slabs(self) -> None:
        """Initializes building slabs.
        """
        for rectangle in self.geometry.slabs_rectangles:
            slab = self.SlabClass(rectangle=rectangle,
                                  typology=self.slab_type,
                                  thickness=self.slab_thickness)
            slab.roof = rectangle in self.geometry.roof_rectangles
            slab.set_loads(self.loads.permanent, self.loads.variable)
            self.slabs.append(slab)
        # If slab thickness is not provided, set a global thickness value
        if self.slab_thickness is None:
            self.slab_thickness = max(slab.t for slab in self.slabs)
            for slab in self.slabs:
                slab.t = self.slab_thickness

    def _initialize_stairs(self) -> None:
        """Initializes building stairs.
        """
        for rectangle in self.geometry.stairs_rectangles:
            slab = self.StairsClass(
                rectangle=rectangle,
                thickness=self.staircase_slab_depth)
            slab.roof = rectangle in self.geometry.roof_rectangles
            slab.set_loads(self.loads.permanent, self.loads.variable)
            self.stairs.append(slab)
        # If staircase slab depth is not provided, set a global depth value
        if self.staircase_slab_depth is None:
            self.staircase_slab_depth = max(slab.t for slab in self.stairs)
            for slab in self.stairs:
                slab.t = self.staircase_slab_depth

    def _initialize_materials(self) -> None:
        """Initializes building materials.
        """
        # Set the current materials
        self.steel = self.materials.get_steel(self.steel_grade)
        self.concrete = self.materials.get_concrete(self.concrete_grade)
        # Update element materials
        self._update_element_materials()

    def _initialize_joints(self) -> None:
        """Initializes building joints.
        """
        for node in self.elastic_nodes:
            # Get elements connected to the node
            (
                left_beam, right_beam,
                front_beam, rear_beam,
                top_column, bottom_column
            ) = self._find_elements_by_point(node)
            # Create joint
            joint = self.JointClass(
                elastic_node=node,
                left_beam=left_beam, right_beam=right_beam,
                front_beam=front_beam, rear_beam=rear_beam,
                top_column=top_column, bottom_column=bottom_column
                )
            self.joints.append(joint)

    def _set_quality_model(self) -> None:
        """Sets construction quality model.
        """
        self.quality.model = self.taxonomy.quality

    def _update_element_materials(self) -> None:
        """Updates beam-column elements' materials."""
        # Update the material grades
        self.concrete_grade = self.concrete.grade
        self.steel_grade = self.steel.grade
        # Update the materials in rebars object
        self.rebars.concrete = self.concrete
        self.rebars.steel = self.steel
        # Update the materials in beam objects
        for beam in self.beams:
            beam.steel = self.steel
            beam.concrete = self.concrete
        # Update the materials in column objects
        for column in self.columns:
            column.steel = self.steel
            column.concrete = self.concrete
        # Update the materials in joint objects
        for joint in self.joints:
            joint.steel = self.steel
            joint.concrete = self.concrete

    def _get_unique_seism_combo_grav_factors(
        self
    ) -> List[Dict[Literal['G', 'Q'], float]]:
        """Retrieves the list containining gravity load factors from seismic
        load combos.

        These factors can be used to compute the mean gravity forces obtained
        from seismic load combinations.

        Returns
        -------
        List[Dict[Literal['G', 'Q'], float]]
            A list containining gravity load factors from seismic load combos.
        """
        factors = []
        unique_pairs = set()
        seismic_strs = ["E+X", "E-X", "E+Y", "E-Y"]
        for combo in self.loads.combinations:
            if any(item in combo.loads for item in seismic_strs):
                if 'G' in combo.loads:
                    g_fact = combo.loads['G']
                else:
                    g_fact = 0.0
                if 'Q' in combo.loads:
                    q_fact = combo.loads['Q']
                else:
                    q_fact = 0.0

                pair = (g_fact, q_fact)
                if pair not in unique_pairs:
                    unique_pairs.add(pair)
                    factors.append({"G": g_fact, "Q": q_fact})
        return factors

    def _get_stairs_midstorey_beams(self) -> List[BeamBase]:
        """Returns midstorey stairs beams along x-direction.

        Returns
        -------
        List[BeamBase]
            List of mid-storey stairs beams along x-direction.
        """
        return [self._find_beam_by_line(line)
                for line in self.geometry.stairs_lines_x1]

    def _get_stairs_columns_disagg(self) -> List[List[List[ColumnBase]]]:
        """Returns disaggregated stairs columns.

        The first level of items corresponds to each stairs columns (has
        length of num stairs).
        There are two second level of items corresponding to the list of z1
        and z2 columns.
        There are two third level of items:
        for List[i][0] these are z11 and z12 columns
        for List[i][1] these are z21 and z22 columns.

        Returns
        -------
        List[List[List[ColumnBase]]]
            List of disaggregated stairs columns lists.
        """
        columns_list_per_stairs = []
        z11_lines = self.geometry.stairs_lines_z11
        z12_lines = self.geometry.stairs_lines_z12
        z21_lines = self.geometry.stairs_lines_z21
        z22_lines = self.geometry.stairs_lines_z22
        for i in range(len(self.geometry.stairs_rectangles)):
            columns = []
            columns_z1 = []
            columns_z2 = []
            columns_z1.append(self._find_column_by_line(z11_lines[i]))
            columns_z1.append(self._find_column_by_line(z12_lines[i]))
            columns_z2.append(self._find_column_by_line(z21_lines[i]))
            columns_z2.append(self._find_column_by_line(z22_lines[i]))
            columns.append(columns_z1.copy())
            columns.append(columns_z2.copy())
            columns_list_per_stairs.append(columns.copy())

        return columns_list_per_stairs

    def _get_stairs_columns_agg(self) -> List[ColumnBase]:
        """Returns aggregated list of stairs columns.

        Returns
        -------
        List[ColumnBase]
            List of all stairs columns
        """
        columns = []
        z11_lines = self.geometry.stairs_lines_z11
        z12_lines = self.geometry.stairs_lines_z12
        z21_lines = self.geometry.stairs_lines_z21
        z22_lines = self.geometry.stairs_lines_z22
        for i in range(len(self.geometry.stairs_rectangles)):
            columns.append(self._find_column_by_line(z11_lines[i]))
            columns.append(self._find_column_by_line(z12_lines[i]))
            columns.append(self._find_column_by_line(z21_lines[i]))
            columns.append(self._find_column_by_line(z22_lines[i]))

        return columns

    def _find_beam_by_line(self, line: Line) -> Optional[BeamBase]:
        """Finds the beam object with given line attribute.

        Parameters
        ----------
        line : Line
            Geometric object (line) representing beam.

        Returns
        -------
        BeamBase | None
            Returns Beam object if line attribute matches with given,
            otherwise, returns None.
        """
        filtered_beams = filter(lambda beam: beam.line == line, self.beams)
        # Retrieve the first beam matching the condition
        matching_beam = next(filtered_beams, None)
        return matching_beam

    def _find_column_by_line(self, line: Line) -> Optional[ColumnBase]:
        """Finds the column object with given line attribute.

        Parameters
        ----------
        line : Line
            Geometric object (line) representing column.

        Returns
        -------
        ColumnBase | None
            Returns Column object if line attribute matches with given,
            otherwise, returns None.
        """
        filtered_columns = filter(lambda column: column.line == line,
                                  self.columns)
        # Retrieve the first column matching the condition
        matching_column = next(filtered_columns, None)
        return matching_column

    def _find_columns_by_beam(self, beam: BeamBase
                              ) -> List[Optional[ColumnBase]]:
        """Finds the columns at both ends of the given beam.

        Parameters
        ----------
        beam : BeamBase
            Beam object for which columns are going to be found.

        Returns
        -------
        List[ColumnBase | None]
            List of found Column objects [Ci_top, Ci_bot, Cj_top, Cj_end],
            Columns which are not found are equal to None.
        """
        columns = []
        for node in beam.elastic_nodes:
            filtered_columns_top = filter(
                lambda column: column.elastic_nodes[0] == node, self.columns)
            filtered_columns_bot = filter(
                lambda column: column.elastic_nodes[1] == node, self.columns)
            # Retrieve the first columns matching the condition
            top_column = next(filtered_columns_top, None)
            bot_column = next(filtered_columns_bot, None)
            columns.extend([top_column, bot_column])
        return columns

    def _find_slab_by_rectangle(self, rectangle: Rectangle
                                ) -> Optional[SlabBase]:
        """Finds slab with given rectangle attribute.

        Parameters
        ----------
        rectangle : Rectangle
            Geometric object (rectangle) representing slab.

        Returns
        -------
        SlabBase | None
            Returns Slab object if rectangle attribute matches with
            given, otherwise, returns None.
        """
        filtered_slabs = filter(
            lambda slab: slab.rectangle == rectangle, self.slabs)
        # Retrieve the first slab matching the condition
        matching_slab = next(filtered_slabs, None)
        return matching_slab

    def _find_stairs_by_rectangle(self, rectangle: Rectangle
                                  ) -> Optional[StairsBase]:
        """Finds stairs with given rectangle attribute.

        Parameters
        ----------
        rectangle : Rectangle
            Geometric object (rectangle) representing stairs.

        Returns
        -------
        StairsBase | None
            Returns Stairs object if rectangle attribute matches with
            given, otherwise, returns None.
        """
        filtered_stairs = filter(
            lambda slab: slab.rectangle == rectangle, self.stairs)
        # Retrieve the first slab matching the condition
        matching_stairs = next(filtered_stairs, None)
        return matching_stairs

    def _find_elements_by_point(
        self, node: Point
        ) -> Tuple[
            Optional[BeamBase], Optional[BeamBase],
            Optional[BeamBase], Optional[BeamBase],
            Optional[ColumnBase], Optional[ColumnBase]
            ]:
        """Finds the elements connected to the given node/point.

        Parameters
        ----------
        node : Point
            Point instance used for search.

        Returns
        -------
        Tuple[ Optional[BeamBase], Optional[BeamBase],
        Optional[BeamBase], Optional[BeamBase],
        Optional[ColumnBase], Optional[ColumnBase] ]
            0. If exists left beam along global x-axis, otherwise None,
            1. If exists right beam along global x-axis, otherwise None,
            2. If exists front beam along global y-axis, otherwise None,
            3. If exists rear beam along global y-axis, otherwise None,
            4. If exists top column along global z-axis, otherwise None,
            5. If exists bottom column along global z-axis, otherwise None
        """
        left_beamx = None
        right_beamx = None
        front_beamy = None
        rear_beamy = None
        top_column = None
        bottom_column = None
        lines = self.geometry.find_lines_by_point(node)
        for line in lines:
            beam = self._find_beam_by_line(line)
            if beam:
                if np.all(line.unit_vector == np.array([1.0, 0.0, 0.0])):
                    if node == beam.elastic_nodes[0]:
                        right_beamx = beam
                    elif node == beam.elastic_nodes[1]:
                        left_beamx = beam
                elif np.all(line.unit_vector == np.array([0.0, 1.0, 0.0])):
                    if node == beam.elastic_nodes[0]:
                        front_beamy = beam
                    elif node == beam.elastic_nodes[1]:
                        rear_beamy = beam
            else:
                column = self._find_column_by_line(line)
                if column:
                    if node == column.elastic_nodes[0]:
                        top_column = column
                    elif node == column.elastic_nodes[1]:
                        bottom_column = column

        return (
            left_beamx, right_beamx,
            front_beamy, rear_beamy,
            top_column, bottom_column
            )

    def _find_joint_by_point(self, node: Point) -> Optional[JointBase]:
        """Finds the joints by the given node/point.

        Parameters
        ----------
        node : Point
            Point instance used for search.

        Returns
        -------
        JointBase | None
            Returns Joint object if elastic_node attribute matches with
            given node, otherwise, returns None.
        """
        filtered_joints = filter(
            lambda joint: joint.elastic_node == node, self.joints)
        # Retrieve the first joint matching the condition
        matching_joint = next(filtered_joints, None)
        return matching_joint

    def _set_beam_gravity_loads(self) -> None:
        """Defines the uniformly distributed gravity loads for beams.

        The loads transferred from slabs are not factored by alpha.
        Hence, alpha factors corresponding to loads transferred from
        each slab are also set.
        """
        exterior_beam_lines = self.geometry.exterior_horizontal_lines

        for slab in self.slabs:
            beams = [self._find_beam_by_line(line)
                     for line in slab.rectangle.lines]

            for i, beam in enumerate(beams):
                tributary_area = slab.beam_tributary_areas[i]
                alpha = slab.beam_alpha_coeffs[i]
                # Add loads from slabs
                beam.slab_alpha.append(alpha)
                beam.slab_wg.append(tributary_area * slab.pg / beam.L)
                beam.slab_wq.append(tributary_area * slab.pq / beam.L)
                # Add infill loads to the exterior beams
                if beam.line in exterior_beam_lines:
                    beam.infill_wg = self.loads.permanent.infill
                else:
                    beam.infill_wg = 0.0
                # At roof level infills do not exist, remove
                if slab.roof:
                    beam.infill_wg = 0.0

        # TODO: Ask about this part to hossam
        mid_beams = self.stairs_midstorey_beams
        for i, slab in enumerate(self.stairs):
            # Beams with staircase loads
            mid_beam = mid_beams[i]
            rect_beams = [self._find_beam_by_line(line)
                          for line in slab.rectangle.lines]

            mid_beam.stairs_wg = slab.beam_influence_areas * \
                slab.pg / mid_beam.L
            mid_beam.stairs_wq = slab.beam_influence_areas * \
                slab.pq / mid_beam.L
            # TODO
            # Factor 0.5 changes from building to building, why?
            # (in general it is 0.5)
            mid_beam.infill_wg = 0.5 * self.loads.permanent.infill

            for j, beam in enumerate(rect_beams):
                if j == 1:  # The beam which supports staircase
                    # TODO
                    # In case of buildings from B07-B10 this is valid for j=3
                    # as well. Why?
                    beam.stairs_wg = slab.beam_influence_areas * \
                        slab.pg / beam.L
                    beam.stairs_wq = slab.beam_influence_areas * \
                        slab.pq / beam.L
                elif j in [0, 2]:
                    beam.infill_wg = self.loads.permanent.infill
                if j == 3:
                    beam.infill_wg = 0.0

                # At roof level infills do not exist
                if slab.roof:
                    beam.infill_wg = 0.0

    def _set_beam_predesign_forces(self) -> None:
        """Defines the beam predesign forces (mid-span moments and shears).

        The expected predesign forces are computed based on the gravity loads.
        The forces computed herein should be used only for the preliminary
        design of the beams.
        """
        # Get the gravity load combinations
        combos = self.loads.get_gravity_load_combos()

        for beam in self.beams:
            Md = 0.0
            Vd = 0.0
            for combo in combos:
                g_fact = combo.loads['G']
                q_fact = combo.loads['Q']
                # Moment at mid-span (alpha factored load)
                Md_tmp = g_fact*beam.simple_Mg + q_fact*beam.simple_Mq
                # Compute the shear at the support
                Vd_tmp = g_fact*beam.simple_Vg + q_fact*beam.simple_Vq
                # Update maximums
                Md = max(Md, Md_tmp)
                Vd = max(Vd, Vd_tmp)
            # Save the pre-design loads
            beam.pre_Md = Md
            beam.pre_Vd = Vd

    def _set_column_predesign_forces(self) -> None:
        """Defines the predesign forces (axial forces) for columns.

        The expected axial forces are first computed due to the gravity loads.
        These are then factored to account for increse in column axial forces
        due to the lateral loads in frame. The forces computed herein should be
        used only for the preliminary design of columns.
        """
        # Get the gravity load combinations
        combos = self.loads.get_gravity_load_combos()
        # Set the position factors
        position_factors = {
            'bot':
                {'central': 1.1,
                 'exterior': 1.3},
            'top':
                {'central': 1.3,
                 'exterior': 1.5}
                            }
        # Get properties of all vertical lines in the geometry
        vertical_lines = self.geometry.lines_z
        facade_ids = self.geometry.lines_z_facades
        max_floor = max(self.geometry.system_grid_data.z.ids)
        # Loop through each column and compute the axial forces due to
        # gravity loads of floor beams and column self weights.
        for column in self.columns:
            # Get position factor
            _, p2 = column.elastic_nodes
            if p2.grid_ids[2] > max_floor/2:
                lvl = "top"
            else:
                lvl = "bot"
            line_idx = vertical_lines.index(column.line)
            facade_id = facade_ids[line_idx]
            if facade_id == 0:
                loc = 'central'
            else:
                loc = 'exterior'
            position_factor = position_factors[lvl][loc]
            column.position_factor = position_factors[lvl][loc]
            # Find the lines of beams transfering gravity loads
            lines = self.geometry.find_lines_by_point(p2)
            # Compute the gravity loads from beams
            Ng = 0.0
            Nq = 0.0
            for line in lines:
                # Skip the columns
                if line not in vertical_lines:
                    beam = self._find_beam_by_line(line)
                    Ng += position_factor * (beam.wg_total * beam.L) / 2
                    Nq += position_factor * (beam.wq_total * beam.L) / 2
            # Add the self weight of column
            Ng += column.self_wg * column.H
            column.pre_Nq = Nq
            column.pre_Ng = Ng

        # If the the column is continuous, add upper storey forces
        for _, column_lists in self.continuous_columns.items():
            for columns in column_lists:
                columns.reverse()
                for i, column in enumerate(columns):
                    if i != 0:
                        column_i_1 = columns[i-1]
                        column.pre_Nq += column_i_1.pre_Nq
                        column.pre_Ng += column_i_1.pre_Ng

        # Compute maximum resulting axial forces from gravity load combinations
        for column in self.columns:
            Nd = 0.0
            for combo in combos:
                g_fact = combo.loads["G"]
                q_fact = combo.loads["Q"]
                tmp = g_fact * column.pre_Ng + q_fact * column.pre_Nq
                Nd = max(tmp, Nd)
            column.pre_Nd = Nd

    def _uniformize_stairs_columns(self) -> None:
        """Uniformizes the continuous columns of the same stairs.
        """
        stairs_columns_disagg = self._get_stairs_columns_disagg()
        for columns_list in stairs_columns_disagg:
            for columns in columns_list:
                bot_col, top_col = columns
                bx_max = max(bot_col.bx, top_col.bx)
                by_max = max(bot_col.by, top_col.by)
                bot_col.bx = bx_max
                bot_col.by = by_max
                top_col.bx = bx_max
                top_col.by = by_max

    def _ensure_column_dim_consistency(self) -> None:
        """Makes lower column dimensions are always greater or equal.
        """
        for _, column_lists in self.continuous_columns.items():
            for columns in column_lists:
                columns.reverse()
                for i, col in enumerate(columns):
                    if i != 0:  # Skip upper column
                        top_col = columns[i - 1]
                        bx_max = max([col.bx, top_col.bx])
                        by_max = max([col.by, top_col.by])
                        if col.bx <= bx_max:
                            col.bx = bx_max
                            col.by = by_max

    def _uniformize_columns_geometry(self) -> None:
        """Uniformizes column section dimensions on the same continuous lines.
        Notes
        -----
        If step size is only 1 storey lower than total number of stories in the
        building a constant section is used for column along the building.
        """
        # Uniformize the continuous columns of same stairs
        # TODO: This seems reduntant for now, following is enough.
        self._uniformize_stairs_columns()
        # Ensuring bottom column dimensions are always greater or equal
        self._ensure_column_dim_consistency()
        # Start section uniformisation
        step = self.COLUMN_UNIFORMIZATION_STEP  # step
        if step is None or (step >= self.num_storeys - 1):  # Constant section
            # If step is None or
            # If the difference between step and number of storeys is 1
            for _, column_lists in self.continuous_columns.items():
                for columns in column_lists:
                    # Get the maximums
                    bx = max(column.bx for column in columns)
                    by = max(column.by for column in columns)
                    # Assign maximum width to each column
                    for column in columns:
                        column.bx = bx
                        column.by = by
        else:
            all_stairs_columns = self._get_stairs_columns_agg()
            for _, column_lists in self.continuous_columns.items():
                for columns in column_lists:
                    # Find the columns with equal sections
                    steps = [0.5 if column in all_stairs_columns else 1.0
                             for column in columns]
                    levels = np.cumsum(steps)
                    remainders = levels % step
                    slices: List[List[ColumnBase]] = []
                    start = 0
                    for i, remainder in enumerate(remainders):
                        if remainder == 0:
                            slices.append(columns[start:i+1])
                            start = i+1
                    # Append the last slice if necessary
                    if remainders[-1] != 0:
                        slices.append(columns[start:])
                    # Now that we identified the columns with equal sections
                    bx = 0
                    by = 0
                    for cols in slices:
                        # Maximum dimensions per "step" columns
                        bx_tmp = max(column.bx for column in cols)
                        by_tmp = max(column.by for column in cols)
                        # To ensure that max difference is 0.10 m between
                        # consecutive varying sections
                        bx = ceil(20 * max(bx_tmp, bx - 0.10)) / 20
                        by = ceil(20 * max(by_tmp, by - 0.10)) / 20
                        for column in cols:
                            column.bx = bx
                            column.by = by

    def _uniformize_beam_geometry(self) -> None:
        """Uniformize the beam section dimensions on the same continuous lines.
        """
        # Beams along x direction
        for _, beam_lists in self.continuous_beams_x.items():
            for beams in beam_lists:
                b_max = ceil(20 * max(beam.b for beam in beams)) / 20
                h_max = ceil(20 * max(beam.h for beam in beams)) / 20
                for beam in beams:
                    beam.b = b_max
                    beam.h = h_max
        # Beams along y direction
        for _, beam_lists in self.continuous_beams_y.items():
            for beams in beam_lists:
                b_max = ceil(20 * max(beam.b for beam in beams)) / 20
                h_max = ceil(20 * max(beam.h for beam in beams)) / 20
                for beam in beams:
                    beam.b = b_max
                    beam.h = h_max

    def _predesign(self) -> None:
        """Does preliminary design of the building beams and columns.

        1) Makes initial guess for section dimensions.
        2) Uniformizes the column sections along the continuous lines.
        3) Uniformizes the beam sections along the continuous lines.
        4) Store preliminary design dimensions.
        """
        # Set design forces for columns and beams
        self._set_column_predesign_forces()
        self._set_beam_predesign_forces()
        # Predesign columns, guess the initial dimensions
        for column in self.columns:
            column.predesign_section_dimensions()
        # Uniformize column sections
        self._uniformize_columns_geometry()
        # Set preliminary design dimensions
        for column in self.columns:
            column.pre_bx = column.bx
            column.pre_by = column.by
        # Predesign beams, guess the initial dimensions
        for beam in self.beams:
            beam.predesign_section_dimensions(self.slab_thickness)
        # Uniformize beam sections
        self._uniformize_beam_geometry()
        # Set preliminary design dimensions
        for beam in self.beams:
            beam.pre_b = beam.b
            beam.pre_h = beam.h

    def _change_materials(self) -> None:
        """The method used for changing materials in iterative design
        algorithm.

        Can be overwritten for each design class.
        """
        # Update the concrete material if it is not the last one
        if self.next_concrete:
            self.concrete = self.next_concrete
        # Update the steel material if it is not the last one
        if self.next_steel:
            self.steel = self.next_steel

    def _change_beam_type(self) -> None:
        """The method used for changing beam types.

        Can be overwritten for each design class.
        """
        self.beam_type = 2

    def _change_column_section(self) -> None:
        """The method used for changing column sections.

        Can be overwritten for each design class.
        """
        self.column_section = 1

    def _increase_beam_dimensions(self) -> None:
        """Used to increase beam dimensions in iterative design algorithm.
        """
        for beam in self.beams:
            beam.increase_dimensions()

    def _increase_column_dimensions(self) -> None:
        """Used to increase column dimensions in iterative design algorithm.
        """
        for column in self.columns:
            column.increase_dimensions()

    def _restore_dimensions(self) -> None:
        """Restore beam and column dimensions from preliminary design."""
        for column in self.columns:
            column.restore_dimensions()
        for beam in self.beams:
            beam.restore_dimensions()

    def _restore_materials(self) -> None:
        """Restore beam and column materials to initial."""
        self._initialize_materials()

    def _set_restore_point(self) -> None:
        """Sets the restore point for beams and columns."""
        for column in self.columns:
            column.set_restore_point()
        for beam in self.beams:
            beam.set_restore_point()

    def _perform_structural_analyses(self) -> None:
        """Analyze the building with all the load cases and combinations.
        """
        # Create the elastic model with current beam and column dimensions
        elastic_model = self.ElasticModelClass(
            self.beams, self.columns, self.loads, self.geometry, self.beta)
        # Determine element forces for each loading combination
        elastic_model.analyze_for_all()

    def _make_trial_structural_design(self) -> None:
        """Makes a trial structural design and checks if it is ok or not.
        """
        self._design_beams_for_flexure()
        self._design_columns_for_flexure()
        self._design_beams_for_shear()
        self._design_columns_for_shear()
        self._validate_structural_design()

    def _validate_structural_design(self) -> None:
        """Determines whether the current design is satisfactory or not.

        All structural element should meet the design criteria.
        """
        if self.beams_fail or self.columns_fail:
            self.ok = False
        else:
            self.ok = True

    def __print_beam_failure(self, text: str) -> None:
        """Prints the number of failed beams and their dimensions.
        """
        idxs = [i for i, beam in enumerate(self.beams) if not beam.ok]
        print(
            len(idxs), f"beams failed to pass {text} design verification."
            )
        # for idx in idxs:
        #     print(f"beam:{idx}, h={self.beams[idx].h},"
        #           f"b={self.beams[idx].b}")

    def __print_column_failure(self, text: str) -> None:
        """Prints the number of failed columns and their dimensions.
        """
        idxs = [i for i, col in enumerate(self.columns)
                if not (col.ok_x and col.ok_y)]
        print(
            f"{len(idxs)} columns failed to pass {text} design verification."
            )
        # for idx in idxs:
        #     print(f"Column:{idx}, bx={self.columns[idx].bx},"
        #           f"by={self.columns[idx].by}")

    def _validate_beam_section_dimensions(self) -> None:
        """Checks if section dimensions of beam are adequate and
        validates against maximum dimensions."""
        for beam in self.beams:
            beam.verify_section_adequacy()
            beam.validate_section_dimensions()

    def _validate_column_section_dimensions(self) -> None:
        """Checks if section dimensions of columns are adequate and
        validates against maximum dimensions."""
        for column in self.columns:
            column.verify_section_adequacy()
            column.validate_section_dimensions()

    def _design_beams_for_flexure(self) -> None:
        """Performs flexure design of the beams.

        1. Perform section adequacy checks (e.g., max. normalized moment).
        2. If the section is adequate for given design forces,
        compute required longitudinal reinforcement area. Then,
        find the rebar solution to meet detailing requirements and validate.
        """
        # STAGE 1: Section adequacy check for design forces.
        self._validate_beam_section_dimensions()
        if self.beams_fail:
            self.__print_beam_failure('stage 1 flexure')
            return  # Beams are not ok, exit and try again with new section

        # STAGE 2: Longitudinal reinforcement design.
        for beam in self.beams:
            beam.compute_required_longitudinal_reinforcement()
        for beams in self._continuous_beams:
            # Append required information of continuous beams
            Asl_top = np.array([])
            Asl_bot = np.array([])
            b = np.array([])
            for beam in beams:
                Asl_top = np.append(Asl_top, beam.Asl_top_req)
                Asl_bot = np.append(Asl_bot, beam.Asl_bot_req)
                b = np.append(b, np.array([beam.b]*len(beam.Asl_top_req)))
            # Determine rebar arrangement
            (
                dbl_t1, nbl_t1, dbl_t2, nbl_t2,
                dbl_b1, nbl_b1, dbl_b2, nbl_b2
            ) = self.rebars.get_beam_long_rebars(Asl_top, Asl_bot, b)

            # NOTE: Use the same reinforcement at two adjacent beam ends
            # Required for lap splices at joints (cont. reinf.)
            # NOTE: This could be unrealistic for adjacent spans with
            # very different lengths
            for kk in range(2, len(nbl_b2)-3, 3):
                nbl_t1[kk] = max(nbl_t1[kk],
                                 nbl_t1[kk + 1])
                nbl_t1[kk+1] = max(nbl_t1[kk],
                                   nbl_t1[kk + 1])
                nbl_t2[kk] = max(nbl_t2[kk],
                                 nbl_t2[kk + 1])
                nbl_t2[kk+1] = max(nbl_t2[kk],
                                   nbl_t2[kk + 1])
                nbl_b1[kk] = max(nbl_b1[kk],
                                 nbl_b1[kk + 1])
                nbl_b1[kk+1] = max(nbl_b1[kk],
                                   nbl_b1[kk + 1])
                nbl_b2[kk] = max(nbl_b2[kk],
                                 nbl_b2[kk + 1])
                nbl_b2[kk+1] = max(nbl_b2[kk],
                                   nbl_b2[kk + 1])
            # Store rebar solutions and validate
            for i, beam in enumerate(beams):
                beam.dbl_t1 = dbl_t1[3*i:3*(i+1)]
                beam.nbl_t1 = nbl_t1[3*i:3*(i+1)]
                beam.dbl_t2 = dbl_t2[3*i:3*(i+1)]
                beam.nbl_t2 = nbl_t2[3*i:3*(i+1)]
                beam.dbl_b1 = dbl_b1[3*i:3*(i+1)]
                beam.nbl_b1 = nbl_b1[3*i:3*(i+1)]
                beam.dbl_b2 = dbl_b2[3*i:3*(i+1)]
                beam.nbl_b2 = nbl_b2[3*i:3*(i+1)]
                beam.validate_longitudinal_reinforcement()
        # Check if beams fail stage 2 flexure design verification
        if self.beams_fail:
            self.__print_beam_failure('stage 2 flexure')

    def _set_column_capacity_design_moments(self) -> None:
        """Appends the capacity design moments to the list of design forces
        for columns.

        References
        ----------
        EN 1998-1:2004 4.4.2.3(4)
        """
        if self.OVERSTRENGTH_FACTOR_COLUMN_MOMENT is None:  # Do not add
            return
        else:
            gamma_rd = self.OVERSTRENGTH_FACTOR_COLUMN_MOMENT

        # Unique gravity load factors from seismic load combinations
        combo_grav_factors = self._get_unique_seism_combo_grav_factors()
        # Loop through each beam-column joint
        for joint in self.joints:
            # Sum of the design values of moment of resistances for beams
            sum_mrdb_x_pos = 0.0
            sum_mrdb_x_neg = 0.0
            sum_mrdb_y_pos = 0.0
            sum_mrdb_y_neg = 0.0
            if joint.left_beam:
                sum_mrdb_x_pos += joint.left_beam.mrd_pos[-1]
                sum_mrdb_x_neg += joint.left_beam.mrd_neg[-1]
            if joint.right_beam:
                sum_mrdb_x_pos += joint.right_beam.mrd_neg[0]
                sum_mrdb_x_neg += joint.right_beam.mrd_pos[0]
            if joint.rear_beam:
                sum_mrdb_y_pos += joint.rear_beam.mrd_pos[-1]
                sum_mrdb_y_neg += joint.rear_beam.mrd_neg[-1]
            if joint.front_beam:
                sum_mrdb_y_pos += joint.front_beam.mrd_neg[0]
                sum_mrdb_y_neg += joint.front_beam.mrd_pos[0]
            sum_mrdb_y = max(sum_mrdb_y_pos, sum_mrdb_y_neg)
            sum_mrdb_x = max(sum_mrdb_x_pos, sum_mrdb_x_neg)

            # Capacity design forces for columns
            for factors in combo_grav_factors:
                # Both top and bottom columns exist
                if joint.top_column and joint.bottom_column:
                    forces_top = (
                        factors['G']*joint.top_column.forces['G/seismic'] +
                        factors['Q']*joint.top_column.forces['Q/seismic']
                        )
                    forces_bottom = (
                        factors['G']*joint.bottom_column.forces['G/seismic'] +
                        factors['Q']*joint.bottom_column.forces['Q/seismic']
                        )
                    forces_top.Mx1 = 0.5 * gamma_rd * sum_mrdb_y
                    forces_top.My1 = 0.5 * gamma_rd * sum_mrdb_x
                    joint.top_column.design_forces.append(forces_top)
                    forces_bottom.Mx9 = 0.5 * gamma_rd * sum_mrdb_y
                    forces_bottom.My9 = 0.5 * gamma_rd * sum_mrdb_x
                    joint.bottom_column.design_forces.append(forces_bottom)
                # Only top column exists
                elif joint.top_column:
                    forces_top = (
                        factors['G']*joint.top_column.forces['G/seismic'] +
                        factors['Q']*joint.top_column.forces['Q/seismic']
                        )
                    forces_top.Mx1 = gamma_rd * sum_mrdb_y
                    forces_top.My1 = gamma_rd * sum_mrdb_x
                    joint.top_column.design_forces.append(forces_top)
                # Only bottom column exists
                elif joint.bottom_column:
                    forces_bottom = (
                        factors['G']*joint.bottom_column.forces['G/seismic'] +
                        factors['Q']*joint.bottom_column.forces['Q/seismic']
                        )
                    forces_bottom.Mx9 = gamma_rd * sum_mrdb_y
                    forces_bottom.My9 = gamma_rd * sum_mrdb_x
                    joint.bottom_column.design_forces.append(forces_bottom)

    def _set_beam_capacity_design_shear_forces(self) -> None:
        """Appends the beam capacity design shear forces to the list of
        beam design forces.

        References
        ----------
        EN 1998-1:2004 5.4.2.2
        """

        def get_sum_mrdb_at_joint(joint: JointBase) -> Tuple[float, float]:
            """Gets the summation of moment of resistances of joint beams.

            Parameters
            ----------
            joint : JointBase
                Instance of the Joint object.

            Returns
            -------
            Tuple[float, float]
                Summation of moment of resistances of joint beams for
                positive and negative directions.
            """
            # Sum of the design values of moment of resistances for beams
            sum_mrd_pos = 0.0  # In positive direction
            sum_mrd_neg = 0.0  # In negative direction

            if beam.direction == 'x':
                # Beam is along x-axis
                if joint.left_beam:
                    sum_mrd_pos += joint.left_beam.mrd_pos[-1]
                    sum_mrd_neg += joint.left_beam.mrd_neg[-1]
                if joint.right_beam:
                    sum_mrd_pos += joint.right_beam.mrd_neg[0]
                    sum_mrd_neg += joint.right_beam.mrd_pos[0]
            elif beam.direction == 'y':
                # Beam is along y-axis
                if joint.rear_beam:
                    sum_mrd_pos += joint.rear_beam.mrd_pos[-1]
                    sum_mrd_neg += joint.rear_beam.mrd_neg[-1]
                if joint.front_beam:
                    sum_mrd_pos += joint.front_beam.mrd_neg[0]
                    sum_mrd_neg += joint.front_beam.mrd_pos[0]

            return sum_mrd_pos, sum_mrd_neg

        def get_sum_mrdc_at_joint(joint: JointBase) -> float:
            """Gets the summation of moment of resistances of joint columns.

            Parameters
            ----------
            joint : JointBase
                Instance of the Joint object.

            Returns
            -------
            float
                Summation of moment of resistances of joint columns.
            """
            # Sum of the design values of moment of resistances for columns
            sum_mrd = 0.0  # Same for positive and negative directions
            # Top column exists
            if joint.top_column:
                forces_top = (
                    factors['G']*joint.top_column.forces['G/seismic'] +
                    factors['Q']*joint.top_column.forces['Q/seismic']
                    )
                if beam.direction == 'x':  # use column mrd_y
                    sum_mrd += joint.top_column.get_mrdy(Ned=forces_top.N1)
                elif beam.direction == 'y':  # use column mrd_x
                    sum_mrd += joint.top_column.get_mrdx(Ned=forces_top.N1)
            # Bottom column exists
            if joint.bottom_column:
                forces_bottom = (
                    factors['G']*joint.bottom_column.forces['G/seismic'] +
                    factors['Q']*joint.bottom_column.forces['Q/seismic']
                    )
                if beam.direction == 'x':  # Use column mrd_y
                    sum_mrd += joint.bottom_column.get_mrdy(
                        Ned=forces_bottom.N9)
                elif beam.direction == 'y':  # Use column mrd_x
                    sum_mrd += joint.bottom_column.get_mrdx(
                        Ned=forces_bottom.N9)

            return sum_mrd

        def get_beam_clear_length() -> float:
            """Gets beam clear length (distance between column faces).

            Returns
            -------
            float
                Beam clear length
            """
            # i'th joint width
            if joint_i.top_column and joint_i.bottom_column:
                if beam.direction == 'x':
                    bc_i = min(joint_i.top_column.bx, joint_i.bottom_column.bx)
                elif beam.direction == 'y':
                    bc_i = min(joint_i.top_column.by, joint_i.bottom_column.by)
            elif joint_i.top_column:
                if beam.direction == 'x':
                    bc_i = joint_i.top_column.bx
                if beam.direction == 'y':
                    bc_i = joint_i.top_column.by
            elif joint_i.bottom_column:
                if beam.direction == 'x':
                    bc_i = joint_i.bottom_column.bx
                if beam.direction == 'y':
                    bc_i = joint_i.bottom_column.by
            # j'th joint width
            if joint_j.top_column and joint_j.bottom_column:
                if beam.direction == 'x':
                    bc_j = min(joint_j.top_column.bx, joint_j.bottom_column.bx)
                elif beam.direction == 'y':
                    bc_j = min(joint_j.top_column.by, joint_j.bottom_column.by)
            elif joint_j.top_column:
                if beam.direction == 'x':
                    bc_j = joint_j.top_column.bx
                if beam.direction == 'y':
                    bc_j = joint_j.top_column.by
            elif joint_j.bottom_column:
                if beam.direction == 'x':
                    bc_j = joint_j.bottom_column.bx
                if beam.direction == 'y':
                    bc_j = joint_j.bottom_column.by
            # Return beam clear length
            return beam.L - (bc_i + bc_j) / 2

        # Check if the capacity design forces will be added
        if self.OVERSTRENGTH_FACTOR_BEAM_SHEAR is None:  # Do not add
            return
        else:  # Add
            gamma_rd = self.OVERSTRENGTH_FACTOR_BEAM_SHEAR

        # Unique gravity load factors from seismic load combinations
        combo_grav_factors = self._get_unique_seism_combo_grav_factors()
        # Loop through each beam
        for beam in self.beams:
            # Find joints at both ends
            joint_i = self._find_joint_by_point(beam.elastic_nodes[0])
            joint_j = self._find_joint_by_point(beam.elastic_nodes[1])
            # Sum of the moment of resistances of the joint beams
            sum_mrdb_i_pos, sum_mrdb_i_neg = get_sum_mrdb_at_joint(joint_i)
            sum_mrdb_j_pos, sum_mrdb_j_neg = get_sum_mrdb_at_joint(joint_j)
            # Clear length of beam
            beam_lc = get_beam_clear_length()

            # Capacity design forces for columns
            for factors in combo_grav_factors:
                # Shear force due to gravity loads (g+nq)
                Vd = (factors['G']*beam.wg_total +
                      factors['Q']*beam.wq_total) * (beam_lc / 2)
                # Sum of the moment of resistances of the joint columns
                sum_mrdc_i = get_sum_mrdc_at_joint(joint_i)
                sum_mrdc_j = get_sum_mrdc_at_joint(joint_j)
                # The beam moment of resistances at both ends
                Mpi_pos = gamma_rd * beam.mrd_pos[0] * min(
                    1.0, sum_mrdc_i/sum_mrdb_i_pos)
                Mpi_neg = gamma_rd * beam.mrd_neg[0] * min(
                    1.0, sum_mrdc_i/sum_mrdb_i_neg)
                Mpj_pos = gamma_rd * beam.mrd_pos[-1] * min(
                    1.0, sum_mrdc_j/sum_mrdb_j_pos)
                Mpj_neg = gamma_rd * beam.mrd_neg[-1] * min(
                    1.0, sum_mrdc_j/sum_mrdb_j_neg)
                # Capacity design shear forces at both ends
                Ved_i_pos = Vd + (Mpi_pos + Mpj_neg) / beam_lc
                Ved_i_neg = Vd - (Mpi_neg + Mpj_pos) / beam_lc
                Ved_j_pos = Vd + (Mpj_pos + Mpi_neg) / beam_lc
                Ved_j_neg = Vd - (Mpj_neg + Mpi_pos) / beam_lc
                # Set the forces and append
                forces = beam.design_forces[-1] - beam.design_forces[-1]
                forces.case = 'seismic'
                forces.V1 = max(Ved_i_pos, abs(Ved_i_neg))
                forces.V9 = max(Ved_j_pos, abs(Ved_j_neg))
                """TODO: Set also design moments as Mp values?
                It does not makes sense to make another check for design
                moment though. Hence, we might need to separate section
                adequacy verification for shear and flexure forces.
                """
                beam.design_forces.append(forces)

    def _design_beams_for_shear(self) -> None:
        """Performs shear design of the beams.

        1. Check if beam and column flexure designs are ok, if ok continue.
        2. Add capacity design shear forces to the design forces list. Then,
        perform section adequacy checks (e.g., checks shear stress).
        If beam sections are ok, continue.
        3. Compute required shear reinforcement (area / spacing). Then,
        find the rebar solution to meet detailing requirements and validate.
        """
        # STAGE 1: Check beam and column flexure designs.
        if self.beams_fail or self.columns_fail:
            return  # Beams or columns are not ok, exit and try again

        # STAGE 2: Section adequacy check for capacity design forces
        self._set_beam_capacity_design_shear_forces()
        self._validate_beam_section_dimensions()
        if self.beams_fail:
            self.__print_beam_failure('stage 1 shear')
            return  # Beams are not ok, exit and try again with new section

        # STAGE 3: Transverse reinforcement design
        for beam in self.beams:
            # Compute required transverse reinforcement
            beam.compute_required_transverse_reinforcement()
        # Determine transverse reinforcement (horizontal rebar) solution
        for beams in self._continuous_beams:
            # Append required information of continuous beams
            Ash_sbh = np.array([])
            nbl_t1 = np.array([])
            nbl_t2 = np.array([])
            nbl_b1 = np.array([])
            nbl_b2 = np.array([])
            dbl_t1 = np.array([])
            dbl_b1 = np.array([])
            b = np.array([])
            h = np.array([])
            for beam in beams:
                Ash_sbh = np.append(Ash_sbh, beam.Ash_sbh_req)
                nbl_t1 = np.append(nbl_t1, beam.nbl_t1)
                nbl_t2 = np.append(nbl_t2, beam.nbl_t2)
                nbl_b1 = np.append(nbl_b1, beam.nbl_b1)
                nbl_b2 = np.append(nbl_b2, beam.nbl_b2)
                dbl_t1 = np.append(dbl_t1, beam.dbl_t1)
                dbl_b1 = np.append(dbl_b1, beam.dbl_b1)
                b = np.append(b, np.array([beam.b]*len(beam.Asl_top_req)))
                h = np.append(h, np.array([beam.h]*len(beam.Asl_top_req)))
            # Determine transverse reinforcement solution
            dbh, sbh, nbh_x, nbh_y = self.rebars.get_beam_transv_rebars(
                Ash_sbh, nbl_t1, nbl_t2, nbl_b1,
                nbl_b2, dbl_t1, dbl_b1, b, h
                )
            # Store rebar solutions and validate
            for i, beam in enumerate(beams):
                beam.dbh = dbh[3*i:3*(i+1)]
                beam.sbh = sbh[3*i:3*(i+1)]
                beam.nbh_b = nbh_x[3*i:3*(i+1)]
                beam.nbh_h = nbh_y[3*i:3*(i+1)]
                beam.validate_transverse_reinforcement()
        if self.beams_fail:
            self.__print_beam_failure('stage 2 shear')

    def _design_columns_for_flexure(self) -> None:
        """Performs flexure design of the columns.

        1. Check if beam flexure designs are ok. If beams are ok, continue.
        2. Add capacity design moments to the design forces list. Then,
        perform section adequacy checks (e.g., checks shear stress).
        If column sections are ok, continue.
        3. Compute required longitudinal reinforcement area. Then,
        find the rebar solution to meet detailing requirements and valdiate.
        """
        # STAGE 1: Check beam flexure designs
        if self.beams_fail:  # Beam sections are not verified.
            # Do section adequacy checks regardless (for faster convergence)
            self._validate_column_section_dimensions()
            return  # Beams are not ok, exit and try again.

        # STAGE 2: Section adequacy checks with capacity design moments.
        self._set_column_capacity_design_moments()
        self._validate_column_section_dimensions()
        if self.columns_fail:
            self.__print_column_failure('stage 1 flexure')
            return  # Columns are not ok, exit and try again

        # STAGE 3: Longitudinal reinforcement design
        for col in self.columns:
            col.compute_required_longitudinal_reinforcement()
        for columns in self._continuous_columns:
            # Append required information of continuous columns
            Aslx_req = np.array([])
            Asly_req = np.array([])
            rhol_min = np.array([])
            bx = np.array([])
            by = np.array([])
            for col in columns:
                Aslx_req = np.append(Aslx_req, col.Aslx_req)
                Asly_req = np.append(Asly_req, col.Asly_req)
                rhol_min = np.append(rhol_min, col.rhol_min)
                bx = np.append(bx, col.bx)
                by = np.append(by, col.by)
            # Determine rebar arrangement
            (
                dbl_cor, dbl_int, nblx_int, nbly_int
            ) = self.rebars.get_column_long_rebars(
                Aslx_req, Asly_req, rhol_min, bx, by
            )
            # Store rebar solutions and validate
            for i, col in enumerate(columns):
                col.dbl_cor = dbl_cor[i]
                col.dbl_int = dbl_int[i]
                col.nblx_int = nblx_int[i]
                col.nbly_int = nbly_int[i]
                col.validate_longitudinal_reinforcement()
        # Check if columns fail stage 2 flexure design verification
        if self.columns_fail:
            self.__print_column_failure('stage 2 flexure')

    def _set_column_capacity_design_shear_forces(self) -> None:
        """Appends the column capacity design shear forces to the list of
        column design forces.

        References
        ----------
        EN 1998-1:2004 5.4.2.3
        """

        def get_sum_mrdb_at_joint(joint: JointBase) -> Tuple[float, float]:
            """Gets the summation of moment of resistances of joint beams.

            Parameters
            ----------
            joint : JointBase
                Instance of the Joint object.

            Returns
            -------
            Tuple[float, float]
                Summation of moment of resistances of joint beams for
                positive and negative directions.
            """
            # Sum of the design values of moment of resistances for beams
            sum_mrdb_x_pos = 0.0
            sum_mrdb_x_neg = 0.0
            sum_mrdb_y_pos = 0.0
            sum_mrdb_y_neg = 0.0
            if joint.left_beam:
                sum_mrdb_x_pos += joint.left_beam.mrd_pos[-1]
                sum_mrdb_x_neg += joint.left_beam.mrd_neg[-1]
            if joint.right_beam:
                sum_mrdb_x_pos += joint.right_beam.mrd_neg[0]
                sum_mrdb_x_neg += joint.right_beam.mrd_pos[0]
            if joint.rear_beam:
                sum_mrdb_y_pos += joint.rear_beam.mrd_pos[-1]
                sum_mrdb_y_neg += joint.rear_beam.mrd_neg[-1]
            if joint.front_beam:
                sum_mrdb_y_pos += joint.front_beam.mrd_neg[0]
                sum_mrdb_y_neg += joint.front_beam.mrd_pos[0]

            return (sum_mrdb_x_pos, sum_mrdb_x_neg,
                    sum_mrdb_y_pos, sum_mrdb_y_neg)

        def get_sum_mrdc_at_joint(joint: JointBase) -> Tuple[float, float]:
            """Gets the summation of moment of resistances of joint columns.

            Parameters
            ----------
            joint : JointBase
                Instance of the Joint object.

            Returns
            -------
            Tuple[float, float]
                Summation of moment of resistances of joint columns around
                local x and y axes of columns.
            """
            # Sum of the design values of moment of resistances for columns
            sum_mrd_x = 0.0
            sum_mrd_y = 0.0
            # Top column exists
            if joint.top_column:
                forces_top = (
                    factors['G']*joint.top_column.forces['G/seismic'] +
                    factors['Q']*joint.top_column.forces['Q/seismic']
                    )
                sum_mrd_x += joint.top_column.get_mrdx(Ned=forces_top.N1)
                sum_mrd_y += joint.top_column.get_mrdy(Ned=forces_top.N1)
            # Bottom column exists
            if joint.bottom_column:
                forces_bottom = (
                    factors['G']*joint.bottom_column.forces['G/seismic'] +
                    factors['Q']*joint.bottom_column.forces['Q/seismic']
                    )
                sum_mrd_x += joint.bottom_column.get_mrdx(Ned=forces_bottom.N9)
                sum_mrd_y += joint.bottom_column.get_mrdy(Ned=forces_bottom.N9)

            return sum_mrd_x, sum_mrd_y

        def get_column_clear_length() -> Tuple[float, float]:
            """Gets column clear length (distance between column faces).

            Returns
            -------
            Tuple[float, float]
                Column clear lengths for shear forces in local x and y axes.
            """
            hx_i = 1000
            hx_j = 1000
            hy_i = 1000
            hy_j = 1000
            # i'th joint height
            if joint_i.left_beam:
                hx_i = min(hx_i, joint_i.left_beam.h)
            if joint_i.right_beam:
                hx_i = min(hx_i, joint_i.right_beam.h)
            if joint_i.rear_beam:
                hy_i = min(hy_i, joint_i.rear_beam.h)
            if joint_i.front_beam:
                hy_i = min(hy_i, joint_i.front_beam.h)
            # j'th joint height
            if joint_j.left_beam:
                hx_j = min(hx_j, joint_j.left_beam.h)
            if joint_j.right_beam:
                hx_j = min(hx_j, joint_j.right_beam.h)
            if joint_j.rear_beam:
                hy_j = min(hy_j, joint_j.rear_beam.h)
            if joint_j.front_beam:
                hy_j = min(hy_j, joint_j.front_beam.h)
            if hx_i == 1000:
                hx_i = 0.0
            if hx_j == 1000:
                hx_j = 0.0
            if hy_i == 1000:
                hy_i = 0.0
            if hy_j == 1000:
                hy_j = 0.0

            # Return beam clear length
            lclx = column.H - (hx_i + hx_j) / 2
            lcly = column.H - (hy_i + hy_j) / 2

            return lclx, lcly

        # Check if the capacity design forces will be added
        if self.OVERSTRENGTH_FACTOR_COLUMN_SHEAR is None:  # Do not add
            return
        else:  # Add
            gamma_rd = self.OVERSTRENGTH_FACTOR_COLUMN_SHEAR

        # Unique gravity load factors from seismic load combinations
        combo_grav_factors = self._get_unique_seism_combo_grav_factors()
        # Loop through each beam
        for column in self.columns:
            # Find joints at both ends
            joint_i = self._find_joint_by_point(column.elastic_nodes[0])
            joint_j = self._find_joint_by_point(column.elastic_nodes[1])
            # Sum of the moment of resistances of the joint beams
            (sum_mrdb_x_pos_i, sum_mrdb_x_neg_i, sum_mrdb_y_pos_i,
             sum_mrdb_y_neg_i) = get_sum_mrdb_at_joint(joint_i)
            (sum_mrdb_x_pos_j, sum_mrdb_x_neg_j, sum_mrdb_y_pos_j,
             sum_mrdb_y_neg_j) = get_sum_mrdb_at_joint(joint_j)
            # Clear lengths of column in x and y
            col_lcx, col_lcy = get_column_clear_length()

            # Capacity design forces for columns
            for factors in combo_grav_factors:
                # Initialize column forces
                forces = (
                    factors['G']*column.forces['G/seismic'] +
                    factors['Q']*column.forces['Q/seismic']
                    )
                forces.case = 'seismic'
                # The beam moment of resistances at both ends
                mrdx_i = column.get_mrdx(Ned=forces.N1)
                mrdy_i = column.get_mrdy(Ned=forces.N1)
                mrdx_j = column.get_mrdx(Ned=forces.N9)
                mrdy_j = column.get_mrdy(Ned=forces.N9)
                # Sum of the moment of resistances of the joint columns
                sum_mrdc_x_i, sum_mrdc_y_i = get_sum_mrdc_at_joint(joint_i)
                sum_mrdc_x_j, sum_mrdc_y_j = get_sum_mrdc_at_joint(joint_j)
                # Plastic moments around column local x and y
                if column.elastic_nodes[0] in self.elastic_nodes_ground:
                    """TODO: Special case is the ground floor --> Discuss
                    Even though not specified in the building codes (i.e, EC8),
                    max moment is the column capacity at the support node."""
                    Mpi_x_pos = gamma_rd * mrdx_i
                    Mpi_x_neg = gamma_rd * mrdx_i
                    Mpi_y_pos = gamma_rd * mrdy_i
                    Mpi_y_neg = gamma_rd * mrdy_i
                else:
                    Mpi_x_pos = gamma_rd * mrdx_i * min(
                        1.0, sum_mrdb_y_pos_i/sum_mrdc_x_i)
                    Mpi_x_neg = gamma_rd * mrdx_i * min(
                        1.0, sum_mrdb_y_neg_i/sum_mrdc_x_i)
                    Mpi_y_pos = gamma_rd * mrdy_i * min(
                        1.0, sum_mrdb_x_pos_i/sum_mrdc_y_i)
                    Mpi_y_neg = gamma_rd * mrdy_i * min(
                        1.0, sum_mrdb_x_neg_i/sum_mrdc_y_i)
                Mpj_x_pos = gamma_rd * mrdx_j * min(
                    1.0, sum_mrdb_y_pos_j/sum_mrdc_x_j)
                Mpj_x_neg = gamma_rd * mrdx_j * min(
                    1.0, sum_mrdb_y_neg_j/sum_mrdc_x_j)
                Mpj_y_pos = gamma_rd * mrdy_j * min(
                    1.0, sum_mrdb_x_pos_j/sum_mrdc_y_j)
                Mpj_y_neg = gamma_rd * mrdy_j * min(
                    1.0, sum_mrdb_x_neg_j/sum_mrdc_y_j)
                # Capacity design shear forces at both ends
                Vdx_pos = (Mpi_y_pos + Mpj_y_neg) / col_lcx
                Vdx_neg = (Mpi_y_neg + Mpj_y_pos) / col_lcx
                Vdy_pos = (Mpi_x_pos + Mpj_x_neg) / col_lcy
                Vdy_neg = (Mpi_x_neg + Mpj_x_pos) / col_lcy
                # Set the forces and append
                forces.Vx1 = max(Vdx_pos, Vdx_neg)
                forces.Vx9 = max(Vdx_pos, Vdx_neg)
                forces.Vy1 = max(Vdy_pos, Vdy_neg)
                forces.Vy9 = max(Vdy_pos, Vdy_neg)
                """TODO: Set also design moments as Mp values?
                It does not makes sense to make another check for design
                moment though. Hence, we might need to separate section
                adequacy verification for shear and flexure forces.
                """
                column.design_forces.append(forces)

    def _design_columns_for_shear(self) -> None:
        """Performs shear design of the columns.

        1. Check if beam and column flexure designs are ok, if ok continue.
        2. Add capacity design shear forces to the design forces list. Then,
        perform section adequacy checks (e.g., checks shear stress).
        If column sections are ok, continue.
        3. Compute required shear reinforcement (area / spacing). Then,
        find the rebar solution to meet detailing requirements and validate.
        """

        # STAGE 1: Check beam designs and column flexure designs
        if self.beams_fail or self.columns_fail:  # They are not ok
            return  # Exit and try again.

        # STAGE 2: Section adequacy checks with capacity design shear forces.
        self._set_column_capacity_design_shear_forces()
        self._validate_column_section_dimensions()
        if self.columns_fail:
            self.__print_column_failure('stage 1 shear')
            return  # Columns are not ok, exit and try again with new sections

        # STAGE 3: Transverse reinforcement design
        for col in self.columns:
            col.compute_required_transverse_reinforcement()
        # Stage 3: Determine rebar distribution
        for columns in self._continuous_columns:
            # Organize
            dbl_c = np.array([])
            nbl_ix = np.array([])
            nbl_iy = np.array([])
            Ashx_sbh_req = np.array([])
            Ashy_sbh_req = np.array([])
            bx = np.array([])
            by = np.array([])
            for col in columns:
                dbl_c = np.append(dbl_c, col.dbl_cor)
                nbl_ix = np.append(nbl_ix, col.nblx_int)
                nbl_iy = np.append(nbl_iy, col.nbly_int)
                Ashx_sbh_req = np.append(Ashx_sbh_req,
                                         col.Ashx_sbh_req)
                Ashy_sbh_req = np.append(Ashy_sbh_req,
                                         col.Ashy_sbh_req)
                bx = np.append(bx, col.bx)
                by = np.append(by, col.by)
            # Determine rebar arrangement
            (
                dbh, sbh, nbh_x, nbh_y
            ) = self.rebars.get_column_transv_rebars(
                bx, by, Ashx_sbh_req, Ashy_sbh_req, dbl_c, nbl_ix, nbl_iy
                )
            for i, col in enumerate(columns):
                col.dbh = dbh[i]
                col.sbh = sbh[i]
                col.nbh_x = nbh_x[i]
                col.nbh_y = nbh_y[i]
                col.validate_transverse_reinforcement()
        # Check if columns fail stage 2 shear design verification
        if self.columns_fail:
            self.__print_column_failure('stage 2 shear')

    def run_iterative_design_algorithm(self) -> None:
        """Routine for iterative design algorithm.

        Notes
        -----
        The algorithm is slightly different than the original algorithm.
        """
        counter = 0  # Counter for design iterations
        while not self.ok and counter <= self.ITER_MAX:  # Iteration loop
            if counter == 0:  # Preliminary design stage
                self._predesign()  # Make a preliminary design
            elif self.dim_change:  # Try increasing beam and column dimensions
                self._increase_beam_dimensions()  # Increase beams
                self._uniformize_beam_geometry()  # Uniformize beams
                self._increase_column_dimensions()  # Increase columns
                self._uniformize_columns_geometry()  # Uniformize columns
            elif self.beams_fail:  # If beams fail to pass design checks
                if self.beam_change:  # Try changing beam type
                    self._change_beam_type()  # Can be overwritten
                    self._restore_materials()  # Restore initial dimensions
                    self._restore_dimensions()  # Restore initial dimensions
                    self._predesign()  # Preliminary design with new settings
                elif self.mat_change:  # Try changing materials
                    self._change_materials()  # Can be overwritten
                    self._update_element_materials()  # Update materials
                    self._restore_dimensions()  # Restore initial dimensions
                    self._predesign()  # Preliminary design with new settings
            elif self.columns_fail:  # If columns fail to pass design checks
                if self.mat_change:  # Try changing materials
                    self._change_materials()  # Can be overwritten
                    self._update_element_materials()  # Update materials
                    self._restore_dimensions()  # Restore initial dimensions
                    self._predesign()  # Preliminary design with new settings
                elif self.column_change:  # Try changing column section type
                    self._change_column_section()  # Can be overwritten
                    self._restore_materials()  # Restore initial dimensions
                    self._restore_dimensions()  # Restore initial dimensions
                    self._predesign()  # Preliminary design with new settings
            else:  # Tried everything
                break  # No design solution is found, it is time to stop

            # Perform all necessary structural analysis
            self._perform_structural_analyses()
            # Make trial structural design
            self._make_trial_structural_design()
            # Increase the counter
            counter += 1

        # Adjust member design attributes for given quality
        if self.ok:
            self.quality.set_adjusted_properties(self.beams, self.columns)
            # Set average column axial forces to be used.
            self._set_column_predesign_forces()
        else:
            Warning('No design solution is found.')

    def to_csv(self, directory: Union[str, Path]) -> None:
        """Saves the generated BDIM data into the specified directory.

        The files will be saved into the directory upon re-creating it.

        Parameters
        ----------
        directory : str | Path
            Output directory where the bdim outputs (.csv files) will be saved.
            e.g., My/Directory/Path
        """
        if not self.ok:
            return

        # Create the output directory
        directory = Path(directory)
        make_dir(directory)

        # Set the paths for .csv files
        joints_path = directory / 'joints.csv'
        columns_path = directory / 'columns.csv'
        beams_path = directory / 'beams.csv'

        # Retrive the bondslip factor and joint model type
        bondslip_factor = self.quality.model.bondslip_factor
        joint_model = self.quality.model.joint

        # Keys to save for joints
        j_keys = (
            'node_id', 'x-coord [m]', 'y-coord [m]', 'z-coord [m]',
            'bottom_column', 'top_column',
            'left_beam_x', 'right_beam_x', 'left_beam_y', 'right_beam_y',
            'fcm [MPa]', 'model_type_q'
        )
        # Start joints dictionary
        j_dict = {key: [] for key in j_keys}
        # Loop through each joint and append
        for jnt in self.joints:
            j_dict['node_id'].append(jnt.elastic_node.tag)
            j_dict['x-coord [m]'].append(jnt.elastic_node.coordinates[0])
            j_dict['y-coord [m]'].append(jnt.elastic_node.coordinates[1])
            j_dict['z-coord [m]'].append(jnt.elastic_node.coordinates[2])
            if jnt.bottom_column is not None:
                j_dict['bottom_column'].append(jnt.bottom_column.line.tag)
            else:
                j_dict['bottom_column'].append(None)
            if jnt.top_column is not None:
                j_dict['top_column'].append(jnt.top_column.line.tag)
            else:
                j_dict['top_column'].append(None)
            if jnt.left_beam is not None:
                j_dict['left_beam_x'].append(jnt.left_beam.line.tag)
            else:
                j_dict['left_beam_x'].append(None)
            if jnt.right_beam is not None:
                j_dict['right_beam_x'].append(jnt.right_beam.line.tag)
            else:
                j_dict['right_beam_x'].append(None)
            if jnt.rear_beam is not None:
                j_dict['left_beam_y'].append(jnt.rear_beam.line.tag)
            else:
                j_dict['left_beam_y'].append(None)
            if jnt.front_beam is not None:
                j_dict['right_beam_y'].append(jnt.front_beam.line.tag)
            else:
                j_dict['right_beam_y'].append(None)
            j_dict['fcm [MPa]'].append(joint_model)
            j_dict['model_type_q'].append(joint_model)
        # Convert joints dictionary to Pandas DataFrame
        joints = pd.DataFrame(j_dict)
        # Export joints DataFrame as .csv file
        joints.to_csv(joints_path, index=False, float_format='%g')

        # Keys to save for columns
        c_keys = (
            'column_id', 'node_i', 'node_j',
            'bx [mm]', 'by [mm]', 'length [mm]',
            'wg [kN/m]', 'wq [kN/m]', 'fcd [MPa]', 'fsyd [MPa]', 'cover [mm]',
            'dbl_cor [mm]', 'dbl_int [mm]', 'nblx_int', 'nbly_int',
            'dbh [mm]', 'sbh [mm]', 'nbh_x', 'nbh_y',
            'fcm_q [MPa]', 'fsyml_q [MPa]', 'fsymh_q [MPa]', 'sbh_q [mm]',
            'cover_q [mm]', 'bondslip_factor_q'
        )
        # Start columns dictionary
        c_dict = {key: [] for key in c_keys}
        # Loop through each column and append
        for col in self.columns:
            c_dict['column_id'].append(col.line.tag)
            c_dict['node_i'].append(col.elastic_nodes[0].tag)
            c_dict['node_j'].append(col.elastic_nodes[1].tag)
            c_dict['bx [mm]'].append(col.bx / mm)
            c_dict['by [mm]'].append(col.by / mm)
            c_dict['length [mm]'].append(col.H / mm)
            c_dict['wg [kN/m]'].append(col.self_wg)
            c_dict['wq [kN/m]'].append(0.0)
            c_dict['fcd [MPa]'].append(col.fcd / MPa)
            c_dict['fsyd [MPa]'].append(col.fsyd / MPa)
            c_dict['cover [mm]'].append(col.cover / mm)
            c_dict['dbl_cor [mm]'].append(col.dbl_cor / mm)
            c_dict['dbl_int [mm]'].append(col.dbl_int / mm)
            c_dict['nblx_int'].append(col.nblx_int)
            c_dict['nbly_int'].append(col.nbly_int)
            c_dict['dbh [mm]'].append(col.dbh / mm)
            c_dict['sbh [mm]'].append(col.sbh / mm)
            c_dict['nbh_x'].append(col.nbh_x)
            c_dict['nbh_y'].append(col.nbh_y)
            c_dict['fcm_q [MPa]'].append(col.fc_q / MPa)
            c_dict['fsyml_q [MPa]'].append(col.fsyl_q / MPa)
            c_dict['fsymh_q [MPa]'].append(col.fsyh_q / MPa)
            c_dict['sbh_q [mm]'].append(col.sbh_q / mm)
            c_dict['cover_q [mm]'].append(col.cover_q / mm)
            c_dict['bondslip_factor_q'].append(bondslip_factor)
        # Convert columns dictionary to Pandas DataFrame
        columns = pd.DataFrame(c_dict)
        # Export columns DataFrame as .csv file
        columns.to_csv(columns_path, index=False, float_format='%g')

        # Keys to save for beams
        b_keys = (
            'beam_id', 'node_i', 'node_j', 'b [mm]', 'h [mm]', 'length [mm]',
            'wg [kN/m]', 'wq [kN/m]', 'wg_alpha [kN/m]', 'wq_alpha [kN/m]',
            'fcd [MPa]', 'fsyd [MPa]', 'cover [mm]',
            'dbl_t1_i [mm]', 'nbl_t1_i', 'dbl_t2_i [mm]', 'nbl_t2_i',
            'dbl_b1_i [mm]', 'nbl_b1_i', 'dbl_b2_i [mm]', 'nbl_b2_i',
            'dbh_i [mm]', 'sbh_i [mm]', 'nbh_b_i', 'nbh_h_i',
            'dbl_t1_mid [mm]', 'nbl_t1_mid', 'dbl_t2_mid [mm]', 'nbl_t2_mid',
            'dbl_b1_mid [mm]', 'nbl_b1_mid', 'dbl_b2_mid [mm]', 'nbl_b2_mid',
            'dbh_mid [mm]', 'sbh_mid [mm]', 'nbh_b_mid', 'nbh_h_mid',
            'dbl_t1_j [mm]', 'nbl_t1_j', 'dbl_t2_j [mm]', 'nbl_t2_j',
            'dbl_b1_j [mm]', 'nbl_b1_j', 'dbl_b2_j [mm]', 'nbl_b2_j',
            'dbh_j [mm]', 'sbh_j [mm]', 'dbh_mid [mm]', 'sbh_mid [mm]',
            'nbh_b_j', 'nbh_h_j',
            'fcm_q [MPa]', 'fsyml_q [MPa]', 'fsymh_q [MPa]',
            'sbh_i_q [mm]', 'sbh_mid_q [mm]', 'sbh_j_q [mm]', 'cover_q [mm]',
            'bondslip_factor_q'
        )
        # Start beams dictionary
        b_dict = {key: [] for key in b_keys}
        # Loop through each column and append
        for beam in self.beams:
            b_dict['beam_id'].append(beam.line.tag)
            b_dict['node_i'].append(beam.elastic_nodes[0].tag)
            b_dict['node_j'].append(beam.elastic_nodes[1].tag)
            b_dict['b [mm]'].append(beam.b / mm)
            b_dict['h [mm]'].append(beam.h / mm)
            b_dict['length [mm]'].append(beam.L / mm)
            b_dict['wg [kN/m]'].append(beam.wg_total)
            b_dict['wq [kN/m]'].append(beam.wq_total)
            b_dict['wg_alpha [kN/m]'].append(beam.wg_total_alpha)
            b_dict['wq_alpha [kN/m]'].append(beam.wq_total_alpha)
            b_dict['fcd [MPa]'].append(beam.fcd / MPa)
            b_dict['fsyd [MPa]'].append(beam.fsyd / MPa)
            b_dict['cover [mm]'].append(beam.cover / mm)
            b_dict['dbl_t1_i [mm]'].append(beam.dbl_t1[0] / mm)
            b_dict['dbl_t1_mid [mm]'].append(beam.dbl_t1[1] / mm)
            b_dict['dbl_t1_j [mm]'].append(beam.dbl_t1[-1] / mm)
            b_dict['nbl_t1_i'].append(beam.nbl_t1[0])
            b_dict['nbl_t1_mid'].append(beam.nbl_t1[1])
            b_dict['nbl_t1_j'].append(beam.nbl_t1[-1])
            b_dict['dbl_t2_i [mm]'].append(beam.dbl_t2[0] / mm)
            b_dict['dbl_t2_mid [mm]'].append(beam.dbl_t2[1] / mm)
            b_dict['dbl_t2_j [mm]'].append(beam.dbl_t2[-1] / mm)
            b_dict['nbl_t2_i'].append(beam.nbl_t2[0])
            b_dict['nbl_t2_mid'].append(beam.nbl_t2[1])
            b_dict['nbl_t2_j'].append(beam.nbl_t2[-1])
            b_dict['dbl_b1_i [mm]'].append(beam.dbl_b1[0] / mm)
            b_dict['dbl_b1_mid [mm]'].append(beam.dbl_b1[1] / mm)
            b_dict['dbl_b1_j [mm]'].append(beam.dbl_b1[-1] / mm)
            b_dict['nbl_b1_i'].append(beam.nbl_b1[0])
            b_dict['nbl_b1_mid'].append(beam.nbl_b1[1])
            b_dict['nbl_b1_j'].append(beam.nbl_b1[-1])
            b_dict['dbl_b2_i [mm]'].append(beam.dbl_b2[0] / mm)
            b_dict['dbl_b2_mid [mm]'].append(beam.dbl_b2[1] / mm)
            b_dict['dbl_b2_j [mm]'].append(beam.dbl_b2[-1] / mm)
            b_dict['nbl_b2_i'].append(beam.nbl_b2[0])
            b_dict['nbl_b2_mid'].append(beam.nbl_b2[1])
            b_dict['nbl_b2_j'].append(beam.nbl_b2[-1])
            b_dict['dbh_i [mm]'].append(beam.dbh[0] / mm)
            b_dict['sbh_i [mm]'].append(beam.sbh[0] / mm)
            b_dict['nbh_b_i'].append(beam.nbh_b[0])
            b_dict['nbh_h_i'].append(beam.nbh_h[0])
            b_dict['dbh_mid [mm]'].append(beam.dbh[1] / mm)
            b_dict['sbh_mid [mm]'].append(beam.sbh[1] / mm)
            b_dict['nbh_b_mid'].append(beam.nbh_b[1])
            b_dict['nbh_h_mid'].append(beam.nbh_h[1])
            b_dict['dbh_j [mm]'].append(beam.dbh[-1] / mm)
            b_dict['sbh_j [mm]'].append(beam.sbh[-1] / mm)
            b_dict['nbh_b_j'].append(beam.nbh_b[-1])
            b_dict['nbh_h_j'].append(beam.nbh_h[-1])
            b_dict['fcm_q [MPa]'].append(beam.fc_q / MPa)
            b_dict['fsyml_q [MPa]'].append(beam.fsyl_q / MPa)
            b_dict['fsymh_q [MPa]'].append(beam.fsyh_q / MPa)
            b_dict['sbh_i_q [mm]'].append(beam.sbh_q[0] / mm)
            b_dict['sbh_mid_q [mm]'].append(beam.sbh_q[1] / mm)
            b_dict['sbh_j_q [mm]'].append(beam.sbh_q[-1] / mm)
            b_dict['cover_q [mm]'].append(beam.cover_q / mm)
            b_dict['bondslip_factor_q'].append(bondslip_factor)
        # Convert beams dictionary to Pandas DataFrame
        beams = pd.DataFrame(b_dict)
        # Export beams DataFrame as .csv file
        beams.to_csv(beams_path, index=False, float_format='%g')

    def set_seed_for_quality_adjustments(self, seed: int) -> None:
        """
        Set a new random seed for reproducibility.

        This method updates the quality object's seed attribute
        and sets the global NumPy random seed to ensure deterministic
        behavior in random operations.

        Parameters
        ----------
        seed : int
            The new seed value to set.
        """
        self.quality.set_new_seed(seed)
