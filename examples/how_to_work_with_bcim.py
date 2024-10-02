from src.rcmrf.bcim.model import BCIM

bcim = BCIM()
bcim.generate(sample_size=10, design_class="eu_cdl", num_storeys=5, beta=0.15)
taxonomy = bcim.taxonomy
bcim.to_csv("bcim_data_1.csv")


my_input = {
  "steel":
    {
      "grade": ["S240", "S400", "S500"],
      "probability": [0.40, 0.50, 0.10]
    },
  "beta": 0.20,
  "num_storeys": 5,
  "design_class": "eu_cdl",
  "sample_size": 20
}


bcim.generate(**my_input)
taxonomy = bcim.taxonomy
bcim.to_csv("bcim_data_2.csv")
