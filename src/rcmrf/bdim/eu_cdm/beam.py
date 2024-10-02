"""
Specific routines for defining and designing eu_cdm beams.

Notes
-----
Methodology follows the case of DCM (REBAP-83) beam design.
Design based on limit state design.
Material qualities are higher compared CDL.

References
----------
REBAP (1983) Regulamento de Estruturas de Betão Armado e PréEsforçado.
Decreto-Lei N.° 349-C/83, Lisbon, Portugal
d'Arga e Lima, J., Monteiro V, Mun M (2005) Betão armado: esforços normais e
de flexão: REBAP-83. Laboratório Nacional de Engenharia Civil, Lisboa.

TODO
----
Discuss the default constants.
See specific lines with TODOs.
Add specific reference pages for design equations.
"""

# Imports from installed packages
from math import ceil
import numpy as np

# Imports from the design class (eu_cdm) library
from .materials import Steel, Concrete

# Imports from bdim base library
from ..baselib.beam import BeamBase

# Imports from units library
from ....utils.units import kN, MPa, m

# Constants
ECONOMIC_MU_EB: float = 0.25
"""Maximum mu value considered for the economic emergent beam design."""
ECONOMIC_MU_WB: float = 0.25
"""Maximum mu value considered for the economic wide beam design."""
TAU_C_VECT = np.array(
    [0.5, 0.6, 0.65, 0.75, 0.85, 0.90, 1.00, 1.10, 1.15]) * MPa
"""Vector of allowable shear stresses that carried by the concrete or
vector of the design shear strength values of concrete."""
TAU_MAX_VECT = np.array([2.4, 3.2, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]) * MPa
"""Vector of allowable shear stresses that can be carried by
the beam section."""
FCK_VECT = np.array([12, 16, 20, 25, 30, 35, 40, 45, 50]) * MPa
"""Vector of characteristic concrete compressive strength values."""


