import openseespy.opensees as ops


def add_columns() -> None:
    """Add components of all columns to ops domain (plastic hinges, column elements and nodes)
    """
    # Create elastic column element nodes
    ops.node(170001, 0.0, 0.0, 0.0)
    ops.node(121001, 0.0, 0.0, 2.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1, 170001, 121001, 0.1, 26164800.56154356, 10902000.23397648, 0.00127345, 0.00146667, 0.00057292, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20001, 81.69015388, 0.00115393, 99.27483931, 0.01995812, 9.92748393, 0.0534038, -81.69015388, -0.00115393, -99.27483931, -0.01995812, -9.92748393, -0.0534038, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10001, 118.62689508, 0.00080076, 144.16261186, 0.02263911, 14.41626119, 0.0703309, -118.62689508, -0.00080076, -144.16261186, -0.02263911, -14.41626119, -0.0703309, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20001, 1, 0.0, 99.4809178, 0.02307863, 99.4809178, 0.0692359, 69.63664246, -1743.17647649, 0.05, 2, 0, 70001, 21001, 2, 3)
    ops.uniaxialMaterial('LimitState', 40001, 24.87022945, 6.296e-05, 74.61068835, 0.00018889, 248.70229451, 0.00062963, -24.87022945, -6.296e-05, -74.61068835, -0.00018889, -248.70229451, -0.00062963, 0.4, 0.3, 0.003, 0.0, 0.0, 20001, 2)
    ops.limitCurve('ThreePoint', 10001, 1, 0.0, 131.40291432, 0.01601521, 131.40291432, 0.04804564, 91.98204002, -3106.06928552, 0.05, 2, 0, 70001, 21001, 1, 3)
    ops.uniaxialMaterial('LimitState', 30001, 32.85072858, 8.317e-05, 98.55218574, 0.0002495, 328.5072858, 0.00083166, -32.85072858, -8.317e-05, -98.55218574, -0.0002495, -328.5072858, -0.00083166, 0.4, 0.3, 0.003, 0.0, 0.0, 10001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1, 99999, 'P', 40001, 'Vy', 30001, 'Vz', 20001, 'My', 10001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170001, 70001, 170001, 1, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121001, 121001, 21001, 1, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170004, 13.8, 0.0, 0.0)
    ops.node(121004, 13.8, 0.0, 2.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4, 170004, 121004, 0.1, 27840449.32158704, 11600187.21732793, 0.00127345, 0.00146667, 0.00057292, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20004, 81.96400541, 0.00114413, 99.4346942, 0.01985463, 9.94346942, 0.05548882, -81.96400541, -0.00114413, -99.4346942, -0.01985463, -9.94346942, -0.05548882, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10004, 119.60691648, 0.00079332, 145.10121978, 0.02252286, 14.51012198, 0.07333533, -119.60691648, -0.00079332, -145.10121978, -0.02252286, -14.51012198, -0.07333533, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20004, 4, 0.0, 103.33766373, 0.02288269, 103.33766373, 0.06864807, 72.33636461, -1700.43867004, 0.05, 2, 0, 70004, 21004, 2, 3)
    ops.uniaxialMaterial('LimitState', 40004, 25.83441593, 6.147e-05, 77.5032478, 0.0001844, 258.34415932, 0.00061467, -25.83441593, -6.147e-05, -77.5032478, -0.0001844, -258.34415932, -0.00061467, 0.4, 0.3, 0.003, 0.0, 0.0, 20004, 2)
    ops.limitCurve('ThreePoint', 10004, 4, 0.0, 135.23866538, 0.01586641, 135.23866538, 0.04759923, 94.66706576, -3014.90358951, 0.05, 2, 0, 70004, 21004, 1, 3)
    ops.uniaxialMaterial('LimitState', 30004, 33.80966634, 8.044e-05, 101.42899903, 0.00024133, 338.09666344, 0.00080442, -33.80966634, -8.044e-05, -101.42899903, -0.00024133, -338.09666344, -0.00080442, 0.4, 0.3, 0.003, 0.0, 0.0, 10004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4, 99999, 'P', 40004, 'Vy', 30004, 'Vz', 20004, 'My', 10004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170004, 70004, 170004, 4, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121004, 121004, 21004, 4, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170005, 0.0, 4.45, 0.0)
    ops.node(121005, 0.0, 4.45, 1.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 5, 170005, 121005, 0.21, 27601235.31822017, 11500514.71592507, 0.00545409, 0.00235812, 0.00693, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20005, 307.73626063, 0.00064862, 374.20467086, 0.03273316, 37.42046709, 0.09443234, -307.73626063, -0.00064862, -374.20467086, -0.03273316, -37.42046709, -0.09443234, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10005, 226.45937015, 0.00086928, 275.37266455, 0.02773603, 27.53726646, 0.06823434, -226.45937015, -0.00086928, -275.37266455, -0.02773603, -27.53726646, -0.06823434, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20005, 5, 0.0, 373.02965728, 0.01297249, 373.02965728, 0.03891747, 261.12076009, -9166.10648571, 0.05, 2, 0, 70005, 21005, 2, 3)
    ops.uniaxialMaterial('LimitState', 40005, 93.25741432, 0.00010658, 279.77224296, 0.00031973, 932.57414319, 0.00106575, -93.25741432, -0.00010658, -279.77224296, -0.00031973, -932.57414319, -0.00106575, 0.4, 0.3, 0.003, 0.0, 0.0, 20005, 2)
    ops.limitCurve('ThreePoint', 10005, 5, 0.0, 220.79242566, 0.01738567, 220.79242566, 0.05215701, 154.55469796, -4321.01505841, 0.05, 2, 0, 70005, 21005, 1, 3)
    ops.uniaxialMaterial('LimitState', 30005, 55.19810642, 6.308e-05, 165.59431925, 0.00018924, 551.98106416, 0.00063081, -55.19810642, -6.308e-05, -165.59431925, -0.00018924, -551.98106416, -0.00063081, 0.4, 0.3, 0.003, 0.0, 0.0, 10005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 5, 99999, 'P', 40005, 'Vy', 30005, 'Vz', 20005, 'My', 10005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170005, 70005, 170005, 5, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121005, 121005, 21005, 5, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170006, 5.45, 4.45, 0.0)
    ops.node(121006, 5.45, 4.45, 1.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 6, 170006, 121006, 0.2275, 27569694.28155567, 11487372.61731486, 0.00616035, 0.00255464, 0.00881089, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20006, 458.69034491, 0.00064661, 557.13405923, 0.0460085, 55.71340592, 0.13025592, -458.69034491, -0.00064661, -557.13405923, -0.0460085, -55.71340592, -0.13025592, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10006, 339.01614517, 0.00089566, 411.77548906, 0.03732001, 41.17754891, 0.08738082, -339.01614517, -0.00089566, -411.77548906, -0.03732001, -41.17754891, -0.08738082, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20006, 6, 0.0, 523.75666031, 0.01293228, 523.75666031, 0.03879684, 366.62966221, -17518.57483318, 0.05, 2, 0, 70006, 21006, 2, 3)
    ops.uniaxialMaterial('LimitState', 40006, 130.93916508, 0.00013829, 392.81749523, 0.00041486, 1309.39165077, 0.00138285, -130.93916508, -0.00013829, -392.81749523, -0.00041486, -1309.39165077, -0.00138285, 0.4, 0.3, 0.003, 0.0, 0.0, 20006, 2)
    ops.limitCurve('ThreePoint', 10006, 6, 0.0, 285.57451584, 0.0179132, 285.57451584, 0.05373961, 199.90216109, -6976.69222783, 0.05, 2, 0, 70006, 21006, 1, 3)
    ops.uniaxialMaterial('LimitState', 30006, 71.39362896, 7.54e-05, 214.18088688, 0.0002262, 713.93628959, 0.00075399, -71.39362896, -7.54e-05, -214.18088688, -0.0002262, -713.93628959, -0.00075399, 0.4, 0.3, 0.003, 0.0, 0.0, 10006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 6, 99999, 'P', 40006, 'Vy', 30006, 'Vz', 20006, 'My', 10006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170006, 70006, 170006, 6, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121006, 121006, 21006, 6, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170007, 8.35, 4.45, 0.0)
    ops.node(121007, 8.35, 4.45, 1.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 7, 170007, 121007, 0.2275, 27373518.03730932, 11405632.51554555, 0.00616035, 0.00255464, 0.00881089, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20007, 459.01030655, 0.00064624, 557.66825806, 0.0460686, 55.76682581, 0.12979119, -459.01030655, -0.00064624, -557.66825806, -0.0460686, -55.76682581, -0.12979119, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10007, 341.1778199, 0.00089247, 414.50929924, 0.03736538, 41.45092992, 0.08711433, -341.1778199, -0.00089247, -414.50929924, -0.03736538, -41.45092992, -0.08711433, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20007, 7, 0.0, 524.52778629, 0.01292484, 524.52778629, 0.03877451, 367.1694504, -17831.98108311, 0.05, 2, 0, 70007, 21007, 2, 3)
    ops.uniaxialMaterial('LimitState', 40007, 131.13194657, 0.00013948, 393.39583972, 0.00041844, 1311.31946573, 0.00139482, -131.13194657, -0.00013948, -393.39583972, -0.00041844, -1311.31946573, -0.00139482, 0.4, 0.3, 0.003, 0.0, 0.0, 20007, 2)
    ops.limitCurve('ThreePoint', 10007, 7, 0.0, 285.95626934, 0.01784946, 285.95626934, 0.05354837, 200.16938854, -7083.12003988, 0.05, 2, 0, 70007, 21007, 1, 3)
    ops.uniaxialMaterial('LimitState', 30007, 71.48906734, 7.604e-05, 214.46720201, 0.00022812, 714.89067336, 0.00076041, -71.48906734, -7.604e-05, -214.46720201, -0.00022812, -714.89067336, -0.00076041, 0.4, 0.3, 0.003, 0.0, 0.0, 10007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 7, 99999, 'P', 40007, 'Vy', 30007, 'Vz', 20007, 'My', 10007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170007, 70007, 170007, 7, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121007, 121007, 21007, 7, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170008, 13.8, 4.45, 0.0)
    ops.node(121008, 13.8, 4.45, 1.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 8, 170008, 121008, 0.21, 27058245.626104, 11274269.01087667, 0.00545409, 0.00235812, 0.00693, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20008, 306.96189289, 0.00064592, 373.5520351, 0.03285451, 37.35520351, 0.09361678, -306.96189289, -0.00064592, -373.5520351, -0.03285451, -37.35520351, -0.09361678, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10008, 228.21547524, 0.00086017, 277.7229265, 0.02783081, 27.77229265, 0.06771415, -228.21547524, -0.00086017, -277.7229265, -0.02783081, -27.77229265, -0.06771415, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20008, 8, 0.0, 366.60976408, 0.01291839, 366.60976408, 0.03875517, 256.62683486, -9084.43184025, 0.05, 2, 0, 70008, 21008, 2, 3)
    ops.uniaxialMaterial('LimitState', 40008, 91.65244102, 0.00010684, 274.95732306, 0.00032053, 916.5244102, 0.00106843, -91.65244102, -0.00010684, -274.95732306, -0.00032053, -916.5244102, -0.00106843, 0.4, 0.3, 0.003, 0.0, 0.0, 20008, 2)
    ops.limitCurve('ThreePoint', 10008, 8, 0.0, 216.96283029, 0.01720348, 216.96283029, 0.05161043, 151.87398121, -4288.29224619, 0.05, 2, 0, 70008, 21008, 1, 3)
    ops.uniaxialMaterial('LimitState', 30008, 54.24070757, 6.323e-05, 162.72212272, 0.00018969, 542.40707574, 0.00063231, -54.24070757, -6.323e-05, -162.72212272, -0.00018969, -542.40707574, -0.00063231, 0.4, 0.3, 0.003, 0.0, 0.0, 10008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 8, 99999, 'P', 40008, 'Vy', 30008, 'Vz', 20008, 'My', 10008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170008, 70008, 170008, 8, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121008, 121008, 21008, 8, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170009, 0.0, 8.9, 0.0)
    ops.node(121009, 0.0, 8.9, 1.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 9, 170009, 121009, 0.21, 27990151.46102585, 11662563.10876077, 0.00545409, 0.00235812, 0.00693, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20009, 311.09050617, 0.00065137, 378.04991331, 0.03291041, 37.80499133, 0.09524112, -311.09050617, -0.00065137, -378.04991331, -0.03291041, -37.80499133, -0.09524112, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10009, 228.94186265, 0.00087341, 278.21952008, 0.02788628, 27.82195201, 0.06879912, -228.94186265, -0.00087341, -278.21952008, -0.02788628, -27.82195201, -0.06879912, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20009, 9, 0.0, 377.59377297, 0.01302731, 377.59377297, 0.03908192, 264.31564108, -9218.81583883, 0.05, 2, 0, 70009, 21009, 2, 3)
    ops.uniaxialMaterial('LimitState', 40009, 94.39844324, 0.00010638, 283.19532973, 0.00031914, 943.98443243, 0.0010638, -94.39844324, -0.00010638, -283.19532973, -0.00031914, -943.98443243, -0.0010638, 0.4, 0.3, 0.003, 0.0, 0.0, 20009, 2)
    ops.limitCurve('ThreePoint', 10009, 9, 0.0, 223.51607591, 0.01746816, 223.51607591, 0.05240447, 156.46125314, -4342.12131824, 0.05, 2, 0, 70009, 21009, 1, 3)
    ops.uniaxialMaterial('LimitState', 30009, 55.87901898, 6.297e-05, 167.63705693, 0.00018891, 558.79018978, 0.00062972, -55.87901898, -6.297e-05, -167.63705693, -0.00018891, -558.79018978, -0.00062972, 0.4, 0.3, 0.003, 0.0, 0.0, 10009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 9, 99999, 'P', 40009, 'Vy', 30009, 'Vz', 20009, 'My', 10009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170009, 70009, 170009, 9, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121009, 121009, 21009, 9, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170010, 5.45, 8.9, 0.0)
    ops.node(121010, 5.45, 8.9, 1.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 10, 170010, 121010, 0.165, 27302653.53285908, 11376105.63869128, 0.00326155, 0.00136125, 0.00457531, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20010, 275.38525033, 0.00068524, 334.01894037, 0.03498919, 33.40189404, 0.09873154, -275.38525033, -0.00068524, -334.01894037, -0.03498919, -33.40189404, -0.09873154, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10010, 186.90812507, 0.00100742, 226.70369531, 0.02895453, 22.67036953, 0.06815532, -186.90812507, -0.00100742, -226.70369531, -0.02895453, -22.67036953, -0.06815532, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20010, 10, 0.0, 315.21388714, 0.01370487, 315.21388714, 0.04111462, 220.649721, -8154.76579537, 0.05, 2, 0, 70010, 21010, 2, 3)
    ops.uniaxialMaterial('LimitState', 40010, 78.80347179, 0.00011587, 236.41041536, 0.00034761, 788.03471786, 0.00115872, -78.80347179, -0.00011587, -236.41041536, -0.00034761, -788.03471786, -0.00115872, 0.4, 0.3, 0.003, 0.0, 0.0, 20010, 2)
    ops.limitCurve('ThreePoint', 10010, 10, 0.0, 188.67480133, 0.0201484, 188.67480133, 0.06044519, 132.07236093, -3659.77262776, 0.05, 2, 0, 70010, 21010, 1, 3)
    ops.uniaxialMaterial('LimitState', 30010, 47.16870033, 6.936e-05, 141.506101, 0.00020807, 471.68700333, 0.00069356, -47.16870033, -6.936e-05, -141.506101, -0.00020807, -471.68700333, -0.00069356, 0.4, 0.3, 0.003, 0.0, 0.0, 10010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 10, 99999, 'P', 40010, 'Vy', 30010, 'Vz', 20010, 'My', 10010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170010, 70010, 170010, 10, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121010, 121010, 21010, 10, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170011, 8.35, 8.9, 0.0)
    ops.node(121011, 8.35, 8.9, 1.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 11, 170011, 121011, 0.165, 27223283.14499593, 11343034.6437483, 0.00326155, 0.00136125, 0.00457531, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20011, 277.86740367, 0.00068121, 337.05731971, 0.03463464, 33.70573197, 0.09817821, -277.86740367, -0.00068121, -337.05731971, -0.03463464, -33.70573197, -0.09817821, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10011, 191.75544113, 0.0009882, 232.60222025, 0.02864975, 23.26022202, 0.06772828, -191.75544113, -0.0009882, -232.60222025, -0.02864975, -23.26022202, -0.06772828, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20011, 11, 0.0, 310.65371628, 0.01362422, 310.65371628, 0.04087267, 217.4576014, -7863.0582732, 0.05, 2, 0, 70011, 21011, 2, 3)
    ops.uniaxialMaterial('LimitState', 40011, 77.66342907, 0.00011453, 232.99028721, 0.00034358, 776.6342907, 0.00114528, -77.66342907, -0.00011453, -232.99028721, -0.00034358, -776.6342907, -0.00114528, 0.4, 0.3, 0.003, 0.0, 0.0, 20011, 2)
    ops.limitCurve('ThreePoint', 10011, 11, 0.0, 186.12484213, 0.01976406, 186.12484213, 0.05929217, 130.28738949, -3552.99957704, 0.05, 2, 0, 70011, 21011, 1, 3)
    ops.uniaxialMaterial('LimitState', 30011, 46.53121053, 6.862e-05, 139.59363159, 0.00020586, 465.31210531, 0.00068618, -46.53121053, -6.862e-05, -139.59363159, -0.00020586, -465.31210531, -0.00068618, 0.4, 0.3, 0.003, 0.0, 0.0, 10011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 11, 99999, 'P', 40011, 'Vy', 30011, 'Vz', 20011, 'My', 10011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170011, 70011, 170011, 11, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121011, 121011, 21011, 11, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170012, 13.8, 8.9, 0.0)
    ops.node(121012, 13.8, 8.9, 1.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 12, 170012, 121012, 0.21, 27994260.73399261, 11664275.30583026, 0.00545409, 0.00235812, 0.00693, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20012, 308.12620364, 0.0006479, 374.44502511, 0.03319193, 37.44450251, 0.09552915, -308.12620364, -0.0006479, -374.44502511, -0.03319193, -37.44450251, -0.09552915, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10012, 225.99665897, 0.0008692, 274.63852033, 0.02812072, 27.46385203, 0.06903783, -225.99665897, -0.0008692, -274.63852033, -0.02812072, -27.46385203, -0.06903783, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20012, 12, 0.0, 382.71629032, 0.01295806, 382.71629032, 0.03887417, 267.90140323, -9639.87189461, 0.05, 2, 0, 70012, 21012, 2, 3)
    ops.uniaxialMaterial('LimitState', 40012, 95.67907258, 0.00010781, 287.03721774, 0.00032342, 956.79072581, 0.00107808, -95.67907258, -0.00010781, -287.03721774, -0.00032342, -956.79072581, -0.00107808, 0.4, 0.3, 0.003, 0.0, 0.0, 20012, 2)
    ops.limitCurve('ThreePoint', 10012, 12, 0.0, 226.50486092, 0.01738409, 226.50486092, 0.05215226, 158.55340264, -4510.40501242, 0.05, 2, 0, 70012, 21012, 1, 3)
    ops.uniaxialMaterial('LimitState', 30012, 56.62621523, 6.38e-05, 169.87864569, 0.00019141, 566.2621523, 0.00063804, -56.62621523, -6.38e-05, -169.87864569, -0.00019141, -566.2621523, -0.00063804, 0.4, 0.3, 0.003, 0.0, 0.0, 10012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 12, 99999, 'P', 40012, 'Vy', 30012, 'Vz', 20012, 'My', 10012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170012, 70012, 170012, 12, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121012, 121012, 21012, 12, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170013, 0.0, 13.35, 0.0)
    ops.node(121013, 0.0, 13.35, 2.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 13, 170013, 121013, 0.1, 27797306.29059401, 11582210.95441417, 0.00127345, 0.00146667, 0.00057292, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20013, 83.3511819, 0.00114749, 101.1234796, 0.02478394, 10.11234796, 0.06666962, -83.3511819, -0.00114749, -101.1234796, -0.02478394, -10.11234796, -0.06666962, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10013, 121.13458075, 0.00079794, 146.96312668, 0.02847356, 14.69631267, 0.08936974, -121.13458075, -0.00079794, -146.96312668, -0.02847356, -14.69631267, -0.08936974, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20013, 13, 0.0, 116.63861239, 0.0229498, 116.63861239, 0.06884939, 81.64702867, -2362.40152397, 0.05, 2, 0, 70013, 21013, 2, 3)
    ops.uniaxialMaterial('LimitState', 40013, 29.1596531, 6.949e-05, 87.47895929, 0.00020846, 291.59653096, 0.00069486, -29.1596531, -6.949e-05, -87.47895929, -0.00020846, -291.59653096, -0.00069486, 0.4, 0.3, 0.003, 0.0, 0.0, 20013, 2)
    ops.limitCurve('ThreePoint', 10013, 13, 0.0, 156.58132791, 0.01595882, 156.58132791, 0.04787647, 109.60692953, -4448.51707071, 0.05, 2, 0, 70013, 21013, 1, 3)
    ops.uniaxialMaterial('LimitState', 30013, 39.14533198, 9.328e-05, 117.43599593, 0.00027985, 391.45331977, 0.00093282, -39.14533198, -9.328e-05, -117.43599593, -0.00027985, -391.45331977, -0.00093282, 0.4, 0.3, 0.003, 0.0, 0.0, 10013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 13, 99999, 'P', 40013, 'Vy', 30013, 'Vz', 20013, 'My', 10013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170013, 70013, 170013, 13, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121013, 121013, 21013, 13, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170014, 5.45, 13.35, 0.0)
    ops.node(121014, 5.45, 13.35, 2.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 14, 170014, 121014, 0.135, 26832014.25445624, 11180005.93935677, 0.002377, 0.00250594, 0.00111375, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20014, 109.43406571, 0.00096309, 132.94881018, 0.02925378, 13.29488102, 0.07569579, -109.43406571, -0.00096309, -132.94881018, -0.02925378, -13.29488102, -0.07569579, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10014, 147.61650367, 0.00073338, 179.33573426, 0.03327793, 17.93357343, 0.09802452, -147.61650367, -0.00073338, -179.33573426, -0.03327793, -17.93357343, -0.09802452, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20014, 14, 0.0, 163.52760919, 0.01926178, 163.52760919, 0.05778533, 114.46932643, -3784.50027982, 0.05, 2, 0, 70014, 21014, 2, 3)
    ops.uniaxialMaterial('LimitState', 40014, 40.8819023, 7.476e-05, 122.64570689, 0.00022428, 408.81902298, 0.00074759, -40.8819023, -7.476e-05, -122.64570689, -0.00022428, -408.81902298, -0.00074759, 0.4, 0.3, 0.003, 0.0, 0.0, 20014, 2)
    ops.limitCurve('ThreePoint', 10014, 14, 0.0, 225.68195566, 0.01466753, 225.68195566, 0.04400258, 157.97736896, -6671.97396343, 0.05, 2, 0, 70014, 21014, 1, 3)
    ops.uniaxialMaterial('LimitState', 30014, 56.42048892, 0.00010317, 169.26146675, 0.00030952, 564.20488916, 0.00103174, -56.42048892, -0.00010317, -169.26146675, -0.00030952, -564.20488916, -0.00103174, 0.4, 0.3, 0.003, 0.0, 0.0, 10014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 14, 99999, 'P', 40014, 'Vy', 30014, 'Vz', 20014, 'My', 10014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170014, 70014, 170014, 14, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121014, 121014, 21014, 14, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170015, 8.35, 13.35, 0.0)
    ops.node(121015, 8.35, 13.35, 2.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 15, 170015, 121015, 0.135, 27764742.8153908, 11568642.83974617, 0.002377, 0.00250594, 0.00111375, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20015, 112.23790805, 0.0009464, 136.20452053, 0.02912538, 13.62045205, 0.07711594, -112.23790805, -0.0009464, -136.20452053, -0.02912538, -13.62045205, -0.07711594, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10015, 150.34190403, 0.00072645, 182.44501621, 0.0331425, 18.24450162, 0.10004798, -150.34190403, -0.00072645, -182.44501621, -0.0331425, -18.24450162, -0.10004798, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20015, 15, 0.0, 168.69817421, 0.01892798, 168.69817421, 0.05678394, 118.08872195, -3876.16369563, 0.05, 2, 0, 70015, 21015, 2, 3)
    ops.uniaxialMaterial('LimitState', 40015, 42.17454355, 7.453e-05, 126.52363066, 0.0002236, 421.74543553, 0.00074532, -42.17454355, -7.453e-05, -126.52363066, -0.0002236, -421.74543553, -0.00074532, 0.4, 0.3, 0.003, 0.0, 0.0, 20015, 2)
    ops.limitCurve('ThreePoint', 10015, 15, 0.0, 232.54050759, 0.014529, 232.54050759, 0.043587, 162.77835531, -6854.67756509, 0.05, 2, 0, 70015, 21015, 1, 3)
    ops.uniaxialMaterial('LimitState', 30015, 58.1351269, 0.00010274, 174.40538069, 0.00030821, 581.35126897, 0.00102738, -58.1351269, -0.00010274, -174.40538069, -0.00030821, -581.35126897, -0.00102738, 0.4, 0.3, 0.003, 0.0, 0.0, 10015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 15, 99999, 'P', 40015, 'Vy', 30015, 'Vz', 20015, 'My', 10015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170015, 70015, 170015, 15, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121015, 121015, 21015, 15, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170016, 13.8, 13.35, 0.0)
    ops.node(121016, 13.8, 13.35, 2.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 16, 170016, 121016, 0.1, 26998694.20683129, 11249455.91951304, 0.00127345, 0.00146667, 0.00057292, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20016, 81.23739041, 0.00116857, 98.65321224, 0.02457188, 9.86532122, 0.06528954, -81.23739041, -0.00116857, -98.65321224, -0.02457188, -9.86532122, -0.06528954, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10016, 118.93187483, 0.00080477, 144.42870986, 0.0282074, 14.44287099, 0.08740543, -118.93187483, -0.00080477, -144.42870986, -0.0282074, -14.44287099, -0.08740543, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20016, 16, 0.0, 113.2243411, 0.02337149, 113.2243411, 0.07011447, 79.25703877, -2303.55691388, 0.05, 2, 0, 70016, 21016, 2, 3)
    ops.uniaxialMaterial('LimitState', 40016, 28.30608528, 6.945e-05, 84.91825583, 0.00020834, 283.06085276, 0.00069448, -28.30608528, -6.945e-05, -84.91825583, -0.00020834, -283.06085276, -0.00069448, 0.4, 0.3, 0.003, 0.0, 0.0, 20016, 2)
    ops.limitCurve('ThreePoint', 10016, 16, 0.0, 152.24056043, 0.01609535, 152.24056043, 0.04828606, 106.5683923, -4319.45380211, 0.05, 2, 0, 70016, 21016, 1, 3)
    ops.uniaxialMaterial('LimitState', 30016, 38.06014011, 9.338e-05, 114.18042032, 0.00028014, 380.60140107, 0.00093379, -38.06014011, -9.338e-05, -114.18042032, -0.00028014, -380.60140107, -0.00093379, 0.4, 0.3, 0.003, 0.0, 0.0, 10016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 16, 99999, 'P', 40016, 'Vy', 30016, 'Vz', 20016, 'My', 10016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170016, 70016, 170016, 16, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121016, 121016, 21016, 16, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171001, 0.0, 0.0, 2.6)
    ops.node(122001, 0.0, 0.0, 4.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1001, 171001, 122001, 0.1, 28401895.65062046, 11834123.18775853, 0.00127345, 0.00146667, 0.00057292, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21001, 94.5130148, 0.00118902, 114.84308544, 0.03352874, 11.48430854, 0.0909985, -94.5130148, -0.00118902, -114.84308544, -0.03352874, -11.48430854, -0.0909985, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11001, 130.61434063, 0.00080972, 158.70992913, 0.03902323, 15.87099291, 0.12440603, -130.61434063, -0.00080972, -158.70992913, -0.03902323, -15.87099291, -0.12440603, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21001, 1001, 0.0, 130.61857237, 0.02378045, 130.61857237, 0.07134134, 91.43300066, -3795.84554318, 0.05, 2, 0, 71001, 22001, 2, 3)
    ops.uniaxialMaterial('LimitState', 41001, 32.65464309, 7.616e-05, 97.96392928, 0.00022848, 326.54643093, 0.00076158, -32.65464309, -7.616e-05, -97.96392928, -0.00022848, -326.54643093, -0.00076158, 0.4, 0.3, 0.003, 0.0, 0.0, 21001, 2)
    ops.limitCurve('ThreePoint', 11001, 1001, 0.0, 179.9629748, 0.01619445, 179.9629748, 0.04858335, 125.97408236, -7955.33827301, 0.05, 2, 0, 71001, 22001, 1, 3)
    ops.uniaxialMaterial('LimitState', 31001, 44.9907437, 0.00010493, 134.9722311, 0.00031479, 449.90743699, 0.00104929, -44.9907437, -0.00010493, -134.9722311, -0.00031479, -449.90743699, -0.00104929, 0.4, 0.3, 0.003, 0.0, 0.0, 11001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1001, 99999, 'P', 41001, 'Vy', 31001, 'Vz', 21001, 'My', 11001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171001, 71001, 171001, 1001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122001, 122001, 22001, 1001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171004, 13.8, 0.0, 2.6)
    ops.node(122004, 13.8, 0.0, 4.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1004, 171004, 122004, 0.1, 28627128.22616072, 11927970.09423363, 0.00127345, 0.00146667, 0.00057292, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21004, 91.47038023, 0.00116269, 111.09841997, 0.03372957, 11.109842, 0.09147684, -91.47038023, -0.00116269, -111.09841997, -0.03372957, -11.109842, -0.09147684, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11004, 127.03545266, 0.00079167, 154.29517222, 0.0392736, 15.42951722, 0.12506868, -127.03545266, -0.00079167, -154.29517222, -0.0392736, -15.42951722, -0.12506868, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21004, 1004, 0.0, 131.90203494, 0.02325387, 131.90203494, 0.06976162, 92.33142446, -3846.12454083, 0.05, 2, 0, 71004, 22004, 2, 3)
    ops.uniaxialMaterial('LimitState', 41004, 32.97550873, 7.63e-05, 98.9265262, 0.00022891, 329.75508734, 0.00076302, -32.97550873, -7.63e-05, -98.9265262, -0.00022891, -329.75508734, -0.00076302, 0.4, 0.3, 0.003, 0.0, 0.0, 21004, 2)
    ops.limitCurve('ThreePoint', 11004, 1004, 0.0, 181.69744085, 0.01583332, 181.69744085, 0.04749996, 127.18820859, -8071.83988671, 0.05, 2, 0, 71004, 22004, 1, 3)
    ops.uniaxialMaterial('LimitState', 31004, 45.42436021, 0.00010511, 136.27308064, 0.00031532, 454.24360212, 0.00105107, -45.42436021, -0.00010511, -136.27308064, -0.00031532, -454.24360212, -0.00105107, 0.4, 0.3, 0.003, 0.0, 0.0, 11004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1004, 99999, 'P', 41004, 'Vy', 31004, 'Vz', 21004, 'My', 11004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171004, 71004, 171004, 1004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122004, 122004, 22004, 1004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171005, 0.0, 4.45, 2.625)
    ops.node(122005, 0.0, 4.45, 4.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1005, 171005, 122005, 0.21, 27724384.06680581, 11551826.69450242, 0.00545409, 0.00235812, 0.00693, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21005, 231.75428419, 0.00060963, 282.33575093, 0.02559444, 28.23357509, 0.0778076, -231.75428419, -0.00060963, -282.33575093, -0.02559444, -28.23357509, -0.0778076, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11005, 112.05452176, 0.00079833, 136.5109502, 0.02198925, 13.65109502, 0.05731677, -112.05452176, -0.00079833, -136.5109502, -0.02198925, -13.65109502, -0.05731677, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21005, 1005, 0.0, 321.82607946, 0.01219256, 321.82607946, 0.03657768, 225.27825562, -7057.98167179, 0.05, 2, 0, 71005, 22005, 2, 3)
    ops.uniaxialMaterial('LimitState', 41005, 80.45651987, 9.154e-05, 241.3695596, 0.00027461, 804.56519866, 0.00091538, -80.45651987, -9.154e-05, -241.3695596, -0.00027461, -804.56519866, -0.00091538, 0.4, 0.3, 0.003, 0.0, 0.0, 21005, 2)
    ops.limitCurve('ThreePoint', 11005, 1005, 0.0, 190.77333474, 0.01596669, 190.77333474, 0.04790006, 133.54133432, -3295.95950096, 0.05, 2, 0, 71005, 22005, 1, 3)
    ops.uniaxialMaterial('LimitState', 31005, 47.69333368, 5.426e-05, 143.08000105, 0.00016279, 476.93333684, 0.00054262, -47.69333368, -5.426e-05, -143.08000105, -0.00016279, -476.93333684, -0.00054262, 0.4, 0.3, 0.003, 0.0, 0.0, 11005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1005, 99999, 'P', 41005, 'Vy', 31005, 'Vz', 21005, 'My', 11005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171005, 71005, 171005, 1005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122005, 122005, 22005, 1005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171006, 5.45, 4.45, 2.625)
    ops.node(122006, 5.45, 4.45, 4.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1006, 171006, 122006, 0.2275, 28599797.08678026, 11916582.11949178, 0.00616035, 0.00255464, 0.00881089, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21006, 293.97921094, 0.00060549, 357.22324161, 0.02489772, 35.72232416, 0.07658211, -293.97921094, -0.00060549, -357.22324161, -0.02489772, -35.72232416, -0.07658211, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11006, 129.44913427, 0.0008116, 157.29765115, 0.02096328, 15.72976512, 0.05414124, -129.44913427, -0.0008116, -157.29765115, -0.02096328, -15.72976512, -0.05414124, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21006, 1006, 0.0, 380.56303706, 0.01210978, 380.56303706, 0.03632935, 266.39412594, -6896.02979388, 0.05, 2, 0, 71006, 22006, 2, 3)
    ops.uniaxialMaterial('LimitState', 41006, 95.14075926, 9.686e-05, 285.42227779, 0.00029058, 951.40759264, 0.0009686, -95.14075926, -9.686e-05, -285.42227779, -0.00029058, -951.40759264, -0.0009686, 0.4, 0.3, 0.003, 0.0, 0.0, 21006, 2)
    ops.limitCurve('ThreePoint', 11006, 1006, 0.0, 208.45060858, 0.01623209, 208.45060858, 0.04869627, 145.915426, -3051.49675748, 0.05, 2, 0, 71006, 22006, 1, 3)
    ops.uniaxialMaterial('LimitState', 31006, 52.11265214, 5.305e-05, 156.33795643, 0.00015916, 521.12652144, 0.00053054, -52.11265214, -5.305e-05, -156.33795643, -0.00015916, -521.12652144, -0.00053054, 0.4, 0.3, 0.003, 0.0, 0.0, 11006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1006, 99999, 'P', 41006, 'Vy', 31006, 'Vz', 21006, 'My', 11006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171006, 71006, 171006, 1006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122006, 122006, 22006, 1006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171007, 8.35, 4.45, 2.625)
    ops.node(122007, 8.35, 4.45, 4.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1007, 171007, 122007, 0.2275, 26589646.42101824, 11079019.34209093, 0.00616035, 0.00255464, 0.00881089, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21007, 285.37938955, 0.00060691, 347.92498498, 0.02591403, 34.7924985, 0.0752479, -285.37938955, -0.00060691, -347.92498498, -0.02591403, -34.7924985, -0.0752479, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11007, 125.4849524, 0.00081995, 152.98704734, 0.02181354, 15.29870473, 0.05348261, -125.4849524, -0.00081995, -152.98704734, -0.02181354, -15.29870473, -0.05348261, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21007, 1007, 0.0, 361.81322698, 0.01213816, 361.81322698, 0.03641448, 253.26925889, -7253.13093335, 0.05, 2, 0, 71007, 22007, 2, 3)
    ops.uniaxialMaterial('LimitState', 41007, 90.45330675, 9.905e-05, 271.35992024, 0.00029715, 904.53306746, 0.00099049, -90.45330675, -9.905e-05, -271.35992024, -0.00029715, -904.53306746, -0.00099049, 0.4, 0.3, 0.003, 0.0, 0.0, 21007, 2)
    ops.limitCurve('ThreePoint', 11007, 1007, 0.0, 198.01516139, 0.01639909, 198.01516139, 0.04919726, 138.61061297, -3179.09866722, 0.05, 2, 0, 71007, 22007, 1, 3)
    ops.uniaxialMaterial('LimitState', 31007, 49.50379035, 5.421e-05, 148.51137104, 0.00016262, 495.03790347, 0.00054208, -49.50379035, -5.421e-05, -148.51137104, -0.00016262, -495.03790347, -0.00054208, 0.4, 0.3, 0.003, 0.0, 0.0, 11007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1007, 99999, 'P', 41007, 'Vy', 31007, 'Vz', 21007, 'My', 11007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171007, 71007, 171007, 1007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122007, 122007, 22007, 1007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171008, 13.8, 4.45, 2.625)
    ops.node(122008, 13.8, 4.45, 4.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1008, 171008, 122008, 0.21, 27747346.85397518, 11561394.52248966, 0.00545409, 0.00235812, 0.00693, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21008, 236.70751917, 0.00061799, 288.35804766, 0.02561547, 28.83580477, 0.07785153, -236.70751917, -0.00061799, -288.35804766, -0.02561547, -28.83580477, -0.07785153, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11008, 114.34542687, 0.00081085, 139.29605687, 0.02201252, 13.92960569, 0.05735553, -114.34542687, -0.00081085, -139.29605687, -0.02201252, -13.92960569, -0.05735553, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21008, 1008, 0.0, 323.05043653, 0.01235976, 323.05043653, 0.03707927, 226.13530557, -7142.22173268, 0.05, 2, 0, 71008, 22008, 2, 3)
    ops.uniaxialMaterial('LimitState', 41008, 80.76260913, 9.181e-05, 242.2878274, 0.00027543, 807.62609132, 0.0009181, -80.76260913, -9.181e-05, -242.2878274, -0.00027543, -807.62609132, -0.0009181, 0.4, 0.3, 0.003, 0.0, 0.0, 21008, 2)
    ops.limitCurve('ThreePoint', 11008, 1008, 0.0, 191.49111544, 0.01621697, 191.49111544, 0.0486509, 134.04378081, -3329.52534196, 0.05, 2, 0, 71008, 22008, 1, 3)
    ops.uniaxialMaterial('LimitState', 31008, 47.87277886, 5.442e-05, 143.61833658, 0.00016326, 478.7277886, 0.00054421, -47.87277886, -5.442e-05, -143.61833658, -0.00016326, -478.7277886, -0.00054421, 0.4, 0.3, 0.003, 0.0, 0.0, 11008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1008, 99999, 'P', 41008, 'Vy', 31008, 'Vz', 21008, 'My', 11008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171008, 71008, 171008, 1008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122008, 122008, 22008, 1008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171009, 0.0, 8.9, 2.625)
    ops.node(122009, 0.0, 8.9, 4.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1009, 171009, 122009, 0.21, 26506509.15412935, 11044378.81422056, 0.00545409, 0.00235812, 0.00693, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21009, 234.42014706, 0.00062074, 286.1474953, 0.0253412, 28.61474953, 0.07622966, -234.42014706, -0.00062074, -286.1474953, -0.0253412, -28.61474953, -0.07622966, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11009, 113.09380073, 0.00081652, 138.04917461, 0.02178323, 13.80491746, 0.05621445, -113.09380073, -0.00081652, -138.04917461, -0.02178323, -13.80491746, -0.05621445, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21009, 1009, 0.0, 308.31497443, 0.0124147, 308.31497443, 0.03724411, 215.8204821, -6927.46630552, 0.05, 2, 0, 71009, 22009, 2, 3)
    ops.uniaxialMaterial('LimitState', 41009, 77.07874361, 9.172e-05, 231.23623082, 0.00027517, 770.78743607, 0.00091724, -77.07874361, -9.172e-05, -231.23623082, -0.00027517, -770.78743607, -0.00091724, 0.4, 0.3, 0.003, 0.0, 0.0, 21009, 2)
    ops.limitCurve('ThreePoint', 11009, 1009, 0.0, 182.70503498, 0.0163304, 182.70503498, 0.04899119, 127.89352448, -3243.896926, 0.05, 2, 0, 71009, 22009, 1, 3)
    ops.uniaxialMaterial('LimitState', 31009, 45.67625874, 5.435e-05, 137.02877623, 0.00016306, 456.76258744, 0.00054355, -45.67625874, -5.435e-05, -137.02877623, -0.00016306, -456.76258744, -0.00054355, 0.4, 0.3, 0.003, 0.0, 0.0, 11009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1009, 99999, 'P', 41009, 'Vy', 31009, 'Vz', 21009, 'My', 11009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171009, 71009, 171009, 1009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122009, 122009, 22009, 1009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171010, 5.45, 8.9, 2.625)
    ops.node(122010, 5.45, 8.9, 4.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1010, 171010, 122010, 0.165, 27586072.2657209, 11494196.77738371, 0.00326155, 0.00136125, 0.00457531, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21010, 186.35892924, 0.0006413, 226.5958788, 0.02630147, 22.65958788, 0.08145316, -186.35892924, -0.0006413, -226.5958788, -0.02630147, -22.65958788, -0.08145316, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11010, 87.60743642, 0.00091376, 106.52284882, 0.02210397, 10.65228488, 0.05712915, -87.60743642, -0.00091376, -106.52284882, -0.02210397, -10.65228488, -0.05712915, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21010, 1010, 0.0, 260.99065609, 0.01282608, 260.99065609, 0.03847824, 182.69345926, -5707.30147666, 0.05, 2, 0, 71010, 22010, 2, 3)
    ops.uniaxialMaterial('LimitState', 41010, 65.24766402, 9.495e-05, 195.74299207, 0.00028486, 652.47664023, 0.00094954, -65.24766402, -9.495e-05, -195.74299207, -0.00028486, -652.47664023, -0.00094954, 0.4, 0.3, 0.003, 0.0, 0.0, 21010, 2)
    ops.limitCurve('ThreePoint', 11010, 1010, 0.0, 158.2647578, 0.01827528, 158.2647578, 0.05482584, 110.78533046, -2583.05028438, 0.05, 2, 0, 71010, 22010, 1, 3)
    ops.uniaxialMaterial('LimitState', 31010, 39.56618945, 5.758e-05, 118.69856835, 0.00017274, 395.66189451, 0.0005758, -39.56618945, -5.758e-05, -118.69856835, -0.00017274, -395.66189451, -0.0005758, 0.4, 0.3, 0.003, 0.0, 0.0, 11010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1010, 99999, 'P', 41010, 'Vy', 31010, 'Vz', 21010, 'My', 11010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171010, 71010, 171010, 1010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122010, 122010, 22010, 1010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171011, 8.35, 8.9, 2.625)
    ops.node(122011, 8.35, 8.9, 4.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1011, 171011, 122011, 0.165, 26674244.54409361, 11114268.560039, 0.00326155, 0.00136125, 0.00457531, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21011, 184.2855022, 0.00065714, 224.3492465, 0.026126, 22.43492465, 0.0798161, -184.2855022, -0.00065714, -224.3492465, -0.026126, -22.43492465, -0.0798161, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11011, 86.4137082, 0.00095787, 105.20008405, 0.0219901, 10.52000841, 0.05608707, -86.4137082, -0.00095787, -105.20008405, -0.0219901, -10.52000841, -0.05608707, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21011, 1011, 0.0, 256.3947589, 0.01314272, 256.3947589, 0.03942816, 179.47633123, -5847.87217669, 0.05, 2, 0, 71011, 22011, 2, 3)
    ops.uniaxialMaterial('LimitState', 41011, 64.09868972, 9.647e-05, 192.29606917, 0.00028941, 640.98689725, 0.0009647, -64.09868972, -9.647e-05, -192.29606917, -0.00028941, -640.98689725, -0.0009647, 0.4, 0.3, 0.003, 0.0, 0.0, 21011, 2)
    ops.limitCurve('ThreePoint', 11011, 1011, 0.0, 155.05317216, 0.01915735, 155.05317216, 0.05747206, 108.53722051, -2634.57365449, 0.05, 2, 0, 71011, 22011, 1, 3)
    ops.uniaxialMaterial('LimitState', 31011, 38.76329304, 5.834e-05, 116.28987912, 0.00017502, 387.63293041, 0.0005834, -38.76329304, -5.834e-05, -116.28987912, -0.00017502, -387.63293041, -0.0005834, 0.4, 0.3, 0.003, 0.0, 0.0, 11011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1011, 99999, 'P', 41011, 'Vy', 31011, 'Vz', 21011, 'My', 11011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171011, 71011, 171011, 1011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122011, 122011, 22011, 1011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171012, 13.8, 8.9, 2.625)
    ops.node(122012, 13.8, 8.9, 4.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1012, 171012, 122012, 0.21, 26803919.79636461, 11168299.91515192, 0.00545409, 0.00235812, 0.00693, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21012, 237.98923499, 0.00062807, 290.37670447, 0.02517532, 29.03767045, 0.07640827, -237.98923499, -0.00062807, -290.37670447, -0.02517532, -29.03767045, -0.07640827, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11012, 114.79186933, 0.0008294, 140.06047256, 0.02164921, 14.00604726, 0.05631351, -114.79186933, -0.0008294, -140.06047256, -0.02164921, -14.00604726, -0.05631351, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21012, 1012, 0.0, 309.98350534, 0.01256141, 309.98350534, 0.03768423, 216.98845373, -6825.843171, 0.05, 2, 0, 71012, 22012, 2, 3)
    ops.uniaxialMaterial('LimitState', 41012, 77.49587633, 9.12e-05, 232.487629, 0.00027359, 774.95876334, 0.00091197, -77.49587633, -9.12e-05, -232.487629, -0.00027359, -774.95876334, -0.00091197, 0.4, 0.3, 0.003, 0.0, 0.0, 21012, 2)
    ops.limitCurve('ThreePoint', 11012, 1012, 0.0, 183.72348662, 0.01658798, 183.72348662, 0.04976395, 128.60644063, -3203.3094196, 0.05, 2, 0, 71012, 22012, 1, 3)
    ops.uniaxialMaterial('LimitState', 31012, 45.93087165, 5.405e-05, 137.79261496, 0.00016215, 459.30871654, 0.00054051, -45.93087165, -5.405e-05, -137.79261496, -0.00016215, -459.30871654, -0.00054051, 0.4, 0.3, 0.003, 0.0, 0.0, 11012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1012, 99999, 'P', 41012, 'Vy', 31012, 'Vz', 21012, 'My', 11012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171012, 71012, 171012, 1012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122012, 122012, 22012, 1012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171013, 0.0, 13.35, 2.6)
    ops.node(122013, 0.0, 13.35, 4.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1013, 171013, 122013, 0.1, 27940958.63968185, 11642066.09986744, 0.00127345, 0.00146667, 0.00057292, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21013, 99.2964396, 0.00112196, 120.75493378, 0.03352069, 12.07549338, 0.09039638, -99.2964396, -0.00112196, -120.75493378, -0.03352069, -12.07549338, -0.09039638, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11013, 132.74241619, 0.00078744, 161.42876563, 0.03907068, 16.14287656, 0.12357086, -132.74241619, -0.00078744, -161.42876563, -0.03907068, -16.14287656, -0.12357086, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21013, 1013, 0.0, 130.11267957, 0.0224392, 130.11267957, 0.06731759, 91.0788757, -3861.95916324, 0.05, 2, 0, 71013, 22013, 2, 3)
    ops.uniaxialMaterial('LimitState', 41013, 32.52816989, 7.711e-05, 97.58450968, 0.00023134, 325.28169893, 0.00077115, -32.52816989, -7.711e-05, -97.58450968, -0.00023134, -325.28169893, -0.00077115, 0.4, 0.3, 0.003, 0.0, 0.0, 21013, 2)
    ops.limitCurve('ThreePoint', 11013, 1013, 0.0, 179.80173981, 0.01574873, 179.80173981, 0.04724618, 125.86121787, -8108.54688592, 0.05, 2, 0, 71013, 22013, 1, 3)
    ops.uniaxialMaterial('LimitState', 31013, 44.95043495, 0.00010656, 134.85130486, 0.00031969, 449.50434954, 0.00106565, -44.95043495, -0.00010656, -134.85130486, -0.00031969, -449.50434954, -0.00106565, 0.4, 0.3, 0.003, 0.0, 0.0, 11013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1013, 99999, 'P', 41013, 'Vy', 31013, 'Vz', 21013, 'My', 11013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171013, 71013, 171013, 1013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122013, 122013, 22013, 1013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171014, 5.45, 13.35, 2.6)
    ops.node(122014, 5.45, 13.35, 4.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1014, 171014, 122014, 0.135, 27117638.0203096, 11299015.84179567, 0.002377, 0.00250594, 0.00111375, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21014, 102.83516385, 0.00096567, 125.23877081, 0.02998865, 12.52387708, 0.0809413, -102.83516385, -0.00096567, -125.23877081, -0.02998865, -12.52387708, -0.0809413, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11014, 138.5265897, 0.00073321, 168.70590923, 0.03412015, 16.87059092, 0.10515521, -138.5265897, -0.00073321, -168.70590923, -0.03412015, -16.87059092, -0.10515521, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21014, 1014, 0.0, 159.45487827, 0.0193135, 159.45487827, 0.05794049, 111.61841479, -4275.46086306, 0.05, 2, 0, 71014, 22014, 2, 3)
    ops.uniaxialMaterial('LimitState', 41014, 39.86371957, 7.213e-05, 119.5911587, 0.00021639, 398.63719568, 0.00072129, -39.86371957, -7.213e-05, -119.5911587, -0.00021639, -398.63719568, -0.00072129, 0.4, 0.3, 0.003, 0.0, 0.0, 21014, 2)
    ops.limitCurve('ThreePoint', 11014, 1014, 0.0, 220.5359896, 0.01466419, 220.5359896, 0.04399256, 154.37519272, -7936.20481774, 0.05, 2, 0, 71014, 22014, 1, 3)
    ops.uniaxialMaterial('LimitState', 31014, 55.1339974, 9.976e-05, 165.4019922, 0.00029928, 551.33997401, 0.00099759, -55.1339974, -9.976e-05, -165.4019922, -0.00029928, -551.33997401, -0.00099759, 0.4, 0.3, 0.003, 0.0, 0.0, 11014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1014, 99999, 'P', 41014, 'Vy', 31014, 'Vz', 21014, 'My', 11014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171014, 71014, 171014, 1014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122014, 122014, 22014, 1014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171015, 8.35, 13.35, 2.6)
    ops.node(122015, 8.35, 13.35, 4.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1015, 171015, 122015, 0.135, 26721209.98199302, 11133837.49249709, 0.002377, 0.00250594, 0.00111375, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21015, 101.42164085, 0.00097023, 123.58517599, 0.03035628, 12.3585176, 0.08076839, -101.42164085, -0.00097023, -123.58517599, -0.03035628, -12.3585176, -0.08076839, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11015, 137.04473522, 0.00073435, 166.99293739, 0.03453897, 16.69929374, 0.10482043, -137.04473522, -0.00073435, -166.99293739, -0.03453897, -16.69929374, -0.10482043, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21015, 1015, 0.0, 158.37765855, 0.01940461, 158.37765855, 0.05821382, 110.86436099, -4306.8168391, 0.05, 2, 0, 71015, 22015, 2, 3)
    ops.uniaxialMaterial('LimitState', 41015, 39.59441464, 7.271e-05, 118.78324392, 0.00021812, 395.94414638, 0.00072705, -39.59441464, -7.271e-05, -118.78324392, -0.00021812, -395.94414638, -0.00072705, 0.4, 0.3, 0.003, 0.0, 0.0, 21015, 2)
    ops.limitCurve('ThreePoint', 11015, 1015, 0.0, 219.29251195, 0.01468705, 219.29251195, 0.04406114, 153.50475836, -8000.2972347, 0.05, 2, 0, 71015, 22015, 1, 3)
    ops.uniaxialMaterial('LimitState', 31015, 54.82312799, 0.00010067, 164.46938396, 0.00030201, 548.23127987, 0.00100669, -54.82312799, -0.00010067, -164.46938396, -0.00030201, -548.23127987, -0.00100669, 0.4, 0.3, 0.003, 0.0, 0.0, 11015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1015, 99999, 'P', 41015, 'Vy', 31015, 'Vz', 21015, 'My', 11015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171015, 71015, 171015, 1015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122015, 122015, 22015, 1015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171016, 13.8, 13.35, 2.6)
    ops.node(122016, 13.8, 13.35, 4.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1016, 171016, 122016, 0.1, 27102092.29440457, 11292538.4560019, 0.00127345, 0.00146667, 0.00057292, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21016, 93.98051267, 0.00120186, 114.44107283, 0.03318796, 11.44410728, 0.08888524, -93.98051267, -0.00120186, -114.44107283, -0.03318796, -11.44410728, -0.08888524, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11016, 129.53267613, 0.00081723, 157.73332153, 0.03861291, 15.77333215, 0.12136232, -129.53267613, -0.00081723, -157.73332153, -0.03861291, -15.77333215, -0.12136232, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21016, 1016, 0.0, 125.93440256, 0.02403713, 125.93440256, 0.0721114, 88.15408179, -3719.29268582, 0.05, 2, 0, 71016, 22016, 2, 3)
    ops.uniaxialMaterial('LimitState', 41016, 31.48360064, 7.695e-05, 94.45080192, 0.00023085, 314.8360064, 0.00076949, -31.48360064, -7.695e-05, -94.45080192, -0.00023085, -314.8360064, -0.00076949, 0.4, 0.3, 0.003, 0.0, 0.0, 21016, 2)
    ops.limitCurve('ThreePoint', 11016, 1016, 0.0, 174.27959611, 0.0163446, 174.27959611, 0.0490338, 121.99571728, -7778.11381474, 0.05, 2, 0, 71016, 22016, 1, 3)
    ops.uniaxialMaterial('LimitState', 31016, 43.56989903, 0.00010649, 130.70969708, 0.00031947, 435.69899027, 0.00106489, -43.56989903, -0.00010649, -130.70969708, -0.00031947, -435.69899027, -0.00106489, 0.4, 0.3, 0.003, 0.0, 0.0, 11016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1016, 99999, 'P', 41016, 'Vy', 31016, 'Vz', 21016, 'My', 11016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171016, 71016, 171016, 1016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122016, 122016, 22016, 1016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172001, 0.0, 0.0, 4.9)
    ops.node(123001, 0.0, 0.0, 6.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2001, 172001, 123001, 0.0875, 27417240.48656357, 11423850.20273482, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22001, 52.71869748, 0.00111873, 64.30300941, 0.02642523, 6.43030094, 0.07938105, -52.71869748, -0.00111873, -64.30300941, -0.02642523, -6.43030094, -0.07938105, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12001, 72.90907267, 0.00084588, 88.92998138, 0.02922583, 8.89299814, 0.09872747, -72.90907267, -0.00084588, -88.92998138, -0.02922583, -8.89299814, -0.09872747, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22001, 2001, 0.0, 99.21597035, 0.02237457, 99.21597035, 0.0671237, 69.45117925, -3091.13979292, 0.05, 2, 0, 72001, 23001, 2, 3)
    ops.uniaxialMaterial('LimitState', 42001, 24.80399259, 6.849e-05, 74.41197776, 0.00020546, 248.03992588, 0.00068487, -24.80399259, -6.849e-05, -74.41197776, -0.00020546, -248.03992588, -0.00068487, 0.4, 0.3, 0.003, 0.0, 0.0, 22001, 2)
    ops.limitCurve('ThreePoint', 12001, 2001, 0.0, 120.13132317, 0.01691769, 120.13132317, 0.05075307, 84.09192622, -5322.82434783, 0.05, 2, 0, 72001, 23001, 1, 3)
    ops.uniaxialMaterial('LimitState', 32001, 30.03283079, 8.292e-05, 90.09849238, 0.00024877, 300.32830793, 0.00082925, -30.03283079, -8.292e-05, -90.09849238, -0.00024877, -300.32830793, -0.00082925, 0.4, 0.3, 0.003, 0.0, 0.0, 12001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2001, 99999, 'P', 42001, 'Vy', 32001, 'Vz', 22001, 'My', 12001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172001, 72001, 172001, 2001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123001, 123001, 23001, 2001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172004, 13.8, 0.0, 4.9)
    ops.node(123004, 13.8, 0.0, 6.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2004, 172004, 123004, 0.0875, 27669223.57413147, 11528843.15588811, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22004, 52.49982825, 0.00110334, 64.00645453, 0.0270054, 6.40064545, 0.0801923, -52.49982825, -0.00110334, -64.00645453, -0.0270054, -6.40064545, -0.0801923, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12004, 72.55507081, 0.0008362, 88.45729587, 0.02988403, 8.84572959, 0.09968897, -72.55507081, -0.0008362, -88.45729587, -0.02988403, -8.84572959, -0.09968897, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22004, 2004, 0.0, 101.23358025, 0.02206674, 101.23358025, 0.06620021, 70.86350617, -3221.33497333, 0.05, 2, 0, 72004, 23004, 2, 3)
    ops.uniaxialMaterial('LimitState', 42004, 25.30839506, 6.924e-05, 75.92518518, 0.00020773, 253.08395061, 0.00069244, -25.30839506, -6.924e-05, -75.92518518, -0.00020773, -253.08395061, -0.00069244, 0.4, 0.3, 0.003, 0.0, 0.0, 22004, 2)
    ops.limitCurve('ThreePoint', 12004, 2004, 0.0, 122.70738644, 0.01672399, 122.70738644, 0.05017197, 85.89517051, -5562.1747481, 0.05, 2, 0, 72004, 23004, 1, 3)
    ops.uniaxialMaterial('LimitState', 32004, 30.67684661, 8.393e-05, 92.03053983, 0.0002518, 306.76846611, 0.00083932, -30.67684661, -8.393e-05, -92.03053983, -0.0002518, -306.76846611, -0.00083932, 0.4, 0.3, 0.003, 0.0, 0.0, 12004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2004, 99999, 'P', 42004, 'Vy', 32004, 'Vz', 22004, 'My', 12004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172004, 72004, 172004, 2004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123004, 123004, 23004, 2004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172005, 0.0, 4.45, 4.925)
    ops.node(123005, 0.0, 4.45, 6.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2005, 172005, 123005, 0.125, 27049902.24789109, 11270792.60328796, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22005, 127.97291233, 0.00065786, 156.05147832, 0.01877669, 15.60514783, 0.06731717, -127.97291233, -0.00065786, -156.05147832, -0.01877669, -15.60514783, -0.06731717, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12005, 55.36924271, 0.00104547, 67.51782094, 0.01584371, 6.75178209, 0.04587335, -55.36924271, -0.00104547, -67.51782094, -0.01584371, -6.75178209, -0.04587335, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22005, 2005, 0.0, 162.7093005, 0.01315722, 162.7093005, 0.03947167, 113.89651035, -3592.70258423, 0.05, 2, 0, 72005, 23005, 2, 3)
    ops.uniaxialMaterial('LimitState', 42005, 40.67732513, 7.969e-05, 122.03197538, 0.00023907, 406.77325125, 0.00079689, -40.67732513, -7.969e-05, -122.03197538, -0.00023907, -406.77325125, -0.00079689, 0.4, 0.3, 0.003, 0.0, 0.0, 22005, 2)
    ops.limitCurve('ThreePoint', 12005, 2005, 0.0, 97.66091154, 0.02090937, 97.66091154, 0.06272812, 68.36263808, -1435.2242176, 0.05, 2, 0, 72005, 23005, 1, 3)
    ops.uniaxialMaterial('LimitState', 32005, 24.41522788, 4.783e-05, 73.24568365, 0.00014349, 244.15227885, 0.00047831, -24.41522788, -4.783e-05, -73.24568365, -0.00014349, -244.15227885, -0.00047831, 0.4, 0.3, 0.003, 0.0, 0.0, 12005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2005, 99999, 'P', 42005, 'Vy', 32005, 'Vz', 22005, 'My', 12005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172005, 72005, 172005, 2005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123005, 123005, 23005, 2005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172006, 5.45, 4.45, 4.925)
    ops.node(123006, 5.45, 4.45, 6.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2006, 172006, 123006, 0.1375, 28037197.21121729, 11682165.50467387, 0.00204719, 0.00078776, 0.00381276, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22006, 154.94308355, 0.00064475, 188.40122159, 0.02343, 18.84012216, 0.07864273, -154.94308355, -0.00064475, -188.40122159, -0.02343, -18.84012216, -0.07864273, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12006, 71.51352841, 0.00107642, 86.95603447, 0.01900476, 8.69560345, 0.05027076, -71.51352841, -0.00107642, -86.95603447, -0.01900476, -8.69560345, -0.05027076, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22006, 2006, 0.0, 216.99476134, 0.01289502, 216.99476134, 0.03868506, 151.89633294, -4933.57907242, 0.05, 2, 0, 72006, 23006, 2, 3)
    ops.uniaxialMaterial('LimitState', 42006, 54.24869033, 9.321e-05, 162.746071, 0.00027964, 542.48690334, 0.00093212, -54.24869033, -9.321e-05, -162.746071, -0.00027964, -542.48690334, -0.00093212, 0.4, 0.3, 0.003, 0.0, 0.0, 22006, 2)
    ops.limitCurve('ThreePoint', 12006, 2006, 0.0, 123.11878716, 0.02152843, 123.11878716, 0.06458528, 86.18315101, -1756.28787719, 0.05, 2, 0, 72006, 23006, 1, 3)
    ops.uniaxialMaterial('LimitState', 32006, 30.77969679, 5.289e-05, 92.33909037, 0.00015866, 307.79696791, 0.00052887, -30.77969679, -5.289e-05, -92.33909037, -0.00015866, -307.79696791, -0.00052887, 0.4, 0.3, 0.003, 0.0, 0.0, 12006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2006, 99999, 'P', 42006, 'Vy', 32006, 'Vz', 22006, 'My', 12006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172006, 72006, 172006, 2006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123006, 123006, 23006, 2006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172007, 8.35, 4.45, 4.925)
    ops.node(123007, 8.35, 4.45, 6.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2007, 172007, 123007, 0.1375, 27701102.23286538, 11542125.93036058, 0.00204719, 0.00078776, 0.00381276, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22007, 155.07645406, 0.00064921, 188.6706767, 0.02299035, 18.86706767, 0.07776846, -155.07645406, -0.00064921, -188.6706767, -0.02299035, -18.86706767, -0.07776846, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12007, 71.44316327, 0.0010898, 86.91990052, 0.01866871, 8.69199005, 0.04968858, -71.44316327, -0.0010898, -86.91990052, -0.01866871, -8.69199005, -0.04968858, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22007, 2007, 0.0, 213.39678276, 0.01298425, 213.39678276, 0.03895276, 149.37774793, -4812.36150531, 0.05, 2, 0, 72007, 23007, 2, 3)
    ops.uniaxialMaterial('LimitState', 42007, 53.34919569, 9.278e-05, 160.04758707, 0.00027834, 533.49195689, 0.00092779, -53.34919569, -9.278e-05, -160.04758707, -0.00027834, -533.49195689, -0.00092779, 0.4, 0.3, 0.003, 0.0, 0.0, 22007, 2)
    ops.limitCurve('ThreePoint', 12007, 2007, 0.0, 121.07988652, 0.02179605, 121.07988652, 0.06538815, 84.75592056, -1723.36464385, 0.05, 2, 0, 72007, 23007, 1, 3)
    ops.uniaxialMaterial('LimitState', 32007, 30.26997163, 5.264e-05, 90.80991489, 0.00015793, 302.6997163, 0.00052642, -30.26997163, -5.264e-05, -90.80991489, -0.00015793, -302.6997163, -0.00052642, 0.4, 0.3, 0.003, 0.0, 0.0, 12007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2007, 99999, 'P', 42007, 'Vy', 32007, 'Vz', 22007, 'My', 12007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172007, 72007, 172007, 2007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123007, 123007, 23007, 2007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172008, 13.8, 4.45, 4.925)
    ops.node(123008, 13.8, 4.45, 6.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2008, 172008, 123008, 0.125, 27747327.30093216, 11561386.3753884, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22008, 132.23226997, 0.00067074, 161.0559714, 0.01868758, 16.10559714, 0.06793901, -132.23226997, -0.00067074, -161.0559714, -0.01868758, -16.10559714, -0.06793901, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12008, 57.2385305, 0.00106897, 69.71526038, 0.01578392, 6.97152604, 0.04625339, -57.2385305, -0.00106897, -69.71526038, -0.01578392, -6.97152604, -0.04625339, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22008, 2008, 0.0, 168.24743926, 0.01341486, 168.24743926, 0.04024458, 117.77320749, -3756.82546014, 0.05, 2, 0, 72008, 23008, 2, 3)
    ops.uniaxialMaterial('LimitState', 42008, 42.06185982, 8.033e-05, 126.18557945, 0.00024099, 420.61859816, 0.0008033, -42.06185982, -8.033e-05, -126.18557945, -0.00024099, -420.61859816, -0.0008033, 0.4, 0.3, 0.003, 0.0, 0.0, 22008, 2)
    ops.limitCurve('ThreePoint', 12008, 2008, 0.0, 102.81043497, 0.02137943, 102.81043497, 0.06413828, 71.96730448, -1486.96988337, 0.05, 2, 0, 72008, 23008, 1, 3)
    ops.uniaxialMaterial('LimitState', 32008, 25.70260874, 4.909e-05, 77.10782623, 0.00014726, 257.02608743, 0.00049087, -25.70260874, -4.909e-05, -77.10782623, -0.00014726, -257.02608743, -0.00049087, 0.4, 0.3, 0.003, 0.0, 0.0, 12008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2008, 99999, 'P', 42008, 'Vy', 32008, 'Vz', 22008, 'My', 12008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172008, 72008, 172008, 2008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123008, 123008, 23008, 2008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172009, 0.0, 8.9, 4.925)
    ops.node(123009, 0.0, 8.9, 6.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2009, 172009, 123009, 0.125, 27498264.73159692, 11457610.30483205, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22009, 130.69169524, 0.00067206, 159.24919989, 0.01867698, 15.92491999, 0.06768229, -130.69169524, -0.00067206, -159.24919989, -0.01867698, -15.92491999, -0.06768229, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12009, 56.45390876, 0.00107987, 68.78967929, 0.01578509, 6.87896793, 0.0461023, -56.45390876, -0.00107987, -68.78967929, -0.01578509, -6.87896793, -0.0461023, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22009, 2009, 0.0, 166.84482619, 0.01344118, 166.84482619, 0.04032355, 116.79137833, -3743.154849, 0.05, 2, 0, 72009, 23009, 2, 3)
    ops.uniaxialMaterial('LimitState', 42009, 41.71120655, 8.038e-05, 125.13361964, 0.00024115, 417.11206547, 0.00080382, -41.71120655, -8.038e-05, -125.13361964, -0.00024115, -417.11206547, -0.00080382, 0.4, 0.3, 0.003, 0.0, 0.0, 22009, 2)
    ops.limitCurve('ThreePoint', 12009, 2009, 0.0, 101.22115142, 0.02159745, 101.22115142, 0.06479235, 70.854806, -1482.66878135, 0.05, 2, 0, 72009, 23009, 1, 3)
    ops.uniaxialMaterial('LimitState', 32009, 25.30528786, 4.877e-05, 75.91586357, 0.0001463, 253.05287856, 0.00048766, -25.30528786, -4.877e-05, -75.91586357, -0.0001463, -253.05287856, -0.00048766, 0.4, 0.3, 0.003, 0.0, 0.0, 12009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2009, 99999, 'P', 42009, 'Vy', 32009, 'Vz', 22009, 'My', 12009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172009, 72009, 172009, 2009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123009, 123009, 23009, 2009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172010, 5.45, 8.9, 4.925)
    ops.node(123010, 5.45, 8.9, 6.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2010, 172010, 123010, 0.125, 28426418.45423739, 11844341.02259891, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22010, 136.2459959, 0.00067331, 165.6193048, 0.02305296, 16.56193048, 0.07944515, -136.2459959, -0.00067331, -165.6193048, -0.02305296, -16.56193048, -0.07944515, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12010, 70.03897158, 0.00107346, 85.13869128, 0.0191455, 8.51386913, 0.05310644, -70.03897158, -0.00107346, -85.13869128, -0.0191455, -8.51386913, -0.05310644, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22010, 2010, 0.0, 185.81563092, 0.01346625, 185.81563092, 0.04039874, 130.07094165, -4477.84757985, 0.05, 2, 0, 72010, 23010, 2, 3)
    ops.uniaxialMaterial('LimitState', 42010, 46.45390773, 8.66e-05, 139.36172319, 0.0002598, 464.53907731, 0.00086599, -46.45390773, -8.66e-05, -139.36172319, -0.0002598, -464.53907731, -0.00086599, 0.4, 0.3, 0.003, 0.0, 0.0, 22010, 2)
    ops.limitCurve('ThreePoint', 12010, 2010, 0.0, 115.33221082, 0.02146917, 115.33221082, 0.06440751, 80.73254757, -1754.00139662, 0.05, 2, 0, 72010, 23010, 1, 3)
    ops.uniaxialMaterial('LimitState', 32010, 28.83305271, 5.375e-05, 86.49915812, 0.00016125, 288.33052705, 0.0005375, -28.83305271, -5.375e-05, -86.49915812, -0.00016125, -288.33052705, -0.0005375, 0.4, 0.3, 0.003, 0.0, 0.0, 12010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2010, 99999, 'P', 42010, 'Vy', 32010, 'Vz', 22010, 'My', 12010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172010, 72010, 172010, 2010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123010, 123010, 23010, 2010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172011, 8.35, 8.9, 4.925)
    ops.node(123011, 8.35, 8.9, 6.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2011, 172011, 123011, 0.125, 27904915.06573193, 11627047.94405497, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22011, 136.64119172, 0.00067857, 166.25923134, 0.02299815, 16.62592313, 0.07877786, -136.64119172, -0.00067857, -166.25923134, -0.02299815, -16.62592313, -0.07877786, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12011, 70.28032922, 0.00108417, 85.51413646, 0.01910771, 8.55141365, 0.0526998, -70.28032922, -0.00108417, -85.51413646, -0.01910771, -8.55141365, -0.0526998, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22011, 2011, 0.0, 182.49762083, 0.01357133, 182.49762083, 0.04071398, 127.74833458, -4421.25200104, 0.05, 2, 0, 72011, 23011, 2, 3)
    ops.uniaxialMaterial('LimitState', 42011, 45.62440521, 8.664e-05, 136.87321562, 0.00025993, 456.24405208, 0.00086642, -45.62440521, -8.664e-05, -136.87321562, -0.00025993, -456.24405208, -0.00086642, 0.4, 0.3, 0.003, 0.0, 0.0, 22011, 2)
    ops.limitCurve('ThreePoint', 12011, 2011, 0.0, 113.1017805, 0.02168334, 113.1017805, 0.06505002, 79.17124635, -1736.27948923, 0.05, 2, 0, 72011, 23011, 1, 3)
    ops.uniaxialMaterial('LimitState', 32011, 28.27544513, 5.37e-05, 84.82633538, 0.00016109, 282.75445126, 0.00053696, -28.27544513, -5.37e-05, -84.82633538, -0.00016109, -282.75445126, -0.00053696, 0.4, 0.3, 0.003, 0.0, 0.0, 12011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2011, 99999, 'P', 42011, 'Vy', 32011, 'Vz', 22011, 'My', 12011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172011, 72011, 172011, 2011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123011, 123011, 23011, 2011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172012, 13.8, 8.9, 4.925)
    ops.node(123012, 13.8, 8.9, 6.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2012, 172012, 123012, 0.125, 26928738.82379294, 11220307.84324706, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22012, 130.69196151, 0.00068604, 159.3971655, 0.01871913, 15.93971655, 0.06712898, -130.69196151, -0.00068604, -159.3971655, -0.01871913, -15.93971655, -0.06712898, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12012, 56.27404121, 0.00112158, 68.63408091, 0.0158498, 6.86340809, 0.04579863, -56.27404121, -0.00112158, -68.63408091, -0.0158498, -6.86340809, -0.04579863, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22012, 2012, 0.0, 163.4503443, 0.01372076, 163.4503443, 0.04116229, 114.41524101, -3695.40510046, 0.05, 2, 0, 72012, 23012, 2, 3)
    ops.uniaxialMaterial('LimitState', 42012, 40.86258607, 8.041e-05, 122.58775822, 0.00024124, 408.62586074, 0.00080412, -40.86258607, -8.041e-05, -122.58775822, -0.00024124, -408.62586074, -0.00080412, 0.4, 0.3, 0.003, 0.0, 0.0, 22012, 2)
    ops.limitCurve('ThreePoint', 12012, 2012, 0.0, 99.45181589, 0.02243154, 99.45181589, 0.06729462, 69.61627113, -1467.6328375, 0.05, 2, 0, 72012, 23012, 1, 3)
    ops.uniaxialMaterial('LimitState', 32012, 24.86295397, 4.893e-05, 74.58886192, 0.00014678, 248.62953974, 0.00048927, -24.86295397, -4.893e-05, -74.58886192, -0.00014678, -248.62953974, -0.00048927, 0.4, 0.3, 0.003, 0.0, 0.0, 12012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2012, 99999, 'P', 42012, 'Vy', 32012, 'Vz', 22012, 'My', 12012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172012, 72012, 172012, 2012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123012, 123012, 23012, 2012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172013, 0.0, 13.35, 4.9)
    ops.node(123013, 0.0, 13.35, 6.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2013, 172013, 123013, 0.0875, 28178032.43047657, 11740846.84603191, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22013, 64.0203981, 0.00110735, 77.97478672, 0.02739934, 7.79747867, 0.08102882, -64.0203981, -0.00110735, -77.97478672, -0.02739934, -7.79747867, -0.08102882, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12013, 83.20505476, 0.00084423, 101.34108178, 0.03032935, 10.13410818, 0.10071514, -83.20505476, -0.00084423, -101.34108178, -0.03032935, -10.13410818, -0.10071514, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22013, 2013, 0.0, 103.8868514, 0.02214704, 103.8868514, 0.06644113, 72.72079598, -3353.3827432, 0.05, 2, 0, 72013, 23013, 2, 3)
    ops.uniaxialMaterial('LimitState', 42013, 25.97171285, 6.978e-05, 77.91513855, 0.00020933, 259.71712851, 0.00069775, -25.97171285, -6.978e-05, -77.91513855, -0.00020933, -259.71712851, -0.00069775, 0.4, 0.3, 0.003, 0.0, 0.0, 22013, 2)
    ops.limitCurve('ThreePoint', 12013, 2013, 0.0, 125.91564505, 0.01688455, 125.91564505, 0.05065366, 88.14095154, -5805.25448282, 0.05, 2, 0, 72013, 23013, 1, 3)
    ops.uniaxialMaterial('LimitState', 32013, 31.47891126, 8.457e-05, 94.43673379, 0.00025371, 314.78911263, 0.00084571, -31.47891126, -8.457e-05, -94.43673379, -0.00025371, -314.78911263, -0.00084571, 0.4, 0.3, 0.003, 0.0, 0.0, 12013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2013, 99999, 'P', 42013, 'Vy', 32013, 'Vz', 22013, 'My', 12013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172013, 72013, 172013, 2013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123013, 123013, 23013, 2013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172014, 5.45, 13.35, 4.9)
    ops.node(123014, 5.45, 13.35, 6.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2014, 172014, 123014, 0.0875, 29280730.9550745, 12200304.56461438, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22014, 55.32611454, 0.00107712, 67.13640636, 0.02075851, 6.71364064, 0.06502592, -55.32611454, -0.00107712, -67.13640636, -0.02075851, -6.71364064, -0.06502592, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12014, 76.28511269, 0.0008215, 92.56945597, 0.02276883, 9.2569456, 0.08009394, -76.28511269, -0.0008215, -92.56945597, -0.02276883, -9.2569456, -0.08009394, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22014, 2014, 0.0, 94.73953649, 0.02154235, 94.73953649, 0.06462706, 66.31767554, -1897.32703792, 0.05, 2, 0, 72014, 23014, 2, 3)
    ops.uniaxialMaterial('LimitState', 42014, 23.68488412, 6.124e-05, 71.05465237, 0.00018371, 236.84884122, 0.00061235, -23.68488412, -6.124e-05, -71.05465237, -0.00018371, -236.84884122, -0.00061235, 0.4, 0.3, 0.003, 0.0, 0.0, 22014, 2)
    ops.limitCurve('ThreePoint', 12014, 2014, 0.0, 111.13703187, 0.01643009, 111.13703187, 0.04929026, 77.79592231, -3063.5633607, 0.05, 2, 0, 72014, 23014, 1, 3)
    ops.uniaxialMaterial('LimitState', 32014, 27.78425797, 7.183e-05, 83.3527739, 0.0002155, 277.84257968, 0.00071834, -27.78425797, -7.183e-05, -83.3527739, -0.0002155, -277.84257968, -0.00071834, 0.4, 0.3, 0.003, 0.0, 0.0, 12014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2014, 99999, 'P', 42014, 'Vy', 32014, 'Vz', 22014, 'My', 12014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172014, 72014, 172014, 2014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123014, 123014, 23014, 2014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172015, 8.35, 13.35, 4.9)
    ops.node(123015, 8.35, 13.35, 6.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2015, 172015, 123015, 0.0875, 27736419.81023252, 11556841.58759688, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22015, 55.20453213, 0.00111386, 67.19090261, 0.02155328, 6.71909026, 0.06448205, -55.20453213, -0.00111386, -67.19090261, -0.02155328, -6.71909026, -0.06448205, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12015, 76.2454017, 0.00084439, 92.80030393, 0.02363701, 9.28003039, 0.07922862, -76.2454017, -0.00084439, -92.80030393, -0.02363701, -9.28003039, -0.07922862, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22015, 2015, 0.0, 92.69828322, 0.02227726, 92.69828322, 0.06683178, 64.88879825, -2016.88908981, 0.05, 2, 0, 72015, 23015, 2, 3)
    ops.uniaxialMaterial('LimitState', 42015, 23.1745708, 6.325e-05, 69.52371241, 0.00018976, 231.74570804, 0.00063252, -23.1745708, -6.325e-05, -69.52371241, -0.00018976, -231.74570804, -0.00063252, 0.4, 0.3, 0.003, 0.0, 0.0, 22015, 2)
    ops.limitCurve('ThreePoint', 12015, 2015, 0.0, 109.84755389, 0.01688779, 109.84755389, 0.05066338, 76.89328772, -3276.59215306, 0.05, 2, 0, 72015, 23015, 1, 3)
    ops.uniaxialMaterial('LimitState', 32015, 27.46188847, 7.495e-05, 82.38566542, 0.00022486, 274.61888472, 0.00074954, -27.46188847, -7.495e-05, -82.38566542, -0.00022486, -274.61888472, -0.00074954, 0.4, 0.3, 0.003, 0.0, 0.0, 12015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2015, 99999, 'P', 42015, 'Vy', 32015, 'Vz', 22015, 'My', 12015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172015, 72015, 172015, 2015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123015, 123015, 23015, 2015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172016, 13.8, 13.35, 4.9)
    ops.node(123016, 13.8, 13.35, 6.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2016, 172016, 123016, 0.0875, 28773795.87523847, 11989081.6146827, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22016, 60.90276355, 0.00112957, 74.08454355, 0.02687552, 7.40845435, 0.0809852, -60.90276355, -0.00112957, -74.08454355, -0.02687552, -7.40845435, -0.0809852, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12016, 80.39769198, 0.00084828, 97.79894977, 0.02972104, 9.77989498, 0.10073708, -80.39769198, -0.00084828, -97.79894977, -0.02972104, -9.77989498, -0.10073708, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22016, 2016, 0.0, 102.79397911, 0.02259142, 102.79397911, 0.06777426, 71.95578538, -3108.71227582, 0.05, 2, 0, 72016, 23016, 2, 3)
    ops.uniaxialMaterial('LimitState', 42016, 25.69849478, 6.761e-05, 77.09548433, 0.00020284, 256.98494778, 0.00067612, -25.69849478, -6.761e-05, -77.09548433, -0.00020284, -256.98494778, -0.00067612, 0.4, 0.3, 0.003, 0.0, 0.0, 22016, 2)
    ops.limitCurve('ThreePoint', 12016, 2016, 0.0, 123.78538411, 0.01696566, 123.78538411, 0.05089698, 86.64976888, -5355.11033509, 0.05, 2, 0, 72016, 23016, 1, 3)
    ops.uniaxialMaterial('LimitState', 32016, 30.94634603, 8.142e-05, 92.83903808, 0.00024426, 309.46346027, 0.00081419, -30.94634603, -8.142e-05, -92.83903808, -0.00024426, -309.46346027, -0.00081419, 0.4, 0.3, 0.003, 0.0, 0.0, 12016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2016, 99999, 'P', 42016, 'Vy', 32016, 'Vz', 22016, 'My', 12016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172016, 72016, 172016, 2016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123016, 123016, 23016, 2016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173001, 0.0, 0.0, 7.2)
    ops.node(124001, 0.0, 0.0, 8.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3001, 173001, 124001, 0.0875, 27398926.139446, 11416219.22476917, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23001, 58.41335147, 0.0011049, 71.50764812, 0.03665293, 7.15076481, 0.1109069, -58.41335147, -0.0011049, -71.50764812, -0.03665293, -7.15076481, -0.1109069, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13001, 75.75141503, 0.0008403, 92.73231879, 0.04095642, 9.27323188, 0.13987148, -75.75141503, -0.0008403, -92.73231879, -0.04095642, -9.27323188, -0.13987148, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23001, 3001, 0.0, 113.0165668, 0.02209805, 113.0165668, 0.06629415, 79.11159676, -14734.44420803, 0.05, 2, 0, 73001, 24001, 2, 3)
    ops.uniaxialMaterial('LimitState', 43001, 28.2541417, 7.807e-05, 84.7624251, 0.0002342, 282.54141701, 0.00078066, -28.2541417, -7.807e-05, -84.7624251, -0.0002342, -282.54141701, -0.00078066, 0.4, 0.3, 0.003, 0.0, 0.0, 23001, 2)
    ops.limitCurve('ThreePoint', 13001, 3001, 0.0, 141.48550271, 0.01680607, 141.48550271, 0.05041821, 99.0398519, -28034.80348391, 0.05, 2, 0, 73001, 24001, 1, 3)
    ops.uniaxialMaterial('LimitState', 33001, 35.37137568, 9.773e-05, 106.11412703, 0.00029319, 353.71375677, 0.00097731, -35.37137568, -9.773e-05, -106.11412703, -0.00029319, -353.71375677, -0.00097731, 0.4, 0.3, 0.003, 0.0, 0.0, 13001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3001, 99999, 'P', 43001, 'Vy', 33001, 'Vz', 23001, 'My', 13001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173001, 73001, 173001, 3001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124001, 124001, 24001, 3001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173004, 13.8, 0.0, 7.2)
    ops.node(124004, 13.8, 0.0, 8.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3004, 173004, 124004, 0.0875, 27877473.28220074, 11615613.86758364, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23004, 58.63703641, 0.00108761, 71.70309081, 0.03584228, 7.17030908, 0.11025573, -58.63703641, -0.00108761, -71.70309081, -0.03584228, -7.17030908, -0.11025573, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13004, 75.86714619, 0.00083022, 92.77257524, 0.04005102, 9.27725752, 0.13917852, -75.86714619, -0.00083022, -92.77257524, -0.04005102, -9.27725752, -0.13917852, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23004, 3004, 0.0, 111.83992489, 0.02175227, 111.83992489, 0.06525682, 78.28794742, -13827.62331623, 0.05, 2, 0, 73004, 24004, 2, 3)
    ops.uniaxialMaterial('LimitState', 43004, 27.95998122, 7.593e-05, 83.87994367, 0.00022778, 279.59981223, 0.00075927, -27.95998122, -7.593e-05, -83.87994367, -0.00022778, -279.59981223, -0.00075927, 0.4, 0.3, 0.003, 0.0, 0.0, 23004, 2)
    ops.limitCurve('ThreePoint', 13004, 3004, 0.0, 139.3705131, 0.01660447, 139.3705131, 0.0498134, 97.55935917, -26284.0366933, 0.05, 2, 0, 73004, 24004, 1, 3)
    ops.uniaxialMaterial('LimitState', 33004, 34.84262827, 9.462e-05, 104.52788482, 0.00028385, 348.42628274, 0.00094617, -34.84262827, -9.462e-05, -104.52788482, -0.00028385, -348.42628274, -0.00094617, 0.4, 0.3, 0.003, 0.0, 0.0, 13004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3004, 99999, 'P', 43004, 'Vy', 33004, 'Vz', 23004, 'My', 13004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173004, 73004, 173004, 3004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124004, 124004, 24004, 3004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173005, 0.0, 4.45, 7.225)
    ops.node(124005, 0.0, 4.45, 8.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3005, 173005, 124005, 0.125, 27584856.71586768, 11493690.2982782, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23005, 110.70216257, 0.00065602, 135.40598361, 0.01985102, 13.54059836, 0.0750852, -110.70216257, -0.00065602, -135.40598361, -0.01985102, -13.54059836, -0.0750852, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13005, 46.78489719, 0.00105988, 57.22521471, 0.01673707, 5.72252147, 0.05090778, -46.78489719, -0.00105988, -57.22521471, -0.01673707, -5.72252147, -0.05090778, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23005, 3005, 0.0, 156.05015831, 0.01312048, 156.05015831, 0.03936144, 109.23511082, -8429.02832551, 0.05, 2, 0, 73005, 24005, 2, 3)
    ops.uniaxialMaterial('LimitState', 43005, 39.01253958, 7.495e-05, 117.03761873, 0.00022484, 390.12539578, 0.00074945, -39.01253958, -7.495e-05, -117.03761873, -0.00022484, -390.12539578, -0.00074945, 0.4, 0.3, 0.003, 0.0, 0.0, 23005, 2)
    ops.limitCurve('ThreePoint', 13005, 3005, 0.0, 93.31592519, 0.02119763, 93.31592519, 0.06359289, 65.32114763, -2521.08014947, 0.05, 2, 0, 73005, 24005, 1, 3)
    ops.uniaxialMaterial('LimitState', 33005, 23.3289813, 4.482e-05, 69.98694389, 0.00013445, 233.28981298, 0.00044816, -23.3289813, -4.482e-05, -69.98694389, -0.00013445, -233.28981298, -0.00044816, 0.4, 0.3, 0.003, 0.0, 0.0, 13005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3005, 99999, 'P', 43005, 'Vy', 33005, 'Vz', 23005, 'My', 13005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173005, 73005, 173005, 3005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124005, 124005, 24005, 3005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173006, 5.45, 4.45, 7.225)
    ops.node(124006, 5.45, 4.45, 8.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3006, 173006, 124006, 0.1375, 27604231.51047998, 11501763.12936666, 0.00204719, 0.00078776, 0.00381276, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23006, 150.10616221, 0.00063281, 183.45112101, 0.02033729, 18.3451121, 0.07429924, -150.10616221, -0.00063281, -183.45112101, -0.02033729, -18.3451121, -0.07429924, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13006, 55.48555783, 0.00104926, 67.81125861, 0.01675823, 6.78112586, 0.04828164, -55.48555783, -0.00104926, -67.81125861, -0.01675823, -6.78112586, -0.04828164, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23006, 3006, 0.0, 184.11713978, 0.01265613, 184.11713978, 0.0379684, 128.88199785, -6887.72250289, 0.05, 2, 0, 73006, 24006, 2, 3)
    ops.uniaxialMaterial('LimitState', 43006, 46.02928494, 8.033e-05, 138.08785483, 0.00024099, 460.29284945, 0.0008033, -46.02928494, -8.033e-05, -138.08785483, -0.00024099, -460.29284945, -0.0008033, 0.4, 0.3, 0.003, 0.0, 0.0, 23006, 2)
    ops.limitCurve('ThreePoint', 13006, 3006, 0.0, 103.14379303, 0.02098518, 103.14379303, 0.06295555, 72.20065512, -1910.04370536, 0.05, 2, 0, 73006, 24006, 1, 3)
    ops.uniaxialMaterial('LimitState', 33006, 25.78594826, 4.5e-05, 77.35784477, 0.000135, 257.85948257, 0.00045001, -25.78594826, -4.5e-05, -77.35784477, -0.000135, -257.85948257, -0.00045001, 0.4, 0.3, 0.003, 0.0, 0.0, 13006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3006, 99999, 'P', 43006, 'Vy', 33006, 'Vz', 23006, 'My', 13006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173006, 73006, 173006, 3006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124006, 124006, 24006, 3006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173007, 8.35, 4.45, 7.225)
    ops.node(124007, 8.35, 4.45, 8.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3007, 173007, 124007, 0.1375, 28376587.9715132, 11823578.32146383, 0.00204719, 0.00078776, 0.00381276, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23007, 151.24446113, 0.00063153, 184.5243958, 0.01963858, 18.45243958, 0.07394711, -151.24446113, -0.00063153, -184.5243958, -0.01963858, -18.45243958, -0.07394711, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13007, 55.97023704, 0.00104459, 68.28596628, 0.01619756, 6.82859663, 0.04792342, -55.97023704, -0.00104459, -68.28596628, -0.01619756, -6.82859663, -0.04792342, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23007, 3007, 0.0, 187.21706382, 0.01263052, 187.21706382, 0.03789157, 131.05194467, -6661.37189245, 0.05, 2, 0, 73007, 24007, 2, 3)
    ops.uniaxialMaterial('LimitState', 43007, 46.80426596, 7.946e-05, 140.41279787, 0.00023838, 468.04265955, 0.00079459, -46.80426596, -7.946e-05, -140.41279787, -0.00023838, -468.04265955, -0.00079459, 0.4, 0.3, 0.003, 0.0, 0.0, 23007, 2)
    ops.limitCurve('ThreePoint', 13007, 3007, 0.0, 102.60197847, 0.02089181, 102.60197847, 0.06267542, 71.82138493, -1855.80129696, 0.05, 2, 0, 73007, 24007, 1, 3)
    ops.uniaxialMaterial('LimitState', 33007, 25.65049462, 4.355e-05, 76.95148385, 0.00013064, 256.50494617, 0.00043546, -25.65049462, -4.355e-05, -76.95148385, -0.00013064, -256.50494617, -0.00043546, 0.4, 0.3, 0.003, 0.0, 0.0, 13007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3007, 99999, 'P', 43007, 'Vy', 33007, 'Vz', 23007, 'My', 13007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173007, 73007, 173007, 3007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124007, 124007, 24007, 3007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173008, 13.8, 4.45, 7.225)
    ops.node(124008, 13.8, 4.45, 8.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3008, 173008, 124008, 0.125, 27810862.23994924, 11587859.26664552, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23008, 114.00764863, 0.00065349, 139.3782648, 0.02005277, 13.93782648, 0.07536043, -114.00764863, -0.00065349, -139.3782648, -0.02005277, -13.93782648, -0.07536043, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13008, 48.4450053, 0.00103432, 59.2256823, 0.01687836, 5.92256823, 0.05109452, -48.4450053, -0.00103432, -59.2256823, -0.01687836, -5.92256823, -0.05109452, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23008, 3008, 0.0, 158.25937871, 0.01306981, 158.25937871, 0.03920944, 110.78156509, -8670.22346676, 0.05, 2, 0, 73008, 24008, 2, 3)
    ops.uniaxialMaterial('LimitState', 43008, 39.56484468, 7.539e-05, 118.69453403, 0.00022617, 395.64844677, 0.00075389, -39.56484468, -7.539e-05, -118.69453403, -0.00022617, -395.64844677, -0.00075389, 0.4, 0.3, 0.003, 0.0, 0.0, 23008, 2)
    ops.limitCurve('ThreePoint', 13008, 3008, 0.0, 97.05569874, 0.02068644, 97.05569874, 0.06205932, 67.93898912, -2586.99456235, 0.05, 2, 0, 73008, 24008, 1, 3)
    ops.uniaxialMaterial('LimitState', 33008, 24.26392468, 4.623e-05, 72.79177405, 0.0001387, 242.63924684, 0.00046234, -24.26392468, -4.623e-05, -72.79177405, -0.0001387, -242.63924684, -0.00046234, 0.4, 0.3, 0.003, 0.0, 0.0, 13008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3008, 99999, 'P', 43008, 'Vy', 33008, 'Vz', 23008, 'My', 13008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173008, 73008, 173008, 3008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124008, 124008, 24008, 3008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173009, 0.0, 8.9, 7.225)
    ops.node(124009, 0.0, 8.9, 8.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3009, 173009, 124009, 0.125, 29172134.69635449, 12155056.12348104, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23009, 111.57669064, 0.00064045, 135.9543531, 0.01978363, 13.59543531, 0.07548538, -111.57669064, -0.00064045, -135.9543531, -0.01978363, -13.59543531, -0.07548538, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13009, 47.38120291, 0.00101331, 57.7332125, 0.01664817, 5.77332125, 0.05110814, -47.38120291, -0.00101331, -57.7332125, -0.01664817, -5.77332125, -0.05110814, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23009, 3009, 0.0, 164.30543787, 0.01280907, 164.30543787, 0.03842721, 115.01380651, -8516.76205072, 0.05, 2, 0, 73009, 24009, 2, 3)
    ops.uniaxialMaterial('LimitState', 43009, 41.07635947, 7.462e-05, 123.22907841, 0.00022385, 410.76359469, 0.00074616, -41.07635947, -7.462e-05, -123.22907841, -0.00022385, -410.76359469, -0.00074616, 0.4, 0.3, 0.003, 0.0, 0.0, 23009, 2)
    ops.limitCurve('ThreePoint', 13009, 3009, 0.0, 101.37706703, 0.02026616, 101.37706703, 0.06079849, 70.96394692, -2545.06542603, 0.05, 2, 0, 73009, 24009, 1, 3)
    ops.uniaxialMaterial('LimitState', 33009, 25.34426676, 4.604e-05, 76.03280028, 0.00013812, 253.44266759, 0.00046039, -25.34426676, -4.604e-05, -76.03280028, -0.00013812, -253.44266759, -0.00046039, 0.4, 0.3, 0.003, 0.0, 0.0, 13009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3009, 99999, 'P', 43009, 'Vy', 33009, 'Vz', 23009, 'My', 13009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173009, 73009, 173009, 3009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124009, 124009, 24009, 3009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173010, 5.45, 8.9, 7.225)
    ops.node(124010, 5.45, 8.9, 8.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3010, 173010, 124010, 0.125, 27828952.93729831, 11595397.05720763, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23010, 132.70090965, 0.00066064, 162.16030922, 0.02051967, 16.21603092, 0.07518202, -132.70090965, -0.00066064, -162.16030922, -0.02051967, -16.21603092, -0.07518202, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13010, 54.1143151, 0.00105296, 66.12761053, 0.01727249, 6.61276105, 0.05108944, -54.1143151, -0.00105296, -66.12761053, -0.01727249, -6.61276105, -0.05108944, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23010, 3010, 0.0, 158.43323446, 0.01321279, 158.43323446, 0.03963836, 110.90326412, -7077.07809073, 0.05, 2, 0, 73010, 24010, 2, 3)
    ops.uniaxialMaterial('LimitState', 43010, 39.60830861, 7.542e-05, 118.82492584, 0.00022627, 396.08308614, 0.00075422, -39.60830861, -7.542e-05, -118.82492584, -0.00022627, -396.08308614, -0.00075422, 0.4, 0.3, 0.003, 0.0, 0.0, 23010, 2)
    ops.limitCurve('ThreePoint', 13010, 3010, 0.0, 96.67045457, 0.02105916, 96.67045457, 0.06317749, 67.6693182, -2196.6894349, 0.05, 2, 0, 73010, 24010, 1, 3)
    ops.uniaxialMaterial('LimitState', 33010, 24.16761364, 4.602e-05, 72.50284093, 0.00013806, 241.67613643, 0.0004602, -24.16761364, -4.602e-05, -72.50284093, -0.00013806, -241.67613643, -0.0004602, 0.4, 0.3, 0.003, 0.0, 0.0, 13010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3010, 99999, 'P', 43010, 'Vy', 33010, 'Vz', 23010, 'My', 13010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173010, 73010, 173010, 3010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124010, 124010, 24010, 3010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173011, 8.35, 8.9, 7.225)
    ops.node(124011, 8.35, 8.9, 8.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3011, 173011, 124011, 0.125, 26602686.18153297, 11084452.57563874, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23011, 132.45074125, 0.00067101, 162.26842434, 0.02070712, 16.22684243, 0.07484086, -132.45074125, -0.00067101, -162.26842434, -0.02070712, -16.22684243, -0.07484086, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13011, 53.8828727, 0.00107929, 66.01313642, 0.01744345, 6.60131364, 0.05093337, -53.8828727, -0.00107929, -66.01313642, -0.01744345, -6.60131364, -0.05093337, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23011, 3011, 0.0, 152.31074094, 0.01342013, 152.31074094, 0.0402604, 106.61751866, -7038.62724387, 0.05, 2, 0, 73011, 24011, 2, 3)
    ops.uniaxialMaterial('LimitState', 43011, 38.07768523, 7.585e-05, 114.2330557, 0.00022755, 380.77685235, 0.0007585, -38.07768523, -7.585e-05, -114.2330557, -0.00022755, -380.77685235, -0.0007585, 0.4, 0.3, 0.003, 0.0, 0.0, 23011, 2)
    ops.limitCurve('ThreePoint', 13011, 3011, 0.0, 91.85759134, 0.02158581, 91.85759134, 0.06475744, 64.30031394, -2185.97685924, 0.05, 2, 0, 73011, 24011, 1, 3)
    ops.uniaxialMaterial('LimitState', 33011, 22.96439783, 4.574e-05, 68.8931935, 0.00013723, 229.64397835, 0.00045745, -22.96439783, -4.574e-05, -68.8931935, -0.00013723, -229.64397835, -0.00045745, 0.4, 0.3, 0.003, 0.0, 0.0, 13011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3011, 99999, 'P', 43011, 'Vy', 33011, 'Vz', 23011, 'My', 13011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173011, 73011, 173011, 3011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124011, 124011, 24011, 3011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173012, 13.8, 8.9, 7.225)
    ops.node(124012, 13.8, 8.9, 8.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3012, 173012, 124012, 0.125, 27453647.18005611, 11439019.65835671, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23012, 110.67921314, 0.00064465, 135.41710589, 0.02032656, 13.54171059, 0.07551692, -110.67921314, -0.00064465, -135.41710589, -0.02032656, -13.54171059, -0.07551692, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13012, 46.948594, 0.00102151, 57.44206654, 0.01709639, 5.74420665, 0.05123998, -46.948594, -0.00102151, -57.44206654, -0.01709639, -5.74420665, -0.05123998, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23012, 3012, 0.0, 157.08766201, 0.01289301, 157.08766201, 0.03867903, 109.96136341, -8794.18801259, 0.05, 2, 0, 73012, 24012, 2, 3)
    ops.uniaxialMaterial('LimitState', 43012, 39.2719155, 7.58e-05, 117.81574651, 0.00022741, 392.71915504, 0.00075804, -39.2719155, -7.58e-05, -117.81574651, -0.00022741, -392.71915504, -0.00075804, 0.4, 0.3, 0.003, 0.0, 0.0, 23012, 2)
    ops.limitCurve('ThreePoint', 13012, 3012, 0.0, 95.87453938, 0.02043027, 95.87453938, 0.06129081, 67.11217757, -2620.84151825, 0.05, 2, 0, 73012, 24012, 1, 3)
    ops.uniaxialMaterial('LimitState', 33012, 23.96863485, 4.627e-05, 71.90590454, 0.0001388, 239.68634845, 0.00046265, -23.96863485, -4.627e-05, -71.90590454, -0.0001388, -239.68634845, -0.00046265, 0.4, 0.3, 0.003, 0.0, 0.0, 13012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3012, 99999, 'P', 43012, 'Vy', 33012, 'Vz', 23012, 'My', 13012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173012, 73012, 173012, 3012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124012, 124012, 24012, 3012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173013, 0.0, 13.35, 7.2)
    ops.node(124013, 0.0, 13.35, 8.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3013, 173013, 124013, 0.0875, 28615495.08058058, 11923122.95024191, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23013, 56.52974114, 0.00107725, 69.00269663, 0.03560539, 6.90026966, 0.11024329, -56.52974114, -0.00107725, -69.00269663, -0.03560539, -6.90026966, -0.11024329, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13013, 73.72935285, 0.00081847, 89.99730168, 0.03978362, 8.99973017, 0.13921013, -73.72935285, -0.00081847, -89.99730168, -0.03978362, -8.99973017, -0.13921013, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23013, 3013, 0.0, 112.61839978, 0.02154507, 112.61839978, 0.0646352, 78.83287985, -13430.71101758, 0.05, 2, 0, 73013, 24013, 2, 3)
    ops.uniaxialMaterial('LimitState', 43013, 28.15459995, 7.448e-05, 84.46379984, 0.00022345, 281.54599946, 0.00074484, -28.15459995, -7.448e-05, -84.46379984, -0.00022345, -281.54599946, -0.00074484, 0.4, 0.3, 0.003, 0.0, 0.0, 23013, 2)
    ops.limitCurve('ThreePoint', 13013, 3013, 0.0, 139.72861116, 0.01636935, 139.72861116, 0.04910804, 97.81002781, -25518.00627094, 0.05, 2, 0, 73013, 24013, 1, 3)
    ops.uniaxialMaterial('LimitState', 33013, 34.93215279, 9.241e-05, 104.79645837, 0.00027724, 349.32152791, 0.00092414, -34.93215279, -9.241e-05, -104.79645837, -0.00027724, -349.32152791, -0.00092414, 0.4, 0.3, 0.003, 0.0, 0.0, 13013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3013, 99999, 'P', 43013, 'Vy', 33013, 'Vz', 23013, 'My', 13013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173013, 73013, 173013, 3013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124013, 124013, 24013, 3013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173014, 5.45, 13.35, 7.2)
    ops.node(124014, 5.45, 13.35, 8.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3014, 173014, 124014, 0.0875, 27539782.31906125, 11474909.29960885, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23014, 39.14527136, 0.00105152, 47.87955633, 0.02227003, 4.78795563, 0.07127027, -39.14527136, -0.00105152, -47.87955633, -0.02227003, -4.78795563, -0.07127027, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13014, 58.08250271, 0.00080461, 71.04215564, 0.02446602, 7.10421556, 0.08792002, -58.08250271, -0.00080461, -71.04215564, -0.02446602, -7.10421556, -0.08792002, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23014, 3014, 0.0, 84.92084694, 0.0210304, 84.92084694, 0.06309119, 59.44459285, -4135.84254984, 0.05, 2, 0, 73014, 24014, 2, 3)
    ops.uniaxialMaterial('LimitState', 43014, 21.23021173, 5.836e-05, 63.6906352, 0.00017508, 212.30211734, 0.00058359, -21.23021173, -5.836e-05, -63.6906352, -0.00017508, -212.30211734, -0.00058359, 0.4, 0.3, 0.003, 0.0, 0.0, 23014, 2)
    ops.limitCurve('ThreePoint', 13014, 3014, 0.0, 101.69360879, 0.01609227, 101.69360879, 0.04827681, 71.18552615, -7577.18580988, 0.05, 2, 0, 73014, 24014, 1, 3)
    ops.uniaxialMaterial('LimitState', 33014, 25.4234022, 6.989e-05, 76.27020659, 0.00020966, 254.23402197, 0.00069885, -25.4234022, -6.989e-05, -76.27020659, -0.00020966, -254.23402197, -0.00069885, 0.4, 0.3, 0.003, 0.0, 0.0, 13014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3014, 99999, 'P', 43014, 'Vy', 33014, 'Vz', 23014, 'My', 13014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173014, 73014, 173014, 3014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124014, 124014, 24014, 3014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173015, 8.35, 13.35, 7.2)
    ops.node(124015, 8.35, 13.35, 8.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3015, 173015, 124015, 0.0875, 26181098.34604938, 10908790.97752057, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23015, 38.51159344, 0.00107574, 47.23487899, 0.02227532, 4.7234879, 0.07079592, -38.51159344, -0.00107574, -47.23487899, -0.02227532, -4.7234879, -0.07079592, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13015, 57.27067066, 0.00081823, 70.24308673, 0.02445853, 7.02430867, 0.08729142, -57.27067066, -0.00081823, -70.24308673, -0.02445853, -7.02430867, -0.08729142, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23015, 3015, 0.0, 81.01495331, 0.0215148, 81.01495331, 0.0645444, 56.71046731, -4024.18838438, 0.05, 2, 0, 73015, 24015, 2, 3)
    ops.uniaxialMaterial('LimitState', 43015, 20.25373833, 5.856e-05, 60.76121498, 0.00017569, 202.53738327, 0.00058564, -20.25373833, -5.856e-05, -60.76121498, -0.00017569, -202.53738327, -0.00058564, 0.4, 0.3, 0.003, 0.0, 0.0, 23015, 2)
    ops.limitCurve('ThreePoint', 13015, 3015, 0.0, 97.52980713, 0.01636464, 97.52980713, 0.04909392, 68.27086499, -7365.65533812, 0.05, 2, 0, 73015, 24015, 1, 3)
    ops.uniaxialMaterial('LimitState', 33015, 24.38245178, 7.05e-05, 73.14735535, 0.00021151, 243.82451783, 0.00070502, -24.38245178, -7.05e-05, -73.14735535, -0.00021151, -243.82451783, -0.00070502, 0.4, 0.3, 0.003, 0.0, 0.0, 13015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3015, 99999, 'P', 43015, 'Vy', 33015, 'Vz', 23015, 'My', 13015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173015, 73015, 173015, 3015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124015, 124015, 24015, 3015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173016, 13.8, 13.35, 7.2)
    ops.node(124016, 13.8, 13.35, 8.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3016, 173016, 124016, 0.0875, 27173540.72653969, 11322308.6360582, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23016, 58.43743582, 0.00110884, 71.57265711, 0.03665484, 7.15726571, 0.11082956, -58.43743582, -0.00110884, -71.57265711, -0.03665484, -7.15726571, -0.11082956, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13016, 75.76854465, 0.00084296, 92.79935012, 0.04095678, 9.27993501, 0.13976627, -75.76854465, -0.00084296, -92.79935012, -0.04095678, -9.27993501, -0.13976627, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23016, 3016, 0.0, 112.22632179, 0.02217677, 112.22632179, 0.06653032, 78.55842526, -14638.69425306, 0.05, 2, 0, 73016, 24016, 2, 3)
    ops.uniaxialMaterial('LimitState', 43016, 28.05658045, 7.816e-05, 84.16974135, 0.00023449, 280.56580449, 0.00078163, -28.05658045, -7.816e-05, -84.16974135, -0.00023449, -280.56580449, -0.00078163, 0.4, 0.3, 0.003, 0.0, 0.0, 23016, 2)
    ops.limitCurve('ThreePoint', 13016, 3016, 0.0, 140.59756855, 0.01685914, 140.59756855, 0.05057743, 98.41829799, -27849.90305959, 0.05, 2, 0, 73016, 24016, 1, 3)
    ops.uniaxialMaterial('LimitState', 33016, 35.14939214, 9.792e-05, 105.44817641, 0.00029377, 351.49392138, 0.00097923, -35.14939214, -9.792e-05, -105.44817641, -0.00029377, -351.49392138, -0.00097923, 0.4, 0.3, 0.003, 0.0, 0.0, 13016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3016, 99999, 'P', 43016, 'Vy', 33016, 'Vz', 23016, 'My', 13016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173016, 73016, 173016, 3016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124016, 124016, 24016, 3016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170002, 5.45, 0.0, 0.0)
    ops.node(124017, 5.45, 0.0, 0.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4041, 170002, 124017, 0.165, 26517997.71690856, 11049165.71537857, 0.00326155, 0.00457531, 0.00136125, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24041, 153.0650813, 0.0007808, 185.97467367, 0.03604384, 18.59746737, 0.0898239, -153.0650813, -0.0007808, -185.97467367, -0.03604384, -18.59746737, -0.0898239, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14041, 236.53093642, 0.00064955, 287.38601476, 0.04461643, 28.73860148, 0.13537378, -236.53093642, -0.00064955, -287.38601476, -0.04461643, -28.73860148, -0.13537378, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24041, 4041, 0.0, 287.13666297, 0.0156159, 287.13666297, 0.04684771, 200.99566408, -12248.79741617, 0.05, 2, 0, 70002, 24017, 2, 3)
    ops.uniaxialMaterial('LimitState', 44041, 71.78416574, 5.434e-05, 215.35249723, 0.00016301, 717.84165742, 0.00054337, -71.78416574, -5.434e-05, -215.35249723, -0.00016301, -717.84165742, -0.00054337, 0.4, 0.3, 0.003, 0.0, 0.0, 24041, 2)
    ops.limitCurve('ThreePoint', 14041, 4041, 0.0, 424.98601947, 0.01299094, 424.98601947, 0.03897281, 297.49021363, -30642.28175592, 0.05, 2, 0, 70002, 24017, 1, 3)
    ops.uniaxialMaterial('LimitState', 34041, 106.24650487, 8.042e-05, 318.73951461, 0.00024127, 1062.46504868, 0.00080423, -106.24650487, -8.042e-05, -318.73951461, -0.00024127, -1062.46504868, -0.00080423, 0.4, 0.3, 0.003, 0.0, 0.0, 14041, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4041, 99999, 'P', 44041, 'Vy', 34041, 'Vz', 24041, 'My', 14041, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170002, 70002, 170002, 4041, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124017, 124017, 24017, 4041, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174017, 5.45, 0.0, 1.35)
    ops.node(121002, 5.45, 0.0, 2.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4042, 174017, 121002, 0.165, 29899798.5694064, 12458249.40391933, 0.00326155, 0.00457531, 0.00136125, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24042, 122.65410653, 0.00076042, 148.36072471, 0.03539487, 14.83607247, 0.09630875, -122.65410653, -0.00076042, -148.36072471, -0.03539487, -14.83607247, -0.09630875, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14042, 204.90694214, 0.00063216, 247.85262634, 0.0438153, 24.78526263, 0.1438153, -204.90694214, -0.00063216, -247.85262634, -0.0438153, -24.78526263, -0.1438153, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24042, 4042, 0.0, 309.19481131, 0.0152084, 309.19481131, 0.0456252, 216.43636792, -12403.68204313, 0.05, 2, 0, 74017, 21002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44042, 77.29870283, 5.189e-05, 231.89610849, 0.00015568, 772.98702828, 0.00051893, -77.29870283, -5.189e-05, -231.89610849, -0.00015568, -772.98702828, -0.00051893, 0.4, 0.3, 0.003, 0.0, 0.0, 24042, 2)
    ops.limitCurve('ThreePoint', 14042, 4042, 0.0, 450.0655134, 0.0126431, 450.0655134, 0.0379293, 315.04585938, -31516.06389285, 0.05, 2, 0, 74017, 21002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34042, 112.51637835, 7.554e-05, 337.54913505, 0.00022661, 1125.16378349, 0.00075536, -112.51637835, -7.554e-05, -337.54913505, -0.00022661, -1125.16378349, -0.00075536, 0.4, 0.3, 0.003, 0.0, 0.0, 14042, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4042, 99999, 'P', 44042, 'Vy', 34042, 'Vz', 24042, 'My', 14042, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174017, 74017, 174017, 4042, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121002, 121002, 21002, 4042, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170003, 8.35, 0.0, 0.0)
    ops.node(124018, 8.35, 0.0, 0.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4043, 170003, 124018, 0.165, 29353960.10187443, 12230816.70911434, 0.00326155, 0.00457531, 0.00136125, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24043, 154.48774989, 0.00074763, 186.958173, 0.03583204, 18.6958173, 0.094833, -154.48774989, -0.00074763, -186.958173, -0.03583204, -18.6958173, -0.094833, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14043, 239.08586316, 0.00063321, 289.33722057, 0.04437738, 28.93372206, 0.14394533, -239.08586316, -0.00063321, -289.33722057, -0.04437738, -28.93372206, -0.14394533, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24043, 4043, 0.0, 306.54666254, 0.01495254, 306.54666254, 0.04485762, 214.58266378, -11800.41893153, 0.05, 2, 0, 70003, 24018, 2, 3)
    ops.uniaxialMaterial('LimitState', 44043, 76.63666563, 5.241e-05, 229.9099969, 0.00015722, 766.36665635, 0.00052405, -76.63666563, -5.241e-05, -229.9099969, -0.00015722, -766.36665635, -0.00052405, 0.4, 0.3, 0.003, 0.0, 0.0, 24043, 2)
    ops.limitCurve('ThreePoint', 14043, 4043, 0.0, 446.0932468, 0.01266421, 446.0932468, 0.03799264, 312.26527276, -29344.0408309, 0.05, 2, 0, 70003, 24018, 1, 3)
    ops.uniaxialMaterial('LimitState', 34043, 111.5233117, 7.626e-05, 334.5699351, 0.00022878, 1115.233117, 0.00076261, -111.5233117, -7.626e-05, -334.5699351, -0.00022878, -1115.233117, -0.00076261, 0.4, 0.3, 0.003, 0.0, 0.0, 14043, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4043, 99999, 'P', 44043, 'Vy', 34043, 'Vz', 24043, 'My', 14043, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170003, 70003, 170003, 4043, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124018, 124018, 24018, 4043, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174018, 8.35, 0.0, 1.35)
    ops.node(121003, 8.35, 0.0, 2.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4044, 174018, 121003, 0.165, 28446412.30822515, 11852671.79509382, 0.00326155, 0.00457531, 0.00136125, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24044, 124.5225627, 0.00074768, 151.04515887, 0.03586436, 15.10451589, 0.09463808, -124.5225627, -0.00074768, -151.04515887, -0.03586436, -15.10451589, -0.09463808, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14044, 204.51764202, 0.00063011, 248.07873417, 0.04441451, 24.80787342, 0.143599, -204.51764202, -0.00063011, -248.07873417, -0.04441451, -24.80787342, -0.143599, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24044, 4044, 0.0, 298.6414648, 0.0149535, 298.6414648, 0.0448605, 209.04902536, -12597.27539268, 0.05, 2, 0, 74018, 21003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44044, 74.6603662, 5.268e-05, 223.9810986, 0.00015805, 746.60366199, 0.00052683, -74.6603662, -5.268e-05, -223.9810986, -0.00015805, -746.60366199, -0.00052683, 0.4, 0.3, 0.003, 0.0, 0.0, 24044, 2)
    ops.limitCurve('ThreePoint', 14044, 4044, 0.0, 438.29240012, 0.01260225, 438.29240012, 0.03780675, 306.80468009, -32082.14013531, 0.05, 2, 0, 74018, 21003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34044, 109.57310003, 7.732e-05, 328.71930009, 0.00023196, 1095.7310003, 0.00077318, -109.57310003, -7.732e-05, -328.71930009, -0.00023196, -1095.7310003, -0.00077318, 0.4, 0.3, 0.003, 0.0, 0.0, 14044, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4044, 99999, 'P', 44044, 'Vy', 34044, 'Vz', 24044, 'My', 14044, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174018, 74018, 174018, 4044, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121003, 121003, 21003, 4044, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171002, 5.45, 0.0, 2.6)
    ops.node(124019, 5.45, 0.0, 3.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4046, 171002, 124019, 0.165, 27951959.79522955, 11646649.91467898, 0.00326155, 0.00457531, 0.00136125, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24046, 90.85830001, 0.00073004, 110.47773166, 0.03599306, 11.04777317, 0.0968344, -90.85830001, -0.00073004, -110.47773166, -0.03599306, -11.04777317, -0.0968344, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14046, 176.61942786, 0.00062091, 214.7576364, 0.04458775, 21.47576364, 0.14458775, -176.61942786, -0.00062091, -214.7576364, -0.04458775, -21.47576364, -0.14458775, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24046, 4046, 0.0, 288.47768661, 0.01460086, 288.47768661, 0.04380258, 201.93438063, -14065.64556068, 0.05, 2, 0, 71002, 24019, 2, 3)
    ops.uniaxialMaterial('LimitState', 44046, 72.11942165, 5.179e-05, 216.35826496, 0.00015537, 721.19421653, 0.0005179, -72.11942165, -5.179e-05, -216.35826496, -0.00015537, -721.19421653, -0.0005179, 0.4, 0.3, 0.003, 0.0, 0.0, 24046, 2)
    ops.limitCurve('ThreePoint', 14046, 4046, 0.0, 426.48182868, 0.01241814, 426.48182868, 0.03725441, 298.53728007, -37456.16686817, 0.05, 2, 0, 71002, 24019, 1, 3)
    ops.uniaxialMaterial('LimitState', 34046, 106.62045717, 7.657e-05, 319.86137151, 0.0002297, 1066.20457169, 0.00076566, -106.62045717, -7.657e-05, -319.86137151, -0.0002297, -1066.20457169, -0.00076566, 0.4, 0.3, 0.003, 0.0, 0.0, 14046, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4046, 99999, 'P', 44046, 'Vy', 34046, 'Vz', 24046, 'My', 14046, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171002, 71002, 171002, 4046, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124019, 124019, 24019, 4046, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174019, 5.45, 0.0, 3.65)
    ops.node(122002, 5.45, 0.0, 4.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4047, 174019, 122002, 0.165, 28344022.70482242, 11810009.46034267, 0.00326155, 0.00457531, 0.00136125, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24047, 93.24492332, 0.00072774, 113.38397837, 0.0360433, 11.33839784, 0.09878784, -93.24492332, -0.00072774, -113.38397837, -0.0360433, -11.33839784, -0.09878784, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14047, 163.04525169, 0.0006201, 198.25979404, 0.04465247, 19.8259794, 0.14465247, -163.04525169, -0.0006201, -198.25979404, -0.04465247, -19.8259794, -0.14465247, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24047, 4047, 0.0, 286.40830748, 0.01455485, 286.40830748, 0.04366455, 200.48581524, -14668.57266951, 0.05, 2, 0, 74019, 22002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44047, 71.60207687, 5.071e-05, 214.80623061, 0.00015212, 716.0207687, 0.00050707, -71.60207687, -5.071e-05, -214.80623061, -0.00015212, -716.0207687, -0.00050707, 0.4, 0.3, 0.003, 0.0, 0.0, 24047, 2)
    ops.limitCurve('ThreePoint', 14047, 4047, 0.0, 422.79150192, 0.01240202, 422.79150192, 0.03720605, 295.95405135, -39822.92362026, 0.05, 2, 0, 74019, 22002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34047, 105.69787548, 7.485e-05, 317.09362644, 0.00022456, 1056.97875481, 0.00074853, -105.69787548, -7.485e-05, -317.09362644, -0.00022456, -1056.97875481, -0.00074853, 0.4, 0.3, 0.003, 0.0, 0.0, 14047, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4047, 99999, 'P', 44047, 'Vy', 34047, 'Vz', 24047, 'My', 14047, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174019, 74019, 174019, 4047, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122002, 122002, 22002, 4047, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171003, 8.35, 0.0, 2.6)
    ops.node(124020, 8.35, 0.0, 3.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4048, 171003, 124020, 0.165, 26951226.28414627, 11229677.61839428, 0.00326155, 0.00457531, 0.00136125, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24048, 92.2004102, 0.00073185, 112.28178075, 0.03606052, 11.22817808, 0.09535624, -92.2004102, -0.00073185, -112.28178075, -0.03606052, -11.22817808, -0.09535624, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14048, 178.46848355, 0.00062457, 217.33915391, 0.04467328, 21.73391539, 0.14467328, -178.46848355, -0.00062457, -217.33915391, -0.04467328, -21.73391539, -0.14467328, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24048, 4048, 0.0, 281.97019812, 0.01463706, 281.97019812, 0.04391117, 197.37913868, -14290.24115864, 0.05, 2, 0, 71003, 24020, 2, 3)
    ops.uniaxialMaterial('LimitState', 44048, 70.49254953, 5.25e-05, 211.47764859, 0.0001575, 704.9254953, 0.00052501, -70.49254953, -5.25e-05, -211.47764859, -0.0001575, -704.9254953, -0.00052501, 0.4, 0.3, 0.003, 0.0, 0.0, 24048, 2)
    ops.limitCurve('ThreePoint', 14048, 4048, 0.0, 419.53497214, 0.01249146, 419.53497214, 0.03747437, 293.6744805, -38128.42615298, 0.05, 2, 0, 71003, 24020, 1, 3)
    ops.uniaxialMaterial('LimitState', 34048, 104.88374304, 7.812e-05, 314.65122911, 0.00023435, 1048.83743035, 0.00078115, -104.88374304, -7.812e-05, -314.65122911, -0.00023435, -1048.83743035, -0.00078115, 0.4, 0.3, 0.003, 0.0, 0.0, 14048, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4048, 99999, 'P', 44048, 'Vy', 34048, 'Vz', 24048, 'My', 14048, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171003, 71003, 171003, 4048, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124020, 124020, 24020, 4048, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174020, 8.35, 0.0, 3.65)
    ops.node(122003, 8.35, 0.0, 4.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4049, 174020, 122003, 0.165, 27286947.98524707, 11369561.66051961, 0.00326155, 0.00457531, 0.00136125, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24049, 96.39995779, 0.00072693, 117.43734981, 0.03641287, 11.74373498, 0.09774693, -96.39995779, -0.00072693, -117.43734981, -0.03641287, -11.74373498, -0.09774693, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14049, 166.07693413, 0.00062413, 202.31995381, 0.04511829, 20.23199538, 0.14511829, -166.07693413, -0.00062413, -202.31995381, -0.04511829, -20.23199538, -0.14511829, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24049, 4049, 0.0, 280.2519936, 0.0145386, 280.2519936, 0.04361579, 196.17639552, -15063.70420207, 0.05, 2, 0, 74020, 22003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44049, 70.0629984, 5.154e-05, 210.1889952, 0.00015462, 700.62998401, 0.00051539, -70.0629984, -5.154e-05, -210.1889952, -0.00015462, -700.62998401, -0.00051539, 0.4, 0.3, 0.003, 0.0, 0.0, 24049, 2)
    ops.limitCurve('ThreePoint', 14049, 4049, 0.0, 416.78869283, 0.01248257, 416.78869283, 0.0374477, 291.75208498, -41017.40895084, 0.05, 2, 0, 74020, 22003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34049, 104.19717321, 7.665e-05, 312.59151962, 0.00022995, 1041.97173207, 0.00076649, -104.19717321, -7.665e-05, -312.59151962, -0.00022995, -1041.97173207, -0.00076649, 0.4, 0.3, 0.003, 0.0, 0.0, 14049, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4049, 99999, 'P', 44049, 'Vy', 34049, 'Vz', 24049, 'My', 14049, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174020, 74020, 174020, 4049, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122003, 122003, 22003, 4049, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172002, 5.45, 0.0, 4.9)
    ops.node(124021, 5.45, 0.0, 5.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4051, 172002, 124021, 0.125, 27786675.74057118, 11577781.55857133, 0.00178813, 0.00286458, 0.00071615, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24051, 69.17105037, 0.00083542, 84.21882163, 0.03813676, 8.42188216, 0.10579058, -69.17105037, -0.00083542, -84.21882163, -0.03813676, -8.42188216, -0.10579058, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14051, 134.87737722, 0.00063378, 164.21918869, 0.04887844, 16.42191887, 0.14887844, -134.87737722, -0.00063378, -164.21918869, -0.04887844, -16.42191887, -0.14887844, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24051, 4051, 0.0, 202.6677819, 0.01670846, 202.6677819, 0.05012538, 141.86744733, -13260.11434474, 0.05, 2, 0, 72002, 24021, 2, 3)
    ops.uniaxialMaterial('LimitState', 44051, 50.66694548, 4.831e-05, 152.00083643, 0.00014494, 506.66945476, 0.00048313, -50.66694548, -4.831e-05, -152.00083643, -0.00014494, -506.66945476, -0.00048313, 0.4, 0.3, 0.003, 0.0, 0.0, 24051, 2)
    ops.limitCurve('ThreePoint', 14051, 4051, 0.0, 350.13545947, 0.01267556, 350.13545947, 0.03802667, 245.09482163, -42991.54320611, 0.05, 2, 0, 72002, 24021, 1, 3)
    ops.uniaxialMaterial('LimitState', 34051, 87.53386487, 8.347e-05, 262.6015946, 0.0002504, 875.33864866, 0.00083468, -87.53386487, -8.347e-05, -262.6015946, -0.0002504, -875.33864866, -0.00083468, 0.4, 0.3, 0.003, 0.0, 0.0, 14051, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4051, 99999, 'P', 44051, 'Vy', 34051, 'Vz', 24051, 'My', 14051, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172002, 72002, 172002, 4051, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124021, 124021, 24021, 4051, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174021, 5.45, 0.0, 5.95)
    ops.node(123002, 5.45, 0.0, 6.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4052, 174021, 123002, 0.125, 27432290.77154844, 11430121.15481185, 0.00178813, 0.00286458, 0.00071615, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24052, 77.50613052, 0.00081681, 94.5394599, 0.03975972, 9.45394599, 0.10938577, -77.50613052, -0.00081681, -94.5394599, -0.03975972, -9.45394599, -0.10938577, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14052, 142.71680075, 0.0006298, 174.08131679, 0.05099763, 17.40813168, 0.15099763, -142.71680075, -0.0006298, -174.08131679, -0.05099763, -17.40813168, -0.15099763, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24052, 4052, 0.0, 197.23952794, 0.01633618, 197.23952794, 0.04900853, 138.06766956, -15182.32234836, 0.05, 2, 0, 74021, 23002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44052, 49.30988198, 4.763e-05, 147.92964595, 0.00014288, 493.09881984, 0.00047627, -49.30988198, -4.763e-05, -147.92964595, -0.00014288, -493.09881984, -0.00047627, 0.4, 0.3, 0.003, 0.0, 0.0, 24052, 2)
    ops.limitCurve('ThreePoint', 14052, 4052, 0.0, 342.04828891, 0.01259603, 342.04828891, 0.03778809, 239.43380224, -51040.81628552, 0.05, 2, 0, 74021, 23002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34052, 85.51207223, 8.259e-05, 256.53621668, 0.00024778, 855.12072227, 0.00082593, -85.51207223, -8.259e-05, -256.53621668, -0.00024778, -855.12072227, -0.00082593, 0.4, 0.3, 0.003, 0.0, 0.0, 14052, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4052, 99999, 'P', 44052, 'Vy', 34052, 'Vz', 24052, 'My', 14052, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174021, 74021, 174021, 4052, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123002, 123002, 23002, 4052, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172003, 8.35, 0.0, 4.9)
    ops.node(124022, 8.35, 0.0, 5.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4053, 172003, 124022, 0.125, 26366582.23586136, 10986075.9316089, 0.00178813, 0.00286458, 0.00071615, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24053, 70.50202146, 0.000845, 86.02781036, 0.03870958, 8.60278104, 0.10417705, -70.50202146, -0.000845, -86.02781036, -0.03870958, -8.60278104, -0.10417705, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14053, 136.19205898, 0.00064181, 166.18395303, 0.04961496, 16.6183953, 0.14961496, -136.19205898, -0.00064181, -166.18395303, -0.04961496, -16.6183953, -0.14961496, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24053, 4053, 0.0, 198.00506101, 0.01689995, 198.00506101, 0.05069984, 138.60354271, -13723.9881598, 0.05, 2, 0, 72003, 24022, 2, 3)
    ops.uniaxialMaterial('LimitState', 44053, 49.50126525, 4.974e-05, 148.50379576, 0.00014923, 495.01265254, 0.00049744, -49.50126525, -4.974e-05, -148.50379576, -0.00014923, -495.01265254, -0.00049744, 0.4, 0.3, 0.003, 0.0, 0.0, 24053, 2)
    ops.limitCurve('ThreePoint', 14053, 4053, 0.0, 344.70641109, 0.01283629, 344.70641109, 0.03850888, 241.29448776, -44663.6382078, 0.05, 2, 0, 72003, 24022, 1, 3)
    ops.uniaxialMaterial('LimitState', 34053, 86.17660277, 8.66e-05, 258.52980832, 0.0002598, 861.76602773, 0.000866, -86.17660277, -8.66e-05, -258.52980832, -0.0002598, -861.76602773, -0.000866, 0.4, 0.3, 0.003, 0.0, 0.0, 14053, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4053, 99999, 'P', 44053, 'Vy', 34053, 'Vz', 24053, 'My', 14053, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172003, 72003, 172003, 4053, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124022, 124022, 24022, 4053, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174022, 8.35, 0.0, 5.95)
    ops.node(123003, 8.35, 0.0, 6.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4054, 174022, 123003, 0.125, 29561045.92235452, 12317102.46764771, 0.00178813, 0.00286458, 0.00071615, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24054, 74.07296743, 0.00083594, 89.94538625, 0.03877902, 8.99453863, 0.11063849, -74.07296743, -0.00083594, -89.94538625, -0.03877902, -8.99453863, -0.11063849, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14054, 140.61986401, 0.00062822, 170.75200876, 0.04970289, 17.07520088, 0.14970289, -140.61986401, -0.00062822, -170.75200876, -0.04970289, -17.07520088, -0.14970289, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24054, 4054, 0.0, 208.25790676, 0.01671873, 208.25790676, 0.0501562, 145.78053473, -15269.76300646, 0.05, 2, 0, 74022, 23003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44054, 52.06447669, 4.667e-05, 156.19343007, 0.00014, 520.64476689, 0.00046666, -52.06447669, -4.667e-05, -156.19343007, -0.00014, -520.64476689, -0.00046666, 0.4, 0.3, 0.003, 0.0, 0.0, 24054, 2)
    ops.limitCurve('ThreePoint', 14054, 4054, 0.0, 358.08907968, 0.01256437, 358.08907968, 0.03769312, 250.66235578, -51361.50946201, 0.05, 2, 0, 74022, 23003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34054, 89.52226992, 8.024e-05, 268.56680976, 0.00024072, 895.22269921, 0.0008024, -89.52226992, -8.024e-05, -268.56680976, -0.00024072, -895.22269921, -0.0008024, 0.4, 0.3, 0.003, 0.0, 0.0, 14054, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4054, 99999, 'P', 44054, 'Vy', 34054, 'Vz', 24054, 'My', 14054, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174022, 74022, 174022, 4054, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123003, 123003, 23003, 4054, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173002, 5.45, 0.0, 7.2)
    ops.node(124023, 5.45, 0.0, 7.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4056, 173002, 124023, 0.125, 27613911.03063542, 11505796.26276476, 0.00178813, 0.00286458, 0.00071615, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24056, 59.22098816, 0.00082402, 72.39720082, 0.03093844, 7.23972008, 0.0854008, -59.22098816, -0.00082402, -72.39720082, -0.03093844, -7.23972008, -0.0854008, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14056, 116.28878489, 0.00062346, 142.16214174, 0.03894003, 14.21621417, 0.13537758, -116.28878489, -0.00062346, -142.16214174, -0.03894003, -14.21621417, -0.13537758, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24056, 4056, 0.0, 157.25742756, 0.01648034, 157.25742756, 0.04944101, 110.08019929, -13679.81782817, 0.05, 2, 0, 73002, 24023, 2, 3)
    ops.uniaxialMaterial('LimitState', 44056, 39.31435689, 3.772e-05, 117.94307067, 0.00011317, 393.1435689, 0.00037723, -39.31435689, -3.772e-05, -117.94307067, -0.00011317, -393.1435689, -0.00037723, 0.4, 0.3, 0.003, 0.0, 0.0, 24056, 2)
    ops.limitCurve('ThreePoint', 14056, 4056, 0.0, 265.66058979, 0.01246913, 265.66058979, 0.0374074, 185.96241285, -48443.1742927, 0.05, 2, 0, 73002, 24023, 1, 3)
    ops.uniaxialMaterial('LimitState', 34056, 66.41514745, 6.373e-05, 199.24544234, 0.00019118, 664.15147448, 0.00063726, -66.41514745, -6.373e-05, -199.24544234, -0.00019118, -664.15147448, -0.00063726, 0.4, 0.3, 0.003, 0.0, 0.0, 14056, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4056, 99999, 'P', 44056, 'Vy', 34056, 'Vz', 24056, 'My', 14056, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173002, 73002, 173002, 4056, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124023, 124023, 24023, 4056, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174023, 5.45, 0.0, 8.25)
    ops.node(124002, 5.45, 0.0, 8.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4057, 174023, 124002, 0.125, 27744747.66448511, 11560311.5268688, 0.00178813, 0.00286458, 0.00071615, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24057, 57.9079016, 0.00082267, 70.85463422, 0.04141656, 7.08546342, 0.11956438, -57.9079016, -0.00082267, -70.85463422, -0.04141656, -7.08546342, -0.11956438, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14057, 113.26047788, 0.00062437, 138.58263744, 0.05312754, 13.85826374, 0.15312754, -113.26047788, -0.00062437, -138.58263744, -0.05312754, -13.85826374, -0.15312754, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24057, 4057, 0.0, 190.0577865, 0.01645336, 190.0577865, 0.04936008, 133.04045055, -59012.12328245, 0.05, 2, 0, 74023, 24002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44057, 47.51444663, 4.538e-05, 142.54333988, 0.00013613, 475.14446626, 0.00045376, -47.51444663, -4.538e-05, -142.54333988, -0.00013613, -475.14446626, -0.00045376, 0.4, 0.3, 0.003, 0.0, 0.0, 24057, 2)
    ops.limitCurve('ThreePoint', 14057, 4057, 0.0, 332.9152458, 0.01248738, 332.9152458, 0.03746215, 233.04067206, -227196.93702231, 0.05, 2, 0, 74023, 24002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34057, 83.22881145, 7.948e-05, 249.68643435, 0.00023845, 832.28811449, 0.00079483, -83.22881145, -7.948e-05, -249.68643435, -0.00023845, -832.28811449, -0.00079483, 0.4, 0.3, 0.003, 0.0, 0.0, 14057, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4057, 99999, 'P', 44057, 'Vy', 34057, 'Vz', 24057, 'My', 14057, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174023, 74023, 174023, 4057, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124002, 124002, 24002, 4057, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173003, 8.35, 0.0, 7.2)
    ops.node(124024, 8.35, 0.0, 7.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4058, 173003, 124024, 0.125, 27358059.12289379, 11399191.30120574, 0.00178813, 0.00286458, 0.00071615, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24058, 61.03558997, 0.00081279, 74.65639141, 0.03070471, 7.46563914, 0.08505799, -61.03558997, -0.00081279, -74.65639141, -0.03070471, -7.46563914, -0.08505799, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14058, 118.35701292, 0.00062342, 144.76975626, 0.03865689, 14.47697563, 0.13490128, -118.35701292, -0.00062342, -144.76975626, -0.03865689, -14.47697563, -0.13490128, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24058, 4058, 0.0, 155.00052311, 0.01625586, 155.00052311, 0.04876759, 108.50036618, -13333.69455503, 0.05, 2, 0, 73003, 24024, 2, 3)
    ops.uniaxialMaterial('LimitState', 44058, 38.75013078, 3.753e-05, 116.25039233, 0.00011259, 387.50130777, 0.00037529, -38.75013078, -3.753e-05, -116.25039233, -0.00011259, -387.50130777, -0.00037529, 0.4, 0.3, 0.003, 0.0, 0.0, 24058, 2)
    ops.limitCurve('ThreePoint', 14058, 4058, 0.0, 261.84448625, 0.01246837, 261.84448625, 0.03740512, 183.29114038, -47141.02088857, 0.05, 2, 0, 73003, 24024, 1, 3)
    ops.uniaxialMaterial('LimitState', 34058, 65.46112156, 6.34e-05, 196.38336469, 0.0001902, 654.61121563, 0.00063398, -65.46112156, -6.34e-05, -196.38336469, -0.0001902, -654.61121563, -0.00063398, 0.4, 0.3, 0.003, 0.0, 0.0, 14058, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4058, 99999, 'P', 44058, 'Vy', 34058, 'Vz', 24058, 'My', 14058, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173003, 73003, 173003, 4058, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124024, 124024, 24024, 4058, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174024, 8.35, 0.0, 8.25)
    ops.node(124003, 8.35, 0.0, 8.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4059, 174024, 124003, 0.125, 27205570.22213296, 11335654.25922207, 0.00178813, 0.00286458, 0.00071615, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24059, 58.31907382, 0.00080043, 71.44564887, 0.04198306, 7.14456489, 0.11998458, -58.31907382, -0.00080043, -71.44564887, -0.04198306, -7.14456489, -0.11998458, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14059, 112.69644029, 0.000618, 138.06238293, 0.05388263, 13.80623829, 0.15388263, -112.69644029, -0.000618, -138.06238293, -0.05388263, -13.80623829, -0.15388263, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24059, 4059, 0.0, 189.432808, 0.0160085, 189.432808, 0.0480255, 132.6029656, -61151.42660657, 0.05, 2, 0, 74024, 24003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44059, 47.358202, 4.612e-05, 142.074606, 0.00013837, 473.58202001, 0.00046123, -47.358202, -4.612e-05, -142.074606, -0.00013837, -473.58202001, -0.00046123, 0.4, 0.3, 0.003, 0.0, 0.0, 24059, 2)
    ops.limitCurve('ThreePoint', 14059, 4059, 0.0, 333.13165876, 0.01236005, 333.13165876, 0.03708015, 233.19216113, -235593.6163018, 0.05, 2, 0, 74024, 24003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34059, 83.28291469, 8.111e-05, 249.84874407, 0.00024333, 832.82914691, 0.00081111, -83.28291469, -8.111e-05, -249.84874407, -0.00024333, -832.82914691, -0.00081111, 0.4, 0.3, 0.003, 0.0, 0.0, 14059, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4059, 99999, 'P', 44059, 'Vy', 34059, 'Vz', 24059, 'My', 14059, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174024, 74024, 174024, 4059, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124003, 124003, 24003, 4059, '-orient', 0, 0, 1, 0, 1, 0)
