import openseespy.opensees as ops


def add_columns() -> None:
    """Add components of all columns to ops domain (plastic hinges, column elements and nodes)
    """
    # Create elastic column element nodes
    ops.node(170001, 0.0, 0.0, 0.0)
    ops.node(121001, 0.0, 0.0, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1, 170001, 121001, 0.0625, 29549137.33101903, 12312140.55459126, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20001, 38.81656656, 0.0007979, 46.69706716, 0.03519381, 4.66970672, 0.10475056, -38.81656656, -0.0007979, -46.69706716, -0.03519381, -4.66970672, -0.10475056, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10001, 38.81656656, 0.0007979, 46.69706716, 0.03519381, 4.66970672, 0.10475056, -38.81656656, -0.0007979, -46.69706716, -0.03519381, -4.66970672, -0.10475056, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20001, 1, 0.0, 89.9779818, 0.01595802, 89.9779818, 0.04787407, 62.98458726, -1530.63735798, 0.05, 2, 0, 70001, 21001, 2, 3)
    ops.uniaxialMaterial('LimitState', 40001, 22.49449545, 9.12e-05, 67.48348635, 0.00027361, 224.94495449, 0.00091205, -22.49449545, -9.12e-05, -67.48348635, -0.00027361, -224.94495449, -0.00091205, 0.4, 0.3, 0.003, 0.0, 0.0, 20001, 2)
    ops.limitCurve('ThreePoint', 10001, 1, 0.0, 89.9779818, 0.01595802, 89.9779818, 0.04787407, 62.98458726, -1530.63735798, 0.05, 2, 0, 70001, 21001, 1, 3)
    ops.uniaxialMaterial('LimitState', 30001, 22.49449545, 9.12e-05, 67.48348635, 0.00027361, 224.94495449, 0.00091205, -22.49449545, -9.12e-05, -67.48348635, -0.00027361, -224.94495449, -0.00091205, 0.4, 0.3, 0.003, 0.0, 0.0, 10001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1, 99999, 'P', 40001, 'Vy', 30001, 'Vz', 20001, 'My', 10001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170001, 70001, 170001, 1, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121001, 121001, 21001, 1, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170002, 7.45, 0.0, 0.0)
    ops.node(121002, 7.45, 0.0, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2, 170002, 121002, 0.09, 31441526.12307622, 13100635.88461509, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20002, 58.43908183, 0.00066359, 70.16730018, 0.04193033, 7.01673002, 0.13707158, -58.43908183, -0.00066359, -70.16730018, -0.04193033, -7.01673002, -0.13707158, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10002, 61.55102973, 0.00066359, 73.9037891, 0.04193033, 7.39037891, 0.13707158, -61.55102973, -0.00066359, -73.9037891, -0.04193033, -7.39037891, -0.13707158, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20002, 2, 0.0, 146.04268833, 0.01327179, 146.04268833, 0.03981538, 102.22988183, -2848.690414, 0.05, 2, 0, 70002, 21002, 2, 3)
    ops.uniaxialMaterial('LimitState', 40002, 36.51067208, 9.661e-05, 109.53201625, 0.00028984, 365.10672082, 0.00096614, -36.51067208, -9.661e-05, -109.53201625, -0.00028984, -365.10672082, -0.00096614, 0.4, 0.3, 0.003, 0.0, 0.0, 20002, 2)
    ops.limitCurve('ThreePoint', 10002, 2, 0.0, 146.04268833, 0.01327179, 146.04268833, 0.03981538, 102.22988183, -2848.690414, 0.05, 2, 0, 70002, 21002, 1, 3)
    ops.uniaxialMaterial('LimitState', 30002, 36.51067208, 9.661e-05, 109.53201625, 0.00028984, 365.10672082, 0.00096614, -36.51067208, -9.661e-05, -109.53201625, -0.00028984, -365.10672082, -0.00096614, 0.4, 0.3, 0.003, 0.0, 0.0, 10002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2, 99999, 'P', 40002, 'Vy', 30002, 'Vz', 20002, 'My', 10002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170002, 70002, 170002, 2, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121002, 121002, 21002, 2, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170003, 10.3, 0.0, 0.0)
    ops.node(121003, 10.3, 0.0, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3, 170003, 121003, 0.09, 31171370.52145547, 12988071.05060645, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20003, 58.28186364, 0.00067596, 70.02121145, 0.04195291, 7.00212114, 0.1363328, -58.28186364, -0.00067596, -70.02121145, -0.04195291, -7.00212114, -0.1363328, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10003, 61.28739117, 0.00067596, 73.63212341, 0.04195291, 7.36321234, 0.1363328, -61.28739117, -0.00067596, -73.63212341, -0.04195291, -7.36321234, -0.1363328, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20003, 3, 0.0, 146.46683851, 0.01351927, 146.46683851, 0.04055782, 102.52678696, -2905.93536526, 0.05, 2, 0, 70003, 21003, 2, 3)
    ops.uniaxialMaterial('LimitState', 40003, 36.61670963, 9.773e-05, 109.85012888, 0.0002932, 366.16709628, 0.00097734, -36.61670963, -9.773e-05, -109.85012888, -0.0002932, -366.16709628, -0.00097734, 0.4, 0.3, 0.003, 0.0, 0.0, 20003, 2)
    ops.limitCurve('ThreePoint', 10003, 3, 0.0, 146.46683851, 0.01351927, 146.46683851, 0.04055782, 102.52678696, -2905.93536526, 0.05, 2, 0, 70003, 21003, 1, 3)
    ops.uniaxialMaterial('LimitState', 30003, 36.61670963, 9.773e-05, 109.85012888, 0.0002932, 366.16709628, 0.00097734, -36.61670963, -9.773e-05, -109.85012888, -0.0002932, -366.16709628, -0.00097734, 0.4, 0.3, 0.003, 0.0, 0.0, 10003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3, 99999, 'P', 40003, 'Vy', 30003, 'Vz', 20003, 'My', 10003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170003, 70003, 170003, 3, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121003, 121003, 21003, 3, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170004, 17.75, 0.0, 0.0)
    ops.node(121004, 17.75, 0.0, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4, 170004, 121004, 0.0625, 31135749.74835729, 12973229.06181554, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20004, 39.03072983, 0.00080719, 46.82777402, 0.03529628, 4.6827774, 0.10933574, -39.03072983, -0.00080719, -46.82777402, -0.03529628, -4.6827774, -0.10933574, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10004, 39.03072983, 0.00080719, 46.82777402, 0.03529628, 4.6827774, 0.10933574, -39.03072983, -0.00080719, -46.82777402, -0.03529628, -4.6827774, -0.10933574, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20004, 4, 0.0, 93.36237207, 0.0161439, 93.36237207, 0.0484317, 65.35366045, -1539.70282009, 0.05, 2, 0, 70004, 21004, 2, 3)
    ops.uniaxialMaterial('LimitState', 40004, 23.34059302, 8.981e-05, 70.02177906, 0.00026944, 233.40593018, 0.00089813, -23.34059302, -8.981e-05, -70.02177906, -0.00026944, -233.40593018, -0.00089813, 0.4, 0.3, 0.003, 0.0, 0.0, 20004, 2)
    ops.limitCurve('ThreePoint', 10004, 4, 0.0, 93.36237207, 0.0161439, 93.36237207, 0.0484317, 65.35366045, -1539.70282009, 0.05, 2, 0, 70004, 21004, 1, 3)
    ops.uniaxialMaterial('LimitState', 30004, 23.34059302, 8.981e-05, 70.02177906, 0.00026944, 233.40593018, 0.00089813, -23.34059302, -8.981e-05, -70.02177906, -0.00026944, -233.40593018, -0.00089813, 0.4, 0.3, 0.003, 0.0, 0.0, 10004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4, 99999, 'P', 40004, 'Vy', 30004, 'Vz', 20004, 'My', 10004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170004, 70004, 170004, 4, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121004, 121004, 21004, 4, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170005, 0.0, 3.5, 0.0)
    ops.node(121005, 0.0, 3.5, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 5, 170005, 121005, 0.09, 30914198.70810824, 12880916.12837843, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20005, 67.2184039, 0.00069677, 80.62337074, 0.0423369, 8.06233707, 0.12997445, -67.2184039, -0.00069677, -80.62337074, -0.0423369, -8.06233707, -0.12997445, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10005, 64.05512968, 0.00069677, 76.82926354, 0.0423369, 7.68292635, 0.12997445, -64.05512968, -0.00069677, -76.82926354, -0.0423369, -7.68292635, -0.12997445, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20005, 5, 0.0, 151.22668171, 0.01393536, 151.22668171, 0.04180608, 105.8586772, -2862.42054348, 0.05, 2, 0, 70005, 21005, 2, 3)
    ops.uniaxialMaterial('LimitState', 40005, 37.80667043, 0.00010175, 113.42001128, 0.00030525, 378.06670428, 0.0010175, -37.80667043, -0.00010175, -113.42001128, -0.00030525, -378.06670428, -0.0010175, 0.4, 0.3, 0.003, 0.0, 0.0, 20005, 2)
    ops.limitCurve('ThreePoint', 10005, 5, 0.0, 151.22668171, 0.01393536, 151.22668171, 0.04180608, 105.8586772, -2862.42054348, 0.05, 2, 0, 70005, 21005, 1, 3)
    ops.uniaxialMaterial('LimitState', 30005, 37.80667043, 0.00010175, 113.42001128, 0.00030525, 378.06670428, 0.0010175, -37.80667043, -0.00010175, -113.42001128, -0.00030525, -378.06670428, -0.0010175, 0.4, 0.3, 0.003, 0.0, 0.0, 10005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 5, 99999, 'P', 40005, 'Vy', 30005, 'Vz', 20005, 'My', 10005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170005, 70005, 170005, 5, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121005, 121005, 21005, 5, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170008, 17.75, 3.5, 0.0)
    ops.node(121008, 17.75, 3.5, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 8, 170008, 121008, 0.09, 30558146.77667942, 12732561.15694976, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20008, 66.87884312, 0.00069542, 80.26729309, 0.04211376, 8.02672931, 0.12852655, -66.87884312, -0.00069542, -80.26729309, -0.04211376, -8.02672931, -0.12852655, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10008, 63.7303053, 0.00069542, 76.48845069, 0.04211376, 7.64884507, 0.12852655, -63.7303053, -0.00069542, -76.48845069, -0.04211376, -7.64884507, -0.12852655, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20008, 8, 0.0, 147.98050399, 0.01390834, 147.98050399, 0.04172503, 103.58635279, -2768.1043021, 0.05, 2, 0, 70008, 21008, 2, 3)
    ops.uniaxialMaterial('LimitState', 40008, 36.995126, 0.00010073, 110.98537799, 0.00030218, 369.95125997, 0.00100726, -36.995126, -0.00010073, -110.98537799, -0.00030218, -369.95125997, -0.00100726, 0.4, 0.3, 0.003, 0.0, 0.0, 20008, 2)
    ops.limitCurve('ThreePoint', 10008, 8, 0.0, 147.98050399, 0.01390834, 147.98050399, 0.04172503, 103.58635279, -2768.1043021, 0.05, 2, 0, 70008, 21008, 1, 3)
    ops.uniaxialMaterial('LimitState', 30008, 36.995126, 0.00010073, 110.98537799, 0.00030218, 369.95125997, 0.00100726, -36.995126, -0.00010073, -110.98537799, -0.00030218, -369.95125997, -0.00100726, 0.4, 0.3, 0.003, 0.0, 0.0, 10008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 8, 99999, 'P', 40008, 'Vy', 30008, 'Vz', 20008, 'My', 10008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170008, 70008, 170008, 8, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121008, 121008, 21008, 8, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170009, 0.0, 7.0, 0.0)
    ops.node(121009, 0.0, 7.0, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 9, 170009, 121009, 0.09, 31610591.77548276, 13171079.90645115, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20009, 74.11065554, 0.00071352, 88.76211874, 0.04298241, 8.87621187, 0.13278427, -74.11065554, -0.00071352, -88.76211874, -0.04298241, -8.87621187, -0.13278427, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10009, 67.9953699, 0.00071352, 81.43785874, 0.04298241, 8.14378587, 0.13278427, -67.9953699, -0.00071352, -81.43785874, -0.04298241, -8.14378587, -0.13278427, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20009, 9, 0.0, 151.8577953, 0.01427034, 151.8577953, 0.04281101, 106.30045671, -2797.91519228, 0.05, 2, 0, 70009, 21009, 2, 3)
    ops.uniaxialMaterial('LimitState', 40009, 37.96444882, 9.992e-05, 113.89334647, 0.00029977, 379.64448825, 0.00099924, -37.96444882, -9.992e-05, -113.89334647, -0.00029977, -379.64448825, -0.00099924, 0.4, 0.3, 0.003, 0.0, 0.0, 20009, 2)
    ops.limitCurve('ThreePoint', 10009, 9, 0.0, 151.8577953, 0.01427034, 151.8577953, 0.04281101, 106.30045671, -2797.91519228, 0.05, 2, 0, 70009, 21009, 1, 3)
    ops.uniaxialMaterial('LimitState', 30009, 37.96444882, 9.992e-05, 113.89334647, 0.00029977, 379.64448825, 0.00099924, -37.96444882, -9.992e-05, -113.89334647, -0.00029977, -379.64448825, -0.00099924, 0.4, 0.3, 0.003, 0.0, 0.0, 10009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 9, 99999, 'P', 40009, 'Vy', 30009, 'Vz', 20009, 'My', 10009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170009, 70009, 170009, 9, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121009, 121009, 21009, 9, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170010, 7.45, 7.0, 0.0)
    ops.node(121010, 7.45, 7.0, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 10, 170010, 121010, 0.09, 30834168.09717469, 12847570.04048946, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20010, 85.19450691, 0.00071205, 102.00366493, 0.04236017, 10.20036649, 0.12487183, -85.19450691, -0.00071205, -102.00366493, -0.04236017, -10.20036649, -0.12487183, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10010, 85.19450691, 0.00071205, 102.00366493, 0.04236017, 10.20036649, 0.12487183, -85.19450691, -0.00071205, -102.00366493, -0.04236017, -10.20036649, -0.12487183, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20010, 10, 0.0, 154.95635192, 0.01424096, 154.95635192, 0.04272288, 108.46944635, -2844.61147843, 0.05, 2, 0, 70010, 21010, 2, 3)
    ops.uniaxialMaterial('LimitState', 40010, 38.73908798, 0.00010453, 116.21726394, 0.00031359, 387.39087981, 0.0010453, -38.73908798, -0.00010453, -116.21726394, -0.00031359, -387.39087981, -0.0010453, 0.4, 0.3, 0.003, 0.0, 0.0, 20010, 2)
    ops.limitCurve('ThreePoint', 10010, 10, 0.0, 154.95635192, 0.01424096, 154.95635192, 0.04272288, 108.46944635, -2844.61147843, 0.05, 2, 0, 70010, 21010, 1, 3)
    ops.uniaxialMaterial('LimitState', 30010, 38.73908798, 0.00010453, 116.21726394, 0.00031359, 387.39087981, 0.0010453, -38.73908798, -0.00010453, -116.21726394, -0.00031359, -387.39087981, -0.0010453, 0.4, 0.3, 0.003, 0.0, 0.0, 10010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 10, 99999, 'P', 40010, 'Vy', 30010, 'Vz', 20010, 'My', 10010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170010, 70010, 170010, 10, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121010, 121010, 21010, 10, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170011, 10.3, 7.0, 0.0)
    ops.node(121011, 10.3, 7.0, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 11, 170011, 121011, 0.09, 30744531.39287541, 12810221.41369809, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20011, 86.51455133, 0.00069893, 103.5990715, 0.04205263, 10.35990715, 0.12422885, -86.51455133, -0.00069893, -103.5990715, -0.04205263, -10.35990715, -0.12422885, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10011, 86.51455133, 0.00069893, 103.5990715, 0.04205263, 10.35990715, 0.12422885, -86.51455133, -0.00069893, -103.5990715, -0.04205263, -10.35990715, -0.12422885, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20011, 11, 0.0, 152.73840974, 0.01397861, 152.73840974, 0.04193583, 106.91688682, -2767.43408793, 0.05, 2, 0, 70011, 21011, 2, 3)
    ops.uniaxialMaterial('LimitState', 40011, 38.18460243, 0.00010333, 114.5538073, 0.00031, 381.84602434, 0.00103334, -38.18460243, -0.00010333, -114.5538073, -0.00031, -381.84602434, -0.00103334, 0.4, 0.3, 0.003, 0.0, 0.0, 20011, 2)
    ops.limitCurve('ThreePoint', 10011, 11, 0.0, 152.73840974, 0.01397861, 152.73840974, 0.04193583, 106.91688682, -2767.43408793, 0.05, 2, 0, 70011, 21011, 1, 3)
    ops.uniaxialMaterial('LimitState', 30011, 38.18460243, 0.00010333, 114.5538073, 0.00031, 381.84602434, 0.00103334, -38.18460243, -0.00010333, -114.5538073, -0.00031, -381.84602434, -0.00103334, 0.4, 0.3, 0.003, 0.0, 0.0, 10011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 11, 99999, 'P', 40011, 'Vy', 30011, 'Vz', 20011, 'My', 10011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170011, 70011, 170011, 11, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121011, 121011, 21011, 11, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170012, 17.75, 7.0, 0.0)
    ops.node(121012, 17.75, 7.0, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 12, 170012, 121012, 0.09, 31615232.57031474, 13173013.57096447, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20012, 73.40224104, 0.00071183, 87.91277491, 0.04317278, 8.79127749, 0.13298927, -73.40224104, -0.00071183, -87.91277491, -0.04317278, -8.79127749, -0.13298927, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10012, 67.44362872, 0.00071183, 80.77623335, 0.04317278, 8.07762333, 0.13298927, -67.44362872, -0.00071183, -80.77623335, -0.04317278, -8.07762333, -0.13298927, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20012, 12, 0.0, 154.1578505, 0.01423659, 154.1578505, 0.04270977, 107.91049535, -2895.6452861, 0.05, 2, 0, 70012, 21012, 2, 3)
    ops.uniaxialMaterial('LimitState', 40012, 38.53946263, 0.00010142, 115.61838788, 0.00030427, 385.39462626, 0.00101422, -38.53946263, -0.00010142, -115.61838788, -0.00030427, -385.39462626, -0.00101422, 0.4, 0.3, 0.003, 0.0, 0.0, 20012, 2)
    ops.limitCurve('ThreePoint', 10012, 12, 0.0, 154.1578505, 0.01423659, 154.1578505, 0.04270977, 107.91049535, -2895.6452861, 0.05, 2, 0, 70012, 21012, 1, 3)
    ops.uniaxialMaterial('LimitState', 30012, 38.53946263, 0.00010142, 115.61838788, 0.00030427, 385.39462626, 0.00101422, -38.53946263, -0.00010142, -115.61838788, -0.00030427, -385.39462626, -0.00101422, 0.4, 0.3, 0.003, 0.0, 0.0, 10012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 12, 99999, 'P', 40012, 'Vy', 30012, 'Vz', 20012, 'My', 10012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170012, 70012, 170012, 12, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121012, 121012, 21012, 12, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170013, 0.0, 10.5, 0.0)
    ops.node(121013, 0.0, 10.5, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 13, 170013, 121013, 0.0625, 31392802.67323792, 13080334.44718247, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20013, 39.45430393, 0.00079616, 47.31056988, 0.03535014, 4.73105699, 0.11004889, -39.45430393, -0.00079616, -47.31056988, -0.03535014, -4.73105699, -0.11004889, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10013, 39.45430393, 0.00079616, 47.31056988, 0.03535014, 4.73105699, 0.11004889, -39.45430393, -0.00079616, -47.31056988, -0.03535014, -4.73105699, -0.11004889, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20013, 13, 0.0, 95.14643949, 0.01592317, 95.14643949, 0.04776952, 66.60250765, -1589.44334156, 0.05, 2, 0, 70013, 21013, 2, 3)
    ops.uniaxialMaterial('LimitState', 40013, 23.78660987, 9.078e-05, 71.35982962, 0.00027234, 237.86609873, 0.0009078, -23.78660987, -9.078e-05, -71.35982962, -0.00027234, -237.86609873, -0.0009078, 0.4, 0.3, 0.003, 0.0, 0.0, 20013, 2)
    ops.limitCurve('ThreePoint', 10013, 13, 0.0, 95.14643949, 0.01592317, 95.14643949, 0.04776952, 66.60250765, -1589.44334156, 0.05, 2, 0, 70013, 21013, 1, 3)
    ops.uniaxialMaterial('LimitState', 30013, 23.78660987, 9.078e-05, 71.35982962, 0.00027234, 237.86609873, 0.0009078, -23.78660987, -9.078e-05, -71.35982962, -0.00027234, -237.86609873, -0.0009078, 0.4, 0.3, 0.003, 0.0, 0.0, 10013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 13, 99999, 'P', 40013, 'Vy', 30013, 'Vz', 20013, 'My', 10013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170013, 70013, 170013, 13, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121013, 121013, 21013, 13, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170014, 7.45, 10.5, 0.0)
    ops.node(121014, 7.45, 10.5, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 14, 170014, 121014, 0.09, 30302653.07040482, 12626105.44600201, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20014, 65.27902165, 0.00067296, 78.56670175, 0.04349436, 7.85667018, 0.13526868, -65.27902165, -0.00067296, -78.56670175, -0.04349436, -7.85667018, -0.13526868, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10014, 65.27902165, 0.00067296, 78.56670175, 0.04349436, 7.85667018, 0.13526868, -65.27902165, -0.00067296, -78.56670175, -0.04349436, -7.85667018, -0.13526868, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20014, 14, 0.0, 144.01732997, 0.0134593, 144.01732997, 0.04037789, 100.81213098, -2906.9814435, 0.05, 2, 0, 70014, 21014, 2, 3)
    ops.uniaxialMaterial('LimitState', 40014, 36.00433249, 9.885e-05, 108.01299748, 0.00029656, 360.04332494, 0.00098855, -36.00433249, -9.885e-05, -108.01299748, -0.00029656, -360.04332494, -0.00098855, 0.4, 0.3, 0.003, 0.0, 0.0, 20014, 2)
    ops.limitCurve('ThreePoint', 10014, 14, 0.0, 144.01732997, 0.0134593, 144.01732997, 0.04037789, 100.81213098, -2906.9814435, 0.05, 2, 0, 70014, 21014, 1, 3)
    ops.uniaxialMaterial('LimitState', 30014, 36.00433249, 9.885e-05, 108.01299748, 0.00029656, 360.04332494, 0.00098855, -36.00433249, -9.885e-05, -108.01299748, -0.00029656, -360.04332494, -0.00098855, 0.4, 0.3, 0.003, 0.0, 0.0, 10014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 14, 99999, 'P', 40014, 'Vy', 30014, 'Vz', 20014, 'My', 10014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170014, 70014, 170014, 14, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121014, 121014, 21014, 14, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170015, 10.3, 10.5, 0.0)
    ops.node(121015, 10.3, 10.5, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 15, 170015, 121015, 0.09, 31356027.21230935, 13065011.33846223, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20015, 66.60559546, 0.00066377, 79.98843661, 0.04311644, 7.99884366, 0.13801915, -66.60559546, -0.00066377, -79.98843661, -0.04311644, -7.99884366, -0.13801915, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10015, 66.60559546, 0.00066377, 79.98843661, 0.04311644, 7.99884366, 0.13801915, -66.60559546, -0.00066377, -79.98843661, -0.04311644, -7.99884366, -0.13801915, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20015, 15, 0.0, 148.41371715, 0.01327536, 148.41371715, 0.03982609, 103.889602, -2974.23316791, 0.05, 2, 0, 70015, 21015, 2, 3)
    ops.uniaxialMaterial('LimitState', 40015, 37.10342929, 9.845e-05, 111.31028786, 0.00029535, 371.03429287, 0.0009845, -37.10342929, -9.845e-05, -111.31028786, -0.00029535, -371.03429287, -0.0009845, 0.4, 0.3, 0.003, 0.0, 0.0, 20015, 2)
    ops.limitCurve('ThreePoint', 10015, 15, 0.0, 148.41371715, 0.01327536, 148.41371715, 0.03982609, 103.889602, -2974.23316791, 0.05, 2, 0, 70015, 21015, 1, 3)
    ops.uniaxialMaterial('LimitState', 30015, 37.10342929, 9.845e-05, 111.31028786, 0.00029535, 371.03429287, 0.0009845, -37.10342929, -9.845e-05, -111.31028786, -0.00029535, -371.03429287, -0.0009845, 0.4, 0.3, 0.003, 0.0, 0.0, 10015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 15, 99999, 'P', 40015, 'Vy', 30015, 'Vz', 20015, 'My', 10015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170015, 70015, 170015, 15, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121015, 121015, 21015, 15, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170016, 17.75, 10.5, 0.0)
    ops.node(121016, 17.75, 10.5, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 16, 170016, 121016, 0.0625, 30490892.56382168, 12704538.56825903, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20016, 38.71234775, 0.00080852, 46.50284954, 0.0352648, 4.65028495, 0.10757067, -38.71234775, -0.00080852, -46.50284954, -0.0352648, -4.65028495, -0.10757067, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10016, 38.71234775, 0.00080852, 46.50284954, 0.0352648, 4.65028495, 0.10757067, -38.71234775, -0.00080852, -46.50284954, -0.0352648, -4.65028495, -0.10757067, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20016, 16, 0.0, 92.44886852, 0.01617043, 92.44886852, 0.04851129, 64.71420797, -1554.45844474, 0.05, 2, 0, 70016, 21016, 2, 3)
    ops.uniaxialMaterial('LimitState', 40016, 23.11221713, 9.081e-05, 69.33665139, 0.00027244, 231.12217131, 0.00090815, -23.11221713, -9.081e-05, -69.33665139, -0.00027244, -231.12217131, -0.00090815, 0.4, 0.3, 0.003, 0.0, 0.0, 20016, 2)
    ops.limitCurve('ThreePoint', 10016, 16, 0.0, 92.44886852, 0.01617043, 92.44886852, 0.04851129, 64.71420797, -1554.45844474, 0.05, 2, 0, 70016, 21016, 1, 3)
    ops.uniaxialMaterial('LimitState', 30016, 23.11221713, 9.081e-05, 69.33665139, 0.00027244, 231.12217131, 0.00090815, -23.11221713, -9.081e-05, -69.33665139, -0.00027244, -231.12217131, -0.00090815, 0.4, 0.3, 0.003, 0.0, 0.0, 10016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 16, 99999, 'P', 40016, 'Vy', 30016, 'Vz', 20016, 'My', 10016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170016, 70016, 170016, 16, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121016, 121016, 21016, 16, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171001, 0.0, 0.0, 2.9)
    ops.node(122001, 0.0, 0.0, 4.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1001, 171001, 122001, 0.0625, 32075593.81419361, 13364830.755914, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21001, 39.34637319, 0.00080189, 47.2399026, 0.04910207, 4.72399026, 0.14910207, -39.34637319, -0.00080189, -47.2399026, -0.04910207, -4.72399026, -0.14910207, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11001, 37.28712703, 0.00080189, 44.7675378, 0.04910207, 4.47675378, 0.14910207, -37.28712703, -0.00080189, -44.7675378, -0.04910207, -4.47675378, -0.14910207, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21001, 1001, 0.0, 112.62728191, 0.01603788, 112.62728191, 0.04811363, 78.83909734, -2780.45926613, 0.05, 2, 0, 71001, 22001, 2, 3)
    ops.uniaxialMaterial('LimitState', 41001, 28.15682048, 0.00010517, 84.47046143, 0.00031551, 281.56820477, 0.00105171, -28.15682048, -0.00010517, -84.47046143, -0.00031551, -281.56820477, -0.00105171, 0.4, 0.3, 0.003, 0.0, 0.0, 21001, 2)
    ops.limitCurve('ThreePoint', 11001, 1001, 0.0, 112.62728191, 0.01603788, 112.62728191, 0.04811363, 78.83909734, -2780.45926613, 0.05, 2, 0, 71001, 22001, 1, 3)
    ops.uniaxialMaterial('LimitState', 31001, 28.15682048, 0.00010517, 84.47046143, 0.00031551, 281.56820477, 0.00105171, -28.15682048, -0.00010517, -84.47046143, -0.00031551, -281.56820477, -0.00105171, 0.4, 0.3, 0.003, 0.0, 0.0, 11001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1001, 99999, 'P', 41001, 'Vy', 31001, 'Vz', 21001, 'My', 11001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171001, 71001, 171001, 1001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122001, 122001, 22001, 1001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171002, 7.45, 0.0, 2.9)
    ops.node(122002, 7.45, 0.0, 4.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1002, 171002, 122002, 0.09, 32329959.53314506, 13470816.47214377, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21002, 42.14275562, 0.00063257, 50.60845027, 0.04203644, 5.06084503, 0.14203644, -42.14275562, -0.00063257, -50.60845027, -0.04203644, -5.06084503, -0.14203644, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11002, 39.54466584, 0.00063257, 47.48845263, 0.04203644, 4.74884526, 0.14203644, -39.54466584, -0.00063257, -47.48845263, -0.04203644, -4.74884526, -0.14203644, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21002, 1002, 0.0, 146.27702813, 0.0126515, 146.27702813, 0.0379545, 102.39391969, -3321.34011479, 0.05, 2, 0, 71002, 22002, 2, 3)
    ops.uniaxialMaterial('LimitState', 41002, 36.56925703, 9.411e-05, 109.7077711, 0.00028233, 365.69257032, 0.0009411, -36.56925703, -9.411e-05, -109.7077711, -0.00028233, -365.69257032, -0.0009411, 0.4, 0.3, 0.003, 0.0, 0.0, 21002, 2)
    ops.limitCurve('ThreePoint', 11002, 1002, 0.0, 146.27702813, 0.0126515, 146.27702813, 0.0379545, 102.39391969, -3321.34011479, 0.05, 2, 0, 71002, 22002, 1, 3)
    ops.uniaxialMaterial('LimitState', 31002, 36.56925703, 9.411e-05, 109.7077711, 0.00028233, 365.69257032, 0.0009411, -36.56925703, -9.411e-05, -109.7077711, -0.00028233, -365.69257032, -0.0009411, 0.4, 0.3, 0.003, 0.0, 0.0, 11002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1002, 99999, 'P', 41002, 'Vy', 31002, 'Vz', 21002, 'My', 11002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171002, 71002, 171002, 1002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122002, 122002, 22002, 1002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171003, 10.3, 0.0, 2.9)
    ops.node(122003, 10.3, 0.0, 4.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1003, 171003, 122003, 0.09, 31310448.18327602, 13046020.07636501, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21003, 42.64106747, 0.00062718, 51.34859686, 0.04223791, 5.13485969, 0.14223791, -42.64106747, -0.00062718, -51.34859686, -0.04223791, -5.13485969, -0.14223791, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11003, 39.82858392, 0.00062718, 47.96178943, 0.04223791, 4.79617894, 0.14223791, -39.82858392, -0.00062718, -47.96178943, -0.04223791, -4.79617894, -0.14223791, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21003, 1003, 0.0, 142.31333628, 0.01254352, 142.31333628, 0.03763056, 99.6193354, -3257.30202522, 0.05, 2, 0, 71003, 22003, 2, 3)
    ops.uniaxialMaterial('LimitState', 41003, 35.57833407, 9.454e-05, 106.73500221, 0.00028362, 355.78334071, 0.00094541, -35.57833407, -9.454e-05, -106.73500221, -0.00028362, -355.78334071, -0.00094541, 0.4, 0.3, 0.003, 0.0, 0.0, 21003, 2)
    ops.limitCurve('ThreePoint', 11003, 1003, 0.0, 142.31333628, 0.01254352, 142.31333628, 0.03763056, 99.6193354, -3257.30202522, 0.05, 2, 0, 71003, 22003, 1, 3)
    ops.uniaxialMaterial('LimitState', 31003, 35.57833407, 9.454e-05, 106.73500221, 0.00028362, 355.78334071, 0.00094541, -35.57833407, -9.454e-05, -106.73500221, -0.00028362, -355.78334071, -0.00094541, 0.4, 0.3, 0.003, 0.0, 0.0, 11003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1003, 99999, 'P', 41003, 'Vy', 31003, 'Vz', 21003, 'My', 11003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171003, 71003, 171003, 1003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122003, 122003, 22003, 1003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171004, 17.75, 0.0, 2.9)
    ops.node(122004, 17.75, 0.0, 4.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1004, 171004, 122004, 0.0625, 32299093.1946432, 13457955.497768, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21004, 40.72155504, 0.00077785, 48.86104886, 0.04851035, 4.88610489, 0.14851035, -40.72155504, -0.00077785, -48.86104886, -0.04851035, -4.88610489, -0.14851035, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11004, 38.37686402, 0.00077785, 46.04769701, 0.04851035, 4.6047697, 0.14851035, -38.37686402, -0.00077785, -46.04769701, -0.04851035, -4.6047697, -0.14851035, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21004, 1004, 0.0, 111.78447194, 0.01555698, 111.78447194, 0.04667095, 78.24913036, -2701.31512081, 0.05, 2, 0, 71004, 22004, 2, 3)
    ops.uniaxialMaterial('LimitState', 41004, 27.94611799, 0.00010366, 83.83835396, 0.00031098, 279.46117986, 0.00103661, -27.94611799, -0.00010366, -83.83835396, -0.00031098, -279.46117986, -0.00103661, 0.4, 0.3, 0.003, 0.0, 0.0, 21004, 2)
    ops.limitCurve('ThreePoint', 11004, 1004, 0.0, 111.78447194, 0.01555698, 111.78447194, 0.04667095, 78.24913036, -2701.31512081, 0.05, 2, 0, 71004, 22004, 1, 3)
    ops.uniaxialMaterial('LimitState', 31004, 27.94611799, 0.00010366, 83.83835396, 0.00031098, 279.46117986, 0.00103661, -27.94611799, -0.00010366, -83.83835396, -0.00031098, -279.46117986, -0.00103661, 0.4, 0.3, 0.003, 0.0, 0.0, 11004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1004, 99999, 'P', 41004, 'Vy', 31004, 'Vz', 21004, 'My', 11004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171004, 71004, 171004, 1004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122004, 122004, 22004, 1004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171005, 0.0, 3.5, 2.9)
    ops.node(122005, 0.0, 3.5, 4.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1005, 171005, 122005, 0.09, 30028935.70045829, 12512056.54185762, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21005, 71.28296606, 0.00068771, 85.93763548, 0.05459516, 8.59376355, 0.15459516, -71.28296606, -0.00068771, -85.93763548, -0.05459516, -8.59376355, -0.15459516, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11005, 62.31279672, 0.00068771, 75.1233388, 0.04675205, 7.51233388, 0.1409383, -62.31279672, -0.00068771, -75.1233388, -0.04675205, -7.51233388, -0.1409383, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21005, 1005, 0.0, 143.20645064, 0.01375429, 143.20645064, 0.04126287, 100.24451544, -3099.1840129, 0.05, 2, 0, 71005, 22005, 2, 3)
    ops.uniaxialMaterial('LimitState', 41005, 35.80161266, 9.919e-05, 107.40483798, 0.00029758, 358.01612659, 0.00099194, -35.80161266, -9.919e-05, -107.40483798, -0.00029758, -358.01612659, -0.00099194, 0.4, 0.3, 0.003, 0.0, 0.0, 21005, 2)
    ops.limitCurve('ThreePoint', 11005, 1005, 0.0, 182.10191533, 0.01375429, 182.10191533, 0.04126287, 127.47134073, -5476.74127335, 0.05, 2, 0, 71005, 22005, 1, 3)
    ops.uniaxialMaterial('LimitState', 31005, 45.52547883, 0.00012614, 136.5764365, 0.00037841, 455.25478833, 0.00126136, -45.52547883, -0.00012614, -136.5764365, -0.00037841, -455.25478833, -0.00126136, 0.4, 0.3, 0.003, 0.0, 0.0, 11005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1005, 99999, 'P', 41005, 'Vy', 31005, 'Vz', 21005, 'My', 11005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171005, 71005, 171005, 1005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122005, 122005, 22005, 1005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171008, 17.75, 3.5, 2.9)
    ops.node(122008, 17.75, 3.5, 4.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1008, 171008, 122008, 0.09, 31336381.13659529, 13056825.47358137, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21008, 72.66317573, 0.00068482, 87.35725957, 0.05401104, 8.73572596, 0.15401104, -72.66317573, -0.00068482, -87.35725957, -0.05401104, -8.73572596, -0.15401104, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11008, 63.45936508, 0.00068482, 76.29223706, 0.0462525, 7.62922371, 0.14406695, -63.45936508, -0.00068482, -76.29223706, -0.0462525, -7.62922371, -0.14406695, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21008, 1008, 0.0, 146.00102579, 0.01369646, 146.00102579, 0.04108937, 102.20071805, -3052.66357393, 0.05, 2, 0, 71008, 22008, 2, 3)
    ops.uniaxialMaterial('LimitState', 41008, 36.50025645, 9.691e-05, 109.50076934, 0.00029073, 365.00256448, 0.0009691, -36.50025645, -9.691e-05, -109.50076934, -0.00029073, -365.00256448, -0.0009691, 0.4, 0.3, 0.003, 0.0, 0.0, 21008, 2)
    ops.limitCurve('ThreePoint', 11008, 1008, 0.0, 184.45162937, 0.01369646, 184.45162937, 0.04108937, 129.11614056, -5384.02378953, 0.05, 2, 0, 71008, 22008, 1, 3)
    ops.uniaxialMaterial('LimitState', 31008, 46.11290734, 0.00012243, 138.33872202, 0.0003673, 461.12907341, 0.00122433, -46.11290734, -0.00012243, -138.33872202, -0.0003673, -461.12907341, -0.00122433, 0.4, 0.3, 0.003, 0.0, 0.0, 11008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1008, 99999, 'P', 41008, 'Vy', 31008, 'Vz', 21008, 'My', 11008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171008, 71008, 171008, 1008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122008, 122008, 22008, 1008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171009, 0.0, 7.0, 2.9)
    ops.node(122009, 0.0, 7.0, 4.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1009, 171009, 122009, 0.09, 29935044.88287506, 12472935.36786461, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21009, 72.04226388, 0.00068851, 86.86415457, 0.0540027, 8.68641546, 0.1540027, -72.04226388, -0.00068851, -86.86415457, -0.0540027, -8.68641546, -0.1540027, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11009, 62.85345591, 0.00068851, 75.78485205, 0.0462459, 7.5784852, 0.14001691, -62.85345591, -0.00068851, -75.78485205, -0.0462459, -7.5784852, -0.14001691, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21009, 1009, 0.0, 140.60045936, 0.0137701, 140.60045936, 0.0413103, 98.42032155, -2969.06297737, 0.05, 2, 0, 71009, 22009, 2, 3)
    ops.uniaxialMaterial('LimitState', 41009, 35.15011484, 9.769e-05, 105.45034452, 0.00029308, 351.50114841, 0.00097695, -35.15011484, -9.769e-05, -105.45034452, -0.00029308, -351.50114841, -0.00097695, 0.4, 0.3, 0.003, 0.0, 0.0, 21009, 2)
    ops.limitCurve('ThreePoint', 11009, 1009, 0.0, 178.28599375, 0.0137701, 178.28599375, 0.0413103, 124.80019562, -5214.25250358, 0.05, 2, 0, 71009, 22009, 1, 3)
    ops.uniaxialMaterial('LimitState', 31009, 44.57149844, 0.00012388, 133.71449531, 0.00037164, 445.71498437, 0.0012388, -44.57149844, -0.00012388, -133.71449531, -0.00037164, -445.71498437, -0.0012388, 0.4, 0.3, 0.003, 0.0, 0.0, 11009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1009, 99999, 'P', 41009, 'Vy', 31009, 'Vz', 21009, 'My', 11009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171009, 71009, 171009, 1009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122009, 122009, 22009, 1009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171010, 7.45, 7.0, 2.9)
    ops.node(122010, 7.45, 7.0, 4.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1010, 171010, 122010, 0.09, 31154246.17458325, 12980935.90607635, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21010, 58.58555379, 0.00065746, 70.35710018, 0.04101302, 7.03571002, 0.13408861, -58.58555379, -0.00065746, -70.35710018, -0.04101302, -7.03571002, -0.13408861, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11010, 52.38525879, 0.00065746, 62.91098508, 0.04101302, 6.29109851, 0.13408861, -52.38525879, -0.00065746, -62.91098508, -0.04101302, -6.29109851, -0.13408861, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21010, 1010, 0.0, 145.66006561, 0.01314917, 145.66006561, 0.03944752, 101.96204593, -2801.9325936, 0.05, 2, 0, 71010, 22010, 2, 3)
    ops.uniaxialMaterial('LimitState', 41010, 36.4150164, 9.725e-05, 109.24504921, 0.00029175, 364.15016404, 0.00097249, -36.4150164, -9.725e-05, -109.24504921, -0.00029175, -364.15016404, -0.00097249, 0.4, 0.3, 0.003, 0.0, 0.0, 21010, 2)
    ops.limitCurve('ThreePoint', 11010, 1010, 0.0, 145.66006561, 0.01314917, 145.66006561, 0.03944752, 101.96204593, -2801.9325936, 0.05, 2, 0, 71010, 22010, 1, 3)
    ops.uniaxialMaterial('LimitState', 31010, 36.4150164, 9.725e-05, 109.24504921, 0.00029175, 364.15016404, 0.00097249, -36.4150164, -9.725e-05, -109.24504921, -0.00029175, -364.15016404, -0.00097249, 0.4, 0.3, 0.003, 0.0, 0.0, 11010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1010, 99999, 'P', 41010, 'Vy', 31010, 'Vz', 21010, 'My', 11010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171010, 71010, 171010, 1010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122010, 122010, 22010, 1010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171011, 10.3, 7.0, 2.9)
    ops.node(122011, 10.3, 7.0, 4.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1011, 171011, 122011, 0.09, 30124476.33149886, 12551865.13812453, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21011, 57.55756358, 0.00068391, 69.26131477, 0.04097965, 6.92613148, 0.13083191, -57.55756358, -0.00068391, -69.26131477, -0.04097965, -6.92613148, -0.13083191, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11011, 51.89634505, 0.00068391, 62.44894444, 0.04097965, 6.24489444, 0.13083191, -51.89634505, -0.00068391, -62.44894444, -0.04097965, -6.24489444, -0.13083191, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21011, 1011, 0.0, 143.98936836, 0.01367822, 143.98936836, 0.04103467, 100.79255785, -2860.39697848, 0.05, 2, 0, 71011, 22011, 2, 3)
    ops.uniaxialMaterial('LimitState', 41011, 35.99734209, 9.942e-05, 107.99202627, 0.00029826, 359.9734209, 0.0009942, -35.99734209, -9.942e-05, -107.99202627, -0.00029826, -359.9734209, -0.0009942, 0.4, 0.3, 0.003, 0.0, 0.0, 21011, 2)
    ops.limitCurve('ThreePoint', 11011, 1011, 0.0, 143.98936836, 0.01367822, 143.98936836, 0.04103467, 100.79255785, -2860.39697848, 0.05, 2, 0, 71011, 22011, 1, 3)
    ops.uniaxialMaterial('LimitState', 31011, 35.99734209, 9.942e-05, 107.99202627, 0.00029826, 359.9734209, 0.0009942, -35.99734209, -9.942e-05, -107.99202627, -0.00029826, -359.9734209, -0.0009942, 0.4, 0.3, 0.003, 0.0, 0.0, 11011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1011, 99999, 'P', 41011, 'Vy', 31011, 'Vz', 21011, 'My', 11011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171011, 71011, 171011, 1011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122011, 122011, 22011, 1011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171012, 17.75, 7.0, 2.9)
    ops.node(122012, 17.75, 7.0, 4.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1012, 171012, 122012, 0.09, 30270924.68025571, 12612885.28343988, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21012, 72.92723545, 0.00069845, 87.874707, 0.0538341, 8.7874707, 0.1538341, -72.92723545, -0.00069845, -87.874707, -0.0538341, -8.7874707, -0.1538341, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11012, 63.67636276, 0.00069845, 76.72773671, 0.04610328, 7.67277367, 0.14087181, -63.67636276, -0.00069845, -76.72773671, -0.04610328, -7.67277367, -0.14087181, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21012, 1012, 0.0, 140.80503691, 0.01396901, 140.80503691, 0.04190702, 98.56352583, -2931.65374403, 0.05, 2, 0, 71012, 22012, 2, 3)
    ops.uniaxialMaterial('LimitState', 41012, 35.20125923, 9.675e-05, 105.60377768, 0.00029025, 352.01259226, 0.00096751, -35.20125923, -9.675e-05, -105.60377768, -0.00029025, -352.01259226, -0.00096751, 0.4, 0.3, 0.003, 0.0, 0.0, 21012, 2)
    ops.limitCurve('ThreePoint', 11012, 1012, 0.0, 178.12440522, 0.01396901, 178.12440522, 0.04190702, 124.68708366, -5139.92068119, 0.05, 2, 0, 71012, 22012, 1, 3)
    ops.uniaxialMaterial('LimitState', 31012, 44.53110131, 0.00012239, 133.59330392, 0.00036718, 445.31101306, 0.00122394, -44.53110131, -0.00012239, -133.59330392, -0.00036718, -445.31101306, -0.00122394, 0.4, 0.3, 0.003, 0.0, 0.0, 11012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1012, 99999, 'P', 41012, 'Vy', 31012, 'Vz', 21012, 'My', 11012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171012, 71012, 171012, 1012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122012, 122012, 22012, 1012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171013, 0.0, 10.5, 2.9)
    ops.node(122013, 0.0, 10.5, 4.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1013, 171013, 122013, 0.0625, 31555036.01345144, 13147931.67227143, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21013, 40.8594036, 0.00076078, 49.12311843, 0.04930276, 4.91231184, 0.14930276, -40.8594036, -0.00076078, -49.12311843, -0.04930276, -4.91231184, -0.14930276, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11013, 38.39436723, 0.00076078, 46.15953446, 0.04930276, 4.61595345, 0.14930276, -38.39436723, -0.00076078, -46.15953446, -0.04930276, -4.61595345, -0.14930276, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21013, 1013, 0.0, 112.33485263, 0.01521556, 112.33485263, 0.04564668, 78.63439684, -2826.53625931, 0.05, 2, 0, 71013, 22013, 2, 3)
    ops.uniaxialMaterial('LimitState', 41013, 28.08371316, 0.00010663, 84.25113948, 0.00031988, 280.83713159, 0.00106628, -28.08371316, -0.00010663, -84.25113948, -0.00031988, -280.83713159, -0.00106628, 0.4, 0.3, 0.003, 0.0, 0.0, 21013, 2)
    ops.limitCurve('ThreePoint', 11013, 1013, 0.0, 112.33485263, 0.01521556, 112.33485263, 0.04564668, 78.63439684, -2826.53625931, 0.05, 2, 0, 71013, 22013, 1, 3)
    ops.uniaxialMaterial('LimitState', 31013, 28.08371316, 0.00010663, 84.25113948, 0.00031988, 280.83713159, 0.00106628, -28.08371316, -0.00010663, -84.25113948, -0.00031988, -280.83713159, -0.00106628, 0.4, 0.3, 0.003, 0.0, 0.0, 11013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1013, 99999, 'P', 41013, 'Vy', 31013, 'Vz', 21013, 'My', 11013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171013, 71013, 171013, 1013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122013, 122013, 22013, 1013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171014, 7.45, 10.5, 2.9)
    ops.node(122014, 7.45, 10.5, 4.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1014, 171014, 122014, 0.09, 30625221.39506496, 12760508.9146104, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21014, 43.36111856, 0.00064478, 52.30234734, 0.04214812, 5.23023473, 0.14214812, -43.36111856, -0.00064478, -52.30234734, -0.04214812, -5.23023473, -0.14214812, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11014, 40.46295357, 0.00064478, 48.80656963, 0.04214812, 4.88065696, 0.14214812, -40.46295357, -0.00064478, -48.80656963, -0.04214812, -4.88065696, -0.14214812, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21014, 1014, 0.0, 139.88619271, 0.01289554, 139.88619271, 0.03868662, 97.9203349, -3226.8739951, 0.05, 2, 0, 71014, 22014, 2, 3)
    ops.uniaxialMaterial('LimitState', 41014, 34.97154818, 9.501e-05, 104.91464453, 0.00028502, 349.71548178, 0.00095008, -34.97154818, -9.501e-05, -104.91464453, -0.00028502, -349.71548178, -0.00095008, 0.4, 0.3, 0.003, 0.0, 0.0, 21014, 2)
    ops.limitCurve('ThreePoint', 11014, 1014, 0.0, 139.88619271, 0.01289554, 139.88619271, 0.03868662, 97.9203349, -3226.8739951, 0.05, 2, 0, 71014, 22014, 1, 3)
    ops.uniaxialMaterial('LimitState', 31014, 34.97154818, 9.501e-05, 104.91464453, 0.00028502, 349.71548178, 0.00095008, -34.97154818, -9.501e-05, -104.91464453, -0.00028502, -349.71548178, -0.00095008, 0.4, 0.3, 0.003, 0.0, 0.0, 11014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1014, 99999, 'P', 41014, 'Vy', 31014, 'Vz', 21014, 'My', 11014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171014, 71014, 171014, 1014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122014, 122014, 22014, 1014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171015, 10.3, 10.5, 2.9)
    ops.node(122015, 10.3, 10.5, 4.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1015, 171015, 122015, 0.09, 30177516.60486295, 12573965.25202623, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21015, 42.94395686, 0.0006468, 51.85075911, 0.04263021, 5.18507591, 0.14245501, -42.94395686, -0.0006468, -51.85075911, -0.04263021, -5.18507591, -0.14245501, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11015, 40.12457468, 0.0006468, 48.44662225, 0.04263021, 4.84466223, 0.14245501, -40.12457468, -0.0006468, -48.44662225, -0.04263021, -4.84466223, -0.14245501, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21015, 1015, 0.0, 139.02967666, 0.01293608, 139.02967666, 0.03880823, 97.32077366, -3249.6954593, 0.05, 2, 0, 71015, 22015, 2, 3)
    ops.uniaxialMaterial('LimitState', 41015, 34.75741916, 9.583e-05, 104.27225749, 0.00028748, 347.57419164, 0.00095827, -34.75741916, -9.583e-05, -104.27225749, -0.00028748, -347.57419164, -0.00095827, 0.4, 0.3, 0.003, 0.0, 0.0, 21015, 2)
    ops.limitCurve('ThreePoint', 11015, 1015, 0.0, 139.02967666, 0.01293608, 139.02967666, 0.03880823, 97.32077366, -3249.6954593, 0.05, 2, 0, 71015, 22015, 1, 3)
    ops.uniaxialMaterial('LimitState', 31015, 34.75741916, 9.583e-05, 104.27225749, 0.00028748, 347.57419164, 0.00095827, -34.75741916, -9.583e-05, -104.27225749, -0.00028748, -347.57419164, -0.00095827, 0.4, 0.3, 0.003, 0.0, 0.0, 11015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1015, 99999, 'P', 41015, 'Vy', 31015, 'Vz', 21015, 'My', 11015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171015, 71015, 171015, 1015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122015, 122015, 22015, 1015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171016, 17.75, 10.5, 2.9)
    ops.node(122016, 17.75, 10.5, 4.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1016, 171016, 122016, 0.0625, 30607664.87715465, 12753193.69881444, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21016, 39.12799183, 0.00080652, 47.14622509, 0.04931697, 4.71462251, 0.14931697, -39.12799183, -0.00080652, -47.14622509, -0.04931697, -4.71462251, -0.14931697, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11016, 37.04202612, 0.00080652, 44.63279662, 0.04931697, 4.46327966, 0.14931697, -37.04202612, -0.00080652, -44.63279662, -0.04931697, -4.46327966, -0.14931697, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21016, 1016, 0.0, 108.86505842, 0.01613046, 108.86505842, 0.04839137, 76.20554089, -2727.08250661, 0.05, 2, 0, 71016, 22016, 2, 3)
    ops.uniaxialMaterial('LimitState', 41016, 27.21626461, 0.00010653, 81.64879382, 0.0003196, 272.16264605, 0.00106533, -27.21626461, -0.00010653, -81.64879382, -0.0003196, -272.16264605, -0.00106533, 0.4, 0.3, 0.003, 0.0, 0.0, 21016, 2)
    ops.limitCurve('ThreePoint', 11016, 1016, 0.0, 108.86505842, 0.01613046, 108.86505842, 0.04839137, 76.20554089, -2727.08250661, 0.05, 2, 0, 71016, 22016, 1, 3)
    ops.uniaxialMaterial('LimitState', 31016, 27.21626461, 0.00010653, 81.64879382, 0.0003196, 272.16264605, 0.00106533, -27.21626461, -0.00010653, -81.64879382, -0.0003196, -272.16264605, -0.00106533, 0.4, 0.3, 0.003, 0.0, 0.0, 11016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1016, 99999, 'P', 41016, 'Vy', 31016, 'Vz', 21016, 'My', 11016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171016, 71016, 171016, 1016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122016, 122016, 22016, 1016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172001, 0.0, 0.0, 5.5)
    ops.node(123001, 0.0, 0.0, 7.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2001, 172001, 123001, 0.0625, 30963576.5221842, 12901490.21757675, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22001, 29.08311094, 0.00076032, 35.12534626, 0.05011723, 3.51253463, 0.15011723, -29.08311094, -0.00076032, -35.12534626, -0.05011723, -3.51253463, -0.15011723, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12001, 29.08311094, 0.00076032, 35.12534626, 0.05011723, 3.51253463, 0.15011723, -29.08311094, -0.00076032, -35.12534626, -0.05011723, -3.51253463, -0.15011723, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22001, 2001, 0.0, 105.12012108, 0.01520641, 105.12012108, 0.04561922, 73.58408476, -3483.5074284, 0.05, 2, 0, 72001, 23001, 2, 3)
    ops.uniaxialMaterial('LimitState', 42001, 26.28003027, 0.00010169, 78.84009081, 0.00030506, 262.80030271, 0.00101686, -26.28003027, -0.00010169, -78.84009081, -0.00030506, -262.80030271, -0.00101686, 0.4, 0.3, 0.003, 0.0, 0.0, 22001, 2)
    ops.limitCurve('ThreePoint', 12001, 2001, 0.0, 105.12012108, 0.01520641, 105.12012108, 0.04561922, 73.58408476, -3483.5074284, 0.05, 2, 0, 72001, 23001, 1, 3)
    ops.uniaxialMaterial('LimitState', 32001, 26.28003027, 0.00010169, 78.84009081, 0.00030506, 262.80030271, 0.00101686, -26.28003027, -0.00010169, -78.84009081, -0.00030506, -262.80030271, -0.00101686, 0.4, 0.3, 0.003, 0.0, 0.0, 12001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2001, 99999, 'P', 42001, 'Vy', 32001, 'Vz', 22001, 'My', 12001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172001, 72001, 172001, 2001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123001, 123001, 23001, 2001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172002, 7.45, 0.0, 5.5)
    ops.node(123002, 7.45, 0.0, 7.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2002, 172002, 123002, 0.0625, 31248152.84991597, 13020063.68746499, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22002, 22.4849093, 0.0007199, 27.10254737, 0.03420907, 2.71025474, 0.12019688, -22.4849093, -0.0007199, -27.10254737, -0.03420907, -2.71025474, -0.12019688, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12002, 22.4849093, 0.0007199, 27.10254737, 0.03420907, 2.71025474, 0.12019688, -22.4849093, -0.0007199, -27.10254737, -0.03420907, -2.71025474, -0.12019688, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22002, 2002, 0.0, 87.57227198, 0.01439804, 87.57227198, 0.04319413, 61.30059039, -1775.52480031, 0.05, 2, 0, 72002, 23002, 2, 3)
    ops.uniaxialMaterial('LimitState', 42002, 21.893068, 8.394e-05, 65.67920399, 0.00025182, 218.93067996, 0.0008394, -21.893068, -8.394e-05, -65.67920399, -0.00025182, -218.93067996, -0.0008394, 0.4, 0.3, 0.003, 0.0, 0.0, 22002, 2)
    ops.limitCurve('ThreePoint', 12002, 2002, 0.0, 87.57227198, 0.01439804, 87.57227198, 0.04319413, 61.30059039, -1775.52480031, 0.05, 2, 0, 72002, 23002, 1, 3)
    ops.uniaxialMaterial('LimitState', 32002, 21.893068, 8.394e-05, 65.67920399, 0.00025182, 218.93067996, 0.0008394, -21.893068, -8.394e-05, -65.67920399, -0.00025182, -218.93067996, -0.0008394, 0.4, 0.3, 0.003, 0.0, 0.0, 12002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2002, 99999, 'P', 42002, 'Vy', 32002, 'Vz', 22002, 'My', 12002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172002, 72002, 172002, 2002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123002, 123002, 23002, 2002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172003, 10.3, 0.0, 5.5)
    ops.node(123003, 10.3, 0.0, 7.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2003, 172003, 123003, 0.0625, 30548724.20806331, 12728635.08669305, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22003, 22.46080037, 0.00070072, 27.12061208, 0.03408579, 2.71206121, 0.11888025, -22.46080037, -0.00070072, -27.12061208, -0.03408579, -2.71206121, -0.11888025, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12003, 22.46080037, 0.00070072, 27.12061208, 0.03408579, 2.71206121, 0.11888025, -22.46080037, -0.00070072, -27.12061208, -0.03408579, -2.71206121, -0.11888025, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22003, 2003, 0.0, 84.65235812, 0.01401438, 84.65235812, 0.04204313, 59.25665068, -1687.97906086, 0.05, 2, 0, 72003, 23003, 2, 3)
    ops.uniaxialMaterial('LimitState', 42003, 21.16308953, 8.3e-05, 63.48926859, 0.000249, 211.63089529, 0.00082999, -21.16308953, -8.3e-05, -63.48926859, -0.000249, -211.63089529, -0.00082999, 0.4, 0.3, 0.003, 0.0, 0.0, 22003, 2)
    ops.limitCurve('ThreePoint', 12003, 2003, 0.0, 84.65235812, 0.01401438, 84.65235812, 0.04204313, 59.25665068, -1687.97906086, 0.05, 2, 0, 72003, 23003, 1, 3)
    ops.uniaxialMaterial('LimitState', 32003, 21.16308953, 8.3e-05, 63.48926859, 0.000249, 211.63089529, 0.00082999, -21.16308953, -8.3e-05, -63.48926859, -0.000249, -211.63089529, -0.00082999, 0.4, 0.3, 0.003, 0.0, 0.0, 12003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2003, 99999, 'P', 42003, 'Vy', 32003, 'Vz', 22003, 'My', 12003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172003, 72003, 172003, 2003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123003, 123003, 23003, 2003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172004, 17.75, 0.0, 5.5)
    ops.node(123004, 17.75, 0.0, 7.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2004, 172004, 123004, 0.0625, 31663722.74928774, 13193217.81220322, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22004, 29.44323243, 0.00074256, 35.49181554, 0.05014509, 3.54918155, 0.15014509, -29.44323243, -0.00074256, -35.49181554, -0.05014509, -3.54918155, -0.15014509, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12004, 29.44323243, 0.00074256, 35.49181554, 0.05014509, 3.54918155, 0.15014509, -29.44323243, -0.00074256, -35.49181554, -0.05014509, -3.54918155, -0.15014509, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22004, 2004, 0.0, 107.72764742, 0.01485117, 107.72764742, 0.04455351, 75.40935319, -3595.74438424, 0.05, 2, 0, 72004, 23004, 2, 3)
    ops.uniaxialMaterial('LimitState', 42004, 26.93191186, 0.0001019, 80.79573557, 0.00030571, 269.31911855, 0.00101904, -26.93191186, -0.0001019, -80.79573557, -0.00030571, -269.31911855, -0.00101904, 0.4, 0.3, 0.003, 0.0, 0.0, 22004, 2)
    ops.limitCurve('ThreePoint', 12004, 2004, 0.0, 107.72764742, 0.01485117, 107.72764742, 0.04455351, 75.40935319, -3595.74438424, 0.05, 2, 0, 72004, 23004, 1, 3)
    ops.uniaxialMaterial('LimitState', 32004, 26.93191186, 0.0001019, 80.79573557, 0.00030571, 269.31911855, 0.00101904, -26.93191186, -0.0001019, -80.79573557, -0.00030571, -269.31911855, -0.00101904, 0.4, 0.3, 0.003, 0.0, 0.0, 12004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2004, 99999, 'P', 42004, 'Vy', 32004, 'Vz', 22004, 'My', 12004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172004, 72004, 172004, 2004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123004, 123004, 23004, 2004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172005, 0.0, 3.5, 5.5)
    ops.node(123005, 0.0, 3.5, 7.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2005, 172005, 123005, 0.0625, 31284154.91546357, 13035064.54810982, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22005, 39.20883064, 0.00078669, 47.18569914, 0.04948979, 4.71856991, 0.14948979, -39.20883064, -0.00078669, -47.18569914, -0.04948979, -4.71856991, -0.14948979, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12005, 37.01735349, 0.00078669, 44.54837537, 0.04948979, 4.45483754, 0.14948979, -37.01735349, -0.00078669, -44.54837537, -0.04948979, -4.45483754, -0.14948979, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22005, 2005, 0.0, 109.6512345, 0.01573372, 109.6512345, 0.04720117, 76.75586415, -2770.35967983, 0.05, 2, 0, 72005, 23005, 2, 3)
    ops.uniaxialMaterial('LimitState', 42005, 27.41280863, 0.00010498, 82.23842588, 0.00031495, 274.12808626, 0.00104982, -27.41280863, -0.00010498, -82.23842588, -0.00031495, -274.12808626, -0.00104982, 0.4, 0.3, 0.003, 0.0, 0.0, 22005, 2)
    ops.limitCurve('ThreePoint', 12005, 2005, 0.0, 109.6512345, 0.01573372, 109.6512345, 0.04720117, 76.75586415, -2770.35967983, 0.05, 2, 0, 72005, 23005, 1, 3)
    ops.uniaxialMaterial('LimitState', 32005, 27.41280863, 0.00010498, 82.23842588, 0.00031495, 274.12808626, 0.00104982, -27.41280863, -0.00010498, -82.23842588, -0.00031495, -274.12808626, -0.00104982, 0.4, 0.3, 0.003, 0.0, 0.0, 12005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2005, 99999, 'P', 42005, 'Vy', 32005, 'Vz', 22005, 'My', 12005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172005, 72005, 172005, 2005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123005, 123005, 23005, 2005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172008, 17.75, 3.5, 5.5)
    ops.node(123008, 17.75, 3.5, 7.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2008, 172008, 123008, 0.0625, 31336359.05442608, 13056816.27267753, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22008, 39.94539488, 0.00078083, 48.06593185, 0.04946956, 4.80659318, 0.14946956, -39.94539488, -0.00078083, -48.06593185, -0.04946956, -4.80659318, -0.14946956, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12008, 37.62426339, 0.00078083, 45.27293535, 0.04946956, 4.52729354, 0.14946956, -37.62426339, -0.00078083, -45.27293535, -0.04946956, -4.52729354, -0.14946956, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22008, 2008, 0.0, 110.79089535, 0.01561667, 110.79089535, 0.04685001, 77.55362674, -2836.09220537, 0.05, 2, 0, 72008, 23008, 2, 3)
    ops.uniaxialMaterial('LimitState', 42008, 27.69772384, 0.0001059, 83.09317151, 0.00031769, 276.97723837, 0.00105896, -27.69772384, -0.0001059, -83.09317151, -0.00031769, -276.97723837, -0.00105896, 0.4, 0.3, 0.003, 0.0, 0.0, 22008, 2)
    ops.limitCurve('ThreePoint', 12008, 2008, 0.0, 110.79089535, 0.01561667, 110.79089535, 0.04685001, 77.55362674, -2836.09220537, 0.05, 2, 0, 72008, 23008, 1, 3)
    ops.uniaxialMaterial('LimitState', 32008, 27.69772384, 0.0001059, 83.09317151, 0.00031769, 276.97723837, 0.00105896, -27.69772384, -0.0001059, -83.09317151, -0.00031769, -276.97723837, -0.00105896, 0.4, 0.3, 0.003, 0.0, 0.0, 12008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2008, 99999, 'P', 42008, 'Vy', 32008, 'Vz', 22008, 'My', 12008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172008, 72008, 172008, 2008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123008, 123008, 23008, 2008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172009, 0.0, 7.0, 5.5)
    ops.node(123009, 0.0, 7.0, 7.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2009, 172009, 123009, 0.09, 31055081.00501032, 12939617.08542097, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22009, 56.86646234, 0.0006611, 68.63078106, 0.05548308, 6.86307811, 0.15548308, -56.86646234, -0.0006611, -68.63078106, -0.05548308, -6.86307811, -0.15548308, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12009, 51.14719793, 0.0006611, 61.72833684, 0.04750691, 6.17283368, 0.14750691, -51.14719793, -0.0006611, -61.72833684, -0.04750691, -6.17283368, -0.14750691, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22009, 2009, 0.0, 138.81814401, 0.0132219, 138.81814401, 0.03966571, 97.17270081, -3681.89705924, 0.05, 2, 0, 72009, 23009, 2, 3)
    ops.uniaxialMaterial('LimitState', 42009, 34.704536, 9.298e-05, 104.11360801, 0.00027893, 347.04536002, 0.00092977, -34.704536, -9.298e-05, -104.11360801, -0.00027893, -347.04536002, -0.00092977, 0.4, 0.3, 0.003, 0.0, 0.0, 22009, 2)
    ops.limitCurve('ThreePoint', 12009, 2009, 0.0, 177.10604819, 0.0132219, 177.10604819, 0.03966571, 123.97423373, -6973.37117669, 0.05, 2, 0, 72009, 23009, 1, 3)
    ops.uniaxialMaterial('LimitState', 32009, 44.27651205, 0.00011862, 132.82953614, 0.00035587, 442.76512047, 0.00118622, -44.27651205, -0.00011862, -132.82953614, -0.00035587, -442.76512047, -0.00118622, 0.4, 0.3, 0.003, 0.0, 0.0, 12009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2009, 99999, 'P', 42009, 'Vy', 32009, 'Vz', 22009, 'My', 12009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172009, 72009, 172009, 2009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123009, 123009, 23009, 2009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172010, 7.45, 7.0, 5.5)
    ops.node(123010, 7.45, 7.0, 7.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2010, 172010, 123010, 0.0625, 32103288.56730719, 13376370.236378, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22010, 28.16162592, 0.00073623, 33.76767805, 0.03185726, 3.37676781, 0.11195872, -28.16162592, -0.00073623, -33.76767805, -0.03185726, -3.37676781, -0.11195872, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12010, 28.16162592, 0.00073623, 33.76767805, 0.03185726, 3.37676781, 0.11195872, -28.16162592, -0.00073623, -33.76767805, -0.03185726, -3.37676781, -0.11195872, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22010, 2010, 0.0, 92.14451438, 0.01472454, 92.14451438, 0.04417361, 64.50116007, -1528.49265877, 0.05, 2, 0, 72010, 23010, 2, 3)
    ops.uniaxialMaterial('LimitState', 42010, 23.0361286, 8.597e-05, 69.10838579, 0.00025791, 230.36128595, 0.0008597, -23.0361286, -8.597e-05, -69.10838579, -0.00025791, -230.36128595, -0.0008597, 0.4, 0.3, 0.003, 0.0, 0.0, 22010, 2)
    ops.limitCurve('ThreePoint', 12010, 2010, 0.0, 92.14451438, 0.01472454, 92.14451438, 0.04417361, 64.50116007, -1528.49265877, 0.05, 2, 0, 72010, 23010, 1, 3)
    ops.uniaxialMaterial('LimitState', 32010, 23.0361286, 8.597e-05, 69.10838579, 0.00025791, 230.36128595, 0.0008597, -23.0361286, -8.597e-05, -69.10838579, -0.00025791, -230.36128595, -0.0008597, 0.4, 0.3, 0.003, 0.0, 0.0, 12010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2010, 99999, 'P', 42010, 'Vy', 32010, 'Vz', 22010, 'My', 12010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172010, 72010, 172010, 2010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123010, 123010, 23010, 2010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172011, 10.3, 7.0, 5.5)
    ops.node(123011, 10.3, 7.0, 7.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2011, 172011, 123011, 0.0625, 31514330.31366819, 13130970.96402841, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22011, 28.19904112, 0.0007409, 33.86185002, 0.03189815, 3.386185, 0.1107387, -28.19904112, -0.0007409, -33.86185002, -0.03189815, -3.386185, -0.1107387, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12011, 28.19904112, 0.0007409, 33.86185002, 0.03189815, 3.386185, 0.1107387, -28.19904112, -0.0007409, -33.86185002, -0.03189815, -3.386185, -0.1107387, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22011, 2011, 0.0, 90.60886473, 0.01481793, 90.60886473, 0.04445379, 63.42620531, -1513.5856036, 0.05, 2, 0, 72011, 23011, 2, 3)
    ops.uniaxialMaterial('LimitState', 42011, 22.65221618, 8.612e-05, 67.95664855, 0.00025835, 226.52216183, 0.00086117, -22.65221618, -8.612e-05, -67.95664855, -0.00025835, -226.52216183, -0.00086117, 0.4, 0.3, 0.003, 0.0, 0.0, 22011, 2)
    ops.limitCurve('ThreePoint', 12011, 2011, 0.0, 90.60886473, 0.01481793, 90.60886473, 0.04445379, 63.42620531, -1513.5856036, 0.05, 2, 0, 72011, 23011, 1, 3)
    ops.uniaxialMaterial('LimitState', 32011, 22.65221618, 8.612e-05, 67.95664855, 0.00025835, 226.52216183, 0.00086117, -22.65221618, -8.612e-05, -67.95664855, -0.00025835, -226.52216183, -0.00086117, 0.4, 0.3, 0.003, 0.0, 0.0, 12011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2011, 99999, 'P', 42011, 'Vy', 32011, 'Vz', 22011, 'My', 12011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172011, 72011, 172011, 2011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123011, 123011, 23011, 2011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172012, 17.75, 7.0, 5.5)
    ops.node(123012, 17.75, 7.0, 7.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2012, 172012, 123012, 0.09, 30411888.6663686, 12671620.27765359, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22012, 56.53956802, 0.00067912, 68.34679536, 0.0558771, 6.83467954, 0.1558771, -56.53956802, -0.00067912, -68.34679536, -0.0558771, -6.83467954, -0.1558771, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12012, 51.02345504, 0.00067912, 61.67874573, 0.04784623, 6.16787457, 0.14784623, -51.02345504, -0.00067912, -61.67874573, -0.04784623, -6.16787457, -0.14784623, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22012, 2012, 0.0, 136.38541369, 0.01358231, 136.38541369, 0.04074693, 95.46978958, -3634.22411113, 0.05, 2, 0, 72012, 23012, 2, 3)
    ops.uniaxialMaterial('LimitState', 42012, 34.09635342, 9.328e-05, 102.28906027, 0.00027984, 340.96353422, 0.0009328, -34.09635342, -9.328e-05, -102.28906027, -0.00027984, -340.96353422, -0.0009328, 0.4, 0.3, 0.003, 0.0, 0.0, 22012, 2)
    ops.limitCurve('ThreePoint', 12012, 2012, 0.0, 174.34281049, 0.01358231, 174.34281049, 0.04074693, 122.03996734, -6874.9878404, 0.05, 2, 0, 72012, 23012, 1, 3)
    ops.uniaxialMaterial('LimitState', 32012, 43.58570262, 0.00011924, 130.75710787, 0.00035772, 435.85702622, 0.00119241, -43.58570262, -0.00011924, -130.75710787, -0.00035772, -435.85702622, -0.00119241, 0.4, 0.3, 0.003, 0.0, 0.0, 12012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2012, 99999, 'P', 42012, 'Vy', 32012, 'Vz', 22012, 'My', 12012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172012, 72012, 172012, 2012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123012, 123012, 23012, 2012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172013, 0.0, 10.5, 5.5)
    ops.node(123013, 0.0, 10.5, 7.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2013, 172013, 123013, 0.0625, 31822774.57256261, 13259489.40523442, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22013, 29.8842843, 0.00074208, 36.00693688, 0.04995601, 3.60069369, 0.14995601, -29.8842843, -0.00074208, -36.00693688, -0.04995601, -3.60069369, -0.14995601, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12013, 29.8842843, 0.00074208, 36.00693688, 0.04995601, 3.60069369, 0.14995601, -29.8842843, -0.00074208, -36.00693688, -0.04995601, -3.60069369, -0.14995601, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22013, 2013, 0.0, 110.12034709, 0.01484162, 110.12034709, 0.04452486, 77.08424296, -3785.67887738, 0.05, 2, 0, 72013, 23013, 2, 3)
    ops.uniaxialMaterial('LimitState', 42013, 27.53008677, 0.00010365, 82.59026031, 0.00031094, 275.30086771, 0.00103647, -27.53008677, -0.00010365, -82.59026031, -0.00031094, -275.30086771, -0.00103647, 0.4, 0.3, 0.003, 0.0, 0.0, 22013, 2)
    ops.limitCurve('ThreePoint', 12013, 2013, 0.0, 110.12034709, 0.01484162, 110.12034709, 0.04452486, 77.08424296, -3785.67887738, 0.05, 2, 0, 72013, 23013, 1, 3)
    ops.uniaxialMaterial('LimitState', 32013, 27.53008677, 0.00010365, 82.59026031, 0.00031094, 275.30086771, 0.00103647, -27.53008677, -0.00010365, -82.59026031, -0.00031094, -275.30086771, -0.00103647, 0.4, 0.3, 0.003, 0.0, 0.0, 12013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2013, 99999, 'P', 42013, 'Vy', 32013, 'Vz', 22013, 'My', 12013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172013, 72013, 172013, 2013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123013, 123013, 23013, 2013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172014, 7.45, 10.5, 5.5)
    ops.node(123014, 7.45, 10.5, 7.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2014, 172014, 123014, 0.0625, 33068103.77205007, 13778376.57168753, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22014, 22.63493178, 0.00070375, 27.13969717, 0.03285418, 2.71396972, 0.12151943, -22.63493178, -0.00070375, -27.13969717, -0.03285418, -2.71396972, -0.12151943, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12014, 22.63493178, 0.00070375, 27.13969717, 0.03285418, 2.71396972, 0.12151943, -22.63493178, -0.00070375, -27.13969717, -0.03285418, -2.71396972, -0.12151943, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22014, 2014, 0.0, 89.21408249, 0.01407506, 89.21408249, 0.04222518, 62.44985775, -1666.95875917, 0.05, 2, 0, 72014, 23014, 2, 3)
    ops.uniaxialMaterial('LimitState', 42014, 22.30352062, 8.081e-05, 66.91056187, 0.00024242, 223.03520624, 0.00080807, -22.30352062, -8.081e-05, -66.91056187, -0.00024242, -223.03520624, -0.00080807, 0.4, 0.3, 0.003, 0.0, 0.0, 22014, 2)
    ops.limitCurve('ThreePoint', 12014, 2014, 0.0, 89.21408249, 0.01407506, 89.21408249, 0.04222518, 62.44985775, -1666.95875917, 0.05, 2, 0, 72014, 23014, 1, 3)
    ops.uniaxialMaterial('LimitState', 32014, 22.30352062, 8.081e-05, 66.91056187, 0.00024242, 223.03520624, 0.00080807, -22.30352062, -8.081e-05, -66.91056187, -0.00024242, -223.03520624, -0.00080807, 0.4, 0.3, 0.003, 0.0, 0.0, 12014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2014, 99999, 'P', 42014, 'Vy', 32014, 'Vz', 22014, 'My', 12014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172014, 72014, 172014, 2014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123014, 123014, 23014, 2014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172015, 10.3, 10.5, 5.5)
    ops.node(123015, 10.3, 10.5, 7.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2015, 172015, 123015, 0.0625, 31324040.71323092, 13051683.63051288, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22015, 22.57636649, 0.00071928, 27.20738698, 0.03422477, 2.7207387, 0.12033614, -22.57636649, -0.00071928, -27.20738698, -0.03422477, -2.7207387, -0.12033614, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12015, 22.57636649, 0.00071928, 27.20738698, 0.03422477, 2.7207387, 0.12033614, -22.57636649, -0.00071928, -27.20738698, -0.03422477, -2.7207387, -0.12033614, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22015, 2015, 0.0, 87.64531775, 0.01438553, 87.64531775, 0.04315658, 61.35172242, -1771.32606697, 0.05, 2, 0, 72015, 23015, 2, 3)
    ops.uniaxialMaterial('LimitState', 42015, 21.91132944, 8.381e-05, 65.73398831, 0.00025142, 219.11329437, 0.00083806, -21.91132944, -8.381e-05, -65.73398831, -0.00025142, -219.11329437, -0.00083806, 0.4, 0.3, 0.003, 0.0, 0.0, 22015, 2)
    ops.limitCurve('ThreePoint', 12015, 2015, 0.0, 87.64531775, 0.01438553, 87.64531775, 0.04315658, 61.35172242, -1771.32606697, 0.05, 2, 0, 72015, 23015, 1, 3)
    ops.uniaxialMaterial('LimitState', 32015, 21.91132944, 8.381e-05, 65.73398831, 0.00025142, 219.11329437, 0.00083806, -21.91132944, -8.381e-05, -65.73398831, -0.00025142, -219.11329437, -0.00083806, 0.4, 0.3, 0.003, 0.0, 0.0, 12015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2015, 99999, 'P', 42015, 'Vy', 32015, 'Vz', 22015, 'My', 12015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172015, 72015, 172015, 2015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123015, 123015, 23015, 2015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172016, 17.75, 10.5, 5.5)
    ops.node(123016, 17.75, 10.5, 7.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2016, 172016, 123016, 0.0625, 32495598.19316168, 13539832.58048403, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22016, 28.6974737, 0.00075783, 34.50686694, 0.04916638, 3.45068669, 0.14916638, -28.6974737, -0.00075783, -34.50686694, -0.04916638, -3.45068669, -0.14916638, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12016, 28.6974737, 0.00075783, 34.50686694, 0.04916638, 3.45068669, 0.14916638, -28.6974737, -0.00075783, -34.50686694, -0.04916638, -3.45068669, -0.14916638, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22016, 2016, 0.0, 108.32756625, 0.01515668, 108.32756625, 0.04547003, 75.82929637, -3503.74701897, 0.05, 2, 0, 72016, 23016, 2, 3)
    ops.uniaxialMaterial('LimitState', 42016, 27.08189156, 9.985e-05, 81.24567468, 0.00029954, 270.81891562, 0.00099848, -27.08189156, -9.985e-05, -81.24567468, -0.00029954, -270.81891562, -0.00099848, 0.4, 0.3, 0.003, 0.0, 0.0, 22016, 2)
    ops.limitCurve('ThreePoint', 12016, 2016, 0.0, 108.32756625, 0.01515668, 108.32756625, 0.04547003, 75.82929637, -3503.74701897, 0.05, 2, 0, 72016, 23016, 1, 3)
    ops.uniaxialMaterial('LimitState', 32016, 27.08189156, 9.985e-05, 81.24567468, 0.00029954, 270.81891562, 0.00099848, -27.08189156, -9.985e-05, -81.24567468, -0.00029954, -270.81891562, -0.00099848, 0.4, 0.3, 0.003, 0.0, 0.0, 12016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2016, 99999, 'P', 42016, 'Vy', 32016, 'Vz', 22016, 'My', 12016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172016, 72016, 172016, 2016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123016, 123016, 23016, 2016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173001, 0.0, 0.0, 8.1)
    ops.node(124001, 0.0, 0.0, 10.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3001, 173001, 124001, 0.0625, 30942893.27039208, 12892872.1959967, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23001, 24.04130448, 0.000719, 29.14320056, 0.05340663, 2.91432006, 0.15340663, -24.04130448, -0.000719, -29.14320056, -0.05340663, -2.91432006, -0.15340663, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13001, 24.04130448, 0.000719, 29.14320056, 0.05340663, 2.91432006, 0.15340663, -24.04130448, -0.000719, -29.14320056, -0.05340663, -2.91432006, -0.15340663, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23001, 3001, 0.0, 101.05273478, 0.01437996, 101.05273478, 0.04313988, 70.73691434, -9970.10515344, 0.05, 2, 0, 73001, 24001, 2, 3)
    ops.uniaxialMaterial('LimitState', 43001, 25.26318369, 9.782e-05, 75.78955108, 0.00029345, 252.63183694, 0.00097817, -25.26318369, -9.782e-05, -75.78955108, -0.00029345, -252.63183694, -0.00097817, 0.4, 0.3, 0.003, 0.0, 0.0, 23001, 2)
    ops.limitCurve('ThreePoint', 13001, 3001, 0.0, 101.05273478, 0.01437996, 101.05273478, 0.04313988, 70.73691434, -9970.10515344, 0.05, 2, 0, 73001, 24001, 1, 3)
    ops.uniaxialMaterial('LimitState', 33001, 25.26318369, 9.782e-05, 75.78955108, 0.00029345, 252.63183694, 0.00097817, -25.26318369, -9.782e-05, -75.78955108, -0.00029345, -252.63183694, -0.00097817, 0.4, 0.3, 0.003, 0.0, 0.0, 13001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3001, 99999, 'P', 43001, 'Vy', 33001, 'Vz', 23001, 'My', 13001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173001, 73001, 173001, 3001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124001, 124001, 24001, 3001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173002, 7.45, 0.0, 8.1)
    ops.node(124002, 7.45, 0.0, 10.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3002, 173002, 124002, 0.0625, 31483339.01953378, 13118057.92480574, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23002, 15.71965666, 0.00066795, 19.01634004, 0.02770051, 1.901634, 0.1042809, -15.71965666, -0.00066795, -19.01634004, -0.02770051, -1.901634, -0.1042809, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13002, 15.71965666, 0.00066795, 19.01634004, 0.02770051, 1.901634, 0.1042809, -15.71965666, -0.00066795, -19.01634004, -0.02770051, -1.901634, -0.1042809, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23002, 3002, 0.0, 69.63571398, 0.01335899, 69.63571398, 0.04007698, 48.74499979, -2163.74323275, 0.05, 2, 0, 73002, 24002, 2, 3)
    ops.uniaxialMaterial('LimitState', 43002, 17.40892849, 6.625e-05, 52.22678548, 0.00019875, 174.08928495, 0.00066249, -17.40892849, -6.625e-05, -52.22678548, -0.00019875, -174.08928495, -0.00066249, 0.4, 0.3, 0.003, 0.0, 0.0, 23002, 2)
    ops.limitCurve('ThreePoint', 13002, 3002, 0.0, 69.63571398, 0.01335899, 69.63571398, 0.04007698, 48.74499979, -2163.74323275, 0.05, 2, 0, 73002, 24002, 1, 3)
    ops.uniaxialMaterial('LimitState', 33002, 17.40892849, 6.625e-05, 52.22678548, 0.00019875, 174.08928495, 0.00066249, -17.40892849, -6.625e-05, -52.22678548, -0.00019875, -174.08928495, -0.00066249, 0.4, 0.3, 0.003, 0.0, 0.0, 13002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3002, 99999, 'P', 43002, 'Vy', 33002, 'Vz', 23002, 'My', 13002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173002, 73002, 173002, 3002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124002, 124002, 24002, 3002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173003, 10.3, 0.0, 8.1)
    ops.node(124003, 10.3, 0.0, 10.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3003, 173003, 124003, 0.0625, 31152873.39708161, 12980363.91545067, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23003, 15.20367972, 0.00068205, 18.41090303, 0.02819703, 1.8410903, 0.104646, -15.20367972, -0.00068205, -18.41090303, -0.02819703, -1.8410903, -0.104646, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13003, 15.20367972, 0.00068205, 18.41090303, 0.02819703, 1.8410903, 0.104646, -15.20367972, -0.00068205, -18.41090303, -0.02819703, -1.8410903, -0.104646, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23003, 3003, 0.0, 69.87693105, 0.01364098, 69.87693105, 0.04092294, 48.91385174, -2268.0664262, 0.05, 2, 0, 73003, 24003, 2, 3)
    ops.uniaxialMaterial('LimitState', 43003, 17.46923276, 6.718e-05, 52.40769829, 0.00020155, 174.69232763, 0.00067183, -17.46923276, -6.718e-05, -52.40769829, -0.00020155, -174.69232763, -0.00067183, 0.4, 0.3, 0.003, 0.0, 0.0, 23003, 2)
    ops.limitCurve('ThreePoint', 13003, 3003, 0.0, 69.87693105, 0.01364098, 69.87693105, 0.04092294, 48.91385174, -2268.0664262, 0.05, 2, 0, 73003, 24003, 1, 3)
    ops.uniaxialMaterial('LimitState', 33003, 17.46923276, 6.718e-05, 52.40769829, 0.00020155, 174.69232763, 0.00067183, -17.46923276, -6.718e-05, -52.40769829, -0.00020155, -174.69232763, -0.00067183, 0.4, 0.3, 0.003, 0.0, 0.0, 13003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3003, 99999, 'P', 43003, 'Vy', 33003, 'Vz', 23003, 'My', 13003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173003, 73003, 173003, 3003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124003, 124003, 24003, 3003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173004, 17.75, 0.0, 8.1)
    ops.node(124004, 17.75, 0.0, 10.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3004, 173004, 124004, 0.0625, 31174754.26200213, 12989480.94250089, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23004, 23.84778091, 0.00071236, 28.8881207, 0.0531174, 2.88881207, 0.1531174, -23.84778091, -0.00071236, -28.8881207, -0.0531174, -2.88881207, -0.1531174, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13004, 23.84778091, 0.00071236, 28.8881207, 0.0531174, 2.88881207, 0.1531174, -23.84778091, -0.00071236, -28.8881207, -0.0531174, -2.88881207, -0.1531174, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23004, 3004, 0.0, 101.2500563, 0.01424722, 101.2500563, 0.04274165, 70.87503941, -9900.00675061, 0.05, 2, 0, 73004, 24004, 2, 3)
    ops.uniaxialMaterial('LimitState', 43004, 25.31251407, 9.728e-05, 75.93754222, 0.00029184, 253.12514075, 0.00097279, -25.31251407, -9.728e-05, -75.93754222, -0.00029184, -253.12514075, -0.00097279, 0.4, 0.3, 0.003, 0.0, 0.0, 23004, 2)
    ops.limitCurve('ThreePoint', 13004, 3004, 0.0, 101.2500563, 0.01424722, 101.2500563, 0.04274165, 70.87503941, -9900.00675061, 0.05, 2, 0, 73004, 24004, 1, 3)
    ops.uniaxialMaterial('LimitState', 33004, 25.31251407, 9.728e-05, 75.93754222, 0.00029184, 253.12514075, 0.00097279, -25.31251407, -9.728e-05, -75.93754222, -0.00029184, -253.12514075, -0.00097279, 0.4, 0.3, 0.003, 0.0, 0.0, 13004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3004, 99999, 'P', 43004, 'Vy', 33004, 'Vz', 23004, 'My', 13004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173004, 73004, 173004, 3004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124004, 124004, 24004, 3004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173005, 0.0, 3.5, 8.1)
    ops.node(124005, 0.0, 3.5, 10.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3005, 173005, 124005, 0.0625, 32047012.6643503, 13352921.94347929, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23005, 31.43487684, 0.00073609, 37.93812329, 0.06168895, 3.79381233, 0.16168895, -31.43487684, -0.00073609, -37.93812329, -0.06168895, -3.79381233, -0.16168895, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13005, 29.34950747, 0.00073609, 35.42133276, 0.05268485, 3.54213328, 0.15268485, -29.34950747, -0.00073609, -35.42133276, -0.05268485, -3.54213328, -0.15268485, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23005, 3005, 0.0, 103.2794438, 0.01472189, 103.2794438, 0.04416568, 72.29561066, -5880.5353154, 0.05, 2, 0, 73005, 24005, 2, 3)
    ops.uniaxialMaterial('LimitState', 43005, 25.81986095, 9.653e-05, 77.45958285, 0.00028958, 258.19860951, 0.00096528, -25.81986095, -9.653e-05, -77.45958285, -0.00028958, -258.19860951, -0.00096528, 0.4, 0.3, 0.003, 0.0, 0.0, 23005, 2)
    ops.limitCurve('ThreePoint', 13005, 3005, 0.0, 134.57770624, 0.01472189, 134.57770624, 0.04416568, 94.20439437, -12306.47453772, 0.05, 2, 0, 73005, 24005, 1, 3)
    ops.uniaxialMaterial('LimitState', 33005, 33.64442656, 0.00012578, 100.93327968, 0.00037734, 336.4442656, 0.0012578, -33.64442656, -0.00012578, -100.93327968, -0.00037734, -336.4442656, -0.0012578, 0.4, 0.3, 0.003, 0.0, 0.0, 13005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3005, 99999, 'P', 43005, 'Vy', 33005, 'Vz', 23005, 'My', 13005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173005, 73005, 173005, 3005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124005, 124005, 24005, 3005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173008, 17.75, 3.5, 8.1)
    ops.node(124008, 17.75, 3.5, 10.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3008, 173008, 124008, 0.0625, 31408112.04309945, 13086713.35129144, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23008, 31.61770649, 0.00073554, 38.23526176, 0.06287162, 3.82352618, 0.16287162, -31.61770649, -0.00073554, -38.23526176, -0.06287162, -3.82352618, -0.16287162, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13008, 29.47855058, 0.00073554, 35.64838259, 0.05369274, 3.56483826, 0.15369274, -29.47855058, -0.00073554, -35.64838259, -0.05369274, -3.56483826, -0.15369274, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23008, 3008, 0.0, 104.1364986, 0.01471071, 104.1364986, 0.04413214, 72.89554902, -6235.47061312, 0.05, 2, 0, 73008, 24008, 2, 3)
    ops.uniaxialMaterial('LimitState', 43008, 26.03412465, 9.931e-05, 78.10237395, 0.00029793, 260.3412465, 0.00099309, -26.03412465, -9.931e-05, -78.10237395, -0.00029793, -260.3412465, -0.00099309, 0.4, 0.3, 0.003, 0.0, 0.0, 23008, 2)
    ops.limitCurve('ThreePoint', 13008, 3008, 0.0, 136.47667523, 0.01471071, 136.47667523, 0.04413214, 95.53367266, -13077.08252284, 0.05, 2, 0, 73008, 24008, 1, 3)
    ops.uniaxialMaterial('LimitState', 33008, 34.11916881, 0.00013015, 102.35750642, 0.00039045, 341.19168807, 0.00130149, -34.11916881, -0.00013015, -102.35750642, -0.00039045, -341.19168807, -0.00130149, 0.4, 0.3, 0.003, 0.0, 0.0, 13008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3008, 99999, 'P', 43008, 'Vy', 33008, 'Vz', 23008, 'My', 13008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173008, 73008, 173008, 3008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124008, 124008, 24008, 3008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173009, 0.0, 7.0, 8.1)
    ops.node(124009, 0.0, 7.0, 10.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3009, 173009, 124009, 0.09, 32945460.92006255, 13727275.3833594, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23009, 46.19592548, 0.00062023, 55.61637341, 0.05692568, 5.56163734, 0.15692568, -46.19592548, -0.00062023, -55.61637341, -0.05692568, -5.56163734, -0.15692568, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13009, 40.93346892, 0.00062023, 49.28077679, 0.04873368, 4.92807768, 0.14873368, -40.93346892, -0.00062023, -49.28077679, -0.04873368, -4.92807768, -0.14873368, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23009, 3009, 0.0, 136.43600675, 0.01240452, 136.43600675, 0.03721356, 95.50520473, -8425.31640062, 0.05, 2, 0, 73009, 24009, 2, 3)
    ops.uniaxialMaterial('LimitState', 43009, 34.10900169, 8.614e-05, 102.32700507, 0.00025842, 341.09001689, 0.00086138, -34.10900169, -8.614e-05, -102.32700507, -0.00025842, -341.09001689, -0.00086138, 0.4, 0.3, 0.003, 0.0, 0.0, 23009, 2)
    ops.limitCurve('ThreePoint', 13009, 3009, 0.0, 174.86408193, 0.01240452, 174.86408193, 0.03721356, 122.40485735, -17839.53879003, 0.05, 2, 0, 73009, 24009, 1, 3)
    ops.uniaxialMaterial('LimitState', 33009, 43.71602048, 0.0001104, 131.14806145, 0.0003312, 437.16020483, 0.001104, -43.71602048, -0.0001104, -131.14806145, -0.0003312, -437.16020483, -0.001104, 0.4, 0.3, 0.003, 0.0, 0.0, 13009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3009, 99999, 'P', 43009, 'Vy', 33009, 'Vz', 23009, 'My', 13009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173009, 73009, 173009, 3009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124009, 124009, 24009, 3009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173010, 7.45, 7.0, 8.1)
    ops.node(124010, 7.45, 7.0, 10.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3010, 173010, 124010, 0.0625, 31428542.7167109, 13095226.13196287, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23010, 18.30564054, 0.00068577, 22.11469952, 0.02757469, 2.21146995, 0.10073275, -18.30564054, -0.00068577, -22.11469952, -0.02757469, -2.21146995, -0.10073275, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13010, 18.30564054, 0.00068577, 22.11469952, 0.02757469, 2.21146995, 0.10073275, -18.30564054, -0.00068577, -22.11469952, -0.02757469, -2.21146995, -0.10073275, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23010, 3010, 0.0, 72.80995696, 0.01371544, 72.80995696, 0.04114631, 50.96696987, -1514.58472202, 0.05, 2, 0, 73010, 24010, 2, 3)
    ops.uniaxialMaterial('LimitState', 43010, 18.20248924, 6.939e-05, 54.60746772, 0.00020817, 182.02489241, 0.00069389, -18.20248924, -6.939e-05, -54.60746772, -0.00020817, -182.02489241, -0.00069389, 0.4, 0.3, 0.003, 0.0, 0.0, 23010, 2)
    ops.limitCurve('ThreePoint', 13010, 3010, 0.0, 72.80995696, 0.01371544, 72.80995696, 0.04114631, 50.96696987, -1514.58472202, 0.05, 2, 0, 73010, 24010, 1, 3)
    ops.uniaxialMaterial('LimitState', 33010, 18.20248924, 6.939e-05, 54.60746772, 0.00020817, 182.02489241, 0.00069389, -18.20248924, -6.939e-05, -54.60746772, -0.00020817, -182.02489241, -0.00069389, 0.4, 0.3, 0.003, 0.0, 0.0, 13010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3010, 99999, 'P', 43010, 'Vy', 33010, 'Vz', 23010, 'My', 13010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173010, 73010, 173010, 3010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124010, 124010, 24010, 3010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173011, 10.3, 7.0, 8.1)
    ops.node(124011, 10.3, 7.0, 10.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3011, 173011, 124011, 0.0625, 30043662.11403469, 12518192.54751446, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23011, 18.22516929, 0.00069632, 22.10152455, 0.02804343, 2.21015245, 0.10009884, -18.22516929, -0.00069632, -22.10152455, -0.02804343, -2.21015245, -0.10009884, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13011, 18.22516929, 0.00069632, 22.10152455, 0.02804343, 2.21015245, 0.10009884, -18.22516929, -0.00069632, -22.10152455, -0.02804343, -2.21015245, -0.10009884, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23011, 3011, 0.0, 70.09569815, 0.01392633, 70.09569815, 0.04177898, 49.0669887, -1507.62933605, 0.05, 2, 0, 73011, 24011, 2, 3)
    ops.uniaxialMaterial('LimitState', 43011, 17.52392454, 6.988e-05, 52.57177361, 0.00020965, 175.23924536, 0.00069882, -17.52392454, -6.988e-05, -52.57177361, -0.00020965, -175.23924536, -0.00069882, 0.4, 0.3, 0.003, 0.0, 0.0, 23011, 2)
    ops.limitCurve('ThreePoint', 13011, 3011, 0.0, 70.09569815, 0.01392633, 70.09569815, 0.04177898, 49.0669887, -1507.62933605, 0.05, 2, 0, 73011, 24011, 1, 3)
    ops.uniaxialMaterial('LimitState', 33011, 17.52392454, 6.988e-05, 52.57177361, 0.00020965, 175.23924536, 0.00069882, -17.52392454, -6.988e-05, -52.57177361, -0.00020965, -175.23924536, -0.00069882, 0.4, 0.3, 0.003, 0.0, 0.0, 13011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3011, 99999, 'P', 43011, 'Vy', 33011, 'Vz', 23011, 'My', 13011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173011, 73011, 173011, 3011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124011, 124011, 24011, 3011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173012, 17.75, 7.0, 8.1)
    ops.node(124012, 17.75, 7.0, 10.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3012, 173012, 124012, 0.09, 31004692.3099101, 12918621.79579588, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23012, 45.85245993, 0.00062159, 55.5541067, 0.05920558, 5.55541067, 0.15920558, -45.85245993, -0.00062159, -55.5541067, -0.05920558, -5.55541067, -0.15920558, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13012, 40.53114726, 0.00062159, 49.10688943, 0.05068208, 4.91068894, 0.15068208, -40.53114726, -0.00062159, -49.10688943, -0.05068208, -4.91068894, -0.15068208, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23012, 3012, 0.0, 132.42383053, 0.0124319, 132.42383053, 0.0372957, 92.69668137, -8700.84572602, 0.05, 2, 0, 73012, 24012, 2, 3)
    ops.uniaxialMaterial('LimitState', 43012, 33.10595763, 8.884e-05, 99.3178729, 0.00026652, 331.05957632, 0.00088839, -33.10595763, -8.884e-05, -99.3178729, -0.00026652, -331.05957632, -0.00088839, 0.4, 0.3, 0.003, 0.0, 0.0, 23012, 2)
    ops.limitCurve('ThreePoint', 13012, 3012, 0.0, 171.53666323, 0.0124319, 171.53666323, 0.0372957, 120.07566426, -18441.08020593, 0.05, 2, 0, 73012, 24012, 1, 3)
    ops.uniaxialMaterial('LimitState', 33012, 42.88416581, 0.00011508, 128.65249742, 0.00034523, 428.84165806, 0.00115078, -42.88416581, -0.00011508, -128.65249742, -0.00034523, -428.84165806, -0.00115078, 0.4, 0.3, 0.003, 0.0, 0.0, 13012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3012, 99999, 'P', 43012, 'Vy', 33012, 'Vz', 23012, 'My', 13012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173012, 73012, 173012, 3012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124012, 124012, 24012, 3012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173013, 0.0, 10.5, 8.1)
    ops.node(124013, 0.0, 10.5, 10.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3013, 173013, 124013, 0.0625, 32316821.6758344, 13465342.364931, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23013, 23.32517947, 0.00070747, 28.1507753, 0.05166846, 2.81507753, 0.15166846, -23.32517947, -0.00070747, -28.1507753, -0.05166846, -2.81507753, -0.15166846, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13013, 23.32517947, 0.00070747, 28.1507753, 0.05166846, 2.81507753, 0.15166846, -23.32517947, -0.00070747, -28.1507753, -0.05166846, -2.81507753, -0.15166846, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23013, 3013, 0.0, 100.62025849, 0.01414942, 100.62025849, 0.04244827, 70.43418094, -9096.77870927, 0.05, 2, 0, 73013, 24013, 2, 3)
    ops.uniaxialMaterial('LimitState', 43013, 25.15506462, 9.326e-05, 75.46519387, 0.00027977, 251.55064622, 0.00093257, -25.15506462, -9.326e-05, -75.46519387, -0.00027977, -251.55064622, -0.00093257, 0.4, 0.3, 0.003, 0.0, 0.0, 23013, 2)
    ops.limitCurve('ThreePoint', 13013, 3013, 0.0, 100.62025849, 0.01414942, 100.62025849, 0.04244827, 70.43418094, -9096.77870927, 0.05, 2, 0, 73013, 24013, 1, 3)
    ops.uniaxialMaterial('LimitState', 33013, 25.15506462, 9.326e-05, 75.46519387, 0.00027977, 251.55064622, 0.00093257, -25.15506462, -9.326e-05, -75.46519387, -0.00027977, -251.55064622, -0.00093257, 0.4, 0.3, 0.003, 0.0, 0.0, 13013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3013, 99999, 'P', 43013, 'Vy', 33013, 'Vz', 23013, 'My', 13013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173013, 73013, 173013, 3013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124013, 124013, 24013, 3013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173014, 7.45, 10.5, 8.1)
    ops.node(124014, 7.45, 10.5, 10.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3014, 173014, 124014, 0.0625, 31101968.76518072, 12959153.65215863, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23014, 15.45588305, 0.00067096, 18.71919811, 0.0283499, 1.87191981, 0.10477811, -15.45588305, -0.00067096, -18.71919811, -0.0283499, -1.87191981, -0.10477811, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13014, 15.45588305, 0.00067096, 18.71919811, 0.0283499, 1.87191981, 0.10477811, -15.45588305, -0.00067096, -18.71919811, -0.0283499, -1.87191981, -0.10477811, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23014, 3014, 0.0, 69.38851941, 0.01341929, 69.38851941, 0.04025786, 48.57196358, -2220.69841767, 0.05, 2, 0, 73014, 24014, 2, 3)
    ops.uniaxialMaterial('LimitState', 43014, 17.34712985, 6.682e-05, 52.04138955, 0.00020047, 173.47129851, 0.00066823, -17.34712985, -6.682e-05, -52.04138955, -0.00020047, -173.47129851, -0.00066823, 0.4, 0.3, 0.003, 0.0, 0.0, 23014, 2)
    ops.limitCurve('ThreePoint', 13014, 3014, 0.0, 69.38851941, 0.01341929, 69.38851941, 0.04025786, 48.57196358, -2220.69841767, 0.05, 2, 0, 73014, 24014, 1, 3)
    ops.uniaxialMaterial('LimitState', 33014, 17.34712985, 6.682e-05, 52.04138955, 0.00020047, 173.47129851, 0.00066823, -17.34712985, -6.682e-05, -52.04138955, -0.00020047, -173.47129851, -0.00066823, 0.4, 0.3, 0.003, 0.0, 0.0, 13014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3014, 99999, 'P', 43014, 'Vy', 33014, 'Vz', 23014, 'My', 13014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173014, 73014, 173014, 3014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124014, 124014, 24014, 3014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173015, 10.3, 10.5, 8.1)
    ops.node(124015, 10.3, 10.5, 10.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3015, 173015, 124015, 0.0625, 29567543.18400541, 12319809.66000226, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23015, 15.23545903, 0.00067964, 18.5323699, 0.02870194, 1.85323699, 0.10443181, -15.23545903, -0.00067964, -18.5323699, -0.02870194, -1.85323699, -0.10443181, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13015, 15.23545903, 0.00067964, 18.5323699, 0.02870194, 1.85323699, 0.10443181, -15.23545903, -0.00067964, -18.5323699, -0.02870194, -1.85323699, -0.10443181, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23015, 3015, 0.0, 66.05014387, 0.01359283, 66.05014387, 0.04077849, 46.23510071, -2162.96503904, 0.05, 2, 0, 73015, 24015, 2, 3)
    ops.uniaxialMaterial('LimitState', 43015, 16.51253597, 6.691e-05, 49.53760791, 0.00020073, 165.12535969, 0.00066909, -16.51253597, -6.691e-05, -49.53760791, -0.00020073, -165.12535969, -0.00066909, 0.4, 0.3, 0.003, 0.0, 0.0, 23015, 2)
    ops.limitCurve('ThreePoint', 13015, 3015, 0.0, 66.05014387, 0.01359283, 66.05014387, 0.04077849, 46.23510071, -2162.96503904, 0.05, 2, 0, 73015, 24015, 1, 3)
    ops.uniaxialMaterial('LimitState', 33015, 16.51253597, 6.691e-05, 49.53760791, 0.00020073, 165.12535969, 0.00066909, -16.51253597, -6.691e-05, -49.53760791, -0.00020073, -165.12535969, -0.00066909, 0.4, 0.3, 0.003, 0.0, 0.0, 13015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3015, 99999, 'P', 43015, 'Vy', 33015, 'Vz', 23015, 'My', 13015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173015, 73015, 173015, 3015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124015, 124015, 24015, 3015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173016, 17.75, 10.5, 8.1)
    ops.node(124016, 17.75, 10.5, 10.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3016, 173016, 124016, 0.0625, 30688354.94502965, 12786814.56042902, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23016, 24.04963231, 0.00072054, 29.17552814, 0.05357249, 2.91755281, 0.15357249, -24.04963231, -0.00072054, -29.17552814, -0.05357249, -2.91755281, -0.15357249, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13016, 24.04963231, 0.00072054, 29.17552814, 0.05357249, 2.91755281, 0.15357249, -24.04963231, -0.00072054, -29.17552814, -0.05357249, -2.91755281, -0.15357249, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23016, 3016, 0.0, 100.35499089, 0.01441074, 100.35499089, 0.04323223, 70.24849362, -9905.97969156, 0.05, 2, 0, 73016, 24016, 2, 3)
    ops.uniaxialMaterial('LimitState', 43016, 25.08874772, 9.795e-05, 75.26624317, 0.00029384, 250.88747723, 0.00097947, -25.08874772, -9.795e-05, -75.26624317, -0.00029384, -250.88747723, -0.00097947, 0.4, 0.3, 0.003, 0.0, 0.0, 23016, 2)
    ops.limitCurve('ThreePoint', 13016, 3016, 0.0, 100.35499089, 0.01441074, 100.35499089, 0.04323223, 70.24849362, -9905.97969156, 0.05, 2, 0, 73016, 24016, 1, 3)
    ops.uniaxialMaterial('LimitState', 33016, 25.08874772, 9.795e-05, 75.26624317, 0.00029384, 250.88747723, 0.00097947, -25.08874772, -9.795e-05, -75.26624317, -0.00029384, -250.88747723, -0.00097947, 0.4, 0.3, 0.003, 0.0, 0.0, 13016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3016, 99999, 'P', 43016, 'Vy', 33016, 'Vz', 23016, 'My', 13016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173016, 73016, 173016, 3016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124016, 124016, 24016, 3016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170006, 7.45, 3.5, 0.0)
    ops.node(124017, 7.45, 3.5, 1.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4041, 170006, 124017, 0.1225, 29948019.45604256, 12478341.44001773, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24041, 110.18143251, 0.00052841, 132.57815707, 0.04945057, 13.25781571, 0.14945057, -110.18143251, -0.00052841, -132.57815707, -0.04945057, -13.25781571, -0.14945057, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14041, 114.15618787, 0.00052841, 137.36086618, 0.04945057, 13.73608662, 0.14945057, -114.15618787, -0.00052841, -137.36086618, -0.04945057, -13.73608662, -0.14945057, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24041, 4041, 0.0, 294.25040931, 0.01056817, 294.25040931, 0.03170451, 205.97528652, -10809.04379807, 0.05, 2, 0, 70006, 24017, 2, 3)
    ops.uniaxialMaterial('LimitState', 44041, 73.56260233, 7.507e-05, 220.68780698, 0.00022522, 735.62602328, 0.00075074, -73.56260233, -7.507e-05, -220.68780698, -0.00022522, -735.62602328, -0.00075074, 0.4, 0.3, 0.003, 0.0, 0.0, 24041, 2)
    ops.limitCurve('ThreePoint', 14041, 4041, 0.0, 294.25040931, 0.01056817, 294.25040931, 0.03170451, 205.97528652, -10809.04379807, 0.05, 2, 0, 70006, 24017, 1, 3)
    ops.uniaxialMaterial('LimitState', 34041, 73.56260233, 7.507e-05, 220.68780698, 0.00022522, 735.62602328, 0.00075074, -73.56260233, -7.507e-05, -220.68780698, -0.00022522, -735.62602328, -0.00075074, 0.4, 0.3, 0.003, 0.0, 0.0, 14041, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4041, 99999, 'P', 44041, 'Vy', 34041, 'Vz', 24041, 'My', 14041, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170006, 70006, 170006, 4041, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124017, 124017, 24017, 4041, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174017, 7.45, 3.5, 1.45)
    ops.node(121006, 7.45, 3.5, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4042, 174017, 121006, 0.1225, 33767245.88513639, 14069685.7854735, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24042, 101.01692998, 0.00052239, 120.49423002, 0.05255, 12.049423, 0.15255, -101.01692998, -0.00052239, -120.49423002, -0.05255, -12.049423, -0.15255, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14042, 91.02835361, 0.00052239, 108.57973392, 0.04696619, 10.85797339, 0.14696619, -91.02835361, -0.00052239, -108.57973392, -0.04696619, -10.85797339, -0.14696619, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24042, 4042, 0.0, 316.09681671, 0.01044773, 316.09681671, 0.03134319, 221.2677717, -10745.75380516, 0.05, 2, 0, 74017, 21006, 2, 3)
    ops.uniaxialMaterial('LimitState', 44042, 79.02420418, 7.153e-05, 237.07261253, 0.00021458, 790.24204177, 0.00071526, -79.02420418, -7.153e-05, -237.07261253, -0.00021458, -790.24204177, -0.00071526, 0.4, 0.3, 0.003, 0.0, 0.0, 24042, 2)
    ops.limitCurve('ThreePoint', 14042, 4042, 0.0, 359.98386744, 0.01044773, 359.98386744, 0.03134319, 251.98870721, -16122.64430064, 0.05, 2, 0, 74017, 21006, 1, 3)
    ops.uniaxialMaterial('LimitState', 34042, 89.99596686, 8.146e-05, 269.98790058, 0.00024437, 899.9596686, 0.00081457, -89.99596686, -8.146e-05, -269.98790058, -0.00024437, -899.9596686, -0.00081457, 0.4, 0.3, 0.003, 0.0, 0.0, 14042, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4042, 99999, 'P', 44042, 'Vy', 34042, 'Vz', 24042, 'My', 14042, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174017, 74017, 174017, 4042, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121006, 121006, 21006, 4042, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170007, 10.3, 3.5, 0.0)
    ops.node(124018, 10.3, 3.5, 1.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4043, 170007, 124018, 0.1225, 33150804.88457468, 13812835.36857278, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24043, 111.38699931, 0.00051634, 133.05964424, 0.04835651, 13.30596442, 0.14835651, -111.38699931, -0.00051634, -133.05964424, -0.04835651, -13.30596442, -0.14835651, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14043, 115.31929652, 0.00051634, 137.75705121, 0.04835651, 13.77570512, 0.14835651, -115.31929652, -0.00051634, -137.75705121, -0.04835651, -13.77570512, -0.14835651, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24043, 4043, 0.0, 312.50885812, 0.01032676, 312.50885812, 0.03098029, 218.75620068, -10430.39310798, 0.05, 2, 0, 70007, 24018, 2, 3)
    ops.uniaxialMaterial('LimitState', 44043, 78.12721453, 7.203e-05, 234.38164359, 0.00021609, 781.2721453, 0.00072029, -78.12721453, -7.203e-05, -234.38164359, -0.00021609, -781.2721453, -0.00072029, 0.4, 0.3, 0.003, 0.0, 0.0, 24043, 2)
    ops.limitCurve('ThreePoint', 14043, 4043, 0.0, 312.50885812, 0.01032676, 312.50885812, 0.03098029, 218.75620068, -10430.39310798, 0.05, 2, 0, 70007, 24018, 1, 3)
    ops.uniaxialMaterial('LimitState', 34043, 78.12721453, 7.203e-05, 234.38164359, 0.00021609, 781.2721453, 0.00072029, -78.12721453, -7.203e-05, -234.38164359, -0.00021609, -781.2721453, -0.00072029, 0.4, 0.3, 0.003, 0.0, 0.0, 14043, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4043, 99999, 'P', 44043, 'Vy', 34043, 'Vz', 24043, 'My', 14043, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170007, 70007, 170007, 4043, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124018, 124018, 24018, 4043, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174018, 10.3, 3.5, 1.45)
    ops.node(121007, 10.3, 3.5, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4044, 174018, 121007, 0.1225, 32125868.56503624, 13385778.5687651, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24044, 101.98954441, 0.00051563, 122.22337273, 0.0537568, 12.22233727, 0.1537568, -101.98954441, -0.00051563, -122.22337273, -0.0537568, -12.22233727, -0.1537568, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14044, 91.02907955, 0.00051563, 109.08844807, 0.04804274, 10.90884481, 0.14804274, -91.02907955, -0.00051563, -109.08844807, -0.04804274, -10.90884481, -0.14804274, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24044, 4044, 0.0, 306.13637186, 0.01031258, 306.13637186, 0.03093774, 214.2954603, -10904.46893694, 0.05, 2, 0, 74018, 21007, 2, 3)
    ops.uniaxialMaterial('LimitState', 44044, 76.53409297, 7.281e-05, 229.6022789, 0.00021843, 765.34092966, 0.00072811, -76.53409297, -7.281e-05, -229.6022789, -0.00021843, -765.34092966, -0.00072811, 0.4, 0.3, 0.003, 0.0, 0.0, 24044, 2)
    ops.limitCurve('ThreePoint', 14044, 4044, 0.0, 350.50203885, 0.01031258, 350.50203885, 0.03093774, 245.35142719, -16381.94140479, 0.05, 2, 0, 74018, 21007, 1, 3)
    ops.uniaxialMaterial('LimitState', 34044, 87.62550971, 8.336e-05, 262.87652914, 0.00025009, 876.25509712, 0.00083363, -87.62550971, -8.336e-05, -262.87652914, -0.00025009, -876.25509712, -0.00083363, 0.4, 0.3, 0.003, 0.0, 0.0, 14044, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4044, 99999, 'P', 44044, 'Vy', 34044, 'Vz', 24044, 'My', 14044, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174018, 74018, 174018, 4044, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121007, 121007, 21007, 4044, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171006, 7.45, 3.5, 2.9)
    ops.node(124019, 7.45, 3.5, 3.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4046, 171006, 124019, 0.1225, 31567460.13475573, 13153108.38948155, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24046, 75.74019418, 0.00050245, 91.08329271, 0.04837634, 9.10832927, 0.14837634, -75.74019418, -0.00050245, -91.08329271, -0.04837634, -9.10832927, -0.14837634, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14046, 72.24930478, 0.00050245, 86.88523507, 0.04151463, 8.68852351, 0.12948328, -72.24930478, -0.00050245, -86.88523507, -0.04151463, -8.68852351, -0.12948328, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24046, 4046, 0.0, 248.85984132, 0.01004908, 248.85984132, 0.03014723, 174.20188893, -6971.89137314, 0.05, 2, 0, 71006, 24019, 2, 3)
    ops.uniaxialMaterial('LimitState', 44046, 62.21496033, 6.024e-05, 186.64488099, 0.00018071, 622.14960331, 0.00060236, -62.21496033, -6.024e-05, -186.64488099, -0.00018071, -622.14960331, -0.00060236, 0.4, 0.3, 0.003, 0.0, 0.0, 24046, 2)
    ops.limitCurve('ThreePoint', 14046, 4046, 0.0, 293.42644062, 0.01004908, 293.42644062, 0.03014723, 205.39850844, -12192.53428427, 0.05, 2, 0, 71006, 24019, 1, 3)
    ops.uniaxialMaterial('LimitState', 34046, 73.35661016, 7.102e-05, 220.06983047, 0.00021307, 733.56610156, 0.00071023, -73.35661016, -7.102e-05, -220.06983047, -0.00021307, -733.56610156, -0.00071023, 0.4, 0.3, 0.003, 0.0, 0.0, 14046, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4046, 99999, 'P', 44046, 'Vy', 34046, 'Vz', 24046, 'My', 14046, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171006, 71006, 171006, 4046, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124019, 124019, 24019, 4046, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174019, 7.45, 3.5, 4.05)
    ops.node(122006, 7.45, 3.5, 4.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4047, 174019, 122006, 0.1225, 32010235.18021073, 13337597.99175447, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24047, 82.70497691, 0.00050423, 99.38738379, 0.04891482, 9.93873838, 0.14891482, -82.70497691, -0.00050423, -99.38738379, -0.04891482, -9.93873838, -0.14891482, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14047, 75.6120665, 0.00050423, 90.86376362, 0.04197619, 9.08637636, 0.13199666, -75.6120665, -0.00050423, -90.86376362, -0.04197619, -9.08637636, -0.13199666, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24047, 4047, 0.0, 248.32234162, 0.0100847, 248.32234162, 0.0302541, 173.82563913, -6974.43150285, 0.05, 2, 0, 74019, 22006, 2, 3)
    ops.uniaxialMaterial('LimitState', 44047, 62.0805854, 5.927e-05, 186.24175621, 0.00017782, 620.80585405, 0.00059274, -62.0805854, -5.927e-05, -186.24175621, -0.00017782, -620.80585405, -0.00059274, 0.4, 0.3, 0.003, 0.0, 0.0, 24047, 2)
    ops.limitCurve('ThreePoint', 14047, 4047, 0.0, 292.22168733, 0.0100847, 292.22168733, 0.0302541, 204.55518113, -12304.66916559, 0.05, 2, 0, 74019, 22006, 1, 3)
    ops.uniaxialMaterial('LimitState', 34047, 73.05542183, 6.975e-05, 219.1662655, 0.00020926, 730.55421833, 0.00069753, -73.05542183, -6.975e-05, -219.1662655, -0.00020926, -730.55421833, -0.00069753, 0.4, 0.3, 0.003, 0.0, 0.0, 14047, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4047, 99999, 'P', 44047, 'Vy', 34047, 'Vz', 24047, 'My', 14047, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174019, 74019, 174019, 4047, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122006, 122006, 22006, 4047, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171007, 10.3, 3.5, 2.9)
    ops.node(124020, 10.3, 3.5, 3.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4048, 171007, 124020, 0.1225, 30437284.81080484, 12682202.00450202, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24048, 76.61157318, 0.00050235, 92.37649302, 0.0487888, 9.2376493, 0.1487888, -76.61157318, -0.00050235, -92.37649302, -0.0487888, -9.2376493, -0.1487888, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14048, 72.88682604, 0.00050235, 87.88527761, 0.04186796, 8.78852776, 0.12741308, -72.88682604, -0.00050235, -87.88527761, -0.04186796, -8.78852776, -0.12741308, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24048, 4048, 0.0, 242.33381579, 0.01004701, 242.33381579, 0.03014102, 169.63367105, -7066.51441109, 0.05, 2, 0, 71007, 24020, 2, 3)
    ops.uniaxialMaterial('LimitState', 44048, 60.58345395, 6.083e-05, 181.75036184, 0.0001825, 605.83453948, 0.00060834, -60.58345395, -6.083e-05, -181.75036184, -0.0001825, -605.83453948, -0.00060834, 0.4, 0.3, 0.003, 0.0, 0.0, 24048, 2)
    ops.limitCurve('ThreePoint', 14048, 4048, 0.0, 287.36782546, 0.01004701, 287.36782546, 0.03014102, 201.15747782, -12380.31730693, 0.05, 2, 0, 71007, 24020, 1, 3)
    ops.uniaxialMaterial('LimitState', 34048, 71.84195636, 7.214e-05, 215.52586909, 0.00021642, 718.41956364, 0.00072139, -71.84195636, -7.214e-05, -215.52586909, -0.00021642, -718.41956364, -0.00072139, 0.4, 0.3, 0.003, 0.0, 0.0, 14048, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4048, 99999, 'P', 44048, 'Vy', 34048, 'Vz', 24048, 'My', 14048, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171007, 71007, 171007, 4048, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124020, 124020, 24020, 4048, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174020, 10.3, 3.5, 4.05)
    ops.node(122007, 10.3, 3.5, 4.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4049, 174020, 122007, 0.1225, 30816431.0851094, 12840179.61879558, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24049, 84.84279305, 0.00050282, 102.26705337, 0.0496936, 10.22670534, 0.1496936, -84.84279305, -0.00050282, -102.26705337, -0.0496936, -10.22670534, -0.1496936, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14049, 76.99075204, 0.00050282, 92.80242983, 0.04264314, 9.28024298, 0.13034568, -76.99075204, -0.00050282, -92.80242983, -0.04264314, -9.28024298, -0.13034568, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24049, 4049, 0.0, 241.9213504, 0.01005636, 241.9213504, 0.03016909, 169.34494528, -7132.96124925, 0.05, 2, 0, 74020, 22007, 2, 3)
    ops.uniaxialMaterial('LimitState', 44049, 60.4803376, 5.998e-05, 181.4410128, 0.00017995, 604.803376, 0.00059983, -60.4803376, -5.998e-05, -181.4410128, -0.00017995, -604.803376, -0.00059983, 0.4, 0.3, 0.003, 0.0, 0.0, 24049, 2)
    ops.limitCurve('ThreePoint', 14049, 4049, 0.0, 286.5763887, 0.01005636, 286.5763887, 0.03016909, 200.60347209, -12620.7498847, 0.05, 2, 0, 74020, 22007, 1, 3)
    ops.uniaxialMaterial('LimitState', 34049, 71.64409718, 7.106e-05, 214.93229153, 0.00021317, 716.44097175, 0.00071056, -71.64409718, -7.106e-05, -214.93229153, -0.00021317, -716.44097175, -0.00071056, 0.4, 0.3, 0.003, 0.0, 0.0, 14049, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4049, 99999, 'P', 44049, 'Vy', 34049, 'Vz', 24049, 'My', 14049, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174020, 74020, 174020, 4049, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122007, 122007, 22007, 4049, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172006, 7.45, 3.5, 5.5)
    ops.node(124021, 7.45, 3.5, 6.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4051, 172006, 124021, 0.0625, 31380797.09414742, 13075332.12256142, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24051, 36.53300537, 0.00059786, 43.86936309, 0.04622088, 4.38693631, 0.14622088, -36.53300537, -0.00059786, -43.86936309, -0.04622088, -4.38693631, -0.14622088, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14051, 36.53300537, 0.00059786, 43.86936309, 0.04622088, 4.38693631, 0.14622088, -36.53300537, -0.00059786, -43.86936309, -0.04622088, -4.38693631, -0.14622088, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24051, 4051, 0.0, 123.57168856, 0.01195719, 123.57168856, 0.03587157, 86.50018199, -5043.23171122, 0.05, 2, 0, 72006, 24021, 2, 3)
    ops.uniaxialMaterial('LimitState', 44051, 30.89292214, 5.897e-05, 92.67876642, 0.00017692, 308.9292214, 0.00058973, -30.89292214, -5.897e-05, -92.67876642, -0.00017692, -308.9292214, -0.00058973, 0.4, 0.3, 0.003, 0.0, 0.0, 24051, 2)
    ops.limitCurve('ThreePoint', 14051, 4051, 0.0, 123.57168856, 0.01195719, 123.57168856, 0.03587157, 86.50018199, -5043.23171122, 0.05, 2, 0, 72006, 24021, 1, 3)
    ops.uniaxialMaterial('LimitState', 34051, 30.89292214, 5.897e-05, 92.67876642, 0.00017692, 308.9292214, 0.00058973, -30.89292214, -5.897e-05, -92.67876642, -0.00017692, -308.9292214, -0.00058973, 0.4, 0.3, 0.003, 0.0, 0.0, 14051, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4051, 99999, 'P', 44051, 'Vy', 34051, 'Vz', 24051, 'My', 14051, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172006, 72006, 172006, 4051, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124021, 124021, 24021, 4051, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174021, 7.45, 3.5, 6.65)
    ops.node(123006, 7.45, 3.5, 7.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4052, 174021, 123006, 0.0625, 30980573.51540961, 12908572.29808734, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24052, 35.41366041, 0.00057755, 42.60971785, 0.04736117, 4.26097179, 0.14736117, -35.41366041, -0.00057755, -42.60971785, -0.04736117, -4.26097179, -0.14736117, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14052, 35.41366041, 0.00057755, 42.60971785, 0.04736117, 4.26097179, 0.14736117, -35.41366041, -0.00057755, -42.60971785, -0.04736117, -4.26097179, -0.14736117, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24052, 4052, 0.0, 120.62779728, 0.01155104, 120.62779728, 0.03465312, 84.4394581, -5228.61343111, 0.05, 2, 0, 74021, 23006, 2, 3)
    ops.uniaxialMaterial('LimitState', 44052, 30.15694932, 5.831e-05, 90.47084796, 0.00017493, 301.56949321, 0.00058311, -30.15694932, -5.831e-05, -90.47084796, -0.00017493, -301.56949321, -0.00058311, 0.4, 0.3, 0.003, 0.0, 0.0, 24052, 2)
    ops.limitCurve('ThreePoint', 14052, 4052, 0.0, 120.62779728, 0.01155104, 120.62779728, 0.03465312, 84.4394581, -5228.61343111, 0.05, 2, 0, 74021, 23006, 1, 3)
    ops.uniaxialMaterial('LimitState', 34052, 30.15694932, 5.831e-05, 90.47084796, 0.00017493, 301.56949321, 0.00058311, -30.15694932, -5.831e-05, -90.47084796, -0.00017493, -301.56949321, -0.00058311, 0.4, 0.3, 0.003, 0.0, 0.0, 14052, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4052, 99999, 'P', 44052, 'Vy', 34052, 'Vz', 24052, 'My', 14052, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174021, 74021, 174021, 4052, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123006, 123006, 23006, 4052, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172007, 10.3, 3.5, 5.5)
    ops.node(124022, 10.3, 3.5, 6.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4053, 172007, 124022, 0.0625, 29777018.84654119, 12407091.18605883, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24053, 37.03201623, 0.00059942, 44.60930348, 0.04680118, 4.46093035, 0.14680118, -37.03201623, -0.00059942, -44.60930348, -0.04680118, -4.46093035, -0.14680118, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14053, 37.03201623, 0.00059942, 44.60930348, 0.04680118, 4.46093035, 0.14680118, -37.03201623, -0.00059942, -44.60930348, -0.04680118, -4.46093035, -0.14680118, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24053, 4053, 0.0, 121.04023917, 0.01198832, 121.04023917, 0.03596496, 84.72816742, -5189.55686816, 0.05, 2, 0, 72007, 24022, 2, 3)
    ops.uniaxialMaterial('LimitState', 44053, 30.26005979, 6.088e-05, 90.78017938, 0.00018263, 302.60059793, 0.00060876, -30.26005979, -6.088e-05, -90.78017938, -0.00018263, -302.60059793, -0.00060876, 0.4, 0.3, 0.003, 0.0, 0.0, 24053, 2)
    ops.limitCurve('ThreePoint', 14053, 4053, 0.0, 121.04023917, 0.01198832, 121.04023917, 0.03596496, 84.72816742, -5189.55686816, 0.05, 2, 0, 72007, 24022, 1, 3)
    ops.uniaxialMaterial('LimitState', 34053, 30.26005979, 6.088e-05, 90.78017938, 0.00018263, 302.60059793, 0.00060876, -30.26005979, -6.088e-05, -90.78017938, -0.00018263, -302.60059793, -0.00060876, 0.4, 0.3, 0.003, 0.0, 0.0, 14053, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4053, 99999, 'P', 44053, 'Vy', 34053, 'Vz', 24053, 'My', 14053, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172007, 72007, 172007, 4053, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124022, 124022, 24022, 4053, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174022, 10.3, 3.5, 6.65)
    ops.node(123007, 10.3, 3.5, 7.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4054, 174022, 123007, 0.0625, 33384676.62131044, 13910281.92554602, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24054, 34.29773341, 0.00059422, 41.00187478, 0.04601886, 4.10018748, 0.14601886, -34.29773341, -0.00059422, -41.00187478, -0.04601886, -4.10018748, -0.14601886, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14054, 34.29773341, 0.00059422, 41.00187478, 0.04601886, 4.10018748, 0.14601886, -34.29773341, -0.00059422, -41.00187478, -0.04601886, -4.10018748, -0.14601886, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24054, 4054, 0.0, 126.79041374, 0.01188431, 126.79041374, 0.03565294, 88.75328961, -5253.54037883, 0.05, 2, 0, 74022, 23007, 2, 3)
    ops.uniaxialMaterial('LimitState', 44054, 31.69760343, 5.688e-05, 95.0928103, 0.00017063, 316.97603434, 0.00056877, -31.69760343, -5.688e-05, -95.0928103, -0.00017063, -316.97603434, -0.00056877, 0.4, 0.3, 0.003, 0.0, 0.0, 24054, 2)
    ops.limitCurve('ThreePoint', 14054, 4054, 0.0, 126.79041374, 0.01188431, 126.79041374, 0.03565294, 88.75328961, -5253.54037883, 0.05, 2, 0, 74022, 23007, 1, 3)
    ops.uniaxialMaterial('LimitState', 34054, 31.69760343, 5.688e-05, 95.0928103, 0.00017063, 316.97603434, 0.00056877, -31.69760343, -5.688e-05, -95.0928103, -0.00017063, -316.97603434, -0.00056877, 0.4, 0.3, 0.003, 0.0, 0.0, 14054, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4054, 99999, 'P', 44054, 'Vy', 34054, 'Vz', 24054, 'My', 14054, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174022, 74022, 174022, 4054, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123007, 123007, 23007, 4054, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173006, 7.45, 3.5, 8.1)
    ops.node(124023, 7.45, 3.5, 8.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4056, 173006, 124023, 0.0625, 31185685.79842636, 12994035.74934432, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24056, 26.25618597, 0.00056957, 31.73699558, 0.03937763, 3.17369956, 0.13228419, -26.25618597, -0.00056957, -31.73699558, -0.03937763, -3.17369956, -0.13228419, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14056, 26.25618597, 0.00056957, 31.73699558, 0.03937763, 3.17369956, 0.13228419, -26.25618597, -0.00056957, -31.73699558, -0.03937763, -3.17369956, -0.13228419, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24056, 4056, 0.0, 92.39890483, 0.01139145, 92.39890483, 0.03417435, 64.67923338, -4561.87840399, 0.05, 2, 0, 73006, 24023, 2, 3)
    ops.uniaxialMaterial('LimitState', 44056, 23.09972621, 4.437e-05, 69.29917862, 0.00013312, 230.99726208, 0.00044372, -23.09972621, -4.437e-05, -69.29917862, -0.00013312, -230.99726208, -0.00044372, 0.4, 0.3, 0.003, 0.0, 0.0, 24056, 2)
    ops.limitCurve('ThreePoint', 14056, 4056, 0.0, 92.39890483, 0.01139145, 92.39890483, 0.03417435, 64.67923338, -4561.87840399, 0.05, 2, 0, 73006, 24023, 1, 3)
    ops.uniaxialMaterial('LimitState', 34056, 23.09972621, 4.437e-05, 69.29917862, 0.00013312, 230.99726208, 0.00044372, -23.09972621, -4.437e-05, -69.29917862, -0.00013312, -230.99726208, -0.00044372, 0.4, 0.3, 0.003, 0.0, 0.0, 14056, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4056, 99999, 'P', 44056, 'Vy', 34056, 'Vz', 24056, 'My', 14056, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173006, 73006, 173006, 4056, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124023, 124023, 24023, 4056, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174023, 7.45, 3.5, 9.25)
    ops.node(124006, 7.45, 3.5, 10.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4057, 174023, 124006, 0.0625, 31333445.74991001, 13055602.39579584, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24057, 25.04112681, 0.00056536, 30.28752757, 0.05190937, 3.02875276, 0.15190937, -25.04112681, -0.00056536, -30.28752757, -0.05190937, -3.02875276, -0.15190937, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14057, 25.04112681, 0.00056536, 30.28752757, 0.05190937, 3.02875276, 0.15190937, -25.04112681, -0.00056536, -30.28752757, -0.05190937, -3.02875276, -0.15190937, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24057, 4057, 0.0, 112.17311269, 0.01130715, 112.17311269, 0.03392144, 78.52117888, -11914.85973681, 0.05, 2, 0, 74023, 24006, 2, 3)
    ops.uniaxialMaterial('LimitState', 44057, 28.04327817, 5.361e-05, 84.12983452, 0.00016084, 280.43278172, 0.00053614, -28.04327817, -5.361e-05, -84.12983452, -0.00016084, -280.43278172, -0.00053614, 0.4, 0.3, 0.003, 0.0, 0.0, 24057, 2)
    ops.limitCurve('ThreePoint', 14057, 4057, 0.0, 112.17311269, 0.01130715, 112.17311269, 0.03392144, 78.52117888, -11914.85973681, 0.05, 2, 0, 74023, 24006, 1, 3)
    ops.uniaxialMaterial('LimitState', 34057, 28.04327817, 5.361e-05, 84.12983452, 0.00016084, 280.43278172, 0.00053614, -28.04327817, -5.361e-05, -84.12983452, -0.00016084, -280.43278172, -0.00053614, 0.4, 0.3, 0.003, 0.0, 0.0, 14057, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4057, 99999, 'P', 44057, 'Vy', 34057, 'Vz', 24057, 'My', 14057, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174023, 74023, 174023, 4057, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124006, 124006, 24006, 4057, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173007, 10.3, 3.5, 8.1)
    ops.node(124024, 10.3, 3.5, 8.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4058, 173007, 124024, 0.0625, 30896740.23048757, 12873641.76270315, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24058, 26.9835438, 0.0005616, 32.64278609, 0.03922672, 3.26427861, 0.13183826, -26.9835438, -0.0005616, -32.64278609, -0.03922672, -3.26427861, -0.13183826, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14058, 26.9835438, 0.0005616, 32.64278609, 0.03922672, 3.26427861, 0.13183826, -26.9835438, -0.0005616, -32.64278609, -0.03922672, -3.26427861, -0.13183826, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24058, 4058, 0.0, 91.1122685, 0.01123191, 91.1122685, 0.03369573, 63.77858795, -4458.39891279, 0.05, 2, 0, 73007, 24024, 2, 3)
    ops.uniaxialMaterial('LimitState', 44058, 22.77806712, 4.416e-05, 68.33420137, 0.00013249, 227.78067125, 0.00044163, -22.77806712, -4.416e-05, -68.33420137, -0.00013249, -227.78067125, -0.00044163, 0.4, 0.3, 0.003, 0.0, 0.0, 24058, 2)
    ops.limitCurve('ThreePoint', 14058, 4058, 0.0, 91.1122685, 0.01123191, 91.1122685, 0.03369573, 63.77858795, -4458.39891279, 0.05, 2, 0, 73007, 24024, 1, 3)
    ops.uniaxialMaterial('LimitState', 34058, 22.77806712, 4.416e-05, 68.33420137, 0.00013249, 227.78067125, 0.00044163, -22.77806712, -4.416e-05, -68.33420137, -0.00013249, -227.78067125, -0.00044163, 0.4, 0.3, 0.003, 0.0, 0.0, 14058, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4058, 99999, 'P', 44058, 'Vy', 34058, 'Vz', 24058, 'My', 14058, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173007, 73007, 173007, 4058, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124024, 124024, 24024, 4058, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174024, 10.3, 3.5, 9.25)
    ops.node(124007, 10.3, 3.5, 10.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4059, 174024, 124007, 0.0625, 30724527.35772214, 12801886.39905089, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24059, 25.2234647, 0.00055167, 30.56265375, 0.05270491, 3.05626538, 0.15270491, -25.2234647, -0.00055167, -30.56265375, -0.05270491, -3.05626538, -0.15270491, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14059, 25.2234647, 0.00055167, 30.56265375, 0.05270491, 3.05626538, 0.15270491, -25.2234647, -0.00055167, -30.56265375, -0.05270491, -3.05626538, -0.15270491, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24059, 4059, 0.0, 111.94368027, 0.01103345, 111.94368027, 0.03310034, 78.36057619, -12315.38403396, 0.05, 2, 0, 74024, 24007, 2, 3)
    ops.uniaxialMaterial('LimitState', 44059, 27.98592007, 5.456e-05, 83.9577602, 0.00016369, 279.85920068, 0.00054565, -27.98592007, -5.456e-05, -83.9577602, -0.00016369, -279.85920068, -0.00054565, 0.4, 0.3, 0.003, 0.0, 0.0, 24059, 2)
    ops.limitCurve('ThreePoint', 14059, 4059, 0.0, 111.94368027, 0.01103345, 111.94368027, 0.03310034, 78.36057619, -12315.38403396, 0.05, 2, 0, 74024, 24007, 1, 3)
    ops.uniaxialMaterial('LimitState', 34059, 27.98592007, 5.456e-05, 83.9577602, 0.00016369, 279.85920068, 0.00054565, -27.98592007, -5.456e-05, -83.9577602, -0.00016369, -279.85920068, -0.00054565, 0.4, 0.3, 0.003, 0.0, 0.0, 14059, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4059, 99999, 'P', 44059, 'Vy', 34059, 'Vz', 24059, 'My', 14059, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174024, 74024, 174024, 4059, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124007, 124007, 24007, 4059, '-orient', 0, 0, 1, 0, 1, 0)
