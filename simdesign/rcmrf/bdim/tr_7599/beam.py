"""
Specific routines for defining and designing tr_7599 beams.

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
from typing import Tuple

# Imports from the design class (tr_7599) library
from .materials import Steel, Concrete

# Imports from bdim base library
from ..baselib.beam import BeamBase, Array3

# Imports from units library
from ....utils.units import MPa, m

# Constants
ECONOMIC_MU_EB: float = 0.25
"""Maximum mu value considered for the economic emergent beam design."""
ECONOMIC_MU_WB: float = 0.25
"""Maximum mu value considered for the economic wide beam design."""
EPS_CU = 0.003
"""Concrete crushing strain used for computing section capacity."""


class Beam(BeamBase):
    """Beam object for design class: tr_7599."""

    steel: Steel
    """Steel material."""
    concrete: Concrete
    """Concrete material."""
    MIN_B_EB: float = 0.20 * m
    """The default minimum breadth (width) of emergent beams."""
    MIN_H_EB: float = 0.30 * m
    """The default minimum breadth (width) of emergent beams."""

    @property
    def fctk(self) -> float:
        """
        Reference
        ----------
        Section 3.3.2 in T5500-1984

        Returns
        -------
        float
            Characteristic value of tensional concrete strength
            (in base units).
        """
        return (0.35 * (self.concrete.fck) ** (1 / 2)) * MPa

    @property
    def fctd(self) -> float:
        """
        Returns
        -------
        float
            Design value of tensional concrete strength (in base units).
        """
        return self.fctk / self.concrete.PARTIAL_FACTOR

    @property
    def rhol_min_tens(self) -> float:
        """
        Reference
        ----------
        # Section 6.9 in TBEC-1975

        Returns
        -------
        float
            Minimum longitudinal reinforcement ratio in tension zone
        """
        if self.steel.grade == "S220":
            return 0.005
        elif self.steel.grade == "S420":
            return 0.003

    @property
    def rhoh_min(self) -> float:
        """
        Reference
        ----------
        # Equation 12.3 in TS500-1984

        Returns
        -------
        float
            Minimum transverse reinforcement ratio
        """
        return 0.15 * (self.fctd) / (self.fsyd)

    def predesign_section_dimensions(self, slab_h: float) -> None:
        """Does preliminary design of beam.

        This method makes initial guess for section dimensions.

        Parameters
        ----------
        slab_h : float
            Slab thickness.
        """
        # Unit conversions
        Md = self.pre_Md
        # Emergent beam cases
        bool1 = self.typology == 2
        bool2 = self.exterior
        bool3 = self.stairs_wg != 0.0
        if bool1 or bool2 or bool3:
            # Set section breadth to minimum
            self.b = self.min_b
            # Compute height for economic section, assuming d = 0.1h
            mu_h = ((Md / (ECONOMIC_MU_EB * self.fcd * self.b)) ** 0.5) / 0.9
            # Compute height to control deformations
            if self.stairs_wg != 0.0 or sum(self.slab_wg) != 0.0:
                # The beam carries a slab (stairs or floor slab)
                def_h = self.L / 12
            else:  # The beam is secondary gravity beam
                def_h = self.L / (0.9 * 18)
            # Get the maximum slab computed from all
            self.h = max(self.min_h, slab_h, mu_h, def_h)
            # Iterate for aspect ratio consideration
            while self.h / self.b > self.MAX_ASPECT_RATIO_EB:
                # Increase breadth
                self.b += self.B_INCR_EB
                # Compute height for economic section, assuming d = 0.1h
                mu_h = ((Md / (ECONOMIC_MU_EB * self.fcd *
                               self.b)) ** 0.5) / 0.9
                # Compute height to control deformations
                if self.stairs_wg != 0.0 or sum(self.slab_wg) != 0.0:
                    # The beam carries a slab (stairs or floor slab)
                    def_h = self.L / 12
                else:  # The beam is secondary gravity beam
                    def_h = self.L / (0.9 * 18)
                # Get the maximum slab computed from all
                self.h = max(self.min_h, slab_h, mu_h, def_h)
        # Wide beam cases
        else:
            # Set section height (slab thickness or minimum)
            self.h = max(slab_h, self.min_h)
            # Section widths
            if sum(self.slab_wg) == 0.0:  # Secondary gravity beams
                self.b = self.min_b  # Use minimum dimension
            else:  # Primary gravity beams
                # Set width based on economic mu value and minimum allowed
                self.b = max(self.min_b,
                             (Md / (ECONOMIC_MU_WB*self.fcd*(0.9*self.h)**2))
                             )
                while (self.b > self.max_b or
                       self.b / self.h > self.MAX_ASPECT_RATIO_WB):
                    self.h += self.H_INCR_WB
                    self.b = Md / (ECONOMIC_MU_WB*self.fcd*(0.9*self.h)**2)
        # Round
        self.h = ceil(20 * self.h) / 20
        self.b = ceil(20 * self.b) / 20

    def verify_section_adequacy(self) -> None:
        """Verifies the beam section dimensions for design forces."""
        # Economic mu values (dimensionless)
        if self.typology == 1:
            mu_economic = ECONOMIC_MU_WB
        elif self.typology == 2:
            mu_economic = ECONOMIC_MU_EB

        # Distance from extreme compression fiber to centroid of longitudinal
        # tension reinforcement.
        d = 0.90 * self.h

        # Maximum of envelope forces
        max_shear = max(
            self.envelope_forces.V1, self.envelope_forces.V5,
            self.envelope_forces.V9)
        max_moment = max(
            self.envelope_forces.M1_pos,
            self.envelope_forces.M5_pos,
            self.envelope_forces.M9_pos,
            abs(self.envelope_forces.M1_neg),
            abs(self.envelope_forces.M5_neg),
            abs(self.envelope_forces.M9_neg)
        )

        # Verify the adequacy of the section dimensions
        Vrd_max = 0.25 * self.fcd * self.b * d  # Eq. 8.49 in TS500-1984
        mu = max_moment / (self.fcd * self.b * d**2)  # for max. bending moment

        if mu < mu_economic and max_shear < Vrd_max:
            self.ok = True  # Ok
        else:
            self.ok = False  # Not ok

    def _get_long_area(self, Md: Array3
                       ) -> Tuple[Array3[np.float64], Array3[np.float64]]:
        """Beam design method to be used in compute_required_reinforcement
        method.

        Parameters
        ----------
        Md : np.ndarray
            Moment value to be used for beam design.

        Returns
        -------
        As_required : np.ndarray
            Required tension steel area.
        Asprime_required : np.ndarray
            Required compression steel area.
        """
        # Initial material and geometrical definitions
        fcd = self.fcd
        fyd = self.fsyd
        Es = self.Es
        bw = self.b
        dprime = 0.1 * self.h
        d = self.h - dprime

        # Definition of k1 and k3
        k1 = min(1 - 0.006 * self.fck / MPa, 0.85)
        k3 = 0.85

        # Bending moment calculation for the choice between single
        # and double reinforcement.
        Mr1 = 0.235 * fcd * bw * (d**2) * (1 - 0.1175 / k3)

        As_required = np.zeros(len(Md))
        Asprime_required = np.zeros(len(Md))
        mask = Md < Mr1
        if np.any(mask):  # Single reinforcement
            K = Md[mask] / (bw * d**2)
            rho = k3 * (fcd / fyd) * (1 - (1 - (2 * K) / (k3 * fcd)) ** 0.5)
            As_required[mask] = rho * bw * d
            Asprime_required[mask] = 0
        else:  # Double reinforcement
            As1 = 0.235 * (fcd / fyd) * bw * d
            Mr2 = Md[~mask] - Mr1
            As2 = Mr2 / (fyd * (d - dprime))
            epss_prime = 0.003 * (1 - (k1 * k3 / 0.235) * (dprime / d))
            sigmas_prime = epss_prime * Es

            if sigmas_prime >= fyd:
                sigmas_prime = fyd
            else:
                sigmas_prime = sigmas_prime

            As_required[~mask] = As1 + As2
            Asprime_required[~mask] = As2 * fyd / sigmas_prime

        return As_required, Asprime_required

    def compute_required_longitudinal_reinforcement(self) -> None:
        """Computes the required longitudinal reinforcement for design forces.

        Notes
        -----
        1. Top reinforcement is calculated as the maximum of required
        reinforcement in tension for maximum of negative bending moments
        and required reinforcement in compression for maximum of positive
        bending moments.
        2. Bottom reinforcement is calculated as the maximum of required
        reinforcement in compression for maximum of negative bending moments
        and required reinforcement in tension for maximum of positive
        bending moments.
        3. Required reinforcement is computed at different sections:
        start, mid, end.
        """

        # Design forces
        moment_pos = np.array(
            [
                self.envelope_forces.M1_pos,
                self.envelope_forces.M5_pos,
                self.envelope_forces.M9_pos,
            ]
        )
        moment_neg = np.array(
            [
                self.envelope_forces.M1_neg,
                self.envelope_forces.M5_neg,
                self.envelope_forces.M9_neg,
            ]
        )
        moment_neg = np.abs(moment_neg)

        # Longitudinal reinforcement computation
        # ...........................................................................

        # For positive moment envelope (+)
        Asl_pos_bot, Asl_pos_top = self._get_long_area(moment_pos)

        # For negative moment envelope (-)
        Asl_neg_top, Asl_neg_bot = self._get_long_area(moment_neg)

        # Determine required reinforcement at top and bottom
        Asl_bot = np.maximum(Asl_pos_bot, Asl_neg_bot)
        Asl_top = np.maximum(Asl_neg_top, Asl_pos_top)

        # Check against minimum longitudinal reinforcement area
        Asl_min_tens = self.rhol_min_tens * self.b * (0.9 * self.h)
        Asl_top = np.maximum(Asl_top, Asl_min_tens)
        Asl_bot = np.maximum(Asl_bot, Asl_min_tens)

        # Compression to tension reinf. ratio must be greater than 0.333
        mask = Asl_top / Asl_bot < (1 / 3)
        if np.any(mask):
            Asl_top[mask] = (1 / 3) * Asl_bot[mask]
        mask = Asl_bot / Asl_top < (1 / 3)
        if np.any(mask):
            Asl_bot[mask] = (1 / 3) * Asl_top[mask]

        # Save required longitudinal steel area
        self.Asl_top_req = Asl_top
        self.Asl_bot_req = Asl_bot

    def compute_required_transverse_reinforcement(self) -> None:
        """Computes the required transverse reinforcement for design forces.

        Notes
        -----
        1. Required reinforcement is computed at different sections:
        start, mid, end.
        """
        # Design shear force
        Vd = np.array(
            [self.envelope_forces.V1, self.envelope_forces.V5,
             self.envelope_forces.V9]
        )

        # Transverse reinforcement computation, Section 8.3 in TBEC-1984
        Vcr = 0.65 * self.fctd * self.b * (0.9 * self.h)
        Ash_sbh = np.zeros(len(Vd))
        Ash_sbh_min = self.rhoh_min * self.b
        mask = Vd <= Vcr
        Ash_sbh[mask] = Ash_sbh_min
        Ash_sbh[~mask] = Vd[~mask] / (self.fsyd * (0.9 * self.h))
        Ash_sbh = np.maximum(Ash_sbh, Ash_sbh_min)

        # Save required transverse reinforcement area to spacing ratio
        self.Ash_sbh_req = Ash_sbh
