from pathlib import Path
import sys

# Add the src directory to sys.path
sys.path.append(str(Path(__file__).parents[1]))

from simdesign.rcmrf import BCIM  # noqa

bcim = BCIM()
bcim.generate(sample_size=10, design_class="eu_cdl", num_storeys=5, beta=0.15)
taxonomy = bcim.taxonomy
bcim.to_csv(Path(__file__).parents[1]
            / "tmp/bcim_data_for_default_inputs.csv")


my_input = {
    "steel": {
        "grade": ["S240", "S400", "S500"],
        "probability": [0.40, 0.50, 0.10],
    },
    "beta": 0.20,
    "num_storeys": 5,
    "design_class": "eu_cdl",
    "sample_size": 20,
}


bcim.generate(**my_input)
taxonomy = bcim.taxonomy
bcim.to_csv(Path(__file__).parents[1]
            / "tmp/bcim_data_for_modified_inputs.csv")
