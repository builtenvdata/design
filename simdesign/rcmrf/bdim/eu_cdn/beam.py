"""
Specific routines for defining and designing eu_cdn beams.

Methodology follows the case of DCL1 (REBAP-83) beam design.
Design based on working stress method.

References
----------
RBA (1935) Regulamento para o Emprego de Betão Armado. Decreto-Lei N.° 4036,
Lisbon, Portugal.
RSCCS (1958) Regulamento de Segurança das Construções contra os Sismos.
Decreto-Lei N.° 41658, Lisbon, Portugal.
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

# Imports from the design class (eu_cdn) library
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
TAU_C = 0.40 * MPa
"""Allowable shear stress carried by the concrete or
the design shear strength of concrete."""
TAU_MAX = 1.40 * MPa
"""Allowable shear stress carried by the beam section."""
MODULAR_RATIO = 15
"""Assumed steel to concrete elastic modular ratio for reinf. computation."""


class Beam(BeamBase):
    """Beam object for design class: eu_cdn.
    """
    steel: Steel
    """Steel material."""
    concrete: Concrete
    """Concrete material."""

    def predesign_section_dimensions(self, slab_h: float) -> None:
        """Makes preliminary design of beam.

        This method makes initial guess for section dimensions.

        Parameters
        ----------
        columns : List[ColumnBase]
            Columns connected to beam end nodes.
        slab_h : float
            Slab thickness.

        Notes
        -----
        It is overwritten for eu_cdn design class with following changes:
        - Allows different constants.
        - It retrieves design concrete strength from concrete attributes.
        - It uses a single expression for computing height to control emergent
        beam deformations `def_h` under gravity loads.
        """
        # Bending moment used for preliminary design of section dimensions
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
        # Distance from extreme compression fiber to centroid of longitudinal
        # tension reinforcement.
        d = 0.9 * self.h
        # Lever arm, i.e., distance between comp. and tens. forces
        z = 0.9 * d
        # Verify the adequacy of the section dimensions
        shear = max(self.envelope_forces.V1,
                    self.envelope_forces.V5,
                    self.envelope_forces.V9)
        tau = shear / (self.b * z)
        if tau < TAU_MAX:
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

        TODO
        ----
        Add specific reference pages and equation numbers.
        """
        # Distance from extreme compression fiber to centroid of longitudinal
        # tension reinforcement.
        d = 0.9 * self.h
        d_prime = 0.1 * self.h
        # TODO: Alternatively, this can be directly computed.
        n = MODULAR_RATIO  # Modular ratio
        # Design forces
        moment_pos = np.array([self.envelope_forces.M1_pos,
                               self.envelope_forces.M5_pos,
                               self.envelope_forces.M9_pos])
        moment_neg = np.array([self.envelope_forces.M1_neg,
                               self.envelope_forces.M5_neg,
                               self.envelope_forces.M9_neg])
        moment_neg = np.abs(moment_neg)  # No need for the sign
        # Balanced moment capacity
        x_bal = (self.fcd * d) / (self.fcd + self.fsyd / n)
        C_bal = 0.50 * self.fcd * self.b * x_bal
        M_bal = C_bal * (d - x_bal / 3)
        # Initialize long. steel area at start, mid and end sections
        Asl_top = np.zeros(3)  # Required steel area at top
        Asl_bot = np.zeros(3)  # Required steel area at bottom
        # 1) Calculate longitudinal steel area for negative moment envelope (-)
        mask1 = moment_neg <= M_bal  # Identify singly reinforced beams
        # Excessive moment (doubly reinforced beam case)
        Mexcess = moment_neg[~mask1] - M_bal
        # Tension reinforcement (singly reinforced beam)
        Asl_top[mask1] = moment_neg[mask1] / (
            self.fsyd * (d - x_bal / 3))
        # As1 (Doubly reinforced beam)
        Asl1 = moment_neg[~mask1] / (self.fsyd * (d - x_bal / 3))
        # As2 (doubly reinforced beam) --> Corrected
        Asl2 = Mexcess / (self.fsyd * (d - d_prime))
        # Total tension reinforcement reinforcement (doubly reinforced beam)
        Asl_top[~mask1] = Asl1 + Asl2
        # Maximum stress of the compression reinforcement (doubly reinforced)
        fsyd_prime = min(self.fsyd,
                         (2*self.fsyd*(x_bal - d_prime)) / (d - x_bal))
        # Compression reinforcement (doubly reinforced beam)
        Asl_bot[~mask1] = (2 * n * Mexcess) / (
            fsyd_prime * (2*n - 1) * (d - d_prime))

        # 2) Calculate longitudinal steel area for positive moment envelope (+)
        mask2 = moment_pos <= M_bal  # Identify singly reinforced beams
        # Excessive moment (doubly reinforced beam case)
        Mexcess = moment_pos[~mask2] - M_bal
        # Tension reinforcement (singly reinforced beam)
        Asl_bot[mask2] = np.maximum(
            Asl_bot[mask2],
            moment_pos[mask2] / (self.fsyd * (d - x_bal / 3))
            )
        # As1 (doubly reinforced beam)
        Asl1 = moment_pos[~mask2] / (self.fsyd * (d - x_bal / 3))
        # As2 (doubly reinforced beam) --> Corrected
        Asl2 = Mexcess / (self.fsyd * (d - d_prime))
        # Total tension reinforcement reinforcement (doubly reinforced beam)
        Asl_bot[~mask2] = np.maximum(Asl1 + Asl2, Asl_bot[~mask2])
        # Maximum stress of the compression reinforcement (doubly reinforced)
        fsyd_prime = min(self.fsyd,
                         (2*self.fsyd*(x_bal - d_prime)) / (d - x_bal))
        # Compression reinforcement (doubly reinforced beam)
        Asl_top[~mask2] = np.maximum(
            (2*n*Mexcess) / (fsyd_prime * (2*n - 1) * (d - d_prime)),
            Asl_top[~mask2])
        # Save the required longitudinal reinforcement area
        self.Asl_top_req = Asl_top
        self.Asl_bot_req = Asl_bot

    def compute_required_transverse_reinforcement(self) -> None:
        """Computes the required transverse reinforcement for design forces.

        Notes
        -----
        1. Required reinforcement is computed at different sections:
        start, mid, end.
        """
        # Distance from extreme compression fiber to centroid of longitudinal
        # tension reinforcement.
        d = 0.9 * self.h
        # Design forces
        shear = np.array([self.envelope_forces.V1,
                          self.envelope_forces.V5,
                          self.envelope_forces.V9])
        # Calculate the required transverse reinforcement area to the spacing
        sbh = 0.5  # stirrup spacing
        dbh = 0.006  # stirrup diameter
        nlegs = 2  # number of legs
        Ash_sbh_min = nlegs * (np.pi * 0.25 * dbh**2) / sbh
        Vrd = TAU_C * self.b * d
        mask = shear > Vrd
        Ash_sbh = np.ones_like(shear) * Ash_sbh_min
        Ash_sbh[mask] = np.maximum(shear[mask] / (self.fsyd*d), Ash_sbh[mask])
        self.Ash_sbh_req = Ash_sbh  # Save
