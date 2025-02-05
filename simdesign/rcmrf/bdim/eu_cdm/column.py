"""
Specific routines for defining and designing eu_cdm columns.

Notes
-----
Methodology follows the case of DCM (REBAP-83) column design.
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
from typing import Tuple

# Imports from the design class (eu_cdm) library
from .materials import Steel, Concrete

# Imports from bdim base library
from ..baselib.column import ColumnBase

# Imports from units library
from ....utils.units import MPa, m

ECONOMIC_MU: float = 0.25
"""Maximum mu value considered for the economic column design."""
TAU_C_VECT = np.array(
    [0.5, 0.6, 0.65, 0.75, 0.85, 0.90, 1.00, 1.10, 1.15]) * MPa
"""Vector of allowable shear stresses that carried by the concrete or
vector of the design shear strength values of concrete."""
TAU_MAX_VECT = np.array([2.4, 3.2, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]) * MPa
"""Vector of allowable shear stresses that can be carried by
the beam section."""
FCK_VECT = np.array([12, 16, 20, 25, 30, 35, 40, 45, 50]) * MPa
"""Vector of characteristic concrete compressive strength values."""
MODULAR_RATIO = 15
"""Assumed steel to concrete elastic modular ratio for reinf. computation."""
BETA_FC_VECTOR = [1.00, 0.93, 0.88, 0.88, 0.93]
"""Stress block coefficients for different axial load ratio (in REBAP 1983)."""
NIU_VECTOR = [0.40, 0.50, 0.60, 0.70, 0.85]
"""Axial load ratio corresponding to each stress block coefficient."""


class Column(ColumnBase):
    """Column object for design class: eu_cdm.
    """
    steel: Steel
    """Steel material."""
    concrete: Concrete
    """Concrete material."""

    @property
    def rhol_max(self) -> float:
        """
        Returns
        -------
        float
            Maximum longitudinal reinforcement ratio.

        References
        ----------
        Article 121.2 REBAP 1983
        """
        return 0.04

    @property
    def rhol_min(self) -> float:
        """
        Returns
        -------
        float
            Minimum longitudinal reinforcement ratio.
        """
        return 0.01

    def predesign_section_dimensions(self) -> None:
        """Does preliminary design of column.

        This method makes initial guess for section dimensions.

        Notes
        -----
        It is overwritten for eu_cdm design class with following changes:
        - It retrieves design concrete strength from concrete attributes.
        """
        # Initial guess for column concrete area
        min_area = self.pre_Nd / self.fcd
        # Determine initial dimensions
        if self.section == 1:  # Square section
            self.bx = (min_area**0.5)
            self.by = (min_area**0.5)
        elif self.section == 2:  # Rectangular section
            if self.orient == 'x':  # Longer dimension is bx
                self.bx = (2*min_area)**0.5
                self.by = 0.5*self.bx
            elif self.orient == 'y':  # Longer dimension is by
                self.by = (2*min_area)**0.5
                self.bx = 0.5*self.by
        # Check against minimum dimensions
        self.bx = max(ceil(20*self.bx)/20, self.min_b)
        self.by = max(ceil(20*self.by)/20, self.min_b)

    def verify_section_adequacy(self) -> None:
        """Verifies the adequacy of section dimensions for design forces.

        TODO
        ----
        The original code does not enforce checks for axial load ratio.
        Is this correct? Maybe, we should add it.
        """
        # Distance of long. bars in tens. to extreme conc. fibers in compr.
        dx = 0.9 * self.bx
        dy = 0.9 * self.by
        # Max. normalised moment
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
        # Max. shear stress
        max_tau_x = max(
            self.envelope_forces.Vx1,
            self.envelope_forces.Vx9
        ) / (self.by * dx)
        max_tau_y = max(
            self.envelope_forces.Vy1,
            self.envelope_forces.Vy9
        ) / (self.bx * dy)

        # Allowable shear stress that can be carried by the beam
        tau_max = np.interp(self.concrete.fck_cube, FCK_VECT, TAU_MAX_VECT)
        # Verify the adequacy of the section dimensions
        if max_mu_y > ECONOMIC_MU or max_tau_x > tau_max:
            # Need to increase dimension parallel to global-x
            self.ok_x = False
        else:
            self.ok_x = True
        if max_mu_x > ECONOMIC_MU or max_tau_y > tau_max:
            # Need to increase dimension parallel to global-y
            self.ok_y = False
        else:
            self.ok_y = True

    def compute_required_longitudinal_reinforcement(self) -> None:
        """Computes the required longitudinal reinforcement for design forces.
        """
        # Initial longitudinal reinforcement area
        Aslx_req = 0.000226195 * m**2  # 2 bars with diam of 12mm
        Asly_req = 0.000226195 * m**2  # 2 bars with diam of 12mm
        for force in self.design_forces:
            # Dimensionless design force quantities
            niu_1 = (-1*force.N1) / (self.Ag * self.fcd)
            niu_9 = (-1*force.N9) / (self.Ag * self.fcd)
            mu_x1 = abs(force.Mx1) / ((self.bx * self.by**2) * self.fcd)
            mu_y1 = abs(force.My1) / ((self.by * self.bx**2) * self.fcd)
            mu_x9 = abs(force.Mx9) / ((self.bx * self.by**2) * self.fcd)
            mu_y9 = abs(force.My9) / ((self.by * self.bx**2) * self.fcd)
            # Determine the required longitudinal reinforcement ratio
            beta1 = np.interp(niu_1, NIU_VECTOR, BETA_FC_VECTOR)
            beta9 = np.interp(niu_9, NIU_VECTOR, BETA_FC_VECTOR)
            # TODO: Should we use cover here or assume ratio as 0.1?
            lambda_x = 0.5 - self.cover / self.bx
            lambda_y = 0.5 - self.cover / self.by
            niuc_1 = niu_1 - 0.85
            niuc_9 = niu_9 - 0.85
            # Start section
            if niu_1 < 0.0:  # Axial force is tensile
                # REBAP (1983), pp. 48, eqn. 22 (HMA)
                omega_x1 = mu_x1 / (lambda_y*beta1) - niu_1
                omega_y1 = mu_y1 / (lambda_x*beta1) - niu_1
            elif niu_1 <= 0.85:
                omega_x1 = (mu_x1 + 0.55*niu_1*niuc_1) / (lambda_y*beta1)
                omega_y1 = (mu_y1 + 0.55*niu_1*niuc_1) / (lambda_x*beta1)
            else:
                omega_x1 = mu_x1 / (lambda_y*beta1) + niuc_1
                omega_y1 = mu_y1 / (lambda_x*beta1) + niuc_1
            # End section
            if niu_9 < 0.0:  # Axial force is tensile
                # REBAP (1983), pp. 48, eqn. 22 (HMA)
                omega_x9 = mu_x9 / (lambda_y*beta9) - niu_9
                omega_y9 = mu_y9 / (lambda_x*beta9) - niu_9
            elif niu_9 <= 0.85:
                omega_x9 = (mu_x9 + 0.55*niu_9*niuc_9) / (lambda_y*beta9)
                omega_y9 = (mu_y9 + 0.55*niu_9*niuc_9) / (lambda_x*beta9)
            else:
                omega_x9 = mu_x9 / (lambda_y*beta9) + niuc_9
                omega_y9 = mu_y9 / (lambda_x*beta9) + niuc_9
            # Compute required reinforcement area on two sides
            omega_x = max(omega_x1, omega_x9)
            omega_y = max(omega_y1, omega_y9)
            Aslx = (0.5 * omega_x * self.Ag * self.fcd / self.fsyd)
            Asly = (0.5 * omega_y * self.Ag * self.fcd / self.fsyd)
            # Update the required reinforcement area
            Aslx_req = max(Aslx_req, Aslx)
            Asly_req = max(Asly_req, Asly)
        # Save the required longitudinal reinforcement area
        self.Aslx_req = Aslx_req
        self.Asly_req = Asly_req

    def compute_required_transverse_reinforcement(self) -> None:
        """Computes the required transverse reinforcement for design forces.
        """
        # Allowable shear stress that can be carried by the beam
        tau_c = np.interp(self.concrete.fck, FCK_VECT, TAU_C_VECT)
        # Initial transverse reinforcement area to spacing ratio
        Ashx_sh_req, Ashy_sh_req = self.__get_min_transv_reinf()
        for force in self.design_forces:
            # Distance of long. bars in tens. to extreme conc. fibers in compr.
            dx = 0.9 * self.bx
            dy = 0.9 * self.by
            # lever arm, i.e., distance between comp. and tens. forces
            zx = 0.9 * dx
            zy = 0.9 * dy
            # Design forces
            Vy1 = abs(force.Vy1)
            Vx1 = abs(force.Vx1)
            Vy9 = abs(force.Vy9)
            Vx9 = abs(force.Vx9)
            # Determine loading eccentricty
            ecc_x1 = force.My1 / force.N1
            ecc_x9 = force.My9 / force.N9
            ecc_y1 = force.Mx1 / force.N1
            ecc_y9 = force.Mx9 / force.N9
            # TO define big and small ecc. section for tensile force and
            # to discard concrete contribution for small eccentricity. (HMA)
            et_x1 = ecc_x1 / dx
            et_x9 = ecc_x9 / dx
            et_y1 = ecc_y1 / dy
            et_y9 = ecc_y9 / dy
            # Allowable shear force in concrete, assuming vertical stirrups
            Vcd_x = tau_c * self.by * dx  # REBAP-83, 53.3, 53.2 c)
            Vcd_y = tau_c * self.bx * dy  # REBAP-83, 53.3, 53.2 c)
            # Start section -X direction
            if force.N1 > 0 and abs(et_x1) < 0.5:
                # Tensile force with small ecc. (cracked concrete) (HMA)
                Ash_sh_x1 = Vx1 / (zx * self.fsyd)
            elif Vx1 > Vcd_x:
                Ash_sh_x1 = (Vx1 - Vcd_x) / (zx * self.fsyd)
            else:
                Ash_sh_x1 = 0.0
            # Start section -Y direction
            if force.N1 > 0 and abs(et_y1) < 0.5:
                # Tensile force with small ecc. (cracked concrete) (HMA)
                Ash_sh_y1 = Vy1 / (zy * self.fsyd)
            elif Vy1 > Vcd_y:
                Ash_sh_y1 = (Vy1 - Vcd_y) / (zy * self.fsyd)
            else:
                Ash_sh_y1 = 0.0
            # End section -X direction
            if force.N9 > 0 and abs(et_x9) < 0.5:
                # Tensile force with small ecc. (cracked concrete) (HMA)
                Ash_sh_x9 = Vx9 / (zx * self.fsyd)
            elif Vx9 > Vcd_x:
                Ash_sh_x9 = (Vx9 - Vcd_x) / (zx * self.fsyd)
            else:
                Ash_sh_x9 = 0.0
            # End section -Y direction
            if force.N9 > 0 and abs(et_y9) < 0.5:
                # Tensile force with small ecc. (cracked concrete) (HMA)
                Ash_sh_y9 = Vy9 / (zy * self.fsyd)
            elif Vy9 > Vcd_y:
                Ash_sh_y9 = (Vy9 - Vcd_y) / (zy * self.fsyd)
            else:
                Ash_sh_y9 = 0.0
            # Update the required reinforcement
            Ashx_sh_req = max(Ashx_sh_req, Ash_sh_x1, Ash_sh_x9)
            Ashy_sh_req = max(Ashy_sh_req, Ash_sh_y1, Ash_sh_y9)
        # Save the required transverse reinforcement area to spacing ratio
        self.Ashx_sbh_req = Ashx_sh_req
        self.Ashy_sbh_req = Ashy_sh_req

    def __get_min_transv_reinf(self) -> Tuple[float]:
        """Retrieves minimum transverse reinforcement.

        Returns
        -------
        Tuple[float]
            Transverse reinforcement area (along x and y axes)
            to spacing ratio.
        """
        if self.fsyd < 230 * MPa:
            Ashx_sh_min = 0.16 * self.bx / 100
            Ashy_sh_min = 0.16 * self.by / 100
        elif self.fsyd < 400 * MPa:
            Ashx_sh_min = 0.10 * self.bx / 100
            Ashy_sh_min = 0.10 * self.by / 100
        else:
            Ashx_sh_min = 0.08 * self.bx / 100
            Ashy_sh_min = 0.08 * self.by / 100

        return Ashx_sh_min, Ashy_sh_min
