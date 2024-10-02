"""
Specific routines for defining and designing tr_7500 columns.

Notes
-----
Design based on limit state design.

References
----------
TBEC-1975(TR)-Specification for Structures to be Built in Disaster Areas
TS500-1975(TR)-Design and Construction Rules for Reinfoced Concrete Buildings
TS500-1984(TR)-Design and Construction Rules for Reinfoced Concrete Buildings
"""

# Imports from installed packages
from math import ceil
import numpy as np

# Imports from the design class (tr_7500) library
from .materials import Steel, Concrete

# Imports from bdim base library
from ..baselib.column import ColumnBase

# Imports from utils library
from ....utils.units import MPa, m
from ....utils.design import SectionDesigner

ECONOMIC_MU: float = 0.25
"""Maximum mu value considered for the economic column design."""
MAX_NIU = 0.60
"""Maximum allowed value of axial load ratio. Section-8.2.6 in TS500-1984"""


class Column(ColumnBase):
    """Column object for design class: tr_7500."""

    steel: Steel
    """Steel material."""
    concrete: Concrete
    """Concrete material."""

    @property
    def fctk(self) -> float:
        """
        Reference
        ---------
        Section 3.3.2 in T5500-1984

        Returns
        -------
        float
            Characteristic value of tensional steel strength (in base units).
        """
        return (0.35 * (self.concrete.fck) ** (1 / 2)) * MPa

    @property
    def fctd(self) -> float:
        """
        Returns
        -------
        float
            Design value of tensional steel strength (in base units).
        """
        return self.fctk / self.concrete.PARTIAL_FACTOR

    @property
    def rhol_max(self) -> float:
        """
        References
        ----------
        # Section 12.3.2 in TS500-1984

        Returns
        -------
        float
            Maximum allowed longitudinal reinforcement ratio.
        """
        return 0.04

    @property
    def rhol_min(self) -> float:
        """
        Reference
        ---------
        #Section 6.6 in TBEC-1975

        Returns
        -------
        float
            Minimum longitudinal reinforcement ratio.
        """

        return 0.01

    @property
    def rhoh_min(self) -> float:
        """
        Reference
        ---------
        Section 7.3.4 in TBEC-1998

        Returns
        -------
        float
            Minimum transverse reinforcement ratio.
        """
        return max(0.12 * self.fck / self.fsyk, 0.01)

    def predesign(self) -> None:
        """Does preliminary design of column.

        This method makes initial guess for section dimensions.
        """
        # Initial guess for column concrete area
        min_area = self.pre_Nd / (MAX_NIU * self.fck)
        # Determine initial dimensions
        if self.section == 1:  # Square section
            self.bx = min_area**0.5
            self.by = min_area**0.5
        elif self.section == 2:  # Rectangular section
            if self.orient == "x":  # Longer dimension is bx
                self.bx = (2 * min_area) ** 0.5
                self.by = 0.50 * self.bx
            elif self.orient == "y":  # Longer dimension is by
                self.by = (2 * min_area) ** 0.5
                self.bx = 0.50 * self.by
        # Check against minimum dimensions
        self.bx = max(ceil(20 * self.bx) / 20, self.min_b)
        self.by = max(ceil(20 * self.by) / 20, self.min_b)

    def verify_section_adequacy(self) -> None:
        """Verifies the column section dimensions for design forces."""
        # Maximum axial load ratio
        max_niu = max(
            self.envelope_forces.N1_pos,
            self.envelope_forces.N9_pos,
            abs(self.envelope_forces.N1_neg),
            abs(self.envelope_forces.N9_neg),
        ) / (self.Ag * self.fck)

        # Maximum moment ratio
        max_mu_x = max(
            self.envelope_forces.Mx1_pos,
            self.envelope_forces.Mx9_pos,
            abs(self.envelope_forces.Mx1_neg),
            abs(self.envelope_forces.Mx9_neg),
        ) / ((self.bx * self.by**2) * self.fcd)
        max_mu_y = max(
            self.envelope_forces.My1_pos,
            self.envelope_forces.My9_pos,
            abs(self.envelope_forces.My1_neg),
            abs(self.envelope_forces.My9_neg),
        ) / ((self.by * self.bx**2) * self.fcd)

        # Maximum shear force
        max_Vx = max(self.envelope_forces.Vx1, self.envelope_forces.Vx9)
        max_Vy = max(self.envelope_forces.Vy1, self.envelope_forces.Vy9)

        # Distance from extreme compression fiber to centroid of longitudinal
        # reinforcement.
        dx = 0.90 * self.bx
        dy = 0.90 * self.by

        # Maximum acceptable shear force # Eq. 8.49 in TS500-1984
        Vrdx = 0.25 * self.fcd * self.by * dx
        Vrdy = 0.25 * self.fcd * self.bx * dy

        if max_mu_y > ECONOMIC_MU or max_Vx > Vrdx:
            # Need to increase dimension parallel to global-x
            self.ok_x = False
        else:
            self.ok_x = True
        if max_mu_x > ECONOMIC_MU or max_Vy > Vrdy:
            # Need to increase dimension parallel to global-y
            self.ok_y = False
        else:
            self.ok_y = True
        if max_niu > MAX_NIU and self.ok_x and self.ok_y:
            # May increase both dimensions or random one?
            self.ok_x = False
            self.ok_y = False

    def compute_required_longitudinal_reinforcement(self) -> None:
        """Computes the required reinforcement area for design forces."""
        Asl_x = 2 * np.pi * 0.25 * ((0.014 * m) ** 2)
        Asl_y = 2 * np.pi * 0.25 * ((0.014 * m) ** 2)
        for force in self.design_forces:
            # Determine the required longitudinal reinforcement ratio
            N1d = 0 if force.N1 > 0 else abs(force.N1)
            N9d = 0 if force.N9 > 0 else abs(force.N9)

            ex = 0.1 * self.bx  # min. eccentr. in the x direct., TS500-1984
            ey = 0.1 * self.by  # min. eccentr. in the y direct., TS500-1984

            Mx1d_ecc = N1d * ex
            Mx9d_ecc = N9d * ex
            My1d_ecc = N1d * ey
            My9d_ecc = N9d * ey

            Mx1d = max(abs(force.Mx1), Mx1d_ecc)
            Mx9d = max(abs(force.Mx9), Mx9d_ecc)
            My1d = max(abs(force.My1), My1d_ecc)
            My9d = max(abs(force.My9), My9d_ecc)

            Asl_1_x, Asl_1_y = SectionDesigner(
                N1d, Mx1d, My1d, self.fcd, self.fsyd, self.bx,
                self.by, self.rhol_min).get_long_reinf_area()
            Asl_9_x, Asl_9_y = SectionDesigner(
                N9d, Mx9d, My9d, self.fcd, self.fsyd, self.bx,
                self.by, self.rhol_min).get_long_reinf_area()

            Asl_x = max(Asl_x, max(Asl_1_x, Asl_9_x))
            Asl_y = max(Asl_y, max(Asl_1_y, Asl_9_y))

        # Save the required longitudinal reinforcement values
        self.Aslx_req = Asl_x
        self.Asly_req = Asl_y

    def compute_required_transverse_reinforcement(self) -> None:
        """Computes the required transverse reinforcement for design forces."""
        # Distance of long. bars in tens. to extreme conc. fibers in compr.
        dx = 0.9 * self.bx
        dy = 0.9 * self.by

        # lever arm, i.e., distance between comp. and tens. forces
        zx = 0.9 * dx
        zy = 0.9 * dy

        # Minimum transverse reinforcement area to spacing ratio
        Ashx_sh_min = self.rhoh_min * self.by
        Ashy_sh_min = self.rhoh_min * self.bx

        # Design shear forces
        Vd_x = max(self.envelope_forces.Vx1, self.envelope_forces.Vx9)
        Vd_y = max(self.envelope_forces.Vy1, self.envelope_forces.Vy9)
        Nd = max(abs(self.envelope_forces.N1_neg),
                 abs(self.envelope_forces.N9_neg))

        # Shear force resisted by concrete, Section 8.3 in TS500-1984
        Vcr_x = 0.65 * self.fctd * self.by * dx * (1 + 0.07 * Nd / self.Ag)
        Vcr_y = 0.65 * self.fctd * self.bx * dy * (1 + 0.07 * Nd / self.Ag)

        # Transverse reinforcement computation, Section 8.3 in TS500-1984
        if Vd_x <= Vcr_x:
            Ashx_sh = self.rhoh_min * self.by
        else:
            Ashx_sh = Vd_x / (self.fsyd * zx)

        if Vd_y <= Vcr_y:
            Ashy_sh = self.rhoh_min * self.bx
        else:
            Ashy_sh = Vd_y / (self.fsyd * zy)

        # Save the required transverse reinforcement area to spacing ratio
        self.Ashx_sbh_req = max(Ashx_sh_min, Ashx_sh)
        self.Ashy_sbh_req = max(Ashy_sh_min, Ashy_sh)
