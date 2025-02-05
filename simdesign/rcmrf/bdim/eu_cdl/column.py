"""
Specific routines for defining and designing eu_cdl columns.

TODO
----
Discuss the default constants.
See specific lines with TODOs.
Add specific reference pages for design equations.

Notes
-----
Design based on working stress method.
Material qualities are higher compared CDN.
--> REBA is the French book followed by the most of EUROPE in that time
Seismic loading is considered with q=1.0, 1.0 DEAD + 1.0 LIVE

References
----------
RSCCS (1958) Regulamento de Segurança das Construções contra os Sismos.
Decreto-Lei N.° 41658, Lisbon, Portugal
André Guerrin (1966) Traité de béton armé. Dunod, Paris.
REBA (1967) Regulamento de Estruturas de Betão Armado. Lisbon, Portugal.
d'Arga e Lima, J., Monteiro V, Mun M (2005) Betão armado: esforços normais e
de flexão: REBAP-83. Laboratório Nacional de Engenharia Civil, Lisboa.
"""

# Imports from installed packages
from math import ceil
import numpy as np
from typing import Tuple
from scipy.interpolate import RegularGridInterpolator

# Imports from the design class (eu_cdl) library
from .materials import Steel, Concrete

# Imports from bdim base library
from ..baselib.column import ColumnBase

# Imports from units library
from ....utils.units import MPa

# CONSTANTS
ECONOMIC_MU = 0.25
"""Maximum mu value considered for the economic column design."""
TAU_C_VECT = np.array([0.4, 0.45, 0.50, 0.55, 0.60]) * MPa
"""Vector of allowable shear stresses that carried by the concrete or
vector of the design shear strength values of concrete."""
TAU_MAX_VECT = np.array([2.4, 2.7, 3.0, 3.3, 3.6]) * MPa
"""Vector of allowable shear stresses that can be carried by
the beam section."""
FCK_CUBE_VECT = np.array([180, 225, 300, 350, 400])
"""Vector of cubic concrete compressive strength values (kg/cm2)."""
MODULAR_RATIO = 15
"""Assumed steel to concrete elastic modular ratio for reinf. computation."""
ABACUS_MU = np.array([
    0.0, 0.0277777777777778, 0.0555555555555556, 0.0833333333333333,
    0.111111111111111, 0.138888888888889, 0.166666666666667,
    0.194444444444444, 0.222222222222222, 0.250000000000000
    ])
ABACUS_NIU = np.array([
    0.0, 0.0777777777777778, 0.155555555555556, 0.233333333333333,
    0.311111111111111, 0.388888888888889, 0.466666666666667,
    0.544444444444444, 0.622222222222222, 0.700000000000000])
