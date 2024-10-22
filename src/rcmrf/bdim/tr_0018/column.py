"""
Specific routines for defining and designing tr_0018 columns.

Notes
-----
Design based on limit state design.
"""

# Imports from installed packages
from math import ceil
import numpy as np

# Imports from the design class (tr_0018) library
from .materials import Steel, Concrete

# Imports from bdim base library
from ..baselib.column import ColumnBase

# Imports from bdim tr_7599.column library
from ..tr_7599.column import LongReinfAreaCalculator

# Imports from utils library
from ....utils.units import MPa, m

ECONOMIC_MU: float = 0.25
"""Maximum mu value considered for the economic column design."""
MAX_NIU = 0.50
"""Maximum allowed value of axial load ratio. Section-7.3 in TBEC-1998
and Section-3.3 in TBEC-2007"""


class Column(ColumnBase):
    """Column object for design class: tr_0018."""

    steel: Steel
    """Steel material."""
    concrete: Concrete
    """Concrete material."""
    MIN_B_SQUARE: float = 0.25 * m
    """The default minimum square column dimension."""
    MIN_B_RECTANGLE: float = 0.25 * m
    """The default minimum rectangular column dimension."""
    Ve_x: float = 0.0
    """Column capacity design shear force through local x direction"""
    Ve_y: float = 0.0
    """Column capacity design shear force through local y direction"""

    @property
    def fctk(self) -> float:
        """
        Reference
        ---------
        Equation 3.1 in T5500-2000

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
        Reference
        ---------
        Section 7.3.2 in TBEC-1998
        Section 3.3.2 in TBEC-2007

        Returns
        -------
        float
            Maximum longitudinal reinforcement ratio.
        """
        return 0.04

    @property
    def rhol_min(self) -> float:
        """
        Reference
        ---------
        Section 7.3.2 in TBEC-1998
        Section 3.3.2 in TBEC-2007

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
        Section 3.3.4 in TBEC-2007

        Returns
        -------
        float
            Minimum transverse reinforcement ratio.
        """
        # Maximum axial load ratio
        max_niu = max(
            self.envelope_forces.N1_pos,
            self.envelope_forces.N9_pos,
            abs(self.envelope_forces.N1_neg),
            abs(self.envelope_forces.N9_neg),
        ) / (self.Ag * self.fck)
        Ack = (self.bx - 2 * self.cover) * (self.by - 2 * self.cover)
        ratio1 = 0.3 * (self.Ag / Ack - 1) * (self.fck / self.fsyk)
        ratio2 = 0.075 * (self.fck / self.fsyk)
        if max_niu > 0.20:
            return max(ratio1, ratio2)
        else:
            return (2 / 3) * max(ratio1, ratio2)

    def predesign_section_dimensions(self) -> None:
        """Does preliminary design of column.

        This method makes initial guess for section dimensions.
        """
        # Unit conversions
        Nd = self.pre_Nd
        # Initial guess for column concrete area
        min_area = max(0.075, Nd / (MAX_NIU * self.fck))
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
        if self.Ve_x != 0 and self.Ve_y != 0:
            max_Vx = self.Ve_x
            max_Vy = self.Ve_y
        else:
            max_Vx = max(self.envelope_forces.Vx1, self.envelope_forces.Vx9)
            max_Vy = max(self.envelope_forces.Vy1, self.envelope_forces.Vy9)

        # Distance from extreme compression fiber to
        # centroid of longitudinal reinforcement.
        dx = 0.90 * self.bx
        dy = 0.90 * self.by

        # Maximum acceptable shear force # Eq. 8.7 in TS500-2000
        Vrdx = 0.22 * self.fcd * self.by * dx
        Vrdy = 0.22 * self.fcd * self.bx * dy

        # Verify the adequacy of the section dimensions
        if (max_mu_y / 0.70) > ECONOMIC_MU or max_Vx > Vrdx:
            # Need to increase dimension parallel to global-x
            self.ok_x = False
        else:
            self.ok_x = True
        if (max_mu_x / 0.70) > ECONOMIC_MU or max_Vy > Vrdy:
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
        # Initial longitudinal reinforcement area
        Asl_x = 2 * np.pi * 0.25 * ((0.014 * m) ** 2)
        Asl_y = 2 * np.pi * 0.25 * ((0.014 * m) ** 2)
        for force in self.design_forces:
            # Determine the required longitudinal reinforcement
            N1d = 0 if force.N1 > 0 else abs(force.N1)
            N9d = 0 if force.N9 > 0 else abs(force.N9)

            # Equation-6.16 in TS500
            ex = 0.015 + 0.03 * self.bx  # minimum eccent. in the x direction
            ey = 0.015 + 0.03 * self.by  # minimum eccent. in the y direction

            My1d_ecc = N1d * ex
            My9d_ecc = N9d * ex
            Mx1d_ecc = N1d * ey
            Mx9d_ecc = N9d * ey

            Mx1d = max(abs(force.Mx1), Mx1d_ecc)
            Mx9d = max(abs(force.Mx9), Mx9d_ecc)
            My1d = max(abs(force.My1), My1d_ecc)
            My9d = max(abs(force.My9), My9d_ecc)

            Asl_1_x, Asl_1_y = LongReinfAreaCalculator(
                N1d, Mx1d, My1d, self.fck, self.fcd, self.fsyd, self.Es,
                self.bx, self.by, self.rhol_min).get_long_reinf_area()
            Asl_9_x, Asl_9_y = LongReinfAreaCalculator(
                N9d, Mx9d, My9d, self.fck, self.fcd, self.fsyd, self.Es,
                self.bx, self.by, self.rhol_min).get_long_reinf_area()

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

        # Minimum transverse reinforcement area to spacing ratio
        Ashx_sh_min = self.rhoh_min * (self.by - self.cover)
        Ashy_sh_min = self.rhoh_min * (self.bx - self.cover)

        # Design forces from envelopes
        Vd_x = max(self.envelope_forces.Vx1, self.envelope_forces.Vx9)
        Vd_y = max(self.envelope_forces.Vy1, self.envelope_forces.Vy9)
        Nd = max(abs(self.envelope_forces.N1_neg),
                 abs(self.envelope_forces.N9_neg))

        # Design shear forces
        if self.Ve_x != 0 and self.Ve_y != 0:
            Ve_x = self.Ve_x
            Ve_y = self.Ve_y
        else:
            Ve_x = Vd_x
            Ve_y = Vd_y

        # Shear force resisted by concrete, Eq.8.1 in TS500-2000
        Vcr_x = 0.65 * self.fctd * self.by * dx * (1 + 0.07 * Nd / self.Ag)
        Vc_x = 0.8 * Vcr_x
        Vcr_y = 0.65 * self.fctd * self.bx * dy * (1 + 0.07 * Nd / self.Ag)
        Vc_y = 0.8 * Vcr_y

        # Transverse reinforcement computation
        # Section 7.3.7 in TBEC-1998 and Section 3.3.7 in TBEC-2007
        if Ve_x <= Vcr_x:
            Ashx_sh = self.rhoh_min * self.by
        else:
            if Ve_x >= 0.5 * Vd_x and Nd <= 0.05 * self.Ag * self.fck:
                Vc_x = 0
            Vw = Ve_x - Vc_x
            Ashx_sh = Vw / (self.fsyd * dx)

        if Ve_y <= Vcr_y:
            Ashy_sh = self.rhoh_min * self.bx
        else:
            if Ve_y >= 0.5 * Vd_y and Nd <= 0.05 * self.Ag * self.fck:
                Vc_y = 0
            Vw = Ve_y - Vc_y
            Ashy_sh = Vw / (self.fsyd * dy)

        # Save the required ratio of transverse reinforcement area along
        # x and y axes to the reinforcement spacing
        self.Ashx_sbh_req = max(Ashx_sh_min, Ashx_sh)
        self.Ashy_sbh_req = max(Ashy_sh_min, Ashy_sh)
