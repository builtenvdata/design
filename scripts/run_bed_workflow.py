from pathlib import Path
import sys

# Add the src directory to sys.path
sys.path.append(str(Path(__file__).parents[1]))

from simdesign import rcmrf  # noqa
from simdesign.utils.misc import make_dir  # noqa

# The main inputs for each design class
inputs = {
    'bcim': {
        'sample_size': 30,
        'num_storeys': 4,
        'beta': 0.1,
        'seed': 2
    },
    'bnsm': {
        "scheme": 'FMP',
        "dincr": 1e-4,
        'max_drift': 0.1,
        'opensees': 'py'
    }
}

# Possible design classes
design_classes = [
    "eu_cdn",
    "eu_cdl",
    "eu_cdm",
    "eu_cdh",
    "tr_pre75",
    "tr_7599",
    "tr_0018",
    "tr_post18"
]

# Make directory for all outputs
outdir_main = Path(__file__).parents[1] / "tmp/Outputs-BED"
make_dir(outdir_main)

# Loop through all design classes
for design_class in design_classes:
    # Set the design class
    inputs['bcim']['design_class'] = design_class
    # Set the output directory for the current design class
    outdir = outdir_main / f"{design_class}"
    # Run the bed-workflow for rcmrf systems and save the outputs
    rcmrf.generate(inputs, outdir)
