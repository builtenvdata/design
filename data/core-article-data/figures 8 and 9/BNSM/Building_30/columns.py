import openseespy.opensees as ops


def add_columns() -> None:
    """Add components of all columns to ops domain (plastic hinges, column elements and nodes)
    """
    # Create elastic column element nodes
    ops.node(170001, 0.0, 0.0, 0.0)
    ops.node(121001, 0.0, 0.0, 2.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1, 170001, 121001, 0.0875, 26164800.56154356, 10902000.23397648, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20001, 53.49201284, 0.00139266, 64.95874491, 0.01482515, 6.49587449, 0.05085149, -53.49201284, -0.00139266, -64.95874491, -0.01482515, -6.49587449, -0.05085149, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10001, 71.65820974, 0.00103324, 87.01911033, 0.01601222, 8.70191103, 0.06266538, -71.65820974, -0.00103324, -87.01911033, -0.01601222, -8.70191103, -0.06266538, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20001, 1, 0.0, 104.01498498, 0.02785313, 104.01498498, 0.0835594, 72.81048948, -2134.30579339, 0.05, 2, 0, 70001, 21001, 2, 3)
    ops.uniaxialMaterial('LimitState', 40001, 26.00374624, 8.178e-05, 78.01123873, 0.00024534, 260.03746244, 0.00081779, -26.00374624, -8.178e-05, -78.01123873, -0.00024534, -260.03746244, -0.00081779, 0.4, 0.3, 0.003, 0.0, 0.0, 20001, 2)
    ops.limitCurve('ThreePoint', 10001, 1, 0.0, 125.3731327, 0.02066482, 125.3731327, 0.06199445, 87.76119289, -3346.02868056, 0.05, 2, 0, 70001, 21001, 1, 3)
    ops.uniaxialMaterial('LimitState', 30001, 31.34328318, 9.857e-05, 94.02984953, 0.00029571, 313.43283176, 0.00098572, -31.34328318, -9.857e-05, -94.02984953, -0.00029571, -313.43283176, -0.00098572, 0.4, 0.3, 0.003, 0.0, 0.0, 10001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1, 99999, 'P', 40001, 'Vy', 30001, 'Vz', 20001, 'My', 10001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170001, 70001, 170001, 1, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121001, 121001, 21001, 1, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170002, 3.85, 0.0, 0.0)
    ops.node(121002, 3.85, 0.0, 2.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2, 170002, 121002, 0.175, 27840449.32158704, 11600187.21732793, 0.00405757, 0.00401042, 0.0019651, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20002, 189.48675552, 0.00103138, 230.12141034, 0.01331635, 23.01214103, 0.04490598, -189.48675552, -0.00103138, -230.12141034, -0.01331635, -23.01214103, -0.04490598, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10002, 212.47340767, 0.00081266, 258.03745544, 0.01445518, 25.80374554, 0.05496151, -212.47340767, -0.00081266, -258.03745544, -0.01445518, -25.80374554, -0.05496151, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20002, 2, 0.0, 178.08756934, 0.0206276, 178.08756934, 0.06188281, 124.66129854, -2780.83359215, 0.05, 2, 0, 70002, 21002, 2, 3)
    ops.uniaxialMaterial('LimitState', 40002, 44.52189234, 6.579e-05, 133.56567701, 0.00019738, 445.21892336, 0.00065795, -44.52189234, -6.579e-05, -133.56567701, -0.00019738, -445.21892336, -0.00065795, 0.4, 0.3, 0.003, 0.0, 0.0, 20002, 2)
    ops.limitCurve('ThreePoint', 10002, 2, 0.0, 238.73893309, 0.01625321, 238.73893309, 0.04875964, 167.11725316, -4342.42272017, 0.05, 2, 0, 70002, 21002, 1, 3)
    ops.uniaxialMaterial('LimitState', 30002, 59.68473327, 8.82e-05, 179.05419982, 0.00026461, 596.84733272, 0.00088203, -59.68473327, -8.82e-05, -179.05419982, -0.00026461, -596.84733272, -0.00088203, 0.4, 0.3, 0.003, 0.0, 0.0, 10002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2, 99999, 'P', 40002, 'Vy', 30002, 'Vz', 20002, 'My', 10002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170002, 70002, 170002, 2, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121002, 121002, 21002, 2, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170005, 14.5, 0.0, 0.0)
    ops.node(121005, 14.5, 0.0, 2.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 5, 170005, 121005, 0.175, 27601235.31822017, 11500514.71592507, 0.00405757, 0.00401042, 0.0019651, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20005, 186.78741075, 0.00101646, 226.92202141, 0.01346904, 22.69220214, 0.04483462, -186.78741075, -0.00101646, -226.92202141, -0.01346904, -22.69220214, -0.04483462, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10005, 209.35927355, 0.00080235, 254.34385199, 0.014631, 25.4343852, 0.05485003, -209.35927355, -0.00080235, -254.34385199, -0.014631, -25.4343852, -0.05485003, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20005, 5, 0.0, 177.9925195, 0.02032917, 177.9925195, 0.06098751, 124.59476365, -2830.70928683, 0.05, 2, 0, 70005, 21005, 2, 3)
    ops.uniaxialMaterial('LimitState', 40005, 44.49812988, 6.633e-05, 133.49438963, 0.00019899, 444.98129875, 0.0006633, -44.49812988, -6.633e-05, -133.49438963, -0.00019899, -444.98129875, -0.0006633, 0.4, 0.3, 0.003, 0.0, 0.0, 20005, 2)
    ops.limitCurve('ThreePoint', 10005, 5, 0.0, 238.78261196, 0.01604691, 238.78261196, 0.04814072, 167.14782837, -4431.51616845, 0.05, 2, 0, 70005, 21005, 1, 3)
    ops.uniaxialMaterial('LimitState', 30005, 59.69565299, 8.898e-05, 179.08695897, 0.00026695, 596.95652989, 0.00088983, -59.69565299, -8.898e-05, -179.08695897, -0.00026695, -596.95652989, -0.00088983, 0.4, 0.3, 0.003, 0.0, 0.0, 10005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 5, 99999, 'P', 40005, 'Vy', 30005, 'Vz', 20005, 'My', 10005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170005, 70005, 170005, 5, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121005, 121005, 21005, 5, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170006, 18.35, 0.0, 0.0)
    ops.node(121006, 18.35, 0.0, 2.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 6, 170006, 121006, 0.0875, 27569694.28155567, 11487372.61731486, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20006, 54.66115124, 0.00133734, 66.29470199, 0.01490776, 6.6294702, 0.05307685, -54.66115124, -0.00133734, -66.29470199, -0.01490776, -6.6294702, -0.05307685, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10006, 72.7749042, 0.00100365, 88.26361093, 0.01613643, 8.82636109, 0.06556438, -72.7749042, -0.00100365, -88.26361093, -0.01613643, -8.82636109, -0.06556438, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20006, 6, 0.0, 108.27989401, 0.02674689, 108.27989401, 0.08024068, 75.79592581, -2171.88808812, 0.05, 2, 0, 70006, 21006, 2, 3)
    ops.uniaxialMaterial('LimitState', 40006, 27.0699735, 8.079e-05, 81.20992051, 0.00024238, 270.69973502, 0.00080794, -27.0699735, -8.079e-05, -81.20992051, -0.00024238, -270.69973502, -0.00080794, 0.4, 0.3, 0.003, 0.0, 0.0, 20006, 2)
    ops.limitCurve('ThreePoint', 10006, 6, 0.0, 129.9351129, 0.02007297, 129.9351129, 0.06021892, 90.95457903, -3411.941768, 0.05, 2, 0, 70006, 21006, 1, 3)
    ops.uniaxialMaterial('LimitState', 30006, 32.48377823, 9.695e-05, 97.45133468, 0.00029086, 324.83778226, 0.00096953, -32.48377823, -9.695e-05, -97.45133468, -0.00029086, -324.83778226, -0.00096953, 0.4, 0.3, 0.003, 0.0, 0.0, 10006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 6, 99999, 'P', 40006, 'Vy', 30006, 'Vz', 20006, 'My', 10006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170006, 70006, 170006, 6, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121006, 121006, 21006, 6, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170007, 0.0, 5.8, 0.0)
    ops.node(121007, 0.0, 5.8, 2.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 7, 170007, 121007, 0.165, 27373518.03730932, 11405632.51554555, 0.00326155, 0.00136125, 0.00457531, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20007, 253.35357854, 0.00078724, 307.50592889, 0.02003242, 30.75059289, 0.07153623, -253.35357854, -0.00078724, -307.50592889, -0.02003242, -30.75059289, -0.07153623, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10007, 175.83514384, 0.00119803, 213.4185337, 0.01709073, 21.34185337, 0.04979926, -175.83514384, -0.00119803, -213.4185337, -0.01709073, -21.34185337, -0.04979926, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20007, 7, 0.0, 282.81148607, 0.01574475, 282.81148607, 0.04723426, 197.96804025, -6516.73611617, 0.05, 2, 0, 70007, 21007, 2, 3)
    ops.uniaxialMaterial('LimitState', 40007, 70.70287152, 0.00011271, 212.10861455, 0.00033812, 707.02871518, 0.00112708, -70.70287152, -0.00011271, -212.10861455, -0.00033812, -707.02871518, -0.00112708, 0.4, 0.3, 0.003, 0.0, 0.0, 20007, 2)
    ops.limitCurve('ThreePoint', 10007, 7, 0.0, 177.4619282, 0.02396055, 177.4619282, 0.07188166, 124.22334974, -2961.84013669, 0.05, 2, 0, 70007, 21007, 1, 3)
    ops.uniaxialMaterial('LimitState', 30007, 44.36548205, 7.072e-05, 133.09644615, 0.00021217, 443.65482049, 0.00070723, -44.36548205, -7.072e-05, -133.09644615, -0.00021217, -443.65482049, -0.00070723, 0.4, 0.3, 0.003, 0.0, 0.0, 10007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 7, 99999, 'P', 40007, 'Vy', 30007, 'Vz', 20007, 'My', 10007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170007, 70007, 170007, 7, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121007, 121007, 21007, 7, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170008, 3.85, 5.8, 0.0)
    ops.node(121008, 3.85, 5.8, 2.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 8, 170008, 121008, 0.2275, 27058245.626104, 11274269.01087667, 0.00616035, 0.00255464, 0.00881089, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20008, 452.46788894, 0.00076174, 549.38009979, 0.0301705, 54.93800998, 0.08697423, -452.46788894, -0.00076174, -549.38009979, -0.0301705, -54.93800998, -0.08697423, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10008, 312.57068016, 0.0011172, 379.51889108, 0.02515121, 37.95188911, 0.06034465, -312.57068016, -0.0011172, -379.51889108, -0.02515121, -37.95188911, -0.06034465, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20008, 8, 0.0, 454.56685157, 0.01523479, 454.56685157, 0.04570437, 318.1967961, -11283.52669106, 0.05, 2, 0, 70008, 21008, 2, 3)
    ops.uniaxialMaterial('LimitState', 40008, 113.64171289, 0.00013292, 340.92513867, 0.00039876, 1136.41712891, 0.0013292, -113.64171289, -0.00013292, -340.92513867, -0.00039876, -1136.41712891, -0.0013292, 0.4, 0.3, 0.003, 0.0, 0.0, 20008, 2)
    ops.limitCurve('ThreePoint', 10008, 8, 0.0, 258.88778473, 0.02234408, 258.88778473, 0.06703225, 181.22144931, -4840.91318619, 0.05, 2, 0, 70008, 21008, 1, 3)
    ops.uniaxialMaterial('LimitState', 30008, 64.72194618, 7.57e-05, 194.16583855, 0.0002271, 647.21946183, 0.00075701, -64.72194618, -7.57e-05, -194.16583855, -0.0002271, -647.21946183, -0.00075701, 0.4, 0.3, 0.003, 0.0, 0.0, 10008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 8, 99999, 'P', 40008, 'Vy', 30008, 'Vz', 20008, 'My', 10008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170008, 70008, 170008, 8, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121008, 121008, 21008, 8, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170009, 7.7, 5.8, 0.0)
    ops.node(121009, 7.7, 5.8, 2.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 9, 170009, 121009, 0.245, 27990151.46102585, 11662563.10876077, 0.00686927, 0.00275115, 0.01100458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20009, 593.61981395, 0.00076256, 720.18970224, 0.03414541, 72.01897022, 0.09345491, -593.61981395, -0.00076256, -720.18970224, -0.03414541, -72.01897022, -0.09345491, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10009, 366.42395846, 0.00116887, 444.55180797, 0.02785656, 44.4551808, 0.06273262, -366.42395846, -0.00116887, -444.55180797, -0.02785656, -44.4551808, -0.06273262, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20009, 9, 0.0, 519.87413075, 0.01525115, 519.87413075, 0.04575344, 363.91189153, -12547.48902828, 0.05, 2, 0, 70009, 21009, 2, 3)
    ops.uniaxialMaterial('LimitState', 40009, 129.96853269, 0.00013646, 389.90559807, 0.00040937, 1299.68532689, 0.00136458, -129.96853269, -0.00013646, -389.90559807, -0.00040937, -1299.68532689, -0.00136458, 0.4, 0.3, 0.003, 0.0, 0.0, 20009, 2)
    ops.limitCurve('ThreePoint', 10009, 9, 0.0, 275.70102792, 0.02337737, 275.70102792, 0.07013212, 192.99071955, -4851.84777899, 0.05, 2, 0, 70009, 21009, 1, 3)
    ops.uniaxialMaterial('LimitState', 30009, 68.92525698, 7.237e-05, 206.77577094, 0.0002171, 689.25256981, 0.00072367, -68.92525698, -7.237e-05, -206.77577094, -0.0002171, -689.25256981, -0.00072367, 0.4, 0.3, 0.003, 0.0, 0.0, 10009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 9, 99999, 'P', 40009, 'Vy', 30009, 'Vz', 20009, 'My', 10009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170009, 70009, 170009, 9, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121009, 121009, 21009, 9, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170010, 10.65, 5.8, 0.0)
    ops.node(121010, 10.65, 5.8, 2.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 10, 170010, 121010, 0.245, 27302653.53285908, 11376105.63869128, 0.00686927, 0.00275115, 0.01100458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20010, 583.09010194, 0.00076013, 708.06019242, 0.03391435, 70.80601924, 0.09189103, -583.09010194, -0.00076013, -708.06019242, -0.03391435, -70.80601924, -0.09189103, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10010, 358.78626522, 0.0011686, 435.68270349, 0.02767352, 43.56827035, 0.06176584, -358.78626522, -0.0011686, -435.68270349, -0.02767352, -43.56827035, -0.06176584, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20010, 10, 0.0, 506.28353639, 0.01520256, 506.28353639, 0.04560769, 354.39847547, -12179.29289476, 0.05, 2, 0, 70010, 21010, 2, 3)
    ops.uniaxialMaterial('LimitState', 40010, 126.5708841, 0.00013624, 379.71265229, 0.00040871, 1265.70884098, 0.00136237, -126.5708841, -0.00013624, -379.71265229, -0.00040871, -1265.70884098, -0.00136237, 0.4, 0.3, 0.003, 0.0, 0.0, 20010, 2)
    ops.limitCurve('ThreePoint', 10010, 10, 0.0, 268.39856029, 0.02337197, 268.39856029, 0.07011591, 187.87899221, -4737.20215134, 0.05, 2, 0, 70010, 21010, 1, 3)
    ops.uniaxialMaterial('LimitState', 30010, 67.09964007, 7.222e-05, 201.29892022, 0.00021667, 670.99640074, 0.00072224, -67.09964007, -7.222e-05, -201.29892022, -0.00021667, -670.99640074, -0.00072224, 0.4, 0.3, 0.003, 0.0, 0.0, 10010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 10, 99999, 'P', 40010, 'Vy', 30010, 'Vz', 20010, 'My', 10010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170010, 70010, 170010, 10, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121010, 121010, 21010, 10, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170011, 14.5, 5.8, 0.0)
    ops.node(121011, 14.5, 5.8, 2.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 11, 170011, 121011, 0.2275, 27223283.14499593, 11343034.6437483, 0.00616035, 0.00255464, 0.00881089, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20011, 447.55827359, 0.00075491, 543.32172002, 0.0305289, 54.332172, 0.08768265, -447.55827359, -0.00075491, -543.32172002, -0.0305289, -54.332172, -0.08768265, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10011, 307.66106852, 0.00110772, 373.49089671, 0.02544021, 37.34908967, 0.0608505, -307.66106852, -0.00110772, -373.49089671, -0.02544021, -37.34908967, -0.0608505, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20011, 11, 0.0, 453.27991914, 0.01509825, 453.27991914, 0.04529474, 317.2959434, -11057.34526968, 0.05, 2, 0, 70011, 21011, 2, 3)
    ops.uniaxialMaterial('LimitState', 40011, 113.31997978, 0.00013174, 339.95993935, 0.00039522, 1133.19979785, 0.0013174, -113.31997978, -0.00013174, -339.95993935, -0.00039522, -1133.19979785, -0.0013174, 0.4, 0.3, 0.003, 0.0, 0.0, 20011, 2)
    ops.limitCurve('ThreePoint', 10011, 11, 0.0, 258.3069531, 0.02215436, 258.3069531, 0.06646309, 180.81486717, -4761.06890537, 0.05, 2, 0, 70011, 21011, 1, 3)
    ops.uniaxialMaterial('LimitState', 30011, 64.57673828, 7.507e-05, 193.73021483, 0.00022522, 645.76738275, 0.00075074, -64.57673828, -7.507e-05, -193.73021483, -0.00022522, -645.76738275, -0.00075074, 0.4, 0.3, 0.003, 0.0, 0.0, 10011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 11, 99999, 'P', 40011, 'Vy', 30011, 'Vz', 20011, 'My', 10011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170011, 70011, 170011, 11, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121011, 121011, 21011, 11, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170012, 18.35, 5.8, 0.0)
    ops.node(121012, 18.35, 5.8, 2.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 12, 170012, 121012, 0.165, 27994260.73399261, 11664275.30583026, 0.00326155, 0.00136125, 0.00457531, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20012, 250.56577989, 0.00076837, 303.87790349, 0.02072775, 30.38779035, 0.07333741, -250.56577989, -0.00076837, -303.87790349, -0.02072775, -30.38779035, -0.07333741, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10012, 174.60789719, 0.00115763, 211.75869169, 0.01764012, 21.17586917, 0.05105094, -174.60789719, -0.00115763, -211.75869169, -0.01764012, -21.17586917, -0.05105094, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20012, 12, 0.0, 293.76093286, 0.01536745, 293.76093286, 0.04610236, 205.63265301, -6969.16326767, 0.05, 2, 0, 70012, 21012, 2, 3)
    ops.uniaxialMaterial('LimitState', 40012, 73.44023322, 0.00011448, 220.32069965, 0.00034343, 734.40233216, 0.00114476, -73.44023322, -0.00011448, -220.32069965, -0.00034343, -734.40233216, -0.00114476, 0.4, 0.3, 0.003, 0.0, 0.0, 20012, 2)
    ops.limitCurve('ThreePoint', 10012, 12, 0.0, 184.1244694, 0.02315256, 184.1244694, 0.06945769, 128.88712858, -3127.67640912, 0.05, 2, 0, 70012, 21012, 1, 3)
    ops.uniaxialMaterial('LimitState', 30012, 46.03111735, 7.175e-05, 138.09335205, 0.00021525, 460.31117349, 0.00071752, -46.03111735, -7.175e-05, -138.09335205, -0.00021525, -460.31117349, -0.00071752, 0.4, 0.3, 0.003, 0.0, 0.0, 10012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 12, 99999, 'P', 40012, 'Vy', 30012, 'Vz', 20012, 'My', 10012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170012, 70012, 170012, 12, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121012, 121012, 21012, 12, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170013, 0.0, 11.6, 0.0)
    ops.node(121013, 0.0, 11.6, 2.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 13, 170013, 121013, 0.165, 27797306.29059401, 11582210.95441417, 0.00326155, 0.00136125, 0.00457531, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20013, 251.7956695, 0.00078216, 305.50101415, 0.02028865, 30.55010142, 0.0728057, -251.7956695, -0.00078216, -305.50101415, -0.02028865, -30.55010142, -0.0728057, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10013, 174.25554519, 0.00119041, 211.42240405, 0.0172989, 21.14224041, 0.05065091, -174.25554519, -0.00119041, -211.42240405, -0.0172989, -21.14224041, -0.05065091, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20013, 13, 0.0, 290.1809164, 0.01564311, 290.1809164, 0.04692934, 203.12664148, -6905.72578284, 0.05, 2, 0, 70013, 21013, 2, 3)
    ops.uniaxialMaterial('LimitState', 40013, 72.5452291, 0.00011388, 217.6356873, 0.00034165, 725.45229099, 0.00113882, -72.5452291, -0.00011388, -217.6356873, -0.00034165, -725.45229099, -0.00113882, 0.4, 0.3, 0.003, 0.0, 0.0, 20013, 2)
    ops.limitCurve('ThreePoint', 10013, 13, 0.0, 181.86533216, 0.02380811, 181.86533216, 0.07142434, 127.30573251, -3094.6252387, 0.05, 2, 0, 70013, 21013, 1, 3)
    ops.uniaxialMaterial('LimitState', 30013, 45.46633304, 7.137e-05, 136.39899912, 0.00021412, 454.6633304, 0.00071373, -45.46633304, -7.137e-05, -136.39899912, -0.00021412, -454.6633304, -0.00071373, 0.4, 0.3, 0.003, 0.0, 0.0, 10013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 13, 99999, 'P', 40013, 'Vy', 30013, 'Vz', 20013, 'My', 10013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170013, 70013, 170013, 13, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121013, 121013, 21013, 13, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170014, 3.85, 11.6, 0.0)
    ops.node(121014, 3.85, 11.6, 2.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 14, 170014, 121014, 0.2275, 26832014.25445624, 11180005.93935677, 0.00616035, 0.00255464, 0.00881089, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20014, 442.19588261, 0.0007522, 537.1498632, 0.03057385, 53.71498632, 0.08726183, -442.19588261, -0.0007522, -537.1498632, -0.03057385, -53.71498632, -0.08726183, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10014, 304.6940667, 0.00110233, 370.12189096, 0.02547376, 37.0121891, 0.06059549, -304.6940667, -0.00110233, -370.12189096, -0.02547376, -37.0121891, -0.06059549, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20014, 14, 0.0, 455.43391637, 0.01504402, 455.43391637, 0.04513206, 318.80374146, -11734.06280685, 0.05, 2, 0, 70014, 21014, 2, 3)
    ops.uniaxialMaterial('LimitState', 40014, 113.85847909, 0.0001343, 341.57543728, 0.00040289, 1138.58479093, 0.00134296, -113.85847909, -0.0001343, -341.57543728, -0.00040289, -1138.58479093, -0.00134296, 0.4, 0.3, 0.003, 0.0, 0.0, 20014, 2)
    ops.limitCurve('ThreePoint', 10014, 14, 0.0, 259.13596146, 0.02204652, 259.13596146, 0.06613955, 181.39517302, -4980.96970438, 0.05, 2, 0, 70014, 21014, 1, 3)
    ops.uniaxialMaterial('LimitState', 30014, 64.78399036, 7.641e-05, 194.35197109, 0.00022924, 647.83990364, 0.00076413, -64.78399036, -7.641e-05, -194.35197109, -0.00022924, -647.83990364, -0.00076413, 0.4, 0.3, 0.003, 0.0, 0.0, 10014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 14, 99999, 'P', 40014, 'Vy', 30014, 'Vz', 20014, 'My', 10014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170014, 70014, 170014, 14, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121014, 121014, 21014, 14, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170015, 7.7, 11.6, 0.0)
    ops.node(121015, 7.7, 11.6, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 15, 170015, 121015, 0.18, 27764742.8153908, 11568642.83974617, 0.00370786, 0.001485, 0.00594, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20015, 357.84105383, 0.00078516, 433.77048808, 0.02445159, 43.37704881, 0.07544342, -357.84105383, -0.00078516, -433.77048808, -0.02445159, -43.37704881, -0.07544342, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10015, 218.70570371, 0.00126936, 265.11234199, 0.0203342, 26.5112342, 0.05086667, -218.70570371, -0.00126936, -265.11234199, -0.0203342, -26.5112342, -0.05086667, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20015, 15, 0.0, 329.59929256, 0.01570327, 329.59929256, 0.04710982, 230.71950479, -6931.64865461, 0.05, 2, 0, 70015, 21015, 2, 3)
    ops.uniaxialMaterial('LimitState', 40015, 82.39982314, 0.00011871, 247.19946942, 0.00035613, 823.99823139, 0.00118711, -82.39982314, -0.00011871, -247.19946942, -0.00035613, -823.99823139, -0.00118711, 0.4, 0.3, 0.003, 0.0, 0.0, 20015, 2)
    ops.limitCurve('ThreePoint', 10015, 15, 0.0, 191.04476981, 0.02538722, 191.04476981, 0.07616166, 133.73133887, -2922.13096581, 0.05, 2, 0, 70015, 21015, 1, 3)
    ops.uniaxialMaterial('LimitState', 30015, 47.76119245, 6.881e-05, 143.28357736, 0.00020643, 477.61192454, 0.00068808, -47.76119245, -6.881e-05, -143.28357736, -0.00020643, -477.61192454, -0.00068808, 0.4, 0.3, 0.003, 0.0, 0.0, 10015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 15, 99999, 'P', 40015, 'Vy', 30015, 'Vz', 20015, 'My', 10015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170015, 70015, 170015, 15, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121015, 121015, 21015, 15, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170016, 10.65, 11.6, 0.0)
    ops.node(121016, 10.65, 11.6, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 16, 170016, 121016, 0.18, 26998694.20683129, 11249455.91951304, 0.00370786, 0.001485, 0.00594, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20016, 358.2374937, 0.00079145, 434.6090942, 0.02459174, 43.46090942, 0.07408594, -358.2374937, -0.00079145, -434.6090942, -0.02459174, -43.46090942, -0.07408594, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10016, 220.27607376, 0.00127818, 267.23608381, 0.02045085, 26.72360838, 0.05008659, -220.27607376, -0.00127818, -267.23608381, -0.02045085, -26.72360838, -0.05008659, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20016, 16, 0.0, 324.04592542, 0.01582899, 324.04592542, 0.04748696, 226.83214779, -6968.59333843, 0.05, 2, 0, 70016, 21016, 2, 3)
    ops.uniaxialMaterial('LimitState', 40016, 81.01148136, 0.00012002, 243.03444407, 0.00036007, 810.11481355, 0.00120023, -81.01148136, -0.00012002, -243.03444407, -0.00036007, -810.11481355, -0.00120023, 0.4, 0.3, 0.003, 0.0, 0.0, 20016, 2)
    ops.limitCurve('ThreePoint', 10016, 16, 0.0, 187.33998891, 0.02556358, 187.33998891, 0.07669073, 131.13799224, -2934.12101076, 0.05, 2, 0, 70016, 21016, 1, 3)
    ops.uniaxialMaterial('LimitState', 30016, 46.83499723, 6.939e-05, 140.50499168, 0.00020817, 468.34997228, 0.00069389, -46.83499723, -6.939e-05, -140.50499168, -0.00020817, -468.34997228, -0.00069389, 0.4, 0.3, 0.003, 0.0, 0.0, 10016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 16, 99999, 'P', 40016, 'Vy', 30016, 'Vz', 20016, 'My', 10016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170016, 70016, 170016, 16, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121016, 121016, 21016, 16, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170017, 14.5, 11.6, 0.0)
    ops.node(121017, 14.5, 11.6, 2.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 17, 170017, 121017, 0.2275, 28401895.65062046, 11834123.18775853, 0.00616035, 0.00255464, 0.00881089, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20017, 452.44419239, 0.00074708, 548.48429329, 0.03027851, 54.84842933, 0.09006451, -452.44419239, -0.00074708, -548.48429329, -0.03027851, -54.84842933, -0.09006451, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10017, 313.44326596, 0.00108538, 379.97771019, 0.02521964, 37.99777102, 0.06226077, -313.44326596, -0.00108538, -379.97771019, -0.02521964, -37.99777102, -0.06226077, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20017, 17, 0.0, 465.26251857, 0.01494164, 465.26251857, 0.04482492, 325.683763, -11179.20205108, 0.05, 2, 0, 70017, 21017, 2, 3)
    ops.uniaxialMaterial('LimitState', 40017, 116.31562964, 0.00012961, 348.94688893, 0.00038883, 1163.15629643, 0.00129611, -116.31562964, -0.00012961, -348.94688893, -0.00038883, -1163.15629643, -0.00129611, 0.4, 0.3, 0.003, 0.0, 0.0, 20017, 2)
    ops.limitCurve('ThreePoint', 10017, 17, 0.0, 265.50410627, 0.02170759, 265.50410627, 0.06512278, 185.85287439, -4785.90299591, 0.05, 2, 0, 70017, 21017, 1, 3)
    ops.uniaxialMaterial('LimitState', 30017, 66.37602657, 7.396e-05, 199.1280797, 0.00022189, 663.76026567, 0.00073963, -66.37602657, -7.396e-05, -199.1280797, -0.00022189, -663.76026567, -0.00073963, 0.4, 0.3, 0.003, 0.0, 0.0, 10017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 17, 99999, 'P', 40017, 'Vy', 30017, 'Vz', 20017, 'My', 10017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170017, 70017, 170017, 17, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121017, 121017, 21017, 17, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170018, 18.35, 11.6, 0.0)
    ops.node(121018, 18.35, 11.6, 2.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 18, 170018, 121018, 0.165, 28627128.22616072, 11927970.09423363, 0.00326155, 0.00136125, 0.00457531, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20018, 251.31282219, 0.0007727, 304.53256987, 0.02037853, 30.45325699, 0.07426441, -251.31282219, -0.0007727, -304.53256987, -0.02037853, -30.45325699, -0.07426441, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10018, 173.5739564, 0.00117234, 210.33118226, 0.01736287, 21.03311823, 0.05158417, -173.5739564, -0.00117234, -210.33118226, -0.01736287, -21.03311823, -0.05158417, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20018, 18, 0.0, 293.96620817, 0.01545397, 293.96620817, 0.0463619, 205.77634572, -6778.65209477, 0.05, 2, 0, 70018, 21018, 2, 3)
    ops.uniaxialMaterial('LimitState', 40018, 73.49155204, 0.00011202, 220.47465612, 0.00033607, 734.91552041, 0.00112023, -73.49155204, -0.00011202, -220.47465612, -0.00033607, -734.91552041, -0.00112023, 0.4, 0.3, 0.003, 0.0, 0.0, 20018, 2)
    ops.limitCurve('ThreePoint', 10018, 18, 0.0, 184.86169022, 0.02344682, 184.86169022, 0.07034047, 129.40318316, -3048.18581432, 0.05, 2, 0, 70018, 21018, 1, 3)
    ops.uniaxialMaterial('LimitState', 30018, 46.21542256, 7.045e-05, 138.64626767, 0.00021134, 462.15422556, 0.00070446, -46.21542256, -7.045e-05, -138.64626767, -0.00021134, -462.15422556, -0.00070446, 0.4, 0.3, 0.003, 0.0, 0.0, 10018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 18, 99999, 'P', 40018, 'Vy', 30018, 'Vz', 20018, 'My', 10018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170018, 70018, 170018, 18, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121018, 121018, 21018, 18, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170019, 0.0, 17.4, 0.0)
    ops.node(121019, 0.0, 17.4, 2.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 19, 170019, 121019, 0.105, 27724384.06680581, 11551826.69450242, 0.00152551, 0.00117906, 0.00086625, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20019, 85.61283975, 0.00115797, 103.98001288, 0.01451411, 10.39800129, 0.05476722, -85.61283975, -0.00115797, -103.98001288, -0.01451411, -10.39800129, -0.05476722, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10019, 86.98704768, 0.00102356, 105.64904008, 0.01504763, 10.56490401, 0.06024074, -86.98704768, -0.00102356, -105.64904008, -0.01504763, -10.56490401, -0.06024074, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20019, 19, 0.0, 125.66424434, 0.0231594, 125.66424434, 0.0694782, 87.96497104, -2615.04433509, 0.05, 2, 0, 70019, 21019, 2, 3)
    ops.uniaxialMaterial('LimitState', 40019, 31.41606109, 7.77e-05, 94.24818326, 0.00023311, 314.16061085, 0.00077702, -31.41606109, -7.77e-05, -94.24818326, -0.00023311, -314.16061085, -0.00077702, 0.4, 0.3, 0.003, 0.0, 0.0, 20019, 2)
    ops.limitCurve('ThreePoint', 10019, 19, 0.0, 136.09453663, 0.02047117, 136.09453663, 0.0614135, 95.26617564, -3226.40598528, 0.05, 2, 0, 70019, 21019, 1, 3)
    ops.uniaxialMaterial('LimitState', 30019, 34.02363416, 8.415e-05, 102.07090247, 0.00025245, 340.23634158, 0.00084152, -34.02363416, -8.415e-05, -102.07090247, -0.00025245, -340.23634158, -0.00084152, 0.4, 0.3, 0.003, 0.0, 0.0, 10019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 19, 99999, 'P', 40019, 'Vy', 30019, 'Vz', 20019, 'My', 10019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170019, 70019, 170019, 19, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121019, 121019, 21019, 19, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170020, 3.85, 17.4, 0.0)
    ops.node(121020, 3.85, 17.4, 2.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 20, 170020, 121020, 0.175, 28599797.08678026, 11916582.11949178, 0.00405757, 0.00401042, 0.0019651, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20020, 274.36733639, 0.00112481, 332.77868937, 0.02217501, 33.27786894, 0.05969392, -274.36733639, -0.00112481, -332.77868937, -0.02217501, -33.27786894, -0.05969392, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10020, 302.32211246, 0.00087485, 366.68488922, 0.02441707, 36.66848892, 0.07334001, -302.32211246, -0.00087485, -366.68488922, -0.02441707, -36.66848892, -0.07334001, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20020, 20, 0.0, 199.45011159, 0.02249623, 199.45011159, 0.0674887, 139.61507811, -3604.97057011, 0.05, 2, 0, 70020, 21020, 2, 3)
    ops.uniaxialMaterial('LimitState', 40020, 49.8625279, 7.173e-05, 149.58758369, 0.00021519, 498.62527897, 0.00071731, -49.8625279, -7.173e-05, -149.58758369, -0.00021519, -498.62527897, -0.00071731, 0.4, 0.3, 0.003, 0.0, 0.0, 20020, 2)
    ops.limitCurve('ThreePoint', 10020, 20, 0.0, 268.66440976, 0.01749709, 268.66440976, 0.05249128, 188.06508683, -5823.45350698, 0.05, 2, 0, 70020, 21020, 1, 3)
    ops.uniaxialMaterial('LimitState', 30020, 67.16610244, 9.662e-05, 201.49830732, 0.00028987, 671.66102441, 0.00096623, -67.16610244, -9.662e-05, -201.49830732, -0.00028987, -671.66102441, -0.00096623, 0.4, 0.3, 0.003, 0.0, 0.0, 10020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 20, 99999, 'P', 40020, 'Vy', 30020, 'Vz', 20020, 'My', 10020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170020, 70020, 170020, 20, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121020, 121020, 21020, 20, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170021, 7.7, 17.4, 0.0)
    ops.node(121021, 7.7, 17.4, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 21, 170021, 121021, 0.1575, 26589646.42101824, 11079019.34209093, 0.00337604, 0.00292359, 0.00176859, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20021, 185.08384578, 0.00105566, 225.16675933, 0.01862933, 22.51667593, 0.05692258, -185.08384578, -0.00105566, -225.16675933, -0.01862933, -22.51667593, -0.05692258, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10021, 183.40026219, 0.00088364, 223.11856837, 0.01992037, 22.31185684, 0.06621223, -183.40026219, -0.00088364, -223.11856837, -0.01992037, -22.31185684, -0.06621223, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20021, 21, 0.0, 185.50640845, 0.02111328, 185.50640845, 0.06333983, 129.85448591, -4111.20544161, 0.05, 2, 0, 70021, 21021, 2, 3)
    ops.uniaxialMaterial('LimitState', 40021, 46.37660211, 7.973e-05, 139.12980634, 0.0002392, 463.76602112, 0.00079733, -46.37660211, -7.973e-05, -139.12980634, -0.0002392, -463.76602112, -0.00079733, 0.4, 0.3, 0.003, 0.0, 0.0, 20021, 2)
    ops.limitCurve('ThreePoint', 10021, 21, 0.0, 226.60829161, 0.01767283, 226.60829161, 0.05301849, 158.62580412, -5855.47526967, 0.05, 2, 0, 70021, 21021, 1, 3)
    ops.uniaxialMaterial('LimitState', 30021, 56.6520729, 9.74e-05, 169.95621871, 0.0002922, 566.52072902, 0.00097399, -56.6520729, -9.74e-05, -169.95621871, -0.0002922, -566.52072902, -0.00097399, 0.4, 0.3, 0.003, 0.0, 0.0, 10021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 21, 99999, 'P', 40021, 'Vy', 30021, 'Vz', 20021, 'My', 10021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170021, 70021, 170021, 21, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121021, 121021, 21021, 21, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170022, 10.65, 17.4, 0.0)
    ops.node(121022, 10.65, 17.4, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 22, 170022, 121022, 0.1575, 27747346.85397518, 11561394.52248966, 0.00337604, 0.00292359, 0.00176859, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20022, 184.37525871, 0.00103881, 223.97616497, 0.01835748, 22.3976165, 0.05809449, -184.37525871, -0.00103881, -223.97616497, -0.01835748, -22.3976165, -0.05809449, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10022, 183.42192447, 0.00087051, 222.81806953, 0.01963101, 22.28180695, 0.06766821, -183.42192447, -0.00087051, -222.81806953, -0.01963101, -22.28180695, -0.06766821, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20022, 22, 0.0, 186.85480612, 0.02077616, 186.85480612, 0.06232849, 130.79836428, -3892.30934463, 0.05, 2, 0, 70022, 21022, 2, 3)
    ops.uniaxialMaterial('LimitState', 40022, 46.71370153, 7.696e-05, 140.14110459, 0.00023089, 467.1370153, 0.00076962, -46.71370153, -7.696e-05, -140.14110459, -0.00023089, -467.1370153, -0.00076962, 0.4, 0.3, 0.003, 0.0, 0.0, 20022, 2)
    ops.limitCurve('ThreePoint', 10022, 22, 0.0, 227.6472414, 0.01741017, 227.6472414, 0.0522305, 159.35306898, -5519.95451149, 0.05, 2, 0, 70022, 21022, 1, 3)
    ops.uniaxialMaterial('LimitState', 30022, 56.91181035, 9.376e-05, 170.73543105, 0.00028129, 569.11810349, 0.00093763, -56.91181035, -9.376e-05, -170.73543105, -0.00028129, -569.11810349, -0.00093763, 0.4, 0.3, 0.003, 0.0, 0.0, 10022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 22, 99999, 'P', 40022, 'Vy', 30022, 'Vz', 20022, 'My', 10022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170022, 70022, 170022, 22, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121022, 121022, 21022, 22, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170023, 14.5, 17.4, 0.0)
    ops.node(121023, 14.5, 17.4, 2.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 23, 170023, 121023, 0.175, 26506509.15412935, 11044378.81422056, 0.00405757, 0.00401042, 0.0019651, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20023, 269.25804638, 0.00113725, 327.52769663, 0.02267171, 32.75276966, 0.05784201, -269.25804638, -0.00113725, -327.52769663, -0.02267171, -32.75276966, -0.05784201, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10023, 295.34336315, 0.00088275, 359.25808996, 0.02496655, 35.925809, 0.07082702, -295.34336315, -0.00088275, -359.25808996, -0.02496655, -35.925809, -0.07082702, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20023, 23, 0.0, 189.47031957, 0.02274499, 189.47031957, 0.06823496, 132.6292237, -3633.18525645, 0.05, 2, 0, 70023, 21023, 2, 3)
    ops.uniaxialMaterial('LimitState', 40023, 47.36757989, 7.352e-05, 142.10273968, 0.00022057, 473.67579892, 0.00073523, -47.36757989, -7.352e-05, -142.10273968, -0.00022057, -473.67579892, -0.00073523, 0.4, 0.3, 0.003, 0.0, 0.0, 20023, 2)
    ops.limitCurve('ThreePoint', 10023, 23, 0.0, 255.97285199, 0.01765499, 255.97285199, 0.05296497, 179.18099639, -5874.69497582, 0.05, 2, 0, 70023, 21023, 1, 3)
    ops.uniaxialMaterial('LimitState', 30023, 63.993213, 9.933e-05, 191.97963899, 0.00029799, 639.93212998, 0.00099329, -63.993213, -9.933e-05, -191.97963899, -0.00029799, -639.93212998, -0.00099329, 0.4, 0.3, 0.003, 0.0, 0.0, 10023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 23, 99999, 'P', 40023, 'Vy', 30023, 'Vz', 20023, 'My', 10023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170023, 70023, 170023, 23, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121023, 121023, 21023, 23, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170024, 18.35, 17.4, 0.0)
    ops.node(121024, 18.35, 17.4, 2.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 24, 170024, 121024, 0.105, 27586072.2657209, 11494196.77738371, 0.00152551, 0.00117906, 0.00086625, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20024, 84.69879766, 0.0011502, 102.89003553, 0.0145441, 10.28900355, 0.05462827, -84.69879766, -0.0011502, -102.89003553, -0.0145441, -10.28900355, -0.05462827, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10024, 86.14095694, 0.0010166, 104.64193548, 0.01508032, 10.46419355, 0.06008375, -86.14095694, -0.0010166, -104.64193548, -0.01508032, -10.46419355, -0.06008375, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20024, 24, 0.0, 125.35493283, 0.02300405, 125.35493283, 0.06901214, 87.74845298, -2621.12380818, 0.05, 2, 0, 70024, 21024, 2, 3)
    ops.uniaxialMaterial('LimitState', 40024, 31.33873321, 7.79e-05, 94.01619962, 0.0002337, 313.38733207, 0.000779, -31.33873321, -7.79e-05, -94.01619962, -0.0002337, -313.38733207, -0.000779, 0.4, 0.3, 0.003, 0.0, 0.0, 20024, 2)
    ops.limitCurve('ThreePoint', 10024, 24, 0.0, 135.8034586, 0.02033205, 135.8034586, 0.06099615, 95.06242102, -3234.28451901, 0.05, 2, 0, 70024, 21024, 1, 3)
    ops.uniaxialMaterial('LimitState', 30024, 33.95086465, 8.439e-05, 101.85259395, 0.00025318, 339.50864649, 0.00084393, -33.95086465, -8.439e-05, -101.85259395, -0.00025318, -339.50864649, -0.00084393, 0.4, 0.3, 0.003, 0.0, 0.0, 10024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 24, 99999, 'P', 40024, 'Vy', 30024, 'Vz', 20024, 'My', 10024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170024, 70024, 170024, 24, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121024, 121024, 21024, 24, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171001, 0.0, 0.0, 2.8)
    ops.node(122001, 0.0, 0.0, 4.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1001, 171001, 122001, 0.0875, 26674244.54409361, 11114268.560039, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21001, 46.36668718, 0.00140013, 56.46720811, 0.01549354, 5.64672081, 0.05605158, -46.36668718, -0.00140013, -56.46720811, -0.01549354, -5.64672081, -0.05605158, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11001, 74.01981272, 0.00103809, 90.14429158, 0.01675408, 9.01442916, 0.06927566, -74.01981272, -0.00103809, -90.14429158, -0.01675408, -9.01442916, -0.06927566, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21001, 1001, 0.0, 102.91005549, 0.02800253, 102.91005549, 0.0840076, 72.03703884, -2458.42665367, 0.05, 2, 0, 71001, 22001, 2, 3)
    ops.uniaxialMaterial('LimitState', 41001, 25.72751387, 7.937e-05, 77.18254162, 0.0002381, 257.27513872, 0.00079365, -25.72751387, -7.937e-05, -77.18254162, -0.0002381, -257.27513872, -0.00079365, 0.4, 0.3, 0.003, 0.0, 0.0, 21001, 2)
    ops.limitCurve('ThreePoint', 11001, 1001, 0.0, 124.71882402, 0.02076171, 124.71882402, 0.06228514, 87.30317681, -4048.97199782, 0.05, 2, 0, 71001, 22001, 1, 3)
    ops.uniaxialMaterial('LimitState', 31001, 31.179706, 9.618e-05, 93.53911801, 0.00028855, 311.79706005, 0.00096184, -31.179706, -9.618e-05, -93.53911801, -0.00028855, -311.79706005, -0.00096184, 0.4, 0.3, 0.003, 0.0, 0.0, 11001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1001, 99999, 'P', 41001, 'Vy', 31001, 'Vz', 21001, 'My', 11001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171001, 71001, 171001, 1001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122001, 122001, 22001, 1001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171002, 3.85, 0.0, 2.725)
    ops.node(122002, 3.85, 0.0, 4.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1002, 171002, 122002, 0.175, 26803919.79636461, 11168299.91515192, 0.00405757, 0.00401042, 0.0019651, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21002, 115.69625514, 0.00101367, 141.0576819, 0.01362487, 14.10576819, 0.04661645, -115.69625514, -0.00101367, -141.0576819, -0.01362487, -14.10576819, -0.04661645, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11002, 213.51804746, 0.00080087, 260.32269393, 0.01480566, 26.03226939, 0.05710967, -213.51804746, -0.00080087, -260.32269393, -0.01480566, -26.03226939, -0.05710967, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21002, 1002, 0.0, 168.95372758, 0.02027345, 168.95372758, 0.06082034, 118.2676093, -3111.92005596, 0.05, 2, 0, 71002, 22002, 2, 3)
    ops.uniaxialMaterial('LimitState', 41002, 42.23843189, 6.483e-05, 126.71529568, 0.0001945, 422.38431894, 0.00064834, -42.23843189, -6.483e-05, -126.71529568, -0.0001945, -422.38431894, -0.00064834, 0.4, 0.3, 0.003, 0.0, 0.0, 21002, 2)
    ops.limitCurve('ThreePoint', 11002, 1002, 0.0, 227.33318771, 0.01601734, 227.33318771, 0.04805203, 159.1332314, -5135.29902482, 0.05, 2, 0, 71002, 22002, 1, 3)
    ops.uniaxialMaterial('LimitState', 31002, 56.83329693, 8.724e-05, 170.49989079, 0.00026171, 568.33296928, 0.00087237, -56.83329693, -8.724e-05, -170.49989079, -0.00026171, -568.33296928, -0.00087237, 0.4, 0.3, 0.003, 0.0, 0.0, 11002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1002, 99999, 'P', 41002, 'Vy', 31002, 'Vz', 21002, 'My', 11002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171002, 71002, 171002, 1002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122002, 122002, 22002, 1002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171005, 14.5, 0.0, 2.725)
    ops.node(122005, 14.5, 0.0, 4.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1005, 171005, 122005, 0.175, 27940958.63968185, 11642066.09986744, 0.00405757, 0.00401042, 0.0019651, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21005, 115.90893338, 0.000984, 141.05775671, 0.01379523, 14.10577567, 0.0476534, -115.90893338, -0.000984, -141.05775671, -0.01379523, -14.10577567, -0.0476534, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11005, 214.128861, 0.0007828, 260.58851461, 0.01500973, 26.05885146, 0.05842494, -214.128861, -0.0007828, -260.58851461, -0.01500973, -26.05885146, -0.05842494, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21005, 1005, 0.0, 175.52394114, 0.0196799, 175.52394114, 0.05903971, 122.8667588, -3164.59914962, 0.05, 2, 0, 71005, 22005, 2, 3)
    ops.uniaxialMaterial('LimitState', 41005, 43.88098529, 6.461e-05, 131.64295586, 0.00019384, 438.80985286, 0.00064614, -43.88098529, -6.461e-05, -131.64295586, -0.00019384, -438.80985286, -0.00064614, 0.4, 0.3, 0.003, 0.0, 0.0, 21005, 2)
    ops.limitCurve('ThreePoint', 11005, 1005, 0.0, 235.88359491, 0.01565594, 235.88359491, 0.04696783, 165.11851644, -5232.01831906, 0.05, 2, 0, 71005, 22005, 1, 3)
    ops.uniaxialMaterial('LimitState', 31005, 58.97089873, 8.683e-05, 176.91269618, 0.0002605, 589.70898728, 0.00086834, -58.97089873, -8.683e-05, -176.91269618, -0.0002605, -589.70898728, -0.00086834, 0.4, 0.3, 0.003, 0.0, 0.0, 11005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1005, 99999, 'P', 41005, 'Vy', 31005, 'Vz', 21005, 'My', 11005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171005, 71005, 171005, 1005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122005, 122005, 22005, 1005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171006, 18.35, 0.0, 2.8)
    ops.node(122006, 18.35, 0.0, 4.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1006, 171006, 122006, 0.0875, 27117638.0203096, 11299015.84179567, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21006, 45.51601258, 0.00133761, 55.39922768, 0.01532758, 5.53992277, 0.05641524, -45.51601258, -0.00133761, -55.39922768, -0.01532758, -5.53992277, -0.05641524, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11006, 72.65131366, 0.00099838, 88.42660941, 0.01659902, 8.84266094, 0.06980645, -72.65131366, -0.00099838, -88.42660941, -0.01659902, -8.84266094, -0.06980645, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21006, 1006, 0.0, 102.78567758, 0.02675224, 102.78567758, 0.08025672, 71.94997431, -2381.32410386, 0.05, 2, 0, 71006, 22006, 2, 3)
    ops.uniaxialMaterial('LimitState', 41006, 25.6964194, 7.797e-05, 77.08925819, 0.00023392, 256.96419395, 0.00077973, -25.6964194, -7.797e-05, -77.08925819, -0.00023392, -256.96419395, -0.00077973, 0.4, 0.3, 0.003, 0.0, 0.0, 21006, 2)
    ops.limitCurve('ThreePoint', 11006, 1006, 0.0, 124.10781323, 0.01996768, 124.10781323, 0.05990304, 86.87546926, -3910.54335916, 0.05, 2, 0, 71006, 22006, 1, 3)
    ops.uniaxialMaterial('LimitState', 31006, 31.02695331, 9.415e-05, 93.08085992, 0.00028244, 310.26953306, 0.00094148, -31.02695331, -9.415e-05, -93.08085992, -0.00028244, -310.26953306, -0.00094148, 0.4, 0.3, 0.003, 0.0, 0.0, 11006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1006, 99999, 'P', 41006, 'Vy', 31006, 'Vz', 21006, 'My', 11006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171006, 71006, 171006, 1006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122006, 122006, 22006, 1006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171007, 0.0, 5.8, 2.8)
    ops.node(122007, 0.0, 5.8, 4.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1007, 171007, 122007, 0.165, 26721209.98199302, 11133837.49249709, 0.00326155, 0.00136125, 0.00457531, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21007, 169.27371624, 0.00075576, 206.21181263, 0.01999569, 20.62118126, 0.07493971, -169.27371624, -0.00075576, -206.21181263, -0.01999569, -20.62118126, -0.07493971, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11007, 106.09487505, 0.00113487, 129.24638852, 0.01702323, 12.92463885, 0.05191653, -106.09487505, -0.00113487, -129.24638852, -0.01702323, -12.92463885, -0.05191653, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21007, 1007, 0.0, 270.57826779, 0.01511527, 270.57826779, 0.0453458, 189.40478745, -7745.5042207, 0.05, 2, 0, 71007, 22007, 2, 3)
    ops.uniaxialMaterial('LimitState', 41007, 67.64456695, 0.00011047, 202.93370084, 0.0003314, 676.44566947, 0.00110465, -67.64456695, -0.00011047, -202.93370084, -0.0003314, -676.44566947, -0.00110465, 0.4, 0.3, 0.003, 0.0, 0.0, 21007, 2)
    ops.limitCurve('ThreePoint', 11007, 1007, 0.0, 168.62565587, 0.02269736, 168.62565587, 0.06809209, 118.03795911, -3228.97154821, 0.05, 2, 0, 71007, 22007, 1, 3)
    ops.uniaxialMaterial('LimitState', 31007, 42.15641397, 6.884e-05, 126.4692419, 0.00020653, 421.56413967, 0.00068842, -42.15641397, -6.884e-05, -126.4692419, -0.00020653, -421.56413967, -0.00068842, 0.4, 0.3, 0.003, 0.0, 0.0, 11007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1007, 99999, 'P', 41007, 'Vy', 31007, 'Vz', 21007, 'My', 11007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171007, 71007, 171007, 1007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122007, 122007, 22007, 1007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171008, 3.85, 5.8, 2.725)
    ops.node(122008, 3.85, 5.8, 4.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1008, 171008, 122008, 0.2275, 27102092.29440457, 11292538.4560019, 0.00616035, 0.00255464, 0.00881089, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21008, 365.9613028, 0.00072303, 445.53532261, 0.02339663, 44.55353226, 0.07235948, -365.9613028, -0.00072303, -445.53532261, -0.02339663, -44.55353226, -0.07235948, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11008, 157.90491209, 0.0010457, 192.23949476, 0.01985465, 19.22394948, 0.05128555, -157.90491209, -0.0010457, -192.23949476, -0.01985465, -19.22394948, -0.05128555, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21008, 1008, 0.0, 383.12359728, 0.01446053, 383.12359728, 0.04338159, 268.1865181, -8475.5590137, 0.05, 2, 0, 71008, 22008, 2, 3)
    ops.uniaxialMaterial('LimitState', 41008, 95.78089932, 0.00011185, 287.34269796, 0.00033554, 957.80899321, 0.00111848, -95.78089932, -0.00011185, -287.34269796, -0.00033554, -957.80899321, -0.00111848, 0.4, 0.3, 0.003, 0.0, 0.0, 21008, 2)
    ops.limitCurve('ThreePoint', 11008, 1008, 0.0, 219.59332752, 0.0209141, 219.59332752, 0.06274229, 153.71532926, -3621.00602533, 0.05, 2, 0, 71008, 22008, 1, 3)
    ops.uniaxialMaterial('LimitState', 31008, 54.89833188, 6.411e-05, 164.69499564, 0.00019232, 548.9833188, 0.00064107, -54.89833188, -6.411e-05, -164.69499564, -0.00019232, -548.9833188, -0.00064107, 0.4, 0.3, 0.003, 0.0, 0.0, 11008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1008, 99999, 'P', 41008, 'Vy', 31008, 'Vz', 21008, 'My', 11008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171008, 71008, 171008, 1008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122008, 122008, 22008, 1008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171009, 7.7, 5.8, 2.725)
    ops.node(122009, 7.7, 5.8, 4.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1009, 171009, 122009, 0.245, 27417240.48656357, 11423850.20273482, 0.00686927, 0.00275115, 0.01100458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21009, 390.84746839, 0.00071234, 475.71844498, 0.01844353, 47.5718445, 0.05527635, -390.84746839, -0.00071234, -475.71844498, -0.01844353, -47.5718445, -0.05527635, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11009, 171.39715017, 0.00106562, 208.6153611, 0.0158813, 20.86153611, 0.03993453, -171.39715017, -0.00106562, -208.6153611, -0.0158813, -20.86153611, -0.03993453, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21009, 1009, 0.0, 374.26758086, 0.0142467, 374.26758086, 0.0427401, 261.9873066, -5340.28042941, 0.05, 2, 0, 71009, 22009, 2, 3)
    ops.uniaxialMaterial('LimitState', 41009, 93.56689521, 0.00010029, 280.70068564, 0.00030088, 935.66895215, 0.00100292, -93.56689521, -0.00010029, -280.70068564, -0.00030088, -935.66895215, -0.00100292, 0.4, 0.3, 0.003, 0.0, 0.0, 21009, 2)
    ops.limitCurve('ThreePoint', 11009, 1009, 0.0, 201.60012937, 0.02131239, 201.60012937, 0.06393716, 141.12009056, -2330.53889506, 0.05, 2, 0, 71009, 22009, 1, 3)
    ops.uniaxialMaterial('LimitState', 31009, 50.40003234, 5.402e-05, 151.20009703, 0.00016207, 504.00032343, 0.00054022, -50.40003234, -5.402e-05, -151.20009703, -0.00016207, -504.00032343, -0.00054022, 0.4, 0.3, 0.003, 0.0, 0.0, 11009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1009, 99999, 'P', 41009, 'Vy', 31009, 'Vz', 21009, 'My', 11009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171009, 71009, 171009, 1009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122009, 122009, 22009, 1009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171010, 10.65, 5.8, 2.725)
    ops.node(122010, 10.65, 5.8, 4.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1010, 171010, 122010, 0.245, 27669223.57413147, 11528843.15588811, 0.00686927, 0.00275115, 0.01100458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21010, 396.94129702, 0.00072343, 482.94312092, 0.0183189, 48.29431209, 0.05538299, -396.94129702, -0.00072343, -482.94312092, -0.0183189, -48.29431209, -0.05538299, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11010, 173.83787049, 0.00108971, 211.50181233, 0.015792, 21.15018123, 0.03999625, -173.83787049, -0.00108971, -211.50181233, -0.015792, -21.15018123, -0.03999625, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21010, 1010, 0.0, 376.43461208, 0.01446861, 376.43461208, 0.04340582, 263.50422846, -5283.34055937, 0.05, 2, 0, 71010, 22010, 2, 3)
    ops.uniaxialMaterial('LimitState', 41010, 94.10865302, 9.995e-05, 282.32595906, 0.00029986, 941.08653021, 0.00099954, -94.10865302, -9.995e-05, -282.32595906, -0.00029986, -941.08653021, -0.00099954, 0.4, 0.3, 0.003, 0.0, 0.0, 21010, 2)
    ops.limitCurve('ThreePoint', 11010, 1010, 0.0, 202.86654068, 0.02179426, 202.86654068, 0.06538277, 142.00657848, -2311.71907381, 0.05, 2, 0, 71010, 22010, 1, 3)
    ops.uniaxialMaterial('LimitState', 31010, 50.71663517, 5.387e-05, 152.14990551, 0.0001616, 507.1663517, 0.00053867, -50.71663517, -5.387e-05, -152.14990551, -0.0001616, -507.1663517, -0.00053867, 0.4, 0.3, 0.003, 0.0, 0.0, 11010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1010, 99999, 'P', 41010, 'Vy', 31010, 'Vz', 21010, 'My', 11010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171010, 71010, 171010, 1010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122010, 122010, 22010, 1010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171011, 14.5, 5.8, 2.725)
    ops.node(122011, 14.5, 5.8, 4.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1011, 171011, 122011, 0.2275, 27049902.24789109, 11270792.60328796, 0.00616035, 0.00255464, 0.00881089, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21011, 371.62331381, 0.00072762, 452.46138962, 0.02314579, 45.24613896, 0.07203819, -371.62331381, -0.00072762, -452.46138962, -0.02314579, -45.24613896, -0.07203819, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11011, 160.18424587, 0.00104907, 195.02863192, 0.01964612, 19.50286319, 0.0510318, -160.18424587, -0.00104907, -195.02863192, -0.01964612, -19.50286319, -0.0510318, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21011, 1011, 0.0, 381.10272037, 0.01455233, 381.10272037, 0.043657, 266.77190426, -8366.66952322, 0.05, 2, 0, 71011, 22011, 2, 3)
    ops.uniaxialMaterial('LimitState', 41011, 95.27568009, 0.00011147, 285.82704027, 0.00033442, 952.75680092, 0.00111472, -95.27568009, -0.00011147, -285.82704027, -0.00033442, -952.75680092, -0.00111472, 0.4, 0.3, 0.003, 0.0, 0.0, 21011, 2)
    ops.limitCurve('ThreePoint', 11011, 1011, 0.0, 218.47030571, 0.02098133, 218.47030571, 0.06294399, 152.92921399, -3582.66017292, 0.05, 2, 0, 71011, 22011, 1, 3)
    ops.uniaxialMaterial('LimitState', 31011, 54.61757643, 6.39e-05, 163.85272928, 0.00019171, 546.17576426, 0.00063902, -54.61757643, -6.39e-05, -163.85272928, -0.00019171, -546.17576426, -0.00063902, 0.4, 0.3, 0.003, 0.0, 0.0, 11011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1011, 99999, 'P', 41011, 'Vy', 31011, 'Vz', 21011, 'My', 11011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171011, 71011, 171011, 1011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122011, 122011, 22011, 1011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171012, 18.35, 5.8, 2.8)
    ops.node(122012, 18.35, 5.8, 4.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1012, 171012, 122012, 0.165, 28037197.21121729, 11682165.50467387, 0.00326155, 0.00136125, 0.00457531, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21012, 169.3376992, 0.00074677, 205.8797092, 0.02013157, 20.58797092, 0.07698161, -169.3376992, -0.00074677, -205.8797092, -0.02013157, -20.58797092, -0.07698161, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11012, 105.70982912, 0.00111995, 128.5213451, 0.01712795, 12.85213451, 0.05323171, -105.70982912, -0.00111995, -128.5213451, -0.01712795, -12.85213451, -0.05323171, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21012, 1012, 0.0, 280.11031459, 0.01493538, 280.11031459, 0.04480614, 196.07722021, -7817.46561208, 0.05, 2, 0, 71012, 22012, 2, 3)
    ops.uniaxialMaterial('LimitState', 41012, 70.02757865, 0.00010899, 210.08273594, 0.00032697, 700.27578647, 0.00108989, -70.02757865, -0.00010899, -210.08273594, -0.00032697, -700.27578647, -0.00108989, 0.4, 0.3, 0.003, 0.0, 0.0, 21012, 2)
    ops.limitCurve('ThreePoint', 11012, 1012, 0.0, 175.25558367, 0.02239908, 175.25558367, 0.06719725, 122.67890857, -3254.30588351, 0.05, 2, 0, 71012, 22012, 1, 3)
    ops.uniaxialMaterial('LimitState', 31012, 43.81389592, 6.819e-05, 131.44168775, 0.00020457, 438.13895916, 0.00068191, -43.81389592, -6.819e-05, -131.44168775, -0.00020457, -438.13895916, -0.00068191, 0.4, 0.3, 0.003, 0.0, 0.0, 11012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1012, 99999, 'P', 41012, 'Vy', 31012, 'Vz', 21012, 'My', 11012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171012, 71012, 171012, 1012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122012, 122012, 22012, 1012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171013, 0.0, 11.6, 2.8)
    ops.node(122013, 0.0, 11.6, 4.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1013, 171013, 122013, 0.165, 27701102.23286538, 11542125.93036058, 0.00326155, 0.00136125, 0.00457531, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21013, 168.1655687, 0.00074827, 204.59393733, 0.01982015, 20.45939373, 0.07641178, -168.1655687, -0.00074827, -204.59393733, -0.01982015, -20.45939373, -0.07641178, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11013, 104.93730466, 0.00112417, 127.66903772, 0.01687376, 12.76690377, 0.05281341, -104.93730466, -0.00112417, -127.66903772, -0.01687376, -12.76690377, -0.05281341, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21013, 1013, 0.0, 274.11013993, 0.01496549, 274.11013993, 0.04489648, 191.87709795, -7607.96852365, 0.05, 2, 0, 71013, 22013, 2, 3)
    ops.uniaxialMaterial('LimitState', 41013, 68.52753498, 0.00010795, 205.58260495, 0.00032385, 685.27534984, 0.00107949, -68.52753498, -0.00010795, -205.58260495, -0.00032385, -685.27534984, -0.00107949, 0.4, 0.3, 0.003, 0.0, 0.0, 21013, 2)
    ops.limitCurve('ThreePoint', 11013, 1013, 0.0, 171.54663262, 0.02248342, 171.54663262, 0.06745027, 120.08264283, -3171.96556453, 0.05, 2, 0, 71013, 22013, 1, 3)
    ops.uniaxialMaterial('LimitState', 31013, 42.88665815, 6.756e-05, 128.65997446, 0.00020267, 428.86658154, 0.00067558, -42.88665815, -6.756e-05, -128.65997446, -0.00020267, -428.86658154, -0.00067558, 0.4, 0.3, 0.003, 0.0, 0.0, 11013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1013, 99999, 'P', 41013, 'Vy', 31013, 'Vz', 21013, 'My', 11013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171013, 71013, 171013, 1013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122013, 122013, 22013, 1013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171014, 3.85, 11.6, 2.725)
    ops.node(122014, 3.85, 11.6, 4.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1014, 171014, 122014, 0.2275, 27747327.30093216, 11561386.3753884, 0.00616035, 0.00255464, 0.00881089, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21014, 365.61319469, 0.00071976, 444.7415882, 0.02336808, 44.47415882, 0.07337921, -365.61319469, -0.00071976, -444.7415882, -0.02336808, -44.47415882, -0.07337921, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11014, 157.76785129, 0.00103922, 191.91299923, 0.01982719, 19.19129992, 0.05193102, -157.76785129, -0.00103922, -191.91299923, -0.01982719, -19.19129992, -0.05193102, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21014, 1014, 0.0, 391.30758119, 0.01439521, 391.30758119, 0.04318563, 273.91530683, -8723.72774215, 0.05, 2, 0, 71014, 22014, 2, 3)
    ops.uniaxialMaterial('LimitState', 41014, 97.8268953, 0.00011158, 293.48068589, 0.00033474, 978.26895298, 0.0011158, -97.8268953, -0.00011158, -293.48068589, -0.00033474, -978.26895298, -0.0011158, 0.4, 0.3, 0.003, 0.0, 0.0, 21014, 2)
    ops.limitCurve('ThreePoint', 11014, 1014, 0.0, 224.38291019, 0.0207844, 224.38291019, 0.06235321, 157.06803714, -3694.62727087, 0.05, 2, 0, 71014, 22014, 1, 3)
    ops.uniaxialMaterial('LimitState', 31014, 56.09572755, 6.398e-05, 168.28718265, 0.00019195, 560.95727548, 0.00063982, -56.09572755, -6.398e-05, -168.28718265, -0.00019195, -560.95727548, -0.00063982, 0.4, 0.3, 0.003, 0.0, 0.0, 11014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1014, 99999, 'P', 41014, 'Vy', 31014, 'Vz', 21014, 'My', 11014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171014, 71014, 171014, 1014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122014, 122014, 22014, 1014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171015, 7.7, 11.6, 2.7)
    ops.node(122015, 7.7, 11.6, 4.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1015, 171015, 122015, 0.18, 27498264.73159692, 11457610.30483205, 0.00370786, 0.001485, 0.00594, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21015, 257.44963719, 0.00073909, 313.05630446, 0.01954747, 31.30563045, 0.06561998, -257.44963719, -0.00073909, -313.05630446, -0.01954747, -31.30563045, -0.06561998, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11015, 109.03979066, 0.00115811, 132.59134593, 0.01651954, 13.25913459, 0.04502237, -109.03979066, -0.00115811, -132.59134593, -0.01651954, -13.25913459, -0.04502237, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21015, 1015, 0.0, 288.48977434, 0.01478181, 288.48977434, 0.04434544, 201.94284204, -5949.01712347, 0.05, 2, 0, 71015, 22015, 2, 3)
    ops.uniaxialMaterial('LimitState', 41015, 72.12244358, 0.00010491, 216.36733075, 0.00031474, 721.22443585, 0.00104912, -72.12244358, -0.00010491, -216.36733075, -0.00031474, -721.22443585, -0.00104912, 0.4, 0.3, 0.003, 0.0, 0.0, 21015, 2)
    ops.limitCurve('ThreePoint', 11015, 1015, 0.0, 168.54509312, 0.02316222, 168.54509312, 0.06948666, 117.98156518, -2421.35545078, 0.05, 2, 0, 71015, 22015, 1, 3)
    ops.uniaxialMaterial('LimitState', 31015, 42.13627328, 6.129e-05, 126.40881984, 0.00018388, 421.36273279, 0.00061293, -42.13627328, -6.129e-05, -126.40881984, -0.00018388, -421.36273279, -0.00061293, 0.4, 0.3, 0.003, 0.0, 0.0, 11015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1015, 99999, 'P', 41015, 'Vy', 31015, 'Vz', 21015, 'My', 11015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171015, 71015, 171015, 1015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122015, 122015, 22015, 1015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171016, 10.65, 11.6, 2.7)
    ops.node(122016, 10.65, 11.6, 4.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1016, 171016, 122016, 0.18, 28426418.45423739, 11844341.02259891, 0.00370786, 0.001485, 0.00594, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21016, 257.75806155, 0.00073621, 312.95848858, 0.01951166, 31.29584886, 0.06671218, -257.75806155, -0.00073621, -312.95848858, -0.01951166, -31.29584886, -0.06671218, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11016, 109.20436801, 0.00115547, 132.59113509, 0.01649, 13.25911351, 0.04569067, -109.20436801, -0.00115547, -132.59113509, -0.01649, -13.25911351, -0.04569067, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21016, 1016, 0.0, 297.40011736, 0.01472429, 297.40011736, 0.04417286, 208.18008215, -6050.75087321, 0.05, 2, 0, 71016, 22016, 2, 3)
    ops.uniaxialMaterial('LimitState', 41016, 74.35002934, 0.00010462, 223.05008802, 0.00031386, 743.50029339, 0.00104621, -74.35002934, -0.00010462, -223.05008802, -0.00031386, -743.50029339, -0.00104621, 0.4, 0.3, 0.003, 0.0, 0.0, 21016, 2)
    ops.limitCurve('ThreePoint', 11016, 1016, 0.0, 174.11945154, 0.02310933, 174.11945154, 0.069328, 121.88361608, -2453.77771751, 0.05, 2, 0, 71016, 22016, 1, 3)
    ops.uniaxialMaterial('LimitState', 31016, 43.52986288, 6.125e-05, 130.58958865, 0.00018376, 435.29862885, 0.00061253, -43.52986288, -6.125e-05, -130.58958865, -0.00018376, -435.29862885, -0.00061253, 0.4, 0.3, 0.003, 0.0, 0.0, 11016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1016, 99999, 'P', 41016, 'Vy', 31016, 'Vz', 21016, 'My', 11016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171016, 71016, 171016, 1016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122016, 122016, 22016, 1016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171017, 14.5, 11.6, 2.725)
    ops.node(122017, 14.5, 11.6, 4.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1017, 171017, 122017, 0.2275, 27904915.06573193, 11627047.94405497, 0.00616035, 0.00255464, 0.00881089, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21017, 361.80759353, 0.0007235, 439.99672745, 0.02361469, 43.99967275, 0.07381527, -361.80759353, -0.0007235, -439.99672745, -0.02361469, -43.99967275, -0.07381527, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11017, 156.38631075, 0.00105593, 190.1824787, 0.02004537, 19.01824787, 0.05227081, -156.38631075, -0.00105593, -190.1824787, -0.02004537, -19.01824787, -0.05227081, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21017, 1017, 0.0, 394.74243311, 0.01447002, 394.74243311, 0.04341005, 276.31970318, -8856.23182963, 0.05, 2, 0, 71017, 22017, 2, 3)
    ops.uniaxialMaterial('LimitState', 41017, 98.68560828, 0.00011192, 296.05682483, 0.00033577, 986.85608277, 0.00111924, -98.68560828, -0.00011192, -296.05682483, -0.00033577, -986.85608277, -0.00111924, 0.4, 0.3, 0.003, 0.0, 0.0, 21017, 2)
    ops.limitCurve('ThreePoint', 11017, 1017, 0.0, 226.33935349, 0.0211185, 226.33935349, 0.06335551, 158.43754745, -3741.0291592, 0.05, 2, 0, 71017, 22017, 1, 3)
    ops.uniaxialMaterial('LimitState', 31017, 56.58483837, 6.418e-05, 169.75451512, 0.00019253, 565.84838373, 0.00064176, -56.58483837, -6.418e-05, -169.75451512, -0.00019253, -565.84838373, -0.00064176, 0.4, 0.3, 0.003, 0.0, 0.0, 11017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1017, 99999, 'P', 41017, 'Vy', 31017, 'Vz', 21017, 'My', 11017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171017, 71017, 171017, 1017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122017, 122017, 22017, 1017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171018, 18.35, 11.6, 2.8)
    ops.node(122018, 18.35, 11.6, 4.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1018, 171018, 122018, 0.165, 26928738.82379294, 11220307.84324706, 0.00326155, 0.00136125, 0.00457531, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21018, 164.94909833, 0.00074435, 200.91424613, 0.02019611, 20.09142461, 0.07567574, -164.94909833, -0.00074435, -200.91424613, -0.02019611, -20.09142461, -0.07567574, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11018, 102.52396669, 0.00112216, 124.87807262, 0.01718545, 12.48780726, 0.0524189, -102.52396669, -0.00112216, -124.87807262, -0.01718545, -12.48780726, -0.0524189, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21018, 1018, 0.0, 274.66460479, 0.01488709, 274.66460479, 0.04466127, 192.26522335, -8091.84331402, 0.05, 2, 0, 71018, 22018, 2, 3)
    ops.uniaxialMaterial('LimitState', 41018, 68.6661512, 0.00011127, 205.99845359, 0.00033381, 686.66151198, 0.00111269, -68.6661512, -0.00011127, -205.99845359, -0.00033381, -686.66151198, -0.00111269, 0.4, 0.3, 0.003, 0.0, 0.0, 21018, 2)
    ops.limitCurve('ThreePoint', 11018, 1018, 0.0, 171.01116127, 0.02244319, 171.01116127, 0.06732958, 119.70781289, -3341.97809539, 0.05, 2, 0, 71018, 22018, 1, 3)
    ops.uniaxialMaterial('LimitState', 31018, 42.75279032, 6.928e-05, 128.25837095, 0.00020783, 427.52790318, 0.00069278, -42.75279032, -6.928e-05, -128.25837095, -0.00020783, -427.52790318, -0.00069278, 0.4, 0.3, 0.003, 0.0, 0.0, 11018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1018, 99999, 'P', 41018, 'Vy', 31018, 'Vz', 21018, 'My', 11018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171018, 71018, 171018, 1018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122018, 122018, 22018, 1018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171019, 0.0, 17.4, 2.8)
    ops.node(122019, 0.0, 17.4, 4.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1019, 171019, 122019, 0.105, 28178032.43047657, 11740846.84603191, 0.00152551, 0.00117906, 0.00086625, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21019, 67.81167274, 0.00113116, 82.49052327, 0.01523894, 8.24905233, 0.05889047, -67.81167274, -0.00113116, -82.49052327, -0.01523894, -8.24905233, -0.05889047, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11019, 94.31723732, 0.00099994, 114.73361362, 0.01581325, 11.47336136, 0.06482184, -94.31723732, -0.00099994, -114.73361362, -0.01581325, -11.47336136, -0.06482184, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21019, 1019, 0.0, 124.06966345, 0.02262311, 124.06966345, 0.06786934, 86.84876441, -3049.03876921, 0.05, 2, 0, 71019, 22019, 2, 3)
    ops.uniaxialMaterial('LimitState', 41019, 31.01741586, 7.548e-05, 93.05224758, 0.00022644, 310.17415862, 0.00075481, -31.01741586, -7.548e-05, -93.05224758, -0.00022644, -310.17415862, -0.00075481, 0.4, 0.3, 0.003, 0.0, 0.0, 21019, 2)
    ops.limitCurve('ThreePoint', 11019, 1019, 0.0, 134.62917078, 0.01999883, 134.62917078, 0.05999649, 94.24041955, -3844.74248557, 0.05, 2, 0, 71019, 22019, 1, 3)
    ops.uniaxialMaterial('LimitState', 31019, 33.6572927, 8.191e-05, 100.97187809, 0.00024572, 336.57292695, 0.00081905, -33.6572927, -8.191e-05, -100.97187809, -0.00024572, -336.57292695, -0.00081905, 0.4, 0.3, 0.003, 0.0, 0.0, 11019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1019, 99999, 'P', 41019, 'Vy', 31019, 'Vz', 21019, 'My', 11019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171019, 71019, 171019, 1019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122019, 122019, 22019, 1019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171020, 3.85, 17.4, 2.725)
    ops.node(122020, 3.85, 17.4, 4.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1020, 171020, 122020, 0.175, 29280730.9550745, 12200304.56461438, 0.00405757, 0.00401042, 0.0019651, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21020, 117.51614843, 0.00098349, 142.62834727, 0.01743185, 14.26283473, 0.05214562, -117.51614843, -0.00098349, -142.62834727, -0.01743185, -14.26283473, -0.05214562, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11020, 191.99056468, 0.00078106, 233.01731122, 0.01904704, 23.30173112, 0.06355936, -191.99056468, -0.00078106, -233.01731122, -0.01904704, -23.30173112, -0.06355936, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21020, 1020, 0.0, 180.12487911, 0.01966974, 180.12487911, 0.05900923, 126.08741538, -3038.81375483, 0.05, 2, 0, 71020, 22020, 2, 3)
    ops.uniaxialMaterial('LimitState', 41020, 45.03121978, 6.327e-05, 135.09365933, 0.00018982, 450.31219777, 0.00063274, -45.03121978, -6.327e-05, -135.09365933, -0.00018982, -450.31219777, -0.00063274, 0.4, 0.3, 0.003, 0.0, 0.0, 21020, 2)
    ops.limitCurve('ThreePoint', 11020, 1020, 0.0, 241.44011164, 0.01562116, 241.44011164, 0.04686349, 169.00807815, -5000.17910662, 0.05, 2, 0, 71020, 22020, 1, 3)
    ops.uniaxialMaterial('LimitState', 31020, 60.36002791, 8.481e-05, 181.08008373, 0.00025444, 603.6002791, 0.00084813, -60.36002791, -8.481e-05, -181.08008373, -0.00025444, -603.6002791, -0.00084813, 0.4, 0.3, 0.003, 0.0, 0.0, 11020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1020, 99999, 'P', 41020, 'Vy', 31020, 'Vz', 21020, 'My', 11020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171020, 71020, 171020, 1020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122020, 122020, 22020, 1020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171021, 7.7, 17.4, 2.7)
    ops.node(122021, 7.7, 17.4, 4.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1021, 171021, 122021, 0.1575, 27736419.81023252, 11556841.58759688, 0.00337604, 0.00292359, 0.00176859, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21021, 106.87462994, 0.00097965, 130.12732009, 0.01398501, 13.01273201, 0.05030132, -106.87462994, -0.00097965, -130.12732009, -0.01398501, -13.01273201, -0.05030132, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11021, 149.79844175, 0.00082678, 182.39005635, 0.01484635, 18.23900564, 0.05824357, -149.79844175, -0.00082678, -182.39005635, -0.01484635, -18.23900564, -0.05824357, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21021, 1021, 0.0, 163.47090425, 0.01959303, 163.47090425, 0.05877908, 114.42963297, -3264.61053529, 0.05, 2, 0, 71021, 22021, 2, 3)
    ops.uniaxialMaterial('LimitState', 41021, 40.86772606, 6.736e-05, 122.60317819, 0.00020207, 408.67726062, 0.00067357, -40.86772606, -6.736e-05, -122.60317819, -0.00020207, -408.67726062, -0.00067357, 0.4, 0.3, 0.003, 0.0, 0.0, 21021, 2)
    ops.limitCurve('ThreePoint', 11021, 1021, 0.0, 198.30164367, 0.0165356, 198.30164367, 0.0496068, 138.81115057, -4683.76093456, 0.05, 2, 0, 71021, 22021, 1, 3)
    ops.uniaxialMaterial('LimitState', 31021, 49.57541092, 8.171e-05, 148.72623276, 0.00024513, 495.75410919, 0.00081709, -49.57541092, -8.171e-05, -148.72623276, -0.00024513, -495.75410919, -0.00081709, 0.4, 0.3, 0.003, 0.0, 0.0, 11021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1021, 99999, 'P', 41021, 'Vy', 31021, 'Vz', 21021, 'My', 11021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171021, 71021, 171021, 1021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122021, 122021, 22021, 1021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171022, 10.65, 17.4, 2.7)
    ops.node(122022, 10.65, 17.4, 4.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1022, 171022, 122022, 0.1575, 28773795.87523847, 11989081.6146827, 0.00337604, 0.00292359, 0.00176859, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21022, 106.32615558, 0.00096024, 129.20317124, 0.01423833, 12.92031712, 0.05129412, -106.32615558, -0.00096024, -129.20317124, -0.01423833, -12.92031712, -0.05129412, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11022, 148.91809789, 0.00081199, 180.95914779, 0.01512557, 18.09591478, 0.05940644, -148.91809789, -0.00081199, -180.95914779, -0.01512557, -18.09591478, -0.05940644, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21022, 1022, 0.0, 168.47408262, 0.01920489, 168.47408262, 0.05761468, 117.93185784, -3282.61812967, 0.05, 2, 0, 71022, 22022, 2, 3)
    ops.uniaxialMaterial('LimitState', 41022, 42.11852066, 6.692e-05, 126.35556197, 0.00020075, 421.18520656, 0.00066916, -42.11852066, -6.692e-05, -126.35556197, -0.00020075, -421.18520656, -0.00066916, 0.4, 0.3, 0.003, 0.0, 0.0, 21022, 2)
    ops.limitCurve('ThreePoint', 11022, 1022, 0.0, 204.10502308, 0.01623988, 204.10502308, 0.04871965, 142.87351616, -4711.49577538, 0.05, 2, 0, 71022, 22022, 1, 3)
    ops.uniaxialMaterial('LimitState', 31022, 51.02625577, 8.107e-05, 153.07876731, 0.0002432, 510.2625577, 0.00081068, -51.02625577, -8.107e-05, -153.07876731, -0.0002432, -510.2625577, -0.00081068, 0.4, 0.3, 0.003, 0.0, 0.0, 11022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1022, 99999, 'P', 41022, 'Vy', 31022, 'Vz', 21022, 'My', 11022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171022, 71022, 171022, 1022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122022, 122022, 22022, 1022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171023, 14.5, 17.4, 2.725)
    ops.node(122023, 14.5, 17.4, 4.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1023, 171023, 122023, 0.175, 27398926.139446, 11416219.22476917, 0.00405757, 0.00401042, 0.0019651, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21023, 118.63123364, 0.00100844, 144.50300618, 0.0177363, 14.45030062, 0.05118647, -118.63123364, -0.00100844, -144.50300618, -0.0177363, -14.45030062, -0.05118647, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11023, 194.18682539, 0.00079975, 236.53619008, 0.01937611, 23.65361901, 0.06226816, -194.18682539, -0.00079975, -236.53619008, -0.01937611, -23.65361901, -0.06226816, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21023, 1023, 0.0, 171.66261434, 0.02016885, 171.66261434, 0.06050655, 120.16383004, -3096.42981899, 0.05, 2, 0, 71023, 22023, 2, 3)
    ops.uniaxialMaterial('LimitState', 41023, 42.91565359, 6.444e-05, 128.74696076, 0.00019333, 429.15653586, 0.00064443, -42.91565359, -6.444e-05, -128.74696076, -0.00019333, -429.15653586, -0.00064443, 0.4, 0.3, 0.003, 0.0, 0.0, 21023, 2)
    ops.limitCurve('ThreePoint', 11023, 1023, 0.0, 230.76402055, 0.01599501, 230.76402055, 0.04798504, 161.53481439, -5105.81659173, 0.05, 2, 0, 71023, 22023, 1, 3)
    ops.uniaxialMaterial('LimitState', 31023, 57.69100514, 8.663e-05, 173.07301541, 0.00025989, 576.91005138, 0.0008663, -57.69100514, -8.663e-05, -173.07301541, -0.00025989, -576.91005138, -0.0008663, 0.4, 0.3, 0.003, 0.0, 0.0, 11023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1023, 99999, 'P', 41023, 'Vy', 31023, 'Vz', 21023, 'My', 11023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171023, 71023, 171023, 1023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122023, 122023, 22023, 1023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171024, 18.35, 17.4, 2.8)
    ops.node(122024, 18.35, 17.4, 4.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1024, 171024, 122024, 0.105, 27877473.28220074, 11615613.86758364, 0.00152551, 0.00117906, 0.00086625, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21024, 67.60965819, 0.00115103, 82.28996065, 0.01538246, 8.22899607, 0.05876613, -67.60965819, -0.00115103, -82.28996065, -0.01538246, -8.22899607, -0.05876613, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11024, 93.77562132, 0.00101501, 114.13742348, 0.01595815, 11.41374235, 0.064666, -93.77562132, -0.00101501, -114.13742348, -0.01595815, -11.41374235, -0.064666, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21024, 1024, 0.0, 123.34476191, 0.02302059, 123.34476191, 0.06906176, 86.34133333, -3061.83696631, 0.05, 2, 0, 71024, 22024, 2, 3)
    ops.uniaxialMaterial('LimitState', 41024, 30.83619048, 7.585e-05, 92.50857143, 0.00022755, 308.36190477, 0.00075849, -30.83619048, -7.585e-05, -92.50857143, -0.00022755, -308.36190477, -0.00075849, 0.4, 0.3, 0.003, 0.0, 0.0, 21024, 2)
    ops.limitCurve('ThreePoint', 11024, 1024, 0.0, 133.93428437, 0.02030018, 133.93428437, 0.06090053, 93.75399906, -3861.50987505, 0.05, 2, 0, 71024, 22024, 1, 3)
    ops.uniaxialMaterial('LimitState', 31024, 33.48357109, 8.236e-05, 100.45071328, 0.00024708, 334.83571092, 0.00082361, -33.48357109, -8.236e-05, -100.45071328, -0.00024708, -334.83571092, -0.00082361, 0.4, 0.3, 0.003, 0.0, 0.0, 11024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1024, 99999, 'P', 41024, 'Vy', 31024, 'Vz', 21024, 'My', 11024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171024, 71024, 171024, 1024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122024, 122024, 22024, 1024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172001, 0.0, 0.0, 5.3)
    ops.node(123001, 0.0, 0.0, 7.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2001, 172001, 123001, 0.0625, 27584856.71586768, 11493690.2982782, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22001, 32.81294028, 0.00131948, 39.95530595, 0.01664863, 3.9955306, 0.07236664, -32.81294028, -0.00131948, -39.95530595, -0.01664863, -3.9955306, -0.07236664, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12001, 32.81294028, 0.00131948, 39.95530595, 0.01664863, 3.9955306, 0.07236664, -32.81294028, -0.00131948, -39.95530595, -0.01664863, -3.9955306, -0.07236664, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22001, 2001, 0.0, 86.92825828, 0.02638952, 86.92825828, 0.07916855, 60.84978079, -2932.71284791, 0.05, 2, 0, 72001, 23001, 2, 3)
    ops.uniaxialMaterial('LimitState', 42001, 21.73206457, 9.076e-05, 65.19619371, 0.00027227, 217.32064569, 0.00090758, -21.73206457, -9.076e-05, -65.19619371, -0.00027227, -217.32064569, -0.00090758, 0.4, 0.3, 0.003, 0.0, 0.0, 22001, 2)
    ops.limitCurve('ThreePoint', 12001, 2001, 0.0, 86.92825828, 0.02638952, 86.92825828, 0.07916855, 60.84978079, -2932.71284791, 0.05, 2, 0, 72001, 23001, 1, 3)
    ops.uniaxialMaterial('LimitState', 32001, 21.73206457, 9.076e-05, 65.19619371, 0.00027227, 217.32064569, 0.00090758, -21.73206457, -9.076e-05, -65.19619371, -0.00027227, -217.32064569, -0.00090758, 0.4, 0.3, 0.003, 0.0, 0.0, 12001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2001, 99999, 'P', 42001, 'Vy', 32001, 'Vz', 22001, 'My', 12001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172001, 72001, 172001, 2001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123001, 123001, 23001, 2001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172002, 3.85, 0.0, 5.225)
    ops.node(123002, 3.85, 0.0, 7.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2002, 172002, 123002, 0.1, 27604231.51047998, 11501763.12936666, 0.00127345, 0.00146667, 0.00057292, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22002, 47.38141695, 0.001325, 57.6661356, 0.01496796, 5.76661356, 0.05351991, -47.38141695, -0.001325, -57.6661356, -0.01496796, -5.76661356, -0.05351991, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12002, 87.44903794, 0.00090265, 106.43092597, 0.01674698, 10.6430926, 0.07172004, -87.44903794, -0.00090265, -106.43092597, -0.01674698, -10.6430926, -0.07172004, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22002, 2002, 0.0, 110.84499935, 0.02649993, 110.84499935, 0.07949979, 77.59149954, -2378.70519917, 0.05, 2, 0, 72002, 23002, 2, 3)
    ops.uniaxialMaterial('LimitState', 42002, 27.71124984, 7.228e-05, 83.13374951, 0.00021684, 277.11249837, 0.00072279, -27.71124984, -7.228e-05, -83.13374951, -0.00021684, -277.11249837, -0.00072279, 0.4, 0.3, 0.003, 0.0, 0.0, 22002, 2)
    ops.limitCurve('ThreePoint', 12002, 2002, 0.0, 144.53403495, 0.01805305, 144.53403495, 0.05415914, 101.17382447, -4786.71877618, 0.05, 2, 0, 72002, 23002, 1, 3)
    ops.uniaxialMaterial('LimitState', 32002, 36.13350874, 9.425e-05, 108.40052621, 0.00028274, 361.33508738, 0.00094247, -36.13350874, -9.425e-05, -108.40052621, -0.00028274, -361.33508738, -0.00094247, 0.4, 0.3, 0.003, 0.0, 0.0, 12002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2002, 99999, 'P', 42002, 'Vy', 32002, 'Vz', 22002, 'My', 12002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172002, 72002, 172002, 2002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123002, 123002, 23002, 2002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172005, 14.5, 0.0, 5.225)
    ops.node(123005, 14.5, 0.0, 7.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2005, 172005, 123005, 0.1, 28376587.9715132, 11823578.32146383, 0.00127345, 0.00146667, 0.00057292, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22005, 46.64042651, 0.00130455, 56.68742927, 0.01435732, 5.66874293, 0.05358258, -46.64042651, -0.00130455, -56.68742927, -0.01435732, -5.66874293, -0.05358258, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12005, 85.91392331, 0.00088711, 104.42098872, 0.01604602, 10.44209887, 0.07197918, -85.91392331, -0.00088711, -104.42098872, -0.01604602, -10.44209887, -0.07197918, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22005, 2005, 0.0, 110.81748816, 0.02609099, 110.81748816, 0.07827296, 77.57224171, -2242.3113528, 0.05, 2, 0, 72005, 23005, 2, 3)
    ops.uniaxialMaterial('LimitState', 42005, 27.70437204, 7.029e-05, 83.11311612, 0.00021088, 277.0437204, 0.00070294, -27.70437204, -7.029e-05, -83.11311612, -0.00021088, -277.0437204, -0.00070294, 0.4, 0.3, 0.003, 0.0, 0.0, 22005, 2)
    ops.limitCurve('ThreePoint', 12005, 2005, 0.0, 143.2118383, 0.01774222, 143.2118383, 0.05322667, 100.24828681, -4477.73001163, 0.05, 2, 0, 72005, 23005, 1, 3)
    ops.uniaxialMaterial('LimitState', 32005, 35.80295958, 9.084e-05, 107.40887873, 0.00027253, 358.02959576, 0.00090843, -35.80295958, -9.084e-05, -107.40887873, -0.00027253, -358.02959576, -0.00090843, 0.4, 0.3, 0.003, 0.0, 0.0, 12005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2005, 99999, 'P', 42005, 'Vy', 32005, 'Vz', 22005, 'My', 12005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172005, 72005, 172005, 2005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123005, 123005, 23005, 2005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172006, 18.35, 0.0, 5.3)
    ops.node(123006, 18.35, 0.0, 7.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2006, 172006, 123006, 0.0625, 27810862.23994924, 11587859.26664552, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22006, 32.54637799, 0.00132301, 39.61536656, 0.01732389, 3.96153666, 0.07331701, -32.54637799, -0.00132301, -39.61536656, -0.01732389, -3.96153666, -0.07331701, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12006, 32.54637799, 0.00132301, 39.61536656, 0.01732389, 3.96153666, 0.07331701, -32.54637799, -0.00132301, -39.61536656, -0.01732389, -3.96153666, -0.07331701, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22006, 2006, 0.0, 89.2185848, 0.02646016, 89.2185848, 0.07938049, 62.45300936, -3104.61564301, 0.05, 2, 0, 72006, 23006, 2, 3)
    ops.uniaxialMaterial('LimitState', 42006, 22.3046462, 9.239e-05, 66.9139386, 0.00027718, 223.04646201, 0.00092392, -22.3046462, -9.239e-05, -66.9139386, -0.00027718, -223.04646201, -0.00092392, 0.4, 0.3, 0.003, 0.0, 0.0, 22006, 2)
    ops.limitCurve('ThreePoint', 12006, 2006, 0.0, 89.2185848, 0.02646016, 89.2185848, 0.07938049, 62.45300936, -3104.61564301, 0.05, 2, 0, 72006, 23006, 1, 3)
    ops.uniaxialMaterial('LimitState', 32006, 22.3046462, 9.239e-05, 66.9139386, 0.00027718, 223.04646201, 0.00092392, -22.3046462, -9.239e-05, -66.9139386, -0.00027718, -223.04646201, -0.00092392, 0.4, 0.3, 0.003, 0.0, 0.0, 12006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2006, 99999, 'P', 42006, 'Vy', 32006, 'Vz', 22006, 'My', 12006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172006, 72006, 172006, 2006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123006, 123006, 23006, 2006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172007, 0.0, 5.8, 5.3)
    ops.node(123007, 0.0, 5.8, 7.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2007, 172007, 123007, 0.125, 29172134.69635449, 12155056.12348104, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22007, 137.40614413, 0.00078353, 166.87728514, 0.01648368, 16.68772851, 0.07473056, -137.40614413, -0.00078353, -166.87728514, -0.01648368, -16.68772851, -0.07473056, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12007, 78.80002528, 0.00130663, 95.70121024, 0.01398483, 9.57012102, 0.04906272, -78.80002528, -0.00130663, -95.70121024, -0.01398483, -9.57012102, -0.04906272, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22007, 2007, 0.0, 202.03726167, 0.01567063, 202.03726167, 0.0470119, 141.42608317, -6431.5051022, 0.05, 2, 0, 72007, 23007, 2, 3)
    ops.uniaxialMaterial('LimitState', 42007, 50.50931542, 9.973e-05, 151.52794625, 0.00029919, 505.09315416, 0.0009973, -50.50931542, -9.973e-05, -151.52794625, -0.00029919, -505.09315416, -0.0009973, 0.4, 0.3, 0.003, 0.0, 0.0, 22007, 2)
    ops.limitCurve('ThreePoint', 12007, 2007, 0.0, 128.01932851, 0.02613259, 128.01932851, 0.07839778, 89.61352995, -2274.9055489, 0.05, 2, 0, 72007, 23007, 1, 3)
    ops.uniaxialMaterial('LimitState', 32007, 32.00483213, 6.319e-05, 96.01449638, 0.00018958, 320.04832127, 0.00063193, -32.00483213, -6.319e-05, -96.01449638, -0.00018958, -320.04832127, -0.00063193, 0.4, 0.3, 0.003, 0.0, 0.0, 12007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2007, 99999, 'P', 42007, 'Vy', 32007, 'Vz', 22007, 'My', 12007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172007, 72007, 172007, 2007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123007, 123007, 23007, 2007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172008, 3.85, 5.8, 5.225)
    ops.node(123008, 3.85, 5.8, 7.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2008, 172008, 123008, 0.1375, 27828952.93729831, 11595397.05720763, 0.00204719, 0.00078776, 0.00381276, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22008, 212.46089505, 0.00079699, 258.27140857, 0.02116578, 25.82714086, 0.0751057, -212.46089505, -0.00079699, -258.27140857, -0.02116578, -25.82714086, -0.0751057, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12008, 103.93131456, 0.00143162, 126.34083557, 0.0174586, 12.63408356, 0.04800382, -103.93131456, -0.00143162, -126.34083557, -0.0174586, -12.63408356, -0.04800382, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22008, 2008, 0.0, 231.64439709, 0.01593986, 231.64439709, 0.04781957, 162.15107796, -6099.68872726, 0.05, 2, 0, 72008, 23008, 2, 3)
    ops.uniaxialMaterial('LimitState', 42008, 57.91109927, 0.00010897, 173.73329782, 0.0003269, 579.11099273, 0.00108967, -57.91109927, -0.00010897, -173.73329782, -0.0003269, -579.11099273, -0.00108967, 0.4, 0.3, 0.003, 0.0, 0.0, 22008, 2)
    ops.limitCurve('ThreePoint', 12008, 2008, 0.0, 134.42069097, 0.02863246, 134.42069097, 0.08589737, 94.09448368, -2071.29299216, 0.05, 2, 0, 72008, 23008, 1, 3)
    ops.uniaxialMaterial('LimitState', 32008, 33.60517274, 6.323e-05, 100.81551822, 0.0001897, 336.05172742, 0.00063232, -33.60517274, -6.323e-05, -100.81551822, -0.0001897, -336.05172742, -0.00063232, 0.4, 0.3, 0.003, 0.0, 0.0, 12008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2008, 99999, 'P', 42008, 'Vy', 32008, 'Vz', 22008, 'My', 12008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172008, 72008, 172008, 2008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123008, 123008, 23008, 2008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172009, 7.7, 5.8, 5.2)
    ops.node(123009, 7.7, 5.8, 7.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2009, 172009, 123009, 0.15, 26602686.18153297, 11084452.57563874, 0.00230675, 0.00085938, 0.00495, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22009, 240.71698056, 0.00078311, 293.18458002, 0.02438249, 29.318458, 0.07681314, -240.71698056, -0.00078311, -293.18458002, -0.02438249, -29.318458, -0.07681314, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12009, 89.79548135, 0.00151185, 109.36765003, 0.01966067, 10.936765, 0.04778247, -89.79548135, -0.00151185, -109.36765003, -0.01966067, -10.936765, -0.04778247, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22009, 2009, 0.0, 255.83611038, 0.01566225, 255.83611038, 0.04698674, 179.08527727, -6791.03359431, 0.05, 2, 0, 72009, 23009, 2, 3)
    ops.uniaxialMaterial('LimitState', 42009, 63.9590276, 0.0001154, 191.87708279, 0.00034621, 639.59027596, 0.00115403, -63.9590276, -0.0001154, -191.87708279, -0.00034621, -639.59027596, -0.00115403, 0.4, 0.3, 0.003, 0.0, 0.0, 22009, 2)
    ops.limitCurve('ThreePoint', 12009, 2009, 0.0, 136.3422357, 0.03023693, 136.3422357, 0.09071078, 95.43956499, -2058.47462108, 0.05, 2, 0, 72009, 23009, 1, 3)
    ops.uniaxialMaterial('LimitState', 32009, 34.08555893, 6.15e-05, 102.25667678, 0.0001845, 340.85558926, 0.00061502, -34.08555893, -6.15e-05, -102.25667678, -0.0001845, -340.85558926, -0.00061502, 0.4, 0.3, 0.003, 0.0, 0.0, 12009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2009, 99999, 'P', 42009, 'Vy', 32009, 'Vz', 22009, 'My', 12009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172009, 72009, 172009, 2009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123009, 123009, 23009, 2009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172010, 10.65, 5.8, 5.2)
    ops.node(123010, 10.65, 5.8, 7.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2010, 172010, 123010, 0.15, 27453647.18005611, 11439019.65835671, 0.00230675, 0.00085938, 0.00495, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22010, 243.50890445, 0.00079585, 296.24442359, 0.02387051, 29.62444236, 0.07759341, -243.50890445, -0.00079585, -296.24442359, -0.02387051, -29.62444236, -0.07759341, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12010, 90.14343278, 0.00156846, 109.6653502, 0.01931376, 10.96653502, 0.04812867, -90.14343278, -0.00156846, -109.6653502, -0.01931376, -10.96653502, -0.04812867, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22010, 2010, 0.0, 257.29126689, 0.01591691, 257.29126689, 0.04775074, 180.10388682, -6463.91595839, 0.05, 2, 0, 72010, 23010, 2, 3)
    ops.uniaxialMaterial('LimitState', 42010, 64.32281672, 0.00011246, 192.96845017, 0.00033739, 643.22816723, 0.00112462, -64.32281672, -0.00011246, -192.96845017, -0.00033739, -643.22816723, -0.00112462, 0.4, 0.3, 0.003, 0.0, 0.0, 22010, 2)
    ops.limitCurve('ThreePoint', 12010, 2010, 0.0, 138.24585486, 0.03136923, 138.24585486, 0.09410768, 96.7720984, -1983.20858326, 0.05, 2, 0, 72010, 23010, 1, 3)
    ops.uniaxialMaterial('LimitState', 32010, 34.56146371, 6.043e-05, 103.68439114, 0.00018128, 345.61463714, 0.00060427, -34.56146371, -6.043e-05, -103.68439114, -0.00018128, -345.61463714, -0.00060427, 0.4, 0.3, 0.003, 0.0, 0.0, 12010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2010, 99999, 'P', 42010, 'Vy', 32010, 'Vz', 22010, 'My', 12010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172010, 72010, 172010, 2010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123010, 123010, 23010, 2010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172011, 14.5, 5.8, 5.225)
    ops.node(123011, 14.5, 5.8, 7.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2011, 172011, 123011, 0.1375, 28615495.08058058, 11923122.95024191, 0.00204719, 0.00078776, 0.00381276, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22011, 209.31860397, 0.00079394, 254.1039681, 0.02082754, 25.41039681, 0.07581106, -209.31860397, -0.00079394, -254.1039681, -0.02082754, -25.41039681, -0.07581106, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12011, 100.60915615, 0.00145464, 122.13527761, 0.01721787, 12.21352776, 0.04835407, -100.60915615, -0.00145464, -122.13527761, -0.01721787, -12.21352776, -0.04835407, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22011, 2011, 0.0, 233.24931955, 0.01587884, 233.24931955, 0.04763651, 163.27452368, -5878.84438876, 0.05, 2, 0, 72011, 23011, 2, 3)
    ops.uniaxialMaterial('LimitState', 42011, 58.31232989, 0.00010671, 174.93698966, 0.00032012, 583.12329887, 0.00106706, -58.31232989, -0.00010671, -174.93698966, -0.00032012, -583.12329887, -0.00106706, 0.4, 0.3, 0.003, 0.0, 0.0, 22011, 2)
    ops.limitCurve('ThreePoint', 12011, 2011, 0.0, 136.27939327, 0.0290927, 136.27939327, 0.08727811, 95.39557529, -2012.67777821, 0.05, 2, 0, 72011, 23011, 1, 3)
    ops.uniaxialMaterial('LimitState', 32011, 34.06984832, 6.234e-05, 102.20954495, 0.00018703, 340.69848318, 0.00062345, -34.06984832, -6.234e-05, -102.20954495, -0.00018703, -340.69848318, -0.00062345, 0.4, 0.3, 0.003, 0.0, 0.0, 12011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2011, 99999, 'P', 42011, 'Vy', 32011, 'Vz', 22011, 'My', 12011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172011, 72011, 172011, 2011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123011, 123011, 23011, 2011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172012, 18.35, 5.8, 5.3)
    ops.node(123012, 18.35, 5.8, 7.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2012, 172012, 123012, 0.125, 27539782.31906125, 11474909.29960885, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22012, 135.44611296, 0.00078864, 165.02921369, 0.01659447, 16.50292137, 0.07315108, -135.44611296, -0.00078864, -165.02921369, -0.01659447, -16.50292137, -0.07315108, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12012, 77.66859691, 0.00132083, 94.6323759, 0.01408438, 9.46323759, 0.04814434, -77.66859691, -0.00132083, -94.6323759, -0.01408438, -9.46323759, -0.04814434, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22012, 2012, 0.0, 196.1513974, 0.0157727, 196.1513974, 0.04731811, 137.30597818, -6593.86436585, 0.05, 2, 0, 72012, 23012, 2, 3)
    ops.uniaxialMaterial('LimitState', 42012, 49.03784935, 0.00010256, 147.11354805, 0.00030769, 490.37849351, 0.00102564, -49.03784935, -0.00010256, -147.11354805, -0.00030769, -490.37849351, -0.00102564, 0.4, 0.3, 0.003, 0.0, 0.0, 22012, 2)
    ops.limitCurve('ThreePoint', 12012, 2012, 0.0, 122.95947366, 0.02641666, 122.95947366, 0.07924997, 86.07163156, -2323.13819211, 0.05, 2, 0, 72012, 23012, 1, 3)
    ops.uniaxialMaterial('LimitState', 32012, 30.73986842, 6.429e-05, 92.21960525, 0.00019288, 307.39868416, 0.00064293, -30.73986842, -6.429e-05, -92.21960525, -0.00019288, -307.39868416, -0.00064293, 0.4, 0.3, 0.003, 0.0, 0.0, 12012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2012, 99999, 'P', 42012, 'Vy', 32012, 'Vz', 22012, 'My', 12012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172012, 72012, 172012, 2012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123012, 123012, 23012, 2012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172013, 0.0, 11.6, 5.3)
    ops.node(123013, 0.0, 11.6, 7.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2013, 172013, 123013, 0.125, 26181098.34604938, 10908790.97752057, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22013, 133.46547, 0.00080346, 162.97173532, 0.01722441, 16.29717353, 0.07226925, -133.46547, -0.00080346, -162.97173532, -0.01722441, -16.29717353, -0.07226925, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12013, 75.79001409, 0.00136933, 92.54551096, 0.01462959, 9.2545511, 0.04777912, -75.79001409, -0.00136933, -92.54551096, -0.01462959, -9.2545511, -0.04777912, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22013, 2013, 0.0, 188.94905011, 0.01606918, 188.94905011, 0.04820755, 132.26433508, -6586.87304631, 0.05, 2, 0, 72013, 23013, 2, 3)
    ops.uniaxialMaterial('LimitState', 42013, 47.23726253, 0.00010392, 141.71178758, 0.00031177, 472.37262528, 0.00103925, -47.23726253, -0.00010392, -141.71178758, -0.00031177, -472.37262528, -0.00103925, 0.4, 0.3, 0.003, 0.0, 0.0, 22013, 2)
    ops.limitCurve('ThreePoint', 12013, 2013, 0.0, 117.58067855, 0.02738651, 117.58067855, 0.08215953, 82.30647498, -2313.91486133, 0.05, 2, 0, 72013, 23013, 1, 3)
    ops.uniaxialMaterial('LimitState', 32013, 29.39516964, 6.467e-05, 88.18550891, 0.00019401, 293.95169637, 0.00064671, -29.39516964, -6.467e-05, -88.18550891, -0.00019401, -293.95169637, -0.00064671, 0.4, 0.3, 0.003, 0.0, 0.0, 12013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2013, 99999, 'P', 42013, 'Vy', 32013, 'Vz', 22013, 'My', 12013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172013, 72013, 172013, 2013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123013, 123013, 23013, 2013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172014, 3.85, 11.6, 5.225)
    ops.node(123014, 3.85, 11.6, 7.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2014, 172014, 123014, 0.1375, 27173540.72653969, 11322308.6360582, 0.00204719, 0.00078776, 0.00381276, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22014, 206.84238199, 0.00079799, 251.73297618, 0.02143426, 25.17329762, 0.07470649, -206.84238199, -0.00079799, -251.73297618, -0.02143426, -25.17329762, -0.07470649, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12014, 99.93245887, 0.00145789, 121.62060331, 0.01769533, 12.16206033, 0.04786245, -99.93245887, -0.00145789, -121.62060331, -0.01769533, -12.16206033, -0.04786245, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22014, 2014, 0.0, 228.89795732, 0.01595981, 228.89795732, 0.04787944, 160.22857012, -6286.49070416, 0.05, 2, 0, 72014, 23014, 2, 3)
    ops.uniaxialMaterial('LimitState', 42014, 57.22448933, 0.00011027, 171.67346799, 0.00033082, 572.2448933, 0.00110272, -57.22448933, -0.00011027, -171.67346799, -0.00033082, -572.2448933, -0.00110272, 0.4, 0.3, 0.003, 0.0, 0.0, 22014, 2)
    ops.limitCurve('ThreePoint', 12014, 2014, 0.0, 132.1226812, 0.02915771, 132.1226812, 0.08747312, 92.48587684, -2109.9890639, 0.05, 2, 0, 72014, 23014, 1, 3)
    ops.uniaxialMaterial('LimitState', 32014, 33.0306703, 6.365e-05, 99.0920109, 0.00019095, 330.30670301, 0.0006365, -33.0306703, -6.365e-05, -99.0920109, -0.00019095, -330.30670301, -0.0006365, 0.4, 0.3, 0.003, 0.0, 0.0, 12014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2014, 99999, 'P', 42014, 'Vy', 32014, 'Vz', 22014, 'My', 12014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172014, 72014, 172014, 2014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123014, 123014, 23014, 2014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172015, 7.7, 11.6, 5.2)
    ops.node(123015, 7.7, 11.6, 7.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2015, 172015, 123015, 0.125, 26517997.71690856, 11049165.71537857, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22015, 153.53675863, 0.00084425, 187.07267071, 0.01650535, 18.70726707, 0.06221857, -153.53675863, -0.00084425, -187.07267071, -0.01650535, -18.70726707, -0.06221857, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12015, 75.50232123, 0.00145102, 91.99374146, 0.01424196, 9.19937415, 0.04252251, -75.50232123, -0.00145102, -91.99374146, -0.01424196, -9.19937415, -0.04252251, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22015, 2015, 0.0, 174.82522181, 0.01688492, 174.82522181, 0.05065477, 122.37765526, -4232.82551284, 0.05, 2, 0, 72015, 23015, 2, 3)
    ops.uniaxialMaterial('LimitState', 42015, 43.70630545, 9.493e-05, 131.11891636, 0.0002848, 437.06305452, 0.00094935, -43.70630545, -9.493e-05, -131.11891636, -0.0002848, -437.06305452, -0.00094935, 0.4, 0.3, 0.003, 0.0, 0.0, 22015, 2)
    ops.limitCurve('ThreePoint', 12015, 2015, 0.0, 106.95554211, 0.02902031, 106.95554211, 0.08706093, 74.86887948, -1682.50924794, 0.05, 2, 0, 72015, 23015, 1, 3)
    ops.uniaxialMaterial('LimitState', 32015, 26.73888553, 5.808e-05, 80.21665658, 0.00017424, 267.38885528, 0.0005808, -26.73888553, -5.808e-05, -80.21665658, -0.00017424, -267.38885528, -0.0005808, 0.4, 0.3, 0.003, 0.0, 0.0, 12015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2015, 99999, 'P', 42015, 'Vy', 32015, 'Vz', 22015, 'My', 12015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172015, 72015, 172015, 2015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123015, 123015, 23015, 2015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172016, 10.65, 11.6, 5.2)
    ops.node(123016, 10.65, 11.6, 7.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2016, 172016, 123016, 0.125, 29899798.5694064, 12458249.40391933, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22016, 152.02367527, 0.00081044, 184.11984539, 0.0168078, 18.41198454, 0.06626516, -152.02367527, -0.00081044, -184.11984539, -0.0168078, -18.41198454, -0.06626516, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12016, 74.35087839, 0.00138965, 90.04829155, 0.01445523, 9.00482916, 0.04505209, -74.35087839, -0.00138965, -90.04829155, -0.01445523, -9.00482916, -0.04505209, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22016, 2016, 0.0, 193.11842849, 0.01620873, 193.11842849, 0.04862618, 135.18289994, -4423.55279144, 0.05, 2, 0, 72016, 23016, 2, 3)
    ops.uniaxialMaterial('LimitState', 42016, 48.27960712, 9.301e-05, 144.83882137, 0.00027902, 482.79607123, 0.00093007, -48.27960712, -9.301e-05, -144.83882137, -0.00027902, -482.79607123, -0.00093007, 0.4, 0.3, 0.003, 0.0, 0.0, 22016, 2)
    ops.limitCurve('ThreePoint', 12016, 2016, 0.0, 124.66291557, 0.02779296, 124.66291557, 0.08337889, 87.2640409, -1742.49595533, 0.05, 2, 0, 72016, 23016, 1, 3)
    ops.uniaxialMaterial('LimitState', 32016, 31.16572889, 6.004e-05, 93.49718668, 0.00018012, 311.65728892, 0.00060039, -31.16572889, -6.004e-05, -93.49718668, -0.00018012, -311.65728892, -0.00060039, 0.4, 0.3, 0.003, 0.0, 0.0, 12016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2016, 99999, 'P', 42016, 'Vy', 32016, 'Vz', 22016, 'My', 12016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172016, 72016, 172016, 2016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123016, 123016, 23016, 2016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172017, 14.5, 11.6, 5.225)
    ops.node(123017, 14.5, 11.6, 7.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2017, 172017, 123017, 0.1375, 29353960.10187443, 12230816.70911434, 0.00204719, 0.00078776, 0.00381276, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22017, 209.42168253, 0.00077945, 253.89111376, 0.02062123, 25.38911138, 0.07672695, -209.42168253, -0.00077945, -253.89111376, -0.02062123, -25.38911138, -0.07672695, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12017, 101.72299828, 0.00140029, 123.32326346, 0.01701259, 12.33232635, 0.04878427, -101.72299828, -0.00140029, -123.32326346, -0.01701259, -12.33232635, -0.04878427, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22017, 2017, 0.0, 234.98175434, 0.01558902, 234.98175434, 0.04676707, 164.48722804, -5795.02949087, 0.05, 2, 0, 72017, 23017, 2, 3)
    ops.uniaxialMaterial('LimitState', 42017, 58.74543858, 0.00010479, 176.23631575, 0.00031438, 587.45438585, 0.00104794, -58.74543858, -0.00010479, -176.23631575, -0.00031438, -587.45438585, -0.00104794, 0.4, 0.3, 0.003, 0.0, 0.0, 22017, 2)
    ops.limitCurve('ThreePoint', 12017, 2017, 0.0, 138.0181693, 0.0280058, 138.0181693, 0.0840174, 96.61271851, -1980.001454, 0.05, 2, 0, 72017, 23017, 1, 3)
    ops.uniaxialMaterial('LimitState', 32017, 34.50454232, 6.155e-05, 103.51362697, 0.00018465, 345.04542325, 0.00061552, -34.50454232, -6.155e-05, -103.51362697, -0.00018465, -345.04542325, -0.00061552, 0.4, 0.3, 0.003, 0.0, 0.0, 12017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2017, 99999, 'P', 42017, 'Vy', 32017, 'Vz', 22017, 'My', 12017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172017, 72017, 172017, 2017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123017, 123017, 23017, 2017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172018, 18.35, 11.6, 5.3)
    ops.node(123018, 18.35, 11.6, 7.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2018, 172018, 123018, 0.125, 28446412.30822515, 11852671.79509382, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22018, 133.27915812, 0.0007721, 162.13008012, 0.01652909, 16.21300801, 0.07423981, -133.27915812, -0.0007721, -162.13008012, -0.01652909, -16.21300801, -0.07423981, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12018, 76.22104688, 0.0012884, 92.72060697, 0.0140125, 9.2720607, 0.0487675, -76.22104688, -0.0012884, -92.72060697, -0.0140125, -9.2720607, -0.0487675, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22018, 2018, 0.0, 193.53400803, 0.015442, 193.53400803, 0.04632601, 135.47380562, -6034.76542326, 0.05, 2, 0, 72018, 23018, 2, 3)
    ops.uniaxialMaterial('LimitState', 42018, 48.38350201, 9.797e-05, 145.15050602, 0.00029391, 483.83502006, 0.0009797, -48.38350201, -9.797e-05, -145.15050602, -0.00029391, -483.83502006, -0.0009797, 0.4, 0.3, 0.003, 0.0, 0.0, 22018, 2)
    ops.limitCurve('ThreePoint', 12018, 2018, 0.0, 122.74177174, 0.02576798, 122.74177174, 0.07730393, 85.91924022, -2149.73814528, 0.05, 2, 0, 72018, 23018, 1, 3)
    ops.uniaxialMaterial('LimitState', 32018, 30.68544293, 6.213e-05, 92.0563288, 0.0001864, 306.85442935, 0.00062134, -30.68544293, -6.213e-05, -92.0563288, -0.0001864, -306.85442935, -0.00062134, 0.4, 0.3, 0.003, 0.0, 0.0, 12018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2018, 99999, 'P', 42018, 'Vy', 32018, 'Vz', 22018, 'My', 12018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172018, 72018, 172018, 2018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123018, 123018, 23018, 2018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172019, 0.0, 17.4, 5.3)
    ops.node(123019, 0.0, 17.4, 7.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2019, 172019, 123019, 0.0625, 27951959.79522955, 11646649.91467898, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22019, 33.19131958, 0.00128392, 40.39028067, 0.01696986, 4.03902807, 0.07313055, -33.19131958, -0.00128392, -40.39028067, -0.01696986, -4.03902807, -0.07313055, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12019, 33.19131958, 0.00128392, 40.39028067, 0.01696986, 4.03902807, 0.07313055, -33.19131958, -0.00128392, -40.39028067, -0.01696986, -4.03902807, -0.07313055, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22019, 2019, 0.0, 89.09606572, 0.02567846, 89.09606572, 0.07703539, 62.367246, -3070.11301177, 0.05, 2, 0, 72019, 23019, 2, 3)
    ops.uniaxialMaterial('LimitState', 42019, 22.27401643, 9.18e-05, 66.82204929, 0.0002754, 222.7401643, 0.00091799, -22.27401643, -9.18e-05, -66.82204929, -0.0002754, -222.7401643, -0.00091799, 0.4, 0.3, 0.003, 0.0, 0.0, 22019, 2)
    ops.limitCurve('ThreePoint', 12019, 2019, 0.0, 89.09606572, 0.02567846, 89.09606572, 0.07703539, 62.367246, -3070.11301177, 0.05, 2, 0, 72019, 23019, 1, 3)
    ops.uniaxialMaterial('LimitState', 32019, 22.27401643, 9.18e-05, 66.82204929, 0.0002754, 222.7401643, 0.00091799, -22.27401643, -9.18e-05, -66.82204929, -0.0002754, -222.7401643, -0.00091799, 0.4, 0.3, 0.003, 0.0, 0.0, 12019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2019, 99999, 'P', 42019, 'Vy', 32019, 'Vz', 22019, 'My', 12019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172019, 72019, 172019, 2019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123019, 123019, 23019, 2019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172020, 3.85, 17.4, 5.225)
    ops.node(123020, 3.85, 17.4, 7.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2020, 172020, 123020, 0.1, 28344022.70482242, 11810009.46034267, 0.00127345, 0.00146667, 0.00057292, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22020, 58.31843033, 0.00141872, 70.88536596, 0.01537108, 7.0885366, 0.04995403, -58.31843033, -0.00141872, -70.88536596, -0.01537108, -7.0885366, -0.04995403, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12020, 99.80807929, 0.00095279, 121.31554615, 0.0170376, 12.13155461, 0.06549743, -99.80807929, -0.00095279, -121.31554615, -0.0170376, -12.13155461, -0.06549743, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22020, 2020, 0.0, 97.65453138, 0.02837442, 97.65453138, 0.08512327, 68.35817197, -1761.54590885, 0.05, 2, 0, 72020, 23020, 2, 3)
    ops.uniaxialMaterial('LimitState', 42020, 24.41363284, 6.202e-05, 73.24089853, 0.00018605, 244.13632845, 0.00062016, -24.41363284, -6.202e-05, -73.24089853, -0.00018605, -244.13632845, -0.00062016, 0.4, 0.3, 0.003, 0.0, 0.0, 22020, 2)
    ops.limitCurve('ThreePoint', 12020, 2020, 0.0, 129.48048791, 0.01905582, 129.48048791, 0.05716745, 90.63634154, -3399.37994158, 0.05, 2, 0, 72020, 23020, 1, 3)
    ops.uniaxialMaterial('LimitState', 32020, 32.37012198, 8.223e-05, 97.11036593, 0.00024668, 323.70121978, 0.00082227, -32.37012198, -8.223e-05, -97.11036593, -0.00024668, -323.70121978, -0.00082227, 0.4, 0.3, 0.003, 0.0, 0.0, 12020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2020, 99999, 'P', 42020, 'Vy', 32020, 'Vz', 22020, 'My', 12020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172020, 72020, 172020, 2020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123020, 123020, 23020, 2020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172021, 7.7, 17.4, 5.2)
    ops.node(123021, 7.7, 17.4, 7.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2021, 172021, 123021, 0.0875, 26951226.28414627, 11229677.61839428, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22021, 49.50117575, 0.00133621, 60.30539264, 0.01546549, 6.03053926, 0.05721868, -49.50117575, -0.00133621, -60.30539264, -0.01546549, -6.03053926, -0.05721868, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12021, 65.68407688, 0.00100177, 80.02040328, 0.01675775, 8.00204033, 0.07082703, -65.68407688, -0.00100177, -80.02040328, -0.01675775, -8.00204033, -0.07082703, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22021, 2021, 0.0, 101.26852124, 0.02672425, 101.26852124, 0.08017274, 70.88796486, -2458.77132642, 0.05, 2, 0, 72021, 23021, 2, 3)
    ops.uniaxialMaterial('LimitState', 42021, 25.31713031, 7.73e-05, 75.95139093, 0.00023189, 253.17130309, 0.00077297, -25.31713031, -7.73e-05, -75.95139093, -0.00023189, -253.17130309, -0.00077297, 0.4, 0.3, 0.003, 0.0, 0.0, 22021, 2)
    ops.limitCurve('ThreePoint', 12021, 2021, 0.0, 122.47755093, 0.02003539, 122.47755093, 0.06010616, 85.73428565, -4083.12498558, 0.05, 2, 0, 72021, 23021, 1, 3)
    ops.uniaxialMaterial('LimitState', 32021, 30.61938773, 9.349e-05, 91.8581632, 0.00028046, 306.19387732, 0.00093485, -30.61938773, -9.349e-05, -91.8581632, -0.00028046, -306.19387732, -0.00093485, 0.4, 0.3, 0.003, 0.0, 0.0, 12021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2021, 99999, 'P', 42021, 'Vy', 32021, 'Vz', 22021, 'My', 12021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172021, 72021, 172021, 2021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123021, 123021, 23021, 2021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172022, 10.65, 17.4, 5.2)
    ops.node(123022, 10.65, 17.4, 7.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2022, 172022, 123022, 0.0875, 27286947.98524707, 11369561.66051961, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22022, 49.07373836, 0.0013338, 59.75525832, 0.0152693, 5.97552583, 0.05738459, -49.07373836, -0.0013338, -59.75525832, -0.0152693, -5.97552583, -0.05738459, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12022, 65.27259891, 0.00099795, 79.48000579, 0.01653784, 7.94800058, 0.07107602, -65.27259891, -0.00099795, -79.48000579, -0.01653784, -7.94800058, -0.07107602, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22022, 2022, 0.0, 102.90874161, 0.02667606, 102.90874161, 0.08002817, 72.03611913, -2513.43360217, 0.05, 2, 0, 72022, 23022, 2, 3)
    ops.uniaxialMaterial('LimitState', 42022, 25.7271854, 7.758e-05, 77.18155621, 0.00023275, 257.27185403, 0.00077582, -25.7271854, -7.758e-05, -77.18155621, -0.00023275, -257.27185403, -0.00077582, 0.4, 0.3, 0.003, 0.0, 0.0, 22022, 2)
    ops.limitCurve('ThreePoint', 12022, 2022, 0.0, 124.44266756, 0.01995891, 124.44266756, 0.05987673, 87.10986729, -4181.78910197, 0.05, 2, 0, 72022, 23022, 1, 3)
    ops.uniaxialMaterial('LimitState', 32022, 31.11066689, 9.382e-05, 93.33200067, 0.00028145, 311.10666889, 0.00093816, -31.11066689, -9.382e-05, -93.33200067, -0.00028145, -311.10666889, -0.00093816, 0.4, 0.3, 0.003, 0.0, 0.0, 12022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2022, 99999, 'P', 42022, 'Vy', 32022, 'Vz', 22022, 'My', 12022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172022, 72022, 172022, 2022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123022, 123022, 23022, 2022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172023, 14.5, 17.4, 5.225)
    ops.node(123023, 14.5, 17.4, 7.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2023, 172023, 123023, 0.1, 27786675.74057118, 11577781.55857133, 0.00127345, 0.00146667, 0.00057292, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22023, 57.91190899, 0.00132705, 70.46107777, 0.0160539, 7.04610778, 0.05021251, -57.91190899, -0.00132705, -70.46107777, -0.0160539, -7.04610778, -0.05021251, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12023, 98.37208137, 0.00090971, 119.68873065, 0.01788738, 11.96887307, 0.06575261, -98.37208137, -0.00090971, -119.68873065, -0.01788738, -11.96887307, -0.06575261, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22023, 2023, 0.0, 103.33900462, 0.02654091, 103.33900462, 0.07962273, 72.33730323, -1919.43549589, 0.05, 2, 0, 72023, 23023, 2, 3)
    ops.uniaxialMaterial('LimitState', 42023, 25.83475115, 6.694e-05, 77.50425346, 0.00020083, 258.34751155, 0.00066942, -25.83475115, -6.694e-05, -77.50425346, -0.00020083, -258.34751155, -0.00066942, 0.4, 0.3, 0.003, 0.0, 0.0, 22023, 2)
    ops.limitCurve('ThreePoint', 12023, 2023, 0.0, 132.50077555, 0.01819429, 132.50077555, 0.05458287, 92.75054289, -3751.45749701, 0.05, 2, 0, 72023, 23023, 1, 3)
    ops.uniaxialMaterial('LimitState', 32023, 33.12519389, 8.583e-05, 99.37558167, 0.0002575, 331.25193888, 0.00085833, -33.12519389, -8.583e-05, -99.37558167, -0.0002575, -331.25193888, -0.00085833, 0.4, 0.3, 0.003, 0.0, 0.0, 12023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2023, 99999, 'P', 42023, 'Vy', 32023, 'Vz', 22023, 'My', 12023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172023, 72023, 172023, 2023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123023, 123023, 23023, 2023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172024, 18.35, 17.4, 5.3)
    ops.node(123024, 18.35, 17.4, 7.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2024, 172024, 123024, 0.0625, 27432290.77154844, 11430121.15481185, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22024, 32.95231913, 0.00130421, 40.13514859, 0.01726419, 4.01351486, 0.0727917, -32.95231913, -0.00130421, -40.13514859, -0.01726419, -4.01351486, -0.0727917, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12024, 32.95231913, 0.00130421, 40.13514859, 0.01726419, 4.01351486, 0.0727917, -32.95231913, -0.00130421, -40.13514859, -0.01726419, -4.01351486, -0.0727917, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22024, 2024, 0.0, 89.33362537, 0.02608412, 89.33362537, 0.07825236, 62.53353776, -3177.78204514, 0.05, 2, 0, 72024, 23024, 2, 3)
    ops.uniaxialMaterial('LimitState', 42024, 22.33340634, 9.379e-05, 67.00021903, 0.00028136, 223.33406344, 0.00093788, -22.33340634, -9.379e-05, -67.00021903, -0.00028136, -223.33406344, -0.00093788, 0.4, 0.3, 0.003, 0.0, 0.0, 22024, 2)
    ops.limitCurve('ThreePoint', 12024, 2024, 0.0, 89.33362537, 0.02608412, 89.33362537, 0.07825236, 62.53353776, -3177.78204514, 0.05, 2, 0, 72024, 23024, 1, 3)
    ops.uniaxialMaterial('LimitState', 32024, 22.33340634, 9.379e-05, 67.00021903, 0.00028136, 223.33406344, 0.00093788, -22.33340634, -9.379e-05, -67.00021903, -0.00028136, -223.33406344, -0.00093788, 0.4, 0.3, 0.003, 0.0, 0.0, 12024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2024, 99999, 'P', 42024, 'Vy', 32024, 'Vz', 22024, 'My', 12024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172024, 72024, 172024, 2024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123024, 123024, 23024, 2024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173001, 0.0, 0.0, 7.8)
    ops.node(124001, 0.0, 0.0, 9.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3001, 173001, 124001, 0.0625, 26366582.23586136, 10986075.9316089, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23001, 36.33033768, 0.0013, 44.5543141, 0.01898879, 4.45543141, 0.08235524, -36.33033768, -0.0013, -44.5543141, -0.01898879, -4.45543141, -0.08235524, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13001, 40.75475038, 0.0013, 49.98026623, 0.01898879, 4.99802662, 0.08235524, -40.75475038, -0.0013, -49.98026623, -0.01898879, -4.99802662, -0.08235524, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23001, 3001, 0.0, 81.66990544, 0.02600005, 81.66990544, 0.07800014, 57.16893381, -8571.83285354, 0.05, 2, 0, 73001, 24001, 2, 3)
    ops.uniaxialMaterial('LimitState', 43001, 20.41747636, 8.921e-05, 61.25242908, 0.00026762, 204.1747636, 0.00089207, -20.41747636, -8.921e-05, -61.25242908, -0.00026762, -204.1747636, -0.00089207, 0.4, 0.3, 0.003, 0.0, 0.0, 23001, 2)
    ops.limitCurve('ThreePoint', 13001, 3001, 0.0, 81.66990544, 0.02600005, 81.66990544, 0.07800014, 57.16893381, -8571.83285354, 0.05, 2, 0, 73001, 24001, 1, 3)
    ops.uniaxialMaterial('LimitState', 33001, 20.41747636, 8.921e-05, 61.25242908, 0.00026762, 204.1747636, 0.00089207, -20.41747636, -8.921e-05, -61.25242908, -0.00026762, -204.1747636, -0.00089207, 0.4, 0.3, 0.003, 0.0, 0.0, 13001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3001, 99999, 'P', 43001, 'Vy', 33001, 'Vz', 23001, 'My', 13001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173001, 73001, 173001, 3001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124001, 124001, 24001, 3001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173002, 3.85, 0.0, 7.725)
    ops.node(124002, 3.85, 0.0, 9.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3002, 173002, 124002, 0.1, 29561045.92235452, 12317102.46764771, 0.00127345, 0.00146667, 0.00057292, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23002, 39.11891237, 0.00122107, 47.6019378, 0.01524391, 4.76019378, 0.05996642, -39.11891237, -0.00122107, -47.6019378, -0.01524391, -4.76019378, -0.05996642, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13002, 73.64618464, 0.00084445, 89.61652787, 0.01712996, 8.96165279, 0.08090191, -73.64618464, -0.00084445, -89.61652787, -0.01712996, -8.96165279, -0.08090191, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23002, 3002, 0.0, 108.28506483, 0.02442131, 108.28506483, 0.07326394, 75.79954538, -4663.03029019, 0.05, 2, 0, 73002, 24002, 2, 3)
    ops.uniaxialMaterial('LimitState', 43002, 27.07126621, 6.594e-05, 81.21379862, 0.00019781, 270.71266207, 0.00065936, -27.07126621, -6.594e-05, -81.21379862, -0.00019781, -270.71266207, -0.00065936, 0.4, 0.3, 0.003, 0.0, 0.0, 23002, 2)
    ops.limitCurve('ThreePoint', 13002, 3002, 0.0, 141.37142498, 0.01688904, 141.37142498, 0.05066712, 98.95999749, -10885.66191046, 0.05, 2, 0, 73002, 24002, 1, 3)
    ops.uniaxialMaterial('LimitState', 33002, 35.34285625, 8.608e-05, 106.02856874, 0.00025825, 353.42856246, 0.00086082, -35.34285625, -8.608e-05, -106.02856874, -0.00025825, -353.42856246, -0.00086082, 0.4, 0.3, 0.003, 0.0, 0.0, 13002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3002, 99999, 'P', 43002, 'Vy', 33002, 'Vz', 23002, 'My', 13002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173002, 73002, 173002, 3002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124002, 124002, 24002, 3002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173005, 14.5, 0.0, 7.725)
    ops.node(124005, 14.5, 0.0, 9.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3005, 173005, 124005, 0.1, 27613911.03063542, 11505796.26276476, 0.00127345, 0.00146667, 0.00057292, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23005, 39.41105676, 0.00123996, 48.18406285, 0.01523169, 4.81840628, 0.05940399, -39.41105676, -0.00123996, -48.18406285, -0.01523169, -4.81840628, -0.05940399, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13005, 74.36250692, 0.00085873, 90.91579881, 0.01710811, 9.09157988, 0.08009548, -74.36250692, -0.00085873, -90.91579881, -0.01710811, -9.09157988, -0.08009548, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23005, 3005, 0.0, 101.47473327, 0.02479916, 101.47473327, 0.07439749, 71.03231329, -4472.50711484, 0.05, 2, 0, 73005, 24005, 2, 3)
    ops.uniaxialMaterial('LimitState', 43005, 25.36868332, 6.615e-05, 76.10604995, 0.00019844, 253.68683316, 0.00066146, -25.36868332, -6.615e-05, -76.10604995, -0.00019844, -253.68683316, -0.00066146, 0.4, 0.3, 0.003, 0.0, 0.0, 23005, 2)
    ops.limitCurve('ThreePoint', 13005, 3005, 0.0, 133.68235631, 0.01717466, 133.68235631, 0.05152399, 93.57764942, -10420.13230978, 0.05, 2, 0, 73005, 24005, 1, 3)
    ops.uniaxialMaterial('LimitState', 33005, 33.42058908, 8.714e-05, 100.26176723, 0.00026142, 334.20589078, 0.0008714, -33.42058908, -8.714e-05, -100.26176723, -0.00026142, -334.20589078, -0.0008714, 0.4, 0.3, 0.003, 0.0, 0.0, 13005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3005, 99999, 'P', 43005, 'Vy', 33005, 'Vz', 23005, 'My', 13005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173005, 73005, 173005, 3005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124005, 124005, 24005, 3005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173006, 18.35, 0.0, 7.8)
    ops.node(124006, 18.35, 0.0, 9.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3006, 173006, 124006, 0.0625, 27744747.66448511, 11560311.5268688, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23006, 35.74741333, 0.00131155, 43.71229595, 0.01823573, 4.37122959, 0.08214815, -35.74741333, -0.00131155, -43.71229595, -0.01823573, -4.37122959, -0.08214815, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13006, 39.75985003, 0.00131155, 48.61874384, 0.01823573, 4.86187438, 0.08214815, -39.75985003, -0.00131155, -48.61874384, -0.01823573, -4.86187438, -0.08214815, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23006, 3006, 0.0, 82.33978905, 0.02623091, 82.33978905, 0.07869272, 57.63785234, -8064.50233831, 0.05, 2, 0, 73006, 24006, 2, 3)
    ops.uniaxialMaterial('LimitState', 43006, 20.58494726, 8.547e-05, 61.75484179, 0.00025641, 205.84947263, 0.00085472, -20.58494726, -8.547e-05, -61.75484179, -0.00025641, -205.84947263, -0.00085472, 0.4, 0.3, 0.003, 0.0, 0.0, 23006, 2)
    ops.limitCurve('ThreePoint', 13006, 3006, 0.0, 82.33978905, 0.02623091, 82.33978905, 0.07869272, 57.63785234, -8064.50233831, 0.05, 2, 0, 73006, 24006, 1, 3)
    ops.uniaxialMaterial('LimitState', 33006, 20.58494726, 8.547e-05, 61.75484179, 0.00025641, 205.84947263, 0.00085472, -20.58494726, -8.547e-05, -61.75484179, -0.00025641, -205.84947263, -0.00085472, 0.4, 0.3, 0.003, 0.0, 0.0, 13006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3006, 99999, 'P', 43006, 'Vy', 33006, 'Vz', 23006, 'My', 13006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173006, 73006, 173006, 3006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124006, 124006, 24006, 3006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173007, 0.0, 5.8, 7.8)
    ops.node(124007, 0.0, 5.8, 9.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3007, 173007, 124007, 0.125, 27358059.12289379, 11399191.30120574, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23007, 119.91693622, 0.00076177, 146.7617438, 0.01811789, 14.67617438, 0.08188859, -119.91693622, -0.00076177, -146.7617438, -0.01811789, -14.67617438, -0.08188859, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13007, 46.89825624, 0.00128795, 57.39697897, 0.01530339, 5.7396979, 0.05370787, -46.89825624, -0.00128795, -57.39697897, -0.01530339, -5.7396979, -0.05370787, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23007, 3007, 0.0, 187.16415309, 0.01523542, 187.16415309, 0.04570625, 131.01490716, -18227.32526833, 0.05, 2, 0, 73007, 24007, 2, 3)
    ops.uniaxialMaterial('LimitState', 43007, 46.79103827, 9.851e-05, 140.37311482, 0.00029554, 467.91038273, 0.00098514, -46.79103827, -9.851e-05, -140.37311482, -0.00029554, -467.91038273, -0.00098514, 0.4, 0.3, 0.003, 0.0, 0.0, 23007, 2)
    ops.limitCurve('ThreePoint', 13007, 3007, 0.0, 115.30790851, 0.025759, 115.30790851, 0.07727699, 80.71553596, -5117.55931312, 0.05, 2, 0, 73007, 24007, 1, 3)
    ops.uniaxialMaterial('LimitState', 33007, 28.82697713, 6.069e-05, 86.48093138, 0.00018208, 288.26977127, 0.00060693, -28.82697713, -6.069e-05, -86.48093138, -0.00018208, -288.26977127, -0.00060693, 0.4, 0.3, 0.003, 0.0, 0.0, 13007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3007, 99999, 'P', 43007, 'Vy', 33007, 'Vz', 23007, 'My', 13007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173007, 73007, 173007, 3007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124007, 124007, 24007, 3007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173008, 3.85, 5.8, 7.725)
    ops.node(124008, 3.85, 5.8, 9.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3008, 173008, 124008, 0.1375, 27205570.22213296, 11335654.25922207, 0.00204719, 0.00078776, 0.00381276, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23008, 156.82362075, 0.00075967, 191.79774002, 0.01818948, 19.179774, 0.07177159, -156.82362075, -0.00075967, -191.79774002, -0.01818948, -19.179774, -0.07177159, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13008, 60.0087459, 0.00137676, 73.39163443, 0.01527229, 7.33916344, 0.0465738, -60.0087459, -0.00137676, -73.39163443, -0.01527229, -7.33916344, -0.0465738, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23008, 3008, 0.0, 194.89547005, 0.0151935, 194.89547005, 0.04558049, 136.42682903, -9328.12306138, 0.05, 2, 0, 73008, 24008, 2, 3)
    ops.uniaxialMaterial('LimitState', 43008, 48.72386751, 9.378e-05, 146.17160254, 0.00028134, 487.23867512, 0.00093781, -48.72386751, -9.378e-05, -146.17160254, -0.00028134, -487.23867512, -0.00093781, 0.4, 0.3, 0.003, 0.0, 0.0, 23008, 2)
    ops.limitCurve('ThreePoint', 13008, 3008, 0.0, 111.22766045, 0.02753514, 111.22766045, 0.08260543, 77.85936232, -2476.53915441, 0.05, 2, 0, 73008, 24008, 1, 3)
    ops.uniaxialMaterial('LimitState', 33008, 27.80691511, 5.352e-05, 83.42074534, 0.00016056, 278.06915113, 0.00053521, -27.80691511, -5.352e-05, -83.42074534, -0.00016056, -278.06915113, -0.00053521, 0.4, 0.3, 0.003, 0.0, 0.0, 13008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3008, 99999, 'P', 43008, 'Vy', 33008, 'Vz', 23008, 'My', 13008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173008, 73008, 173008, 3008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124008, 124008, 24008, 3008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173009, 7.7, 5.8, 7.7)
    ops.node(124009, 7.7, 5.8, 9.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3009, 173009, 124009, 0.15, 27498258.771178, 11457607.82132417, 0.00230675, 0.00085938, 0.00495, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23009, 211.97192461, 0.00076066, 259.04746276, 0.01572743, 25.90474628, 0.05898248, -211.97192461, -0.00076066, -259.04746276, -0.01572743, -25.90474628, -0.05898248, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13009, 78.00750115, 0.00145827, 95.33170625, 0.01343466, 9.53317062, 0.03892723, -78.00750115, -0.00145827, -95.33170625, -0.01343466, -9.53317062, -0.03892723, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23009, 3009, 0.0, 199.60900839, 0.01521322, 199.60900839, 0.04563966, 139.72630587, -6152.46212464, 0.05, 2, 0, 73009, 24009, 2, 3)
    ops.uniaxialMaterial('LimitState', 43009, 49.9022521, 8.711e-05, 149.70675629, 0.00026132, 499.02252098, 0.00087108, -49.9022521, -8.711e-05, -149.70675629, -0.00026132, -499.02252098, -0.00087108, 0.4, 0.3, 0.003, 0.0, 0.0, 23009, 2)
    ops.limitCurve('ThreePoint', 13009, 3009, 0.0, 75.87199206, 0.02916532, 75.87199206, 0.08749597, 53.11039444, -1554.95663538, 0.05, 2, 0, 73009, 24009, 1, 3)
    ops.uniaxialMaterial('LimitState', 33009, 18.96799801, 3.311e-05, 56.90399404, 9.933e-05, 189.67998015, 0.0003311, -18.96799801, -3.311e-05, -56.90399404, -9.933e-05, -189.67998015, -0.0003311, 0.4, 0.3, 0.003, 0.0, 0.0, 13009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3009, 99999, 'P', 43009, 'Vy', 33009, 'Vz', 23009, 'My', 13009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173009, 73009, 173009, 3009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124009, 124009, 24009, 3009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173010, 10.65, 5.8, 7.7)
    ops.node(124010, 10.65, 5.8, 9.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3010, 173010, 124010, 0.15, 28548679.90146926, 11895283.29227886, 0.00230675, 0.00085938, 0.00495, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23010, 209.85584455, 0.0007415, 255.86771223, 0.01544471, 25.58677122, 0.05911797, -209.85584455, -0.0007415, -255.86771223, -0.01544471, -25.58677122, -0.05911797, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13010, 77.48454479, 0.00140186, 94.47339077, 0.01316736, 9.44733908, 0.0389064, -77.48454479, -0.00140186, -94.47339077, -0.01316736, -9.44733908, -0.0389064, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23010, 3010, 0.0, 203.02975402, 0.01482991, 203.02975402, 0.04448973, 142.12082782, -5727.81562577, 0.05, 2, 0, 73010, 24010, 2, 3)
    ops.uniaxialMaterial('LimitState', 43010, 50.75743851, 8.534e-05, 152.27231552, 0.00025602, 507.57438506, 0.0008534, -50.75743851, -8.534e-05, -152.27231552, -0.00025602, -507.57438506, -0.0008534, 0.4, 0.3, 0.003, 0.0, 0.0, 23010, 2)
    ops.limitCurve('ThreePoint', 13010, 3010, 0.0, 80.32757582, 0.02803717, 80.32757582, 0.0841115, 56.22930308, -1465.7333725, 0.05, 2, 0, 73010, 24010, 1, 3)
    ops.uniaxialMaterial('LimitState', 33010, 20.08189396, 3.376e-05, 60.24568187, 0.00010129, 200.81893956, 0.00033764, -20.08189396, -3.376e-05, -60.24568187, -0.00010129, -200.81893956, -0.00033764, 0.4, 0.3, 0.003, 0.0, 0.0, 13010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3010, 99999, 'P', 43010, 'Vy', 33010, 'Vz', 23010, 'My', 13010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173010, 73010, 173010, 3010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124010, 124010, 24010, 3010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173011, 14.5, 5.8, 7.725)
    ops.node(124011, 14.5, 5.8, 9.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3011, 173011, 124011, 0.1375, 28268445.41777076, 11778518.92407115, 0.00204719, 0.00078776, 0.00381276, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23011, 164.96843896, 0.00075453, 201.29807193, 0.01720346, 20.12980719, 0.07130156, -164.96843896, -0.00075453, -201.29807193, -0.01720346, -20.12980719, -0.07130156, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13011, 63.90110604, 0.00131701, 77.97351737, 0.01443057, 7.79735174, 0.04603351, -63.90110604, -0.00131701, -77.97351737, -0.01443057, -7.79735174, -0.04603351, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23011, 3011, 0.0, 196.82393928, 0.01509061, 196.82393928, 0.04527183, 137.77675749, -8695.07646129, 0.05, 2, 0, 73011, 24011, 2, 3)
    ops.uniaxialMaterial('LimitState', 43011, 49.20598482, 9.115e-05, 147.61795446, 0.00027344, 492.05984819, 0.00091148, -49.20598482, -9.115e-05, -147.61795446, -0.00027344, -492.05984819, -0.00091148, 0.4, 0.3, 0.003, 0.0, 0.0, 23011, 2)
    ops.limitCurve('ThreePoint', 13011, 3011, 0.0, 109.28655485, 0.02634023, 109.28655485, 0.07902069, 76.5005884, -2327.96730857, 0.05, 2, 0, 73011, 24011, 1, 3)
    ops.uniaxialMaterial('LimitState', 33011, 27.32163871, 5.061e-05, 81.96491614, 0.00015183, 273.21638713, 0.0005061, -27.32163871, -5.061e-05, -81.96491614, -0.00015183, -273.21638713, -0.0005061, 0.4, 0.3, 0.003, 0.0, 0.0, 13011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3011, 99999, 'P', 43011, 'Vy', 33011, 'Vz', 23011, 'My', 13011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173011, 73011, 173011, 3011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124011, 124011, 24011, 3011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173012, 18.35, 5.8, 7.8)
    ops.node(124012, 18.35, 5.8, 9.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3012, 173012, 124012, 0.125, 27481665.46781997, 11450693.94492499, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23012, 121.75319124, 0.00076022, 148.96869384, 0.01762196, 14.89686938, 0.08143887, -121.75319124, -0.00076022, -148.96869384, -0.01762196, -14.89686938, -0.08143887, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13012, 47.52078114, 0.00127154, 58.14310593, 0.01488776, 5.81431059, 0.05332007, -47.52078114, -0.00127154, -58.14310593, -0.01488776, -5.81431059, -0.05332007, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23012, 3012, 0.0, 183.86408398, 0.01520444, 183.86408398, 0.04561331, 128.70485879, -17046.5707758, 0.05, 2, 0, 73012, 24012, 2, 3)
    ops.uniaxialMaterial('LimitState', 43012, 45.96602099, 9.634e-05, 137.89806298, 0.00028903, 459.66020995, 0.00096342, -45.96602099, -9.634e-05, -137.89806298, -0.00028903, -459.66020995, -0.00096342, 0.4, 0.3, 0.003, 0.0, 0.0, 23012, 2)
    ops.limitCurve('ThreePoint', 13012, 3012, 0.0, 113.81247516, 0.02543087, 113.81247516, 0.07629262, 79.66873261, -4804.44042204, 0.05, 2, 0, 73012, 24012, 1, 3)
    ops.uniaxialMaterial('LimitState', 33012, 28.45311879, 5.964e-05, 85.35935637, 0.00017891, 284.53118791, 0.00059636, -28.45311879, -5.964e-05, -85.35935637, -0.00017891, -284.53118791, -0.00059636, 0.4, 0.3, 0.003, 0.0, 0.0, 13012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3012, 99999, 'P', 43012, 'Vy', 33012, 'Vz', 23012, 'My', 13012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173012, 73012, 173012, 3012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124012, 124012, 24012, 3012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173013, 0.0, 11.6, 7.8)
    ops.node(124013, 0.0, 11.6, 9.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3013, 173013, 124013, 0.125, 25944895.63551983, 10810373.1814666, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23013, 122.8893447, 0.00077221, 150.83821637, 0.01836421, 15.08382164, 0.08166529, -122.8893447, -0.00077221, -150.83821637, -0.01836421, -15.08382164, -0.08166529, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13013, 47.76046025, 0.00128925, 58.62267925, 0.01549518, 5.86226792, 0.05361684, -47.76046025, -0.00128925, -58.62267925, -0.01549518, -5.86226792, -0.05361684, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23013, 3013, 0.0, 178.9669584, 0.01544412, 178.9669584, 0.04633235, 125.27687088, -18200.06178774, 0.05, 2, 0, 73013, 24013, 2, 3)
    ops.uniaxialMaterial('LimitState', 43013, 44.7417396, 9.933e-05, 134.2252188, 0.00029799, 447.41739599, 0.00099331, -44.7417396, -9.933e-05, -134.2252188, -0.00029799, -447.41739599, -0.00099331, 0.4, 0.3, 0.003, 0.0, 0.0, 23013, 2)
    ops.limitCurve('ThreePoint', 13013, 3013, 0.0, 109.43259821, 0.02578508, 109.43259821, 0.07735523, 76.60281875, -5100.30338511, 0.05, 2, 0, 73013, 24013, 1, 3)
    ops.uniaxialMaterial('LimitState', 33013, 27.35814955, 6.074e-05, 82.07444866, 0.00018221, 273.58149553, 0.00060738, -27.35814955, -6.074e-05, -82.07444866, -0.00018221, -273.58149553, -0.00060738, 0.4, 0.3, 0.003, 0.0, 0.0, 13013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3013, 99999, 'P', 43013, 'Vy', 33013, 'Vz', 23013, 'My', 13013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173013, 73013, 173013, 3013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124013, 124013, 24013, 3013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173014, 3.85, 11.6, 7.725)
    ops.node(124014, 3.85, 11.6, 9.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3014, 173014, 124014, 0.1375, 28437746.00914134, 11849060.83714222, 0.00204719, 0.00078776, 0.00381276, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23014, 159.56255043, 0.00075085, 194.64077732, 0.01767005, 19.46407773, 0.0719691, -159.56255043, -0.00075085, -194.64077732, -0.01767005, -19.46407773, -0.0719691, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13014, 61.33430593, 0.00133566, 74.81803813, 0.01482413, 7.48180381, 0.04654445, -61.33430593, -0.00133566, -74.81803813, -0.01482413, -7.48180381, -0.04654445, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23014, 3014, 0.0, 199.47622023, 0.01501703, 199.47622023, 0.04505108, 139.63335416, -9264.26117529, 0.05, 2, 0, 73014, 24014, 2, 3)
    ops.uniaxialMaterial('LimitState', 43014, 49.86905506, 9.183e-05, 149.60716517, 0.00027548, 498.69055058, 0.00091826, -49.86905506, -9.183e-05, -149.60716517, -0.00027548, -498.69055058, -0.00091826, 0.4, 0.3, 0.003, 0.0, 0.0, 23014, 2)
    ops.limitCurve('ThreePoint', 13014, 3014, 0.0, 113.36877222, 0.0267132, 113.36877222, 0.08013959, 79.35814055, -2451.70792684, 0.05, 2, 0, 73014, 24014, 1, 3)
    ops.uniaxialMaterial('LimitState', 33014, 28.34219305, 5.219e-05, 85.02657916, 0.00015656, 283.42193055, 0.00052188, -28.34219305, -5.219e-05, -85.02657916, -0.00015656, -283.42193055, -0.00052188, 0.4, 0.3, 0.003, 0.0, 0.0, 13014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3014, 99999, 'P', 43014, 'Vy', 33014, 'Vz', 23014, 'My', 13014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173014, 73014, 173014, 3014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124014, 124014, 24014, 3014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173015, 7.7, 11.6, 7.7)
    ops.node(124015, 7.7, 11.6, 9.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3015, 173015, 124015, 0.125, 27229633.27405487, 11345680.5308562, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23015, 140.27809827, 0.00080449, 171.59244916, 0.01776134, 17.15924492, 0.07171557, -140.27809827, -0.00080449, -171.59244916, -0.01776134, -17.15924492, -0.07171557, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13015, 59.44278492, 0.00137841, 72.71222789, 0.01522763, 7.27122279, 0.0486065, -59.44278492, -0.00137841, -72.71222789, -0.01522763, -7.27122279, -0.0486065, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23015, 3015, 0.0, 164.44835071, 0.0160897, 164.44835071, 0.04826911, 115.11384549, -8315.67165056, 0.05, 2, 0, 73015, 24015, 2, 3)
    ops.uniaxialMaterial('LimitState', 43015, 41.11208768, 8.697e-05, 123.33626303, 0.0002609, 411.12087677, 0.00086966, -41.11208768, -8.697e-05, -123.33626303, -0.0002609, -411.12087677, -0.00086966, 0.4, 0.3, 0.003, 0.0, 0.0, 23015, 2)
    ops.limitCurve('ThreePoint', 13015, 3015, 0.0, 98.37129645, 0.0275682, 98.37129645, 0.08270459, 68.85990751, -2550.29648245, 0.05, 2, 0, 73015, 24015, 1, 3)
    ops.uniaxialMaterial('LimitState', 33015, 24.59282411, 5.202e-05, 73.77847234, 0.00015607, 245.92824112, 0.00052022, -24.59282411, -5.202e-05, -73.77847234, -0.00015607, -245.92824112, -0.00052022, 0.4, 0.3, 0.003, 0.0, 0.0, 13015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3015, 99999, 'P', 43015, 'Vy', 33015, 'Vz', 23015, 'My', 13015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173015, 73015, 173015, 3015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124015, 124015, 24015, 3015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173016, 10.65, 11.6, 7.7)
    ops.node(124016, 10.65, 11.6, 9.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3016, 173016, 124016, 0.125, 27910660.76253617, 11629441.98439007, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23016, 141.74385351, 0.0007934, 173.13343299, 0.01758038, 17.3133433, 0.07184681, -141.74385351, -0.0007934, -173.13343299, -0.01758038, -17.3133433, -0.07184681, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13016, 60.29363269, 0.0013397, 73.64582912, 0.01505018, 7.36458291, 0.04862219, -60.29363269, -0.0013397, -73.64582912, -0.01505018, -7.36458291, -0.04862219, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23016, 3016, 0.0, 167.64783212, 0.01586809, 167.64783212, 0.04760427, 117.35348248, -8342.39667343, 0.05, 2, 0, 73016, 24016, 2, 3)
    ops.uniaxialMaterial('LimitState', 43016, 41.91195803, 8.649e-05, 125.73587409, 0.00025948, 419.1195803, 0.00086495, -41.91195803, -8.649e-05, -125.73587409, -0.00025948, -419.1195803, -0.00086495, 0.4, 0.3, 0.003, 0.0, 0.0, 23016, 2)
    ops.limitCurve('ThreePoint', 13016, 3016, 0.0, 100.56109182, 0.02679397, 100.56109182, 0.0803819, 70.39276427, -2557.69595765, 0.05, 2, 0, 73016, 24016, 1, 3)
    ops.uniaxialMaterial('LimitState', 33016, 25.14027295, 5.188e-05, 75.42081886, 0.00015565, 251.40272954, 0.00051883, -25.14027295, -5.188e-05, -75.42081886, -0.00015565, -251.40272954, -0.00051883, 0.4, 0.3, 0.003, 0.0, 0.0, 13016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3016, 99999, 'P', 43016, 'Vy', 33016, 'Vz', 23016, 'My', 13016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173016, 73016, 173016, 3016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124016, 124016, 24016, 3016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173017, 14.5, 11.6, 7.725)
    ops.node(124017, 14.5, 11.6, 9.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3017, 173017, 124017, 0.1375, 26159882.08283219, 10899950.86784675, 0.00204719, 0.00078776, 0.00381276, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23017, 157.86196514, 0.00076756, 193.4683446, 0.01782619, 19.34683446, 0.07097675, -157.86196514, -0.00076756, -193.4683446, -0.01782619, -19.34683446, -0.07097675, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13017, 60.44470142, 0.00138408, 74.07823863, 0.01498372, 7.40782386, 0.04603312, -60.44470142, -0.00138408, -74.07823863, -0.01498372, -7.40782386, -0.04603312, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23017, 3017, 0.0, 184.16153097, 0.01535111, 184.16153097, 0.04605333, 128.91307168, -8751.39131805, 0.05, 2, 0, 73017, 24017, 2, 3)
    ops.uniaxialMaterial('LimitState', 43017, 46.04038274, 9.216e-05, 138.12114823, 0.00027647, 460.40382743, 0.00092158, -46.04038274, -9.216e-05, -138.12114823, -0.00027647, -460.40382743, -0.00092158, 0.4, 0.3, 0.003, 0.0, 0.0, 23017, 2)
    ops.limitCurve('ThreePoint', 13017, 3017, 0.0, 100.87331219, 0.02768162, 100.87331219, 0.08304486, 70.61131853, -2331.58313081, 0.05, 2, 0, 73017, 24017, 1, 3)
    ops.uniaxialMaterial('LimitState', 33017, 25.21832805, 5.048e-05, 75.65498414, 0.00015144, 252.18328047, 0.00050479, -25.21832805, -5.048e-05, -75.65498414, -0.00015144, -252.18328047, -0.00050479, 0.4, 0.3, 0.003, 0.0, 0.0, 13017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3017, 99999, 'P', 43017, 'Vy', 33017, 'Vz', 23017, 'My', 13017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173017, 73017, 173017, 3017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124017, 124017, 24017, 3017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173018, 18.35, 11.6, 7.8)
    ops.node(124018, 18.35, 11.6, 9.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3018, 173018, 124018, 0.125, 28086811.52729093, 11702838.13637122, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23018, 122.30621164, 0.00075514, 149.44688629, 0.01730827, 14.94468863, 0.08143777, -122.30621164, -0.00075514, -149.44688629, -0.01730827, -14.94468863, -0.08143777, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13018, 47.726376, 0.00125469, 58.31722029, 0.01462171, 5.83172203, 0.05324227, -47.726376, -0.00125469, -58.31722029, -0.01462171, -5.83172203, -0.05324227, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23018, 3018, 0.0, 185.3467858, 0.01510275, 185.3467858, 0.04530826, 129.74275006, -17245.38205562, 0.05, 2, 0, 73018, 24018, 2, 3)
    ops.uniaxialMaterial('LimitState', 43018, 46.33669645, 9.503e-05, 139.01008935, 0.00028508, 463.36696449, 0.00095027, -46.33669645, -9.503e-05, -139.01008935, -0.00028508, -463.36696449, -0.00095027, 0.4, 0.3, 0.003, 0.0, 0.0, 23018, 2)
    ops.limitCurve('ThreePoint', 13018, 3018, 0.0, 115.27490785, 0.02509389, 115.27490785, 0.07528168, 80.69243549, -4847.42382153, 0.05, 2, 0, 73018, 24018, 1, 3)
    ops.uniaxialMaterial('LimitState', 33018, 28.81872696, 5.91e-05, 86.45618088, 0.0001773, 288.18726961, 0.00059101, -28.81872696, -5.91e-05, -86.45618088, -0.0001773, -288.18726961, -0.00059101, 0.4, 0.3, 0.003, 0.0, 0.0, 13018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3018, 99999, 'P', 43018, 'Vy', 33018, 'Vz', 23018, 'My', 13018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173018, 73018, 173018, 3018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124018, 124018, 24018, 3018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173019, 0.0, 17.4, 7.8)
    ops.node(124019, 0.0, 17.4, 9.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3019, 173019, 124019, 0.0625, 27499623.79075484, 11458176.57948118, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23019, 35.75414474, 0.00130173, 43.74453692, 0.01899638, 4.37445369, 0.08281993, -35.75414474, -0.00130173, -43.74453692, -0.01899638, -4.37445369, -0.08281993, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13019, 39.84767187, 0.00130173, 48.75289189, 0.01899638, 4.87528919, 0.08281993, -39.84767187, -0.00130173, -48.75289189, -0.01899638, -4.87528919, -0.08281993, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23019, 3019, 0.0, 83.80387585, 0.02603466, 83.80387585, 0.07810397, 58.66271309, -8629.05415361, 0.05, 2, 0, 73019, 24019, 2, 3)
    ops.uniaxialMaterial('LimitState', 43019, 20.95096896, 8.777e-05, 62.85290688, 0.0002633, 209.50968961, 0.00087767, -20.95096896, -8.777e-05, -62.85290688, -0.0002633, -209.50968961, -0.00087767, 0.4, 0.3, 0.003, 0.0, 0.0, 23019, 2)
    ops.limitCurve('ThreePoint', 13019, 3019, 0.0, 83.80387585, 0.02603466, 83.80387585, 0.07810397, 58.66271309, -8629.05415361, 0.05, 2, 0, 73019, 24019, 1, 3)
    ops.uniaxialMaterial('LimitState', 33019, 20.95096896, 8.777e-05, 62.85290688, 0.0002633, 209.50968961, 0.00087767, -20.95096896, -8.777e-05, -62.85290688, -0.0002633, -209.50968961, -0.00087767, 0.4, 0.3, 0.003, 0.0, 0.0, 13019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3019, 99999, 'P', 43019, 'Vy', 33019, 'Vz', 23019, 'My', 13019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173019, 73019, 173019, 3019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124019, 124019, 24019, 3019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173020, 3.85, 17.4, 7.725)
    ops.node(124020, 3.85, 17.4, 9.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3020, 173020, 124020, 0.1, 27730299.67653756, 11554291.53189065, 0.00127345, 0.00146667, 0.00057292, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23020, 49.04905653, 0.00139339, 59.95218245, 0.01635038, 5.99521825, 0.0553548, -49.04905653, -0.00139339, -59.95218245, -0.01635038, -5.99521825, -0.0553548, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13020, 84.91577846, 0.00093189, 103.79172614, 0.01817487, 10.37917261, 0.07283035, -84.91577846, -0.00093189, -103.79172614, -0.01817487, -10.37917261, -0.07283035, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23020, 3020, 0.0, 87.48372446, 0.02786776, 87.48372446, 0.08360328, 61.23860712, -3277.68218067, 0.05, 2, 0, 73020, 24020, 2, 3)
    ops.uniaxialMaterial('LimitState', 43020, 21.87093111, 5.679e-05, 65.61279334, 0.00017036, 218.70931114, 0.00056787, -21.87093111, -5.679e-05, -65.61279334, -0.00017036, -218.70931114, -0.00056787, 0.4, 0.3, 0.003, 0.0, 0.0, 23020, 2)
    ops.limitCurve('ThreePoint', 13020, 3020, 0.0, 120.4477057, 0.01863789, 120.4477057, 0.05591366, 84.31339399, -7513.04671374, 0.05, 2, 0, 73020, 24020, 1, 3)
    ops.uniaxialMaterial('LimitState', 33020, 30.11192643, 7.818e-05, 90.33577928, 0.00023455, 301.11926426, 0.00078184, -30.11192643, -7.818e-05, -90.33577928, -0.00023455, -301.11926426, -0.00078184, 0.4, 0.3, 0.003, 0.0, 0.0, 13020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3020, 99999, 'P', 43020, 'Vy', 33020, 'Vz', 23020, 'My', 13020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173020, 73020, 173020, 3020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124020, 124020, 24020, 3020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173021, 7.7, 17.4, 7.7)
    ops.node(124021, 7.7, 17.4, 9.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3021, 173021, 124021, 0.0875, 27558125.32389544, 11482552.21828977, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23021, 46.25774974, 0.00133921, 56.56352278, 0.01685224, 5.65635228, 0.06551857, -46.25774974, -0.00133921, -56.56352278, -0.01685224, -5.65635228, -0.06551857, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13021, 80.53213206, 0.00099848, 98.47390138, 0.01829754, 9.84739014, 0.08131913, -80.53213206, -0.00099848, -98.47390138, -0.01829754, -9.84739014, -0.08131913, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23021, 3021, 0.0, 96.70935068, 0.02678414, 96.70935068, 0.08035242, 67.69654548, -5305.61251936, 0.05, 2, 0, 73021, 24021, 2, 3)
    ops.uniaxialMaterial('LimitState', 43021, 24.17733767, 7.219e-05, 72.53201301, 0.00021657, 241.7733767, 0.00072191, -24.17733767, -7.219e-05, -72.53201301, -0.00021657, -241.7733767, -0.00072191, 0.4, 0.3, 0.003, 0.0, 0.0, 23021, 2)
    ops.limitCurve('ThreePoint', 13021, 3021, 0.0, 118.04116835, 0.0199696, 118.04116835, 0.05990881, 82.62881785, -9786.93529531, 0.05, 2, 0, 73021, 24021, 1, 3)
    ops.uniaxialMaterial('LimitState', 33021, 29.51029209, 8.811e-05, 88.53087626, 0.00026434, 295.10292088, 0.00088115, -29.51029209, -8.811e-05, -88.53087626, -0.00026434, -295.10292088, -0.00088115, 0.4, 0.3, 0.003, 0.0, 0.0, 13021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3021, 99999, 'P', 43021, 'Vy', 33021, 'Vz', 23021, 'My', 13021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173021, 73021, 173021, 3021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124021, 124021, 24021, 3021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173022, 10.65, 17.4, 7.7)
    ops.node(124022, 10.65, 17.4, 9.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3022, 173022, 124022, 0.0875, 27419561.66541083, 11424817.36058785, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23022, 46.39371019, 0.00129561, 56.74671741, 0.01643436, 5.67467174, 0.06505091, -46.39371019, -0.00129561, -56.74671741, -0.01643436, -5.67467174, -0.06505091, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13022, 81.26429872, 0.00097626, 99.39886627, 0.01785794, 9.93988663, 0.08081509, -81.26429872, -0.00097626, -99.39886627, -0.01785794, -9.93988663, -0.08081509, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23022, 3022, 0.0, 94.21154357, 0.02591213, 94.21154357, 0.07773639, 65.9480805, -4927.76044731, 0.05, 2, 0, 73022, 24022, 2, 3)
    ops.uniaxialMaterial('LimitState', 43022, 23.55288589, 7.068e-05, 70.65865768, 0.00021205, 235.52885893, 0.00070682, -23.55288589, -7.068e-05, -70.65865768, -0.00021205, -235.52885893, -0.00070682, 0.4, 0.3, 0.003, 0.0, 0.0, 23022, 2)
    ops.limitCurve('ThreePoint', 13022, 3022, 0.0, 114.67939494, 0.01952513, 114.67939494, 0.05857539, 80.27557646, -9068.87920315, 0.05, 2, 0, 73022, 24022, 1, 3)
    ops.uniaxialMaterial('LimitState', 33022, 28.66984874, 8.604e-05, 86.00954621, 0.00025811, 286.69848736, 0.00086038, -28.66984874, -8.604e-05, -86.00954621, -0.00025811, -286.69848736, -0.00086038, 0.4, 0.3, 0.003, 0.0, 0.0, 13022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3022, 99999, 'P', 43022, 'Vy', 33022, 'Vz', 23022, 'My', 13022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173022, 73022, 173022, 3022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124022, 124022, 24022, 3022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173023, 14.5, 17.4, 7.725)
    ops.node(124023, 14.5, 17.4, 9.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3023, 173023, 124023, 0.1, 27843225.51297492, 11601343.96373955, 0.00127345, 0.00146667, 0.00057292, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23023, 49.12882776, 0.00141068, 60.03460716, 0.01692247, 6.00346072, 0.05595844, -49.12882776, -0.00141068, -60.03460716, -0.01692247, -6.00346072, -0.05595844, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13023, 85.15477872, 0.00093971, 104.05771765, 0.01882228, 10.40577177, 0.07352196, -85.15477872, -0.00093971, -104.05771765, -0.01882228, -10.40577177, -0.07352196, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23023, 3023, 0.0, 95.86286404, 0.0282136, 95.86286404, 0.08464079, 67.10400483, -3611.94367392, 0.05, 2, 0, 73023, 24023, 2, 3)
    ops.uniaxialMaterial('LimitState', 43023, 23.96571601, 6.197e-05, 71.89714803, 0.00018592, 239.65716009, 0.00061973, -23.96571601, -6.197e-05, -71.89714803, -0.00018592, -239.65716009, -0.00061973, 0.4, 0.3, 0.003, 0.0, 0.0, 23023, 2)
    ops.limitCurve('ThreePoint', 13023, 3023, 0.0, 124.7873432, 0.01879413, 124.7873432, 0.0563824, 87.35114024, -8323.87588365, 0.05, 2, 0, 73023, 24023, 1, 3)
    ops.uniaxialMaterial('LimitState', 33023, 31.1968358, 8.067e-05, 93.5905074, 0.00024202, 311.96835799, 0.00080672, -31.1968358, -8.067e-05, -93.5905074, -0.00024202, -311.96835799, -0.00080672, 0.4, 0.3, 0.003, 0.0, 0.0, 13023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3023, 99999, 'P', 43023, 'Vy', 33023, 'Vz', 23023, 'My', 13023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173023, 73023, 173023, 3023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124023, 124023, 24023, 3023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173024, 18.35, 17.4, 7.8)
    ops.node(124024, 18.35, 17.4, 9.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3024, 173024, 124024, 0.0625, 29385691.93850982, 12244038.30771242, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23024, 37.06988368, 0.00123961, 45.14650735, 0.01855663, 4.51465073, 0.0829875, -37.06988368, -0.00123961, -45.14650735, -0.01855663, -4.51465073, -0.0829875, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13024, 41.64209885, 0.00123961, 50.7148967, 0.01855663, 5.07148967, 0.0829875, -41.64209885, -0.00123961, -50.7148967, -0.01855663, -5.07148967, -0.0829875, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23024, 3024, 0.0, 88.23998331, 0.02479215, 88.23998331, 0.07437645, 61.76798832, -8959.72705207, 0.05, 2, 0, 73024, 24024, 2, 3)
    ops.uniaxialMaterial('LimitState', 43024, 22.05999583, 8.648e-05, 66.17998748, 0.00025944, 220.59995827, 0.00086481, -22.05999583, -8.648e-05, -66.17998748, -0.00025944, -220.59995827, -0.00086481, 0.4, 0.3, 0.003, 0.0, 0.0, 23024, 2)
    ops.limitCurve('ThreePoint', 13024, 3024, 0.0, 88.23998331, 0.02479215, 88.23998331, 0.07437645, 61.76798832, -8959.72705207, 0.05, 2, 0, 73024, 24024, 1, 3)
    ops.uniaxialMaterial('LimitState', 33024, 22.05999583, 8.648e-05, 66.17998748, 0.00025944, 220.59995827, 0.00086481, -22.05999583, -8.648e-05, -66.17998748, -0.00025944, -220.59995827, -0.00086481, 0.4, 0.3, 0.003, 0.0, 0.0, 13024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3024, 99999, 'P', 43024, 'Vy', 33024, 'Vz', 23024, 'My', 13024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173024, 73024, 173024, 3024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124024, 124024, 24024, 3024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170003, 7.7, 0.0, 0.0)
    ops.node(124025, 7.7, 0.0, 1.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4063, 170003, 124025, 0.1925, 26746104.96671351, 11144210.40279729, 0.00475217, 0.00533786, 0.00216161, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24063, 340.47087314, 0.00089754, 413.83955434, 0.03744973, 41.38395543, 0.09270951, -340.47087314, -0.00089754, -413.83955434, -0.03744973, -41.38395543, -0.09270951, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14063, 392.75948844, 0.0007519, 477.39593745, 0.04375915, 47.73959375, 0.1250321, -392.75948844, -0.0007519, -477.39593745, -0.04375915, -47.73959375, -0.1250321, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24063, 4063, 0.0, 381.3733474, 0.01795083, 381.3733474, 0.05385249, 266.96134318, -18060.94521706, 0.05, 2, 0, 70003, 24025, 2, 3)
    ops.uniaxialMaterial('LimitState', 44063, 95.34333685, 6.667e-05, 286.03001055, 0.0002, 953.4333685, 0.00066666, -95.34333685, -6.667e-05, -286.03001055, -0.0002, -953.4333685, -0.00066666, 0.4, 0.3, 0.003, 0.0, 0.0, 24063, 2)
    ops.limitCurve('ThreePoint', 14063, 4063, 0.0, 508.44024784, 0.015038, 508.44024784, 0.045114, 355.90817349, -36855.22225054, 0.05, 2, 0, 70003, 24025, 1, 3)
    ops.uniaxialMaterial('LimitState', 34063, 127.11006196, 8.888e-05, 381.33018588, 0.00026663, 1271.1006196, 0.00088877, -127.11006196, -8.888e-05, -381.33018588, -0.00026663, -1271.1006196, -0.00088877, 0.4, 0.3, 0.003, 0.0, 0.0, 14063, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4063, 99999, 'P', 44063, 'Vy', 34063, 'Vz', 24063, 'My', 14063, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170003, 70003, 170003, 4063, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124025, 124025, 24025, 4063, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174025, 7.7, 0.0, 1.5)
    ops.node(121003, 7.7, 0.0, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4064, 174025, 121003, 0.1925, 27334418.72312696, 11389341.13463623, 0.00475217, 0.00533786, 0.00216161, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24064, 176.44724688, 0.00083374, 214.52538451, 0.03533927, 21.45253845, 0.09332933, -176.44724688, -0.00083374, -214.52538451, -0.03533927, -21.45253845, -0.09332933, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14064, 243.75593681, 0.00071292, 296.3596032, 0.04131208, 29.63596032, 0.12660058, -243.75593681, -0.00071292, -296.3596032, -0.04131208, -29.63596032, -0.12660058, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24064, 4064, 0.0, 392.39401093, 0.01667482, 392.39401093, 0.05002447, 274.67580765, -20658.45123719, 0.05, 2, 0, 74025, 21003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44064, 98.09850273, 6.712e-05, 294.2955082, 0.00020135, 980.98502733, 0.00067116, -98.09850273, -6.712e-05, -294.2955082, -0.00020135, -980.98502733, -0.00067116, 0.4, 0.3, 0.003, 0.0, 0.0, 24064, 2)
    ops.limitCurve('ThreePoint', 14064, 4064, 0.0, 525.10361188, 0.01425847, 525.10361188, 0.0427754, 367.57252832, -43115.46383163, 0.05, 2, 0, 74025, 21003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34064, 131.27590297, 8.981e-05, 393.82770891, 0.00026944, 1312.7590297, 0.00089815, -131.27590297, -8.981e-05, -393.82770891, -0.00026944, -1312.7590297, -0.00089815, 0.4, 0.3, 0.003, 0.0, 0.0, 14064, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4064, 99999, 'P', 44064, 'Vy', 34064, 'Vz', 24064, 'My', 14064, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174025, 74025, 174025, 4064, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121003, 121003, 21003, 4064, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170004, 10.65, 0.0, 0.0)
    ops.node(124026, 10.65, 0.0, 1.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4065, 170004, 124026, 0.1925, 26333446.51420285, 10972269.38091785, 0.00475217, 0.00533786, 0.00216161, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24065, 336.96732801, 0.00090077, 409.73933835, 0.0376241, 40.97393384, 0.09202242, -336.96732801, -0.00090077, -409.73933835, -0.0376241, -40.97393384, -0.09202242, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14065, 389.30247972, 0.00075306, 473.37687426, 0.04396168, 47.33768743, 0.12396765, -389.30247972, -0.00075306, -473.37687426, -0.04396168, -47.33768743, -0.12396765, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24065, 4065, 0.0, 382.28849617, 0.01801535, 382.28849617, 0.05404604, 267.60194732, -18803.30548623, 0.05, 2, 0, 70004, 24026, 2, 3)
    ops.uniaxialMaterial('LimitState', 44065, 95.57212404, 6.787e-05, 286.71637213, 0.00020362, 955.72124043, 0.00067873, -95.57212404, -6.787e-05, -286.71637213, -0.00020362, -955.72124043, -0.00067873, 0.4, 0.3, 0.003, 0.0, 0.0, 24065, 2)
    ops.limitCurve('ThreePoint', 14065, 4065, 0.0, 511.7080618, 0.01506125, 511.7080618, 0.04518374, 358.19564326, -38523.33731579, 0.05, 2, 0, 70004, 24026, 1, 3)
    ops.uniaxialMaterial('LimitState', 34065, 127.92701545, 9.085e-05, 383.78104635, 0.00027255, 1279.2701545, 0.0009085, -127.92701545, -9.085e-05, -383.78104635, -0.00027255, -1279.2701545, -0.0009085, 0.4, 0.3, 0.003, 0.0, 0.0, 14065, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4065, 99999, 'P', 44065, 'Vy', 34065, 'Vz', 24065, 'My', 14065, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170004, 70004, 170004, 4065, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124026, 124026, 24026, 4065, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174026, 10.65, 0.0, 1.5)
    ops.node(121004, 10.65, 0.0, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4066, 174026, 121004, 0.1925, 28272746.168736, 11780310.90364, 0.00475217, 0.00533786, 0.00216161, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24066, 178.61908828, 0.00083187, 216.8548261, 0.03508581, 21.68548261, 0.09462104, -178.61908828, -0.00083187, -216.8548261, -0.03508581, -21.68548261, -0.09462104, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14066, 246.92224235, 0.0007122, 299.77915821, 0.04101534, 29.97791582, 0.12857639, -246.92224235, -0.0007122, -299.77915821, -0.04101534, -29.97791582, -0.12857639, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24066, 4066, 0.0, 401.63479768, 0.01663733, 401.63479768, 0.049912, 281.14435838, -20642.67223635, 0.05, 2, 0, 74026, 21004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44066, 100.40869942, 6.642e-05, 301.22609826, 0.00019925, 1004.08699421, 0.00066416, -100.40869942, -6.642e-05, -301.22609826, -0.00019925, -1004.08699421, -0.00066416, 0.4, 0.3, 0.003, 0.0, 0.0, 24066, 2)
    ops.limitCurve('ThreePoint', 14066, 4066, 0.0, 535.37420426, 0.01424405, 535.37420426, 0.04273214, 374.76194298, -43079.64309467, 0.05, 2, 0, 74026, 21004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34066, 133.84355106, 8.853e-05, 401.53065319, 0.0002656, 1338.43551064, 0.00088532, -133.84355106, -8.853e-05, -401.53065319, -0.0002656, -1338.43551064, -0.00088532, 0.4, 0.3, 0.003, 0.0, 0.0, 14066, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4066, 99999, 'P', 44066, 'Vy', 34066, 'Vz', 24066, 'My', 14066, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174026, 74026, 174026, 4066, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121004, 121004, 21004, 4066, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171003, 7.7, 0.0, 2.7)
    ops.node(124027, 7.7, 0.0, 3.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4068, 171003, 124027, 0.1925, 28076030.86234329, 11698346.19264304, 0.00475217, 0.00533786, 0.00216161, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24068, 203.13177031, 0.00083989, 247.02532805, 0.03650778, 24.7025328, 0.09814272, -203.13177031, -0.00083989, -247.02532805, -0.03650778, -24.7025328, -0.09814272, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14068, 266.12389827, 0.00071612, 323.62905699, 0.04268291, 32.3629057, 0.1333321, -266.12389827, -0.00071612, -323.62905699, -0.04268291, -32.3629057, -0.1333321, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24068, 4068, 0.0, 388.42616241, 0.01679771, 388.42616241, 0.05039313, 271.89831368, -22343.37566623, 0.05, 2, 0, 71003, 24027, 2, 3)
    ops.uniaxialMaterial('LimitState', 44068, 97.1065406, 6.468e-05, 291.31962181, 0.00019405, 971.06540602, 0.00064682, -97.1065406, -6.468e-05, -291.31962181, -0.00019405, -971.06540602, -0.00064682, 0.4, 0.3, 0.003, 0.0, 0.0, 24068, 2)
    ops.limitCurve('ThreePoint', 14068, 4068, 0.0, 518.76629663, 0.01432237, 518.76629663, 0.04296712, 363.13640764, -47679.88036329, 0.05, 2, 0, 71003, 24027, 1, 3)
    ops.uniaxialMaterial('LimitState', 34068, 129.69157416, 8.639e-05, 389.07472247, 0.00025916, 1296.91574157, 0.00086387, -129.69157416, -8.639e-05, -389.07472247, -0.00025916, -1296.91574157, -0.00086387, 0.4, 0.3, 0.003, 0.0, 0.0, 14068, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4068, 99999, 'P', 44068, 'Vy', 34068, 'Vz', 24068, 'My', 14068, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171003, 71003, 171003, 4068, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124027, 124027, 24027, 4068, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174027, 7.7, 0.0, 4.075)
    ops.node(122003, 7.7, 0.0, 4.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4069, 174027, 122003, 0.1925, 27086421.4415645, 11286008.93398521, 0.00475217, 0.00533786, 0.00216161, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24069, 165.21857984, 0.00083987, 201.43992104, 0.03651524, 20.1439921, 0.09849819, -165.21857984, -0.00083987, -201.43992104, -0.03651524, -20.1439921, -0.09849819, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14069, 227.61551335, 0.0007152, 277.51631252, 0.04269079, 27.75163125, 0.1338518, -227.61551335, -0.0007152, -277.51631252, -0.04269079, -27.75163125, -0.1338518, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24069, 4069, 0.0, 371.0792646, 0.01679745, 371.0792646, 0.05039235, 259.75548522, -23960.48004676, 0.05, 2, 0, 74027, 22003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44069, 92.76981615, 6.405e-05, 278.30944845, 0.00019215, 927.6981615, 0.00064051, -92.76981615, -6.405e-05, -278.30944845, -0.00019215, -927.6981615, -0.00064051, 0.4, 0.3, 0.003, 0.0, 0.0, 24069, 2)
    ops.limitCurve('ThreePoint', 14069, 4069, 0.0, 498.09434757, 0.01430405, 498.09434757, 0.04291216, 348.6660433, -51941.22681641, 0.05, 2, 0, 74027, 22003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34069, 124.52358689, 8.597e-05, 373.57076068, 0.00025792, 1245.23586892, 0.00085975, -124.52358689, -8.597e-05, -373.57076068, -0.00025792, -1245.23586892, -0.00085975, 0.4, 0.3, 0.003, 0.0, 0.0, 14069, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4069, 99999, 'P', 44069, 'Vy', 34069, 'Vz', 24069, 'My', 14069, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174027, 74027, 174027, 4069, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122003, 122003, 22003, 4069, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171004, 10.65, 0.0, 2.7)
    ops.node(124028, 10.65, 0.0, 3.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4070, 171004, 124028, 0.1925, 27562041.95944459, 11484184.14976858, 0.00475217, 0.00533786, 0.00216161, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24070, 203.09126291, 0.00085549, 247.19183253, 0.03643989, 24.71918325, 0.09735019, -203.09126291, -0.00085549, -247.19183253, -0.03643989, -24.71918325, -0.09735019, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14070, 266.71570426, 0.00072502, 324.63210261, 0.04259357, 32.46321026, 0.13217699, -266.71570426, -0.00072502, -324.63210261, -0.04259357, -32.46321026, -0.13217699, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24070, 4070, 0.0, 379.47122709, 0.01710985, 379.47122709, 0.05132955, 265.62985896, -21602.86176726, 0.05, 2, 0, 71004, 24028, 2, 3)
    ops.uniaxialMaterial('LimitState', 44070, 94.86780677, 6.437e-05, 284.60342032, 0.00019311, 948.67806772, 0.00064369, -94.86780677, -6.437e-05, -284.60342032, -0.00019311, -948.67806772, -0.00064369, 0.4, 0.3, 0.003, 0.0, 0.0, 24070, 2)
    ops.limitCurve('ThreePoint', 14070, 4070, 0.0, 507.00526137, 0.01450043, 507.00526137, 0.04350128, 354.90368296, -45981.07409658, 0.05, 2, 0, 71004, 24028, 1, 3)
    ops.uniaxialMaterial('LimitState', 34070, 126.75131534, 8.6e-05, 380.25394602, 0.00025801, 1267.51315341, 0.00086003, -126.75131534, -8.6e-05, -380.25394602, -0.00025801, -1267.51315341, -0.00086003, 0.4, 0.3, 0.003, 0.0, 0.0, 14070, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4070, 99999, 'P', 44070, 'Vy', 34070, 'Vz', 24070, 'My', 14070, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171004, 71004, 171004, 4070, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124028, 124028, 24028, 4070, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174028, 10.65, 0.0, 4.075)
    ops.node(122004, 10.65, 0.0, 4.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4071, 174028, 122004, 0.1925, 28044937.45338374, 11685390.60557656, 0.00475217, 0.00533786, 0.00216161, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24071, 160.83513022, 0.00079834, 195.77107263, 0.03625943, 19.57710726, 0.09947941, -160.83513022, -0.00079834, -195.77107263, -0.03625943, -19.57710726, -0.09947941, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14071, 221.46697452, 0.00068923, 269.57311562, 0.0424127, 26.95731156, 0.13539306, -221.46697452, -0.00068923, -269.57311562, -0.0424127, -26.95731156, -0.13539306, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24071, 4071, 0.0, 379.68984201, 0.01596686, 379.68984201, 0.04790059, 265.78288941, -23798.30267859, 0.05, 2, 0, 74028, 22004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44071, 94.9224605, 6.33e-05, 284.76738151, 0.00018989, 949.22460502, 0.00063297, -94.9224605, -6.33e-05, -284.76738151, -0.00018989, -949.22460502, -0.00063297, 0.4, 0.3, 0.003, 0.0, 0.0, 24071, 2)
    ops.limitCurve('ThreePoint', 14071, 4071, 0.0, 507.36010074, 0.01378463, 507.36010074, 0.04135389, 355.15207052, -51566.04342106, 0.05, 2, 0, 74028, 22004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34071, 126.84002519, 8.458e-05, 380.52007556, 0.00025374, 1268.40025185, 0.00084581, -126.84002519, -8.458e-05, -380.52007556, -0.00025374, -1268.40025185, -0.00084581, 0.4, 0.3, 0.003, 0.0, 0.0, 14071, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4071, 99999, 'P', 44071, 'Vy', 34071, 'Vz', 24071, 'My', 14071, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174028, 74028, 174028, 4071, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122004, 122004, 22004, 4071, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172003, 7.7, 0.0, 5.2)
    ops.node(124029, 7.7, 0.0, 6.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4073, 172003, 124029, 0.125, 28085150.79333648, 11702146.1638902, 0.00178813, 0.00286458, 0.00071615, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24073, 126.92166866, 0.00106219, 154.34940212, 0.03955491, 15.43494021, 0.10632215, -126.92166866, -0.00106219, -154.34940212, -0.03955491, -15.43494021, -0.10632215, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14073, 216.95685885, 0.00073982, 263.84116916, 0.05052537, 26.38411692, 0.15052537, -216.95685885, -0.00073982, -263.84116916, -0.05052537, -26.38411692, -0.15052537, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24073, 4073, 0.0, 225.20538824, 0.02124381, 225.20538824, 0.06373144, 157.64377177, -16616.57428538, 0.05, 2, 0, 72003, 24029, 2, 3)
    ops.uniaxialMaterial('LimitState', 44073, 56.30134706, 5.773e-05, 168.90404118, 0.0001732, 563.0134706, 0.00057734, -56.30134706, -5.773e-05, -168.90404118, -0.0001732, -563.0134706, -0.00057734, 0.4, 0.3, 0.003, 0.0, 0.0, 24073, 2)
    ops.limitCurve('ThreePoint', 14073, 4073, 0.0, 409.59662975, 0.01479639, 409.59662975, 0.04438917, 286.71764083, -55012.35972543, 0.05, 2, 0, 72003, 24029, 1, 3)
    ops.uniaxialMaterial('LimitState', 34073, 102.39915744, 0.00010501, 307.19747232, 0.00031502, 1023.99157439, 0.00105006, -102.39915744, -0.00010501, -307.19747232, -0.00031502, -1023.99157439, -0.00105006, 0.4, 0.3, 0.003, 0.0, 0.0, 14073, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4073, 99999, 'P', 44073, 'Vy', 34073, 'Vz', 24073, 'My', 14073, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172003, 72003, 172003, 4073, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124029, 124029, 24029, 4073, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174029, 7.7, 0.0, 6.5)
    ops.node(123003, 7.7, 0.0, 7.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4074, 174029, 123003, 0.125, 26955228.12887306, 11231345.05369711, 0.00178813, 0.00286458, 0.00071615, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24074, 79.93181027, 0.00107106, 97.5469183, 0.03843449, 9.75469183, 0.10678851, -79.93181027, -0.00107106, -97.5469183, -0.03843449, -9.75469183, -0.10678851, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14074, 156.71969909, 0.00073879, 191.25706814, 0.04906376, 19.12570681, 0.14906376, -156.71969909, -0.00073879, -191.25706814, -0.04906376, -19.12570681, -0.14906376, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24074, 4074, 0.0, 213.18584118, 0.02142127, 213.18584118, 0.0642638, 149.23008883, -19187.60903152, 0.05, 2, 0, 74029, 23003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44074, 53.2964603, 5.694e-05, 159.88938089, 0.00017083, 532.96460296, 0.00056944, -53.2964603, -5.694e-05, -159.88938089, -0.00017083, -532.96460296, -0.00056944, 0.4, 0.3, 0.003, 0.0, 0.0, 24074, 2)
    ops.limitCurve('ThreePoint', 14074, 4074, 0.0, 389.4590789, 0.01477581, 389.4590789, 0.04432743, 272.62135523, -65914.98920874, 0.05, 2, 0, 74029, 23003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34074, 97.36476973, 0.00010403, 292.09430918, 0.00031208, 973.64769726, 0.00104028, -97.36476973, -0.00010403, -292.09430918, -0.00031208, -973.64769726, -0.00104028, 0.4, 0.3, 0.003, 0.0, 0.0, 14074, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4074, 99999, 'P', 44074, 'Vy', 34074, 'Vz', 24074, 'My', 14074, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174029, 74029, 174029, 4074, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123003, 123003, 23003, 4074, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172004, 10.65, 0.0, 5.2)
    ops.node(124030, 10.65, 0.0, 6.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4075, 172004, 124030, 0.125, 28738690.54415097, 11974454.39339624, 0.00178813, 0.00286458, 0.00071615, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24075, 122.68245244, 0.00106731, 149.0095136, 0.03934616, 14.90095136, 0.10703191, -122.68245244, -0.00106731, -149.0095136, -0.03934616, -14.90095136, -0.10703191, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14075, 213.54456293, 0.000735, 259.37019371, 0.05024395, 25.93701937, 0.15024395, -213.54456293, -0.000735, -259.37019371, -0.05024395, -25.93701937, -0.15024395, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24075, 4075, 0.0, 226.74372697, 0.02134627, 226.74372697, 0.06403882, 158.72060888, -16309.75418406, 0.05, 2, 0, 72004, 24030, 2, 3)
    ops.uniaxialMaterial('LimitState', 44075, 56.68593174, 5.681e-05, 170.05779523, 0.00017042, 566.85931742, 0.00056807, -56.68593174, -5.681e-05, -170.05779523, -0.00017042, -566.85931742, -0.00056807, 0.4, 0.3, 0.003, 0.0, 0.0, 24075, 2)
    ops.limitCurve('ThreePoint', 14075, 4075, 0.0, 411.34709161, 0.01470009, 411.34709161, 0.04410026, 287.94296413, -53896.33851583, 0.05, 2, 0, 72004, 24030, 1, 3)
    ops.uniaxialMaterial('LimitState', 34075, 102.8367729, 0.00010306, 308.51031871, 0.00030917, 1028.36772902, 0.00103056, -102.8367729, -0.00010306, -308.51031871, -0.00030917, -1028.36772902, -0.00103056, 0.4, 0.3, 0.003, 0.0, 0.0, 14075, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4075, 99999, 'P', 44075, 'Vy', 34075, 'Vz', 24075, 'My', 14075, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172004, 72004, 172004, 4075, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124030, 124030, 24030, 4075, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174030, 10.65, 0.0, 6.5)
    ops.node(123004, 10.65, 0.0, 7.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4076, 174030, 123004, 0.125, 28380725.09280906, 11825302.12200378, 0.00178813, 0.00286458, 0.00071615, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24076, 78.34723347, 0.00102381, 95.36266908, 0.03863105, 9.53626691, 0.10875112, -78.34723347, -0.00102381, -95.36266908, -0.03863105, -9.53626691, -0.10875112, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14076, 153.91936278, 0.00071572, 187.34753748, 0.04935602, 18.73475375, 0.14935602, -153.91936278, -0.00071572, -187.34753748, -0.04935602, -18.73475375, -0.14935602, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24076, 4076, 0.0, 225.65944147, 0.02047613, 225.65944147, 0.06142838, 157.96160903, -20748.47083964, 0.05, 2, 0, 74030, 23004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44076, 56.41486037, 5.725e-05, 169.2445811, 0.00017174, 564.14860367, 0.00057248, -56.41486037, -5.725e-05, -169.2445811, -0.00017174, -564.14860367, -0.00057248, 0.4, 0.3, 0.003, 0.0, 0.0, 24076, 2)
    ops.limitCurve('ThreePoint', 14076, 4076, 0.0, 411.58238462, 0.01431445, 411.58238462, 0.04294335, 288.10766923, -71709.90179296, 0.05, 2, 0, 74030, 23004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34076, 102.89559616, 0.00010442, 308.68678847, 0.00031325, 1028.95596155, 0.00104416, -102.89559616, -0.00010442, -308.68678847, -0.00031325, -1028.95596155, -0.00104416, 0.4, 0.3, 0.003, 0.0, 0.0, 14076, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4076, 99999, 'P', 44076, 'Vy', 34076, 'Vz', 24076, 'My', 14076, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174030, 74030, 174030, 4076, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123004, 123004, 23004, 4076, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173003, 7.7, 0.0, 7.7)
    ops.node(124031, 7.7, 0.0, 8.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4078, 173003, 124031, 0.125, 26829685.76651913, 11179035.73604964, 0.00178813, 0.00286458, 0.00071615, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24078, 67.68453889, 0.00101385, 82.84104094, 0.01567009, 8.28410409, 0.04869908, -67.68453889, -0.00101385, -82.84104094, -0.01567009, -8.28410409, -0.04869908, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14078, 165.92705363, 0.0007178, 203.0828616, 0.01866277, 20.30828616, 0.07205145, -165.92705363, -0.0007178, -203.0828616, -0.01866277, -20.30828616, -0.07205145, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24078, 4078, 0.0, 119.47012289, 0.02027698, 119.47012289, 0.06083094, 83.62908602, -5197.20583348, 0.05, 2, 0, 73003, 24031, 2, 3)
    ops.uniaxialMaterial('LimitState', 44078, 29.86753072, 3.206e-05, 89.60259217, 9.618e-05, 298.67530723, 0.00032061, -29.86753072, -3.206e-05, -89.60259217, -9.618e-05, -298.67530723, -0.00032061, 0.4, 0.3, 0.003, 0.0, 0.0, 24078, 2)
    ops.limitCurve('ThreePoint', 14078, 4078, 0.0, 210.69993772, 0.01435608, 210.69993772, 0.04306823, 147.4899564, -16822.8248942, 0.05, 2, 0, 73003, 24031, 1, 3)
    ops.uniaxialMaterial('LimitState', 34078, 52.67498443, 5.654e-05, 158.02495329, 0.00016963, 526.7498443, 0.00056543, -52.67498443, -5.654e-05, -158.02495329, -0.00016963, -526.7498443, -0.00056543, 0.4, 0.3, 0.003, 0.0, 0.0, 14078, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4078, 99999, 'P', 44078, 'Vy', 34078, 'Vz', 24078, 'My', 14078, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173003, 73003, 173003, 4078, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124031, 124031, 24031, 4078, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174031, 7.7, 0.0, 8.95)
    ops.node(124003, 7.7, 0.0, 9.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4079, 174031, 124003, 0.125, 28685284.4072923, 11952201.83637179, 0.00178813, 0.00286458, 0.00071615, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24079, 64.55749674, 0.00098337, 78.80435887, 0.01553372, 7.88043589, 0.05049775, -64.55749674, -0.00098337, -78.80435887, -0.01553372, -7.88043589, -0.05049775, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14079, 159.18218004, 0.00070198, 194.31127714, 0.01851728, 19.43112771, 0.07503381, -159.18218004, -0.00070198, -194.31127714, -0.01851728, -19.43112771, -0.07503381, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24079, 4079, 0.0, 121.54180051, 0.0196674, 121.54180051, 0.05900221, 85.07926036, -9519.2704655, 0.05, 2, 0, 74031, 24003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44079, 30.38545013, 3.051e-05, 91.15635038, 9.152e-05, 303.85450128, 0.00030507, -30.38545013, -3.051e-05, -91.15635038, -9.152e-05, -303.85450128, -0.00030507, 0.4, 0.3, 0.003, 0.0, 0.0, 24079, 2)
    ops.limitCurve('ThreePoint', 14079, 4079, 0.0, 214.29487546, 0.01403964, 214.29487546, 0.04211893, 150.00641282, -34595.71389446, 0.05, 2, 0, 74031, 24003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34079, 53.57371887, 5.379e-05, 160.7211566, 0.00016136, 535.73718866, 0.00053788, -53.57371887, -5.379e-05, -160.7211566, -0.00016136, -535.73718866, -0.00053788, 0.4, 0.3, 0.003, 0.0, 0.0, 14079, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4079, 99999, 'P', 44079, 'Vy', 34079, 'Vz', 24079, 'My', 14079, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174031, 74031, 174031, 4079, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124003, 124003, 24003, 4079, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173004, 10.65, 0.0, 7.7)
    ops.node(124032, 10.65, 0.0, 8.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4080, 173004, 124032, 0.125, 28300095.56479199, 11791706.48532999, 0.00178813, 0.00286458, 0.00071615, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24080, 66.32025746, 0.00101414, 80.91995338, 0.01558349, 8.09199534, 0.04906508, -66.32025746, -0.00101414, -80.91995338, -0.01558349, -8.09199534, -0.04906508, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14080, 162.75328932, 0.00071055, 198.58168663, 0.01854912, 19.85816866, 0.0726694, -162.75328932, -0.00071055, -198.58168663, -0.01854912, -19.85816866, -0.0726694, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24080, 4080, 0.0, 126.54604167, 0.02028273, 126.54604167, 0.06084818, 88.58222917, -5077.52981381, 0.05, 2, 0, 73004, 24032, 2, 3)
    ops.uniaxialMaterial('LimitState', 44080, 31.63651042, 3.22e-05, 94.90953125, 9.659e-05, 316.36510417, 0.00032195, -31.63651042, -3.22e-05, -94.90953125, -9.659e-05, -316.36510417, -0.00032195, 0.4, 0.3, 0.003, 0.0, 0.0, 24080, 2)
    ops.limitCurve('ThreePoint', 14080, 4080, 0.0, 219.68051039, 0.01421097, 219.68051039, 0.0426329, 153.77635728, -16392.47751656, 0.05, 2, 0, 73004, 24032, 1, 3)
    ops.uniaxialMaterial('LimitState', 34080, 54.9201276, 5.589e-05, 164.7603828, 0.00016767, 549.20127598, 0.0005589, -54.9201276, -5.589e-05, -164.7603828, -0.00016767, -549.20127598, -0.0005589, 0.4, 0.3, 0.003, 0.0, 0.0, 14080, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4080, 99999, 'P', 44080, 'Vy', 34080, 'Vz', 24080, 'My', 14080, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173004, 73004, 173004, 4080, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124032, 124032, 24032, 4080, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174032, 10.65, 0.0, 8.95)
    ops.node(124004, 10.65, 0.0, 9.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4081, 174032, 124004, 0.125, 28441322.78929318, 11850551.16220549, 0.00178813, 0.00286458, 0.00071615, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24081, 63.92968212, 0.00097771, 78.08602733, 0.0156295, 7.80860273, 0.05056669, -63.92968212, -0.00097771, -78.08602733, -0.0156295, -7.80860273, -0.05056669, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14081, 157.6741484, 0.00069899, 192.58891101, 0.0186385, 19.2588911, 0.07511163, -157.6741484, -0.00069899, -192.58891101, -0.0186385, -19.2588911, -0.07511163, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24081, 4081, 0.0, 120.73469216, 0.01955419, 120.73469216, 0.05866256, 84.51428451, -9748.07328112, 0.05, 2, 0, 74032, 24004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44081, 30.18367304, 3.056e-05, 90.55101912, 9.169e-05, 301.83673039, 0.00030564, -30.18367304, -3.056e-05, -90.55101912, -9.169e-05, -301.83673039, -0.00030564, 0.4, 0.3, 0.003, 0.0, 0.0, 24081, 2)
    ops.limitCurve('ThreePoint', 14081, 4081, 0.0, 213.6977671, 0.01397975, 213.6977671, 0.04193924, 149.58843697, -35468.33818357, 0.05, 2, 0, 74032, 24004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34081, 53.42444178, 5.41e-05, 160.27332533, 0.00016229, 534.24441775, 0.00054098, -53.42444178, -5.41e-05, -160.27332533, -0.00016229, -534.24441775, -0.00054098, 0.4, 0.3, 0.003, 0.0, 0.0, 14081, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4081, 99999, 'P', 44081, 'Vy', 34081, 'Vz', 24081, 'My', 14081, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174032, 74032, 174032, 4081, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124004, 124004, 24004, 4081, '-orient', 0, 0, 1, 0, 1, 0)
