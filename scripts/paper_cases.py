import matplotlib.pyplot as plt
from pathlib import Path
import sys

# Add the src directory to sys.path
sys.path.append(str(Path(__file__).parents[1]))

from src import rcmrf  # noqa
from src.utils.misc import make_dir  # noqa

concrete_grades = {
    "eu_cdn": "C14",
    "eu_cdl": "C14",
    "eu_cdm": "C16",
    "eu_cdh": "C20",
}
steel_grades = {
    "eu_cdn": "S240",
    "eu_cdl": "S240",
    "eu_cdm": "S400",
    "eu_cdh": "S400",
}


typical_span_length_x = [4.5] * 66
typical_span_length_y = [4.5] * 66
staircase_span_length_x = [2.5] * 66
staircase_span_length_y = [4.5] * 66
typical_storey_height = [2.8] * 66
ground_storey_height = [3.1] * 66
slab_type = [1] * 66
layout = ['B05'] * 66
slab_type = [1] * 66
slab_orient = [3] * 66
beam_type = [2] * 66
num_storeys = [4] * 66
slab_thickness = [0.15] * 66
column_section = [1] * 66
design_classes = ["eu_cdn"] * 3 + ["eu_cdl"] * 21 + ["eu_cdm"] * 21\
    + ["eu_cdh"] * 21
beta = [0, 0, 0] + [0, 0, 0,
                    0.05, 0.05, 0.05,
                    0.1, 0.1, 0.1,
                    0.15, 0.15, 0.15,
                    0.2, 0.2, 0.2,
                    0.25, 0.25, 0.25,
                    0.3, 0.3, 0.3] * 3
quality = [1, 2, 3] * 22
concere_grade = [concrete_grades.get(d) for d in design_classes]
steel_grade = [steel_grades.get(d) for d in design_classes]

bcim = rcmrf.BCIM()
# Generate a building portfolio
bcim.generate(
    sample_size=66,
    design_class='eu_cdh',
    num_storeys=4,
    beta=0.15
)

bcim.quality = quality
bcim.concrete_grade = concere_grade
bcim.steel_grade = steel_grade
bcim.num_storeys = num_storeys
bcim.beta = beta
bcim.design_class = design_classes
bcim.slab_orient = slab_orient
bcim.slab_type = slab_type
bcim.slab_thickness = slab_thickness
bcim.beam_type = beam_type
bcim.column_section = column_section
bcim.layout = layout
bcim.ground_storey_height = ground_storey_height
bcim.typical_storey_height = typical_storey_height
bcim.staircase_span_length_y = staircase_span_length_y
bcim.staircase_span_length_x = staircase_span_length_x
bcim.typical_span_length_y = typical_span_length_y
bcim.typical_span_length_x = typical_span_length_x
bcim._update_geometries()

# Make directory for all outputs
outdir_main = Path(__file__).parents[1] / "tmp/Outputs-Paper-EU"
make_dir(outdir_main)

# Loop through each building in portfolio
for i, taxonomy in enumerate(bcim.taxonomy):
    print("----------------------------------------------------")
    print(f"Designing building: {i+1}/{len(bcim.taxonomy)}")
    # Set the output directory
    outdir_building = outdir_main / f'Building_{i+1}'
    # Initialize BDIM
    bdim = rcmrf.BDIM(taxonomy)
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
    # Initialize FIM
    fim = rcmrf.FIM(bdim, scheme='EQL', dincr=1e-3, max_drift=0.1)
    # Perform the pushover directly
    push_dir = outdir_building / 'NSPA-Results-X'
    dx, vx, ok_x = fim.do_nspa(ctrl_dof=1, out_dir=push_dir)
    push_dir = outdir_building / 'NSPA-Results-Y'
    dy, vy, ok_y = fim.do_nspa(ctrl_dof=2, out_dir=push_dir)
    dincr_x = 1e-3
    dincr_y = 1e-3
    if ok_x != 0:
        fim = rcmrf.FIM(bdim, scheme='EQL', dincr=1e-4, max_drift=0.1)
        # Perform the pushover directly
        push_dir = outdir_building / 'NSPA-Results-X'
        dx, vx, ok_x = fim.do_nspa(ctrl_dof=1, out_dir=push_dir)
        dincr_x = 1e-4
    if ok_x != 0:
        fim = rcmrf.FIM(bdim, scheme='EQL', dincr=1e-5, max_drift=0.1)
        push_dir = outdir_building / 'NSPA-Results-X'
        dx, vx, ok_x = fim.do_nspa(ctrl_dof=1, out_dir=push_dir)
        dincr_x = 1e-5
    if ok_y != 0:
        fim = rcmrf.FIM(bdim, scheme='EQL', dincr=1e-4, max_drift=0.1)
        push_dir = outdir_building / 'NSPA-Results-Y'
        dy, vy, ok_y = fim.do_nspa(ctrl_dof=2, out_dir=push_dir)
        dincr_y = 1e-4
    if ok_y != 0:
        fim = rcmrf.FIM(bdim, scheme='EQL', dincr=1e-5, max_drift=0.1)
        push_dir = outdir_building / 'NSPA-Results-Y'
        dy, vy, ok_y = fim.do_nspa(ctrl_dof=2, out_dir=push_dir)
        dincr_y = 1e-5

    fim = rcmrf.FIM(bdim, scheme='EQL', dincr=min(dincr_x, dincr_y),
                    max_drift=0.1)
    # Export numerical models for OpenSeesPy
    fim.to_py(outdir_building / 'OpsPy-Model')
    # Export numerical models for OpenSeesTcl
    fim.to_tcl(outdir_building / 'OpsTcl-Model')
    # Do modal analysis
    modal_dir = outdir_building / 'Modal-Results'
    fim.do_modal(num_modes=6, out_dir=modal_dir)
    # Plot the model and save
    fim.plot_model(directory=outdir_building, show=False)
    # Plot the first two mode shapes and save
    fim.plot_mode_shape(mode_number=1, contour='x', show=False,
                        directory=outdir_building)
    fim.plot_mode_shape(mode_number=2, contour='y', show=False,
                        directory=outdir_building)
    # Plot pushover results
    plt.plot(dx, vx, label='X-dir')
    plt.plot(dy, vy, label='Y-dir')
    plt.xlabel("Control Node Displacement [m]")
    plt.ylabel("Base Shear [kN]")
    plt.legend()
    plt.savefig(outdir_building / "nspa.png", dpi=300)
    plt.close()
# Save bcim information
bcim.to_csv(outdir_main / "bcim_data.csv")
