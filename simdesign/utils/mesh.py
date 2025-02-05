"""
Objects used to define structural meshes with varying geometries.
"""

# Imports from installed packages
import numpy as np
from typing import Union, Optional, List
from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract base class for geometric shapes.

    Attributes
    ----------
    tag : Optional[int]
        Unique identifier for the shape.

    Methods
    -------
    __init__
        Initialize a Shape object.
    ndim
        Abstract property to get the number of dimensions of the shape.
    """

    tag: Optional[int]
    """Unique identifier for the shape."""

    def __init__(self, tag: int | None) -> None:
        """Initialize a Shape object.

        Parameters
        ----------
        tag : int | None
            Unique identifier for the shape.
        """
        self.tag = tag

    @property
    @abstractmethod
    def ndim(self) -> int:
        """Abstract property to get the number of dimensions of the shape.

        Returns
        -------
        int
            Number of dimensions.
        """
        pass


class Point(Shape):
    """Point object.

    Attributes
    ----------
    grid_ids : List[Union[int, float]]
        Point grid identifiers (x, y, z).
    coordinates : List[float]
        Point coordinates (x, y, z).

    Methods
    -------
    __init__
        Initialize a Point object.
    __str__
        String representation of the Point object.
    ndim
        Number of dimensions of the point.

    Notes
    -----
    Inherits from Shape class.
    """
    grid_ids: List[Union[int, float]]
    """Point grid identifiers (x, y, z)."""
    coordinates: List[float]
    """Point coordinates (x, y, z)."""

    def __init__(self, grid: List[Union[int, float]], coordinates: List[float],
                 tag: int) -> None:
        """Initialize a Point object.

        Parameters
        ----------
        grid : List[Union[int, float]]
            Grid IDs in x, y, z.
        coordinates : List[float]
            Coordinates in x, y, z.
        tag : int
            Unique identifier for the point.
        """
        super().__init__(tag)
        self.grid_ids = grid  # Grid IDs in x, y, z
        self.coordinates = coordinates  # Coordinates in x, y, z

    def __str__(self) -> str:
        """Return a string representation of the Point object.

        Returns
        -------
        str
            String representation.
        """
        return f"Point{self.tag}{tuple(self.coordinates)}"

    @property
    def ndim(self) -> int:
        """
        Returns
        -------
        int
            Number of dimensions (always 0 for a point).
        """
        return 0


class Line(Shape):
    """Line object.

    Attributes
    ----------
    points : List[Point]
        List of points defining the line.

    Methods
    -------
    __init__
        Initialize a Line object.
    __str__
        String representation of the Line object.
    direction_vector
        Get the direction vector of the line.
    unit_vector
        Unit vector of the line.
    ndim
        Number of dimensions of the line.
    length
        Line length.
    sort_by_xy
        Sort points to form a line in the xy plane.
    _is_line
        Check if the shape is a line.

    Notes
    -----
    Inherits from Shape class.
    """
    points: List[Point]
    """List of points defining the line."""

    def __init__(self, points: List[Point], tag: Optional[int] = None) -> None:
        """Initialize a Line object.

        Parameters
        ----------
        points : List[Point]
            List of points defining the line.
        tag : int, optional
            Unique identifier for the line. By default None.
        """
        super().__init__(tag)

        # Check for None points
        if None in points:
            raise ValueError("The object contains undefined points.")
        else:
            self.points = points

    def __str__(self) -> str:
        """Return a string representation of the Line object.

        Returns
        -------
        str
            String representation.
        """
        points = ", ".join([str(point) for point in self.points])
        return (f"Line[{points}]")

    @property
    def direction_vector(self) -> np.ndarray:
        """
        Returns
        -------
        np.ndarray
            Direction vector of the line.
        """
        start_point = np.array(self.points[0].coordinates)
        end_point = np.array(self.points[1].coordinates)
        return end_point - start_point

    @property
    def unit_vector(self) -> np.ndarray:
        """
        Returns
        -------
        np.ndarray
            Unit vector of the line.
        """
        magnitude = np.linalg.norm(self.direction_vector)
        if magnitude != 0:
            return self.direction_vector / magnitude
        else:
            return self.direction_vector

    @property
    def ndim(self) -> int:
        """
        Returns
        -------
        int
            Number of dimensions (always 1 for a line).
        """
        return 1

    @property
    def length(self) -> np.float64:
        """
        Returns
        -------
        np.float64
            Line length.
        """
        start_point = np.array(self.points[0].coordinates)
        end_point = np.array(self.points[1].coordinates)
        return np.sum((end_point - start_point)**2)**0.5

    def _is_line(self) -> None:
        """Check if the shape is a line.

        Raises
        ------
        ValueError
            If the shape is not a line.
        """
        if len(self.points) != 2:
            ValueError("The points in shape is not 2."
                       "It cannot be a line.")

    def sort_by_xy(self) -> None:
        """Sort points such that they form a line with two points [p1, p2]
        such that:

        y
        |__x
                     l(p1, p2)
        p1(x1,y1,zi) o-------->o p2(x2,y2,zi)
        """
        point1 = self.points[0]
        point2 = self.points[1]
        x1, y1, _ = point1.coordinates
        x2, y2, _ = point2.coordinates
        # Order the points
        if x1 < x2 or (x1 == x2 and y1 <= y2):
            self.points = [point1, point2]
        else:
            self.points = [point2, point1]


class Polygon(Shape):
    """Polygon object.

    Attributes
    ----------
    points : List[Point]
        List of points defining the polygon.
    lines : List[Line]
        List of lines composing the polygon.

    Methods
    -------
    __init__
        Initialize a Polygon object.
    ndim
        Number of dimensions of the polygon.
    vertices
        Vertices of the polygon.
    centroid
        Coordinates of the centroid of the polygon.
    normal_vector
        Normal vector of the polygon.
    unit_normal_vector
        Unit normal vector of the polygon.
    perimeter
        Polygon perimeter.
    area
        Polygon area.
    _is_polygon
        Check if the shape is a polygon.
    _is_coplanar
        Check if the polygon's points are coplanar.

    Notes
    -----
    Inherits from Shape class.
    """
    points: List[Point]
    """List of points defining the polygon."""
    lines: List[Line]
    """List of lines composing the polygon."""

    def __init__(self, points: List[Point], lines: List[Line],
                 tag: Optional[int] = None) -> None:
        """Initialize a Polygon object.

        Parameters
        ----------
        points : List[Point]
            List of points defining the polygon.
        lines : List[Line]
            List of lines composing the polygon.
        tag : int, optional
            Unique identifier for the polygon. By default None.
        """
        super().__init__(tag)

        # Check for None points
        if None in points:
            raise ValueError("The object contains undefined points.")
        elif None in lines:
            raise ValueError("The object contains undefined lines.")
        else:
            self.points = points
            self.lines = lines
            self._is_polygon()
            self._is_coplanar()

    @property
    def ndim(self) -> int:
        """
        Returns
        -------
        int
            Number of dimensions (always 2 for a polygon).
        """
        return 2

    @property
    def vertices(self) -> np.ndarray:
        """
        Returns
        -------
        np.ndarray
            Vertices of the polygon.
        """
        return np.array([point.coordinates for point in self.points])

    @property
    def centroid(self) -> np.ndarray:
        """
        Returns
        -------
        np.ndarray
            Coordinates of the centroid of the polygon.
        """
        return np.mean(
            np.array([point.coordinates for point in self.points]),
            axis=0)

    @property
    def normal_vector(self) -> np.ndarray:
        """
        Returns
        -------
        np.ndarray
            Normal vector of the polygon.
        """
        # Convert the coordinates of the three points on polygon to arrays
        point1 = np.array(self.points[0].coordinates)
        point2 = np.array(self.points[1].coordinates)
        point3 = np.array(self.points[2].coordinates)
        # Compute vectors lying in the polygon's plane.
        vector1 = point2 - point1
        vector2 = point3 - point1
        # Calculate the cross product to get the vector normal to the
        # polygon's plane.
        return np.cross(vector1, vector2)

    @property
    def unit_normal_vector(self) -> np.ndarray:
        """
        Returns
        -------
        np.ndarray
            Unit normal vector of the polygon.
        """
        # Normalize the vector to get a unit vector.
        return self.normal_vector / np.linalg.norm(self.normal_vector)

    @property
    def perimeter(self) -> float:
        """
        Returns
        -------
        float
            Polygon perimeter.
        """
        return sum([line.length for line in self.lines])

    @property
    def area(self) -> float:
        """
        Returns
        -------
        float
            Polygon area.
        """
        total_area = 0.0
        # Select a fixed vertex
        fixed_vertex = np.array(self.points[0].coordinates)
        for i in range(1, len(self.points) - 1):
            # Get the coordinates of consecutive vertices
            vertex1 = np.array(self.points[i].coordinates)
            vertex2 = np.array(self.points[i + 1].coordinates)
            # Calculate the cross product of the vectors formed by the vertices
            cross_product = np.cross(vertex1 - fixed_vertex,
                                     vertex2 - fixed_vertex)
            # Calculate the area of the triangle formed by the vertices
            triangle_area = 0.5 * np.linalg.norm(cross_product)
            # Add the area of the triangle to the total area
            total_area += triangle_area
        return total_area

    def _is_polygon(self) -> None:
        """Check if the shape is a polygon.

        Raises
        ------
        ValueError
            If the shape is not a polygon.
        """
        # Check if polygon has enough points
        if len(self.vertices) < 3:
            # Coplanarity is not defined for fewer than three points
            raise ValueError("The shape contains points less than 3."
                             "It cannot be a polygon")

    def _is_coplanar(self) -> None:
        """Check if the polygon's points are coplanar.

        Raises
        ------
        ValueError
            If the points are not coplanar.
        """
        # Check if all points are coplanar
        for vertex in self.vertices[3:]:
            vector = vertex - self.vertices[0]
            if not np.isclose(np.dot(self.normal_vector, vector), 0):
                raise ValueError(
                    "The given points does not satisfy coplanarity."
                    "The shape cannot be a polygon."
                    "Check if points are correctly defined. Adjacent lines"
                    "between consecutive points should not be in the same"
                    "direction.")


class Quadrilateral(Polygon):
    """Quadrilateral object.

    Methods
    -------
    __init__
        Initialize a Quadrilateral object.
    __str__
        String representation of the Quadrilateral object.
    _is_quadrilateral
        Check if the shape is a quadrilateral.
    sort_by_xy
        Sort points to form a quadrilateral in the xy plane.

    Notes
    -----
    Inherits from Polygon class.
    """

    def __init__(self, points: List[Point], lines: List[Line],
                 tag: Optional[int] = None) -> None:
        """Initialize a Quadrilateral object.

        Parameters
        ----------
        points : List[Point]
            List of points defining the quadrilateral.
        lines : List[Line]
            List of lines composing the quadrilateral.
        tag : int, optional
            Unique identifier for the quadrilateral. By default None.
        """
        super().__init__(points, lines, tag)
        # Check if the points satisfy quadrilateral conditions
        self._is_quadrilateral()

    def __str__(self) -> str:
        """String representation of the Quadrilateral object.

        Returns
        -------
        str
            String representation.
        """
        points = ", ".join([str(point) for point in self.points])
        return (f"Quad[{points}]")

    def _is_quadrilateral(self) -> None:
        """Check if the shape is a quadrilateral.

        Raises
        ------
        ValueError
            If the shape is not a quadrilateral.
        """
        # Check the number of vertices
        if len(self.vertices) != 4:
            raise ValueError(
                "The number of points in Polygon is not 4."
                "It cannot be quadrilateral.")

    def sort_by_xy(self) -> None:
        """Sort points such that they form a quadrilateral with four points
        [p1, p2, p3, p4] in the xy plane such that:

        y
        |__x
                         l2(p2,p3)
            p2(x2,y2,z2) o------>o p3(x3,y3,z3)
                         ^       ^
               l1(p1,p2) |       | l3(p4,p3)
                         |       |
            p1(x1,y1,z1) o------>o p4(x4,y4,z4)
                         l4(p1,p4)
        """

        self.points = sorted(
            self.points, key=lambda point: np.arctan2(
                point.coordinates[0] - self.centroid[0],
                point.coordinates[1] - self.centroid[1])
            )

        line_points = [
            [self.points[0], self.points[1]],
            [self.points[1], self.points[2]],
            [self.points[3], self.points[2]],
            [self.points[0], self.points[3]]
        ]

        self.lines = sorted(self.lines, key=lambda line: line_points.index(
            line.points))


class Parallelogram(Quadrilateral):
    """Parallelogram object.

    Methods
    -------
    __init__
        Initialize a Parallelogram object.
    _is_parallelogram
        Check if the shape is a parallelogram.

    Notes
    -----
    Inherits from Quadrilateral class.
    """

    def __init__(self, points: List[Point], lines: List[Line],
                 tag: Optional[int] = None) -> None:
        """Initialize a Parallelogram object.

        Parameters
        ----------
        points : List[Point]
            List of points defining the parallelogram.
        lines : List[Line]
            List of lines composing the parallelogram.
        tag : int, optional
            Unique identifier for the parallelogram. By default None.
        """
        super().__init__(points, lines, tag)
        self._is_parallelogram()

    def _is_parallelogram(self) -> None:
        """Check if the shape is a parallelogram.

        Raises
        ------
        ValueError
            If the shape is not a parallelogram.
        """
        # Check if opposite sides are parallel
        v1 = self.vertices[1] - self.vertices[0]
        v2 = self.vertices[2] - self.vertices[3]
        v3 = self.vertices[2] - self.vertices[1]
        v4 = self.vertices[3] - self.vertices[0]
        bool1 = np.allclose(np.cross(v1, v2), 0)
        bool2 = np.allclose(np.cross(v3, v4), 0)

        if not (bool1 and bool2):
            raise ValueError(
                "Quadrilateral does not have parallel opposite sides."
                "It cannot be a parallelogram.")


class Rectangle(Parallelogram):
    """Rectangle object.

    Methods
    -------
    __init__
        Initialize a Rectangle object.
    _is_rectangle
        Check if the shape is a rectangle.

    Notes
    -----
    Inherits from Parallelogram class.
    """

    def __init__(self, points: List[Point], lines: List[Line],
                 tag: Optional[int] = None) -> None:
        """Initialize a Rectangle object.

        Parameters
        ----------
        points : List[Point]
            List of points defining the rectangle.
        lines : List[Line]
            List of lines composing the rectangle.
        tag : int, optional
            Unique identifier for the rectangle. By default None.
        """
        super().__init__(points, lines, tag)
        self._is_rectangle()

    def _is_rectangle(self) -> None:
        """Check if the shape is a rectangle.

        Raises
        ------
        ValueError
            If the shape is not a rectangle.
        """
        # Check if opposite sides are equal
        side_lengths = []
        for i in range(4):
            side_lengths.append(
                np.linalg.norm(self.vertices[i] - self.vertices[i - 1]))
        bool1 = np.allclose(side_lengths[0], side_lengths[2])
        bool2 = np.allclose(side_lengths[1], side_lengths[3])
        if not (bool1 and bool2):
            raise ValueError(
                "Parallelogram does not have equal opposite sides."
                "It cannot be a Rectangle.")


class Square(Rectangle):
    """Square object.

    Methods
    -------
    __init__
        Initialize a Square object.
    _is_square
        Check if the shape is a square.

    Notes
    -----
    Inherits from Rectangle class.
    """

    def __init__(self, points: List[Point], lines: List[Line],
                 tag: Optional[int] = None) -> None:
        """Initialize a Square object.

        Parameters
        ----------
        points : List[Point]
            List of points defining the square.
        lines : List[Line]
            List of lines composing the square.
        tag : int, optional
            Unique identifier for the square. By default None.
        """
        super().__init__(points, lines, tag)
        self._is_square()

    def _is_square(self) -> None:
        """Check if the shape is a square.

        Raises
        ------
        ValueError
            If the shape is not a square.
        """
        # Check if all sides are equal
        side_lengths = []
        for i in range(4):
            side_lengths.append(
                np.linalg.norm(self.vertices[i] - self.vertices[i - 1]))
        bool1 = np.allclose(side_lengths[0], side_lengths[1])
        bool2 = np.allclose(side_lengths[1], side_lengths[2])
        if not (bool1 and bool2):
            raise ValueError(
                "Rectangle does not have equal adjacent sides."
                "It cannot be a Square.")


class Trapezoid(Quadrilateral):
    """Trapezoid object.

    Methods
    -------
    __init__
        Initialize a Trapezoid object.
    _is_trapezoid
        Check if the shape is a trapezoid.

    Notes
    -----
    Inherits from Quadrilateral class.
    """

    def __init__(self, points: List[Point], lines: List[Line],
                 tag: Optional[int] = None) -> None:
        """
        Initialize a Trapezoid object.

        Parameters
        ----------
        points : List[Point]
            List of points defining the trapezoid.
        lines : List[Line]
            List of lines composing the trapezoid.
        tag : int, optional
            Unique identifier for the trapezoid. By default None.
        """
        super().__init__(points, lines, tag)
        self._is_trapezoid()

    def _is_trapezoid(self) -> None:
        """
        Check if the shape is a trapezoid.

        Raises
        ------
        ValueError
            If the shape is not a trapezoid.
        """
        # Check if at least one pair of opposite sides is parallel
        v1 = self.vertices[1] - self.vertices[0]
        v2 = self.vertices[2] - self.vertices[3]
        v3 = self.vertices[2] - self.vertices[1]
        v4 = self.vertices[3] - self.vertices[0]
        bool1 = np.allclose(np.cross(v1, v2), 0)
        bool2 = np.allclose(np.cross(v3, v4), 0)
        if not (bool1 or bool2):
            raise ValueError(
                "Quadrilateral does not have any parallel opposite sides."
                "It cannot be a trapezoid")
