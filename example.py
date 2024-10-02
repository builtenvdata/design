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
    outdir_main = my_path / f"{design_class}"
    make_dir(outdir_main)
    # Save bcim information
    bcim.to_csv(outdir_main / "bcim_data.csv")
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
        outdir = outdir_main / f'Building_{i+1}'
        # Export numerical models for OpenSeesPy
        fim.to_py(outdir / 'OpsPy-Model')
        # Export numerical models for OpenSeesTcl
        fim.to_tcl(outdir / 'OpsTcl-Model')
        # Do modal analysis
        file_path = str(outdir / 'ModalResults.txt')
        fim.do_modal(num_modes=6, report_file=file_path)

    # Perform the pushover directly for the last building
    push_file = outdir / "push_x.csv"
    d, v = fim.do_nspa(ctrl_dof=1, report_file_path=push_file)
    plt.plot(d, v)
    plt.xlabel("Roof displacement [m]")
    plt.ylabel("Base Shear [kN]")
    plt.savefig(outdir / "push_x.png", dpi=300)
    plt.close()

# for _, columns_list in bdim.continuous_columns.items():
#     for columns in columns_list:
#         print('-------------------')
#         for column in columns:
#             print(f'column, bx:{column.bx}m, by:{column.by}m')

# for _, beams_list in bdim.continuous_beams_x.items():
#     for beams in beams_list:
#         # print('-------------------')
#         for beam in beams:
#             print(
#                 f'stairs_wg: {beam.stairs_wg}\n'
#                 f'Asl_top_req: {beam.Asl_top_req}, '
#                 f'Asl_top: {beam.rhol_top*beam.Ag}\n'
#                 f'Asl_bot_req: {beam.Asl_bot_req}, '
#                 f'Asl_bot: {beam.rhol_bot*beam.Ag}\n'
#                 f'Ash_sbh_req: {beam.Ash_sbh_req},'
#                 f'Ash_sbh: {beam.rhoh_y*beam.b}\n'
#                 f'h:{beam.h}m, b:{beam.b}m, length: {beam.L}m\n'
#                 f'rhol: {beam.rhol}\n'
#                 f'dbl_topc:{beam.dbl_t1}, nbl_topc:{beam.nbl_t1}\n'
#                 f'dbl_botc:{beam.dbl_b1}, nbl_botc:{beam.nbl_b1}\n'
#                 f'dbl_topi:{beam.dbl_t2}, nbl_topi:{beam.nbl_t2}\n'
#                 f'dbl_boti:{beam.dbl_b2}, nbl_boti:{beam.nbl_b2}\n'
#                 f'dbh:{beam.dbh}, sbh:{beam.sbh}\n'
#                 f'rhoh_x: {beam.rhoh_x}, nbh_b: {beam.nbh_b}\n'
#                 f'rhoh_y: {beam.rhoh_y}, nbh_b: {beam.nbh_h}'
#                 )
#             print('==========================================================')
#             print(f'beam_x, b:{beam.b}m, h:{beam.h}m')

# for _, beams_list in bdim.continuous_beams_y.items():
#     for beams in beams_list:
#         # print('-------------------')
#         for beam in beams:
#             print(
#                 f'stairs_wg: {beam.stairs_wg}\n'
#                 f'Asl_top_req: {beam.Asl_top_req}, '
#                 f'Asl_top: {beam.rhol_top*beam.Ag}\n'
#                 f'Asl_bot_req: {beam.Asl_bot_req}, '
#                 f'Asl_bot: {beam.rhol_bot*beam.Ag}\n'
#                 f'Ash_sbh_req: {beam.Ash_sbh_req},'
#                 f'Ash_sbh: {beam.rhoh_y*beam.b}\n'
#                 f'h:{beam.h}m, b:{beam.b}m, length: {beam.L}m\n'
#                 f'rhol: {beam.rhol}\n'
#                 f'dbl_topc:{beam.dbl_t1}, nbl_topc:{beam.nbl_t1}\n'
#                 f'dbl_botc:{beam.dbl_b1}, nbl_botc:{beam.nbl_b1}\n'
#                 f'dbl_topi:{beam.dbl_t2}, nbl_topi:{beam.nbl_t2}\n'
#                 f'dbl_boti:{beam.dbl_b2}, nbl_boti:{beam.nbl_b2}\n'
#                 f'dbh:{beam.dbh}, sbh:{beam.sbh}\n'
#                 f'rhoh_x: {beam.rhoh_x}, nbh_b: {beam.nbh_b}\n'
#                 f'rhoh_y: {beam.rhoh_y}, nbh_b: {beam.nbh_h}'
#                 )
#             print('==========================================================')
#             # print(f'beam_y, b:{beam.b}m, h:{beam.h}m')

# # Check beam loads
# for beam in bdim.beams:
#     if beam.line in bcim.taxonomy[0].geometry.lines_y:
#         # Original loading
#         print(beam, 1.35*(beam.wg_total - beam.self_wg) +
#               1.5 * beam.wq_total + beam.b * beam.L * beam.gamma_rc / 10)
#         # New loading (difference is in the beam weight)
#         print(beam, 1.35*beam.wg_total + 1.5*beam.wq_total)