ABACUS_RHOL = np.array([
    [0.0, 0.00970555555555555, 0.0194111111111111, 0.0291166666666667,
     0.0440915555555555, 0.0702232222222222, 0.102243666666667,
     0.131266888888889, 0.164154666666667, 0.198892000000000],
    [0.0, 0.0102261111111111, 0.0205228888888889, 0.0309256666666667,
     0.0472451111111111, 0.0758481111111111, 0.108280777777778,
     0.141384444444444, 0.178964000000000, 0.217524333333333],
    [0.0, 0.0100394444444444, 0.0200788888888889, 0.0301183333333333,
     0.0487321111111111, 0.0823443333333333, 0.117531222222222,
     0.155449111111111, 0.195662444444444, 0.236222222222222],
    [0, 0.00899250000000000, 0.0164730000000000, 0.0235755000000000,
     0.0437693333333333, 0.0865265555555556, 0.127303000000000,
     0.170060666666667, 0.213891555555556, 0.257134666666667],
    [0.0, 0.00529166666666667, 0.0105833333333333, 0.0155798888888889,
     0.0384402222222222, 0.0905643333333333, 0.137157222222222,
     0.185445111111111, 0.232910444444444, 0.279392888888889],
    [0.0, 0.00386794444444444, 0.00794322222222222, 0.0120185000000000,
     0.0384363333333333, 0.0967137777777778, 0.150187333333333,
     0.203398333333333, 0.253433222222222, 0.299813444444444],
    [0.0, 0.00610583333333333, 0.0122116666666667, 0.0204363333333333,
     0.0506684444444444, 0.110025777777778, 0.166942333333333,
     0.220166777777778, 0.271086333333333, 0.315488333333333],
    [0.0, 0.0122712222222222, 0.0262984444444444, 0.0403256666666666,
     0.0718958888888889, 0.129945222222222, 0.186308666666667,
     0.238572111111111, 0.289164000000000, 0.332430555555556],
    [0.0, 0.0195072222222222, 0.0390144444444444, 0.0639063888888889,
     0.100675333333333, 0.156645555555556, 0.210372888888889,
     0.260533555555556, 0.312908111111111, 0.359491777777778],
    [0.0, 0.0309847222222222, 0.0619694444444444, 0.0929541666666667,
     0.132961000000000, 0.185786555555556, 0.239298333333333,
     0.283691888888889, 0.338197000000000, 0.387725000000000]
          ]) / MODULAR_RATIO
# Interpolator used for retrieving the required column long. reinf. ratio
# NOTE: The values outside the domain are extrapolated
rho_interpolator = RegularGridInterpolator(
    (ABACUS_MU, ABACUS_NIU), ABACUS_RHOL.T,
    method='linear', bounds_error=False, fill_value=None)


def get_rhol(niu: float, mu_x: float, mu_y: float,
             fcd: float, fsyd: float) -> Tuple[float, float]:
    """ Computes required reinforcement ratio for given dimensionless forces.

    Parameters
    ----------
    niu : float
        Normalized axial load or axial load ratio.
    mu_x : float
        Normalized moment around x-axis.
    mu_y : float
        Normalized moment around y-axis.
    fcd : float
        Design concrete compressive strength.
    fsyd : float
        Design yield steel strength.

    Returns
    -------
    Tuple[float, float]
        Required reinforcement ratio around x and y axes.

    References
    ----------
    Traité de béton armé by A Guerrin, Dunod, Paris, 1966. pp 146
    """
    if niu < 0.0:  # for tensile force
        rhol_xm = rho_interpolator((mu_x, 0.001))
        rhol_ym = rho_interpolator((mu_y, 0.001))
        # 0.50 bcs it will be uniformally distributed over the cross-section
        rhol_x = rhol_xm - 0.5 * niu * fcd / fsyd
        rhol_y = rhol_ym - 0.5 * niu * fcd / fsyd
    else:
        rhol_x = rho_interpolator((mu_x, niu))
        rhol_y = rho_interpolator((mu_y, niu))

    return rhol_x, rhol_y


