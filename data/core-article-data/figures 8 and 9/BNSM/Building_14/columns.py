import openseespy.opensees as ops


def add_columns() -> None:
    """Add components of all columns to ops domain (plastic hinges, column elements and nodes)
    """
    # Create elastic column element nodes
    ops.node(170003, 7.65, 0.0, 0.0)
    ops.node(121003, 7.65, 0.0, 2.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3, 170003, 121003, 0.16, 27740401.98307873, 11558500.8262828, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20003, 149.54104852, 0.00090761, 180.5859427, 0.02743505, 18.05859427, 0.07289731, -149.54104852, -0.00090761, -180.5859427, -0.02743505, -18.05859427, -0.07289731, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10003, 164.57173449, 0.00090761, 198.73701641, 0.02743505, 19.87370164, 0.07289731, -164.57173449, -0.00090761, -198.73701641, -0.02743505, -19.87370164, -0.07289731, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20003, 3, 0.0, 209.32982541, 0.01815215, 209.32982541, 0.05445646, 146.53087779, -3115.53816212, 0.05, 2, 0, 70003, 21003, 2, 3)
    ops.uniaxialMaterial('LimitState', 40003, 52.33245635, 0.00010357, 156.99736906, 0.00031071, 523.32456353, 0.00103569, -52.33245635, -0.00010357, -156.99736906, -0.00031071, -523.32456353, -0.00103569, 0.4, 0.3, 0.003, 0.0, 0.0, 20003, 2)
    ops.limitCurve('ThreePoint', 10003, 3, 0.0, 209.32982541, 0.01815215, 209.32982541, 0.05445646, 146.53087779, -3115.53816212, 0.05, 2, 0, 70003, 21003, 1, 3)
    ops.uniaxialMaterial('LimitState', 30003, 52.33245635, 0.00010357, 156.99736906, 0.00031071, 523.32456353, 0.00103569, -52.33245635, -0.00010357, -156.99736906, -0.00031071, -523.32456353, -0.00103569, 0.4, 0.3, 0.003, 0.0, 0.0, 10003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3, 99999, 'P', 40003, 'Vy', 30003, 'Vz', 20003, 'My', 10003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170003, 70003, 170003, 3, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121003, 121003, 21003, 3, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170004, 12.3, 0.0, 0.0)
    ops.node(121004, 12.3, 0.0, 2.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4, 170004, 121004, 0.09, 31407283.37034314, 13086368.07097631, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20004, 67.02013246, 0.00111163, 80.47351334, 0.01564241, 8.04735133, 0.0596151, -67.02013246, -0.00111163, -80.47351334, -0.01564241, -8.04735133, -0.0596151, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10004, 62.19248676, 0.00111163, 74.67678337, 0.01564241, 7.46767834, 0.0596151, -62.19248676, -0.00111163, -74.67678337, -0.01564241, -7.46767834, -0.0596151, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20004, 4, 0.0, 112.63311809, 0.02223259, 112.63311809, 0.06669776, 78.84318266, -1265.87599031, 0.05, 2, 0, 70004, 21004, 2, 3)
    ops.uniaxialMaterial('LimitState', 40004, 28.15827952, 8.75e-05, 84.47483856, 0.00026251, 281.58279521, 0.00087504, -28.15827952, -8.75e-05, -84.47483856, -0.00026251, -281.58279521, -0.00087504, 0.4, 0.3, 0.003, 0.0, 0.0, 20004, 2)
    ops.limitCurve('ThreePoint', 10004, 4, 0.0, 112.63311809, 0.02223259, 112.63311809, 0.06669776, 78.84318266, -1265.87599031, 0.05, 2, 0, 70004, 21004, 1, 3)
    ops.uniaxialMaterial('LimitState', 30004, 28.15827952, 8.75e-05, 84.47483856, 0.00026251, 281.58279521, 0.00087504, -28.15827952, -8.75e-05, -84.47483856, -0.00026251, -281.58279521, -0.00087504, 0.4, 0.3, 0.003, 0.0, 0.0, 10004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4, 99999, 'P', 40004, 'Vy', 30004, 'Vz', 20004, 'My', 10004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170004, 70004, 170004, 4, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121004, 121004, 21004, 4, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170005, 0.0, 5.2, 0.0)
    ops.node(121005, 0.0, 5.2, 2.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 5, 170005, 121005, 0.09, 30869879.35122587, 12862449.72967745, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20005, 71.87998657, 0.00118696, 86.2391129, 0.01510602, 8.62391129, 0.05587656, -71.87998657, -0.00118696, -86.2391129, -0.01510602, -8.62391129, -0.05587656, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10005, 67.28346295, 0.00118696, 80.7243634, 0.01510602, 8.07243634, 0.05587656, -67.28346295, -0.00118696, -80.7243634, -0.01510602, -8.07243634, -0.05587656, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20005, 5, 0.0, 116.01681552, 0.02373919, 116.01681552, 0.07121758, 81.21177087, -1331.04213664, 0.05, 2, 0, 70005, 21005, 2, 3)
    ops.uniaxialMaterial('LimitState', 40005, 29.00420388, 9.17e-05, 87.01261164, 0.0002751, 290.0420388, 0.00091701, -29.00420388, -9.17e-05, -87.01261164, -0.0002751, -290.0420388, -0.00091701, 0.4, 0.3, 0.003, 0.0, 0.0, 20005, 2)
    ops.limitCurve('ThreePoint', 10005, 5, 0.0, 116.01681552, 0.02373919, 116.01681552, 0.07121758, 81.21177087, -1331.04213664, 0.05, 2, 0, 70005, 21005, 1, 3)
    ops.uniaxialMaterial('LimitState', 30005, 29.00420388, 9.17e-05, 87.01261164, 0.0002751, 290.0420388, 0.00091701, -29.00420388, -9.17e-05, -87.01261164, -0.0002751, -290.0420388, -0.00091701, 0.4, 0.3, 0.003, 0.0, 0.0, 10005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 5, 99999, 'P', 40005, 'Vy', 30005, 'Vz', 20005, 'My', 10005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170005, 70005, 170005, 5, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121005, 121005, 21005, 5, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170006, 3.0, 5.2, 0.0)
    ops.node(121006, 3.0, 5.2, 2.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 6, 170006, 121006, 0.16, 30799367.16867132, 12833069.65361305, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20006, 203.62029853, 0.00094944, 244.18268254, 0.02800991, 24.41826825, 0.07561586, -203.62029853, -0.00094944, -244.18268254, -0.02800991, -24.41826825, -0.07561586, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10006, 203.62029853, 0.00094944, 244.18268254, 0.02800991, 24.41826825, 0.07561586, -203.62029853, -0.00094944, -244.18268254, -0.02800991, -24.41826825, -0.07561586, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20006, 6, 0.0, 237.12623078, 0.01898876, 237.12623078, 0.05696629, 165.98836155, -3234.95950222, 0.05, 2, 0, 70006, 21006, 2, 3)
    ops.uniaxialMaterial('LimitState', 40006, 59.2815577, 0.00010567, 177.84467309, 0.00031701, 592.81557696, 0.0010567, -59.2815577, -0.00010567, -177.84467309, -0.00031701, -592.81557696, -0.0010567, 0.4, 0.3, 0.003, 0.0, 0.0, 20006, 2)
    ops.limitCurve('ThreePoint', 10006, 6, 0.0, 237.12623078, 0.01898876, 237.12623078, 0.05696629, 165.98836155, -3234.95950222, 0.05, 2, 0, 70006, 21006, 1, 3)
    ops.uniaxialMaterial('LimitState', 30006, 59.2815577, 0.00010567, 177.84467309, 0.00031701, 592.81557696, 0.0010567, -59.2815577, -0.00010567, -177.84467309, -0.00031701, -592.81557696, -0.0010567, 0.4, 0.3, 0.003, 0.0, 0.0, 10006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 6, 99999, 'P', 40006, 'Vy', 30006, 'Vz', 20006, 'My', 10006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170006, 70006, 170006, 6, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121006, 121006, 21006, 6, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170007, 7.65, 5.2, 0.0)
    ops.node(121007, 7.65, 5.2, 2.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 7, 170007, 121007, 0.2025, 30362611.69571528, 12651088.20654804, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20007, 293.26492429, 0.00086994, 352.21331695, 0.0388963, 35.2213317, 0.09960607, -293.26492429, -0.00086994, -352.21331695, -0.0388963, -35.2213317, -0.09960607, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10007, 302.4744039, 0.00086994, 363.27396925, 0.0388963, 36.32739692, 0.09960607, -302.4744039, -0.00086994, -363.27396925, -0.0388963, -36.32739692, -0.09960607, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20007, 7, 0.0, 347.47608192, 0.01739888, 347.47608192, 0.05219663, 243.23325734, -5973.59807045, 0.05, 2, 0, 70007, 21007, 2, 3)
    ops.uniaxialMaterial('LimitState', 40007, 86.86902048, 0.00012411, 260.60706144, 0.00037232, 868.69020479, 0.00124106, -86.86902048, -0.00012411, -260.60706144, -0.00037232, -868.69020479, -0.00124106, 0.4, 0.3, 0.003, 0.0, 0.0, 20007, 2)
    ops.limitCurve('ThreePoint', 10007, 7, 0.0, 347.47608192, 0.01739888, 347.47608192, 0.05219663, 243.23325734, -5973.59807045, 0.05, 2, 0, 70007, 21007, 1, 3)
    ops.uniaxialMaterial('LimitState', 30007, 86.86902048, 0.00012411, 260.60706144, 0.00037232, 868.69020479, 0.00124106, -86.86902048, -0.00012411, -260.60706144, -0.00037232, -868.69020479, -0.00124106, 0.4, 0.3, 0.003, 0.0, 0.0, 10007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 7, 99999, 'P', 40007, 'Vy', 30007, 'Vz', 20007, 'My', 10007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170007, 70007, 170007, 7, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121007, 121007, 21007, 7, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170008, 12.3, 5.2, 0.0)
    ops.node(121008, 12.3, 5.2, 2.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 8, 170008, 121008, 0.16, 29667241.18818079, 12361350.49507533, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20008, 160.37458386, 0.00090925, 193.20026937, 0.02661198, 19.32002694, 0.07589006, -160.37458386, -0.00090925, -193.20026937, -0.02661198, -19.32002694, -0.07589006, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10008, 160.37458386, 0.00090925, 193.20026937, 0.02661198, 19.32002694, 0.07589006, -160.37458386, -0.00090925, -193.20026937, -0.02661198, -19.32002694, -0.07589006, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20008, 8, 0.0, 213.56198754, 0.01818501, 213.56198754, 0.05455502, 149.49339128, -2927.78034406, 0.05, 2, 0, 70008, 21008, 2, 3)
    ops.uniaxialMaterial('LimitState', 40008, 53.39049689, 9.88e-05, 160.17149066, 0.0002964, 533.90496886, 0.00098801, -53.39049689, -9.88e-05, -160.17149066, -0.0002964, -533.90496886, -0.00098801, 0.4, 0.3, 0.003, 0.0, 0.0, 20008, 2)
    ops.limitCurve('ThreePoint', 10008, 8, 0.0, 213.56198754, 0.01818501, 213.56198754, 0.05455502, 149.49339128, -2927.78034406, 0.05, 2, 0, 70008, 21008, 1, 3)
    ops.uniaxialMaterial('LimitState', 30008, 53.39049689, 9.88e-05, 160.17149066, 0.0002964, 533.90496886, 0.00098801, -53.39049689, -9.88e-05, -160.17149066, -0.0002964, -533.90496886, -0.00098801, 0.4, 0.3, 0.003, 0.0, 0.0, 10008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 8, 99999, 'P', 40008, 'Vy', 30008, 'Vz', 20008, 'My', 10008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170008, 70008, 170008, 8, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121008, 121008, 21008, 8, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170009, 0.0, 10.4, 0.0)
    ops.node(121009, 0.0, 10.4, 2.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 9, 170009, 121009, 0.09, 31745954.51912984, 13227481.04963744, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20009, 73.45119165, 0.00120422, 87.96020738, 0.01658634, 8.79602074, 0.05857724, -73.45119165, -0.00120422, -87.96020738, -0.01658634, -8.79602074, -0.05857724, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10009, 68.73301751, 0.00120422, 82.31003934, 0.01658634, 8.23100393, 0.05857724, -68.73301751, -0.00120422, -82.31003934, -0.01658634, -8.23100393, -0.05857724, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20009, 9, 0.0, 121.5387646, 0.02408436, 121.5387646, 0.07225308, 85.07713522, -1410.51753177, 0.05, 2, 0, 70009, 21009, 2, 3)
    ops.uniaxialMaterial('LimitState', 40009, 30.38469115, 9.341e-05, 91.15407345, 0.00028024, 303.84691151, 0.00093415, -30.38469115, -9.341e-05, -91.15407345, -0.00028024, -303.84691151, -0.00093415, 0.4, 0.3, 0.003, 0.0, 0.0, 20009, 2)
    ops.limitCurve('ThreePoint', 10009, 9, 0.0, 121.5387646, 0.02408436, 121.5387646, 0.07225308, 85.07713522, -1410.51753177, 0.05, 2, 0, 70009, 21009, 1, 3)
    ops.uniaxialMaterial('LimitState', 30009, 30.38469115, 9.341e-05, 91.15407345, 0.00028024, 303.84691151, 0.00093415, -30.38469115, -9.341e-05, -91.15407345, -0.00028024, -303.84691151, -0.00093415, 0.4, 0.3, 0.003, 0.0, 0.0, 10009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 9, 99999, 'P', 40009, 'Vy', 30009, 'Vz', 20009, 'My', 10009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170009, 70009, 170009, 9, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121009, 121009, 21009, 9, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170010, 3.0, 10.4, 0.0)
    ops.node(121010, 3.0, 10.4, 2.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 10, 170010, 121010, 0.16, 30205609.85479016, 12585670.77282923, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20010, 212.14067724, 0.00094402, 254.76550814, 0.02923317, 25.47655081, 0.07629657, -212.14067724, -0.00094402, -254.76550814, -0.02923317, -25.47655081, -0.07629657, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10010, 204.83721256, 0.00094402, 245.9945788, 0.02923317, 24.59945788, 0.07629657, -204.83721256, -0.00094402, -245.9945788, -0.02923317, -24.59945788, -0.07629657, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20010, 10, 0.0, 240.91321949, 0.01888034, 240.91321949, 0.05664102, 168.63925364, -3498.05165724, 0.05, 2, 0, 70010, 21010, 2, 3)
    ops.uniaxialMaterial('LimitState', 40010, 60.22830487, 0.00010947, 180.68491462, 0.0003284, 602.28304873, 0.00109468, -60.22830487, -0.00010947, -180.68491462, -0.0003284, -602.28304873, -0.00109468, 0.4, 0.3, 0.003, 0.0, 0.0, 20010, 2)
    ops.limitCurve('ThreePoint', 10010, 10, 0.0, 240.91321949, 0.01888034, 240.91321949, 0.05664102, 168.63925364, -3498.05165724, 0.05, 2, 0, 70010, 21010, 1, 3)
    ops.uniaxialMaterial('LimitState', 30010, 60.22830487, 0.00010947, 180.68491462, 0.0003284, 602.28304873, 0.00109468, -60.22830487, -0.00010947, -180.68491462, -0.0003284, -602.28304873, -0.00109468, 0.4, 0.3, 0.003, 0.0, 0.0, 10010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 10, 99999, 'P', 40010, 'Vy', 30010, 'Vz', 20010, 'My', 10010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170010, 70010, 170010, 10, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121010, 121010, 21010, 10, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170011, 7.65, 10.4, 0.0)
    ops.node(121011, 7.65, 10.4, 2.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 11, 170011, 121011, 0.2025, 30030246.22341901, 12512602.59309125, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20011, 310.34519561, 0.00085458, 372.92788298, 0.03753704, 37.2927883, 0.09742868, -310.34519561, -0.00085458, -372.92788298, -0.03753704, -37.2927883, -0.09742868, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10011, 310.34519561, 0.00085458, 372.92788298, 0.03753704, 37.2927883, 0.09742868, -310.34519561, -0.00085458, -372.92788298, -0.03753704, -37.2927883, -0.09742868, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20011, 11, 0.0, 328.19722225, 0.01709164, 328.19722225, 0.05127493, 229.73805558, -5329.82684961, 0.05, 2, 0, 70011, 21011, 2, 3)
    ops.uniaxialMaterial('LimitState', 40011, 82.04930556, 0.00011852, 246.14791669, 0.00035555, 820.49305563, 0.00118518, -82.04930556, -0.00011852, -246.14791669, -0.00035555, -820.49305563, -0.00118518, 0.4, 0.3, 0.003, 0.0, 0.0, 20011, 2)
    ops.limitCurve('ThreePoint', 10011, 11, 0.0, 328.19722225, 0.01709164, 328.19722225, 0.05127493, 229.73805558, -5329.82684961, 0.05, 2, 0, 70011, 21011, 1, 3)
    ops.uniaxialMaterial('LimitState', 30011, 82.04930556, 0.00011852, 246.14791669, 0.00035555, 820.49305563, 0.00118518, -82.04930556, -0.00011852, -246.14791669, -0.00035555, -820.49305563, -0.00118518, 0.4, 0.3, 0.003, 0.0, 0.0, 10011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 11, 99999, 'P', 40011, 'Vy', 30011, 'Vz', 20011, 'My', 10011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170011, 70011, 170011, 11, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121011, 121011, 21011, 11, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170012, 12.3, 10.4, 0.0)
    ops.node(121012, 12.3, 10.4, 2.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 12, 170012, 121012, 0.16, 31755276.53861723, 13231365.22442385, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20012, 160.31192295, 0.0009253, 192.31737479, 0.02913942, 19.23173748, 0.08193443, -160.31192295, -0.0009253, -192.31737479, -0.02913942, -19.23173748, -0.08193443, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10012, 160.31192295, 0.0009253, 192.31737479, 0.02913942, 19.23173748, 0.08193443, -160.31192295, -0.0009253, -192.31737479, -0.02913942, -19.23173748, -0.08193443, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20012, 12, 0.0, 243.67201923, 0.01850603, 243.67201923, 0.05551809, 170.57041346, -3610.52031065, 0.05, 2, 0, 70012, 21012, 2, 3)
    ops.uniaxialMaterial('LimitState', 40012, 60.91800481, 0.00010532, 182.75401442, 0.00031595, 609.18004807, 0.00105318, -60.91800481, -0.00010532, -182.75401442, -0.00031595, -609.18004807, -0.00105318, 0.4, 0.3, 0.003, 0.0, 0.0, 20012, 2)
    ops.limitCurve('ThreePoint', 10012, 12, 0.0, 243.67201923, 0.01850603, 243.67201923, 0.05551809, 170.57041346, -3610.52031065, 0.05, 2, 0, 70012, 21012, 1, 3)
    ops.uniaxialMaterial('LimitState', 30012, 60.91800481, 0.00010532, 182.75401442, 0.00031595, 609.18004807, 0.00105318, -60.91800481, -0.00010532, -182.75401442, -0.00031595, -609.18004807, -0.00105318, 0.4, 0.3, 0.003, 0.0, 0.0, 10012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 12, 99999, 'P', 40012, 'Vy', 30012, 'Vz', 20012, 'My', 10012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170012, 70012, 170012, 12, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121012, 121012, 21012, 12, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170013, 0.0, 15.6, 0.0)
    ops.node(121013, 0.0, 15.6, 2.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 13, 170013, 121013, 0.0625, 31310018.02162411, 13045840.84234338, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20013, 37.84940974, 0.00132615, 45.46700529, 0.02001548, 4.54670053, 0.07091429, -37.84940974, -0.00132615, -45.46700529, -0.02001548, -4.54670053, -0.07091429, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10013, 37.84940974, 0.00132615, 45.46700529, 0.02001548, 4.54670053, 0.07091429, -37.84940974, -0.00132615, -45.46700529, -0.02001548, -4.54670053, -0.07091429, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20013, 13, 0.0, 93.07399855, 0.02652305, 93.07399855, 0.07956914, 65.15179899, -1387.73738793, 0.05, 2, 0, 70013, 21013, 2, 3)
    ops.uniaxialMaterial('LimitState', 40013, 23.26849964, 0.00010445, 69.80549891, 0.00031334, 232.68499638, 0.00104447, -23.26849964, -0.00010445, -69.80549891, -0.00031334, -232.68499638, -0.00104447, 0.4, 0.3, 0.003, 0.0, 0.0, 20013, 2)
    ops.limitCurve('ThreePoint', 10013, 13, 0.0, 93.07399855, 0.02652305, 93.07399855, 0.07956914, 65.15179899, -1387.73738793, 0.05, 2, 0, 70013, 21013, 1, 3)
    ops.uniaxialMaterial('LimitState', 30013, 23.26849964, 0.00010445, 69.80549891, 0.00031334, 232.68499638, 0.00104447, -23.26849964, -0.00010445, -69.80549891, -0.00031334, -232.68499638, -0.00104447, 0.4, 0.3, 0.003, 0.0, 0.0, 10013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 13, 99999, 'P', 40013, 'Vy', 30013, 'Vz', 20013, 'My', 10013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170013, 70013, 170013, 13, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121013, 121013, 21013, 13, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170014, 3.0, 15.6, 0.0)
    ops.node(121014, 3.0, 15.6, 2.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 14, 170014, 121014, 0.1225, 29173225.20600023, 12155510.50250009, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20014, 117.08025492, 0.0010151, 141.0715531, 0.0237663, 14.10715531, 0.06584553, -117.08025492, -0.0010151, -141.0715531, -0.0237663, -14.10715531, -0.06584553, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10014, 110.79689587, 0.0010151, 133.50065037, 0.0237663, 13.35006504, 0.06584553, -110.79689587, -0.0010151, -133.50065037, -0.0237663, -13.35006504, -0.06584553, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20014, 14, 0.0, 160.27830395, 0.02030194, 160.27830395, 0.06090583, 112.19481276, -2159.03077802, 0.05, 2, 0, 70014, 21014, 2, 3)
    ops.uniaxialMaterial('LimitState', 40014, 40.06957599, 9.849e-05, 120.20872796, 0.00029547, 400.69575987, 0.00098489, -40.06957599, -9.849e-05, -120.20872796, -0.00029547, -400.69575987, -0.00098489, 0.4, 0.3, 0.003, 0.0, 0.0, 20014, 2)
    ops.limitCurve('ThreePoint', 10014, 14, 0.0, 160.27830395, 0.02030194, 160.27830395, 0.06090583, 112.19481276, -2159.03077802, 0.05, 2, 0, 70014, 21014, 1, 3)
    ops.uniaxialMaterial('LimitState', 30014, 40.06957599, 9.849e-05, 120.20872796, 0.00029547, 400.69575987, 0.00098489, -40.06957599, -9.849e-05, -120.20872796, -0.00029547, -400.69575987, -0.00098489, 0.4, 0.3, 0.003, 0.0, 0.0, 10014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 14, 99999, 'P', 40014, 'Vy', 30014, 'Vz', 20014, 'My', 10014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170014, 70014, 170014, 14, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121014, 121014, 21014, 14, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170015, 7.65, 15.6, 0.0)
    ops.node(121015, 7.65, 15.6, 2.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 15, 170015, 121015, 0.16, 31236704.02526855, 13015293.3438619, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20015, 182.08572161, 0.00094476, 218.71734809, 0.03297197, 21.87173481, 0.0850873, -182.08572161, -0.00094476, -218.71734809, -0.03297197, -21.87173481, -0.0850873, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10015, 174.13461358, 0.00094476, 209.16665269, 0.03297197, 20.91666527, 0.0850873, -174.13461358, -0.00094476, -209.16665269, -0.03297197, -20.91666527, -0.0850873, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20015, 15, 0.0, 234.88855133, 0.01889519, 234.88855133, 0.05668558, 164.42198593, -3401.77309893, 0.05, 2, 0, 70015, 21015, 2, 3)
    ops.uniaxialMaterial('LimitState', 40015, 58.72213783, 0.00010321, 176.1664135, 0.00030962, 587.22137832, 0.00103207, -58.72213783, -0.00010321, -176.1664135, -0.00030962, -587.22137832, -0.00103207, 0.4, 0.3, 0.003, 0.0, 0.0, 20015, 2)
    ops.limitCurve('ThreePoint', 10015, 15, 0.0, 234.88855133, 0.01889519, 234.88855133, 0.05668558, 164.42198593, -3401.77309893, 0.05, 2, 0, 70015, 21015, 1, 3)
    ops.uniaxialMaterial('LimitState', 30015, 58.72213783, 0.00010321, 176.1664135, 0.00030962, 587.22137832, 0.00103207, -58.72213783, -0.00010321, -176.1664135, -0.00030962, -587.22137832, -0.00103207, 0.4, 0.3, 0.003, 0.0, 0.0, 10015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 15, 99999, 'P', 40015, 'Vy', 30015, 'Vz', 20015, 'My', 10015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170015, 70015, 170015, 15, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121015, 121015, 21015, 15, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170016, 12.3, 15.6, 0.0)
    ops.node(121016, 12.3, 15.6, 2.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 16, 170016, 121016, 0.09, 29536797.98176469, 12306999.15906862, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20016, 66.29711028, 0.00115269, 79.89107494, 0.01720766, 7.98910749, 0.05846784, -66.29711028, -0.00115269, -79.89107494, -0.01720766, -7.98910749, -0.05846784, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10016, 61.61275307, 0.00115269, 74.24620851, 0.01720766, 7.42462085, 0.05846784, -61.61275307, -0.00115269, -74.24620851, -0.01720766, -7.42462085, -0.05846784, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20016, 16, 0.0, 113.36521882, 0.02305376, 113.36521882, 0.06916128, 79.35565317, -1446.70748084, 0.05, 2, 0, 70016, 21016, 2, 3)
    ops.uniaxialMaterial('LimitState', 40016, 28.3413047, 9.365e-05, 85.02391411, 0.00028095, 283.41304704, 0.0009365, -28.3413047, -9.365e-05, -85.02391411, -0.00028095, -283.41304704, -0.0009365, 0.4, 0.3, 0.003, 0.0, 0.0, 20016, 2)
    ops.limitCurve('ThreePoint', 10016, 16, 0.0, 113.36521882, 0.02305376, 113.36521882, 0.06916128, 79.35565317, -1446.70748084, 0.05, 2, 0, 70016, 21016, 1, 3)
    ops.uniaxialMaterial('LimitState', 30016, 28.3413047, 9.365e-05, 85.02391411, 0.00028095, 283.41304704, 0.0009365, -28.3413047, -9.365e-05, -85.02391411, -0.00028095, -283.41304704, -0.0009365, 0.4, 0.3, 0.003, 0.0, 0.0, 10016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 16, 99999, 'P', 40016, 'Vy', 30016, 'Vz', 20016, 'My', 10016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170016, 70016, 170016, 16, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121016, 121016, 21016, 16, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171003, 7.65, 0.0, 3.3)
    ops.node(122003, 7.65, 0.0, 5.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1003, 171003, 122003, 0.16, 32686810.6782801, 13619504.44928337, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21003, 138.64193747, 0.00084776, 166.30598375, 0.02931609, 16.63059838, 0.08731231, -138.64193747, -0.00084776, -166.30598375, -0.02931609, -16.63059838, -0.08731231, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11003, 119.17121311, 0.00084776, 142.95015054, 0.02931609, 14.29501505, 0.08731231, -119.17121311, -0.00084776, -142.95015054, -0.02931609, -14.29501505, -0.08731231, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21003, 1003, 0.0, 232.03732756, 0.01695522, 232.03732756, 0.05086567, 162.42612929, -3981.01060036, 0.05, 2, 0, 71003, 22003, 2, 3)
    ops.uniaxialMaterial('LimitState', 41003, 58.00933189, 8.785e-05, 174.02799567, 0.00026354, 580.0933189, 0.00087848, -58.00933189, -8.785e-05, -174.02799567, -0.00026354, -580.0933189, -0.00087848, 0.4, 0.3, 0.003, 0.0, 0.0, 21003, 2)
    ops.limitCurve('ThreePoint', 11003, 1003, 0.0, 232.03732756, 0.01695522, 232.03732756, 0.05086567, 162.42612929, -3981.01060036, 0.05, 2, 0, 71003, 22003, 1, 3)
    ops.uniaxialMaterial('LimitState', 31003, 58.00933189, 8.785e-05, 174.02799567, 0.00026354, 580.0933189, 0.00087848, -58.00933189, -8.785e-05, -174.02799567, -0.00026354, -580.0933189, -0.00087848, 0.4, 0.3, 0.003, 0.0, 0.0, 11003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1003, 99999, 'P', 41003, 'Vy', 31003, 'Vz', 21003, 'My', 11003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171003, 71003, 171003, 1003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122003, 122003, 22003, 1003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171004, 12.3, 0.0, 3.275)
    ops.node(122004, 12.3, 0.0, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1004, 171004, 122004, 0.09, 33207291.86222024, 13836371.60925843, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21004, 51.87150714, 0.00100833, 62.12397046, 0.02541689, 6.21239705, 0.08399691, -51.87150714, -0.00100833, -62.12397046, -0.02541689, -6.21239705, -0.08399691, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11004, 55.53059322, 0.00100833, 66.50627912, 0.02541689, 6.65062791, 0.08399691, -55.53059322, -0.00100833, -66.50627912, -0.02541689, -6.65062791, -0.08399691, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21004, 1004, 0.0, 134.26437037, 0.02016667, 134.26437037, 0.0605, 93.98505926, -2355.73229058, 0.05, 2, 0, 71004, 22004, 2, 3)
    ops.uniaxialMaterial('LimitState', 41004, 33.56609259, 8.895e-05, 100.69827778, 0.00026685, 335.66092592, 0.00088951, -33.56609259, -8.895e-05, -100.69827778, -0.00026685, -335.66092592, -0.00088951, 0.4, 0.3, 0.003, 0.0, 0.0, 21004, 2)
    ops.limitCurve('ThreePoint', 11004, 1004, 0.0, 134.26437037, 0.02016667, 134.26437037, 0.0605, 93.98505926, -2355.73229058, 0.05, 2, 0, 71004, 22004, 1, 3)
    ops.uniaxialMaterial('LimitState', 31004, 33.56609259, 8.895e-05, 100.69827778, 0.00026685, 335.66092592, 0.00088951, -33.56609259, -8.895e-05, -100.69827778, -0.00026685, -335.66092592, -0.00088951, 0.4, 0.3, 0.003, 0.0, 0.0, 11004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1004, 99999, 'P', 41004, 'Vy', 31004, 'Vz', 21004, 'My', 11004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171004, 71004, 171004, 1004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122004, 122004, 22004, 1004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171005, 0.0, 5.2, 3.275)
    ops.node(122005, 0.0, 5.2, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1005, 171005, 122005, 0.09, 31145958.86428956, 12977482.86012065, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21005, 61.63636943, 0.00101142, 74.13637349, 0.01765532, 7.41363735, 0.06278396, -61.63636943, -0.00101142, -74.13637349, -0.01765532, -7.41363735, -0.06278396, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11005, 57.19661439, 0.00101142, 68.79622543, 0.01765532, 6.87962254, 0.06278396, -57.19661439, -0.00101142, -68.79622543, -0.01765532, -6.87962254, -0.06278396, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21005, 1005, 0.0, 113.91193652, 0.02022831, 113.91193652, 0.06068492, 79.73835556, -1544.41792189, 0.05, 2, 0, 71005, 22005, 2, 3)
    ops.uniaxialMaterial('LimitState', 41005, 28.47798413, 8.046e-05, 85.43395239, 0.00024139, 284.77984129, 0.00080462, -28.47798413, -8.046e-05, -85.43395239, -0.00024139, -284.77984129, -0.00080462, 0.4, 0.3, 0.003, 0.0, 0.0, 21005, 2)
    ops.limitCurve('ThreePoint', 11005, 1005, 0.0, 113.91193652, 0.02022831, 113.91193652, 0.06068492, 79.73835556, -1544.41792189, 0.05, 2, 0, 71005, 22005, 1, 3)
    ops.uniaxialMaterial('LimitState', 31005, 28.47798413, 8.046e-05, 85.43395239, 0.00024139, 284.77984129, 0.00080462, -28.47798413, -8.046e-05, -85.43395239, -0.00024139, -284.77984129, -0.00080462, 0.4, 0.3, 0.003, 0.0, 0.0, 11005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1005, 99999, 'P', 41005, 'Vy', 31005, 'Vz', 21005, 'My', 11005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171005, 71005, 171005, 1005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122005, 122005, 22005, 1005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171006, 3.0, 5.2, 3.3)
    ops.node(122006, 3.0, 5.2, 5.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1006, 171006, 122006, 0.16, 33143914.22527458, 13809964.26053108, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21006, 158.54780218, 0.00084428, 189.61553696, 0.0179644, 18.9615537, 0.06250909, -158.54780218, -0.00084428, -189.61553696, -0.0179644, -18.9615537, -0.06250909, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11006, 135.53020367, 0.00084428, 162.08759749, 0.0179644, 16.20875975, 0.06250909, -135.53020367, -0.00084428, -162.08759749, -0.0179644, -16.20875975, -0.06250909, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21006, 1006, 0.0, 202.6805102, 0.01688552, 202.6805102, 0.05065655, 141.87635714, -2346.0590352, 0.05, 2, 0, 71006, 22006, 2, 3)
    ops.uniaxialMaterial('LimitState', 41006, 50.67012755, 7.568e-05, 152.01038265, 0.00022703, 506.7012755, 0.00075675, -50.67012755, -7.568e-05, -152.01038265, -0.00022703, -506.7012755, -0.00075675, 0.4, 0.3, 0.003, 0.0, 0.0, 21006, 2)
    ops.limitCurve('ThreePoint', 11006, 1006, 0.0, 202.6805102, 0.01688552, 202.6805102, 0.05065655, 141.87635714, -2346.0590352, 0.05, 2, 0, 71006, 22006, 1, 3)
    ops.uniaxialMaterial('LimitState', 31006, 50.67012755, 7.568e-05, 152.01038265, 0.00022703, 506.7012755, 0.00075675, -50.67012755, -7.568e-05, -152.01038265, -0.00022703, -506.7012755, -0.00075675, 0.4, 0.3, 0.003, 0.0, 0.0, 11006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1006, 99999, 'P', 41006, 'Vy', 31006, 'Vz', 21006, 'My', 11006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171006, 71006, 171006, 1006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122006, 122006, 22006, 1006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171007, 7.65, 5.2, 3.3)
    ops.node(122007, 7.65, 5.2, 5.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1007, 171007, 122007, 0.2025, 28648574.50466887, 11936906.04361203, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21007, 202.24449138, 0.00078359, 244.41673926, 0.02920716, 24.44167393, 0.07457722, -202.24449138, -0.00078359, -244.41673926, -0.02920716, -24.44167393, -0.07457722, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11007, 169.93644618, 0.00078359, 205.37178429, 0.02920716, 20.53717843, 0.07457722, -169.93644618, -0.00078359, -205.37178429, -0.02920716, -20.53717843, -0.07457722, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21007, 1007, 0.0, 273.02336716, 0.01567189, 273.02336716, 0.04701567, 191.11635701, -4497.86835142, 0.05, 2, 0, 71007, 22007, 2, 3)
    ops.uniaxialMaterial('LimitState', 41007, 68.25584179, 9.318e-05, 204.76752537, 0.00027955, 682.55841789, 0.00093183, -68.25584179, -9.318e-05, -204.76752537, -0.00027955, -682.55841789, -0.00093183, 0.4, 0.3, 0.003, 0.0, 0.0, 21007, 2)
    ops.limitCurve('ThreePoint', 11007, 1007, 0.0, 273.02336716, 0.01567189, 273.02336716, 0.04701567, 191.11635701, -4497.86835142, 0.05, 2, 0, 71007, 22007, 1, 3)
    ops.uniaxialMaterial('LimitState', 31007, 68.25584179, 9.318e-05, 204.76752537, 0.00027955, 682.55841789, 0.00093183, -68.25584179, -9.318e-05, -204.76752537, -0.00027955, -682.55841789, -0.00093183, 0.4, 0.3, 0.003, 0.0, 0.0, 11007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1007, 99999, 'P', 41007, 'Vy', 31007, 'Vz', 21007, 'My', 11007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171007, 71007, 171007, 1007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122007, 122007, 22007, 1007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171008, 12.3, 5.2, 3.275)
    ops.node(122008, 12.3, 5.2, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1008, 171008, 122008, 0.16, 31197573.65977765, 12998989.02490735, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21008, 141.45154054, 0.000836, 170.3598708, 0.01702594, 17.03598708, 0.05516254, -141.45154054, -0.000836, -170.3598708, -0.01702594, -17.03598708, -0.05516254, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11008, 119.9864142, 0.000836, 144.50793496, 0.01702594, 14.4507935, 0.05516254, -119.9864142, -0.000836, -144.50793496, -0.01702594, -14.4507935, -0.05516254, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21008, 1008, 0.0, 181.50934084, 0.01672001, 181.50934084, 0.05016003, 127.05653859, -2178.77905645, 0.05, 2, 0, 71008, 22008, 2, 3)
    ops.uniaxialMaterial('LimitState', 41008, 45.37733521, 7.2e-05, 136.13200563, 0.000216, 453.7733521, 0.00071998, -45.37733521, -7.2e-05, -136.13200563, -0.000216, -453.7733521, -0.00071998, 0.4, 0.3, 0.003, 0.0, 0.0, 21008, 2)
    ops.limitCurve('ThreePoint', 11008, 1008, 0.0, 181.50934084, 0.01672001, 181.50934084, 0.05016003, 127.05653859, -2178.77905645, 0.05, 2, 0, 71008, 22008, 1, 3)
    ops.uniaxialMaterial('LimitState', 31008, 45.37733521, 7.2e-05, 136.13200563, 0.000216, 453.7733521, 0.00071998, -45.37733521, -7.2e-05, -136.13200563, -0.000216, -453.7733521, -0.00071998, 0.4, 0.3, 0.003, 0.0, 0.0, 11008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1008, 99999, 'P', 41008, 'Vy', 31008, 'Vz', 21008, 'My', 11008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171008, 71008, 171008, 1008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122008, 122008, 22008, 1008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171009, 0.0, 10.4, 3.275)
    ops.node(122009, 0.0, 10.4, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1009, 171009, 122009, 0.09, 28469704.83172237, 11862377.01321765, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21009, 62.65058722, 0.00107038, 75.73501368, 0.01573453, 7.57350137, 0.05729508, -62.65058722, -0.00107038, -75.73501368, -0.01573453, -7.57350137, -0.05729508, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11009, 57.86844682, 0.00107038, 69.95413461, 0.01573453, 6.99541346, 0.05729508, -57.86844682, -0.00107038, -69.95413461, -0.01573453, -6.99541346, -0.05729508, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21009, 1009, 0.0, 102.63796537, 0.02140769, 102.63796537, 0.06422308, 71.84657576, -1417.29676383, 0.05, 2, 0, 71009, 22009, 2, 3)
    ops.uniaxialMaterial('LimitState', 41009, 25.65949134, 7.931e-05, 76.97847403, 0.00023794, 256.59491343, 0.00079314, -25.65949134, -7.931e-05, -76.97847403, -0.00023794, -256.59491343, -0.00079314, 0.4, 0.3, 0.003, 0.0, 0.0, 21009, 2)
    ops.limitCurve('ThreePoint', 11009, 1009, 0.0, 102.63796537, 0.02140769, 102.63796537, 0.06422308, 71.84657576, -1417.29676383, 0.05, 2, 0, 71009, 22009, 1, 3)
    ops.uniaxialMaterial('LimitState', 31009, 25.65949134, 7.931e-05, 76.97847403, 0.00023794, 256.59491343, 0.00079314, -25.65949134, -7.931e-05, -76.97847403, -0.00023794, -256.59491343, -0.00079314, 0.4, 0.3, 0.003, 0.0, 0.0, 11009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1009, 99999, 'P', 41009, 'Vy', 31009, 'Vz', 21009, 'My', 11009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171009, 71009, 171009, 1009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122009, 122009, 22009, 1009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171010, 3.0, 10.4, 3.3)
    ops.node(122010, 3.0, 10.4, 5.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1010, 171010, 122010, 0.16, 30835971.22915247, 12848321.34548019, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21010, 148.89102887, 0.00082695, 179.19600495, 0.02005959, 17.91960049, 0.06255229, -148.89102887, -0.00082695, -179.19600495, -0.02005959, -17.91960049, -0.06255229, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11010, 127.48281603, 0.00082695, 153.43040817, 0.02005959, 15.34304082, 0.06255229, -127.48281603, -0.00082695, -153.43040817, -0.02005959, -15.34304082, -0.06255229, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21010, 1010, 0.0, 190.16776462, 0.01653905, 190.16776462, 0.04961714, 133.11743523, -2361.33614933, 0.05, 2, 0, 71010, 22010, 2, 3)
    ops.uniaxialMaterial('LimitState', 41010, 47.54194116, 7.632e-05, 142.62582347, 0.00022895, 475.41941155, 0.00076318, -47.54194116, -7.632e-05, -142.62582347, -0.00022895, -475.41941155, -0.00076318, 0.4, 0.3, 0.003, 0.0, 0.0, 21010, 2)
    ops.limitCurve('ThreePoint', 11010, 1010, 0.0, 190.16776462, 0.01653905, 190.16776462, 0.04961714, 133.11743523, -2361.33614933, 0.05, 2, 0, 71010, 22010, 1, 3)
    ops.uniaxialMaterial('LimitState', 31010, 47.54194116, 7.632e-05, 142.62582347, 0.00022895, 475.41941155, 0.00076318, -47.54194116, -7.632e-05, -142.62582347, -0.00022895, -475.41941155, -0.00076318, 0.4, 0.3, 0.003, 0.0, 0.0, 11010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1010, 99999, 'P', 41010, 'Vy', 31010, 'Vz', 21010, 'My', 11010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171010, 71010, 171010, 1010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122010, 122010, 22010, 1010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171011, 7.65, 10.4, 3.3)
    ops.node(122011, 7.65, 10.4, 5.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1011, 171011, 122011, 0.2025, 28831162.20095946, 12012984.25039978, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21011, 200.79567641, 0.00082082, 242.60575007, 0.02539108, 24.26057501, 0.07108578, -200.79567641, -0.00082082, -242.60575007, -0.02539108, -24.26057501, -0.07108578, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11011, 170.9660277, 0.00082082, 206.5649128, 0.02539108, 20.65649128, 0.07108578, -170.9660277, -0.00082082, -206.5649128, -0.02539108, -20.65649128, -0.07108578, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21011, 1011, 0.0, 252.10702475, 0.01641644, 252.10702475, 0.04924933, 176.47491732, -3632.29506226, 0.05, 2, 0, 71011, 22011, 2, 3)
    ops.uniaxialMaterial('LimitState', 41011, 63.02675619, 8.55e-05, 189.08026856, 0.0002565, 630.26756187, 0.00085499, -63.02675619, -8.55e-05, -189.08026856, -0.0002565, -630.26756187, -0.00085499, 0.4, 0.3, 0.003, 0.0, 0.0, 21011, 2)
    ops.limitCurve('ThreePoint', 11011, 1011, 0.0, 252.10702475, 0.01641644, 252.10702475, 0.04924933, 176.47491732, -3632.29506226, 0.05, 2, 0, 71011, 22011, 1, 3)
    ops.uniaxialMaterial('LimitState', 31011, 63.02675619, 8.55e-05, 189.08026856, 0.0002565, 630.26756187, 0.00085499, -63.02675619, -8.55e-05, -189.08026856, -0.0002565, -630.26756187, -0.00085499, 0.4, 0.3, 0.003, 0.0, 0.0, 11011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1011, 99999, 'P', 41011, 'Vy', 31011, 'Vz', 21011, 'My', 11011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171011, 71011, 171011, 1011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122011, 122011, 22011, 1011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171012, 12.3, 10.4, 3.275)
    ops.node(122012, 12.3, 10.4, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1012, 171012, 122012, 0.16, 29112165.54338898, 12130068.97641208, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21012, 142.86731312, 0.00087967, 172.82729314, 0.01415886, 17.28272931, 0.05030063, -142.86731312, -0.00087967, -172.82729314, -0.01415886, -17.28272931, -0.05030063, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11012, 120.99614543, 0.00087967, 146.36963374, 0.01415886, 14.63696337, 0.05030063, -120.99614543, -0.00087967, -146.36963374, -0.01415886, -14.63696337, -0.05030063, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21012, 1012, 0.0, 161.39700614, 0.01759342, 161.39700614, 0.05278027, 112.9779043, -1844.34570466, 0.05, 2, 0, 71012, 22012, 2, 3)
    ops.uniaxialMaterial('LimitState', 41012, 40.34925153, 6.861e-05, 121.0477546, 0.00020582, 403.49251534, 0.00068607, -40.34925153, -6.861e-05, -121.0477546, -0.00020582, -403.49251534, -0.00068607, 0.4, 0.3, 0.003, 0.0, 0.0, 21012, 2)
    ops.limitCurve('ThreePoint', 11012, 1012, 0.0, 161.39700614, 0.01759342, 161.39700614, 0.05278027, 112.9779043, -1844.34570466, 0.05, 2, 0, 71012, 22012, 1, 3)
    ops.uniaxialMaterial('LimitState', 31012, 40.34925153, 6.861e-05, 121.0477546, 0.00020582, 403.49251534, 0.00068607, -40.34925153, -6.861e-05, -121.0477546, -0.00020582, -403.49251534, -0.00068607, 0.4, 0.3, 0.003, 0.0, 0.0, 11012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1012, 99999, 'P', 41012, 'Vy', 31012, 'Vz', 21012, 'My', 11012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171012, 71012, 171012, 1012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122012, 122012, 22012, 1012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171013, 0.0, 15.6, 3.275)
    ops.node(122013, 0.0, 15.6, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1013, 171013, 122013, 0.0625, 31634465.25138603, 13181027.18807751, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21013, 33.76461191, 0.00114819, 40.63197141, 0.02009183, 4.06319714, 0.07548649, -33.76461191, -0.00114819, -40.63197141, -0.02009183, -4.06319714, -0.07548649, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11013, 33.76461191, 0.00114819, 40.63197141, 0.02009183, 4.06319714, 0.07548649, -33.76461191, -0.00114819, -40.63197141, -0.02009183, -4.06319714, -0.07548649, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21013, 1013, 0.0, 87.33897872, 0.02296384, 87.33897872, 0.06889151, 61.13728511, -1530.19877895, 0.05, 2, 0, 71013, 22013, 2, 3)
    ops.uniaxialMaterial('LimitState', 41013, 21.83474468, 8.746e-05, 65.50423404, 0.00026239, 218.34744681, 0.00087465, -21.83474468, -8.746e-05, -65.50423404, -0.00026239, -218.34744681, -0.00087465, 0.4, 0.3, 0.003, 0.0, 0.0, 21013, 2)
    ops.limitCurve('ThreePoint', 11013, 1013, 0.0, 87.33897872, 0.02296384, 87.33897872, 0.06889151, 61.13728511, -1530.19877895, 0.05, 2, 0, 71013, 22013, 1, 3)
    ops.uniaxialMaterial('LimitState', 31013, 21.83474468, 8.746e-05, 65.50423404, 0.00026239, 218.34744681, 0.00087465, -21.83474468, -8.746e-05, -65.50423404, -0.00026239, -218.34744681, -0.00087465, 0.4, 0.3, 0.003, 0.0, 0.0, 11013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1013, 99999, 'P', 41013, 'Vy', 31013, 'Vz', 21013, 'My', 11013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171013, 71013, 171013, 1013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122013, 122013, 22013, 1013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171014, 3.0, 15.6, 3.3)
    ops.node(122014, 3.0, 15.6, 5.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1014, 171014, 122014, 0.1225, 29797622.31469679, 12415675.96445699, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21014, 92.08850166, 0.00096912, 111.22025845, 0.02841622, 11.12202584, 0.08838024, -92.08850166, -0.00096912, -111.22025845, -0.02841622, -11.12202584, -0.08838024, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11014, 92.08850166, 0.00096912, 111.22025845, 0.02841622, 11.12202584, 0.08838024, -92.08850166, -0.00096912, -111.22025845, -0.02841622, -11.12202584, -0.08838024, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21014, 1014, 0.0, 169.29058933, 0.01938237, 169.29058933, 0.0581471, 118.50341253, -3091.08188634, 0.05, 2, 0, 71014, 22014, 2, 3)
    ops.uniaxialMaterial('LimitState', 41014, 42.32264733, 9.183e-05, 126.967942, 0.00027549, 423.22647332, 0.00091829, -42.32264733, -9.183e-05, -126.967942, -0.00027549, -423.22647332, -0.00091829, 0.4, 0.3, 0.003, 0.0, 0.0, 21014, 2)
    ops.limitCurve('ThreePoint', 11014, 1014, 0.0, 169.29058933, 0.01938237, 169.29058933, 0.0581471, 118.50341253, -3091.08188634, 0.05, 2, 0, 71014, 22014, 1, 3)
    ops.uniaxialMaterial('LimitState', 31014, 42.32264733, 9.183e-05, 126.967942, 0.00027549, 423.22647332, 0.00091829, -42.32264733, -9.183e-05, -126.967942, -0.00027549, -423.22647332, -0.00091829, 0.4, 0.3, 0.003, 0.0, 0.0, 11014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1014, 99999, 'P', 41014, 'Vy', 31014, 'Vz', 21014, 'My', 11014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171014, 71014, 171014, 1014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122014, 122014, 22014, 1014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171015, 7.65, 15.6, 3.3)
    ops.node(122015, 7.65, 15.6, 5.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1015, 171015, 122015, 0.16, 28932777.84087041, 12055324.10036267, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21015, 147.49957603, 0.00093156, 178.49962715, 0.03422417, 17.84996271, 0.08731144, -147.49957603, -0.00093156, -178.49962715, -0.03422417, -17.84996271, -0.08731144, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11015, 134.00666674, 0.00093156, 162.17090715, 0.03422417, 16.21709071, 0.08731144, -134.00666674, -0.00093156, -162.17090715, -0.03422417, -16.21709071, -0.08731144, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21015, 1015, 0.0, 209.97853532, 0.01863114, 209.97853532, 0.05589343, 146.98497472, -3818.27045391, 0.05, 2, 0, 71015, 22015, 2, 3)
    ops.uniaxialMaterial('LimitState', 41015, 52.49463383, 8.981e-05, 157.48390149, 0.00026943, 524.94633829, 0.00089811, -52.49463383, -8.981e-05, -157.48390149, -0.00026943, -524.94633829, -0.00089811, 0.4, 0.3, 0.003, 0.0, 0.0, 21015, 2)
    ops.limitCurve('ThreePoint', 11015, 1015, 0.0, 209.97853532, 0.01863114, 209.97853532, 0.05589343, 146.98497472, -3818.27045391, 0.05, 2, 0, 71015, 22015, 1, 3)
    ops.uniaxialMaterial('LimitState', 31015, 52.49463383, 8.981e-05, 157.48390149, 0.00026943, 524.94633829, 0.00089811, -52.49463383, -8.981e-05, -157.48390149, -0.00026943, -524.94633829, -0.00089811, 0.4, 0.3, 0.003, 0.0, 0.0, 11015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1015, 99999, 'P', 41015, 'Vy', 31015, 'Vz', 21015, 'My', 11015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171015, 71015, 171015, 1015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122015, 122015, 22015, 1015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171016, 12.3, 15.6, 3.275)
    ops.node(122016, 12.3, 15.6, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1016, 171016, 122016, 0.09, 29763467.94681929, 12401444.97784137, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21016, 53.81443373, 0.00108907, 65.02839055, 0.02137396, 6.50283906, 0.07581805, -53.81443373, -0.00108907, -65.02839055, -0.02137396, -6.50283906, -0.07581805, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11016, 58.00964548, 0.00108907, 70.09780872, 0.02137396, 7.00978087, 0.07581805, -58.00964548, -0.00108907, -70.09780872, -0.02137396, -7.00978087, -0.07581805, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21016, 1016, 0.0, 114.31331607, 0.02178145, 114.31331607, 0.06534434, 80.01932125, -1878.85682057, 0.05, 2, 0, 71016, 22016, 2, 3)
    ops.uniaxialMaterial('LimitState', 41016, 28.57832902, 8.45e-05, 85.73498706, 0.00025349, 285.78329019, 0.00084496, -28.57832902, -8.45e-05, -85.73498706, -0.00025349, -285.78329019, -0.00084496, 0.4, 0.3, 0.003, 0.0, 0.0, 21016, 2)
    ops.limitCurve('ThreePoint', 11016, 1016, 0.0, 114.31331607, 0.02178145, 114.31331607, 0.06534434, 80.01932125, -1878.85682057, 0.05, 2, 0, 71016, 22016, 1, 3)
    ops.uniaxialMaterial('LimitState', 31016, 28.57832902, 8.45e-05, 85.73498706, 0.00025349, 285.78329019, 0.00084496, -28.57832902, -8.45e-05, -85.73498706, -0.00025349, -285.78329019, -0.00084496, 0.4, 0.3, 0.003, 0.0, 0.0, 11016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1016, 99999, 'P', 41016, 'Vy', 31016, 'Vz', 21016, 'My', 11016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171016, 71016, 171016, 1016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122016, 122016, 22016, 1016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172003, 7.65, 0.0, 6.05)
    ops.node(123003, 7.65, 0.0, 8.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2003, 172003, 123003, 0.1225, 30459682.73689429, 12691534.47370596, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22003, 87.49303937, 0.00093135, 105.7120369, 0.02041901, 10.57120369, 0.07147904, -87.49303937, -0.00093135, -105.7120369, -0.02041901, -10.57120369, -0.07147904, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12003, 76.75240256, 0.00093135, 92.73483777, 0.02041901, 9.27348378, 0.07147904, -76.75240256, -0.00093135, -92.73483777, -0.02041901, -9.27348378, -0.07147904, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22003, 2003, 0.0, 143.85790374, 0.01862708, 143.85790374, 0.05588125, 100.70053262, -2178.59945547, 0.05, 2, 0, 72003, 23003, 2, 3)
    ops.uniaxialMaterial('LimitState', 42003, 35.96447593, 7.634e-05, 107.8934278, 0.00022901, 359.64475934, 0.00076337, -35.96447593, -7.634e-05, -107.8934278, -0.00022901, -359.64475934, -0.00076337, 0.4, 0.3, 0.003, 0.0, 0.0, 22003, 2)
    ops.limitCurve('ThreePoint', 12003, 2003, 0.0, 143.85790374, 0.01862708, 143.85790374, 0.05588125, 100.70053262, -2178.59945547, 0.05, 2, 0, 72003, 23003, 1, 3)
    ops.uniaxialMaterial('LimitState', 32003, 35.96447593, 7.634e-05, 107.8934278, 0.00022901, 359.64475934, 0.00076337, -35.96447593, -7.634e-05, -107.8934278, -0.00022901, -359.64475934, -0.00076337, 0.4, 0.3, 0.003, 0.0, 0.0, 12003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2003, 99999, 'P', 42003, 'Vy', 32003, 'Vz', 22003, 'My', 12003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172003, 72003, 172003, 2003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123003, 123003, 23003, 2003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172004, 12.3, 0.0, 6.025)
    ops.node(123004, 12.3, 0.0, 8.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2004, 172004, 123004, 0.0625, 31022146.02594959, 12925894.177479, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22004, 30.59890496, 0.00121857, 36.90192386, 0.02101563, 3.69019239, 0.07667719, -30.59890496, -0.00121857, -36.90192386, -0.02101563, -3.69019239, -0.07667719, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12004, 30.59890496, 0.00121857, 36.90192386, 0.02101563, 3.69019239, 0.07667719, -30.59890496, -0.00121857, -36.90192386, -0.02101563, -3.69019239, -0.07667719, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22004, 2004, 0.0, 85.38165784, 0.02437134, 85.38165784, 0.07311401, 59.76716049, -1576.44290324, 0.05, 2, 0, 72004, 23004, 2, 3)
    ops.uniaxialMaterial('LimitState', 42004, 21.34541446, 8.719e-05, 64.03624338, 0.00026158, 213.4541446, 0.00087192, -21.34541446, -8.719e-05, -64.03624338, -0.00026158, -213.4541446, -0.00087192, 0.4, 0.3, 0.003, 0.0, 0.0, 22004, 2)
    ops.limitCurve('ThreePoint', 12004, 2004, 0.0, 85.38165784, 0.02437134, 85.38165784, 0.07311401, 59.76716049, -1576.44290324, 0.05, 2, 0, 72004, 23004, 1, 3)
    ops.uniaxialMaterial('LimitState', 32004, 21.34541446, 8.719e-05, 64.03624338, 0.00026158, 213.4541446, 0.00087192, -21.34541446, -8.719e-05, -64.03624338, -0.00026158, -213.4541446, -0.00087192, 0.4, 0.3, 0.003, 0.0, 0.0, 12004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2004, 99999, 'P', 42004, 'Vy', 32004, 'Vz', 22004, 'My', 12004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172004, 72004, 172004, 2004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123004, 123004, 23004, 2004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172005, 0.0, 5.2, 6.025)
    ops.node(123005, 0.0, 5.2, 8.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2005, 172005, 123005, 0.0625, 29648948.29106077, 12353728.45460865, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22005, 33.04432947, 0.00116026, 39.89900485, 0.01775146, 3.98990049, 0.06872472, -33.04432947, -0.00116026, -39.89900485, -0.01775146, -3.98990049, -0.06872472, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12005, 33.04432947, 0.00116026, 39.89900485, 0.01775146, 3.98990049, 0.06872472, -33.04432947, -0.00116026, -39.89900485, -0.01775146, -3.98990049, -0.06872472, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22005, 2005, 0.0, 74.23892693, 0.02320525, 74.23892693, 0.06961574, 51.96724885, -1181.87017668, 0.05, 2, 0, 72005, 23005, 2, 3)
    ops.uniaxialMaterial('LimitState', 42005, 18.55973173, 7.932e-05, 55.6791952, 0.00023797, 185.59731732, 0.00079325, -18.55973173, -7.932e-05, -55.6791952, -0.00023797, -185.59731732, -0.00079325, 0.4, 0.3, 0.003, 0.0, 0.0, 22005, 2)
    ops.limitCurve('ThreePoint', 12005, 2005, 0.0, 74.23892693, 0.02320525, 74.23892693, 0.06961574, 51.96724885, -1181.87017668, 0.05, 2, 0, 72005, 23005, 1, 3)
    ops.uniaxialMaterial('LimitState', 32005, 18.55973173, 7.932e-05, 55.6791952, 0.00023797, 185.59731732, 0.00079325, -18.55973173, -7.932e-05, -55.6791952, -0.00023797, -185.59731732, -0.00079325, 0.4, 0.3, 0.003, 0.0, 0.0, 12005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2005, 99999, 'P', 42005, 'Vy', 32005, 'Vz', 22005, 'My', 12005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172005, 72005, 172005, 2005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123005, 123005, 23005, 2005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172006, 3.0, 5.2, 6.05)
    ops.node(123006, 3.0, 5.2, 8.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2006, 172006, 123006, 0.1225, 31852761.18597458, 13271983.82748941, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22006, 97.19343161, 0.00090819, 116.80688141, 0.01860171, 11.68068814, 0.06063357, -97.19343161, -0.00090819, -116.80688141, -0.01860171, -11.68068814, -0.06063357, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12006, 85.51587619, 0.00090819, 102.7728175, 0.01860171, 10.27728175, 0.06063357, -85.51587619, -0.00090819, -102.7728175, -0.01860171, -10.27728175, -0.06063357, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22006, 2006, 0.0, 151.24165435, 0.01816383, 151.24165435, 0.05449148, 105.86915804, -1969.56056463, 0.05, 2, 0, 72006, 23006, 2, 3)
    ops.uniaxialMaterial('LimitState', 42006, 37.81041359, 7.675e-05, 113.43124076, 0.00023024, 378.10413587, 0.00076746, -37.81041359, -7.675e-05, -113.43124076, -0.00023024, -378.10413587, -0.00076746, 0.4, 0.3, 0.003, 0.0, 0.0, 22006, 2)
    ops.limitCurve('ThreePoint', 12006, 2006, 0.0, 151.24165435, 0.01816383, 151.24165435, 0.05449148, 105.86915804, -1969.56056463, 0.05, 2, 0, 72006, 23006, 1, 3)
    ops.uniaxialMaterial('LimitState', 32006, 37.81041359, 7.675e-05, 113.43124076, 0.00023024, 378.10413587, 0.00076746, -37.81041359, -7.675e-05, -113.43124076, -0.00023024, -378.10413587, -0.00076746, 0.4, 0.3, 0.003, 0.0, 0.0, 12006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2006, 99999, 'P', 42006, 'Vy', 32006, 'Vz', 22006, 'My', 12006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172006, 72006, 172006, 2006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123006, 123006, 23006, 2006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172007, 7.65, 5.2, 6.05)
    ops.node(123007, 7.65, 5.2, 8.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2007, 172007, 123007, 0.1225, 31093670.5558692, 12955696.0649455, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22007, 102.95202633, 0.00093872, 123.80758012, 0.01579668, 12.38075801, 0.05556746, -102.95202633, -0.00093872, -123.80758012, -0.01579668, -12.38075801, -0.05556746, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12007, 91.17345226, 0.00093872, 109.64295603, 0.01579668, 10.9642956, 0.05556746, -91.17345226, -0.00093872, -109.64295603, -0.01579668, -10.9642956, -0.05556746, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22007, 2007, 0.0, 144.67644601, 0.01877443, 144.67644601, 0.05632328, 101.2735122, -1728.82954006, 0.05, 2, 0, 72007, 23007, 2, 3)
    ops.uniaxialMaterial('LimitState', 42007, 36.1691115, 7.521e-05, 108.5073345, 0.00022562, 361.69111501, 0.00075206, -36.1691115, -7.521e-05, -108.5073345, -0.00022562, -361.69111501, -0.00075206, 0.4, 0.3, 0.003, 0.0, 0.0, 22007, 2)
    ops.limitCurve('ThreePoint', 12007, 2007, 0.0, 144.67644601, 0.01877443, 144.67644601, 0.05632328, 101.2735122, -1728.82954006, 0.05, 2, 0, 72007, 23007, 1, 3)
    ops.uniaxialMaterial('LimitState', 32007, 36.1691115, 7.521e-05, 108.5073345, 0.00022562, 361.69111501, 0.00075206, -36.1691115, -7.521e-05, -108.5073345, -0.00022562, -361.69111501, -0.00075206, 0.4, 0.3, 0.003, 0.0, 0.0, 12007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2007, 99999, 'P', 42007, 'Vy', 32007, 'Vz', 22007, 'My', 12007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172007, 72007, 172007, 2007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123007, 123007, 23007, 2007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172008, 12.3, 5.2, 6.025)
    ops.node(123008, 12.3, 5.2, 8.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2008, 172008, 123008, 0.1225, 31197529.69108484, 12998970.70461868, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22008, 92.03860884, 0.00091648, 110.99427637, 0.01680416, 11.09942764, 0.06047599, -92.03860884, -0.00091648, -110.99427637, -0.01680416, -11.09942764, -0.06047599, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12008, 79.7340009, 0.00091648, 96.15549218, 0.01680416, 9.61554922, 0.06047599, -79.7340009, -0.00091648, -96.15549218, -0.01680416, -9.61554922, -0.06047599, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22008, 2008, 0.0, 140.18798105, 0.01832951, 140.18798105, 0.05498853, 98.13158673, -1891.70332032, 0.05, 2, 0, 72008, 23008, 2, 3)
    ops.uniaxialMaterial('LimitState', 42008, 35.04699526, 7.263e-05, 105.14098579, 0.00021789, 350.46995262, 0.00072631, -35.04699526, -7.263e-05, -105.14098579, -0.00021789, -350.46995262, -0.00072631, 0.4, 0.3, 0.003, 0.0, 0.0, 22008, 2)
    ops.limitCurve('ThreePoint', 12008, 2008, 0.0, 140.18798105, 0.01832951, 140.18798105, 0.05498853, 98.13158673, -1891.70332032, 0.05, 2, 0, 72008, 23008, 1, 3)
    ops.uniaxialMaterial('LimitState', 32008, 35.04699526, 7.263e-05, 105.14098579, 0.00021789, 350.46995262, 0.00072631, -35.04699526, -7.263e-05, -105.14098579, -0.00021789, -350.46995262, -0.00072631, 0.4, 0.3, 0.003, 0.0, 0.0, 12008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2008, 99999, 'P', 42008, 'Vy', 32008, 'Vz', 22008, 'My', 12008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172008, 72008, 172008, 2008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123008, 123008, 23008, 2008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172009, 0.0, 10.4, 6.025)
    ops.node(123009, 0.0, 10.4, 8.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2009, 172009, 123009, 0.0625, 30639979.47479929, 12766658.1144997, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22009, 33.56470421, 0.00124719, 40.46692581, 0.01817392, 4.04669258, 0.07141774, -33.56470421, -0.00124719, -40.46692581, -0.01817392, -4.04669258, -0.07141774, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12009, 33.56470421, 0.00124719, 40.46692581, 0.01817392, 4.04669258, 0.07141774, -33.56470421, -0.00124719, -40.46692581, -0.01817392, -4.04669258, -0.07141774, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22009, 2009, 0.0, 82.71166209, 0.02494383, 82.71166209, 0.0748315, 57.89816347, -1340.24684188, 0.05, 2, 0, 72009, 23009, 2, 3)
    ops.uniaxialMaterial('LimitState', 42009, 20.67791552, 8.552e-05, 62.03374657, 0.00025656, 206.77915523, 0.00085519, -20.67791552, -8.552e-05, -62.03374657, -0.00025656, -206.77915523, -0.00085519, 0.4, 0.3, 0.003, 0.0, 0.0, 22009, 2)
    ops.limitCurve('ThreePoint', 12009, 2009, 0.0, 82.71166209, 0.02494383, 82.71166209, 0.0748315, 57.89816347, -1340.24684188, 0.05, 2, 0, 72009, 23009, 1, 3)
    ops.uniaxialMaterial('LimitState', 32009, 20.67791552, 8.552e-05, 62.03374657, 0.00025656, 206.77915523, 0.00085519, -20.67791552, -8.552e-05, -62.03374657, -0.00025656, -206.77915523, -0.00085519, 0.4, 0.3, 0.003, 0.0, 0.0, 12009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2009, 99999, 'P', 42009, 'Vy', 32009, 'Vz', 22009, 'My', 12009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172009, 72009, 172009, 2009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123009, 123009, 23009, 2009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172010, 3.0, 10.4, 6.05)
    ops.node(123010, 3.0, 10.4, 8.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2010, 172010, 123010, 0.1225, 32743280.02781167, 13643033.34492153, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22010, 98.4559394, 0.00090688, 118.07043457, 0.01503436, 11.80704346, 0.0583003, -98.4559394, -0.00090688, -118.07043457, -0.01503436, -11.80704346, -0.0583003, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12010, 85.97233135, 0.00090688, 103.09982907, 0.01503436, 10.30998291, 0.0583003, -85.97233135, -0.00090688, -103.09982907, -0.01503436, -10.30998291, -0.0583003, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22010, 2010, 0.0, 144.87803362, 0.01813763, 144.87803362, 0.0544129, 101.41462354, -1660.43660576, 0.05, 2, 0, 72010, 23010, 2, 3)
    ops.uniaxialMaterial('LimitState', 42010, 36.21950841, 7.152e-05, 108.65852522, 0.00021455, 362.19508406, 0.00071517, -36.21950841, -7.152e-05, -108.65852522, -0.00021455, -362.19508406, -0.00071517, 0.4, 0.3, 0.003, 0.0, 0.0, 22010, 2)
    ops.limitCurve('ThreePoint', 12010, 2010, 0.0, 144.87803362, 0.01813763, 144.87803362, 0.0544129, 101.41462354, -1660.43660576, 0.05, 2, 0, 72010, 23010, 1, 3)
    ops.uniaxialMaterial('LimitState', 32010, 36.21950841, 7.152e-05, 108.65852522, 0.00021455, 362.19508406, 0.00071517, -36.21950841, -7.152e-05, -108.65852522, -0.00021455, -362.19508406, -0.00071517, 0.4, 0.3, 0.003, 0.0, 0.0, 12010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2010, 99999, 'P', 42010, 'Vy', 32010, 'Vz', 22010, 'My', 12010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172010, 72010, 172010, 2010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123010, 123010, 23010, 2010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172011, 7.65, 10.4, 6.05)
    ops.node(123011, 7.65, 10.4, 8.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2011, 172011, 123011, 0.1225, 31552901.56802548, 13147042.32001062, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22011, 106.77187278, 0.00094022, 128.263023, 0.01438732, 12.8263023, 0.05465866, -106.77187278, -0.00094022, -128.263023, -0.01438732, -12.8263023, -0.05465866, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12011, 93.80676011, 0.00094022, 112.68827938, 0.01438732, 11.26882794, 0.05465866, -93.80676011, -0.00094022, -112.68827938, -0.01438732, -11.26882794, -0.05465866, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22011, 2011, 0.0, 142.86315984, 0.01880442, 142.86315984, 0.05641325, 100.00421189, -1615.02859523, 0.05, 2, 0, 72011, 23011, 2, 3)
    ops.uniaxialMaterial('LimitState', 42011, 35.71578996, 7.318e-05, 107.14736988, 0.00021955, 357.1578996, 0.00073183, -35.71578996, -7.318e-05, -107.14736988, -0.00021955, -357.1578996, -0.00073183, 0.4, 0.3, 0.003, 0.0, 0.0, 22011, 2)
    ops.limitCurve('ThreePoint', 12011, 2011, 0.0, 142.86315984, 0.01880442, 142.86315984, 0.05641325, 100.00421189, -1615.02859523, 0.05, 2, 0, 72011, 23011, 1, 3)
    ops.uniaxialMaterial('LimitState', 32011, 35.71578996, 7.318e-05, 107.14736988, 0.00021955, 357.1578996, 0.00073183, -35.71578996, -7.318e-05, -107.14736988, -0.00021955, -357.1578996, -0.00073183, 0.4, 0.3, 0.003, 0.0, 0.0, 12011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2011, 99999, 'P', 42011, 'Vy', 32011, 'Vz', 22011, 'My', 12011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172011, 72011, 172011, 2011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123011, 123011, 23011, 2011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172012, 12.3, 10.4, 6.025)
    ops.node(123012, 12.3, 10.4, 8.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2012, 172012, 123012, 0.1225, 29383932.72866164, 12243305.30360902, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22012, 89.45867181, 0.00098492, 108.33897807, 0.0169417, 10.83389781, 0.05901589, -89.45867181, -0.00098492, -108.33897807, -0.0169417, -10.83389781, -0.05901589, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12012, 78.52730105, 0.00098492, 95.10053497, 0.0169417, 9.5100535, 0.05901589, -78.52730105, -0.00098492, -95.10053497, -0.0169417, -9.5100535, -0.05901589, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22012, 2012, 0.0, 131.79729328, 0.01969845, 131.79729328, 0.05909536, 92.2581053, -1824.24090988, 0.05, 2, 0, 72012, 23012, 2, 3)
    ops.uniaxialMaterial('LimitState', 42012, 32.94932332, 7.25e-05, 98.84796996, 0.00021749, 329.4932332, 0.00072498, -32.94932332, -7.25e-05, -98.84796996, -0.00021749, -329.4932332, -0.00072498, 0.4, 0.3, 0.003, 0.0, 0.0, 22012, 2)
    ops.limitCurve('ThreePoint', 12012, 2012, 0.0, 131.79729328, 0.01969845, 131.79729328, 0.05909536, 92.2581053, -1824.24090988, 0.05, 2, 0, 72012, 23012, 1, 3)
    ops.uniaxialMaterial('LimitState', 32012, 32.94932332, 7.25e-05, 98.84796996, 0.00021749, 329.4932332, 0.00072498, -32.94932332, -7.25e-05, -98.84796996, -0.00021749, -329.4932332, -0.00072498, 0.4, 0.3, 0.003, 0.0, 0.0, 12012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2012, 99999, 'P', 42012, 'Vy', 32012, 'Vz', 22012, 'My', 12012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172012, 72012, 172012, 2012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123012, 123012, 23012, 2012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172013, 0.0, 15.6, 6.025)
    ops.node(123013, 0.0, 15.6, 8.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2013, 172013, 123013, 0.0625, 32173567.68366997, 13405653.20152915, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22013, 28.9678788, 0.00117005, 34.89042142, 0.02135125, 3.48904214, 0.08141839, -28.9678788, -0.00117005, -34.89042142, -0.02135125, -3.48904214, -0.08141839, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12013, 28.9678788, 0.00117005, 34.89042142, 0.02135125, 3.48904214, 0.08141839, -28.9678788, -0.00117005, -34.89042142, -0.02135125, -3.48904214, -0.08141839, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22013, 2013, 0.0, 88.06807365, 0.02340098, 88.06807365, 0.07020294, 61.64765156, -2116.64848639, 0.05, 2, 0, 72013, 23013, 2, 3)
    ops.uniaxialMaterial('LimitState', 42013, 22.01701841, 8.672e-05, 66.05105524, 0.00026015, 220.17018414, 0.00086717, -22.01701841, -8.672e-05, -66.05105524, -0.00026015, -220.17018414, -0.00086717, 0.4, 0.3, 0.003, 0.0, 0.0, 22013, 2)
    ops.limitCurve('ThreePoint', 12013, 2013, 0.0, 88.06807365, 0.02340098, 88.06807365, 0.07020294, 61.64765156, -2116.64848639, 0.05, 2, 0, 72013, 23013, 1, 3)
    ops.uniaxialMaterial('LimitState', 32013, 22.01701841, 8.672e-05, 66.05105524, 0.00026015, 220.17018414, 0.00086717, -22.01701841, -8.672e-05, -66.05105524, -0.00026015, -220.17018414, -0.00086717, 0.4, 0.3, 0.003, 0.0, 0.0, 12013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2013, 99999, 'P', 42013, 'Vy', 32013, 'Vz', 22013, 'My', 12013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172013, 72013, 172013, 2013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123013, 123013, 23013, 2013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172014, 3.0, 15.6, 6.05)
    ops.node(123014, 3.0, 15.6, 8.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2014, 172014, 123014, 0.0625, 34740952.45671548, 14475396.85696478, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22014, 41.416229, 0.00119349, 49.27575004, 0.0163748, 4.927575, 0.07212718, -41.416229, -0.00119349, -49.27575004, -0.0163748, -4.927575, -0.07212718, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12014, 44.80160685, 0.00119349, 53.30356804, 0.0163748, 5.3303568, 0.07212718, -44.80160685, -0.00119349, -53.30356804, -0.0163748, -5.3303568, -0.07212718, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22014, 2014, 0.0, 82.275237, 0.0238699, 82.275237, 0.07160969, 57.5926659, -1121.78383251, 0.05, 2, 0, 72014, 23014, 2, 3)
    ops.uniaxialMaterial('LimitState', 42014, 20.56880925, 7.503e-05, 61.70642775, 0.00022508, 205.6880925, 0.00075026, -20.56880925, -7.503e-05, -61.70642775, -0.00022508, -205.6880925, -0.00075026, 0.4, 0.3, 0.003, 0.0, 0.0, 22014, 2)
    ops.limitCurve('ThreePoint', 12014, 2014, 0.0, 82.275237, 0.0238699, 82.275237, 0.07160969, 57.5926659, -1121.78383251, 0.05, 2, 0, 72014, 23014, 1, 3)
    ops.uniaxialMaterial('LimitState', 32014, 20.56880925, 7.503e-05, 61.70642775, 0.00022508, 205.6880925, 0.00075026, -20.56880925, -7.503e-05, -61.70642775, -0.00022508, -205.6880925, -0.00075026, 0.4, 0.3, 0.003, 0.0, 0.0, 12014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2014, 99999, 'P', 42014, 'Vy', 32014, 'Vz', 22014, 'My', 12014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172014, 72014, 172014, 2014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123014, 123014, 23014, 2014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172015, 7.65, 15.6, 6.05)
    ops.node(123015, 7.65, 15.6, 8.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2015, 172015, 123015, 0.1225, 31173006.9773976, 12988752.907249, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22015, 94.940469, 0.00096566, 114.50559204, 0.02939103, 11.4505592, 0.08114363, -94.940469, -0.00096566, -114.50559204, -0.02939103, -11.4505592, -0.08114363, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12015, 89.56293768, 0.00096566, 108.01987089, 0.02939103, 10.80198709, 0.08114363, -89.56293768, -0.00096566, -108.01987089, -0.02939103, -10.80198709, -0.08114363, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22015, 2015, 0.0, 158.94031003, 0.01931312, 158.94031003, 0.05793935, 111.25821702, -2771.07895313, 0.05, 2, 0, 72015, 23015, 2, 3)
    ops.uniaxialMaterial('LimitState', 42015, 39.73507751, 8.241e-05, 119.20523252, 0.00024723, 397.35077508, 0.00082411, -39.73507751, -8.241e-05, -119.20523252, -0.00024723, -397.35077508, -0.00082411, 0.4, 0.3, 0.003, 0.0, 0.0, 22015, 2)
    ops.limitCurve('ThreePoint', 12015, 2015, 0.0, 158.94031003, 0.01931312, 158.94031003, 0.05793935, 111.25821702, -2771.07895313, 0.05, 2, 0, 72015, 23015, 1, 3)
    ops.uniaxialMaterial('LimitState', 32015, 39.73507751, 8.241e-05, 119.20523252, 0.00024723, 397.35077508, 0.00082411, -39.73507751, -8.241e-05, -119.20523252, -0.00024723, -397.35077508, -0.00082411, 0.4, 0.3, 0.003, 0.0, 0.0, 12015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2015, 99999, 'P', 42015, 'Vy', 32015, 'Vz', 22015, 'My', 12015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172015, 72015, 172015, 2015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123015, 123015, 23015, 2015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172016, 12.3, 15.6, 6.025)
    ops.node(123016, 12.3, 15.6, 8.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2016, 172016, 123016, 0.0625, 33548430.65450311, 13978512.77270963, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22016, 30.1113244, 0.00123049, 36.04547382, 0.0172203, 3.60454738, 0.07529234, -30.1113244, -0.00123049, -36.04547382, -0.0172203, -3.60454738, -0.07529234, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12016, 30.1113244, 0.00123049, 36.04547382, 0.0172203, 3.60454738, 0.07529234, -30.1113244, -0.00123049, -36.04547382, -0.0172203, -3.60454738, -0.07529234, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22016, 2016, 0.0, 81.39085387, 0.02460975, 81.39085387, 0.07382924, 56.97359771, -1301.92020872, 0.05, 2, 0, 72016, 23016, 2, 3)
    ops.uniaxialMaterial('LimitState', 42016, 20.34771347, 7.686e-05, 61.0431404, 0.00023057, 203.47713468, 0.00076858, -20.34771347, -7.686e-05, -61.0431404, -0.00023057, -203.47713468, -0.00076858, 0.4, 0.3, 0.003, 0.0, 0.0, 22016, 2)
    ops.limitCurve('ThreePoint', 12016, 2016, 0.0, 81.39085387, 0.02460975, 81.39085387, 0.07382924, 56.97359771, -1301.92020872, 0.05, 2, 0, 72016, 23016, 1, 3)
    ops.uniaxialMaterial('LimitState', 32016, 20.34771347, 7.686e-05, 61.0431404, 0.00023057, 203.47713468, 0.00076858, -20.34771347, -7.686e-05, -61.0431404, -0.00023057, -203.47713468, -0.00076858, 0.4, 0.3, 0.003, 0.0, 0.0, 12016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2016, 99999, 'P', 42016, 'Vy', 32016, 'Vz', 22016, 'My', 12016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172016, 72016, 172016, 2016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123016, 123016, 23016, 2016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173003, 7.65, 0.0, 8.8)
    ops.node(124003, 7.65, 0.0, 11.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3003, 173003, 124003, 0.1225, 30419003.01311731, 12674584.58879888, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23003, 61.40287991, 0.00089525, 74.51076658, 0.03444142, 7.45107666, 0.10738004, -61.40287991, -0.00089525, -74.51076658, -0.03444142, -7.45107666, -0.10738004, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13003, 72.74384412, 0.00089525, 88.27272593, 0.03444142, 8.82727259, 0.10738004, -72.74384412, -0.00089525, -88.27272593, -0.03444142, -8.82727259, -0.10738004, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23003, 3003, 0.0, 167.24157742, 0.01790503, 167.24157742, 0.05371509, 117.06910419, -8516.97505807, 0.05, 2, 0, 73003, 24003, 2, 3)
    ops.uniaxialMaterial('LimitState', 43003, 41.81039436, 8.886e-05, 125.43118307, 0.00026659, 418.10394355, 0.00088865, -41.81039436, -8.886e-05, -125.43118307, -0.00026659, -418.10394355, -0.00088865, 0.4, 0.3, 0.003, 0.0, 0.0, 23003, 2)
    ops.limitCurve('ThreePoint', 13003, 3003, 0.0, 167.24157742, 0.01790503, 167.24157742, 0.05371509, 117.06910419, -8516.97505807, 0.05, 2, 0, 73003, 24003, 1, 3)
    ops.uniaxialMaterial('LimitState', 33003, 41.81039436, 8.886e-05, 125.43118307, 0.00026659, 418.10394355, 0.00088865, -41.81039436, -8.886e-05, -125.43118307, -0.00026659, -418.10394355, -0.00088865, 0.4, 0.3, 0.003, 0.0, 0.0, 13003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3003, 99999, 'P', 43003, 'Vy', 33003, 'Vz', 23003, 'My', 13003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173003, 73003, 173003, 3003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124003, 124003, 24003, 3003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173004, 12.3, 0.0, 8.775)
    ops.node(124004, 12.3, 0.0, 11.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3004, 173004, 124004, 0.0625, 31490873.63180486, 13121197.34658536, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23004, 24.91949059, 0.00114723, 30.14287066, 0.01781584, 3.01428707, 0.08150325, -24.91949059, -0.00114723, -30.14287066, -0.01781584, -3.01428707, -0.08150325, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13004, 24.91949059, 0.00114723, 30.14287066, 0.01781584, 3.01428707, 0.08150325, -24.91949059, -0.00114723, -30.14287066, -0.01781584, -3.01428707, -0.08150325, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23004, 3004, 0.0, 66.47721405, 0.02294465, 66.47721405, 0.06883395, 46.53404984, -2291.09662478, 0.05, 2, 0, 73004, 24004, 2, 3)
    ops.uniaxialMaterial('LimitState', 43004, 16.61930351, 6.688e-05, 49.85791054, 0.00020063, 166.19303513, 0.00066876, -16.61930351, -6.688e-05, -49.85791054, -0.00020063, -166.19303513, -0.00066876, 0.4, 0.3, 0.003, 0.0, 0.0, 23004, 2)
    ops.limitCurve('ThreePoint', 13004, 3004, 0.0, 66.47721405, 0.02294465, 66.47721405, 0.06883395, 46.53404984, -2291.09662478, 0.05, 2, 0, 73004, 24004, 1, 3)
    ops.uniaxialMaterial('LimitState', 33004, 16.61930351, 6.688e-05, 49.85791054, 0.00020063, 166.19303513, 0.00066876, -16.61930351, -6.688e-05, -49.85791054, -0.00020063, -166.19303513, -0.00066876, 0.4, 0.3, 0.003, 0.0, 0.0, 13004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3004, 99999, 'P', 43004, 'Vy', 33004, 'Vz', 23004, 'My', 13004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173004, 73004, 173004, 3004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124004, 124004, 24004, 3004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173005, 0.0, 5.2, 8.775)
    ops.node(124005, 0.0, 5.2, 11.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3005, 173005, 124005, 0.0625, 30833253.78289012, 12847189.07620422, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23005, 24.79494473, 0.001215, 30.02079491, 0.01944612, 3.00207949, 0.08095945, -24.79494473, -0.001215, -30.02079491, -0.01944612, -3.00207949, -0.08095945, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13005, 24.79494473, 0.001215, 30.02079491, 0.01944612, 3.00207949, 0.08095945, -24.79494473, -0.001215, -30.02079491, -0.01944612, -3.00207949, -0.08095945, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23005, 3005, 0.0, 76.37128995, 0.02430006, 76.37128995, 0.07290018, 53.45990297, -2006.08506611, 0.05, 2, 0, 73005, 24005, 2, 3)
    ops.uniaxialMaterial('LimitState', 43005, 19.09282249, 7.847e-05, 57.27846746, 0.00023541, 190.92822488, 0.00078469, -19.09282249, -7.847e-05, -57.27846746, -0.00023541, -190.92822488, -0.00078469, 0.4, 0.3, 0.003, 0.0, 0.0, 23005, 2)
    ops.limitCurve('ThreePoint', 13005, 3005, 0.0, 76.37128995, 0.02430006, 76.37128995, 0.07290018, 53.45990297, -2006.08506611, 0.05, 2, 0, 73005, 24005, 1, 3)
    ops.uniaxialMaterial('LimitState', 33005, 19.09282249, 7.847e-05, 57.27846746, 0.00023541, 190.92822488, 0.00078469, -19.09282249, -7.847e-05, -57.27846746, -0.00023541, -190.92822488, -0.00078469, 0.4, 0.3, 0.003, 0.0, 0.0, 13005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3005, 99999, 'P', 43005, 'Vy', 33005, 'Vz', 23005, 'My', 13005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173005, 73005, 173005, 3005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124005, 124005, 24005, 3005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173006, 3.0, 5.2, 8.8)
    ops.node(124006, 3.0, 5.2, 11.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3006, 173006, 124006, 0.1225, 30876581.74064044, 12865242.39193352, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23006, 75.53296169, 0.00088053, 91.45127137, 0.01871154, 9.14512714, 0.06638756, -75.53296169, -0.00088053, -91.45127137, -0.01871154, -9.14512714, -0.06638756, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13006, 64.31809338, 0.00088053, 77.87290846, 0.01871154, 7.78729085, 0.06638756, -64.31809338, -0.00088053, -77.87290846, -0.01871154, -7.78729085, -0.06638756, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23006, 3006, 0.0, 131.38161206, 0.01761065, 131.38161206, 0.05283195, 91.96712844, -2569.59011587, 0.05, 2, 0, 73006, 24006, 2, 3)
    ops.uniaxialMaterial('LimitState', 43006, 32.84540302, 6.878e-05, 98.53620905, 0.00020633, 328.45403015, 0.00068776, -32.84540302, -6.878e-05, -98.53620905, -0.00020633, -328.45403015, -0.00068776, 0.4, 0.3, 0.003, 0.0, 0.0, 23006, 2)
    ops.limitCurve('ThreePoint', 13006, 3006, 0.0, 131.38161206, 0.01761065, 131.38161206, 0.05283195, 91.96712844, -2569.59011587, 0.05, 2, 0, 73006, 24006, 1, 3)
    ops.uniaxialMaterial('LimitState', 33006, 32.84540302, 6.878e-05, 98.53620905, 0.00020633, 328.45403015, 0.00068776, -32.84540302, -6.878e-05, -98.53620905, -0.00020633, -328.45403015, -0.00068776, 0.4, 0.3, 0.003, 0.0, 0.0, 13006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3006, 99999, 'P', 43006, 'Vy', 33006, 'Vz', 23006, 'My', 13006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173006, 73006, 173006, 3006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124006, 124006, 24006, 3006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173007, 7.65, 5.2, 8.8)
    ops.node(124007, 7.65, 5.2, 11.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3007, 173007, 124007, 0.1225, 32628585.07440268, 13595243.78100112, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23007, 78.11716534, 0.00087932, 94.04600898, 0.01542875, 9.4046009, 0.06343724, -78.11716534, -0.00087932, -94.04600898, -0.01542875, -9.4046009, -0.06343724, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13007, 66.69829443, 0.00087932, 80.29872013, 0.01542875, 8.02987201, 0.06343724, -66.69829443, -0.00087932, -80.29872013, -0.01542875, -8.02987201, -0.06343724, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23007, 3007, 0.0, 132.43604041, 0.01758634, 132.43604041, 0.05275903, 92.70522829, -2046.36066724, 0.05, 2, 0, 73007, 24007, 2, 3)
    ops.uniaxialMaterial('LimitState', 43007, 33.1090101, 6.561e-05, 99.32703031, 0.00019682, 331.09010103, 0.00065605, -33.1090101, -6.561e-05, -99.32703031, -0.00019682, -331.09010103, -0.00065605, 0.4, 0.3, 0.003, 0.0, 0.0, 23007, 2)
    ops.limitCurve('ThreePoint', 13007, 3007, 0.0, 132.43604041, 0.01758634, 132.43604041, 0.05275903, 92.70522829, -2046.36066724, 0.05, 2, 0, 73007, 24007, 1, 3)
    ops.uniaxialMaterial('LimitState', 33007, 33.1090101, 6.561e-05, 99.32703031, 0.00019682, 331.09010103, 0.00065605, -33.1090101, -6.561e-05, -99.32703031, -0.00019682, -331.09010103, -0.00065605, 0.4, 0.3, 0.003, 0.0, 0.0, 13007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3007, 99999, 'P', 43007, 'Vy', 33007, 'Vz', 23007, 'My', 13007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173007, 73007, 173007, 3007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124007, 124007, 24007, 3007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173008, 12.3, 5.2, 8.775)
    ops.node(124008, 12.3, 5.2, 11.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3008, 173008, 124008, 0.1225, 31340563.46419737, 13058568.11008224, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23008, 73.18952222, 0.00087574, 88.57239414, 0.01931103, 8.85723941, 0.06845716, -73.18952222, -0.00087574, -88.57239414, -0.01931103, -8.85723941, -0.06845716, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13008, 61.5980061, 0.00087574, 74.54458929, 0.01931103, 7.45445893, 0.06845716, -61.5980061, -0.00087574, -74.54458929, -0.01931103, -7.45445893, -0.06845716, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23008, 3008, 0.0, 133.39138994, 0.0175147, 133.39138994, 0.0525441, 93.37397296, -3612.55277699, 0.05, 2, 0, 73008, 24008, 2, 3)
    ops.uniaxialMaterial('LimitState', 43008, 33.34784748, 6.879e-05, 100.04354245, 0.00020638, 333.47847485, 0.00068794, -33.34784748, -6.879e-05, -100.04354245, -0.00020638, -333.47847485, -0.00068794, 0.4, 0.3, 0.003, 0.0, 0.0, 23008, 2)
    ops.limitCurve('ThreePoint', 13008, 3008, 0.0, 133.39138994, 0.0175147, 133.39138994, 0.0525441, 93.37397296, -3612.55277699, 0.05, 2, 0, 73008, 24008, 1, 3)
    ops.uniaxialMaterial('LimitState', 33008, 33.34784748, 6.879e-05, 100.04354245, 0.00020638, 333.47847485, 0.00068794, -33.34784748, -6.879e-05, -100.04354245, -0.00020638, -333.47847485, -0.00068794, 0.4, 0.3, 0.003, 0.0, 0.0, 13008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3008, 99999, 'P', 43008, 'Vy', 33008, 'Vz', 23008, 'My', 13008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173008, 73008, 173008, 3008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124008, 124008, 24008, 3008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173009, 0.0, 10.4, 8.775)
    ops.node(124009, 0.0, 10.4, 11.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3009, 173009, 124009, 0.0625, 34483736.1112569, 14368223.37969038, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23009, 24.05305607, 0.00109308, 28.78493413, 0.02047815, 2.87849341, 0.08475434, -24.05305607, -0.00109308, -28.78493413, -0.02047815, -2.87849341, -0.08475434, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13009, 24.05305607, 0.00109308, 28.78493413, 0.02047815, 2.87849341, 0.08475434, -24.05305607, -0.00109308, -28.78493413, -0.02047815, -2.87849341, -0.08475434, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23009, 3009, 0.0, 85.11407729, 0.02186157, 85.11407729, 0.0655847, 59.5798541, -2892.4647847, 0.05, 2, 0, 73009, 24009, 2, 3)
    ops.uniaxialMaterial('LimitState', 43009, 21.27851932, 7.819e-05, 63.83555797, 0.00023458, 212.78519322, 0.00078194, -21.27851932, -7.819e-05, -63.83555797, -0.00023458, -212.78519322, -0.00078194, 0.4, 0.3, 0.003, 0.0, 0.0, 23009, 2)
    ops.limitCurve('ThreePoint', 13009, 3009, 0.0, 85.11407729, 0.02186157, 85.11407729, 0.0655847, 59.5798541, -2892.4647847, 0.05, 2, 0, 73009, 24009, 1, 3)
    ops.uniaxialMaterial('LimitState', 33009, 21.27851932, 7.819e-05, 63.83555797, 0.00023458, 212.78519322, 0.00078194, -21.27851932, -7.819e-05, -63.83555797, -0.00023458, -212.78519322, -0.00078194, 0.4, 0.3, 0.003, 0.0, 0.0, 13009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3009, 99999, 'P', 43009, 'Vy', 33009, 'Vz', 23009, 'My', 13009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173009, 73009, 173009, 3009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124009, 124009, 24009, 3009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173010, 3.0, 10.4, 8.8)
    ops.node(124010, 3.0, 10.4, 11.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3010, 173010, 124010, 0.1225, 31381350.19339714, 13075562.58058214, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23010, 74.82501032, 0.00087775, 90.49262027, 0.01847899, 9.04926203, 0.06687128, -74.82501032, -0.00087775, -90.49262027, -0.01847899, -9.04926203, -0.06687128, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13010, 63.42893263, 0.00087775, 76.71031771, 0.01847899, 7.67103177, 0.06687128, -63.42893263, -0.00087775, -76.71031771, -0.01847899, -7.67103177, -0.06687128, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23010, 3010, 0.0, 131.70787438, 0.01755496, 131.70787438, 0.05266488, 92.19551207, -2754.88080387, 0.05, 2, 0, 73010, 24010, 2, 3)
    ops.uniaxialMaterial('LimitState', 43010, 32.9269686, 6.784e-05, 98.78090579, 0.00020351, 329.26968595, 0.00067837, -32.9269686, -6.784e-05, -98.78090579, -0.00020351, -329.26968595, -0.00067837, 0.4, 0.3, 0.003, 0.0, 0.0, 23010, 2)
    ops.limitCurve('ThreePoint', 13010, 3010, 0.0, 131.70787438, 0.01755496, 131.70787438, 0.05266488, 92.19551207, -2754.88080387, 0.05, 2, 0, 73010, 24010, 1, 3)
    ops.uniaxialMaterial('LimitState', 33010, 32.9269686, 6.784e-05, 98.78090579, 0.00020351, 329.26968595, 0.00067837, -32.9269686, -6.784e-05, -98.78090579, -0.00020351, -329.26968595, -0.00067837, 0.4, 0.3, 0.003, 0.0, 0.0, 13010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3010, 99999, 'P', 43010, 'Vy', 33010, 'Vz', 23010, 'My', 13010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173010, 73010, 173010, 3010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124010, 124010, 24010, 3010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173011, 7.65, 10.4, 8.8)
    ops.node(124011, 7.65, 10.4, 11.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3011, 173011, 124011, 0.1225, 28676680.34297918, 11948616.80957466, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23011, 77.40566128, 0.00092332, 94.21409587, 0.01850032, 9.42140959, 0.0646359, -77.40566128, -0.00092332, -94.21409587, -0.01850032, -9.42140959, -0.0646359, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13011, 65.96667553, 0.00092332, 80.29116462, 0.01850032, 8.02911646, 0.0646359, -65.96667553, -0.00092332, -80.29116462, -0.01850032, -8.02911646, -0.0646359, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23011, 3011, 0.0, 122.62598961, 0.0184664, 122.62598961, 0.05539919, 85.83819273, -2346.73102977, 0.05, 2, 0, 73011, 24011, 2, 3)
    ops.uniaxialMaterial('LimitState', 43011, 30.6564974, 6.912e-05, 91.96949221, 0.00020735, 306.56497402, 0.00069117, -30.6564974, -6.912e-05, -91.96949221, -0.00020735, -306.56497402, -0.00069117, 0.4, 0.3, 0.003, 0.0, 0.0, 23011, 2)
    ops.limitCurve('ThreePoint', 13011, 3011, 0.0, 122.62598961, 0.0184664, 122.62598961, 0.05539919, 85.83819273, -2346.73102977, 0.05, 2, 0, 73011, 24011, 1, 3)
    ops.uniaxialMaterial('LimitState', 33011, 30.6564974, 6.912e-05, 91.96949221, 0.00020735, 306.56497402, 0.00069117, -30.6564974, -6.912e-05, -91.96949221, -0.00020735, -306.56497402, -0.00069117, 0.4, 0.3, 0.003, 0.0, 0.0, 13011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3011, 99999, 'P', 43011, 'Vy', 33011, 'Vz', 23011, 'My', 13011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173011, 73011, 173011, 3011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124011, 124011, 24011, 3011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173012, 12.3, 10.4, 8.775)
    ops.node(124012, 12.3, 10.4, 11.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3012, 173012, 124012, 0.1225, 30540629.80366812, 12725262.41819505, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23012, 68.21910889, 0.00083959, 82.75407713, 0.0199669, 8.27540771, 0.06888983, -68.21910889, -0.00083959, -82.75407713, -0.0199669, -8.27540771, -0.06888983, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13012, 57.68641643, 0.00083959, 69.97725759, 0.0199669, 6.99772576, 0.06888983, -57.68641643, -0.00083959, -69.97725759, -0.0199669, -6.99772576, -0.06888983, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23012, 3012, 0.0, 131.22009506, 0.01679185, 131.22009506, 0.05037555, 91.85406654, -3694.98544243, 0.05, 2, 0, 73012, 24012, 2, 3)
    ops.uniaxialMaterial('LimitState', 43012, 32.80502376, 6.945e-05, 98.41507129, 0.00020834, 328.05023765, 0.00069447, -32.80502376, -6.945e-05, -98.41507129, -0.00020834, -328.05023765, -0.00069447, 0.4, 0.3, 0.003, 0.0, 0.0, 23012, 2)
    ops.limitCurve('ThreePoint', 13012, 3012, 0.0, 131.22009506, 0.01679185, 131.22009506, 0.05037555, 91.85406654, -3694.98544243, 0.05, 2, 0, 73012, 24012, 1, 3)
    ops.uniaxialMaterial('LimitState', 33012, 32.80502376, 6.945e-05, 98.41507129, 0.00020834, 328.05023765, 0.00069447, -32.80502376, -6.945e-05, -98.41507129, -0.00020834, -328.05023765, -0.00069447, 0.4, 0.3, 0.003, 0.0, 0.0, 13012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3012, 99999, 'P', 43012, 'Vy', 33012, 'Vz', 23012, 'My', 13012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173012, 73012, 173012, 3012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124012, 124012, 24012, 3012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173013, 0.0, 15.6, 8.775)
    ops.node(124013, 0.0, 15.6, 11.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3013, 173013, 124013, 0.0625, 33180308.59191259, 13825128.57996358, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23013, 21.99478796, 0.00109925, 26.47023489, 0.01777957, 2.64702349, 0.08309918, -21.99478796, -0.00109925, -26.47023489, -0.01777957, -2.64702349, -0.08309918, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13013, 21.99478796, 0.00109925, 26.47023489, 0.01777957, 2.64702349, 0.08309918, -21.99478796, -0.00109925, -26.47023489, -0.01777957, -2.64702349, -0.08309918, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23013, 3013, 0.0, 67.08492426, 0.02198509, 67.08492426, 0.06595527, 46.95944698, -3206.70242435, 0.05, 2, 0, 73013, 24013, 2, 3)
    ops.uniaxialMaterial('LimitState', 43013, 16.77123107, 6.405e-05, 50.3136932, 0.00019215, 167.71231066, 0.00064052, -16.77123107, -6.405e-05, -50.3136932, -0.00019215, -167.71231066, -0.00064052, 0.4, 0.3, 0.003, 0.0, 0.0, 23013, 2)
    ops.limitCurve('ThreePoint', 13013, 3013, 0.0, 67.08492426, 0.02198509, 67.08492426, 0.06595527, 46.95944698, -3206.70242435, 0.05, 2, 0, 73013, 24013, 1, 3)
    ops.uniaxialMaterial('LimitState', 33013, 16.77123107, 6.405e-05, 50.3136932, 0.00019215, 167.71231066, 0.00064052, -16.77123107, -6.405e-05, -50.3136932, -0.00019215, -167.71231066, -0.00064052, 0.4, 0.3, 0.003, 0.0, 0.0, 13013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3013, 99999, 'P', 43013, 'Vy', 33013, 'Vz', 23013, 'My', 13013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173013, 73013, 173013, 3013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124013, 124013, 24013, 3013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173014, 3.0, 15.6, 8.8)
    ops.node(124014, 3.0, 15.6, 11.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3014, 173014, 124014, 0.0625, 30732571.37929501, 12805238.07470626, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23014, 31.89817817, 0.00120592, 38.63714199, 0.02105882, 3.8637142, 0.08275502, -31.89817817, -0.00120592, -38.63714199, -0.02105882, -3.8637142, -0.08275502, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13014, 35.21828428, 0.00120592, 42.65866981, 0.02105882, 4.26586698, 0.08275502, -35.21828428, -0.00120592, -42.65866981, -0.02105882, -4.26586698, -0.08275502, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23014, 3014, 0.0, 75.82569897, 0.02411847, 75.82569897, 0.07235542, 53.07798928, -2049.65820955, 0.05, 2, 0, 73014, 24014, 2, 3)
    ops.uniaxialMaterial('LimitState', 43014, 18.95642474, 7.816e-05, 56.86927423, 0.00023449, 189.56424743, 0.00078163, -18.95642474, -7.816e-05, -56.86927423, -0.00023449, -189.56424743, -0.00078163, 0.4, 0.3, 0.003, 0.0, 0.0, 23014, 2)
    ops.limitCurve('ThreePoint', 13014, 3014, 0.0, 75.82569897, 0.02411847, 75.82569897, 0.07235542, 53.07798928, -2049.65820955, 0.05, 2, 0, 73014, 24014, 1, 3)
    ops.uniaxialMaterial('LimitState', 33014, 18.95642474, 7.816e-05, 56.86927423, 0.00023449, 189.56424743, 0.00078163, -18.95642474, -7.816e-05, -56.86927423, -0.00023449, -189.56424743, -0.00078163, 0.4, 0.3, 0.003, 0.0, 0.0, 13014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3014, 99999, 'P', 43014, 'Vy', 33014, 'Vz', 23014, 'My', 13014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173014, 73014, 173014, 3014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124014, 124014, 24014, 3014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173015, 7.65, 15.6, 8.8)
    ops.node(124015, 7.65, 15.6, 11.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3015, 173015, 124015, 0.1225, 27774971.16689382, 11572904.65287242, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23015, 75.68638498, 0.00096862, 92.45119049, 0.03717934, 9.24511905, 0.10868281, -75.68638498, -0.00096862, -92.45119049, -0.03717934, -9.24511905, -0.10868281, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13015, 70.60390022, 0.00096862, 86.24291714, 0.03717934, 8.62429171, 0.10868281, -70.60390022, -0.00096862, -86.24291714, -0.03717934, -8.62429171, -0.10868281, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23015, 3015, 0.0, 140.71134175, 0.01937237, 140.71134175, 0.0581171, 98.49793923, -5993.84555184, 0.05, 2, 0, 73015, 24015, 2, 3)
    ops.uniaxialMaterial('LimitState', 43015, 35.17783544, 8.189e-05, 105.53350631, 0.00024566, 351.77835438, 0.00081885, -35.17783544, -8.189e-05, -105.53350631, -0.00024566, -351.77835438, -0.00081885, 0.4, 0.3, 0.003, 0.0, 0.0, 23015, 2)
    ops.limitCurve('ThreePoint', 13015, 3015, 0.0, 140.71134175, 0.01937237, 140.71134175, 0.0581171, 98.49793923, -5993.84555184, 0.05, 2, 0, 73015, 24015, 1, 3)
    ops.uniaxialMaterial('LimitState', 33015, 35.17783544, 8.189e-05, 105.53350631, 0.00024566, 351.77835438, 0.00081885, -35.17783544, -8.189e-05, -105.53350631, -0.00024566, -351.77835438, -0.00081885, 0.4, 0.3, 0.003, 0.0, 0.0, 13015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3015, 99999, 'P', 43015, 'Vy', 33015, 'Vz', 23015, 'My', 13015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173015, 73015, 173015, 3015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124015, 124015, 24015, 3015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173016, 12.3, 15.6, 8.775)
    ops.node(124016, 12.3, 15.6, 11.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3016, 173016, 124016, 0.0625, 29920603.87423344, 12466918.2809306, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23016, 24.85230352, 0.00119281, 30.19946128, 0.02173532, 3.01994613, 0.08483495, -24.85230352, -0.00119281, -30.19946128, -0.02173532, -3.01994613, -0.08483495, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13016, 24.85230352, 0.00119281, 30.19946128, 0.02173532, 3.01994613, 0.08483495, -24.85230352, -0.00119281, -30.19946128, -0.02173532, -3.01994613, -0.08483495, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23016, 3016, 0.0, 75.43142877, 0.02385613, 75.43142877, 0.07156838, 52.80200014, -3035.11875134, 0.05, 2, 0, 73016, 24016, 2, 3)
    ops.uniaxialMaterial('LimitState', 43016, 18.85785719, 7.987e-05, 56.57357158, 0.0002396, 188.57857192, 0.00079867, -18.85785719, -7.987e-05, -56.57357158, -0.0002396, -188.57857192, -0.00079867, 0.4, 0.3, 0.003, 0.0, 0.0, 23016, 2)
    ops.limitCurve('ThreePoint', 13016, 3016, 0.0, 75.43142877, 0.02385613, 75.43142877, 0.07156838, 52.80200014, -3035.11875134, 0.05, 2, 0, 73016, 24016, 1, 3)
    ops.uniaxialMaterial('LimitState', 33016, 18.85785719, 7.987e-05, 56.57357158, 0.0002396, 188.57857192, 0.00079867, -18.85785719, -7.987e-05, -56.57357158, -0.0002396, -188.57857192, -0.00079867, 0.4, 0.3, 0.003, 0.0, 0.0, 13016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3016, 99999, 'P', 43016, 'Vy', 33016, 'Vz', 23016, 'My', 13016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173016, 73016, 173016, 3016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124016, 124016, 24016, 3016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170001, 0.0, 0.0, 0.0)
    ops.node(124017, 0.0, 0.0, 1.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4041, 170001, 124017, 0.0625, 28494389.09857085, 11872662.12440452, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24041, 46.59863464, 0.00101863, 56.25693033, 0.02445301, 5.62569303, 0.07988887, -46.59863464, -0.00101863, -56.25693033, -0.02445301, -5.62569303, -0.07988887, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14041, 42.80174598, 0.00101863, 51.67307713, 0.02445301, 5.16730771, 0.07988887, -42.80174598, -0.00101863, -51.67307713, -0.02445301, -5.16730771, -0.07988887, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24041, 4041, 0.0, 93.36230588, 0.02037268, 93.36230588, 0.06111804, 65.35361412, -3067.12716793, 0.05, 2, 0, 70001, 24017, 2, 3)
    ops.uniaxialMaterial('LimitState', 44041, 23.34057647, 5.756e-05, 70.02172941, 0.00017269, 233.4057647, 0.00057562, -23.34057647, -5.756e-05, -70.02172941, -0.00017269, -233.4057647, -0.00057562, 0.4, 0.3, 0.003, 0.0, 0.0, 24041, 2)
    ops.limitCurve('ThreePoint', 14041, 4041, 0.0, 93.36230588, 0.02037268, 93.36230588, 0.06111804, 65.35361412, -3067.12716793, 0.05, 2, 0, 70001, 24017, 1, 3)
    ops.uniaxialMaterial('LimitState', 34041, 23.34057647, 5.756e-05, 70.02172941, 0.00017269, 233.4057647, 0.00057562, -23.34057647, -5.756e-05, -70.02172941, -0.00017269, -233.4057647, -0.00057562, 0.4, 0.3, 0.003, 0.0, 0.0, 14041, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4041, 99999, 'P', 44041, 'Vy', 34041, 'Vz', 24041, 'My', 14041, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170001, 70001, 170001, 4041, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124017, 124017, 24017, 4041, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174017, 0.0, 0.0, 1.725)
    ops.node(121001, 0.0, 0.0, 2.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4042, 174017, 121001, 0.0625, 36225502.4401664, 15093959.35006933, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24042, 32.70486121, 0.00100042, 38.71898193, 0.02903334, 3.87189819, 0.11859117, -32.70486121, -0.00100042, -38.71898193, -0.02903334, -3.87189819, -0.11859117, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14042, 32.70486121, 0.00100042, 38.71898193, 0.02903334, 3.87189819, 0.11859117, -32.70486121, -0.00100042, -38.71898193, -0.02903334, -3.87189819, -0.11859117, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24042, 4042, 0.0, 118.2540658, 0.02000838, 118.2540658, 0.06002514, 82.77784606, -4242.96811607, 0.05, 2, 0, 74017, 21001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44042, 29.56351645, 5.735e-05, 88.69054935, 0.00017205, 295.6351645, 0.00057349, -29.56351645, -5.735e-05, -88.69054935, -0.00017205, -295.6351645, -0.00057349, 0.4, 0.3, 0.003, 0.0, 0.0, 24042, 2)
    ops.limitCurve('ThreePoint', 14042, 4042, 0.0, 118.2540658, 0.02000838, 118.2540658, 0.06002514, 82.77784606, -4242.96811607, 0.05, 2, 0, 74017, 21001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34042, 29.56351645, 5.735e-05, 88.69054935, 0.00017205, 295.6351645, 0.00057349, -29.56351645, -5.735e-05, -88.69054935, -0.00017205, -295.6351645, -0.00057349, 0.4, 0.3, 0.003, 0.0, 0.0, 14042, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4042, 99999, 'P', 44042, 'Vy', 34042, 'Vz', 24042, 'My', 14042, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174017, 74017, 174017, 4042, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121001, 121001, 21001, 4042, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170002, 3.0, 0.0, 0.0)
    ops.node(124018, 3.0, 0.0, 1.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4043, 170002, 124018, 0.1225, 34914939.33983225, 14547891.39159677, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24043, 122.89085598, 0.00074224, 145.93257557, 0.03678209, 14.59325756, 0.12456843, -122.89085598, -0.00074224, -145.93257557, -0.03678209, -14.59325756, -0.12456843, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14043, 116.61419585, 0.00074224, 138.4790578, 0.03678209, 13.84790578, 0.12456843, -116.61419585, -0.00074224, -138.4790578, -0.03678209, -13.84790578, -0.12456843, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24043, 4043, 0.0, 284.65889322, 0.01484487, 284.65889322, 0.04453462, 199.26122526, -7661.33381637, 0.05, 2, 0, 70002, 24018, 2, 3)
    ops.uniaxialMaterial('LimitState', 44043, 71.16472331, 7.308e-05, 213.49416992, 0.00021923, 711.64723305, 0.00073077, -71.16472331, -7.308e-05, -213.49416992, -0.00021923, -711.64723305, -0.00073077, 0.4, 0.3, 0.003, 0.0, 0.0, 24043, 2)
    ops.limitCurve('ThreePoint', 14043, 4043, 0.0, 284.65889322, 0.01484487, 284.65889322, 0.04453462, 199.26122526, -7661.33381637, 0.05, 2, 0, 70002, 24018, 1, 3)
    ops.uniaxialMaterial('LimitState', 34043, 71.16472331, 7.308e-05, 213.49416992, 0.00021923, 711.64723305, 0.00073077, -71.16472331, -7.308e-05, -213.49416992, -0.00021923, -711.64723305, -0.00073077, 0.4, 0.3, 0.003, 0.0, 0.0, 14043, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4043, 99999, 'P', 44043, 'Vy', 34043, 'Vz', 24043, 'My', 14043, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170002, 70002, 170002, 4043, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124018, 124018, 24018, 4043, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174018, 3.0, 0.0, 1.725)
    ops.node(121002, 3.0, 0.0, 2.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4044, 174018, 121002, 0.1225, 32789356.50358199, 13662231.87649249, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24044, 106.12683816, 0.00075065, 126.95020784, 0.02829768, 12.69502078, 0.08850674, -106.12683816, -0.00075065, -126.95020784, -0.02829768, -12.69502078, -0.08850674, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14044, 95.11918703, 0.00075065, 113.78272237, 0.02829768, 11.37827224, 0.08850674, -95.11918703, -0.00075065, -113.78272237, -0.02829768, -11.37827224, -0.08850674, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24044, 4044, 0.0, 239.76138128, 0.01501297, 239.76138128, 0.04503891, 167.83296689, -5523.5808126, 0.05, 2, 0, 74018, 21002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44044, 59.94034532, 6.554e-05, 179.82103596, 0.00019662, 599.40345319, 0.00065541, -59.94034532, -6.554e-05, -179.82103596, -0.00019662, -599.40345319, -0.00065541, 0.4, 0.3, 0.003, 0.0, 0.0, 24044, 2)
    ops.limitCurve('ThreePoint', 14044, 4044, 0.0, 239.76138128, 0.01501297, 239.76138128, 0.04503891, 167.83296689, -5523.5808126, 0.05, 2, 0, 74018, 21002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34044, 59.94034532, 6.554e-05, 179.82103596, 0.00019662, 599.40345319, 0.00065541, -59.94034532, -6.554e-05, -179.82103596, -0.00019662, -599.40345319, -0.00065541, 0.4, 0.3, 0.003, 0.0, 0.0, 14044, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4044, 99999, 'P', 44044, 'Vy', 34044, 'Vz', 24044, 'My', 14044, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174018, 74018, 174018, 4044, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121002, 121002, 21002, 4044, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171001, 0.0, 0.0, 3.275)
    ops.node(124019, 0.0, 0.0, 4.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4046, 171001, 124019, 0.0625, 31659380.94517132, 13191408.72715472, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24046, 32.05515176, 0.00088964, 38.56251374, 0.03359304, 3.85625137, 0.11803797, -32.05515176, -0.00088964, -38.56251374, -0.03359304, -3.85625137, -0.11803797, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14046, 32.05515176, 0.00088964, 38.56251374, 0.03359304, 3.85625137, 0.11803797, -32.05515176, -0.00088964, -38.56251374, -0.03359304, -3.85625137, -0.11803797, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24046, 4046, 0.0, 117.76888121, 0.01779286, 117.76888121, 0.05337857, 82.43821685, -5510.16785128, 0.05, 2, 0, 71001, 24019, 2, 3)
    ops.uniaxialMaterial('LimitState', 44046, 29.4422203, 5.892e-05, 88.32666091, 0.00017677, 294.42220303, 0.00058923, -29.4422203, -5.892e-05, -88.32666091, -0.00017677, -294.42220303, -0.00058923, 0.4, 0.3, 0.003, 0.0, 0.0, 24046, 2)
    ops.limitCurve('ThreePoint', 14046, 4046, 0.0, 117.76888121, 0.01779286, 117.76888121, 0.05337857, 82.43821685, -5510.16785128, 0.05, 2, 0, 71001, 24019, 1, 3)
    ops.uniaxialMaterial('LimitState', 34046, 29.4422203, 5.892e-05, 88.32666091, 0.00017677, 294.42220303, 0.00058923, -29.4422203, -5.892e-05, -88.32666091, -0.00017677, -294.42220303, -0.00058923, 0.4, 0.3, 0.003, 0.0, 0.0, 14046, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4046, 99999, 'P', 44046, 'Vy', 34046, 'Vz', 24046, 'My', 14046, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171001, 71001, 171001, 4046, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124019, 124019, 24019, 4046, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174019, 0.0, 0.0, 4.625)
    ops.node(122001, 0.0, 0.0, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4047, 174019, 122001, 0.0625, 32553738.24122203, 13564057.60050918, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24047, 30.08913751, 0.00088251, 36.1570966, 0.03111936, 3.61570966, 0.12068237, -30.08913751, -0.00088251, -36.1570966, -0.03111936, -3.61570966, -0.12068237, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14047, 30.08913751, 0.00088251, 36.1570966, 0.03111936, 3.61570966, 0.12068237, -30.08913751, -0.00088251, -36.1570966, -0.03111936, -3.61570966, -0.12068237, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24047, 4047, 0.0, 111.36552966, 0.01765016, 111.36552966, 0.05295049, 77.95587076, -5429.64644808, 0.05, 2, 0, 74019, 22001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44047, 27.84138241, 5.419e-05, 83.52414724, 0.00016256, 278.41382414, 0.00054188, -27.84138241, -5.419e-05, -83.52414724, -0.00016256, -278.41382414, -0.00054188, 0.4, 0.3, 0.003, 0.0, 0.0, 24047, 2)
    ops.limitCurve('ThreePoint', 14047, 4047, 0.0, 111.36552966, 0.01765016, 111.36552966, 0.05295049, 77.95587076, -5429.64644808, 0.05, 2, 0, 74019, 22001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34047, 27.84138241, 5.419e-05, 83.52414724, 0.00016256, 278.41382414, 0.00054188, -27.84138241, -5.419e-05, -83.52414724, -0.00016256, -278.41382414, -0.00054188, 0.4, 0.3, 0.003, 0.0, 0.0, 14047, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4047, 99999, 'P', 44047, 'Vy', 34047, 'Vz', 24047, 'My', 14047, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174019, 74019, 174019, 4047, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122001, 122001, 22001, 4047, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171002, 3.0, 0.0, 3.3)
    ops.node(124020, 3.0, 0.0, 4.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4048, 171002, 124020, 0.1225, 29433028.67200749, 12263761.94666979, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24048, 99.5808685, 0.0007371, 120.26591489, 0.04236207, 12.02659149, 0.12457265, -99.5808685, -0.0007371, -120.26591489, -0.04236207, -12.02659149, -0.12457265, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14048, 87.20067126, 0.0007371, 105.3140896, 0.04236207, 10.53140896, 0.12457265, -87.20067126, -0.0007371, -105.3140896, -0.04236207, -10.53140896, -0.12457265, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24048, 4048, 0.0, 276.61003769, 0.01474202, 276.61003769, 0.04422606, 193.62702638, -11804.31553502, 0.05, 2, 0, 71002, 24020, 2, 3)
    ops.uniaxialMaterial('LimitState', 44048, 69.15250942, 7.595e-05, 207.45752827, 0.00022785, 691.52509423, 0.00075951, -69.15250942, -7.595e-05, -207.45752827, -0.00022785, -691.52509423, -0.00075951, 0.4, 0.3, 0.003, 0.0, 0.0, 24048, 2)
    ops.limitCurve('ThreePoint', 14048, 4048, 0.0, 276.61003769, 0.01474202, 276.61003769, 0.04422606, 193.62702638, -11804.31553502, 0.05, 2, 0, 71002, 24020, 1, 3)
    ops.uniaxialMaterial('LimitState', 34048, 69.15250942, 7.595e-05, 207.45752827, 0.00022785, 691.52509423, 0.00075951, -69.15250942, -7.595e-05, -207.45752827, -0.00022785, -691.52509423, -0.00075951, 0.4, 0.3, 0.003, 0.0, 0.0, 14048, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4048, 99999, 'P', 44048, 'Vy', 34048, 'Vz', 24048, 'My', 14048, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171002, 71002, 171002, 4048, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124020, 124020, 24020, 4048, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174020, 3.0, 0.0, 4.625)
    ops.node(122002, 3.0, 0.0, 5.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4049, 174020, 122002, 0.1225, 30170868.96795686, 12571195.40331536, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24049, 100.27205428, 0.0007394, 121.04579441, 0.04245502, 12.10457944, 0.12890714, -100.27205428, -0.0007394, -121.04579441, -0.04245502, -12.10457944, -0.12890714, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14049, 86.80471001, 0.0007394, 104.78836958, 0.04245502, 10.47883696, 0.12890714, -86.80471001, -0.0007394, -104.78836958, -0.04245502, -10.47883696, -0.12890714, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24049, 4049, 0.0, 274.64045016, 0.01478808, 274.64045016, 0.04436424, 192.24831511, -12050.79049598, 0.05, 2, 0, 74020, 22002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44049, 68.66011254, 7.357e-05, 205.98033762, 0.0002207, 686.60112539, 0.00073566, -68.66011254, -7.357e-05, -205.98033762, -0.0002207, -686.60112539, -0.00073566, 0.4, 0.3, 0.003, 0.0, 0.0, 24049, 2)
    ops.limitCurve('ThreePoint', 14049, 4049, 0.0, 274.64045016, 0.01478808, 274.64045016, 0.04436424, 192.24831511, -12050.79049598, 0.05, 2, 0, 74020, 22002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34049, 68.66011254, 7.357e-05, 205.98033762, 0.0002207, 686.60112539, 0.00073566, -68.66011254, -7.357e-05, -205.98033762, -0.0002207, -686.60112539, -0.00073566, 0.4, 0.3, 0.003, 0.0, 0.0, 14049, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4049, 99999, 'P', 44049, 'Vy', 34049, 'Vz', 24049, 'My', 14049, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174020, 74020, 174020, 4049, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122002, 122002, 22002, 4049, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172001, 0.0, 0.0, 6.025)
    ops.node(124021, 0.0, 0.0, 7.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4051, 172001, 124021, 0.0625, 31286074.76146504, 13035864.48394377, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24051, 28.73960097, 0.00090239, 34.6853361, 0.0227955, 3.46853361, 0.09284267, -28.73960097, -0.00090239, -34.6853361, -0.0227955, -3.46853361, -0.09284267, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14051, 28.73960097, 0.00090239, 34.6853361, 0.0227955, 3.46853361, 0.09284267, -28.73960097, -0.00090239, -34.6853361, -0.0227955, -3.46853361, -0.09284267, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24051, 4051, 0.0, 92.92538847, 0.01804776, 92.92538847, 0.05414327, 65.04777193, -3766.02629726, 0.05, 2, 0, 72001, 24021, 2, 3)
    ops.uniaxialMaterial('LimitState', 44051, 23.23134712, 4.705e-05, 69.69404135, 0.00014114, 232.31347118, 0.00047048, -23.23134712, -4.705e-05, -69.69404135, -0.00014114, -232.31347118, -0.00047048, 0.4, 0.3, 0.003, 0.0, 0.0, 24051, 2)
    ops.limitCurve('ThreePoint', 14051, 4051, 0.0, 92.92538847, 0.01804776, 92.92538847, 0.05414327, 65.04777193, -3766.02629726, 0.05, 2, 0, 72001, 24021, 1, 3)
    ops.uniaxialMaterial('LimitState', 34051, 23.23134712, 4.705e-05, 69.69404135, 0.00014114, 232.31347118, 0.00047048, -23.23134712, -4.705e-05, -69.69404135, -0.00014114, -232.31347118, -0.00047048, 0.4, 0.3, 0.003, 0.0, 0.0, 14051, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4051, 99999, 'P', 44051, 'Vy', 34051, 'Vz', 24051, 'My', 14051, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172001, 72001, 172001, 4051, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124021, 124021, 24021, 4051, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174021, 0.0, 0.0, 7.35)
    ops.node(123001, 0.0, 0.0, 8.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4052, 174021, 123001, 0.0625, 30493132.69180626, 12705471.95491927, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24052, 26.38634392, 0.00083789, 31.97505048, 0.01983938, 3.19750505, 0.08099464, -26.38634392, -0.00083789, -31.97505048, -0.01983938, -3.19750505, -0.08099464, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14052, 26.38634392, 0.00083789, 31.97505048, 0.01983938, 3.19750505, 0.08099464, -26.38634392, -0.00083789, -31.97505048, -0.01983938, -3.19750505, -0.08099464, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24052, 4052, 0.0, 81.01174859, 0.01675771, 81.01174859, 0.05027312, 56.70822401, -3747.22546645, 0.05, 2, 0, 74021, 23001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44052, 20.25293715, 4.208e-05, 60.75881144, 0.00012625, 202.52937147, 0.00042082, -20.25293715, -4.208e-05, -60.75881144, -0.00012625, -202.52937147, -0.00042082, 0.4, 0.3, 0.003, 0.0, 0.0, 24052, 2)
    ops.limitCurve('ThreePoint', 14052, 4052, 0.0, 81.01174859, 0.01675771, 81.01174859, 0.05027312, 56.70822401, -3747.22546645, 0.05, 2, 0, 74021, 23001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34052, 20.25293715, 4.208e-05, 60.75881144, 0.00012625, 202.52937147, 0.00042082, -20.25293715, -4.208e-05, -60.75881144, -0.00012625, -202.52937147, -0.00042082, 0.4, 0.3, 0.003, 0.0, 0.0, 14052, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4052, 99999, 'P', 44052, 'Vy', 34052, 'Vz', 24052, 'My', 14052, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174021, 74021, 174021, 4052, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123001, 123001, 23001, 4052, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172002, 3.0, 0.0, 6.05)
    ops.node(124022, 3.0, 0.0, 7.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4053, 172002, 124022, 0.0625, 28169917.09349846, 11737465.45562436, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24053, 38.29925651, 0.00097935, 46.20995432, 0.02505623, 4.62099543, 0.07817886, -38.29925651, -0.00097935, -46.20995432, -0.02505623, -4.62099543, -0.07817886, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14053, 38.29925651, 0.00097935, 46.20995432, 0.02505623, 4.62099543, 0.07817886, -38.29925651, -0.00097935, -46.20995432, -0.02505623, -4.62099543, -0.07817886, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24053, 4053, 0.0, 101.7553428, 0.01958704, 101.7553428, 0.05876112, 71.22873996, -3625.42245169, 0.05, 2, 0, 72002, 24022, 2, 3)
    ops.uniaxialMaterial('LimitState', 44053, 25.4388357, 5.722e-05, 76.3165071, 0.00017165, 254.38835701, 0.00057217, -25.4388357, -5.722e-05, -76.3165071, -0.00017165, -254.38835701, -0.00057217, 0.4, 0.3, 0.003, 0.0, 0.0, 24053, 2)
    ops.limitCurve('ThreePoint', 14053, 4053, 0.0, 101.7553428, 0.01958704, 101.7553428, 0.05876112, 71.22873996, -3625.42245169, 0.05, 2, 0, 72002, 24022, 1, 3)
    ops.uniaxialMaterial('LimitState', 34053, 25.4388357, 5.722e-05, 76.3165071, 0.00017165, 254.38835701, 0.00057217, -25.4388357, -5.722e-05, -76.3165071, -0.00017165, -254.38835701, -0.00057217, 0.4, 0.3, 0.003, 0.0, 0.0, 14053, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4053, 99999, 'P', 44053, 'Vy', 34053, 'Vz', 24053, 'My', 14053, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172002, 72002, 172002, 4053, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124022, 124022, 24022, 4053, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174022, 3.0, 0.0, 7.35)
    ops.node(123002, 3.0, 0.0, 8.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4054, 174022, 123002, 0.0625, 35409311.70032092, 14753879.87513372, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24054, 33.29511211, 0.00092414, 39.53543943, 0.02888171, 3.95354394, 0.11670442, -33.29511211, -0.00092414, -39.53543943, -0.02888171, -3.95354394, -0.11670442, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14054, 33.29511211, 0.00092414, 39.53543943, 0.02888171, 3.95354394, 0.11670442, -33.29511211, -0.00092414, -39.53543943, -0.02888171, -3.95354394, -0.11670442, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24054, 4054, 0.0, 122.35107281, 0.01848286, 122.35107281, 0.05544859, 85.64575097, -4485.36830959, 0.05, 2, 0, 74022, 23002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44054, 30.5877682, 5.473e-05, 91.76330461, 0.0001642, 305.87768202, 0.00054733, -30.5877682, -5.473e-05, -91.76330461, -0.0001642, -305.87768202, -0.00054733, 0.4, 0.3, 0.003, 0.0, 0.0, 24054, 2)
    ops.limitCurve('ThreePoint', 14054, 4054, 0.0, 122.35107281, 0.01848286, 122.35107281, 0.05544859, 85.64575097, -4485.36830959, 0.05, 2, 0, 74022, 23002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34054, 30.5877682, 5.473e-05, 91.76330461, 0.0001642, 305.87768202, 0.00054733, -30.5877682, -5.473e-05, -91.76330461, -0.0001642, -305.87768202, -0.00054733, 0.4, 0.3, 0.003, 0.0, 0.0, 14054, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4054, 99999, 'P', 44054, 'Vy', 34054, 'Vz', 24054, 'My', 14054, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174022, 74022, 174022, 4054, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123002, 123002, 23002, 4054, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173001, 0.0, 0.0, 8.775)
    ops.node(124023, 0.0, 0.0, 9.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4056, 173001, 124023, 0.0625, 30898239.49953636, 12874266.45814015, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24056, 22.95162107, 0.0008948, 27.80362305, 0.02015739, 2.78036231, 0.08302749, -22.95162107, -0.0008948, -27.80362305, -0.02015739, -2.78036231, -0.08302749, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14056, 22.95162107, 0.0008948, 27.80362305, 0.02015739, 2.78036231, 0.08302749, -22.95162107, -0.0008948, -27.80362305, -0.02015739, -2.78036231, -0.08302749, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24056, 4056, 0.0, 81.8752419, 0.01789599, 81.8752419, 0.05368796, 57.31266933, -4895.87378251, 0.05, 2, 0, 73001, 24023, 2, 3)
    ops.uniaxialMaterial('LimitState', 44056, 20.46881047, 4.197e-05, 61.40643142, 0.00012592, 204.68810474, 0.00041973, -20.46881047, -4.197e-05, -61.40643142, -0.00012592, -204.68810474, -0.00041973, 0.4, 0.3, 0.003, 0.0, 0.0, 24056, 2)
    ops.limitCurve('ThreePoint', 14056, 4056, 0.0, 81.8752419, 0.01789599, 81.8752419, 0.05368796, 57.31266933, -4895.87378251, 0.05, 2, 0, 73001, 24023, 1, 3)
    ops.uniaxialMaterial('LimitState', 34056, 20.46881047, 4.197e-05, 61.40643142, 0.00012592, 204.68810474, 0.00041973, -20.46881047, -4.197e-05, -61.40643142, -0.00012592, -204.68810474, -0.00041973, 0.4, 0.3, 0.003, 0.0, 0.0, 14056, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4056, 99999, 'P', 44056, 'Vy', 34056, 'Vz', 24056, 'My', 14056, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173001, 73001, 173001, 4056, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124023, 124023, 24023, 4056, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174023, 0.0, 0.0, 10.1)
    ops.node(124001, 0.0, 0.0, 11.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4057, 174023, 124001, 0.0625, 31191729.16530515, 12996553.81887715, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24057, 20.91736255, 0.00089314, 25.36372384, 0.02096249, 2.53637238, 0.08749486, -20.91736255, -0.00089314, -25.36372384, -0.02096249, -2.53637238, -0.08749486, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14057, 20.91736255, 0.00089314, 25.36372384, 0.02096249, 2.53637238, 0.08749486, -20.91736255, -0.00089314, -25.36372384, -0.02096249, -2.53637238, -0.08749486, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24057, 4057, 0.0, 80.29131403, 0.01786272, 80.29131403, 0.05358815, 56.20391982, -38286.15982841, 0.05, 2, 0, 74023, 24001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44057, 20.07282851, 4.077e-05, 60.21848552, 0.00012232, 200.72828507, 0.00040774, -20.07282851, -4.077e-05, -60.21848552, -0.00012232, -200.72828507, -0.00040774, 0.4, 0.3, 0.003, 0.0, 0.0, 24057, 2)
    ops.limitCurve('ThreePoint', 14057, 4057, 0.0, 80.29131403, 0.01786272, 80.29131403, 0.05358815, 56.20391982, -38286.15982841, 0.05, 2, 0, 74023, 24001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34057, 20.07282851, 4.077e-05, 60.21848552, 0.00012232, 200.72828507, 0.00040774, -20.07282851, -4.077e-05, -60.21848552, -0.00012232, -200.72828507, -0.00040774, 0.4, 0.3, 0.003, 0.0, 0.0, 14057, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4057, 99999, 'P', 44057, 'Vy', 34057, 'Vz', 24057, 'My', 14057, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174023, 74023, 174023, 4057, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124001, 124001, 24001, 4057, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173002, 3.0, 0.0, 8.8)
    ops.node(124024, 3.0, 0.0, 9.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4058, 173002, 124024, 0.0625, 30328327.43030292, 12636803.09595955, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24058, 27.03226894, 0.00088514, 32.74284806, 0.01757834, 3.27428481, 0.07701308, -27.03226894, -0.00088514, -32.74284806, -0.01757834, -3.27428481, -0.07701308, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14058, 27.03226894, 0.00088514, 32.74284806, 0.01757834, 3.27428481, 0.07701308, -27.03226894, -0.00088514, -32.74284806, -0.01757834, -3.27428481, -0.07701308, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24058, 4058, 0.0, 74.28176594, 0.01770271, 74.28176594, 0.05310814, 51.99723616, -3024.10027103, 0.05, 2, 0, 73002, 24024, 2, 3)
    ops.uniaxialMaterial('LimitState', 44058, 18.57044148, 3.88e-05, 55.71132445, 0.00011639, 185.70441485, 0.00038796, -18.57044148, -3.88e-05, -55.71132445, -0.00011639, -185.70441485, -0.00038796, 0.4, 0.3, 0.003, 0.0, 0.0, 24058, 2)
    ops.limitCurve('ThreePoint', 14058, 4058, 0.0, 74.28176594, 0.01770271, 74.28176594, 0.05310814, 51.99723616, -3024.10027103, 0.05, 2, 0, 73002, 24024, 1, 3)
    ops.uniaxialMaterial('LimitState', 34058, 18.57044148, 3.88e-05, 55.71132445, 0.00011639, 185.70441485, 0.00038796, -18.57044148, -3.88e-05, -55.71132445, -0.00011639, -185.70441485, -0.00038796, 0.4, 0.3, 0.003, 0.0, 0.0, 14058, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4058, 99999, 'P', 44058, 'Vy', 34058, 'Vz', 24058, 'My', 14058, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173002, 73002, 173002, 4058, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124024, 124024, 24024, 4058, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174024, 3.0, 0.0, 10.1)
    ops.node(124002, 3.0, 0.0, 11.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4059, 174024, 124002, 0.0625, 29991180.37062142, 12496325.15442559, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24059, 23.78375873, 0.00085264, 28.89304299, 0.02327424, 2.8893043, 0.08624517, -23.78375873, -0.00085264, -28.89304299, -0.02327424, -2.8893043, -0.08624517, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14059, 23.78375873, 0.00085264, 28.89304299, 0.02327424, 2.8893043, 0.08624517, -23.78375873, -0.00085264, -28.89304299, -0.02327424, -2.8893043, -0.08624517, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24059, 4059, 0.0, 84.8480517, 0.01705287, 84.8480517, 0.05115861, 59.39363619, -6758.2918758, 0.05, 2, 0, 74024, 24002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44059, 21.21201293, 4.481e-05, 63.63603878, 0.00013444, 212.12012926, 0.00044813, -21.21201293, -4.481e-05, -63.63603878, -0.00013444, -212.12012926, -0.00044813, 0.4, 0.3, 0.003, 0.0, 0.0, 24059, 2)
    ops.limitCurve('ThreePoint', 14059, 4059, 0.0, 84.8480517, 0.01705287, 84.8480517, 0.05115861, 59.39363619, -6758.2918758, 0.05, 2, 0, 74024, 24002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34059, 21.21201293, 4.481e-05, 63.63603878, 0.00013444, 212.12012926, 0.00044813, -21.21201293, -4.481e-05, -63.63603878, -0.00013444, -212.12012926, -0.00044813, 0.4, 0.3, 0.003, 0.0, 0.0, 14059, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4059, 99999, 'P', 44059, 'Vy', 34059, 'Vz', 24059, 'My', 14059, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174024, 74024, 174024, 4059, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124002, 124002, 24002, 4059, '-orient', 0, 0, 1, 0, 1, 0)
