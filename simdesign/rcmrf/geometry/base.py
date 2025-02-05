"""
Frame geometry generator for moment-resisting-frame structures.

Notes
-----
Whatever you do add the lines and points for stairs upon
finalising the base geometry.
May add new futures to shapes. e.g., divide option for Line class.
May add new futures to the FrameBase class, e.g., remove_line remove_point.
"""

# Imports from installed packages
from abc import ABC, abstractmethod
import numpy as np
import pandas as pd
from pathlib import Path
import pyvista as pv
from pyvista.plotting.plotter import Plotter
from typing import Union, Optional, Literal, Tuple, List, Dict
import warnings
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from mpl_toolkits.mplot3d import Axes3D
# Imports from utils library
from ...utils.misc import PRECISION, round_list
from ...utils.mesh import Point, Line, Rectangle


class GridData:
    """A class representing grid data along a specific axis.

    Attributes
    ----------
    ids : List[Union[int, float]]
        Grid identifiers.
    ordinates : List[float]
        Grid ordinates.

    Methods
    -------
    __init__
        Initialize GridData.
    ord_by_id
        Get the ordinate corresponding to the given grid ID.
    id_by_ord
        Get the grid ID corresponding to the given ordinate.
    """
    ids: List[Union[int, float]]
    """Grid identifiers."""
    ordinates: List[float]
    """Grid ordinates."""

    def __init__(self, ids: List[Union[int, float]],
                 ordinates: List[Union[float]]) -> None:
        """Initialize GridData.

        Parameters
        ----------
        ids : List[int]
            List of grid IDs.
        ordinates : List[float]
            List of grid ordinates.
        """
        self.ids = ids
        self.ordinates = ordinates

    def ord_by_id(self, grid_id: Union[int, float]) -> Union[float]:
        """Get the ordinate corresponding to the given grid ID.

        Parameters
        ----------
        grid_id : Union[int, float]
            The grid ID.

        Returns
        -------
        float
            The corresponding ordinate value.
        """
        idx = self.ids.index(grid_id)
        ordinate = self.ordinates[idx]
        return ordinate

    def id_by_ord(self, ordinate: float) -> Union[int, float]:
        """Get the grid ID corresponding to the given ordinate.

        Parameters
        ----------
        ordinate : float
            The ordinate value.

        Returns
        -------
        Union[int, float]
            The corresponding grid ID.
        """
        idx = self.ordinates.index(ordinate)
        grid_id = self.ids[idx]
        return grid_id


class SystemGridData:
    """A class representing the data for the entire grid system.

    Attributes
    ----------
    x : GridData
        Grid data along -x axis.
    y : GridData
        Grid data along -y axis.
    z : GridData
        Grid data along -z axis.

    Methods
    -------
    __init__
        Initialize the SystemGridData instance based on the provided list of
        points.
    update_data
        Update grid data based on the provided list of points.
    update_points_grid_ids
        Update the grid IDs of points based on the current grid data.
    update_points_coordinates
        Update the coordinates of points based on the current grid data.
    """
    x: GridData
    "Grid data along -x axis."
    y: GridData
    "Grid data along -y axis."
    z: GridData
    "Grid data along -z axis."

    def __init__(self, points: List[Point]) -> None:
        """Initialize the SystemGridData instance based on the provided
        list of points.

        Parameters
        ----------
        points : List[Point]
            The list of points used to initialize the grid data.
        """
        point_coordinates = np.array(
            [point.coordinates for point in points])
        xs = np.unique(point_coordinates[:, 0]).tolist()
        ys = np.unique(point_coordinates[:, 1]).tolist()
        zs = np.unique(point_coordinates[:, 2]).tolist()
        x_ids = [i for i in range(len(xs))]
        y_ids = [i for i in range(len(ys))]
        z_ids = [i for i in range(len(zs))]
        self.x = GridData(x_ids, xs)
        self.y = GridData(y_ids, ys)
        self.z = GridData(z_ids, zs)

    def update_data(self, points: List[Point]) -> None:
        """Update grid data based on the provided list of points.

        Parameters
        ----------
        points : List[Point]
            The list of points used to update grid data.
        """
        self.__init__(points)

    def update_points_grid_ids(self, points: List[Point]) -> None:
        """Update the grid IDs of points based on the current grid data.

        Parameters
        ----------
        points : List[Point]
            The list of points whose grid IDs need to be updated.
        """
        for point in points:
            x, y, z = point.coordinates
            point.grid_ids[0] = self.x.id_by_ord(x)
            point.grid_ids[1] = self.y.id_by_ord(y)
            point.grid_ids[2] = self.z.id_by_ord(z)

    def update_points_coordinates(self, points: List[Point]) -> None:
        """Update the coordinates of points based on the current grid data.

        Parameters
        ----------
        points : List[Point]
            The list of points whose coordinates need to be updated.
        """
        for point in points:
            x, y, z = point.grid_ids
            point.coordinates[0] = self.x.ord_by_id(x)
            point.coordinates[1] = self.y.ord_by_id(y)
            point.coordinates[2] = self.z.ord_by_id(z)


