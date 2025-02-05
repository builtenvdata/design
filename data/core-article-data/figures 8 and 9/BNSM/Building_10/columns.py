import openseespy.opensees as ops


def add_columns() -> None:
    """Add components of all columns to ops domain (plastic hinges, column elements and nodes)
    """
    # Create elastic column element nodes
    ops.node(170001, 0.0, 0.0, 0.0)
    ops.node(121001, 0.0, 0.0, 2.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1, 170001, 121001, 0.09, 26119670.70288791, 10883196.1262033, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20001, 66.1547625, 0.00147024, 80.41031801, 0.01413884, 8.0410318, 0.05559862, -66.1547625, -0.00147024, -80.41031801, -0.01413884, -8.0410318, -0.05559862, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10001, 60.7162776, 0.00147024, 73.79990505, 0.01413884, 7.3799905, 0.05559862, -60.7162776, -0.00147024, -73.79990505, -0.01413884, -7.3799905, -0.05559862, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20001, 1, 0.0, 101.69928331, 0.02940478, 101.69928331, 0.08821434, 71.18949832, -1743.51030973, 0.05, 2, 0, 70001, 21001, 2, 3)
    ops.uniaxialMaterial('LimitState', 40001, 25.42482083, 9.033e-05, 76.27446248, 0.00027099, 254.24820827, 0.00090331, -25.42482083, -9.033e-05, -76.27446248, -0.00027099, -254.24820827, -0.00090331, 0.4, 0.3, 0.003, 0.0, 0.0, 20001, 2)
    ops.limitCurve('ThreePoint', 10001, 1, 0.0, 101.69928331, 0.02940478, 101.69928331, 0.08821434, 71.18949832, -1743.51030973, 0.05, 2, 0, 70001, 21001, 1, 3)
    ops.uniaxialMaterial('LimitState', 30001, 25.42482083, 9.033e-05, 76.27446248, 0.00027099, 254.24820827, 0.00090331, -25.42482083, -9.033e-05, -76.27446248, -0.00027099, -254.24820827, -0.00090331, 0.4, 0.3, 0.003, 0.0, 0.0, 10001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1, 99999, 'P', 40001, 'Vy', 30001, 'Vz', 20001, 'My', 10001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170001, 70001, 170001, 1, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121001, 121001, 21001, 1, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170002, 4.2, 0.0, 0.0)
    ops.node(121002, 4.2, 0.0, 2.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2, 170002, 121002, 0.1225, 29572314.77056647, 12321797.82106936, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20002, 103.98816542, 0.00121219, 125.63092081, 0.01531017, 12.56309208, 0.05508643, -103.98816542, -0.00121219, -125.63092081, -0.01531017, -12.56309208, -0.05508643, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10002, 103.98816542, 0.00121219, 125.63092081, 0.01531017, 12.56309208, 0.05508643, -103.98816542, -0.00121219, -125.63092081, -0.01531017, -12.56309208, -0.05508643, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20002, 2, 0.0, 149.63618515, 0.02424387, 149.63618515, 0.0727316, 104.7453296, -2136.67169813, 0.05, 2, 0, 70002, 21002, 2, 3)
    ops.uniaxialMaterial('LimitState', 40002, 37.40904629, 8.625e-05, 112.22713886, 0.00025874, 374.09046287, 0.00086247, -37.40904629, -8.625e-05, -112.22713886, -0.00025874, -374.09046287, -0.00086247, 0.4, 0.3, 0.003, 0.0, 0.0, 20002, 2)
    ops.limitCurve('ThreePoint', 10002, 2, 0.0, 149.63618515, 0.02424387, 149.63618515, 0.0727316, 104.7453296, -2136.67169813, 0.05, 2, 0, 70002, 21002, 1, 3)
    ops.uniaxialMaterial('LimitState', 30002, 37.40904629, 8.625e-05, 112.22713886, 0.00025874, 374.09046287, 0.00086247, -37.40904629, -8.625e-05, -112.22713886, -0.00025874, -374.09046287, -0.00086247, 0.4, 0.3, 0.003, 0.0, 0.0, 10002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2, 99999, 'P', 40002, 'Vy', 30002, 'Vz', 20002, 'My', 10002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170002, 70002, 170002, 2, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121002, 121002, 21002, 2, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170003, 8.4, 0.0, 0.0)
    ops.node(121003, 8.4, 0.0, 2.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3, 170003, 121003, 0.1225, 29066308.54822284, 12110961.89509285, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20003, 104.98170996, 0.00116786, 126.94451018, 0.01417508, 12.69445102, 0.05333875, -104.98170996, -0.00116786, -126.94451018, -0.01417508, -12.69445102, -0.05333875, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10003, 104.98170996, 0.00116786, 126.94451018, 0.01417508, 12.69445102, 0.05333875, -104.98170996, -0.00116786, -126.94451018, -0.01417508, -12.69445102, -0.05333875, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20003, 3, 0.0, 143.10531799, 0.0233572, 143.10531799, 0.07007159, 100.17372259, -1964.04135848, 0.05, 2, 0, 70003, 21003, 2, 3)
    ops.uniaxialMaterial('LimitState', 40003, 35.7763295, 8.392e-05, 107.32898849, 0.00025176, 357.76329497, 0.00083919, -35.7763295, -8.392e-05, -107.32898849, -0.00025176, -357.76329497, -0.00083919, 0.4, 0.3, 0.003, 0.0, 0.0, 20003, 2)
    ops.limitCurve('ThreePoint', 10003, 3, 0.0, 143.10531799, 0.0233572, 143.10531799, 0.07007159, 100.17372259, -1964.04135848, 0.05, 2, 0, 70003, 21003, 1, 3)
    ops.uniaxialMaterial('LimitState', 30003, 35.7763295, 8.392e-05, 107.32898849, 0.00025176, 357.76329497, 0.00083919, -35.7763295, -8.392e-05, -107.32898849, -0.00025176, -357.76329497, -0.00083919, 0.4, 0.3, 0.003, 0.0, 0.0, 10003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3, 99999, 'P', 40003, 'Vy', 30003, 'Vz', 20003, 'My', 10003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170003, 70003, 170003, 3, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121003, 121003, 21003, 3, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170006, 19.7, 0.0, 0.0)
    ops.node(121006, 19.7, 0.0, 2.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 6, 170006, 121006, 0.1225, 28999916.03559846, 12083298.34816602, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20006, 106.80113569, 0.00125829, 129.15877327, 0.01655864, 12.91587733, 0.05563921, -106.80113569, -0.00125829, -129.15877327, -0.01655864, -12.91587733, -0.05563921, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10006, 106.80113569, 0.00125829, 129.15877327, 0.01655864, 12.91587733, 0.05563921, -106.80113569, -0.00125829, -129.15877327, -0.01655864, -12.91587733, -0.05563921, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20006, 6, 0.0, 151.60887402, 0.02516572, 151.60887402, 0.07549716, 106.12621181, -2294.44797966, 0.05, 2, 0, 70006, 21006, 2, 3)
    ops.uniaxialMaterial('LimitState', 40006, 37.90221851, 8.911e-05, 113.70665552, 0.00026733, 379.02218505, 0.00089109, -37.90221851, -8.911e-05, -113.70665552, -0.00026733, -379.02218505, -0.00089109, 0.4, 0.3, 0.003, 0.0, 0.0, 20006, 2)
    ops.limitCurve('ThreePoint', 10006, 6, 0.0, 151.60887402, 0.02516572, 151.60887402, 0.07549716, 106.12621181, -2294.44797966, 0.05, 2, 0, 70006, 21006, 1, 3)
    ops.uniaxialMaterial('LimitState', 30006, 37.90221851, 8.911e-05, 113.70665552, 0.00026733, 379.02218505, 0.00089109, -37.90221851, -8.911e-05, -113.70665552, -0.00026733, -379.02218505, -0.00089109, 0.4, 0.3, 0.003, 0.0, 0.0, 10006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 6, 99999, 'P', 40006, 'Vy', 30006, 'Vz', 20006, 'My', 10006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170006, 70006, 170006, 6, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121006, 121006, 21006, 6, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170007, 23.9, 0.0, 0.0)
    ops.node(121007, 23.9, 0.0, 2.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 7, 170007, 121007, 0.1225, 28588677.97429515, 11911949.15595631, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20007, 106.80702545, 0.00123459, 129.24905126, 0.01488278, 12.92490513, 0.0534339, -106.80702545, -0.00123459, -129.24905126, -0.01488278, -12.92490513, -0.0534339, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10007, 106.80702545, 0.00123459, 129.24905126, 0.01488278, 12.92490513, 0.0534339, -106.80702545, -0.00123459, -129.24905126, -0.01488278, -12.92490513, -0.0534339, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20007, 7, 0.0, 145.65520899, 0.02469189, 145.65520899, 0.07407568, 101.95864629, -2123.36744889, 0.05, 2, 0, 70007, 21007, 2, 3)
    ops.uniaxialMaterial('LimitState', 40007, 36.41380225, 8.684e-05, 109.24140674, 0.00026052, 364.13802247, 0.00086841, -36.41380225, -8.684e-05, -109.24140674, -0.00026052, -364.13802247, -0.00086841, 0.4, 0.3, 0.003, 0.0, 0.0, 20007, 2)
    ops.limitCurve('ThreePoint', 10007, 7, 0.0, 145.65520899, 0.02469189, 145.65520899, 0.07407568, 101.95864629, -2123.36744889, 0.05, 2, 0, 70007, 21007, 1, 3)
    ops.uniaxialMaterial('LimitState', 30007, 36.41380225, 8.684e-05, 109.24140674, 0.00026052, 364.13802247, 0.00086841, -36.41380225, -8.684e-05, -109.24140674, -0.00026052, -364.13802247, -0.00086841, 0.4, 0.3, 0.003, 0.0, 0.0, 10007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 7, 99999, 'P', 40007, 'Vy', 30007, 'Vz', 20007, 'My', 10007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170007, 70007, 170007, 7, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121007, 121007, 21007, 7, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170008, 28.1, 0.0, 0.0)
    ops.node(121008, 28.1, 0.0, 2.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 8, 170008, 121008, 0.09, 27933934.44590719, 11639139.35246133, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20008, 69.67667992, 0.00138051, 84.52791919, 0.01817, 8.45279192, 0.06252358, -69.67667992, -0.00138051, -84.52791919, -0.01817, -8.45279192, -0.06252358, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10008, 63.33620979, 0.00138051, 76.83600925, 0.01817, 7.68360093, 0.06252358, -63.33620979, -0.00138051, -76.83600925, -0.01817, -7.68360093, -0.06252358, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20008, 8, 0.0, 118.98092751, 0.02761014, 118.98092751, 0.08283042, 83.28664926, -2332.558092, 0.05, 2, 0, 70008, 21008, 2, 3)
    ops.uniaxialMaterial('LimitState', 40008, 29.74523188, 9.882e-05, 89.23569563, 0.00029645, 297.45231877, 0.00098817, -29.74523188, -9.882e-05, -89.23569563, -0.00029645, -297.45231877, -0.00098817, 0.4, 0.3, 0.003, 0.0, 0.0, 20008, 2)
    ops.limitCurve('ThreePoint', 10008, 8, 0.0, 118.98092751, 0.02761014, 118.98092751, 0.08283042, 83.28664926, -2332.558092, 0.05, 2, 0, 70008, 21008, 1, 3)
    ops.uniaxialMaterial('LimitState', 30008, 29.74523188, 9.882e-05, 89.23569563, 0.00029645, 297.45231877, 0.00098817, -29.74523188, -9.882e-05, -89.23569563, -0.00029645, -297.45231877, -0.00098817, 0.4, 0.3, 0.003, 0.0, 0.0, 10008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 8, 99999, 'P', 40008, 'Vy', 30008, 'Vz', 20008, 'My', 10008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170008, 70008, 170008, 8, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121008, 121008, 21008, 8, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170009, 0.0, 5.1, 0.0)
    ops.node(121009, 0.0, 5.1, 2.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 9, 170009, 121009, 0.1225, 29891199.07830913, 12454666.28262881, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20009, 110.14565062, 0.00124157, 132.91403704, 0.0146481, 13.2914037, 0.05412647, -110.14565062, -0.00124157, -132.91403704, -0.0146481, -13.2914037, -0.05412647, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10009, 110.14565062, 0.00124157, 132.91403704, 0.0146481, 13.2914037, 0.05412647, -110.14565062, -0.00124157, -132.91403704, -0.0146481, -13.2914037, -0.05412647, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20009, 9, 0.0, 151.60629788, 0.02483134, 151.60629788, 0.07449402, 106.12440852, -2101.94809315, 0.05, 2, 0, 70009, 21009, 2, 3)
    ops.uniaxialMaterial('LimitState', 40009, 37.90157447, 8.645e-05, 113.70472341, 0.00025935, 379.01574471, 0.00086451, -37.90157447, -8.645e-05, -113.70472341, -0.00025935, -379.01574471, -0.00086451, 0.4, 0.3, 0.003, 0.0, 0.0, 20009, 2)
    ops.limitCurve('ThreePoint', 10009, 9, 0.0, 151.60629788, 0.02483134, 151.60629788, 0.07449402, 106.12440852, -2101.94809315, 0.05, 2, 0, 70009, 21009, 1, 3)
    ops.uniaxialMaterial('LimitState', 30009, 37.90157447, 8.645e-05, 113.70472341, 0.00025935, 379.01574471, 0.00086451, -37.90157447, -8.645e-05, -113.70472341, -0.00025935, -379.01574471, -0.00086451, 0.4, 0.3, 0.003, 0.0, 0.0, 10009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 9, 99999, 'P', 40009, 'Vy', 30009, 'Vz', 20009, 'My', 10009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170009, 70009, 170009, 9, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121009, 121009, 21009, 9, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170010, 4.2, 5.1, 0.0)
    ops.node(121010, 4.2, 5.1, 2.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 10, 170010, 121010, 0.16, 28440848.95627252, 11850353.73178022, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20010, 214.73742106, 0.00105792, 259.66541101, 0.01770315, 25.9665411, 0.05155726, -214.73742106, -0.00105792, -259.66541101, -0.01770315, -25.9665411, -0.05155726, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10010, 206.25345508, 0.00105792, 249.40640491, 0.01770315, 24.94064049, 0.05155726, -206.25345508, -0.00105792, -249.40640491, -0.01770315, -24.94064049, -0.05155726, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20010, 10, 0.0, 190.81381343, 0.02115846, 190.81381343, 0.06347538, 133.5696694, -2706.55897408, 0.05, 2, 0, 70010, 21010, 2, 3)
    ops.uniaxialMaterial('LimitState', 40010, 47.70345336, 8.755e-05, 143.11036007, 0.00026266, 477.03453357, 0.00087554, -47.70345336, -8.755e-05, -143.11036007, -0.00026266, -477.03453357, -0.00087554, 0.4, 0.3, 0.003, 0.0, 0.0, 20010, 2)
    ops.limitCurve('ThreePoint', 10010, 10, 0.0, 190.81381343, 0.02115846, 190.81381343, 0.06347538, 133.5696694, -2706.55897408, 0.05, 2, 0, 70010, 21010, 1, 3)
    ops.uniaxialMaterial('LimitState', 30010, 47.70345336, 8.755e-05, 143.11036007, 0.00026266, 477.03453357, 0.00087554, -47.70345336, -8.755e-05, -143.11036007, -0.00026266, -477.03453357, -0.00087554, 0.4, 0.3, 0.003, 0.0, 0.0, 10010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 10, 99999, 'P', 40010, 'Vy', 30010, 'Vz', 20010, 'My', 10010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170010, 70010, 170010, 10, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121010, 121010, 21010, 10, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170011, 8.4, 5.1, 0.0)
    ops.node(121011, 8.4, 5.1, 2.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 11, 170011, 121011, 0.16, 28275730.93428167, 11781554.55595069, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20011, 222.49632678, 0.00116292, 269.10461922, 0.01704096, 26.91046192, 0.05067883, -222.49632678, -0.00116292, -269.10461922, -0.01704096, -26.91046192, -0.05067883, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10011, 214.08784127, 0.00116292, 258.93473316, 0.01704096, 25.89347332, 0.05067883, -214.08784127, -0.00116292, -258.93473316, -0.01704096, -25.89347332, -0.05067883, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20011, 11, 0.0, 192.32120225, 0.02325849, 192.32120225, 0.06977548, 134.62484157, -2789.01628549, 0.05, 2, 0, 70011, 21011, 2, 3)
    ops.uniaxialMaterial('LimitState', 40011, 48.08030056, 8.876e-05, 144.24090168, 0.00026628, 480.80300561, 0.00088761, -48.08030056, -8.876e-05, -144.24090168, -0.00026628, -480.80300561, -0.00088761, 0.4, 0.3, 0.003, 0.0, 0.0, 20011, 2)
    ops.limitCurve('ThreePoint', 10011, 11, 0.0, 192.32120225, 0.02325849, 192.32120225, 0.06977548, 134.62484157, -2789.01628549, 0.05, 2, 0, 70011, 21011, 1, 3)
    ops.uniaxialMaterial('LimitState', 30011, 48.08030056, 8.876e-05, 144.24090168, 0.00026628, 480.80300561, 0.00088761, -48.08030056, -8.876e-05, -144.24090168, -0.00026628, -480.80300561, -0.00088761, 0.4, 0.3, 0.003, 0.0, 0.0, 10011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 11, 99999, 'P', 40011, 'Vy', 30011, 'Vz', 20011, 'My', 10011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170011, 70011, 170011, 11, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121011, 121011, 21011, 11, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170012, 12.6, 5.1, 0.0)
    ops.node(121012, 12.6, 5.1, 2.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 12, 170012, 121012, 0.16, 29899976.45938116, 12458323.52474215, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20012, 242.38254221, 0.00115094, 292.43794202, 0.01772021, 29.2437942, 0.05974913, -242.38254221, -0.00115094, -292.43794202, -0.01772021, -29.2437942, -0.05974913, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10012, 214.70579996, 0.00115094, 259.04556372, 0.01772021, 25.90455637, 0.05974913, -214.70579996, -0.00115094, -259.04556372, -0.01772021, -25.90455637, -0.05974913, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20012, 12, 0.0, 202.19233496, 0.02301886, 202.19233496, 0.06905659, 141.53463447, -2876.04362946, 0.05, 2, 0, 70012, 21012, 2, 3)
    ops.uniaxialMaterial('LimitState', 40012, 50.54808374, 8.825e-05, 151.64425122, 0.00026474, 505.4808374, 0.00088248, -50.54808374, -8.825e-05, -151.64425122, -0.00026474, -505.4808374, -0.00088248, 0.4, 0.3, 0.003, 0.0, 0.0, 20012, 2)
    ops.limitCurve('ThreePoint', 10012, 12, 0.0, 202.19233496, 0.02301886, 202.19233496, 0.06905659, 141.53463447, -2876.04362946, 0.05, 2, 0, 70012, 21012, 1, 3)
    ops.uniaxialMaterial('LimitState', 30012, 50.54808374, 8.825e-05, 151.64425122, 0.00026474, 505.4808374, 0.00088248, -50.54808374, -8.825e-05, -151.64425122, -0.00026474, -505.4808374, -0.00088248, 0.4, 0.3, 0.003, 0.0, 0.0, 10012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 12, 99999, 'P', 40012, 'Vy', 30012, 'Vz', 20012, 'My', 10012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170012, 70012, 170012, 12, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121012, 121012, 21012, 12, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170013, 15.5, 5.1, 0.0)
    ops.node(121013, 15.5, 5.1, 2.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 13, 170013, 121013, 0.16, 29480732.14386581, 12283638.39327742, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20013, 226.89264214, 0.00110641, 273.95817597, 0.01840139, 27.3958176, 0.05987949, -226.89264214, -0.00110641, -273.95817597, -0.01840139, -27.3958176, -0.05987949, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10013, 202.14710049, 0.00110641, 244.0795365, 0.01840139, 24.40795365, 0.05987949, -202.14710049, -0.00110641, -244.0795365, -0.01840139, -24.40795365, -0.05987949, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20013, 13, 0.0, 193.08256036, 0.02212814, 193.08256036, 0.06638442, 135.15779225, -2621.41791554, 0.05, 2, 0, 70013, 21013, 2, 3)
    ops.uniaxialMaterial('LimitState', 40013, 48.27064009, 8.547e-05, 144.81192027, 0.00025641, 482.70640091, 0.0008547, -48.27064009, -8.547e-05, -144.81192027, -0.00025641, -482.70640091, -0.0008547, 0.4, 0.3, 0.003, 0.0, 0.0, 20013, 2)
    ops.limitCurve('ThreePoint', 10013, 13, 0.0, 193.08256036, 0.02212814, 193.08256036, 0.06638442, 135.15779225, -2621.41791554, 0.05, 2, 0, 70013, 21013, 1, 3)
    ops.uniaxialMaterial('LimitState', 30013, 48.27064009, 8.547e-05, 144.81192027, 0.00025641, 482.70640091, 0.0008547, -48.27064009, -8.547e-05, -144.81192027, -0.00025641, -482.70640091, -0.0008547, 0.4, 0.3, 0.003, 0.0, 0.0, 10013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 13, 99999, 'P', 40013, 'Vy', 30013, 'Vz', 20013, 'My', 10013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170013, 70013, 170013, 13, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121013, 121013, 21013, 13, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170014, 19.7, 5.1, 0.0)
    ops.node(121014, 19.7, 5.1, 2.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 14, 170014, 121014, 0.16, 27468781.31711004, 11445325.54879585, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20014, 223.40023283, 0.00112828, 270.4329787, 0.01379177, 27.04329787, 0.04631238, -223.40023283, -0.00112828, -270.4329787, -0.01379177, -27.04329787, -0.04631238, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10014, 214.393313, 0.00112828, 259.52982016, 0.01379177, 25.95298202, 0.04631238, -214.393313, -0.00112828, -259.52982016, -0.01379177, -25.95298202, -0.04631238, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20014, 14, 0.0, 171.96831591, 0.0225655, 171.96831591, 0.06769651, 120.37782114, -2223.25583499, 0.05, 2, 0, 70014, 21014, 2, 3)
    ops.uniaxialMaterial('LimitState', 40014, 42.99207898, 8.17e-05, 128.97623694, 0.0002451, 429.92078979, 0.000817, -42.99207898, -8.17e-05, -128.97623694, -0.0002451, -429.92078979, -0.000817, 0.4, 0.3, 0.003, 0.0, 0.0, 20014, 2)
    ops.limitCurve('ThreePoint', 10014, 14, 0.0, 171.96831591, 0.0225655, 171.96831591, 0.06769651, 120.37782114, -2223.25583499, 0.05, 2, 0, 70014, 21014, 1, 3)
    ops.uniaxialMaterial('LimitState', 30014, 42.99207898, 8.17e-05, 128.97623694, 0.0002451, 429.92078979, 0.000817, -42.99207898, -8.17e-05, -128.97623694, -0.0002451, -429.92078979, -0.000817, 0.4, 0.3, 0.003, 0.0, 0.0, 10014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 14, 99999, 'P', 40014, 'Vy', 30014, 'Vz', 20014, 'My', 10014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170014, 70014, 170014, 14, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121014, 121014, 21014, 14, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170015, 23.9, 5.1, 0.0)
    ops.node(121015, 23.9, 5.1, 2.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 15, 170015, 121015, 0.16, 29411701.51323947, 12254875.63051645, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20015, 225.34846319, 0.00112759, 272.0971372, 0.01474056, 27.20971372, 0.0497869, -225.34846319, -0.00112759, -272.0971372, -0.01474056, -27.20971372, -0.0497869, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10015, 216.63405648, 0.00112759, 261.57492159, 0.01474056, 26.15749216, 0.0497869, -216.63405648, -0.00112759, -261.57492159, -0.01474056, -26.15749216, -0.0497869, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20015, 15, 0.0, 189.46802456, 0.02255177, 189.46802456, 0.0676553, 132.62761719, -2495.66938346, 0.05, 2, 0, 70015, 21015, 2, 3)
    ops.uniaxialMaterial('LimitState', 40015, 47.36700614, 8.407e-05, 142.10101842, 0.0002522, 473.6700614, 0.00084067, -47.36700614, -8.407e-05, -142.10101842, -0.0002522, -473.6700614, -0.00084067, 0.4, 0.3, 0.003, 0.0, 0.0, 20015, 2)
    ops.limitCurve('ThreePoint', 10015, 15, 0.0, 189.46802456, 0.02255177, 189.46802456, 0.0676553, 132.62761719, -2495.66938346, 0.05, 2, 0, 70015, 21015, 1, 3)
    ops.uniaxialMaterial('LimitState', 30015, 47.36700614, 8.407e-05, 142.10101842, 0.0002522, 473.6700614, 0.00084067, -47.36700614, -8.407e-05, -142.10101842, -0.0002522, -473.6700614, -0.00084067, 0.4, 0.3, 0.003, 0.0, 0.0, 10015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 15, 99999, 'P', 40015, 'Vy', 30015, 'Vz', 20015, 'My', 10015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170015, 70015, 170015, 15, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121015, 121015, 21015, 15, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170016, 28.1, 5.1, 0.0)
    ops.node(121016, 28.1, 5.1, 2.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 16, 170016, 121016, 0.1225, 27811112.37580542, 11587963.48991892, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20016, 104.64366306, 0.00130774, 126.67194879, 0.01645872, 12.66719488, 0.05314755, -104.64366306, -0.00130774, -126.67194879, -0.01645872, -12.66719488, -0.05314755, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10016, 104.64366306, 0.00130774, 126.67194879, 0.01645872, 12.66719488, 0.05314755, -104.64366306, -0.00130774, -126.67194879, -0.01645872, -12.66719488, -0.05314755, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20016, 16, 0.0, 152.39952815, 0.02615482, 152.39952815, 0.07846445, 106.6796697, -2421.16557072, 0.05, 2, 0, 70016, 21016, 2, 3)
    ops.uniaxialMaterial('LimitState', 40016, 38.09988204, 9.34e-05, 114.29964611, 0.00028021, 380.99882037, 0.00093403, -38.09988204, -9.34e-05, -114.29964611, -0.00028021, -380.99882037, -0.00093403, 0.4, 0.3, 0.003, 0.0, 0.0, 20016, 2)
    ops.limitCurve('ThreePoint', 10016, 16, 0.0, 152.39952815, 0.02615482, 152.39952815, 0.07846445, 106.6796697, -2421.16557072, 0.05, 2, 0, 70016, 21016, 1, 3)
    ops.uniaxialMaterial('LimitState', 30016, 38.09988204, 9.34e-05, 114.29964611, 0.00028021, 380.99882037, 0.00093403, -38.09988204, -9.34e-05, -114.29964611, -0.00028021, -380.99882037, -0.00093403, 0.4, 0.3, 0.003, 0.0, 0.0, 10016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 16, 99999, 'P', 40016, 'Vy', 30016, 'Vz', 20016, 'My', 10016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170016, 70016, 170016, 16, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121016, 121016, 21016, 16, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170017, 0.0, 10.2, 0.0)
    ops.node(121017, 0.0, 10.2, 2.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 17, 170017, 121017, 0.1225, 30777085.77421134, 12823785.73925472, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20017, 108.4817189, 0.00112456, 130.67394344, 0.01391126, 13.06739434, 0.05446736, -108.4817189, -0.00112456, -130.67394344, -0.01391126, -13.06739434, -0.05446736, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10017, 108.4817189, 0.00112456, 130.67394344, 0.01391126, 13.06739434, 0.05446736, -108.4817189, -0.00112456, -130.67394344, -0.01391126, -13.06739434, -0.05446736, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20017, 17, 0.0, 153.99201015, 0.02249114, 153.99201015, 0.06747342, 107.7944071, -2074.10926399, 0.05, 2, 0, 70017, 21017, 2, 3)
    ops.uniaxialMaterial('LimitState', 40017, 38.49800254, 8.528e-05, 115.49400761, 0.00025585, 384.98002537, 0.00085284, -38.49800254, -8.528e-05, -115.49400761, -0.00025585, -384.98002537, -0.00085284, 0.4, 0.3, 0.003, 0.0, 0.0, 20017, 2)
    ops.limitCurve('ThreePoint', 10017, 17, 0.0, 153.99201015, 0.02249114, 153.99201015, 0.06747342, 107.7944071, -2074.10926399, 0.05, 2, 0, 70017, 21017, 1, 3)
    ops.uniaxialMaterial('LimitState', 30017, 38.49800254, 8.528e-05, 115.49400761, 0.00025585, 384.98002537, 0.00085284, -38.49800254, -8.528e-05, -115.49400761, -0.00025585, -384.98002537, -0.00085284, 0.4, 0.3, 0.003, 0.0, 0.0, 10017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 17, 99999, 'P', 40017, 'Vy', 30017, 'Vz', 20017, 'My', 10017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170017, 70017, 170017, 17, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121017, 121017, 21017, 17, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170018, 4.2, 10.2, 0.0)
    ops.node(121018, 4.2, 10.2, 2.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 18, 170018, 121018, 0.16, 31267157.87698254, 13027982.44874272, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20018, 170.67172394, 0.0011054, 205.31116538, 0.01990868, 20.53111654, 0.05698495, -170.67172394, -0.0011054, -205.31116538, -0.01990868, -20.53111654, -0.05698495, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10018, 170.67172394, 0.0011054, 205.31116538, 0.01990868, 20.53111654, 0.05698495, -170.67172394, -0.0011054, -205.31116538, -0.01990868, -20.53111654, -0.05698495, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20018, 18, 0.0, 205.39566577, 0.02210804, 205.39566577, 0.06632411, 143.77696604, -2743.20509229, 0.05, 2, 0, 70018, 21018, 2, 3)
    ops.uniaxialMaterial('LimitState', 40018, 51.34891644, 8.573e-05, 154.04674932, 0.00025718, 513.48916442, 0.00085726, -51.34891644, -8.573e-05, -154.04674932, -0.00025718, -513.48916442, -0.00085726, 0.4, 0.3, 0.003, 0.0, 0.0, 20018, 2)
    ops.limitCurve('ThreePoint', 10018, 18, 0.0, 205.39566577, 0.02210804, 205.39566577, 0.06632411, 143.77696604, -2743.20509229, 0.05, 2, 0, 70018, 21018, 1, 3)
    ops.uniaxialMaterial('LimitState', 30018, 51.34891644, 8.573e-05, 154.04674932, 0.00025718, 513.48916442, 0.00085726, -51.34891644, -8.573e-05, -154.04674932, -0.00025718, -513.48916442, -0.00085726, 0.4, 0.3, 0.003, 0.0, 0.0, 10018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 18, 99999, 'P', 40018, 'Vy', 30018, 'Vz', 20018, 'My', 10018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170018, 70018, 170018, 18, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121018, 121018, 21018, 18, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170019, 8.4, 10.2, 0.0)
    ops.node(121019, 8.4, 10.2, 2.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 19, 170019, 121019, 0.16, 29326258.13271105, 12219274.22196294, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20019, 173.89985909, 0.00117617, 210.02644548, 0.02060625, 21.00264455, 0.05565579, -173.89985909, -0.00117617, -210.02644548, -0.02060625, -21.00264455, -0.05565579, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10019, 173.89985909, 0.00117617, 210.02644548, 0.02060625, 21.00264455, 0.05565579, -173.89985909, -0.00117617, -210.02644548, -0.02060625, -21.00264455, -0.05565579, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20019, 19, 0.0, 195.11794152, 0.02352337, 195.11794152, 0.0705701, 136.58255907, -2719.53772873, 0.05, 2, 0, 70019, 21019, 2, 3)
    ops.uniaxialMaterial('LimitState', 40019, 48.77948538, 8.683e-05, 146.33845614, 0.00026048, 487.79485381, 0.00086826, -48.77948538, -8.683e-05, -146.33845614, -0.00026048, -487.79485381, -0.00086826, 0.4, 0.3, 0.003, 0.0, 0.0, 20019, 2)
    ops.limitCurve('ThreePoint', 10019, 19, 0.0, 195.11794152, 0.02352337, 195.11794152, 0.0705701, 136.58255907, -2719.53772873, 0.05, 2, 0, 70019, 21019, 1, 3)
    ops.uniaxialMaterial('LimitState', 30019, 48.77948538, 8.683e-05, 146.33845614, 0.00026048, 487.79485381, 0.00086826, -48.77948538, -8.683e-05, -146.33845614, -0.00026048, -487.79485381, -0.00086826, 0.4, 0.3, 0.003, 0.0, 0.0, 10019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 19, 99999, 'P', 40019, 'Vy', 30019, 'Vz', 20019, 'My', 10019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170019, 70019, 170019, 19, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121019, 121019, 21019, 19, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170020, 12.6, 10.2, 0.0)
    ops.node(121020, 12.6, 10.2, 2.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 20, 170020, 121020, 0.1225, 31207483.07457853, 13003117.94774106, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20020, 123.59034458, 0.0011604, 148.59511288, 0.01604768, 14.85951129, 0.05600083, -123.59034458, -0.0011604, -148.59511288, -0.01604768, -14.85951129, -0.05600083, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10020, 117.0241376, 0.0011604, 140.70043251, 0.01604768, 14.07004325, 0.05600083, -117.0241376, -0.0011604, -140.70043251, -0.01604768, -14.07004325, -0.05600083, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20020, 20, 0.0, 164.6560992, 0.02320804, 164.6560992, 0.06962413, 115.25926944, -2295.0078843, 0.05, 2, 0, 70020, 21020, 2, 3)
    ops.uniaxialMaterial('LimitState', 40020, 41.1640248, 8.993e-05, 123.4920744, 0.0002698, 411.64024799, 0.00089932, -41.1640248, -8.993e-05, -123.4920744, -0.0002698, -411.64024799, -0.00089932, 0.4, 0.3, 0.003, 0.0, 0.0, 20020, 2)
    ops.limitCurve('ThreePoint', 10020, 20, 0.0, 164.6560992, 0.02320804, 164.6560992, 0.06962413, 115.25926944, -2295.0078843, 0.05, 2, 0, 70020, 21020, 1, 3)
    ops.uniaxialMaterial('LimitState', 30020, 41.1640248, 8.993e-05, 123.4920744, 0.0002698, 411.64024799, 0.00089932, -41.1640248, -8.993e-05, -123.4920744, -0.0002698, -411.64024799, -0.00089932, 0.4, 0.3, 0.003, 0.0, 0.0, 10020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 20, 99999, 'P', 40020, 'Vy', 30020, 'Vz', 20020, 'My', 10020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170020, 70020, 170020, 20, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121020, 121020, 21020, 20, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170021, 15.5, 10.2, 0.0)
    ops.node(121021, 15.5, 10.2, 2.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 21, 170021, 121021, 0.1225, 26974783.30074484, 11239493.04197701, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20021, 133.04144662, 0.00125325, 160.95843111, 0.01427865, 16.09584311, 0.04828419, -133.04144662, -0.00125325, -160.95843111, -0.01427865, -16.09584311, -0.04828419, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10021, 124.66150845, 0.00125325, 150.82007397, 0.01427865, 15.0820074, 0.04828419, -124.66150845, -0.00125325, -150.82007397, -0.01427865, -15.0820074, -0.04828419, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20021, 21, 0.0, 141.92617606, 0.025065, 141.92617606, 0.07519499, 99.34832324, -2051.11439494, 0.05, 2, 0, 70021, 21021, 2, 3)
    ops.uniaxialMaterial('LimitState', 40021, 35.48154401, 8.968e-05, 106.44463204, 0.00026904, 354.81544015, 0.00089681, -35.48154401, -8.968e-05, -106.44463204, -0.00026904, -354.81544015, -0.00089681, 0.4, 0.3, 0.003, 0.0, 0.0, 20021, 2)
    ops.limitCurve('ThreePoint', 10021, 21, 0.0, 141.92617606, 0.025065, 141.92617606, 0.07519499, 99.34832324, -2051.11439494, 0.05, 2, 0, 70021, 21021, 1, 3)
    ops.uniaxialMaterial('LimitState', 30021, 35.48154401, 8.968e-05, 106.44463204, 0.00026904, 354.81544015, 0.00089681, -35.48154401, -8.968e-05, -106.44463204, -0.00026904, -354.81544015, -0.00089681, 0.4, 0.3, 0.003, 0.0, 0.0, 10021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 21, 99999, 'P', 40021, 'Vy', 30021, 'Vz', 20021, 'My', 10021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170021, 70021, 170021, 21, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121021, 121021, 21021, 21, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170022, 19.7, 10.2, 0.0)
    ops.node(121022, 19.7, 10.2, 2.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 22, 170022, 121022, 0.16, 29374857.33694636, 12239523.89039432, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20022, 170.34235856, 0.0011556, 205.71300616, 0.0184716, 20.57130062, 0.05357758, -170.34235856, -0.0011556, -205.71300616, -0.0184716, -20.57130062, -0.05357758, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10022, 170.34235856, 0.0011556, 205.71300616, 0.0184716, 20.57130062, 0.05357758, -170.34235856, -0.0011556, -205.71300616, -0.0184716, -20.57130062, -0.05357758, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20022, 22, 0.0, 188.47967046, 0.02311208, 188.47967046, 0.06933623, 131.93576932, -2478.38263509, 0.05, 2, 0, 70022, 21022, 2, 3)
    ops.uniaxialMaterial('LimitState', 40022, 47.11991761, 8.373e-05, 141.35975284, 0.0002512, 471.19917615, 0.00083734, -47.11991761, -8.373e-05, -141.35975284, -0.0002512, -471.19917615, -0.00083734, 0.4, 0.3, 0.003, 0.0, 0.0, 20022, 2)
    ops.limitCurve('ThreePoint', 10022, 22, 0.0, 188.47967046, 0.02311208, 188.47967046, 0.06933623, 131.93576932, -2478.38263509, 0.05, 2, 0, 70022, 21022, 1, 3)
    ops.uniaxialMaterial('LimitState', 30022, 47.11991761, 8.373e-05, 141.35975284, 0.0002512, 471.19917615, 0.00083734, -47.11991761, -8.373e-05, -141.35975284, -0.0002512, -471.19917615, -0.00083734, 0.4, 0.3, 0.003, 0.0, 0.0, 10022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 22, 99999, 'P', 40022, 'Vy', 30022, 'Vz', 20022, 'My', 10022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170022, 70022, 170022, 22, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121022, 121022, 21022, 22, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170023, 23.9, 10.2, 0.0)
    ops.node(121023, 23.9, 10.2, 2.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 23, 170023, 121023, 0.16, 26806364.07744209, 11169318.36560087, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20023, 172.53710148, 0.00121309, 208.99396968, 0.01723107, 20.89939697, 0.0488804, -172.53710148, -0.00121309, -208.99396968, -0.01723107, -20.89939697, -0.0488804, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10023, 172.53710148, 0.00121309, 208.99396968, 0.01723107, 20.89939697, 0.0488804, -172.53710148, -0.00121309, -208.99396968, -0.01723107, -20.89939697, -0.0488804, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20023, 23, 0.0, 171.98444733, 0.02426184, 171.98444733, 0.07278553, 120.38911313, -2333.80542611, 0.05, 2, 0, 70023, 21023, 2, 3)
    ops.uniaxialMaterial('LimitState', 40023, 42.99611183, 8.373e-05, 128.9883355, 0.00025118, 429.96111833, 0.00083726, -42.99611183, -8.373e-05, -128.9883355, -0.00025118, -429.96111833, -0.00083726, 0.4, 0.3, 0.003, 0.0, 0.0, 20023, 2)
    ops.limitCurve('ThreePoint', 10023, 23, 0.0, 171.98444733, 0.02426184, 171.98444733, 0.07278553, 120.38911313, -2333.80542611, 0.05, 2, 0, 70023, 21023, 1, 3)
    ops.uniaxialMaterial('LimitState', 30023, 42.99611183, 8.373e-05, 128.9883355, 0.00025118, 429.96111833, 0.00083726, -42.99611183, -8.373e-05, -128.9883355, -0.00025118, -429.96111833, -0.00083726, 0.4, 0.3, 0.003, 0.0, 0.0, 10023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 23, 99999, 'P', 40023, 'Vy', 30023, 'Vz', 20023, 'My', 10023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170023, 70023, 170023, 23, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121023, 121023, 21023, 23, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170024, 28.1, 10.2, 0.0)
    ops.node(121024, 28.1, 10.2, 2.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 24, 170024, 121024, 0.1225, 29034381.50609666, 12097658.96087361, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20024, 107.68545928, 0.0012199, 130.15054054, 0.01536532, 13.01505405, 0.05386462, -107.68545928, -0.0012199, -130.15054054, -0.01536532, -13.01505405, -0.05386462, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10024, 107.68545928, 0.0012199, 130.15054054, 0.01536532, 13.01505405, 0.05386462, -107.68545928, -0.0012199, -130.15054054, -0.01536532, -13.01505405, -0.05386462, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20024, 24, 0.0, 150.04728962, 0.02439808, 150.04728962, 0.07319425, 105.03310273, -2169.85429302, 0.05, 2, 0, 70024, 21024, 2, 3)
    ops.uniaxialMaterial('LimitState', 40024, 37.51182241, 8.809e-05, 112.53546722, 0.00026426, 375.11822405, 0.00088087, -37.51182241, -8.809e-05, -112.53546722, -0.00026426, -375.11822405, -0.00088087, 0.4, 0.3, 0.003, 0.0, 0.0, 20024, 2)
    ops.limitCurve('ThreePoint', 10024, 24, 0.0, 150.04728962, 0.02439808, 150.04728962, 0.07319425, 105.03310273, -2169.85429302, 0.05, 2, 0, 70024, 21024, 1, 3)
    ops.uniaxialMaterial('LimitState', 30024, 37.51182241, 8.809e-05, 112.53546722, 0.00026426, 375.11822405, 0.00088087, -37.51182241, -8.809e-05, -112.53546722, -0.00026426, -375.11822405, -0.00088087, 0.4, 0.3, 0.003, 0.0, 0.0, 10024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 24, 99999, 'P', 40024, 'Vy', 30024, 'Vz', 20024, 'My', 10024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170024, 70024, 170024, 24, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121024, 121024, 21024, 24, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170025, 0.0, 15.3, 0.0)
    ops.node(121025, 0.0, 15.3, 2.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 25, 170025, 121025, 0.09, 27146703.3221064, 11311126.384211, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20025, 64.39288166, 0.0013846, 78.19591435, 0.01837917, 7.81959144, 0.0615561, -64.39288166, -0.0013846, -78.19591435, -0.01837917, -7.81959144, -0.0615561, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10025, 59.19248132, 0.0013846, 71.88077439, 0.01837917, 7.18807744, 0.0615561, -59.19248132, -0.0013846, -71.88077439, -0.01837917, -7.18807744, -0.0615561, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20025, 25, 0.0, 117.41080917, 0.0276919, 117.41080917, 0.0830757, 82.18756642, -2356.59517439, 0.05, 2, 0, 70025, 21025, 2, 3)
    ops.uniaxialMaterial('LimitState', 40025, 29.35270229, 0.00010034, 88.05810688, 0.00030102, 293.52702292, 0.00100341, -29.35270229, -0.00010034, -88.05810688, -0.00030102, -293.52702292, -0.00100341, 0.4, 0.3, 0.003, 0.0, 0.0, 20025, 2)
    ops.limitCurve('ThreePoint', 10025, 25, 0.0, 117.41080917, 0.0276919, 117.41080917, 0.0830757, 82.18756642, -2356.59517439, 0.05, 2, 0, 70025, 21025, 1, 3)
    ops.uniaxialMaterial('LimitState', 30025, 29.35270229, 0.00010034, 88.05810688, 0.00030102, 293.52702292, 0.00100341, -29.35270229, -0.00010034, -88.05810688, -0.00030102, -293.52702292, -0.00100341, 0.4, 0.3, 0.003, 0.0, 0.0, 10025, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 25, 99999, 'P', 40025, 'Vy', 30025, 'Vz', 20025, 'My', 10025, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170025, 70025, 170025, 25, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121025, 121025, 21025, 25, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170026, 4.2, 15.3, 0.0)
    ops.node(121026, 4.2, 15.3, 2.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 26, 170026, 121026, 0.1225, 27411289.06153249, 11421370.4423052, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20026, 106.25737116, 0.0012839, 128.77343874, 0.01702607, 12.87734387, 0.05391215, -106.25737116, -0.0012839, -128.77343874, -0.01702607, -12.87734387, -0.05391215, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10026, 106.25737116, 0.0012839, 128.77343874, 0.01702607, 12.87734387, 0.05391215, -106.25737116, -0.0012839, -128.77343874, -0.01702607, -12.87734387, -0.05391215, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20026, 26, 0.0, 148.7922769, 0.02567798, 148.7922769, 0.07703394, 104.15459383, -2411.47802438, 0.05, 2, 0, 70026, 21026, 2, 3)
    ops.uniaxialMaterial('LimitState', 40026, 37.19806922, 9.252e-05, 111.59420767, 0.00027757, 371.98069225, 0.00092522, -37.19806922, -9.252e-05, -111.59420767, -0.00027757, -371.98069225, -0.00092522, 0.4, 0.3, 0.003, 0.0, 0.0, 20026, 2)
    ops.limitCurve('ThreePoint', 10026, 26, 0.0, 148.7922769, 0.02567798, 148.7922769, 0.07703394, 104.15459383, -2411.47802438, 0.05, 2, 0, 70026, 21026, 1, 3)
    ops.uniaxialMaterial('LimitState', 30026, 37.19806922, 9.252e-05, 111.59420767, 0.00027757, 371.98069225, 0.00092522, -37.19806922, -9.252e-05, -111.59420767, -0.00027757, -371.98069225, -0.00092522, 0.4, 0.3, 0.003, 0.0, 0.0, 10026, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 26, 99999, 'P', 40026, 'Vy', 30026, 'Vz', 20026, 'My', 10026, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170026, 70026, 170026, 26, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121026, 121026, 21026, 26, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170027, 8.4, 15.3, 0.0)
    ops.node(121027, 8.4, 15.3, 2.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 27, 170027, 121027, 0.1225, 29786223.56417813, 12410926.48507422, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20027, 107.43878597, 0.00119858, 129.74702589, 0.01626893, 12.97470259, 0.05629344, -107.43878597, -0.00119858, -129.74702589, -0.01626893, -12.97470259, -0.05629344, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10027, 107.43878597, 0.00119858, 129.74702589, 0.01626893, 12.97470259, 0.05629344, -107.43878597, -0.00119858, -129.74702589, -0.01626893, -12.97470259, -0.05629344, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20027, 27, 0.0, 157.63697469, 0.02397158, 157.63697469, 0.07191474, 110.34588228, -2418.07753571, 0.05, 2, 0, 70027, 21027, 2, 3)
    ops.uniaxialMaterial('LimitState', 40027, 39.40924367, 9.021e-05, 118.22773102, 0.00027062, 394.09243672, 0.00090206, -39.40924367, -9.021e-05, -118.22773102, -0.00027062, -394.09243672, -0.00090206, 0.4, 0.3, 0.003, 0.0, 0.0, 20027, 2)
    ops.limitCurve('ThreePoint', 10027, 27, 0.0, 157.63697469, 0.02397158, 157.63697469, 0.07191474, 110.34588228, -2418.07753571, 0.05, 2, 0, 70027, 21027, 1, 3)
    ops.uniaxialMaterial('LimitState', 30027, 39.40924367, 9.021e-05, 118.22773102, 0.00027062, 394.09243672, 0.00090206, -39.40924367, -9.021e-05, -118.22773102, -0.00027062, -394.09243672, -0.00090206, 0.4, 0.3, 0.003, 0.0, 0.0, 10027, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 27, 99999, 'P', 40027, 'Vy', 30027, 'Vz', 20027, 'My', 10027, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170027, 70027, 170027, 27, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121027, 121027, 21027, 27, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170028, 12.6, 15.3, 0.0)
    ops.node(121028, 12.6, 15.3, 2.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 28, 170028, 121028, 0.09, 28056698.06312323, 11690290.85963468, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20028, 82.53186805, 0.00139929, 99.80004509, 0.01414729, 9.98000451, 0.05479834, -82.53186805, -0.00139929, -99.80004509, -0.01414729, -9.98000451, -0.05479834, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10028, 82.53186805, 0.00139929, 99.80004509, 0.01414729, 9.98000451, 0.05479834, -82.53186805, -0.00139929, -99.80004509, -0.01414729, -9.98000451, -0.05479834, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20028, 28, 0.0, 110.77152645, 0.0279859, 110.77152645, 0.08395769, 77.54006852, -1655.58680442, 0.05, 2, 0, 70028, 21028, 2, 3)
    ops.uniaxialMaterial('LimitState', 40028, 27.69288161, 9.16e-05, 83.07864484, 0.00027479, 276.92881613, 0.00091597, -27.69288161, -9.16e-05, -83.07864484, -0.00027479, -276.92881613, -0.00091597, 0.4, 0.3, 0.003, 0.0, 0.0, 20028, 2)
    ops.limitCurve('ThreePoint', 10028, 28, 0.0, 110.77152645, 0.0279859, 110.77152645, 0.08395769, 77.54006852, -1655.58680442, 0.05, 2, 0, 70028, 21028, 1, 3)
    ops.uniaxialMaterial('LimitState', 30028, 27.69288161, 9.16e-05, 83.07864484, 0.00027479, 276.92881613, 0.00091597, -27.69288161, -9.16e-05, -83.07864484, -0.00027479, -276.92881613, -0.00091597, 0.4, 0.3, 0.003, 0.0, 0.0, 10028, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 28, 99999, 'P', 40028, 'Vy', 30028, 'Vz', 20028, 'My', 10028, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170028, 70028, 170028, 28, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121028, 121028, 21028, 28, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170029, 15.5, 15.3, 0.0)
    ops.node(121029, 15.5, 15.3, 2.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 29, 170029, 121029, 0.09, 27242382.07450357, 11350992.53104316, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20029, 79.17833643, 0.00147515, 95.81681738, 0.01842647, 9.58168174, 0.05761128, -79.17833643, -0.00147515, -95.81681738, -0.01842647, -9.58168174, -0.05761128, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10029, 79.17833643, 0.00147515, 95.81681738, 0.01842647, 9.58168174, 0.05761128, -79.17833643, -0.00147515, -95.81681738, -0.01842647, -9.58168174, -0.05761128, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20029, 29, 0.0, 122.61006163, 0.02950296, 122.61006163, 0.08850889, 85.82704314, -2204.93752309, 0.05, 2, 0, 70029, 21029, 2, 3)
    ops.uniaxialMaterial('LimitState', 40029, 30.65251541, 0.00010442, 91.95754622, 0.00031325, 306.52515407, 0.00104416, -30.65251541, -0.00010442, -91.95754622, -0.00031325, -306.52515407, -0.00104416, 0.4, 0.3, 0.003, 0.0, 0.0, 20029, 2)
    ops.limitCurve('ThreePoint', 10029, 29, 0.0, 122.61006163, 0.02950296, 122.61006163, 0.08850889, 85.82704314, -2204.93752309, 0.05, 2, 0, 70029, 21029, 1, 3)
    ops.uniaxialMaterial('LimitState', 30029, 30.65251541, 0.00010442, 91.95754622, 0.00031325, 306.52515407, 0.00104416, -30.65251541, -0.00010442, -91.95754622, -0.00031325, -306.52515407, -0.00104416, 0.4, 0.3, 0.003, 0.0, 0.0, 10029, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 29, 99999, 'P', 40029, 'Vy', 30029, 'Vz', 20029, 'My', 10029, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170029, 70029, 170029, 29, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121029, 121029, 21029, 29, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170030, 19.7, 15.3, 0.0)
    ops.node(121030, 19.7, 15.3, 2.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 30, 170030, 121030, 0.1225, 28024539.16208893, 11676891.31753705, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20030, 101.77856353, 0.00117618, 123.25957524, 0.0147807, 12.32595752, 0.05256268, -101.77856353, -0.00117618, -123.25957524, -0.0147807, -12.32595752, -0.05256268, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10030, 101.77856353, 0.00117618, 123.25957524, 0.0147807, 12.32595752, 0.05256268, -101.77856353, -0.00117618, -123.25957524, -0.0147807, -12.32595752, -0.05256268, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20030, 30, 0.0, 143.88992286, 0.02352352, 143.88992286, 0.07057055, 100.72294601, -2134.1386695, 0.05, 2, 0, 70030, 21030, 2, 3)
    ops.uniaxialMaterial('LimitState', 40030, 35.97248072, 8.752e-05, 107.91744215, 0.00026255, 359.72480716, 0.00087516, -35.97248072, -8.752e-05, -107.91744215, -0.00026255, -359.72480716, -0.00087516, 0.4, 0.3, 0.003, 0.0, 0.0, 20030, 2)
    ops.limitCurve('ThreePoint', 10030, 30, 0.0, 143.88992286, 0.02352352, 143.88992286, 0.07057055, 100.72294601, -2134.1386695, 0.05, 2, 0, 70030, 21030, 1, 3)
    ops.uniaxialMaterial('LimitState', 30030, 35.97248072, 8.752e-05, 107.91744215, 0.00026255, 359.72480716, 0.00087516, -35.97248072, -8.752e-05, -107.91744215, -0.00026255, -359.72480716, -0.00087516, 0.4, 0.3, 0.003, 0.0, 0.0, 10030, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 30, 99999, 'P', 40030, 'Vy', 30030, 'Vz', 20030, 'My', 10030, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170030, 70030, 170030, 30, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121030, 121030, 21030, 30, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170031, 23.9, 15.3, 0.0)
    ops.node(121031, 23.9, 15.3, 2.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 31, 170031, 121031, 0.1225, 28680077.64586187, 11950032.35244245, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20031, 100.77937902, 0.00125984, 121.93813437, 0.01554623, 12.19381344, 0.05421724, -100.77937902, -0.00125984, -121.93813437, -0.01554623, -12.19381344, -0.05421724, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10031, 100.77937902, 0.00125984, 121.93813437, 0.01554623, 12.19381344, 0.05421724, -100.77937902, -0.00125984, -121.93813437, -0.01554623, -12.19381344, -0.05421724, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20031, 31, 0.0, 150.47268088, 0.02519685, 150.47268088, 0.07559056, 105.33087662, -2295.95314807, 0.05, 2, 0, 70031, 21031, 2, 3)
    ops.uniaxialMaterial('LimitState', 40031, 37.61817022, 8.943e-05, 112.85451066, 0.00026828, 376.18170221, 0.00089428, -37.61817022, -8.943e-05, -112.85451066, -0.00026828, -376.18170221, -0.00089428, 0.4, 0.3, 0.003, 0.0, 0.0, 20031, 2)
    ops.limitCurve('ThreePoint', 10031, 31, 0.0, 150.47268088, 0.02519685, 150.47268088, 0.07559056, 105.33087662, -2295.95314807, 0.05, 2, 0, 70031, 21031, 1, 3)
    ops.uniaxialMaterial('LimitState', 30031, 37.61817022, 8.943e-05, 112.85451066, 0.00026828, 376.18170221, 0.00089428, -37.61817022, -8.943e-05, -112.85451066, -0.00026828, -376.18170221, -0.00089428, 0.4, 0.3, 0.003, 0.0, 0.0, 10031, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 31, 99999, 'P', 40031, 'Vy', 30031, 'Vz', 20031, 'My', 10031, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170031, 70031, 170031, 31, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121031, 121031, 21031, 31, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170032, 28.1, 15.3, 0.0)
    ops.node(121032, 28.1, 15.3, 2.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 32, 170032, 121032, 0.09, 29209679.05183822, 12170699.60493259, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20032, 67.07496557, 0.00139524, 81.20033515, 0.01775511, 8.12003351, 0.06378956, -67.07496557, -0.00139524, -81.20033515, -0.01775511, -8.12003351, -0.06378956, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10032, 61.62446811, 0.00139524, 74.60201315, 0.01775511, 7.46020132, 0.06378956, -61.62446811, -0.00139524, -74.60201315, -0.01775511, -7.46020132, -0.06378956, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20032, 32, 0.0, 120.80224782, 0.02790486, 120.80224782, 0.08371458, 84.56157347, -2254.59055619, 0.05, 2, 0, 70032, 21032, 2, 3)
    ops.uniaxialMaterial('LimitState', 40032, 30.20056195, 9.595e-05, 90.60168586, 0.00028784, 302.00561954, 0.00095948, -30.20056195, -9.595e-05, -90.60168586, -0.00028784, -302.00561954, -0.00095948, 0.4, 0.3, 0.003, 0.0, 0.0, 20032, 2)
    ops.limitCurve('ThreePoint', 10032, 32, 0.0, 120.80224782, 0.02790486, 120.80224782, 0.08371458, 84.56157347, -2254.59055619, 0.05, 2, 0, 70032, 21032, 1, 3)
    ops.uniaxialMaterial('LimitState', 30032, 30.20056195, 9.595e-05, 90.60168586, 0.00028784, 302.00561954, 0.00095948, -30.20056195, -9.595e-05, -90.60168586, -0.00028784, -302.00561954, -0.00095948, 0.4, 0.3, 0.003, 0.0, 0.0, 10032, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 32, 99999, 'P', 40032, 'Vy', 30032, 'Vz', 20032, 'My', 10032, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170032, 70032, 170032, 32, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121032, 121032, 21032, 32, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171001, 0.0, 0.0, 3.15)
    ops.node(122001, 0.0, 0.0, 5.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1001, 171001, 122001, 0.09, 27916710.31017665, 11631962.62924027, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21001, 63.64919837, 0.00137365, 77.41585834, 0.01590509, 7.74158583, 0.06375556, -63.64919837, -0.00137365, -77.41585834, -0.01590509, -7.74158583, -0.06375556, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11001, 57.7037847, 0.00137365, 70.18451349, 0.01590509, 7.01845135, 0.06375556, -57.7037847, -0.00137365, -70.18451349, -0.01590509, -7.01845135, -0.06375556, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21001, 1001, 0.0, 104.49829963, 0.02747307, 104.49829963, 0.0824192, 73.14880974, -2036.98711165, 0.05, 2, 0, 71001, 22001, 2, 3)
    ops.uniaxialMaterial('LimitState', 41001, 26.12457491, 8.684e-05, 78.37372472, 0.00026053, 261.24574908, 0.00086843, -26.12457491, -8.684e-05, -78.37372472, -0.00026053, -261.24574908, -0.00086843, 0.4, 0.3, 0.003, 0.0, 0.0, 21001, 2)
    ops.limitCurve('ThreePoint', 11001, 1001, 0.0, 104.49829963, 0.02747307, 104.49829963, 0.0824192, 73.14880974, -2036.98711165, 0.05, 2, 0, 71001, 22001, 1, 3)
    ops.uniaxialMaterial('LimitState', 31001, 26.12457491, 8.684e-05, 78.37372472, 0.00026053, 261.24574908, 0.00086843, -26.12457491, -8.684e-05, -78.37372472, -0.00026053, -261.24574908, -0.00086843, 0.4, 0.3, 0.003, 0.0, 0.0, 11001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1001, 99999, 'P', 41001, 'Vy', 31001, 'Vz', 21001, 'My', 11001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171001, 71001, 171001, 1001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122001, 122001, 22001, 1001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171002, 4.2, 0.0, 3.175)
    ops.node(122002, 4.2, 0.0, 5.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1002, 171002, 122002, 0.1225, 29991765.57221067, 12496568.98842111, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21002, 88.6886593, 0.00113031, 107.31165524, 0.0151799, 10.73116552, 0.05835296, -88.6886593, -0.00113031, -107.31165524, -0.0151799, -10.73116552, -0.05835296, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11002, 103.20924701, 0.00113031, 124.88130071, 0.0151799, 12.48813007, 0.05835296, -103.20924701, -0.00113031, -124.88130071, -0.0151799, -12.48813007, -0.05835296, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21002, 1002, 0.0, 147.55954129, 0.02260611, 147.55954129, 0.06781833, 103.2916789, -2385.48154503, 0.05, 2, 0, 71002, 22002, 2, 3)
    ops.uniaxialMaterial('LimitState', 41002, 36.88988532, 8.386e-05, 110.66965597, 0.00025158, 368.89885323, 0.00083861, -36.88988532, -8.386e-05, -110.66965597, -0.00025158, -368.89885323, -0.00083861, 0.4, 0.3, 0.003, 0.0, 0.0, 21002, 2)
    ops.limitCurve('ThreePoint', 11002, 1002, 0.0, 147.55954129, 0.02260611, 147.55954129, 0.06781833, 103.2916789, -2385.48154503, 0.05, 2, 0, 71002, 22002, 1, 3)
    ops.uniaxialMaterial('LimitState', 31002, 36.88988532, 8.386e-05, 110.66965597, 0.00025158, 368.89885323, 0.00083861, -36.88988532, -8.386e-05, -110.66965597, -0.00025158, -368.89885323, -0.00083861, 0.4, 0.3, 0.003, 0.0, 0.0, 11002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1002, 99999, 'P', 41002, 'Vy', 31002, 'Vz', 21002, 'My', 11002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171002, 71002, 171002, 1002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122002, 122002, 22002, 1002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171003, 8.4, 0.0, 3.175)
    ops.node(122003, 8.4, 0.0, 5.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1003, 171003, 122003, 0.1225, 29277024.7654951, 12198760.31895629, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21003, 87.646855, 0.00114296, 106.21462068, 0.01790835, 10.62146207, 0.06043514, -87.646855, -0.00114296, -106.21462068, -0.01790835, -10.62146207, -0.06043514, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11003, 101.70890919, 0.00114296, 123.25568568, 0.01790835, 12.32556857, 0.06043514, -101.70890919, -0.00114296, -123.25568568, -0.01790835, -12.32556857, -0.06043514, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21003, 1003, 0.0, 149.88553121, 0.02285916, 149.88553121, 0.06857747, 104.91987185, -2624.40670469, 0.05, 2, 0, 71003, 22003, 2, 3)
    ops.uniaxialMaterial('LimitState', 41003, 37.4713828, 8.726e-05, 112.41414841, 0.00026179, 374.71382803, 0.00087262, -37.4713828, -8.726e-05, -112.41414841, -0.00026179, -374.71382803, -0.00087262, 0.4, 0.3, 0.003, 0.0, 0.0, 21003, 2)
    ops.limitCurve('ThreePoint', 11003, 1003, 0.0, 149.88553121, 0.02285916, 149.88553121, 0.06857747, 104.91987185, -2624.40670469, 0.05, 2, 0, 71003, 22003, 1, 3)
    ops.uniaxialMaterial('LimitState', 31003, 37.4713828, 8.726e-05, 112.41414841, 0.00026179, 374.71382803, 0.00087262, -37.4713828, -8.726e-05, -112.41414841, -0.00026179, -374.71382803, -0.00087262, 0.4, 0.3, 0.003, 0.0, 0.0, 11003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1003, 99999, 'P', 41003, 'Vy', 31003, 'Vz', 21003, 'My', 11003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171003, 71003, 171003, 1003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122003, 122003, 22003, 1003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171006, 19.7, 0.0, 3.175)
    ops.node(122006, 19.7, 0.0, 5.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1006, 171006, 122006, 0.1225, 29374815.93712174, 12239506.64046739, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21006, 87.2231166, 0.00117947, 105.67988466, 0.01499062, 10.56798847, 0.05760929, -87.2231166, -0.00117947, -105.67988466, -0.01499062, -10.56798847, -0.05760929, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11006, 100.29761195, 0.00117947, 121.52099667, 0.01499062, 12.15209967, 0.05760929, -100.29761195, -0.00117947, -121.52099667, -0.01499062, -12.15209967, -0.05760929, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21006, 1006, 0.0, 143.2576788, 0.02358941, 143.2576788, 0.07076822, 100.28037516, -2290.46269671, 0.05, 2, 0, 71006, 22006, 2, 3)
    ops.uniaxialMaterial('LimitState', 41006, 35.8144197, 8.313e-05, 107.4432591, 0.00024938, 358.14419701, 0.00083126, -35.8144197, -8.313e-05, -107.4432591, -0.00024938, -358.14419701, -0.00083126, 0.4, 0.3, 0.003, 0.0, 0.0, 21006, 2)
    ops.limitCurve('ThreePoint', 11006, 1006, 0.0, 143.2576788, 0.02358941, 143.2576788, 0.07076822, 100.28037516, -2290.46269671, 0.05, 2, 0, 71006, 22006, 1, 3)
    ops.uniaxialMaterial('LimitState', 31006, 35.8144197, 8.313e-05, 107.4432591, 0.00024938, 358.14419701, 0.00083126, -35.8144197, -8.313e-05, -107.4432591, -0.00024938, -358.14419701, -0.00083126, 0.4, 0.3, 0.003, 0.0, 0.0, 11006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1006, 99999, 'P', 41006, 'Vy', 31006, 'Vz', 21006, 'My', 11006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171006, 71006, 171006, 1006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122006, 122006, 22006, 1006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171007, 23.9, 0.0, 3.175)
    ops.node(122007, 23.9, 0.0, 5.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1007, 171007, 122007, 0.1225, 28849840.55794065, 12020766.89914194, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21007, 91.50165781, 0.00123482, 110.97924518, 0.01741258, 11.09792452, 0.05952448, -91.50165781, -0.00123482, -110.97924518, -0.01741258, -11.09792452, -0.05952448, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11007, 106.14986991, 0.00123482, 128.74556287, 0.01741258, 12.87455629, 0.05952448, -106.14986991, -0.00123482, -128.74556287, -0.01741258, -12.87455629, -0.05952448, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21007, 1007, 0.0, 148.81698493, 0.02469645, 148.81698493, 0.07408935, 104.17188945, -2648.21070885, 0.05, 2, 0, 71007, 22007, 2, 3)
    ops.uniaxialMaterial('LimitState', 41007, 37.20424623, 8.792e-05, 111.6127387, 0.00026377, 372.04246233, 0.00087923, -37.20424623, -8.792e-05, -111.6127387, -0.00026377, -372.04246233, -0.00087923, 0.4, 0.3, 0.003, 0.0, 0.0, 21007, 2)
    ops.limitCurve('ThreePoint', 11007, 1007, 0.0, 148.81698493, 0.02469645, 148.81698493, 0.07408935, 104.17188945, -2648.21070885, 0.05, 2, 0, 71007, 22007, 1, 3)
    ops.uniaxialMaterial('LimitState', 31007, 37.20424623, 8.792e-05, 111.6127387, 0.00026377, 372.04246233, 0.00087923, -37.20424623, -8.792e-05, -111.6127387, -0.00026377, -372.04246233, -0.00087923, 0.4, 0.3, 0.003, 0.0, 0.0, 11007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1007, 99999, 'P', 41007, 'Vy', 31007, 'Vz', 21007, 'My', 11007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171007, 71007, 171007, 1007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122007, 122007, 22007, 1007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171008, 28.1, 0.0, 3.15)
    ops.node(122008, 28.1, 0.0, 5.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1008, 171008, 122008, 0.09, 30830255.90546865, 12845939.96061194, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21008, 60.18647558, 0.00126953, 72.74020664, 0.01816768, 7.27402066, 0.06869265, -60.18647558, -0.00126953, -72.74020664, -0.01816768, -7.27402066, -0.06869265, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11008, 54.9916359, 0.00126953, 66.4618242, 0.01816768, 6.64618242, 0.06869265, -54.9916359, -0.00126953, -66.4618242, -0.01816768, -6.64618242, -0.06869265, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21008, 1008, 0.0, 123.05625262, 0.02539066, 123.05625262, 0.07617198, 86.13937683, -2677.90499327, 0.05, 2, 0, 71008, 22008, 2, 3)
    ops.uniaxialMaterial('LimitState', 41008, 30.76406315, 9.26e-05, 92.29218946, 0.0002778, 307.64063154, 0.00092601, -30.76406315, -9.26e-05, -92.29218946, -0.0002778, -307.64063154, -0.00092601, 0.4, 0.3, 0.003, 0.0, 0.0, 21008, 2)
    ops.limitCurve('ThreePoint', 11008, 1008, 0.0, 123.05625262, 0.02539066, 123.05625262, 0.07617198, 86.13937683, -2677.90499327, 0.05, 2, 0, 71008, 22008, 1, 3)
    ops.uniaxialMaterial('LimitState', 31008, 30.76406315, 9.26e-05, 92.29218946, 0.0002778, 307.64063154, 0.00092601, -30.76406315, -9.26e-05, -92.29218946, -0.0002778, -307.64063154, -0.00092601, 0.4, 0.3, 0.003, 0.0, 0.0, 11008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1008, 99999, 'P', 41008, 'Vy', 31008, 'Vz', 21008, 'My', 11008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171008, 71008, 171008, 1008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122008, 122008, 22008, 1008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171009, 0.0, 5.1, 3.15)
    ops.node(122009, 0.0, 5.1, 5.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1009, 171009, 122009, 0.1225, 29709425.23400282, 12378927.18083451, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21009, 101.74656273, 0.00114928, 123.14051267, 0.01537364, 12.31405127, 0.05779847, -101.74656273, -0.00114928, -123.14051267, -0.01537364, -12.31405127, -0.05779847, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11009, 88.34233217, 0.00114928, 106.91781405, 0.01537364, 10.69178141, 0.05779847, -88.34233217, -0.00114928, -106.91781405, -0.01537364, -10.69178141, -0.05779847, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21009, 1009, 0.0, 146.15350665, 0.02298557, 146.15350665, 0.06895672, 102.30745465, -2284.70100819, 0.05, 2, 0, 71009, 22009, 2, 3)
    ops.uniaxialMaterial('LimitState', 41009, 36.53837666, 8.385e-05, 109.61512999, 0.00025155, 365.38376662, 0.00083851, -36.53837666, -8.385e-05, -109.61512999, -0.00025155, -365.38376662, -0.00083851, 0.4, 0.3, 0.003, 0.0, 0.0, 21009, 2)
    ops.limitCurve('ThreePoint', 11009, 1009, 0.0, 146.15350665, 0.02298557, 146.15350665, 0.06895672, 102.30745465, -2284.70100819, 0.05, 2, 0, 71009, 22009, 1, 3)
    ops.uniaxialMaterial('LimitState', 31009, 36.53837666, 8.385e-05, 109.61512999, 0.00025155, 365.38376662, 0.00083851, -36.53837666, -8.385e-05, -109.61512999, -0.00025155, -365.38376662, -0.00083851, 0.4, 0.3, 0.003, 0.0, 0.0, 11009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1009, 99999, 'P', 41009, 'Vy', 31009, 'Vz', 21009, 'My', 11009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171009, 71009, 171009, 1009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122009, 122009, 22009, 1009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171010, 4.2, 5.1, 3.175)
    ops.node(122010, 4.2, 5.1, 5.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1010, 171010, 122010, 0.16, 27667178.2657157, 11527990.94404821, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21010, 157.49089695, 0.00108269, 191.23315526, 0.01380637, 19.12331553, 0.04995308, -157.49089695, -0.00108269, -191.23315526, -0.01380637, -19.12331553, -0.04995308, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11010, 130.46124984, 0.00108269, 158.41243481, 0.01380637, 15.84124348, 0.04995308, -130.46124984, -0.00108269, -158.41243481, -0.01380637, -15.84124348, -0.04995308, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21010, 1010, 0.0, 167.20222896, 0.02165376, 167.20222896, 0.06496129, 117.04156027, -2336.80161822, 0.05, 2, 0, 71010, 22010, 2, 3)
    ops.uniaxialMaterial('LimitState', 41010, 41.80055724, 7.887e-05, 125.40167172, 0.0002366, 418.00557239, 0.00078866, -41.80055724, -7.887e-05, -125.40167172, -0.0002366, -418.00557239, -0.00078866, 0.4, 0.3, 0.003, 0.0, 0.0, 21010, 2)
    ops.limitCurve('ThreePoint', 11010, 1010, 0.0, 167.20222896, 0.02165376, 167.20222896, 0.06496129, 117.04156027, -2336.80161822, 0.05, 2, 0, 71010, 22010, 1, 3)
    ops.uniaxialMaterial('LimitState', 31010, 41.80055724, 7.887e-05, 125.40167172, 0.0002366, 418.00557239, 0.00078866, -41.80055724, -7.887e-05, -125.40167172, -0.0002366, -418.00557239, -0.00078866, 0.4, 0.3, 0.003, 0.0, 0.0, 11010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1010, 99999, 'P', 41010, 'Vy', 31010, 'Vz', 21010, 'My', 11010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171010, 71010, 171010, 1010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122010, 122010, 22010, 1010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171011, 8.4, 5.1, 3.175)
    ops.node(122011, 8.4, 5.1, 5.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1011, 171011, 122011, 0.16, 30293828.9700036, 12622428.7375015, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21011, 152.47759354, 0.00101167, 184.24830148, 0.01449635, 18.42483015, 0.05319466, -152.47759354, -0.00101167, -184.24830148, -0.01449635, -18.42483015, -0.05319466, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11011, 127.37313877, 0.00101167, 153.91300406, 0.01449635, 15.39130041, 0.05319466, -127.37313877, -0.00101167, -153.91300406, -0.01449635, -15.39130041, -0.05319466, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21011, 1011, 0.0, 185.15086272, 0.02023348, 185.15086272, 0.06070044, 129.60560391, -2553.76690663, 0.05, 2, 0, 71011, 22011, 2, 3)
    ops.uniaxialMaterial('LimitState', 41011, 46.28771568, 7.976e-05, 138.86314704, 0.00023928, 462.8771568, 0.00079759, -46.28771568, -7.976e-05, -138.86314704, -0.00023928, -462.8771568, -0.00079759, 0.4, 0.3, 0.003, 0.0, 0.0, 21011, 2)
    ops.limitCurve('ThreePoint', 11011, 1011, 0.0, 185.15086272, 0.02023348, 185.15086272, 0.06070044, 129.60560391, -2553.76690663, 0.05, 2, 0, 71011, 22011, 1, 3)
    ops.uniaxialMaterial('LimitState', 31011, 46.28771568, 7.976e-05, 138.86314704, 0.00023928, 462.8771568, 0.00079759, -46.28771568, -7.976e-05, -138.86314704, -0.00023928, -462.8771568, -0.00079759, 0.4, 0.3, 0.003, 0.0, 0.0, 11011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1011, 99999, 'P', 41011, 'Vy', 31011, 'Vz', 21011, 'My', 11011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171011, 71011, 171011, 1011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122011, 122011, 22011, 1011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171012, 12.6, 5.1, 3.15)
    ops.node(122012, 12.6, 5.1, 5.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1012, 171012, 122012, 0.16, 32711214.44554438, 13629672.68564349, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21012, 154.53596834, 0.00099115, 185.52125651, 0.01274945, 18.55212565, 0.05317556, -154.53596834, -0.00099115, -185.52125651, -0.01274945, -18.55212565, -0.05317556, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11012, 129.23708932, 0.00099115, 155.14981694, 0.01274945, 15.51498169, 0.05317556, -129.23708932, -0.00099115, -155.14981694, -0.01274945, -15.51498169, -0.05317556, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21012, 1012, 0.0, 188.00567163, 0.0198229, 188.00567163, 0.0594687, 131.60397014, -2194.55708623, 0.05, 2, 0, 71012, 22012, 2, 3)
    ops.uniaxialMaterial('LimitState', 41012, 47.00141791, 7.5e-05, 141.00425372, 0.00022501, 470.01417907, 0.00075004, -47.00141791, -7.5e-05, -141.00425372, -0.00022501, -470.01417907, -0.00075004, 0.4, 0.3, 0.003, 0.0, 0.0, 21012, 2)
    ops.limitCurve('ThreePoint', 11012, 1012, 0.0, 188.00567163, 0.0198229, 188.00567163, 0.0594687, 131.60397014, -2194.55708623, 0.05, 2, 0, 71012, 22012, 1, 3)
    ops.uniaxialMaterial('LimitState', 31012, 47.00141791, 7.5e-05, 141.00425372, 0.00022501, 470.01417907, 0.00075004, -47.00141791, -7.5e-05, -141.00425372, -0.00022501, -470.01417907, -0.00075004, 0.4, 0.3, 0.003, 0.0, 0.0, 11012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1012, 99999, 'P', 41012, 'Vy', 31012, 'Vz', 21012, 'My', 11012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171012, 71012, 171012, 1012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122012, 122012, 22012, 1012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171013, 15.5, 5.1, 3.15)
    ops.node(122013, 15.5, 5.1, 5.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1013, 171013, 122013, 0.16, 29351725.96147385, 12229885.81728077, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21013, 152.93059543, 0.00111387, 185.16949627, 0.01377937, 18.51694963, 0.05165885, -152.93059543, -0.00111387, -185.16949627, -0.01377937, -18.51694963, -0.05165885, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11013, 129.61101341, 0.00111387, 156.93397384, 0.01377937, 15.69339738, 0.05165885, -129.61101341, -0.00111387, -156.93397384, -0.01377937, -15.69339738, -0.05165885, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21013, 1013, 0.0, 174.88368178, 0.02227744, 174.88368178, 0.06683231, 122.41857725, -2327.78361411, 0.05, 2, 0, 71013, 22013, 2, 3)
    ops.uniaxialMaterial('LimitState', 41013, 43.72092045, 7.775e-05, 131.16276134, 0.00023326, 437.20920446, 0.00077755, -43.72092045, -7.775e-05, -131.16276134, -0.00023326, -437.20920446, -0.00077755, 0.4, 0.3, 0.003, 0.0, 0.0, 21013, 2)
    ops.limitCurve('ThreePoint', 11013, 1013, 0.0, 174.88368178, 0.02227744, 174.88368178, 0.06683231, 122.41857725, -2327.78361411, 0.05, 2, 0, 71013, 22013, 1, 3)
    ops.uniaxialMaterial('LimitState', 31013, 43.72092045, 7.775e-05, 131.16276134, 0.00023326, 437.20920446, 0.00077755, -43.72092045, -7.775e-05, -131.16276134, -0.00023326, -437.20920446, -0.00077755, 0.4, 0.3, 0.003, 0.0, 0.0, 11013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1013, 99999, 'P', 41013, 'Vy', 31013, 'Vz', 21013, 'My', 11013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171013, 71013, 171013, 1013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122013, 122013, 22013, 1013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171014, 19.7, 5.1, 3.175)
    ops.node(122014, 19.7, 5.1, 5.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1014, 171014, 122014, 0.16, 31588365.65630184, 13161819.0234591, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21014, 157.85555123, 0.00098344, 190.12667619, 0.01263752, 19.01266762, 0.05232171, -157.85555123, -0.00098344, -190.12667619, -0.01263752, -19.01266762, -0.05232171, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11014, 130.4342989, 0.00098344, 157.09957311, 0.01263752, 15.70995731, 0.05232171, -130.4342989, -0.00098344, -157.09957311, -0.01263752, -15.70995731, -0.05232171, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21014, 1014, 0.0, 181.97977804, 0.01966888, 181.97977804, 0.05900665, 127.38584463, -2180.96012452, 0.05, 2, 0, 71014, 22014, 2, 3)
    ops.uniaxialMaterial('LimitState', 41014, 45.49494451, 7.518e-05, 136.48483353, 0.00022554, 454.94944511, 0.00075181, -45.49494451, -7.518e-05, -136.48483353, -0.00022554, -454.94944511, -0.00075181, 0.4, 0.3, 0.003, 0.0, 0.0, 21014, 2)
    ops.limitCurve('ThreePoint', 11014, 1014, 0.0, 181.97977804, 0.01966888, 181.97977804, 0.05900665, 127.38584463, -2180.96012452, 0.05, 2, 0, 71014, 22014, 1, 3)
    ops.uniaxialMaterial('LimitState', 31014, 45.49494451, 7.518e-05, 136.48483353, 0.00022554, 454.94944511, 0.00075181, -45.49494451, -7.518e-05, -136.48483353, -0.00022554, -454.94944511, -0.00075181, 0.4, 0.3, 0.003, 0.0, 0.0, 11014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1014, 99999, 'P', 41014, 'Vy', 31014, 'Vz', 21014, 'My', 11014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171014, 71014, 171014, 1014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122014, 122014, 22014, 1014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171015, 23.9, 5.1, 3.175)
    ops.node(122015, 23.9, 5.1, 5.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1015, 171015, 122015, 0.16, 28641774.63244529, 11934072.76351887, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21015, 150.53151861, 0.00111449, 182.50497636, 0.01581045, 18.25049764, 0.05300193, -150.53151861, -0.00111449, -182.50497636, -0.01581045, -18.25049764, -0.05300193, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11015, 127.81354301, 0.00111449, 154.96161774, 0.01581045, 15.49616177, 0.05300193, -127.81354301, -0.00111449, -154.96161774, -0.01581045, -15.49616177, -0.05300193, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21015, 1015, 0.0, 180.95724979, 0.02228988, 180.95724979, 0.06686963, 126.67007485, -2707.1680289, 0.05, 2, 0, 71015, 22015, 2, 3)
    ops.uniaxialMaterial('LimitState', 41015, 45.23931245, 8.245e-05, 135.71793734, 0.00024735, 452.39312447, 0.00082449, -45.23931245, -8.245e-05, -135.71793734, -0.00024735, -452.39312447, -0.00082449, 0.4, 0.3, 0.003, 0.0, 0.0, 21015, 2)
    ops.limitCurve('ThreePoint', 11015, 1015, 0.0, 180.95724979, 0.02228988, 180.95724979, 0.06686963, 126.67007485, -2707.1680289, 0.05, 2, 0, 71015, 22015, 1, 3)
    ops.uniaxialMaterial('LimitState', 31015, 45.23931245, 8.245e-05, 135.71793734, 0.00024735, 452.39312447, 0.00082449, -45.23931245, -8.245e-05, -135.71793734, -0.00024735, -452.39312447, -0.00082449, 0.4, 0.3, 0.003, 0.0, 0.0, 11015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1015, 99999, 'P', 41015, 'Vy', 31015, 'Vz', 21015, 'My', 11015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171015, 71015, 171015, 1015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122015, 122015, 22015, 1015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171016, 28.1, 5.1, 3.15)
    ops.node(122016, 28.1, 5.1, 5.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1016, 171016, 122016, 0.1225, 29651021.27614199, 12354592.1983925, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21016, 106.13561354, 0.00115463, 128.46839218, 0.01339762, 12.84683922, 0.0557673, -106.13561354, -0.00115463, -128.46839218, -0.01339762, -12.84683922, -0.0557673, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11016, 91.23306856, 0.00115463, 110.4300926, 0.01339762, 11.04300926, 0.0557673, -91.23306856, -0.00115463, -110.4300926, -0.01339762, -11.04300926, -0.0557673, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21016, 1016, 0.0, 138.00919762, 0.02309253, 138.00919762, 0.06927759, 96.60643833, -1943.70659069, 0.05, 2, 0, 71016, 22016, 2, 3)
    ops.uniaxialMaterial('LimitState', 41016, 34.5022994, 7.933e-05, 103.50689821, 0.000238, 345.02299404, 0.00079335, -34.5022994, -7.933e-05, -103.50689821, -0.000238, -345.02299404, -0.00079335, 0.4, 0.3, 0.003, 0.0, 0.0, 21016, 2)
    ops.limitCurve('ThreePoint', 11016, 1016, 0.0, 138.00919762, 0.02309253, 138.00919762, 0.06927759, 96.60643833, -1943.70659069, 0.05, 2, 0, 71016, 22016, 1, 3)
    ops.uniaxialMaterial('LimitState', 31016, 34.5022994, 7.933e-05, 103.50689821, 0.000238, 345.02299404, 0.00079335, -34.5022994, -7.933e-05, -103.50689821, -0.000238, -345.02299404, -0.00079335, 0.4, 0.3, 0.003, 0.0, 0.0, 11016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1016, 99999, 'P', 41016, 'Vy', 31016, 'Vz', 21016, 'My', 11016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171016, 71016, 171016, 1016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122016, 122016, 22016, 1016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171017, 0.0, 10.2, 3.15)
    ops.node(122017, 0.0, 10.2, 5.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1017, 171017, 122017, 0.1225, 29031822.8264651, 12096592.84436046, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21017, 102.37575712, 0.00116733, 124.07771488, 0.01716793, 12.40777149, 0.05898603, -102.37575712, -0.00116733, -124.07771488, -0.01716793, -12.40777149, -0.05898603, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11017, 88.70043128, 0.00116733, 107.50344742, 0.01716793, 10.75034474, 0.05898603, -88.70043128, -0.00116733, -107.50344742, -0.01716793, -10.75034474, -0.05898603, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21017, 1017, 0.0, 152.48167416, 0.02334667, 152.48167416, 0.07004, 106.73717191, -2706.51339251, 0.05, 2, 0, 71017, 22017, 2, 3)
    ops.uniaxialMaterial('LimitState', 41017, 38.12041854, 8.952e-05, 114.36125562, 0.00026857, 381.2041854, 0.00089524, -38.12041854, -8.952e-05, -114.36125562, -0.00026857, -381.2041854, -0.00089524, 0.4, 0.3, 0.003, 0.0, 0.0, 21017, 2)
    ops.limitCurve('ThreePoint', 11017, 1017, 0.0, 152.48167416, 0.02334667, 152.48167416, 0.07004, 106.73717191, -2706.51339251, 0.05, 2, 0, 71017, 22017, 1, 3)
    ops.uniaxialMaterial('LimitState', 31017, 38.12041854, 8.952e-05, 114.36125562, 0.00026857, 381.2041854, 0.00089524, -38.12041854, -8.952e-05, -114.36125562, -0.00026857, -381.2041854, -0.00089524, 0.4, 0.3, 0.003, 0.0, 0.0, 11017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1017, 99999, 'P', 41017, 'Vy', 31017, 'Vz', 21017, 'My', 11017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171017, 71017, 171017, 1017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122017, 122017, 22017, 1017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171018, 4.2, 10.2, 3.175)
    ops.node(122018, 4.2, 10.2, 5.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1018, 171018, 122018, 0.16, 29072619.35094796, 12113591.39622832, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21018, 164.46407612, 0.00111106, 199.25349209, 0.01711286, 19.92534921, 0.05035882, -164.46407612, -0.00111106, -199.25349209, -0.01711286, -19.92534921, -0.05035882, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11018, 147.47849441, 0.00111106, 178.6749162, 0.01711286, 17.86749162, 0.05035882, -147.47849441, -0.00111106, -178.6749162, -0.01711286, -17.86749162, -0.05035882, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21018, 1018, 0.0, 171.18640606, 0.02222129, 171.18640606, 0.06666387, 119.83048424, -2245.93788357, 0.05, 2, 0, 71018, 22018, 2, 3)
    ops.uniaxialMaterial('LimitState', 41018, 42.79660151, 7.684e-05, 128.38980454, 0.00023052, 427.96601514, 0.00076841, -42.79660151, -7.684e-05, -128.38980454, -0.00023052, -427.96601514, -0.00076841, 0.4, 0.3, 0.003, 0.0, 0.0, 21018, 2)
    ops.limitCurve('ThreePoint', 11018, 1018, 0.0, 171.18640606, 0.02222129, 171.18640606, 0.06666387, 119.83048424, -2245.93788357, 0.05, 2, 0, 71018, 22018, 1, 3)
    ops.uniaxialMaterial('LimitState', 31018, 42.79660151, 7.684e-05, 128.38980454, 0.00023052, 427.96601514, 0.00076841, -42.79660151, -7.684e-05, -128.38980454, -0.00023052, -427.96601514, -0.00076841, 0.4, 0.3, 0.003, 0.0, 0.0, 11018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1018, 99999, 'P', 41018, 'Vy', 31018, 'Vz', 21018, 'My', 11018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171018, 71018, 171018, 1018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122018, 122018, 22018, 1018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171019, 8.4, 10.2, 3.175)
    ops.node(122019, 8.4, 10.2, 5.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1019, 171019, 122019, 0.16, 30722261.99766035, 12800942.49902515, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21019, 164.96555908, 0.00108723, 199.14587491, 0.01688598, 19.91458749, 0.05138296, -164.96555908, -0.00108723, -199.14587491, -0.01688598, -19.91458749, -0.05138296, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11019, 148.15430369, 0.00108723, 178.85138325, 0.01688598, 17.88513832, 0.05138296, -148.15430369, -0.00108723, -178.85138325, -0.01688598, -17.88513832, -0.05138296, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21019, 1019, 0.0, 182.38251916, 0.02174469, 182.38251916, 0.06523406, 127.66776341, -2370.42931829, 0.05, 2, 0, 71019, 22019, 2, 3)
    ops.uniaxialMaterial('LimitState', 41019, 45.59562979, 7.747e-05, 136.78688937, 0.00023241, 455.95629791, 0.00077471, -45.59562979, -7.747e-05, -136.78688937, -0.00023241, -455.95629791, -0.00077471, 0.4, 0.3, 0.003, 0.0, 0.0, 21019, 2)
    ops.limitCurve('ThreePoint', 11019, 1019, 0.0, 182.38251916, 0.02174469, 182.38251916, 0.06523406, 127.66776341, -2370.42931829, 0.05, 2, 0, 71019, 22019, 1, 3)
    ops.uniaxialMaterial('LimitState', 31019, 45.59562979, 7.747e-05, 136.78688937, 0.00023241, 455.95629791, 0.00077471, -45.59562979, -7.747e-05, -136.78688937, -0.00023241, -455.95629791, -0.00077471, 0.4, 0.3, 0.003, 0.0, 0.0, 11019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1019, 99999, 'P', 41019, 'Vy', 31019, 'Vz', 21019, 'My', 11019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171019, 71019, 171019, 1019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122019, 122019, 22019, 1019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171020, 12.6, 10.2, 3.15)
    ops.node(122020, 12.6, 10.2, 5.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1020, 171020, 122020, 0.1225, 29509492.97083487, 12295622.07118119, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21020, 108.09012365, 0.00123553, 130.76610168, 0.01697138, 13.07661017, 0.0581901, -108.09012365, -0.00123553, -130.76610168, -0.01697138, -13.07661017, -0.0581901, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11020, 94.37395491, 0.00123553, 114.1724495, 0.01697138, 11.41724495, 0.0581901, -94.37395491, -0.00123553, -114.1724495, -0.01697138, -11.41724495, -0.0581901, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21020, 1020, 0.0, 153.92827425, 0.02471064, 153.92827425, 0.07413191, 107.74979197, -2508.1791464, 0.05, 2, 0, 71020, 22020, 2, 3)
    ops.uniaxialMaterial('LimitState', 41020, 38.48206856, 8.891e-05, 115.44620568, 0.00026673, 384.82068562, 0.0008891, -38.48206856, -8.891e-05, -115.44620568, -0.00026673, -384.82068562, -0.0008891, 0.4, 0.3, 0.003, 0.0, 0.0, 21020, 2)
    ops.limitCurve('ThreePoint', 11020, 1020, 0.0, 153.92827425, 0.02471064, 153.92827425, 0.07413191, 107.74979197, -2508.1791464, 0.05, 2, 0, 71020, 22020, 1, 3)
    ops.uniaxialMaterial('LimitState', 31020, 38.48206856, 8.891e-05, 115.44620568, 0.00026673, 384.82068562, 0.0008891, -38.48206856, -8.891e-05, -115.44620568, -0.00026673, -384.82068562, -0.0008891, 0.4, 0.3, 0.003, 0.0, 0.0, 11020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1020, 99999, 'P', 41020, 'Vy', 31020, 'Vz', 21020, 'My', 11020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171020, 71020, 171020, 1020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122020, 122020, 22020, 1020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171021, 15.5, 10.2, 3.15)
    ops.node(122021, 15.5, 10.2, 5.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1021, 171021, 122021, 0.1225, 32469025.9492538, 13528760.81218908, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21021, 102.82496682, 0.00109312, 123.4860969, 0.01474501, 12.34860969, 0.05859089, -102.82496682, -0.00109312, -123.4860969, -0.01474501, -12.34860969, -0.05859089, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11021, 90.06051833, 0.00109312, 108.15682453, 0.01474501, 10.81568245, 0.05859089, -90.06051833, -0.00109312, -108.15682453, -0.01474501, -10.81568245, -0.05859089, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21021, 1021, 0.0, 156.83440503, 0.02186244, 156.83440503, 0.06558732, 109.78408352, -2152.97495353, 0.05, 2, 0, 71021, 22021, 2, 3)
    ops.uniaxialMaterial('LimitState', 41021, 39.20860126, 8.233e-05, 117.62580377, 0.00024699, 392.08601258, 0.00082332, -39.20860126, -8.233e-05, -117.62580377, -0.00024699, -392.08601258, -0.00082332, 0.4, 0.3, 0.003, 0.0, 0.0, 21021, 2)
    ops.limitCurve('ThreePoint', 11021, 1021, 0.0, 156.83440503, 0.02186244, 156.83440503, 0.06558732, 109.78408352, -2152.97495353, 0.05, 2, 0, 71021, 22021, 1, 3)
    ops.uniaxialMaterial('LimitState', 31021, 39.20860126, 8.233e-05, 117.62580377, 0.00024699, 392.08601258, 0.00082332, -39.20860126, -8.233e-05, -117.62580377, -0.00024699, -392.08601258, -0.00082332, 0.4, 0.3, 0.003, 0.0, 0.0, 11021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1021, 99999, 'P', 41021, 'Vy', 31021, 'Vz', 21021, 'My', 11021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171021, 71021, 171021, 1021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122021, 122021, 22021, 1021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171022, 19.7, 10.2, 3.175)
    ops.node(122022, 19.7, 10.2, 5.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1022, 171022, 122022, 0.16, 29547896.73788899, 12311623.64078708, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21022, 159.24579471, 0.00111094, 192.75040082, 0.01807717, 19.27504008, 0.0517099, -159.24579471, -0.00111094, -192.75040082, -0.01807717, -19.27504008, -0.0517099, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11022, 143.78769752, 0.00111094, 174.0399888, 0.01807717, 17.40399888, 0.0517099, -143.78769752, -0.00111094, -174.0399888, -0.01807717, -17.40399888, -0.0517099, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21022, 1022, 0.0, 179.11811826, 0.02221877, 179.11811826, 0.0666563, 125.38268278, -2467.10649277, 0.05, 2, 0, 71022, 22022, 2, 3)
    ops.uniaxialMaterial('LimitState', 41022, 44.77952956, 7.911e-05, 134.33858869, 0.00023733, 447.79529564, 0.00079109, -44.77952956, -7.911e-05, -134.33858869, -0.00023733, -447.79529564, -0.00079109, 0.4, 0.3, 0.003, 0.0, 0.0, 21022, 2)
    ops.limitCurve('ThreePoint', 11022, 1022, 0.0, 179.11811826, 0.02221877, 179.11811826, 0.0666563, 125.38268278, -2467.10649277, 0.05, 2, 0, 71022, 22022, 1, 3)
    ops.uniaxialMaterial('LimitState', 31022, 44.77952956, 7.911e-05, 134.33858869, 0.00023733, 447.79529564, 0.00079109, -44.77952956, -7.911e-05, -134.33858869, -0.00023733, -447.79529564, -0.00079109, 0.4, 0.3, 0.003, 0.0, 0.0, 11022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1022, 99999, 'P', 41022, 'Vy', 31022, 'Vz', 21022, 'My', 11022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171022, 71022, 171022, 1022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122022, 122022, 22022, 1022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171023, 23.9, 10.2, 3.175)
    ops.node(122023, 23.9, 10.2, 5.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1023, 171023, 122023, 0.16, 27001247.05718, 11250519.60715833, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21023, 165.3233431, 0.00115825, 200.92750632, 0.01456656, 20.09275063, 0.04583216, -165.3233431, -0.00115825, -200.92750632, -0.01456656, -20.09275063, -0.04583216, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11023, 147.86282996, 0.00115825, 179.70668355, 0.01456656, 17.97066835, 0.04583216, -147.86282996, -0.00115825, -179.70668355, -0.01456656, -17.97066835, -0.04583216, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21023, 1023, 0.0, 155.0867252, 0.02316496, 155.0867252, 0.06949489, 108.56070764, -2006.42650331, 0.05, 2, 0, 71023, 22023, 2, 3)
    ops.uniaxialMaterial('LimitState', 41023, 38.7716813, 7.496e-05, 116.3150439, 0.00022487, 387.71681301, 0.00074955, -38.7716813, -7.496e-05, -116.3150439, -0.00022487, -387.71681301, -0.00074955, 0.4, 0.3, 0.003, 0.0, 0.0, 21023, 2)
    ops.limitCurve('ThreePoint', 11023, 1023, 0.0, 155.0867252, 0.02316496, 155.0867252, 0.06949489, 108.56070764, -2006.42650331, 0.05, 2, 0, 71023, 22023, 1, 3)
    ops.uniaxialMaterial('LimitState', 31023, 38.7716813, 7.496e-05, 116.3150439, 0.00022487, 387.71681301, 0.00074955, -38.7716813, -7.496e-05, -116.3150439, -0.00022487, -387.71681301, -0.00074955, 0.4, 0.3, 0.003, 0.0, 0.0, 11023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1023, 99999, 'P', 41023, 'Vy', 31023, 'Vz', 21023, 'My', 11023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171023, 71023, 171023, 1023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122023, 122023, 22023, 1023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171024, 28.1, 10.2, 3.15)
    ops.node(122024, 28.1, 10.2, 5.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1024, 171024, 122024, 0.1225, 28756295.38523661, 11981789.74384859, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21024, 103.58057674, 0.0011473, 125.60247941, 0.01527964, 12.56024794, 0.05681233, -103.58057674, -0.0011473, -125.60247941, -0.01527964, -12.56024794, -0.05681233, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11024, 89.13928939, 0.0011473, 108.09088068, 0.01527964, 10.80908807, 0.05681233, -89.13928939, -0.0011473, -108.09088068, -0.01527964, -10.80908807, -0.05681233, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21024, 1024, 0.0, 141.3306511, 0.02294601, 141.3306511, 0.06883802, 98.93145577, -2233.19854809, 0.05, 2, 0, 71024, 22024, 2, 3)
    ops.uniaxialMaterial('LimitState', 41024, 35.33266277, 8.377e-05, 105.99798832, 0.00025132, 353.32662774, 0.00083772, -35.33266277, -8.377e-05, -105.99798832, -0.00025132, -353.32662774, -0.00083772, 0.4, 0.3, 0.003, 0.0, 0.0, 21024, 2)
    ops.limitCurve('ThreePoint', 11024, 1024, 0.0, 141.3306511, 0.02294601, 141.3306511, 0.06883802, 98.93145577, -2233.19854809, 0.05, 2, 0, 71024, 22024, 1, 3)
    ops.uniaxialMaterial('LimitState', 31024, 35.33266277, 8.377e-05, 105.99798832, 0.00025132, 353.32662774, 0.00083772, -35.33266277, -8.377e-05, -105.99798832, -0.00025132, -353.32662774, -0.00083772, 0.4, 0.3, 0.003, 0.0, 0.0, 11024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1024, 99999, 'P', 41024, 'Vy', 31024, 'Vz', 21024, 'My', 11024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171024, 71024, 171024, 1024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122024, 122024, 22024, 1024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171025, 0.0, 15.3, 3.15)
    ops.node(122025, 0.0, 15.3, 5.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1025, 171025, 122025, 0.09, 31241751.10258349, 13017396.29274312, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21025, 61.30514421, 0.0013291, 74.0099097, 0.01738442, 7.40099097, 0.06821318, -61.30514421, -0.0013291, -74.0099097, -0.01738442, -7.40099097, -0.06821318, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11025, 56.19006222, 0.0013291, 67.83478751, 0.01738442, 6.78347875, 0.06821318, -56.19006222, -0.0013291, -67.83478751, -0.01738442, -6.78347875, -0.06821318, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21025, 1025, 0.0, 120.73861779, 0.02658209, 120.73861779, 0.07974627, 84.51703245, -2463.41734386, 0.05, 2, 0, 71025, 22025, 2, 3)
    ops.uniaxialMaterial('LimitState', 41025, 30.18465445, 8.966e-05, 90.55396334, 0.00026898, 301.84654448, 0.0008966, -30.18465445, -8.966e-05, -90.55396334, -0.00026898, -301.84654448, -0.0008966, 0.4, 0.3, 0.003, 0.0, 0.0, 21025, 2)
    ops.limitCurve('ThreePoint', 11025, 1025, 0.0, 120.73861779, 0.02658209, 120.73861779, 0.07974627, 84.51703245, -2463.41734386, 0.05, 2, 0, 71025, 22025, 1, 3)
    ops.uniaxialMaterial('LimitState', 31025, 30.18465445, 8.966e-05, 90.55396334, 0.00026898, 301.84654448, 0.0008966, -30.18465445, -8.966e-05, -90.55396334, -0.00026898, -301.84654448, -0.0008966, 0.4, 0.3, 0.003, 0.0, 0.0, 11025, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1025, 99999, 'P', 41025, 'Vy', 31025, 'Vz', 21025, 'My', 11025, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171025, 71025, 171025, 1025, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122025, 122025, 22025, 1025, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171026, 4.2, 15.3, 3.175)
    ops.node(122026, 4.2, 15.3, 5.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1026, 171026, 122026, 0.1225, 28937022.7861094, 12057092.82754558, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21026, 89.50936189, 0.0011593, 108.54478497, 0.01393057, 10.8544785, 0.05612897, -89.50936189, -0.0011593, -108.54478497, -0.01393057, -10.8544785, -0.05612897, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11026, 104.44546701, 0.0011593, 126.65726264, 0.01393057, 12.66572626, 0.05612897, -104.44546701, -0.0011593, -126.65726264, -0.01393057, -12.66572626, -0.05612897, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21026, 1026, 0.0, 139.3320287, 0.02318601, 139.3320287, 0.06955804, 97.53242009, -2183.87549765, 0.05, 2, 0, 71026, 22026, 2, 3)
    ops.uniaxialMaterial('LimitState', 41026, 34.83300718, 8.207e-05, 104.49902153, 0.00024621, 348.33007176, 0.00082071, -34.83300718, -8.207e-05, -104.49902153, -0.00024621, -348.33007176, -0.00082071, 0.4, 0.3, 0.003, 0.0, 0.0, 21026, 2)
    ops.limitCurve('ThreePoint', 11026, 1026, 0.0, 139.3320287, 0.02318601, 139.3320287, 0.06955804, 97.53242009, -2183.87549765, 0.05, 2, 0, 71026, 22026, 1, 3)
    ops.uniaxialMaterial('LimitState', 31026, 34.83300718, 8.207e-05, 104.49902153, 0.00024621, 348.33007176, 0.00082071, -34.83300718, -8.207e-05, -104.49902153, -0.00024621, -348.33007176, -0.00082071, 0.4, 0.3, 0.003, 0.0, 0.0, 11026, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1026, 99999, 'P', 41026, 'Vy', 31026, 'Vz', 21026, 'My', 11026, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171026, 71026, 171026, 1026, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122026, 122026, 22026, 1026, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171027, 8.4, 15.3, 3.175)
    ops.node(122027, 8.4, 15.3, 5.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1027, 171027, 122027, 0.1225, 26152220.18426416, 10896758.41011007, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21027, 86.5663641, 0.00127929, 105.39670918, 0.01428465, 10.53967092, 0.05318305, -86.5663641, -0.00127929, -105.39670918, -0.01428465, -10.53967092, -0.05318305, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11027, 99.30919595, 0.00127929, 120.91142504, 0.01428465, 12.0911425, 0.05318305, -99.30919595, -0.00127929, -120.91142504, -0.01428465, -12.0911425, -0.05318305, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21027, 1027, 0.0, 127.59701665, 0.02558572, 127.59701665, 0.07675717, 89.31791166, -2096.62264189, 0.05, 2, 0, 71027, 22027, 2, 3)
    ops.uniaxialMaterial('LimitState', 41027, 31.89925416, 8.316e-05, 95.69776249, 0.00024949, 318.99254163, 0.00083162, -31.89925416, -8.316e-05, -95.69776249, -0.00024949, -318.99254163, -0.00083162, 0.4, 0.3, 0.003, 0.0, 0.0, 21027, 2)
    ops.limitCurve('ThreePoint', 11027, 1027, 0.0, 127.59701665, 0.02558572, 127.59701665, 0.07675717, 89.31791166, -2096.62264189, 0.05, 2, 0, 71027, 22027, 1, 3)
    ops.uniaxialMaterial('LimitState', 31027, 31.89925416, 8.316e-05, 95.69776249, 0.00024949, 318.99254163, 0.00083162, -31.89925416, -8.316e-05, -95.69776249, -0.00024949, -318.99254163, -0.00083162, 0.4, 0.3, 0.003, 0.0, 0.0, 11027, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1027, 99999, 'P', 41027, 'Vy', 31027, 'Vz', 21027, 'My', 11027, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171027, 71027, 171027, 1027, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122027, 122027, 22027, 1027, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171028, 12.6, 15.3, 3.15)
    ops.node(122028, 12.6, 15.3, 5.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1028, 171028, 122028, 0.09, 28172494.4326057, 11738539.34691904, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21028, 58.9022944, 0.00142363, 71.45133132, 0.01595166, 7.14513313, 0.06099994, -58.9022944, -0.00142363, -71.45133132, -0.01595166, -7.14513313, -0.06099994, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11028, 63.69567951, 0.00142363, 77.26593925, 0.01595166, 7.72659392, 0.06099994, -63.69567951, -0.00142363, -77.26593925, -0.01595166, -7.72659392, -0.06099994, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21028, 1028, 0.0, 110.54212975, 0.02847252, 110.54212975, 0.08541756, 77.37949083, -1934.87664114, 0.05, 2, 0, 71028, 22028, 2, 3)
    ops.uniaxialMaterial('LimitState', 41028, 27.63553244, 9.103e-05, 82.90659731, 0.00027309, 276.35532438, 0.00091031, -27.63553244, -9.103e-05, -82.90659731, -0.00027309, -276.35532438, -0.00091031, 0.4, 0.3, 0.003, 0.0, 0.0, 21028, 2)
    ops.limitCurve('ThreePoint', 11028, 1028, 0.0, 110.54212975, 0.02847252, 110.54212975, 0.08541756, 77.37949083, -1934.87664114, 0.05, 2, 0, 71028, 22028, 1, 3)
    ops.uniaxialMaterial('LimitState', 31028, 27.63553244, 9.103e-05, 82.90659731, 0.00027309, 276.35532438, 0.00091031, -27.63553244, -9.103e-05, -82.90659731, -0.00027309, -276.35532438, -0.00091031, 0.4, 0.3, 0.003, 0.0, 0.0, 11028, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1028, 99999, 'P', 41028, 'Vy', 31028, 'Vz', 21028, 'My', 11028, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171028, 71028, 171028, 1028, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122028, 122028, 22028, 1028, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171029, 15.5, 15.3, 3.15)
    ops.node(122029, 15.5, 15.3, 5.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1029, 171029, 122029, 0.09, 26829606.16751771, 11179002.56979905, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21029, 60.46593254, 0.00141629, 73.4749701, 0.01856335, 7.34749701, 0.06163798, -60.46593254, -0.00141629, -73.4749701, -0.01856335, -7.34749701, -0.06163798, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11029, 66.09797814, 0.00141629, 80.31873096, 0.01856335, 8.0318731, 0.06163798, -66.09797814, -0.00141629, -80.31873096, -0.01856335, -8.0318731, -0.06163798, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21029, 1029, 0.0, 118.92051482, 0.02832586, 118.92051482, 0.08497759, 83.24436037, -2523.84301458, 0.05, 2, 0, 71029, 22029, 2, 3)
    ops.uniaxialMaterial('LimitState', 41029, 29.73012871, 0.00010283, 89.19038612, 0.0003085, 297.30128705, 0.00102833, -29.73012871, -0.00010283, -89.19038612, -0.0003085, -297.30128705, -0.00102833, 0.4, 0.3, 0.003, 0.0, 0.0, 21029, 2)
    ops.limitCurve('ThreePoint', 11029, 1029, 0.0, 118.92051482, 0.02832586, 118.92051482, 0.08497759, 83.24436037, -2523.84301458, 0.05, 2, 0, 71029, 22029, 1, 3)
    ops.uniaxialMaterial('LimitState', 31029, 29.73012871, 0.00010283, 89.19038612, 0.0003085, 297.30128705, 0.00102833, -29.73012871, -0.00010283, -89.19038612, -0.0003085, -297.30128705, -0.00102833, 0.4, 0.3, 0.003, 0.0, 0.0, 11029, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1029, 99999, 'P', 41029, 'Vy', 31029, 'Vz', 21029, 'My', 11029, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171029, 71029, 171029, 1029, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122029, 122029, 22029, 1029, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171030, 19.7, 15.3, 3.175)
    ops.node(122030, 19.7, 15.3, 5.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1030, 171030, 122030, 0.1225, 34109029.68749252, 14212095.70312188, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21030, 90.37748363, 0.00113936, 108.04224847, 0.01266693, 10.80422485, 0.0586392, -90.37748363, -0.00113936, -108.04224847, -0.01266693, -10.80422485, -0.0586392, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11030, 103.77475847, 0.00113936, 124.05809267, 0.01266693, 12.40580927, 0.0586392, -103.77475847, -0.00113936, -124.05809267, -0.01266693, -12.40580927, -0.0586392, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21030, 1030, 0.0, 155.59715594, 0.02278725, 155.59715594, 0.06836175, 108.91800916, -2031.9460535, 0.05, 2, 0, 71030, 22030, 2, 3)
    ops.uniaxialMaterial('LimitState', 41030, 38.89928899, 7.775e-05, 116.69786696, 0.00023326, 388.99288986, 0.00077755, -38.89928899, -7.775e-05, -116.69786696, -0.00023326, -388.99288986, -0.00077755, 0.4, 0.3, 0.003, 0.0, 0.0, 21030, 2)
    ops.limitCurve('ThreePoint', 11030, 1030, 0.0, 155.59715594, 0.02278725, 155.59715594, 0.06836175, 108.91800916, -2031.9460535, 0.05, 2, 0, 71030, 22030, 1, 3)
    ops.uniaxialMaterial('LimitState', 31030, 38.89928899, 7.775e-05, 116.69786696, 0.00023326, 388.99288986, 0.00077755, -38.89928899, -7.775e-05, -116.69786696, -0.00023326, -388.99288986, -0.00077755, 0.4, 0.3, 0.003, 0.0, 0.0, 11030, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1030, 99999, 'P', 41030, 'Vy', 31030, 'Vz', 21030, 'My', 11030, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171030, 71030, 171030, 1030, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122030, 122030, 22030, 1030, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171031, 23.9, 15.3, 3.175)
    ops.node(122031, 23.9, 15.3, 5.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1031, 171031, 122031, 0.1225, 32875036.15571297, 13697931.73154707, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21031, 91.0791522, 0.00113544, 109.33796717, 0.0142943, 10.93379672, 0.05956699, -91.0791522, -0.00113544, -109.33796717, -0.0142943, -10.93379672, -0.05956699, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11031, 105.4656945, 0.00113544, 126.60860761, 0.0142943, 12.66086076, 0.05956699, -105.4656945, -0.00113544, -126.60860761, -0.0142943, -12.66086076, -0.05956699, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21031, 1031, 0.0, 154.08638599, 0.02270875, 154.08638599, 0.06812625, 107.8604702, -2181.05137563, 0.05, 2, 0, 71031, 22031, 2, 3)
    ops.uniaxialMaterial('LimitState', 41031, 38.5215965, 7.989e-05, 115.5647895, 0.00023967, 385.21596499, 0.0007989, -38.5215965, -7.989e-05, -115.5647895, -0.00023967, -385.21596499, -0.0007989, 0.4, 0.3, 0.003, 0.0, 0.0, 21031, 2)
    ops.limitCurve('ThreePoint', 11031, 1031, 0.0, 154.08638599, 0.02270875, 154.08638599, 0.06812625, 107.8604702, -2181.05137563, 0.05, 2, 0, 71031, 22031, 1, 3)
    ops.uniaxialMaterial('LimitState', 31031, 38.5215965, 7.989e-05, 115.5647895, 0.00023967, 385.21596499, 0.0007989, -38.5215965, -7.989e-05, -115.5647895, -0.00023967, -385.21596499, -0.0007989, 0.4, 0.3, 0.003, 0.0, 0.0, 11031, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1031, 99999, 'P', 41031, 'Vy', 31031, 'Vz', 21031, 'My', 11031, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171031, 71031, 171031, 1031, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122031, 122031, 22031, 1031, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171032, 28.1, 15.3, 3.15)
    ops.node(122032, 28.1, 15.3, 5.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1032, 171032, 122032, 0.09, 30873640.36597519, 12864016.81915633, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21032, 61.62814405, 0.00132008, 74.47403555, 0.01470053, 7.44740356, 0.06525827, -61.62814405, -0.00132008, -74.47403555, -0.01470053, -7.44740356, -0.06525827, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11032, 56.34356144, 0.00132008, 68.08792416, 0.01470053, 6.80879242, 0.06525827, -56.34356144, -0.00132008, -68.08792416, -0.01470053, -6.80879242, -0.06525827, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21032, 1032, 0.0, 113.53745223, 0.02640162, 113.53745223, 0.07920487, 79.47621656, -2101.46623119, 0.05, 2, 0, 71032, 22032, 2, 3)
    ops.uniaxialMaterial('LimitState', 41032, 28.38436306, 8.532e-05, 85.15308917, 0.00025595, 283.84363058, 0.00085318, -28.38436306, -8.532e-05, -85.15308917, -0.00025595, -283.84363058, -0.00085318, 0.4, 0.3, 0.003, 0.0, 0.0, 21032, 2)
    ops.limitCurve('ThreePoint', 11032, 1032, 0.0, 113.53745223, 0.02640162, 113.53745223, 0.07920487, 79.47621656, -2101.46623119, 0.05, 2, 0, 71032, 22032, 1, 3)
    ops.uniaxialMaterial('LimitState', 31032, 28.38436306, 8.532e-05, 85.15308917, 0.00025595, 283.84363058, 0.00085318, -28.38436306, -8.532e-05, -85.15308917, -0.00025595, -283.84363058, -0.00085318, 0.4, 0.3, 0.003, 0.0, 0.0, 11032, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1032, 99999, 'P', 41032, 'Vy', 31032, 'Vz', 21032, 'My', 11032, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171032, 71032, 171032, 1032, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122032, 122032, 22032, 1032, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172001, 0.0, 0.0, 6.05)
    ops.node(123001, 0.0, 0.0, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2001, 172001, 123001, 0.0625, 29809683.56008601, 12420701.48336917, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22001, 34.71792461, 0.00152164, 42.09423812, 0.01962255, 4.20942381, 0.07811697, -34.71792461, -0.00152164, -42.09423812, -0.01962255, -4.20942381, -0.07811697, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12001, 34.71792461, 0.00152164, 42.09423812, 0.01962255, 4.20942381, 0.07811697, -34.71792461, -0.00152164, -42.09423812, -0.01962255, -4.20942381, -0.07811697, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22001, 2001, 0.0, 90.66631654, 0.03043286, 90.66631654, 0.09129857, 63.46642158, -2600.96511045, 0.05, 2, 0, 72001, 23001, 2, 3)
    ops.uniaxialMaterial('LimitState', 42001, 22.66657914, 0.00010161, 67.99973741, 0.00030483, 226.66579136, 0.00101611, -22.66657914, -0.00010161, -67.99973741, -0.00030483, -226.66579136, -0.00101611, 0.4, 0.3, 0.003, 0.0, 0.0, 22001, 2)
    ops.limitCurve('ThreePoint', 12001, 2001, 0.0, 90.66631654, 0.03043286, 90.66631654, 0.09129857, 63.46642158, -2600.96511045, 0.05, 2, 0, 72001, 23001, 1, 3)
    ops.uniaxialMaterial('LimitState', 32001, 22.66657914, 0.00010161, 67.99973741, 0.00030483, 226.66579136, 0.00101611, -22.66657914, -0.00010161, -67.99973741, -0.00030483, -226.66579136, -0.00101611, 0.4, 0.3, 0.003, 0.0, 0.0, 12001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2001, 99999, 'P', 42001, 'Vy', 32001, 'Vz', 22001, 'My', 12001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172001, 72001, 172001, 2001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123001, 123001, 23001, 2001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172002, 4.2, 0.0, 6.075)
    ops.node(123002, 4.2, 0.0, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2002, 172002, 123002, 0.0625, 30651788.08610618, 12771578.36921091, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22002, 36.40305575, 0.00147602, 43.92866926, 0.02009121, 4.39286693, 0.07484979, -36.40305575, -0.00147602, -43.92866926, -0.02009121, -4.39286693, -0.07484979, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12002, 36.40305575, 0.00147602, 43.92866926, 0.02009121, 4.39286693, 0.07484979, -36.40305575, -0.00147602, -43.92866926, -0.02009121, -4.39286693, -0.07484979, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22002, 2002, 0.0, 97.30395583, 0.02952031, 97.30395583, 0.08856092, 68.11276908, -2110.5124476, 0.05, 2, 0, 72002, 23002, 2, 3)
    ops.uniaxialMaterial('LimitState', 42002, 24.32598896, 0.00010605, 72.97796687, 0.00031816, 243.25988958, 0.00106054, -24.32598896, -0.00010605, -72.97796687, -0.00031816, -243.25988958, -0.00106054, 0.4, 0.3, 0.003, 0.0, 0.0, 22002, 2)
    ops.limitCurve('ThreePoint', 12002, 2002, 0.0, 97.30395583, 0.02952031, 97.30395583, 0.08856092, 68.11276908, -2110.5124476, 0.05, 2, 0, 72002, 23002, 1, 3)
    ops.uniaxialMaterial('LimitState', 32002, 24.32598896, 0.00010605, 72.97796687, 0.00031816, 243.25988958, 0.00106054, -24.32598896, -0.00010605, -72.97796687, -0.00031816, -243.25988958, -0.00106054, 0.4, 0.3, 0.003, 0.0, 0.0, 12002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2002, 99999, 'P', 42002, 'Vy', 32002, 'Vz', 22002, 'My', 12002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172002, 72002, 172002, 2002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123002, 123002, 23002, 2002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172003, 8.4, 0.0, 6.075)
    ops.node(123003, 8.4, 0.0, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2003, 172003, 123003, 0.0625, 27713405.78159033, 11547252.40899597, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22003, 36.26284621, 0.00161235, 43.99805693, 0.01870773, 4.39980569, 0.06924542, -36.26284621, -0.00161235, -43.99805693, -0.01870773, -4.39980569, -0.06924542, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12003, 36.26284621, 0.00161235, 43.99805693, 0.01870773, 4.39980569, 0.06924542, -36.26284621, -0.00161235, -43.99805693, -0.01870773, -4.39980569, -0.06924542, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22003, 2003, 0.0, 89.88097353, 0.03224694, 89.88097353, 0.09674083, 62.91668147, -2002.6629972, 0.05, 2, 0, 72003, 23003, 2, 3)
    ops.uniaxialMaterial('LimitState', 42003, 22.47024338, 0.00010835, 67.41073015, 0.00032505, 224.70243382, 0.0010835, -22.47024338, -0.00010835, -67.41073015, -0.00032505, -224.70243382, -0.0010835, 0.4, 0.3, 0.003, 0.0, 0.0, 22003, 2)
    ops.limitCurve('ThreePoint', 12003, 2003, 0.0, 89.88097353, 0.03224694, 89.88097353, 0.09674083, 62.91668147, -2002.6629972, 0.05, 2, 0, 72003, 23003, 1, 3)
    ops.uniaxialMaterial('LimitState', 32003, 22.47024338, 0.00010835, 67.41073015, 0.00032505, 224.70243382, 0.0010835, -22.47024338, -0.00010835, -67.41073015, -0.00032505, -224.70243382, -0.0010835, 0.4, 0.3, 0.003, 0.0, 0.0, 12003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2003, 99999, 'P', 42003, 'Vy', 32003, 'Vz', 22003, 'My', 12003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172003, 72003, 172003, 2003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123003, 123003, 23003, 2003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172006, 19.7, 0.0, 6.075)
    ops.node(123006, 19.7, 0.0, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2006, 172006, 123006, 0.0625, 28408137.80361635, 11836724.08484015, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22006, 37.35764619, 0.00166989, 45.28087977, 0.01595755, 4.52808798, 0.06763341, -37.35764619, -0.00166989, -45.28087977, -0.01595755, -4.52808798, -0.06763341, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12006, 37.35764619, 0.00166989, 45.28087977, 0.01595755, 4.52808798, 0.06763341, -37.35764619, -0.00166989, -45.28087977, -0.01595755, -4.52808798, -0.06763341, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22006, 2006, 0.0, 77.73741691, 0.03339788, 77.73741691, 0.10019363, 54.41619184, -1500.2933265, 0.05, 2, 0, 72006, 23006, 2, 3)
    ops.uniaxialMaterial('LimitState', 42006, 19.43435423, 9.142e-05, 58.30306268, 0.00027426, 194.34354227, 0.00091419, -19.43435423, -9.142e-05, -58.30306268, -0.00027426, -194.34354227, -0.00091419, 0.4, 0.3, 0.003, 0.0, 0.0, 22006, 2)
    ops.limitCurve('ThreePoint', 12006, 2006, 0.0, 77.73741691, 0.03339788, 77.73741691, 0.10019363, 54.41619184, -1500.2933265, 0.05, 2, 0, 72006, 23006, 1, 3)
    ops.uniaxialMaterial('LimitState', 32006, 19.43435423, 9.142e-05, 58.30306268, 0.00027426, 194.34354227, 0.00091419, -19.43435423, -9.142e-05, -58.30306268, -0.00027426, -194.34354227, -0.00091419, 0.4, 0.3, 0.003, 0.0, 0.0, 12006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2006, 99999, 'P', 42006, 'Vy', 32006, 'Vz', 22006, 'My', 12006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172006, 72006, 172006, 2006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123006, 123006, 23006, 2006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172007, 23.9, 0.0, 6.075)
    ops.node(123007, 23.9, 0.0, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2007, 172007, 123007, 0.0625, 29458187.76720933, 12274244.90300389, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22007, 35.07300904, 0.00176114, 42.43293782, 0.01605146, 4.24329378, 0.06927445, -35.07300904, -0.00176114, -42.43293782, -0.01605146, -4.24329378, -0.06927445, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12007, 35.07300904, 0.00176114, 42.43293782, 0.01605146, 4.24329378, 0.06927445, -35.07300904, -0.00176114, -42.43293782, -0.01605146, -4.24329378, -0.06927445, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22007, 2007, 0.0, 81.67029741, 0.03522288, 81.67029741, 0.10566865, 57.16920819, -1679.68053333, 0.05, 2, 0, 72007, 23007, 2, 3)
    ops.uniaxialMaterial('LimitState', 42007, 20.41757435, 9.262e-05, 61.25272306, 0.00027786, 204.17574352, 0.00092621, -20.41757435, -9.262e-05, -61.25272306, -0.00027786, -204.17574352, -0.00092621, 0.4, 0.3, 0.003, 0.0, 0.0, 22007, 2)
    ops.limitCurve('ThreePoint', 12007, 2007, 0.0, 81.67029741, 0.03522288, 81.67029741, 0.10566865, 57.16920819, -1679.68053333, 0.05, 2, 0, 72007, 23007, 1, 3)
    ops.uniaxialMaterial('LimitState', 32007, 20.41757435, 9.262e-05, 61.25272306, 0.00027786, 204.17574352, 0.00092621, -20.41757435, -9.262e-05, -61.25272306, -0.00027786, -204.17574352, -0.00092621, 0.4, 0.3, 0.003, 0.0, 0.0, 12007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2007, 99999, 'P', 42007, 'Vy', 32007, 'Vz', 22007, 'My', 12007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172007, 72007, 172007, 2007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123007, 123007, 23007, 2007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172008, 28.1, 0.0, 6.05)
    ops.node(123008, 28.1, 0.0, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2008, 172008, 123008, 0.0625, 28711573.28921484, 11963155.53717285, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22008, 30.19325362, 0.00183158, 36.69803373, 0.01664262, 3.66980337, 0.07409456, -30.19325362, -0.00183158, -36.69803373, -0.01664262, -3.66980337, -0.07409456, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12008, 30.19325362, 0.00183158, 36.69803373, 0.01664262, 3.66980337, 0.07409456, -30.19325362, -0.00183158, -36.69803373, -0.01664262, -3.66980337, -0.07409456, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22008, 2008, 0.0, 71.38869277, 0.03663164, 71.38869277, 0.10989492, 49.97208494, -1835.96906782, 0.05, 2, 0, 72008, 23008, 2, 3)
    ops.uniaxialMaterial('LimitState', 42008, 17.84717319, 8.307e-05, 53.54151958, 0.0002492, 178.47173194, 0.00083066, -17.84717319, -8.307e-05, -53.54151958, -0.0002492, -178.47173194, -0.00083066, 0.4, 0.3, 0.003, 0.0, 0.0, 22008, 2)
    ops.limitCurve('ThreePoint', 12008, 2008, 0.0, 71.38869277, 0.03663164, 71.38869277, 0.10989492, 49.97208494, -1835.96906782, 0.05, 2, 0, 72008, 23008, 1, 3)
    ops.uniaxialMaterial('LimitState', 32008, 17.84717319, 8.307e-05, 53.54151958, 0.0002492, 178.47173194, 0.00083066, -17.84717319, -8.307e-05, -53.54151958, -0.0002492, -178.47173194, -0.00083066, 0.4, 0.3, 0.003, 0.0, 0.0, 12008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2008, 99999, 'P', 42008, 'Vy', 32008, 'Vz', 22008, 'My', 12008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172008, 72008, 172008, 2008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123008, 123008, 23008, 2008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172009, 0.0, 5.1, 6.05)
    ops.node(123009, 0.0, 5.1, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2009, 172009, 123009, 0.0625, 26524091.41939091, 11051704.75807955, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22009, 38.29754789, 0.00165918, 46.49698342, 0.01792897, 4.64969834, 0.06537218, -38.29754789, -0.00165918, -46.49698342, -0.01792897, -4.64969834, -0.06537218, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12009, 38.29754789, 0.00165918, 46.49698342, 0.01792897, 4.64969834, 0.06537218, -38.29754789, -0.00165918, -46.49698342, -0.01792897, -4.64969834, -0.06537218, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22009, 2009, 0.0, 84.13786411, 0.03318352, 84.13786411, 0.09955056, 58.89650488, -1746.70515608, 0.05, 2, 0, 72009, 23009, 2, 3)
    ops.uniaxialMaterial('LimitState', 42009, 21.03446603, 0.00010597, 63.10339808, 0.00031792, 210.34466027, 0.00105975, -21.03446603, -0.00010597, -63.10339808, -0.00031792, -210.34466027, -0.00105975, 0.4, 0.3, 0.003, 0.0, 0.0, 22009, 2)
    ops.limitCurve('ThreePoint', 12009, 2009, 0.0, 84.13786411, 0.03318352, 84.13786411, 0.09955056, 58.89650488, -1746.70515608, 0.05, 2, 0, 72009, 23009, 1, 3)
    ops.uniaxialMaterial('LimitState', 32009, 21.03446603, 0.00010597, 63.10339808, 0.00031792, 210.34466027, 0.00105975, -21.03446603, -0.00010597, -63.10339808, -0.00031792, -210.34466027, -0.00105975, 0.4, 0.3, 0.003, 0.0, 0.0, 12009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2009, 99999, 'P', 42009, 'Vy', 32009, 'Vz', 22009, 'My', 12009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172009, 72009, 172009, 2009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123009, 123009, 23009, 2009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172010, 4.2, 5.1, 6.075)
    ops.node(123010, 4.2, 5.1, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2010, 172010, 123010, 0.1225, 33340524.8414375, 13891885.35059896, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22010, 87.20039087, 0.00108977, 104.5608299, 0.01365256, 10.45608299, 0.05970346, -87.20039087, -0.00108977, -104.5608299, -0.01365256, -10.45608299, -0.05970346, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12010, 101.22516777, 0.00108977, 121.3777535, 0.01365256, 12.13777535, 0.05970346, -101.22516777, -0.00108977, -121.3777535, -0.01365256, -12.13777535, -0.05970346, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22010, 2010, 0.0, 155.80199498, 0.02179541, 155.80199498, 0.06538622, 109.06139649, -2299.41927406, 0.05, 2, 0, 72010, 23010, 2, 3)
    ops.uniaxialMaterial('LimitState', 42010, 38.95049875, 7.965e-05, 116.85149624, 0.00023896, 389.50498745, 0.00079652, -38.95049875, -7.965e-05, -116.85149624, -0.00023896, -389.50498745, -0.00079652, 0.4, 0.3, 0.003, 0.0, 0.0, 22010, 2)
    ops.limitCurve('ThreePoint', 12010, 2010, 0.0, 155.80199498, 0.02179541, 155.80199498, 0.06538622, 109.06139649, -2299.41927406, 0.05, 2, 0, 72010, 23010, 1, 3)
    ops.uniaxialMaterial('LimitState', 32010, 38.95049875, 7.965e-05, 116.85149624, 0.00023896, 389.50498745, 0.00079652, -38.95049875, -7.965e-05, -116.85149624, -0.00023896, -389.50498745, -0.00079652, 0.4, 0.3, 0.003, 0.0, 0.0, 12010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2010, 99999, 'P', 42010, 'Vy', 32010, 'Vz', 22010, 'My', 12010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172010, 72010, 172010, 2010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123010, 123010, 23010, 2010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172011, 8.4, 5.1, 6.075)
    ops.node(123011, 8.4, 5.1, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2011, 172011, 123011, 0.1225, 29093011.75661206, 12122088.23192169, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22011, 89.70863584, 0.00118372, 108.8163917, 0.01718124, 10.88163917, 0.06027006, -89.70863584, -0.00118372, -108.8163917, -0.01718124, -10.88163917, -0.06027006, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12011, 105.16430004, 0.00118372, 127.56408074, 0.01718124, 12.75640807, 0.06027006, -105.16430004, -0.00118372, -127.56408074, -0.01718124, -12.75640807, -0.06027006, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22011, 2011, 0.0, 148.82101362, 0.0236744, 148.82101362, 0.07102321, 104.17470953, -2758.54235444, 0.05, 2, 0, 72011, 23011, 2, 3)
    ops.uniaxialMaterial('LimitState', 42011, 37.2052534, 8.719e-05, 111.61576021, 0.00026157, 372.05253405, 0.00087191, -37.2052534, -8.719e-05, -111.61576021, -0.00026157, -372.05253405, -0.00087191, 0.4, 0.3, 0.003, 0.0, 0.0, 22011, 2)
    ops.limitCurve('ThreePoint', 12011, 2011, 0.0, 148.82101362, 0.0236744, 148.82101362, 0.07102321, 104.17470953, -2758.54235444, 0.05, 2, 0, 72011, 23011, 1, 3)
    ops.uniaxialMaterial('LimitState', 32011, 37.2052534, 8.719e-05, 111.61576021, 0.00026157, 372.05253405, 0.00087191, -37.2052534, -8.719e-05, -111.61576021, -0.00026157, -372.05253405, -0.00087191, 0.4, 0.3, 0.003, 0.0, 0.0, 12011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2011, 99999, 'P', 42011, 'Vy', 32011, 'Vz', 22011, 'My', 12011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172011, 72011, 172011, 2011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123011, 123011, 23011, 2011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172012, 12.6, 5.1, 6.05)
    ops.node(123012, 12.6, 5.1, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2012, 172012, 123012, 0.1225, 29369354.30670407, 12237230.96112669, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22012, 100.9543606, 0.00115234, 122.3707619, 0.0155345, 12.23707619, 0.05869839, -100.9543606, -0.00115234, -122.3707619, -0.0155345, -12.23707619, -0.05869839, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12012, 86.83059451, 0.00115234, 105.25078801, 0.0155345, 10.5250788, 0.05869839, -86.83059451, -0.00115234, -105.25078801, -0.0155345, -10.5250788, -0.05869839, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22012, 2012, 0.0, 141.35817923, 0.02304672, 141.35817923, 0.06914016, 98.95072546, -2296.78038867, 0.05, 2, 0, 72012, 23012, 2, 3)
    ops.uniaxialMaterial('LimitState', 42012, 35.33954481, 8.204e-05, 106.01863442, 0.00024612, 353.39544807, 0.00082039, -35.33954481, -8.204e-05, -106.01863442, -0.00024612, -353.39544807, -0.00082039, 0.4, 0.3, 0.003, 0.0, 0.0, 22012, 2)
    ops.limitCurve('ThreePoint', 12012, 2012, 0.0, 141.35817923, 0.02304672, 141.35817923, 0.06914016, 98.95072546, -2296.78038867, 0.05, 2, 0, 72012, 23012, 1, 3)
    ops.uniaxialMaterial('LimitState', 32012, 35.33954481, 8.204e-05, 106.01863442, 0.00024612, 353.39544807, 0.00082039, -35.33954481, -8.204e-05, -106.01863442, -0.00024612, -353.39544807, -0.00082039, 0.4, 0.3, 0.003, 0.0, 0.0, 12012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2012, 99999, 'P', 42012, 'Vy', 32012, 'Vz', 22012, 'My', 12012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172012, 72012, 172012, 2012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123012, 123012, 23012, 2012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172013, 15.5, 5.1, 6.05)
    ops.node(123013, 15.5, 5.1, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2013, 172013, 123013, 0.1225, 28556396.76498147, 11898498.65207561, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22013, 99.36174981, 0.00126495, 120.63476519, 0.01790954, 12.06347652, 0.0603165, -99.36174981, -0.00126495, -120.63476519, -0.01790954, -12.06347652, -0.0603165, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12013, 86.90520662, 0.00126495, 105.51131813, 0.01790954, 10.55113181, 0.0603165, -86.90520662, -0.00126495, -105.51131813, -0.01790954, -10.55113181, -0.0603165, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22013, 2013, 0.0, 153.56320905, 0.02529904, 153.56320905, 0.07589713, 107.49424634, -3078.58769028, 0.05, 2, 0, 72013, 23013, 2, 3)
    ops.uniaxialMaterial('LimitState', 42013, 38.39080226, 9.166e-05, 115.17240679, 0.00027498, 383.90802264, 0.0009166, -38.39080226, -9.166e-05, -115.17240679, -0.00027498, -383.90802264, -0.0009166, 0.4, 0.3, 0.003, 0.0, 0.0, 22013, 2)
    ops.limitCurve('ThreePoint', 12013, 2013, 0.0, 153.56320905, 0.02529904, 153.56320905, 0.07589713, 107.49424634, -3078.58769028, 0.05, 2, 0, 72013, 23013, 1, 3)
    ops.uniaxialMaterial('LimitState', 32013, 38.39080226, 9.166e-05, 115.17240679, 0.00027498, 383.90802264, 0.0009166, -38.39080226, -9.166e-05, -115.17240679, -0.00027498, -383.90802264, -0.0009166, 0.4, 0.3, 0.003, 0.0, 0.0, 12013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2013, 99999, 'P', 42013, 'Vy', 32013, 'Vz', 22013, 'My', 12013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172013, 72013, 172013, 2013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123013, 123013, 23013, 2013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172014, 19.7, 5.1, 6.075)
    ops.node(123014, 19.7, 5.1, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2014, 172014, 123014, 0.1225, 28238947.50153174, 11766228.12563823, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22014, 86.50974666, 0.00120135, 105.10685622, 0.01482812, 10.51068562, 0.05710531, -86.50974666, -0.00120135, -105.10685622, -0.01482812, -10.51068562, -0.05710531, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12014, 100.34697542, 0.00120135, 121.91869153, 0.01482812, 12.19186915, 0.05710531, -100.34697542, -0.00120135, -121.91869153, -0.01482812, -12.19186915, -0.05710531, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22014, 2014, 0.0, 135.07661152, 0.02402696, 135.07661152, 0.07208089, 94.55362806, -2220.9916535, 0.05, 2, 0, 72014, 23014, 2, 3)
    ops.uniaxialMaterial('LimitState', 42014, 33.76915288, 8.153e-05, 101.30745864, 0.00024459, 337.6915288, 0.00081532, -33.76915288, -8.153e-05, -101.30745864, -0.00024459, -337.6915288, -0.00081532, 0.4, 0.3, 0.003, 0.0, 0.0, 22014, 2)
    ops.limitCurve('ThreePoint', 12014, 2014, 0.0, 135.07661152, 0.02402696, 135.07661152, 0.07208089, 94.55362806, -2220.9916535, 0.05, 2, 0, 72014, 23014, 1, 3)
    ops.uniaxialMaterial('LimitState', 32014, 33.76915288, 8.153e-05, 101.30745864, 0.00024459, 337.6915288, 0.00081532, -33.76915288, -8.153e-05, -101.30745864, -0.00024459, -337.6915288, -0.00081532, 0.4, 0.3, 0.003, 0.0, 0.0, 12014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2014, 99999, 'P', 42014, 'Vy', 32014, 'Vz', 22014, 'My', 12014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172014, 72014, 172014, 2014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123014, 123014, 23014, 2014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172015, 23.9, 5.1, 6.075)
    ops.node(123015, 23.9, 5.1, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2015, 172015, 123015, 0.1225, 28849828.05117931, 12020761.68799138, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22015, 89.93349462, 0.00118232, 109.14230522, 0.01616428, 10.91423052, 0.05903102, -89.93349462, -0.00118232, -109.14230522, -0.01616428, -10.91423052, -0.05903102, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12015, 105.66471309, 0.00118232, 128.23353987, 0.01616428, 12.82335399, 0.05903102, -105.66471309, -0.00118232, -128.23353987, -0.01616428, -12.82335399, -0.05903102, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22015, 2015, 0.0, 146.7137693, 0.02364636, 146.7137693, 0.07093908, 102.69963851, -2693.67960346, 0.05, 2, 0, 72015, 23015, 2, 3)
    ops.uniaxialMaterial('LimitState', 42015, 36.67844233, 8.668e-05, 110.03532698, 0.00026004, 366.78442326, 0.00086681, -36.67844233, -8.668e-05, -110.03532698, -0.00026004, -366.78442326, -0.00086681, 0.4, 0.3, 0.003, 0.0, 0.0, 22015, 2)
    ops.limitCurve('ThreePoint', 12015, 2015, 0.0, 146.7137693, 0.02364636, 146.7137693, 0.07093908, 102.69963851, -2693.67960346, 0.05, 2, 0, 72015, 23015, 1, 3)
    ops.uniaxialMaterial('LimitState', 32015, 36.67844233, 8.668e-05, 110.03532698, 0.00026004, 366.78442326, 0.00086681, -36.67844233, -8.668e-05, -110.03532698, -0.00026004, -366.78442326, -0.00086681, 0.4, 0.3, 0.003, 0.0, 0.0, 12015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2015, 99999, 'P', 42015, 'Vy', 32015, 'Vz', 22015, 'My', 12015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172015, 72015, 172015, 2015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123015, 123015, 23015, 2015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172016, 28.1, 5.1, 6.05)
    ops.node(123016, 28.1, 5.1, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2016, 172016, 123016, 0.0625, 31096026.82304648, 12956677.84293604, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22016, 37.64339723, 0.00157847, 45.35925989, 0.01912293, 4.53592599, 0.073787, -37.64339723, -0.00157847, -45.35925989, -0.01912293, -4.53592599, -0.073787, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12016, 37.64339723, 0.00157847, 45.35925989, 0.01912293, 4.53592599, 0.073787, -37.64339723, -0.00157847, -45.35925989, -0.01912293, -4.53592599, -0.073787, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22016, 2016, 0.0, 97.74007818, 0.0315694, 97.74007818, 0.09470819, 68.41805472, -2011.08633516, 0.05, 2, 0, 72016, 23016, 2, 3)
    ops.uniaxialMaterial('LimitState', 42016, 24.43501954, 0.00010501, 73.30505863, 0.00031502, 244.35019545, 0.00105007, -24.43501954, -0.00010501, -73.30505863, -0.00031502, -244.35019545, -0.00105007, 0.4, 0.3, 0.003, 0.0, 0.0, 22016, 2)
    ops.limitCurve('ThreePoint', 12016, 2016, 0.0, 97.74007818, 0.0315694, 97.74007818, 0.09470819, 68.41805472, -2011.08633516, 0.05, 2, 0, 72016, 23016, 1, 3)
    ops.uniaxialMaterial('LimitState', 32016, 24.43501954, 0.00010501, 73.30505863, 0.00031502, 244.35019545, 0.00105007, -24.43501954, -0.00010501, -73.30505863, -0.00031502, -244.35019545, -0.00105007, 0.4, 0.3, 0.003, 0.0, 0.0, 12016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2016, 99999, 'P', 42016, 'Vy', 32016, 'Vz', 22016, 'My', 12016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172016, 72016, 172016, 2016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123016, 123016, 23016, 2016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172017, 0.0, 10.2, 6.05)
    ops.node(123017, 0.0, 10.2, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2017, 172017, 123017, 0.0625, 30488544.4621688, 12703560.19257033, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22017, 37.57751162, 0.00176726, 45.3464212, 0.01613177, 4.53464212, 0.07009381, -37.57751162, -0.00176726, -45.3464212, -0.01613177, -4.53464212, -0.07009381, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12017, 37.57751162, 0.00176726, 45.3464212, 0.01613177, 4.53464212, 0.07009381, -37.57751162, -0.00176726, -45.3464212, -0.01613177, -4.53464212, -0.07009381, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22017, 2017, 0.0, 88.95658505, 0.03534518, 88.95658505, 0.10603554, 62.26960954, -1626.53910485, 0.05, 2, 0, 72017, 23017, 2, 3)
    ops.uniaxialMaterial('LimitState', 42017, 22.23914626, 9.747e-05, 66.71743879, 0.00029242, 222.39146263, 0.00097475, -22.23914626, -9.747e-05, -66.71743879, -0.00029242, -222.39146263, -0.00097475, 0.4, 0.3, 0.003, 0.0, 0.0, 22017, 2)
    ops.limitCurve('ThreePoint', 12017, 2017, 0.0, 88.95658505, 0.03534518, 88.95658505, 0.10603554, 62.26960954, -1626.53910485, 0.05, 2, 0, 72017, 23017, 1, 3)
    ops.uniaxialMaterial('LimitState', 32017, 22.23914626, 9.747e-05, 66.71743879, 0.00029242, 222.39146263, 0.00097475, -22.23914626, -9.747e-05, -66.71743879, -0.00029242, -222.39146263, -0.00097475, 0.4, 0.3, 0.003, 0.0, 0.0, 12017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2017, 99999, 'P', 42017, 'Vy', 32017, 'Vz', 22017, 'My', 12017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172017, 72017, 172017, 2017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123017, 123017, 23017, 2017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172018, 4.2, 10.2, 6.075)
    ops.node(123018, 4.2, 10.2, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2018, 172018, 123018, 0.1225, 28815020.79176477, 12006258.66323532, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22018, 105.6924268, 0.00135191, 128.27981811, 0.01705735, 12.82798181, 0.05468172, -105.6924268, -0.00135191, -128.27981811, -0.01705735, -12.82798181, -0.05468172, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12018, 99.86082996, 0.00135191, 121.20195828, 0.01705735, 12.12019583, 0.05468172, -99.86082996, -0.00135191, -121.20195828, -0.01705735, -12.12019583, -0.05468172, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22018, 2018, 0.0, 131.64937561, 0.02703816, 131.64937561, 0.08111449, 92.15456293, -1973.17028947, 0.05, 2, 0, 72018, 23018, 2, 3)
    ops.uniaxialMaterial('LimitState', 42018, 32.9123439, 7.787e-05, 98.73703171, 0.00023362, 329.12343903, 0.00077874, -32.9123439, -7.787e-05, -98.73703171, -0.00023362, -329.12343903, -0.00077874, 0.4, 0.3, 0.003, 0.0, 0.0, 22018, 2)
    ops.limitCurve('ThreePoint', 12018, 2018, 0.0, 131.64937561, 0.02703816, 131.64937561, 0.08111449, 92.15456293, -1973.17028947, 0.05, 2, 0, 72018, 23018, 1, 3)
    ops.uniaxialMaterial('LimitState', 32018, 32.9123439, 7.787e-05, 98.73703171, 0.00023362, 329.12343903, 0.00077874, -32.9123439, -7.787e-05, -98.73703171, -0.00023362, -329.12343903, -0.00077874, 0.4, 0.3, 0.003, 0.0, 0.0, 12018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2018, 99999, 'P', 42018, 'Vy', 32018, 'Vz', 22018, 'My', 12018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172018, 72018, 172018, 2018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123018, 123018, 23018, 2018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172019, 8.4, 10.2, 6.075)
    ops.node(123019, 8.4, 10.2, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2019, 172019, 123019, 0.1225, 25682464.47562659, 10701026.86484441, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22019, 102.10417345, 0.0013387, 124.47765577, 0.0180152, 12.44776558, 0.05248739, -102.10417345, -0.0013387, -124.47765577, -0.0180152, -12.44776558, -0.05248739, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12019, 96.12444718, 0.0013387, 117.18762752, 0.0180152, 11.71876275, 0.05248739, -96.12444718, -0.0013387, -117.18762752, -0.0180152, -11.71876275, -0.05248739, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22019, 2019, 0.0, 124.11955272, 0.02677392, 124.11955272, 0.08032176, 86.8836869, -2126.94198308, 0.05, 2, 0, 72019, 23019, 2, 3)
    ops.uniaxialMaterial('LimitState', 42019, 31.02988818, 8.238e-05, 93.08966454, 0.00024713, 310.29888179, 0.00082375, -31.02988818, -8.238e-05, -93.08966454, -0.00024713, -310.29888179, -0.00082375, 0.4, 0.3, 0.003, 0.0, 0.0, 22019, 2)
    ops.limitCurve('ThreePoint', 12019, 2019, 0.0, 124.11955272, 0.02677392, 124.11955272, 0.08032176, 86.8836869, -2126.94198308, 0.05, 2, 0, 72019, 23019, 1, 3)
    ops.uniaxialMaterial('LimitState', 32019, 31.02988818, 8.238e-05, 93.08966454, 0.00024713, 310.29888179, 0.00082375, -31.02988818, -8.238e-05, -93.08966454, -0.00024713, -310.29888179, -0.00082375, 0.4, 0.3, 0.003, 0.0, 0.0, 12019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2019, 99999, 'P', 42019, 'Vy', 32019, 'Vz', 22019, 'My', 12019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172019, 72019, 172019, 2019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123019, 123019, 23019, 2019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172020, 12.6, 10.2, 6.05)
    ops.node(123020, 12.6, 10.2, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2020, 172020, 123020, 0.0625, 30854831.70625789, 12856179.87760746, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22020, 39.35934332, 0.00166624, 47.40194631, 0.0174289, 4.74019463, 0.07002665, -39.35934332, -0.00166624, -47.40194631, -0.0174289, -4.74019463, -0.07002665, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12020, 39.35934332, 0.00166624, 47.40194631, 0.0174289, 4.74019463, 0.07002665, -39.35934332, -0.00166624, -47.40194631, -0.0174289, -4.74019463, -0.07002665, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22020, 2020, 0.0, 97.73704121, 0.03332486, 97.73704121, 0.09997459, 68.41592885, -1857.99993078, 0.05, 2, 0, 72020, 23020, 2, 3)
    ops.uniaxialMaterial('LimitState', 42020, 24.4342603, 0.00010582, 73.30278091, 0.00031747, 244.34260302, 0.00105825, -24.4342603, -0.00010582, -73.30278091, -0.00031747, -244.34260302, -0.00105825, 0.4, 0.3, 0.003, 0.0, 0.0, 22020, 2)
    ops.limitCurve('ThreePoint', 12020, 2020, 0.0, 97.73704121, 0.03332486, 97.73704121, 0.09997459, 68.41592885, -1857.99993078, 0.05, 2, 0, 72020, 23020, 1, 3)
    ops.uniaxialMaterial('LimitState', 32020, 24.4342603, 0.00010582, 73.30278091, 0.00031747, 244.34260302, 0.00105825, -24.4342603, -0.00010582, -73.30278091, -0.00031747, -244.34260302, -0.00105825, 0.4, 0.3, 0.003, 0.0, 0.0, 12020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2020, 99999, 'P', 42020, 'Vy', 32020, 'Vz', 22020, 'My', 12020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172020, 72020, 172020, 2020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123020, 123020, 23020, 2020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172021, 15.5, 10.2, 6.05)
    ops.node(123021, 15.5, 10.2, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2021, 172021, 123021, 0.0625, 28288923.7208566, 11787051.55035692, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22021, 40.49399281, 0.00168127, 48.99342901, 0.01551568, 4.8993429, 0.0640233, -40.49399281, -0.00168127, -48.99342901, -0.01551568, -4.8993429, -0.0640233, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12021, 40.49399281, 0.00168127, 48.99342901, 0.01551568, 4.8993429, 0.0640233, -40.49399281, -0.00168127, -48.99342901, -0.01551568, -4.8993429, -0.0640233, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22021, 2021, 0.0, 82.76027562, 0.03362531, 82.76027562, 0.10087593, 57.93219293, -1546.48453322, 0.05, 2, 0, 72021, 23021, 2, 3)
    ops.uniaxialMaterial('LimitState', 42021, 20.69006891, 9.774e-05, 62.07020672, 0.00029321, 206.90068905, 0.00097736, -20.69006891, -9.774e-05, -62.07020672, -0.00029321, -206.90068905, -0.00097736, 0.4, 0.3, 0.003, 0.0, 0.0, 22021, 2)
    ops.limitCurve('ThreePoint', 12021, 2021, 0.0, 82.76027562, 0.03362531, 82.76027562, 0.10087593, 57.93219293, -1546.48453322, 0.05, 2, 0, 72021, 23021, 1, 3)
    ops.uniaxialMaterial('LimitState', 32021, 20.69006891, 9.774e-05, 62.07020672, 0.00029321, 206.90068905, 0.00097736, -20.69006891, -9.774e-05, -62.07020672, -0.00029321, -206.90068905, -0.00097736, 0.4, 0.3, 0.003, 0.0, 0.0, 12021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2021, 99999, 'P', 42021, 'Vy', 32021, 'Vz', 22021, 'My', 12021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172021, 72021, 172021, 2021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123021, 123021, 23021, 2021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172022, 19.7, 10.2, 6.075)
    ops.node(123022, 19.7, 10.2, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2022, 172022, 123022, 0.1225, 29721660.9941299, 12384025.41422079, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22022, 104.32907172, 0.00125394, 126.38394317, 0.01724654, 12.63839432, 0.05556803, -104.32907172, -0.00125394, -126.38394317, -0.01724654, -12.63839432, -0.05556803, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12022, 98.34524013, 0.00125394, 119.13514646, 0.01724654, 11.91351465, 0.05556803, -98.34524013, -0.00125394, -119.13514646, -0.01724654, -11.91351465, -0.05556803, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22022, 2022, 0.0, 134.47755643, 0.02507886, 134.47755643, 0.07523659, 94.1342895, -1952.48918479, 0.05, 2, 0, 72022, 23022, 2, 3)
    ops.uniaxialMaterial('LimitState', 42022, 33.61938911, 7.712e-05, 100.85816732, 0.00023136, 336.19389108, 0.00077121, -33.61938911, -7.712e-05, -100.85816732, -0.00023136, -336.19389108, -0.00077121, 0.4, 0.3, 0.003, 0.0, 0.0, 22022, 2)
    ops.limitCurve('ThreePoint', 12022, 2022, 0.0, 134.47755643, 0.02507886, 134.47755643, 0.07523659, 94.1342895, -1952.48918479, 0.05, 2, 0, 72022, 23022, 1, 3)
    ops.uniaxialMaterial('LimitState', 32022, 33.61938911, 7.712e-05, 100.85816732, 0.00023136, 336.19389108, 0.00077121, -33.61938911, -7.712e-05, -100.85816732, -0.00023136, -336.19389108, -0.00077121, 0.4, 0.3, 0.003, 0.0, 0.0, 12022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2022, 99999, 'P', 42022, 'Vy', 32022, 'Vz', 22022, 'My', 12022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172022, 72022, 172022, 2022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123022, 123022, 23022, 2022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172023, 23.9, 10.2, 6.075)
    ops.node(123023, 23.9, 10.2, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2023, 172023, 123023, 0.1225, 26109851.63553866, 10879104.84814111, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22023, 114.20103384, 0.00140244, 139.16950384, 0.01490843, 13.91695038, 0.04989111, -114.20103384, -0.00140244, -139.16950384, -0.01490843, -13.91695038, -0.04989111, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12023, 106.7077808, 0.00140244, 130.03795509, 0.01490843, 13.00379551, 0.04989111, -106.7077808, -0.00140244, -130.03795509, -0.01490843, -13.00379551, -0.04989111, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22023, 2023, 0.0, 117.27720136, 0.02804886, 117.27720136, 0.08414657, 82.09404095, -1757.81687291, 0.05, 2, 0, 72023, 23023, 2, 3)
    ops.uniaxialMaterial('LimitState', 42023, 29.31930034, 7.656e-05, 87.95790102, 0.00022968, 293.1930034, 0.0007656, -29.31930034, -7.656e-05, -87.95790102, -0.00022968, -293.1930034, -0.0007656, 0.4, 0.3, 0.003, 0.0, 0.0, 22023, 2)
    ops.limitCurve('ThreePoint', 12023, 2023, 0.0, 117.27720136, 0.02804886, 117.27720136, 0.08414657, 82.09404095, -1757.81687291, 0.05, 2, 0, 72023, 23023, 1, 3)
    ops.uniaxialMaterial('LimitState', 32023, 29.31930034, 7.656e-05, 87.95790102, 0.00022968, 293.1930034, 0.0007656, -29.31930034, -7.656e-05, -87.95790102, -0.00022968, -293.1930034, -0.0007656, 0.4, 0.3, 0.003, 0.0, 0.0, 12023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2023, 99999, 'P', 42023, 'Vy', 32023, 'Vz', 22023, 'My', 12023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172023, 72023, 172023, 2023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123023, 123023, 23023, 2023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172024, 28.1, 10.2, 6.05)
    ops.node(123024, 28.1, 10.2, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2024, 172024, 123024, 0.0625, 30098005.68731456, 12540835.70304773, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22024, 36.79517679, 0.00168048, 44.44052939, 0.01907285, 4.44405294, 0.07252648, -36.79517679, -0.00168048, -44.44052939, -0.01907285, -4.44405294, -0.07252648, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12024, 36.79517679, 0.00168048, 44.44052939, 0.01907285, 4.44405294, 0.07252648, -36.79517679, -0.00168048, -44.44052939, -0.01907285, -4.44405294, -0.07252648, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22024, 2024, 0.0, 97.13441511, 0.03360956, 97.13441511, 0.10082869, 67.99409057, -2087.93401204, 0.05, 2, 0, 72024, 23024, 2, 3)
    ops.uniaxialMaterial('LimitState', 42024, 24.28360378, 0.00010782, 72.85081133, 0.00032345, 242.83603777, 0.00107817, -24.28360378, -0.00010782, -72.85081133, -0.00032345, -242.83603777, -0.00107817, 0.4, 0.3, 0.003, 0.0, 0.0, 22024, 2)
    ops.limitCurve('ThreePoint', 12024, 2024, 0.0, 97.13441511, 0.03360956, 97.13441511, 0.10082869, 67.99409057, -2087.93401204, 0.05, 2, 0, 72024, 23024, 1, 3)
    ops.uniaxialMaterial('LimitState', 32024, 24.28360378, 0.00010782, 72.85081133, 0.00032345, 242.83603777, 0.00107817, -24.28360378, -0.00010782, -72.85081133, -0.00032345, -242.83603777, -0.00107817, 0.4, 0.3, 0.003, 0.0, 0.0, 12024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2024, 99999, 'P', 42024, 'Vy', 32024, 'Vz', 22024, 'My', 12024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172024, 72024, 172024, 2024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123024, 123024, 23024, 2024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172025, 0.0, 15.3, 6.05)
    ops.node(123025, 0.0, 15.3, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2025, 172025, 123025, 0.0625, 28852692.34581239, 12021955.1440885, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22025, 34.38283906, 0.00154368, 41.77791747, 0.0185999, 4.17779175, 0.07619442, -34.38283906, -0.00154368, -41.77791747, -0.0185999, -4.17779175, -0.07619442, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12025, 34.38283906, 0.00154368, 41.77791747, 0.0185999, 4.17779175, 0.07619442, -34.38283906, -0.00154368, -41.77791747, -0.0185999, -4.17779175, -0.07619442, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22025, 2025, 0.0, 85.91424137, 0.03087365, 85.91424137, 0.09262094, 60.13996896, -2366.05327029, 0.05, 2, 0, 72025, 23025, 2, 3)
    ops.uniaxialMaterial('LimitState', 42025, 21.47856034, 9.948e-05, 64.43568103, 0.00029844, 214.78560343, 0.00099479, -21.47856034, -9.948e-05, -64.43568103, -0.00029844, -214.78560343, -0.00099479, 0.4, 0.3, 0.003, 0.0, 0.0, 22025, 2)
    ops.limitCurve('ThreePoint', 12025, 2025, 0.0, 85.91424137, 0.03087365, 85.91424137, 0.09262094, 60.13996896, -2366.05327029, 0.05, 2, 0, 72025, 23025, 1, 3)
    ops.uniaxialMaterial('LimitState', 32025, 21.47856034, 9.948e-05, 64.43568103, 0.00029844, 214.78560343, 0.00099479, -21.47856034, -9.948e-05, -64.43568103, -0.00029844, -214.78560343, -0.00099479, 0.4, 0.3, 0.003, 0.0, 0.0, 12025, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2025, 99999, 'P', 42025, 'Vy', 32025, 'Vz', 22025, 'My', 12025, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172025, 72025, 172025, 2025, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123025, 123025, 23025, 2025, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172026, 4.2, 15.3, 6.075)
    ops.node(123026, 4.2, 15.3, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2026, 172026, 123026, 0.0625, 29338774.27776011, 12224489.28240005, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22026, 37.51905637, 0.00151686, 45.40275258, 0.01571858, 4.54027526, 0.06877541, -37.51905637, -0.00151686, -45.40275258, -0.01571858, -4.54027526, -0.06877541, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12026, 37.51905637, 0.00151686, 45.40275258, 0.01571858, 4.54027526, 0.06877541, -37.51905637, -0.00151686, -45.40275258, -0.01571858, -4.54027526, -0.06877541, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22026, 2026, 0.0, 78.47326663, 0.03033724, 78.47326663, 0.09101172, 54.93128664, -1596.25223164, 0.05, 2, 0, 72026, 23026, 2, 3)
    ops.uniaxialMaterial('LimitState', 42026, 19.61831666, 8.936e-05, 58.85494997, 0.00026807, 196.18316658, 0.00089357, -19.61831666, -8.936e-05, -58.85494997, -0.00026807, -196.18316658, -0.00089357, 0.4, 0.3, 0.003, 0.0, 0.0, 22026, 2)
    ops.limitCurve('ThreePoint', 12026, 2026, 0.0, 78.47326663, 0.03033724, 78.47326663, 0.09101172, 54.93128664, -1596.25223164, 0.05, 2, 0, 72026, 23026, 1, 3)
    ops.uniaxialMaterial('LimitState', 32026, 19.61831666, 8.936e-05, 58.85494997, 0.00026807, 196.18316658, 0.00089357, -19.61831666, -8.936e-05, -58.85494997, -0.00026807, -196.18316658, -0.00089357, 0.4, 0.3, 0.003, 0.0, 0.0, 12026, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2026, 99999, 'P', 42026, 'Vy', 32026, 'Vz', 22026, 'My', 12026, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172026, 72026, 172026, 2026, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123026, 123026, 23026, 2026, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172027, 8.4, 15.3, 6.075)
    ops.node(123027, 8.4, 15.3, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2027, 172027, 123027, 0.0625, 28975582.9105846, 12073159.54607692, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22027, 37.308402, 0.0017485, 45.17812391, 0.0166862, 4.51781239, 0.06922263, -37.308402, -0.0017485, -45.17812391, -0.0166862, -4.51781239, -0.06922263, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12027, 37.308402, 0.0017485, 45.17812391, 0.0166862, 4.51781239, 0.06922263, -37.308402, -0.0017485, -45.17812391, -0.0166862, -4.51781239, -0.06922263, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22027, 2027, 0.0, 88.12197714, 0.03497007, 88.12197714, 0.10491021, 61.685384, -1783.72155147, 0.05, 2, 0, 72027, 23027, 2, 3)
    ops.uniaxialMaterial('LimitState', 42027, 22.03049429, 0.0001016, 66.09148286, 0.00030481, 220.30494286, 0.00101602, -22.03049429, -0.0001016, -66.09148286, -0.00030481, -220.30494286, -0.00101602, 0.4, 0.3, 0.003, 0.0, 0.0, 22027, 2)
    ops.limitCurve('ThreePoint', 12027, 2027, 0.0, 88.12197714, 0.03497007, 88.12197714, 0.10491021, 61.685384, -1783.72155147, 0.05, 2, 0, 72027, 23027, 1, 3)
    ops.uniaxialMaterial('LimitState', 32027, 22.03049429, 0.0001016, 66.09148286, 0.00030481, 220.30494286, 0.00101602, -22.03049429, -0.0001016, -66.09148286, -0.00030481, -220.30494286, -0.00101602, 0.4, 0.3, 0.003, 0.0, 0.0, 12027, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2027, 99999, 'P', 42027, 'Vy', 32027, 'Vz', 22027, 'My', 12027, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172027, 72027, 172027, 2027, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123027, 123027, 23027, 2027, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172028, 12.6, 15.3, 6.05)
    ops.node(123028, 12.6, 15.3, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2028, 172028, 123028, 0.0625, 28684934.03595847, 11952055.84831603, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22028, 36.34306765, 0.00157685, 44.09000633, 0.01651192, 4.40900063, 0.07072634, -36.34306765, -0.00157685, -44.09000633, -0.01651192, -4.40900063, -0.07072634, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12028, 36.34306765, 0.00157685, 44.09000633, 0.01651192, 4.40900063, 0.07072634, -36.34306765, -0.00157685, -44.09000633, -0.01651192, -4.40900063, -0.07072634, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22028, 2028, 0.0, 82.03279769, 0.03153705, 82.03279769, 0.09461116, 57.42295839, -1788.3557348, 0.05, 2, 0, 72028, 23028, 2, 3)
    ops.uniaxialMaterial('LimitState', 42028, 20.50819942, 9.554e-05, 61.52459827, 0.00028662, 205.08199424, 0.0009554, -20.50819942, -9.554e-05, -61.52459827, -0.00028662, -205.08199424, -0.0009554, 0.4, 0.3, 0.003, 0.0, 0.0, 22028, 2)
    ops.limitCurve('ThreePoint', 12028, 2028, 0.0, 82.03279769, 0.03153705, 82.03279769, 0.09461116, 57.42295839, -1788.3557348, 0.05, 2, 0, 72028, 23028, 1, 3)
    ops.uniaxialMaterial('LimitState', 32028, 20.50819942, 9.554e-05, 61.52459827, 0.00028662, 205.08199424, 0.0009554, -20.50819942, -9.554e-05, -61.52459827, -0.00028662, -205.08199424, -0.0009554, 0.4, 0.3, 0.003, 0.0, 0.0, 12028, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2028, 99999, 'P', 42028, 'Vy', 32028, 'Vz', 22028, 'My', 12028, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172028, 72028, 172028, 2028, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123028, 123028, 23028, 2028, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172029, 15.5, 15.3, 6.05)
    ops.node(123029, 15.5, 15.3, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2029, 172029, 123029, 0.0625, 29578212.84340128, 12324255.3514172, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22029, 35.48295655, 0.00159083, 42.97040612, 0.01597054, 4.29704061, 0.07130752, -35.48295655, -0.00159083, -42.97040612, -0.01597054, -4.29704061, -0.07130752, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12029, 35.48295655, 0.00159083, 42.97040612, 0.01597054, 4.29704061, 0.07130752, -35.48295655, -0.00159083, -42.97040612, -0.01597054, -4.29704061, -0.07130752, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22029, 2029, 0.0, 78.59762335, 0.03181668, 78.59762335, 0.09545004, 55.01833635, -1712.22623329, 0.05, 2, 0, 72029, 23029, 2, 3)
    ops.uniaxialMaterial('LimitState', 42029, 19.64940584, 8.877e-05, 58.94821751, 0.00026632, 196.49405838, 0.00088774, -19.64940584, -8.877e-05, -58.94821751, -0.00026632, -196.49405838, -0.00088774, 0.4, 0.3, 0.003, 0.0, 0.0, 22029, 2)
    ops.limitCurve('ThreePoint', 12029, 2029, 0.0, 78.59762335, 0.03181668, 78.59762335, 0.09545004, 55.01833635, -1712.22623329, 0.05, 2, 0, 72029, 23029, 1, 3)
    ops.uniaxialMaterial('LimitState', 32029, 19.64940584, 8.877e-05, 58.94821751, 0.00026632, 196.49405838, 0.00088774, -19.64940584, -8.877e-05, -58.94821751, -0.00026632, -196.49405838, -0.00088774, 0.4, 0.3, 0.003, 0.0, 0.0, 12029, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2029, 99999, 'P', 42029, 'Vy', 32029, 'Vz', 22029, 'My', 12029, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172029, 72029, 172029, 2029, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123029, 123029, 23029, 2029, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172030, 19.7, 15.3, 6.075)
    ops.node(123030, 19.7, 15.3, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2030, 172030, 123030, 0.0625, 32946150.86175956, 13727562.85906648, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22030, 38.7088124, 0.00158317, 46.41736061, 0.0162586, 4.64173606, 0.07342139, -38.7088124, -0.00158317, -46.41736061, -0.0162586, -4.64173606, -0.07342139, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12030, 38.7088124, 0.00158317, 46.41736061, 0.0162586, 4.64173606, 0.07342139, -38.7088124, -0.00158317, -46.41736061, -0.0162586, -4.64173606, -0.07342139, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22030, 2030, 0.0, 94.99105158, 0.03166337, 94.99105158, 0.09499011, 66.49373611, -1741.36556656, 0.05, 2, 0, 72030, 23030, 2, 3)
    ops.uniaxialMaterial('LimitState', 42030, 23.7477629, 9.632e-05, 71.24328869, 0.00028897, 237.47762896, 0.00096323, -23.7477629, -9.632e-05, -71.24328869, -0.00028897, -237.47762896, -0.00096323, 0.4, 0.3, 0.003, 0.0, 0.0, 22030, 2)
    ops.limitCurve('ThreePoint', 12030, 2030, 0.0, 94.99105158, 0.03166337, 94.99105158, 0.09499011, 66.49373611, -1741.36556656, 0.05, 2, 0, 72030, 23030, 1, 3)
    ops.uniaxialMaterial('LimitState', 32030, 23.7477629, 9.632e-05, 71.24328869, 0.00028897, 237.47762896, 0.00096323, -23.7477629, -9.632e-05, -71.24328869, -0.00028897, -237.47762896, -0.00096323, 0.4, 0.3, 0.003, 0.0, 0.0, 12030, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2030, 99999, 'P', 42030, 'Vy', 32030, 'Vz', 22030, 'My', 12030, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172030, 72030, 172030, 2030, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123030, 123030, 23030, 2030, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172031, 23.9, 15.3, 6.075)
    ops.node(123031, 23.9, 15.3, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2031, 172031, 123031, 0.0625, 27293166.79645327, 11372152.83185553, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22031, 37.33149633, 0.00165203, 45.31813948, 0.01941353, 4.53181395, 0.06921423, -37.33149633, -0.00165203, -45.31813948, -0.01941353, -4.53181395, -0.06921423, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12031, 37.33149633, 0.00165203, 45.31813948, 0.01941353, 4.53181395, 0.06921423, -37.33149633, -0.00165203, -45.31813948, -0.01941353, -4.53181395, -0.06921423, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22031, 2031, 0.0, 90.36416554, 0.03304063, 90.36416554, 0.09912189, 63.25491588, -2071.87207016, 0.05, 2, 0, 72031, 23031, 2, 3)
    ops.uniaxialMaterial('LimitState', 42031, 22.59104139, 0.00011061, 67.77312416, 0.00033183, 225.91041386, 0.0011061, -22.59104139, -0.00011061, -67.77312416, -0.00033183, -225.91041386, -0.0011061, 0.4, 0.3, 0.003, 0.0, 0.0, 22031, 2)
    ops.limitCurve('ThreePoint', 12031, 2031, 0.0, 90.36416554, 0.03304063, 90.36416554, 0.09912189, 63.25491588, -2071.87207016, 0.05, 2, 0, 72031, 23031, 1, 3)
    ops.uniaxialMaterial('LimitState', 32031, 22.59104139, 0.00011061, 67.77312416, 0.00033183, 225.91041386, 0.0011061, -22.59104139, -0.00011061, -67.77312416, -0.00033183, -225.91041386, -0.0011061, 0.4, 0.3, 0.003, 0.0, 0.0, 12031, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2031, 99999, 'P', 42031, 'Vy', 32031, 'Vz', 22031, 'My', 12031, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172031, 72031, 172031, 2031, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123031, 123031, 23031, 2031, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172032, 28.1, 15.3, 6.05)
    ops.node(123032, 28.1, 15.3, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2032, 172032, 123032, 0.0625, 28507066.29469013, 11877944.28945422, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22032, 33.08283996, 0.0015849, 40.22686701, 0.01918597, 4.0226867, 0.07642646, -33.08283996, -0.0015849, -40.22686701, -0.01918597, -4.0226867, -0.07642646, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12032, 33.08283996, 0.0015849, 40.22686701, 0.01918597, 4.0226867, 0.07642646, -33.08283996, -0.0015849, -40.22686701, -0.01918597, -4.0226867, -0.07642646, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22032, 2032, 0.0, 85.14958799, 0.03169796, 85.14958799, 0.09509388, 59.60471159, -2355.55484271, 0.05, 2, 0, 72032, 23032, 2, 3)
    ops.uniaxialMaterial('LimitState', 42032, 21.287397, 9.979e-05, 63.86219099, 0.00029937, 212.87396997, 0.00099789, -21.287397, -9.979e-05, -63.86219099, -0.00029937, -212.87396997, -0.00099789, 0.4, 0.3, 0.003, 0.0, 0.0, 22032, 2)
    ops.limitCurve('ThreePoint', 12032, 2032, 0.0, 85.14958799, 0.03169796, 85.14958799, 0.09509388, 59.60471159, -2355.55484271, 0.05, 2, 0, 72032, 23032, 1, 3)
    ops.uniaxialMaterial('LimitState', 32032, 21.287397, 9.979e-05, 63.86219099, 0.00029937, 212.87396997, 0.00099789, -21.287397, -9.979e-05, -63.86219099, -0.00029937, -212.87396997, -0.00099789, 0.4, 0.3, 0.003, 0.0, 0.0, 12032, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2032, 99999, 'P', 42032, 'Vy', 32032, 'Vz', 22032, 'My', 12032, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172032, 72032, 172032, 2032, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123032, 123032, 23032, 2032, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173001, 0.0, 0.0, 8.95)
    ops.node(124001, 0.0, 0.0, 11.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3001, 173001, 124001, 0.0625, 26457465.97396301, 11023944.15581792, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23001, 26.71367894, 0.00153112, 32.75724867, 0.02159499, 3.27572487, 0.08513471, -26.71367894, -0.00153112, -32.75724867, -0.02159499, -3.27572487, -0.08513471, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13001, 26.71367894, 0.00153112, 32.75724867, 0.02159499, 3.27572487, 0.08513471, -26.71367894, -0.00153112, -32.75724867, -0.02159499, -3.27572487, -0.08513471, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23001, 3001, 0.0, 77.3956671, 0.0306224, 77.3956671, 0.09186721, 54.17696697, -6515.91355478, 0.05, 2, 0, 73001, 24001, 2, 3)
    ops.uniaxialMaterial('LimitState', 43001, 19.34891677, 9.773e-05, 58.04675032, 0.00029318, 193.48916775, 0.00097728, -19.34891677, -9.773e-05, -58.04675032, -0.00029318, -193.48916775, -0.00097728, 0.4, 0.3, 0.003, 0.0, 0.0, 23001, 2)
    ops.limitCurve('ThreePoint', 13001, 3001, 0.0, 77.3956671, 0.0306224, 77.3956671, 0.09186721, 54.17696697, -6515.91355478, 0.05, 2, 0, 73001, 24001, 1, 3)
    ops.uniaxialMaterial('LimitState', 33001, 19.34891677, 9.773e-05, 58.04675032, 0.00029318, 193.48916775, 0.00097728, -19.34891677, -9.773e-05, -58.04675032, -0.00029318, -193.48916775, -0.00097728, 0.4, 0.3, 0.003, 0.0, 0.0, 13001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3001, 99999, 'P', 43001, 'Vy', 33001, 'Vz', 23001, 'My', 13001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173001, 73001, 173001, 3001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124001, 124001, 24001, 3001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173002, 4.2, 0.0, 8.975)
    ops.node(124002, 4.2, 0.0, 11.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3002, 173002, 124002, 0.0625, 30497822.19991756, 12707425.91663232, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23002, 28.72257899, 0.00157623, 34.8426979, 0.02041043, 3.48426979, 0.08353846, -28.72257899, -0.00157623, -34.8426979, -0.02041043, -3.48426979, -0.08353846, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13002, 28.72257899, 0.00157623, 34.8426979, 0.02041043, 3.48426979, 0.08353846, -28.72257899, -0.00157623, -34.8426979, -0.02041043, -3.48426979, -0.08353846, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23002, 3002, 0.0, 88.10454685, 0.03152466, 88.10454685, 0.09457399, 61.6731828, -4318.82330567, 0.05, 2, 0, 73002, 24002, 2, 3)
    ops.uniaxialMaterial('LimitState', 43002, 22.02613671, 9.651e-05, 66.07841014, 0.00028954, 220.26136713, 0.00096512, -22.02613671, -9.651e-05, -66.07841014, -0.00028954, -220.26136713, -0.00096512, 0.4, 0.3, 0.003, 0.0, 0.0, 23002, 2)
    ops.limitCurve('ThreePoint', 13002, 3002, 0.0, 88.10454685, 0.03152466, 88.10454685, 0.09457399, 61.6731828, -4318.82330567, 0.05, 2, 0, 73002, 24002, 1, 3)
    ops.uniaxialMaterial('LimitState', 33002, 22.02613671, 9.651e-05, 66.07841014, 0.00028954, 220.26136713, 0.00096512, -22.02613671, -9.651e-05, -66.07841014, -0.00028954, -220.26136713, -0.00096512, 0.4, 0.3, 0.003, 0.0, 0.0, 13002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3002, 99999, 'P', 43002, 'Vy', 33002, 'Vz', 23002, 'My', 13002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173002, 73002, 173002, 3002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124002, 124002, 24002, 3002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173003, 8.4, 0.0, 8.975)
    ops.node(124003, 8.4, 0.0, 11.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3003, 173003, 124003, 0.0625, 30074904.86349335, 12531210.3597889, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23003, 29.56498441, 0.00156837, 35.90695602, 0.01786009, 3.5906956, 0.08081182, -29.56498441, -0.00156837, -35.90695602, -0.01786009, -3.5906956, -0.08081182, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13003, 29.56498441, 0.00156837, 35.90695602, 0.01786009, 3.5906956, 0.08081182, -29.56498441, -0.00156837, -35.90695602, -0.01786009, -3.5906956, -0.08081182, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23003, 3003, 0.0, 82.06918483, 0.03136737, 82.06918483, 0.0941021, 57.44842938, -3561.28772122, 0.05, 2, 0, 73003, 24003, 2, 3)
    ops.uniaxialMaterial('LimitState', 43003, 20.51729621, 9.116e-05, 61.55188863, 0.00027349, 205.17296208, 0.00091165, -20.51729621, -9.116e-05, -61.55188863, -0.00027349, -205.17296208, -0.00091165, 0.4, 0.3, 0.003, 0.0, 0.0, 23003, 2)
    ops.limitCurve('ThreePoint', 13003, 3003, 0.0, 82.06918483, 0.03136737, 82.06918483, 0.0941021, 57.44842938, -3561.28772122, 0.05, 2, 0, 73003, 24003, 1, 3)
    ops.uniaxialMaterial('LimitState', 33003, 20.51729621, 9.116e-05, 61.55188863, 0.00027349, 205.17296208, 0.00091165, -20.51729621, -9.116e-05, -61.55188863, -0.00027349, -205.17296208, -0.00091165, 0.4, 0.3, 0.003, 0.0, 0.0, 13003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3003, 99999, 'P', 43003, 'Vy', 33003, 'Vz', 23003, 'My', 13003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173003, 73003, 173003, 3003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124003, 124003, 24003, 3003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173006, 19.7, 0.0, 8.975)
    ops.node(124006, 19.7, 0.0, 11.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3006, 173006, 124006, 0.0625, 27992140.07958784, 11663391.69982827, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23006, 28.03351561, 0.00164552, 34.22214321, 0.02091832, 3.42221432, 0.08283247, -28.03351561, -0.00164552, -34.22214321, -0.02091832, -3.42221432, -0.08283247, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13006, 28.03351561, 0.00164552, 34.22214321, 0.02091832, 3.42221432, 0.08283247, -28.03351561, -0.00164552, -34.22214321, -0.02091832, -3.42221432, -0.08283247, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23006, 3006, 0.0, 83.0221024, 0.03291036, 83.0221024, 0.09873109, 58.11547168, -4239.24305713, 0.05, 2, 0, 73006, 24006, 2, 3)
    ops.uniaxialMaterial('LimitState', 43006, 20.7555256, 9.909e-05, 62.2665768, 0.00029726, 207.555256, 0.00099085, -20.7555256, -9.909e-05, -62.2665768, -0.00029726, -207.555256, -0.00099085, 0.4, 0.3, 0.003, 0.0, 0.0, 23006, 2)
    ops.limitCurve('ThreePoint', 13006, 3006, 0.0, 83.0221024, 0.03291036, 83.0221024, 0.09873109, 58.11547168, -4239.24305713, 0.05, 2, 0, 73006, 24006, 1, 3)
    ops.uniaxialMaterial('LimitState', 33006, 20.7555256, 9.909e-05, 62.2665768, 0.00029726, 207.555256, 0.00099085, -20.7555256, -9.909e-05, -62.2665768, -0.00029726, -207.555256, -0.00099085, 0.4, 0.3, 0.003, 0.0, 0.0, 13006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3006, 99999, 'P', 43006, 'Vy', 33006, 'Vz', 23006, 'My', 13006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173006, 73006, 173006, 3006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124006, 124006, 24006, 3006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173007, 23.9, 0.0, 8.975)
    ops.node(124007, 23.9, 0.0, 11.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3007, 173007, 124007, 0.0625, 28983819.67279368, 12076591.5303307, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23007, 28.86486957, 0.00162932, 35.15596184, 0.01692638, 3.51559618, 0.07937269, -28.86486957, -0.00162932, -35.15596184, -0.01692638, -3.51559618, -0.07937269, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13007, 28.86486957, 0.00162932, 35.15596184, 0.01692638, 3.51559618, 0.07937269, -28.86486957, -0.00162932, -35.15596184, -0.01692638, -3.51559618, -0.07937269, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23007, 3007, 0.0, 71.60193691, 0.03258643, 71.60193691, 0.09775929, 50.12135584, -3281.71786547, 0.05, 2, 0, 73007, 24007, 2, 3)
    ops.uniaxialMaterial('LimitState', 43007, 17.90048423, 8.253e-05, 53.70145269, 0.00024759, 179.00484229, 0.00082531, -17.90048423, -8.253e-05, -53.70145269, -0.00024759, -179.00484229, -0.00082531, 0.4, 0.3, 0.003, 0.0, 0.0, 23007, 2)
    ops.limitCurve('ThreePoint', 13007, 3007, 0.0, 71.60193691, 0.03258643, 71.60193691, 0.09775929, 50.12135584, -3281.71786547, 0.05, 2, 0, 73007, 24007, 1, 3)
    ops.uniaxialMaterial('LimitState', 33007, 17.90048423, 8.253e-05, 53.70145269, 0.00024759, 179.00484229, 0.00082531, -17.90048423, -8.253e-05, -53.70145269, -0.00024759, -179.00484229, -0.00082531, 0.4, 0.3, 0.003, 0.0, 0.0, 13007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3007, 99999, 'P', 43007, 'Vy', 33007, 'Vz', 23007, 'My', 13007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173007, 73007, 173007, 3007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124007, 124007, 24007, 3007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173008, 28.1, 0.0, 8.95)
    ops.node(124008, 28.1, 0.0, 11.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3008, 173008, 124008, 0.0625, 30008327.53956894, 12503469.80815372, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23008, 28.74326536, 0.00147464, 34.94770513, 0.01897099, 3.49477051, 0.08365792, -28.74326536, -0.00147464, -34.94770513, -0.01897099, -3.49477051, -0.08365792, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13008, 28.74326536, 0.00147464, 34.94770513, 0.01897099, 3.49477051, 0.08365792, -28.74326536, -0.00147464, -34.94770513, -0.01897099, -3.49477051, -0.08365792, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23008, 3008, 0.0, 82.26095384, 0.02949287, 82.26095384, 0.08847862, 57.58266769, -6165.6957263, 0.05, 2, 0, 73008, 24008, 2, 3)
    ops.uniaxialMaterial('LimitState', 43008, 20.56523846, 9.158e-05, 61.69571538, 0.00027474, 205.6523846, 0.0009158, -20.56523846, -9.158e-05, -61.69571538, -0.00027474, -205.6523846, -0.0009158, 0.4, 0.3, 0.003, 0.0, 0.0, 23008, 2)
    ops.limitCurve('ThreePoint', 13008, 3008, 0.0, 82.26095384, 0.02949287, 82.26095384, 0.08847862, 57.58266769, -6165.6957263, 0.05, 2, 0, 73008, 24008, 1, 3)
    ops.uniaxialMaterial('LimitState', 33008, 20.56523846, 9.158e-05, 61.69571538, 0.00027474, 205.6523846, 0.0009158, -20.56523846, -9.158e-05, -61.69571538, -0.00027474, -205.6523846, -0.0009158, 0.4, 0.3, 0.003, 0.0, 0.0, 13008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3008, 99999, 'P', 43008, 'Vy', 33008, 'Vz', 23008, 'My', 13008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173008, 73008, 173008, 3008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124008, 124008, 24008, 3008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173009, 0.0, 5.1, 8.95)
    ops.node(124009, 0.0, 5.1, 11.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3009, 173009, 124009, 0.0625, 30094446.48642823, 12539352.70267843, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23009, 29.04850186, 0.00148405, 35.27563942, 0.01713178, 3.52756394, 0.07997727, -29.04850186, -0.00148405, -35.27563942, -0.01713178, -3.52756394, -0.07997727, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13009, 29.04850186, 0.00148405, 35.27563942, 0.01713178, 3.52756394, 0.07997727, -29.04850186, -0.00148405, -35.27563942, -0.01713178, -3.52756394, -0.07997727, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23009, 3009, 0.0, 75.70971653, 0.02968102, 75.70971653, 0.08904305, 52.99680157, -3217.29183566, 0.05, 2, 0, 73009, 24009, 2, 3)
    ops.uniaxialMaterial('LimitState', 43009, 18.92742913, 8.405e-05, 56.7822874, 0.00025214, 189.27429132, 0.00084046, -18.92742913, -8.405e-05, -56.7822874, -0.00025214, -189.27429132, -0.00084046, 0.4, 0.3, 0.003, 0.0, 0.0, 23009, 2)
    ops.limitCurve('ThreePoint', 13009, 3009, 0.0, 75.70971653, 0.02968102, 75.70971653, 0.08904305, 52.99680157, -3217.29183566, 0.05, 2, 0, 73009, 24009, 1, 3)
    ops.uniaxialMaterial('LimitState', 33009, 18.92742913, 8.405e-05, 56.7822874, 0.00025214, 189.27429132, 0.00084046, -18.92742913, -8.405e-05, -56.7822874, -0.00025214, -189.27429132, -0.00084046, 0.4, 0.3, 0.003, 0.0, 0.0, 13009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3009, 99999, 'P', 43009, 'Vy', 33009, 'Vz', 23009, 'My', 13009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173009, 73009, 173009, 3009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124009, 124009, 24009, 3009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173010, 4.2, 5.1, 8.975)
    ops.node(124010, 4.2, 5.1, 11.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3010, 173010, 124010, 0.1225, 27721636.42604771, 11550681.84418655, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23010, 84.83421909, 0.00116587, 103.6626522, 0.01535021, 10.36626522, 0.06359128, -84.83421909, -0.00116587, -103.6626522, -0.01535021, -10.36626522, -0.06359128, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13010, 71.45791323, 0.00116587, 87.31755754, 0.01535021, 8.73175575, 0.06359128, -71.45791323, -0.00116587, -87.31755754, -0.01535021, -8.73175575, -0.06359128, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23010, 3010, 0.0, 121.77554561, 0.02331732, 121.77554561, 0.06995195, 85.24288193, -3859.86593748, 0.05, 2, 0, 73010, 24010, 2, 3)
    ops.uniaxialMaterial('LimitState', 43010, 30.4438864, 7.487e-05, 91.33165921, 0.00022462, 304.43886402, 0.00074875, -30.4438864, -7.487e-05, -91.33165921, -0.00022462, -304.43886402, -0.00074875, 0.4, 0.3, 0.003, 0.0, 0.0, 23010, 2)
    ops.limitCurve('ThreePoint', 13010, 3010, 0.0, 121.77554561, 0.02331732, 121.77554561, 0.06995195, 85.24288193, -3859.86593748, 0.05, 2, 0, 73010, 24010, 1, 3)
    ops.uniaxialMaterial('LimitState', 33010, 30.4438864, 7.487e-05, 91.33165921, 0.00022462, 304.43886402, 0.00074875, -30.4438864, -7.487e-05, -91.33165921, -0.00022462, -304.43886402, -0.00074875, 0.4, 0.3, 0.003, 0.0, 0.0, 13010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3010, 99999, 'P', 43010, 'Vy', 33010, 'Vz', 23010, 'My', 13010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173010, 73010, 173010, 3010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124010, 124010, 24010, 3010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173011, 8.4, 5.1, 8.975)
    ops.node(124011, 8.4, 5.1, 11.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3011, 173011, 124011, 0.1225, 31511334.20911921, 13129722.58713301, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23011, 86.07604672, 0.00108566, 104.12804134, 0.01532468, 10.41280413, 0.06473957, -86.07604672, -0.00108566, -104.12804134, -0.01532468, -10.41280413, -0.06473957, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13011, 72.33373446, 0.00108566, 87.50367122, 0.01532468, 8.75036712, 0.06473957, -72.33373446, -0.00108566, -87.50367122, -0.01532468, -8.75036712, -0.06473957, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23011, 3011, 0.0, 136.92674756, 0.02171316, 136.92674756, 0.06513949, 95.84872329, -4033.19812537, 0.05, 2, 0, 73011, 24011, 2, 3)
    ops.uniaxialMaterial('LimitState', 43011, 34.23168689, 7.407e-05, 102.69506067, 0.0002222, 342.31686889, 0.00074065, -34.23168689, -7.407e-05, -102.69506067, -0.0002222, -342.31686889, -0.00074065, 0.4, 0.3, 0.003, 0.0, 0.0, 23011, 2)
    ops.limitCurve('ThreePoint', 13011, 3011, 0.0, 136.92674756, 0.02171316, 136.92674756, 0.06513949, 95.84872329, -4033.19812537, 0.05, 2, 0, 73011, 24011, 1, 3)
    ops.uniaxialMaterial('LimitState', 33011, 34.23168689, 7.407e-05, 102.69506067, 0.0002222, 342.31686889, 0.00074065, -34.23168689, -7.407e-05, -102.69506067, -0.0002222, -342.31686889, -0.00074065, 0.4, 0.3, 0.003, 0.0, 0.0, 13011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3011, 99999, 'P', 43011, 'Vy', 33011, 'Vz', 23011, 'My', 13011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173011, 73011, 173011, 3011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124011, 124011, 24011, 3011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173012, 12.6, 5.1, 8.95)
    ops.node(124012, 12.6, 5.1, 11.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3012, 173012, 124012, 0.1225, 30731220.86119926, 12804675.35883303, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23012, 85.10034853, 0.00110633, 103.16711878, 0.01486818, 10.31671188, 0.06373316, -85.10034853, -0.00110633, -103.16711878, -0.01486818, -10.31671188, -0.06373316, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13012, 72.08522691, 0.00110633, 87.38889199, 0.01486818, 8.7388892, 0.06373316, -72.08522691, -0.00110633, -87.38889199, -0.01486818, -8.7388892, -0.06373316, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23012, 3012, 0.0, 135.31261589, 0.02212651, 135.31261589, 0.06637953, 94.71883112, -3718.96163784, 0.05, 2, 0, 73012, 24012, 2, 3)
    ops.uniaxialMaterial('LimitState', 43012, 33.82815397, 7.505e-05, 101.48446192, 0.00022515, 338.28153972, 0.0007505, -33.82815397, -7.505e-05, -101.48446192, -0.00022515, -338.28153972, -0.0007505, 0.4, 0.3, 0.003, 0.0, 0.0, 23012, 2)
    ops.limitCurve('ThreePoint', 13012, 3012, 0.0, 135.31261589, 0.02212651, 135.31261589, 0.06637953, 94.71883112, -3718.96163784, 0.05, 2, 0, 73012, 24012, 1, 3)
    ops.uniaxialMaterial('LimitState', 33012, 33.82815397, 7.505e-05, 101.48446192, 0.00022515, 338.28153972, 0.0007505, -33.82815397, -7.505e-05, -101.48446192, -0.00022515, -338.28153972, -0.0007505, 0.4, 0.3, 0.003, 0.0, 0.0, 13012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3012, 99999, 'P', 43012, 'Vy', 33012, 'Vz', 23012, 'My', 13012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173012, 73012, 173012, 3012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124012, 124012, 24012, 3012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173013, 15.5, 5.1, 8.95)
    ops.node(124013, 15.5, 5.1, 11.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3013, 173013, 124013, 0.1225, 27464014.03053401, 11443339.17938917, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23013, 82.80254789, 0.00124254, 101.19999882, 0.01557667, 10.11999988, 0.06320686, -82.80254789, -0.00124254, -101.19999882, -0.01557667, -10.11999988, -0.06320686, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13013, 71.28721336, 0.00124254, 87.12613429, 0.01557667, 8.71261343, 0.06320686, -71.28721336, -0.00124254, -87.12613429, -0.01557667, -8.71261343, -0.06320686, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23013, 3013, 0.0, 122.11547849, 0.02485081, 122.11547849, 0.07455243, 85.48083494, -3559.09174364, 0.05, 2, 0, 73013, 24013, 2, 3)
    ops.uniaxialMaterial('LimitState', 43013, 30.52886962, 7.579e-05, 91.58660887, 0.00022736, 305.28869623, 0.00075788, -30.52886962, -7.579e-05, -91.58660887, -0.00022736, -305.28869623, -0.00075788, 0.4, 0.3, 0.003, 0.0, 0.0, 23013, 2)
    ops.limitCurve('ThreePoint', 13013, 3013, 0.0, 122.11547849, 0.02485081, 122.11547849, 0.07455243, 85.48083494, -3559.09174364, 0.05, 2, 0, 73013, 24013, 1, 3)
    ops.uniaxialMaterial('LimitState', 33013, 30.52886962, 7.579e-05, 91.58660887, 0.00022736, 305.28869623, 0.00075788, -30.52886962, -7.579e-05, -91.58660887, -0.00022736, -305.28869623, -0.00075788, 0.4, 0.3, 0.003, 0.0, 0.0, 13013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3013, 99999, 'P', 43013, 'Vy', 33013, 'Vz', 23013, 'My', 13013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173013, 73013, 173013, 3013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124013, 124013, 24013, 3013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173014, 19.7, 5.1, 8.975)
    ops.node(124014, 19.7, 5.1, 11.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3014, 173014, 124014, 0.1225, 31394325.75117134, 13080969.06298806, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23014, 83.34210972, 0.00104666, 100.85765712, 0.01602792, 10.08576571, 0.065415, -83.34210972, -0.00104666, -100.85765712, -0.01602792, -10.08576571, -0.065415, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13014, 70.0136972, 0.00104666, 84.72808632, 0.01602792, 8.47280863, 0.065415, -70.0136972, -0.00104666, -84.72808632, -0.01602792, -8.47280863, -0.065415, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23014, 3014, 0.0, 139.76239636, 0.0209332, 139.76239636, 0.0627996, 97.83367745, -4410.72596339, 0.05, 2, 0, 73014, 24014, 2, 3)
    ops.uniaxialMaterial('LimitState', 43014, 34.94059909, 7.588e-05, 104.82179727, 0.00022764, 349.4059909, 0.00075881, -34.94059909, -7.588e-05, -104.82179727, -0.00022764, -349.4059909, -0.00075881, 0.4, 0.3, 0.003, 0.0, 0.0, 23014, 2)
    ops.limitCurve('ThreePoint', 13014, 3014, 0.0, 139.76239636, 0.0209332, 139.76239636, 0.0627996, 97.83367745, -4410.72596339, 0.05, 2, 0, 73014, 24014, 1, 3)
    ops.uniaxialMaterial('LimitState', 33014, 34.94059909, 7.588e-05, 104.82179727, 0.00022764, 349.4059909, 0.00075881, -34.94059909, -7.588e-05, -104.82179727, -0.00022764, -349.4059909, -0.00075881, 0.4, 0.3, 0.003, 0.0, 0.0, 13014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3014, 99999, 'P', 43014, 'Vy', 33014, 'Vz', 23014, 'My', 13014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173014, 73014, 173014, 3014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124014, 124014, 24014, 3014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173015, 23.9, 5.1, 8.975)
    ops.node(124015, 23.9, 5.1, 11.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3015, 173015, 124015, 0.1225, 30556854.34638626, 12732022.64432761, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23015, 83.05919496, 0.0011244, 100.7683658, 0.01729133, 10.07683658, 0.06646608, -83.05919496, -0.0011244, -100.7683658, -0.01729133, -10.07683658, -0.06646608, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13015, 70.63129793, 0.0011244, 85.6906989, 0.01729133, 8.56906989, 0.06646608, -70.63129793, -0.0011244, -85.6906989, -0.01729133, -8.56906989, -0.06646608, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23015, 3015, 0.0, 141.6776632, 0.02248801, 141.6776632, 0.06746404, 99.17436424, -5021.48972646, 0.05, 2, 0, 73015, 24015, 2, 3)
    ops.uniaxialMaterial('LimitState', 43015, 35.4194158, 7.903e-05, 106.2582474, 0.00023709, 354.194158, 0.00079029, -35.4194158, -7.903e-05, -106.2582474, -0.00023709, -354.194158, -0.00079029, 0.4, 0.3, 0.003, 0.0, 0.0, 23015, 2)
    ops.limitCurve('ThreePoint', 13015, 3015, 0.0, 141.6776632, 0.02248801, 141.6776632, 0.06746404, 99.17436424, -5021.48972646, 0.05, 2, 0, 73015, 24015, 1, 3)
    ops.uniaxialMaterial('LimitState', 33015, 35.4194158, 7.903e-05, 106.2582474, 0.00023709, 354.194158, 0.00079029, -35.4194158, -7.903e-05, -106.2582474, -0.00023709, -354.194158, -0.00079029, 0.4, 0.3, 0.003, 0.0, 0.0, 13015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3015, 99999, 'P', 43015, 'Vy', 33015, 'Vz', 23015, 'My', 13015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173015, 73015, 173015, 3015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124015, 124015, 24015, 3015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173016, 28.1, 5.1, 8.95)
    ops.node(124016, 28.1, 5.1, 11.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3016, 173016, 124016, 0.0625, 30862593.77642816, 12859414.07351173, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23016, 27.46402966, 0.00168824, 33.27894572, 0.01899252, 3.32789457, 0.08215879, -27.46402966, -0.00168824, -33.27894572, -0.01899252, -3.32789457, -0.08215879, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13016, 27.46402966, 0.00168824, 33.27894572, 0.01899252, 3.32789457, 0.08215879, -27.46402966, -0.00168824, -33.27894572, -0.01899252, -3.32789457, -0.08215879, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23016, 3016, 0.0, 86.69251059, 0.03376472, 86.69251059, 0.10129416, 60.68475742, -3905.34136605, 0.05, 2, 0, 73016, 24016, 2, 3)
    ops.uniaxialMaterial('LimitState', 43016, 21.67312765, 9.384e-05, 65.01938295, 0.00028153, 216.73127648, 0.00093843, -21.67312765, -9.384e-05, -65.01938295, -0.00028153, -216.73127648, -0.00093843, 0.4, 0.3, 0.003, 0.0, 0.0, 23016, 2)
    ops.limitCurve('ThreePoint', 13016, 3016, 0.0, 86.69251059, 0.03376472, 86.69251059, 0.10129416, 60.68475742, -3905.34136605, 0.05, 2, 0, 73016, 24016, 1, 3)
    ops.uniaxialMaterial('LimitState', 33016, 21.67312765, 9.384e-05, 65.01938295, 0.00028153, 216.73127648, 0.00093843, -21.67312765, -9.384e-05, -65.01938295, -0.00028153, -216.73127648, -0.00093843, 0.4, 0.3, 0.003, 0.0, 0.0, 13016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3016, 99999, 'P', 43016, 'Vy', 33016, 'Vz', 23016, 'My', 13016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173016, 73016, 173016, 3016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124016, 124016, 24016, 3016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173017, 0.0, 10.2, 8.95)
    ops.node(124017, 0.0, 10.2, 11.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3017, 173017, 124017, 0.0625, 29544038.93459187, 12310016.22274661, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23017, 31.16989344, 0.00158968, 37.90787476, 0.0193309, 3.79078748, 0.08195444, -31.16989344, -0.00158968, -37.90787476, -0.0193309, -3.79078748, -0.08195444, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13017, 31.16989344, 0.00158968, 37.90787476, 0.0193309, 3.79078748, 0.08195444, -31.16989344, -0.00158968, -37.90787476, -0.0193309, -3.79078748, -0.08195444, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23017, 3017, 0.0, 84.85726313, 0.0317936, 84.85726313, 0.09538081, 59.40008419, -4017.60697304, 0.05, 2, 0, 73017, 24017, 2, 3)
    ops.uniaxialMaterial('LimitState', 43017, 21.21431578, 9.596e-05, 63.64294735, 0.00028787, 212.14315782, 0.00095955, -21.21431578, -9.596e-05, -63.64294735, -0.00028787, -212.14315782, -0.00095955, 0.4, 0.3, 0.003, 0.0, 0.0, 23017, 2)
    ops.limitCurve('ThreePoint', 13017, 3017, 0.0, 84.85726313, 0.0317936, 84.85726313, 0.09538081, 59.40008419, -4017.60697304, 0.05, 2, 0, 73017, 24017, 1, 3)
    ops.uniaxialMaterial('LimitState', 33017, 21.21431578, 9.596e-05, 63.64294735, 0.00028787, 212.14315782, 0.00095955, -21.21431578, -9.596e-05, -63.64294735, -0.00028787, -212.14315782, -0.00095955, 0.4, 0.3, 0.003, 0.0, 0.0, 13017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3017, 99999, 'P', 43017, 'Vy', 33017, 'Vz', 23017, 'My', 13017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173017, 73017, 173017, 3017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124017, 124017, 24017, 3017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173018, 4.2, 10.2, 8.975)
    ops.node(124018, 4.2, 10.2, 11.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3018, 173018, 124018, 0.1225, 28027554.32497219, 11678147.63540508, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23018, 93.25520527, 0.00130706, 113.87751371, 0.01791835, 11.38775137, 0.06037979, -93.25520527, -0.00130706, -113.87751371, -0.01791835, -11.38775137, -0.06037979, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13018, 87.06285305, 0.00130706, 106.31579452, 0.01791835, 10.63157945, 0.06037979, -87.06285305, -0.00130706, -106.31579452, -0.01791835, -10.63157945, -0.06037979, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23018, 3018, 0.0, 117.51316292, 0.02614124, 117.51316292, 0.07842373, 82.25921404, -3316.1593111, 0.05, 2, 0, 73018, 24018, 2, 3)
    ops.uniaxialMaterial('LimitState', 43018, 29.37829073, 7.147e-05, 88.13487219, 0.0002144, 293.7829073, 0.00071465, -29.37829073, -7.147e-05, -88.13487219, -0.0002144, -293.7829073, -0.00071465, 0.4, 0.3, 0.003, 0.0, 0.0, 23018, 2)
    ops.limitCurve('ThreePoint', 13018, 3018, 0.0, 117.51316292, 0.02614124, 117.51316292, 0.07842373, 82.25921404, -3316.1593111, 0.05, 2, 0, 73018, 24018, 1, 3)
    ops.uniaxialMaterial('LimitState', 33018, 29.37829073, 7.147e-05, 88.13487219, 0.0002144, 293.7829073, 0.00071465, -29.37829073, -7.147e-05, -88.13487219, -0.0002144, -293.7829073, -0.00071465, 0.4, 0.3, 0.003, 0.0, 0.0, 13018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3018, 99999, 'P', 43018, 'Vy', 33018, 'Vz', 23018, 'My', 13018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173018, 73018, 173018, 3018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124018, 124018, 24018, 3018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173019, 8.4, 10.2, 8.975)
    ops.node(124019, 8.4, 10.2, 11.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3019, 173019, 124019, 0.1225, 31913744.87390431, 13297393.69746013, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23019, 97.19922257, 0.00116712, 117.43401829, 0.01718345, 11.74340183, 0.06064372, -97.19922257, -0.00116712, -117.43401829, -0.01718345, -11.74340183, -0.06064372, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13019, 90.23447082, 0.00116712, 109.01935444, 0.01718345, 10.90193544, 0.06064372, -90.23447082, -0.00116712, -109.01935444, -0.01718345, -10.90193544, -0.06064372, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23019, 3019, 0.0, 135.35284034, 0.02334242, 135.35284034, 0.07002725, 94.74698824, -3716.30886812, 0.05, 2, 0, 73019, 24019, 2, 3)
    ops.uniaxialMaterial('LimitState', 43019, 33.83821008, 7.229e-05, 101.51463025, 0.00021687, 338.38210084, 0.00072291, -33.83821008, -7.229e-05, -101.51463025, -0.00021687, -338.38210084, -0.00072291, 0.4, 0.3, 0.003, 0.0, 0.0, 23019, 2)
    ops.limitCurve('ThreePoint', 13019, 3019, 0.0, 135.35284034, 0.02334242, 135.35284034, 0.07002725, 94.74698824, -3716.30886812, 0.05, 2, 0, 73019, 24019, 1, 3)
    ops.uniaxialMaterial('LimitState', 33019, 33.83821008, 7.229e-05, 101.51463025, 0.00021687, 338.38210084, 0.00072291, -33.83821008, -7.229e-05, -101.51463025, -0.00021687, -338.38210084, -0.00072291, 0.4, 0.3, 0.003, 0.0, 0.0, 13019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3019, 99999, 'P', 43019, 'Vy', 33019, 'Vz', 23019, 'My', 13019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173019, 73019, 173019, 3019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124019, 124019, 24019, 3019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173020, 12.6, 10.2, 8.95)
    ops.node(124020, 12.6, 10.2, 11.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3020, 173020, 124020, 0.0625, 29764747.63168217, 12401978.17986757, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23020, 28.78356606, 0.00158786, 34.95977158, 0.01966981, 3.49597716, 0.08103713, -28.78356606, -0.00158786, -34.95977158, -0.01966981, -3.49597716, -0.08103713, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13020, 28.78356606, 0.00158786, 34.95977158, 0.01966981, 3.49597716, 0.08103713, -28.78356606, -0.00158786, -34.95977158, -0.01966981, -3.49597716, -0.08103713, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23020, 3020, 0.0, 86.56864594, 0.03175711, 86.56864594, 0.09527132, 60.59805216, -3272.92979018, 0.05, 2, 0, 73020, 24020, 2, 3)
    ops.uniaxialMaterial('LimitState', 43020, 21.64216149, 9.716e-05, 64.92648446, 0.00029149, 216.42161486, 0.00097165, -21.64216149, -9.716e-05, -64.92648446, -0.00029149, -216.42161486, -0.00097165, 0.4, 0.3, 0.003, 0.0, 0.0, 23020, 2)
    ops.limitCurve('ThreePoint', 13020, 3020, 0.0, 86.56864594, 0.03175711, 86.56864594, 0.09527132, 60.59805216, -3272.92979018, 0.05, 2, 0, 73020, 24020, 1, 3)
    ops.uniaxialMaterial('LimitState', 33020, 21.64216149, 9.716e-05, 64.92648446, 0.00029149, 216.42161486, 0.00097165, -21.64216149, -9.716e-05, -64.92648446, -0.00029149, -216.42161486, -0.00097165, 0.4, 0.3, 0.003, 0.0, 0.0, 13020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3020, 99999, 'P', 43020, 'Vy', 33020, 'Vz', 23020, 'My', 13020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173020, 73020, 173020, 3020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124020, 124020, 24020, 3020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173021, 15.5, 10.2, 8.95)
    ops.node(124021, 15.5, 10.2, 11.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3021, 173021, 124021, 0.0625, 28663377.06654114, 11943073.77772548, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23021, 30.67189807, 0.00154003, 37.35251968, 0.02096363, 3.73525197, 0.08162022, -30.67189807, -0.00154003, -37.35251968, -0.02096363, -3.73525197, -0.08162022, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13021, 30.67189807, 0.00154003, 37.35251968, 0.02096363, 3.73525197, 0.08162022, -30.67189807, -0.00154003, -37.35251968, -0.02096363, -3.73525197, -0.08162022, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23021, 3021, 0.0, 86.3794263, 0.03080059, 86.3794263, 0.09240176, 60.46559841, -3480.86521622, 0.05, 2, 0, 73021, 24021, 2, 3)
    ops.uniaxialMaterial('LimitState', 43021, 21.59485658, 0.00010068, 64.78456973, 0.00030203, 215.94856575, 0.00100678, -21.59485658, -0.00010068, -64.78456973, -0.00030203, -215.94856575, -0.00100678, 0.4, 0.3, 0.003, 0.0, 0.0, 23021, 2)
    ops.limitCurve('ThreePoint', 13021, 3021, 0.0, 86.3794263, 0.03080059, 86.3794263, 0.09240176, 60.46559841, -3480.86521622, 0.05, 2, 0, 73021, 24021, 1, 3)
    ops.uniaxialMaterial('LimitState', 33021, 21.59485658, 0.00010068, 64.78456973, 0.00030203, 215.94856575, 0.00100678, -21.59485658, -0.00010068, -64.78456973, -0.00030203, -215.94856575, -0.00100678, 0.4, 0.3, 0.003, 0.0, 0.0, 13021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3021, 99999, 'P', 43021, 'Vy', 33021, 'Vz', 23021, 'My', 13021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173021, 73021, 173021, 3021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124021, 124021, 24021, 3021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173022, 19.7, 10.2, 8.975)
    ops.node(124022, 19.7, 10.2, 11.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3022, 173022, 124022, 0.1225, 28259953.11707816, 11774980.46544923, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23022, 94.74168777, 0.00122487, 115.63144964, 0.01832139, 11.56314496, 0.06085919, -94.74168777, -0.00122487, -115.63144964, -0.01832139, -11.56314496, -0.06085919, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13022, 87.92592242, 0.00122487, 107.31286416, 0.01832139, 10.73128642, 0.06085919, -87.92592242, -0.00122487, -107.31286416, -0.01832139, -10.73128642, -0.06085919, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23022, 3022, 0.0, 121.20570343, 0.02449747, 121.20570343, 0.07349242, 84.8439924, -3619.03784435, 0.05, 2, 0, 73022, 24022, 2, 3)
    ops.uniaxialMaterial('LimitState', 43022, 30.30142586, 7.31e-05, 90.90427757, 0.00021931, 303.01425858, 0.00073105, -30.30142586, -7.31e-05, -90.90427757, -0.00021931, -303.01425858, -0.00073105, 0.4, 0.3, 0.003, 0.0, 0.0, 23022, 2)
    ops.limitCurve('ThreePoint', 13022, 3022, 0.0, 121.20570343, 0.02449747, 121.20570343, 0.07349242, 84.8439924, -3619.03784435, 0.05, 2, 0, 73022, 24022, 1, 3)
    ops.uniaxialMaterial('LimitState', 33022, 30.30142586, 7.31e-05, 90.90427757, 0.00021931, 303.01425858, 0.00073105, -30.30142586, -7.31e-05, -90.90427757, -0.00021931, -303.01425858, -0.00073105, 0.4, 0.3, 0.003, 0.0, 0.0, 13022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3022, 99999, 'P', 43022, 'Vy', 33022, 'Vz', 23022, 'My', 13022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173022, 73022, 173022, 3022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124022, 124022, 24022, 3022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173023, 23.9, 10.2, 8.975)
    ops.node(124023, 23.9, 10.2, 11.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3023, 173023, 124023, 0.1225, 31857286.53821601, 13273869.39092334, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23023, 95.49206348, 0.00126814, 115.39260994, 0.0182944, 11.53926099, 0.06174362, -95.49206348, -0.00126814, -115.39260994, -0.0182944, -11.53926099, -0.06174362, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13023, 89.37310769, 0.00126814, 107.99846373, 0.0182944, 10.79984637, 0.06174362, -89.37310769, -0.00126814, -107.99846373, -0.0182944, -10.79984637, -0.06174362, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23023, 3023, 0.0, 137.77857579, 0.02536274, 137.77857579, 0.07608822, 96.44500305, -4008.55158834, 0.05, 2, 0, 73023, 24023, 2, 3)
    ops.uniaxialMaterial('LimitState', 43023, 34.44464395, 7.372e-05, 103.33393184, 0.00022115, 344.44643948, 0.00073717, -34.44464395, -7.372e-05, -103.33393184, -0.00022115, -344.44643948, -0.00073717, 0.4, 0.3, 0.003, 0.0, 0.0, 23023, 2)
    ops.limitCurve('ThreePoint', 13023, 3023, 0.0, 137.77857579, 0.02536274, 137.77857579, 0.07608822, 96.44500305, -4008.55158834, 0.05, 2, 0, 73023, 24023, 1, 3)
    ops.uniaxialMaterial('LimitState', 33023, 34.44464395, 7.372e-05, 103.33393184, 0.00022115, 344.44643948, 0.00073717, -34.44464395, -7.372e-05, -103.33393184, -0.00022115, -344.44643948, -0.00073717, 0.4, 0.3, 0.003, 0.0, 0.0, 13023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3023, 99999, 'P', 43023, 'Vy', 33023, 'Vz', 23023, 'My', 13023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173023, 73023, 173023, 3023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124023, 124023, 24023, 3023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173024, 28.1, 10.2, 8.95)
    ops.node(124024, 28.1, 10.2, 11.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3024, 173024, 124024, 0.0625, 28997101.49415643, 12082125.62256518, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23024, 29.66730943, 0.00152128, 36.13022547, 0.01959641, 3.61302255, 0.081952, -29.66730943, -0.00152128, -36.13022547, -0.01959641, -3.61302255, -0.081952, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13024, 29.66730943, 0.00152128, 36.13022547, 0.01959641, 3.61302255, 0.081952, -29.66730943, -0.00152128, -36.13022547, -0.01959641, -3.61302255, -0.081952, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23024, 3024, 0.0, 83.07081584, 0.03042553, 83.07081584, 0.09127658, 58.14957109, -3904.19158952, 0.05, 2, 0, 73024, 24024, 2, 3)
    ops.uniaxialMaterial('LimitState', 43024, 20.76770396, 9.571e-05, 62.30311188, 0.00028712, 207.6770396, 0.00095707, -20.76770396, -9.571e-05, -62.30311188, -0.00028712, -207.6770396, -0.00095707, 0.4, 0.3, 0.003, 0.0, 0.0, 23024, 2)
    ops.limitCurve('ThreePoint', 13024, 3024, 0.0, 83.07081584, 0.03042553, 83.07081584, 0.09127658, 58.14957109, -3904.19158952, 0.05, 2, 0, 73024, 24024, 1, 3)
    ops.uniaxialMaterial('LimitState', 33024, 20.76770396, 9.571e-05, 62.30311188, 0.00028712, 207.6770396, 0.00095707, -20.76770396, -9.571e-05, -62.30311188, -0.00028712, -207.6770396, -0.00095707, 0.4, 0.3, 0.003, 0.0, 0.0, 13024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3024, 99999, 'P', 43024, 'Vy', 33024, 'Vz', 23024, 'My', 13024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173024, 73024, 173024, 3024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124024, 124024, 24024, 3024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173025, 0.0, 15.3, 8.95)
    ops.node(124025, 0.0, 15.3, 11.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3025, 173025, 124025, 0.0625, 29529951.88257354, 12304146.61773898, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23025, 29.14879448, 0.00153344, 35.4876224, 0.02099463, 3.54876224, 0.08555957, -29.14879448, -0.00153344, -35.4876224, -0.02099463, -3.54876224, -0.08555957, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13025, 29.14879448, 0.00153344, 35.4876224, 0.02099463, 3.54876224, 0.08555957, -29.14879448, -0.00153344, -35.4876224, -0.02099463, -3.54876224, -0.08555957, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23025, 3025, 0.0, 84.885586, 0.03066878, 84.885586, 0.09200634, 59.4199102, -7045.68956287, 0.05, 2, 0, 73025, 24025, 2, 3)
    ops.uniaxialMaterial('LimitState', 43025, 21.2213965, 9.603e-05, 63.6641895, 0.0002881, 212.21396499, 0.00096033, -21.2213965, -9.603e-05, -63.6641895, -0.0002881, -212.21396499, -0.00096033, 0.4, 0.3, 0.003, 0.0, 0.0, 23025, 2)
    ops.limitCurve('ThreePoint', 13025, 3025, 0.0, 84.885586, 0.03066878, 84.885586, 0.09200634, 59.4199102, -7045.68956287, 0.05, 2, 0, 73025, 24025, 1, 3)
    ops.uniaxialMaterial('LimitState', 33025, 21.2213965, 9.603e-05, 63.6641895, 0.0002881, 212.21396499, 0.00096033, -21.2213965, -9.603e-05, -63.6641895, -0.0002881, -212.21396499, -0.00096033, 0.4, 0.3, 0.003, 0.0, 0.0, 13025, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3025, 99999, 'P', 43025, 'Vy', 33025, 'Vz', 23025, 'My', 13025, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173025, 73025, 173025, 3025, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124025, 124025, 24025, 3025, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173026, 4.2, 15.3, 8.975)
    ops.node(124026, 4.2, 15.3, 11.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3026, 173026, 124026, 0.0625, 29840476.87872986, 12433532.03280411, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23026, 29.94338773, 0.00152389, 36.38959306, 0.01915097, 3.63895931, 0.08200048, -29.94338773, -0.00152389, -36.38959306, -0.01915097, -3.63895931, -0.08200048, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13026, 29.94338773, 0.00152389, 36.38959306, 0.01915097, 3.63895931, 0.08200048, -29.94338773, -0.00152389, -36.38959306, -0.01915097, -3.63895931, -0.08200048, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23026, 3026, 0.0, 83.61542402, 0.03047773, 83.61542402, 0.09143318, 58.53079681, -3838.34514658, 0.05, 2, 0, 73026, 24026, 2, 3)
    ops.uniaxialMaterial('LimitState', 43026, 20.903856, 9.361e-05, 62.71156801, 0.00028084, 209.03856004, 0.00093612, -20.903856, -9.361e-05, -62.71156801, -0.00028084, -209.03856004, -0.00093612, 0.4, 0.3, 0.003, 0.0, 0.0, 23026, 2)
    ops.limitCurve('ThreePoint', 13026, 3026, 0.0, 83.61542402, 0.03047773, 83.61542402, 0.09143318, 58.53079681, -3838.34514658, 0.05, 2, 0, 73026, 24026, 1, 3)
    ops.uniaxialMaterial('LimitState', 33026, 20.903856, 9.361e-05, 62.71156801, 0.00028084, 209.03856004, 0.00093612, -20.903856, -9.361e-05, -62.71156801, -0.00028084, -209.03856004, -0.00093612, 0.4, 0.3, 0.003, 0.0, 0.0, 13026, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3026, 99999, 'P', 43026, 'Vy', 33026, 'Vz', 23026, 'My', 13026, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173026, 73026, 173026, 3026, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124026, 124026, 24026, 3026, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173027, 8.4, 15.3, 8.975)
    ops.node(124027, 8.4, 15.3, 11.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3027, 173027, 124027, 0.0625, 31053670.81572603, 12939029.50655251, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23027, 29.84221924, 0.00157588, 36.14218736, 0.01782376, 3.61421874, 0.08116868, -29.84221924, -0.00157588, -36.14218736, -0.01782376, -3.61421874, -0.08116868, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13027, 29.84221924, 0.00157588, 36.14218736, 0.01782376, 3.61421874, 0.08116868, -29.84221924, -0.00157588, -36.14218736, -0.01782376, -3.61421874, -0.08116868, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23027, 3027, 0.0, 83.41928445, 0.03151767, 83.41928445, 0.09455301, 58.39349911, -3495.51728665, 0.05, 2, 0, 73027, 24027, 2, 3)
    ops.uniaxialMaterial('LimitState', 43027, 20.85482111, 8.974e-05, 62.56446333, 0.00026923, 208.54821112, 0.00089744, -20.85482111, -8.974e-05, -62.56446333, -0.00026923, -208.54821112, -0.00089744, 0.4, 0.3, 0.003, 0.0, 0.0, 23027, 2)
    ops.limitCurve('ThreePoint', 13027, 3027, 0.0, 83.41928445, 0.03151767, 83.41928445, 0.09455301, 58.39349911, -3495.51728665, 0.05, 2, 0, 73027, 24027, 1, 3)
    ops.uniaxialMaterial('LimitState', 33027, 20.85482111, 8.974e-05, 62.56446333, 0.00026923, 208.54821112, 0.00089744, -20.85482111, -8.974e-05, -62.56446333, -0.00026923, -208.54821112, -0.00089744, 0.4, 0.3, 0.003, 0.0, 0.0, 13027, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3027, 99999, 'P', 43027, 'Vy', 33027, 'Vz', 23027, 'My', 13027, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173027, 73027, 173027, 3027, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124027, 124027, 24027, 3027, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173028, 12.6, 15.3, 8.95)
    ops.node(124028, 12.6, 15.3, 11.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3028, 173028, 124028, 0.0625, 29911446.83995828, 12463102.84998262, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23028, 28.31025726, 0.00134683, 34.40970682, 0.02171005, 3.44097068, 0.08521362, -28.31025726, -0.00134683, -34.40970682, -0.02171005, -3.44097068, -0.08521362, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13028, 28.31025726, 0.00134683, 34.40970682, 0.02171005, 3.44097068, 0.08521362, -28.31025726, -0.00134683, -34.40970682, -0.02171005, -3.44097068, -0.08521362, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23028, 3028, 0.0, 89.31385826, 0.02693655, 89.31385826, 0.08080965, 62.51970078, -5453.5730423, 0.05, 2, 0, 73028, 24028, 2, 3)
    ops.uniaxialMaterial('LimitState', 43028, 22.32846456, 9.975e-05, 66.98539369, 0.00029926, 223.28464564, 0.00099754, -22.32846456, -9.975e-05, -66.98539369, -0.00029926, -223.28464564, -0.00099754, 0.4, 0.3, 0.003, 0.0, 0.0, 23028, 2)
    ops.limitCurve('ThreePoint', 13028, 3028, 0.0, 89.31385826, 0.02693655, 89.31385826, 0.08080965, 62.51970078, -5453.5730423, 0.05, 2, 0, 73028, 24028, 1, 3)
    ops.uniaxialMaterial('LimitState', 33028, 22.32846456, 9.975e-05, 66.98539369, 0.00029926, 223.28464564, 0.00099754, -22.32846456, -9.975e-05, -66.98539369, -0.00029926, -223.28464564, -0.00099754, 0.4, 0.3, 0.003, 0.0, 0.0, 13028, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3028, 99999, 'P', 43028, 'Vy', 33028, 'Vz', 23028, 'My', 13028, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173028, 73028, 173028, 3028, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124028, 124028, 24028, 3028, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173029, 15.5, 15.3, 8.95)
    ops.node(124029, 15.5, 15.3, 11.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3029, 173029, 124029, 0.0625, 27762106.93672669, 11567544.55696946, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23029, 30.4094009, 0.00159457, 37.15676583, 0.0202995, 3.71567658, 0.08286452, -30.4094009, -0.00159457, -37.15676583, -0.0202995, -3.71567658, -0.08286452, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13029, 30.4094009, 0.00159457, 37.15676583, 0.0202995, 3.71567658, 0.08286452, -30.4094009, -0.00159457, -37.15676583, -0.0202995, -3.71567658, -0.08286452, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23029, 3029, 0.0, 82.9084082, 0.03189143, 82.9084082, 0.0956743, 58.03588574, -4993.46823976, 0.05, 2, 0, 73029, 24029, 2, 3)
    ops.uniaxialMaterial('LimitState', 43029, 20.72710205, 9.977e-05, 62.18130615, 0.00029931, 207.2710205, 0.00099769, -20.72710205, -9.977e-05, -62.18130615, -0.00029931, -207.2710205, -0.00099769, 0.4, 0.3, 0.003, 0.0, 0.0, 23029, 2)
    ops.limitCurve('ThreePoint', 13029, 3029, 0.0, 82.9084082, 0.03189143, 82.9084082, 0.0956743, 58.03588574, -4993.46823976, 0.05, 2, 0, 73029, 24029, 1, 3)
    ops.uniaxialMaterial('LimitState', 33029, 20.72710205, 9.977e-05, 62.18130615, 0.00029931, 207.2710205, 0.00099769, -20.72710205, -9.977e-05, -62.18130615, -0.00029931, -207.2710205, -0.00099769, 0.4, 0.3, 0.003, 0.0, 0.0, 13029, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3029, 99999, 'P', 43029, 'Vy', 33029, 'Vz', 23029, 'My', 13029, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173029, 73029, 173029, 3029, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124029, 124029, 24029, 3029, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173030, 19.7, 15.3, 8.975)
    ops.node(124030, 19.7, 15.3, 11.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3030, 173030, 124030, 0.0625, 29760943.88531344, 12400393.28554727, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23030, 31.2818626, 0.00154855, 38.02426757, 0.01862479, 3.80242676, 0.08143886, -31.2818626, -0.00154855, -38.02426757, -0.01862479, -3.80242676, -0.08143886, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13030, 31.2818626, 0.00154855, 38.02426757, 0.01862479, 3.80242676, 0.08143886, -31.2818626, -0.00154855, -38.02426757, -0.01862479, -3.80242676, -0.08143886, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23030, 3030, 0.0, 83.63622562, 0.03097099, 83.63622562, 0.09291296, 58.54535793, -3862.21994603, 0.05, 2, 0, 73030, 24030, 2, 3)
    ops.uniaxialMaterial('LimitState', 43030, 20.90905641, 9.389e-05, 62.72716922, 0.00028166, 209.09056405, 0.00093885, -20.90905641, -9.389e-05, -62.72716922, -0.00028166, -209.09056405, -0.00093885, 0.4, 0.3, 0.003, 0.0, 0.0, 23030, 2)
    ops.limitCurve('ThreePoint', 13030, 3030, 0.0, 83.63622562, 0.03097099, 83.63622562, 0.09291296, 58.54535793, -3862.21994603, 0.05, 2, 0, 73030, 24030, 1, 3)
    ops.uniaxialMaterial('LimitState', 33030, 20.90905641, 9.389e-05, 62.72716922, 0.00028166, 209.09056405, 0.00093885, -20.90905641, -9.389e-05, -62.72716922, -0.00028166, -209.09056405, -0.00093885, 0.4, 0.3, 0.003, 0.0, 0.0, 13030, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3030, 99999, 'P', 43030, 'Vy', 33030, 'Vz', 23030, 'My', 13030, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173030, 73030, 173030, 3030, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124030, 124030, 24030, 3030, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173031, 23.9, 15.3, 8.975)
    ops.node(124031, 23.9, 15.3, 11.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3031, 173031, 124031, 0.0625, 29304337.85267856, 12210140.7719494, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23031, 28.61393978, 0.00150497, 34.82251579, 0.02028588, 3.48225158, 0.08288873, -28.61393978, -0.00150497, -34.82251579, -0.02028588, -3.48225158, -0.08288873, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13031, 28.61393978, 0.00150497, 34.82251579, 0.02028588, 3.48225158, 0.08288873, -28.61393978, -0.00150497, -34.82251579, -0.02028588, -3.48225158, -0.08288873, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23031, 3031, 0.0, 83.07621479, 0.0300995, 83.07621479, 0.09029849, 58.15335035, -3901.69320346, 0.05, 2, 0, 73031, 24031, 2, 3)
    ops.uniaxialMaterial('LimitState', 43031, 20.7690537, 9.471e-05, 62.30716109, 0.00028413, 207.69053697, 0.0009471, -20.7690537, -9.471e-05, -62.30716109, -0.00028413, -207.69053697, -0.0009471, 0.4, 0.3, 0.003, 0.0, 0.0, 23031, 2)
    ops.limitCurve('ThreePoint', 13031, 3031, 0.0, 83.07621479, 0.0300995, 83.07621479, 0.09029849, 58.15335035, -3901.69320346, 0.05, 2, 0, 73031, 24031, 1, 3)
    ops.uniaxialMaterial('LimitState', 33031, 20.7690537, 9.471e-05, 62.30716109, 0.00028413, 207.69053697, 0.0009471, -20.7690537, -9.471e-05, -62.30716109, -0.00028413, -207.69053697, -0.0009471, 0.4, 0.3, 0.003, 0.0, 0.0, 13031, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3031, 99999, 'P', 43031, 'Vy', 33031, 'Vz', 23031, 'My', 13031, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173031, 73031, 173031, 3031, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124031, 124031, 24031, 3031, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173032, 28.1, 15.3, 8.95)
    ops.node(124032, 28.1, 15.3, 11.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3032, 173032, 124032, 0.0625, 29564452.73588933, 12318521.97328722, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23032, 27.95489756, 0.0014001, 34.03091672, 0.01887377, 3.40309167, 0.08344779, -27.95489756, -0.0014001, -34.03091672, -0.01887377, -3.40309167, -0.08344779, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13032, 27.95489756, 0.0014001, 34.03091672, 0.01887377, 3.40309167, 0.08344779, -27.95489756, -0.0014001, -34.03091672, -0.01887377, -3.40309167, -0.08344779, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23032, 3032, 0.0, 79.38267052, 0.02800198, 79.38267052, 0.08400595, 55.56786936, -5674.56491515, 0.05, 2, 0, 73032, 24032, 2, 3)
    ops.uniaxialMaterial('LimitState', 43032, 19.84566763, 8.97e-05, 59.53700289, 0.00026911, 198.45667629, 0.00089703, -19.84566763, -8.97e-05, -59.53700289, -0.00026911, -198.45667629, -0.00089703, 0.4, 0.3, 0.003, 0.0, 0.0, 23032, 2)
    ops.limitCurve('ThreePoint', 13032, 3032, 0.0, 79.38267052, 0.02800198, 79.38267052, 0.08400595, 55.56786936, -5674.56491515, 0.05, 2, 0, 73032, 24032, 1, 3)
    ops.uniaxialMaterial('LimitState', 33032, 19.84566763, 8.97e-05, 59.53700289, 0.00026911, 198.45667629, 0.00089703, -19.84566763, -8.97e-05, -59.53700289, -0.00026911, -198.45667629, -0.00089703, 0.4, 0.3, 0.003, 0.0, 0.0, 13032, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3032, 99999, 'P', 43032, 'Vy', 33032, 'Vz', 23032, 'My', 13032, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173032, 73032, 173032, 3032, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124032, 124032, 24032, 3032, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170004, 12.6, 0.0, 0.0)
    ops.node(124033, 12.6, 0.0, 1.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4085, 170004, 124033, 0.1225, 30287389.23523812, 12619745.51468255, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24085, 156.16769495, 0.00096266, 188.25700449, 0.02707559, 18.82570045, 0.08626385, -156.16769495, -0.00096266, -188.25700449, -0.02707559, -18.82570045, -0.08626385, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14085, 136.39636174, 0.00096266, 164.42306133, 0.02707559, 16.44230613, 0.08626385, -136.39636174, -0.00096266, -164.42306133, -0.02707559, -16.44230613, -0.08626385, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24085, 4085, 0.0, 243.653519, 0.0192531, 243.653519, 0.05775931, 170.5574633, -7691.87472112, 0.05, 2, 0, 70004, 24033, 2, 3)
    ops.uniaxialMaterial('LimitState', 44085, 60.91337975, 6.856e-05, 182.74013925, 0.00020568, 609.1337975, 0.00068561, -60.91337975, -6.856e-05, -182.74013925, -0.00020568, -609.1337975, -0.00068561, 0.4, 0.3, 0.003, 0.0, 0.0, 24085, 2)
    ops.limitCurve('ThreePoint', 14085, 4085, 0.0, 243.653519, 0.0192531, 243.653519, 0.05775931, 170.5574633, -7691.87472112, 0.05, 2, 0, 70004, 24033, 1, 3)
    ops.uniaxialMaterial('LimitState', 34085, 60.91337975, 6.856e-05, 182.74013925, 0.00020568, 609.1337975, 0.00068561, -60.91337975, -6.856e-05, -182.74013925, -0.00020568, -609.1337975, -0.00068561, 0.4, 0.3, 0.003, 0.0, 0.0, 14085, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4085, 99999, 'P', 44085, 'Vy', 34085, 'Vz', 24085, 'My', 14085, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170004, 70004, 170004, 4085, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124033, 124033, 24033, 4085, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174033, 12.6, 0.0, 1.675)
    ops.node(121004, 12.6, 0.0, 2.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4086, 174033, 121004, 0.1225, 28165173.87929891, 11735489.11637455, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24086, 111.73590745, 0.00094737, 135.31512253, 0.02632196, 13.53151225, 0.08326574, -111.73590745, -0.00094737, -135.31512253, -0.02632196, -13.53151225, -0.08326574, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14086, 97.3057298, 0.00094737, 117.83979788, 0.02632196, 11.78397979, 0.08326574, -97.3057298, -0.00094737, -117.83979788, -0.02632196, -11.78397979, -0.08326574, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24086, 4086, 0.0, 228.15715895, 0.01894747, 228.15715895, 0.05684241, 159.71001127, -7969.35694541, 0.05, 2, 0, 74033, 21004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44086, 57.03928974, 6.904e-05, 171.11786921, 0.00020711, 570.39289738, 0.00069038, -57.03928974, -6.904e-05, -171.11786921, -0.00020711, -570.39289738, -0.00069038, 0.4, 0.3, 0.003, 0.0, 0.0, 24086, 2)
    ops.limitCurve('ThreePoint', 14086, 4086, 0.0, 228.15715895, 0.01894747, 228.15715895, 0.05684241, 159.71001127, -7969.35694541, 0.05, 2, 0, 74033, 21004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34086, 57.03928974, 6.904e-05, 171.11786921, 0.00020711, 570.39289738, 0.00069038, -57.03928974, -6.904e-05, -171.11786921, -0.00020711, -570.39289738, -0.00069038, 0.4, 0.3, 0.003, 0.0, 0.0, 14086, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4086, 99999, 'P', 44086, 'Vy', 34086, 'Vz', 24086, 'My', 14086, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174033, 74033, 174033, 4086, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121004, 121004, 21004, 4086, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170005, 15.5, 0.0, 0.0)
    ops.node(124034, 15.5, 0.0, 1.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4087, 170005, 124034, 0.1225, 27824764.82519826, 11593652.01049927, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24087, 160.60110125, 0.00099501, 194.34556258, 0.03009095, 19.43455626, 0.08437034, -160.60110125, -0.00099501, -194.34556258, -0.03009095, -19.43455626, -0.08437034, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14087, 138.41135799, 0.00099501, 167.49345445, 0.03009095, 16.74934544, 0.08437034, -138.41135799, -0.00099501, -167.49345445, -0.03009095, -16.74934544, -0.08437034, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24087, 4087, 0.0, 241.95397585, 0.01990013, 241.95397585, 0.05970039, 169.36778309, -8944.57393734, 0.05, 2, 0, 70005, 24034, 2, 3)
    ops.uniaxialMaterial('LimitState', 44087, 60.48849396, 7.411e-05, 181.46548189, 0.00022232, 604.88493962, 0.00074108, -60.48849396, -7.411e-05, -181.46548189, -0.00022232, -604.88493962, -0.00074108, 0.4, 0.3, 0.003, 0.0, 0.0, 24087, 2)
    ops.limitCurve('ThreePoint', 14087, 4087, 0.0, 241.95397585, 0.01990013, 241.95397585, 0.05970039, 169.36778309, -8944.57393734, 0.05, 2, 0, 70005, 24034, 1, 3)
    ops.uniaxialMaterial('LimitState', 34087, 60.48849396, 7.411e-05, 181.46548189, 0.00022232, 604.88493962, 0.00074108, -60.48849396, -7.411e-05, -181.46548189, -0.00022232, -604.88493962, -0.00074108, 0.4, 0.3, 0.003, 0.0, 0.0, 14087, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4087, 99999, 'P', 44087, 'Vy', 34087, 'Vz', 24087, 'My', 14087, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170005, 70005, 170005, 4087, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124034, 124034, 24034, 4087, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174034, 15.5, 0.0, 1.675)
    ops.node(121005, 15.5, 0.0, 2.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4088, 174034, 121005, 0.1225, 27274279.87850375, 11364283.2827099, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24088, 112.06983613, 0.00094376, 135.85952721, 0.02929896, 13.58595272, 0.0843203, -112.06983613, -0.00094376, -135.85952721, -0.02929896, -13.58595272, -0.0843203, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14088, 97.0483413, 0.00094376, 117.64933562, 0.02929896, 11.76493356, 0.0843203, -97.0483413, -0.00094376, -117.64933562, -0.02929896, -11.76493356, -0.0843203, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24088, 4088, 0.0, 233.78709445, 0.01887519, 233.78709445, 0.05662558, 163.65096612, -9108.74532915, 0.05, 2, 0, 74034, 21005, 2, 3)
    ops.uniaxialMaterial('LimitState', 44088, 58.44677361, 7.305e-05, 175.34032084, 0.00021916, 584.46773613, 0.00073052, -58.44677361, -7.305e-05, -175.34032084, -0.00021916, -584.46773613, -0.00073052, 0.4, 0.3, 0.003, 0.0, 0.0, 24088, 2)
    ops.limitCurve('ThreePoint', 14088, 4088, 0.0, 233.78709445, 0.01887519, 233.78709445, 0.05662558, 163.65096612, -9108.74532915, 0.05, 2, 0, 74034, 21005, 1, 3)
    ops.uniaxialMaterial('LimitState', 34088, 58.44677361, 7.305e-05, 175.34032084, 0.00021916, 584.46773613, 0.00073052, -58.44677361, -7.305e-05, -175.34032084, -0.00021916, -584.46773613, -0.00073052, 0.4, 0.3, 0.003, 0.0, 0.0, 14088, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4088, 99999, 'P', 44088, 'Vy', 34088, 'Vz', 24088, 'My', 14088, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174034, 74034, 174034, 4088, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121005, 121005, 21005, 4088, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171004, 12.6, 0.0, 3.15)
    ops.node(124035, 12.6, 0.0, 4.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4090, 171004, 124035, 0.1225, 28312833.43157547, 11797013.92982311, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24090, 106.93374881, 0.00097242, 129.70826226, 0.02794398, 12.97082623, 0.08836418, -106.93374881, -0.00097242, -129.70826226, -0.02794398, -12.97082623, -0.08836418, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14090, 92.91227433, 0.00097242, 112.70052514, 0.02794398, 11.27005251, 0.08836418, -92.91227433, -0.00097242, -112.70052514, -0.02794398, -11.27005251, -0.08836418, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24090, 4090, 0.0, 226.13920159, 0.0194484, 226.13920159, 0.05834519, 158.29744111, -8954.65704278, 0.05, 2, 0, 71004, 24035, 2, 3)
    ops.uniaxialMaterial('LimitState', 44090, 56.5348004, 6.807e-05, 169.60440119, 0.00020421, 565.34800397, 0.0006807, -56.5348004, -6.807e-05, -169.60440119, -0.00020421, -565.34800397, -0.0006807, 0.4, 0.3, 0.003, 0.0, 0.0, 24090, 2)
    ops.limitCurve('ThreePoint', 14090, 4090, 0.0, 226.13920159, 0.0194484, 226.13920159, 0.05834519, 158.29744111, -8954.65704278, 0.05, 2, 0, 71004, 24035, 1, 3)
    ops.uniaxialMaterial('LimitState', 34090, 56.5348004, 6.807e-05, 169.60440119, 0.00020421, 565.34800397, 0.0006807, -56.5348004, -6.807e-05, -169.60440119, -0.00020421, -565.34800397, -0.0006807, 0.4, 0.3, 0.003, 0.0, 0.0, 14090, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4090, 99999, 'P', 44090, 'Vy', 34090, 'Vz', 24090, 'My', 14090, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171004, 71004, 171004, 4090, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124035, 124035, 24035, 4090, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174035, 12.6, 0.0, 4.6)
    ops.node(122004, 12.6, 0.0, 5.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4091, 174035, 122004, 0.1225, 25542048.86927399, 10642520.3621975, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24091, 104.32968543, 0.00095662, 127.1308704, 0.02963419, 12.71308704, 0.08694778, -104.32968543, -0.00095662, -127.1308704, -0.02963419, -12.71308704, -0.08694778, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14091, 88.59341984, 0.00095662, 107.9554542, 0.02963419, 10.79554542, 0.08694778, -88.59341984, -0.00095662, -107.9554542, -0.02963419, -10.79554542, -0.08694778, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24091, 4091, 0.0, 213.52819614, 0.01913234, 213.52819614, 0.05739702, 149.4697373, -10411.05519393, 0.05, 2, 0, 74035, 22004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44091, 53.38204904, 7.125e-05, 160.14614711, 0.00021374, 533.82049035, 0.00071247, -53.38204904, -7.125e-05, -160.14614711, -0.00021374, -533.82049035, -0.00071247, 0.4, 0.3, 0.003, 0.0, 0.0, 24091, 2)
    ops.limitCurve('ThreePoint', 14091, 4091, 0.0, 213.52819614, 0.01913234, 213.52819614, 0.05739702, 149.4697373, -10411.05519393, 0.05, 2, 0, 74035, 22004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34091, 53.38204904, 7.125e-05, 160.14614711, 0.00021374, 533.82049035, 0.00071247, -53.38204904, -7.125e-05, -160.14614711, -0.00021374, -533.82049035, -0.00071247, 0.4, 0.3, 0.003, 0.0, 0.0, 14091, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4091, 99999, 'P', 44091, 'Vy', 34091, 'Vz', 24091, 'My', 14091, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174035, 74035, 174035, 4091, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122004, 122004, 22004, 4091, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171005, 15.5, 0.0, 3.15)
    ops.node(124036, 15.5, 0.0, 4.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4092, 171005, 124036, 0.1225, 29938928.05613865, 12474553.35672444, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24092, 110.76886528, 0.00091699, 133.94684102, 0.03044845, 13.3946841, 0.09342978, -110.76886528, -0.00091699, -133.94684102, -0.03044845, -13.3946841, -0.09342978, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14092, 95.11125809, 0.00091699, 115.01293738, 0.03044845, 11.50129374, 0.09342978, -95.11125809, -0.00091699, -115.01293738, -0.03044845, -11.50129374, -0.09342978, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24092, 4092, 0.0, 245.82039259, 0.01833976, 245.82039259, 0.05501927, 172.07427481, -10284.05793094, 0.05, 2, 0, 71005, 24036, 2, 3)
    ops.uniaxialMaterial('LimitState', 44092, 61.45509815, 6.998e-05, 184.36529444, 0.00020993, 614.55098148, 0.00069976, -61.45509815, -6.998e-05, -184.36529444, -0.00020993, -614.55098148, -0.00069976, 0.4, 0.3, 0.003, 0.0, 0.0, 24092, 2)
    ops.limitCurve('ThreePoint', 14092, 4092, 0.0, 245.82039259, 0.01833976, 245.82039259, 0.05501927, 172.07427481, -10284.05793094, 0.05, 2, 0, 71005, 24036, 1, 3)
    ops.uniaxialMaterial('LimitState', 34092, 61.45509815, 6.998e-05, 184.36529444, 0.00020993, 614.55098148, 0.00069976, -61.45509815, -6.998e-05, -184.36529444, -0.00020993, -614.55098148, -0.00069976, 0.4, 0.3, 0.003, 0.0, 0.0, 14092, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4092, 99999, 'P', 44092, 'Vy', 34092, 'Vz', 24092, 'My', 14092, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171005, 71005, 171005, 4092, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124036, 124036, 24036, 4092, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174036, 15.5, 0.0, 4.6)
    ops.node(122005, 15.5, 0.0, 5.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4093, 174036, 122005, 0.1225, 28418771.36843697, 11841154.73684874, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24093, 99.22658857, 0.00095537, 120.47282921, 0.03048676, 12.04728292, 0.09313318, -99.22658857, -0.00095537, -120.47282921, -0.03048676, -12.04728292, -0.09313318, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14093, 86.63300529, 0.00095537, 105.18272774, 0.03048676, 10.51827277, 0.09313318, -86.63300529, -0.00095537, -105.18272774, -0.03048676, -10.51827277, -0.09313318, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24093, 4093, 0.0, 235.45267049, 0.01910737, 235.45267049, 0.0573221, 164.81686934, -11356.95697261, 0.05, 2, 0, 74036, 22005, 2, 3)
    ops.uniaxialMaterial('LimitState', 44093, 58.86316762, 7.061e-05, 176.58950287, 0.00021183, 588.63167622, 0.00070609, -58.86316762, -7.061e-05, -176.58950287, -0.00021183, -588.63167622, -0.00070609, 0.4, 0.3, 0.003, 0.0, 0.0, 24093, 2)
    ops.limitCurve('ThreePoint', 14093, 4093, 0.0, 235.45267049, 0.01910737, 235.45267049, 0.0573221, 164.81686934, -11356.95697261, 0.05, 2, 0, 74036, 22005, 1, 3)
    ops.uniaxialMaterial('LimitState', 34093, 58.86316762, 7.061e-05, 176.58950287, 0.00021183, 588.63167622, 0.00070609, -58.86316762, -7.061e-05, -176.58950287, -0.00021183, -588.63167622, -0.00070609, 0.4, 0.3, 0.003, 0.0, 0.0, 14093, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4093, 99999, 'P', 44093, 'Vy', 34093, 'Vz', 24093, 'My', 14093, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174036, 74036, 174036, 4093, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122005, 122005, 22005, 4093, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172004, 12.6, 0.0, 6.05)
    ops.node(124037, 12.6, 0.0, 7.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4095, 172004, 124037, 0.0625, 27828862.46290033, 11595359.3595418, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24095, 50.64648278, 0.00120103, 61.34089154, 0.01510495, 6.13408915, 0.06344602, -50.64648278, -0.00120103, -61.34089154, -0.01510495, -6.13408915, -0.06344602, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14095, 46.06848862, 0.00120103, 55.7962174, 0.01510495, 5.57962174, 0.06344602, -46.06848862, -0.00120103, -55.7962174, -0.01510495, -5.57962174, -0.06344602, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24095, 4095, 0.0, 77.23895333, 0.02402056, 77.23895333, 0.07206168, 54.06726733, -2936.6980483, 0.05, 2, 0, 72004, 24037, 2, 3)
    ops.uniaxialMaterial('LimitState', 44095, 19.30973833, 4.636e-05, 57.929215, 0.00013909, 193.09738333, 0.00046362, -19.30973833, -4.636e-05, -57.929215, -0.00013909, -193.09738333, -0.00046362, 0.4, 0.3, 0.003, 0.0, 0.0, 24095, 2)
    ops.limitCurve('ThreePoint', 14095, 4095, 0.0, 77.23895333, 0.02402056, 77.23895333, 0.07206168, 54.06726733, -2936.6980483, 0.05, 2, 0, 72004, 24037, 1, 3)
    ops.uniaxialMaterial('LimitState', 34095, 19.30973833, 4.636e-05, 57.929215, 0.00013909, 193.09738333, 0.00046362, -19.30973833, -4.636e-05, -57.929215, -0.00013909, -193.09738333, -0.00046362, 0.4, 0.3, 0.003, 0.0, 0.0, 14095, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4095, 99999, 'P', 44095, 'Vy', 34095, 'Vz', 24095, 'My', 14095, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172004, 72004, 172004, 4095, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124037, 124037, 24037, 4095, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174037, 12.6, 0.0, 7.45)
    ops.node(123004, 12.6, 0.0, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4096, 174037, 123004, 0.0625, 27134812.25109316, 11306171.77128882, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24096, 37.15716319, 0.00129887, 45.16101806, 0.01461337, 4.51610181, 0.06567074, -37.15716319, -0.00129887, -45.16101806, -0.01461337, -4.51610181, -0.06567074, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14096, 37.15716319, 0.00129887, 45.16101806, 0.01461337, 4.51610181, 0.06567074, -37.15716319, -0.00129887, -45.16101806, -0.01461337, -4.51610181, -0.06567074, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24096, 4096, 0.0, 72.99140292, 0.0259774, 72.99140292, 0.07793219, 51.09398205, -3177.22463162, 0.05, 2, 0, 74037, 23004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44096, 18.24785073, 4.493e-05, 54.74355219, 0.0001348, 182.47850731, 0.00044933, -18.24785073, -4.493e-05, -54.74355219, -0.0001348, -182.47850731, -0.00044933, 0.4, 0.3, 0.003, 0.0, 0.0, 24096, 2)
    ops.limitCurve('ThreePoint', 14096, 4096, 0.0, 72.99140292, 0.0259774, 72.99140292, 0.07793219, 51.09398205, -3177.22463162, 0.05, 2, 0, 74037, 23004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34096, 18.24785073, 4.493e-05, 54.74355219, 0.0001348, 182.47850731, 0.00044933, -18.24785073, -4.493e-05, -54.74355219, -0.0001348, -182.47850731, -0.00044933, 0.4, 0.3, 0.003, 0.0, 0.0, 14096, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4096, 99999, 'P', 44096, 'Vy', 34096, 'Vz', 24096, 'My', 14096, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174037, 74037, 174037, 4096, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123004, 123004, 23004, 4096, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172005, 15.5, 0.0, 6.05)
    ops.node(124038, 15.5, 0.0, 7.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4097, 172005, 124038, 0.0625, 28361905.44655066, 11817460.60272944, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24097, 53.57258261, 0.00135245, 64.8408554, 0.01727276, 6.48408554, 0.06658808, -53.57258261, -0.00135245, -64.8408554, -0.01727276, -6.48408554, -0.06658808, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14097, 48.96636387, 0.00135245, 59.26578044, 0.01727276, 5.92657804, 0.06658808, -48.96636387, -0.00135245, -59.26578044, -0.01727276, -5.92657804, -0.06658808, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24097, 4097, 0.0, 95.4060416, 0.02704908, 95.4060416, 0.08114724, 66.78422912, -3635.2720831, 0.05, 2, 0, 72005, 24038, 2, 3)
    ops.uniaxialMaterial('LimitState', 44097, 23.8515104, 5.619e-05, 71.5545312, 0.00016857, 238.515104, 0.0005619, -23.8515104, -5.619e-05, -71.5545312, -0.00016857, -238.515104, -0.0005619, 0.4, 0.3, 0.003, 0.0, 0.0, 24097, 2)
    ops.limitCurve('ThreePoint', 14097, 4097, 0.0, 95.4060416, 0.02704908, 95.4060416, 0.08114724, 66.78422912, -3635.2720831, 0.05, 2, 0, 72005, 24038, 1, 3)
    ops.uniaxialMaterial('LimitState', 34097, 23.8515104, 5.619e-05, 71.5545312, 0.00016857, 238.515104, 0.0005619, -23.8515104, -5.619e-05, -71.5545312, -0.00016857, -238.515104, -0.0005619, 0.4, 0.3, 0.003, 0.0, 0.0, 14097, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4097, 99999, 'P', 44097, 'Vy', 34097, 'Vz', 24097, 'My', 14097, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172005, 72005, 172005, 4097, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124038, 124038, 24038, 4097, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174038, 15.5, 0.0, 7.45)
    ops.node(123005, 15.5, 0.0, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4098, 174038, 123005, 0.0625, 27993800.22407941, 11664083.42669975, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24098, 36.33116404, 0.00116813, 44.10498474, 0.01976193, 4.41049847, 0.07220253, -36.33116404, -0.00116813, -44.10498474, -0.01976193, -4.41049847, -0.07220253, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14098, 36.33116404, 0.00116813, 44.10498474, 0.01976193, 4.41049847, 0.07220253, -36.33116404, -0.00116813, -44.10498474, -0.01976193, -4.41049847, -0.07220253, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24098, 4098, 0.0, 96.89815452, 0.02336251, 96.89815452, 0.07008753, 67.82870816, -4616.84328972, 0.05, 2, 0, 74038, 23005, 2, 3)
    ops.uniaxialMaterial('LimitState', 44098, 24.22453863, 5.782e-05, 72.67361589, 0.00017346, 242.24538629, 0.00057819, -24.22453863, -5.782e-05, -72.67361589, -0.00017346, -242.24538629, -0.00057819, 0.4, 0.3, 0.003, 0.0, 0.0, 24098, 2)
    ops.limitCurve('ThreePoint', 14098, 4098, 0.0, 96.89815452, 0.02336251, 96.89815452, 0.07008753, 67.82870816, -4616.84328972, 0.05, 2, 0, 74038, 23005, 1, 3)
    ops.uniaxialMaterial('LimitState', 34098, 24.22453863, 5.782e-05, 72.67361589, 0.00017346, 242.24538629, 0.00057819, -24.22453863, -5.782e-05, -72.67361589, -0.00017346, -242.24538629, -0.00057819, 0.4, 0.3, 0.003, 0.0, 0.0, 14098, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4098, 99999, 'P', 44098, 'Vy', 34098, 'Vz', 24098, 'My', 14098, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174038, 74038, 174038, 4098, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123005, 123005, 23005, 4098, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173004, 12.6, 0.0, 8.95)
    ops.node(124039, 12.6, 0.0, 9.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4100, 173004, 124039, 0.0625, 28371174.50627796, 11821322.71094915, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24100, 31.25076658, 0.00119047, 38.0655879, 0.01652243, 3.80655879, 0.07618962, -31.25076658, -0.00119047, -38.0655879, -0.01652243, -3.80655879, -0.07618962, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14100, 31.25076658, 0.00119047, 38.0655879, 0.01652243, 3.80655879, 0.07618962, -31.25076658, -0.00119047, -38.0655879, -0.01652243, -3.80655879, -0.07618962, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24100, 4100, 0.0, 76.9194405, 0.02380935, 76.9194405, 0.07142804, 53.84360835, -4696.62865198, 0.05, 2, 0, 73004, 24039, 2, 3)
    ops.uniaxialMaterial('LimitState', 44100, 19.22986013, 4.529e-05, 57.68958038, 0.00013586, 192.29860126, 0.00045288, -19.22986013, -4.529e-05, -57.68958038, -0.00013586, -192.29860126, -0.00045288, 0.4, 0.3, 0.003, 0.0, 0.0, 24100, 2)
    ops.limitCurve('ThreePoint', 14100, 4100, 0.0, 76.9194405, 0.02380935, 76.9194405, 0.07142804, 53.84360835, -4696.62865198, 0.05, 2, 0, 73004, 24039, 1, 3)
    ops.uniaxialMaterial('LimitState', 34100, 19.22986013, 4.529e-05, 57.68958038, 0.00013586, 192.29860126, 0.00045288, -19.22986013, -4.529e-05, -57.68958038, -0.00013586, -192.29860126, -0.00045288, 0.4, 0.3, 0.003, 0.0, 0.0, 14100, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4100, 99999, 'P', 44100, 'Vy', 34100, 'Vz', 24100, 'My', 14100, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173004, 73004, 173004, 4100, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124039, 124039, 24039, 4100, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174039, 12.6, 0.0, 10.325)
    ops.node(124004, 12.6, 0.0, 11.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4101, 174039, 124004, 0.0625, 29225643.16337052, 12177351.31807105, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24101, 28.67036373, 0.00110947, 34.93101175, 0.01977582, 3.49310117, 0.08412319, -28.67036373, -0.00110947, -34.93101175, -0.01977582, -3.49310117, -0.08412319, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14101, 28.67036373, 0.00110947, 34.93101175, 0.01977582, 3.49310117, 0.08412319, -28.67036373, -0.00110947, -34.93101175, -0.01977582, -3.49310117, -0.08412319, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24101, 4101, 0.0, 85.23920777, 0.02218932, 85.23920777, 0.06656796, 59.66744544, -12158.00091246, 0.05, 2, 0, 74039, 24004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44101, 21.30980194, 4.872e-05, 63.92940583, 0.00014616, 213.09801942, 0.00048719, -21.30980194, -4.872e-05, -63.92940583, -0.00014616, -213.09801942, -0.00048719, 0.4, 0.3, 0.003, 0.0, 0.0, 24101, 2)
    ops.limitCurve('ThreePoint', 14101, 4101, 0.0, 85.23920777, 0.02218932, 85.23920777, 0.06656796, 59.66744544, -12158.00091246, 0.05, 2, 0, 74039, 24004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34101, 21.30980194, 4.872e-05, 63.92940583, 0.00014616, 213.09801942, 0.00048719, -21.30980194, -4.872e-05, -63.92940583, -0.00014616, -213.09801942, -0.00048719, 0.4, 0.3, 0.003, 0.0, 0.0, 14101, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4101, 99999, 'P', 44101, 'Vy', 34101, 'Vz', 24101, 'My', 14101, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174039, 74039, 174039, 4101, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124004, 124004, 24004, 4101, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173005, 15.5, 0.0, 8.95)
    ops.node(124040, 15.5, 0.0, 9.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4102, 173005, 124040, 0.0625, 29571572.26192649, 12321488.44246937, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24102, 30.14698333, 0.0011177, 36.61977816, 0.02076943, 3.66197782, 0.08132913, -30.14698333, -0.0011177, -36.61977816, -0.02076943, -3.66197782, -0.08132913, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14102, 30.14698333, 0.0011177, 36.61977816, 0.02076943, 3.66197782, 0.08132913, -30.14698333, -0.0011177, -36.61977816, -0.02076943, -3.66197782, -0.08132913, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24102, 4102, 0.0, 93.69924231, 0.02235393, 93.69924231, 0.0670618, 65.58946962, -6684.58834368, 0.05, 2, 0, 73005, 24040, 2, 3)
    ops.uniaxialMaterial('LimitState', 44102, 23.42481058, 5.293e-05, 70.27443173, 0.00015878, 234.24810578, 0.00052928, -23.42481058, -5.293e-05, -70.27443173, -0.00015878, -234.24810578, -0.00052928, 0.4, 0.3, 0.003, 0.0, 0.0, 24102, 2)
    ops.limitCurve('ThreePoint', 14102, 4102, 0.0, 93.69924231, 0.02235393, 93.69924231, 0.0670618, 65.58946962, -6684.58834368, 0.05, 2, 0, 73005, 24040, 1, 3)
    ops.uniaxialMaterial('LimitState', 34102, 23.42481058, 5.293e-05, 70.27443173, 0.00015878, 234.24810578, 0.00052928, -23.42481058, -5.293e-05, -70.27443173, -0.00015878, -234.24810578, -0.00052928, 0.4, 0.3, 0.003, 0.0, 0.0, 14102, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4102, 99999, 'P', 44102, 'Vy', 34102, 'Vz', 24102, 'My', 14102, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173005, 73005, 173005, 4102, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124040, 124040, 24040, 4102, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174040, 15.5, 0.0, 10.325)
    ops.node(124005, 15.5, 0.0, 11.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4103, 174040, 124005, 0.0625, 31196063.10076448, 12998359.62531853, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24103, 28.66057926, 0.00106485, 34.72251323, 0.01934652, 3.47225132, 0.08419345, -28.66057926, -0.00106485, -34.72251323, -0.01934652, -3.47225132, -0.08419345, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14103, 28.66057926, 0.00106485, 34.72251323, 0.01934652, 3.47225132, 0.08419345, -28.66057926, -0.00106485, -34.72251323, -0.01934652, -3.47225132, -0.08419345, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24103, 4103, 0.0, 93.0997251, 0.02129692, 93.0997251, 0.06389076, 65.16980757, -14023.8060005, 0.05, 2, 0, 74040, 24005, 2, 3)
    ops.uniaxialMaterial('LimitState', 44103, 23.27493127, 4.985e-05, 69.82479382, 0.00014955, 232.74931275, 0.0004985, -23.27493127, -4.985e-05, -69.82479382, -0.00014955, -232.74931275, -0.0004985, 0.4, 0.3, 0.003, 0.0, 0.0, 24103, 2)
    ops.limitCurve('ThreePoint', 14103, 4103, 0.0, 93.0997251, 0.02129692, 93.0997251, 0.06389076, 65.16980757, -14023.8060005, 0.05, 2, 0, 74040, 24005, 1, 3)
    ops.uniaxialMaterial('LimitState', 34103, 23.27493127, 4.985e-05, 69.82479382, 0.00014955, 232.74931275, 0.0004985, -23.27493127, -4.985e-05, -69.82479382, -0.00014955, -232.74931275, -0.0004985, 0.4, 0.3, 0.003, 0.0, 0.0, 14103, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4103, 99999, 'P', 44103, 'Vy', 34103, 'Vz', 24103, 'My', 14103, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174040, 74040, 174040, 4103, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124005, 124005, 24005, 4103, '-orient', 0, 0, 1, 0, 1, 0)
