# Imports from installed packages
from typing import List

# Imports from the design class (tr_7599) library
from .beam import Beam
from .column import Column

# Imports from bdim base library
from ..baselib.analysis import ElasticModelBase

"""
Notes
-----
Cracked stiffness was not considered in design between 1975-1999
"""


class ElasticModel(ElasticModelBase):
    """Elastic model builder in OpenSees for design class tr_7599."""

    beams: List[Beam]
    """Beam objects of the building."""
    columns: List[Column]
    """Column objects of the building."""

    def _build_ops_model_seismic(self) -> None:
        """Builds the model for load cases of seismic load combos."""
        self._init_ops_model()
        self._add_ops_nodes()
        self._add_ops_beam_column_elements()
        self._add_ops_sp_constraints()
        self._add_ops_mp_constraints()
