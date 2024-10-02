# Imports from installed packages
from typing import List

# Imports from the design class (eu_cdn) library
from .beam import Beam
from .column import Column

# Imports from bdim base library
from ..baselib.analysis import ElasticModelBase


class ElasticModel(ElasticModelBase):
    """Elastic model builder in OpenSees for design class eu_cdn.
    """
    beams: List[Beam]
    """Beam objects of the building."""
    columns: List[Column]
    """Column objects of the building."""