class Beam(BeamBase):
    """Beam object for design class: eu_cdm.
    """
    steel: Steel
    """Steel material."""
    concrete: Concrete
    """Concrete material."""
    MIN_B_EB: float = 0.25 * m
    """The default minimum breadth (width) of emergent beams."""

    @property
    def rhol_min_tens(self) -> float:
        """
        Returns
        -------
        float
            Minimum longitudinal reinforcement ratio in tension zone

        Notes
        -----
        Based on REBAP 90.1.
        """
        if self.steel.grade == "S500":
            return 0.12 / 100
        elif self.steel.grade == "S400":
            return 0.15 / 100
        else:
            return 0.25 / 100

    @property
    def rhoh_min(self) -> float:
        """
        Returns
        -------
        float
            Minimum transverse reinforcement ratio

        Notes
        -----
        Based on REBAP 94.2.
        """
        if self.steel.grade == "S500":
            return 0.08 / 100
        elif self.steel.grade == "S400":
            return 0.10 / 100
        else:
            return 0.16 / 100

    def predesign_section_dimensions(self, slab_h: float) -> None:
        """Does preliminary design of beam.

        This method makes initial guess for section dimensions.

        Parameters
        ----------
        slab_h : float
            Slab thickness.

        Notes
        -----
        It is overwritten for eu_cdm design class with following changes:
        - Allows different constants.
        - It retrieves design concrete strength from concrete attributes.
        """
        # Unit conversions
        Md = self.pre_Md * kN * m
        # Emergent beam cases
        bool1 = self.typology == 2
        bool2 = self.exterior
        bool3 = self.stairs_wg != 0.0
        if bool1 or bool2 or bool3:
            # Set section breadth to minimum
            self.b = self.min_b
            # Compute height for economic section, assuming d = 0.1h
            mu_h = ((Md / (ECONOMIC_MU_EB * self.fcd * self.b))**0.5) / 0.9
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
                mu_h = ((Md / (ECONOMIC_MU_EB * self.fcd * self.b))**0.5) / 0.9
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
        """Verifies the beam section dimensions for design forces.

        TODO
        ----
        Add specific reference pages and equation numbers.
        """
        # Allowable shear stress that can be carried by the beam
        tau_max = np.interp(self.concrete.fck,
                            FCK_VECT, TAU_MAX_VECT)
        # Economic mu values (dimensionless)
        if self.typology == 1:
            mu_economic = ECONOMIC_MU_WB
        elif self.typology == 2:
            mu_economic = ECONOMIC_MU_EB
        # Distance from extreme compression fiber to centroid of longitudinal
        # tension reinforcement.
        d = 0.9 * self.h

        # Maximum of envelope forces
        max_shear = max(self.envelope_forces.V1, self.envelope_forces.V5,
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
        tau = max_shear / (self.b * d)  # for max. shear force
        mu = max_moment / (self.fcd * self.b * d**2)  # for max. bending moment
        if mu < mu_economic and tau < tau_max:
            self.ok = True  # Ok
        else:
            self.ok = False  # Not ok

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
        # Distance from extreme compression fiber to centroid of longitudinal
        # tension reinforcement.
        d = 0.9 * self.h
        # Dimensionless limit values
        mu_lim = 0.31  # mu limit defined in REBAP-83
        omega_lim = 0.41  # omega limit defined in REBAP-83
        # Design forces
        moment_pos = np.array([self.envelope_forces.M1_pos,
                               self.envelope_forces.M5_pos,
                               self.envelope_forces.M9_pos])
        moment_neg = np.array([self.envelope_forces.M1_neg,
                               self.envelope_forces.M5_neg,
                               self.envelope_forces.M9_neg])
        moment_neg = np.abs(moment_neg)
        # Reinforcement area computation for positive moment envelope (+)
        # REBAP pp. 33
        mu_pos = moment_pos / (self.fcd * self.b * d**2)
        # REBAP pp. 35, eq 11
        omega_pos_prime = (mu_pos - mu_lim) / (1 - (self.cover / (d)))
        # REBAP pp. 35, eq 10
        omega_pos_prime[mu_pos <= mu_lim] = 0
        # REBAP pp. 35, eq 11
        omega_pos = omega_lim + omega_pos_prime
        # REBAP pp. 35, eq 10
        omega_pos[mu_pos <= mu_lim] = (
            mu_pos[mu_pos <= mu_lim] * (1 + mu_pos[mu_pos <= mu_lim]))
        # Reinforcement area computation for negative moment envelope (-)
        # REBAP pp. 33
        mu_neg = moment_neg / (self.fcd * self.b * d**2)
        # REBAP pp. 35, eq 11
        omega_neg_prime = (mu_neg - mu_lim) / (1 - (self.cover / (d)))
        # REBAP pp. 35, eq 10
        omega_neg_prime[mu_neg <= mu_lim] = 0
        # REBAP pp. 35, eq 11
        omega_neg = omega_lim + omega_neg_prime
        # REBAP pp. 35, eq 10
        omega_neg[mu_neg <= mu_lim] = (
            mu_neg[mu_neg <= mu_lim] * (1 + mu_neg[mu_neg <= mu_lim]))
        # Prime is used for compression reinforcement.
        # It can be both at top and bottom due to seismic loading
        omega_pos = np.maximum(omega_pos, omega_neg_prime)
        omega_neg = np.maximum(omega_neg, omega_pos_prime)
        # Determine required reinforcement at top and bottom
        Asl_top = omega_neg * self.b * d * self.fcd / self.fsyd
        Asl_bot = omega_pos * self.b * d * self.fcd / self.fsyd
        # Check against minimum longitudinal reinforcement area
        Asl_min_top = self.rhol_min_tens * self.b * d  # REBAP 90.1
        Asl_min_bot = self.rhol_min_tens * self.b * d  # REBAP 90.1
        Asl_top = np.maximum(Asl_top, Asl_min_top)
        Asl_bot = np.maximum(Asl_bot, Asl_min_bot)
        # Save required longitudinal reinforcement area
        self.Asl_top_req = Asl_top
        self.Asl_bot_req = Asl_bot

    def compute_required_transverse_reinforcement(self) -> None:
        """Computes the required transverse reinforcement for design forces.

        Notes
        -----
        1. Required reinforcement is computed at different sections:
        start, mid, end.
        """
        # Allowable shear stress that can be carried by the beam
        tau_c = np.interp(self.concrete.fck, FCK_VECT, TAU_C_VECT)
        # Distance from extreme compression fiber to centroid of longitudinal
        # tension reinforcement.
        d = 0.9 * self.h
        # lever arm, i.e., distance between comp. and tens. forces
        z = 0.9 * d
        # Design forces
        shear = np.array([self.envelope_forces.V1,
                          self.envelope_forces.V5,
                          self.envelope_forces.V9])
        # REBAP 53.1 V < Vcd + Vwd
        Vcd = tau_c * self.b * d  # REBAP 53.2
        Ash_sbh = (shear - Vcd) / (z * self.fsyd)  # REBAP 53.3
        Ash_sbh_min = self.rhoh_min * self.b  # REBAP 94.2
        Ash_sbh = np.maximum(Ash_sbh, Ash_sbh_min)
        # Save required transverse reinforcement area to spacing ratio
        self.Ash_sbh_req = Ash_sbh
