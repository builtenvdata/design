import openseespy.opensees as ops


def add_columns() -> None:
    """Add components of all columns to ops domain (plastic hinges, column elements and nodes)
    """
    # Create elastic column element nodes
    ops.node(170003, 7.35, 0.0, 0.0)
    ops.node(121003, 7.35, 0.0, 2.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3, 170003, 121003, 0.1925, 26119670.70288791, 10883196.1262033, 0.00475217, 0.00533786, 0.00216161, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20003, 159.51481889, 0.00073998, 193.95960152, 0.05632542, 19.39596015, 0.1320238, -159.51481889, -0.00073998, -193.95960152, -0.05632542, -19.39596015, -0.1320238, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10003, 198.57024398, 0.00055958, 241.44844764, 0.05711322, 24.14484476, 0.13597679, -198.57024398, -0.00055958, -241.44844764, -0.05711322, -24.14484476, -0.13597679, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20003, 3, 0.0, 193.19553705, 0.01479969, 193.19553705, 0.04439906, 135.23687594, -2571.74329227, 0.05, 2, 0, 70003, 21003, 2, 3)
    ops.uniaxialMaterial('LimitState', 40003, 48.29888426, 8.714e-05, 144.89665279, 0.00026143, 482.98884263, 0.00087145, -48.29888426, -8.714e-05, -144.89665279, -0.00026143, -482.98884263, -0.00087145, 0.4, 0.3, 0.003, 0.0, 0.0, 20003, 2)
    ops.limitCurve('ThreePoint', 10003, 3, 0.0, 321.03202551, 0.01119153, 321.03202551, 0.0335746, 224.72241786, -8197.07561385, 0.05, 2, 0, 70003, 21003, 1, 3)
    ops.uniaxialMaterial('LimitState', 30003, 80.25800638, 0.00014481, 240.77401913, 0.00043442, 802.58006378, 0.00144808, -80.25800638, -0.00014481, -240.77401913, -0.00043442, -802.58006378, -0.00144808, 0.4, 0.3, 0.003, 0.0, 0.0, 10003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3, 99999, 'P', 40003, 'Vy', 30003, 'Vz', 20003, 'My', 10003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170003, 70003, 170003, 3, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121003, 121003, 21003, 3, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170004, 11.6, 0.0, 0.0)
    ops.node(121004, 11.6, 0.0, 2.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4, 170004, 121004, 0.105, 29572314.77056647, 12321797.82106936, 0.00152551, 0.00117906, 0.00086625, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20004, 52.14262584, 0.0007609, 63.0708473, 0.02574671, 6.30708473, 0.07457124, -52.14262584, -0.0007609, -63.0708473, -0.02574671, -6.30708473, -0.07457124, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10004, 54.78446858, 0.00067809, 66.26637606, 0.02698483, 6.62663761, 0.08215569, -54.78446858, -0.00067809, -66.26637606, -0.02698483, -6.62663761, -0.08215569, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20004, 4, 0.0, 101.39851795, 0.01521798, 101.39851795, 0.04565393, 70.97896257, -922.4024895, 0.05, 2, 0, 70004, 21004, 2, 3)
    ops.uniaxialMaterial('LimitState', 40004, 25.34962949, 7.406e-05, 76.04888846, 0.00022219, 253.49629488, 0.00074063, -25.34962949, -7.406e-05, -76.04888846, -0.00022219, -253.49629488, -0.00074063, 0.4, 0.3, 0.003, 0.0, 0.0, 20004, 2)
    ops.limitCurve('ThreePoint', 10004, 4, 0.0, 106.57492863, 0.01356188, 106.57492863, 0.04068565, 74.60245004, -1071.65785781, 0.05, 2, 0, 70004, 21004, 1, 3)
    ops.uniaxialMaterial('LimitState', 30004, 26.64373216, 7.784e-05, 79.93119647, 0.00023353, 266.43732156, 0.00077844, -26.64373216, -7.784e-05, -79.93119647, -0.00023353, -266.43732156, -0.00077844, 0.4, 0.3, 0.003, 0.0, 0.0, 10004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4, 99999, 'P', 40004, 'Vy', 30004, 'Vz', 20004, 'My', 10004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170004, 70004, 170004, 4, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121004, 121004, 21004, 4, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170005, 0.0, 4.4, 0.0)
    ops.node(121005, 0.0, 4.4, 2.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 5, 170005, 121005, 0.1, 29066308.54822284, 12110961.89509285, 0.00127345, 0.00057292, 0.00146667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20005, 69.97719252, 0.00062294, 84.4448542, 0.02812456, 8.44448542, 0.0854101, -69.97719252, -0.00062294, -84.4448542, -0.02812456, -8.44448542, -0.0854101, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10005, 46.92652291, 0.00089248, 56.62849913, 0.02438032, 5.66284991, 0.06378253, -46.92652291, -0.00089248, -56.62849913, -0.02438032, -5.66284991, -0.06378253, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20005, 5, 0.0, 114.13762927, 0.01245887, 114.13762927, 0.03737661, 79.89634049, -1284.94560056, 0.05, 2, 0, 70005, 21005, 2, 3)
    ops.uniaxialMaterial('LimitState', 40005, 28.53440732, 8.906e-05, 85.60322195, 0.00026718, 285.34407318, 0.0008906, -28.53440732, -8.906e-05, -85.60322195, -0.00026718, -285.34407318, -0.0008906, 0.4, 0.3, 0.003, 0.0, 0.0, 20005, 2)
    ops.limitCurve('ThreePoint', 10005, 5, 0.0, 97.87878859, 0.01784968, 97.87878859, 0.05354904, 68.51515202, -866.70454869, 0.05, 2, 0, 70005, 21005, 1, 3)
    ops.uniaxialMaterial('LimitState', 30005, 24.46969715, 7.637e-05, 73.40909144, 0.00022912, 244.69697148, 0.00076373, -24.46969715, -7.637e-05, -73.40909144, -0.00022912, -244.69697148, -0.00076373, 0.4, 0.3, 0.003, 0.0, 0.0, 10005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 5, 99999, 'P', 40005, 'Vy', 30005, 'Vz', 20005, 'My', 10005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170005, 70005, 170005, 5, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121005, 121005, 21005, 5, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170006, 3.1, 4.4, 0.0)
    ops.node(121006, 3.1, 4.4, 2.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 6, 170006, 121006, 0.2275, 28999916.03559846, 12083298.34816602, 0.00616035, 0.00255464, 0.00881089, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20006, 263.41799097, 0.00050601, 318.82219463, 0.05455028, 31.88221946, 0.13913859, -263.41799097, -0.00050601, -318.82219463, -0.05455028, -31.88221946, -0.13913859, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10006, 175.53845361, 0.00069401, 212.45912178, 0.05066643, 21.24591218, 0.12091114, -175.53845361, -0.00069401, -212.45912178, -0.05066643, -21.24591218, -0.12091114, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20006, 6, 0.0, 445.20027637, 0.01012022, 445.20027637, 0.03036065, 311.64019346, -9795.64443807, 0.05, 2, 0, 70006, 21006, 2, 3)
    ops.uniaxialMaterial('LimitState', 40006, 111.30006909, 0.00015305, 333.90020728, 0.00045914, 1113.00069094, 0.00153045, -111.30006909, -0.00015305, -333.90020728, -0.00045914, -1113.00069094, -0.00153045, 0.4, 0.3, 0.003, 0.0, 0.0, 20006, 2)
    ops.limitCurve('ThreePoint', 10006, 6, 0.0, 238.83617884, 0.01388014, 238.83617884, 0.04164042, 167.18532519, -2624.61880515, 0.05, 2, 0, 70006, 21006, 1, 3)
    ops.uniaxialMaterial('LimitState', 30006, 59.70904471, 8.21e-05, 179.12713413, 0.00024631, 597.09044711, 0.00082104, -59.70904471, -8.21e-05, -179.12713413, -0.00024631, -597.09044711, -0.00082104, 0.4, 0.3, 0.003, 0.0, 0.0, 10006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 6, 99999, 'P', 40006, 'Vy', 30006, 'Vz', 20006, 'My', 10006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170006, 70006, 170006, 6, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121006, 121006, 21006, 6, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170007, 7.35, 4.4, 0.0)
    ops.node(121007, 7.35, 4.4, 2.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 7, 170007, 121007, 0.3, 28588677.97429515, 11911949.15595631, 0.01066025, 0.0044, 0.01546875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20007, 377.416126, 0.00049586, 457.73135515, 0.05150113, 45.77313551, 0.12890209, -377.416126, -0.00049586, -457.73135515, -0.05150113, -45.77313551, -0.12890209, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10007, 260.07993845, 0.00065419, 315.42569189, 0.04773356, 31.54256919, 0.11174157, -260.07993845, -0.00065419, -315.42569189, -0.04773356, -31.54256919, -0.11174157, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20007, 7, 0.0, 519.26955142, 0.00991728, 519.26955142, 0.02975185, 363.48868599, -8521.92605081, 0.05, 2, 0, 70007, 21007, 2, 3)
    ops.uniaxialMaterial('LimitState', 40007, 129.81738785, 0.00013732, 389.45216356, 0.00041195, 1298.17387854, 0.00137316, -129.81738785, -0.00013732, -389.45216356, -0.00041195, -1298.17387854, -0.00137316, 0.4, 0.3, 0.003, 0.0, 0.0, 20007, 2)
    ops.limitCurve('ThreePoint', 10007, 7, 0.0, 270.78302231, 0.01308382, 270.78302231, 0.03925146, 189.54811562, -2452.54997178, 0.05, 2, 0, 70007, 21007, 1, 3)
    ops.uniaxialMaterial('LimitState', 30007, 67.69575558, 7.161e-05, 203.08726673, 0.00021482, 676.95755577, 0.00071606, -67.69575558, -7.161e-05, -203.08726673, -0.00021482, -676.95755577, -0.00071606, 0.4, 0.3, 0.003, 0.0, 0.0, 10007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 7, 99999, 'P', 40007, 'Vy', 30007, 'Vz', 20007, 'My', 10007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170007, 70007, 170007, 7, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121007, 121007, 21007, 7, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170008, 11.6, 4.4, 0.0)
    ops.node(121008, 11.6, 4.4, 2.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 8, 170008, 121008, 0.165, 27933934.44590719, 11639139.35246133, 0.00326155, 0.00136125, 0.00457531, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20008, 143.58131035, 0.0005397, 173.98039284, 0.04901799, 17.39803928, 0.14147337, -143.58131035, -0.0005397, -173.98039284, -0.04901799, -17.39803928, -0.14147337, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10008, 92.89365877, 0.00077352, 112.5611349, 0.03965488, 11.25611349, 0.09444114, -92.89365877, -0.00077352, -112.5611349, -0.03965488, -11.25611349, -0.09444114, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20008, 8, 0.0, 236.51214359, 0.01079393, 236.51214359, 0.0323818, 165.55850051, -3921.35568479, 0.05, 2, 0, 70008, 21008, 2, 3)
    ops.uniaxialMaterial('LimitState', 40008, 59.1280359, 0.00011638, 177.38410769, 0.00034914, 591.28035898, 0.00116381, -59.1280359, -0.00011638, -177.38410769, -0.00034914, -591.28035898, -0.00116381, 0.4, 0.3, 0.003, 0.0, 0.0, 20008, 2)
    ops.limitCurve('ThreePoint', 10008, 8, 0.0, 169.97359641, 0.01547043, 169.97359641, 0.0464113, 118.98151749, -1925.09877747, 0.05, 2, 0, 70008, 21008, 1, 3)
    ops.uniaxialMaterial('LimitState', 30008, 42.4933991, 8.364e-05, 127.48019731, 0.00025092, 424.93399103, 0.00083639, -42.4933991, -8.364e-05, -127.48019731, -0.00025092, -424.93399103, -0.00083639, 0.4, 0.3, 0.003, 0.0, 0.0, 10008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 8, 99999, 'P', 40008, 'Vy', 30008, 'Vz', 20008, 'My', 10008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170008, 70008, 170008, 8, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121008, 121008, 21008, 8, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170009, 0.0, 8.8, 0.0)
    ops.node(121009, 0.0, 8.8, 2.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 9, 170009, 121009, 0.1, 29891199.07830913, 12454666.28262881, 0.00127345, 0.00057292, 0.00146667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20009, 67.97847687, 0.00063497, 81.93167639, 0.02953293, 8.19316764, 0.08872557, -67.97847687, -0.00063497, -81.93167639, -0.02953293, -8.19316764, -0.08872557, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10009, 44.06967579, 0.00089393, 53.11537683, 0.02557432, 5.31153768, 0.06628828, -44.06967579, -0.00089393, -53.11537683, -0.02557432, -5.31153768, -0.06628828, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20009, 9, 0.0, 121.14867017, 0.01269941, 121.14867017, 0.03809822, 84.80406912, -1418.9394056, 0.05, 2, 0, 70009, 21009, 2, 3)
    ops.uniaxialMaterial('LimitState', 40009, 30.28716754, 9.192e-05, 90.86150263, 0.00027577, 302.87167543, 0.00091922, -30.28716754, -9.192e-05, -90.86150263, -0.00027577, -302.87167543, -0.00091922, 0.4, 0.3, 0.003, 0.0, 0.0, 20009, 2)
    ops.limitCurve('ThreePoint', 10009, 9, 0.0, 103.15604063, 0.01787865, 103.15604063, 0.05363596, 72.20922844, -933.24284124, 0.05, 2, 0, 70009, 21009, 1, 3)
    ops.uniaxialMaterial('LimitState', 30009, 25.78901016, 7.827e-05, 77.36703047, 0.00023481, 257.89010158, 0.0007827, -25.78901016, -7.827e-05, -77.36703047, -0.00023481, -257.89010158, -0.0007827, 0.4, 0.3, 0.003, 0.0, 0.0, 10009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 9, 99999, 'P', 40009, 'Vy', 30009, 'Vz', 20009, 'My', 10009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170009, 70009, 170009, 9, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121009, 121009, 21009, 9, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170010, 3.1, 8.8, 0.0)
    ops.node(121010, 3.1, 8.8, 2.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 10, 170010, 121010, 0.2275, 28440848.95627252, 11850353.73178022, 0.00616035, 0.00255464, 0.00881089, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20010, 256.1180184, 0.00051416, 310.39535548, 0.05240063, 31.03953555, 0.13655867, -256.1180184, -0.00051416, -310.39535548, -0.05240063, -31.03953555, -0.13655867, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10010, 169.43718802, 0.0007069, 205.34485054, 0.0486841, 20.53448505, 0.11857149, -169.43718802, -0.0007069, -205.34485054, -0.0486841, -20.53448505, -0.11857149, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20010, 10, 0.0, 399.39063987, 0.0102832, 399.39063987, 0.03084961, 279.57344791, -7761.38635419, 0.05, 2, 0, 70010, 21010, 2, 3)
    ops.uniaxialMaterial('LimitState', 40010, 99.84765997, 0.00014, 299.5429799, 0.00041999, 998.47659968, 0.00139996, -99.84765997, -0.00014, -299.5429799, -0.00041999, -998.47659968, -0.00139996, 0.4, 0.3, 0.003, 0.0, 0.0, 20010, 2)
    ops.limitCurve('ThreePoint', 10010, 10, 0.0, 219.66448448, 0.014138, 219.66448448, 0.042414, 153.76513914, -2206.85950498, 0.05, 2, 0, 70010, 21010, 1, 3)
    ops.uniaxialMaterial('LimitState', 30010, 54.91612112, 7.7e-05, 164.74836336, 0.00023099, 549.1612112, 0.00076998, -54.91612112, -7.7e-05, -164.74836336, -0.00023099, -549.1612112, -0.00076998, 0.4, 0.3, 0.003, 0.0, 0.0, 10010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 10, 99999, 'P', 40010, 'Vy', 30010, 'Vz', 20010, 'My', 10010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170010, 70010, 170010, 10, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121010, 121010, 21010, 10, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170011, 7.35, 8.8, 0.0)
    ops.node(121011, 7.35, 8.8, 2.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 11, 170011, 121011, 0.3, 28275730.93428167, 11781554.55595069, 0.01066025, 0.0044, 0.01546875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20011, 373.31346775, 0.00049166, 453.00109587, 0.05268907, 45.30010959, 0.12946594, -373.31346775, -0.00049166, -453.00109587, -0.05268907, -45.30010959, -0.12946594, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10011, 258.58843121, 0.00064464, 313.78681144, 0.04882438, 31.37868114, 0.1123163, -258.58843121, -0.00064464, -313.78681144, -0.04882438, -31.37868114, -0.1123163, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20011, 11, 0.0, 529.59015135, 0.00983325, 529.59015135, 0.02949974, 370.71310595, -9316.03096292, 0.05, 2, 0, 70011, 21011, 2, 3)
    ops.uniaxialMaterial('LimitState', 40011, 132.39753784, 0.00014159, 397.19261351, 0.00042478, 1323.97537838, 0.00141595, -132.39753784, -0.00014159, -397.19261351, -0.00042478, -1323.97537838, -0.00141595, 0.4, 0.3, 0.003, 0.0, 0.0, 20011, 2)
    ops.limitCurve('ThreePoint', 10011, 11, 0.0, 273.16328373, 0.01289278, 273.16328373, 0.03867833, 191.21429861, -2601.4395986, 0.05, 2, 0, 70011, 21011, 1, 3)
    ops.uniaxialMaterial('LimitState', 30011, 68.29082093, 7.303e-05, 204.87246279, 0.0002191, 682.90820931, 0.00073035, -68.29082093, -7.303e-05, -204.87246279, -0.0002191, -682.90820931, -0.00073035, 0.4, 0.3, 0.003, 0.0, 0.0, 10011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 11, 99999, 'P', 40011, 'Vy', 30011, 'Vz', 20011, 'My', 10011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170011, 70011, 170011, 11, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121011, 121011, 21011, 11, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170012, 11.6, 8.8, 0.0)
    ops.node(121012, 11.6, 8.8, 2.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 12, 170012, 121012, 0.165, 29899976.45938116, 12458323.52474215, 0.00326155, 0.00136125, 0.00457531, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20012, 139.17387053, 0.00051331, 168.09433915, 0.05246169, 16.80943392, 0.15083151, -139.17387053, -0.00051331, -168.09433915, -0.05246169, -16.80943392, -0.15083151, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10012, 89.23472271, 0.00072636, 107.77778679, 0.04239086, 10.77777868, 0.10068184, -89.23472271, -0.00072636, -107.77778679, -0.04239086, -10.77777868, -0.10068184, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20012, 12, 0.0, 268.33826183, 0.01026625, 268.33826183, 0.03079876, 187.83678328, -4886.6419969, 0.05, 2, 0, 70012, 21012, 2, 3)
    ops.uniaxialMaterial('LimitState', 40012, 67.08456546, 0.00012336, 201.25369637, 0.00037008, 670.84565458, 0.00123359, -67.08456546, -0.00012336, -201.25369637, -0.00037008, -670.84565458, -0.00123359, 0.4, 0.3, 0.003, 0.0, 0.0, 20012, 2)
    ops.limitCurve('ThreePoint', 10012, 12, 0.0, 191.11264627, 0.01452728, 191.11264627, 0.04358184, 133.77885239, -2288.85244413, 0.05, 2, 0, 70012, 21012, 1, 3)
    ops.uniaxialMaterial('LimitState', 30012, 47.77816157, 8.786e-05, 143.3344847, 0.00026357, 477.78161567, 0.00087857, -47.77816157, -8.786e-05, -143.3344847, -0.00026357, -477.78161567, -0.00087857, 0.4, 0.3, 0.003, 0.0, 0.0, 10012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 12, 99999, 'P', 40012, 'Vy', 30012, 'Vz', 20012, 'My', 10012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170012, 70012, 170012, 12, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121012, 121012, 21012, 12, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170013, 0.0, 13.2, 0.0)
    ops.node(121013, 0.0, 13.2, 2.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 13, 170013, 121013, 0.1, 29480732.14386581, 12283638.39327742, 0.00127345, 0.00057292, 0.00146667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20013, 65.61386319, 0.00063109, 79.13681991, 0.02834003, 7.91368199, 0.08668574, -65.61386319, -0.00063109, -79.13681991, -0.02834003, -7.91368199, -0.08668574, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10013, 42.07880022, 0.00090611, 50.75120216, 0.02457102, 5.07512022, 0.06470244, -42.07880022, -0.00090611, -50.75120216, -0.02457102, -5.07512022, -0.06470244, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20013, 13, 0.0, 118.20227464, 0.0126217, 118.20227464, 0.03786511, 82.74159224, -1369.31729103, 0.05, 2, 0, 70013, 21013, 2, 3)
    ops.uniaxialMaterial('LimitState', 40013, 29.55056866, 9.093e-05, 88.65170598, 0.0002728, 295.50568659, 0.00090935, -29.55056866, -9.093e-05, -88.65170598, -0.0002728, -295.50568659, -0.00090935, 0.4, 0.3, 0.003, 0.0, 0.0, 20013, 2)
    ops.limitCurve('ThreePoint', 10013, 13, 0.0, 100.83939759, 0.01812221, 100.83939759, 0.05436662, 70.58757832, -908.03961491, 0.05, 2, 0, 70013, 21013, 1, 3)
    ops.uniaxialMaterial('LimitState', 30013, 25.2098494, 7.758e-05, 75.6295482, 0.00023273, 252.09849398, 0.00077577, -25.2098494, -7.758e-05, -75.6295482, -0.00023273, -252.09849398, -0.00077577, 0.4, 0.3, 0.003, 0.0, 0.0, 10013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 13, 99999, 'P', 40013, 'Vy', 30013, 'Vz', 20013, 'My', 10013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170013, 70013, 170013, 13, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121013, 121013, 21013, 13, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170014, 3.1, 13.2, 0.0)
    ops.node(121014, 3.1, 13.2, 2.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 14, 170014, 121014, 0.2275, 27468781.31711004, 11445325.54879585, 0.00616035, 0.00255464, 0.00881089, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20014, 249.53978586, 0.00050969, 302.83328069, 0.05317656, 30.28332807, 0.13468301, -249.53978586, -0.00050969, -302.83328069, -0.05317656, -30.28332807, -0.13468301, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10014, 164.4145099, 0.00070137, 199.52804421, 0.04940017, 19.95280442, 0.11708561, -164.4145099, -0.00070137, -199.52804421, -0.04940017, -19.95280442, -0.11708561, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20014, 14, 0.0, 412.70793684, 0.01019389, 412.70793684, 0.03058167, 288.89555579, -8995.18848186, 0.05, 2, 0, 70014, 21014, 2, 3)
    ops.uniaxialMaterial('LimitState', 40014, 103.17698421, 0.00014978, 309.53095263, 0.00044935, 1031.7698421, 0.00149784, -103.17698421, -0.00014978, -309.53095263, -0.00044935, -1031.7698421, -0.00149784, 0.4, 0.3, 0.003, 0.0, 0.0, 20014, 2)
    ops.limitCurve('ThreePoint', 10014, 14, 0.0, 221.04782075, 0.01402748, 221.04782075, 0.04208245, 154.73347452, -2440.18525838, 0.05, 2, 0, 70014, 21014, 1, 3)
    ops.uniaxialMaterial('LimitState', 30014, 55.26195519, 8.022e-05, 165.78586556, 0.00024067, 552.61955187, 0.00080225, -55.26195519, -8.022e-05, -165.78586556, -0.00024067, -552.61955187, -0.00080225, 0.4, 0.3, 0.003, 0.0, 0.0, 10014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 14, 99999, 'P', 40014, 'Vy', 30014, 'Vz', 20014, 'My', 10014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170014, 70014, 170014, 14, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121014, 121014, 21014, 14, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170015, 7.35, 13.2, 0.0)
    ops.node(121015, 7.35, 13.2, 2.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 15, 170015, 121015, 0.3, 29411701.51323947, 12254875.63051645, 0.01066025, 0.0044, 0.01546875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20015, 375.27701092, 0.00048886, 454.43628883, 0.05081731, 45.44362888, 0.12985052, -375.27701092, -0.00048886, -454.43628883, -0.05081731, -45.44362888, -0.12985052, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10015, 258.88099825, 0.00063971, 313.4882145, 0.04709435, 31.34882145, 0.11245219, -258.88099825, -0.00063971, -313.4882145, -0.04709435, -31.34882145, -0.11245219, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20015, 15, 0.0, 528.86097919, 0.00977722, 528.86097919, 0.02933165, 370.20268543, -8450.90272553, 0.05, 2, 0, 70015, 21015, 2, 3)
    ops.uniaxialMaterial('LimitState', 40015, 132.2152448, 0.00013594, 396.64573439, 0.00040782, 1322.15244797, 0.00135939, -132.2152448, -0.00013594, -396.64573439, -0.00040782, -1322.15244797, -0.00135939, 0.4, 0.3, 0.003, 0.0, 0.0, 20015, 2)
    ops.limitCurve('ThreePoint', 10015, 15, 0.0, 277.51951432, 0.01279428, 277.51951432, 0.03838285, 194.26366003, -2437.59697792, 0.05, 2, 0, 70015, 21015, 1, 3)
    ops.uniaxialMaterial('LimitState', 30015, 69.37987858, 7.133e-05, 208.13963574, 0.000214, 693.7987858, 0.00071334, -69.37987858, -7.133e-05, -208.13963574, -0.000214, -693.7987858, -0.00071334, 0.4, 0.3, 0.003, 0.0, 0.0, 10015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 15, 99999, 'P', 40015, 'Vy', 30015, 'Vz', 20015, 'My', 10015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170015, 70015, 170015, 15, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121015, 121015, 21015, 15, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170016, 11.6, 13.2, 0.0)
    ops.node(121016, 11.6, 13.2, 2.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 16, 170016, 121016, 0.165, 27811112.37580542, 11587963.48991892, 0.00326155, 0.00136125, 0.00457531, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20016, 141.467156, 0.00053327, 171.44756393, 0.05008474, 17.14475639, 0.14216593, -141.467156, -0.00053327, -171.44756393, -0.05008474, -17.14475639, -0.14216593, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10016, 91.29453368, 0.00076291, 110.6421154, 0.04050499, 11.06421154, 0.09506952, -91.29453368, -0.00076291, -110.6421154, -0.04050499, -11.06421154, -0.09506952, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20016, 16, 0.0, 235.41077763, 0.0106655, 235.41077763, 0.03199649, 164.78754434, -3905.86031372, 0.05, 2, 0, 70016, 21016, 2, 3)
    ops.uniaxialMaterial('LimitState', 40016, 58.85269441, 0.00011635, 176.55808322, 0.00034905, 588.52694408, 0.0011635, -58.85269441, -0.00011635, -176.55808322, -0.00034905, -588.52694408, -0.0011635, 0.4, 0.3, 0.003, 0.0, 0.0, 20016, 2)
    ops.limitCurve('ThreePoint', 10016, 16, 0.0, 169.12748215, 0.01525825, 169.12748215, 0.04577474, 118.38923751, -1918.56464508, 0.05, 2, 0, 70016, 21016, 1, 3)
    ops.uniaxialMaterial('LimitState', 30016, 42.28187054, 8.359e-05, 126.84561162, 0.00025077, 422.81870539, 0.0008359, -42.28187054, -8.359e-05, -126.84561162, -0.00025077, -422.81870539, -0.0008359, 0.4, 0.3, 0.003, 0.0, 0.0, 10016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 16, 99999, 'P', 40016, 'Vy', 30016, 'Vz', 20016, 'My', 10016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170016, 70016, 170016, 16, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121016, 121016, 21016, 16, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170017, 0.0, 17.6, 0.0)
    ops.node(121017, 0.0, 17.6, 2.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 17, 170017, 121017, 0.1, 30777085.77421134, 12823785.73925472, 0.00127345, 0.00057292, 0.00146667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20017, 67.25961349, 0.00061686, 80.92528666, 0.02652363, 8.09252867, 0.0874179, -67.25961349, -0.00061686, -80.92528666, -0.02652363, -8.09252867, -0.0874179, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10017, 43.62293394, 0.00086253, 52.48615404, 0.02298827, 5.2486154, 0.06487265, -43.62293394, -0.00086253, -52.48615404, -0.02298827, -5.2486154, -0.06487265, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20017, 17, 0.0, 117.49116537, 0.0123373, 117.49116537, 0.0370119, 82.24381576, -1233.8852848, 0.05, 2, 0, 70017, 21017, 2, 3)
    ops.uniaxialMaterial('LimitState', 40017, 29.37279134, 8.658e-05, 88.11837403, 0.00025974, 293.72791342, 0.00086581, -29.37279134, -8.658e-05, -88.11837403, -0.00025974, -293.72791342, -0.00086581, 0.4, 0.3, 0.003, 0.0, 0.0, 20017, 2)
    ops.limitCurve('ThreePoint', 10017, 17, 0.0, 101.90762539, 0.01725053, 101.90762539, 0.0517516, 71.33533777, -838.69350657, 0.05, 2, 0, 70017, 21017, 1, 3)
    ops.uniaxialMaterial('LimitState', 30017, 25.47690635, 7.51e-05, 76.43071904, 0.00022529, 254.76906348, 0.00075097, -25.47690635, -7.51e-05, -76.43071904, -0.00022529, -254.76906348, -0.00075097, 0.4, 0.3, 0.003, 0.0, 0.0, 10017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 17, 99999, 'P', 40017, 'Vy', 30017, 'Vz', 20017, 'My', 10017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170017, 70017, 170017, 17, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121017, 121017, 21017, 17, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170018, 3.1, 17.6, 0.0)
    ops.node(121018, 3.1, 17.6, 2.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 18, 170018, 121018, 0.2275, 31267157.87698254, 13027982.44874272, 0.00616035, 0.00255464, 0.00881089, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20018, 253.67948939, 0.00050207, 305.63855195, 0.05241238, 30.56385519, 0.14272099, -253.67948939, -0.00050207, -305.63855195, -0.05241238, -30.56385519, -0.14272099, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10018, 164.3330543, 0.00069133, 197.99202874, 0.04869058, 19.79920287, 0.12368559, -164.3330543, -0.00069133, -197.99202874, -0.04869058, -19.79920287, -0.12368559, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20018, 18, 0.0, 437.92307063, 0.01004147, 437.92307063, 0.03012442, 306.54614944, -8471.62936806, 0.05, 2, 0, 70018, 21018, 2, 3)
    ops.uniaxialMaterial('LimitState', 40018, 109.48076766, 0.00013963, 328.44230297, 0.00041888, 1094.80767657, 0.00139628, -109.48076766, -0.00013963, -328.44230297, -0.00041888, -1094.80767657, -0.00139628, 0.4, 0.3, 0.003, 0.0, 0.0, 20018, 2)
    ops.limitCurve('ThreePoint', 10018, 18, 0.0, 243.75521567, 0.01382664, 243.75521567, 0.04147992, 170.62865097, -2341.83986738, 0.05, 2, 0, 70018, 21018, 1, 3)
    ops.uniaxialMaterial('LimitState', 30018, 60.93880392, 7.772e-05, 182.81641175, 0.00023316, 609.38803917, 0.00077719, -60.93880392, -7.772e-05, -182.81641175, -0.00023316, -609.38803917, -0.00077719, 0.4, 0.3, 0.003, 0.0, 0.0, 10018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 18, 99999, 'P', 40018, 'Vy', 30018, 'Vz', 20018, 'My', 10018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170018, 70018, 170018, 18, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121018, 121018, 21018, 18, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170019, 7.35, 17.6, 0.0)
    ops.node(121019, 7.35, 17.6, 2.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 19, 170019, 121019, 0.3, 29326258.13271105, 12219274.22196294, 0.01066025, 0.0044, 0.01546875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20019, 390.91253704, 0.00050221, 473.45137405, 0.05102583, 47.34513741, 0.12990021, -390.91253704, -0.00050221, -473.45137405, -0.05102583, -47.34513741, -0.12990021, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10019, 273.08384063, 0.00066033, 330.74385528, 0.04729513, 33.07438553, 0.11252162, -273.08384063, -0.00066033, -330.74385528, -0.04729513, -33.07438553, -0.11252162, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20019, 19, 0.0, 534.76912912, 0.01004411, 534.76912912, 0.03013232, 374.33839038, -8826.39154954, 0.05, 2, 0, 70019, 21019, 2, 3)
    ops.uniaxialMaterial('LimitState', 40019, 133.69228228, 0.00013786, 401.07684684, 0.00041357, 1336.92282279, 0.00137858, -133.69228228, -0.00013786, -401.07684684, -0.00041357, -1336.92282279, -0.00137858, 0.4, 0.3, 0.003, 0.0, 0.0, 20019, 2)
    ops.limitCurve('ThreePoint', 10019, 19, 0.0, 279.26930553, 0.01320668, 279.26930553, 0.03962003, 195.48851387, -2509.03604713, 0.05, 2, 0, 70019, 21019, 1, 3)
    ops.uniaxialMaterial('LimitState', 30019, 69.81732638, 7.199e-05, 209.45197914, 0.00021598, 698.17326381, 0.00071993, -69.81732638, -7.199e-05, -209.45197914, -0.00021598, -698.17326381, -0.00071993, 0.4, 0.3, 0.003, 0.0, 0.0, 10019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 19, 99999, 'P', 40019, 'Vy', 30019, 'Vz', 20019, 'My', 10019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170019, 70019, 170019, 19, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121019, 121019, 21019, 19, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170020, 11.6, 17.6, 0.0)
    ops.node(121020, 11.6, 17.6, 2.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 20, 170020, 121020, 0.165, 31207483.07457853, 13003117.94774106, 0.00326155, 0.00136125, 0.00457531, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20020, 147.64546199, 0.00054082, 177.80240658, 0.0472758, 17.78024066, 0.1472758, -147.64546199, -0.00054082, -177.80240658, -0.0472758, -17.78024066, -0.1472758, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10020, 94.56785505, 0.00077896, 113.88356937, 0.03826213, 11.38835694, 0.09845881, -94.56785505, -0.00077896, -113.88356937, -0.03826213, -11.38835694, -0.09845881, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20020, 20, 0.0, 244.6017515, 0.0108163, 244.6017515, 0.03244891, 171.22122605, -3494.53588703, 0.05, 2, 0, 70020, 21020, 2, 3)
    ops.uniaxialMaterial('LimitState', 40020, 61.15043787, 0.00010774, 183.45131362, 0.00032321, 611.50437874, 0.00107736, -61.15043787, -0.00010774, -183.45131362, -0.00032321, -611.50437874, -0.00107736, 0.4, 0.3, 0.003, 0.0, 0.0, 20020, 2)
    ops.limitCurve('ThreePoint', 10020, 20, 0.0, 180.76822663, 0.01557929, 180.76822663, 0.04673788, 126.53775864, -1760.35136009, 0.05, 2, 0, 70020, 21020, 1, 3)
    ops.uniaxialMaterial('LimitState', 30020, 45.19205666, 7.962e-05, 135.57616997, 0.00023886, 451.92056656, 0.0007962, -45.19205666, -7.962e-05, -135.57616997, -0.00023886, -451.92056656, -0.0007962, 0.4, 0.3, 0.003, 0.0, 0.0, 10020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 20, 99999, 'P', 40020, 'Vy', 30020, 'Vz', 20020, 'My', 10020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170020, 70020, 170020, 20, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121020, 121020, 21020, 20, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170021, 0.0, 22.0, 0.0)
    ops.node(121021, 0.0, 22.0, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 21, 170021, 121021, 0.0625, 26974783.30074484, 11239493.04197701, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20021, 26.05741137, 0.00093269, 31.55012073, 0.0250486, 3.15501207, 0.07013386, -26.05741137, -0.00093269, -31.55012073, -0.0250486, -3.15501207, -0.07013386, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10021, 26.05741137, 0.00093269, 31.55012073, 0.0250486, 3.15501207, 0.07013386, -26.05741137, -0.00093269, -31.55012073, -0.0250486, -3.15501207, -0.07013386, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20021, 21, 0.0, 66.37295108, 0.01865376, 66.37295108, 0.05596127, 46.46106575, -798.59376535, 0.05, 2, 0, 70021, 21021, 2, 3)
    ops.uniaxialMaterial('LimitState', 40021, 16.59323777, 8.929e-05, 49.77971331, 0.00026787, 165.9323777, 0.00089289, -16.59323777, -8.929e-05, -49.77971331, -0.00026787, -165.9323777, -0.00089289, 0.4, 0.3, 0.003, 0.0, 0.0, 20021, 2)
    ops.limitCurve('ThreePoint', 10021, 21, 0.0, 66.37295108, 0.01865376, 66.37295108, 0.05596127, 46.46106575, -798.59376535, 0.05, 2, 0, 70021, 21021, 1, 3)
    ops.uniaxialMaterial('LimitState', 30021, 16.59323777, 8.929e-05, 49.77971331, 0.00026787, 165.9323777, 0.00089289, -16.59323777, -8.929e-05, -49.77971331, -0.00026787, -165.9323777, -0.00089289, 0.4, 0.3, 0.003, 0.0, 0.0, 10021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 21, 99999, 'P', 40021, 'Vy', 30021, 'Vz', 20021, 'My', 10021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170021, 70021, 170021, 21, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121021, 121021, 21021, 21, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170022, 3.1, 22.0, 0.0)
    ops.node(121022, 3.1, 22.0, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 22, 170022, 121022, 0.1575, 29374857.33694636, 12239523.89039432, 0.00337604, 0.00292359, 0.00176859, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20022, 122.55152425, 0.00071944, 148.2898988, 0.0566592, 14.82898988, 0.1560079, -122.55152425, -0.00071944, -148.2898988, -0.0566592, -14.82898988, -0.1560079, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10022, 131.69268184, 0.0006104, 159.35089003, 0.05339934, 15.935089, 0.13998353, -131.69268184, -0.0006104, -159.35089003, -0.05339934, -15.935089, -0.13998353, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20022, 22, 0.0, 184.44866306, 0.01438888, 184.44866306, 0.04316664, 129.11406414, -2457.47778195, 0.05, 2, 0, 70022, 21022, 2, 3)
    ops.uniaxialMaterial('LimitState', 40022, 46.11216577, 9.042e-05, 138.3364973, 0.00027126, 461.12165765, 0.0009042, -46.11216577, -9.042e-05, -138.3364973, -0.00027126, -461.12165765, -0.0009042, 0.4, 0.3, 0.003, 0.0, 0.0, 20022, 2)
    ops.limitCurve('ThreePoint', 10022, 22, 0.0, 258.55389639, 0.01220807, 258.55389639, 0.0366242, 180.98772748, -5955.7775165, 0.05, 2, 0, 70022, 21022, 1, 3)
    ops.uniaxialMaterial('LimitState', 30022, 64.6384741, 0.00012675, 193.91542229, 0.00038024, 646.38474098, 0.00126747, -64.6384741, -0.00012675, -193.91542229, -0.00038024, -646.38474098, -0.00126747, 0.4, 0.3, 0.003, 0.0, 0.0, 10022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 22, 99999, 'P', 40022, 'Vy', 30022, 'Vz', 20022, 'My', 10022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170022, 70022, 170022, 22, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121022, 121022, 21022, 22, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170023, 7.35, 22.0, 0.0)
    ops.node(121023, 7.35, 22.0, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 23, 170023, 121023, 0.22, 26806364.07744209, 11169318.36560087, 0.00648267, 0.00610042, 0.00322667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20023, 218.95715688, 0.00066878, 266.37679729, 0.05614317, 26.63767973, 0.13657023, -218.95715688, -0.00066878, -266.37679729, -0.05614317, -26.63767973, -0.13657023, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10023, 224.94358759, 0.00056156, 273.65971174, 0.05428906, 27.36597117, 0.12883775, -224.94358759, -0.00056156, -273.65971174, -0.05428906, -27.36597117, -0.12883775, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20023, 23, 0.0, 211.30144979, 0.01337564, 211.30144979, 0.04012692, 147.91101486, -2618.86429072, 0.05, 2, 0, 70023, 21023, 2, 3)
    ops.uniaxialMaterial('LimitState', 40023, 52.82536245, 8.126e-05, 158.47608735, 0.00024378, 528.25362449, 0.00081262, -52.82536245, -8.126e-05, -158.47608735, -0.00024378, -528.25362449, -0.00081262, 0.4, 0.3, 0.003, 0.0, 0.0, 20023, 2)
    ops.limitCurve('ThreePoint', 10023, 23, 0.0, 317.69696522, 0.01123126, 317.69696522, 0.03369378, 222.38787565, -6836.91804752, 0.05, 2, 0, 70023, 21023, 1, 3)
    ops.uniaxialMaterial('LimitState', 30023, 79.4242413, 0.00012218, 238.27272391, 0.00036654, 794.24241304, 0.00122179, -79.4242413, -0.00012218, -238.27272391, -0.00036654, -794.24241304, -0.00122179, 0.4, 0.3, 0.003, 0.0, 0.0, 10023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 23, 99999, 'P', 40023, 'Vy', 30023, 'Vz', 20023, 'My', 10023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170023, 70023, 170023, 23, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121023, 121023, 21023, 23, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170024, 11.6, 22.0, 0.0)
    ops.node(121024, 11.6, 22.0, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 24, 170024, 121024, 0.105, 29034381.50609666, 12097658.96087361, 0.00152551, 0.00117906, 0.00086625, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20024, 60.96756991, 0.00076342, 73.8191213, 0.03439172, 7.38191213, 0.09501168, -60.96756991, -0.00076342, -73.8191213, -0.03439172, -7.38191213, -0.09501168, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10024, 60.62711641, 0.00068251, 73.40690251, 0.03619635, 7.34069025, 0.10519123, -60.62711641, -0.00068251, -73.40690251, -0.03619635, -7.34069025, -0.10519123, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20024, 24, 0.0, 110.90365424, 0.0152684, 110.90365424, 0.04580519, 77.63255797, -1257.86530082, 0.05, 2, 0, 70024, 21024, 2, 3)
    ops.uniaxialMaterial('LimitState', 40024, 27.72591356, 8.251e-05, 83.17774068, 0.00024752, 277.25913561, 0.00082506, -27.72591356, -8.251e-05, -83.17774068, -0.00024752, -277.25913561, -0.00082506, 0.4, 0.3, 0.003, 0.0, 0.0, 20024, 2)
    ops.limitCurve('ThreePoint', 10024, 24, 0.0, 117.94024185, 0.01365028, 117.94024185, 0.04095083, 82.55816929, -1495.91544776, 0.05, 2, 0, 70024, 21024, 1, 3)
    ops.uniaxialMaterial('LimitState', 30024, 29.48506046, 8.774e-05, 88.45518139, 0.00026322, 294.85060462, 0.00087741, -29.48506046, -8.774e-05, -88.45518139, -0.00026322, -294.85060462, -0.00087741, 0.4, 0.3, 0.003, 0.0, 0.0, 10024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 24, 99999, 'P', 40024, 'Vy', 30024, 'Vz', 20024, 'My', 10024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170024, 70024, 170024, 24, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121024, 121024, 21024, 24, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171003, 7.35, 0.0, 3.375)
    ops.node(122003, 7.35, 0.0, 6.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1003, 171003, 122003, 0.1925, 27146703.3221064, 11311126.384211, 0.00475217, 0.00533786, 0.00216161, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21003, 85.52422906, 0.00072958, 104.16951038, 0.04793514, 10.41695104, 0.10834609, -85.52422906, -0.00072958, -104.16951038, -0.04793514, -10.41695104, -0.10834609, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11003, 160.69925223, 0.00055494, 195.73356704, 0.05609693, 19.5733567, 0.14494594, -160.69925223, -0.00055494, -195.73356704, -0.05609693, -19.5733567, -0.14494594, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21003, 1003, 0.0, 198.89011769, 0.01459164, 198.89011769, 0.04377493, 139.22308238, -3090.58702694, 0.05, 2, 0, 71003, 22003, 2, 3)
    ops.uniaxialMaterial('LimitState', 41003, 49.72252942, 8.632e-05, 149.16758827, 0.00025896, 497.22529422, 0.00086319, -49.72252942, -8.632e-05, -149.16758827, -0.00025896, -497.22529422, -0.00086319, 0.4, 0.3, 0.003, 0.0, 0.0, 21003, 2)
    ops.limitCurve('ThreePoint', 11003, 1003, 0.0, 263.96943174, 0.01109883, 263.96943174, 0.03329648, 184.77860222, -5928.32690033, 0.05, 2, 0, 71003, 22003, 1, 3)
    ops.uniaxialMaterial('LimitState', 31003, 65.99235794, 0.00011456, 197.97707381, 0.00034369, 659.92357936, 0.00114564, -65.99235794, -0.00011456, -197.97707381, -0.00034369, -659.92357936, -0.00114564, 0.4, 0.3, 0.003, 0.0, 0.0, 11003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1003, 99999, 'P', 41003, 'Vy', 31003, 'Vz', 21003, 'My', 11003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171003, 71003, 171003, 1003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122003, 122003, 22003, 1003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171004, 11.6, 0.0, 3.375)
    ops.node(122004, 11.6, 0.0, 6.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1004, 171004, 122004, 0.105, 27411289.06153249, 11421370.4423052, 0.00152551, 0.00117906, 0.00086625, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21004, 46.56713136, 0.00076373, 56.67934126, 0.02780208, 5.66793413, 0.07749174, -46.56713136, -0.00076373, -56.67934126, -0.02780208, -5.66793413, -0.07749174, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11004, 48.28971725, 0.00068059, 58.7759925, 0.02914836, 5.87759925, 0.08529681, -48.28971725, -0.00068059, -58.7759925, -0.02914836, -5.87759925, -0.08529681, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21004, 1004, 0.0, 93.65109833, 0.0152747, 93.65109833, 0.04582409, 65.55576883, -1028.90415946, 0.05, 2, 0, 71004, 22004, 2, 3)
    ops.uniaxialMaterial('LimitState', 41004, 23.41277458, 7.38e-05, 70.23832375, 0.00022139, 234.12774582, 0.00073797, -23.41277458, -7.38e-05, -70.23832375, -0.00022139, -234.12774582, -0.00073797, 0.4, 0.3, 0.003, 0.0, 0.0, 21004, 2)
    ops.limitCurve('ThreePoint', 11004, 1004, 0.0, 99.32611871, 0.01361187, 99.32611871, 0.0408356, 69.5282831, -1234.8470072, 0.05, 2, 0, 71004, 22004, 1, 3)
    ops.uniaxialMaterial('LimitState', 31004, 24.83152968, 7.827e-05, 74.49458903, 0.00023481, 248.31529678, 0.00078269, -24.83152968, -7.827e-05, -74.49458903, -0.00023481, -248.31529678, -0.00078269, 0.4, 0.3, 0.003, 0.0, 0.0, 11004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1004, 99999, 'P', 41004, 'Vy', 31004, 'Vz', 21004, 'My', 11004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171004, 71004, 171004, 1004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122004, 122004, 22004, 1004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171005, 0.0, 4.4, 3.375)
    ops.node(122005, 0.0, 4.4, 6.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1005, 171005, 122005, 0.1, 29786223.56417813, 12410926.48507422, 0.00127345, 0.00057292, 0.00146667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21005, 62.85409089, 0.00061041, 75.97317148, 0.04052181, 7.59731715, 0.12225258, -62.85409089, -0.00061041, -75.97317148, -0.04052181, -7.59731715, -0.12225258, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11005, 42.9047999, 0.00085895, 51.860009, 0.03463557, 5.1860009, 0.08964721, -42.9047999, -0.00085895, -51.860009, -0.03463557, -5.1860009, -0.08964721, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21005, 1005, 0.0, 133.37189095, 0.01220827, 133.37189095, 0.0366248, 93.36032367, -2122.22873121, 0.05, 2, 0, 71005, 22005, 2, 3)
    ops.uniaxialMaterial('LimitState', 41005, 33.34297274, 0.00010155, 100.02891822, 0.00030466, 333.42972738, 0.00101553, -33.34297274, -0.00010155, -100.02891822, -0.00030466, -333.42972738, -0.00101553, 0.4, 0.3, 0.003, 0.0, 0.0, 21005, 2)
    ops.limitCurve('ThreePoint', 11005, 1005, 0.0, 108.91021475, 0.01717895, 108.91021475, 0.05153686, 76.23715033, -1212.67220623, 0.05, 2, 0, 71005, 22005, 1, 3)
    ops.uniaxialMaterial('LimitState', 31005, 27.22755369, 8.293e-05, 81.68266106, 0.00024878, 272.27553688, 0.00082927, -27.22755369, -8.293e-05, -81.68266106, -0.00024878, -272.27553688, -0.00082927, 0.4, 0.3, 0.003, 0.0, 0.0, 11005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1005, 99999, 'P', 41005, 'Vy', 31005, 'Vz', 21005, 'My', 11005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171005, 71005, 171005, 1005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122005, 122005, 22005, 1005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171006, 3.1, 4.4, 3.375)
    ops.node(122006, 3.1, 4.4, 6.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1006, 171006, 122006, 0.2275, 28056698.06312323, 11690290.85963468, 0.00616035, 0.00255464, 0.00881089, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21006, 212.11412543, 0.00049184, 257.75960494, 0.05296467, 25.77596049, 0.14152567, -212.11412543, -0.00049184, -257.75960494, -0.05296467, -25.77596049, -0.14152567, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11006, 95.37163582, 0.0006731, 115.89494628, 0.04280735, 11.58949463, 0.09543134, -95.37163582, -0.0006731, -115.89494628, -0.04280735, -11.58949463, -0.09543134, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21006, 1006, 0.0, 328.8207852, 0.00983684, 328.8207852, 0.02951052, 230.17454964, -5456.91249415, 0.05, 2, 0, 71006, 22006, 2, 3)
    ops.uniaxialMaterial('LimitState', 41006, 82.2051963, 0.00011684, 246.6155889, 0.00035051, 822.05196299, 0.00116838, -82.2051963, -0.00011684, -246.6155889, -0.00035051, -822.05196299, -0.00116838, 0.4, 0.3, 0.003, 0.0, 0.0, 21006, 2)
    ops.limitCurve('ThreePoint', 11006, 1006, 0.0, 216.13795554, 0.01346201, 216.13795554, 0.04038604, 151.29656888, -2446.99238417, 0.05, 2, 0, 71006, 22006, 1, 3)
    ops.uniaxialMaterial('LimitState', 31006, 54.03448888, 7.68e-05, 162.10346665, 0.0002304, 540.34488885, 0.00076799, -54.03448888, -7.68e-05, -162.10346665, -0.0002304, -540.34488885, -0.00076799, 0.4, 0.3, 0.003, 0.0, 0.0, 11006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1006, 99999, 'P', 41006, 'Vy', 31006, 'Vz', 21006, 'My', 11006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171006, 71006, 171006, 1006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122006, 122006, 22006, 1006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171007, 7.35, 4.4, 3.375)
    ops.node(122007, 7.35, 4.4, 6.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1007, 171007, 122007, 0.3, 27242382.07450357, 11350992.53104316, 0.01066025, 0.0044, 0.01546875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21007, 295.97163058, 0.00048099, 360.55167208, 0.05068861, 36.05516721, 0.13062964, -295.97163058, -0.00048099, -360.55167208, -0.05068861, -36.05516721, -0.13062964, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11007, 128.6019278, 0.00062509, 156.66244772, 0.04103126, 15.66624477, 0.08878741, -128.6019278, -0.00062509, -156.66244772, -0.04103126, -15.66624477, -0.08878741, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21007, 1007, 0.0, 410.85499925, 0.00961981, 410.85499925, 0.02885944, 287.59849947, -5580.46969433, 0.05, 2, 0, 71007, 22007, 2, 3)
    ops.uniaxialMaterial('LimitState', 41007, 102.71374981, 0.00011402, 308.14124944, 0.00034205, 1027.13749812, 0.00114016, -102.71374981, -0.00011402, -308.14124944, -0.00034205, -1027.13749812, -0.00114016, 0.4, 0.3, 0.003, 0.0, 0.0, 21007, 2)
    ops.limitCurve('ThreePoint', 11007, 1007, 0.0, 250.27026194, 0.01250179, 250.27026194, 0.03750537, 175.18918335, -2517.79186238, 0.05, 2, 0, 71007, 22007, 1, 3)
    ops.uniaxialMaterial('LimitState', 31007, 62.56756548, 6.945e-05, 187.70269645, 0.00020836, 625.67565484, 0.00069452, -62.56756548, -6.945e-05, -187.70269645, -0.00020836, -625.67565484, -0.00069452, 0.4, 0.3, 0.003, 0.0, 0.0, 11007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1007, 99999, 'P', 41007, 'Vy', 31007, 'Vz', 21007, 'My', 11007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171007, 71007, 171007, 1007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122007, 122007, 22007, 1007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171008, 11.6, 4.4, 3.375)
    ops.node(122008, 11.6, 4.4, 6.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1008, 171008, 122008, 0.165, 28024539.16208893, 11676891.31753705, 0.00326155, 0.00136125, 0.00457531, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21008, 120.60766318, 0.00051257, 146.53566505, 0.05099756, 14.6535665, 0.15099756, -120.60766318, -0.00051257, -146.53566505, -0.05099756, -14.6535665, -0.15099756, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11008, 60.26080605, 0.00072591, 73.21555743, 0.04121672, 7.32155574, 0.10097079, -60.26080605, -0.00072591, -73.21555743, -0.04121672, -7.32155574, -0.10097079, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21008, 1008, 0.0, 229.50269757, 0.01025131, 229.50269757, 0.03075392, 160.6518883, -4454.51560599, 0.05, 2, 0, 71008, 22008, 2, 3)
    ops.uniaxialMaterial('LimitState', 41008, 57.37567439, 0.00011257, 172.12702318, 0.0003377, 573.75674393, 0.00112566, -57.37567439, -0.00011257, -172.12702318, -0.0003377, -573.75674393, -0.00112566, 0.4, 0.3, 0.003, 0.0, 0.0, 21008, 2)
    ops.limitCurve('ThreePoint', 11008, 1008, 0.0, 163.66222078, 0.01451823, 163.66222078, 0.0435547, 114.56355455, -1994.90936632, 0.05, 2, 0, 71008, 22008, 1, 3)
    ops.uniaxialMaterial('LimitState', 31008, 40.91555519, 8.027e-05, 122.74666558, 0.00024082, 409.15555195, 0.00080273, -40.91555519, -8.027e-05, -122.74666558, -0.00024082, -409.15555195, -0.00080273, 0.4, 0.3, 0.003, 0.0, 0.0, 11008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1008, 99999, 'P', 41008, 'Vy', 31008, 'Vz', 21008, 'My', 11008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171008, 71008, 171008, 1008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122008, 122008, 22008, 1008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171009, 0.0, 8.8, 3.375)
    ops.node(122009, 0.0, 8.8, 6.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1009, 171009, 122009, 0.1, 28680077.64586187, 11950032.35244245, 0.00127345, 0.00057292, 0.00146667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21009, 55.41804018, 0.00059061, 67.13964185, 0.04057017, 6.71396419, 0.12046169, -55.41804018, -0.00059061, -67.13964185, -0.04057017, -6.71396419, -0.12046169, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11009, 36.0576838, 0.00082043, 43.68433038, 0.03465473, 4.36843304, 0.0884284, -36.0576838, -0.00082043, -43.68433038, -0.03465473, -4.36843304, -0.0884284, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21009, 1009, 0.0, 128.93806889, 0.0118123, 128.93806889, 0.03543689, 90.25664822, -2113.29398437, 0.05, 2, 0, 71009, 22009, 2, 3)
    ops.uniaxialMaterial('LimitState', 41009, 32.23451722, 0.00010196, 96.70355167, 0.00030589, 322.34517223, 0.00101963, -32.23451722, -0.00010196, -96.70355167, -0.00030589, -322.34517223, -0.00101963, 0.4, 0.3, 0.003, 0.0, 0.0, 21009, 2)
    ops.limitCurve('ThreePoint', 11009, 1009, 0.0, 104.73431483, 0.01640851, 104.73431483, 0.04922553, 73.31402038, -1201.9230584, 0.05, 2, 0, 71009, 22009, 1, 3)
    ops.uniaxialMaterial('LimitState', 31009, 26.18357871, 8.282e-05, 78.55073613, 0.00024847, 261.83578709, 0.00082823, -26.18357871, -8.282e-05, -78.55073613, -0.00024847, -261.83578709, -0.00082823, 0.4, 0.3, 0.003, 0.0, 0.0, 11009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1009, 99999, 'P', 41009, 'Vy', 31009, 'Vz', 21009, 'My', 11009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171009, 71009, 171009, 1009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122009, 122009, 22009, 1009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171010, 3.1, 8.8, 3.375)
    ops.node(122010, 3.1, 8.8, 6.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1010, 171010, 122010, 0.2275, 29209679.05183822, 12170699.60493259, 0.00616035, 0.00255464, 0.00881089, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21010, 220.73488293, 0.00050031, 267.74289242, 0.05343939, 26.77428924, 0.14525187, -220.73488293, -0.00050031, -267.74289242, -0.05343939, -26.77428924, -0.14525187, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11010, 98.56011568, 0.00067895, 119.54961581, 0.04318759, 11.95496158, 0.09774365, -98.56011568, -0.00067895, -119.54961581, -0.04318759, -11.95496158, -0.09774365, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21010, 1010, 0.0, 342.26825236, 0.01000612, 342.26825236, 0.03001837, 239.58777666, -5868.33858312, 0.05, 2, 0, 71010, 22010, 2, 3)
    ops.uniaxialMaterial('LimitState', 41010, 85.56706309, 0.00011682, 256.70118927, 0.00035045, 855.67063091, 0.00116816, -85.56706309, -0.00011682, -256.70118927, -0.00035045, -855.67063091, -0.00116816, 0.4, 0.3, 0.003, 0.0, 0.0, 21010, 2)
    ops.limitCurve('ThreePoint', 11010, 1010, 0.0, 225.21102978, 0.01357905, 225.21102978, 0.04073716, 157.64772085, -2568.27162287, 0.05, 2, 0, 71010, 22010, 1, 3)
    ops.uniaxialMaterial('LimitState', 31010, 56.30275745, 7.686e-05, 168.90827234, 0.00023059, 563.02757445, 0.00076864, -56.30275745, -7.686e-05, -168.90827234, -0.00023059, -563.02757445, -0.00076864, 0.4, 0.3, 0.003, 0.0, 0.0, 11010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1010, 99999, 'P', 41010, 'Vy', 31010, 'Vz', 21010, 'My', 11010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171010, 71010, 171010, 1010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122010, 122010, 22010, 1010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171011, 7.35, 8.8, 3.375)
    ops.node(122011, 7.35, 8.8, 6.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1011, 171011, 122011, 0.3, 27916710.31017665, 11631962.62924027, 0.01066025, 0.0044, 0.01546875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21011, 301.80828297, 0.00047959, 367.25512489, 0.05001843, 36.72551249, 0.1312229, -301.80828297, -0.00047959, -367.25512489, -0.05001843, -36.72551249, -0.1312229, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11011, 130.89662304, 0.00061691, 159.28143246, 0.04048487, 15.92814325, 0.08899579, -130.89662304, -0.00061691, -159.28143246, -0.04048487, -15.92814325, -0.08899579, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21011, 1011, 0.0, 417.05339358, 0.00959172, 417.05339358, 0.02877515, 291.9373755, -5463.38364348, 0.05, 2, 0, 71011, 22011, 2, 3)
    ops.uniaxialMaterial('LimitState', 41011, 104.26334839, 0.00011294, 312.79004518, 0.00033882, 1042.63348394, 0.0011294, -104.26334839, -0.00011294, -312.79004518, -0.00033882, -1042.63348394, -0.0011294, 0.4, 0.3, 0.003, 0.0, 0.0, 21011, 2)
    ops.limitCurve('ThreePoint', 11011, 1011, 0.0, 254.64073915, 0.01233824, 254.64073915, 0.03701472, 178.2485174, -2474.60915235, 0.05, 2, 0, 71011, 22011, 1, 3)
    ops.uniaxialMaterial('LimitState', 31011, 63.66018479, 6.896e-05, 190.98055436, 0.00020687, 636.60184787, 0.00068958, -63.66018479, -6.896e-05, -190.98055436, -0.00020687, -636.60184787, -0.00068958, 0.4, 0.3, 0.003, 0.0, 0.0, 11011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1011, 99999, 'P', 41011, 'Vy', 31011, 'Vz', 21011, 'My', 11011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171011, 71011, 171011, 1011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122011, 122011, 22011, 1011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171012, 11.6, 8.8, 3.375)
    ops.node(122012, 11.6, 8.8, 6.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1012, 171012, 122012, 0.165, 29991765.57221067, 12496568.98842111, 0.00326155, 0.00136125, 0.00457531, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21012, 121.10496263, 0.00051231, 146.57061156, 0.05085589, 14.65706116, 0.15085589, -121.10496263, -0.00051231, -146.57061156, -0.05085589, -14.65706116, -0.15085589, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11012, 60.52790954, 0.00073055, 73.25556712, 0.04110794, 7.32555671, 0.10356844, -60.52790954, -0.00073055, -73.25556712, -0.04110794, -7.32555671, -0.10356844, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21012, 1012, 0.0, 241.26654493, 0.0102462, 241.26654493, 0.03073859, 168.88658145, -4518.49270328, 0.05, 2, 0, 71012, 22012, 2, 3)
    ops.uniaxialMaterial('LimitState', 41012, 60.31663623, 0.00011057, 180.94990869, 0.00033172, 603.16636231, 0.00110574, -60.31663623, -0.00011057, -180.94990869, -0.00033172, -603.16636231, -0.00110574, 0.4, 0.3, 0.003, 0.0, 0.0, 21012, 2)
    ops.limitCurve('ThreePoint', 11012, 1012, 0.0, 173.80570824, 0.01461096, 173.80570824, 0.04383287, 121.66399577, -2017.50988467, 0.05, 2, 0, 71012, 22012, 1, 3)
    ops.uniaxialMaterial('LimitState', 31012, 43.45142706, 7.966e-05, 130.35428118, 0.00023897, 434.5142706, 0.00079656, -43.45142706, -7.966e-05, -130.35428118, -0.00023897, -434.5142706, -0.00079656, 0.4, 0.3, 0.003, 0.0, 0.0, 11012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1012, 99999, 'P', 41012, 'Vy', 31012, 'Vz', 21012, 'My', 11012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171012, 71012, 171012, 1012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122012, 122012, 22012, 1012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171013, 0.0, 13.2, 3.375)
    ops.node(122013, 0.0, 13.2, 6.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1013, 171013, 122013, 0.1, 29277024.7654951, 12198760.31895629, 0.00127345, 0.00057292, 0.00146667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21013, 55.35189483, 0.00061263, 66.98834223, 0.03664952, 6.69883422, 0.11788751, -55.35189483, -0.00061263, -66.98834223, -0.03664952, -6.69883422, -0.11788751, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11013, 35.52028858, 0.00087637, 42.98760241, 0.03137404, 4.29876024, 0.08605399, -35.52028858, -0.00087637, -42.98760241, -0.03137404, -4.29876024, -0.08605399, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21013, 1013, 0.0, 118.08652153, 0.01225263, 118.08652153, 0.03675789, 82.66056507, -1605.81450116, 0.05, 2, 0, 71013, 22013, 2, 3)
    ops.uniaxialMaterial('LimitState', 41013, 29.52163038, 9.148e-05, 88.56489115, 0.00027443, 295.21630383, 0.00091478, -29.52163038, -9.148e-05, -88.56489115, -0.00027443, -295.21630383, -0.00091478, 0.4, 0.3, 0.003, 0.0, 0.0, 21013, 2)
    ops.limitCurve('ThreePoint', 11013, 1013, 0.0, 98.61937894, 0.0175275, 98.61937894, 0.05258249, 69.03356526, -959.91752035, 0.05, 2, 0, 71013, 22013, 1, 3)
    ops.uniaxialMaterial('LimitState', 31013, 24.65484474, 7.64e-05, 73.96453421, 0.00022919, 246.54844736, 0.00076397, -24.65484474, -7.64e-05, -73.96453421, -0.00022919, -246.54844736, -0.00076397, 0.4, 0.3, 0.003, 0.0, 0.0, 11013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1013, 99999, 'P', 41013, 'Vy', 31013, 'Vz', 21013, 'My', 11013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171013, 71013, 171013, 1013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122013, 122013, 22013, 1013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171014, 3.1, 13.2, 3.375)
    ops.node(122014, 3.1, 13.2, 6.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1014, 171014, 122014, 0.2275, 29374815.93712174, 12239506.64046739, 0.00616035, 0.00255464, 0.00881089, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21014, 215.14884766, 0.00049256, 260.87542537, 0.05197838, 26.08754254, 0.14408776, -215.14884766, -0.00049256, -260.87542537, -0.05197838, -26.08754254, -0.14408776, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11014, 96.30974125, 0.00066797, 116.77889512, 0.04200968, 11.67788951, 0.09674216, -96.30974125, -0.00066797, -116.77889512, -0.04200968, -11.67788951, -0.09674216, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21014, 1014, 0.0, 333.25439116, 0.00985111, 333.25439116, 0.02955332, 233.27807381, -5301.56826442, 0.05, 2, 0, 71014, 22014, 2, 3)
    ops.uniaxialMaterial('LimitState', 41014, 83.31359779, 0.0001131, 249.94079337, 0.0003393, 833.13597789, 0.001131, -83.31359779, -0.0001131, -249.94079337, -0.0003393, -833.13597789, -0.001131, 0.4, 0.3, 0.003, 0.0, 0.0, 21014, 2)
    ops.limitCurve('ThreePoint', 11014, 1014, 0.0, 220.67866775, 0.01335938, 220.67866775, 0.04007814, 154.47506743, -2365.423386, 0.05, 2, 0, 71014, 22014, 1, 3)
    ops.uniaxialMaterial('LimitState', 31014, 55.16966694, 7.489e-05, 165.50900081, 0.00022468, 551.69666938, 0.00074894, -55.16966694, -7.489e-05, -165.50900081, -0.00022468, -551.69666938, -0.00074894, 0.4, 0.3, 0.003, 0.0, 0.0, 11014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1014, 99999, 'P', 41014, 'Vy', 31014, 'Vz', 21014, 'My', 11014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171014, 71014, 171014, 1014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122014, 122014, 22014, 1014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171015, 7.35, 13.2, 3.375)
    ops.node(122015, 7.35, 13.2, 6.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1015, 171015, 122015, 0.3, 28849840.55794065, 12020766.89914194, 0.01066025, 0.0044, 0.01546875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21015, 294.96283131, 0.0004664, 358.28264601, 0.05205153, 35.8282646, 0.13478188, -294.96283131, -0.0004664, -358.28264601, -0.05205153, -35.8282646, -0.13478188, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11015, 128.3545149, 0.00059179, 155.90844115, 0.04210655, 15.59084412, 0.09152903, -128.3545149, -0.00059179, -155.90844115, -0.04210655, -15.59084412, -0.09152903, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21015, 1015, 0.0, 453.11101761, 0.00932805, 453.11101761, 0.02798414, 317.17771233, -6697.92739012, 0.05, 2, 0, 71015, 22015, 2, 3)
    ops.uniaxialMaterial('LimitState', 41015, 113.2777544, 0.00011874, 339.83326321, 0.00035621, 1132.77754403, 0.00118736, -113.2777544, -0.00011874, -339.83326321, -0.00035621, -1132.77754403, -0.00118736, 0.4, 0.3, 0.003, 0.0, 0.0, 21015, 2)
    ops.limitCurve('ThreePoint', 11015, 1015, 0.0, 275.38804974, 0.01183585, 275.38804974, 0.03550755, 192.77163482, -2913.05552285, 0.05, 2, 0, 71015, 22015, 1, 3)
    ops.uniaxialMaterial('LimitState', 31015, 68.84701243, 7.216e-05, 206.5410373, 0.00021649, 688.47012434, 0.00072164, -68.84701243, -7.216e-05, -206.5410373, -0.00021649, -688.47012434, -0.00072164, 0.4, 0.3, 0.003, 0.0, 0.0, 11015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1015, 99999, 'P', 41015, 'Vy', 31015, 'Vz', 21015, 'My', 11015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171015, 71015, 171015, 1015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122015, 122015, 22015, 1015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171016, 11.6, 13.2, 3.375)
    ops.node(122016, 11.6, 13.2, 6.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1016, 171016, 122016, 0.165, 30830255.90546865, 12845939.96061194, 0.00326155, 0.00136125, 0.00457531, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21016, 122.06118879, 0.00050129, 147.42665356, 0.05198451, 14.74266536, 0.15198451, -122.06118879, -0.00050129, -147.42665356, -0.05198451, -14.74266536, -0.15198451, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11016, 61.16362111, 0.00069898, 73.87399771, 0.04199039, 7.38739977, 0.10540631, -61.16362111, -0.00069898, -73.87399771, -0.04199039, -7.38739977, -0.10540631, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21016, 1016, 0.0, 261.63508288, 0.01002578, 261.63508288, 0.03007735, 183.14455802, -5417.33563974, 0.05, 2, 0, 71016, 22016, 2, 3)
    ops.uniaxialMaterial('LimitState', 41016, 65.40877072, 0.00011665, 196.22631216, 0.00034994, 654.08770721, 0.00116648, -65.40877072, -0.00011665, -196.22631216, -0.00034994, -654.08770721, -0.00116648, 0.4, 0.3, 0.003, 0.0, 0.0, 21016, 2)
    ops.limitCurve('ThreePoint', 11016, 1016, 0.0, 186.5566186, 0.01397951, 186.5566186, 0.04193854, 130.58963302, -2342.38926225, 0.05, 2, 0, 71016, 22016, 1, 3)
    ops.uniaxialMaterial('LimitState', 31016, 46.63915465, 8.317e-05, 139.91746395, 0.00024952, 466.3915465, 0.00083175, -46.63915465, -8.317e-05, -139.91746395, -0.00024952, -466.3915465, -0.00083175, 0.4, 0.3, 0.003, 0.0, 0.0, 11016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1016, 99999, 'P', 41016, 'Vy', 31016, 'Vz', 21016, 'My', 11016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171016, 71016, 171016, 1016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122016, 122016, 22016, 1016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171017, 0.0, 17.6, 3.375)
    ops.node(122017, 0.0, 17.6, 6.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1017, 171017, 122017, 0.1, 29709425.23400282, 12378927.18083451, 0.00127345, 0.00057292, 0.00146667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21017, 54.89838786, 0.00062046, 66.38316281, 0.03984919, 6.63831628, 0.12200337, -54.89838786, -0.00062046, -66.38316281, -0.03984919, -6.63831628, -0.12200337, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11017, 34.98810866, 0.00090377, 42.30764153, 0.03410266, 4.23076415, 0.08939929, -34.98810866, -0.00090377, -42.30764153, -0.03410266, -4.23076415, -0.08939929, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21017, 1017, 0.0, 131.30904904, 0.01240922, 131.30904904, 0.03722765, 91.91633433, -2082.89813741, 0.05, 2, 0, 71017, 22017, 2, 3)
    ops.uniaxialMaterial('LimitState', 41017, 32.82726226, 0.00010024, 98.48178678, 0.00030072, 328.2726226, 0.00100241, -32.82726226, -0.00010024, -98.48178678, -0.00030072, -328.2726226, -0.00100241, 0.4, 0.3, 0.003, 0.0, 0.0, 21017, 2)
    ops.limitCurve('ThreePoint', 11017, 1017, 0.0, 107.37176, 0.01807546, 107.37176, 0.05422638, 75.160232, -1187.58725838, 0.05, 2, 0, 71017, 22017, 1, 3)
    ops.uniaxialMaterial('LimitState', 31017, 26.84294, 8.197e-05, 80.52882, 0.0002459, 268.42940001, 0.00081967, -26.84294, -8.197e-05, -80.52882, -0.0002459, -268.42940001, -0.00081967, 0.4, 0.3, 0.003, 0.0, 0.0, 11017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1017, 99999, 'P', 41017, 'Vy', 31017, 'Vz', 21017, 'My', 11017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171017, 71017, 171017, 1017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122017, 122017, 22017, 1017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171018, 3.1, 17.6, 3.375)
    ops.node(122018, 3.1, 17.6, 6.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1018, 171018, 122018, 0.2275, 27667178.2657157, 11527990.94404821, 0.00616035, 0.00255464, 0.00881089, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21018, 204.44980914, 0.00048898, 248.70008012, 0.05248831, 24.87000801, 0.14119815, -204.44980914, -0.00048898, -248.70008012, -0.05248831, -24.87000801, -0.14119815, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11018, 91.805797, 0.00067185, 111.67586395, 0.04242589, 11.1675864, 0.09513832, -91.805797, -0.00067185, -111.67586395, -0.04242589, -11.1675864, -0.09513832, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21018, 1018, 0.0, 316.79080871, 0.00977962, 316.79080871, 0.02933887, 221.7535661, -5221.66717849, 0.05, 2, 0, 71018, 22018, 2, 3)
    ops.uniaxialMaterial('LimitState', 41018, 79.19770218, 0.00011415, 237.59310653, 0.00034244, 791.97702178, 0.00114148, -79.19770218, -0.00011415, -237.59310653, -0.00034244, -791.97702178, -0.00114148, 0.4, 0.3, 0.003, 0.0, 0.0, 21018, 2)
    ops.limitCurve('ThreePoint', 11018, 1018, 0.0, 208.54519635, 0.01343694, 208.54519635, 0.04031083, 145.98163744, -2336.66402886, 0.05, 2, 0, 71018, 22018, 1, 3)
    ops.uniaxialMaterial('LimitState', 31018, 52.13629909, 7.514e-05, 156.40889726, 0.00022543, 521.36299087, 0.00075144, -52.13629909, -7.514e-05, -156.40889726, -0.00022543, -521.36299087, -0.00075144, 0.4, 0.3, 0.003, 0.0, 0.0, 11018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1018, 99999, 'P', 41018, 'Vy', 31018, 'Vz', 21018, 'My', 11018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171018, 71018, 171018, 1018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122018, 122018, 22018, 1018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171019, 7.35, 17.6, 3.375)
    ops.node(122019, 7.35, 17.6, 6.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1019, 171019, 122019, 0.3, 30293828.9700036, 12622428.7375015, 0.01066025, 0.0044, 0.01546875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21019, 302.43697351, 0.0004765, 366.14889888, 0.05026437, 36.61488989, 0.13501671, -302.43697351, -0.0004765, -366.14889888, -0.05026437, -36.61488989, -0.13501671, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11019, 131.73625546, 0.00061404, 159.4880557, 0.0406824, 15.94880557, 0.09131279, -131.73625546, -0.00061404, -159.4880557, -0.0406824, -15.94880557, -0.09131279, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21019, 1019, 0.0, 463.54883341, 0.00953005, 463.54883341, 0.02859014, 324.48418339, -6207.04397768, 0.05, 2, 0, 71019, 22019, 2, 3)
    ops.uniaxialMaterial('LimitState', 41019, 115.88720835, 0.00011568, 347.66162506, 0.00034704, 1158.87208353, 0.00115681, -115.88720835, -0.00011568, -347.66162506, -0.00034704, -1158.87208353, -0.00115681, 0.4, 0.3, 0.003, 0.0, 0.0, 21019, 2)
    ops.limitCurve('ThreePoint', 11019, 1019, 0.0, 283.3619907, 0.01228087, 283.3619907, 0.03684262, 198.35339349, -2739.77132368, 0.05, 2, 0, 71019, 22019, 1, 3)
    ops.uniaxialMaterial('LimitState', 31019, 70.84049767, 7.071e-05, 212.52149302, 0.00021214, 708.40497674, 0.00070715, -70.84049767, -7.071e-05, -212.52149302, -0.00021214, -708.40497674, -0.00070715, 0.4, 0.3, 0.003, 0.0, 0.0, 11019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1019, 99999, 'P', 41019, 'Vy', 31019, 'Vz', 21019, 'My', 11019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171019, 71019, 171019, 1019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122019, 122019, 22019, 1019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171020, 11.6, 17.6, 3.375)
    ops.node(122020, 11.6, 17.6, 6.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1020, 171020, 122020, 0.165, 32711214.44554438, 13629672.68564349, 0.00326155, 0.00136125, 0.00457531, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21020, 119.566707, 0.00048433, 143.63733936, 0.04923435, 14.36373394, 0.14923435, -119.566707, -0.00048433, -143.63733936, -0.04923435, -14.36373394, -0.14923435, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11020, 60.06399297, 0.00066691, 72.15580623, 0.0397662, 7.21558062, 0.10499907, -60.06399297, -0.00066691, -72.15580623, -0.0397662, -7.21558062, -0.10499907, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21020, 1020, 0.0, 255.99443495, 0.00968667, 255.99443495, 0.02906001, 179.19610447, -4475.52256567, 0.05, 2, 0, 71020, 22020, 2, 3)
    ops.uniaxialMaterial('LimitState', 41020, 63.99860874, 0.00010757, 191.99582622, 0.00032271, 639.98608739, 0.0010757, -63.99860874, -0.00010757, -191.99582622, -0.00032271, -639.98608739, -0.0010757, 0.4, 0.3, 0.003, 0.0, 0.0, 21020, 2)
    ops.limitCurve('ThreePoint', 11020, 1020, 0.0, 187.26039704, 0.01333813, 187.26039704, 0.04001439, 131.08227793, -2001.84140364, 0.05, 2, 0, 71020, 22020, 1, 3)
    ops.uniaxialMaterial('LimitState', 31020, 46.81509926, 7.869e-05, 140.44529778, 0.00023606, 468.15099261, 0.00078688, -46.81509926, -7.869e-05, -140.44529778, -0.00023606, -468.15099261, -0.00078688, 0.4, 0.3, 0.003, 0.0, 0.0, 11020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1020, 99999, 'P', 41020, 'Vy', 31020, 'Vz', 21020, 'My', 11020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171020, 71020, 171020, 1020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122020, 122020, 22020, 1020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171021, 0.0, 22.0, 3.4)
    ops.node(122021, 0.0, 22.0, 6.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1021, 171021, 122021, 0.0625, 29351725.96147385, 12229885.81728077, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21021, 22.24664053, 0.00084512, 26.93767075, 0.02360813, 2.69376708, 0.07769847, -22.24664053, -0.00084512, -26.93767075, -0.02360813, -2.69376708, -0.07769847, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11021, 22.24664053, 0.00084512, 26.93767075, 0.02360813, 2.69376708, 0.07769847, -22.24664053, -0.00084512, -26.93767075, -0.02360813, -2.69376708, -0.07769847, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21021, 1021, 0.0, 63.52631472, 0.01690233, 63.52631472, 0.050707, 44.4684203, -677.27464627, 0.05, 2, 0, 71021, 22021, 2, 3)
    ops.uniaxialMaterial('LimitState', 41021, 15.88157868, 7.854e-05, 47.64473604, 0.00023562, 158.8157868, 0.00078539, -15.88157868, -7.854e-05, -47.64473604, -0.00023562, -158.8157868, -0.00078539, 0.4, 0.3, 0.003, 0.0, 0.0, 21021, 2)
    ops.limitCurve('ThreePoint', 11021, 1021, 0.0, 63.52631472, 0.01690233, 63.52631472, 0.050707, 44.4684203, -677.27464627, 0.05, 2, 0, 71021, 22021, 1, 3)
    ops.uniaxialMaterial('LimitState', 31021, 15.88157868, 7.854e-05, 47.64473604, 0.00023562, 158.8157868, 0.00078539, -15.88157868, -7.854e-05, -47.64473604, -0.00023562, -158.8157868, -0.00078539, 0.4, 0.3, 0.003, 0.0, 0.0, 11021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1021, 99999, 'P', 41021, 'Vy', 31021, 'Vz', 21021, 'My', 11021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171021, 71021, 171021, 1021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122021, 122021, 22021, 1021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171022, 3.1, 22.0, 3.4)
    ops.node(122022, 3.1, 22.0, 6.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1022, 171022, 122022, 0.1575, 31588365.65630184, 13161819.0234591, 0.00337604, 0.00292359, 0.00176859, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21022, 85.50175281, 0.00064467, 103.11009562, 0.04867681, 10.31100956, 0.12571866, -85.50175281, -0.00064467, -103.11009562, -0.04867681, -10.31100956, -0.12571866, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11022, 98.51779569, 0.00055536, 118.80667939, 0.05321136, 11.88066794, 0.14902137, -98.51779569, -0.00055536, -118.80667939, -0.05321136, -11.88066794, -0.14902137, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21022, 1022, 0.0, 194.59448587, 0.01289338, 194.59448587, 0.03868015, 136.21614011, -2961.93521752, 0.05, 2, 0, 71022, 22022, 2, 3)
    ops.uniaxialMaterial('LimitState', 41022, 48.64862147, 8.871e-05, 145.9458644, 0.00026613, 486.48621468, 0.00088709, -48.64862147, -8.871e-05, -145.9458644, -0.00026613, -486.48621468, -0.00088709, 0.4, 0.3, 0.003, 0.0, 0.0, 21022, 2)
    ops.limitCurve('ThreePoint', 11022, 1022, 0.0, 219.03919208, 0.01110726, 219.03919208, 0.03332177, 153.32743446, -4246.78839268, 0.05, 2, 0, 71022, 22022, 1, 3)
    ops.uniaxialMaterial('LimitState', 31022, 54.75979802, 9.985e-05, 164.27939406, 0.00029956, 547.5979802, 0.00099852, -54.75979802, -9.985e-05, -164.27939406, -0.00029956, -547.5979802, -0.00099852, 0.4, 0.3, 0.003, 0.0, 0.0, 11022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1022, 99999, 'P', 41022, 'Vy', 31022, 'Vz', 21022, 'My', 11022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171022, 71022, 171022, 1022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122022, 122022, 22022, 1022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171023, 7.35, 22.0, 3.4)
    ops.node(122023, 7.35, 22.0, 6.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1023, 171023, 122023, 0.22, 28641774.63244529, 11934072.76351887, 0.00648267, 0.00610042, 0.00322667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21023, 98.93668991, 0.00058766, 120.27276341, 0.04690055, 12.02727634, 0.1106053, -98.93668991, -0.00058766, -120.27276341, -0.04690055, -12.02727634, -0.1106053, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11023, 161.013676, 0.00050634, 195.73688767, 0.05237855, 19.57368877, 0.13573835, -161.013676, -0.00050634, -195.73688767, -0.05237855, -19.57368877, -0.13573835, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21023, 1023, 0.0, 222.3824196, 0.01175318, 222.3824196, 0.03525955, 155.66769372, -3130.2010821, 0.05, 2, 0, 71023, 22023, 2, 3)
    ops.uniaxialMaterial('LimitState', 41023, 55.5956049, 8.004e-05, 166.7868147, 0.00024013, 555.95604899, 0.00080043, -55.5956049, -8.004e-05, -166.7868147, -0.00024013, -555.95604899, -0.00080043, 0.4, 0.3, 0.003, 0.0, 0.0, 21023, 2)
    ops.limitCurve('ThreePoint', 11023, 1023, 0.0, 272.48517025, 0.0101269, 272.48517025, 0.03038069, 190.73961917, -4910.78068375, 0.05, 2, 0, 71023, 22023, 1, 3)
    ops.uniaxialMaterial('LimitState', 31023, 68.12129256, 9.808e-05, 204.36387769, 0.00029423, 681.21292562, 0.00098076, -68.12129256, -9.808e-05, -204.36387769, -0.00029423, -681.21292562, -0.00098076, 0.4, 0.3, 0.003, 0.0, 0.0, 11023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1023, 99999, 'P', 41023, 'Vy', 31023, 'Vz', 21023, 'My', 11023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171023, 71023, 171023, 1023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122023, 122023, 22023, 1023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171024, 11.6, 22.0, 3.4)
    ops.node(122024, 11.6, 22.0, 6.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1024, 171024, 122024, 0.105, 29651021.27614199, 12354592.1983925, 0.00152551, 0.00117906, 0.00086625, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21024, 47.04446596, 0.00075878, 57.01619159, 0.03704042, 5.70161916, 0.10272513, -47.04446596, -0.00075878, -57.01619159, -0.03704042, -5.70161916, -0.10272513, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11024, 48.96923563, 0.0006761, 59.34894283, 0.03899205, 5.93489428, 0.1137514, -48.96923563, -0.0006761, -59.34894283, -0.03899205, -5.93489428, -0.1137514, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21024, 1024, 0.0, 113.12564187, 0.01517567, 113.12564187, 0.04552702, 79.18794931, -1511.17127977, 0.05, 2, 0, 71024, 22024, 2, 3)
    ops.uniaxialMaterial('LimitState', 41024, 28.28141047, 8.241e-05, 84.8442314, 0.00024723, 282.81410468, 0.00082409, -28.28141047, -8.241e-05, -84.8442314, -0.00024723, -282.81410468, -0.00082409, 0.4, 0.3, 0.003, 0.0, 0.0, 21024, 2)
    ops.limitCurve('ThreePoint', 11024, 1024, 0.0, 120.9023821, 0.01352202, 120.9023821, 0.04056605, 84.63166747, -1854.88321688, 0.05, 2, 0, 71024, 22024, 1, 3)
    ops.uniaxialMaterial('LimitState', 31024, 30.22559553, 8.807e-05, 90.67678658, 0.00026422, 302.25595526, 0.00088074, -30.22559553, -8.807e-05, -90.67678658, -0.00026422, -302.25595526, -0.00088074, 0.4, 0.3, 0.003, 0.0, 0.0, 11024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1024, 99999, 'P', 41024, 'Vy', 31024, 'Vz', 21024, 'My', 11024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171024, 71024, 171024, 1024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122024, 122024, 22024, 1024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172003, 7.35, 0.0, 6.525)
    ops.node(123003, 7.35, 0.0, 9.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2003, 172003, 123003, 0.125, 29031822.8264651, 12096592.84436046, 0.00178813, 0.00286458, 0.00071615, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22003, 45.63229924, 0.00089176, 55.40962887, 0.03609845, 5.54096289, 0.08575402, -45.63229924, -0.00089176, -55.40962887, -0.03609845, -5.54096289, -0.08575402, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12003, 89.99845317, 0.00054805, 109.28182389, 0.04534386, 10.92818239, 0.13326995, -89.99845317, -0.00054805, -109.28182389, -0.04534386, -10.92818239, -0.13326995, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22003, 2003, 0.0, 109.38313938, 0.01783513, 109.38313938, 0.0535054, 76.56819756, -1010.38418138, 0.05, 2, 0, 72003, 23003, 2, 3)
    ops.uniaxialMaterial('LimitState', 42003, 27.34578484, 6.836e-05, 82.03735453, 0.00020508, 273.45784844, 0.00068361, -27.34578484, -6.836e-05, -82.03735453, -0.00020508, -273.45784844, -0.00068361, 0.4, 0.3, 0.003, 0.0, 0.0, 22003, 2)
    ops.limitCurve('ThreePoint', 12003, 2003, 0.0, 144.37112823, 0.0109611, 144.37112823, 0.03288329, 101.05978976, -2435.89938488, 0.05, 2, 0, 72003, 23003, 1, 3)
    ops.uniaxialMaterial('LimitState', 32003, 36.09278206, 9.023e-05, 108.27834617, 0.00027068, 360.92782058, 0.00090228, -36.09278206, -9.023e-05, -108.27834617, -0.00027068, -360.92782058, -0.00090228, 0.4, 0.3, 0.003, 0.0, 0.0, 12003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2003, 99999, 'P', 42003, 'Vy', 32003, 'Vz', 22003, 'My', 12003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172003, 72003, 172003, 2003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123003, 123003, 23003, 2003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172004, 11.6, 0.0, 6.525)
    ops.node(123004, 11.6, 0.0, 9.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2004, 172004, 123004, 0.0625, 29072619.35094796, 12113591.39622832, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22004, 20.44229113, 0.00085708, 24.80419372, 0.02719421, 2.48041937, 0.08342062, -20.44229113, -0.00085708, -24.80419372, -0.02719421, -2.48041937, -0.08342062, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12004, 20.44229113, 0.00085708, 24.80419372, 0.02719421, 2.48041937, 0.08342062, -20.44229113, -0.00085708, -24.80419372, -0.02719421, -2.48041937, -0.08342062, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22004, 2004, 0.0, 64.11746174, 0.01714154, 64.11746174, 0.05142461, 44.88222322, -804.55794151, 0.05, 2, 0, 72004, 23004, 2, 3)
    ops.uniaxialMaterial('LimitState', 42004, 16.02936544, 8.003e-05, 48.08809631, 0.00024009, 160.29365435, 0.0008003, -16.02936544, -8.003e-05, -48.08809631, -0.00024009, -160.29365435, -0.0008003, 0.4, 0.3, 0.003, 0.0, 0.0, 22004, 2)
    ops.limitCurve('ThreePoint', 12004, 2004, 0.0, 64.11746174, 0.01714154, 64.11746174, 0.05142461, 44.88222322, -804.55794151, 0.05, 2, 0, 72004, 23004, 1, 3)
    ops.uniaxialMaterial('LimitState', 32004, 16.02936544, 8.003e-05, 48.08809631, 0.00024009, 160.29365435, 0.0008003, -16.02936544, -8.003e-05, -48.08809631, -0.00024009, -160.29365435, -0.0008003, 0.4, 0.3, 0.003, 0.0, 0.0, 12004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2004, 99999, 'P', 42004, 'Vy', 32004, 'Vz', 22004, 'My', 12004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172004, 72004, 172004, 2004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123004, 123004, 23004, 2004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172005, 0.0, 4.4, 6.525)
    ops.node(123005, 0.0, 4.4, 9.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2005, 172005, 123005, 0.0875, 30722261.99766035, 12800942.49902515, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22005, 42.5055063, 0.00064045, 51.36692533, 0.02209544, 5.13669253, 0.07964096, -42.5055063, -0.00064045, -51.36692533, -0.02209544, -5.13669253, -0.07964096, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12005, 27.34708165, 0.00083749, 33.04831829, 0.02007739, 3.30483183, 0.06451499, -27.34708165, -0.00083749, -33.04831829, -0.02007739, -3.30483183, -0.06451499, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22005, 2005, 0.0, 86.83425285, 0.01280891, 86.83425285, 0.03842673, 60.78397699, -841.4081723, 0.05, 2, 0, 72005, 23005, 2, 3)
    ops.uniaxialMaterial('LimitState', 42005, 21.70856321, 7.326e-05, 65.12568964, 0.00021978, 217.08563212, 0.00073261, -21.70856321, -7.326e-05, -65.12568964, -0.00021978, -217.08563212, -0.00073261, 0.4, 0.3, 0.003, 0.0, 0.0, 22005, 2)
    ops.limitCurve('ThreePoint', 12005, 2005, 0.0, 74.45027225, 0.01674978, 74.45027225, 0.05024935, 52.11519057, -595.22527493, 0.05, 2, 0, 72005, 23005, 1, 3)
    ops.uniaxialMaterial('LimitState', 32005, 18.61256806, 6.281e-05, 55.83770419, 0.00018844, 186.12568062, 0.00062813, -18.61256806, -6.281e-05, -55.83770419, -0.00018844, -186.12568062, -0.00062813, 0.4, 0.3, 0.003, 0.0, 0.0, 12005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2005, 99999, 'P', 42005, 'Vy', 32005, 'Vz', 22005, 'My', 12005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172005, 72005, 172005, 2005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123005, 123005, 23005, 2005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172006, 3.1, 4.4, 6.525)
    ops.node(123006, 3.1, 4.4, 9.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2006, 172006, 123006, 0.1375, 29509492.97083487, 12295622.07118119, 0.00204719, 0.00078776, 0.00381276, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22006, 110.735832, 0.00052508, 134.1413266, 0.04604058, 13.41413266, 0.1312263, -110.735832, -0.00052508, -134.1413266, -0.04604058, -13.41413266, -0.1312263, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12006, 44.55775092, 0.0008983, 53.97562569, 0.03559926, 5.39756257, 0.08035947, -44.55775092, -0.0008983, -53.97562569, -0.03559926, -5.39756257, -0.08035947, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22006, 2006, 0.0, 189.60808732, 0.01050157, 189.60808732, 0.0315047, 132.72566112, -3214.43671656, 0.05, 2, 0, 72006, 23006, 2, 3)
    ops.uniaxialMaterial('LimitState', 42006, 47.40202183, 0.00010598, 142.20606549, 0.00031795, 474.02021829, 0.00105983, -47.40202183, -0.00010598, -142.20606549, -0.00031795, -474.02021829, -0.00105983, 0.4, 0.3, 0.003, 0.0, 0.0, 22006, 2)
    ops.limitCurve('ThreePoint', 12006, 2006, 0.0, 129.74646899, 0.0179661, 129.74646899, 0.0538983, 90.82252829, -1220.67024885, 0.05, 2, 0, 72006, 23006, 1, 3)
    ops.uniaxialMaterial('LimitState', 32006, 32.43661725, 7.252e-05, 97.30985174, 0.00021757, 324.36617248, 0.00072523, -32.43661725, -7.252e-05, -97.30985174, -0.00021757, -324.36617248, -0.00072523, 0.4, 0.3, 0.003, 0.0, 0.0, 12006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2006, 99999, 'P', 42006, 'Vy', 32006, 'Vz', 22006, 'My', 12006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172006, 72006, 172006, 2006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123006, 123006, 23006, 2006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172007, 7.35, 4.4, 6.525)
    ops.node(123007, 7.35, 4.4, 9.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2007, 172007, 123007, 0.2275, 32469025.9492538, 13528760.81218908, 0.00616035, 0.00255464, 0.00881089, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22007, 194.30876928, 0.00048288, 233.9321569, 0.03917927, 23.39321569, 0.10963946, -194.30876928, -0.00048288, -233.9321569, -0.03917927, -23.39321569, -0.10963946, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12007, 87.05221818, 0.00064561, 104.80388115, 0.03226984, 10.48038812, 0.0759243, -87.05221818, -0.00064561, -104.80388115, -0.03226984, -10.48038812, -0.0759243, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22007, 2007, 0.0, 306.35379732, 0.00965752, 306.35379732, 0.02897257, 214.44765812, -3442.10413333, 0.05, 2, 0, 72007, 23007, 2, 3)
    ops.uniaxialMaterial('LimitState', 42007, 76.58844933, 9.406e-05, 229.76534799, 0.00028219, 765.88449329, 0.00094062, -76.58844933, -9.406e-05, -229.76534799, -0.00028219, -765.88449329, -0.00094062, 0.4, 0.3, 0.003, 0.0, 0.0, 22007, 2)
    ops.limitCurve('ThreePoint', 12007, 2007, 0.0, 210.5707675, 0.01291226, 210.5707675, 0.03873679, 147.39953725, -1578.07291712, 0.05, 2, 0, 72007, 23007, 1, 3)
    ops.uniaxialMaterial('LimitState', 32007, 52.64269187, 6.465e-05, 157.92807562, 0.00019396, 526.42691874, 0.00064653, -52.64269187, -6.465e-05, -157.92807562, -0.00019396, -526.42691874, -0.00064653, 0.4, 0.3, 0.003, 0.0, 0.0, 12007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2007, 99999, 'P', 42007, 'Vy', 32007, 'Vz', 22007, 'My', 12007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172007, 72007, 172007, 2007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123007, 123007, 23007, 2007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172008, 11.6, 4.4, 6.525)
    ops.node(123008, 11.6, 4.4, 9.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2008, 172008, 123008, 0.125, 29547896.73788899, 12311623.64078708, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22008, 81.11089446, 0.00053063, 98.37400743, 0.04160756, 9.83740074, 0.13021711, -81.11089446, -0.00053063, -98.37400743, -0.04160756, -9.83740074, -0.13021711, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12008, 38.61372367, 0.00082239, 46.8320164, 0.03310628, 4.68320164, 0.08314784, -38.61372367, -0.00082239, -46.8320164, -0.03310628, -4.68320164, -0.08314784, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22008, 2008, 0.0, 159.06369841, 0.01061261, 159.06369841, 0.03183784, 111.34458889, -3117.37330655, 0.05, 2, 0, 72008, 23008, 2, 3)
    ops.uniaxialMaterial('LimitState', 42008, 39.7659246, 9.767e-05, 119.29777381, 0.00029302, 397.65924603, 0.00097674, -39.7659246, -9.767e-05, -119.29777381, -0.00029302, -397.65924603, -0.00097674, 0.4, 0.3, 0.003, 0.0, 0.0, 22008, 2)
    ops.limitCurve('ThreePoint', 12008, 2008, 0.0, 117.71094437, 0.01644786, 117.71094437, 0.04934358, 82.39766106, -1228.76424654, 0.05, 2, 0, 72008, 23008, 1, 3)
    ops.uniaxialMaterial('LimitState', 32008, 29.42773609, 7.228e-05, 88.28320828, 0.00021684, 294.27736094, 0.00072281, -29.42773609, -7.228e-05, -88.28320828, -0.00021684, -294.27736094, -0.00072281, 0.4, 0.3, 0.003, 0.0, 0.0, 12008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2008, 99999, 'P', 42008, 'Vy', 32008, 'Vz', 22008, 'My', 12008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172008, 72008, 172008, 2008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123008, 123008, 23008, 2008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172009, 0.0, 8.8, 6.525)
    ops.node(123009, 0.0, 8.8, 9.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2009, 172009, 123009, 0.0875, 27001247.05718, 11250519.60715833, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22009, 42.19341432, 0.00065037, 51.3953524, 0.02603265, 5.13953524, 0.08005926, -42.19341432, -0.00065037, -51.3953524, -0.02603265, -5.13953524, -0.08005926, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12009, 26.85174255, 0.00084246, 32.70782402, 0.02360418, 3.2707824, 0.06532443, -26.85174255, -0.00084246, -32.70782402, -0.02360418, -3.2707824, -0.06532443, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22009, 2009, 0.0, 82.26950621, 0.01300735, 82.26950621, 0.03902206, 57.58865434, -1061.98784915, 0.05, 2, 0, 72009, 23009, 2, 3)
    ops.uniaxialMaterial('LimitState', 42009, 20.56737655, 7.898e-05, 61.70212966, 0.00023693, 205.67376552, 0.00078975, -20.56737655, -7.898e-05, -61.70212966, -0.00023693, -205.67376552, -0.00078975, 0.4, 0.3, 0.003, 0.0, 0.0, 22009, 2)
    ops.limitCurve('ThreePoint', 12009, 2009, 0.0, 72.60774366, 0.01684923, 72.60774366, 0.05054769, 50.82542056, -718.66283507, 0.05, 2, 0, 72009, 23009, 1, 3)
    ops.uniaxialMaterial('LimitState', 32009, 18.15193591, 6.97e-05, 54.45580774, 0.0002091, 181.51935915, 0.000697, -18.15193591, -6.97e-05, -54.45580774, -0.0002091, -181.51935915, -0.000697, 0.4, 0.3, 0.003, 0.0, 0.0, 12009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2009, 99999, 'P', 42009, 'Vy', 32009, 'Vz', 22009, 'My', 12009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172009, 72009, 172009, 2009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123009, 123009, 23009, 2009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172010, 3.1, 8.8, 6.525)
    ops.node(123010, 3.1, 8.8, 9.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2010, 172010, 123010, 0.1375, 28756295.38523661, 11981789.74384859, 0.00204719, 0.00078776, 0.00381276, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22010, 105.40244485, 0.00054904, 127.93655199, 0.04334882, 12.7936552, 0.12835561, -105.40244485, -0.00054904, -127.93655199, -0.04334882, -12.7936552, -0.12835561, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12010, 46.43054054, 0.00096165, 56.35697798, 0.03359214, 5.6356978, 0.07825833, -46.43054054, -0.00096165, -56.35697798, -0.03359214, -5.6356978, -0.07825833, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22010, 2010, 0.0, 170.96491212, 0.01098078, 170.96491212, 0.03294233, 119.67543848, -2625.29634343, 0.05, 2, 0, 72010, 23010, 2, 3)
    ops.uniaxialMaterial('LimitState', 42010, 42.74122803, 9.807e-05, 128.22368409, 0.0002942, 427.4122803, 0.00098065, -42.74122803, -9.807e-05, -128.22368409, -0.0002942, -427.4122803, -0.00098065, 0.4, 0.3, 0.003, 0.0, 0.0, 22010, 2)
    ops.limitCurve('ThreePoint', 12010, 2010, 0.0, 119.19955848, 0.01923292, 119.19955848, 0.05769876, 83.43969094, -1031.65754793, 0.05, 2, 0, 72010, 23010, 1, 3)
    ops.uniaxialMaterial('LimitState', 32010, 29.79988962, 6.837e-05, 89.39966886, 0.00020512, 297.99889621, 0.00068373, -29.79988962, -6.837e-05, -89.39966886, -0.00020512, -297.99889621, -0.00068373, 0.4, 0.3, 0.003, 0.0, 0.0, 12010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2010, 99999, 'P', 42010, 'Vy', 32010, 'Vz', 22010, 'My', 12010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172010, 72010, 172010, 2010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123010, 123010, 23010, 2010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172011, 7.35, 8.8, 6.525)
    ops.node(123011, 7.35, 8.8, 9.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2011, 172011, 123011, 0.2275, 31241751.10258349, 13017396.29274312, 0.00616035, 0.00255464, 0.00881089, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22011, 188.63982871, 0.00048596, 227.9618745, 0.03956346, 22.79618745, 0.10917952, -188.63982871, -0.00048596, -227.9618745, -0.03956346, -22.79618745, -0.10917952, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12011, 84.58823422, 0.00066057, 102.22068459, 0.03259626, 10.22206846, 0.07572772, -84.58823422, -0.00066057, -102.22068459, -0.03259626, -10.22206846, -0.07572772, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22011, 2011, 0.0, 289.45300082, 0.00971913, 289.45300082, 0.02915738, 202.61710057, -3186.22792513, 0.05, 2, 0, 72011, 23011, 2, 3)
    ops.uniaxialMaterial('LimitState', 42011, 72.36325021, 9.236e-05, 217.08975062, 0.00027709, 723.63250205, 0.00092364, -72.36325021, -9.236e-05, -217.08975062, -0.00027709, -723.63250205, -0.00092364, 0.4, 0.3, 0.003, 0.0, 0.0, 22011, 2)
    ops.limitCurve('ThreePoint', 12011, 2011, 0.0, 198.95264112, 0.01321138, 198.95264112, 0.03963414, 139.26684878, -1483.26620785, 0.05, 2, 0, 72011, 23011, 1, 3)
    ops.uniaxialMaterial('LimitState', 32011, 49.73816028, 6.349e-05, 149.21448084, 0.00019046, 497.38160279, 0.00063486, -49.73816028, -6.349e-05, -149.21448084, -0.00019046, -497.38160279, -0.00063486, 0.4, 0.3, 0.003, 0.0, 0.0, 12011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2011, 99999, 'P', 42011, 'Vy', 32011, 'Vz', 22011, 'My', 12011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172011, 72011, 172011, 2011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123011, 123011, 23011, 2011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172012, 11.6, 8.8, 6.525)
    ops.node(123012, 11.6, 8.8, 9.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2012, 172012, 123012, 0.125, 28937022.7861094, 12057092.82754558, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22012, 78.73761015, 0.00052547, 95.62501944, 0.03948069, 9.56250194, 0.12719263, -78.73761015, -0.00052547, -95.62501944, -0.03948069, -9.56250194, -0.12719263, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12012, 37.34433719, 0.0008206, 45.35383996, 0.03143695, 4.535384, 0.08097158, -37.34433719, -0.0008206, -45.35383996, -0.03143695, -4.535384, -0.08097158, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22012, 2012, 0.0, 152.49579354, 0.01050949, 152.49579354, 0.03152848, 106.74705548, -2881.10291675, 0.05, 2, 0, 72012, 23012, 2, 3)
    ops.uniaxialMaterial('LimitState', 42012, 38.12394838, 9.562e-05, 114.37184515, 0.00028685, 381.23948385, 0.00095617, -38.12394838, -9.562e-05, -114.37184515, -0.00028685, -381.23948385, -0.00095617, 0.4, 0.3, 0.003, 0.0, 0.0, 22012, 2)
    ops.limitCurve('ThreePoint', 12012, 2012, 0.0, 113.30132368, 0.01641191, 113.30132368, 0.04923573, 79.31092658, -1153.51742529, 0.05, 2, 0, 72012, 23012, 1, 3)
    ops.uniaxialMaterial('LimitState', 32012, 28.32533092, 7.104e-05, 84.97599276, 0.00021313, 283.2533092, 0.00071042, -28.32533092, -7.104e-05, -84.97599276, -0.00021313, -283.2533092, -0.00071042, 0.4, 0.3, 0.003, 0.0, 0.0, 12012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2012, 99999, 'P', 42012, 'Vy', 32012, 'Vz', 22012, 'My', 12012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172012, 72012, 172012, 2012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123012, 123012, 23012, 2012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172013, 0.0, 13.2, 6.525)
    ops.node(123013, 0.0, 13.2, 9.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2013, 172013, 123013, 0.0875, 26152220.18426416, 10896758.41011007, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22013, 41.65632173, 0.00067112, 50.7958382, 0.02662966, 5.07958382, 0.07937025, -41.65632173, -0.00067112, -50.7958382, -0.02662966, -5.07958382, -0.07937025, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12013, 26.56394361, 0.00088172, 32.39214903, 0.0241602, 3.2392149, 0.06488736, -26.56394361, -0.00088172, -32.39214903, -0.0241602, -3.2392149, -0.06488736, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22013, 2013, 0.0, 80.29776381, 0.01342236, 80.29776381, 0.04026707, 56.20843467, -1065.79804541, 0.05, 2, 0, 72013, 23013, 2, 3)
    ops.uniaxialMaterial('LimitState', 42013, 20.07444095, 7.958e-05, 60.22332286, 0.00023875, 200.74440953, 0.00079585, -20.07444095, -7.958e-05, -60.22332286, -0.00023875, -200.74440953, -0.00079585, 0.4, 0.3, 0.003, 0.0, 0.0, 22013, 2)
    ops.limitCurve('ThreePoint', 12013, 2013, 0.0, 70.60810738, 0.01763434, 70.60810738, 0.05290302, 49.42567517, -720.90140629, 0.05, 2, 0, 72013, 23013, 1, 3)
    ops.uniaxialMaterial('LimitState', 32013, 17.65202685, 6.998e-05, 52.95608054, 0.00020994, 176.52026846, 0.00069981, -17.65202685, -6.998e-05, -52.95608054, -0.00020994, -176.52026846, -0.00069981, 0.4, 0.3, 0.003, 0.0, 0.0, 12013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2013, 99999, 'P', 42013, 'Vy', 32013, 'Vz', 22013, 'My', 12013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172013, 72013, 172013, 2013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123013, 123013, 23013, 2013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172014, 3.1, 13.2, 6.525)
    ops.node(123014, 3.1, 13.2, 9.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2014, 172014, 123014, 0.1375, 28172494.4326057, 11738539.34691904, 0.00204719, 0.00078776, 0.00381276, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22014, 102.52423772, 0.0005266, 124.57639637, 0.0464143, 12.45763964, 0.13028716, -102.52423772, -0.0005266, -124.57639637, -0.0464143, -12.45763964, -0.13028716, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12014, 45.6133063, 0.00088897, 55.42437039, 0.0358737, 5.54243704, 0.07994406, -45.6133063, -0.00088897, -55.42437039, -0.0358737, -5.54243704, -0.07994406, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22014, 2014, 0.0, 183.29719694, 0.01053205, 183.29719694, 0.03159615, 128.30803786, -3371.32660304, 0.05, 2, 0, 72014, 23014, 2, 3)
    ops.uniaxialMaterial('LimitState', 42014, 45.82429924, 0.00010732, 137.47289771, 0.00032195, 458.24299236, 0.00107318, -45.82429924, -0.00010732, -137.47289771, -0.00032195, -458.24299236, -0.00107318, 0.4, 0.3, 0.003, 0.0, 0.0, 22014, 2)
    ops.limitCurve('ThreePoint', 12014, 2014, 0.0, 123.65455372, 0.01777948, 123.65455372, 0.05333845, 86.55818761, -1240.58346232, 0.05, 2, 0, 72014, 23014, 1, 3)
    ops.uniaxialMaterial('LimitState', 32014, 30.91363843, 7.24e-05, 92.74091529, 0.00021719, 309.13638431, 0.00072398, -30.91363843, -7.24e-05, -92.74091529, -0.00021719, -309.13638431, -0.00072398, 0.4, 0.3, 0.003, 0.0, 0.0, 12014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2014, 99999, 'P', 42014, 'Vy', 32014, 'Vz', 22014, 'My', 12014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172014, 72014, 172014, 2014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123014, 123014, 23014, 2014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172015, 7.35, 13.2, 6.525)
    ops.node(123015, 7.35, 13.2, 9.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2015, 172015, 123015, 0.2275, 26829606.16751771, 11179002.56979905, 0.00616035, 0.00255464, 0.00881089, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22015, 194.06189727, 0.00050554, 236.82454995, 0.04077872, 23.68245499, 0.10582276, -194.06189727, -0.00050554, -236.82454995, -0.04077872, -23.68245499, -0.10582276, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12015, 86.26803856, 0.00069052, 105.2776959, 0.03360336, 10.52776959, 0.07390218, -86.26803856, -0.00069052, -105.2776959, -0.03360336, -10.52776959, -0.07390218, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22015, 2015, 0.0, 251.51239468, 0.01011075, 251.51239468, 0.03033224, 176.05867628, -3222.35291983, 0.05, 2, 0, 72015, 23015, 2, 3)
    ops.uniaxialMaterial('LimitState', 42015, 62.87809867, 9.346e-05, 188.63429601, 0.00028037, 628.7809867, 0.00093456, -62.87809867, -9.346e-05, -188.63429601, -0.00028037, -628.7809867, -0.00093456, 0.4, 0.3, 0.003, 0.0, 0.0, 22015, 2)
    ops.limitCurve('ThreePoint', 12015, 2015, 0.0, 170.0574897, 0.01381032, 170.0574897, 0.04143095, 119.04024279, -1496.53023781, 0.05, 2, 0, 72015, 23015, 1, 3)
    ops.uniaxialMaterial('LimitState', 32015, 42.51437243, 6.319e-05, 127.54311728, 0.00018957, 425.14372425, 0.00063189, -42.51437243, -6.319e-05, -127.54311728, -0.00018957, -425.14372425, -0.00063189, 0.4, 0.3, 0.003, 0.0, 0.0, 12015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2015, 99999, 'P', 42015, 'Vy', 32015, 'Vz', 22015, 'My', 12015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172015, 72015, 172015, 2015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123015, 123015, 23015, 2015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172016, 11.6, 13.2, 6.525)
    ops.node(123016, 11.6, 13.2, 9.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2016, 172016, 123016, 0.125, 34109029.68749252, 14212095.70312188, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22016, 79.27452896, 0.0005198, 94.85103326, 0.03968743, 9.48510333, 0.1334647, -79.27452896, -0.0005198, -94.85103326, -0.03968743, -9.48510333, -0.1334647, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12016, 37.47508952, 0.00082227, 44.83849994, 0.03160557, 4.48384999, 0.08456556, -37.47508952, -0.00082227, -44.83849994, -0.03160557, -4.48384999, -0.08456556, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22016, 2016, 0.0, 181.37751938, 0.01039602, 181.37751938, 0.03118805, 126.96426357, -3380.53081696, 0.05, 2, 0, 72016, 23016, 2, 3)
    ops.uniaxialMaterial('LimitState', 42016, 45.34437985, 9.648e-05, 136.03313954, 0.00028945, 453.44379846, 0.00096482, -45.34437985, -9.648e-05, -136.03313954, -0.00028945, -453.44379846, -0.00096482, 0.4, 0.3, 0.003, 0.0, 0.0, 22016, 2)
    ops.limitCurve('ThreePoint', 12016, 2016, 0.0, 137.56138858, 0.0164455, 137.56138858, 0.04933649, 96.29297201, -1310.20000342, 0.05, 2, 0, 72016, 23016, 1, 3)
    ops.uniaxialMaterial('LimitState', 32016, 34.39034714, 7.317e-05, 103.17104143, 0.00021952, 343.90347145, 0.00073175, -34.39034714, -7.317e-05, -103.17104143, -0.00021952, -343.90347145, -0.00073175, 0.4, 0.3, 0.003, 0.0, 0.0, 12016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2016, 99999, 'P', 42016, 'Vy', 32016, 'Vz', 22016, 'My', 12016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172016, 72016, 172016, 2016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123016, 123016, 23016, 2016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172017, 0.0, 17.6, 6.525)
    ops.node(123017, 0.0, 17.6, 9.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2017, 172017, 123017, 0.0875, 32875036.15571297, 13697931.73154707, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22017, 43.22613558, 0.00062498, 51.92908158, 0.02144562, 5.19290816, 0.08134247, -43.22613558, -0.00062498, -51.92908158, -0.02144562, -5.19290816, -0.08134247, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12017, 27.62317575, 0.00080235, 33.1846955, 0.01947338, 3.31846955, 0.06572673, -27.62317575, -0.00080235, -33.1846955, -0.01947338, -3.31846955, -0.06572673, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22017, 2017, 0.0, 91.69589999, 0.01249964, 91.69589999, 0.03749892, 64.18712999, -842.14329355, 0.05, 2, 0, 72017, 23017, 2, 3)
    ops.uniaxialMaterial('LimitState', 42017, 22.923975, 7.23e-05, 68.77192499, 0.00021689, 229.23974997, 0.00072297, -22.923975, -7.23e-05, -68.77192499, -0.00021689, -229.23974997, -0.00072297, 0.4, 0.3, 0.003, 0.0, 0.0, 22017, 2)
    ops.limitCurve('ThreePoint', 12017, 2017, 0.0, 80.14946896, 0.01604699, 80.14946896, 0.04814098, 56.10462827, -588.49883126, 0.05, 2, 0, 72017, 23017, 1, 3)
    ops.uniaxialMaterial('LimitState', 32017, 20.03736724, 6.319e-05, 60.11210172, 0.00018958, 200.37367241, 0.00063193, -20.03736724, -6.319e-05, -60.11210172, -0.00018958, -200.37367241, -0.00063193, 0.4, 0.3, 0.003, 0.0, 0.0, 12017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2017, 99999, 'P', 42017, 'Vy', 32017, 'Vz', 22017, 'My', 12017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172017, 72017, 172017, 2017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123017, 123017, 23017, 2017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172018, 3.1, 17.6, 6.525)
    ops.node(123018, 3.1, 17.6, 9.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2018, 172018, 123018, 0.1375, 30873640.36597519, 12864016.81915633, 0.00204719, 0.00078776, 0.00381276, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22018, 101.46953266, 0.0005034, 122.57171088, 0.04259528, 12.25717109, 0.13107295, -101.46953266, -0.0005034, -122.57171088, -0.04259528, -12.25717109, -0.13107295, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12018, 45.42320552, 0.0008248, 54.86967239, 0.03291559, 5.48696724, 0.07940553, -45.42320552, -0.0008248, -54.86967239, -0.03291559, -5.48696724, -0.07940553, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22018, 2018, 0.0, 174.17819516, 0.01006791, 174.17819516, 0.03020373, 121.92473661, -2328.43197024, 0.05, 2, 0, 72018, 23018, 2, 3)
    ops.uniaxialMaterial('LimitState', 42018, 43.54454879, 9.306e-05, 130.63364637, 0.00027917, 435.44548791, 0.00093056, -43.54454879, -9.306e-05, -130.63364637, -0.00027917, -435.44548791, -0.00093056, 0.4, 0.3, 0.003, 0.0, 0.0, 22018, 2)
    ops.limitCurve('ThreePoint', 12018, 2018, 0.0, 124.95202148, 0.01649591, 124.95202148, 0.04948774, 87.46641503, -946.37113847, 0.05, 2, 0, 72018, 23018, 1, 3)
    ops.uniaxialMaterial('LimitState', 32018, 31.23800537, 6.676e-05, 93.71401611, 0.00020027, 312.38005369, 0.00066757, -31.23800537, -6.676e-05, -93.71401611, -0.00020027, -312.38005369, -0.00066757, 0.4, 0.3, 0.003, 0.0, 0.0, 12018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2018, 99999, 'P', 42018, 'Vy', 32018, 'Vz', 22018, 'My', 12018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172018, 72018, 172018, 2018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123018, 123018, 23018, 2018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172019, 7.35, 17.6, 6.525)
    ops.node(123019, 7.35, 17.6, 9.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2019, 172019, 123019, 0.2275, 29809683.56008601, 12420701.48336917, 0.00616035, 0.00255464, 0.00881089, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22019, 187.24200083, 0.00047761, 227.13684335, 0.04128772, 22.71368433, 0.10970323, -187.24200083, -0.00047761, -227.13684335, -0.04128772, -22.71368433, -0.10970323, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12019, 83.7893041, 0.0006369, 101.64192838, 0.03398853, 10.16419284, 0.07637619, -83.7893041, -0.0006369, -101.64192838, -0.03398853, -10.16419284, -0.07637619, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22019, 2019, 0.0, 283.72098059, 0.00955229, 283.72098059, 0.02865687, 198.60468641, -3538.71212333, 0.05, 2, 0, 72019, 23019, 2, 3)
    ops.uniaxialMaterial('LimitState', 42019, 70.93024515, 9.488e-05, 212.79073544, 0.00028465, 709.30245148, 0.00094885, -70.93024515, -9.488e-05, -212.79073544, -0.00028465, -709.30245148, -0.00094885, 0.4, 0.3, 0.003, 0.0, 0.0, 22019, 2)
    ops.limitCurve('ThreePoint', 12019, 2019, 0.0, 193.02976299, 0.01273791, 193.02976299, 0.03821372, 135.12083409, -1612.04899905, 0.05, 2, 0, 72019, 23019, 1, 3)
    ops.uniaxialMaterial('LimitState', 32019, 48.25744075, 6.455e-05, 144.77232224, 0.00019366, 482.57440747, 0.00064555, -48.25744075, -6.455e-05, -144.77232224, -0.00019366, -482.57440747, -0.00064555, 0.4, 0.3, 0.003, 0.0, 0.0, 12019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2019, 99999, 'P', 42019, 'Vy', 32019, 'Vz', 22019, 'My', 12019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172019, 72019, 172019, 2019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123019, 123019, 23019, 2019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172020, 11.6, 17.6, 6.525)
    ops.node(123020, 11.6, 17.6, 9.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2020, 172020, 123020, 0.125, 30651788.08610618, 12771578.36921091, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22020, 80.52448578, 0.00053658, 97.40024172, 0.03870894, 9.74002417, 0.12888157, -80.52448578, -0.00053658, -97.40024172, -0.03870894, -9.74002417, -0.12888157, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12020, 38.05477023, 0.00085269, 46.03002159, 0.03085376, 4.60300216, 0.08177805, -38.05477023, -0.00085269, -46.03002159, -0.03085376, -4.60300216, -0.08177805, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22020, 2020, 0.0, 152.27119092, 0.01073161, 152.27119092, 0.03219484, 106.58983364, -2519.3407674, 0.05, 2, 0, 72020, 23020, 2, 3)
    ops.uniaxialMaterial('LimitState', 42020, 38.06779773, 9.014e-05, 114.20339319, 0.00027041, 380.67797729, 0.00090135, -38.06779773, -9.014e-05, -114.20339319, -0.00027041, -380.67797729, -0.00090135, 0.4, 0.3, 0.003, 0.0, 0.0, 22020, 2)
    ops.limitCurve('ThreePoint', 12020, 2020, 0.0, 116.33225124, 0.01705371, 116.33225124, 0.05116112, 81.43257587, -1038.25962348, 0.05, 2, 0, 72020, 23020, 1, 3)
    ops.uniaxialMaterial('LimitState', 32020, 29.08306281, 6.886e-05, 87.24918843, 0.00020658, 290.8306281, 0.00068862, -29.08306281, -6.886e-05, -87.24918843, -0.00020658, -290.8306281, -0.00068862, 0.4, 0.3, 0.003, 0.0, 0.0, 12020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2020, 99999, 'P', 42020, 'Vy', 32020, 'Vz', 22020, 'My', 12020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172020, 72020, 172020, 2020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123020, 123020, 23020, 2020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172021, 0.0, 22.0, 6.525)
    ops.node(123021, 0.0, 22.0, 9.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2021, 172021, 123021, 0.0625, 27713405.78159033, 11547252.40899597, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22021, 18.54528557, 0.00083652, 22.5961455, 0.02627104, 2.25961455, 0.08356951, -18.54528557, -0.00083652, -22.5961455, -0.02627104, -2.25961455, -0.08356951, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12021, 18.54528557, 0.00083652, 22.5961455, 0.02627104, 2.25961455, 0.08356951, -18.54528557, -0.00083652, -22.5961455, -0.02627104, -2.25961455, -0.08356951, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22021, 2021, 0.0, 57.8305261, 0.01673046, 57.8305261, 0.05019138, 40.48136827, -773.27679087, 0.05, 2, 0, 72021, 23021, 2, 3)
    ops.uniaxialMaterial('LimitState', 42021, 14.45763153, 7.572e-05, 43.37289458, 0.00022717, 144.57631526, 0.00075723, -14.45763153, -7.572e-05, -43.37289458, -0.00022717, -144.57631526, -0.00075723, 0.4, 0.3, 0.003, 0.0, 0.0, 22021, 2)
    ops.limitCurve('ThreePoint', 12021, 2021, 0.0, 57.8305261, 0.01673046, 57.8305261, 0.05019138, 40.48136827, -773.27679087, 0.05, 2, 0, 72021, 23021, 1, 3)
    ops.uniaxialMaterial('LimitState', 32021, 14.45763153, 7.572e-05, 43.37289458, 0.00022717, 144.57631526, 0.00075723, -14.45763153, -7.572e-05, -43.37289458, -0.00022717, -144.57631526, -0.00075723, 0.4, 0.3, 0.003, 0.0, 0.0, 12021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2021, 99999, 'P', 42021, 'Vy', 32021, 'Vz', 22021, 'My', 12021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172021, 72021, 172021, 2021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123021, 123021, 23021, 2021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172022, 3.1, 22.0, 6.525)
    ops.node(123022, 3.1, 22.0, 9.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2022, 172022, 123022, 0.0875, 28408137.80361635, 11836724.08484015, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22022, 38.41953689, 0.00092067, 46.65307327, 0.04059604, 4.66530733, 0.10347982, -38.41953689, -0.00092067, -46.65307327, -0.04059604, -4.66530733, -0.10347982, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12022, 53.18426564, 0.00069563, 64.58197164, 0.04546947, 6.45819716, 0.12923809, -53.18426564, -0.00069563, -64.58197164, -0.04546947, -6.45819716, -0.12923809, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22022, 2022, 0.0, 91.70726722, 0.01841344, 91.70726722, 0.05524033, 64.19508706, -1216.1012511, 0.05, 2, 0, 72022, 23022, 2, 3)
    ops.uniaxialMaterial('LimitState', 42022, 22.92681681, 8.368e-05, 68.78045042, 0.00025103, 229.26816806, 0.00083675, -22.92681681, -8.368e-05, -68.78045042, -0.00025103, -229.26816806, -0.00083675, 0.4, 0.3, 0.003, 0.0, 0.0, 22022, 2)
    ops.limitCurve('ThreePoint', 12022, 2022, 0.0, 107.15532015, 0.01391269, 107.15532015, 0.04173806, 75.0087241, -1898.18838521, 0.05, 2, 0, 72022, 23022, 1, 3)
    ops.uniaxialMaterial('LimitState', 32022, 26.78883004, 9.777e-05, 80.36649011, 0.00029331, 267.88830037, 0.0009777, -26.78883004, -9.777e-05, -80.36649011, -0.00029331, -267.88830037, -0.0009777, 0.4, 0.3, 0.003, 0.0, 0.0, 12022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2022, 99999, 'P', 42022, 'Vy', 32022, 'Vz', 22022, 'My', 12022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172022, 72022, 172022, 2022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123022, 123022, 23022, 2022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172023, 7.35, 22.0, 6.525)
    ops.node(123023, 7.35, 22.0, 9.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2023, 172023, 123023, 0.175, 29458187.76720933, 12274244.90300389, 0.00405757, 0.00401042, 0.0019651, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22023, 62.42849432, 0.00060298, 75.83737792, 0.04997824, 7.58373779, 0.12210772, -62.42849432, -0.00060298, -75.83737792, -0.04997824, -7.58373779, -0.12210772, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12023, 100.78342822, 0.00050285, 122.43048654, 0.05669677, 12.24304865, 0.15473079, -100.78342822, -0.00050285, -122.43048654, -0.05669677, -12.24304865, -0.15473079, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22023, 2023, 0.0, 198.15561047, 0.01205966, 198.15561047, 0.03617897, 138.70892733, -3995.27801841, 0.05, 2, 0, 72023, 23023, 2, 3)
    ops.uniaxialMaterial('LimitState', 42023, 49.53890262, 8.718e-05, 148.61670785, 0.00026153, 495.38902618, 0.00087178, -49.53890262, -8.718e-05, -148.61670785, -0.00026153, -495.38902618, -0.00087178, 0.4, 0.3, 0.003, 0.0, 0.0, 22023, 2)
    ops.limitCurve('ThreePoint', 12023, 2023, 0.0, 240.404755, 0.01005703, 240.404755, 0.0301711, 168.2833285, -7082.10994561, 0.05, 2, 0, 72023, 23023, 1, 3)
    ops.uniaxialMaterial('LimitState', 32023, 60.10118875, 0.00010577, 180.30356625, 0.0003173, 601.01188751, 0.00105765, -60.10118875, -0.00010577, -180.30356625, -0.0003173, -601.01188751, -0.00105765, 0.4, 0.3, 0.003, 0.0, 0.0, 12023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2023, 99999, 'P', 42023, 'Vy', 32023, 'Vz', 22023, 'My', 12023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172023, 72023, 172023, 2023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123023, 123023, 23023, 2023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172024, 11.6, 22.0, 6.525)
    ops.node(123024, 11.6, 22.0, 9.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2024, 172024, 123024, 0.0625, 28711573.28921484, 11963155.53717285, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22024, 20.18489289, 0.00082682, 24.50964746, 0.02633178, 2.45096475, 0.08214247, -20.18489289, -0.00082682, -24.50964746, -0.02633178, -2.45096475, -0.08214247, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12024, 20.18489289, 0.00082682, 24.50964746, 0.02633178, 2.45096475, 0.08214247, -20.18489289, -0.00082682, -24.50964746, -0.02633178, -2.45096475, -0.08214247, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22024, 2024, 0.0, 63.25835698, 0.01653642, 63.25835698, 0.04960927, 44.28084989, -796.82523779, 0.05, 2, 0, 72024, 23024, 2, 3)
    ops.uniaxialMaterial('LimitState', 42024, 15.81458925, 7.995e-05, 47.44376774, 0.00023985, 158.14589246, 0.00079951, -15.81458925, -7.995e-05, -47.44376774, -0.00023985, -158.14589246, -0.00079951, 0.4, 0.3, 0.003, 0.0, 0.0, 22024, 2)
    ops.limitCurve('ThreePoint', 12024, 2024, 0.0, 63.25835698, 0.01653642, 63.25835698, 0.04960927, 44.28084989, -796.82523779, 0.05, 2, 0, 72024, 23024, 1, 3)
    ops.uniaxialMaterial('LimitState', 32024, 15.81458925, 7.995e-05, 47.44376774, 0.00023985, 158.14589246, 0.00079951, -15.81458925, -7.995e-05, -47.44376774, -0.00023985, -158.14589246, -0.00079951, 0.4, 0.3, 0.003, 0.0, 0.0, 12024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2024, 99999, 'P', 42024, 'Vy', 32024, 'Vz', 22024, 'My', 12024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172024, 72024, 172024, 2024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123024, 123024, 23024, 2024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173003, 7.35, 0.0, 9.675)
    ops.node(124003, 7.35, 0.0, 12.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3003, 173003, 124003, 0.125, 26524091.41939091, 11051704.75807955, 0.00178813, 0.00286458, 0.00071615, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23003, 33.73103661, 0.00082041, 41.34133879, 0.02358265, 4.13413388, 0.05730208, -33.73103661, -0.00082041, -41.34133879, -0.02358265, -4.13413388, -0.05730208, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13003, 82.00544048, 0.0005261, 100.50727871, 0.02839596, 10.05072787, 0.08290068, -82.00544048, -0.0005261, -100.50727871, -0.02839596, -10.05072787, -0.08290068, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23003, 3003, 0.0, 69.41787042, 0.01640818, 69.41787042, 0.04922454, 48.59250929, -679.20974725, 0.05, 2, 0, 73003, 24003, 2, 3)
    ops.uniaxialMaterial('LimitState', 43003, 17.35446761, 4.749e-05, 52.06340282, 0.00014246, 173.54467605, 0.00047486, -17.35446761, -4.749e-05, -52.06340282, -0.00014246, -173.54467605, -0.00047486, 0.4, 0.3, 0.003, 0.0, 0.0, 23003, 2)
    ops.limitCurve('ThreePoint', 13003, 3003, 0.0, 97.39892218, 0.01052206, 97.39892218, 0.03156619, 68.17924552, -1967.89554112, 0.05, 2, 0, 73003, 24003, 1, 3)
    ops.uniaxialMaterial('LimitState', 33003, 24.34973054, 6.663e-05, 73.04919163, 0.00019988, 243.49730544, 0.00066626, -24.34973054, -6.663e-05, -73.04919163, -0.00019988, -243.49730544, -0.00066626, 0.4, 0.3, 0.003, 0.0, 0.0, 13003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3003, 99999, 'P', 43003, 'Vy', 33003, 'Vz', 23003, 'My', 13003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173003, 73003, 173003, 3003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124003, 124003, 24003, 3003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173004, 11.6, 0.0, 9.675)
    ops.node(124004, 11.6, 0.0, 12.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3004, 173004, 124004, 0.0625, 33340524.8414375, 13891885.35059896, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23004, 14.67881976, 0.00074139, 17.65182105, 0.02445723, 1.76518211, 0.08942446, -14.67881976, -0.00074139, -17.65182105, -0.02445723, -1.76518211, -0.08942446, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13004, 14.67881976, 0.00074139, 17.65182105, 0.02445723, 1.76518211, 0.08942446, -14.67881976, -0.00074139, -17.65182105, -0.02445723, -1.76518211, -0.08942446, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23004, 3004, 0.0, 64.27312319, 0.01482785, 64.27312319, 0.04448354, 44.99118623, -1276.30621683, 0.05, 2, 0, 73004, 24004, 2, 3)
    ops.uniaxialMaterial('LimitState', 43004, 16.0682808, 6.996e-05, 48.20484239, 0.00020987, 160.68280797, 0.00069955, -16.0682808, -6.996e-05, -48.20484239, -0.00020987, -160.68280797, -0.00069955, 0.4, 0.3, 0.003, 0.0, 0.0, 23004, 2)
    ops.limitCurve('ThreePoint', 13004, 3004, 0.0, 64.27312319, 0.01482785, 64.27312319, 0.04448354, 44.99118623, -1276.30621683, 0.05, 2, 0, 73004, 24004, 1, 3)
    ops.uniaxialMaterial('LimitState', 33004, 16.0682808, 6.996e-05, 48.20484239, 0.00020987, 160.68280797, 0.00069955, -16.0682808, -6.996e-05, -48.20484239, -0.00020987, -160.68280797, -0.00069955, 0.4, 0.3, 0.003, 0.0, 0.0, 13004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3004, 99999, 'P', 43004, 'Vy', 33004, 'Vz', 23004, 'My', 13004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173004, 73004, 173004, 3004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124004, 124004, 24004, 3004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173005, 0.0, 4.4, 9.675)
    ops.node(124005, 0.0, 4.4, 12.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3005, 173005, 124005, 0.0875, 29093011.75661206, 12122088.23192169, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23005, 34.13773026, 0.0006051, 41.57202702, 0.02342046, 4.1572027, 0.08615321, -34.13773026, -0.0006051, -41.57202702, -0.02342046, -4.1572027, -0.08615321, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13005, 21.20612702, 0.00076991, 25.82426186, 0.02122972, 2.58242619, 0.06967299, -21.20612702, -0.00076991, -25.82426186, -0.02122972, -2.58242619, -0.06967299, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23005, 3005, 0.0, 76.14803134, 0.01210209, 76.14803134, 0.03630627, 53.30362193, -1201.17068509, 0.05, 2, 0, 73005, 24005, 2, 3)
    ops.uniaxialMaterial('LimitState', 43005, 19.03700783, 6.784e-05, 57.1110235, 0.00020353, 190.37007834, 0.00067843, -19.03700783, -6.784e-05, -57.1110235, -0.00020353, -190.37007834, -0.00067843, 0.4, 0.3, 0.003, 0.0, 0.0, 23005, 2)
    ops.limitCurve('ThreePoint', 13005, 3005, 0.0, 63.32173297, 0.01539813, 63.32173297, 0.04619438, 44.32521308, -726.66850698, 0.05, 2, 0, 73005, 24005, 1, 3)
    ops.uniaxialMaterial('LimitState', 33005, 15.83043324, 5.642e-05, 47.49129973, 0.00016925, 158.30433242, 0.00056416, -15.83043324, -5.642e-05, -47.49129973, -0.00016925, -158.30433242, -0.00056416, 0.4, 0.3, 0.003, 0.0, 0.0, 13005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3005, 99999, 'P', 43005, 'Vy', 33005, 'Vz', 23005, 'My', 13005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173005, 73005, 173005, 3005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124005, 124005, 24005, 3005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173006, 3.1, 4.4, 9.675)
    ops.node(124006, 3.1, 4.4, 12.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3006, 173006, 124006, 0.1375, 29369354.30670407, 12237230.96112669, 0.00204719, 0.00078776, 0.00381276, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23006, 83.97214339, 0.00049897, 102.17309121, 0.02348031, 10.21730912, 0.07774781, -83.97214339, -0.00049897, -102.17309121, -0.02348031, -10.21730912, -0.07774781, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13006, 32.76497887, 0.00082281, 39.86678248, 0.0191442, 3.98667825, 0.05084609, -32.76497887, -0.00082281, -39.86678248, -0.0191442, -3.98667825, -0.05084609, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23006, 3006, 0.0, 122.45689847, 0.00997934, 122.45689847, 0.02993803, 85.71982893, -1364.05983774, 0.05, 2, 0, 73006, 24006, 2, 3)
    ops.uniaxialMaterial('LimitState', 43006, 30.61422462, 6.877e-05, 91.84267386, 0.00020632, 306.14224618, 0.00068775, -30.61422462, -6.877e-05, -91.84267386, -0.00020632, -306.14224618, -0.00068775, 0.4, 0.3, 0.003, 0.0, 0.0, 23006, 2)
    ops.limitCurve('ThreePoint', 13006, 3006, 0.0, 78.69942995, 0.0164562, 78.69942995, 0.04936861, 55.08960096, -494.17418771, 0.05, 2, 0, 73006, 24006, 1, 3)
    ops.uniaxialMaterial('LimitState', 33006, 19.67485749, 4.42e-05, 59.02457246, 0.0001326, 196.74857486, 0.000442, -19.67485749, -4.42e-05, -59.02457246, -0.0001326, -196.74857486, -0.000442, 0.4, 0.3, 0.003, 0.0, 0.0, 13006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3006, 99999, 'P', 43006, 'Vy', 33006, 'Vz', 23006, 'My', 13006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173006, 73006, 173006, 3006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124006, 124006, 24006, 3006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173007, 7.35, 4.4, 9.675)
    ops.node(124007, 7.35, 4.4, 12.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3007, 173007, 124007, 0.2275, 28556396.76498147, 11898498.65207561, 0.00616035, 0.00255464, 0.00881089, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23007, 142.85442716, 0.00046934, 174.32795757, 0.02630876, 17.43279576, 0.06964973, -142.85442716, -0.00046934, -174.32795757, -0.02630876, -17.43279576, -0.06964973, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13007, 61.52390762, 0.00063564, 75.07878733, 0.02259254, 7.50787873, 0.05204787, -61.52390762, -0.00063564, -75.07878733, -0.02259254, -7.50787873, -0.05204787, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23007, 3007, 0.0, 212.90092956, 0.00938682, 212.90092956, 0.02816045, 149.03065069, -2687.6503786, 0.05, 2, 0, 73007, 24007, 2, 3)
    ops.uniaxialMaterial('LimitState', 43007, 53.22523239, 7.433e-05, 159.67569717, 0.00022298, 532.25232389, 0.00074325, -53.22523239, -7.433e-05, -159.67569717, -0.00022298, -532.25232389, -0.00074325, 0.4, 0.3, 0.003, 0.0, 0.0, 23007, 2)
    ops.limitCurve('ThreePoint', 13007, 3007, 0.0, 148.73896658, 0.01271275, 148.73896658, 0.03813824, 104.11727661, -1061.15537872, 0.05, 2, 0, 73007, 24007, 1, 3)
    ops.uniaxialMaterial('LimitState', 33007, 37.18474164, 5.193e-05, 111.55422493, 0.00015578, 371.84741645, 0.00051926, -37.18474164, -5.193e-05, -111.55422493, -0.00015578, -371.84741645, -0.00051926, 0.4, 0.3, 0.003, 0.0, 0.0, 13007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3007, 99999, 'P', 43007, 'Vy', 33007, 'Vz', 23007, 'My', 13007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173007, 73007, 173007, 3007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124007, 124007, 24007, 3007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173008, 11.6, 4.4, 9.675)
    ops.node(124008, 11.6, 4.4, 12.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3008, 173008, 124008, 0.125, 28238947.50153174, 11766228.12563823, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23008, 61.34140823, 0.00050574, 74.9049353, 0.02788724, 7.49049353, 0.09151833, -61.34140823, -0.00050574, -74.9049353, -0.02788724, -7.49049353, -0.09151833, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13008, 24.50166652, 0.00080327, 29.91936114, 0.02291442, 2.99193611, 0.06123483, -24.50166652, -0.00080327, -29.91936114, -0.02291442, -2.99193611, -0.06123483, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23008, 3008, 0.0, 114.22612597, 0.01011472, 114.22612597, 0.03034417, 79.95828818, -2995.86195222, 0.05, 2, 0, 73008, 24008, 2, 3)
    ops.uniaxialMaterial('LimitState', 43008, 28.55653149, 7.339e-05, 85.66959448, 0.00022018, 285.56531492, 0.00073392, -28.55653149, -7.339e-05, -85.66959448, -0.00022018, -285.56531492, -0.00073392, 0.4, 0.3, 0.003, 0.0, 0.0, 23008, 2)
    ops.limitCurve('ThreePoint', 13008, 3008, 0.0, 88.5987826, 0.01606536, 88.5987826, 0.04819608, 62.01914782, -975.89531304, 0.05, 2, 0, 73008, 24008, 1, 3)
    ops.uniaxialMaterial('LimitState', 33008, 22.14969565, 5.693e-05, 66.44908695, 0.00017078, 221.49695649, 0.00056926, -22.14969565, -5.693e-05, -66.44908695, -0.00017078, -221.49695649, -0.00056926, 0.4, 0.3, 0.003, 0.0, 0.0, 13008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3008, 99999, 'P', 43008, 'Vy', 33008, 'Vz', 23008, 'My', 13008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173008, 73008, 173008, 3008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124008, 124008, 24008, 3008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173009, 0.0, 8.8, 9.675)
    ops.node(124009, 0.0, 8.8, 12.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3009, 173009, 124009, 0.0875, 28849828.05117931, 12020761.68799138, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23009, 31.85124733, 0.0006173, 38.83802882, 0.02872804, 3.88380288, 0.09266628, -31.85124733, -0.0006173, -38.83802882, -0.02872804, -3.88380288, -0.09266628, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13009, 19.70400904, 0.00079603, 24.02621358, 0.02600451, 2.40262136, 0.07537868, -19.70400904, -0.00079603, -24.02621358, -0.02600451, -2.40262136, -0.07537868, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23009, 3009, 0.0, 84.04554785, 0.01234601, 84.04554785, 0.03703804, 58.83188349, -2513.96742815, 0.05, 2, 0, 73009, 24009, 2, 3)
    ops.uniaxialMaterial('LimitState', 43009, 21.01138696, 7.551e-05, 63.03416089, 0.00022653, 210.11386962, 0.0007551, -21.01138696, -7.551e-05, -63.03416089, -0.00022653, -210.11386962, -0.0007551, 0.4, 0.3, 0.003, 0.0, 0.0, 23009, 2)
    ops.limitCurve('ThreePoint', 13009, 3009, 0.0, 73.24405986, 0.01592065, 73.24405986, 0.04776195, 51.2708419, -1416.70093925, 0.05, 2, 0, 73009, 24009, 1, 3)
    ops.uniaxialMaterial('LimitState', 33009, 18.31101496, 6.581e-05, 54.93304489, 0.00019742, 183.11014965, 0.00065806, -18.31101496, -6.581e-05, -54.93304489, -0.00019742, -183.11014965, -0.00065806, 0.4, 0.3, 0.003, 0.0, 0.0, 13009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3009, 99999, 'P', 43009, 'Vy', 33009, 'Vz', 23009, 'My', 13009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173009, 73009, 173009, 3009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124009, 124009, 24009, 3009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173010, 3.1, 8.8, 9.675)
    ops.node(124010, 3.1, 8.8, 12.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3010, 173010, 124010, 0.1375, 31096026.82304648, 12956677.84293604, 0.00204719, 0.00078776, 0.00381276, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23010, 81.00148259, 0.00048459, 98.11745681, 0.02618823, 9.81174568, 0.08159517, -81.00148259, -0.00048459, -98.11745681, -0.02618823, -9.81174568, -0.08159517, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13010, 31.62626231, 0.00078165, 38.30903246, 0.02127332, 3.83090325, 0.05364086, -31.62626231, -0.00078165, -38.30903246, -0.02127332, -3.83090325, -0.05364086, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23010, 3010, 0.0, 135.54959864, 0.00969181, 135.54959864, 0.02907543, 94.88471905, -1917.4821733, 0.05, 2, 0, 73010, 24010, 2, 3)
    ops.uniaxialMaterial('LimitState', 43010, 33.88739966, 7.19e-05, 101.66219898, 0.0002157, 338.87399659, 0.00071901, -33.88739966, -7.19e-05, -101.66219898, -0.0002157, -338.87399659, -0.00071901, 0.4, 0.3, 0.003, 0.0, 0.0, 23010, 2)
    ops.limitCurve('ThreePoint', 13010, 3010, 0.0, 96.49314839, 0.01563301, 96.49314839, 0.04689903, 67.54520388, -618.97620786, 0.05, 2, 0, 73010, 24010, 1, 3)
    ops.uniaxialMaterial('LimitState', 33010, 24.1232871, 5.118e-05, 72.3698613, 0.00015355, 241.23287099, 0.00051184, -24.1232871, -5.118e-05, -72.3698613, -0.00015355, -241.23287099, -0.00051184, 0.4, 0.3, 0.003, 0.0, 0.0, 13010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3010, 99999, 'P', 43010, 'Vy', 33010, 'Vz', 23010, 'My', 13010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173010, 73010, 173010, 3010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124010, 124010, 24010, 3010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173011, 7.35, 8.8, 9.675)
    ops.node(124011, 7.35, 8.8, 12.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3011, 173011, 124011, 0.2275, 30488544.4621688, 12703560.19257033, 0.00616035, 0.00255464, 0.00881089, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23011, 159.2786426, 0.00047327, 193.36655846, 0.02112648, 19.33665585, 0.0648663, -159.2786426, -0.00047327, -193.36655846, -0.02112648, -19.33665585, -0.0648663, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13011, 68.51063595, 0.00062172, 83.17289547, 0.01817167, 8.31728955, 0.04789807, -68.51063595, -0.00062172, -83.17289547, -0.01817167, -8.31728955, -0.04789807, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23011, 3011, 0.0, 216.95192651, 0.00946531, 216.95192651, 0.02839593, 151.86634856, -1806.1999736, 0.05, 2, 0, 73011, 24011, 2, 3)
    ops.uniaxialMaterial('LimitState', 43011, 54.23798163, 7.094e-05, 162.71394488, 0.00021282, 542.37981627, 0.0007094, -54.23798163, -7.094e-05, -162.71394488, -0.00021282, -542.37981627, -0.0007094, 0.4, 0.3, 0.003, 0.0, 0.0, 23011, 2)
    ops.limitCurve('ThreePoint', 13011, 3011, 0.0, 154.61644742, 0.01243432, 154.61644742, 0.03730295, 108.23151319, -757.98077976, 0.05, 2, 0, 73011, 24011, 1, 3)
    ops.uniaxialMaterial('LimitState', 33011, 38.65411185, 5.056e-05, 115.96233556, 0.00015167, 386.54111855, 0.00050557, -38.65411185, -5.056e-05, -115.96233556, -0.00015167, -386.54111855, -0.00050557, 0.4, 0.3, 0.003, 0.0, 0.0, 13011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3011, 99999, 'P', 43011, 'Vy', 33011, 'Vz', 23011, 'My', 13011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173011, 73011, 173011, 3011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124011, 124011, 24011, 3011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173012, 11.6, 8.8, 9.675)
    ops.node(124012, 11.6, 8.8, 12.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3012, 173012, 124012, 0.125, 28815020.79176477, 12006258.66323532, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23012, 62.6428429, 0.00050377, 76.38789863, 0.02586443, 7.63878986, 0.0897227, -62.6428429, -0.00050377, -76.38789863, -0.02586443, -7.63878986, -0.0897227, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13012, 24.94472726, 0.00078829, 30.41808463, 0.02126756, 3.04180846, 0.05972479, -24.94472726, -0.00078829, -30.41808463, -0.02126756, -3.04180846, -0.05972479, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23012, 3012, 0.0, 112.10648442, 0.01007542, 112.10648442, 0.03022625, 78.4745391, -2584.21673255, 0.05, 2, 0, 73012, 24012, 2, 3)
    ops.uniaxialMaterial('LimitState', 43012, 28.02662111, 7.059e-05, 84.07986332, 0.00021177, 280.26621106, 0.0007059, -28.02662111, -7.059e-05, -84.07986332, -0.00021177, -280.26621106, -0.0007059, 0.4, 0.3, 0.003, 0.0, 0.0, 23012, 2)
    ops.limitCurve('ThreePoint', 13012, 3012, 0.0, 88.53984661, 0.01576582, 88.53984661, 0.04729746, 61.97789263, -857.26492316, 0.05, 2, 0, 73012, 24012, 1, 3)
    ops.uniaxialMaterial('LimitState', 33012, 22.13496165, 5.575e-05, 66.40488496, 0.00016725, 221.34961653, 0.00055751, -22.13496165, -5.575e-05, -66.40488496, -0.00016725, -221.34961653, -0.00055751, 0.4, 0.3, 0.003, 0.0, 0.0, 13012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3012, 99999, 'P', 43012, 'Vy', 33012, 'Vz', 23012, 'My', 13012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173012, 73012, 173012, 3012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124012, 124012, 24012, 3012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173013, 0.0, 13.2, 9.675)
    ops.node(124013, 0.0, 13.2, 12.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3013, 173013, 124013, 0.0875, 25682464.47562659, 10701026.86484441, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23013, 31.90927349, 0.00062918, 39.1723408, 0.03010887, 3.91723408, 0.09267113, -31.90927349, -0.00062918, -39.1723408, -0.03010887, -3.91723408, -0.09267113, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13013, 19.65228255, 0.0008111, 24.12546026, 0.0272472, 2.41254603, 0.07555881, -19.65228255, -0.0008111, -24.12546026, -0.0272472, -2.41254603, -0.07555881, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23013, 3013, 0.0, 74.34598835, 0.01258356, 74.34598835, 0.03775068, 52.04219185, -2284.74836489, 0.05, 2, 0, 73013, 24013, 2, 3)
    ops.uniaxialMaterial('LimitState', 43013, 18.58649709, 7.503e-05, 55.75949126, 0.0002251, 185.86497088, 0.00075034, -18.58649709, -7.503e-05, -55.75949126, -0.0002251, -185.86497088, -0.00075034, 0.4, 0.3, 0.003, 0.0, 0.0, 23013, 2)
    ops.limitCurve('ThreePoint', 13013, 3013, 0.0, 64.12231576, 0.01622199, 64.12231576, 0.04866596, 44.88562103, -1293.6499995, 0.05, 2, 0, 73013, 24013, 1, 3)
    ops.uniaxialMaterial('LimitState', 33013, 16.03057894, 6.472e-05, 48.09173682, 0.00019415, 160.30578939, 0.00064715, -16.03057894, -6.472e-05, -48.09173682, -0.00019415, -160.30578939, -0.00064715, 0.4, 0.3, 0.003, 0.0, 0.0, 13013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3013, 99999, 'P', 43013, 'Vy', 33013, 'Vz', 23013, 'My', 13013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173013, 73013, 173013, 3013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124013, 124013, 24013, 3013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173014, 3.1, 13.2, 9.675)
    ops.node(124014, 3.1, 13.2, 12.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3014, 173014, 124014, 0.1375, 30854831.70625789, 12856179.87760746, 0.00204719, 0.00078776, 0.00381276, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23014, 83.04438911, 0.00049532, 100.66497794, 0.02513017, 10.06649779, 0.08046951, -83.04438911, -0.00049532, -100.66497794, -0.02513017, -10.06649779, -0.08046951, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13014, 32.37502623, 0.00080782, 39.2444491, 0.02044742, 3.92444491, 0.05277547, -32.37502623, -0.00080782, -39.2444491, -0.02044742, -3.92444491, -0.05277547, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23014, 3014, 0.0, 133.19832294, 0.00990635, 133.19832294, 0.02971904, 93.23882606, -1830.94309708, 0.05, 2, 0, 73014, 24014, 2, 3)
    ops.uniaxialMaterial('LimitState', 43014, 33.29958073, 7.121e-05, 99.8987422, 0.00021362, 332.99580734, 0.00071206, -33.29958073, -7.121e-05, -99.8987422, -0.00021362, -332.99580734, -0.00071206, 0.4, 0.3, 0.003, 0.0, 0.0, 23014, 2)
    ops.limitCurve('ThreePoint', 13014, 3014, 0.0, 92.05887122, 0.01615631, 92.05887122, 0.04846893, 64.44120985, -596.57546809, 0.05, 2, 0, 73014, 24014, 1, 3)
    ops.uniaxialMaterial('LimitState', 33014, 23.0147178, 4.921e-05, 69.04415341, 0.00014764, 230.14717804, 0.00049213, -23.0147178, -4.921e-05, -69.04415341, -0.00014764, -230.14717804, -0.00049213, 0.4, 0.3, 0.003, 0.0, 0.0, 13014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3014, 99999, 'P', 43014, 'Vy', 33014, 'Vz', 23014, 'My', 13014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173014, 73014, 173014, 3014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124014, 124014, 24014, 3014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173015, 7.35, 13.2, 9.675)
    ops.node(124015, 7.35, 13.2, 12.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3015, 173015, 124015, 0.2275, 28288923.7208566, 11787051.55035692, 0.00616035, 0.00255464, 0.00881089, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23015, 147.84796164, 0.0004728, 180.53984008, 0.02240526, 18.05398401, 0.06569457, -147.84796164, -0.0004728, -180.53984008, -0.02240526, -18.05398401, -0.06569457, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13015, 63.48935076, 0.00063477, 77.52800314, 0.01927175, 7.75280031, 0.04869197, -63.48935076, -0.00063477, -77.52800314, -0.01927175, -7.75280031, -0.04869197, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23015, 3015, 0.0, 196.72691429, 0.009456, 196.72691429, 0.02836799, 137.70884, -1744.88812032, 0.05, 2, 0, 73015, 24015, 2, 3)
    ops.uniaxialMaterial('LimitState', 43015, 49.18172857, 6.933e-05, 147.54518572, 0.00020798, 491.81728572, 0.00069328, -49.18172857, -6.933e-05, -147.54518572, -0.00020798, -491.81728572, -0.00069328, 0.4, 0.3, 0.003, 0.0, 0.0, 23015, 2)
    ops.limitCurve('ThreePoint', 13015, 3015, 0.0, 139.51859506, 0.01269531, 139.51859506, 0.03808593, 97.66301654, -736.56283764, 0.05, 2, 0, 73015, 24015, 1, 3)
    ops.uniaxialMaterial('LimitState', 33015, 34.87964876, 4.917e-05, 104.63894629, 0.0001475, 348.79648765, 0.00049167, -34.87964876, -4.917e-05, -104.63894629, -0.0001475, -348.79648765, -0.00049167, 0.4, 0.3, 0.003, 0.0, 0.0, 13015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3015, 99999, 'P', 43015, 'Vy', 33015, 'Vz', 23015, 'My', 13015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173015, 73015, 173015, 3015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124015, 124015, 24015, 3015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173016, 11.6, 13.2, 9.675)
    ops.node(124016, 11.6, 13.2, 12.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3016, 173016, 124016, 0.125, 29721660.9941299, 12384025.41422079, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23016, 64.26366893, 0.00049817, 78.17910589, 0.02330361, 7.81791059, 0.08745826, -64.26366893, -0.00049817, -78.17910589, -0.02330361, -7.81791059, -0.08745826, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13016, 25.54230777, 0.00076164, 31.07315248, 0.01917752, 3.10731525, 0.05781323, -25.54230777, -0.00076164, -31.07315248, -0.01917752, -3.10731525, -0.05781323, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23016, 3016, 0.0, 110.26753239, 0.00996346, 110.26753239, 0.02989039, 77.18727268, -2104.5287529, 0.05, 2, 0, 73016, 24016, 2, 3)
    ops.uniaxialMaterial('LimitState', 43016, 27.5668831, 6.731e-05, 82.70064929, 0.00020194, 275.66883098, 0.00067314, -27.5668831, -6.731e-05, -82.70064929, -0.00020194, -275.66883098, -0.00067314, 0.4, 0.3, 0.003, 0.0, 0.0, 23016, 2)
    ops.limitCurve('ThreePoint', 13016, 3016, 0.0, 84.66407873, 0.01523277, 84.66407873, 0.04569832, 59.26485511, -718.18974522, 0.05, 2, 0, 73016, 24016, 1, 3)
    ops.uniaxialMaterial('LimitState', 33016, 21.16601968, 5.168e-05, 63.49805905, 0.00015505, 211.66019682, 0.00051684, -21.16601968, -5.168e-05, -63.49805905, -0.00015505, -211.66019682, -0.00051684, 0.4, 0.3, 0.003, 0.0, 0.0, 13016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3016, 99999, 'P', 43016, 'Vy', 33016, 'Vz', 23016, 'My', 13016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173016, 73016, 173016, 3016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124016, 124016, 24016, 3016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173017, 0.0, 17.6, 9.675)
    ops.node(124017, 0.0, 17.6, 12.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3017, 173017, 124017, 0.0875, 26109851.63553866, 10879104.84814111, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23017, 31.06951799, 0.00062441, 38.11201305, 0.02506211, 3.8112013, 0.08785149, -31.06951799, -0.00062441, -38.11201305, -0.02506211, -3.8112013, -0.08785149, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13017, 19.18157656, 0.00080872, 23.5294444, 0.02272337, 2.35294444, 0.07121038, -19.18157656, -0.00080872, -23.5294444, -0.02272337, -2.35294444, -0.07121038, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23017, 3017, 0.0, 67.42996733, 0.01248828, 67.42996733, 0.03746485, 47.20097713, -1492.7635704, 0.05, 2, 0, 73017, 24017, 2, 3)
    ops.uniaxialMaterial('LimitState', 43017, 16.85749183, 6.694e-05, 50.5724755, 0.00020082, 168.57491832, 0.0006694, -16.85749183, -6.694e-05, -50.5724755, -0.00020082, -168.57491832, -0.0006694, 0.4, 0.3, 0.003, 0.0, 0.0, 23017, 2)
    ops.limitCurve('ThreePoint', 13017, 3017, 0.0, 55.80822748, 0.0161744, 55.80822748, 0.0485232, 39.06575923, -865.68526993, 0.05, 2, 0, 73017, 24017, 1, 3)
    ops.uniaxialMaterial('LimitState', 33017, 13.95205687, 5.54e-05, 41.85617061, 0.00016621, 139.52056869, 0.00055402, -13.95205687, -5.54e-05, -41.85617061, -0.00016621, -139.52056869, -0.00055402, 0.4, 0.3, 0.003, 0.0, 0.0, 13017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3017, 99999, 'P', 43017, 'Vy', 33017, 'Vz', 23017, 'My', 13017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173017, 73017, 173017, 3017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124017, 124017, 24017, 3017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173018, 3.1, 17.6, 9.675)
    ops.node(124018, 3.1, 17.6, 12.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3018, 173018, 124018, 0.1375, 30098005.68731456, 12540835.70304773, 0.00204719, 0.00078776, 0.00381276, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23018, 82.19089292, 0.00049544, 99.84739393, 0.02951815, 9.98473939, 0.09308583, -82.19089292, -0.00049544, -99.84739393, -0.02951815, -9.98473939, -0.09308583, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13018, 32.00002471, 0.00081067, 38.87436867, 0.0236469, 3.88743687, 0.05964416, -32.00002471, -0.00081067, -38.87436867, -0.0236469, -3.88743687, -0.05964416, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23018, 3018, 0.0, 135.30892626, 0.00990877, 135.30892626, 0.0297263, 94.71624838, -2238.57070698, 0.05, 2, 0, 73018, 24018, 2, 3)
    ops.uniaxialMaterial('LimitState', 43018, 33.82723156, 7.415e-05, 101.48169469, 0.00022246, 338.27231564, 0.00074153, -33.82723156, -7.415e-05, -101.48169469, -0.00022246, -338.27231564, -0.00074153, 0.4, 0.3, 0.003, 0.0, 0.0, 23018, 2)
    ops.limitCurve('ThreePoint', 13018, 3018, 0.0, 98.84957499, 0.01621342, 98.84957499, 0.04864026, 69.19470249, -701.2573976, 0.05, 2, 0, 73018, 24018, 1, 3)
    ops.uniaxialMaterial('LimitState', 33018, 24.71239375, 5.417e-05, 74.13718124, 0.00016252, 247.12393747, 0.00054172, -24.71239375, -5.417e-05, -74.13718124, -0.00016252, -247.12393747, -0.00054172, 0.4, 0.3, 0.003, 0.0, 0.0, 13018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3018, 99999, 'P', 43018, 'Vy', 33018, 'Vz', 23018, 'My', 13018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173018, 73018, 173018, 3018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124018, 124018, 24018, 3018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173019, 7.35, 17.6, 9.675)
    ops.node(124019, 7.35, 17.6, 12.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3019, 173019, 124019, 0.2275, 28852692.34581239, 12021955.1440885, 0.00616035, 0.00255464, 0.00881089, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23019, 146.87383837, 0.00046499, 179.10257042, 0.02548618, 17.91025704, 0.06890485, -146.87383837, -0.00046499, -179.10257042, -0.02548618, -17.91025704, -0.06890485, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13019, 63.12175424, 0.0006168, 76.97264917, 0.02187841, 7.69726492, 0.05138655, -63.12175424, -0.0006168, -76.97264917, -0.02187841, -7.69726492, -0.05138655, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23019, 3019, 0.0, 210.32420732, 0.00929983, 210.32420732, 0.02789948, 147.22694512, -2323.49189781, 0.05, 2, 0, 73019, 24019, 2, 3)
    ops.uniaxialMaterial('LimitState', 43019, 52.58105183, 7.267e-05, 157.74315549, 0.00021801, 525.81051829, 0.00072672, -52.58105183, -7.267e-05, -157.74315549, -0.00021801, -525.81051829, -0.00072672, 0.4, 0.3, 0.003, 0.0, 0.0, 23019, 2)
    ops.limitCurve('ThreePoint', 13019, 3019, 0.0, 147.89870513, 0.01233598, 147.89870513, 0.03700795, 103.52909359, -936.50721667, 0.05, 2, 0, 73019, 24019, 1, 3)
    ops.uniaxialMaterial('LimitState', 33019, 36.97467628, 5.11e-05, 110.92402884, 0.00015331, 369.74676281, 0.00051102, -36.97467628, -5.11e-05, -110.92402884, -0.00015331, -369.74676281, -0.00051102, 0.4, 0.3, 0.003, 0.0, 0.0, 13019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3019, 99999, 'P', 43019, 'Vy', 33019, 'Vz', 23019, 'My', 13019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173019, 73019, 173019, 3019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124019, 124019, 24019, 3019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173020, 11.6, 17.6, 9.675)
    ops.node(124020, 11.6, 17.6, 12.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3020, 173020, 124020, 0.125, 29338774.27776011, 12224489.28240005, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23020, 63.87386725, 0.00051644, 77.78453612, 0.02357044, 7.77845361, 0.0876046, -63.87386725, -0.00051644, -77.78453612, -0.02357044, -7.77845361, -0.0876046, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13020, 25.51291437, 0.00082407, 31.06920396, 0.01944067, 3.1069204, 0.05800381, -25.51291437, -0.00082407, -31.06920396, -0.01944067, -3.1069204, -0.05800381, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23020, 3020, 0.0, 109.82802912, 0.01032885, 109.82802912, 0.03098655, 76.87962038, -2191.52180712, 0.05, 2, 0, 73020, 24020, 2, 3)
    ops.uniaxialMaterial('LimitState', 43020, 27.45700728, 6.792e-05, 82.37102184, 0.00020376, 274.57007279, 0.00067921, -27.45700728, -6.792e-05, -82.37102184, -0.00020376, -274.57007279, -0.00067921, 0.4, 0.3, 0.003, 0.0, 0.0, 23020, 2)
    ops.limitCurve('ThreePoint', 13020, 3020, 0.0, 84.75020507, 0.01648133, 84.75020507, 0.04944398, 59.32514355, -743.56220884, 0.05, 2, 0, 73020, 24020, 1, 3)
    ops.uniaxialMaterial('LimitState', 33020, 21.18755127, 5.241e-05, 63.5626538, 0.00015724, 211.87551268, 0.00052412, -21.18755127, -5.241e-05, -63.5626538, -0.00015724, -211.87551268, -0.00052412, 0.4, 0.3, 0.003, 0.0, 0.0, 13020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3020, 99999, 'P', 43020, 'Vy', 33020, 'Vz', 23020, 'My', 13020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173020, 73020, 173020, 3020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124020, 124020, 24020, 3020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173021, 0.0, 22.0, 9.675)
    ops.node(124021, 0.0, 22.0, 12.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3021, 173021, 124021, 0.0625, 28975582.9105846, 12073159.54607692, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23021, 13.97494121, 0.00080856, 17.04161108, 0.02751872, 1.70416111, 0.092241, -13.97494121, -0.00080856, -17.04161108, -0.02751872, -1.70416111, -0.092241, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13021, 13.97494121, 0.00080856, 17.04161108, 0.02751872, 1.70416111, 0.092241, -13.97494121, -0.00080856, -17.04161108, -0.02751872, -1.70416111, -0.092241, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23021, 3021, 0.0, 56.50660347, 0.01617116, 56.50660347, 0.04851349, 39.55462243, -1790.8042981, 0.05, 2, 0, 73021, 24021, 2, 3)
    ops.uniaxialMaterial('LimitState', 43021, 14.12665087, 7.077e-05, 42.3799526, 0.0002123, 141.26650868, 0.00070767, -14.12665087, -7.077e-05, -42.3799526, -0.0002123, -141.26650868, -0.00070767, 0.4, 0.3, 0.003, 0.0, 0.0, 23021, 2)
    ops.limitCurve('ThreePoint', 13021, 3021, 0.0, 56.50660347, 0.01617116, 56.50660347, 0.04851349, 39.55462243, -1790.8042981, 0.05, 2, 0, 73021, 24021, 1, 3)
    ops.uniaxialMaterial('LimitState', 33021, 14.12665087, 7.077e-05, 42.3799526, 0.0002123, 141.26650868, 0.00070767, -14.12665087, -7.077e-05, -42.3799526, -0.0002123, -141.26650868, -0.00070767, 0.4, 0.3, 0.003, 0.0, 0.0, 13021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3021, 99999, 'P', 43021, 'Vy', 33021, 'Vz', 23021, 'My', 13021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173021, 73021, 173021, 3021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124021, 124021, 24021, 3021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173022, 3.1, 22.0, 9.675)
    ops.node(124022, 3.1, 22.0, 12.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3022, 173022, 124022, 0.0875, 28684934.03595847, 11952055.84831603, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23022, 25.58583673, 0.00081671, 31.20008154, 0.02696618, 3.12000815, 0.0757811, -25.58583673, -0.00081671, -31.20008154, -0.02696618, -3.12000815, -0.0757811, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13022, 37.65517228, 0.00063336, 45.91776528, 0.02979343, 4.59177653, 0.09300746, -37.65517228, -0.00063336, -45.91776528, -0.02979343, -4.59177653, -0.09300746, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23022, 3022, 0.0, 63.0989682, 0.01633416, 63.0989682, 0.04900249, 44.16927774, -772.08685369, 0.05, 2, 0, 73022, 24022, 2, 3)
    ops.uniaxialMaterial('LimitState', 43022, 15.77474205, 5.702e-05, 47.32422615, 0.00017105, 157.74742049, 0.00057017, -15.77474205, -5.702e-05, -47.32422615, -0.00017105, -157.74742049, -0.00057017, 0.4, 0.3, 0.003, 0.0, 0.0, 23022, 2)
    ops.limitCurve('ThreePoint', 13022, 3022, 0.0, 74.15663499, 0.01266722, 74.15663499, 0.03800167, 51.90964449, -1301.31038164, 0.05, 2, 0, 73022, 24022, 1, 3)
    ops.uniaxialMaterial('LimitState', 33022, 18.53915875, 6.701e-05, 55.61747624, 0.00020103, 185.39158746, 0.00067009, -18.53915875, -6.701e-05, -55.61747624, -0.00020103, -185.39158746, -0.00067009, 0.4, 0.3, 0.003, 0.0, 0.0, 13022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3022, 99999, 'P', 43022, 'Vy', 33022, 'Vz', 23022, 'My', 13022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173022, 73022, 173022, 3022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124022, 124022, 24022, 3022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173023, 7.35, 22.0, 9.675)
    ops.node(124023, 7.35, 22.0, 12.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3023, 173023, 124023, 0.175, 29578212.84340128, 12324255.3514172, 0.00405757, 0.00401042, 0.0019651, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23023, 50.27957584, 0.00065988, 61.21368887, 0.03290925, 6.12136889, 0.0783756, -50.27957584, -0.00065988, -61.21368887, -0.03290925, -6.12136889, -0.0783756, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13023, 83.18699326, 0.00053397, 101.2773604, 0.03660115, 10.12773604, 0.09588719, -83.18699326, -0.00053397, -101.2773604, -0.03660115, -10.12773604, -0.09588719, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23023, 3023, 0.0, 141.34628485, 0.01319769, 141.34628485, 0.03959308, 98.94239939, -2657.50820026, 0.05, 2, 0, 73023, 24023, 2, 3)
    ops.uniaxialMaterial('LimitState', 43023, 35.33657121, 6.193e-05, 106.00971364, 0.0001858, 353.36571212, 0.00061932, -35.33657121, -6.193e-05, -106.00971364, -0.0001858, -353.36571212, -0.00061932, 0.4, 0.3, 0.003, 0.0, 0.0, 23023, 2)
    ops.limitCurve('ThreePoint', 13023, 3023, 0.0, 162.77244633, 0.0106794, 162.77244633, 0.0320382, 113.94071243, -4938.31997895, 0.05, 2, 0, 73023, 24023, 1, 3)
    ops.uniaxialMaterial('LimitState', 33023, 40.69311158, 7.132e-05, 122.07933475, 0.00021396, 406.93111584, 0.0007132, -40.69311158, -7.132e-05, -122.07933475, -0.00021396, -406.93111584, -0.0007132, 0.4, 0.3, 0.003, 0.0, 0.0, 13023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3023, 99999, 'P', 43023, 'Vy', 33023, 'Vz', 23023, 'My', 13023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173023, 73023, 173023, 3023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124023, 124023, 24023, 3023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173024, 11.6, 22.0, 9.675)
    ops.node(124024, 11.6, 22.0, 12.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3024, 173024, 124024, 0.0625, 32946150.86175956, 13727562.85906648, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23024, 15.52243127, 0.00072017, 18.6929236, 0.02685861, 1.86929236, 0.09174708, -15.52243127, -0.00072017, -18.6929236, -0.02685861, -1.86929236, -0.09174708, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13024, 15.52243127, 0.00072017, 18.6929236, 0.02685861, 1.86929236, 0.09174708, -15.52243127, -0.00072017, -18.6929236, -0.02685861, -1.86929236, -0.09174708, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23024, 3024, 0.0, 66.85625121, 0.01440344, 66.85625121, 0.04321033, 46.79937585, -1616.12992916, 0.05, 2, 0, 73024, 24024, 2, 3)
    ops.uniaxialMaterial('LimitState', 43024, 16.7140628, 7.364e-05, 50.14218841, 0.00022091, 167.14062803, 0.00073638, -16.7140628, -7.364e-05, -50.14218841, -0.00022091, -167.14062803, -0.00073638, 0.4, 0.3, 0.003, 0.0, 0.0, 23024, 2)
    ops.limitCurve('ThreePoint', 13024, 3024, 0.0, 66.85625121, 0.01440344, 66.85625121, 0.04321033, 46.79937585, -1616.12992916, 0.05, 2, 0, 73024, 24024, 1, 3)
    ops.uniaxialMaterial('LimitState', 33024, 16.7140628, 7.364e-05, 50.14218841, 0.00022091, 167.14062803, 0.00073638, -16.7140628, -7.364e-05, -50.14218841, -0.00022091, -167.14062803, -0.00073638, 0.4, 0.3, 0.003, 0.0, 0.0, 13024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3024, 99999, 'P', 43024, 'Vy', 33024, 'Vz', 23024, 'My', 13024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173024, 73024, 173024, 3024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124024, 124024, 24024, 3024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170001, 0.0, 0.0, 0.0)
    ops.node(124025, 0.0, 0.0, 1.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4063, 170001, 124025, 0.0625, 27293166.79645327, 11372152.83185553, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24063, 38.03457252, 0.00067246, 46.02681329, 0.03801803, 4.60268133, 0.1076371, -38.03457252, -0.00067246, -46.02681329, -0.03801803, -4.60268133, -0.1076371, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14063, 33.05478599, 0.00067246, 40.00061949, 0.03801803, 4.00006195, 0.1076371, -33.05478599, -0.00067246, -40.00061949, -0.03801803, -4.00006195, -0.1076371, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24063, 4063, 0.0, 75.43025963, 0.01344915, 75.43025963, 0.04034746, 52.80118174, -2071.07774158, 0.05, 2, 0, 70001, 24025, 2, 3)
    ops.uniaxialMaterial('LimitState', 44063, 18.85756491, 5.014e-05, 56.57269472, 0.00015043, 188.57564906, 0.00050145, -18.85756491, -5.014e-05, -56.57269472, -0.00015043, -188.57564906, -0.00050145, 0.4, 0.3, 0.003, 0.0, 0.0, 24063, 2)
    ops.limitCurve('ThreePoint', 14063, 4063, 0.0, 75.43025963, 0.01344915, 75.43025963, 0.04034746, 52.80118174, -2071.07774158, 0.05, 2, 0, 70001, 24025, 1, 3)
    ops.uniaxialMaterial('LimitState', 34063, 18.85756491, 5.014e-05, 56.57269472, 0.00015043, 188.57564906, 0.00050145, -18.85756491, -5.014e-05, -56.57269472, -0.00015043, -188.57564906, -0.00050145, 0.4, 0.3, 0.003, 0.0, 0.0, 14063, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4063, 99999, 'P', 44063, 'Vy', 34063, 'Vz', 24063, 'My', 14063, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170001, 70001, 170001, 4063, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124025, 124025, 24025, 4063, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174025, 0.0, 0.0, 1.8)
    ops.node(121001, 0.0, 0.0, 2.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4064, 174025, 121001, 0.0625, 28507066.29469013, 11877944.28945422, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24064, 36.05264242, 0.00064319, 43.6600576, 0.05851614, 4.36600576, 0.15851614, -36.05264242, -0.00064319, -43.6600576, -0.05851614, -4.36600576, -0.15851614, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14064, 31.08487966, 0.00064319, 37.64405451, 0.05851614, 3.76440545, 0.15851614, -31.08487966, -0.00064319, -37.64405451, -0.05851614, -3.76440545, -0.15851614, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24064, 4064, 0.0, 106.41055281, 0.01286383, 106.41055281, 0.03859148, 74.48738697, -5006.40021262, 0.05, 2, 0, 74025, 21001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44064, 26.6026382, 6.773e-05, 79.80791461, 0.00020318, 266.02638203, 0.00067728, -26.6026382, -6.773e-05, -79.80791461, -0.00020318, -266.02638203, -0.00067728, 0.4, 0.3, 0.003, 0.0, 0.0, 24064, 2)
    ops.limitCurve('ThreePoint', 14064, 4064, 0.0, 106.41055281, 0.01286383, 106.41055281, 0.03859148, 74.48738697, -5006.40021262, 0.05, 2, 0, 74025, 21001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34064, 26.6026382, 6.773e-05, 79.80791461, 0.00020318, 266.02638203, 0.00067728, -26.6026382, -6.773e-05, -79.80791461, -0.00020318, -266.02638203, -0.00067728, 0.4, 0.3, 0.003, 0.0, 0.0, 14064, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4064, 99999, 'P', 44064, 'Vy', 34064, 'Vz', 24064, 'My', 14064, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174025, 74025, 174025, 4064, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121001, 121001, 21001, 4064, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170002, 3.1, 0.0, 0.0)
    ops.node(124026, 3.1, 0.0, 1.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4065, 170002, 124026, 0.175, 26457465.97396301, 11023944.15581792, 0.00405757, 0.00401042, 0.0019651, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24065, 164.70298231, 0.00058729, 200.15201788, 0.06435036, 20.01520179, 0.16435036, -164.70298231, -0.00058729, -200.15201788, -0.06435036, -20.01520179, -0.16435036, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14065, 179.4597575, 0.00052696, 218.08489492, 0.0566349, 21.80848949, 0.135856, -179.4597575, -0.00052696, -218.08489492, -0.0566349, -21.80848949, -0.135856, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24065, 4065, 0.0, 224.90330949, 0.01174573, 224.90330949, 0.0352372, 157.43231664, -4964.51260258, 0.05, 2, 0, 70002, 24026, 2, 3)
    ops.uniaxialMaterial('LimitState', 44065, 56.22582737, 5.508e-05, 168.67748212, 0.00016525, 562.25827372, 0.00055084, -56.22582737, -5.508e-05, -168.67748212, -0.00016525, -562.25827372, -0.00055084, 0.4, 0.3, 0.003, 0.0, 0.0, 24065, 2)
    ops.limitCurve('ThreePoint', 14065, 4065, 0.0, 434.52773575, 0.01053911, 434.52773575, 0.03161734, 304.16941502, -21617.13572472, 0.05, 2, 0, 70002, 24026, 1, 3)
    ops.uniaxialMaterial('LimitState', 34065, 108.63193394, 0.00010643, 325.89580181, 0.00031928, 1086.31933936, 0.00106425, -108.63193394, -0.00010643, -325.89580181, -0.00031928, -1086.31933936, -0.00106425, 0.4, 0.3, 0.003, 0.0, 0.0, 14065, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4065, 99999, 'P', 44065, 'Vy', 34065, 'Vz', 24065, 'My', 14065, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170002, 70002, 170002, 4065, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124026, 124026, 24026, 4065, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174026, 3.1, 0.0, 1.8)
    ops.node(121002, 3.1, 0.0, 2.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4066, 174026, 121002, 0.175, 30497822.19991756, 12707425.91663232, 0.00405757, 0.00401042, 0.0019651, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24066, 83.26755313, 0.00054723, 100.59251507, 0.05278951, 10.05925151, 0.14782655, -83.26755313, -0.00054723, -100.59251507, -0.05278951, -10.05925151, -0.14782655, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14066, 132.03046056, 0.00050152, 159.50121739, 0.05180019, 15.95012174, 0.14281572, -132.03046056, -0.00050152, -159.50121739, -0.05180019, -15.95012174, -0.14281572, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24066, 4066, 0.0, 257.84032236, 0.01094466, 257.84032236, 0.03283397, 180.48822565, -5538.38996882, 0.05, 2, 0, 74026, 21002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44066, 64.46008059, 5.478e-05, 193.38024177, 0.00016435, 644.60080591, 0.00054784, -64.46008059, -5.478e-05, -193.38024177, -0.00016435, -644.60080591, -0.00054784, 0.4, 0.3, 0.003, 0.0, 0.0, 24066, 2)
    ops.limitCurve('ThreePoint', 14066, 4066, 0.0, 427.25436247, 0.0100303, 427.25436247, 0.0300909, 299.07805373, -16276.53858815, 0.05, 2, 0, 74026, 21002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34066, 106.81359062, 9.078e-05, 320.44077185, 0.00027234, 1068.13590617, 0.00090781, -106.81359062, -9.078e-05, -320.44077185, -0.00027234, -1068.13590617, -0.00090781, 0.4, 0.3, 0.003, 0.0, 0.0, 14066, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4066, 99999, 'P', 44066, 'Vy', 34066, 'Vz', 24066, 'My', 14066, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174026, 74026, 174026, 4066, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121002, 121002, 21002, 4066, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171001, 0.0, 0.0, 3.375)
    ops.node(124027, 0.0, 0.0, 4.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4068, 171001, 124027, 0.0625, 30074904.86349335, 12531210.3597889, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24068, 35.434325, 0.00064612, 42.81928212, 0.05779665, 4.28192821, 0.15779665, -35.434325, -0.00064612, -42.81928212, -0.05779665, -4.28192821, -0.15779665, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14068, 30.65898995, 0.00064612, 37.04870744, 0.05779665, 3.70487074, 0.15779665, -30.65898995, -0.00064612, -37.04870744, -0.05779665, -3.70487074, -0.15779665, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24068, 4068, 0.0, 103.39920455, 0.01292245, 103.39920455, 0.03876735, 72.37944318, -4634.52830518, 0.05, 2, 0, 71001, 24027, 2, 3)
    ops.uniaxialMaterial('LimitState', 44068, 25.84980114, 6.238e-05, 77.54940341, 0.00018714, 258.49801137, 0.0006238, -25.84980114, -6.238e-05, -77.54940341, -0.00018714, -258.49801137, -0.0006238, 0.4, 0.3, 0.003, 0.0, 0.0, 24068, 2)
    ops.limitCurve('ThreePoint', 14068, 4068, 0.0, 103.39920455, 0.01292245, 103.39920455, 0.03876735, 72.37944318, -4634.52830518, 0.05, 2, 0, 71001, 24027, 1, 3)
    ops.uniaxialMaterial('LimitState', 34068, 25.84980114, 6.238e-05, 77.54940341, 0.00018714, 258.49801137, 0.0006238, -25.84980114, -6.238e-05, -77.54940341, -0.00018714, -258.49801137, -0.0006238, 0.4, 0.3, 0.003, 0.0, 0.0, 14068, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4068, 99999, 'P', 44068, 'Vy', 34068, 'Vz', 24068, 'My', 14068, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171001, 71001, 171001, 4068, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124027, 124027, 24027, 4068, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174027, 0.0, 0.0, 4.95)
    ops.node(122001, 0.0, 0.0, 6.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4069, 174027, 122001, 0.0625, 27992140.07958784, 11663391.69982827, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24069, 26.88574891, 0.00064646, 32.68057288, 0.05797227, 3.26805729, 0.15797227, -26.88574891, -0.00064646, -32.68057288, -0.05797227, -3.26805729, -0.15797227, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14069, 24.65206747, 0.00064646, 29.96545458, 0.05797227, 2.99654546, 0.15797227, -24.65206747, -0.00064646, -29.96545458, -0.05797227, -2.99654546, -0.15797227, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24069, 4069, 0.0, 94.45185977, 0.01292921, 94.45185977, 0.03878763, 66.11630184, -4925.80955351, 0.05, 2, 0, 74027, 22001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44069, 23.61296494, 6.122e-05, 70.83889483, 0.00018367, 236.12964943, 0.00061222, -23.61296494, -6.122e-05, -70.83889483, -0.00018367, -236.12964943, -0.00061222, 0.4, 0.3, 0.003, 0.0, 0.0, 24069, 2)
    ops.limitCurve('ThreePoint', 14069, 4069, 0.0, 94.45185977, 0.01292921, 94.45185977, 0.03878763, 66.11630184, -4925.80955351, 0.05, 2, 0, 74027, 22001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34069, 23.61296494, 6.122e-05, 70.83889483, 0.00018367, 236.12964943, 0.00061222, -23.61296494, -6.122e-05, -70.83889483, -0.00018367, -236.12964943, -0.00061222, 0.4, 0.3, 0.003, 0.0, 0.0, 14069, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4069, 99999, 'P', 44069, 'Vy', 34069, 'Vz', 24069, 'My', 14069, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174027, 74027, 174027, 4069, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122001, 122001, 22001, 4069, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171002, 3.1, 0.0, 3.375)
    ops.node(124028, 3.1, 0.0, 4.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4070, 171002, 124028, 0.175, 28983819.67279368, 12076591.5303307, 0.00405757, 0.00401042, 0.0019651, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24070, 81.8940698, 0.00055848, 99.39509224, 0.05400323, 9.93950922, 0.14984859, -81.8940698, -0.00055848, -99.39509224, -0.05400323, -9.93950922, -0.14984859, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14070, 110.46865043, 0.00050759, 134.07615138, 0.05298702, 13.40761514, 0.14477667, -110.46865043, -0.00050759, -134.07615138, -0.05298702, -13.40761514, -0.14477667, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24070, 4070, 0.0, 229.96454592, 0.0111696, 229.96454592, 0.03350879, 160.97518214, -4998.37957892, 0.05, 2, 0, 71002, 24028, 2, 3)
    ops.uniaxialMaterial('LimitState', 44070, 57.49113648, 5.141e-05, 172.47340944, 0.00015424, 574.91136479, 0.00051414, -57.49113648, -5.141e-05, -172.47340944, -0.00015424, -574.91136479, -0.00051414, 0.4, 0.3, 0.003, 0.0, 0.0, 24070, 2)
    ops.limitCurve('ThreePoint', 14070, 4070, 0.0, 380.33814496, 0.01015182, 380.33814496, 0.03045546, 266.23670147, -15101.89526883, 0.05, 2, 0, 71002, 24028, 1, 3)
    ops.uniaxialMaterial('LimitState', 34070, 95.08453624, 8.503e-05, 285.25360872, 0.0002551, 950.8453624, 0.00085033, -95.08453624, -8.503e-05, -285.25360872, -0.0002551, -950.8453624, -0.00085033, 0.4, 0.3, 0.003, 0.0, 0.0, 14070, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4070, 99999, 'P', 44070, 'Vy', 34070, 'Vz', 24070, 'My', 14070, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171002, 71002, 171002, 4070, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124028, 124028, 24028, 4070, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174028, 3.1, 0.0, 4.95)
    ops.node(122002, 3.1, 0.0, 6.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4071, 174028, 122002, 0.175, 30008327.53956894, 12503469.80815372, 0.00405757, 0.00401042, 0.0019651, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24071, 73.43378981, 0.00050717, 88.98089031, 0.05355866, 8.89808903, 0.1530828, -73.43378981, -0.00050717, -88.98089031, -0.05355866, -8.89808903, -0.1530828, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14071, 98.73819248, 0.00047213, 119.64263723, 0.0525654, 11.96426372, 0.14787816, -98.73819248, -0.00047213, -119.64263723, -0.0525654, -11.96426372, -0.14787816, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24071, 4071, 0.0, 231.21594456, 0.01014349, 231.21594456, 0.03043048, 161.85116119, -4923.22291476, 0.05, 2, 0, 74028, 22002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44071, 57.80398614, 4.993e-05, 173.41195842, 0.00014979, 578.03986139, 0.00049929, -57.80398614, -4.993e-05, -173.41195842, -0.00014979, -578.03986139, -0.00049929, 0.4, 0.3, 0.003, 0.0, 0.0, 24071, 2)
    ops.limitCurve('ThreePoint', 14071, 4071, 0.0, 379.74948547, 0.0094426, 379.74948547, 0.02832779, 265.82463983, -15259.41203794, 0.05, 2, 0, 74028, 22002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34071, 94.93737137, 8.2e-05, 284.8121141, 0.00024601, 949.37371367, 0.00082003, -94.93737137, -8.2e-05, -284.8121141, -0.00024601, -949.37371367, -0.00082003, 0.4, 0.3, 0.003, 0.0, 0.0, 14071, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4071, 99999, 'P', 44071, 'Vy', 34071, 'Vz', 24071, 'My', 14071, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174028, 74028, 174028, 4071, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122002, 122002, 22002, 4071, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172001, 0.0, 0.0, 6.525)
    ops.node(124029, 0.0, 0.0, 7.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4073, 172001, 124029, 0.0625, 30094446.48642823, 12539352.70267843, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24073, 20.1613602, 0.00058714, 24.41931568, 0.05504013, 2.44193157, 0.15504013, -20.1613602, -0.00058714, -24.41931568, -0.05504013, -2.44193157, -0.15504013, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14073, 20.1613602, 0.00058714, 24.41931568, 0.05504013, 2.44193157, 0.15504013, -20.1613602, -0.00058714, -24.41931568, -0.05504013, -2.44193157, -0.15504013, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24073, 4073, 0.0, 95.76281349, 0.01174278, 95.76281349, 0.03522833, 67.03396944, -5073.03540952, 0.05, 2, 0, 72001, 24029, 2, 3)
    ops.uniaxialMaterial('LimitState', 44073, 23.94070337, 5.774e-05, 71.82211012, 0.00017321, 239.40703373, 0.00057736, -23.94070337, -5.774e-05, -71.82211012, -0.00017321, -239.40703373, -0.00057736, 0.4, 0.3, 0.003, 0.0, 0.0, 24073, 2)
    ops.limitCurve('ThreePoint', 14073, 4073, 0.0, 95.76281349, 0.01174278, 95.76281349, 0.03522833, 67.03396944, -5073.03540952, 0.05, 2, 0, 72001, 24029, 1, 3)
    ops.uniaxialMaterial('LimitState', 34073, 23.94070337, 5.774e-05, 71.82211012, 0.00017321, 239.40703373, 0.00057736, -23.94070337, -5.774e-05, -71.82211012, -0.00017321, -239.40703373, -0.00057736, 0.4, 0.3, 0.003, 0.0, 0.0, 14073, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4073, 99999, 'P', 44073, 'Vy', 34073, 'Vz', 24073, 'My', 14073, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172001, 72001, 172001, 4073, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124029, 124029, 24029, 4073, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174029, 0.0, 0.0, 8.075)
    ops.node(123001, 0.0, 0.0, 9.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4074, 174029, 123001, 0.0625, 27721636.42604771, 11550681.84418655, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24074, 17.27386727, 0.00062708, 21.07755035, 0.04019111, 2.10775504, 0.13209565, -17.27386727, -0.00062708, -21.07755035, -0.04019111, -2.10775504, -0.13209565, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14074, 17.27386727, 0.00062708, 21.07755035, 0.04019111, 2.10775504, 0.13209565, -17.27386727, -0.00062708, -21.07755035, -0.04019111, -2.10775504, -0.13209565, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24074, 4074, 0.0, 67.11649293, 0.01254169, 67.11649293, 0.03762508, 46.98154505, -3087.22543225, 0.05, 2, 0, 74029, 23001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44074, 16.77912323, 4.393e-05, 50.3373697, 0.00013178, 167.79123234, 0.00043928, -16.77912323, -4.393e-05, -50.3373697, -0.00013178, -167.79123234, -0.00043928, 0.4, 0.3, 0.003, 0.0, 0.0, 24074, 2)
    ops.limitCurve('ThreePoint', 14074, 4074, 0.0, 67.11649293, 0.01254169, 67.11649293, 0.03762508, 46.98154505, -3087.22543225, 0.05, 2, 0, 74029, 23001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34074, 16.77912323, 4.393e-05, 50.3373697, 0.00013178, 167.79123234, 0.00043928, -16.77912323, -4.393e-05, -50.3373697, -0.00013178, -167.79123234, -0.00043928, 0.4, 0.3, 0.003, 0.0, 0.0, 14074, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4074, 99999, 'P', 44074, 'Vy', 34074, 'Vz', 24074, 'My', 14074, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174029, 74029, 174029, 4074, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123001, 123001, 23001, 4074, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172002, 3.1, 0.0, 6.525)
    ops.node(124030, 3.1, 0.0, 7.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4075, 172002, 124030, 0.1, 31511334.20911921, 13129722.58713301, 0.00127345, 0.00146667, 0.00057292, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24075, 34.91969887, 0.00062883, 42.09919585, 0.05651377, 4.20991959, 0.15651377, -34.91969887, -0.00062883, -42.09919585, -0.05651377, -4.20991959, -0.15651377, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14075, 58.98073408, 0.00050681, 71.10718464, 0.05780121, 7.11071846, 0.15780121, -58.98073408, -0.00050681, -71.10718464, -0.05780121, -7.11071846, -0.15780121, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24075, 4075, 0.0, 123.51579532, 0.01257655, 123.51579532, 0.03772966, 86.46105673, -3435.17426425, 0.05, 2, 0, 72002, 24030, 2, 3)
    ops.uniaxialMaterial('LimitState', 44075, 30.87894883, 4.445e-05, 92.63684649, 0.00013335, 308.78948831, 0.0004445, -30.87894883, -4.445e-05, -92.63684649, -0.00013335, -308.78948831, -0.0004445, 0.4, 0.3, 0.003, 0.0, 0.0, 24075, 2)
    ops.limitCurve('ThreePoint', 14075, 4075, 0.0, 239.40845321, 0.01013611, 239.40845321, 0.03040833, 167.58591724, -12692.76926048, 0.05, 2, 0, 72002, 24030, 1, 3)
    ops.uniaxialMaterial('LimitState', 34075, 59.8521133, 8.616e-05, 179.5563399, 0.00025847, 598.52113301, 0.00086156, -59.8521133, -8.616e-05, -179.5563399, -0.00025847, -598.52113301, -0.00086156, 0.4, 0.3, 0.003, 0.0, 0.0, 14075, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4075, 99999, 'P', 44075, 'Vy', 34075, 'Vz', 24075, 'My', 14075, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172002, 72002, 172002, 4075, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124030, 124030, 24030, 4075, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174030, 3.1, 0.0, 8.075)
    ops.node(123002, 3.1, 0.0, 9.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4076, 174030, 123002, 0.1, 30731220.86119926, 12804675.35883303, 0.00127345, 0.00146667, 0.00057292, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24076, 42.00300983, 0.0006469, 50.80070009, 0.06265538, 5.08007001, 0.16265538, -42.00300983, -0.0006469, -50.80070009, -0.06265538, -5.08007001, -0.16265538, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14076, 65.00893043, 0.00051614, 78.6252983, 0.06408853, 7.86252983, 0.16408853, -65.00893043, -0.00051614, -78.6252983, -0.06408853, -7.86252983, -0.16408853, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24076, 4076, 0.0, 128.91148041, 0.01293796, 128.91148041, 0.03881388, 90.23803629, -4864.40010088, 0.05, 2, 0, 74030, 23002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44076, 32.2278701, 4.757e-05, 96.68361031, 0.00014271, 322.27870102, 0.00047569, -32.2278701, -4.757e-05, -96.68361031, -0.00014271, -322.27870102, -0.00047569, 0.4, 0.3, 0.003, 0.0, 0.0, 24076, 2)
    ops.limitCurve('ThreePoint', 14076, 4076, 0.0, 256.27829749, 0.01032287, 256.27829749, 0.0309686, 179.39480824, -20299.05528043, 0.05, 2, 0, 74030, 23002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34076, 64.06957437, 9.457e-05, 192.20872311, 0.0002837, 640.69574371, 0.00094568, -64.06957437, -9.457e-05, -192.20872311, -0.0002837, -640.69574371, -0.00094568, 0.4, 0.3, 0.003, 0.0, 0.0, 14076, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4076, 99999, 'P', 44076, 'Vy', 34076, 'Vz', 24076, 'My', 14076, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174030, 74030, 174030, 4076, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123002, 123002, 23002, 4076, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173001, 0.0, 0.0, 9.675)
    ops.node(124031, 0.0, 0.0, 10.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4078, 173001, 124031, 0.0625, 27464014.03053401, 11443339.17938917, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24078, 16.27648239, 0.00058072, 19.89121177, 0.02661675, 1.98912118, 0.08814386, -16.27648239, -0.00058072, -19.89121177, -0.02661675, -1.98912118, -0.08814386, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14078, 16.27648239, 0.00058072, 19.89121177, 0.02661675, 1.98912118, 0.08814386, -16.27648239, -0.00058072, -19.89121177, -0.02661675, -1.98912118, -0.08814386, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24078, 4078, 0.0, 55.88022333, 0.01161447, 55.88022333, 0.0348434, 39.11615633, -2150.52958958, 0.05, 2, 0, 73001, 24031, 2, 3)
    ops.uniaxialMaterial('LimitState', 44078, 13.97005583, 3.692e-05, 41.9101675, 0.00011075, 139.70055833, 0.00036917, -13.97005583, -3.692e-05, -41.9101675, -0.00011075, -139.70055833, -0.00036917, 0.4, 0.3, 0.003, 0.0, 0.0, 24078, 2)
    ops.limitCurve('ThreePoint', 14078, 4078, 0.0, 55.88022333, 0.01161447, 55.88022333, 0.0348434, 39.11615633, -2150.52958958, 0.05, 2, 0, 73001, 24031, 1, 3)
    ops.uniaxialMaterial('LimitState', 34078, 13.97005583, 3.692e-05, 41.9101675, 0.00011075, 139.70055833, 0.00036917, -13.97005583, -3.692e-05, -41.9101675, -0.00011075, -139.70055833, -0.00036917, 0.4, 0.3, 0.003, 0.0, 0.0, 14078, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4078, 99999, 'P', 44078, 'Vy', 34078, 'Vz', 24078, 'My', 14078, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173001, 73001, 173001, 4078, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124031, 124031, 24031, 4078, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174031, 0.0, 0.0, 11.225)
    ops.node(124001, 0.0, 0.0, 12.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4079, 174031, 124001, 0.0625, 31394325.75117134, 13080969.06298806, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24079, 13.4729657, 0.00055423, 16.32636823, 0.02507072, 1.63263682, 0.0916322, -13.4729657, -0.00055423, -16.32636823, -0.02507072, -1.63263682, -0.0916322, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14079, 13.4729657, 0.00055423, 16.32636823, 0.02507072, 1.63263682, 0.0916322, -13.4729657, -0.00055423, -16.32636823, -0.02507072, -1.63263682, -0.0916322, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24079, 4079, 0.0, 58.23354245, 0.01108457, 58.23354245, 0.03325371, 40.76347972, -11197.51470482, 0.05, 2, 0, 74031, 24001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44079, 14.55838561, 3.366e-05, 43.67515684, 0.00010097, 145.58385613, 0.00033655, -14.55838561, -3.366e-05, -43.67515684, -0.00010097, -145.58385613, -0.00033655, 0.4, 0.3, 0.003, 0.0, 0.0, 24079, 2)
    ops.limitCurve('ThreePoint', 14079, 4079, 0.0, 58.23354245, 0.01108457, 58.23354245, 0.03325371, 40.76347972, -11197.51470482, 0.05, 2, 0, 74031, 24001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34079, 14.55838561, 3.366e-05, 43.67515684, 0.00010097, 145.58385613, 0.00033655, -14.55838561, -3.366e-05, -43.67515684, -0.00010097, -145.58385613, -0.00033655, 0.4, 0.3, 0.003, 0.0, 0.0, 14079, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4079, 99999, 'P', 44079, 'Vy', 34079, 'Vz', 24079, 'My', 14079, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174031, 74031, 174031, 4079, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124001, 124001, 24001, 4079, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173002, 3.1, 0.0, 9.675)
    ops.node(124032, 3.1, 0.0, 10.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4080, 173002, 124032, 0.1, 30556854.34638626, 12732022.64432761, 0.00127345, 0.00146667, 0.00057292, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24080, 26.70111963, 0.00061791, 32.38296149, 0.04152581, 3.23829615, 0.10665564, -26.70111963, -0.00061791, -32.38296149, -0.04152581, -3.23829615, -0.10665564, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14080, 45.78139283, 0.00049948, 55.52340506, 0.0488374, 5.55234051, 0.14560074, -45.78139283, -0.00049948, -55.52340506, -0.0488374, -5.55234051, -0.14560074, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24080, 4080, 0.0, 99.71666651, 0.01235813, 99.71666651, 0.03707439, 69.80166656, -3565.14970623, 0.05, 2, 0, 73002, 24032, 2, 3)
    ops.uniaxialMaterial('LimitState', 44080, 24.92916663, 3.701e-05, 74.78749988, 0.00011102, 249.29166628, 0.00037006, -24.92916663, -3.701e-05, -74.78749988, -0.00011102, -249.29166628, -0.00037006, 0.4, 0.3, 0.003, 0.0, 0.0, 24080, 2)
    ops.limitCurve('ThreePoint', 14080, 4080, 0.0, 159.54666642, 0.00998953, 159.54666642, 0.02996859, 111.68266649, -7784.76825211, 0.05, 2, 0, 73002, 24032, 1, 3)
    ops.uniaxialMaterial('LimitState', 34080, 39.88666661, 5.921e-05, 119.65999982, 0.00017763, 398.86666605, 0.0005921, -39.88666661, -5.921e-05, -119.65999982, -0.00017763, -398.86666605, -0.0005921, 0.4, 0.3, 0.003, 0.0, 0.0, 14080, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4080, 99999, 'P', 44080, 'Vy', 34080, 'Vz', 24080, 'My', 14080, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173002, 73002, 173002, 4080, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124032, 124032, 24032, 4080, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174032, 3.1, 0.0, 11.225)
    ops.node(124002, 3.1, 0.0, 12.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4081, 174032, 124002, 0.1, 30862593.77642816, 12859414.07351173, 0.00127345, 0.00146667, 0.00057292, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24081, 24.78106639, 0.00058229, 30.06041902, 0.03272672, 3.0060419, 0.08657894, -24.78106639, -0.00058229, -30.06041902, -0.03272672, -3.0060419, -0.08657894, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14081, 42.27835431, 0.0004836, 51.28532511, 0.03812111, 5.12853251, 0.11641503, -42.27835431, -0.0004836, -51.28532511, -0.03812111, -5.12853251, -0.11641503, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24081, 4081, 0.0, 86.50652878, 0.01164572, 86.50652878, 0.03493715, 60.55457015, -3446.63006831, 0.05, 2, 0, 74032, 24002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44081, 21.6266322, 3.179e-05, 64.87989659, 9.536e-05, 216.26632196, 0.00031786, -21.6266322, -3.179e-05, -64.87989659, -9.536e-05, -216.26632196, -0.00031786, 0.4, 0.3, 0.003, 0.0, 0.0, 24081, 2)
    ops.limitCurve('ThreePoint', 14081, 4081, 0.0, 138.41044605, 0.00967193, 138.41044605, 0.02901579, 96.88731224, -7933.32012825, 0.05, 2, 0, 74032, 24002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34081, 34.60261151, 5.086e-05, 103.80783454, 0.00015257, 346.02611513, 0.00050857, -34.60261151, -5.086e-05, -103.80783454, -0.00015257, -346.02611513, -0.00050857, 0.4, 0.3, 0.003, 0.0, 0.0, 14081, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4081, 99999, 'P', 44081, 'Vy', 34081, 'Vz', 24081, 'My', 14081, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174032, 74032, 174032, 4081, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124002, 124002, 24002, 4081, '-orient', 0, 0, 1, 0, 1, 0)
