"""
Specific routines for defining and designing eu_cdn columns.

Design is based on DCL1 properties.
Design based on ultimate strength analysis.

References
----------
RBA (1935) Regulamento para o Emprego de Betão Armado.
Decreto-Lei N.° 4036, Lisbon, Portugal.
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
from math import ceil, pi

# Imports from the design class (eu_cdn) library
from .materials import Steel, Concrete

# Imports from bdim base library
from ..baselib.column import ColumnBase


class Column(ColumnBase):
    """Column object for design class: eu_cdn.
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
            Maximum allowed longitudinal reinforcement ratio.
        """
        return 0.05

    @property
    def rhol_min(self) -> float:
        """
        Returns
        -------
        float
            Minimum allowed longitudinal reinforcement ratio.
        """
        aux = 0.005 + 0.0006 * (self.line.length / min(self.bx, self.by) - 5)
        if aux < 0.005:
            return 0.005
        elif aux > 0.008:
            return 0.008
        else:
            return aux

    def predesign_section_dimensions(self) -> None:
        """Does preliminary design of column.

        This method makes initial guess for section dimensions.

        Notes
        -----
        It is overwritten for eu_cdn design class with following changes:
        - It retrieves design concrete strength from concrete attributes.
        - In case of the rectangular sections, the longer dimension does no
        longer need to be twice of shorter one.
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
        It is overwritten for eu_cdn design class with following changes:
        - In case of the rectangular sections, the longer dimension no
        longer needs to be twice of the shorter one.

        TODO
        ----
        Axial load ratio restriction?
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
        Axial load ratio restriction?
        """
        # Only adequacy check is maximum dimensions
        if self.bx > self.max_b:
            self.ok_x = False
        else:
            self.ok_x = True
        if self.by > self.max_b:
            self.ok_y = False
        else:
            self.ok_y = True

    def compute_required_longitudinal_reinforcement(self) -> None:
        """Computes the required longitudinal reinforcement for design forces.

        TODO
        ----
        Add specific reference pages and equation numbers.
        """
        # Design is based on minimum reinforcement requirement
        Asl_min = self.rhol_min * self.Ag
        Aslx = (0.5**2) * Asl_min
        Asly = (0.5**2) * Asl_min
        if self.section == 1:  # Square section
            pass
        elif self.section == 2:  # Rectangular section
            bx_by_ratio = self.bx / self.by
            if 0.8 < bx_by_ratio < 1.2:  # dims are close
                pass  # use the same reinf. area
            elif bx_by_ratio >= 1.2:  # bx is much larger
                Aslx = 0.33 * Asl_min
                Asly = 0.17 * Asl_min
            elif bx_by_ratio <= 0.8:  # by is much larger
                Aslx = 0.17 * Asl_min
                Asly = 0.33 * Asl_min
        # Save required reinforcement
        self.Aslx_req = Aslx
        self.Asly_req = Asly

    def compute_required_transverse_reinforcement(self) -> None:
        """Computes the required transverse reinforcement for design forces.

        TODO
        ----
        Add specific reference pages and equation numbers.
        """
        # NOTE: If the minimum based on the values from rebars.json is greater,
        # it will be considered instead. Thus, could be left as 0.0
        sbh = 0.5  # stirrup spacing
        dbh = 0.006  # stirrup diameter
        nlegs = 2  # number of legs
        Ash_sbh_min = nlegs * (pi * 0.25 * dbh**2) / sbh
        self.Ashx_sbh_req = Ash_sbh_min
        self.Ashy_sbh_req = Ash_sbh_min
