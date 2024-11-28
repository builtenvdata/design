from src import rcmrf

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


# Initialize BCIM
bcim = rcmrf.BCIM()
# Generate a building portfolio
bcim.generate(
    sample_size=1,
    design_class="eu_cdh",
    num_storeys=5,
    beta=0.1
)
# Initialize BDIM
bdim = rcmrf.BDIM(bcim.taxonomy[0])
# Make simumlated design
bdim.run_iterative_design_algorithm()

for _, columns_list in bdim.continuous_columns.items():
    for columns in columns_list:
        print('-------------------')
        for column in columns:
            print(f'column, bx:{column.bx}m, by:{column.by}m')

for _, beams_list in bdim.continuous_beams_x.items():
    for beams in beams_list:
        # print('-------------------')
        for beam in beams:
            print(
                f'stairs_wg: {beam.stairs_wg}\n'
                f'Asl_top_req: {beam.Asl_top_req}, '
                f'Asl_top: {beam.rhol_top*beam.Ag}\n'
                f'Asl_bot_req: {beam.Asl_bot_req}, '
                f'Asl_bot: {beam.rhol_bot*beam.Ag}\n'
                f'Ash_sbh_req: {beam.Ash_sbh_req},'
                f'Ash_sbh: {beam.rhoh_y*beam.b}\n'
                f'h:{beam.h}m, b:{beam.b}m, length: {beam.L}m\n'
                f'rhol: {beam.rhol}\n'
                f'dbl_topc:{beam.dbl_t1}, nbl_topc:{beam.nbl_t1}\n'
                f'dbl_botc:{beam.dbl_b1}, nbl_botc:{beam.nbl_b1}\n'
                f'dbl_topi:{beam.dbl_t2}, nbl_topi:{beam.nbl_t2}\n'
                f'dbl_boti:{beam.dbl_b2}, nbl_boti:{beam.nbl_b2}\n'
                f'dbh:{beam.dbh}, sbh:{beam.sbh}\n'
                f'rhoh_x: {beam.rhoh_x}, nbh_b: {beam.nbh_b}\n'
                f'rhoh_y: {beam.rhoh_y}, nbh_b: {beam.nbh_h}'
                )
            print('==========================================================')
            print(f'beam_x, b:{beam.b}m, h:{beam.h}m')

for _, beams_list in bdim.continuous_beams_y.items():
    for beams in beams_list:
        # print('-------------------')
        for beam in beams:
            print(
                f'stairs_wg: {beam.stairs_wg}\n'
                f'Asl_top_req: {beam.Asl_top_req}, '
                f'Asl_top: {beam.rhol_top*beam.Ag}\n'
                f'Asl_bot_req: {beam.Asl_bot_req}, '
                f'Asl_bot: {beam.rhol_bot*beam.Ag}\n'
                f'Ash_sbh_req: {beam.Ash_sbh_req},'
                f'Ash_sbh: {beam.rhoh_y*beam.b}\n'
                f'h:{beam.h}m, b:{beam.b}m, length: {beam.L}m\n'
                f'rhol: {beam.rhol}\n'
                f'dbl_topc:{beam.dbl_t1}, nbl_topc:{beam.nbl_t1}\n'
                f'dbl_botc:{beam.dbl_b1}, nbl_botc:{beam.nbl_b1}\n'
                f'dbl_topi:{beam.dbl_t2}, nbl_topi:{beam.nbl_t2}\n'
                f'dbl_boti:{beam.dbl_b2}, nbl_boti:{beam.nbl_b2}\n'
                f'dbh:{beam.dbh}, sbh:{beam.sbh}\n'
                f'rhoh_x: {beam.rhoh_x}, nbh_b: {beam.nbh_b}\n'
                f'rhoh_y: {beam.rhoh_y}, nbh_b: {beam.nbh_h}'
                )
            print('==========================================================')
            # print(f'beam_y, b:{beam.b}m, h:{beam.h}m')

# Check beam loads
for beam in bdim.beams:
    if beam.line in bcim.taxonomy[0].geometry.lines_y:
        # Original loading
        print(beam, 1.35*(beam.wg_total - beam.self_wg) +
              1.5 * beam.wq_total + beam.b * beam.L * beam.gamma_rc / 10)
        # New loading (difference is in the beam weight)
        print(beam, 1.35*beam.wg_total + 1.5*beam.wq_total)
