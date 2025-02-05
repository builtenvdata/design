import matplotlib.pyplot as plt
from pathlib import Path
import sys

# Add the src directory to sys.path
sys.path.append(str(Path(__file__).parents[1]))

from simdesign import rcmrf  # noqa
from simdesign.utils.misc import make_dir  # noqa


if __name__ == '__main__':
    # Path to the geometry mesh file
    data_folder = Path(__file__).parents[1] / 'data'
    input_path = data_folder / 'example-custom-geometry.xlsx'
    # Create geometry object based on excel sheet
    custom_frame = rcmrf.CustomGeometry(input_path)
    # Adding new lines and points for stairs (This must be always done)
    # Note that rectangles are specified in custom geometry
    custom_frame.add_new_lines_and_points_for_stairs()
    # Show the mesh
    custom_frame.show_mesh()
    # Set the output directory
    outdir_building = Path(__file__).parents[1] / 'tmp/Outputs-Single'
    make_dir(outdir_building)
    # Save geometry visualization
    path = outdir_building / 'geometry.html'
    custom_frame.export_mesh_to_html(path=str(path))
    # Set the building taxonomy data
    taxonomy_data = {
        "beta": 0.15,
        "beam_type": 2,
        "column_section": 1,
        "concrete_grade": "C19",
        "design_class": "eu_cdl",
        "quality": 1,
        # "slab_orient": 3,
        # "slab_thickness": 0.15,
        "slab_type": 1,
        # "staircase_slab_depth": 0.15,
        "steel_grade": "S400",
        "geometry": custom_frame
    }
    taxonomy = rcmrf.TaxonomyData(**taxonomy_data)
    # Initialize BDIM
    bdim = rcmrf.BDIM(taxonomy)
    # Make simumlated design
    bdim.run_iterative_design_algorithm()
    if bdim.ok:  # Design solution is found
        # Export to csv
        bdim.to_csv(outdir_building / 'BDIM-Data')
        # Initialize BNSM
        bnsm = rcmrf.BNSM(bdim, dincr=2e-4)
        # Export numerical models for OpenSeesPy
        bnsm.to_py(outdir_building / 'OpsPy-Model')
        # Export numerical models for OpenSeesTcl
        bnsm.to_tcl(outdir_building / 'OpsTcl-Model')
        # Do modal analysis
        modal_dir = outdir_building / 'Modal-Results'
        bnsm.do_modal(num_modes=2, out_dir=modal_dir)
        # Plot the model and save
        bnsm.plot_model(directory=outdir_building, show=True)
        # Plot the first two mode shapes and save
        bnsm.plot_mode_shape(mode_number=1, contour='x', show=True,
                             directory=outdir_building)
        bnsm.plot_mode_shape(mode_number=2, contour='y', show=True,
                             directory=outdir_building)
        # Perform the pushover directly
        push_dir = outdir_building / 'NSPA-Results-X'
        dx, vx, _ = bnsm.do_nspa(ctrl_dof=1, out_dir=push_dir)
        push_dir = outdir_building / 'NSPA-Results-Y'
        dy, vy, _ = bnsm.do_nspa(ctrl_dof=2, out_dir=push_dir)
        plt.plot(dx, vx, label='X-dir')
        plt.plot(dy, vy, label='Y-dir')
        plt.xlabel("Control Node Displacement [m]")
        plt.ylabel("Base Shear [kN]")
        plt.legend()
        plt.savefig(outdir_building / "nspa.png", dpi=300)
        plt.close()