class Column(ColumnBase):
    """Column object for design class: eu_cdl.
    """
    steel: Steel
    """Steel material."""
    concrete: Concrete
    """Concrete material."""

    @property
    def fcd_eq(self) -> float:
        """
        Returns
        -------
        float
            Seismic design concrete compressive strength (in base units).
        """
        return self.concrete.fcd_eq * MPa

    @property
    def fsyd_eq(self) -> float:
        """
        Returns
        -------
        float
            Seismic design steel yield strength (in base units).
        """
        return self.steel.fsyd_eq * MPa

    @property
    def rhol_max(self) -> float:
        """
        Returns
        -------
        float
            Maximum longitudinal reinforcement ratio.
        """
        if self.concrete.fck_cube <= 180:
            return 0.03
        elif 180 < self.concrete.fck_cube <= 225:
            return 0.04
        elif 225 < self.concrete.fck_cube <= 300:
            return 0.05
        elif 300 < self.concrete.fck_cube:
            return 0.06

    @property
    def rhol_min(self) -> float:
        """
        Returns
        -------
        float
            Minimum longitudinal reinforcement ratio.

        References
        ----------
        REBA (1967) Regulamento de Estruturas de Betão Armado. Lisbon, Portugal
        """
        # Assuming the area of core concrete = 80% total area of the section
        return 0.01 * 0.66

    def predesign_section_dimensions(self) -> None:
        """Does preliminary design of column.

        This method makes initial guess for section dimensions.

        Notes
        -----
        It is overwritten for eu_cdl design class with following changes:
        - It retrieves design concrete strength from concrete attributes.
        - In case of the rectangular sections, the longer dimension does no
        longer need to be twice of shorter one.

        TODO
        ----
        Axial load ratio restriction?
        """
        # Initial guess for column concrete area
        min_area = self.pre_Nd / self.fcd
        # Determine initial dimensions
        if self.section == 1:  # Square section
            self.bx = (min_area**0.5)
            self.by = (min_area**0.5)
        elif self.section == 2:  # Rectangular section
            if self.orient == 'x':  # Longer dimension is bx
                self.by = self.min_b
                self.bx = min_area/self.min_b
            elif self.orient == 'y':  # Longer dimension is by
                self.bx = self.min_b
                self.by = min_area/self.min_b
        # Check against minimum dimensions
        self.bx = max(ceil(20*self.bx)/20, self.min_b)
        self.by = max(ceil(20*self.by)/20, self.min_b)

    def apply_section_compatibility(self) -> None:
        """Modifies the section dimensions for square section compatibility.

        This method is used in design iterations while increasing section
        dimensions.

        Notes
        -----
        It is overwritten for eu_cdl design class with following changes:
        - In case of the rectangular sections, the longer dimension does no
        longer need to be twice of shorter one.
        """
        if self.section == 1:  # Square section
            # Make both dimensions equal to their maximum
            self.bx = ceil(20*max(self.bx, self.by)) / 20
            self.by = ceil(20*max(self.bx, self.by)) / 20
        elif self.section == 2:  # Rectangular section
            pass

    def verify_section_adequacy(self) -> None:
        """Verifies the adequacy of section dimensions for design forces.

        TODO
        ----
        The original code does not enforce checks for axial load ratio.
        Moreover, although it is not checked the given code snippet
        use axial load ratio for tension only.
        Is this correct?
        """
        # Distance of long. bars in tens. to extreme conc. fibers in compr.
        dx = 0.9 * self.bx
        dy = 0.9 * self.by
        # lever arm, i.e., distance between comp. and tens. forces
        zx = 0.9 * dx
        zy = 0.9 * dy
        # Variables considered for section adequacy checks.
        max_niu = 0.0
        max_mu_x = 0.0
        max_mu_y = 0.0
        max_tau_x = 0.0
        max_tau_y = 0.0
        # fc to use for calculations
        fc_map = {'gravity': self.fcd,
                  'seismic': self.fcd_eq}
        for force in self.design_forces:
            # Other force related quantities (normalized)
            fc = fc_map.get(force.case)
            niu_1 = abs(force.N1 / (self.Ag * fc))
            niu_9 = abs(force.N9 / (self.Ag * fc))
            mu_x1 = abs(force.Mx1 / ((self.bx * self.by**2) * fc))
            mu_y1 = abs(force.My1 / ((self.by * self.bx**2) * fc))
            mu_x9 = abs(force.Mx9 / ((self.bx * self.by**2) * fc))
            mu_y9 = abs(force.My9 / ((self.by * self.bx**2) * fc))
            tau_x1 = abs(force.Vx1 / (self.by * zx))
            tau_y1 = abs(force.Vy1 / (self.bx * zy))
            tau_x9 = abs(force.Vx9 / (self.by * zx))
            tau_y9 = abs(force.Vy9 / (self.bx * zy))
            # update max values
            max_niu = max(max_niu, niu_1, niu_9)
            max_mu_x = max(max_mu_x, mu_x1, mu_x9)
            max_mu_y = max(max_mu_y, mu_y1, mu_y9)
            max_tau_x = max(max_tau_x, tau_x1, tau_x9)
            max_tau_y = max(max_tau_y, tau_y1, tau_y9)

        # Allowable shear stress that can be carried by the beam
        tau_max = np.interp(self.concrete.fck_cube,
                            FCK_CUBE_VECT, TAU_MAX_VECT)
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
        # if max_niu > 0.5 and self.ok_x and self.ok_y:
        #     # May increase both dimensions or random one?
        #     self.ok_x = False
        #     self.ok_y = False

    def compute_required_longitudinal_reinforcement(self) -> None:
        """Computes the required longitudinal reinforcement for design forces.
        """
        # fc and fsy to use for calculations
        fc_map = {'gravity': self.fcd,
                  'seismic': self.fcd_eq}
        fsy_map = {'gravity': self.fsyd,
                   'seismic': self.fsyd_eq}
        # Initial longitudinal reinforcement area
        Aslx_req = 0.0
        Asly_req = 0.0
        for force in self.design_forces:
            # Design strength values considered for this combo
            fc = fc_map.get(force.case)
            fsy = fsy_map.get(force.case)
            # Dimensionless design force quantities
            niu_1 = (-1*force.N1) / (self.Ag * fc)
            niu_9 = (-1*force.N9) / (self.Ag * fc)
            mu_x1 = abs(force.Mx1) / ((self.bx * self.by**2) * fc)
            mu_y1 = abs(force.My1) / ((self.by * self.bx**2) * fc)
            mu_x9 = abs(force.Mx9) / ((self.bx * self.by**2) * fc)
            mu_y9 = abs(force.My9) / ((self.by * self.bx**2) * fc)
            # Determine the required longitudinal reinforcement ratio
            rhol_x1, rhol_y1 = get_rhol(niu_1, mu_x1, mu_y1, fc, fsy)
            rhol_x9, rhol_y9 = get_rhol(niu_9, mu_x9, mu_y9, fc, fsy)
            rhol_x = max(rhol_x1, rhol_x9)
            rhol_y = max(rhol_y1, rhol_y9)
            Aslx = 0.5*rhol_x*self.Ag
            Asly = 0.5*rhol_y*self.Ag
            # Update the required area based on maximum
            Aslx_req = max(Aslx_req, Aslx)
            Asly_req = max(Asly_req, Asly)
        # Save the required longitudinal reinforcement area
        self.Aslx_req = Aslx_req
        self.Asly_req = Asly_req

    def compute_required_transverse_reinforcement(self) -> None:
        """Computes the required transverse reinforcement for design forces.
        """
        # fc to use for calculations
        fc_map = {'gravity': self.fcd,
                  'seismic': self.fcd_eq}
        fsy_map = {'gravity': self.fsyd,
                   'seismic': self.fsyd_eq}
        # Allowable shear stress that can be carried by the beam
        tau_c = np.interp(self.concrete.fck_cube, FCK_CUBE_VECT, TAU_C_VECT)
        # Initial transverse reinforcement area to spacing ratio
        Ashx_sh_req = 0.0  # along X
        Ashy_sh_req = 0.0  # along Y
        for force in self.design_forces:
            # Design strength values considered for this combo
            fc = fc_map.get(force.case)
            fsy = fsy_map.get(force.case)
            # Dimensionless design force quantities
            niu_1 = (-1*force.N1) / (self.Ag * fc)
            niu_9 = (-1*force.N9) / (self.Ag * fc)
            mu_x1 = abs(force.Mx1) / ((self.bx * self.by**2) * fc)
            mu_y1 = abs(force.My1) / ((self.by * self.bx**2) * fc)
            mu_x9 = abs(force.Mx9) / ((self.bx * self.by**2) * fc)
            mu_y9 = abs(force.My9) / ((self.by * self.bx**2) * fc)
            # Determine the required longitudinal reinforcement ratio
            rhol_x1, rhol_y1 = get_rhol(niu_1, mu_x1, mu_y1, fc, fsy)
            rhol_x9, rhol_y9 = get_rhol(niu_9, mu_x9, mu_y9, fc, fsy)
            rhol_x = max(rhol_x1, rhol_x9)
            rhol_y = max(rhol_y1, rhol_y9)
            Aslx = 0.5*rhol_x*self.Ag
            Asly = 0.5*rhol_y*self.Ag
            # TODO: Does this makes sense? Shouldn't we use the finalised long.
            # reinf. for the calculation of shear reinforcement?
            # Abl_cor = (np.pi * self.dbl_int**2) / 4
            # Abl_int = (np.pi * self.dbl_int**2) / 4
            # Aslx = self.nblx_int * Abl_int + 2 * Abl_cor
            # Asly = self.nbly_int * Abl_int + 2 * Abl_cor
            # Distance of long. bars in tens. to extreme conc. fibers in compr.
            dx = 0.9 * self.bx
            dy = 0.9 * self.by
            # Lever arms
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
            # To define big and small ecc. section for tensile force and
            # to discard concrete contribution for small eccentricity. (HMA)
            et_x1 = ecc_x1 / dx
            et_x9 = ecc_x9 / dx
            et_y1 = ecc_y1 / dy
            et_y9 = ecc_y9 / dy
            # Allowable shear force in concrete (tauc*b*0.9h)
            Vcd_x = tau_c * self.by * dx
            Vcd_y = tau_c * self.bx * dy
            # TODO: Calculations in the following should be checked
            # Start section -X direction
            if (
                Aslx * self.fsyd * zx < Vcd_x * dx or
                (force.N1 > 0 and abs(et_x1) < 0.5)
            ):
                Ash_sh_x1 = Vx1 / (zx * fsy)
            elif Vx1 > Vcd_x:
                Ash_sh_x1 = (Vx1 - Vcd_x) / (zx * fsy)
            else:
                Ash_sh_x1 = 0
            # Start section -Y direction
            if (
                Asly * self.fsyd * zy < Vcd_y * dy or
                (force.N1 > 0 and abs(et_y1) < 0.5)
            ):
                Ash_sh_y1 = Vy1 / (zy * fsy)
            elif Vy1 > Vcd_y:
                Ash_sh_y1 = (Vy1 - Vcd_y) / (zy * fsy)
            else:
                Ash_sh_y1 = 0
            # End section -X direction
            if (
                Aslx * self.fsyd * zx < Vcd_x * dx or
                (force.N9 > 0 and abs(et_x9) < 0.5)
            ):
                Ash_sh_x9 = Vx9 / (zx * fsy)
            elif Vx9 > Vcd_x:
                Ash_sh_x9 = (Vx9 - Vcd_x) / (zx * fsy)
            else:
                Ash_sh_x9 = 0
            # End section -Y direction
            if (
                Asly * self.fsyd * zy < Vcd_y * dy or
                (force.N9 > 0 and abs(et_y9) < 0.5)
            ):
                Ash_sh_y9 = Vy9 / (zy * fsy)
            elif Vy9 > Vcd_y:
                Ash_sh_y9 = (Vy9 - Vcd_y) / (zy * fsy)
            else:
                Ash_sh_y9 = 0
            # Update the required transverse reinforcement based on maximum
            Ashx_sh_req = max(Ashx_sh_req, Ash_sh_x1, Ash_sh_x9)
            Ashy_sh_req = max(Ashy_sh_req, Ash_sh_y1, Ash_sh_y9)
        # Save the required transverse reinforcement area to spacing ratio
        self.Ashx_sbh_req = Ashx_sh_req
        self.Ashy_sbh_req = Ashy_sh_req
