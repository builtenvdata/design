# Imports from installed packages
import numpy as np
from scipy.optimize import root
from typing import Tuple, List


class SectionDesigner:
    """Longititutional reinforcement area calculator class for biaxially loaded
    reinforced concrete rectangular column sections.

    Attributes
    ----------
    b : float
        Column width (m).
    h : float
        Column height (m).
    Nd : float
        Axial load on RC column (kN).
    Mxd : float
        Bending moment on RC column in the X direction (kNm).
    Myd : float
        Bending moment on RC column in the Y direction (kNm).
    fcd : float
        Design value of concrete strength (kPa).
    fyd : float
        Design value of steel strength (kPa).
    cover_b : float
        Clear cover in the width direction (m).
    cover_h : float
        Clear cover in the height direction (m).
    Es : float
        Modulus of elasticity of steel (kPa).
    eps_cu : float
        Ultimate compressive strain value for concrete.
    k1 : float
        Reduction factor for concrete compressive stress block.
    rho_l_min : float
        Minimum reinforcement ratio for longitudinal steel bars.
    section_corner_coordinates : np.ndarray
        Array of coordinates of the column section corners.
    x_coordinates : np.ndarray
        Array of x-coordinates of the column section corners.
    y_coordinates : np.ndarray
        Array of y-coordinates of the column section corners.
    dist_between_bars_b : float
        Distance between longitudinal bars along the width direction (m).
    num_bars_int_b : int
        Number of longitudinal bars along the width direction.
    dist_between_bars_h : float
        Distance between longitudinal bars along the height direction (m).
    num_bars_int_h : int
        Number of longitudinal bars along the height direction.
    num_bars : int
        Total number of longitudinal bars in the section.
    bar_coords : np.ndarray
        Array of coordinates of the longitudinal steel bars.
    section_area : float
        Total area of the column section (m2).
    xg : float
        X-coordinate of the centroid of the column section.
    yg : float
        Y-coordinate of the centroid of the column section.
    max_dist : float
        Maximum perpendicular distance from a corner point to the reduced
        neutral axis.

    Assumptions
    -----------
    1- Equally spaced steel bars are used over the section.
        |  ---------------
        |  --o-o-o-o-o-o--
        |  --o---------o--
        |  --o---------o--
        h  --o---------o--
        |  --o---------o--
        |  --o-o-o-o-o-o--
        |  ---------------
            -------b-------

    2- Equivalent rectangular stress block approach is used to represent
    stresses on compression zone.
    3- Only axial compressive forces are accepted.
    4- The ultimate compressive strain value, epsc_u, is assumed to be
    equal to 0.003.
    5- Longititional steel bar diameters are assumed to be equal.
    """

    b: float
    """Column width (m)."""
    h: float
    """Column height (m)."""
    Nd: float
    """Axial load on RC column (kN)."""
    Mxd: float
    """Bending moment on RC column in the X direction (kNm)."""
    Myd: float
    """Bending moment on RC column in the Y direction (kNm)."""
    fcd: float
    """Design value of concrete strength (kPa)."""
    fyd: float
    """Design value of steel strength (kPa)."""
    cover_b: float
    """Clear cover in the width direction (m)."""
    cover_h: float
    """Clear cover in the height direction (m)."""
    Es: float
    """Modulus of elasticity of steel (kPa)."""
    eps_cu: float
    """Ultimate compressive strain value for concrete."""
    k1: float
    """Reduction factor for concrete compressive stress block."""
    rho_l_min: float
    """Minimum reinforcement ratio for longitudinal steel bars."""
    section_corner_coordinates: np.ndarray
    """Array of coordinates of the column section corners."""
    x_coordinates: np.ndarray
    """Array of x-coordinates of the column section corners."""
    y_coordinates: np.ndarray
    """Array of y-coordinates of the column section corners."""
    dist_between_bars_b: float
    """Distance between longitudinal bars along the width direction (m)."""
    num_bars_int_b: int
    """Number of longitudinal bars along the width direction"""
    dist_between_bars_h: float
    """Distance between longitudinal bars along the height direction (m)."""
    num_bars_int_h: int
    """Number of longitudinal bars along the height direction."""
    num_bars: int
    """Total number of longitudinal bars in the section."""
    bar_coords: np.ndarray
    """Array of coordinates of the longitudinal steel bars."""
    section_area: float
    """Total area of the column section (m2)."""
    xg: float
    """X-coordinate of the centroid of the column section."""
    yg: float
    """Y-coordinate of the centroid of the column section."""
    max_dist: float
    """Maximum perpendicular distance from a corner point to the reduced
    neutral axis."""

    def __init__(
        self, Nd: float, Mxd: float, Myd: float, fcd: float,
        fyd: float, Es: float, b: float, h: float, rho_l_min: float
    ) -> None:
        """Initializes the ColumnSectionDesigner object.

        Parameters
        ----------
        Nd : float
            Axial load on RC column, (kN)
        Mxd : float
            Bending moment on RC column in the X direction, (kNm)
        Myd : float
            Bending moment on RC column in the Y direction, (kNm)
        fcd : float
            Design value of concrete strength, (kPa)
        fyd : float
            Design value of steel strength, (kPa)
        Es : float
            Elastic young modulus of steel, (kPa)
        b : float
            Column width, (m)
        h : float
            Column height, (m)
        """
        # Section sizes
        self.b = b
        self.h = h

        # Considers minimum eccentricity moments
        self.Nd = Nd
        self.Mxd = Mxd
        self.Myd = Myd
        self.fcd = fcd
        self.fyd = fyd
        self.cover_b = 0.1 * b  # clear cover + stirrup diam. + 0.5*long.diam.
        self.cover_h = 0.1 * h  # clear cover + stirrup diam. + 0.5*long.diam.
        self.Es = Es  # Elasticity modulus of steel, kPa
        self.eps_cu = 0.003
        self.k1 = min(1 - 0.006 * self.fcd / 1000, 0.85)
        self.rho_l_min = rho_l_min

        # Defines section corner points
        self.section_corner_coordinates = np.array(
            [[0, 0], [0, 0 + self.h],
             [0 + self.b, 0 + self.h], [0 + self.b, 0]]
        )
        self.x_coordinates = self.section_corner_coordinates[:, 0]
        self.y_coordinates = self.section_corner_coordinates[:, 1]

        # Find spacing between rebars and their number
        self._find_bar_spacing()
        # Get coordinates of the steel rebars
        self._get_bar_coordinates()
        # Area of the section
        self.section_area = self._find_section_area(
            self.x_coordinates, self.y_coordinates
        )
        # Coordinates of mass center of section
        self.xg, self.yg = self._find_center(
            self.section_area, self.x_coordinates, self.y_coordinates
        )

    def _find_bar_spacing(self) -> None:
        """Finds the bar spacing and quantity on each side of the section.
        """
        # Finds short and long side lengths for between outermost rebars
        shortside, longside = min(
            self.b - 2 * self.cover_b, self.h - 2 * self.cover_h
        ), max(self.b - 2 * self.cover_b, self.h - 2 * self.cover_h)

        # Finds the index of the closest spacing to 0.15 m.
        possible_spacings = shortside / np.arange(1, 10)  # Possible spacings
        closest_idx = np.argmin(np.abs(possible_spacings - 0.15))

        if shortside == self.b - 2 * self.cover_b:
            self.dist_between_bars_b = round(possible_spacings[closest_idx], 4)
            self.num_bars_int_b = closest_idx
            self.dist_between_bars_h = round(
                longside / np.floor(longside /
                                    possible_spacings[closest_idx]), 4
            )
            self.num_bars_int_h = int(
                np.floor(longside / possible_spacings[closest_idx]) - 1
            )
        else:
            self.dist_between_bars_h = round(possible_spacings[closest_idx], 4)
            self.num_bars_int_h = closest_idx
            self.dist_between_bars_b = round(
                longside / np.floor(longside /
                                    possible_spacings[closest_idx]), 4
            )
            self.num_bars_int_b = int(
                np.floor(longside / possible_spacings[closest_idx]) - 1
            )

    def _get_bar_coordinates(self) -> None:
        """Determines the coordinates and amount of the steel bars
        around the section.
        """
        bar_coords = []
        bar_coords.append(
            [self.x_coordinates[0] + self.cover_b,
             self.y_coordinates[0] + self.cover_h]
        )

        for i in range(1, int(self.num_bars_int_h) + 1):
            bar_coords.append(
                [
                    round(self.x_coordinates[0] + self.cover_b, 4),
                    round(
                        self.y_coordinates[0]
                        + self.cover_h
                        + i * self.dist_between_bars_h,
                        4,
                    ),
                ]
            )
        bar_coords.append(
            [
                round(self.x_coordinates[1] + self.cover_b, 4),
                round(self.y_coordinates[1] - self.cover_h, 4),
            ]
        )

        for i in range(1, int(self.num_bars_int_b) + 1):
            bar_coords.append(
                [
                    round(
                        self.x_coordinates[1]
                        + self.cover_b
                        + i * self.dist_between_bars_b,
                        4,
                    ),
                    round(self.y_coordinates[1] - self.cover_h, 4),
                ]
            )
        bar_coords.append(
            [
                round(self.x_coordinates[2] - self.cover_b, 4),
                round(self.y_coordinates[2] - self.cover_h, 4),
            ]
        )

        for i in range(1, int(self.num_bars_int_h) + 1):
            bar_coords.append(
                [
                    round(self.x_coordinates[2] - self.cover_b, 4),
                    round(
                        self.y_coordinates[2]
                        - self.cover_h
                        - i * self.dist_between_bars_h,
                        4,
                    ),
                ]
            )
        bar_coords.append(
            [
                round(self.x_coordinates[3] - self.cover_b, 4),
                round(self.y_coordinates[3] + self.cover_h, 4),
            ]
        )

        for i in range(1, int(self.num_bars_int_b) + 1):
            bar_coords.append(
                [
                    round(
                        self.x_coordinates[3]
                        - self.cover_b
                        - i * self.dist_between_bars_b,
                        4,
                    ),
                    round(self.y_coordinates[3] + self.cover_h, 4),
                ]
            )

        self.num_bars = len(bar_coords)
        self.bar_coords = np.array(bar_coords)

    def _find_section_area(self, x_coordinates: np.ndarray,
                           y_coordinates: np.ndarray) -> float:
        """Finds the area of a given section.

        Parameters
        ----------
        x_coordinates : np.ndarray
            x coordinates belonging to section corner coordinates.
        y_coordinates : np.ndarray
            y coordinates belonging to section corner coordinates.

        Returns
        -------
        float
            Section area.
        """
        area = 0
        for i in range(len(x_coordinates)):
            if i == len(x_coordinates) - 1:
                area += (
                    0.5
                    * (x_coordinates[0] - x_coordinates[i])
                    * (y_coordinates[0] + y_coordinates[i])
                )
            else:
                area += (
                    0.5
                    * (x_coordinates[i + 1] - x_coordinates[i])
                    * (y_coordinates[i + 1] + y_coordinates[i])
                )

        return round(area, 4)

    def _find_center(
        self, section_area: float,
        x_coordinates: np.ndarray,
        y_coordinates: np.ndarray
    ) -> Tuple[float, float]:
        """Finds the geometric center coordinates of a given section

        Parameters
        ----------
        section_area : float
            The area of given section
        x_coordinates : np.ndarray
            x coordinates belonging to section corner coordinates.
        y_coordinates : np.ndarray
            y coordinates belonging to section corner coordinates.

        Returns
        -------
        Tuple[float, float]
            Coordinates (x, y) of the center of given section.
        """
        section_area = max(section_area, 1e-10)
        xg, yg = 0, 0
        for i in range(len(x_coordinates)):
            if i == len(x_coordinates) - 1:
                xg += (
                    -(1 / (6 * section_area))
                    * (y_coordinates[0] - y_coordinates[i])
                    * (
                        x_coordinates[i] ** 2
                        + x_coordinates[i] * x_coordinates[0]
                        + x_coordinates[0] ** 2
                    )
                )
                yg += (
                    (1 / (6 * section_area))
                    * (x_coordinates[0] - x_coordinates[i])
                    * (
                        y_coordinates[i] ** 2
                        + y_coordinates[i] * y_coordinates[0]
                        + y_coordinates[0] ** 2
                    )
                )
            else:
                xg += (
                    -(1 / (6 * section_area))
                    * (y_coordinates[i + 1] - y_coordinates[i])
                    * (
                        x_coordinates[i] ** 2
                        + x_coordinates[i] * x_coordinates[i + 1]
                        + x_coordinates[i + 1] ** 2
                    )
                )
                yg += (
                    (1 / (6 * section_area))
                    * (x_coordinates[i + 1] - x_coordinates[i])
                    * (
                        y_coordinates[i] ** 2
                        + y_coordinates[i] * y_coordinates[i + 1]
                        + y_coordinates[i + 1] ** 2
                    )
                )

        return round(xg, 5), round(yg, 5)

    def _find_tdistance(self, coeff_c: float, coeff_a: float, xt: float,
                        yt: float) -> float:
        """Calculates the perpendicular distance between a corner point
        and the reduced neutral axis.

        Parameters
        ----------
        coeff_c : float
            The y-intercept of the reduced neutral axis equation (y = -ax + c).
        coeff_a : float
           The slope of the reduced neutral axis equation (y = -ax + c).
        xt : float
            The x-coordinate of the corner point.
        yt : float
            The y-coordinate of the corner point.

        Returns
        -------
        float
            The perpendicular distance between the corner point
            and the reduced neutral axis.
        """
        t = (
            -((coeff_c / coeff_a) * xt + yt - coeff_c)
            / ((coeff_c / coeff_a) ** 2 + 1) ** 0.5
        )

        return t

    def _find_sdistance(self, coeff_c: float, coeff_a: float, xi: float,
                        yi: float) -> float:
        """Calculates the perpendicular distance from a steel bar
        to the reduced neutral axis.

        Parameters
        ----------
        coeff_c : float
            The y-intercept of the reduced neutral axis equation (y = -ax + c).
        coeff_a : float
           The slope of the reduced neutral axis equation (y = -ax + c).
        xi : float
            The x-coordinate of the steel bar
        yi : float
            The y-coordinate of the steel bar

        Returns
        -------
        float
            The perpendicular distance between the steel bar and the
            reduced neutral axis.
        """
        s = (
            -((coeff_c / coeff_a) * xi + yi - coeff_c)
            / ((coeff_c / coeff_a) ** 2 + 1) ** 0.5
        )

        return s

    def _find_distance_max(self, coeff_c: float, coeff_a: float) -> float:
        """Calculates the maximum perpendicular positive distance to the
        reduced neutral axis from section corner points.

        Parameters
        ----------
        coeff_c : float
            The y-intercept of the reduced neutral axis equation (y = -ax + c).
        coeff_a : float
           The slope of the reduced neutral axis equation (y = -ax + c).

        Returns
        -------
        float
            The maximum perpendicular positive distance between the reduced
            neutral axis and corner points.
        """
        distances = [
            self._find_tdistance(coeff_c, coeff_a, i[0], i[1])
            for i in self.section_corner_coordinates
        ]
        max_dist = round(max(distances), 4)
        self.max_dist = max(max_dist, 1e-10)

    def _find_intsectpoint_line_naxis(
        self, coeff_c: float, coeff_a: float,
        x1: float, y1: float, x2: float, y2: float
    ) -> List[float] | None:
        """Finds the intersection point between a line segment and the
        reduced neutral axis.

        Parameters
        ----------
        coeff_c : float
            Coefficient C defining the reduced neutral axis equation
            (y = -ax + c).
        coeff_a : float
            Coefficient A defining the reduced neutral axis equation
            (y = -ax + c).
        x1 : float
            x-coordinate of the first point on the line segment.
        y1 : float
            y-coordinate of the first point on the line segment.
        x2 : float
            x-coordinate of the second point on the line segment.
        y2 : float
            y-coordinate of the second point on the line segment.

        Returns
        -------
        List[float] | None
            x and y coordinates of the intersection point, or None if no
            intersection or parallel lines.
        """
        # Calculate slope of the line segment
        if x1 == x2:
            y_check = (-coeff_c / coeff_a) * x1 + coeff_c
            if y1 < y_check < y2 or y1 > y_check > y2:
                x_int = x1
                y_int = y_check
                out = [x_int, y_int]
            else:
                out = None
        else:
            yt1 = (-coeff_c / coeff_a) * x1 + coeff_c
            yt2 = (-coeff_c / coeff_a) * x2 + coeff_c
            if yt1 < y1 < yt2 or yt1 > y1 > yt2:
                x_int = (y1 - coeff_c) * (-coeff_a / coeff_c)
                y_int = y1
                out = [x_int, y_int]
            else:
                out = None

        return out

    def _find_pressure_boundary(self, coeff_c: float, coeff_a: float
                                ) -> List[float]:
        """Finds the coordinates of the points that define the boundary of
        the pressure area.

        Parameters
        ----------
        coeff_c : float
            Coefficient C defining the reduced neutral axis equation
            (y = -ax + c).
        coeff_a : float
            Coefficient A defining the reduced neutral axis equation
            (y = -ax + c).

        Returns
        -------
        List[float]
            Coordinates of points defining the pressure area boundary.
        """
        sign_prev = 1
        boundary_points = []
        for i in range(len(self.x_coordinates)):
            # Calculate distance between point and neutral axis
            distance = self._find_tdistance(
                coeff_c, coeff_a, self.x_coordinates[i], self.y_coordinates[i]
            )

            # Set sign to 1 if within or on the pressure area
            if distance >= 0:
                sign = 1
            else:
                sign = 0

            if sign_prev != sign:
                # Find intersection point with neutral axis line segment
                intersection_point = self._find_intsectpoint_line_naxis(
                    coeff_c,
                    coeff_a,
                    self.x_coordinates[i - 1],
                    self.y_coordinates[i - 1],
                    self.x_coordinates[i],
                    self.y_coordinates[i],
                )
                # Add intersection point if it is exist
                if intersection_point is not None:
                    boundary_points.append(intersection_point)

            if distance >= 0:
                boundary_points.append((self.x_coordinates[i],
                                        self.y_coordinates[i]))

            if i == len(self.x_coordinates) - 1:
                # Find intersection point with neutral axis line segment
                intersection_point = self._find_intsectpoint_line_naxis(
                    coeff_c,
                    coeff_a,
                    self.x_coordinates[0],
                    self.y_coordinates[0],
                    self.x_coordinates[i],
                    self.y_coordinates[i],
                )
                # Add intersection point if it is exist
                if intersection_point is not None:
                    boundary_points.append(intersection_point)
            sign_prev = sign

        return boundary_points

    def _find_bar_stresses(self, coeff_c: float, coeff_a: float
                           ) -> List[float]:
        """Calculates the stresses in each steel bar based on their
        distance to the reduced neutral axis.

        Parameters
        ----------
        coeff_c : float
            The y-intercept of the reduced neutral axis equation (y = -ax + c).
        coeff_a : float
            The x-intercept of the reduced neutral axis equation (y = -ax + c).

        Returns
        -------
        List[float]
            List containing the stress values (sigma_si) for each steel bar.
        """
        self._find_distance_max(coeff_c, coeff_a)
        coords = self.bar_coords
        eps_si = np.array(
            [
                self.eps_cu
                * (
                    1
                    + self.k1
                    * self._find_sdistance(coeff_c, coeff_a,
                                           coords[i][0], coords[i][1])
                    / self.max_dist
                    - self.k1
                )
                for i in range(len(coords))
            ]
        )
        sigma_si = self.Es * eps_si
        sigma_si = [max(-self.fyd, val) for val in sigma_si]
        sigma_si = [min(self.fyd, val) for val in sigma_si]

        return sigma_si

    def _objective_function(self, input: List[float]) -> List[float]:
        """Solves the equilibrium equations for a given set of parameters.

        Parameters
        ----------
        input : List[float]
            An array containing trial values of coeff_c, coeff_a,
            and area_steel.

        Returns
        -------
        List[float]
            A list of three values representing the equilibrium equations.
        """
        coeff_c, coeff_a, area_steel = abs(input)
        boundary_points = np.array(self._find_pressure_boundary(coeff_c,
                                                                coeff_a))
        x_coords = [point[0] for point in boundary_points]
        y_coords = [point[1] for point in boundary_points]
        area_cc = self._find_section_area(x_coords, y_coords)
        xc, yc = self._find_center(area_cc, x_coords, y_coords)
        sigma_si = self._find_bar_stresses(coeff_c, coeff_a)

        eq1 = (
            0.85 * self.fcd * area_cc
            + (area_steel / self.num_bars) * np.sum(sigma_si)
            - self.Nd
        )
        eq2 = (
            0.85 * self.fcd * area_cc * (self.yg - yc)
            + (area_steel / self.num_bars)
            * np.sum(sigma_si * (self.yg - self.bar_coords[:, 1]))
            - self.Mxd
        )
        eq3 = (
            0.85 * self.fcd * area_cc * (self.xg - xc)
            + (area_steel / self.num_bars)
            * np.sum(sigma_si * (self.xg - self.bar_coords[:, 0]))
            - self.Myd
        )

        return [eq1, eq2, eq3]

    def get_long_reinf_area(self) -> Tuple[float, float]:
        """
        Finds the optimum values for for required steel area.

        Returns
        -------
        Tuple[float, float]
            Required longitudinal reinforcement area of bars
            distributed along -x and -y on each side.

        Raises
        ------
        RuntimeError: If fsolve fails to converge.
        """
        try:
            min_area = self.rho_l_min * self.section_area
            x0 = [0.5 * self.b, 0.5 * self.h, min_area]
            solution = root(self._objective_function, x0)
            total_area = abs(solution.x[2])
            rebar_area = total_area / self.num_bars
            area_x = (2 + self.num_bars_int_b) * rebar_area
            area_y = (2 + self.num_bars_int_h) * rebar_area
            return area_x, area_y
        except RuntimeError as e:
            print(f"fsolve failed to converge: {e}")
        raise
