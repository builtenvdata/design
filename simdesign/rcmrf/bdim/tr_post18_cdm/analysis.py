# Imports from installed packages
from typing import List

# Imports from the design class (tr_post18_cdm) library
from .beam import Beam
from .column import Column

# Imports from bdim base library
from ..baselib.analysis import ElasticModelBase
from ..baselib.beam import BeamForces
from ..baselib.column import ColumnForces

"""
Notes
-----
1- Cracked stiffness has been considered in design since 2018.
2- The method named "analyze_for_all" has been overwritten here
to include an overstrength factor of 2.5, which is the value for
RCMRF buildings with high ductility in the case of DTS1 and DTS2.
"""


class ElasticModel(ElasticModelBase):
    """Elastic model builder in OpenSees for design class tr_post18_cdm.
    """
    beams: List[Beam]
    """Beam objects of the building."""
    columns: List[Column]
    """Column objects of the building."""

    def build_ops_model_seismic(self) -> None:
        """Builds the model for load cases of seismic load combos.
        """
        self._init_ops_model()
        self._add_ops_nodes()
        self._add_ops_beam_column_elements(True)
        self._add_ops_sp_constraints()
        self._add_ops_mp_constraints()

    def analyze_for_all(self):
        """Analyzes the building all load cases and combinations.

        Stores element forces for each.
        """
        # Seismic load cases
        seismic_load_cases = ["E+X", "E-X", "E+Y", "E-Y"]
        # Distinguish gravity and seismic load combinations
        seismic_combos = self.loads.get_seismic_load_combos()
        gravity_combos = self.loads.get_gravity_load_combos()
        # Run all load cases
        self._run_gravity_load_cases()
        if any(seismic_combos):
            self._run_seismic_load_cases()

        # Start combining forces for BEAMS
        for beam in self.beams:
            # Restart combo forces
            beam.design_forces = []
            beam.design_forces_overstrength_adjusted = []
            # Loop through combinations
            for combo in self.loads.combinations:
                # Initialzie total combined forces
                forces = BeamForces(0, 0, 0, 0, 0, 0)
                # Determine type of the load combination
                if combo in seismic_combos:
                    combo_type = 'seismic'
                elif combo in gravity_combos:
                    combo_type = 'gravity'
                # Permanent Loads
                if 'G' in combo.loads:
                    gfactor = combo.loads['G']
                    if combo_type == 'gravity':
                        forces += gfactor * beam.forces["G/gravity/alpha"]
                    if combo_type == 'seismic':
                        forces += gfactor * beam.forces["G/seismic/alpha"]
                # Variable Loads
                if 'Q' in combo.loads:
                    qfactor = combo.loads['Q']
                    if combo_type == 'gravity':
                        forces += qfactor * beam.forces["Q/gravity/alpha"]
                    if combo_type == 'seismic':
                        forces += qfactor * beam.forces["Q/seismic/alpha"]
                # Add the forces from seismic loading
                forces_ov = forces
                if combo_type == 'seismic':
                    gfactor = combo.masses['G']
                    qfactor = combo.masses['Q']
                    for load_case in seismic_load_cases:
                        if load_case in combo.loads:
                            tag = f"{load_case}/{gfactor}G/{qfactor}Q"
                            fact = combo.loads[load_case]
                            forces += fact * beam.forces[tag]
                            forces_ov += 2.5 * fact * beam.forces[tag]
                # Set the loading case (type)
                forces.case = combo_type
                forces_ov.case = combo_type
                # Append the combined forces
                beam.design_forces.append(forces)
                beam.design_forces_overstrength_adjusted.append(forces_ov)
        # Start combining forces for COLUMNS
        for column in self.columns:
            # Restart combo forces
            column.design_forces = []
            column.design_forces_overstrength_adjusted = []
            # Loop through combinations
            for combo in self.loads.combinations:
                # Initialzie total combined forces
                forces = ColumnForces(0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                # Determine type of the load combination
                if combo in seismic_combos:
                    combo_type = 'seismic'
                elif combo in gravity_combos:
                    combo_type = 'gravity'
                # Permanent Loads
                if 'G' in combo.loads:
                    gfactor = combo.loads['G']
                    if combo_type == 'gravity':
                        forces += gfactor * column.forces["G/gravity"]
                    if combo_type == 'seismic':
                        forces += gfactor * column.forces["G/seismic"]
                # Variable Loads
                if 'Q' in combo.loads:
                    qfactor = combo.loads['Q']
                    if combo_type == 'gravity':
                        forces += qfactor * column.forces["Q/gravity"]
                    if combo_type == 'seismic':
                        forces += qfactor * column.forces["Q/seismic"]
                # Add the forces from seismic loading
                forces_ov = forces
                if combo_type == 'seismic':
                    gfactor = combo.masses['G']
                    qfactor = combo.masses['Q']
                    for load_case in seismic_load_cases:
                        if load_case in combo.loads:
                            tag = f"{load_case}/{gfactor}G/{qfactor}Q"
                            fact = combo.loads[load_case]
                            forces += fact * column.forces[tag]
                            forces_ov += 2.5 * fact * column.forces[tag]
                # Set the loading case (type)
                forces.case = combo_type
                forces_ov.case = combo_type
                # Append the combined forces
                column.design_forces.append(forces)
                column.design_forces_overstrength_adjusted.append(forces_ov)
