# Imports from installed packages
import pandas as pd
from pathlib import Path
from typing import Union

# Imports from geometry library
from .base import FrameBase, Point, Line, Rectangle, SystemGridData


# TODO: Use pydantic to set schema for CustomFrame
class CustomFrame(FrameBase):
    """
    Class representing a custom frame structure.

    This class inherits from FrameBase and extends it to represent a
    custom frame structure. It initializes the frame with data from
    an Excel file specified by the provided path.

    Parameters
    ----------
    xlsx_path : Union[str, Path]
        The path to the Excel file containing the frame data.

    Attributes
    ----------
    xlsx_path : Union[str, Path]
        The path to the Excel file containing the frame data.
    __str: str
       The private attribute for string representation of the StandardFrame.

    Methods
    -------
    __init__
        Initializes the CustomFrame with data from the specified Excel file.
    __str__
        Returns a string representation of the CustomFrame.
    _initialise_points
        Initializes the points of the frame.
    _initialise_lines
        Initializes the lines of the frame.
    _initialise_rectangles
        Initializes the rectangles of the frame.
    """
    __str: str
    """The private attribute for string representation of the CustomFrame."""
    xlsx_path: Union[str, Path]
    """The path to the Excel file containing the frame data."""

    def __init__(self, xlsx_path: Union[str, Path]) -> None:
        """
        Initialize the CustomFrame with data from the specified Excel file.

        Parameters
        ----------
        xlsx_path : Union[str, Path]
            The path to the Excel file containing the frame data.
        """
        tag = Path(xlsx_path).name.removeprefix(".xlsx")
        self.__str = f"CustomFrame-{tag}"
        self.xlsx_path = xlsx_path
        self._build_base()
        self._check_for_any_not_allowed_lines()
        self._check_for_any_not_allowed_rectangles()

    def __str__(self) -> str:
        """
        Return a string representation of the CustomFrame.

        Returns
        -------
        str
            String representation of the CustomFrame.
        """
        return self.__str

    def _initialise_points(self) -> None:
        """
        Initialize the points of the frame.
        """
        # Get the data from excel sheet containing points tags and coordinates
        df = pd.read_excel(self.xlsx_path, sheet_name=self.POINTS_SHEET)
        # Set the grid coordinates
        unique_xs: list = (df['x-coord'].unique()).tolist()
        unique_ys: list = (df['y-coord'].unique()).tolist()
        unique_zs: list = (df['z-coord'].unique()).tolist()
        # Start creating points
        for _, row in df.iterrows():
            coords = [row['x-coord'], row['y-coord'], row['z-coord']]
            i = float(unique_xs.index(coords[0]))
            j = float(unique_ys.index(coords[1]))
            k = float(unique_zs.index(coords[2]))
            tag = int(row['tag'])
            grid = [i, j, k]
            point = Point(grid, coords, tag)
            self.points.append(point)
        # Set the system grid data
        self.system_grid_data = SystemGridData(self.points)

    def _initialise_lines(self) -> None:
        """
        Initialize the lines of the frame.
        """
        # Get the data from excel sheet containing lines connectivity
        df = pd.read_excel(self.xlsx_path, sheet_name=self.LINES_SHEET)
        # Start creating lines
        for _, row in df.iterrows():
            tag = int(row['tag'])
            point1 = self.find_point_by_tag(row['point-1'])
            point2 = self.find_point_by_tag(row['point-2'])
            line = Line([point1, point2], tag)
            line.sort_by_xy()
            self.lines.append(line)

    def _initialise_rectangles(self) -> None:
        """
        Initialize the rectangles of the frame.
        """
        # Dataframe containing rectangles of floor slabs
        df = pd.read_excel(self.xlsx_path, sheet_name=self.RECTANGLES_SHEET)
        # Go through rectangle shapes
        for _, row in df.iterrows():
            # Find points on the rectangle
            tag = int(row['tag'])
            point1 = self.find_point_by_tag(row['point-1'])
            point2 = self.find_point_by_tag(row['point-2'])
            point3 = self.find_point_by_tag(row['point-3'])
            point4 = self.find_point_by_tag(row['point-4'])
            points = [point1, point2, point3, point4]
            # Find lines on the rectangle
            line1 = self.find_line_by_points([point1, point2])
            line2 = self.find_line_by_points([point2, point3])
            line3 = self.find_line_by_points([point4, point3])
            line4 = self.find_line_by_points([point1, point4])
            lines = [line1, line2, line3, line4]
            rectangle = Rectangle(points, lines, tag)
            rectangle.sort_by_xy()
            self.rectangles.append(rectangle)

        if self.STAIRS_SHEET in pd.ExcelFile(self.xlsx_path).sheet_names:
            df = pd.read_excel(self.xlsx_path, sheet_name=self.STAIRS_SHEET)
            for _, row in df.iterrows():
                # Find stairs locations (rectangles)
                tag = row['rectangle-tag']
                rectangle = self.find_rectangle_by_tag(tag)
                self.stairs_rectangles.append(rectangle)
