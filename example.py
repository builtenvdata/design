from src.rcmrf.bcim.model import BCIM
from src.rcmrf.bdim.model import get_bdim
from src.rcmrf.fim.model import FIM
from src.utils.misc import make_dir
import matplotlib.pyplot as plt
from pathlib import Path

# File directory
my_path = Path(__file__).parent

# Design classes
design_classes = [
    "eu_cdn",
    "eu_cdl",
    "eu_cdm",
    "eu_cdh",
    "tr_pre75",
    "tr_7500",
    "tr_0007",
    "tr_0718",
    "tr_post18"
]

# Make directory for all outputs
outdir_main = "Outputs"
make_dir(outdir_main)

# Loop through all design classes
for design_class in design_classes:
    # Initialize BCIM
    bcim = BCIM()
    # Generate a building portfolio
    bcim.generate(
        sample_size=10,
        design_class=design_class,
        num_storeys=5,
        beta=0.1
    )
    # Make directory specific to the design class
    outdir_class = my_path / f"{design_class}"
    make_dir(outdir_class)
    # Save bcim information
    bcim.to_csv(outdir_class / "bcim_data.csv")
    # Loop through each building in portfolio
    for i, taxonomy in enumerate(bcim.taxonomy):
        print("----------------------------------------------------")
        print(f"Designing {design_class.upper()} building: "
              f"{i+1}/{len(bcim.taxonomy)}")
        # Initialize BDIM
        bdim = get_bdim(taxonomy)
        # Make simumlated design
        bdim.run_iterative_design_algorithm()
        # Initialize FIM
        fim = FIM(bdim)
        # Set the output directory
        outdir_building = outdir_class / f'Building_{i+1}'
        # Export numerical models for OpenSeesPy
        fim.to_py(outdir_building / 'OpsPy-Model')
        # Export numerical models for OpenSeesTcl
        fim.to_tcl(outdir_building / 'OpsTcl-Model')
        # Do modal analysis
        file_path = str(outdir_building / 'ModalResults.txt')
        fim.do_modal(num_modes=6, report_file=file_path)

    # Perform the pushover directly for the last building
    push_file = outdir_building / "push_x.csv"
    d, v = fim.do_nspa(ctrl_dof=1, report_file_path=push_file)
    plt.plot(d, v)
    plt.xlabel("Roof displacement [m]")
    plt.ylabel("Base Shear [kN]")
    plt.savefig(outdir_building / "push_x.png", dpi=300)
    plt.close()
