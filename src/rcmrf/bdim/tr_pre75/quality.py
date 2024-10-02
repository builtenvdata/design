"""
Specific routines for defining tr_pre75 construction quality adjusments.
"""
# Imports from installed packages
from pathlib import Path

# Imports from bdim base library
from ..baselib.quality import QualityBase


class Quality(QualityBase):
    """Quality object for design class: tr_pre75.
    """
    data_path = Path(__file__).parent / 'data' / 'quality.json'
    """Path to the json file containing all the construction quality data."""
