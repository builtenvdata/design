import pytest
from pathlib import Path
import sys

# Add the src directory to sys.path
sys.path.append(str(Path(__file__).parents[1]))

from src import rcmrf  # noqa
from src.utils.misc import remove_dir  # noqa


# Main inputs for each design class
@pytest.fixture
def base_inputs_opspy():
    return {
        'bcim': {
            'sample_size': 2,
            'num_storeys': 5,
            'beta': 0.1
        },
        'fim': {
            'opensees': 'py'
        }
    }


# Test each design class
@pytest.mark.parametrize("design_class", [
    "eu_cdn",
    "eu_cdl",
    "eu_cdm",
    "eu_cdh",
    "tr_pre75",
    "tr_7599",
    "tr_0018",
    "tr_post18"
])
def test_rcmrf_opspy(base_inputs_opspy, design_class):
    """
    Test rcmrf.generate for each design class with base inputs.
    """
    # Set the design class
    base_inputs_opspy['bcim']['design_class'] = design_class
    # Output directory
    outdir = Path(__file__).parent / f"{design_class}"
    # Run the rcmrf workflow
    rcmrf.generate(base_inputs_opspy, outdir)
    # Clean-up
    remove_dir(outdir)


# Main inputs for each design class
@pytest.fixture
def base_inputs_opstcl():
    return {
        'bcim': {
            'sample_size': 2,
            'num_storeys': 4,
            'beta': 0.1
        },
        'fim': {
            'opensees': 'tcl'
        }
    }


# Test each design class
@pytest.mark.parametrize("design_class", [
    "eu_cdn",
    "eu_cdl",
    "eu_cdm",
    "eu_cdh",
    "tr_pre75",
    "tr_7599",
    "tr_0018",
    "tr_post18"
])
def test_rcmrf_opstcl(base_inputs_opstcl, design_class):
    """
    Test rcmrf.generate for each design class with base inputs.
    """
    # Set the design class
    base_inputs_opstcl['bcim']['design_class'] = design_class
    # Output directory
    outdir = Path(__file__).parent / f"{design_class}"
    # Run the rcmrf workflow
    rcmrf.generate(base_inputs_opstcl, outdir)
    # Clean-up
    remove_dir(outdir)
