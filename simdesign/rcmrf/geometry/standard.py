# Imports from geometry library
from .base import FrameBase, Line, Rectangle, Point, SystemGridData

# Imports from utils library
from ...utils.misc import round_list


class StandardFrame(FrameBase):
    """
    Class representing a standard frame structure.

    This class inherits from FrameBase and extends it to represent a
    standard frame structure. It initializes the frame with the given
    parameters and constructs the base geometry of the frame. It is
    called StandardFrame because its base geometry is built as a
    uniform and regular frame (equal bay widths and storey heights).

    Parameters
    ----------
    num_storeys : int
        The number of storeys in the frame.
    storey_height : float
        The height of each storey.
    num_bays_x : int
        The number of bays along the x-direction.
    bay_width_x : float
        The width of each bay along the x-direction.
    num_bays_y : int
        The number of bays along the y-direction.
    bay_width_y : float
        The width of each bay along the y-direction.

    Attributes
    ----------
    _num_storeys : int
        The number of storeys in the frame.
    _num_bays_x : int
        The number of bays along the x-direction.
    _num_bays_y : int
        The number of bays along the y-direction.
    _storey_height : float
        The height of each storey.
    _bay_width_x : float
        The width of each bay along the x-direction.
    _bay_width_y : float
        The width of each bay along the y-direction.

    Methods
    -------
    __init__
        Initializes the StandardFrame with the given parameters.
    __str__
        Returns a string representation of the StandardFrame.
    _initialise_points
        Initializes the points of the frame.
    _initialise_lines
        Initializes the lines of the frame.
    _initialise_rectangles
        Initializes the rectangles of the frame.
    """
    _num_storeys: int
    """The number of storeys in the frame."""
    _num_bays_x: int
    """The number of bays along the x-direction."""
    _num_bays_y: int
    """The number of bays along the y-direction."""
    _storey_height: float
    """The height of each storey."""
    _bay_width_x: float
    """The width of each bay along the x-direction."""
    _bay_width_y: float
    """The width of each bay along the y-direction."""
    __str: str = "StandardFrame"
    """The private attribute for string representation of the StandardFrame."""

    def __init__(
        self, num_storeys: int, storey_height: float, num_bays_x: int,
        bay_width_x: float, num_bays_y: int, bay_width_y: float,
        tag: str | None = None
    ) -> None:
        """
        Initialize the StandardFrame with the given parameters.

        Parameters
        ----------
        num_storeys : int
            The number of storeys in the frame.
        storey_height : float
            The height of each storey.
        num_bays_x : int
            The number of bays along the x-direction.
        bay_width_x : float
            The width of each bay along the x-direction.
        num_bays_y : int
            The number of bays along the y-direction.
        bay_width_y : float
            The width of each bay along the y-direction.
        tag : str | None
            Tag of the StandardFrame instance. If not None,
            string added to the string representation of instance:
            `self.__str = f"StandardFrame-{tag}"`
        """
        if tag:
            self.__str = f"StandardFrame-{tag}"

        self._num_storeys = num_storeys
        self._storey_height = storey_height
        self._num_bays_x = num_bays_x
        self._bay_width_x = bay_width_x
        self._num_bays_y = num_bays_y
        self._bay_width_y = bay_width_y
        self._build_base()
        self._check_for_any_not_allowed_lines()
        self._check_for_any_not_allowed_rectangles()

    def __str__(self) -> str:
        """
        Return a string representation of the StandardFrame.

        Returns
        -------
        str
            String representation of the StandardFrame.
        """
        return self.__str

    def _initialise_points(self) -> None:
        """
        Initialize the points of the frame.
        """
        for k in range(self._num_storeys + 1):  # Along -z
            tag = k*1000 + 1  # add 1000 for each floor
            for j in range(self._num_bays_y + 1):  # Along -y
                for i in range(self._num_bays_x + 1):  # Along -x
                    x = i * self._bay_width_x  # x-coord
                    y = j * self._bay_width_y  # y-coord
                    z = k * self._storey_height  # z-coord
                    grid = [i, j, k]  # Grid IDs in x, y, z
                    coords = round_list([x, y, z])  # # Coordinates in x, y, z
                    new_point = Point(grid, coords, tag)  # create the Point
                    self.points.append(new_point)  # append to points
                    tag += 1  # Add new tag

        # Set the system grid data
        self.system_grid_data = SystemGridData(self.points)

    def _initialise_lines(self) -> None:
        """
        Initialize the lines of the frame.
        """
        # Lines along -Z
        counter_ = 1
        for k in range(self._num_storeys):  # Along -z
            counter = counter_  # Counter for line tags
            for j in range(self._num_bays_y + 1):  # Along -y
                for i in range(self._num_bays_x + 1):  # Along -x
                    point1_grid = [i, j, k]
                    point2_grid = [i, j, k+1]
                    point1 = self.find_point_by_grid_ids(point1_grid)
                    point2 = self.find_point_by_grid_ids(point2_grid)
                    points = [point1, point2]
                    tag = k*1000 + counter
                    counter += 1
                    new_line = Line(points, tag)
                    self.lines.append(new_line)
        # Lines along -X
        counter_ = counter
        for k in range(1, self._num_storeys + 1):  # Along -z
            counter = counter_
            for j in range(self._num_bays_y + 1):  # Along -y
                for i in range(self._num_bays_x):  # Along -x
                    point1_grid = [i, j, k]
                    point2_grid = [i+1, j, k]
                    point1 = self.find_point_by_grid_ids(point1_grid)
                    point2 = self.find_point_by_grid_ids(point2_grid)
                    points = [point1, point2]
                    tag = k*1000 + counter
                    counter += 1
                    new_line = Line(points, tag)
                    self.lines.append(new_line)
        # Lines along -Y
        counter_ = counter
        for k in range(1, self._num_storeys + 1):  # Along -z
            counter = counter_
            for j in range(self._num_bays_y):  # Along -y
                for i in range(self._num_bays_x + 1):  # Along -x
                    point1_grid = [i, j, k]
                    point2_grid = [i, j+1, k]
                    point1 = self.find_point_by_grid_ids(point1_grid)
                    point2 = self.find_point_by_grid_ids(point2_grid)
                    points = [point1, point2]
                    tag = k*1000 + counter
                    counter += 1
                    new_line = Line(points, tag)
                    self.lines.append(new_line)

    def _initialise_rectangles(self) -> None:
        """
        Initialize the rectangles of the frame.
        """
        # Counter for line tags
        for k in range(1, self._num_storeys + 1):  # Along -z
            counter = 1
            for j in range(self._num_bays_y):  # Along -y
                for i in range(self._num_bays_x):  # Along -x
                    # Find points on the rectangle
                    lower_left_grid = [i, j, k]
                    upper_right_grid = [i+1, j+1, k]
                    lower_right_grid = [i+1, j, k]
                    upper_left_grid = [i, j+1, k]
                    point1 = self.find_point_by_grid_ids(lower_left_grid)
                    point2 = self.find_point_by_grid_ids(upper_left_grid)
                    point3 = self.find_point_by_grid_ids(upper_right_grid)
                    point4 = self.find_point_by_grid_ids(lower_right_grid)
                    points = [point1, point2, point3, point4]
                    # Find lines on the rectangle
                    line1_points = [point1, point2]
                    line2_points = [point2, point3]
                    line3_points = [point4, point3]
                    line4_points = [point1, point4]
                    line1 = self.find_line_by_points(line1_points)
                    line2 = self.find_line_by_points(line2_points)
                    line3 = self.find_line_by_points(line3_points)
                    line4 = self.find_line_by_points(line4_points)
                    lines = [line1, line2, line3, line4]
                    # Create a Rectangle object and append
                    tag = k*1000 + counter
                    counter += 1
                    rectangle = Rectangle(points, lines, tag)
                    rectangle.sort_by_xy()
                    self.rectangles.append(rectangle)
