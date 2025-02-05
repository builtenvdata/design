import matplotlib.pyplot as plt
from pathlib import Path
import sys

# Add the src directory to sys.path
sys.path.append(str(Path(__file__).parents[1]))

from simdesign import rcmrf  # noqa
from simdesign.utils.misc import make_dir  # noqa


# File directory
my_path = Path(__file__).parents[1]

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
outdir_main = Path(__file__).parents[1] / "tmp/Outputs-NSPA-Batch"
make_dir(outdir_main)

# Loop through all design classes
for design_class in design_classes:
    # Make directory specific to the design class
    outdir_class = outdir_main / f"{design_class}"
    make_dir(outdir_class)
    # Initialize BCIM
    bcim = rcmrf.BCIM()
    # Generate a building portfolio
    bcim.generate(
        sample_size=30,
        design_class=design_class,
        num_storeys=4,
        beta=0.1
    )
    # Save bcim information
    bcim.to_csv(outdir_class / "BCIM_initial.csv")
    # Loop through each building in portfolio
    for i, taxonomy in enumerate(bcim.taxonomy):
        print("----------------------------------------------------")
        print(f"Designing {design_class.upper()} building: "
              f"{i+1}/{len(bcim.taxonomy)}")
        # Set the output directory
        outdir_building = outdir_class / f'Building_{i+1}'
        # Initialize BDIM
        bdim = rcmrf.BDIM(taxonomy)
        # To ensure the reproducibility of BDIM set the seed
        bdim.set_seed_for_quality_adjustments(bcim.inputs.seed)
        # Make simumlated design
        bdim.run_iterative_design_algorithm()
        # Update BCIM in case some properties changed during design
        if bdim.ok:
            bcim.column_section[i] = bdim.column_section
            bcim.beam_type[i] = bdim.beam_type
            bcim.concrete_grade[i] = bdim.concrete_grade
            bcim.steel_grade[i] = bdim.steel_grade
            # Export to csv
            bdim.to_csv(outdir_building / 'BDIM-Data')
            # Initialize BNSM
            bnsm = rcmrf.BNSM(bdim, scheme='FMP', dincr=1e-3, max_drift=0.1)
            # Do modal analysis
            modal_dir = outdir_building / 'Modal-Results'
            bnsm.do_modal(num_modes=6, out_dir=modal_dir)
            # Plot the model and save
            bnsm.plot_model(directory=outdir_building, show=False)
            # Plot the first two mode shapes and save
            bnsm.plot_mode_shape(mode_number=1, contour='x', show=False,
                                 directory=outdir_building)
            bnsm.plot_mode_shape(mode_number=2, contour='y', show=False,
                                 directory=outdir_building)
            # Perform the pushover directly
            push_dir = outdir_building / 'NSPA-Results-X'
            dx, vx, ok_x = bnsm.do_nspa(ctrl_dof=1, out_dir=push_dir)
            push_dir = outdir_building / 'NSPA-Results-Y'
            dy, vy, ok_y = bnsm.do_nspa(ctrl_dof=2, out_dir=push_dir)
            dincr_x = 1e-3
            dincr_y = 1e-3
            if ok_x != 0:
                bnsm = rcmrf.BNSM(
                    bdim, scheme='FMP', dincr=1e-4, max_drift=0.1)
                # Perform the pushover directly
                push_dir = outdir_building / 'NSPA-Results-X'
                dx, vx, ok_x = bnsm.do_nspa(ctrl_dof=1, out_dir=push_dir)
                dincr_x = 1e-4
            if ok_x != 0:
                bnsm = rcmrf.BNSM(
                    bdim, scheme='FMP', dincr=1e-5, max_drift=0.1)
                push_dir = outdir_building / 'NSPA-Results-X'
                dx, vx, ok_x = bnsm.do_nspa(ctrl_dof=1, out_dir=push_dir)
                dincr_x = 1e-5
            if ok_y != 0:
                bnsm = rcmrf.BNSM(
                    bdim, scheme='FMP', dincr=1e-4, max_drift=0.1)
                push_dir = outdir_building / 'NSPA-Results-Y'
                dy, vy, ok_y = bnsm.do_nspa(ctrl_dof=2, out_dir=push_dir)
                dincr_y = 1e-4
            if ok_y != 0:
                bnsm = rcmrf.BNSM(
                    bdim, scheme='FMP', dincr=1e-5, max_drift=0.1)
                push_dir = outdir_building / 'NSPA-Results-Y'
                dy, vy, ok_y = bnsm.do_nspa(ctrl_dof=2, out_dir=push_dir)
                dincr_y = 1e-5
            # Restart BNSM with the dincr which worked for both
            bnsm = rcmrf.BNSM(bdim, scheme='FMP', dincr=min(dincr_x, dincr_y),
                              max_drift=0.1)
            # Export numerical models for OpenSeesPy
            bnsm.to_py(outdir_building / 'OpsPy-Model')
            # Export numerical models for OpenSeesTcl
            bnsm.to_tcl(outdir_building / 'OpsTcl-Model')
            # Plot the pushover analysis results
            plt.plot(dx, vx, label='X-dir')
            plt.plot(dy, vy, label='Y-dir')
            plt.xlabel("Control Node Displacement [m]")
            plt.ylabel("Base Shear [kN]")
            plt.legend()
            plt.savefig(outdir_building / "nspa.png", dpi=300)
            plt.close()
    # Save updated BCIM
    bcim.to_csv(outdir_class / "BCIM_final.csv")