class FrameBase(ABC):
    """Base class for representing a frame structure.

    Attributes
    ----------
    points : List[Point]
        List of points in the frame.
    lines : List[Line]
        List of lines in the frame.
    rectangles : List[Rectangle]
        List of rectangles in the frame.
    stairs_rectangles : List[Rectangle]
        List of rectangles representing stairs in the frame.
    stairs_lines : List[List[Line]]
        List of lines representing stairs in the frame.
    system_grid_data : SystemGridData
        Grid data for the entire frame.
    stairs_width_x : float
        Width of stairs along the x-axis.
    stairs_width_y : float
        Width of stairs along the y-axis.
    stairs_location : List[int]
        Location of stairs defined by grid ids in x and y for lower left
        corner point.
    POINTS_SHEET : str
        Sheet name for points data in Excel.
        Default is "Points".
    LINES_SHEET : str
        Sheet name for lines data in Excel.
        Default is "Lines".
    RECTANGLES_SHEET : str
        Sheet name for rectangles data in Excel.
        Default is "Rectangles".
    STAIRS_SHEET : str
        Sheet name for stairs data in Excel.
        Default is "Stairs Locations".
    ALLOWED_LINE_UNIT_VECTORS : Tuple[list]
        Tuple of allowed unit vectors for lines.
        Default is ([1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]).
    ALLOWED_RECTANGLE_UNIT_NORMAL_VECTOR : list
        Allowed unit normal vector for rectangles.
        Default is [0.0, 0.0, -1.0].

    Methods
    -------
    __init__
        Initialize the FrameBase instance.
    find_point_by_grid_ids
        Find a point in the frame by its grid IDs.
    find_point_by_tag
        Find a point in the frame by its tag.
    find_point_by_coordinates
        Find a point in the frame by its coordinates.
    find_line_by_points
        Find a line in the frame by its defining points.
    find_line_by_tag
        Find a line in the frame by its tag.
    find_lines_by_point
        Find all lines passing through a given point.
    find_rectangle_by_points
        Find a rectangle in the frame by its defining points.
    find_rectangle_by_tag
        Find a rectangle in the frame by its tag.
    find_rectangles_by_line
        Find all rectangles sharing a given line.
    find_rectangles_by_point
        Find all rectangles containing a given point.
    find_rectangles_by_left_lower_point
        Find all rectangles having a given left-lower point.
    find_rectangles_by_line_and_point
        Find all rectangles sharing a given line and containing a given point.
    find_rectangles_by_line_and_tag
        Find all rectangles sharing a given line and having a given tag.
    find_lines_by_rectangle
        Find all lines defining a given rectangle.
    find_lines_by_tag
        Find all lines in the frame with a given tag.
    find_rectangles_by_tag
        Find all rectangles in the frame with a given tag.
    find_lines_by_point_and_tag
        Find all lines passing through a given point and having a given tag.
    find_points_by_level
        Find all points on a specific level.
    find_lines_by_level
        Find all lines on a specific level.
    find_rectangles_by_level
        Find all rectangles on a specific level.
    find_rectangles_by_line_and_point_and_tag
        Find all rectangles sharing a given line, containing a given point,
        and having a given tag.
    write_mesh_to_xlsx
        Write the frame mesh to an Excel file.
    export_mesh_to_html
        Export the frame mesh to an HTML file.
    show_mesh
        Display the frame mesh.
    modify_floor_height
        Modify the height of a floor in the frame.
    modify_bay_width
        Modify the width of a bay in the frame.
    remove_rectangle
        Remove a rectangle from the frame.
    add_new_point
        Add a new point to the frame.
    add_new_line
        Add a new line to the frame.
    add_new_rectangle
        Add a new rectangle to the frame.
    add_new_lines_and_points_for_stairs
        Add new lines and points for stairs in the frame.
    get_points
        Get all points in the frame.
    get_lines
        Get all lines in the frame.
    get_slabs_rectangles
        Get all rectangles representing slabs in the frame.
    get_stairs_rectangles
        Get all rectangles representing stairs in the frame.

    Stairs lines
    ------------
    yz-view: x=i
    z12|__x1__|z22
    z12|      |z21
    yz-view: x=i+1
         __x2__
        |      |
        |      |
        z3     z4
    """
    points: List[Point]
    """List of points in the frame."""
    lines: List[Line]
    """List of lines in the frame."""
    rectangles: List[Rectangle]
    """List of rectangles in the frame."""
    stairs_rectangles: List[Rectangle]
    """List of rectangles representing stairs in the frame."""
    stairs_lines: List[List[Line]]
    """List of lines representing stairs in the frame."""
    system_grid_data: SystemGridData
    """Grid data for the entire frame."""
    stairs_width_x = float
    """Width of stairs along the x-axis."""
    stairs_width_y = float
    """Width of stairs along the y-axis."""
    stairs_location = List[int]
    """Location of stairs defined by grid ids in x and y for lower left
    corner point."""
    POINTS_SHEET: str = "Points"
    """Sheet name for points data in Excel.
    Default is "Points"."""
    LINES_SHEET: str = "Lines"
    """Sheet name for lines data in Excel.
    Default is "Lines"."""
    RECTANGLES_SHEET: str = "Rectangles"
    """Sheet name for rectangles data in Excel.
    Default is "Rectangles"."""
    STAIRS_SHEET: str = "Stairs Locations"
    """Sheet name for stairs data in Excel.
    Default is "Stairs Locations"."""
    ALLOWED_LINE_UNIT_VECTORS: Tuple[List[float]] = (
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0],
        [0.0, 0.0, 1.0])
    """Tuple of allowed unit vectors for lines.
    Default is ([1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0])."""
    ALLOWED_RECTANGLE_UNIT_NORMAL_VECTOR: List[float] = (
        [0.0, 0.0, -1.0])
    """Allowed unit normal vector for rectangles.
    Default is [0.0, 0.0, -1.0]."""

    @property
    def slabs_rectangles(self) -> List[Rectangle]:
        """
        Returns
        -------
        List[Rectangle]
            The list of rectangles representing the slabs in the frame.
        """

        rectangles = [rect for rect in self.rectangles
                      if rect not in self.stairs_rectangles]
        return rectangles

    @property
    def lines_x(self) -> List[Line]:
        """
        Returns
        -------
        List[Line]
            Lines along x-axis.
        """
        return [line
                for line in self.lines
                if np.all(line.unit_vector == np.array([1.0, 0.0, 0.0]))]

    @property
    def lines_y(self) -> List[Line]:
        """
        Returns
        -------
        List[Line]
            Lines along y-axis.
        """
        return [line
                for line in self.lines
                if np.all(line.unit_vector == np.array([0.0, 1.0, 0.0]))]

    @property
    def lines_z(self) -> List[Line]:
        """
        Returns
        -------
        List[Line]
            Lines along z-axis.
        """
        return [line
                for line in self.lines
                if np.all(line.unit_vector == np.array([0.0, 0.0, 1.0]))]

    @property
    def lines_z_facades(self) -> List[Literal[0, 1, 2, 3, 4]]:
        """
        Returns
        -------
        List[Literal[0, 1, 2, 3, 4]]
            Facade IDs of lines along z-axis.

        Notes
        -----
        At the moment, does not work for irregular frames.

        TODO
        ----
        Adapt it for irregular frames.
        """
        facades = []
        xid_min = min(self.system_grid_data.x.ids)
        xid_max = max(self.system_grid_data.x.ids)
        yid_min = min(self.system_grid_data.y.ids)
        yid_max = max(self.system_grid_data.y.ids)
        for line in self.lines_z:
            loc = 0
            pi, _ = line.points
            grid_i = pi.grid_ids.copy()
            if grid_i[0] == xid_min:
                loc = 1
            elif grid_i[0] == xid_max:
                loc = 3
            elif grid_i[1] == yid_min:
                loc = 2
            elif grid_i[1] == yid_max:
                loc = 4
            # Corner lines
            if grid_i[0] == xid_min and grid_i[1] == yid_min:
                loc = 12
            elif grid_i[0] == xid_min and grid_i[1] == yid_max:
                loc = 14
            elif grid_i[0] == xid_max and grid_i[1] == yid_min:
                loc = 32
            elif grid_i[0] == xid_max and grid_i[1] == yid_max:
                loc = 34
            facades.append(loc)

        return facades

    @property
    def continuous_lines_along_x(self) -> Dict[Tuple[Union[float, int]],
                                               List[Line]]:
        """
        Returns
        -------
        Dict[Tuple[Union[float, int]], List[Line]]
            Continuous lines along the x-direction.

        Notes
        -----
        In case there are None's in the lists, it means that there is
        a discontinuity at `None`.
        """

        cont_lines_in_x = {}
        for j in self.system_grid_data.y.ids:
            for k in self.system_grid_data.z.ids:

                points = []
                for i in self.system_grid_data.x.ids:
                    point = self.find_point_by_grid_ids([i, j, k])
                    if point is not None:
                        points.append(point)

                lines = []
                for pt_i in range(len(points)-1):
                    p1 = points[pt_i]
                    p2 = points[pt_i+1]
                    line = self.find_line_by_points([p1, p2])
                    lines.append(line)
                if any(lines):
                    cont_lines_in_x[(j, k)] = lines

        return cont_lines_in_x

    @property
    def continuous_lines_along_y(self) -> Dict[Tuple[Union[float, int]],
                                               List[Line]]:
        """
        Returns
        -------
        Dict[Tuple[Union[float, int]], List[Line]]
            Continuous lines along the y-direction.

        Notes
        -----
        In case there are None's in the lists, it means that there is
        a discontinuity at `None`.
        """
        cont_lines_in_y = {}
        for i in self.system_grid_data.x.ids:
            for k in self.system_grid_data.z.ids:
                points = []
                for j in self.system_grid_data.y.ids:
                    point = self.find_point_by_grid_ids([i, j, k])
                    if point is not None:
                        points.append(point)

                lines = []
                for pt_i in range(len(points)-1):
                    p1 = points[pt_i]
                    p2 = points[pt_i+1]
                    line = self.find_line_by_points([p1, p2])
                    lines.append(line)
                if any(lines):
                    cont_lines_in_y[(i, k)] = lines

        return cont_lines_in_y

    @property
    def continuous_lines_along_z(
        self
    ) -> Dict[Tuple[Union[float, int]], List[Line]]:
        """
        Returns
        -------
        Dict[Tuple[Union[float, int]], List[Line]]
            Continuous lines along the z-direction.

        Notes
        -----
        In case there are None's in the lists, it means that there is
        a discontinuity at `None`.
        """
        cont_lines_in_z = {}
        for i in self.system_grid_data.x.ids:
            for j in self.system_grid_data.y.ids:
                points = []
                for k in self.system_grid_data.z.ids:
                    point = self.find_point_by_grid_ids([i, j, k])
                    if point is not None:
                        points.append(point)

                lines = []
                for pt_i in range(len(points)-1):
                    p1 = points[pt_i]
                    p2 = points[pt_i+1]
                    line = self.find_line_by_points([p1, p2])
                    lines.append(line)
                if any(lines):
                    cont_lines_in_z[(i, j)] = lines

        return cont_lines_in_z

    @property
    def ground_level_points(self) -> List[Point]:
        """
        Returns
        -------
        List[Point]
            Ground level points (first points of continuous lines).
        """
        points = []
        for _, lines in self.continuous_lines_along_z.items():
            for line in lines:
                if line:
                    points.append(line.points[0])
                    break
        return points

    @property
    def points_at_mid_floor_levels(self) -> List[Point]:
        """
        Returns
        -------
        List[Point]
           Points at mid floor levels (points of stairs_lines_x1).
        """
        mid_floor_points = []
        for line in self.stairs_lines_x1:
            mid_floor_points.extend(line.points)
        return mid_floor_points

    @property
    def floor_level_points(self) -> List[List[Point]]:
        """
        Returns
        -------
        List[List[Point]]
            List which contains lists of points at each floor level.
        """
        not_floor_points = self.points_at_mid_floor_levels + \
            self.ground_level_points
        floor_level_points = []
        for z_id in self.system_grid_data.z.ids:
            points = self.find_points_by_level(z_grid_id=z_id)
            if any(points):
                common_points = set(points) & set(not_floor_points)
                points = [item for item in points if item not in common_points]
                if any(points):
                    floor_level_points.append(points)
        return floor_level_points

    @property
    def point_tags(self) -> List[int]:
        """
        Returns
        -------
        List[int]
            Tags of defined points.
        """
        return [point.tag for point in self.points]

    @property
    def line_tags(self) -> List[int]:
        """
        Returns
        -------
        List[int]
            Tags of defined lines.
        """

        return [line.tag for line in self.lines]

    @property
    def rectangle_tags(self) -> List[int]:
        """
        Returns
        -------
        List[int]
            Tags of defined rectangles.
        """
        return [rect.tag for rect in self.rectangles]

    @property
    def roof_rectangles(self) -> List[Rectangle]:
        """
        Returns
        -------
        List[Rectangle]
            Rectangles at the roof level.
        """

        rectangles = []
        for rect in self.rectangles:
            point = rect.points[0]
            grid_ids = point.grid_ids.copy()
            idx = self.system_grid_data.z.ids.index(grid_ids[2])
            idx_max = len(self.system_grid_data.z.ids) - 1
            if idx == idx_max:  # This is already roof level
                rectangles.append(rect)
            else:  # Check if any rectangle exist above
                check = []
                for i in range(idx+1, idx_max+1):
                    grid_ids[2] = self.system_grid_data.z.ids[i]
                    point = self.find_point_by_grid_ids(grid_ids)
                    rect_up = self.find_rectangles_by_left_lower_point(point)
                    check.append(rect_up)
                if any(check) is False:
                    rectangles.append(rect)

        return rectangles

    @property
    def exterior_horizontal_lines(self) -> List[Line]:
        """
        Returns
        -------
        List[Line]
            Exterior horizontal lines.

        Notes
        -----
        Does not consider the lines around interior openings as exterior.
        """
        lines = []
        imin = 0
        imax = len(self.system_grid_data.y.ids) - 1
        for i, yid in enumerate(self.system_grid_data.y.ids):
            for zid in self.system_grid_data.z.ids:
                if zid % 1 == 0:  # this is not staircase line
                    points: List[Point] = []
                    for xid in self.system_grid_data.x.ids:
                        point = self.find_point_by_grid_ids([xid, yid, zid])
                        if point is not None:
                            points.append(point)

                    for pt_i in range(len(points)-1):
                        add = True
                        p1 = points[pt_i]
                        p2 = points[pt_i+1]
                        line = self.find_line_by_points([p1, p2])
                        if line is None:
                            add = False
                        elif i != imin and i != imax:
                            grids = p1.grid_ids.copy()
                            # Check for any next points in y
                            for ii in range(i+1, imax+1):
                                grids[1] = ii
                                p = self.find_point_by_grid_ids(grids)
                                if p:
                                    add = False
                                    break
                            # Check for any previous points in y
                            for ii in range(imin, i):
                                grids[1] = ii
                                p = self.find_point_by_grid_ids(grids)
                                if p:
                                    add = False
                                    break
                        if add:
                            lines.append(line)

        imin = 0
        imax = len(self.system_grid_data.x.ids) - 1
        for i, xid in enumerate(self.system_grid_data.x.ids):
            for zid in self.system_grid_data.z.ids:
                if zid % 1 == 0:  # this is not staircase line
                    points: List[Point] = []
                    for yid in self.system_grid_data.y.ids:
                        point = self.find_point_by_grid_ids([xid, yid, zid])
                        if point is not None:
                            points.append(point)

                    for pt_i in range(len(points)-1):
                        add = True
                        p1 = points[pt_i]
                        p2 = points[pt_i+1]
                        line = self.find_line_by_points([p1, p2])
                        if line is None:
                            add = False
                        elif i != imin and i != imax:
                            grids = p1.grid_ids.copy()
                            # Check for any next points in y
                            for ii in range(i+1, imax+1):
                                grids[0] = ii
                                p = self.find_point_by_grid_ids(grids)
                                if p:
                                    add = False
                                    break
                            # Check for any previous points in y
                            for ii in range(imin, i):
                                grids[0] = ii
                                p = self.find_point_by_grid_ids(grids)
                                if p:
                                    add = False
                                    break
                        if add:
                            lines.append(line)
        return lines

    @property
    def stairs_lines_z11(self) -> List[Line]:
        """
        Returns
        -------
        List[Line]
            List of stairs z11 lines.

        Notes
        -----
        The vertical z1 line is divided into two since an horizontal line along
        x-axis (x1), which represents the supporting beam at the mid-storey
        level, is inserted.
        z11 line is the lower half of the original vertical line.
        It is connected to the start point of mid horizontal line (x1).
        """
        return [lines[0] for lines in self.stairs_lines]

    @property
    def stairs_lines_z12(self) -> List[Line]:
        """
        Returns
        -------
        List[Line]
            List of stairs z12 lines.

        Notes
        -----
        The vertical z1 line is divided into two since an horizontal line along
        x-axis (x1), which represents the supporting beam at the mid-storey
        level, is inserted.
        z12 line is the upper half of the original vertical line.
        It is connected to the start point of mid horizontal line (x1).
        """
        return [lines[1] for lines in self.stairs_lines]

    @property
    def stairs_lines_z21(self) -> List[Line]:
        """
        Returns
        -------
        List[Line]
            List of stairs z21 lines.

        Notes
        -----
        The vertical z2 line is divided into two since an horizontal line along
        x-axis (x1), which represents the supporting beam at the mid-storey
        level, is inserted.
        z21 line is the lower half of the original vertical line.
        It is connected to the end point of mid horizontal line (x1).
        """
        return [lines[2] for lines in self.stairs_lines]

    @property
    def stairs_lines_z22(self) -> List[Line]:
        """
        Returns
        -------
        List[Line]
            List of stairs z22 lines.

        Notes
        -----
        The vertical z2 line is divided into two since an horizontal line along
        x-axis (x1), which represents the supporting beam at the mid-storey
        level, is inserted.
        z22 line is the upper half of the original vertical line.
        It is connected to the end point of mid horizontal line (x1).
        """
        return [lines[3] for lines in self.stairs_lines]

    @property
    def stairs_lines_z3(self) -> List[Line]:
        """
        Returns
        -------
        List[Line]
            List of stairs z3 lines.

        Notes
        -----
        It is connected to the start point of upper horizontal line along
        x-axis (x2), which represents the supporting beam at the floor level,
        is inserted.
        """
        return [lines[4] for lines in self.stairs_lines]

    @property
    def stairs_lines_z4(self) -> List[Line]:
        """
        Returns
        -------
        List[Line]
            List of stairs z4 lines.

        Notes
        -----
        It is connected to the end point of upper horizontal line along
        x-axis (x2), which represents the supporting beam at the floor level,
        is inserted.
        """
        return [lines[5] for lines in self.stairs_lines]

    @property
    def stairs_lines_x1(self) -> List[Line]:
        """
        Returns
        -------
        List[Line]
            Stairs x1 lines.

        Notes
        -----
        x1 line represents the supporting beam at the mid-storey level.
        """
        return [lines[6] for lines in self.stairs_lines]

    @property
    def stairs_lines_x2(self) -> List[Line]:
        """
        Returns
        -------
        List[Line]
            Staircase supporting lines along x-axis (beams) at storey level.

        Notes
        -----
        x2 line represents the supporting beam at the floor level.
        """
        return [lines[7] for lines in self.stairs_lines]

    @abstractmethod
    def _initialise_points(self) -> None:
        """Abstract method to initialise points
        representing structural nodes.
        """
        pass

    @abstractmethod
    def _initialise_lines(self) -> None:
        """Abstract method to initialise lines
        representing columns and beams.
        """
        pass

    @abstractmethod
    def _initialise_rectangles(self) -> None:
        """Abstract method to initialise rectangles
        representing slabs or staircase openings.
        """
        pass

    def _build_base(self) -> None:
        """Build the base frame geometry.
        """
        self.points = []
        self.lines = []
        self.rectangles = []
        self.stairs_lines = []
        self.stairs_rectangles = []

        self._initialise_points()
        self._initialise_lines()
        self._initialise_rectangles()

    def _check_for_any_not_allowed_lines(self) -> None:
        """Check if any lines in the frame are not aligned with allowed planes.

        Raises
        ------
        ValueError
            If any line in the frame is not parallel to the xy, xz, or yz
            planes.
        """
        for line in self.lines:
            vector = line.unit_vector.tolist()
            if vector not in self.ALLOWED_LINE_UNIT_VECTORS:
                raise ValueError(
                    "You have an invalid line. The lines should be in parallel"
                    " with either of xy, xz or yz planes")

    def _check_for_any_not_allowed_rectangles(self) -> None:
        """Check if any rectangles in the frame are not parallel to the xy
        plane.

        Raises
        ------
        ValueError
            If any rectangle in the frame is not parallel to the xy plane.
        """
        all_rectangles = self.rectangles + self.stairs_rectangles
        for rectangle in all_rectangles:
            vector = rectangle.unit_normal_vector.tolist()
            if vector != self.ALLOWED_RECTANGLE_UNIT_NORMAL_VECTOR:
                raise ValueError(
                    "You have an invalid rectangle. The rectangles should be "
                    "in parallel with xy plane.")

    def _plot_mesh(self) -> Plotter:
        """Plot the mesh representation of the frame structure using
        pyvista.

        Returns
        -------
        Plotter
            The plotter object containing the mesh representation.
        """
        # Points (nodes)
        points = np.array([point.coordinates for point in self.points])
        # Lines (beams)
        points_in_lines = [line.points for line in self.lines]
        lines = []
        for point_in_line in points_in_lines:
            indices = []
            for point in point_in_line:
                indices.append(self.points.index(point))
            indices.insert(0, len(indices))
            lines.append(indices)
        lines = np.vstack(lines)
        # Faces (slabs)
        faces_gray = []
        for rectangle in self.slabs_rectangles:
            indices = []
            for point in rectangle.points:
                indices.append(self.points.index(point))
            indices.insert(0, len(indices))
            faces_gray.append(indices)
        faces_gray = np.vstack(faces_gray)
        # Faces (stairs)
        faces_blue = []
        if any(self.stairs_rectangles):
            for rectangle in self.stairs_rectangles:
                indices = []
                for point in rectangle.points:
                    indices.append(self.points.index(point))
                indices.insert(0, len(indices))
                faces_blue.append(indices)
            faces_blue = np.vstack(faces_blue)
        # Create a PyVista plotter
        plotter = Plotter()
        # Add points, lines, and faces to the plotter with different colors
        mesh_faces = pv.PolyData(points, faces=faces_gray)
        mesh_lines = pv.PolyData(points, lines=lines)
        plotter.add_points(mesh_faces.points, color='black', point_size=10)
        # plotter.add_point_labels(mesh_faces.points, points.tolist(),
        #                          point_size=10, font_size=10, pickable=True,
        #                          font_family='times', shape_color='yellow',
        #                          fill_shape=True, italic=False, bold=True,
        #                          point_color='black')
        plotter.add_mesh(mesh_faces, color='gray',
                         show_edges=False, opacity=0.5)
        plotter.add_mesh(mesh_lines, color='red', line_width=3,
                         style='wireframe')
        # Add stairs faces
        if np.any(faces_blue):
            mesh_faces_stairs = pv.PolyData(points, faces=faces_blue)
            plotter.add_mesh(mesh_faces_stairs, color='blue',
                             show_edges=False, opacity=0.5)
        # Show the axes orientation widget in all subplots
        plotter.add_axes_at_origin(labels_off=True, line_width=3)

        return plotter

    def _plot_mesh2(self):
        """Plot the mesh representation of the frame structure using
        matplotlib.

        Returns
        -------
        matplotlib.pyplot.Figure
            The figure object containing the axes with mesh representation.
        mpl_toolkits.mplot3d.Axes3D
            The axes object containing the mesh representation.
        """
        # Points (nodes)
        points = np.array([point.coordinates for point in self.points])

        # Lines (beams)
        points_in_lines = [line.points for line in self.lines]
        lines = []
        for point_in_line in points_in_lines:
            line = []
            for point in point_in_line:
                line.append(self.points.index(point))
            lines.append(line)

        # Faces (slabs)
        faces_gray = []
        for rectangle in self.slabs_rectangles:
            face = []
            for point in rectangle.points:
                face.append(self.points.index(point))
            faces_gray.append(face)

        # Faces (stairs)
        faces_blue = []
        if any(self.stairs_rectangles):
            for rectangle in self.stairs_rectangles:
                face = []
                for point in rectangle.points:
                    face.append(self.points.index(point))
                faces_blue.append(face)

        # Set up 3D plot
        fig = plt.figure(figsize=(10.24, 7.68), dpi=100)
        ax: Axes3D = fig.add_subplot(111, projection='3d')

        # Plot points
        ax.scatter(
            points[:, 0], points[:, 1], points[:, 2], color='black',
            s=10, alpha=1, marker='s')

        # Plot lines
        for line in lines:
            ax.plot(
                points[line, 0], points[line, 1], points[line, 2],
                color='red', linewidth=2
            )

        # Plot gray faces (slabs)
        for face in faces_gray:
            verts = [points[face]]
            poly = Poly3DCollection(
                verts, color='gray', alpha=0.5, edgecolor='none')
            ax.add_collection3d(poly)

        # Plot blue faces (stairs)
        if faces_blue:
            for face in faces_blue:
                verts = [points[face]]
                poly = Poly3DCollection(
                    verts, color='blue', alpha=0.5, edgecolor='none')
                ax.add_collection3d(poly)

        # Customize axes
        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')
        ax.set_zlabel('Z-axis')
        ax.set_box_aspect([1, 1, 1])  # Aspect ratio 1:1:1
        ax.grid(True)

        return fig, ax

    def find_point_by_tag(self, tag: int) -> Optional[Point]:
        """Find a point in the frame by its tag.

        Parameters
        ----------
        tag : int
            The tag of the point to find.

        Returns
        -------
        Optional[Point]
            The point with the specified tag if found, otherwise None.
        """
        for point in self.points:
            if point.tag == tag:
                return point

    def find_point_by_grid_ids(self, grid_ids: List[Union[int, float]]
                               ) -> Optional[Point]:
        """Find a point in the frame by its grid ids.

        Parameters
        ----------
        grid_ids : List[Union[int, float]]
            The grid ids of the point to find.

        Returns
        -------
        Optional[Point]
            The point with the specified grid ids if found, otherwise None.
        """
        for point in self.points:
            if point.grid_ids == grid_ids:
                return point

    def find_points_by_level(self, z_grid_id: Union[int, float]
                             ) -> Optional[List[Point]]:
        """Find points in the frame that belong to a specific level.

        Parameters
        ----------
        z_grid_id : Union[int, float]
            The grid id representing the level along the z-axis.

        Returns
        -------
        Optional[List[Point]]
            A list of points belonging to the specified level if found,
            otherwise None.
        """
        points = []
        for point in self.points:
            if point.grid_ids[2] == z_grid_id:
                points.append(point)
        if any(points):
            return points

    def find_point_by_coordinates(self, coordinates: List[float]
                                  ) -> Optional[Point]:
        """Find a point in the frame based on its coordinates.

        Parameters
        ----------
        coordinates : List[float]
            The coordinates [x, y, z] of the point to search for.

        Returns
        -------
        Optional[Point]
            The point object if found, otherwise None.
        """
        for point in self.points:
            if point.coordinates == coordinates:
                return point

    def find_line_by_points(self, points: List[Point]) -> Optional[Line]:
        """Find a line in the frame based on its defining points.

        Parameters
        ----------
        points : List[Point]
            The list of two points defining the line.

        Returns
        -------
        Optional[Line]
            The line object if found, otherwise None.
        """
        for line in self.lines:
            if set(points).issubset(line.points):
                return line

    def find_line_by_tag(self, tag: int) -> Optional[Line]:
        """Find a line in the frame based on its tag.

        Parameters
        ----------
        tag : int
            The tag of the line to be found.

        Returns
        -------
        Optional[Line]
            The line object if found, otherwise None.
        """
        for line in self.lines:
            if line.tag == tag:
                return line

    def find_lines_by_point(self, point: Point) -> Optional[List[Line]]:
        """Find lines connected to a given point.

        Parameters
        ----------
        point : Point
            The point for which to find connected lines.

        Returns
        -------
        Optional[List[Line]]
            A list of lines connected to the given point, if any are found.
            Returns None if no connected lines are found.
        """
        lines = []
        for line in self.lines:
            if point in line.points:
                lines.append(line)
        if any(lines):
            return lines

    def find_rectangle_by_points(self, points: List[Point]
                                 ) -> Optional[Rectangle]:
        """Find a rectangle defined by a list of points.

        Parameters
        ----------
        points : List[Point]
            The list of points defining the rectangle.

        Returns
        -------
        Optional[Rectangle]
            The rectangle object if found, otherwise None.
        """
        for rectangle in self.rectangles:
            if set(rectangle.points).issubset(set(points)):
                return rectangle

    def find_rectangle_by_tag(self, tag: int) -> Optional[Rectangle]:
        """Find a rectangle in the frame based on its tag.

        Parameters
        ----------
        tag : int
            The tag of the rectangle to be found.

        Returns
        -------
        Optional[Rectangle]
            The rectangle object if found, otherwise None.
        """
        for rectangle in self.rectangles:
            if rectangle.tag == tag:
                return rectangle

    def find_rectangle_by_lines(self, lines: List[Line]
                                ) -> Optional[Rectangle]:
        """Find a rectangle in the frame based on its defining lines.

        Parameters
        ----------
        lines : List[Line]
            The list of lines that define the rectangle.

        Returns
        -------
        Optional[Rectangle]
            The rectangle object if found, otherwise None.
        """
        for rectangle in self.rectangles:
            if set(rectangle.lines).issubset(set(lines)):
                return rectangle

    def find_rectangles_by_line(self, line: Line
                                ) -> Optional[List[Rectangle]]:
        """Find all rectangles in the frame that contain the given line.

        Parameters
        ----------
        line : Line
            The line to search for within rectangles.

        Returns
        -------
        Optional[List[Rectangle]]
            A list of rectangles containing the given line, or
            None if no rectangles are found.
        """
        rectangles = []
        for rectangle in self.rectangles:
            if line in rectangle.lines:
                rectangles.append(rectangle)

        if any(rectangles):
            return rectangles

    def find_rectangles_by_point(self, point: Point
                                 ) -> Optional[List[Rectangle]]:
        """Find all rectangles in the frame that contain the given point.

        Parameters
        ----------
        point : Point
            The point to search for within rectangles.

        Returns
        -------
        Optional[List[Rectangle]]
            A list of rectangles containing the given point, or
            None if no rectangles are found.
        """
        rectangles = []
        for rectangle in self.rectangles:
            if point in rectangle.points:
                rectangles.append(rectangle)
        if any(rectangles):
            return rectangles

    def find_rectangles_by_left_lower_point(self, point: Point
                                            ) -> Optional[Rectangle]:
        """Find the rectangle in the frame with the given left-lower corner
        point.

        Parameters
        ----------
        point : Point
            The left-lower corner point of the rectangle to search for.

        Returns
        -------
        Optional[Rectangle]
            The rectangle object if found, otherwise None.
        """
        for rectangle in self.rectangles:
            if rectangle.points[0] == point:
                return rectangle

    def write_mesh_to_xlsx(self, path: Union[str, Path]) -> None:
        """Write the mesh data to an Excel file.

        The mesh data includes information about points, lines (beams), and
        rectangles (slabs or stairs). The data is written to separate sheets
        in the Excel file.

        Parameters
        ----------
        path : Union[str, Path]
            The file path where the Excel file will be saved.

        Notes
        -----
        This method uses the openpyxl engine for writing to Excel files.
        """
        # Points
        tags = [point.tag for point in self.points]
        coords = np.array([point.coordinates for point in self.points])
        points_df = pd.DataFrame({'tag': tags,
                                  'x-coord': coords[:, 0],
                                  'y-coord': coords[:, 1],
                                  'z-coord': coords[:, 2]})
        # Lines
        tags = [line.tag for line in self.lines]
        point1s = [line.points[0].tag for line in self.lines]
        point2s = [line.points[1].tag for line in self.lines]
        lines_df = pd.DataFrame({'tag': tags,
                                 'point-1': point1s,
                                 'point-2': point2s})
        # Rectangles (Slabs)
        tags = [rect.tag for rect in self.rectangles]
        point1s = [rect.points[0].tag for rect in self.rectangles]
        point2s = [rect.points[1].tag for rect in self.rectangles]
        point3s = [rect.points[2].tag for rect in self.rectangles]
        point4s = [rect.points[3].tag for rect in self.rectangles]
        rectangles_df = pd.DataFrame({'tag': tags,
                                      'point-1': point1s,
                                      'point-2': point2s,
                                      'point-3': point3s,
                                      'point-4': point4s})

        # Save each DataFrame to a separate sheet
        with pd.ExcelWriter(path, engine='openpyxl', mode='w') as writer:
            points_df.to_excel(writer, sheet_name=self.POINTS_SHEET,
                               index=False)
            lines_df.to_excel(writer, sheet_name=self.LINES_SHEET,
                              index=False)
            rectangles_df.to_excel(writer, sheet_name=self.RECTANGLES_SHEET,
                                   index=False)

        if any(self.stairs_rectangles):
            tags = [rect.tag for rect in self.stairs_rectangles]
            stairs_df = pd.DataFrame({'rectangle-tag': tags})
            with pd.ExcelWriter(path, engine='openpyxl', mode='a') as writer:
                stairs_df.to_excel(writer, sheet_name=self.STAIRS_SHEET,
                                   index=False)

    def set_continuous_stairs_rectangles(
        self, location: List[int], width_x: Optional[float] = None,
        width_y: Optional[float] = None
    ) -> None:
        """Sets the rectangles which are located along the staircase (-Z).

        The rectangle location is set based on the grid ids of the left
        corner point. The rectangle dimensions along the staircase case are
        modified based on the user input.

        Parameters
        ----------
        location : List[int]
            Grid ids in x and y for lower left corner point.
        width_x : float
            The width of rectangle containing stairs in x direction.
            If None, width will not be changed, by default None.
        width_y : float
            The width of rectangle containing stairs in y direction.
            If None, width will not be changed, by default None.

        Notes
        -----
        The staircase is assumed to be continuous along all the floors.
        In other words, the geometry should contain rectangles at each
        floor at the same location in xy plane.
        """

        x_grid = location[0]
        y_grid = location[1]
        p1 = self.find_point_by_grid_ids([x_grid, y_grid, 0])
        p2 = self.find_point_by_grid_ids([x_grid+1, y_grid, 0])
        p3 = self.find_point_by_grid_ids([x_grid, y_grid+1, 0])
        p4 = self.find_point_by_grid_ids([x_grid+1, y_grid+1, 0])
        if None in [p1, p2, p3, p4]:
            raise ValueError("Cannot add continuous stairs to this location. "
                             "Base points do not exist.")
        else:
            # Find changes in coordinates if points beyond grid location
            x1 = p1.coordinates[0]
            x2_old = p2.coordinates[0]
            if width_x is None:
                width_x = p2.coordinates[0] - p1.coordinates[0]
            x2_new = x1 + width_x
            change_in_xs = x2_new - x2_old
            y1 = p1.coordinates[1]
            y3_old = p3.coordinates[1]
            if width_y is None:
                width_y = p3.coordinates[1] - p1.coordinates[1]
            y3_new = y1 + width_y
            change_in_ys = y3_new - y3_old
            # Save
            self.stairs_location = location
            self.stairs_width_x = width_x
            self.stairs_width_y = width_y

        # Set the points for stairs_rectangles and adjust point coordinates
        for k in self.system_grid_data.z.ids:
            for j in self.system_grid_data.y.ids:
                for i in self.system_grid_data.x.ids:
                    # Changing coordinates of points for stairs
                    if i > location[0]:
                        point = self.find_point_by_grid_ids([i, j, k])
                        if point:
                            point.coordinates[0] += change_in_xs
                            point.coordinates = round_list(point.coordinates)
                    if j > location[1]:
                        point = self.find_point_by_grid_ids([i, j, k])
                        if point:
                            point.coordinates[1] += change_in_ys
                            point.coordinates = round_list(point.coordinates)

                    # Saving stairs points
                    if k != 0 and i == location[0] and j == location[1]:
                        # find lower left point
                        p1 = self.find_point_by_grid_ids([i, j, k])
                        # find upper left point
                        p2 = self.find_point_by_grid_ids([i, j+1, k])
                        # find upper right point
                        p3 = self.find_point_by_grid_ids([i+1, j+1, k])
                        # find lower right point
                        p4 = self.find_point_by_grid_ids([i+1, j, k])
                        points = [p1, p2, p3, p4]
                        if None in points:
                            raise ValueError(
                                "Cannot add continuous stairs to this location"
                                ". Grid points do not exist.")
                        else:
                            rectangle = self.find_rectangle_by_points(points)
                            # Create the rectangle if it does not exist
                            if rectangle is None:
                                rectangle = self.add_new_rectangle(points)
                                self.rectangles.append(rectangle)

                            if rectangle not in self.stairs_rectangles:
                                self.stairs_rectangles.append(rectangle)
        # Set the system grid data using the new point coordinates
        self.system_grid_data.update_data(self.points)

    def add_new_lines_and_points_for_stairs(self) -> None:
        """Add new lines (beams) and connecting points for supporting stairs.

        This method adds new lines and points to represent stairs in the frame.
        It identifies rectangles that represent stairs and generates additional
        points and lines for each staircase within those rectangles. For each
        staircase, it creates two additional points at mid-storey height,
        divides the vertical lines passing through these points into two, and
        adds a beam between the two nodes supporting the staircase loads.

        Notes
        -----
        - Ensure to add the lines and points for stairs after finalizing the
        base geometry.
        - The grid IDs at the stair line levels should always end with
        '.5'. For example, for stairs between floor one and two the grid id
        will be 1.5.
        - Do not update the grid system after using this method.

        #### TODO list
        - Improve the the behaviour grid id restrictions of stairs.
        """
        for rectangle in self.stairs_rectangles:

            stairs_mid_points = []
            stairs_lines = []

            # Create new nodes at mid storey height for each staircase
            for top_point in rectangle.points[::3]:  # TODO: ask beam loc
                # Getting mid point coordinates and grids
                i, j, k = top_point.grid_ids
                bot_point = self.find_point_by_grid_ids([i, j, k-1])
                coords_top = np.array(top_point.coordinates)
                coords_bot = np.array(bot_point.coordinates)
                coords_mid = (coords_top + coords_bot) / 2
                coords_mid = round_list(coords_mid.tolist())
                # create the mid Point
                grid = [i, j, k-0.5]
                tag = max(self.point_tags) + 1
                mid_point = Point(grid, coords_mid, tag)
                self.points.append(mid_point)
                stairs_mid_points.append(mid_point)
                # Remove old vertical line (column)
                old_line_points = [bot_point, top_point]
                old_line = self.find_line_by_points(old_line_points)
                self.lines.remove(old_line)
                # Create lower and upper vertical Lines (column)
                lower_line_points = [bot_point, mid_point]
                upper_line_points = [mid_point, top_point]
                lower_line = self.add_new_line(lower_line_points)
                upper_line = self.add_new_line(upper_line_points)
                stairs_lines.extend([lower_line, upper_line])

            # Add supporting vertical lines which are not divided
            for top_point in rectangle.points[1:3]:
                i, j, k = top_point.grid_ids
                bot_point = self.find_point_by_grid_ids([i, j, k-1])
                vert_line_points = [bot_point, top_point]
                vert_line = self.find_line_by_points(vert_line_points)
                stairs_lines.append(vert_line)

            # Adding horizontal staircase line along -x at the mid storey
            mid_hor_line = self.add_new_line(stairs_mid_points)
            stairs_lines.append(mid_hor_line)

            # Adding horizontal staircase line along -x at the storey level
            stairs_lines.append(rectangle.lines[1])

            # Append to the self
            self.stairs_lines.append(stairs_lines)

            # update grid system data
            self.system_grid_data.z.ids.append(k-0.5)
            self.system_grid_data.z.ordinates.append(coords_mid[-1])

        # Sort 'ID' list and get the permutation indices
        sorted_indices = sorted(
            range(len(self.system_grid_data.z.ids)),
            key=lambda i: self.system_grid_data.z.ids[i])

        # Apply the same permutation to the 'ID' and 'Ordinate' lists
        self.system_grid_data.z.ids = [
            self.system_grid_data.z.ids[i] for i in sorted_indices]
        self.system_grid_data.z.ordinates = [
            self.system_grid_data.z.ordinates[i] for i in sorted_indices]

    def get_points(self) -> List[Point]:
        """Get all points in the frame.

        Returns
        -------
        List[Point]
            A list containing all points in the frame.
        """
        return self.points

    def get_lines(self) -> List[Line]:
        """
        Get all lines in the frame.

        Returns
        -------
        List[Line]
            A list containing all lines in the frame.
        """
        return self.lines

    def get_slabs_rectangles(self) -> List[Rectangle]:
        """
        Get all slab rectangles in the frame.

        Returns
        -------
        List[Rectangle]
            A list containing all slab rectangles in the frame.
        """
        return self.slabs_rectangles

    def get_stairs_rectangles(self) -> List[Rectangle]:
        """
        Get all stairs rectangles in the frame.

        Returns
        -------
        List[Rectangle]
            A list containing all stairs rectangles in the frame.
        """
        return self.stairs_rectangles

    def export_mesh_to_html(self, path: str) -> None:
        """
        Export the mesh data to an HTML file.

        This method exports the mesh data, including points, lines, and
        rectangles, to an HTML file for visualization.

        Parameters
        ----------
        filename : str
            The name of the HTML file to export the mesh data to.

        Notes
        -----
        - The exported HTML file contains visual representations of the mesh
          data using Three.js for 3D rendering.
        """
        plotter = self._plot_mesh()
        plotter.export_html(path)
        plotter.close()

    def show_mesh(self) -> None:
        """
        Display the mesh data.

        This method displays the mesh data, including points, lines, and
        rectangles, using a graphical user interface (GUI) for visualization.

        Notes
        -----
        - The method opens a window or interface to visualize the mesh data.
        """
        plotter = self._plot_mesh()
        points = np.array([point.coordinates for point in self.points])
        # Stuff to show grids later
        x_ticks = np.unique(points[:, 0])
        y_ticks = np.unique(points[:, 1])
        z_ticks = np.unique(points[:, 2])
        bounds = [min(x_ticks), max(x_ticks), min(y_ticks),
                  max(y_ticks), min(z_ticks), max(z_ticks)]
        # TODO: Can't show exact grid lines at the moment.
        # plotter.show_grid(bounds=bounds, font_family='times',
        #                   n_xlabels=len(x_ticks), n_ylabels=len(y_ticks),
        #                   n_zlabels=len(z_ticks))
        plotter.show_grid(bounds=bounds, font_family='times')

        plotter.show()

    def modify_floor_height(self, floor_id: Union[int, float],
                            new_height: float) -> None:
        """
        Modify the height of a floor level in the frame.

        This method adjusts the height of a specific floor level in the frame
        by updating the z-coordinates of the points associated with that level
        and adjusting the grid accordingly.

        Parameters
        ----------
        floor_id : Union[int, float]
            The identifier of the floor level to be modified. It corresponds
            to the associated grid id of the floor in -z direction.
        new_height : float
            The new height to set for the specified floor level.
        """
        floor_idx = self.system_grid_data.z.ids.index(floor_id)
        old_height = self.system_grid_data.z.ordinates[floor_idx]
        h_difference = new_height - old_height
        for i, z_id in enumerate(self.system_grid_data.z.ids):
            points = self.find_points_by_level(z_id)
            if z_id == floor_id - 0.5:
                for point in points:
                    point.coordinates[2] += h_difference/2
                    point.coordinates[2] = \
                        round(point.coordinates[2], PRECISION)
                self.system_grid_data.z.ordinates[i] += h_difference/2
                self.system_grid_data.z.ordinates[i] = \
                    round(self.system_grid_data.z.ordinates[i], PRECISION)
            elif z_id >= floor_id:
                for point in points:
                    point.coordinates[2] += h_difference
                    point.coordinates[2] = \
                        round(point.coordinates[2], PRECISION)
                self.system_grid_data.z.ordinates[i] += h_difference
                self.system_grid_data.z.ordinates[i] = \
                    round(self.system_grid_data.z.ordinates[i], PRECISION)

    def modify_bay_width(self, bay_id: int, width: float,
                         direction: Literal['x', 'y']) -> None:
        """Modify the width of a bay in the frame.

        This method adjusts the width of a specific bay in the frame by
        updating the x-coordinates or y-coordinates of the points associated
        with that bay and adjusting the grid accordingly.

        Parameters
        ----------
        bay_id : int
            The identifier of the bay to be modified. It corresponds
            to the associated grid id of the floor in -x or -y direction.
        width : float
            The new width to set for the specified bay.
        direction : {'x', 'y'}
            The direction along which to modify the bay width.
            'x' indicates modification along the x-axis,
            'y' indicates modification along the y-axis.

        Notes
        -----
        This method updates the x-coordinates or y-coordinates of the points
        belonging to the specified bay and adjusts the grid system accordingly
        to reflect the changes in bay width along the specified direction.
        """
        attr: GridData = getattr(self.system_grid_data, direction)
        coord1 = attr.ord_by_id(bay_id - 1)
        coord2_old = attr.ord_by_id(bay_id)
        coord2_new = coord1 + width
        change = coord2_new - coord2_old
        for i in range(len(attr.ids)):
            if attr.ids[i] >= bay_id:
                attr.ordinates[i] += change
                attr.ordinates[i] = round(attr.ordinates[i], PRECISION)

        setattr(self.system_grid_data, direction, attr)
        self.system_grid_data.update_points_coordinates(self.points)

    def remove_rectangle(
        self, left_lower_point_grid_ids: List[int], remove_lines: bool = True,
        remove_points: bool = True
    ) -> None:
        """Remove a rectangle from the frame.

        This method removes a rectangle from the frame based on the grid IDs of
        its left-lower point. It also provides options to remove lines and
        points only associated with removed rectangle.

        Parameters
        ----------
        left_lower_point_grid_ids : List[int]
            The grid IDs of the left-lower point of the rectangle to be
            removed.
        remove_lines : bool, optional
            Whether to remove associated lines, by default True.
        remove_points : bool, optional
            Whether to remove associated points, by default True.

        Notes
        -----
        - This method first identifies the rectangle based on the grid IDs of
        its left-lower point. It then removes associated lines and points
        based on the specified parameters.
        - If remove_lines is True, lines that are only associated with the
        removed rectangle are removed
        - Similarly, if remove_points is True, points that are only
        associated with the removed rectangle are removed.
        """
        # Identify the rectangle
        left_lower_point = self.find_point_by_grid_ids(
            left_lower_point_grid_ids)
        rectangle_to_remove = self.find_rectangles_by_left_lower_point(
            left_lower_point)
        # Set the lines and points to remove
        lines_to_remove = []
        points_to_remove = []
        # Lines to remove in horizontal plane (beams)
        for line in rectangle_to_remove.lines:
            rectangles = self.find_rectangles_by_line(line)
            if len(rectangles) == 1:  # Not shared by any other rectangle
                lines_to_remove.append(line)
        # Lines to remove in vertical direction (columns)
        vert_unit_vector = np.array([0.0, 0.0, 1.0])
        for point in rectangle_to_remove.points:
            rectangles = self.find_rectangles_by_point(point)
            lines = self.find_lines_by_point(point)
            if len(rectangles) == 1:
                # Points to remove
                points_to_remove.append(point)
                for line in lines:
                    if np.all(line.unit_vector == vert_unit_vector):
                        lines_to_remove.append(line)
        # Remove rectangle
        self.rectangles.remove(rectangle_to_remove)
        # Remove lines
        if remove_lines:
            for line in lines_to_remove:
                if line in self.lines:
                    self.lines.remove(line)
        if remove_points:
            # Remove points
            for point in points_to_remove:
                if point in self.points:
                    self.points.remove(point)
            # Ensure that there are no free nodes
            for point in self.points:
                lines = self.find_lines_by_point(point)
                if lines is None:
                    self.points.remove(point)

    def add_new_point(self, coordinates: List[float], tag: Optional[int] = None
                      ) -> Point:
        """Add a new point to the frame.

        This method adds a new point to the frame with the specified
        coordinates and optional tag. If a point with the same coordinates
        already exists, a warning is issued.

        Parameters
        ----------
        coordinates : List[float]
            The coordinates [x, y, z] of the new point.
        tag : Optional[int], optional
            The tag to assign to the new point. If None or if the provided tag
            already exists, a new tag is automatically assigned,
            by default None.

        Returns
        -------
        Point
            The newly created or existing point object.

        Notes
        -----
        - If the provided tag is None or if it already exists in the frame, the
        method automatically assigns a new tag by incrementing the maximum tag
        value found in the frame.
        - The method also updates the system grid data based on the newly
        added point and updates the grid IDs of existing points accordingly.
        """
        point = self.find_point_by_coordinates(coordinates)
        if point:
            warnings.warn("The point already exits", UserWarning)
        else:
            # Set the tag
            if tag is None or self.find_point_by_tag(tag):
                tag = max(self.point_tags) + 1
            # Set the grid ids
            x, y, z = coordinates
            # For x
            if x in self.system_grid_data.x.ordinates:
                x_id = self.system_grid_data.x.id_by_ord(x)
            else:
                x_id = max(self.system_grid_data.x.ids) + 1
            # For y
            if y in self.system_grid_data.y.ordinates:
                y_id = self.system_grid_data.y.id_by_ord(y)
            else:
                y_id = max(self.system_grid_data.y.ids) + 1
            # For z
            if z in self.system_grid_data.z.ordinates:
                z_id = self.system_grid_data.z.id_by_ord(z)
            else:
                z_id = max(self.system_grid_data.z.ids) + 1
            # Create the point
            point = Point([x_id, y_id, z_id], coordinates, tag)
            self.points.append(point)
            # Set the system grid data based on the updated list of grids
            self.system_grid_data.update_data(self.points)
            # Update points grid ids
            self.system_grid_data.update_points_grid_ids(self.points)
        # Return the added or found point
        return point

    def add_new_line(self, points: List[Point], tag: Optional[int] = None
                     ) -> Line:
        """Add a new line to the frame.

        This method adds a new line to the frame with the specified points
        and optional tag. If a line with the same points already exists,
        a warning is issued.

        Parameters
        ----------
        points : List[Point]
            The list of points that define the new line.
        tag : Optional[int], optional
            The tag to assign to the new line. If None or if the provided tag
            already exists, a new tag is automatically assigned,
            by default None.

        Returns
        -------
        Line
            The newly created or existing line object.

        Notes
        -----
        - If the provided tag is None or if it already exists in the frame, the
        method automatically assigns a new tag by incrementing the maximum tag
        value found in the frame.
        - The method also ensures that the points defining the line are sorted
        in ascending order of their x and y coordinates for consistency.
        """
        # Set the tag
        if tag is None or self.find_line_by_tag(tag):
            tag = max(self.line_tags) + 1
        # Find the line
        line = self.find_line_by_points(points)
        if line:  # Already exist
            warnings.warn("The line already exits", UserWarning)
        else:  # Create the new line
            line = Line(points, tag)
            line.sort_by_xy()
            self.lines.append(line)
        # Return the new line or the found one
        return line

    def add_new_rectangle(self, points: List[Point], tag: Optional[int] = None
                          ) -> Rectangle:
        """Add a new rectangle to the frame.

        This method adds a new rectangle to the frame with the specified
        corner points and optional tag. If a rectangle with the same points
        already exists, a warning is issued.

        Parameters
        ----------
        points : List[Point]
            The list of four points that define the rectangle.
        tag : Optional[int], optional
            The tag to assign to the new rectangle. If None or if the provided
            tag already exists, a new tag is automatically assigned,
            by default None.

        Returns
        -------
        Rectangle
            The newly created or existing rectangle object.

        Notes
        -----
        - If the provided tag is None or if it already exists in the frame, the
        method automatically assigns a new tag by incrementing the maximum tag
        value found in the frame.
        - The method also ensures that the lines defining the rectangle are
        created if they do not exist, and the rectangle points are sorted in
        ascending order of their x and y coordinates to maintain consistency.
        """
        # Set the tag
        if tag is None or self.find_rectangle_by_tag(tag):
            tag = max(self.rectangle_tags) + 1
        # Find the rectangle
        rectangle = self.find_rectangle_by_points(points)
        if rectangle:  # Already exists in the frame
            warnings.warn("The rectangle already exits", UserWarning)
        else:  # Create the new one
            line1_points = [points[0], points[1]]
            line2_points = [points[1], points[2]]
            line3_points = [points[3], points[2]]
            line4_points = [points[0], points[3]]
            line1 = self.add_new_line(line1_points)
            line2 = self.add_new_line(line2_points)
            line3 = self.add_new_line(line3_points)
            line4 = self.add_new_line(line4_points)
            lines = [line1, line2, line3, line4]
            rectangle = Rectangle(points, lines, tag)
            rectangle.sort_by_xy
            self.rectangles.append(rectangle)
        # Return the new rectangle or the found one
        return rectangle

    def uniformise(
        self, bay_width_x: Optional[float] = None,
        bay_width_y: Optional[float] = None,
        storey_height: Optional[float] = None
    ) -> None:
        """Uniformise the bay width and storey heights of the frame structure.

        This method uniformly scales the frame structure based on the
        provided bay widths and storey height.

        Parameters
        ----------
        bay_width_x : Optional[float], optional
            The width of each bay in the x-direction, by default None.
        bay_width_y : Optional[float], optional
            The width of each bay in the y-direction, by default None.
        storey_height : Optional[float], optional
            The height of each storey, by default None.
        """
        for i in self.system_grid_data.x.ids:
            for j in self.system_grid_data.y.ids:
                for k in self.system_grid_data.z.ids:
                    point = self.find_point_by_grid_ids([i, j, k])
                    if point:
                        x, y, z = point.coordinates
                        if bay_width_x:  # x-coord
                            x = i * bay_width_x
                        if bay_width_y:  # y-coord
                            y = j * bay_width_y
                        if storey_height:  # z-coord
                            z = k * storey_height
                        point.coordinates = round_list([x, y, z])
