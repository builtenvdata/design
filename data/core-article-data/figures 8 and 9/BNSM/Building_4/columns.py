import openseespy.opensees as ops


def add_columns() -> None:
    """Add components of all columns to ops domain (plastic hinges, column elements and nodes)
    """
    # Create elastic column element nodes
    ops.node(170003, 7.7, 0.0, 0.0)
    ops.node(121003, 7.7, 0.0, 3.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3, 170003, 121003, 0.35, 26119670.70288791, 10883196.1262033, 0.01632638, 0.01572083, 0.00802083, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20003, 549.57378519, 0.00094479, 669.98366469, 0.04733965, 66.99836647, 0.11377811, -549.57378519, -0.00094479, -669.98366469, -0.04733965, -66.99836647, -0.11377811, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10003, 553.59436389, 0.00075831, 674.88513947, 0.04603277, 67.48851395, 0.10872819, -553.59436389, -0.00075831, -674.88513947, -0.04603277, -67.48851395, -0.10872819, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20003, 3, 0.0, 366.00198201, 0.01889571, 366.00198201, 0.05668714, 256.20138741, -5170.53256877, 0.05, 2, 0, 70003, 21003, 2, 3)
    ops.uniaxialMaterial('LimitState', 40003, 91.5004955, 0.00010666, 274.50148651, 0.00031997, 915.00495502, 0.00106655, -91.5004955, -0.00010666, -274.50148651, -0.00031997, -915.00495502, -0.00106655, 0.4, 0.3, 0.003, 0.0, 0.0, 20003, 2)
    ops.limitCurve('ThreePoint', 10003, 3, 0.0, 602.82923503, 0.0151662, 602.82923503, 0.04549861, 421.98046452, -15743.95077101, 0.05, 2, 0, 70003, 21003, 1, 3)
    ops.uniaxialMaterial('LimitState', 30003, 150.70730876, 0.00017567, 452.12192627, 0.000527, 1507.07308757, 0.00175668, -150.70730876, -0.00017567, -452.12192627, -0.000527, -1507.07308757, -0.00175668, 0.4, 0.3, 0.003, 0.0, 0.0, 10003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3, 99999, 'P', 40003, 'Vy', 30003, 'Vz', 20003, 'My', 10003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170003, 70003, 170003, 3, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121003, 121003, 21003, 3, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170004, 12.45, 0.0, 0.0)
    ops.node(121004, 12.45, 0.0, 3.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4, 170004, 121004, 0.1575, 29572314.77056647, 12321797.82106936, 0.00337604, 0.00292359, 0.00176859, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20004, 124.94119647, 0.00114363, 151.24210264, 0.01785501, 15.12421026, 0.05315164, -124.94119647, -0.00114363, -151.24210264, -0.01785501, -15.12421026, -0.05315164, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10004, 135.06990094, 0.00092854, 163.50296298, 0.01894314, 16.3502963, 0.06112186, -135.06990094, -0.00092854, -163.50296298, -0.01894314, -16.3502963, -0.06112186, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20004, 4, 0.0, 163.35738006, 0.02287268, 163.35738006, 0.06861803, 114.35016604, -1530.35346323, 0.05, 2, 0, 70004, 21004, 2, 3)
    ops.uniaxialMaterial('LimitState', 40004, 40.83934501, 9.343e-05, 122.51803504, 0.0002803, 408.39345014, 0.00093434, -40.83934501, -9.343e-05, -122.51803504, -0.0002803, -408.39345014, -0.00093434, 0.4, 0.3, 0.003, 0.0, 0.0, 20004, 2)
    ops.limitCurve('ThreePoint', 10004, 4, 0.0, 180.50167958, 0.01857072, 180.50167958, 0.05571215, 126.35117571, -2055.90642857, 0.05, 2, 0, 70004, 21004, 1, 3)
    ops.uniaxialMaterial('LimitState', 30004, 45.12541989, 0.00010324, 135.37625968, 0.00030972, 451.25419895, 0.0010324, -45.12541989, -0.00010324, -135.37625968, -0.00030972, -451.25419895, -0.0010324, 0.4, 0.3, 0.003, 0.0, 0.0, 10004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4, 99999, 'P', 40004, 'Vy', 30004, 'Vz', 20004, 'My', 10004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170004, 70004, 170004, 4, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121004, 121004, 21004, 4, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170005, 0.0, 5.15, 0.0)
    ops.node(121005, 0.0, 5.15, 3.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 5, 170005, 121005, 0.1125, 29066308.54822284, 12110961.89509285, 0.00152995, 0.00064453, 0.00208828, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20005, 129.14352629, 0.00091106, 155.80255008, 0.01872241, 15.58025501, 0.06607939, -129.14352629, -0.00091106, -155.80255008, -0.01872241, -15.58025501, -0.06607939, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10005, 60.83911574, 0.0015389, 73.39809938, 0.01635584, 7.33980994, 0.04695877, -60.83911574, -0.0015389, -73.39809938, -0.01635584, -7.33980994, -0.04695877, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20005, 5, 0.0, 150.53884087, 0.01822119, 150.53884087, 0.05466356, 105.37718861, -1801.76848309, 0.05, 2, 0, 70005, 21005, 2, 3)
    ops.uniaxialMaterial('LimitState', 40005, 37.63471022, 0.00012264, 112.90413065, 0.00036793, 376.34710217, 0.00122642, -37.63471022, -0.00012264, -112.90413065, -0.00036793, -376.34710217, -0.00122642, 0.4, 0.3, 0.003, 0.0, 0.0, 20005, 2)
    ops.limitCurve('ThreePoint', 10005, 5, 0.0, 119.22636943, 0.03077797, 119.22636943, 0.09233391, 83.4584586, -1013.61160814, 0.05, 2, 0, 70005, 21005, 1, 3)
    ops.uniaxialMaterial('LimitState', 30005, 29.80659236, 9.713e-05, 89.41977708, 0.0002914, 298.06592359, 0.00097132, -29.80659236, -9.713e-05, -89.41977708, -0.0002914, -298.06592359, -0.00097132, 0.4, 0.3, 0.003, 0.0, 0.0, 10005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 5, 99999, 'P', 40005, 'Vy', 30005, 'Vz', 20005, 'My', 10005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170005, 70005, 170005, 5, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121005, 121005, 21005, 5, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170006, 2.95, 5.15, 0.0)
    ops.node(121006, 2.95, 5.15, 3.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 6, 170006, 121006, 0.2975, 28999916.03559846, 12083298.34816602, 0.00900415, 0.00334068, 0.01970318, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20006, 741.46970911, 0.00069084, 897.50095499, 0.05595423, 89.7500955, 0.14076574, -741.46970911, -0.00069084, -897.50095499, -0.05595423, -89.7500955, -0.14076574, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10006, 389.13057825, 0.00125588, 471.01730698, 0.04194196, 47.1017307, 0.08296105, -389.13057825, -0.00125588, -471.01730698, -0.04194196, -47.1017307, -0.08296105, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20006, 6, 0.0, 673.59290795, 0.01381682, 673.59290795, 0.04145045, 471.51503556, -14409.05822201, 0.05, 2, 0, 70006, 21006, 2, 3)
    ops.uniaxialMaterial('LimitState', 40006, 168.39822699, 0.00020799, 505.19468096, 0.00062398, 1683.98226987, 0.00207993, -168.39822699, -0.00020799, -505.19468096, -0.00062398, -1683.98226987, -0.00207993, 0.4, 0.3, 0.003, 0.0, 0.0, 20006, 2)
    ops.limitCurve('ThreePoint', 10006, 6, 0.0, 354.72246964, 0.02511755, 354.72246964, 0.07535265, 248.30572874, -4166.99076919, 0.05, 2, 0, 70006, 21006, 1, 3)
    ops.uniaxialMaterial('LimitState', 30006, 88.68061741, 0.00010953, 266.04185223, 0.00032859, 886.80617409, 0.00109532, -88.68061741, -0.00010953, -266.04185223, -0.00032859, -886.80617409, -0.00109532, 0.4, 0.3, 0.003, 0.0, 0.0, 10006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 6, 99999, 'P', 40006, 'Vy', 30006, 'Vz', 20006, 'My', 10006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170006, 70006, 170006, 6, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121006, 121006, 21006, 6, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170007, 7.7, 5.15, 0.0)
    ops.node(121007, 7.7, 5.15, 3.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 7, 170007, 121007, 0.45, 28588677.97429515, 11911949.15595631, 0.02179311, 0.00835313, 0.04125, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20007, 1139.38121606, 0.00066129, 1382.52932687, 0.04905743, 138.25293269, 0.12005209, -1139.38121606, -0.00066129, -1382.52932687, -0.04905743, -138.25293269, -0.12005209, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10007, 699.19132316, 0.00103346, 848.40130391, 0.04327746, 84.84013039, 0.09470125, -699.19132316, -0.00103346, -848.40130391, -0.04327746, -84.84013039, -0.09470125, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20007, 7, 0.0, 996.98002291, 0.01322585, 996.98002291, 0.03967754, 697.88601604, -20409.05463431, 0.05, 2, 0, 70007, 21007, 2, 3)
    ops.uniaxialMaterial('LimitState', 40007, 249.24500573, 0.00020645, 747.73501718, 0.00061935, 2492.45005727, 0.0020645, -249.24500573, -0.00020645, -747.73501718, -0.00061935, -2492.45005727, -0.0020645, 0.4, 0.3, 0.003, 0.0, 0.0, 20007, 2)
    ops.limitCurve('ThreePoint', 10007, 7, 0.0, 433.04665033, 0.02066911, 433.04665033, 0.06200732, 303.13265523, -3928.84644004, 0.05, 2, 0, 70007, 21007, 1, 3)
    ops.uniaxialMaterial('LimitState', 30007, 108.26166258, 8.967e-05, 324.78498775, 0.00026902, 1082.61662583, 0.00089673, -108.26166258, -8.967e-05, -324.78498775, -0.00026902, -1082.61662583, -0.00089673, 0.4, 0.3, 0.003, 0.0, 0.0, 10007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 7, 99999, 'P', 40007, 'Vy', 30007, 'Vz', 20007, 'My', 10007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170007, 70007, 170007, 7, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121007, 121007, 21007, 7, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170008, 12.45, 5.15, 0.0)
    ops.node(121008, 12.45, 5.15, 3.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 8, 170008, 121008, 0.225, 27933934.44590719, 11639139.35246133, 0.00505263, 0.00185625, 0.01160156, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20008, 439.50058358, 0.00073327, 532.5244943, 0.04014177, 53.25244943, 0.10483528, -439.50058358, -0.00073327, -532.5244943, -0.04014177, -53.25244943, -0.10483528, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10008, 215.13798667, 0.00142961, 260.67370974, 0.03066995, 26.06737097, 0.06254271, -215.13798667, -0.00142961, -260.67370974, -0.03066995, -26.06737097, -0.06254271, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20008, 8, 0.0, 390.24258539, 0.01466536, 390.24258539, 0.04399608, 273.16980977, -6210.29727946, 0.05, 2, 0, 70008, 21008, 2, 3)
    ops.uniaxialMaterial('LimitState', 40008, 97.56064635, 0.00016541, 292.68193904, 0.00049622, 975.60646346, 0.00165407, -97.56064635, -0.00016541, -292.68193904, -0.00049622, -975.60646346, -0.00165407, 0.4, 0.3, 0.003, 0.0, 0.0, 20008, 2)
    ops.limitCurve('ThreePoint', 10008, 8, 0.0, 225.00171485, 0.02859223, 225.00171485, 0.08577669, 157.50120039, -2059.34833435, 0.05, 2, 0, 70008, 21008, 1, 3)
    ops.uniaxialMaterial('LimitState', 30008, 56.25042871, 9.537e-05, 168.75128614, 0.00028611, 562.50428712, 0.00095369, -56.25042871, -9.537e-05, -168.75128614, -0.00028611, -562.50428712, -0.00095369, 0.4, 0.3, 0.003, 0.0, 0.0, 10008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 8, 99999, 'P', 40008, 'Vy', 30008, 'Vz', 20008, 'My', 10008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170008, 70008, 170008, 8, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121008, 121008, 21008, 8, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170009, 0.0, 10.3, 0.0)
    ops.node(121009, 0.0, 10.3, 3.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 9, 170009, 121009, 0.125, 29891199.07830913, 12454666.28262881, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20009, 128.51855537, 0.0008489, 154.99532327, 0.01966665, 15.49953233, 0.06991778, -128.51855537, -0.0008489, -154.99532327, -0.01966665, -15.49953233, -0.06991778, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10009, 67.79069515, 0.00157214, 81.75660456, 0.01676787, 8.17566046, 0.0470305, -67.79069515, -0.00157214, -81.75660456, -0.01676787, -8.17566046, -0.0470305, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20009, 9, 0.0, 169.25840675, 0.01697808, 169.25840675, 0.05093423, 118.48088472, -2056.82431372, 0.05, 2, 0, 70009, 21009, 2, 3)
    ops.uniaxialMaterial('LimitState', 40009, 42.31460169, 0.00012068, 126.94380506, 0.00036204, 423.14601687, 0.00120679, -42.31460169, -0.00012068, -126.94380506, -0.00036204, -423.14601687, -0.00120679, 0.4, 0.3, 0.003, 0.0, 0.0, 20009, 2)
    ops.limitCurve('ThreePoint', 10009, 9, 0.0, 129.68132888, 0.03144282, 129.68132888, 0.09432847, 90.77693021, -1024.84202987, 0.05, 2, 0, 70009, 21009, 1, 3)
    ops.uniaxialMaterial('LimitState', 30009, 32.42033222, 9.246e-05, 97.26099666, 0.00027738, 324.20332219, 0.00092461, -32.42033222, -9.246e-05, -97.26099666, -0.00027738, -324.20332219, -0.00092461, 0.4, 0.3, 0.003, 0.0, 0.0, 10009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 9, 99999, 'P', 40009, 'Vy', 30009, 'Vz', 20009, 'My', 10009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170009, 70009, 170009, 9, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121009, 121009, 21009, 9, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170010, 2.95, 10.3, 0.0)
    ops.node(121010, 2.95, 10.3, 3.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 10, 170010, 121010, 0.28, 28440848.95627252, 11850353.73178022, 0.00829164, 0.00314417, 0.01642667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20010, 615.43461072, 0.00074856, 745.44845733, 0.05158063, 74.54484573, 0.13436722, -615.43461072, -0.00074856, -745.44845733, -0.05158063, -74.54484573, -0.13436722, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10010, 319.7439357, 0.00136408, 387.29154887, 0.03950952, 38.72915489, 0.08140543, -319.7439357, -0.00136408, -387.29154887, -0.03950952, -38.72915489, -0.08140543, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20010, 10, 0.0, 541.63468647, 0.01497114, 541.63468647, 0.04491342, 379.14428053, -9567.57524612, 0.05, 2, 0, 70010, 21010, 2, 3)
    ops.uniaxialMaterial('LimitState', 40010, 135.40867162, 0.00018119, 406.22601486, 0.00054358, 1354.08671618, 0.00181192, -135.40867162, -0.00018119, -406.22601486, -0.00054358, -1354.08671618, -0.00181192, 0.4, 0.3, 0.003, 0.0, 0.0, 20010, 2)
    ops.limitCurve('ThreePoint', 10010, 10, 0.0, 308.34638542, 0.02728153, 308.34638542, 0.08184459, 215.8424698, -3250.32472744, 0.05, 2, 0, 70010, 21010, 1, 3)
    ops.uniaxialMaterial('LimitState', 30010, 77.08659636, 0.00010315, 231.25978907, 0.00030945, 770.86596355, 0.00103151, -77.08659636, -0.00010315, -231.25978907, -0.00030945, -770.86596355, -0.00103151, 0.4, 0.3, 0.003, 0.0, 0.0, 10010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 10, 99999, 'P', 40010, 'Vy', 30010, 'Vz', 20010, 'My', 10010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170010, 70010, 170010, 10, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121010, 121010, 21010, 10, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170011, 7.7, 10.3, 0.0)
    ops.node(121011, 7.7, 10.3, 3.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 11, 170011, 121011, 0.45, 28275730.93428167, 11781554.55595069, 0.02179311, 0.00835313, 0.04125, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20011, 1120.84166337, 0.00065519, 1360.77765985, 0.04960381, 136.07776599, 0.12003679, -1120.84166337, -0.00065519, -1360.77765985, -0.04960381, -136.07776599, -0.12003679, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10011, 686.46198373, 0.00102224, 833.41132145, 0.04374849, 83.34113214, 0.09476543, -686.46198373, -0.00102224, -833.41132145, -0.04374849, -83.34113214, -0.09476543, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20011, 11, 0.0, 1007.51503143, 0.01310387, 1007.51503143, 0.0393116, 705.260522, -21545.50034052, 0.05, 2, 0, 70011, 21011, 2, 3)
    ops.uniaxialMaterial('LimitState', 40011, 251.87875786, 0.00021094, 755.63627357, 0.00063282, 2518.78757857, 0.0021094, -251.87875786, -0.00021094, -755.63627357, -0.00063282, -2518.78757857, -0.0021094, 0.4, 0.3, 0.003, 0.0, 0.0, 20011, 2)
    ops.limitCurve('ThreePoint', 10011, 11, 0.0, 434.2274252, 0.02044481, 434.2274252, 0.06133443, 303.95919764, -4077.79164991, 0.05, 2, 0, 70011, 21011, 1, 3)
    ops.uniaxialMaterial('LimitState', 30011, 108.5568563, 9.091e-05, 325.6705689, 0.00027274, 1085.56856301, 0.00090913, -108.5568563, -9.091e-05, -325.6705689, -0.00027274, -1085.56856301, -0.00090913, 0.4, 0.3, 0.003, 0.0, 0.0, 10011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 11, 99999, 'P', 40011, 'Vy', 30011, 'Vz', 20011, 'My', 10011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170011, 70011, 170011, 11, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121011, 121011, 21011, 11, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170012, 12.45, 10.3, 0.0)
    ops.node(121012, 12.45, 10.3, 3.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 12, 170012, 121012, 0.225, 29899976.45938116, 12458323.52474215, 0.00505263, 0.00185625, 0.01160156, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20012, 426.06651427, 0.00071714, 514.57653323, 0.03973903, 51.45765332, 0.10856846, -426.06651427, -0.00071714, -514.57653323, -0.03973903, -51.45765332, -0.10856846, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10012, 197.2716176, 0.00146871, 238.25234252, 0.03042219, 23.82523425, 0.06433261, -197.2716176, -0.00146871, -238.25234252, -0.03042219, -23.82523425, -0.06433261, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20012, 12, 0.0, 402.92020943, 0.01434287, 402.92020943, 0.04302862, 282.0441466, -6018.03787806, 0.05, 2, 0, 70012, 21012, 2, 3)
    ops.uniaxialMaterial('LimitState', 40012, 100.73005236, 0.00015955, 302.19015707, 0.00047865, 1007.30052358, 0.00159551, -100.73005236, -0.00015955, -302.19015707, -0.00047865, -1007.30052358, -0.00159551, 0.4, 0.3, 0.003, 0.0, 0.0, 20012, 2)
    ops.limitCurve('ThreePoint', 10012, 12, 0.0, 236.44708541, 0.02937428, 236.44708541, 0.08812283, 165.51295979, -2014.95705356, 0.05, 2, 0, 70012, 21012, 1, 3)
    ops.uniaxialMaterial('LimitState', 30012, 59.11177135, 9.363e-05, 177.33531406, 0.00028089, 591.11771353, 0.0009363, -59.11177135, -9.363e-05, -177.33531406, -0.00028089, -591.11771353, -0.0009363, 0.4, 0.3, 0.003, 0.0, 0.0, 10012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 12, 99999, 'P', 40012, 'Vy', 30012, 'Vz', 20012, 'My', 10012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170012, 70012, 170012, 12, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121012, 121012, 21012, 12, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170013, 0.0, 15.45, 0.0)
    ops.node(121013, 0.0, 15.45, 3.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 13, 170013, 121013, 0.125, 29480732.14386581, 12283638.39327742, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20013, 129.88916814, 0.0008418, 156.76211528, 0.01995495, 15.67621153, 0.06953079, -129.88916814, -0.0008418, -156.76211528, -0.01995495, -15.67621153, -0.06953079, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10013, 69.51708689, 0.00151673, 83.8995718, 0.01695101, 8.38995718, 0.04680695, -69.51708689, -0.00151673, -83.8995718, -0.01695101, -8.38995718, -0.04680695, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20013, 13, 0.0, 171.76924282, 0.01683592, 171.76924282, 0.05050776, 120.23846997, -2183.6730938, 0.05, 2, 0, 70013, 21013, 2, 3)
    ops.uniaxialMaterial('LimitState', 40013, 42.9423107, 0.00012417, 128.82693211, 0.00037252, 429.42310705, 0.00124174, -42.9423107, -0.00012417, -128.82693211, -0.00037252, -429.42310705, -0.00124174, 0.4, 0.3, 0.003, 0.0, 0.0, 20013, 2)
    ops.limitCurve('ThreePoint', 10013, 13, 0.0, 130.14854734, 0.03033459, 130.14854734, 0.09100378, 91.10398314, -1069.4165884, 0.05, 2, 0, 70013, 21013, 1, 3)
    ops.uniaxialMaterial('LimitState', 30013, 32.53713684, 9.409e-05, 97.61141051, 0.00028226, 325.37136836, 0.00094086, -32.53713684, -9.409e-05, -97.61141051, -0.00028226, -325.37136836, -0.00094086, 0.4, 0.3, 0.003, 0.0, 0.0, 10013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 13, 99999, 'P', 40013, 'Vy', 30013, 'Vz', 20013, 'My', 10013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170013, 70013, 170013, 13, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121013, 121013, 21013, 13, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170014, 2.95, 15.45, 0.0)
    ops.node(121014, 2.95, 15.45, 3.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 14, 170014, 121014, 0.28, 27468781.31711004, 11445325.54879585, 0.00829164, 0.00314417, 0.01642667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20014, 592.05610252, 0.00071727, 718.05525821, 0.05427363, 71.80552582, 0.13429009, -592.05610252, -0.00071727, -718.05525821, -0.05427363, -71.80552582, -0.13429009, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10014, 314.13331989, 0.0012674, 380.985993, 0.04145721, 38.0985993, 0.08195123, -314.13331989, -0.0012674, -380.985993, -0.04145721, -38.0985993, -0.08195123, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20014, 14, 0.0, 584.75687231, 0.01434549, 584.75687231, 0.04303648, 409.32981062, -12387.93639502, 0.05, 2, 0, 70014, 21014, 2, 3)
    ops.uniaxialMaterial('LimitState', 40014, 146.18921808, 0.00020254, 438.56765424, 0.00060762, 1461.89218079, 0.00202541, -146.18921808, -0.00020254, -438.56765424, -0.00060762, -1461.89218079, -0.00202541, 0.4, 0.3, 0.003, 0.0, 0.0, 20014, 2)
    ops.limitCurve('ThreePoint', 10014, 14, 0.0, 324.06357446, 0.02534801, 324.06357446, 0.07604402, 226.84450212, -3957.94943702, 0.05, 2, 0, 70014, 21014, 1, 3)
    ops.uniaxialMaterial('LimitState', 30014, 81.01589361, 0.00011225, 243.04768084, 0.00033674, 810.15893615, 0.00112245, -81.01589361, -0.00011225, -243.04768084, -0.00033674, -810.15893615, -0.00112245, 0.4, 0.3, 0.003, 0.0, 0.0, 10014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 14, 99999, 'P', 40014, 'Vy', 30014, 'Vz', 20014, 'My', 10014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170014, 70014, 170014, 14, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121014, 121014, 21014, 14, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170015, 7.7, 15.45, 0.0)
    ops.node(121015, 7.7, 15.45, 3.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 15, 170015, 121015, 0.45, 29411701.51323947, 12254875.63051645, 0.02179311, 0.00835313, 0.04125, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20015, 1149.15882365, 0.0006653, 1392.16807927, 0.05148331, 139.21680793, 0.12385326, -1149.15882365, -0.0006653, -1392.16807927, -0.05148331, -139.21680793, -0.12385326, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10015, 692.97261217, 0.00105233, 839.51350381, 0.04541034, 83.95135038, 0.09783029, -692.97261217, -0.00105233, -839.51350381, -0.04541034, -83.95135038, -0.09783029, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20015, 15, 0.0, 1154.01717129, 0.01330606, 1154.01717129, 0.03991818, 807.8120199, -30120.78320166, 0.05, 2, 0, 70015, 21015, 2, 3)
    ops.uniaxialMaterial('LimitState', 40015, 288.50429282, 0.00023228, 865.51287847, 0.00069684, 2885.04292822, 0.00232281, -288.50429282, -0.00023228, -865.51287847, -0.00069684, -2885.04292822, -0.00232281, 0.4, 0.3, 0.003, 0.0, 0.0, 20015, 2)
    ops.limitCurve('ThreePoint', 10015, 15, 0.0, 485.42598209, 0.02104661, 485.42598209, 0.06313982, 339.79818746, -5167.94960832, 0.05, 2, 0, 70015, 21015, 1, 3)
    ops.uniaxialMaterial('LimitState', 30015, 121.35649552, 9.771e-05, 364.06948656, 0.00029312, 1213.56495521, 0.00097707, -121.35649552, -9.771e-05, -364.06948656, -0.00029312, -1213.56495521, -0.00097707, 0.4, 0.3, 0.003, 0.0, 0.0, 10015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 15, 99999, 'P', 40015, 'Vy', 30015, 'Vz', 20015, 'My', 10015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170015, 70015, 170015, 15, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121015, 121015, 21015, 15, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170016, 12.45, 15.45, 0.0)
    ops.node(121016, 12.45, 15.45, 3.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 16, 170016, 121016, 0.225, 27811112.37580542, 11587963.48991892, 0.00505263, 0.00185625, 0.01160156, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20016, 431.7436322, 0.00072644, 523.20586054, 0.03650132, 52.32058605, 0.10090305, -431.7436322, -0.00072644, -523.20586054, -0.03650132, -52.32058605, -0.10090305, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10016, 208.96108461, 0.00142788, 253.2282029, 0.02797214, 25.32282029, 0.05970115, -208.96108461, -0.00142788, -253.2282029, -0.02797214, -25.32282029, -0.05970115, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20016, 16, 0.0, 349.65875443, 0.0145288, 349.65875443, 0.04358641, 244.7611281, -4628.45753849, 0.05, 2, 0, 70016, 21016, 2, 3)
    ops.uniaxialMaterial('LimitState', 40016, 87.41468861, 0.00014886, 262.24406582, 0.00044658, 874.14688607, 0.0014886, -87.41468861, -0.00014886, -262.24406582, -0.00044658, -874.14688607, -0.0014886, 0.4, 0.3, 0.003, 0.0, 0.0, 20016, 2)
    ops.limitCurve('ThreePoint', 10016, 16, 0.0, 208.37808238, 0.02855752, 208.37808238, 0.08567256, 145.86465767, -1686.82497407, 0.05, 2, 0, 70016, 21016, 1, 3)
    ops.uniaxialMaterial('LimitState', 30016, 52.0945206, 8.871e-05, 156.28356179, 0.00026614, 520.94520596, 0.00088713, -52.0945206, -8.871e-05, -156.28356179, -0.00026614, -520.94520596, -0.00088713, 0.4, 0.3, 0.003, 0.0, 0.0, 10016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 16, 99999, 'P', 40016, 'Vy', 30016, 'Vz', 20016, 'My', 10016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170016, 70016, 170016, 16, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121016, 121016, 21016, 16, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170017, 0.0, 20.6, 0.0)
    ops.node(121017, 0.0, 20.6, 3.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 17, 170017, 121017, 0.125, 30777085.77421134, 12823785.73925472, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20017, 131.68559777, 0.00082956, 158.53138062, 0.01964419, 15.85313806, 0.07125034, -131.68559777, -0.00082956, -158.53138062, -0.01964419, -15.85313806, -0.07125034, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10017, 71.0772135, 0.00146929, 85.56720687, 0.0166625, 8.55672069, 0.04774116, -71.0772135, -0.00146929, -85.56720687, -0.0166625, -8.55672069, -0.04774116, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20017, 17, 0.0, 173.51937531, 0.01659122, 173.51937531, 0.04977365, 121.46356272, -2081.90931317, 0.05, 2, 0, 70017, 21017, 2, 3)
    ops.uniaxialMaterial('LimitState', 40017, 43.37984383, 0.00012016, 130.13953149, 0.00036047, 433.79843829, 0.00120156, -43.37984383, -0.00012016, -130.13953149, -0.00036047, -433.79843829, -0.00120156, 0.4, 0.3, 0.003, 0.0, 0.0, 20017, 2)
    ops.limitCurve('ThreePoint', 10017, 17, 0.0, 133.53326712, 0.02938575, 133.53326712, 0.08815724, 93.47328699, -1033.68768339, 0.05, 2, 0, 70017, 21017, 1, 3)
    ops.uniaxialMaterial('LimitState', 30017, 33.38331678, 9.247e-05, 100.14995034, 0.0002774, 333.83316781, 0.00092467, -33.38331678, -9.247e-05, -100.14995034, -0.0002774, -333.83316781, -0.00092467, 0.4, 0.3, 0.003, 0.0, 0.0, 10017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 17, 99999, 'P', 40017, 'Vy', 30017, 'Vz', 20017, 'My', 10017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170017, 70017, 170017, 17, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121017, 121017, 21017, 17, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170018, 2.95, 20.6, 0.0)
    ops.node(121018, 2.95, 20.6, 3.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 18, 170018, 121018, 0.28, 31267157.87698254, 13027982.44874272, 0.00829164, 0.00314417, 0.01642667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20018, 580.94205823, 0.00067548, 699.65033034, 0.05244913, 69.96503303, 0.1416822, -580.94205823, -0.00067548, -699.65033034, -0.05244913, -69.96503303, -0.1416822, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10018, 301.15152687, 0.00118496, 362.68808959, 0.04003698, 36.26880896, 0.08519527, -301.15152687, -0.00118496, -362.68808959, -0.04003698, -36.26880896, -0.08519527, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20018, 18, 0.0, 592.44700534, 0.0135096, 592.44700534, 0.0405288, 414.71290374, -10438.24000995, 0.05, 2, 0, 70018, 21018, 2, 3)
    ops.uniaxialMaterial('LimitState', 40018, 148.11175133, 0.00018028, 444.335254, 0.00054083, 1481.11751334, 0.00180276, -148.11175133, -0.00018028, -444.335254, -0.00054083, -1481.11751334, -0.00180276, 0.4, 0.3, 0.003, 0.0, 0.0, 20018, 2)
    ops.limitCurve('ThreePoint', 10018, 18, 0.0, 340.08038307, 0.02369911, 340.08038307, 0.07109732, 238.05626815, -3471.13898393, 0.05, 2, 0, 70018, 21018, 1, 3)
    ops.uniaxialMaterial('LimitState', 30018, 85.02009577, 0.00010348, 255.0602873, 0.00031045, 850.20095767, 0.00103483, -85.02009577, -0.00010348, -255.0602873, -0.00031045, -850.20095767, -0.00103483, 0.4, 0.3, 0.003, 0.0, 0.0, 10018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 18, 99999, 'P', 40018, 'Vy', 30018, 'Vz', 20018, 'My', 10018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170018, 70018, 170018, 18, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121018, 121018, 21018, 18, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170019, 7.7, 20.6, 0.0)
    ops.node(121019, 7.7, 20.6, 3.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 19, 170019, 121019, 0.45, 29326258.13271105, 12219274.22196294, 0.02179311, 0.00835313, 0.04125, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20019, 1095.99559342, 0.00063918, 1327.99677184, 0.04950021, 132.79967718, 0.12173393, -1095.99559342, -0.00063918, -1327.99677184, -0.04950021, -132.79967718, -0.12173393, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10019, 658.54103014, 0.00099744, 797.94149484, 0.04364725, 79.79414948, 0.09596852, -658.54103014, -0.00099744, -797.94149484, -0.04364725, -79.79414948, -0.09596852, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20019, 19, 0.0, 1013.64472679, 0.01278362, 1013.64472679, 0.03835086, 709.55130875, -20390.28081795, 0.05, 2, 0, 70019, 21019, 2, 3)
    ops.uniaxialMaterial('LimitState', 40019, 253.4111817, 0.00020462, 760.23354509, 0.00061386, 2534.11181697, 0.00204621, -253.4111817, -0.00020462, -760.23354509, -0.00061386, -2534.11181697, -0.00204621, 0.4, 0.3, 0.003, 0.0, 0.0, 20019, 2)
    ops.limitCurve('ThreePoint', 10019, 19, 0.0, 442.76317334, 0.01994885, 442.76317334, 0.05984656, 309.93422134, -3926.37513417, 0.05, 2, 0, 70019, 21019, 1, 3)
    ops.uniaxialMaterial('LimitState', 30019, 110.69079334, 8.938e-05, 332.07238001, 0.00026814, 1106.90793335, 0.00089379, -110.69079334, -8.938e-05, -332.07238001, -0.00026814, -1106.90793335, -0.00089379, 0.4, 0.3, 0.003, 0.0, 0.0, 10019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 19, 99999, 'P', 40019, 'Vy', 30019, 'Vz', 20019, 'My', 10019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170019, 70019, 170019, 19, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121019, 121019, 21019, 19, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170020, 12.45, 20.6, 0.0)
    ops.node(121020, 12.45, 20.6, 3.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 20, 170020, 121020, 0.225, 31207483.07457853, 13003117.94774106, 0.00505263, 0.00185625, 0.01160156, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20020, 445.60011826, 0.00071337, 536.59059057, 0.03538315, 53.65905906, 0.10647761, -445.60011826, -0.00071337, -536.59059057, -0.03538315, -53.65905906, -0.10647761, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10020, 216.11969499, 0.00138021, 260.25081686, 0.02710451, 26.02508169, 0.06213085, -216.11969499, -0.00138021, -260.25081686, -0.02710451, -26.02508169, -0.06213085, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20020, 20, 0.0, 392.32936088, 0.01426746, 392.32936088, 0.04280238, 274.63055261, -5108.74533092, 0.05, 2, 0, 70020, 21020, 2, 3)
    ops.uniaxialMaterial('LimitState', 40020, 98.08234022, 0.00014885, 294.24702066, 0.00044654, 980.82340219, 0.00148848, -98.08234022, -0.00014885, -294.24702066, -0.00044654, -980.82340219, -0.00148848, 0.4, 0.3, 0.003, 0.0, 0.0, 20020, 2)
    ops.limitCurve('ThreePoint', 10020, 20, 0.0, 236.58506404, 0.02760422, 236.58506404, 0.08281267, 165.60954483, -1801.83802163, 0.05, 2, 0, 70020, 21020, 1, 3)
    ops.uniaxialMaterial('LimitState', 30020, 59.14626601, 8.976e-05, 177.43879803, 0.00026928, 591.46266011, 0.00089759, -59.14626601, -8.976e-05, -177.43879803, -0.00026928, -591.46266011, -0.00089759, 0.4, 0.3, 0.003, 0.0, 0.0, 10020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 20, 99999, 'P', 40020, 'Vy', 30020, 'Vz', 20020, 'My', 10020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170020, 70020, 170020, 20, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121020, 121020, 21020, 20, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170021, 0.0, 25.75, 0.0)
    ops.node(121021, 0.0, 25.75, 3.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 21, 170021, 121021, 0.125, 26974783.30074484, 11239493.04197701, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20021, 129.18812205, 0.00088543, 156.37382109, 0.01618012, 15.63738211, 0.06087011, -129.18812205, -0.00088543, -156.37382109, -0.01618012, -15.63738211, -0.06087011, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10021, 68.54542215, 0.00164097, 82.96977624, 0.01399175, 8.29697762, 0.04090531, -68.54542215, -0.00164097, -82.96977624, -0.01399175, -8.29697762, -0.04090531, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20021, 21, 0.0, 146.57045344, 0.0177087, 146.57045344, 0.0531261, 102.59931741, -1712.96618616, 0.05, 2, 0, 70021, 21021, 2, 3)
    ops.uniaxialMaterial('LimitState', 40021, 36.64261336, 0.0001158, 109.92784008, 0.0003474, 366.42613361, 0.00115801, -36.64261336, -0.0001158, -109.92784008, -0.0003474, -366.42613361, -0.00115801, 0.4, 0.3, 0.003, 0.0, 0.0, 20021, 2)
    ops.limitCurve('ThreePoint', 10021, 21, 0.0, 107.67009341, 0.03281938, 107.67009341, 0.09845814, 75.36906539, -902.03207449, 0.05, 2, 0, 70021, 21021, 1, 3)
    ops.uniaxialMaterial('LimitState', 30021, 26.91752335, 8.507e-05, 80.75257006, 0.0002552, 269.17523353, 0.00085067, -26.91752335, -8.507e-05, -80.75257006, -0.0002552, -269.17523353, -0.00085067, 0.4, 0.3, 0.003, 0.0, 0.0, 10021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 21, 99999, 'P', 40021, 'Vy', 30021, 'Vz', 20021, 'My', 10021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170021, 70021, 170021, 21, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121021, 121021, 21021, 21, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170022, 2.95, 25.75, 0.0)
    ops.node(121022, 2.95, 25.75, 3.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 22, 170022, 121022, 0.28, 29374857.33694636, 12239523.89039432, 0.00829164, 0.00314417, 0.01642667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20022, 593.40048423, 0.00070594, 717.62344748, 0.05110547, 71.76234475, 0.1362509, -593.40048423, -0.00070594, -717.62344748, -0.05110547, -71.76234475, -0.1362509, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10022, 309.6505715, 0.00125423, 374.47308612, 0.0390751, 37.44730861, 0.08216474, -309.6505715, -0.00125423, -374.47308612, -0.0390751, -37.44730861, -0.08216474, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20022, 22, 0.0, 535.36212632, 0.01411871, 535.36212632, 0.04235613, 374.75348843, -8748.62676211, 0.05, 2, 0, 70022, 21022, 2, 3)
    ops.uniaxialMaterial('LimitState', 40022, 133.84053158, 0.0001734, 401.52159474, 0.0005202, 1338.4053158, 0.001734, -133.84053158, -0.0001734, -401.52159474, -0.0005202, -1338.4053158, -0.001734, 0.4, 0.3, 0.003, 0.0, 0.0, 20022, 2)
    ops.limitCurve('ThreePoint', 10022, 22, 0.0, 308.69691949, 0.02508465, 308.69691949, 0.07525394, 216.08784365, -3040.89657819, 0.05, 2, 0, 70022, 21022, 1, 3)
    ops.uniaxialMaterial('LimitState', 30022, 77.17422987, 9.998e-05, 231.52268962, 0.00029995, 771.74229874, 0.00099985, -77.17422987, -9.998e-05, -231.52268962, -0.00029995, -771.74229874, -0.00099985, 0.4, 0.3, 0.003, 0.0, 0.0, 10022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 22, 99999, 'P', 40022, 'Vy', 30022, 'Vz', 20022, 'My', 10022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170022, 70022, 170022, 22, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121022, 121022, 21022, 22, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170023, 7.7, 25.75, 0.0)
    ops.node(121023, 7.7, 25.75, 3.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 23, 170023, 121023, 0.45, 26806364.07744209, 11169318.36560087, 0.02179311, 0.00835313, 0.04125, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20023, 1053.03743177, 0.00063642, 1281.14801265, 0.04984669, 128.11480126, 0.11730755, -1053.03743177, -0.00063642, -1281.14801265, -0.04984669, -128.11480126, -0.11730755, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10023, 638.9968964, 0.00099085, 777.41738252, 0.04394549, 77.74173825, 0.09280963, -638.9968964, -0.00099085, -777.41738252, -0.04394549, -77.74173825, -0.09280963, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20023, 23, 0.0, 961.2509482, 0.01272849, 961.2509482, 0.03818547, 672.87566374, -20662.85893714, 0.05, 2, 0, 70023, 21023, 2, 3)
    ops.uniaxialMaterial('LimitState', 40023, 240.31273705, 0.00021229, 720.93821115, 0.00063686, 2403.1273705, 0.00212286, -240.31273705, -0.00021229, -720.93821115, -0.00063686, -2403.1273705, -0.00212286, 0.4, 0.3, 0.003, 0.0, 0.0, 20023, 2)
    ops.limitCurve('ThreePoint', 10023, 23, 0.0, 411.24378658, 0.01981705, 411.24378658, 0.05945115, 287.8706506, -3963.11089768, 0.05, 2, 0, 70023, 21023, 1, 3)
    ops.uniaxialMaterial('LimitState', 30023, 102.81094664, 9.082e-05, 308.43283993, 0.00027246, 1028.10946644, 0.0009082, -102.81094664, -9.082e-05, -308.43283993, -0.00027246, -1028.10946644, -0.0009082, 0.4, 0.3, 0.003, 0.0, 0.0, 10023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 23, 99999, 'P', 40023, 'Vy', 30023, 'Vz', 20023, 'My', 10023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170023, 70023, 170023, 23, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121023, 121023, 21023, 23, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170024, 12.45, 25.75, 0.0)
    ops.node(121024, 12.45, 25.75, 3.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 24, 170024, 121024, 0.225, 29034381.50609666, 12097658.96087361, 0.00505263, 0.00185625, 0.01160156, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20024, 425.57542585, 0.00069709, 514.80655412, 0.03932054, 51.48065541, 0.10643558, -425.57542585, -0.00069709, -514.80655412, -0.03932054, -51.48065541, -0.10643558, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10024, 207.82346553, 0.0013351, 251.39816741, 0.02999295, 25.13981674, 0.06305873, -207.82346553, -0.0013351, -251.39816741, -0.02999295, -25.13981674, -0.06305873, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20024, 24, 0.0, 395.81170809, 0.01394175, 395.81170809, 0.04182524, 277.06819567, -6038.22068089, 0.05, 2, 0, 70024, 21024, 2, 3)
    ops.uniaxialMaterial('LimitState', 40024, 98.95292702, 0.00016141, 296.85878107, 0.00048423, 989.52927024, 0.00161409, -98.95292702, -0.00016141, -296.85878107, -0.00048423, -989.52927024, -0.00161409, 0.4, 0.3, 0.003, 0.0, 0.0, 20024, 2)
    ops.limitCurve('ThreePoint', 10024, 24, 0.0, 230.77716309, 0.02670204, 230.77716309, 0.08010611, 161.54401417, -2020.02175157, 0.05, 2, 0, 70024, 21024, 1, 3)
    ops.uniaxialMaterial('LimitState', 30024, 57.69429077, 9.411e-05, 173.08287232, 0.00028233, 576.94290773, 0.00094109, -57.69429077, -9.411e-05, -173.08287232, -0.00028233, -576.94290773, -0.00094109, 0.4, 0.3, 0.003, 0.0, 0.0, 10024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 24, 99999, 'P', 40024, 'Vy', 30024, 'Vz', 20024, 'My', 10024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170024, 70024, 170024, 24, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121024, 121024, 21024, 24, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170025, 0.0, 30.9, 0.0)
    ops.node(121025, 0.0, 30.9, 3.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 25, 170025, 121025, 0.09, 27146703.3221064, 11311126.384211, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20025, 57.04430593, 0.00127592, 69.24102499, 0.01764936, 6.9241025, 0.0602522, -57.04430593, -0.00127592, -69.24102499, -0.01764936, -6.9241025, -0.0602522, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10025, 52.51239599, 0.00127592, 63.74014135, 0.01764936, 6.37401413, 0.0602522, -52.51239599, -0.00127592, -63.74014135, -0.01764936, -6.37401413, -0.0602522, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20025, 25, 0.0, 96.20762512, 0.02551844, 96.20762512, 0.07655533, 67.34533759, -1081.38925292, 0.05, 2, 0, 70025, 21025, 2, 3)
    ops.uniaxialMaterial('LimitState', 40025, 24.05190628, 0.0001049, 72.15571884, 0.00031471, 240.51906281, 0.00104902, -24.05190628, -0.0001049, -72.15571884, -0.00031471, -240.51906281, -0.00104902, 0.4, 0.3, 0.003, 0.0, 0.0, 20025, 2)
    ops.limitCurve('ThreePoint', 10025, 25, 0.0, 96.20762512, 0.02551844, 96.20762512, 0.07655533, 67.34533759, -1081.38925292, 0.05, 2, 0, 70025, 21025, 1, 3)
    ops.uniaxialMaterial('LimitState', 30025, 24.05190628, 0.0001049, 72.15571884, 0.00031471, 240.51906281, 0.00104902, -24.05190628, -0.0001049, -72.15571884, -0.00031471, -240.51906281, -0.00104902, 0.4, 0.3, 0.003, 0.0, 0.0, 10025, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 25, 99999, 'P', 40025, 'Vy', 30025, 'Vz', 20025, 'My', 10025, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170025, 70025, 170025, 25, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121025, 121025, 21025, 25, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170026, 2.95, 30.9, 0.0)
    ops.node(121026, 2.95, 30.9, 3.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 26, 170026, 121026, 0.27, 27411289.06153249, 11421370.4423052, 0.00984074, 0.00891, 0.00501188, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20026, 381.34111442, 0.0009515, 463.96153551, 0.04303972, 46.39615355, 0.09851029, -381.34111442, -0.0009515, -463.96153551, -0.04303972, -46.39615355, -0.09851029, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10026, 372.07251382, 0.00078484, 452.68482286, 0.0473253, 45.26848229, 0.11773819, -372.07251382, -0.00078484, -452.68482286, -0.0473253, -45.26848229, -0.11773819, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20026, 26, 0.0, 314.22844796, 0.01902997, 314.22844796, 0.0570899, 219.95991357, -4757.84490683, 0.05, 2, 0, 70026, 21026, 2, 3)
    ops.uniaxialMaterial('LimitState', 40026, 78.55711199, 0.00011311, 235.67133597, 0.00033932, 785.57111989, 0.00113106, -78.55711199, -0.00011311, -235.67133597, -0.00033932, -785.57111989, -0.00113106, 0.4, 0.3, 0.003, 0.0, 0.0, 20026, 2)
    ops.limitCurve('ThreePoint', 10026, 26, 0.0, 373.21941414, 0.01569684, 373.21941414, 0.04709053, 261.2535899, -7228.7656011, 0.05, 2, 0, 70026, 21026, 1, 3)
    ops.uniaxialMaterial('LimitState', 30026, 93.30485353, 0.00013434, 279.9145606, 0.00040302, 933.04853535, 0.0013434, -93.30485353, -0.00013434, -279.9145606, -0.00040302, -933.04853535, -0.0013434, 0.4, 0.3, 0.003, 0.0, 0.0, 10026, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 26, 99999, 'P', 40026, 'Vy', 30026, 'Vz', 20026, 'My', 10026, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170026, 70026, 170026, 26, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121026, 121026, 21026, 26, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170027, 7.7, 30.9, 0.0)
    ops.node(121027, 7.7, 30.9, 3.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 27, 170027, 121027, 0.35, 29786223.56417813, 12410926.48507422, 0.01632638, 0.01572083, 0.00802083, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20027, 624.48792816, 0.0009467, 756.57084138, 0.05170178, 75.65708414, 0.12421593, -624.48792816, -0.0009467, -756.57084138, -0.05170178, -75.65708414, -0.12421593, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10027, 646.13830828, 0.00075838, 782.80040574, 0.05028776, 78.28004057, 0.11871656, -646.13830828, -0.00075838, -782.80040574, -0.05028776, -78.28004057, -0.11871656, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20027, 27, 0.0, 416.2856454, 0.0189341, 416.2856454, 0.05680229, 291.39995178, -5695.59381683, 0.05, 2, 0, 70027, 21027, 2, 3)
    ops.uniaxialMaterial('LimitState', 40027, 104.07141135, 0.00010638, 312.21423405, 0.00031913, 1040.71411351, 0.00106376, -104.07141135, -0.00010638, -312.21423405, -0.00031913, -1040.71411351, -0.00106376, 0.4, 0.3, 0.003, 0.0, 0.0, 20027, 2)
    ops.limitCurve('ThreePoint', 10027, 27, 0.0, 675.52580527, 0.01516762, 675.52580527, 0.04550287, 472.86806369, -17668.11039141, 0.05, 2, 0, 70027, 21027, 1, 3)
    ops.uniaxialMaterial('LimitState', 30027, 168.88145132, 0.00017262, 506.64435395, 0.00051786, 1688.81451317, 0.00172621, -168.88145132, -0.00017262, -506.64435395, -0.00051786, -1688.81451317, -0.00172621, 0.4, 0.3, 0.003, 0.0, 0.0, 10027, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 27, 99999, 'P', 40027, 'Vy', 30027, 'Vz', 20027, 'My', 10027, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170027, 70027, 170027, 27, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121027, 121027, 21027, 27, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170028, 12.45, 30.9, 0.0)
    ops.node(121028, 12.45, 30.9, 3.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 28, 170028, 121028, 0.1575, 28056698.06312323, 11690290.85963468, 0.00337604, 0.00292359, 0.00176859, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20028, 152.74522372, 0.00111351, 185.40597842, 0.021699, 18.54059784, 0.06141201, -152.74522372, -0.00111351, -185.40597842, -0.021699, -18.54059784, -0.06141201, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10028, 153.22076967, 0.00091117, 185.98320801, 0.02321047, 18.5983208, 0.07121866, -153.22076967, -0.00091117, -185.98320801, -0.02321047, -18.5983208, -0.07121866, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20028, 28, 0.0, 158.78644218, 0.02227018, 158.78644218, 0.06681054, 111.15050953, -1599.73759922, 0.05, 2, 0, 70028, 21028, 2, 3)
    ops.uniaxialMaterial('LimitState', 40028, 39.69661054, 9.573e-05, 119.08983163, 0.00028718, 396.96610545, 0.00095726, -39.69661054, -9.573e-05, -119.08983163, -0.00028718, -396.96610545, -0.00095726, 0.4, 0.3, 0.003, 0.0, 0.0, 20028, 2)
    ops.limitCurve('ThreePoint', 10028, 28, 0.0, 176.62627029, 0.01822346, 176.62627029, 0.05467037, 123.6383892, -2158.86041302, 0.05, 2, 0, 70028, 21028, 1, 3)
    ops.uniaxialMaterial('LimitState', 30028, 44.15656757, 0.00010648, 132.46970272, 0.00031944, 441.56567573, 0.00106481, -44.15656757, -0.00010648, -132.46970272, -0.00031944, -441.56567573, -0.00106481, 0.4, 0.3, 0.003, 0.0, 0.0, 10028, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 28, 99999, 'P', 40028, 'Vy', 30028, 'Vz', 20028, 'My', 10028, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170028, 70028, 170028, 28, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121028, 121028, 21028, 28, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171003, 7.7, 0.0, 3.975)
    ops.node(122003, 7.7, 0.0, 6.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1003, 171003, 122003, 0.35, 27242382.07450357, 11350992.53104316, 0.01632638, 0.01572083, 0.00802083, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21003, 238.12778853, 0.00077175, 290.47772609, 0.01803477, 29.04777261, 0.04609809, -238.12778853, -0.00077175, -290.47772609, -0.01803477, -29.04777261, -0.04609809, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11003, 426.46578284, 0.00065071, 520.21988538, 0.0194913, 52.02198854, 0.05402367, -426.46578284, -0.00065071, -520.21988538, -0.0194913, -52.02198854, -0.05402367, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21003, 1003, 0.0, 278.03171812, 0.01543507, 278.03171812, 0.0463052, 194.62220268, -2223.98138375, 0.05, 2, 0, 71003, 22003, 2, 3)
    ops.uniaxialMaterial('LimitState', 41003, 69.50792953, 5.984e-05, 208.52378859, 0.00017951, 695.07929529, 0.00059835, -69.50792953, -5.984e-05, -208.52378859, -0.00017951, -695.07929529, -0.00059835, 0.4, 0.3, 0.003, 0.0, 0.0, 21003, 2)
    ops.limitCurve('ThreePoint', 11003, 1003, 0.0, 389.24440536, 0.01301419, 389.24440536, 0.03904258, 272.47108376, -3255.63312464, 0.05, 2, 0, 71003, 22003, 1, 3)
    ops.uniaxialMaterial('LimitState', 31003, 97.31110134, 8.377e-05, 291.93330402, 0.00025131, 973.11101341, 0.0008377, -97.31110134, -8.377e-05, -291.93330402, -0.00025131, -973.11101341, -0.0008377, 0.4, 0.3, 0.003, 0.0, 0.0, 11003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1003, 99999, 'P', 41003, 'Vy', 31003, 'Vz', 21003, 'My', 11003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171003, 71003, 171003, 1003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122003, 122003, 22003, 1003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171004, 12.45, 0.0, 3.95)
    ops.node(122004, 12.45, 0.0, 6.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1004, 171004, 122004, 0.1575, 28024539.16208893, 11676891.31753705, 0.00337604, 0.00292359, 0.00176859, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21004, 100.4133303, 0.00091041, 122.17707605, 0.02296084, 12.21770761, 0.06551616, -100.4133303, -0.00091041, -122.17707605, -0.02296084, -12.21770761, -0.06551616, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11004, 108.93123824, 0.00076657, 132.54116897, 0.02465277, 13.2541169, 0.07609696, -108.93123824, -0.00076657, -132.54116897, -0.02465277, -13.2541169, -0.07609696, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21004, 1004, 0.0, 159.88362519, 0.01820822, 159.88362519, 0.05462466, 111.91853763, -2564.1147124, 0.05, 2, 0, 71004, 22004, 2, 3)
    ops.uniaxialMaterial('LimitState', 41004, 39.9709063, 7.433e-05, 119.91271889, 0.00022299, 399.70906297, 0.0007433, -39.9709063, -7.433e-05, -119.91271889, -0.00022299, -399.70906297, -0.0007433, 0.4, 0.3, 0.003, 0.0, 0.0, 21004, 2)
    ops.limitCurve('ThreePoint', 11004, 1004, 0.0, 180.65576274, 0.01533148, 180.65576274, 0.04599445, 126.45903392, -3640.00379984, 0.05, 2, 0, 71004, 22004, 1, 3)
    ops.uniaxialMaterial('LimitState', 31004, 45.16394068, 8.399e-05, 135.49182205, 0.00025196, 451.63940685, 0.00083987, -45.16394068, -8.399e-05, -135.49182205, -0.00025196, -451.63940685, -0.00083987, 0.4, 0.3, 0.003, 0.0, 0.0, 11004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1004, 99999, 'P', 41004, 'Vy', 31004, 'Vz', 21004, 'My', 11004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171004, 71004, 171004, 1004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122004, 122004, 22004, 1004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171005, 0.0, 5.15, 3.95)
    ops.node(122005, 0.0, 5.15, 6.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1005, 171005, 122005, 0.1125, 28680077.64586187, 11950032.35244245, 0.00152995, 0.00064453, 0.00208828, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21005, 102.72096287, 0.00080945, 124.39297032, 0.01674499, 12.43929703, 0.06810707, -102.72096287, -0.00080945, -124.39297032, -0.01674499, -12.43929703, -0.06810707, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11005, 61.94704578, 0.00129918, 75.01659653, 0.01455567, 7.50165965, 0.04774677, -61.94704578, -0.00129918, -75.01659653, -0.01455567, -7.50165965, -0.04774677, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21005, 1005, 0.0, 136.71166821, 0.01618902, 136.71166821, 0.04856706, 95.69816774, -2153.65877598, 0.05, 2, 0, 71005, 22005, 2, 3)
    ops.uniaxialMaterial('LimitState', 41005, 34.17791705, 8.695e-05, 102.53375115, 0.00026084, 341.77917051, 0.00086946, -34.17791705, -8.695e-05, -102.53375115, -0.00026084, -341.77917051, -0.00086946, 0.4, 0.3, 0.003, 0.0, 0.0, 21005, 2)
    ops.limitCurve('ThreePoint', 11005, 1005, 0.0, 101.43358806, 0.02598357, 101.43358806, 0.07795072, 71.00351164, -1144.47925001, 0.05, 2, 0, 71005, 22005, 1, 3)
    ops.uniaxialMaterial('LimitState', 31005, 25.35839701, 6.451e-05, 76.07519104, 0.00019353, 253.58397015, 0.0006451, -25.35839701, -6.451e-05, -76.07519104, -0.00019353, -253.58397015, -0.0006451, 0.4, 0.3, 0.003, 0.0, 0.0, 11005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1005, 99999, 'P', 41005, 'Vy', 31005, 'Vz', 21005, 'My', 11005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171005, 71005, 171005, 1005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122005, 122005, 22005, 1005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171006, 2.95, 5.15, 3.975)
    ops.node(122006, 2.95, 5.15, 6.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1006, 171006, 122006, 0.2975, 29209679.05183822, 12170699.60493259, 0.00900415, 0.00334068, 0.01970318, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21006, 497.14842643, 0.00062079, 602.87396918, 0.03786317, 60.28739692, 0.10225653, -497.14842643, -0.00062079, -602.87396918, -0.03786317, -60.28739692, -0.10225653, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11006, 171.61107915, 0.00101368, 208.10656726, 0.02918723, 20.81065673, 0.06240366, -171.61107915, -0.00101368, -208.10656726, -0.02918723, -20.81065673, -0.06240366, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21006, 1006, 0.0, 545.16906993, 0.01241572, 545.16906993, 0.03724717, 381.61834895, -7520.70806155, 0.05, 2, 0, 71006, 22006, 2, 3)
    ops.uniaxialMaterial('LimitState', 41006, 136.29226748, 0.00012873, 408.87680245, 0.0003862, 1362.92267483, 0.00128734, -136.29226748, -0.00012873, -408.87680245, -0.0003862, -1362.92267483, -0.00128734, 0.4, 0.3, 0.003, 0.0, 0.0, 21006, 2)
    ops.limitCurve('ThreePoint', 11006, 1006, 0.0, 264.39987546, 0.02027357, 264.39987546, 0.06082071, 185.07991282, -2546.04743199, 0.05, 2, 0, 71006, 22006, 1, 3)
    ops.uniaxialMaterial('LimitState', 31006, 66.09996886, 6.243e-05, 198.29990659, 0.0001873, 660.99968864, 0.00062435, -66.09996886, -6.243e-05, -198.29990659, -0.0001873, -660.99968864, -0.00062435, 0.4, 0.3, 0.003, 0.0, 0.0, 11006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1006, 99999, 'P', 41006, 'Vy', 31006, 'Vz', 21006, 'My', 11006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171006, 71006, 171006, 1006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122006, 122006, 22006, 1006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171007, 7.7, 5.15, 3.975)
    ops.node(122007, 7.7, 5.15, 6.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1007, 171007, 122007, 0.45, 27916710.31017665, 11631962.62924027, 0.02179311, 0.00835313, 0.04125, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21007, 890.1073593, 0.00063604, 1083.54945896, 0.02973752, 108.3549459, 0.07255892, -890.1073593, -0.00063604, -1083.54945896, -0.02973752, -108.3549459, -0.07255892, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11007, 312.2168261, 0.00093069, 380.06917869, 0.02440255, 38.00691787, 0.0501174, -312.2168261, -0.00093069, -380.06917869, -0.02440255, -38.00691787, -0.0501174, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21007, 1007, 0.0, 692.60302076, 0.01272075, 692.60302076, 0.03816226, 484.82211453, -6655.69607, 0.05, 2, 0, 71007, 22007, 2, 3)
    ops.uniaxialMaterial('LimitState', 41007, 173.15075519, 0.00011313, 519.45226557, 0.0003394, 1731.5075519, 0.00113132, -173.15075519, -0.00011313, -519.45226557, -0.0003394, -1731.5075519, -0.00113132, 0.4, 0.3, 0.003, 0.0, 0.0, 21007, 2)
    ops.limitCurve('ThreePoint', 11007, 1007, 0.0, 339.87976927, 0.01861373, 339.87976927, 0.05584118, 237.91583849, -2689.69326772, 0.05, 2, 0, 71007, 22007, 1, 3)
    ops.uniaxialMaterial('LimitState', 31007, 84.96994232, 5.552e-05, 254.90982695, 0.00016655, 849.69942316, 0.00055517, -84.96994232, -5.552e-05, -254.90982695, -0.00016655, -849.69942316, -0.00055517, 0.4, 0.3, 0.003, 0.0, 0.0, 11007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1007, 99999, 'P', 41007, 'Vy', 31007, 'Vz', 21007, 'My', 11007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171007, 71007, 171007, 1007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122007, 122007, 22007, 1007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171008, 12.45, 5.15, 3.95)
    ops.node(122008, 12.45, 5.15, 6.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1008, 171008, 122008, 0.225, 29991765.57221067, 12496568.98842111, 0.00505263, 0.00185625, 0.01160156, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21008, 349.63918482, 0.00062442, 423.1433706, 0.03618645, 42.31433706, 0.10996601, -349.63918482, -0.00062442, -423.1433706, -0.03618645, -42.31433706, -0.10996601, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11008, 113.58685925, 0.00107381, 137.46607521, 0.02746015, 13.74660752, 0.06380936, -113.58685925, -0.00107381, -137.46607521, -0.02746015, -13.74660752, -0.06380936, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21008, 1008, 0.0, 416.88540747, 0.01248835, 416.88540747, 0.03746504, 291.81978523, -7034.76437806, 0.05, 2, 0, 71008, 22008, 2, 3)
    ops.uniaxialMaterial('LimitState', 41008, 104.22135187, 0.00012677, 312.6640556, 0.0003803, 1042.21351867, 0.00126768, -104.22135187, -0.00012677, -312.6640556, -0.0003803, -1042.21351867, -0.00126768, 0.4, 0.3, 0.003, 0.0, 0.0, 21008, 2)
    ops.limitCurve('ThreePoint', 11008, 1008, 0.0, 214.90844986, 0.02147618, 214.90844986, 0.06442853, 150.4359149, -2205.93823568, 0.05, 2, 0, 71008, 22008, 1, 3)
    ops.uniaxialMaterial('LimitState', 31008, 53.72711246, 6.535e-05, 161.18133739, 0.00019605, 537.27112465, 0.0006535, -53.72711246, -6.535e-05, -161.18133739, -0.00019605, -537.27112465, -0.0006535, 0.4, 0.3, 0.003, 0.0, 0.0, 11008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1008, 99999, 'P', 41008, 'Vy', 31008, 'Vz', 21008, 'My', 11008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171008, 71008, 171008, 1008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122008, 122008, 22008, 1008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171009, 0.0, 10.3, 3.95)
    ops.node(122009, 0.0, 10.3, 6.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1009, 171009, 122009, 0.125, 29277024.7654951, 12198760.31895629, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21009, 124.66940372, 0.00074338, 150.95383188, 0.01762901, 15.09538319, 0.07134229, -124.66940372, -0.00074338, -150.95383188, -0.01762901, -15.09538319, -0.07134229, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11009, 58.88900752, 0.0012605, 71.30475542, 0.014896, 7.13047554, 0.04724363, -58.88900752, -0.0012605, -71.30475542, -0.014896, -7.13047554, -0.04724363, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21009, 1009, 0.0, 161.41273002, 0.01486768, 161.41273002, 0.04460305, 112.98891101, -2465.61970863, 0.05, 2, 0, 71009, 22009, 2, 3)
    ops.uniaxialMaterial('LimitState', 41009, 40.3531825, 9.051e-05, 121.05954751, 0.00027152, 403.53182504, 0.00090506, -40.3531825, -9.051e-05, -121.05954751, -0.00027152, -403.53182504, -0.00090506, 0.4, 0.3, 0.003, 0.0, 0.0, 21009, 2)
    ops.limitCurve('ThreePoint', 11009, 1009, 0.0, 114.49901752, 0.02521002, 114.49901752, 0.07563006, 80.14931226, -1144.60390992, 0.05, 2, 0, 71009, 22009, 1, 3)
    ops.uniaxialMaterial('LimitState', 31009, 28.62475438, 6.42e-05, 85.87426314, 0.0001926, 286.2475438, 0.00064201, -28.62475438, -6.42e-05, -85.87426314, -0.0001926, -286.2475438, -0.00064201, 0.4, 0.3, 0.003, 0.0, 0.0, 11009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1009, 99999, 'P', 41009, 'Vy', 31009, 'Vz', 21009, 'My', 11009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171009, 71009, 171009, 1009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122009, 122009, 22009, 1009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171010, 2.95, 10.3, 3.975)
    ops.node(122010, 2.95, 10.3, 6.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1010, 171010, 122010, 0.28, 29374815.93712174, 12239506.64046739, 0.00829164, 0.00314417, 0.01642667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21010, 475.83642539, 0.00064205, 576.76201841, 0.03864541, 57.67620184, 0.1030316, -475.83642539, -0.00064205, -576.76201841, -0.03864541, -57.67620184, -0.1030316, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11010, 174.90925308, 0.00102162, 212.00775826, 0.03025944, 21.20077583, 0.06482677, -174.90925308, -0.00102162, -212.00775826, -0.03025944, -21.20077583, -0.06482677, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21010, 1010, 0.0, 516.68609161, 0.01284101, 516.68609161, 0.03852304, 361.68026413, -8166.2875063, 0.05, 2, 0, 71010, 22010, 2, 3)
    ops.uniaxialMaterial('LimitState', 41010, 129.1715229, 0.00012891, 387.51456871, 0.00038672, 1291.71522902, 0.00128905, -129.1715229, -0.00012891, -387.51456871, -0.00038672, -1291.71522902, -0.00128905, 0.4, 0.3, 0.003, 0.0, 0.0, 21010, 2)
    ops.limitCurve('ThreePoint', 11010, 1010, 0.0, 264.04104373, 0.02043245, 264.04104373, 0.06129734, 184.82873061, -2846.44961694, 0.05, 2, 0, 71010, 22010, 1, 3)
    ops.uniaxialMaterial('LimitState', 31010, 66.01026093, 6.587e-05, 198.0307828, 0.00019762, 660.10260933, 0.00065874, -66.01026093, -6.587e-05, -198.0307828, -0.00019762, -660.10260933, -0.00065874, 0.4, 0.3, 0.003, 0.0, 0.0, 11010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1010, 99999, 'P', 41010, 'Vy', 31010, 'Vz', 21010, 'My', 11010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171010, 71010, 171010, 1010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122010, 122010, 22010, 1010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171011, 7.7, 10.3, 3.975)
    ops.node(122011, 7.7, 10.3, 6.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1011, 171011, 122011, 0.45, 28849840.55794065, 12020766.89914194, 0.02179311, 0.00835313, 0.04125, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21011, 855.20174922, 0.00060967, 1039.15202559, 0.03186974, 103.91520256, 0.07544308, -855.20174922, -0.00060967, -1039.15202559, -0.03186974, -103.91520256, -0.07544308, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11011, 301.20272508, 0.00087354, 365.99015632, 0.0260864, 36.59901563, 0.05225281, -301.20272508, -0.00087354, -365.99015632, -0.0260864, -36.59901563, -0.05225281, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21011, 1011, 0.0, 749.14057506, 0.01219342, 749.14057506, 0.03658026, 524.39840254, -8310.51862231, 0.05, 2, 0, 71011, 22011, 2, 3)
    ops.uniaxialMaterial('LimitState', 41011, 187.28514376, 0.00011841, 561.85543129, 0.00035523, 1872.85143764, 0.00118409, -187.28514376, -0.00011841, -561.85543129, -0.00035523, -1872.85143764, -0.00118409, 0.4, 0.3, 0.003, 0.0, 0.0, 21011, 2)
    ops.limitCurve('ThreePoint', 11011, 1011, 0.0, 366.6614374, 0.0174707, 366.6614374, 0.0524121, 256.66300618, -3155.41392977, 0.05, 2, 0, 71011, 22011, 1, 3)
    ops.uniaxialMaterial('LimitState', 31011, 91.66535935, 5.795e-05, 274.99607805, 0.00017386, 916.65359349, 0.00057954, -91.66535935, -5.795e-05, -274.99607805, -0.00017386, -916.65359349, -0.00057954, 0.4, 0.3, 0.003, 0.0, 0.0, 11011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1011, 99999, 'P', 41011, 'Vy', 31011, 'Vz', 21011, 'My', 11011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171011, 71011, 171011, 1011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122011, 122011, 22011, 1011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171012, 12.45, 10.3, 3.95)
    ops.node(122012, 12.45, 10.3, 6.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1012, 171012, 122012, 0.225, 30830255.90546865, 12845939.96061194, 0.00505263, 0.00185625, 0.01160156, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21012, 346.66527602, 0.00063142, 418.69018013, 0.03656663, 41.86901801, 0.11148265, -346.66527602, -0.00063142, -418.69018013, -0.03656663, -41.86901801, -0.11148265, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11012, 112.58872075, 0.00112453, 135.98071406, 0.02778776, 13.59807141, 0.06469687, -112.58872075, -0.00112453, -135.98071406, -0.02778776, -13.59807141, -0.06469687, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21012, 1012, 0.0, 433.83684118, 0.01262842, 433.83684118, 0.03788527, 303.68578883, -7489.20445643, 0.05, 2, 0, 71012, 22012, 2, 3)
    ops.uniaxialMaterial('LimitState', 41012, 108.4592103, 0.00012833, 325.37763089, 0.000385, 1084.59210296, 0.00128335, -108.4592103, -0.00012833, -325.37763089, -0.000385, -1084.59210296, -0.00128335, 0.4, 0.3, 0.003, 0.0, 0.0, 21012, 2)
    ops.limitCurve('ThreePoint', 11012, 1012, 0.0, 223.55928716, 0.02249063, 223.55928716, 0.0674719, 156.49150101, -2307.27397333, 0.05, 2, 0, 71012, 22012, 1, 3)
    ops.uniaxialMaterial('LimitState', 31012, 55.88982179, 6.613e-05, 167.66946537, 0.0001984, 558.89821791, 0.00066132, -55.88982179, -6.613e-05, -167.66946537, -0.0001984, -558.89821791, -0.00066132, 0.4, 0.3, 0.003, 0.0, 0.0, 11012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1012, 99999, 'P', 41012, 'Vy', 31012, 'Vz', 21012, 'My', 11012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171012, 71012, 171012, 1012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122012, 122012, 22012, 1012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171013, 0.0, 15.45, 3.95)
    ops.node(122013, 0.0, 15.45, 6.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1013, 171013, 122013, 0.125, 29709425.23400282, 12378927.18083451, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21013, 123.26053736, 0.00072972, 149.11782231, 0.02068125, 14.91178223, 0.07496164, -123.26053736, -0.00072972, -149.11782231, -0.02068125, -14.91178223, -0.07496164, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11013, 58.2517393, 0.00123167, 70.47164239, 0.01734296, 7.04716424, 0.05003211, -58.2517393, -0.00123167, -70.47164239, -0.01734296, -7.04716424, -0.05003211, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21013, 1013, 0.0, 175.6603832, 0.01459432, 175.6603832, 0.04378296, 122.96226824, -3057.30878579, 0.05, 2, 0, 71013, 22013, 2, 3)
    ops.uniaxialMaterial('LimitState', 41013, 43.9150958, 9.706e-05, 131.7452874, 0.00029118, 439.150958, 0.00097061, -43.9150958, -9.706e-05, -131.7452874, -0.00029118, -439.150958, -0.00097061, 0.4, 0.3, 0.003, 0.0, 0.0, 21013, 2)
    ops.limitCurve('ThreePoint', 11013, 1013, 0.0, 124.34840493, 0.02463336, 124.34840493, 0.07390009, 87.04388345, -1343.29286752, 0.05, 2, 0, 71013, 22013, 1, 3)
    ops.uniaxialMaterial('LimitState', 31013, 31.08710123, 6.871e-05, 93.26130369, 0.00020613, 310.87101231, 0.00068709, -31.08710123, -6.871e-05, -93.26130369, -0.00020613, -310.87101231, -0.00068709, 0.4, 0.3, 0.003, 0.0, 0.0, 11013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1013, 99999, 'P', 41013, 'Vy', 31013, 'Vz', 21013, 'My', 11013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171013, 71013, 171013, 1013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122013, 122013, 22013, 1013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171014, 2.95, 15.45, 3.975)
    ops.node(122014, 2.95, 15.45, 6.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1014, 171014, 122014, 0.28, 27667178.2657157, 11527990.94404821, 0.00829164, 0.00314417, 0.01642667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21014, 465.53818551, 0.00065739, 566.05034617, 0.03889523, 56.60503462, 0.10075931, -465.53818551, -0.00065739, -566.05034617, -0.03889523, -56.60503462, -0.10075931, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11014, 170.04166258, 0.00108017, 206.75455841, 0.03049838, 20.67545584, 0.06371166, -170.04166258, -0.00108017, -206.75455841, -0.03049838, -20.67545584, -0.06371166, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21014, 1014, 0.0, 476.63487731, 0.01314777, 476.63487731, 0.03944332, 333.64441412, -7290.56209001, 0.05, 2, 0, 71014, 22014, 2, 3)
    ops.uniaxialMaterial('LimitState', 41014, 119.15871933, 0.00012625, 357.47615798, 0.00037876, 1191.58719328, 0.00126253, -119.15871933, -0.00012625, -357.47615798, -0.00037876, -1191.58719328, -0.00126253, 0.4, 0.3, 0.003, 0.0, 0.0, 21014, 2)
    ops.limitCurve('ThreePoint', 11014, 1014, 0.0, 243.53142217, 0.02160331, 243.53142217, 0.06480993, 170.47199552, -2618.59264639, 0.05, 2, 0, 71014, 22014, 1, 3)
    ops.uniaxialMaterial('LimitState', 31014, 60.88285554, 6.451e-05, 182.64856663, 0.00019352, 608.82855543, 0.00064507, -60.88285554, -6.451e-05, -182.64856663, -0.00019352, -608.82855543, -0.00064507, 0.4, 0.3, 0.003, 0.0, 0.0, 11014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1014, 99999, 'P', 41014, 'Vy', 31014, 'Vz', 21014, 'My', 11014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171014, 71014, 171014, 1014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122014, 122014, 22014, 1014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171015, 7.7, 15.45, 3.975)
    ops.node(122015, 7.7, 15.45, 6.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1015, 171015, 122015, 0.45, 30293828.9700036, 12622428.7375015, 0.02179311, 0.00835313, 0.04125, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21015, 853.94301363, 0.0005924, 1034.14378627, 0.03172537, 103.41437863, 0.07629374, -853.94301363, -0.0005924, -1034.14378627, -0.03172537, -103.41437863, -0.07629374, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11015, 301.43595488, 0.00082489, 365.04557649, 0.02593524, 36.50455765, 0.05269918, -301.43595488, -0.00082489, -365.04557649, -0.02593524, -36.50455765, -0.05269918, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21015, 1015, 0.0, 787.69737951, 0.0118481, 787.69737951, 0.03554429, 551.38816565, -8314.32351543, 0.05, 2, 0, 71015, 22015, 2, 3)
    ops.uniaxialMaterial('LimitState', 41015, 196.92434488, 0.00011857, 590.77303463, 0.00035571, 1969.24344877, 0.00118569, -196.92434488, -0.00011857, -590.77303463, -0.00035571, -1969.24344877, -0.00118569, 0.4, 0.3, 0.003, 0.0, 0.0, 21015, 2)
    ops.limitCurve('ThreePoint', 11015, 1015, 0.0, 386.13888276, 0.01649776, 386.13888276, 0.04949327, 270.29721793, -3156.46893759, 0.05, 2, 0, 71015, 22015, 1, 3)
    ops.uniaxialMaterial('LimitState', 31015, 96.53472069, 5.812e-05, 289.60416207, 0.00017437, 965.3472069, 0.00058124, -96.53472069, -5.812e-05, -289.60416207, -0.00017437, -965.3472069, -0.00058124, 0.4, 0.3, 0.003, 0.0, 0.0, 11015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1015, 99999, 'P', 41015, 'Vy', 31015, 'Vz', 21015, 'My', 11015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171015, 71015, 171015, 1015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122015, 122015, 22015, 1015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171016, 12.45, 15.45, 3.95)
    ops.node(122016, 12.45, 15.45, 6.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1016, 171016, 122016, 0.225, 32711214.44554438, 13629672.68564349, 0.00505263, 0.00185625, 0.01160156, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21016, 355.49777452, 0.00062874, 427.05209123, 0.03483412, 42.70520912, 0.11191172, -355.49777452, -0.00062874, -427.05209123, -0.03483412, -42.70520912, -0.11191172, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11016, 115.59646139, 0.00110225, 138.8636276, 0.02648197, 13.88636276, 0.06445604, -115.59646139, -0.00110225, -138.8636276, -0.02648197, -13.88636276, -0.06445604, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21016, 1016, 0.0, 455.02763821, 0.01257477, 455.02763821, 0.03772432, 318.51934675, -7422.97082741, 0.05, 2, 0, 71016, 22016, 2, 3)
    ops.uniaxialMaterial('LimitState', 41016, 113.75690955, 0.00012686, 341.27072866, 0.00038059, 1137.56909554, 0.00126863, -113.75690955, -0.00012686, -341.27072866, -0.00038059, -1137.56909554, -0.00126863, 0.4, 0.3, 0.003, 0.0, 0.0, 21016, 2)
    ops.limitCurve('ThreePoint', 11016, 1016, 0.0, 236.34469664, 0.02204501, 236.34469664, 0.06613504, 165.44128765, -2292.55967284, 0.05, 2, 0, 71016, 22016, 1, 3)
    ops.uniaxialMaterial('LimitState', 31016, 59.08617416, 6.589e-05, 177.25852248, 0.00019768, 590.8617416, 0.00065894, -59.08617416, -6.589e-05, -177.25852248, -0.00019768, -590.8617416, -0.00065894, 0.4, 0.3, 0.003, 0.0, 0.0, 11016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1016, 99999, 'P', 41016, 'Vy', 31016, 'Vz', 21016, 'My', 11016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171016, 71016, 171016, 1016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122016, 122016, 22016, 1016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171017, 0.0, 20.6, 3.95)
    ops.node(122017, 0.0, 20.6, 6.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1017, 171017, 122017, 0.125, 29351725.96147385, 12229885.81728077, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21017, 124.05085608, 0.00076228, 150.18293521, 0.020421, 15.01829352, 0.07423442, -124.05085608, -0.00076228, -150.18293521, -0.020421, -15.01829352, -0.07423442, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11017, 58.24267846, 0.00133325, 70.51185845, 0.01720809, 7.05118585, 0.04961602, -58.24267846, -0.00133325, -70.51185845, -0.01720809, -7.05118585, -0.04961602, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21017, 1017, 0.0, 172.70669035, 0.01524551, 172.70669035, 0.04573652, 120.89468325, -2985.20524155, 0.05, 2, 0, 71017, 22017, 2, 3)
    ops.uniaxialMaterial('LimitState', 41017, 43.17667259, 9.659e-05, 129.53001776, 0.00028978, 431.76672588, 0.00096592, -43.17667259, -9.659e-05, -129.53001776, -0.00028978, -431.76672588, -0.00096592, 0.4, 0.3, 0.003, 0.0, 0.0, 21017, 2)
    ops.limitCurve('ThreePoint', 11017, 1017, 0.0, 122.28246437, 0.02666497, 122.28246437, 0.07999492, 85.59772506, -1319.36089604, 0.05, 2, 0, 71017, 22017, 1, 3)
    ops.uniaxialMaterial('LimitState', 31017, 30.57061609, 6.839e-05, 91.71184828, 0.00020517, 305.70616094, 0.00068391, -30.57061609, -6.839e-05, -91.71184828, -0.00020517, -305.70616094, -0.00068391, 0.4, 0.3, 0.003, 0.0, 0.0, 11017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1017, 99999, 'P', 41017, 'Vy', 31017, 'Vz', 21017, 'My', 11017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171017, 71017, 171017, 1017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122017, 122017, 22017, 1017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171018, 2.95, 20.6, 3.975)
    ops.node(122018, 2.95, 20.6, 6.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1018, 171018, 122018, 0.28, 31588365.65630184, 13161819.0234591, 0.00829164, 0.00314417, 0.01642667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21018, 460.41406056, 0.00063945, 555.02477148, 0.03728058, 55.50247715, 0.10422046, -460.41406056, -0.00063945, -555.02477148, -0.03728058, -55.50247715, -0.10422046, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11018, 168.52534994, 0.0010637, 203.15570668, 0.02925349, 20.31557067, 0.06519183, -168.52534994, -0.0010637, -203.15570668, -0.02925349, -20.31557067, -0.06519183, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21018, 1018, 0.0, 536.24270141, 0.01278909, 536.24270141, 0.03836726, 375.36989099, -7330.22929103, 0.05, 2, 0, 71018, 22018, 2, 3)
    ops.uniaxialMaterial('LimitState', 41018, 134.06067535, 0.00012441, 402.18202606, 0.00037323, 1340.60675352, 0.0012441, -134.06067535, -0.00012441, -402.18202606, -0.00037323, -1340.60675352, -0.0012441, 0.4, 0.3, 0.003, 0.0, 0.0, 21018, 2)
    ops.limitCurve('ThreePoint', 11018, 1018, 0.0, 276.62848104, 0.02127397, 276.62848104, 0.06382191, 193.63993673, -2628.98954924, 0.05, 2, 0, 71018, 22018, 1, 3)
    ops.uniaxialMaterial('LimitState', 31018, 69.15712026, 6.418e-05, 207.47136078, 0.00019254, 691.57120259, 0.00064178, -69.15712026, -6.418e-05, -207.47136078, -0.00019254, -691.57120259, -0.00064178, 0.4, 0.3, 0.003, 0.0, 0.0, 11018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1018, 99999, 'P', 41018, 'Vy', 31018, 'Vz', 21018, 'My', 11018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171018, 71018, 171018, 1018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122018, 122018, 22018, 1018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171019, 7.7, 20.6, 3.975)
    ops.node(122019, 7.7, 20.6, 6.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1019, 171019, 122019, 0.45, 28641774.63244529, 11934072.76351887, 0.02179311, 0.00835313, 0.04125, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21019, 900.44345391, 0.0006207, 1094.59758876, 0.02843134, 109.45975888, 0.07184506, -900.44345391, -0.0006207, -1094.59758876, -0.02843134, -109.45975888, -0.07184506, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11019, 316.20678501, 0.00087733, 384.38747366, 0.02330807, 38.43874737, 0.04937862, -316.20678501, -0.00087733, -384.38747366, -0.02330807, -38.43874737, -0.04937862, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21019, 1019, 0.0, 702.34648045, 0.01241393, 702.34648045, 0.0372418, 491.64253632, -6224.8100308, 0.05, 2, 0, 71019, 22019, 2, 3)
    ops.uniaxialMaterial('LimitState', 41019, 175.58662011, 0.00011182, 526.75986034, 0.00033546, 1755.86620113, 0.00111819, -175.58662011, -0.00011182, -526.75986034, -0.00033546, -1755.86620113, -0.00111819, 0.4, 0.3, 0.003, 0.0, 0.0, 21019, 2)
    ops.limitCurve('ThreePoint', 11019, 1019, 0.0, 345.302992, 0.01754669, 345.302992, 0.05264008, 241.7120944, -2565.82872115, 0.05, 2, 0, 71019, 22019, 1, 3)
    ops.uniaxialMaterial('LimitState', 31019, 86.325748, 5.498e-05, 258.977244, 0.00016493, 863.25747999, 0.00054975, -86.325748, -5.498e-05, -258.977244, -0.00016493, -863.25747999, -0.00054975, 0.4, 0.3, 0.003, 0.0, 0.0, 11019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1019, 99999, 'P', 41019, 'Vy', 31019, 'Vz', 21019, 'My', 11019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171019, 71019, 171019, 1019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122019, 122019, 22019, 1019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171020, 12.45, 20.6, 3.95)
    ops.node(122020, 12.45, 20.6, 6.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1020, 171020, 122020, 0.225, 29651021.27614199, 12354592.1983925, 0.00505263, 0.00185625, 0.01160156, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21020, 349.51143174, 0.00063702, 423.31181012, 0.0400561, 42.33118101, 0.11333875, -349.51143174, -0.00063702, -423.31181012, -0.0400561, -42.33118101, -0.11333875, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11020, 113.28411235, 0.00112594, 137.20438962, 0.03037413, 13.72043896, 0.06647853, -113.28411235, -0.00112594, -137.20438962, -0.03037413, -13.72043896, -0.06647853, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21020, 1020, 0.0, 454.5760036, 0.01274048, 454.5760036, 0.03822144, 318.20320252, -9813.10925408, 0.05, 2, 0, 71020, 22020, 2, 3)
    ops.uniaxialMaterial('LimitState', 41020, 113.6440009, 0.00013982, 340.9320027, 0.00041945, 1136.44000899, 0.00139818, -113.6440009, -0.00013982, -340.9320027, -0.00041945, -1136.44000899, -0.00139818, 0.4, 0.3, 0.003, 0.0, 0.0, 21020, 2)
    ops.limitCurve('ThreePoint', 11020, 1020, 0.0, 229.23362464, 0.02251883, 229.23362464, 0.06755649, 160.46353725, -2813.50377612, 0.05, 2, 0, 71020, 22020, 1, 3)
    ops.uniaxialMaterial('LimitState', 31020, 57.30840616, 7.051e-05, 171.92521848, 0.00021152, 573.08406161, 0.00070507, -57.30840616, -7.051e-05, -171.92521848, -0.00021152, -573.08406161, -0.00070507, 0.4, 0.3, 0.003, 0.0, 0.0, 11020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1020, 99999, 'P', 41020, 'Vy', 31020, 'Vz', 21020, 'My', 11020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171020, 71020, 171020, 1020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122020, 122020, 22020, 1020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171021, 0.0, 25.75, 3.95)
    ops.node(122021, 0.0, 25.75, 6.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1021, 171021, 122021, 0.125, 29031822.8264651, 12096592.84436046, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21021, 123.45781103, 0.00076667, 149.55549583, 0.02087867, 14.95554958, 0.07424657, -123.45781103, -0.00076667, -149.55549583, -0.02087867, -14.95554958, -0.07424657, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11021, 57.90458441, 0.00135141, 70.14500549, 0.01759228, 7.01450055, 0.04973191, -57.90458441, -0.00135141, -70.14500549, -0.01759228, -7.01450055, -0.04973191, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21021, 1021, 0.0, 174.86289532, 0.01533341, 174.86289532, 0.04600023, 122.40402672, -3159.32235135, 0.05, 2, 0, 71021, 22021, 2, 3)
    ops.uniaxialMaterial('LimitState', 41021, 43.71572383, 9.888e-05, 131.14717149, 0.00029663, 437.1572383, 0.00098876, -43.71572383, -9.888e-05, -131.14717149, -0.00029663, -437.1572383, -0.00098876, 0.4, 0.3, 0.003, 0.0, 0.0, 21021, 2)
    ops.limitCurve('ThreePoint', 11021, 1021, 0.0, 122.84316197, 0.02702826, 122.84316197, 0.08108479, 85.99021338, -1377.31528122, 0.05, 2, 0, 71021, 22021, 1, 3)
    ops.uniaxialMaterial('LimitState', 31021, 30.71079049, 6.946e-05, 92.13237148, 0.00020838, 307.10790493, 0.00069461, -30.71079049, -6.946e-05, -92.13237148, -0.00020838, -307.10790493, -0.00069461, 0.4, 0.3, 0.003, 0.0, 0.0, 11021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1021, 99999, 'P', 41021, 'Vy', 31021, 'Vz', 21021, 'My', 11021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171021, 71021, 171021, 1021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122021, 122021, 22021, 1021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171022, 2.95, 25.75, 3.975)
    ops.node(122022, 2.95, 25.75, 6.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1022, 171022, 122022, 0.28, 29072619.35094796, 12113591.39622832, 0.00829164, 0.00314417, 0.01642667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21022, 474.6994371, 0.00065107, 575.73990485, 0.0376915, 57.57399048, 0.10165867, -474.6994371, -0.00065107, -575.73990485, -0.0376915, -57.57399048, -0.10165867, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11022, 173.90341118, 0.00105396, 210.91900597, 0.02955095, 21.0919006, 0.06389332, -173.90341118, -0.00105396, -210.91900597, -0.02955095, -21.0919006, -0.06389332, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21022, 1022, 0.0, 489.81541765, 0.01302142, 489.81541765, 0.03906426, 342.87079236, -6870.97118242, 0.05, 2, 0, 71022, 22022, 2, 3)
    ops.uniaxialMaterial('LimitState', 41022, 122.45385441, 0.00012347, 367.36156324, 0.00037042, 1224.53854413, 0.00123472, -122.45385441, -0.00012347, -367.36156324, -0.00037042, -1224.53854413, -0.00123472, 0.4, 0.3, 0.003, 0.0, 0.0, 21022, 2)
    ops.limitCurve('ThreePoint', 11022, 1022, 0.0, 251.75522782, 0.02107913, 251.75522782, 0.0632374, 176.22865947, -2508.82615947, 0.05, 2, 0, 71022, 22022, 1, 3)
    ops.uniaxialMaterial('LimitState', 31022, 62.93880696, 6.346e-05, 188.81642087, 0.00019039, 629.38806955, 0.00063462, -62.93880696, -6.346e-05, -188.81642087, -0.00019039, -629.38806955, -0.00063462, 0.4, 0.3, 0.003, 0.0, 0.0, 11022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1022, 99999, 'P', 41022, 'Vy', 31022, 'Vz', 21022, 'My', 11022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171022, 71022, 171022, 1022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122022, 122022, 22022, 1022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171023, 7.7, 25.75, 3.975)
    ops.node(122023, 7.7, 25.75, 6.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1023, 171023, 122023, 0.45, 30722261.99766035, 12800942.49902515, 0.02179311, 0.00835313, 0.04125, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21023, 870.83012057, 0.0005952, 1053.41296034, 0.02778843, 105.34129603, 0.07261253, -870.83012057, -0.0005952, -1053.41296034, -0.02778843, -105.34129603, -0.07261253, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11023, 307.30683141, 0.00082552, 371.7384038, 0.02275828, 37.17384038, 0.04967579, -307.30683141, -0.00082552, -371.7384038, -0.02275828, -37.17384038, -0.04967579, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21023, 1023, 0.0, 756.0275309, 0.01190393, 756.0275309, 0.0357118, 529.21927163, -6130.78588736, 0.05, 2, 0, 71023, 22023, 2, 3)
    ops.uniaxialMaterial('LimitState', 41023, 189.00688273, 0.00011221, 567.02064818, 0.00033664, 1890.06882725, 0.00112215, -189.00688273, -0.00011221, -567.02064818, -0.00033664, -1890.06882725, -0.00112215, 0.4, 0.3, 0.003, 0.0, 0.0, 21023, 2)
    ops.limitCurve('ThreePoint', 11023, 1023, 0.0, 372.53536676, 0.01651041, 372.53536676, 0.04953122, 260.77475673, -2539.3800919, 0.05, 2, 0, 71023, 22023, 1, 3)
    ops.uniaxialMaterial('LimitState', 31023, 93.13384169, 5.529e-05, 279.40152507, 0.00016588, 931.3384169, 0.00055294, -93.13384169, -5.529e-05, -279.40152507, -0.00016588, -931.3384169, -0.00055294, 0.4, 0.3, 0.003, 0.0, 0.0, 11023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1023, 99999, 'P', 41023, 'Vy', 31023, 'Vz', 21023, 'My', 11023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171023, 71023, 171023, 1023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122023, 122023, 22023, 1023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171024, 12.45, 25.75, 3.95)
    ops.node(122024, 12.45, 25.75, 6.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1024, 171024, 122024, 0.225, 29509492.97083487, 12295622.07118119, 0.00505263, 0.00185625, 0.01160156, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21024, 364.56152776, 0.00065312, 441.67252685, 0.03976022, 44.16725269, 0.11281836, -364.56152776, -0.00065312, -441.67252685, -0.03976022, -44.16725269, -0.11281836, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11024, 118.03357329, 0.00114534, 142.99969305, 0.03016204, 14.29996931, 0.06615583, -118.03357329, -0.00114534, -142.99969305, -0.03016204, -14.29996931, -0.06615583, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21024, 1024, 0.0, 447.76359867, 0.01306248, 447.76359867, 0.03918743, 313.43451907, -9432.43570515, 0.05, 2, 0, 71024, 22024, 2, 3)
    ops.uniaxialMaterial('LimitState', 41024, 111.94089967, 0.00013838, 335.82269901, 0.00041515, 1119.40899668, 0.00138383, -111.94089967, -0.00013838, -335.82269901, -0.00041515, -1119.40899668, -0.00138383, 0.4, 0.3, 0.003, 0.0, 0.0, 21024, 2)
    ops.limitCurve('ThreePoint', 11024, 1024, 0.0, 226.20552797, 0.02290678, 226.20552797, 0.06872033, 158.34386958, -2732.38198243, 0.05, 2, 0, 71024, 22024, 1, 3)
    ops.uniaxialMaterial('LimitState', 31024, 56.55138199, 6.991e-05, 169.65414598, 0.00020973, 565.51381994, 0.0006991, -56.55138199, -6.991e-05, -169.65414598, -0.00020973, -565.51381994, -0.0006991, 0.4, 0.3, 0.003, 0.0, 0.0, 11024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1024, 99999, 'P', 41024, 'Vy', 31024, 'Vz', 21024, 'My', 11024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171024, 71024, 171024, 1024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122024, 122024, 22024, 1024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171025, 0.0, 30.9, 3.975)
    ops.node(122025, 0.0, 30.9, 6.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1025, 171025, 122025, 0.09, 32469025.9492538, 13528760.81218908, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21025, 65.82237753, 0.001078, 79.16472362, 0.01737028, 7.91647236, 0.06880294, -65.82237753, -0.001078, -79.16472362, -0.01737028, -7.91647236, -0.06880294, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11025, 56.88562085, 0.001078, 68.41646597, 0.01737028, 6.8416466, 0.06880294, -56.88562085, -0.001078, -68.41646597, -0.01737028, -6.8416466, -0.06880294, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21025, 1025, 0.0, 108.58941762, 0.02156005, 108.58941762, 0.06468015, 76.01259233, -1598.96781432, 0.05, 2, 0, 71025, 22025, 2, 3)
    ops.uniaxialMaterial('LimitState', 41025, 27.1473544, 7.625e-05, 81.44206321, 0.00022876, 271.47354404, 0.00076252, -27.1473544, -7.625e-05, -81.44206321, -0.00022876, -271.47354404, -0.00076252, 0.4, 0.3, 0.003, 0.0, 0.0, 21025, 2)
    ops.limitCurve('ThreePoint', 11025, 1025, 0.0, 108.58941762, 0.02156005, 108.58941762, 0.06468015, 76.01259233, -1598.96781432, 0.05, 2, 0, 71025, 22025, 1, 3)
    ops.uniaxialMaterial('LimitState', 31025, 27.1473544, 7.625e-05, 81.44206321, 0.00022876, 271.47354404, 0.00076252, -27.1473544, -7.625e-05, -81.44206321, -0.00022876, -271.47354404, -0.00076252, 0.4, 0.3, 0.003, 0.0, 0.0, 11025, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1025, 99999, 'P', 41025, 'Vy', 31025, 'Vz', 21025, 'My', 11025, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171025, 71025, 171025, 1025, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122025, 122025, 22025, 1025, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171026, 2.95, 30.9, 3.975)
    ops.node(122026, 2.95, 30.9, 6.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1026, 171026, 122026, 0.27, 29547896.73788899, 12311623.64078708, 0.00984074, 0.00891, 0.00501188, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21026, 235.59099567, 0.00082459, 285.97504417, 0.04237274, 28.59750442, 0.10354119, -235.59099567, -0.00082459, -285.97504417, -0.04237274, -28.59750442, -0.10354119, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11026, 259.34261496, 0.00070174, 314.80624104, 0.046645, 31.4806241, 0.12429063, -259.34261496, -0.00070174, -314.80624104, -0.046645, -31.4806241, -0.12429063, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21026, 1026, 0.0, 338.41529954, 0.01649181, 338.41529954, 0.04947542, 236.89070968, -8222.56097275, 0.05, 2, 0, 71026, 22026, 2, 3)
    ops.uniaxialMaterial('LimitState', 41026, 84.60382489, 8.704e-05, 253.81147466, 0.00026113, 846.03824886, 0.00087044, -84.60382489, -8.704e-05, -253.81147466, -0.00026113, -846.03824886, -0.00087044, 0.4, 0.3, 0.003, 0.0, 0.0, 21026, 2)
    ops.limitCurve('ThreePoint', 11026, 1026, 0.0, 451.22039939, 0.01403489, 451.22039939, 0.04210467, 315.85427957, -13043.62857233, 0.05, 2, 0, 71026, 22026, 1, 3)
    ops.uniaxialMaterial('LimitState', 31026, 112.80509985, 0.00011606, 338.41529954, 0.00034817, 1128.05099848, 0.00116058, -112.80509985, -0.00011606, -338.41529954, -0.00034817, -1128.05099848, -0.00116058, 0.4, 0.3, 0.003, 0.0, 0.0, 11026, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1026, 99999, 'P', 41026, 'Vy', 31026, 'Vz', 21026, 'My', 11026, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171026, 71026, 171026, 1026, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122026, 122026, 22026, 1026, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171027, 7.7, 30.9, 3.975)
    ops.node(122027, 7.7, 30.9, 6.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1027, 171027, 122027, 0.35, 27001247.05718, 11250519.60715833, 0.01632638, 0.01572083, 0.00802083, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21027, 279.41124817, 0.000859, 340.97190262, 0.02898043, 34.09719026, 0.06092576, -279.41124817, -0.000859, -340.97190262, -0.02898043, -34.09719026, -0.06092576, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11027, 476.25934757, 0.00071558, 581.19011652, 0.03163784, 58.11901165, 0.07165242, -476.25934757, -0.00071558, -581.19011652, -0.03163784, -58.11901165, -0.07165242, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21027, 1027, 0.0, 310.95864531, 0.01718003, 310.95864531, 0.05154008, 217.67105172, -3611.64476969, 0.05, 2, 0, 71027, 22027, 2, 3)
    ops.uniaxialMaterial('LimitState', 41027, 77.73966133, 6.752e-05, 233.21898398, 0.00020256, 777.39661327, 0.00067519, -77.73966133, -6.752e-05, -233.21898398, -0.00020256, -777.39661327, -0.00067519, 0.4, 0.3, 0.003, 0.0, 0.0, 21027, 2)
    ops.limitCurve('ThreePoint', 11027, 1027, 0.0, 435.34210343, 0.0143116, 435.34210343, 0.04293481, 304.7394724, -5649.52531239, 0.05, 2, 0, 71027, 22027, 1, 3)
    ops.uniaxialMaterial('LimitState', 31027, 108.83552586, 9.453e-05, 326.50657758, 0.00028358, 1088.35525858, 0.00094527, -108.83552586, -9.453e-05, -326.50657758, -0.00028358, -1088.35525858, -0.00094527, 0.4, 0.3, 0.003, 0.0, 0.0, 11027, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1027, 99999, 'P', 41027, 'Vy', 31027, 'Vz', 21027, 'My', 11027, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171027, 71027, 171027, 1027, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122027, 122027, 22027, 1027, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171028, 12.45, 30.9, 3.975)
    ops.node(122028, 12.45, 30.9, 6.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1028, 171028, 122028, 0.1575, 28756295.38523661, 11981789.74384859, 0.00337604, 0.00292359, 0.00176859, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21028, 97.39830219, 0.0008753, 118.33992836, 0.02826652, 11.83399284, 0.0819452, -97.39830219, -0.0008753, -118.33992836, -0.02826652, -11.83399284, -0.0819452, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11028, 106.10493007, 0.00073891, 128.91856985, 0.0305758, 12.89185698, 0.09632741, -106.10493007, -0.00073891, -128.91856985, -0.0305758, -12.89185698, -0.09632741, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21028, 1028, 0.0, 176.7507241, 0.017506, 176.7507241, 0.05251801, 123.72550687, -3275.06203293, 0.05, 2, 0, 71028, 22028, 2, 3)
    ops.uniaxialMaterial('LimitState', 41028, 44.18768102, 8.008e-05, 132.56304307, 0.00024024, 441.87681025, 0.0008008, -44.18768102, -8.008e-05, -132.56304307, -0.00024024, -441.87681025, -0.0008008, 0.4, 0.3, 0.003, 0.0, 0.0, 21028, 2)
    ops.limitCurve('ThreePoint', 11028, 1028, 0.0, 201.41868923, 0.01477815, 201.41868923, 0.04433445, 140.99308246, -4733.84250088, 0.05, 2, 0, 71028, 22028, 1, 3)
    ops.uniaxialMaterial('LimitState', 31028, 50.35467231, 9.126e-05, 151.06401692, 0.00027377, 503.54672308, 0.00091256, -50.35467231, -9.126e-05, -151.06401692, -0.00027377, -503.54672308, -0.00091256, 0.4, 0.3, 0.003, 0.0, 0.0, 11028, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1028, 99999, 'P', 41028, 'Vy', 31028, 'Vz', 21028, 'My', 11028, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171028, 71028, 171028, 1028, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122028, 122028, 22028, 1028, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172003, 7.7, 0.0, 6.825)
    ops.node(123003, 7.7, 0.0, 9.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2003, 172003, 123003, 0.24, 31241751.10258349, 13017396.29274312, 0.00751249, 0.00792, 0.00352, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22003, 137.12065911, 0.00085877, 165.78185103, 0.0236625, 16.5781851, 0.06156793, -137.12065911, -0.00085877, -165.78185103, -0.0236625, -16.5781851, -0.06156793, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12003, 248.87712956, 0.00067589, 300.89784781, 0.02642702, 30.08978478, 0.07700078, -248.87712956, -0.00067589, -300.89784781, -0.02642702, -30.08978478, -0.07700078, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22003, 2003, 0.0, 225.56157206, 0.01717549, 225.56157206, 0.05152647, 157.89310044, -2549.47253138, 0.05, 2, 0, 72003, 23003, 2, 3)
    ops.uniaxialMaterial('LimitState', 42003, 56.39039302, 6.173e-05, 169.17117905, 0.00018519, 563.90393016, 0.0006173, -56.39039302, -6.173e-05, -169.17117905, -0.00018519, -563.90393016, -0.0006173, 0.4, 0.3, 0.003, 0.0, 0.0, 22003, 2)
    ops.limitCurve('ThreePoint', 12003, 2003, 0.0, 314.74087642, 0.01351776, 314.74087642, 0.04055327, 220.31861349, -4477.78113113, 0.05, 2, 0, 72003, 23003, 1, 3)
    ops.uniaxialMaterial('LimitState', 32003, 78.6852191, 8.614e-05, 236.05565731, 0.00025841, 786.85219105, 0.00086136, -78.6852191, -8.614e-05, -236.05565731, -0.00025841, -786.85219105, -0.00086136, 0.4, 0.3, 0.003, 0.0, 0.0, 12003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2003, 99999, 'P', 42003, 'Vy', 32003, 'Vz', 22003, 'My', 12003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172003, 72003, 172003, 2003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123003, 123003, 23003, 2003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172004, 12.45, 0.0, 6.8)
    ops.node(123004, 12.45, 0.0, 9.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2004, 172004, 123004, 0.0875, 28937022.7861094, 12057092.82754558, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22004, 41.47108909, 0.00140592, 50.3430335, 0.0200892, 5.03430335, 0.0636216, -41.47108909, -0.00140592, -50.3430335, -0.0200892, -5.03430335, -0.0636216, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12004, 56.08503063, 0.00101804, 68.08334765, 0.02185232, 6.80833477, 0.07822562, -56.08503063, -0.00101804, -68.08334765, -0.02185232, -6.80833477, -0.07822562, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22004, 2004, 0.0, 95.97741227, 0.0281185, 95.97741227, 0.0843555, 67.18418859, -1576.17920483, 0.05, 2, 0, 72004, 23004, 2, 3)
    ops.uniaxialMaterial('LimitState', 42004, 23.99435307, 7.778e-05, 71.9830592, 0.00023335, 239.94353067, 0.00077783, -23.99435307, -7.778e-05, -71.9830592, -0.00023335, -239.94353067, -0.00077783, 0.4, 0.3, 0.003, 0.0, 0.0, 22004, 2)
    ops.limitCurve('ThreePoint', 12004, 2004, 0.0, 113.00638968, 0.02036073, 113.00638968, 0.06108219, 79.10447278, -2536.09684972, 0.05, 2, 0, 72004, 23004, 1, 3)
    ops.uniaxialMaterial('LimitState', 32004, 28.25159742, 9.158e-05, 84.75479226, 0.00027475, 282.51597421, 0.00091584, -28.25159742, -9.158e-05, -84.75479226, -0.00027475, -282.51597421, -0.00091584, 0.4, 0.3, 0.003, 0.0, 0.0, 12004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2004, 99999, 'P', 42004, 'Vy', 32004, 'Vz', 22004, 'My', 12004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172004, 72004, 172004, 2004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123004, 123004, 23004, 2004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172005, 0.0, 5.15, 6.8)
    ops.node(123005, 0.0, 5.15, 9.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2005, 172005, 123005, 0.0875, 26152220.18426416, 10896758.41011007, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22005, 60.37080626, 0.0010279, 73.47422755, 0.01988416, 7.34742275, 0.06967281, -60.37080626, -0.0010279, -73.47422755, -0.01988416, -7.34742275, -0.06967281, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12005, 38.66750489, 0.00143943, 47.06024698, 0.01834889, 4.7060247, 0.05679652, -38.66750489, -0.00143943, -47.06024698, -0.01834889, -4.7060247, -0.05679652, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22005, 2005, 0.0, 102.30193391, 0.02055798, 102.30193391, 0.06167393, 71.61135374, -2016.44098391, 0.05, 2, 0, 72005, 23005, 2, 3)
    ops.uniaxialMaterial('LimitState', 42005, 25.57548348, 9.174e-05, 76.72645044, 0.00027521, 255.75483479, 0.00091737, -25.57548348, -9.174e-05, -76.72645044, -0.00027521, -255.75483479, -0.00091737, 0.4, 0.3, 0.003, 0.0, 0.0, 22005, 2)
    ops.limitCurve('ThreePoint', 12005, 2005, 0.0, 86.89989098, 0.02878851, 86.89989098, 0.08636553, 60.82992369, -1311.21428241, 0.05, 2, 0, 72005, 23005, 1, 3)
    ops.uniaxialMaterial('LimitState', 32005, 21.72497275, 7.793e-05, 65.17491824, 0.00023378, 217.24972746, 0.00077926, -21.72497275, -7.793e-05, -65.17491824, -0.00023378, -217.24972746, -0.00077926, 0.4, 0.3, 0.003, 0.0, 0.0, 12005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2005, 99999, 'P', 42005, 'Vy', 32005, 'Vz', 22005, 'My', 12005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172005, 72005, 172005, 2005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123005, 123005, 23005, 2005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172006, 2.95, 5.15, 6.825)
    ops.node(123006, 2.95, 5.15, 9.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2006, 172006, 123006, 0.1875, 28172494.4326057, 11738539.34691904, 0.00308678, 0.00107422, 0.00966797, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22006, 274.27215377, 0.00066045, 333.21860039, 0.04481646, 33.32186004, 0.1283349, -274.27215377, -0.00066045, -333.21860039, -0.04481646, -33.32186004, -0.1283349, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12006, 82.27755736, 0.00141311, 99.96061259, 0.03207307, 9.99606126, 0.0672291, -82.27755736, -0.00141311, -99.96061259, -0.03207307, -9.99606126, -0.0672291, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22006, 2006, 0.0, 379.55399845, 0.01320906, 379.55399845, 0.03962718, 265.68779892, -9532.5669714, 0.05, 2, 0, 72006, 23006, 2, 3)
    ops.uniaxialMaterial('LimitState', 42006, 94.88849961, 0.00014744, 284.66549884, 0.00044233, 948.88499613, 0.00147443, -94.88849961, -0.00014744, -284.66549884, -0.00044233, -948.88499613, -0.00147443, 0.4, 0.3, 0.003, 0.0, 0.0, 22006, 2)
    ops.limitCurve('ThreePoint', 12006, 2006, 0.0, 175.72978023, 0.02826212, 175.72978023, 0.08478635, 123.01084616, -2109.653922, 0.05, 2, 0, 72006, 23006, 1, 3)
    ops.uniaxialMaterial('LimitState', 32006, 43.93244506, 6.826e-05, 131.79733517, 0.00020479, 439.32445057, 0.00068265, -43.93244506, -6.826e-05, -131.79733517, -0.00020479, -439.32445057, -0.00068265, 0.4, 0.3, 0.003, 0.0, 0.0, 12006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2006, 99999, 'P', 42006, 'Vy', 32006, 'Vz', 22006, 'My', 12006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172006, 72006, 172006, 2006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123006, 123006, 23006, 2006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172007, 7.7, 5.15, 6.825)
    ops.node(123007, 7.7, 5.15, 9.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2007, 172007, 123007, 0.315, 26829606.16751771, 11179002.56979905, 0.00971719, 0.00353719, 0.02338875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22007, 595.90641108, 0.00063905, 727.14078231, 0.0314659, 72.71407823, 0.08291482, -595.90641108, -0.00063905, -727.14078231, -0.0314659, -72.71407823, -0.08291482, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12007, 182.25898161, 0.00107927, 222.39723555, 0.02460438, 22.23972355, 0.05169996, -182.25898161, -0.00107927, -222.39723555, -0.02460438, -22.23972355, -0.05169996, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22007, 2007, 0.0, 483.52303597, 0.01278093, 483.52303597, 0.0383428, 338.46612518, -6086.70637155, 0.05, 2, 0, 72007, 23007, 2, 3)
    ops.uniaxialMaterial('LimitState', 42007, 120.88075899, 0.0001174, 362.64227697, 0.0003522, 1208.80758992, 0.001174, -120.88075899, -0.0001174, -362.64227697, -0.0003522, -1208.80758992, -0.001174, 0.4, 0.3, 0.003, 0.0, 0.0, 22007, 2)
    ops.limitCurve('ThreePoint', 12007, 2007, 0.0, 225.02122005, 0.02158543, 225.02122005, 0.06475629, 157.51485404, -1915.02825128, 0.05, 2, 0, 72007, 23007, 1, 3)
    ops.uniaxialMaterial('LimitState', 32007, 56.25530501, 5.464e-05, 168.76591504, 0.00016391, 562.55305013, 0.00054636, -56.25530501, -5.464e-05, -168.76591504, -0.00016391, -562.55305013, -0.00054636, 0.4, 0.3, 0.003, 0.0, 0.0, 12007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2007, 99999, 'P', 42007, 'Vy', 32007, 'Vz', 22007, 'My', 12007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172007, 72007, 172007, 2007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123007, 123007, 23007, 2007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172008, 12.45, 5.15, 6.8)
    ops.node(123008, 12.45, 5.15, 9.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2008, 172008, 123008, 0.1625, 34109029.68749252, 14212095.70312188, 0.0025666, 0.00093099, 0.00629349, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22008, 217.59838427, 0.00065423, 260.30197745, 0.02720557, 26.03019774, 0.10008333, -217.59838427, -0.00065423, -260.30197745, -0.02720557, -26.03019774, -0.10008333, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12008, 69.96604052, 0.00129128, 83.69684712, 0.02093171, 8.36968471, 0.05657713, -69.96604052, -0.00129128, -83.69684712, -0.02093171, -8.36968471, -0.05657713, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22008, 2008, 0.0, 291.17542024, 0.01308455, 291.17542024, 0.03925365, 203.82279417, -4639.57151555, 0.05, 2, 0, 72008, 23008, 2, 3)
    ops.uniaxialMaterial('LimitState', 42008, 72.79385506, 0.0001078, 218.38156518, 0.00032339, 727.9385506, 0.00107798, -72.79385506, -0.0001078, -218.38156518, -0.00032339, -727.9385506, -0.00107798, 0.4, 0.3, 0.003, 0.0, 0.0, 22008, 2)
    ops.limitCurve('ThreePoint', 12008, 2008, 0.0, 166.75536617, 0.02582554, 166.75536617, 0.07747661, 116.72875632, -1372.39647272, 0.05, 2, 0, 72008, 23008, 1, 3)
    ops.uniaxialMaterial('LimitState', 32008, 41.68884154, 6.174e-05, 125.06652463, 0.00018521, 416.88841544, 0.00061735, -41.68884154, -6.174e-05, -125.06652463, -0.00018521, -416.88841544, -0.00061735, 0.4, 0.3, 0.003, 0.0, 0.0, 12008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2008, 99999, 'P', 42008, 'Vy', 32008, 'Vz', 22008, 'My', 12008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172008, 72008, 172008, 2008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123008, 123008, 23008, 2008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172009, 0.0, 10.3, 6.8)
    ops.node(123009, 0.0, 10.3, 9.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2009, 172009, 123009, 0.1, 32875036.15571297, 13697931.73154707, 0.00127345, 0.00057292, 0.00146667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22009, 73.68514086, 0.00081366, 88.51235873, 0.02000959, 8.85123587, 0.07974126, -73.68514086, -0.00081366, -88.51235873, -0.02000959, -8.85123587, -0.07974126, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12009, 40.47353695, 0.00119988, 48.61778345, 0.01772878, 4.86177834, 0.05961789, -40.47353695, -0.00119988, -48.61778345, -0.01772878, -4.86177834, -0.05961789, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22009, 2009, 0.0, 138.05982912, 0.01627312, 138.05982912, 0.04881936, 96.64188038, -2677.22036653, 0.05, 2, 0, 72009, 23009, 2, 3)
    ops.uniaxialMaterial('LimitState', 42009, 34.51495728, 8.617e-05, 103.54487184, 0.00025852, 345.1495728, 0.00086174, -34.51495728, -8.617e-05, -103.54487184, -0.00025852, -345.1495728, -0.00086174, 0.4, 0.3, 0.003, 0.0, 0.0, 22009, 2)
    ops.limitCurve('ThreePoint', 12009, 2009, 0.0, 113.74539071, 0.02399759, 113.74539071, 0.07199277, 79.62177349, -1414.58991421, 0.05, 2, 0, 72009, 23009, 1, 3)
    ops.uniaxialMaterial('LimitState', 32009, 28.43634768, 7.1e-05, 85.30904303, 0.00021299, 284.36347677, 0.00070998, -28.43634768, -7.1e-05, -85.30904303, -0.00021299, -284.36347677, -0.00070998, 0.4, 0.3, 0.003, 0.0, 0.0, 12009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2009, 99999, 'P', 42009, 'Vy', 32009, 'Vz', 22009, 'My', 12009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172009, 72009, 172009, 2009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123009, 123009, 23009, 2009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172010, 2.95, 10.3, 6.825)
    ops.node(123010, 2.95, 10.3, 9.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2010, 172010, 123010, 0.1875, 30873640.36597519, 12864016.81915633, 0.00308678, 0.00107422, 0.00966797, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22010, 306.47313525, 0.00064788, 370.27427409, 0.0432214, 37.02742741, 0.13216512, -306.47313525, -0.00064788, -370.27427409, -0.0432214, -37.02742741, -0.13216512, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12010, 98.72889903, 0.00136818, 119.28213998, 0.03092934, 11.928214, 0.06836907, -98.72889903, -0.00136818, -119.28213998, -0.03092934, -11.928214, -0.06836907, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22010, 2010, 0.0, 387.61249588, 0.01295759, 387.61249588, 0.03887278, 271.32874712, -8618.69878657, 0.05, 2, 0, 72010, 23010, 2, 3)
    ops.uniaxialMaterial('LimitState', 42010, 96.90312397, 0.0001374, 290.70937191, 0.0004122, 969.03123971, 0.001374, -96.90312397, -0.0001374, -290.70937191, -0.0004122, -969.03123971, -0.001374, 0.4, 0.3, 0.003, 0.0, 0.0, 22010, 2)
    ops.limitCurve('ThreePoint', 12010, 2010, 0.0, 184.53103653, 0.02736358, 184.53103653, 0.08209074, 129.17172557, -1932.47144485, 0.05, 2, 0, 72010, 23010, 1, 3)
    ops.uniaxialMaterial('LimitState', 32010, 46.13275913, 6.541e-05, 138.3982774, 0.00019624, 461.32759132, 0.00065412, -46.13275913, -6.541e-05, -138.3982774, -0.00019624, -461.32759132, -0.00065412, 0.4, 0.3, 0.003, 0.0, 0.0, 12010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2010, 99999, 'P', 42010, 'Vy', 32010, 'Vz', 22010, 'My', 12010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172010, 72010, 172010, 2010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123010, 123010, 23010, 2010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172011, 7.7, 10.3, 6.825)
    ops.node(123011, 7.7, 10.3, 9.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2011, 172011, 123011, 0.315, 29809683.56008601, 12420701.48336917, 0.00971719, 0.00353719, 0.02338875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22011, 595.62064506, 0.00063406, 722.47308614, 0.03195287, 72.24730861, 0.08611919, -595.62064506, -0.00063406, -722.47308614, -0.03195287, -72.24730861, -0.08611919, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12011, 182.28841585, 0.00109673, 221.11133228, 0.02499727, 22.11113323, 0.05352397, -182.28841585, -0.00109673, -221.11133228, -0.02499727, -22.11113323, -0.05352397, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22011, 2011, 0.0, 547.21411582, 0.01268113, 547.21411582, 0.0380434, 383.04988107, -6663.30298116, 0.05, 2, 0, 72011, 23011, 2, 3)
    ops.uniaxialMaterial('LimitState', 42011, 136.80352895, 0.00011958, 410.41058686, 0.00035875, 1368.03528955, 0.00119582, -136.80352895, -0.00011958, -410.41058686, -0.00035875, -1368.03528955, -0.00119582, 0.4, 0.3, 0.003, 0.0, 0.0, 22011, 2)
    ops.limitCurve('ThreePoint', 12011, 2011, 0.0, 255.78817165, 0.02193457, 255.78817165, 0.06580372, 179.05172015, -2039.93051007, 0.05, 2, 0, 72011, 23011, 1, 3)
    ops.uniaxialMaterial('LimitState', 32011, 63.94704291, 5.59e-05, 191.84112874, 0.00016769, 639.47042912, 0.00055897, -63.94704291, -5.59e-05, -191.84112874, -0.00016769, -639.47042912, -0.00055897, 0.4, 0.3, 0.003, 0.0, 0.0, 12011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2011, 99999, 'P', 42011, 'Vy', 32011, 'Vz', 22011, 'My', 12011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172011, 72011, 172011, 2011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123011, 123011, 23011, 2011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172012, 12.45, 10.3, 6.8)
    ops.node(123012, 12.45, 10.3, 9.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2012, 172012, 123012, 0.1625, 30651788.08610618, 12771578.36921091, 0.0025666, 0.00093099, 0.00629349, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22012, 206.85942361, 0.00064834, 250.14033769, 0.02560696, 25.01403377, 0.08384773, -206.85942361, -0.00064834, -250.14033769, -0.02560696, -25.01403377, -0.08384773, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12012, 66.35114187, 0.00129042, 80.23370047, 0.02009766, 8.02337005, 0.04986278, -66.35114187, -0.00129042, -80.23370047, -0.02009766, -8.02337005, -0.04986278, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22012, 2012, 0.0, 259.72073735, 0.01296673, 259.72073735, 0.03890019, 181.80451615, -4288.26216054, 0.05, 2, 0, 72012, 23012, 2, 3)
    ops.uniaxialMaterial('LimitState', 42012, 64.93018434, 0.000107, 194.79055301, 0.00032099, 649.30184338, 0.00106998, -64.93018434, -0.000107, -194.79055301, -0.00032099, -649.30184338, -0.00106998, 0.4, 0.3, 0.003, 0.0, 0.0, 22012, 2)
    ops.limitCurve('ThreePoint', 12012, 2012, 0.0, 146.91050729, 0.02580842, 146.91050729, 0.07742526, 102.8373551, -1298.4847825, 0.05, 2, 0, 72012, 23012, 1, 3)
    ops.uniaxialMaterial('LimitState', 32012, 36.72762682, 6.052e-05, 110.18288046, 0.00018157, 367.27626821, 0.00060523, -36.72762682, -6.052e-05, -110.18288046, -0.00018157, -367.27626821, -0.00060523, 0.4, 0.3, 0.003, 0.0, 0.0, 12012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2012, 99999, 'P', 42012, 'Vy', 32012, 'Vz', 22012, 'My', 12012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172012, 72012, 172012, 2012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123012, 123012, 23012, 2012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172013, 0.0, 15.45, 6.8)
    ops.node(123013, 0.0, 15.45, 9.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2013, 172013, 123013, 0.1, 27713405.78159033, 11547252.40899597, 0.00127345, 0.00057292, 0.00146667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22013, 76.21868276, 0.0008667, 92.72442884, 0.01894574, 9.27244288, 0.07367597, -76.21868276, -0.0008667, -92.72442884, -0.01894574, -9.27244288, -0.07367597, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12013, 41.54908164, 0.00127141, 50.54685707, 0.0168386, 5.05468571, 0.05522026, -41.54908164, -0.00127141, -50.54685707, -0.0168386, -5.05468571, -0.05522026, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22013, 2013, 0.0, 116.92635786, 0.01733402, 116.92635786, 0.05200207, 81.8484505, -2353.77874233, 0.05, 2, 0, 72013, 23013, 2, 3)
    ops.uniaxialMaterial('LimitState', 42013, 29.23158947, 8.658e-05, 87.6947684, 0.00025973, 292.31589466, 0.00086576, -29.23158947, -8.658e-05, -87.6947684, -0.00025973, -292.31589466, -0.00086576, 0.4, 0.3, 0.003, 0.0, 0.0, 22013, 2)
    ops.limitCurve('ThreePoint', 12013, 2013, 0.0, 94.6935632, 0.02542828, 94.6935632, 0.07628483, 66.28549424, -1266.98400396, 0.05, 2, 0, 72013, 23013, 1, 3)
    ops.uniaxialMaterial('LimitState', 32013, 23.6733908, 7.011e-05, 71.0201724, 0.00021034, 236.733908, 0.00070115, -23.6733908, -7.011e-05, -71.0201724, -0.00021034, -236.733908, -0.00070115, 0.4, 0.3, 0.003, 0.0, 0.0, 12013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2013, 99999, 'P', 42013, 'Vy', 32013, 'Vz', 22013, 'My', 12013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172013, 72013, 172013, 2013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123013, 123013, 23013, 2013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172014, 2.95, 15.45, 6.825)
    ops.node(123014, 2.95, 15.45, 9.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2014, 172014, 123014, 0.1875, 28408137.80361635, 11836724.08484015, 0.00308678, 0.00107422, 0.00966797, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22014, 305.9066835, 0.0006731, 371.63559229, 0.04570651, 37.16355923, 0.13063418, -305.9066835, -0.0006731, -371.63559229, -0.04570651, -37.16355923, -0.13063418, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12014, 97.64825713, 0.00147396, 118.62953584, 0.03274316, 11.86295358, 0.06849239, -97.64825713, -0.00147396, -118.62953584, -0.03274316, -11.86295358, -0.06849239, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22014, 2014, 0.0, 385.16429372, 0.01346195, 385.16429372, 0.04038585, 269.6150056, -10308.15260489, 0.05, 2, 0, 72014, 23014, 2, 3)
    ops.uniaxialMaterial('LimitState', 42014, 96.29107343, 0.00014838, 288.87322029, 0.00044514, 962.91073429, 0.00148381, -96.29107343, -0.00014838, -288.87322029, -0.00044514, -962.91073429, -0.00148381, 0.4, 0.3, 0.003, 0.0, 0.0, 22014, 2)
    ops.limitCurve('ThreePoint', 12014, 2014, 0.0, 177.66954121, 0.02947914, 177.66954121, 0.08843743, 124.36867885, -2195.60277972, 0.05, 2, 0, 72014, 23014, 1, 3)
    ops.uniaxialMaterial('LimitState', 32014, 44.4173853, 6.845e-05, 133.25215591, 0.00020534, 444.17385302, 0.00068446, -44.4173853, -6.845e-05, -133.25215591, -0.00020534, -444.17385302, -0.00068446, 0.4, 0.3, 0.003, 0.0, 0.0, 12014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2014, 99999, 'P', 42014, 'Vy', 32014, 'Vz', 22014, 'My', 12014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172014, 72014, 172014, 2014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123014, 123014, 23014, 2014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172015, 7.7, 15.45, 6.825)
    ops.node(123015, 7.7, 15.45, 9.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2015, 172015, 123015, 0.315, 29458187.76720933, 12274244.90300389, 0.00971719, 0.00353719, 0.02338875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22015, 604.03721925, 0.00062216, 733.29856294, 0.03497308, 73.32985629, 0.08887274, -604.03721925, -0.00062216, -733.29856294, -0.03497308, -73.32985629, -0.08887274, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12015, 185.74609499, 0.00102404, 225.49495327, 0.02723849, 22.54949533, 0.05562476, -185.74609499, -0.00102404, -225.49495327, -0.02723849, -22.54949533, -0.05562476, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22015, 2015, 0.0, 573.8637999, 0.01244321, 573.8637999, 0.03732962, 401.70465993, -8832.63676576, 0.05, 2, 0, 72015, 23015, 2, 3)
    ops.uniaxialMaterial('LimitState', 42015, 143.46594997, 0.0001269, 430.39784992, 0.00038071, 1434.65949975, 0.00126902, -143.46594997, -0.0001269, -430.39784992, -0.00038071, -1434.65949975, -0.00126902, 0.4, 0.3, 0.003, 0.0, 0.0, 22015, 2)
    ops.limitCurve('ThreePoint', 12015, 2015, 0.0, 265.42394259, 0.02048077, 265.42394259, 0.0614423, 185.79675981, -2496.95636476, 0.05, 2, 0, 72015, 23015, 1, 3)
    ops.uniaxialMaterial('LimitState', 32015, 66.35598565, 5.869e-05, 199.06795694, 0.00017608, 663.55985647, 0.00058695, -66.35598565, -5.869e-05, -199.06795694, -0.00017608, -663.55985647, -0.00058695, 0.4, 0.3, 0.003, 0.0, 0.0, 12015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2015, 99999, 'P', 42015, 'Vy', 32015, 'Vz', 22015, 'My', 12015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172015, 72015, 172015, 2015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123015, 123015, 23015, 2015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172016, 12.45, 15.45, 6.8)
    ops.node(123016, 12.45, 15.45, 9.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2016, 172016, 123016, 0.1625, 28711573.28921484, 11963155.53717285, 0.0025666, 0.00093099, 0.00629349, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22016, 217.72418346, 0.00068733, 264.45028332, 0.02386505, 26.44502833, 0.0801634, -217.72418346, -0.00068733, -264.45028332, -0.02386505, -26.44502833, -0.0801634, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12016, 69.632826, 0.00137686, 84.57682684, 0.01884213, 8.45768268, 0.04761453, -69.632826, -0.00137686, -84.57682684, -0.01884213, -8.45768268, -0.04761453, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22016, 2016, 0.0, 233.5440773, 0.01374656, 233.5440773, 0.04123967, 163.48085411, -3564.67332944, 0.05, 2, 0, 72016, 23016, 2, 3)
    ops.uniaxialMaterial('LimitState', 42016, 58.38601932, 0.00010272, 175.15805797, 0.00030815, 583.86019325, 0.00102715, -58.38601932, -0.00010272, -175.15805797, -0.00030815, -583.86019325, -0.00102715, 0.4, 0.3, 0.003, 0.0, 0.0, 22016, 2)
    ops.limitCurve('ThreePoint', 12016, 2016, 0.0, 130.41408858, 0.02753722, 130.41408858, 0.08261165, 91.28986201, -1143.21354513, 0.05, 2, 0, 72016, 23016, 1, 3)
    ops.uniaxialMaterial('LimitState', 32016, 32.60352214, 5.736e-05, 97.81056643, 0.00017207, 326.03522145, 0.00057358, -32.60352214, -5.736e-05, -97.81056643, -0.00017207, -326.03522145, -0.00057358, 0.4, 0.3, 0.003, 0.0, 0.0, 12016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2016, 99999, 'P', 42016, 'Vy', 32016, 'Vz', 22016, 'My', 12016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172016, 72016, 172016, 2016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123016, 123016, 23016, 2016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172017, 0.0, 20.6, 6.8)
    ops.node(123017, 0.0, 20.6, 9.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2017, 172017, 123017, 0.1, 26524091.41939091, 11051704.75807955, 0.00127345, 0.00057292, 0.00146667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22017, 72.18657916, 0.00085458, 87.96904801, 0.01837579, 8.7969048, 0.07139747, -72.18657916, -0.00085458, -87.96904801, -0.01837579, -8.7969048, -0.07139747, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12017, 39.40275727, 0.00126851, 48.01755516, 0.01635537, 4.80175552, 0.05353884, -39.40275727, -0.00126851, -48.01755516, -0.01635537, -4.80175552, -0.05353884, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22017, 2017, 0.0, 110.30376019, 0.0170916, 110.30376019, 0.05127479, 77.21263213, -2173.20333192, 0.05, 2, 0, 72017, 23017, 2, 3)
    ops.uniaxialMaterial('LimitState', 42017, 27.57594005, 8.533e-05, 82.72782014, 0.000256, 275.75940048, 0.00085335, -27.57594005, -8.533e-05, -82.72782014, -0.000256, -275.75940048, -0.00085335, 0.4, 0.3, 0.003, 0.0, 0.0, 22017, 2)
    ops.limitCurve('ThreePoint', 12017, 2017, 0.0, 85.90769783, 0.02537012, 85.90769783, 0.07611037, 60.13538848, -1183.9371878, 0.05, 2, 0, 72017, 23017, 1, 3)
    ops.uniaxialMaterial('LimitState', 32017, 21.47692446, 6.646e-05, 64.43077337, 0.00019938, 214.76924458, 0.00066461, -21.47692446, -6.646e-05, -64.43077337, -0.00019938, -214.76924458, -0.00066461, 0.4, 0.3, 0.003, 0.0, 0.0, 12017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2017, 99999, 'P', 42017, 'Vy', 32017, 'Vz', 22017, 'My', 12017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172017, 72017, 172017, 2017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123017, 123017, 23017, 2017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172018, 2.95, 20.6, 6.825)
    ops.node(123018, 2.95, 20.6, 9.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2018, 172018, 123018, 0.1875, 33340524.8414375, 13891885.35059896, 0.00308678, 0.00107422, 0.00966797, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22018, 319.15106139, 0.00065241, 382.7383157, 0.0405108, 38.27383157, 0.13240788, -319.15106139, -0.00065241, -382.7383157, -0.0405108, -38.27383157, -0.13240788, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12018, 103.25520933, 0.00136773, 123.8276468, 0.02904362, 12.38276468, 0.06772654, -103.25520933, -0.00136773, -123.8276468, -0.02904362, -12.38276468, -0.06772654, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22018, 2018, 0.0, 410.41051716, 0.01304814, 410.41051716, 0.03914441, 287.28736201, -8494.53385576, 0.05, 2, 0, 72018, 23018, 2, 3)
    ops.uniaxialMaterial('LimitState', 42018, 102.60262929, 0.00013472, 307.80788787, 0.00040415, 1026.0262929, 0.00134717, -102.60262929, -0.00013472, -307.80788787, -0.00040415, -1026.0262929, -0.00134717, 0.4, 0.3, 0.003, 0.0, 0.0, 22018, 2)
    ops.limitCurve('ThreePoint', 12018, 2018, 0.0, 198.48492414, 0.02735457, 198.48492414, 0.08206372, 138.9394469, -1912.85232276, 0.05, 2, 0, 72018, 23018, 1, 3)
    ops.uniaxialMaterial('LimitState', 32018, 49.62123104, 6.515e-05, 148.86369311, 0.00019546, 496.21231035, 0.00065153, -49.62123104, -6.515e-05, -148.86369311, -0.00019546, -496.21231035, -0.00065153, 0.4, 0.3, 0.003, 0.0, 0.0, 12018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2018, 99999, 'P', 42018, 'Vy', 32018, 'Vz', 22018, 'My', 12018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172018, 72018, 172018, 2018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123018, 123018, 23018, 2018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172019, 7.7, 20.6, 6.825)
    ops.node(123019, 7.7, 20.6, 9.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2019, 172019, 123019, 0.315, 29093011.75661206, 12122088.23192169, 0.00971719, 0.00353719, 0.02338875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22019, 611.63309303, 0.00063058, 743.14023166, 0.03278028, 74.31402317, 0.08638942, -611.63309303, -0.00063058, -743.14023166, -0.03278028, -74.31402317, -0.08638942, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12019, 187.92698186, 0.00104439, 228.33313375, 0.02557902, 22.83331338, 0.05381228, -187.92698186, -0.00104439, -228.33313375, -0.02557902, -22.83331338, -0.05381228, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22019, 2019, 0.0, 547.50087837, 0.01261157, 547.50087837, 0.03783472, 383.25061486, -7514.59032173, 0.05, 2, 0, 72019, 23019, 2, 3)
    ops.uniaxialMaterial('LimitState', 42019, 136.87521959, 0.00012259, 410.62565878, 0.00036778, 1368.75219592, 0.00122592, -136.87521959, -0.00012259, -410.62565878, -0.00036778, -1368.75219592, -0.00122592, 0.4, 0.3, 0.003, 0.0, 0.0, 22019, 2)
    ops.limitCurve('ThreePoint', 12019, 2019, 0.0, 254.42114562, 0.02088788, 254.42114562, 0.06266365, 178.09480193, -2221.46928063, 0.05, 2, 0, 72019, 23019, 1, 3)
    ops.uniaxialMaterial('LimitState', 32019, 63.6052864, 5.697e-05, 190.81585921, 0.0001709, 636.05286405, 0.00056968, -63.6052864, -5.697e-05, -190.81585921, -0.0001709, -636.05286405, -0.00056968, 0.4, 0.3, 0.003, 0.0, 0.0, 12019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2019, 99999, 'P', 42019, 'Vy', 32019, 'Vz', 22019, 'My', 12019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172019, 72019, 172019, 2019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123019, 123019, 23019, 2019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172020, 12.45, 20.6, 6.8)
    ops.node(123020, 12.45, 20.6, 9.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2020, 172020, 123020, 0.1625, 29369354.30670407, 12237230.96112669, 0.0025666, 0.00093099, 0.00629349, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22020, 216.23854304, 0.00066636, 262.28513196, 0.02760972, 26.2285132, 0.08462168, -216.23854304, -0.00066636, -262.28513196, -0.02760972, -26.2285132, -0.08462168, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12020, 69.52266033, 0.00129347, 84.3270579, 0.02159629, 8.43270579, 0.05073339, -69.52266033, -0.00129347, -84.3270579, -0.02159629, -8.43270579, -0.05073339, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22020, 2020, 0.0, 262.46539974, 0.01332728, 262.46539974, 0.03998183, 183.72577982, -5038.92012829, 0.05, 2, 0, 72020, 23020, 2, 3)
    ops.uniaxialMaterial('LimitState', 42020, 65.61634993, 0.00011285, 196.8490498, 0.00033855, 656.16349934, 0.0011285, -65.61634993, -0.00011285, -196.8490498, -0.00033855, -656.16349934, -0.0011285, 0.4, 0.3, 0.003, 0.0, 0.0, 22020, 2)
    ops.limitCurve('ThreePoint', 12020, 2020, 0.0, 145.22514679, 0.02586947, 145.22514679, 0.07760842, 101.65760275, -1455.42874781, 0.05, 2, 0, 72020, 23020, 1, 3)
    ops.uniaxialMaterial('LimitState', 32020, 36.3062867, 6.244e-05, 108.91886009, 0.00018732, 363.06286697, 0.00062441, -36.3062867, -6.244e-05, -108.91886009, -0.00018732, -363.06286697, -0.00062441, 0.4, 0.3, 0.003, 0.0, 0.0, 12020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2020, 99999, 'P', 42020, 'Vy', 32020, 'Vz', 22020, 'My', 12020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172020, 72020, 172020, 2020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123020, 123020, 23020, 2020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172021, 0.0, 25.75, 6.8)
    ops.node(123021, 0.0, 25.75, 9.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2021, 172021, 123021, 0.1, 28556396.76498147, 11898498.65207561, 0.00127345, 0.00057292, 0.00146667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22021, 73.22033606, 0.00083683, 88.94358178, 0.01753145, 8.89435818, 0.07331979, -73.22033606, -0.00083683, -88.94358178, -0.01753145, -8.89435818, -0.07331979, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12021, 40.02769249, 0.00123322, 48.62319038, 0.01560833, 4.86231904, 0.05473203, -40.02769249, -0.00123322, -48.62319038, -0.01560833, -4.86231904, -0.05473203, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22021, 2021, 0.0, 113.38521279, 0.01673654, 113.38521279, 0.05020963, 79.36964896, -2028.9605196, 0.05, 2, 0, 72021, 23021, 2, 3)
    ops.uniaxialMaterial('LimitState', 42021, 28.3463032, 8.148e-05, 85.0389096, 0.00024443, 283.46303198, 0.00081476, -28.3463032, -8.148e-05, -85.0389096, -0.00024443, -283.46303198, -0.00081476, 0.4, 0.3, 0.003, 0.0, 0.0, 22021, 2)
    ops.limitCurve('ThreePoint', 12021, 2021, 0.0, 86.89510765, 0.0246643, 86.89510765, 0.07399291, 60.82657535, -1117.22129239, 0.05, 2, 0, 72021, 23021, 1, 3)
    ops.uniaxialMaterial('LimitState', 32021, 21.72377691, 6.244e-05, 65.17133073, 0.00018732, 217.23776911, 0.00062441, -21.72377691, -6.244e-05, -65.17133073, -0.00018732, -217.23776911, -0.00062441, 0.4, 0.3, 0.003, 0.0, 0.0, 12021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2021, 99999, 'P', 42021, 'Vy', 32021, 'Vz', 22021, 'My', 12021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172021, 72021, 172021, 2021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123021, 123021, 23021, 2021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172022, 2.95, 25.75, 6.825)
    ops.node(123022, 2.95, 25.75, 9.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2022, 172022, 123022, 0.1875, 28238947.50153174, 11766228.12563823, 0.00308678, 0.00107422, 0.00966797, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22022, 301.0175915, 0.00065175, 365.80838341, 0.04674316, 36.58083834, 0.13134572, -301.0175915, -0.00065175, -365.80838341, -0.04674316, -36.58083834, -0.13134572, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12022, 98.06989357, 0.00136297, 119.17838107, 0.0333668, 11.91783811, 0.06897917, -98.06989357, -0.00136297, -119.17838107, -0.0333668, -11.91783811, -0.06897917, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22022, 2022, 0.0, 387.62787152, 0.01303502, 387.62787152, 0.03910505, 271.33951006, -10652.07149484, 0.05, 2, 0, 72022, 23022, 2, 3)
    ops.uniaxialMaterial('LimitState', 42022, 96.90696788, 0.00015023, 290.72090364, 0.00045068, 969.06967879, 0.00150225, -96.90696788, -0.00015023, -290.72090364, -0.00045068, -969.06967879, -0.00150225, 0.4, 0.3, 0.003, 0.0, 0.0, 22022, 2)
    ops.limitCurve('ThreePoint', 12022, 2022, 0.0, 178.08718926, 0.02725942, 178.08718926, 0.08177826, 124.66103248, -2248.39020188, 0.05, 2, 0, 72022, 23022, 1, 3)
    ops.uniaxialMaterial('LimitState', 32022, 44.52179732, 6.902e-05, 133.56539195, 0.00020705, 445.21797316, 0.00069018, -44.52179732, -6.902e-05, -133.56539195, -0.00020705, -445.21797316, -0.00069018, 0.4, 0.3, 0.003, 0.0, 0.0, 12022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2022, 99999, 'P', 42022, 'Vy', 32022, 'Vz', 22022, 'My', 12022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172022, 72022, 172022, 2022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123022, 123022, 23022, 2022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172023, 7.7, 25.75, 6.825)
    ops.node(123023, 7.7, 25.75, 9.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2023, 172023, 123023, 0.315, 28849828.05117931, 12020761.68799138, 0.00971719, 0.00353719, 0.02338875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22023, 592.15250789, 0.0006183, 719.85558459, 0.03491152, 71.98555846, 0.08831916, -592.15250789, -0.0006183, -719.85558459, -0.03491152, -71.98555846, -0.08831916, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12023, 181.91339016, 0.0010196, 221.14466809, 0.02719002, 22.11446681, 0.05531717, -181.91339016, -0.0010196, -221.14466809, -0.02719002, -22.11446681, -0.05531717, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22023, 2023, 0.0, 551.59902637, 0.01236597, 551.59902637, 0.0370979, 386.11931846, -8077.37202592, 0.05, 2, 0, 72023, 23023, 2, 3)
    ops.uniaxialMaterial('LimitState', 42023, 137.89975659, 0.00012455, 413.69926978, 0.00037365, 1378.99756592, 0.00124551, -137.89975659, -0.00012455, -413.69926978, -0.00037365, -1378.99756592, -0.00124551, 0.4, 0.3, 0.003, 0.0, 0.0, 22023, 2)
    ops.limitCurve('ThreePoint', 12023, 2023, 0.0, 255.51832666, 0.02039201, 255.51832666, 0.06117604, 178.86282866, -2339.85374496, 0.05, 2, 0, 72023, 23023, 1, 3)
    ops.uniaxialMaterial('LimitState', 32023, 63.87958166, 5.77e-05, 191.63874499, 0.00017309, 638.79581664, 0.00057696, -63.87958166, -5.77e-05, -191.63874499, -0.00017309, -638.79581664, -0.00057696, 0.4, 0.3, 0.003, 0.0, 0.0, 12023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2023, 99999, 'P', 42023, 'Vy', 32023, 'Vz', 22023, 'My', 12023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172023, 72023, 172023, 2023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123023, 123023, 23023, 2023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172024, 12.45, 25.75, 6.8)
    ops.node(123024, 12.45, 25.75, 9.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2024, 172024, 123024, 0.1625, 31096026.82304648, 12956677.84293604, 0.0025666, 0.00093099, 0.00629349, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22024, 220.25932864, 0.00066571, 266.02954556, 0.02644752, 26.60295456, 0.08506941, -220.25932864, -0.00066571, -266.02954556, -0.02644752, -26.60295456, -0.08506941, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12024, 70.89157057, 0.00128943, 85.62294465, 0.02071697, 8.56229446, 0.05067686, -70.89157057, -0.00128943, -85.62294465, -0.02071697, -8.56229446, -0.05067686, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22024, 2024, 0.0, 274.19752827, 0.01331423, 274.19752827, 0.03994269, 191.93826979, -4999.1273902, 0.05, 2, 0, 72024, 23024, 2, 3)
    ops.uniaxialMaterial('LimitState', 42024, 68.54938207, 0.00011135, 205.6481462, 0.00033404, 685.49382068, 0.00111348, -68.54938207, -0.00011135, -205.6481462, -0.00033404, -685.49382068, -0.00111348, 0.4, 0.3, 0.003, 0.0, 0.0, 22024, 2)
    ops.limitCurve('ThreePoint', 12024, 2024, 0.0, 153.44484007, 0.02578856, 153.44484007, 0.07736568, 107.41138805, -1447.19870833, 0.05, 2, 0, 72024, 23024, 1, 3)
    ops.uniaxialMaterial('LimitState', 32024, 38.36121002, 6.231e-05, 115.08363005, 0.00018694, 383.61210016, 0.00062312, -38.36121002, -6.231e-05, -115.08363005, -0.00018694, -383.61210016, -0.00062312, 0.4, 0.3, 0.003, 0.0, 0.0, 12024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2024, 99999, 'P', 42024, 'Vy', 32024, 'Vz', 22024, 'My', 12024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172024, 72024, 172024, 2024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123024, 123024, 23024, 2024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172025, 0.0, 30.9, 6.8)
    ops.node(123025, 0.0, 30.9, 9.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2025, 172025, 123025, 0.0625, 30488544.4621688, 12703560.19257033, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22025, 28.41239292, 0.00124493, 34.38620785, 0.01907807, 3.43862078, 0.07792065, -28.41239292, -0.00124493, -34.38620785, -0.01907807, -3.43862078, -0.07792065, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12025, 28.41239292, 0.00124493, 34.38620785, 0.01907807, 3.43862078, 0.07792065, -28.41239292, -0.00124493, -34.38620785, -0.01907807, -3.43862078, -0.07792065, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22025, 2025, 0.0, 77.54708931, 0.02489851, 77.54708931, 0.07469554, 54.28296252, -1566.14216796, 0.05, 2, 0, 72025, 23025, 2, 3)
    ops.uniaxialMaterial('LimitState', 42025, 19.38677233, 8.351e-05, 58.16031698, 0.00025052, 193.86772328, 0.00083508, -19.38677233, -8.351e-05, -58.16031698, -0.00025052, -193.86772328, -0.00083508, 0.4, 0.3, 0.003, 0.0, 0.0, 22025, 2)
    ops.limitCurve('ThreePoint', 12025, 2025, 0.0, 77.54708931, 0.02489851, 77.54708931, 0.07469554, 54.28296252, -1566.14216796, 0.05, 2, 0, 72025, 23025, 1, 3)
    ops.uniaxialMaterial('LimitState', 32025, 19.38677233, 8.351e-05, 58.16031698, 0.00025052, 193.86772328, 0.00083508, -19.38677233, -8.351e-05, -58.16031698, -0.00025052, -193.86772328, -0.00083508, 0.4, 0.3, 0.003, 0.0, 0.0, 12025, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2025, 99999, 'P', 42025, 'Vy', 32025, 'Vz', 22025, 'My', 12025, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172025, 72025, 172025, 2025, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123025, 123025, 23025, 2025, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172026, 2.95, 30.9, 6.825)
    ops.node(123026, 2.95, 30.9, 9.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2026, 172026, 123026, 0.175, 28815020.79176477, 12006258.66323532, 0.00405757, 0.00401042, 0.0019651, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22026, 103.24021853, 0.00097241, 125.55744181, 0.03426899, 12.55574418, 0.08539754, -103.24021853, -0.00097241, -125.55744181, -0.03426899, -12.55574418, -0.08539754, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12026, 137.99078653, 0.00075933, 167.8199678, 0.03830056, 16.78199678, 0.10626325, -137.99078653, -0.00075933, -167.8199678, -0.03830056, -16.78199678, -0.10626325, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22026, 2026, 0.0, 193.19273556, 0.01944814, 193.19273556, 0.05834441, 135.23491489, -4026.19876285, 0.05, 2, 0, 72026, 23026, 2, 3)
    ops.uniaxialMaterial('LimitState', 42026, 48.29818389, 7.862e-05, 144.89455167, 0.00023585, 482.98183889, 0.00078616, -48.29818389, -7.862e-05, -144.89455167, -0.00023585, -482.98183889, -0.00078616, 0.4, 0.3, 0.003, 0.0, 0.0, 22026, 2)
    ops.limitCurve('ThreePoint', 12026, 2026, 0.0, 245.02756538, 0.01518667, 245.02756538, 0.04556, 171.51929577, -7038.87254863, 0.05, 2, 0, 72026, 23026, 1, 3)
    ops.uniaxialMaterial('LimitState', 32026, 61.25689135, 9.971e-05, 183.77067404, 0.00029913, 612.56891345, 0.00099709, -61.25689135, -9.971e-05, -183.77067404, -0.00029913, -612.56891345, -0.00099709, 0.4, 0.3, 0.003, 0.0, 0.0, 12026, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2026, 99999, 'P', 42026, 'Vy', 32026, 'Vz', 22026, 'My', 12026, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172026, 72026, 172026, 2026, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123026, 123026, 23026, 2026, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172027, 7.7, 30.9, 6.825)
    ops.node(123027, 7.7, 30.9, 9.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2027, 172027, 123027, 0.24, 25682464.47562659, 10701026.86484441, 0.00751249, 0.00792, 0.00352, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22027, 158.84771205, 0.00097165, 194.3335395, 0.03562027, 19.43335395, 0.07832735, -158.84771205, -0.00097165, -194.3335395, -0.03562027, -19.43335395, -0.07832735, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12027, 276.74014259, 0.00074804, 338.56258134, 0.04026552, 33.85625813, 0.09860387, -276.74014259, -0.00074804, -338.56258134, -0.04026552, -33.85625813, -0.09860387, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22027, 2027, 0.0, 211.39134903, 0.019433, 211.39134903, 0.058299, 147.97394432, -3805.34812561, 0.05, 2, 0, 72027, 23027, 2, 3)
    ops.uniaxialMaterial('LimitState', 42027, 52.84783726, 7.037e-05, 158.54351177, 0.00021112, 528.47837257, 0.00070375, -52.84783726, -7.037e-05, -158.54351177, -0.00021112, -528.47837257, -0.00070375, 0.4, 0.3, 0.003, 0.0, 0.0, 22027, 2)
    ops.limitCurve('ThreePoint', 12027, 2027, 0.0, 299.33819738, 0.01496087, 299.33819738, 0.04488262, 209.53673816, -7007.20134744, 0.05, 2, 0, 72027, 23027, 1, 3)
    ops.uniaxialMaterial('LimitState', 32027, 74.83454934, 9.965e-05, 224.50364803, 0.00029896, 748.34549344, 0.00099653, -74.83454934, -9.965e-05, -224.50364803, -0.00029896, -748.34549344, -0.00099653, 0.4, 0.3, 0.003, 0.0, 0.0, 12027, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2027, 99999, 'P', 42027, 'Vy', 32027, 'Vz', 22027, 'My', 12027, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172027, 72027, 172027, 2027, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123027, 123027, 23027, 2027, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172028, 12.45, 30.9, 6.8)
    ops.node(123028, 12.45, 30.9, 9.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2028, 172028, 123028, 0.0875, 30854831.70625789, 12856179.87760746, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22028, 41.38547462, 0.00123332, 50.0136371, 0.0198882, 5.00136371, 0.0648855, -41.38547462, -0.00123332, -50.0136371, -0.0198882, -5.00136371, -0.0648855, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12028, 55.31118168, 0.00091901, 66.84261553, 0.02172163, 6.68426155, 0.07999194, -55.31118168, -0.00091901, -66.84261553, -0.02172163, -6.68426155, -0.07999194, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22028, 2028, 0.0, 100.06806225, 0.02466649, 100.06806225, 0.07399948, 70.04764357, -1530.17670382, 0.05, 2, 0, 72028, 23028, 2, 3)
    ops.uniaxialMaterial('LimitState', 42028, 25.01701556, 7.606e-05, 75.05104668, 0.00022817, 250.17015561, 0.00076057, -25.01701556, -7.606e-05, -75.05104668, -0.00022817, -250.17015561, -0.00076057, 0.4, 0.3, 0.003, 0.0, 0.0, 22028, 2)
    ops.limitCurve('ThreePoint', 12028, 2028, 0.0, 116.72404457, 0.01838024, 116.72404457, 0.05514072, 81.7068312, -2454.46568295, 0.05, 2, 0, 72028, 23028, 1, 3)
    ops.uniaxialMaterial('LimitState', 32028, 29.18101114, 8.872e-05, 87.54303342, 0.00026615, 291.81011141, 0.00088717, -29.18101114, -8.872e-05, -87.54303342, -0.00026615, -291.81011141, -0.00088717, 0.4, 0.3, 0.003, 0.0, 0.0, 12028, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2028, 99999, 'P', 42028, 'Vy', 32028, 'Vz', 22028, 'My', 12028, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172028, 72028, 172028, 2028, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123028, 123028, 23028, 2028, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173003, 7.7, 0.0, 9.675)
    ops.node(124003, 7.7, 0.0, 12.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3003, 173003, 124003, 0.24, 28288923.7208566, 11787051.55035692, 0.00751249, 0.00792, 0.00352, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23003, 118.40678013, 0.00093225, 144.62885144, 0.028221, 14.46288514, 0.06807274, -118.40678013, -0.00093225, -144.62885144, -0.028221, -14.46288514, -0.06807274, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13003, 220.51025399, 0.00071834, 269.3439069, 0.03153419, 26.93439069, 0.08470474, -220.51025399, -0.00071834, -269.3439069, -0.03153419, -26.93439069, -0.08470474, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23003, 3003, 0.0, 207.22102226, 0.01864497, 207.22102226, 0.05593492, 145.05471558, -6551.7260034, 0.05, 2, 0, 73003, 24003, 2, 3)
    ops.uniaxialMaterial('LimitState', 43003, 51.80525556, 6.263e-05, 155.41576669, 0.00018789, 518.05255565, 0.0006263, -51.80525556, -6.263e-05, -155.41576669, -0.00018789, -518.05255565, -0.0006263, 0.4, 0.3, 0.003, 0.0, 0.0, 23003, 2)
    ops.limitCurve('ThreePoint', 13003, 3003, 0.0, 292.30112512, 0.01436686, 292.30112512, 0.04310058, 204.61078759, -13567.93210424, 0.05, 2, 0, 73003, 24003, 1, 3)
    ops.uniaxialMaterial('LimitState', 33003, 73.07528128, 8.834e-05, 219.22584384, 0.00026503, 730.7528128, 0.00088345, -73.07528128, -8.834e-05, -219.22584384, -0.00026503, -730.7528128, -0.00088345, 0.4, 0.3, 0.003, 0.0, 0.0, 13003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3003, 99999, 'P', 43003, 'Vy', 33003, 'Vz', 23003, 'My', 13003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173003, 73003, 173003, 3003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124003, 124003, 24003, 3003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173004, 12.45, 0.0, 9.65)
    ops.node(124004, 12.45, 0.0, 12.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3004, 173004, 124004, 0.0875, 29721660.9941299, 12384025.41422079, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23004, 30.72040185, 0.00113973, 37.3695325, 0.0169838, 3.73695325, 0.06640822, -30.72040185, -0.00113973, -37.3695325, -0.0169838, -3.73695325, -0.06640822, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13004, 49.96357463, 0.0008631, 60.77770189, 0.01853131, 6.07777019, 0.08253462, -49.96357463, -0.0008631, -60.77770189, -0.01853131, -6.07777019, -0.08253462, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23004, 3004, 0.0, 74.59889649, 0.02279456, 74.59889649, 0.06838369, 52.21922754, -2107.56466472, 0.05, 2, 0, 73004, 24004, 2, 3)
    ops.uniaxialMaterial('LimitState', 43004, 18.64972412, 5.886e-05, 55.94917236, 0.00017658, 186.49724121, 0.00058861, -18.64972412, -5.886e-05, -55.94917236, -0.00017658, -186.49724121, -0.00058861, 0.4, 0.3, 0.003, 0.0, 0.0, 23004, 2)
    ops.limitCurve('ThreePoint', 13004, 3004, 0.0, 95.22045556, 0.01726204, 95.22045556, 0.05178612, 66.65431889, -3779.77891672, 0.05, 2, 0, 73004, 24004, 1, 3)
    ops.uniaxialMaterial('LimitState', 33004, 23.80511389, 7.513e-05, 71.41534167, 0.0002254, 238.0511389, 0.00075132, -23.80511389, -7.513e-05, -71.41534167, -0.0002254, -238.0511389, -0.00075132, 0.4, 0.3, 0.003, 0.0, 0.0, 13004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3004, 99999, 'P', 43004, 'Vy', 33004, 'Vz', 23004, 'My', 13004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173004, 73004, 173004, 3004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124004, 124004, 24004, 3004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173005, 0.0, 5.15, 9.65)
    ops.node(124005, 0.0, 5.15, 12.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3005, 173005, 124005, 0.0875, 26109851.63553866, 10879104.84814111, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23005, 48.87827509, 0.00099021, 59.87403679, 0.02405256, 5.98740368, 0.08428917, -48.87827509, -0.00099021, -59.87403679, -0.02405256, -5.98740368, -0.08428917, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13005, 30.67552477, 0.00138333, 37.57635668, 0.02206464, 3.75763567, 0.06858035, -30.67552477, -0.00138333, -37.57635668, -0.02206464, -3.75763567, -0.06858035, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23005, 3005, 0.0, 100.55960889, 0.01980423, 100.55960889, 0.0594127, 70.39172622, -4203.65205466, 0.05, 2, 0, 73005, 24005, 2, 3)
    ops.uniaxialMaterial('LimitState', 43005, 25.13990222, 9.032e-05, 75.41970667, 0.00027096, 251.39902223, 0.00090321, -25.13990222, -9.032e-05, -75.41970667, -0.00027096, -251.39902223, -0.00090321, 0.4, 0.3, 0.003, 0.0, 0.0, 23005, 2)
    ops.limitCurve('ThreePoint', 13005, 3005, 0.0, 83.61407135, 0.02766669, 83.61407135, 0.08300006, 58.52984994, -2378.92595785, 0.05, 2, 0, 73005, 24005, 1, 3)
    ops.uniaxialMaterial('LimitState', 33005, 20.90351784, 7.51e-05, 62.71055351, 0.0002253, 209.03517836, 0.00075101, -20.90351784, -7.51e-05, -62.71055351, -0.0002253, -209.03517836, -0.00075101, 0.4, 0.3, 0.003, 0.0, 0.0, 13005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3005, 99999, 'P', 43005, 'Vy', 33005, 'Vz', 23005, 'My', 13005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173005, 73005, 173005, 3005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124005, 124005, 24005, 3005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173006, 2.95, 5.15, 9.675)
    ops.node(124006, 2.95, 5.15, 12.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3006, 173006, 124006, 0.1875, 30098005.68731456, 12540835.70304773, 0.00308678, 0.00107422, 0.00966797, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23006, 230.70129453, 0.00064224, 280.19699178, 0.02547417, 28.01969918, 0.08021096, -230.70129453, -0.00064224, -280.19699178, -0.02547417, -28.01969918, -0.08021096, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13006, 67.8471622, 0.00135427, 82.40339868, 0.01977559, 8.24033987, 0.04673079, -67.8471622, -0.00135427, -82.40339868, -0.01977559, -8.24033987, -0.04673079, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23006, 3006, 0.0, 283.49639929, 0.01284474, 283.49639929, 0.03853421, 198.4474795, -6547.6976016, 0.05, 2, 0, 73006, 24006, 2, 3)
    ops.uniaxialMaterial('LimitState', 43006, 70.87409982, 0.00010308, 212.62229947, 0.00030925, 708.74099823, 0.00103083, -70.87409982, -0.00010308, -212.62229947, -0.00030925, -708.74099823, -0.00103083, 0.4, 0.3, 0.003, 0.0, 0.0, 23006, 2)
    ops.limitCurve('ThreePoint', 13006, 3006, 0.0, 131.6916614, 0.02708539, 131.6916614, 0.08125618, 92.18416298, -1219.08728311, 0.05, 2, 0, 73006, 24006, 1, 3)
    ops.uniaxialMaterial('LimitState', 33006, 32.92291535, 4.788e-05, 98.76874605, 0.00014365, 329.22915351, 0.00047885, -32.92291535, -4.788e-05, -98.76874605, -0.00014365, -329.22915351, -0.00047885, 0.4, 0.3, 0.003, 0.0, 0.0, 13006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3006, 99999, 'P', 43006, 'Vy', 33006, 'Vz', 23006, 'My', 13006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173006, 73006, 173006, 3006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124006, 124006, 24006, 3006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173007, 7.7, 5.15, 9.675)
    ops.node(124007, 7.7, 5.15, 12.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3007, 173007, 124007, 0.315, 28852692.34581239, 12021955.1440885, 0.00971719, 0.00353719, 0.02338875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23007, 506.72821706, 0.00060407, 617.87654005, 0.01957371, 61.787654, 0.0553688, -506.72821706, -0.00060407, -617.87654005, -0.01957371, -61.787654, -0.0553688, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13007, 150.86827454, 0.00099918, 183.96048284, 0.01647117, 18.39604828, 0.0385442, -150.86827454, -0.00099918, -183.96048284, -0.01647117, -18.39604828, -0.0385442, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23007, 3007, 0.0, 432.5428252, 0.01208137, 432.5428252, 0.03624411, 302.77997764, -5856.62800997, 0.05, 2, 0, 73007, 24007, 2, 3)
    ops.uniaxialMaterial('LimitState', 43007, 108.1357063, 9.766e-05, 324.4071189, 0.00029298, 1081.35706299, 0.00097658, -108.1357063, -9.766e-05, -324.4071189, -0.00029298, -1081.35706299, -0.00097658, 0.4, 0.3, 0.003, 0.0, 0.0, 23007, 2)
    ops.limitCurve('ThreePoint', 13007, 3007, 0.0, 205.21232495, 0.01998368, 205.21232495, 0.05995104, 143.64862747, -1410.30416527, 0.05, 2, 0, 73007, 24007, 1, 3)
    ops.uniaxialMaterial('LimitState', 33007, 51.30308124, 4.633e-05, 153.90924371, 0.000139, 513.03081238, 0.00046332, -51.30308124, -4.633e-05, -153.90924371, -0.000139, -513.03081238, -0.00046332, 0.4, 0.3, 0.003, 0.0, 0.0, 13007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3007, 99999, 'P', 43007, 'Vy', 33007, 'Vz', 23007, 'My', 13007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173007, 73007, 173007, 3007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124007, 124007, 24007, 3007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173008, 12.45, 5.15, 9.65)
    ops.node(124008, 12.45, 5.15, 12.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3008, 173008, 124008, 0.1625, 29338774.27776011, 12224489.28240005, 0.0025666, 0.00093099, 0.00629349, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23008, 178.29473443, 0.0006468, 217.08777547, 0.01963886, 21.70877755, 0.07487729, -178.29473443, -0.0006468, -217.08777547, -0.01963886, -21.70877755, -0.07487729, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13008, 55.48232513, 0.00125457, 67.55406759, 0.01580101, 6.75540676, 0.04514485, -55.48232513, -0.00125457, -67.55406759, -0.01580101, -6.75540676, -0.04514485, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23008, 3008, 0.0, 203.04920688, 0.01293598, 203.04920688, 0.03880793, 142.13444482, -5058.78153244, 0.05, 2, 0, 73008, 24008, 2, 3)
    ops.uniaxialMaterial('LimitState', 43008, 50.76230172, 8.739e-05, 152.28690516, 0.00026218, 507.6230172, 0.00087394, -50.76230172, -8.739e-05, -152.28690516, -0.00026218, -507.6230172, -0.00087394, 0.4, 0.3, 0.003, 0.0, 0.0, 23008, 2)
    ops.limitCurve('ThreePoint', 13008, 3008, 0.0, 94.64229804, 0.02509145, 94.64229804, 0.07527435, 66.24960863, -1113.29496295, 0.05, 2, 0, 73008, 24008, 1, 3)
    ops.uniaxialMaterial('LimitState', 33008, 23.66057451, 4.073e-05, 70.98172353, 0.0001222, 236.6057451, 0.00040735, -23.66057451, -4.073e-05, -70.98172353, -0.0001222, -236.6057451, -0.00040735, 0.4, 0.3, 0.003, 0.0, 0.0, 13008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3008, 99999, 'P', 43008, 'Vy', 33008, 'Vz', 23008, 'My', 13008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173008, 73008, 173008, 3008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124008, 124008, 24008, 3008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173009, 0.0, 10.3, 9.65)
    ops.node(124009, 0.0, 10.3, 12.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3009, 173009, 124009, 0.1, 28975582.9105846, 12073159.54607692, 0.00127345, 0.00057292, 0.00146667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23009, 60.38089244, 0.0008394, 73.59935431, 0.01858942, 7.35993543, 0.08248987, -60.38089244, -0.0008394, -73.59935431, -0.01858942, -7.35993543, -0.08248987, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13009, 32.1236724, 0.00124586, 39.15612126, 0.01652974, 3.91561213, 0.06134236, -32.1236724, -0.00124586, -39.15612126, -0.01652974, -3.91561213, -0.06134236, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23009, 3009, 0.0, 107.43694072, 0.01678807, 107.43694072, 0.05036422, 75.2058585, -4632.68500435, 0.05, 2, 0, 73009, 24009, 2, 3)
    ops.uniaxialMaterial('LimitState', 43009, 26.85923518, 7.608e-05, 80.57770554, 0.00022825, 268.59235179, 0.00076085, -26.85923518, -7.608e-05, -80.57770554, -0.00022825, -268.59235179, -0.00076085, 0.4, 0.3, 0.003, 0.0, 0.0, 23009, 2)
    ops.limitCurve('ThreePoint', 13009, 3009, 0.0, 82.56017715, 0.02491721, 82.56017715, 0.07475162, 57.792124, -2049.30349634, 0.05, 2, 0, 73009, 24009, 1, 3)
    ops.uniaxialMaterial('LimitState', 33009, 20.64004429, 5.847e-05, 61.92013286, 0.0001754, 206.40044287, 0.00058468, -20.64004429, -5.847e-05, -61.92013286, -0.0001754, -206.40044287, -0.00058468, 0.4, 0.3, 0.003, 0.0, 0.0, 13009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3009, 99999, 'P', 43009, 'Vy', 33009, 'Vz', 23009, 'My', 13009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173009, 73009, 173009, 3009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124009, 124009, 24009, 3009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173010, 2.95, 10.3, 9.675)
    ops.node(124010, 2.95, 10.3, 12.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3010, 173010, 124010, 0.1875, 28684934.03595847, 11952055.84831603, 0.00308678, 0.00107422, 0.00966797, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23010, 218.27625849, 0.00064488, 266.15152538, 0.02512328, 26.61515254, 0.0798025, -218.27625849, -0.00064488, -266.15152538, -0.02512328, -26.61515254, -0.0798025, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13010, 62.82503936, 0.00141873, 76.60466683, 0.01957777, 7.66046668, 0.04650463, -62.82503936, -0.00141873, -76.60466683, -0.01957777, -7.66046668, -0.04650463, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23010, 3010, 0.0, 261.6738655, 0.0128976, 261.6738655, 0.0386928, 183.17170585, -6411.17091802, 0.05, 2, 0, 73010, 24010, 2, 3)
    ops.uniaxialMaterial('LimitState', 43010, 65.41846638, 9.983e-05, 196.25539913, 0.0002995, 654.18466375, 0.00099835, -65.41846638, -9.983e-05, -196.25539913, -0.0002995, -654.18466375, -0.00099835, 0.4, 0.3, 0.003, 0.0, 0.0, 23010, 2)
    ops.limitCurve('ThreePoint', 13010, 3010, 0.0, 114.44278449, 0.02837451, 114.44278449, 0.08512353, 80.10994914, -1161.89221968, 0.05, 2, 0, 73010, 24010, 1, 3)
    ops.uniaxialMaterial('LimitState', 33010, 28.61069612, 4.366e-05, 85.83208837, 0.00013099, 286.10696123, 0.00043663, -28.61069612, -4.366e-05, -85.83208837, -0.00013099, -286.10696123, -0.00043663, 0.4, 0.3, 0.003, 0.0, 0.0, 13010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3010, 99999, 'P', 43010, 'Vy', 33010, 'Vz', 23010, 'My', 13010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173010, 73010, 173010, 3010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124010, 124010, 24010, 3010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173011, 7.7, 10.3, 9.675)
    ops.node(124011, 7.7, 10.3, 12.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3011, 173011, 124011, 0.315, 29578212.84340128, 12324255.3514172, 0.00971719, 0.00353719, 0.02338875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23011, 520.10297637, 0.00061537, 632.98930216, 0.01839799, 63.29893022, 0.05432412, -520.10297637, -0.00061537, -632.98930216, -0.01839799, -63.29893022, -0.05432412, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13011, 154.74666887, 0.00103499, 188.33383077, 0.01553881, 18.83338308, 0.03769265, -154.74666887, -0.00103499, -188.33383077, -0.01553881, -18.83338308, -0.03769265, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23011, 3011, 0.0, 439.05466181, 0.01230739, 439.05466181, 0.03692216, 307.33826327, -5214.08698709, 0.05, 2, 0, 73011, 24011, 2, 3)
    ops.uniaxialMaterial('LimitState', 43011, 109.76366545, 9.67e-05, 329.29099636, 0.00029009, 1097.63665453, 0.00096697, -109.76366545, -9.67e-05, -329.29099636, -0.00029009, -1097.63665453, -0.00096697, 0.4, 0.3, 0.003, 0.0, 0.0, 23011, 2)
    ops.limitCurve('ThreePoint', 13011, 3011, 0.0, 209.21734193, 0.02069979, 209.21734193, 0.06209938, 146.45213935, -1286.94579577, 0.05, 2, 0, 73011, 24011, 1, 3)
    ops.uniaxialMaterial('LimitState', 33011, 52.30433548, 4.608e-05, 156.91300645, 0.00013823, 523.04335483, 0.00046078, -52.30433548, -4.608e-05, -156.91300645, -0.00013823, -523.04335483, -0.00046078, 0.4, 0.3, 0.003, 0.0, 0.0, 13011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3011, 99999, 'P', 43011, 'Vy', 33011, 'Vz', 23011, 'My', 13011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173011, 73011, 173011, 3011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124011, 124011, 24011, 3011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173012, 12.45, 10.3, 9.65)
    ops.node(124012, 12.45, 10.3, 12.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3012, 173012, 124012, 0.1625, 32946150.86175956, 13727562.85906648, 0.0025666, 0.00093099, 0.00629349, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23012, 180.83040814, 0.00063878, 217.7477735, 0.01857199, 21.77477735, 0.0746935, -180.83040814, -0.00063878, -217.7477735, -0.01857199, -21.77477735, -0.0746935, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13012, 56.34584161, 0.00124353, 67.84910614, 0.01497897, 6.78491061, 0.04479192, -56.34584161, -0.00124353, -67.84910614, -0.01497897, -6.78491061, -0.04479192, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23012, 3012, 0.0, 229.75250826, 0.01277563, 229.75250826, 0.03832688, 160.82675578, -5156.11791273, 0.05, 2, 0, 73012, 24012, 2, 3)
    ops.uniaxialMaterial('LimitState', 43012, 57.43812707, 8.806e-05, 172.3143812, 0.00026418, 574.38127066, 0.0008806, -57.43812707, -8.806e-05, -172.3143812, -0.00026418, -574.38127066, -0.0008806, 0.4, 0.3, 0.003, 0.0, 0.0, 23012, 2)
    ops.limitCurve('ThreePoint', 13012, 3012, 0.0, 114.54660631, 0.0248705, 114.54660631, 0.07461151, 80.18262442, -1130.84229581, 0.05, 2, 0, 73012, 24012, 1, 3)
    ops.uniaxialMaterial('LimitState', 33012, 28.63665158, 4.39e-05, 85.90995473, 0.00013171, 286.36651577, 0.00043904, -28.63665158, -4.39e-05, -85.90995473, -0.00013171, -286.36651577, -0.00043904, 0.4, 0.3, 0.003, 0.0, 0.0, 13012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3012, 99999, 'P', 43012, 'Vy', 33012, 'Vz', 23012, 'My', 13012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173012, 73012, 173012, 3012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124012, 124012, 24012, 3012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173013, 0.0, 15.45, 9.65)
    ops.node(124013, 0.0, 15.45, 12.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3013, 173013, 124013, 0.1, 27293166.79645327, 11372152.83185553, 0.00127345, 0.00057292, 0.00146667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23013, 58.58724598, 0.00082441, 71.69390123, 0.02394751, 7.16939012, 0.08719515, -58.58724598, -0.00082441, -71.69390123, -0.02394751, -7.16939012, -0.08719515, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13013, 31.10812415, 0.00121683, 38.067377, 0.02112727, 3.8067377, 0.06548209, -31.10812415, -0.00121683, -38.067377, -0.02112727, -3.8067377, -0.06548209, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23013, 3013, 0.0, 117.09132559, 0.01648823, 117.09132559, 0.04946469, 81.96392792, -7097.23166207, 0.05, 2, 0, 73013, 24013, 2, 3)
    ops.uniaxialMaterial('LimitState', 43013, 29.2728314, 8.803e-05, 87.8184942, 0.0002641, 292.72831399, 0.00088034, -29.2728314, -8.803e-05, -87.8184942, -0.0002641, -292.72831399, -0.00088034, 0.4, 0.3, 0.003, 0.0, 0.0, 23013, 2)
    ops.limitCurve('ThreePoint', 13013, 3013, 0.0, 91.38244607, 0.02433669, 91.38244607, 0.07301006, 63.96771225, -3067.22215115, 0.05, 2, 0, 73013, 24013, 1, 3)
    ops.uniaxialMaterial('LimitState', 33013, 22.84561152, 6.87e-05, 68.53683455, 0.00020611, 228.45611518, 0.00068705, -22.84561152, -6.87e-05, -68.53683455, -0.00020611, -228.45611518, -0.00068705, 0.4, 0.3, 0.003, 0.0, 0.0, 13013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3013, 99999, 'P', 43013, 'Vy', 33013, 'Vz', 23013, 'My', 13013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173013, 73013, 173013, 3013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124013, 124013, 24013, 3013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173014, 2.95, 15.45, 9.675)
    ops.node(124014, 2.95, 15.45, 12.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3014, 173014, 124014, 0.1875, 28507066.29469013, 11877944.28945422, 0.00308678, 0.00107422, 0.00966797, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23014, 221.85048781, 0.00063574, 270.62516018, 0.02587603, 27.06251602, 0.08048697, -221.85048781, -0.00063574, -270.62516018, -0.02587603, -27.06251602, -0.08048697, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13014, 65.545753, 0.00132331, 79.95623575, 0.02004757, 7.99562358, 0.0469408, -65.545753, -0.00132331, -79.95623575, -0.02004757, -7.99562358, -0.0469408, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23014, 3014, 0.0, 259.03759555, 0.01271477, 259.03759555, 0.03814432, 181.32631689, -6290.42560742, 0.05, 2, 0, 73014, 24014, 2, 3)
    ops.uniaxialMaterial('LimitState', 43014, 64.75939889, 9.945e-05, 194.27819666, 0.00029834, 647.59398888, 0.00099446, -64.75939889, -9.945e-05, -194.27819666, -0.00029834, -647.59398888, -0.00099446, 0.4, 0.3, 0.003, 0.0, 0.0, 23014, 2)
    ops.limitCurve('ThreePoint', 13014, 3014, 0.0, 116.97944194, 0.02646629, 116.97944194, 0.07939886, 81.88560936, -1144.74036937, 0.05, 2, 0, 73014, 24014, 1, 3)
    ops.uniaxialMaterial('LimitState', 33014, 29.24486048, 4.491e-05, 87.73458145, 0.00013473, 292.44860485, 0.00044909, -29.24486048, -4.491e-05, -87.73458145, -0.00013473, -292.44860485, -0.00044909, 0.4, 0.3, 0.003, 0.0, 0.0, 13014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3014, 99999, 'P', 43014, 'Vy', 33014, 'Vz', 23014, 'My', 13014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173014, 73014, 173014, 3014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124014, 124014, 24014, 3014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173015, 7.7, 15.45, 9.675)
    ops.node(124015, 7.7, 15.45, 12.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3015, 173015, 124015, 0.315, 26457465.97396301, 11023944.15581792, 0.00971719, 0.00353719, 0.02338875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23015, 508.74552859, 0.00062798, 623.64893263, 0.01855578, 62.36489326, 0.05380362, -508.74552859, -0.00062798, -623.64893263, -0.01855578, -62.36489326, -0.05380362, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13015, 150.58644173, 0.00107547, 184.5973446, 0.01569771, 18.45973446, 0.03743328, -150.58644173, -0.00107547, -184.5973446, -0.01569771, -18.45973446, -0.03743328, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23015, 3015, 0.0, 377.20387289, 0.01255951, 377.20387289, 0.03767853, 264.04271102, -4638.53408903, 0.05, 2, 0, 73015, 24015, 2, 3)
    ops.uniaxialMaterial('LimitState', 43015, 94.30096822, 9.287e-05, 282.90290467, 0.00027862, 943.00968222, 0.00092874, -94.30096822, -9.287e-05, -282.90290467, -0.00027862, -943.00968222, -0.00092874, 0.4, 0.3, 0.003, 0.0, 0.0, 23015, 2)
    ops.limitCurve('ThreePoint', 13015, 3015, 0.0, 174.70795132, 0.02150935, 174.70795132, 0.06452804, 122.29556592, -1175.04042163, 0.05, 2, 0, 73015, 24015, 1, 3)
    ops.uniaxialMaterial('LimitState', 33015, 43.67698783, 4.302e-05, 131.03096349, 0.00012905, 436.7698783, 0.00043016, -43.67698783, -4.302e-05, -131.03096349, -0.00012905, -436.7698783, -0.00043016, 0.4, 0.3, 0.003, 0.0, 0.0, 13015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3015, 99999, 'P', 43015, 'Vy', 33015, 'Vz', 23015, 'My', 13015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173015, 73015, 173015, 3015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124015, 124015, 24015, 3015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173016, 12.45, 15.45, 9.65)
    ops.node(124016, 12.45, 15.45, 12.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3016, 173016, 124016, 0.1625, 30497822.19991756, 12707425.91663232, 0.0025666, 0.00093099, 0.00629349, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23016, 179.77463193, 0.00067768, 218.1918405, 0.01833948, 21.81918405, 0.07390999, -179.77463193, -0.00067768, -218.1918405, -0.01833948, -21.81918405, -0.07390999, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13016, 55.7659762, 0.00142979, 67.68296981, 0.01495737, 6.76829698, 0.04447761, -55.7659762, -0.00142979, -67.68296981, -0.01495737, -6.76829698, -0.04447761, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23016, 3016, 0.0, 206.26956649, 0.01355356, 206.26956649, 0.04066068, 144.38869654, -4494.53198614, 0.05, 2, 0, 73016, 24016, 2, 3)
    ops.uniaxialMaterial('LimitState', 43016, 51.56739162, 8.541e-05, 154.70217487, 0.00025622, 515.67391622, 0.00085406, -51.56739162, -8.541e-05, -154.70217487, -0.00025622, -515.67391622, -0.00085406, 0.4, 0.3, 0.003, 0.0, 0.0, 23016, 2)
    ops.limitCurve('ThreePoint', 13016, 3016, 0.0, 97.1143827, 0.0285959, 97.1143827, 0.08578769, 67.98006789, -1010.94535827, 0.05, 2, 0, 73016, 24016, 1, 3)
    ops.uniaxialMaterial('LimitState', 33016, 24.27859567, 4.021e-05, 72.83578702, 0.00012063, 242.78595674, 0.0004021, -24.27859567, -4.021e-05, -72.83578702, -0.00012063, -242.78595674, -0.0004021, 0.4, 0.3, 0.003, 0.0, 0.0, 13016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3016, 99999, 'P', 43016, 'Vy', 33016, 'Vz', 23016, 'My', 13016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173016, 73016, 173016, 3016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124016, 124016, 24016, 3016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173017, 0.0, 20.6, 9.65)
    ops.node(124017, 0.0, 20.6, 12.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3017, 173017, 124017, 0.1, 30074904.86349335, 12531210.3597889, 0.00127345, 0.00057292, 0.00146667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23017, 56.70715628, 0.00077584, 68.91850908, 0.01833974, 6.89185091, 0.08258824, -56.70715628, -0.00077584, -68.91850908, -0.01833974, -6.89185091, -0.08258824, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13017, 30.22227646, 0.00113582, 36.73035947, 0.01625943, 3.67303595, 0.06131614, -30.22227646, -0.00113582, -36.73035947, -0.01625943, -3.67303595, -0.06131614, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23017, 3017, 0.0, 109.14517515, 0.01551689, 109.14517515, 0.04655067, 76.40162261, -4405.98406156, 0.05, 2, 0, 73017, 24017, 2, 3)
    ops.uniaxialMaterial('LimitState', 43017, 27.28629379, 7.447e-05, 81.85888137, 0.00022341, 272.86293788, 0.00074469, -27.28629379, -7.447e-05, -81.85888137, -0.00022341, -272.86293788, -0.00074469, 0.4, 0.3, 0.003, 0.0, 0.0, 23017, 2)
    ops.limitCurve('ThreePoint', 13017, 3017, 0.0, 81.72845609, 0.02271631, 81.72845609, 0.06814894, 57.20991926, -1954.9955275, 0.05, 2, 0, 73017, 24017, 1, 3)
    ops.uniaxialMaterial('LimitState', 33017, 20.43211402, 5.576e-05, 61.29634206, 0.00016729, 204.32114021, 0.00055763, -20.43211402, -5.576e-05, -61.29634206, -0.00016729, -204.32114021, -0.00055763, 0.4, 0.3, 0.003, 0.0, 0.0, 13017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3017, 99999, 'P', 43017, 'Vy', 33017, 'Vz', 23017, 'My', 13017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173017, 73017, 173017, 3017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124017, 124017, 24017, 3017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173018, 2.95, 20.6, 9.675)
    ops.node(124018, 2.95, 20.6, 12.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3018, 173018, 124018, 0.1875, 27992140.07958784, 11663391.69982827, 0.00308678, 0.00107422, 0.00966797, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23018, 216.1904352, 0.00063635, 264.03493856, 0.02434787, 26.40349386, 0.07875088, -216.1904352, -0.00063635, -264.03493856, -0.02434787, -26.40349386, -0.07875088, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13018, 62.87995158, 0.00136145, 76.79573862, 0.01895159, 7.67957386, 0.04574243, -62.87995158, -0.00136145, -76.79573862, -0.01895159, -7.67957386, -0.04574243, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23018, 3018, 0.0, 248.58459541, 0.01272703, 248.58459541, 0.03818108, 174.00921679, -5627.11082136, 0.05, 2, 0, 73018, 24018, 2, 3)
    ops.uniaxialMaterial('LimitState', 43018, 62.14614885, 9.719e-05, 186.43844656, 0.00029157, 621.46148852, 0.00097188, -62.14614885, -9.719e-05, -186.43844656, -0.00029157, -621.46148852, -0.00097188, 0.4, 0.3, 0.003, 0.0, 0.0, 23018, 2)
    ops.limitCurve('ThreePoint', 13018, 3018, 0.0, 103.35598255, 0.02722897, 103.35598255, 0.0816869, 72.34918778, -1049.84431701, 0.05, 2, 0, 73018, 24018, 1, 3)
    ops.uniaxialMaterial('LimitState', 33018, 25.83899564, 4.041e-05, 77.51698691, 0.00012123, 258.38995637, 0.00040409, -25.83899564, -4.041e-05, -77.51698691, -0.00012123, -258.38995637, -0.00040409, 0.4, 0.3, 0.003, 0.0, 0.0, 13018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3018, 99999, 'P', 43018, 'Vy', 33018, 'Vz', 23018, 'My', 13018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173018, 73018, 173018, 3018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124018, 124018, 24018, 3018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173019, 7.7, 20.6, 9.675)
    ops.node(124019, 7.7, 20.6, 12.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3019, 173019, 124019, 0.315, 28983819.67279368, 12076591.5303307, 0.00971719, 0.00353719, 0.02338875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23019, 519.94105264, 0.00060669, 633.77741559, 0.01731344, 63.37774156, 0.05313323, -519.94105264, -0.00060669, -633.77741559, -0.01731344, -63.37774156, -0.05313323, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13019, 155.31293989, 0.00099024, 189.31729502, 0.01461657, 18.9317295, 0.03670483, -155.31293989, -0.00099024, -189.31729502, -0.01461657, -18.9317295, -0.03670483, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23019, 3019, 0.0, 419.36613048, 0.01213383, 419.36613048, 0.0364015, 293.55629134, -4430.3471642, 0.05, 2, 0, 73019, 24019, 2, 3)
    ops.uniaxialMaterial('LimitState', 43019, 104.84153262, 9.426e-05, 314.52459786, 0.00028277, 1048.41532621, 0.00094255, -104.84153262, -9.426e-05, -314.52459786, -0.00028277, -1048.41532621, -0.00094255, 0.4, 0.3, 0.003, 0.0, 0.0, 23019, 2)
    ops.limitCurve('ThreePoint', 13019, 3019, 0.0, 192.3917353, 0.01980487, 192.3917353, 0.0594146, 134.67421471, -1134.18525968, 0.05, 2, 0, 73019, 24019, 1, 3)
    ops.uniaxialMaterial('LimitState', 33019, 48.09793383, 4.324e-05, 144.29380148, 0.00012972, 480.97933825, 0.00043241, -48.09793383, -4.324e-05, -144.29380148, -0.00012972, -480.97933825, -0.00043241, 0.4, 0.3, 0.003, 0.0, 0.0, 13019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3019, 99999, 'P', 43019, 'Vy', 33019, 'Vz', 23019, 'My', 13019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173019, 73019, 173019, 3019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124019, 124019, 24019, 3019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173020, 12.45, 20.6, 9.65)
    ops.node(124020, 12.45, 20.6, 12.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3020, 173020, 124020, 0.1625, 30008327.53956894, 12503469.80815372, 0.0025666, 0.00093099, 0.00629349, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23020, 178.2243553, 0.00063966, 216.61117646, 0.02137641, 21.66111765, 0.07681319, -178.2243553, -0.00063966, -216.61117646, -0.02137641, -21.66111765, -0.07681319, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13020, 55.5730054, 0.00122868, 67.54258731, 0.01711141, 6.75425873, 0.04656062, -55.5730054, -0.00122868, -67.54258731, -0.01711141, -6.75425873, -0.04656062, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23020, 3020, 0.0, 213.15049376, 0.01279325, 213.15049376, 0.03837974, 149.20534563, -5727.72152222, 0.05, 2, 0, 73020, 24020, 2, 3)
    ops.uniaxialMaterial('LimitState', 43020, 53.28762344, 8.97e-05, 159.86287032, 0.00026909, 532.87623441, 0.00089695, -53.28762344, -8.97e-05, -159.86287032, -0.00026909, -532.87623441, -0.00089695, 0.4, 0.3, 0.003, 0.0, 0.0, 23020, 2)
    ops.limitCurve('ThreePoint', 13020, 3020, 0.0, 108.64759645, 0.02457353, 108.64759645, 0.07372059, 76.05331751, -1233.31701667, 0.05, 2, 0, 73020, 24020, 1, 3)
    ops.uniaxialMaterial('LimitState', 33020, 27.16189911, 4.572e-05, 81.48569734, 0.00013716, 271.61899112, 0.0004572, -27.16189911, -4.572e-05, -81.48569734, -0.00013716, -271.61899112, -0.0004572, 0.4, 0.3, 0.003, 0.0, 0.0, 13020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3020, 99999, 'P', 43020, 'Vy', 33020, 'Vz', 23020, 'My', 13020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173020, 73020, 173020, 3020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124020, 124020, 24020, 3020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173021, 0.0, 25.75, 9.65)
    ops.node(124021, 0.0, 25.75, 12.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3021, 173021, 124021, 0.1, 30094446.48642823, 12539352.70267843, 0.00127345, 0.00057292, 0.00146667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23021, 60.37805461, 0.00080567, 73.37586668, 0.01997055, 7.33758667, 0.08422477, -60.37805461, -0.00080567, -73.37586668, -0.01997055, -7.33758667, -0.08422477, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13021, 32.12388997, 0.00117504, 39.0393212, 0.01767721, 3.90393212, 0.06273793, -32.12388997, -0.00117504, -39.0393212, -0.01767721, -3.90393212, -0.06273793, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23021, 3021, 0.0, 116.15416096, 0.01611334, 116.15416096, 0.04834003, 81.30791267, -5502.89375237, 0.05, 2, 0, 73021, 24021, 2, 3)
    ops.uniaxialMaterial('LimitState', 43021, 29.03854024, 7.92e-05, 87.11562072, 0.0002376, 290.38540239, 0.000792, -29.03854024, -7.92e-05, -87.11562072, -0.0002376, -290.38540239, -0.000792, 0.4, 0.3, 0.003, 0.0, 0.0, 23021, 2)
    ops.limitCurve('ThreePoint', 13021, 3021, 0.0, 93.80677221, 0.02350085, 93.80677221, 0.07050254, 65.66474055, -2410.10025759, 0.05, 2, 0, 73021, 24021, 1, 3)
    ops.uniaxialMaterial('LimitState', 33021, 23.45169305, 6.396e-05, 70.35507916, 0.00019189, 234.51693053, 0.00063962, -23.45169305, -6.396e-05, -70.35507916, -0.00019189, -234.51693053, -0.00063962, 0.4, 0.3, 0.003, 0.0, 0.0, 13021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3021, 99999, 'P', 43021, 'Vy', 33021, 'Vz', 23021, 'My', 13021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173021, 73021, 173021, 3021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124021, 124021, 24021, 3021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173022, 2.95, 25.75, 9.675)
    ops.node(124022, 2.95, 25.75, 12.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3022, 173022, 124022, 0.1875, 27721636.42604771, 11550681.84418655, 0.00308678, 0.00107422, 0.00966797, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23022, 225.29437731, 0.00065184, 275.31853276, 0.02542804, 27.53185328, 0.07971535, -225.29437731, -0.00065184, -275.31853276, -0.02542804, -27.53185328, -0.07971535, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13022, 66.38513902, 0.00137931, 81.12523397, 0.01975927, 8.1125234, 0.04649313, -66.38513902, -0.00137931, -81.12523397, -0.01975927, -8.1125234, -0.04649313, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23022, 3022, 0.0, 255.44068134, 0.01303679, 255.44068134, 0.03911037, 178.80847694, -6696.6747893, 0.05, 2, 0, 73022, 24022, 2, 3)
    ops.uniaxialMaterial('LimitState', 43022, 63.86017033, 0.00010084, 191.580511, 0.00030253, 638.60170334, 0.00100843, -63.86017033, -0.00010084, -191.580511, -0.00030253, -638.60170334, -0.00100843, 0.4, 0.3, 0.003, 0.0, 0.0, 23022, 2)
    ops.limitCurve('ThreePoint', 13022, 3022, 0.0, 110.5462548, 0.02758612, 110.5462548, 0.08275835, 77.38237836, -1202.31045327, 0.05, 2, 0, 73022, 24022, 1, 3)
    ops.uniaxialMaterial('LimitState', 33022, 27.6365637, 4.364e-05, 82.9096911, 0.00013092, 276.36563701, 0.00043642, -27.6365637, -4.364e-05, -82.9096911, -0.00013092, -276.36563701, -0.00043642, 0.4, 0.3, 0.003, 0.0, 0.0, 13022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3022, 99999, 'P', 43022, 'Vy', 33022, 'Vz', 23022, 'My', 13022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173022, 73022, 173022, 3022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124022, 124022, 24022, 3022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173023, 7.7, 25.75, 9.675)
    ops.node(124023, 7.7, 25.75, 12.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3023, 173023, 124023, 0.315, 31511334.20911921, 13129722.58713301, 0.00971719, 0.00353719, 0.02338875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23023, 508.95386748, 0.0006084, 615.9162073, 0.0177294, 61.59162073, 0.05394612, -508.95386748, -0.0006084, -615.9162073, -0.0177294, -61.59162073, -0.05394612, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13023, 151.76487023, 0.0010436, 183.6599528, 0.0150078, 18.36599528, 0.03734082, -151.76487023, -0.0010436, -183.6599528, -0.0150078, -18.36599528, -0.03734082, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23023, 3023, 0.0, 470.16783015, 0.01216804, 470.16783015, 0.03650411, 329.1174811, -4739.19925884, 0.05, 2, 0, 73023, 24023, 2, 3)
    ops.uniaxialMaterial('LimitState', 43023, 117.54195754, 9.72e-05, 352.62587261, 0.00029159, 1175.41957537, 0.00097197, -117.54195754, -9.72e-05, -352.62587261, -0.00029159, -1175.41957537, -0.00097197, 0.4, 0.3, 0.003, 0.0, 0.0, 23023, 2)
    ops.limitCurve('ThreePoint', 13023, 3023, 0.0, 224.90783986, 0.02087208, 224.90783986, 0.06261623, 157.4354879, -1194.71976197, 0.05, 2, 0, 73023, 24023, 1, 3)
    ops.uniaxialMaterial('LimitState', 33023, 56.22695996, 4.649e-05, 168.68087989, 0.00013948, 562.26959964, 0.00046495, -56.22695996, -4.649e-05, -168.68087989, -0.00013948, -562.26959964, -0.00046495, 0.4, 0.3, 0.003, 0.0, 0.0, 13023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3023, 99999, 'P', 43023, 'Vy', 33023, 'Vz', 23023, 'My', 13023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173023, 73023, 173023, 3023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124023, 124023, 24023, 3023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173024, 12.45, 25.75, 9.65)
    ops.node(124024, 12.45, 25.75, 12.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3024, 173024, 124024, 0.1625, 30731220.86119926, 12804675.35883303, 0.0025666, 0.00093099, 0.00629349, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23024, 175.0057521, 0.00064939, 212.25853793, 0.02269353, 21.22585379, 0.0783247, -175.0057521, -0.00064939, -212.25853793, -0.02269353, -21.22585379, -0.0783247, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13024, 54.26534868, 0.0013151, 65.81659992, 0.01819921, 6.58165999, 0.04775167, -54.26534868, -0.0013151, -65.81659992, -0.01819921, -6.58165999, -0.04775167, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23024, 3024, 0.0, 226.56761856, 0.01298781, 226.56761856, 0.03896343, 158.59733299, -6828.92857262, 0.05, 2, 0, 73024, 24024, 2, 3)
    ops.uniaxialMaterial('LimitState', 43024, 56.64190464, 9.31e-05, 169.92571392, 0.0002793, 566.41904639, 0.00093098, -56.64190464, -9.31e-05, -169.92571392, -0.0002793, -566.41904639, -0.00093098, 0.4, 0.3, 0.003, 0.0, 0.0, 23024, 2)
    ops.limitCurve('ThreePoint', 13024, 3024, 0.0, 122.9798311, 0.02630208, 122.9798311, 0.07890624, 86.08588177, -1428.37523866, 0.05, 2, 0, 73024, 24024, 1, 3)
    ops.uniaxialMaterial('LimitState', 33024, 30.74495778, 5.053e-05, 92.23487333, 0.0001516, 307.44957776, 0.00050533, -30.74495778, -5.053e-05, -92.23487333, -0.0001516, -307.44957776, -0.00050533, 0.4, 0.3, 0.003, 0.0, 0.0, 13024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3024, 99999, 'P', 43024, 'Vy', 33024, 'Vz', 23024, 'My', 13024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173024, 73024, 173024, 3024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124024, 124024, 24024, 3024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173025, 0.0, 30.9, 9.65)
    ops.node(124025, 0.0, 30.9, 12.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3025, 173025, 124025, 0.0625, 27464014.03053401, 11443339.17938917, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23025, 22.80024752, 0.00121858, 27.89966469, 0.02047726, 2.78996647, 0.08440979, -22.80024752, -0.00121858, -27.89966469, -0.02047726, -2.78996647, -0.08440979, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13025, 22.80024752, 0.00121858, 27.89966469, 0.02047726, 2.78996647, 0.08440979, -22.80024752, -0.00121858, -27.89966469, -0.02047726, -2.78996647, -0.08440979, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23025, 3025, 0.0, 66.20639447, 0.02437163, 66.20639447, 0.07311489, 46.34447613, -3970.81774887, 0.05, 2, 0, 73025, 24025, 2, 3)
    ops.uniaxialMaterial('LimitState', 43025, 16.55159862, 7.915e-05, 49.65479586, 0.00023744, 165.51598618, 0.00079147, -16.55159862, -7.915e-05, -49.65479586, -0.00023744, -165.51598618, -0.00079147, 0.4, 0.3, 0.003, 0.0, 0.0, 23025, 2)
    ops.limitCurve('ThreePoint', 13025, 3025, 0.0, 66.20639447, 0.02437163, 66.20639447, 0.07311489, 46.34447613, -3970.81774887, 0.05, 2, 0, 73025, 24025, 1, 3)
    ops.uniaxialMaterial('LimitState', 33025, 16.55159862, 7.915e-05, 49.65479586, 0.00023744, 165.51598618, 0.00079147, -16.55159862, -7.915e-05, -49.65479586, -0.00023744, -165.51598618, -0.00079147, 0.4, 0.3, 0.003, 0.0, 0.0, 13025, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3025, 99999, 'P', 43025, 'Vy', 33025, 'Vz', 23025, 'My', 13025, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173025, 73025, 173025, 3025, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124025, 124025, 24025, 3025, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173026, 2.95, 30.9, 9.675)
    ops.node(124026, 2.95, 30.9, 12.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3026, 173026, 124026, 0.175, 31394325.75117134, 13080969.06298806, 0.00405757, 0.00401042, 0.0019651, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23026, 82.66358887, 0.00092219, 100.09379274, 0.01959295, 10.00937927, 0.05877098, -82.66358887, -0.00092219, -100.09379274, -0.01959295, -10.00937927, -0.05877098, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13026, 137.42998936, 0.00072957, 166.40807712, 0.02146354, 16.64080771, 0.07170022, -137.42998936, -0.00072957, -166.40807712, -0.02146354, -16.64080771, -0.07170022, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23026, 3026, 0.0, 153.61764085, 0.01844383, 153.61764085, 0.0553315, 107.5323486, -3017.69080939, 0.05, 2, 0, 73026, 24026, 2, 3)
    ops.uniaxialMaterial('LimitState', 43026, 38.40441021, 5.738e-05, 115.21323064, 0.00017213, 384.04410213, 0.00057376, -38.40441021, -5.738e-05, -115.21323064, -0.00017213, -384.04410213, -0.00057376, 0.4, 0.3, 0.003, 0.0, 0.0, 23026, 2)
    ops.limitCurve('ThreePoint', 13026, 3026, 0.0, 187.43769561, 0.01459141, 187.43769561, 0.04377424, 131.20638693, -5591.6602792, 0.05, 2, 0, 73026, 24026, 1, 3)
    ops.uniaxialMaterial('LimitState', 33026, 46.8594239, 7.001e-05, 140.57827171, 0.00021002, 468.59423903, 0.00070008, -46.8594239, -7.001e-05, -140.57827171, -0.00021002, -468.59423903, -0.00070008, 0.4, 0.3, 0.003, 0.0, 0.0, 13026, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3026, 99999, 'P', 43026, 'Vy', 33026, 'Vz', 23026, 'My', 13026, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173026, 73026, 173026, 3026, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124026, 124026, 24026, 3026, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173027, 7.7, 30.9, 9.675)
    ops.node(124027, 7.7, 30.9, 12.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3027, 173027, 124027, 0.24, 30556854.34638626, 12732022.64432761, 0.00751249, 0.00792, 0.00352, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23027, 144.59482166, 0.00090882, 175.54271485, 0.02724269, 17.55427148, 0.06744455, -144.59482166, -0.00090882, -175.54271485, -0.02724269, -17.55427148, -0.06744455, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13027, 254.90631303, 0.0007082, 309.46437575, 0.03044575, 30.94643758, 0.08408343, -254.90631303, -0.0007082, -309.46437575, -0.03044575, -30.94643758, -0.08408343, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23027, 3027, 0.0, 206.32788283, 0.01817637, 206.32788283, 0.05452912, 144.42951798, -4499.52495053, 0.05, 2, 0, 73027, 24027, 2, 3)
    ops.uniaxialMaterial('LimitState', 43027, 51.58197071, 5.773e-05, 154.74591212, 0.0001732, 515.81970707, 0.00057732, -51.58197071, -5.773e-05, -154.74591212, -0.0001732, -515.81970707, -0.00057732, 0.4, 0.3, 0.003, 0.0, 0.0, 23027, 2)
    ops.limitCurve('ThreePoint', 13027, 3027, 0.0, 288.54285412, 0.01416405, 288.54285412, 0.04249214, 201.97999789, -9155.6412559, 0.05, 2, 0, 73027, 24027, 1, 3)
    ops.uniaxialMaterial('LimitState', 33027, 72.13571353, 8.074e-05, 216.40714059, 0.00024221, 721.3571353, 0.00080736, -72.13571353, -8.074e-05, -216.40714059, -0.00024221, -721.3571353, -0.00080736, 0.4, 0.3, 0.003, 0.0, 0.0, 13027, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3027, 99999, 'P', 43027, 'Vy', 33027, 'Vz', 23027, 'My', 13027, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173027, 73027, 173027, 3027, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124027, 124027, 24027, 3027, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173028, 12.45, 30.9, 9.65)
    ops.node(124028, 12.45, 30.9, 12.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3028, 173028, 124028, 0.0875, 30862593.77642816, 12859414.07351173, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23028, 31.89159158, 0.00115592, 38.66789428, 0.01725725, 3.86678943, 0.06694438, -31.89159158, -0.00115592, -38.66789428, -0.01725725, -3.86678943, -0.06694438, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13028, 51.85867114, 0.00087639, 62.87756472, 0.01883146, 6.28775647, 0.08317498, -51.85867114, -0.00087639, -62.87756472, -0.01883146, -6.28775647, -0.08317498, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23028, 3028, 0.0, 85.61377702, 0.02311849, 85.61377702, 0.06935548, 59.92964391, -2478.41427614, 0.05, 2, 0, 73028, 24028, 2, 3)
    ops.uniaxialMaterial('LimitState', 43028, 21.40344426, 6.505e-05, 64.21033277, 0.00019516, 214.03444255, 0.00065055, -21.40344426, -6.505e-05, -64.21033277, -0.00019516, -214.03444255, -0.00065055, 0.4, 0.3, 0.003, 0.0, 0.0, 23028, 2)
    ops.limitCurve('ThreePoint', 13028, 3028, 0.0, 102.82017188, 0.01752774, 102.82017188, 0.05258323, 71.97412032, -4476.35172502, 0.05, 2, 0, 73028, 24028, 1, 3)
    ops.uniaxialMaterial('LimitState', 33028, 25.70504297, 7.813e-05, 77.11512891, 0.00023439, 257.0504297, 0.0007813, -25.70504297, -7.813e-05, -77.11512891, -0.00023439, -257.0504297, -0.0007813, 0.4, 0.3, 0.003, 0.0, 0.0, 13028, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3028, 99999, 'P', 43028, 'Vy', 33028, 'Vz', 23028, 'My', 13028, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173028, 73028, 173028, 3028, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124028, 124028, 24028, 3028, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170001, 0.0, 0.0, 0.0)
    ops.node(124029, 0.0, 0.0, 1.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4074, 170001, 124029, 0.075, 29544038.93459187, 12310016.22274661, 0.00077515, 0.00042969, 0.00061875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24074, 58.076094, 0.00093007, 70.12877019, 0.0181433, 7.01287702, 0.06878049, -58.076094, -0.00093007, -70.12877019, -0.0181433, -7.01287702, -0.06878049, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14074, 43.72353848, 0.00107916, 52.79759313, 0.01728718, 5.27975931, 0.06118889, -43.72353848, -0.00107916, -52.79759313, -0.01728718, -5.27975931, -0.06118889, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24074, 4074, 0.0, 98.26088494, 0.01860144, 98.26088494, 0.05580433, 68.78261946, -2271.60286696, 0.05, 2, 0, 70001, 24029, 2, 3)
    ops.uniaxialMaterial('LimitState', 44074, 24.56522124, 5.907e-05, 73.69566371, 0.0001772, 245.65221235, 0.00059068, -24.56522124, -5.907e-05, -73.69566371, -0.0001772, -245.65221235, -0.00059068, 0.4, 0.3, 0.003, 0.0, 0.0, 24074, 2)
    ops.limitCurve('ThreePoint', 14074, 4074, 0.0, 88.97277791, 0.02158316, 88.97277791, 0.06474948, 62.28094453, -1850.42228637, 0.05, 2, 0, 70001, 24029, 1, 3)
    ops.uniaxialMaterial('LimitState', 34074, 22.24319448, 5.348e-05, 66.72958343, 0.00016045, 222.43194477, 0.00053485, -22.24319448, -5.348e-05, -66.72958343, -0.00016045, -222.43194477, -0.00053485, 0.4, 0.3, 0.003, 0.0, 0.0, 14074, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4074, 99999, 'P', 44074, 'Vy', 34074, 'Vz', 24074, 'My', 14074, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170001, 70001, 170001, 4074, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124029, 124029, 24029, 4074, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174029, 0.0, 0.0, 2.1)
    ops.node(121001, 0.0, 0.0, 3.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4075, 174029, 121001, 0.075, 28027554.32497219, 11678147.63540508, 0.00077515, 0.00042969, 0.00061875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24075, 64.81162736, 0.00088178, 78.59272022, 0.02892778, 7.85927202, 0.08998365, -64.81162736, -0.00088178, -78.59272022, -0.02892778, -7.85927202, -0.08998365, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14075, 45.22542197, 0.0010156, 54.84184057, 0.02734645, 5.48418406, 0.079914, -45.22542197, -0.0010156, -54.84184057, -0.02734645, -5.48418406, -0.079914, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24075, 4075, 0.0, 113.26828961, 0.01763554, 113.26828961, 0.05290662, 79.28780273, -3990.42906916, 0.05, 2, 0, 74029, 21001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44075, 28.3170724, 7.177e-05, 84.95121721, 0.00021532, 283.17072403, 0.00071774, -28.3170724, -7.177e-05, -84.95121721, -0.00021532, -283.17072403, -0.00071774, 0.4, 0.3, 0.003, 0.0, 0.0, 24075, 2)
    ops.limitCurve('ThreePoint', 14075, 4075, 0.0, 100.73494712, 0.02031208, 100.73494712, 0.06093623, 70.51446299, -3095.55344094, 0.05, 2, 0, 74029, 21001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34075, 25.18373678, 6.383e-05, 75.55121034, 0.0001915, 251.83736781, 0.00063832, -25.18373678, -6.383e-05, -75.55121034, -0.0001915, -251.83736781, -0.00063832, 0.4, 0.3, 0.003, 0.0, 0.0, 14075, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4075, 99999, 'P', 44075, 'Vy', 34075, 'Vz', 24075, 'My', 14075, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174029, 74029, 174029, 4075, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121001, 121001, 21001, 4075, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170002, 2.95, 0.0, 0.0)
    ops.node(124030, 2.95, 0.0, 1.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4076, 170002, 124030, 0.27, 31913744.87390431, 13297393.69746013, 0.00984074, 0.00891, 0.00501188, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24076, 424.20260613, 0.00070741, 510.82693055, 0.05036753, 51.08269305, 0.13473507, -424.20260613, -0.00070741, -510.82693055, -0.05036753, -51.08269305, -0.13473507, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14076, 407.25164396, 0.00063881, 490.41449589, 0.0482257, 49.04144959, 0.1244763, -407.25164396, -0.00063881, -490.41449589, -0.0482257, -49.04144959, -0.1244763, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24076, 4076, 0.0, 487.86704013, 0.01414823, 487.86704013, 0.0424447, 341.50692809, -11685.87773814, 0.05, 2, 0, 70002, 24030, 2, 3)
    ops.uniaxialMaterial('LimitState', 44076, 121.96676003, 7.542e-05, 365.9002801, 0.00022625, 1219.66760033, 0.00075416, -121.96676003, -7.542e-05, -365.9002801, -0.00022625, -1219.66760033, -0.00075416, 0.4, 0.3, 0.003, 0.0, 0.0, 24076, 2)
    ops.limitCurve('ThreePoint', 14076, 4076, 0.0, 760.90062727, 0.01277622, 760.90062727, 0.03832865, 532.63043909, -34535.74649858, 0.05, 2, 0, 70002, 24030, 1, 3)
    ops.uniaxialMaterial('LimitState', 34076, 190.22515682, 0.00011762, 570.67547045, 0.00035287, 1902.25156818, 0.00117623, -190.22515682, -0.00011762, -570.67547045, -0.00035287, -1902.25156818, -0.00117623, 0.4, 0.3, 0.003, 0.0, 0.0, 14076, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4076, 99999, 'P', 44076, 'Vy', 34076, 'Vz', 24076, 'My', 14076, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170002, 70002, 170002, 4076, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124030, 124030, 24030, 4076, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174030, 2.95, 0.0, 2.1)
    ops.node(121002, 2.95, 0.0, 3.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4077, 174030, 121002, 0.27, 29764747.63168217, 12401978.17986757, 0.00984074, 0.00891, 0.00501188, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24077, 247.13064535, 0.00073968, 299.38815272, 0.04842131, 29.93881527, 0.13091543, -247.13064535, -0.00073968, -299.38815272, -0.04842131, -29.93881527, -0.13091543, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14077, 277.39135382, 0.00066021, 336.04770013, 0.04635121, 33.60477001, 0.12090862, -277.39135382, -0.00066021, -336.04770013, -0.04635121, -33.60477001, -0.12090862, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24077, 4077, 0.0, 463.00394171, 0.01479368, 463.00394171, 0.04438104, 324.1027592, -12792.74102555, 0.05, 2, 0, 74030, 21002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44077, 115.75098543, 7.674e-05, 347.25295628, 0.00023022, 1157.50985427, 0.0007674, -115.75098543, -7.674e-05, -347.25295628, -0.00023022, -1157.50985427, -0.0007674, 0.4, 0.3, 0.003, 0.0, 0.0, 24077, 2)
    ops.limitCurve('ThreePoint', 14077, 4077, 0.0, 733.75392875, 0.01320421, 733.75392875, 0.03961264, 513.62775013, -38850.29888683, 0.05, 2, 0, 74030, 21002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34077, 183.43848219, 0.00012162, 550.31544657, 0.00036485, 1834.38482188, 0.00121615, -183.43848219, -0.00012162, -550.31544657, -0.00036485, -1834.38482188, -0.00121615, 0.4, 0.3, 0.003, 0.0, 0.0, 14077, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4077, 99999, 'P', 44077, 'Vy', 34077, 'Vz', 24077, 'My', 14077, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174030, 74030, 174030, 4077, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121002, 121002, 21002, 4077, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171001, 0.0, 0.0, 3.95)
    ops.node(124031, 0.0, 0.0, 4.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4079, 171001, 124031, 0.075, 28663377.06654114, 11943073.77772548, 0.00077515, 0.00042969, 0.00061875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24079, 64.54774958, 0.00083807, 78.26221879, 0.03476489, 7.82622188, 0.1164528, -64.54774958, -0.00083807, -78.26221879, -0.03476489, -7.82622188, -0.1164528, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14079, 45.11074194, 0.00095479, 54.69542748, 0.03270396, 5.46954275, 0.10249768, -45.11074194, -0.00095479, -54.69542748, -0.03270396, -5.46954275, -0.10249768, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24079, 4079, 0.0, 138.61182209, 0.01676149, 138.61182209, 0.05028448, 97.02827547, -6777.24085511, 0.05, 2, 0, 71001, 24031, 2, 3)
    ops.uniaxialMaterial('LimitState', 44079, 34.65295552, 6.615e-05, 103.95886657, 0.00019846, 346.52955524, 0.00066154, -34.65295552, -6.615e-05, -103.95886657, -0.00019846, -346.52955524, -0.00066154, 0.4, 0.3, 0.003, 0.0, 0.0, 24079, 2)
    ops.limitCurve('ThreePoint', 14079, 4079, 0.0, 115.50985175, 0.01909573, 115.50985175, 0.05728719, 80.85689622, -5161.60910497, 0.05, 2, 0, 71001, 24031, 1, 3)
    ops.uniaxialMaterial('LimitState', 34079, 28.87746294, 5.513e-05, 86.63238881, 0.00016539, 288.77462936, 0.00055129, -28.87746294, -5.513e-05, -86.63238881, -0.00016539, -288.77462936, -0.00055129, 0.4, 0.3, 0.003, 0.0, 0.0, 14079, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4079, 99999, 'P', 44079, 'Vy', 34079, 'Vz', 24079, 'My', 14079, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171001, 71001, 171001, 4079, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124031, 124031, 24031, 4079, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174031, 0.0, 0.0, 5.375)
    ops.node(122001, 0.0, 0.0, 6.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4080, 174031, 122001, 0.075, 28259953.11707816, 11774980.46544923, 0.00077515, 0.00042969, 0.00061875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24080, 48.37565539, 0.00083035, 58.80326838, 0.03757367, 5.88032684, 0.12297076, -48.37565539, -0.00083035, -58.80326838, -0.03757367, -5.88032684, -0.12297076, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14080, 36.03033075, 0.00094903, 43.79684764, 0.03533392, 4.37968476, 0.10829675, -36.03033075, -0.00094903, -43.79684764, -0.03533392, -4.37968476, -0.10829675, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24080, 4080, 0.0, 137.84319036, 0.01660708, 137.84319036, 0.04982123, 96.49023325, -8460.60854593, 0.05, 2, 0, 74031, 22001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44080, 34.46079759, 6.673e-05, 103.38239277, 0.00020018, 344.6079759, 0.00066727, -34.46079759, -6.673e-05, -103.38239277, -0.00020018, -344.6079759, -0.00066727, 0.4, 0.3, 0.003, 0.0, 0.0, 24080, 2)
    ops.limitCurve('ThreePoint', 14080, 4080, 0.0, 114.8693253, 0.01898063, 114.8693253, 0.05694188, 80.40852771, -6319.31612277, 0.05, 2, 0, 74031, 22001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34080, 28.71733132, 5.561e-05, 86.15199397, 0.00016682, 287.17331325, 0.00055606, -28.71733132, -5.561e-05, -86.15199397, -0.00016682, -287.17331325, -0.00055606, 0.4, 0.3, 0.003, 0.0, 0.0, 14080, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4080, 99999, 'P', 44080, 'Vy', 34080, 'Vz', 24080, 'My', 14080, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174031, 74031, 174031, 4080, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122001, 122001, 22001, 4080, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171002, 2.95, 0.0, 3.975)
    ops.node(124032, 2.95, 0.0, 4.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4081, 171002, 124032, 0.27, 31857286.53821601, 13273869.39092334, 0.00984074, 0.00891, 0.00501188, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24081, 192.62464538, 0.00067981, 232.29852378, 0.04068109, 23.22985238, 0.10306523, -192.62464538, -0.00067981, -232.29852378, -0.04068109, -23.22985238, -0.10306523, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14081, 319.4367611, 0.00063502, 385.2294596, 0.04486778, 38.52294596, 0.12405657, -319.4367611, -0.00063502, -385.2294596, -0.04486778, -38.52294596, -0.12405657, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24081, 4081, 0.0, 544.85039802, 0.01359618, 544.85039802, 0.04078854, 381.39527861, -16302.7919716, 0.05, 2, 0, 71002, 24032, 2, 3)
    ops.uniaxialMaterial('LimitState', 44081, 136.2125995, 6.499e-05, 408.63779851, 0.00019497, 1362.12599504, 0.00064991, -136.2125995, -6.499e-05, -408.63779851, -0.00019497, -1362.12599504, -0.00064991, 0.4, 0.3, 0.003, 0.0, 0.0, 24081, 2)
    ops.limitCurve('ThreePoint', 14081, 4081, 0.0, 603.94972501, 0.0127005, 603.94972501, 0.0381015, 422.7648075, -25729.69728606, 0.05, 2, 0, 71002, 24032, 1, 3)
    ops.uniaxialMaterial('LimitState', 34081, 150.98743125, 7.204e-05, 452.96229375, 0.00021612, 1509.87431251, 0.0007204, -150.98743125, -7.204e-05, -452.96229375, -0.00021612, -1509.87431251, -0.0007204, 0.4, 0.3, 0.003, 0.0, 0.0, 14081, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4081, 99999, 'P', 44081, 'Vy', 34081, 'Vz', 24081, 'My', 14081, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171002, 71002, 171002, 4081, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124032, 124032, 24032, 4081, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174032, 2.95, 0.0, 5.375)
    ops.node(122002, 2.95, 0.0, 6.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4082, 174032, 122002, 0.27, 28997101.49415643, 12082125.62256518, 0.00984074, 0.00891, 0.00501188, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24082, 184.05113722, 0.00069927, 223.73145056, 0.04359916, 22.37314506, 0.10457252, -184.05113722, -0.00069927, -223.73145056, -0.04359916, -22.37314506, -0.10457252, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14082, 307.17529138, 0.00064855, 373.40042857, 0.04808654, 37.34004286, 0.12548452, -307.17529138, -0.00064855, -373.40042857, -0.04808654, -37.34004286, -0.12548452, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24082, 4082, 0.0, 495.23453225, 0.01398536, 495.23453225, 0.04195608, 346.66417257, -17667.99731765, 0.05, 2, 0, 74032, 22002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44082, 123.80863306, 6.49e-05, 371.42589918, 0.0001947, 1238.08633061, 0.00064899, -123.80863306, -6.49e-05, -371.42589918, -0.0001947, -1238.08633061, -0.00064899, 0.4, 0.3, 0.003, 0.0, 0.0, 24082, 2)
    ops.limitCurve('ThreePoint', 14082, 4082, 0.0, 554.97777055, 0.01297098, 554.97777055, 0.03891295, 388.48443939, -28201.41183226, 0.05, 2, 0, 74032, 22002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34082, 138.74444264, 7.273e-05, 416.23332792, 0.00021819, 1387.44442639, 0.00072728, -138.74444264, -7.273e-05, -416.23332792, -0.00021819, -1387.44442639, -0.00072728, 0.4, 0.3, 0.003, 0.0, 0.0, 14082, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4082, 99999, 'P', 44082, 'Vy', 34082, 'Vz', 24082, 'My', 14082, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174032, 74032, 174032, 4082, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122002, 122002, 22002, 4082, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172001, 0.0, 0.0, 6.8)
    ops.node(124033, 0.0, 0.0, 7.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4084, 172001, 124033, 0.0625, 29529951.88257354, 12304146.61773898, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24084, 39.98193532, 0.00095632, 48.46476898, 0.02777809, 4.8464769, 0.09582047, -39.98193532, -0.00095632, -48.46476898, -0.02777809, -4.8464769, -0.09582047, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14084, 36.31927393, 0.00095632, 44.02501296, 0.02777809, 4.4025013, 0.09582047, -36.31927393, -0.00095632, -44.02501296, -0.02777809, -4.4025013, -0.09582047, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24084, 4084, 0.0, 95.31103385, 0.01912646, 95.31103385, 0.05737939, 66.7177237, -4677.27718831, 0.05, 2, 0, 72001, 24033, 2, 3)
    ops.uniaxialMaterial('LimitState', 44084, 23.82775846, 5.298e-05, 71.48327539, 0.00015895, 238.27758463, 0.00052984, -23.82775846, -5.298e-05, -71.48327539, -0.00015895, -238.27758463, -0.00052984, 0.4, 0.3, 0.003, 0.0, 0.0, 24084, 2)
    ops.limitCurve('ThreePoint', 14084, 4084, 0.0, 95.31103385, 0.01912646, 95.31103385, 0.05737939, 66.7177237, -4677.27718831, 0.05, 2, 0, 72001, 24033, 1, 3)
    ops.uniaxialMaterial('LimitState', 34084, 23.82775846, 5.298e-05, 71.48327539, 0.00015895, 238.27758463, 0.00052984, -23.82775846, -5.298e-05, -71.48327539, -0.00015895, -238.27758463, -0.00052984, 0.4, 0.3, 0.003, 0.0, 0.0, 14084, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4084, 99999, 'P', 44084, 'Vy', 34084, 'Vz', 24084, 'My', 14084, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172001, 72001, 172001, 4084, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124033, 124033, 24033, 4084, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174033, 0.0, 0.0, 8.175)
    ops.node(123001, 0.0, 0.0, 9.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4085, 174033, 123001, 0.0625, 29840476.87872986, 12433532.03280411, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24085, 25.53100236, 0.00088995, 30.99136149, 0.02075885, 3.09913615, 0.08147353, -25.53100236, -0.00088995, -30.99136149, -0.02075885, -3.09913615, -0.08147353, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14085, 25.53100236, 0.00088995, 30.99136149, 0.02075885, 3.09913615, 0.08147353, -25.53100236, -0.00088995, -30.99136149, -0.02075885, -3.09913615, -0.08147353, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24085, 4085, 0.0, 81.01817719, 0.01779898, 81.01817719, 0.05339695, 56.71272403, -4083.96531306, 0.05, 2, 0, 74033, 23001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44085, 20.2545443, 4.457e-05, 60.76363289, 0.00013371, 202.54544296, 0.0004457, -20.2545443, -4.457e-05, -60.76363289, -0.00013371, -202.54544296, -0.0004457, 0.4, 0.3, 0.003, 0.0, 0.0, 24085, 2)
    ops.limitCurve('ThreePoint', 14085, 4085, 0.0, 81.01817719, 0.01779898, 81.01817719, 0.05339695, 56.71272403, -4083.96531306, 0.05, 2, 0, 74033, 23001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34085, 20.2545443, 4.457e-05, 60.76363289, 0.00013371, 202.54544296, 0.0004457, -20.2545443, -4.457e-05, -60.76363289, -0.00013371, -202.54544296, -0.0004457, 0.4, 0.3, 0.003, 0.0, 0.0, 14085, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4085, 99999, 'P', 44085, 'Vy', 34085, 'Vz', 24085, 'My', 14085, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174033, 74033, 174033, 4085, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123001, 123001, 23001, 4085, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172002, 2.95, 0.0, 6.825)
    ops.node(124034, 2.95, 0.0, 7.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4086, 172002, 124034, 0.175, 31053670.81572603, 12939029.50655251, 0.00405757, 0.00401042, 0.0019651, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24086, 99.68304188, 0.00077818, 120.50252235, 0.04292612, 12.05025224, 0.1148466, -99.68304188, -0.00077818, -120.50252235, -0.04292612, -12.05025224, -0.1148466, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14086, 162.301957, 0.00067117, 196.19982328, 0.04863969, 19.61998233, 0.14638964, -162.301957, -0.00067117, -196.19982328, -0.04863969, -19.61998233, -0.14638964, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24086, 4086, 0.0, 309.25593454, 0.0155636, 309.25593454, 0.0466908, 216.47915418, -12796.82250725, 0.05, 2, 0, 72002, 24034, 2, 3)
    ops.uniaxialMaterial('LimitState', 44086, 77.31398364, 5.839e-05, 231.94195091, 0.00017516, 773.13983636, 0.00058387, -77.31398364, -5.839e-05, -231.94195091, -0.00017516, -773.13983636, -0.00058387, 0.4, 0.3, 0.003, 0.0, 0.0, 24086, 2)
    ops.limitCurve('ThreePoint', 14086, 4086, 0.0, 413.6588477, 0.01342343, 413.6588477, 0.0402703, 289.56119339, -22952.21453288, 0.05, 2, 0, 72002, 24034, 1, 3)
    ops.uniaxialMaterial('LimitState', 34086, 103.41471193, 7.81e-05, 310.24413578, 0.00023429, 1034.14711926, 0.00078098, -103.41471193, -7.81e-05, -310.24413578, -0.00023429, -1034.14711926, -0.00078098, 0.4, 0.3, 0.003, 0.0, 0.0, 14086, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4086, 99999, 'P', 44086, 'Vy', 34086, 'Vz', 24086, 'My', 14086, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172002, 72002, 172002, 4086, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124034, 124034, 24034, 4086, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174034, 2.95, 0.0, 8.175)
    ops.node(123002, 2.95, 0.0, 9.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4087, 174034, 123002, 0.175, 29911446.83995828, 12463102.84998262, 0.00405757, 0.00401042, 0.0019651, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24087, 102.73603262, 0.00077811, 124.6627202, 0.04288814, 12.46627202, 0.1154112, -102.73603262, -0.00077811, -124.6627202, -0.04288814, -12.46627202, -0.1154112, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14087, 137.37339062, 0.00066981, 166.69264055, 0.04859519, 16.66926406, 0.14716413, -137.37339062, -0.00066981, -166.69264055, -0.04859519, -16.66926406, -0.14716413, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24087, 4087, 0.0, 285.83125008, 0.01556212, 285.83125008, 0.04668636, 200.08187505, -12787.63425418, 0.05, 2, 0, 74034, 23002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44087, 71.45781252, 5.602e-05, 214.37343756, 0.00016807, 714.57812519, 0.00056025, -71.45781252, -5.602e-05, -214.37343756, -0.00016807, -714.57812519, -0.00056025, 0.4, 0.3, 0.003, 0.0, 0.0, 24087, 2)
    ops.limitCurve('ThreePoint', 14087, 4087, 0.0, 382.36028888, 0.01339624, 382.36028888, 0.04018873, 267.65220221, -23231.31210866, 0.05, 2, 0, 74034, 23002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34087, 95.59007222, 7.495e-05, 286.77021666, 0.00022484, 955.90072219, 0.00074945, -95.59007222, -7.495e-05, -286.77021666, -0.00022484, -955.90072219, -0.00074945, 0.4, 0.3, 0.003, 0.0, 0.0, 14087, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4087, 99999, 'P', 44087, 'Vy', 34087, 'Vz', 24087, 'My', 14087, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174034, 74034, 174034, 4087, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123002, 123002, 23002, 4087, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173001, 0.0, 0.0, 9.65)
    ops.node(124035, 0.0, 0.0, 10.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4089, 173001, 124035, 0.0625, 27762106.93672669, 11567544.55696946, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24089, 26.30805876, 0.00089867, 32.1225268, 0.02263427, 3.21225268, 0.08388572, -26.30805876, -0.00089867, -32.1225268, -0.02263427, -3.21225268, -0.08388572, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14089, 26.30805876, 0.00089867, 32.1225268, 0.02263427, 3.21225268, 0.08388572, -26.30805876, -0.00089867, -32.1225268, -0.02263427, -3.21225268, -0.08388572, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24089, 4089, 0.0, 79.42013134, 0.01797334, 79.42013134, 0.05392001, 55.59409194, -6025.1885467, 0.05, 2, 0, 73001, 24035, 2, 3)
    ops.uniaxialMaterial('LimitState', 44089, 19.85503283, 4.696e-05, 59.5650985, 0.00014089, 198.55032835, 0.00046962, -19.85503283, -4.696e-05, -59.5650985, -0.00014089, -198.55032835, -0.00046962, 0.4, 0.3, 0.003, 0.0, 0.0, 24089, 2)
    ops.limitCurve('ThreePoint', 14089, 4089, 0.0, 79.42013134, 0.01797334, 79.42013134, 0.05392001, 55.59409194, -6025.1885467, 0.05, 2, 0, 73001, 24035, 1, 3)
    ops.uniaxialMaterial('LimitState', 34089, 19.85503283, 4.696e-05, 59.5650985, 0.00014089, 198.55032835, 0.00046962, -19.85503283, -4.696e-05, -59.5650985, -0.00014089, -198.55032835, -0.00046962, 0.4, 0.3, 0.003, 0.0, 0.0, 14089, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4089, 99999, 'P', 44089, 'Vy', 34089, 'Vz', 24089, 'My', 14089, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173001, 73001, 173001, 4089, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124035, 124035, 24035, 4089, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174035, 0.0, 0.0, 11.025)
    ops.node(124001, 0.0, 0.0, 12.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4090, 174035, 124001, 0.0625, 29760943.88531344, 12400393.28554727, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24090, 20.23573433, 0.00092073, 24.64347777, 0.02218244, 2.46434778, 0.08860944, -20.23573433, -0.00092073, -24.64347777, -0.02218244, -2.46434778, -0.08860944, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14090, 20.23573433, 0.00092073, 24.64347777, 0.02218244, 2.46434778, 0.08860944, -20.23573433, -0.00092073, -24.64347777, -0.02218244, -2.46434778, -0.08860944, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24090, 4090, 0.0, 77.07062342, 0.01841461, 77.07062342, 0.05524382, 53.94943639, -36589.16711973, 0.05, 2, 0, 74035, 24001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44090, 19.26765585, 4.251e-05, 57.80296756, 0.00012754, 192.67655854, 0.00042512, -19.26765585, -4.251e-05, -57.80296756, -0.00012754, -192.67655854, -0.00042512, 0.4, 0.3, 0.003, 0.0, 0.0, 24090, 2)
    ops.limitCurve('ThreePoint', 14090, 4090, 0.0, 77.07062342, 0.01841461, 77.07062342, 0.05524382, 53.94943639, -36589.16711973, 0.05, 2, 0, 74035, 24001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34090, 19.26765585, 4.251e-05, 57.80296756, 0.00012754, 192.67655854, 0.00042512, -19.26765585, -4.251e-05, -57.80296756, -0.00012754, -192.67655854, -0.00042512, 0.4, 0.3, 0.003, 0.0, 0.0, 14090, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4090, 99999, 'P', 44090, 'Vy', 34090, 'Vz', 24090, 'My', 14090, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174035, 74035, 174035, 4090, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124001, 124001, 24001, 4090, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173002, 2.95, 0.0, 9.675)
    ops.node(124036, 2.95, 0.0, 10.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4091, 173002, 124036, 0.175, 29304337.85267856, 12210140.7719494, 0.00405757, 0.00401042, 0.0019651, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24091, 86.24861343, 0.00078725, 105.02520567, 0.01531891, 10.50252057, 0.0494988, -86.24861343, -0.00078725, -105.02520567, -0.01531891, -10.50252057, -0.0494988, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14091, 143.18699659, 0.00067855, 174.35925248, 0.01671586, 17.43592525, 0.05990104, -143.18699659, -0.00067855, -174.35925248, -0.01671586, -17.43592525, -0.05990104, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24091, 4091, 0.0, 187.69976793, 0.01574509, 187.69976793, 0.04723528, 131.38983755, -3287.24811153, 0.05, 2, 0, 73002, 24036, 2, 3)
    ops.uniaxialMaterial('LimitState', 44091, 46.92494198, 3.755e-05, 140.77482595, 0.00011266, 469.24941984, 0.00037553, -46.92494198, -3.755e-05, -140.77482595, -0.00011266, -469.24941984, -0.00037553, 0.4, 0.3, 0.003, 0.0, 0.0, 24091, 2)
    ops.limitCurve('ThreePoint', 14091, 4091, 0.0, 244.69223339, 0.01357108, 244.69223339, 0.04071324, 171.28456338, -5743.73109351, 0.05, 2, 0, 73002, 24036, 1, 3)
    ops.uniaxialMaterial('LimitState', 34091, 61.17305835, 4.896e-05, 183.51917504, 0.00014687, 611.73058348, 0.00048955, -61.17305835, -4.896e-05, -183.51917504, -0.00014687, -611.73058348, -0.00048955, 0.4, 0.3, 0.003, 0.0, 0.0, 14091, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4091, 99999, 'P', 44091, 'Vy', 34091, 'Vz', 24091, 'My', 14091, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173002, 73002, 173002, 4091, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124036, 124036, 24036, 4091, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174036, 2.95, 0.0, 11.025)
    ops.node(124002, 2.95, 0.0, 12.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4092, 174036, 124002, 0.175, 29564452.73588933, 12318521.97328722, 0.00405757, 0.00401042, 0.0019651, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24092, 79.57462133, 0.00074412, 96.90910856, 0.01616243, 9.69091086, 0.05121426, -79.57462133, -0.00074412, -96.90910856, -0.01616243, -9.69091086, -0.05121426, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14092, 132.83855698, 0.0006497, 161.77602763, 0.01766552, 16.17760276, 0.06195237, -132.83855698, -0.0006497, -161.77602763, -0.01766552, -16.17760276, -0.06195237, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24092, 4092, 0.0, 188.82357804, 0.01488241, 188.82357804, 0.04464723, 132.17650463, -5927.17519658, 0.05, 2, 0, 74036, 24002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44092, 47.20589451, 3.745e-05, 141.61768353, 0.00011234, 472.0589451, 0.00037445, -47.20589451, -3.745e-05, -141.61768353, -0.00011234, -472.0589451, -0.00037445, 0.4, 0.3, 0.003, 0.0, 0.0, 24092, 2)
    ops.limitCurve('ThreePoint', 14092, 4092, 0.0, 246.72008766, 0.01299396, 246.72008766, 0.03898189, 172.70406136, -11160.11227373, 0.05, 2, 0, 74036, 24002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34092, 61.68002192, 4.893e-05, 185.04006575, 0.00014678, 616.80021916, 0.00048926, -61.68002192, -4.893e-05, -185.04006575, -0.00014678, -616.80021916, -0.00048926, 0.4, 0.3, 0.003, 0.0, 0.0, 14092, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4092, 99999, 'P', 44092, 'Vy', 34092, 'Vz', 24092, 'My', 14092, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174036, 74036, 174036, 4092, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124002, 124002, 24002, 4092, '-orient', 0, 0, 1, 0, 1, 0)
