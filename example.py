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
    "tr_7599",
    "tr_0018",
    "tr_post18"
]

# Make directory for all outputs
outdir_main = Path("Outputs")
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
    outdir_class = outdir_main / f"{design_class}"
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
        modal_dir = outdir_building / 'Modal-Results'
        fim.do_modal(num_modes=6, out_dir=modal_dir)

    # Plot the model of the last building
    fim.plot_model(directory=outdir_building)
    # Plot the first mode shape of the last building
    fim.plot_mode_shape(mode_number=1, contour='x', directory=outdir_building)
    fim.plot_mode_shape(mode_number=2, contour='y', directory=outdir_building)
    # Perform the pushover directly for the last building
    push_dir = outdir_building / 'NSPA-Results-X'
    dx, vx = fim.do_nspa(ctrl_dof=1, out_dir=push_dir)
    push_dir = outdir_building / 'NSPA-Results-Y'
    dy, vy = fim.do_nspa(ctrl_dof=2, out_dir=push_dir)
    plt.plot(dx, vx, label='X-dir')
    plt.plot(dy, vy, label='Y-dir')
    plt.xlabel("Displacement of control node [m]")
    plt.ylabel("Base Shear [kN]")
    plt.legend()
    plt.savefig(outdir_building / "nspa.png", dpi=300)
    plt.close()
