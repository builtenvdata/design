"""
Specific routines for defining and designing eu_cdh columns.

Notes
-----
Design based on limit state design.
Material qualities are higher compared CDM.

References
----------
CEN (2004) Eurocode 2: Design of concrete structures - Part 1-1:
General rules and rules for buildings. Brussels, Belgium
CEN (2004) Eurocode 8: Design of structures for earthquake resistance - Part 1:
General rules, seismic actions and rules for buildings. Brussels, Belgium
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

# Imports from the design class (eu_cdh) library
from .materials import Steel, Concrete

# Imports from bdim base library
from ..baselib.column import ColumnBase

# Imports from units library
from ....utils.units import MPa, m

# Constants
ECONOMIC_MU: float = 0.25
"""Maximum mu value considered for the economic column design."""
MAX_NIU = 0.55
"""Maximum allowed value of axial load ratio.
0.65 according to Eurocode 8 - Part 1: 5.4.3.2.1(3)P
0.55 according to Eurocode 8 - Part 1: 5.5.3.2.1(3)P
"""
BETA_FC_VECTOR = [1.00, 0.93, 0.88, 0.88, 0.93]
"""Stress block coefficients for different axial load ratio (in REBAP 1983)."""
NIU_VECTOR = [0.40, 0.50, 0.60, 0.70, 0.85]
"""Axial load ratio corresponding to each stress block coefficient."""


class Column(ColumnBase):
    """Column object for design class: eu_cdh.
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
        EN 1992-1-1:2004 9.5.2(3)
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
        min_tensile_force = min(
            self.envelope_forces.N1_pos,
            self.envelope_forces.N9_pos,
        )
        if min_tensile_force > 0.0:  # Tensile axial force
            Ned = 0.0
        else:  # Compressive axial force
            Ned = min(
                abs(self.envelope_forces.N1_neg),
                abs(self.envelope_forces.N9_neg),
            )
        # EN 1992-1-1:2004 9.5.2(2)
        rhol_min_ec2 = max(0.1*Ned/self.fsyd, 0.002*self.Ag) / self.Ag
        # 0.01 is introduced as a rule of thumb from practical point.
        # It is not a code requirement.
        return max(0.01, rhol_min_ec2)

    @property
    def rhoh_min(self) -> float:
        """
        Returns
        -------
        float
            Minimum transverse reinforcement ratio.

        Notes
        -----
        The equation used herein is originally defined for beams.
        We keep using it for columns just to ensure safety.
        """
        # EN 1992-1-1:2004, 9.2.2(5), Eqn. 9.5N
        return 0.08 * ((self.fck/MPa)**0.5) / (self.fsyk/MPa)

    def predesign_section_dimensions(self) -> None:
        """Does preliminary design of column.

        This method makes initial guess for section dimensions.

        Notes
        -----
        It is overwritten for eu_cdh design class with following changes:
        - It retrieves design concrete strength from concrete attributes.
        - Eurocode enforces checks for axial load ratio which was missing in
        the original code. This, is now added.
        """
        # Initial guess for column concrete area
        min_area = self.pre_Nd / (self.fcd * MAX_NIU)
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

        Notes
        -----
        - Eurocode enforces checks for axial load ratio which was missing in
        the original code. This is now added.
        - In accordance with EN 1992-1-1:2004 5.4.3.2.1(2) biaxial bending
        is taken into account by decreasing the uniaxial moment of resistance
        or increasing the demand by 30%.
        """
        # Distance from extreme compression fiber to centroid of longitudinal
        # tension reinforcement.
        dx = 0.9 * self.bx
        dy = 0.9 * self.by
        # Following EC2-1/6.2.3: Members with vertical shear reinforcement
        # Strength reduction factor for concrete cracked in shear
        v = 0.6 * (1 - self.fck / (250*MPa))  # Eqn 6.6N
        if self.fsyd / self.fsyk >= 0.80:
            v1 = v  # Note 1: Recommended strength reduction factor
        else:  # Note 2: If fsyd is below 80% of fsyk
            if self.fck <= 60 * MPa:
                v1 = 0.6
            else:
                v1 = max(0.6 * (1 - self.fck / (200*MPa)), 0.5)
        # Coefficient taking account the stress state in the comp. chord
        alpha_cw = 1.0  # assuming no axial force (tension case), eqn. 6.11aN
        # Angle between the conc. comp. strut and the beam axis perp. to shear
        theta = 21.80140948635181  # in degrees, based on eqn. 6.7N
        theta = 45  # in degrees, based on eqn. 6.7N
        tan_theta = np.tan(theta*np.pi/180)  # 0.4 - 1.0
        cot_theta = 1/tan_theta  # 1.0 - 2.5
        # lever arm, i.e., distance between comp. and tens. forces
        zx = 0.9*dx
        zy = 0.9*dy
        # Assuming vertical shear reinforcement is provided: Eqn. 6.9
        Vrdx = (alpha_cw*self.by*zx*v1*self.fcd) / (cot_theta+tan_theta)
        Vrdy = (alpha_cw*self.bx*zy*v1*self.fcd) / (cot_theta+tan_theta)

        # Maximum axial load ratio
        max_niu = max(
            self.envelope_forces.N1_pos,
            self.envelope_forces.N9_pos,
            abs(self.envelope_forces.N1_neg),
            abs(self.envelope_forces.N9_neg),
        ) / (self.Ag * self.fcd)
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
        max_Vx = max(
            self.envelope_forces.Vx1,
            self.envelope_forces.Vx9
        )
        max_Vy = max(
            self.envelope_forces.Vy1,
            self.envelope_forces.Vy9
        )

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
        """Computes the required longitudinal reinforcement for design forces.

        Notes
        -----
        - In accordance with EN 1992-1-1:2004 5.4.3.2.1(2) biaxial bending
        is taken into account by decreasing the uniaxial moment of resistance
        or increasing the demand by 30%.
        """
        # Initial longitudinal reinforcement area
        Aslx_req = 2*np.pi*0.25*((0.012*m)**2)  # Minimum reinforcement
        Asly_req = 2*np.pi*0.25*((0.012*m)**2)  # Minimum reinforcement
        for force in self.design_forces:
            # Dimensionless design force quantities
            niu_1 = (-1*force.N1) / (self.Ag * self.fcd)
            niu_9 = (-1*force.N9) / (self.Ag * self.fcd)
            mu_x1 = abs(force.Mx1) / ((self.bx * self.by**2) * self.fcd) / 0.7
            mu_y1 = abs(force.My1) / ((self.by * self.bx**2) * self.fcd) / 0.7
            mu_x9 = abs(force.Mx9) / ((self.bx * self.by**2) * self.fcd) / 0.7
            mu_y9 = abs(force.My9) / ((self.by * self.bx**2) * self.fcd) / 0.7
            # Determine the required longitudinal reinforcement ratio
            beta1 = np.interp(niu_1, NIU_VECTOR, BETA_FC_VECTOR)
            beta9 = np.interp(niu_9, NIU_VECTOR, BETA_FC_VECTOR)
            lambda_y = 0.5 - self.cover / self.bx
            lambda_x = 0.5 - self.cover / self.by
            niuc_1 = niu_1 - 0.85
            niuc_9 = niu_9 - 0.85
            # Start section
            if niu_1 < 0.0:  # Axial force is tensile
                # REBAP (1983), pp. 48, eqn. 22 (HMA)
                omega_x1 = mu_x1 / (lambda_x*beta1) - niu_1
                omega_y1 = mu_y1 / (lambda_y*beta1) - niu_1
            elif niu_1 <= 0.85:
                omega_x1 = (mu_x1 + 0.55*niu_1*niuc_1) / (lambda_x*beta1)
                omega_y1 = (mu_y1 + 0.55*niu_1*niuc_1) / (lambda_y*beta1)
            else:
                omega_x1 = mu_x1 / (lambda_x*beta1) + niuc_1
                omega_y1 = mu_y1 / (lambda_y*beta1) + niuc_1
            # End section
            if niu_9 < 0.0:  # Axial force is tensile
                # REBAP (1983), pp. 48, eqn. 22 (HMA)
                omega_x9 = mu_x9 / (lambda_x*beta9) - niu_9
                omega_y9 = mu_y9 / (lambda_y*beta9) - niu_9
            elif niu_9 <= 0.85:
                omega_x9 = (mu_x9 + 0.55*niu_9*niuc_9) / (lambda_x*beta9)
                omega_y9 = (mu_y9 + 0.55*niu_9*niuc_9) / (lambda_y*beta9)
            else:
                omega_x9 = mu_x9 / (lambda_x*beta9) + niuc_9
                omega_y9 = mu_y9 / (lambda_y*beta9) + niuc_9
            # Compute required reinforcement area on two sides
            omega_x = max(omega_x1, omega_x9)
            omega_y = max(omega_y1, omega_y9)
            Aslx = (0.5 * omega_x * self.Ag * self.fcd / self.fsyd)
            Asly = (0.5 * omega_y * self.Ag * self.fcd / self.fsyd)
            # Update the reinforcement area
            Aslx_req = max(Aslx_req, Aslx)
            Asly_req = max(Asly_req, Asly)
        # Save the required longitudinal reinforcement area
        # on each side, along x and y axes
        self.Aslx_req = Aslx_req
        self.Asly_req = Asly_req

    def compute_required_transverse_reinforcement(self) -> None:
        """Computes the required transverse reinforcement for design forces.
        """
        # Distance of long. bars in tens. to extreme conc. fibers in compr.
        dx = 0.9 * self.bx
        dy = 0.9 * self.by
        # lever arm, i.e., distance between comp. and tens. forces
        zx = 0.9 * dx
        zy = 0.9 * dy
        # Compression strut angle, EN 1992-1-1:2004 eqn. 6.7N
        """TODO: This could 2.0 for both beams and columns.
        1.0 is not ralistic (too conservative)."""
        cot_theta = 1.0  # 45 degrees
        # Initial transverse reinforcement area to spacing ratio
        Ashx_sh_min = self.rhoh_min * self.by
        Ashy_sh_min = self.rhoh_min * self.bx
        # Design forces
        Ved_x = max(self.envelope_forces.Vx1, self.envelope_forces.Vx9)
        Ved_y = max(self.envelope_forces.Vy1, self.envelope_forces.Vy9)
        # EN 1992-1-1:2004 6.2.3(3) eqn. 6.8
        Ashx_sh = Ved_x / (zx * self.fsyd * cot_theta)
        Ashy_sh = Ved_y / (zy * self.fsyd * cot_theta)
        # Save the required ratio of transverse reinforcement area along
        # x and y axes to the reinforcement spacing
        self.Ashx_sbh_req = max(Ashx_sh_min, Ashx_sh)
        self.Ashy_sbh_req = max(Ashy_sh_min, Ashy_sh)

    def check_local_ductility_requirement(self) -> None:
        """Checks local ductility requirement for column.

        TODO
        ----
        INCOMPLETE !
        Compute bi values correctly.
        Come up with strategy to change transverse reinforcement.
        1. First add more stirrup legs,
        2. Then, decrease spacing,
        3. Then, go back to iterations.

        Notes
        -----
        Use DCM multi-storey frame for behaviour factor.
        Assume T1>Tc
        """
        # alpha_u and alpha_1 ratio, EN 1998-1:2004 5.2.2.2(5)
        alpha_u_1_rat = 1.3  # Multi-storey, multi-bay frame
        # Behaviour factor, q0, EN 1998-1:2004 5.2.2.2(2)
        q0 = 3.0 * alpha_u_1_rat  # DCM frame
        # EN 1998-1:2004 5.2.3.4(3)
        curv_duct = 2*q0 - 1  # Assuming T1>Tc, use eqn. 5.4
        # Check local ductility requirement in EN 1998-1: 2004, eqn. 5.15
        b0_x = self.bx - 2*self.cover - self.dbh
        nx = self.nbh_x - 1
        bi_x = b0_x / nx
        b0_y = self.by - 2*self.cover - self.dbh
        ny = self.nbh_y - 1
        bi_y = b0_y / ny
        # eqn. 5.16a
        alpha_n = 1 - (2*nx*bi_x**2 + 2*ny*bi_y**2) / (6*b0_x*b0_y)
        # eqn. 5.16b
        alpha_s = (1-self.sbh/(2*b0_x)) * (1-self.sbh/(2*b0_y))
        alpha = alpha_n * alpha_s
        omega_wd_x = self.rhoh_x * (self.fsyd/self.fcd)
        omega_wd_y = self.rhoh_y * (self.fsyd/self.fcd)
        alpha_omega_x = alpha * omega_wd_x
        alpha_omega_y = alpha * omega_wd_y
        epsyd = self.fsyd / self.Es
        max_local_curv_duct_x = 0.0
        max_local_curv_duct_y = 0.0
        for factors in self.seism_comb_grav_facts:
            forces = factors['G'] * self.forces['G/seismic'] + \
                factors['Q'] * self.forces['Q/seismic']
            niu_d = -forces.N1 / (self.Ag * self.fcd)
            tmp_x = 2 * (alpha_omega_x+0.035) / (
                30*niu_d*epsyd*(self.by / b0_y))
            tmp_y = 2 * (alpha_omega_y+0.035) / (
                30*niu_d*epsyd*(self.bx / b0_x))
            max_local_curv_duct_x = max(max_local_curv_duct_x, tmp_x)
            max_local_curv_duct_y = max(max_local_curv_duct_y, tmp_y)

        # Should we increase shear reinforcement instead?
        if curv_duct > max_local_curv_duct_x:
            self.ok_y = False
        if curv_duct > max_local_curv_duct_y:
            self.ok_x = False
