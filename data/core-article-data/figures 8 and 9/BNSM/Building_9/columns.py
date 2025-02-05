import openseespy.opensees as ops


def add_columns() -> None:
    """Add components of all columns to ops domain (plastic hinges, column elements and nodes)
    """
    # Create elastic column element nodes
    ops.node(170003, 6.6, 0.0, 0.0)
    ops.node(121003, 6.6, 0.0, 2.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3, 170003, 121003, 0.135, 29549137.33101903, 12312140.55459126, 0.002377, 0.00250594, 0.00111375, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20003, 159.47065619, 0.00106484, 192.14586905, 0.0373012, 19.21458691, 0.09956017, -159.47065619, -0.00106484, -192.14586905, -0.0373012, -19.21458691, -0.09956017, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10003, 199.63588002, 0.00078986, 240.5408655, 0.04288559, 24.05408655, 0.13172583, -199.63588002, -0.00078986, -240.5408655, -0.04288559, -24.05408655, -0.13172583, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20003, 3, 0.0, 226.97230694, 0.02129677, 226.97230694, 0.0638903, 158.88061486, -4834.44846719, 0.05, 2, 0, 70003, 21003, 2, 3)
    ops.uniaxialMaterial('LimitState', 40003, 56.74307674, 0.00011061, 170.22923021, 0.00033183, 567.43076736, 0.00110609, -56.74307674, -0.00011061, -170.22923021, -0.00033183, -567.43076736, -0.00110609, 0.4, 0.3, 0.003, 0.0, 0.0, 20003, 2)
    ops.limitCurve('ThreePoint', 10003, 3, 0.0, 297.4299428, 0.0157972, 297.4299428, 0.04739159, 208.20095996, -8481.42688082, 0.05, 2, 0, 70003, 21003, 1, 3)
    ops.uniaxialMaterial('LimitState', 30003, 74.3574857, 0.00014494, 223.0724571, 0.00043483, 743.57485699, 0.00144945, -74.3574857, -0.00014494, -223.0724571, -0.00043483, -743.57485699, -0.00144945, 0.4, 0.3, 0.003, 0.0, 0.0, 10003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3, 99999, 'P', 40003, 'Vy', 30003, 'Vz', 20003, 'My', 10003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170003, 70003, 170003, 3, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121003, 121003, 21003, 3, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170004, 10.3, 0.0, 0.0)
    ops.node(121004, 10.3, 0.0, 2.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4, 170004, 121004, 0.075, 31441526.12307622, 13100635.88461509, 0.00077515, 0.00061875, 0.00042969, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20004, 51.35568743, 0.00115695, 61.62491146, 0.01612992, 6.16249115, 0.05941064, -51.35568743, -0.00115695, -61.62491146, -0.01612992, -6.16249115, -0.05941064, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10004, 58.23567799, 0.00098584, 69.88064378, 0.01688742, 6.98806438, 0.06680835, -58.23567799, -0.00098584, -69.88064378, -0.01688742, -6.98806438, -0.06680835, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20004, 4, 0.0, 103.58921323, 0.023139, 103.58921323, 0.06941701, 72.51244926, -1493.9539875, 0.05, 2, 0, 70004, 21004, 2, 3)
    ops.uniaxialMaterial('LimitState', 40004, 25.89730331, 8.54e-05, 77.69190992, 0.00025619, 258.97303307, 0.00085398, -25.89730331, -8.54e-05, -77.69190992, -0.00025619, -258.97303307, -0.00085398, 0.4, 0.3, 0.003, 0.0, 0.0, 20004, 2)
    ops.limitCurve('ThreePoint', 10004, 4, 0.0, 112.23866558, 0.01971687, 112.23866558, 0.05915061, 78.5670659, -1819.49678466, 0.05, 2, 0, 70004, 21004, 1, 3)
    ops.uniaxialMaterial('LimitState', 30004, 28.05966639, 9.253e-05, 84.17899918, 0.00027758, 280.59666394, 0.00092528, -28.05966639, -9.253e-05, -84.17899918, -0.00027758, -280.59666394, -0.00092528, 0.4, 0.3, 0.003, 0.0, 0.0, 10004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4, 99999, 'P', 40004, 'Vy', 30004, 'Vz', 20004, 'My', 10004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170004, 70004, 170004, 4, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121004, 121004, 21004, 4, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170005, 0.0, 5.7, 0.0)
    ops.node(121005, 0.0, 5.7, 2.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 5, 170005, 121005, 0.1, 31171370.52145547, 12988071.05060645, 0.00127345, 0.00057292, 0.00146667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20005, 95.7970601, 0.00080505, 114.89628469, 0.02027657, 11.48962847, 0.07778903, -95.7970601, -0.00080505, -114.89628469, -0.02027657, -11.48962847, -0.07778903, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10005, 61.64213566, 0.00117197, 73.93183424, 0.01780168, 7.39318342, 0.05735998, -61.64213566, -0.00117197, -73.93183424, -0.01780168, -7.39318342, -0.05735998, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20005, 5, 0.0, 164.83639872, 0.01610104, 164.83639872, 0.04830311, 115.3854791, -2950.98106204, 0.05, 2, 0, 70005, 21005, 2, 3)
    ops.uniaxialMaterial('LimitState', 40005, 41.20909968, 0.0001028, 123.62729904, 0.0003084, 412.0909968, 0.001028, -41.20909968, -0.0001028, -123.62729904, -0.0003084, -412.0909968, -0.001028, 0.4, 0.3, 0.003, 0.0, 0.0, 20005, 2)
    ops.limitCurve('ThreePoint', 10005, 5, 0.0, 133.65041023, 0.02343943, 133.65041023, 0.0703183, 93.55528716, -1801.22520555, 0.05, 2, 0, 70005, 21005, 1, 3)
    ops.uniaxialMaterial('LimitState', 30005, 33.41260256, 8.335e-05, 100.23780768, 0.00025005, 334.12602559, 0.00083351, -33.41260256, -8.335e-05, -100.23780768, -0.00025005, -334.12602559, -0.00083351, 0.4, 0.3, 0.003, 0.0, 0.0, 10005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 5, 99999, 'P', 40005, 'Vy', 30005, 'Vz', 20005, 'My', 10005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170005, 70005, 170005, 5, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121005, 121005, 21005, 5, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170006, 2.9, 5.7, 0.0)
    ops.node(121006, 2.9, 5.7, 2.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 6, 170006, 121006, 0.18, 31135749.74835729, 12973229.06181554, 0.00370786, 0.001485, 0.00594, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20006, 353.88593698, 0.0006806, 424.85915871, 0.04274266, 42.48591587, 0.13479193, -353.88593698, -0.0006806, -424.85915871, -0.04274266, -42.48591587, -0.13479193, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10006, 215.37507629, 0.00107041, 258.56939809, 0.03885524, 25.85693981, 0.11023, -215.37507629, -0.00107041, -258.56939809, -0.03885524, -25.85693981, -0.11023, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20006, 6, 0.0, 602.11949683, 0.01361207, 602.11949683, 0.0408362, 421.48364778, -21598.15622362, 0.05, 2, 0, 70006, 21006, 2, 3)
    ops.uniaxialMaterial('LimitState', 40006, 150.52987421, 0.00020886, 451.58962262, 0.00062657, 1505.29874207, 0.00208856, -150.52987421, -0.00020886, -451.58962262, -0.00062657, -1505.29874207, -0.00208856, 0.4, 0.3, 0.003, 0.0, 0.0, 20006, 2)
    ops.limitCurve('ThreePoint', 10006, 6, 0.0, 276.26425988, 0.02140812, 276.26425988, 0.06422436, 193.38498192, -4678.06905628, 0.05, 2, 0, 70006, 21006, 1, 3)
    ops.uniaxialMaterial('LimitState', 30006, 69.06606497, 9.583e-05, 207.19819491, 0.00028748, 690.66064971, 0.00095827, -69.06606497, -9.583e-05, -207.19819491, -0.00028748, -690.66064971, -0.00095827, 0.4, 0.3, 0.003, 0.0, 0.0, 10006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 6, 99999, 'P', 40006, 'Vy', 30006, 'Vz', 20006, 'My', 10006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170006, 70006, 170006, 6, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121006, 121006, 21006, 6, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170007, 6.6, 5.7, 0.0)
    ops.node(121007, 6.6, 5.7, 2.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 7, 170007, 121007, 0.195, 30914198.70810824, 12880916.12837843, 0.00415543, 0.00160875, 0.00755219, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20007, 440.31012829, 0.00065774, 528.88238384, 0.04440954, 52.88823838, 0.1359052, -440.31012829, -0.00065774, -528.88238384, -0.04440954, -52.88823838, -0.1359052, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10007, 256.73363398, 0.00107301, 308.37786284, 0.03924977, 30.83778628, 0.10546839, -256.73363398, -0.00107301, -308.37786284, -0.03924977, -30.83778628, -0.10546839, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20007, 7, 0.0, 656.35497428, 0.01315478, 656.35497428, 0.03946433, 459.448482, -22424.29644205, 0.05, 2, 0, 70007, 21007, 2, 3)
    ops.uniaxialMaterial('LimitState', 40007, 164.08874357, 0.00021166, 492.26623071, 0.00063499, 1640.8874357, 0.00211662, -164.08874357, -0.00021166, -492.26623071, -0.00063499, -1640.8874357, -0.00211662, 0.4, 0.3, 0.003, 0.0, 0.0, 20007, 2)
    ops.limitCurve('ThreePoint', 10007, 7, 0.0, 282.99281047, 0.02146019, 282.99281047, 0.06438056, 198.09496733, -4490.06029086, 0.05, 2, 0, 70007, 21007, 1, 3)
    ops.uniaxialMaterial('LimitState', 30007, 70.74820262, 9.126e-05, 212.24460786, 0.00027378, 707.48202619, 0.0009126, -70.74820262, -9.126e-05, -212.24460786, -0.00027378, -707.48202619, -0.0009126, 0.4, 0.3, 0.003, 0.0, 0.0, 10007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 7, 99999, 'P', 40007, 'Vy', 30007, 'Vz', 20007, 'My', 10007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170007, 70007, 170007, 7, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121007, 121007, 21007, 7, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170008, 10.3, 5.7, 0.0)
    ops.node(121008, 10.3, 5.7, 2.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 8, 170008, 121008, 0.125, 30558146.77667942, 12732561.15694976, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20008, 183.46326783, 0.00071874, 220.33288605, 0.02910954, 22.03328861, 0.1013646, -183.46326783, -0.00071874, -220.33288605, -0.02910954, -22.03328861, -0.1013646, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10008, 108.38317113, 0.00119182, 130.16434939, 0.02350521, 13.01643494, 0.06431069, -108.38317113, -0.00119182, -130.16434939, -0.02350521, -13.01643494, -0.06431069, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20008, 8, 0.0, 261.5436605, 0.01437475, 261.5436605, 0.04312425, 183.08056235, -5551.94186764, 0.05, 2, 0, 70008, 21008, 2, 3)
    ops.uniaxialMaterial('LimitState', 40008, 65.38591513, 0.00013311, 196.15774538, 0.00039932, 653.85915125, 0.00133108, -65.38591513, -0.00013311, -196.15774538, -0.00039932, -653.85915125, -0.00133108, 0.4, 0.3, 0.003, 0.0, 0.0, 20008, 2)
    ops.limitCurve('ThreePoint', 10008, 8, 0.0, 171.21407549, 0.02383636, 171.21407549, 0.07150907, 119.84985284, -2482.36276842, 0.05, 2, 0, 70008, 21008, 1, 3)
    ops.uniaxialMaterial('LimitState', 30008, 42.80351887, 8.714e-05, 128.41055662, 0.00026141, 428.03518873, 0.00087136, -42.80351887, -8.714e-05, -128.41055662, -0.00026141, -428.03518873, -0.00087136, 0.4, 0.3, 0.003, 0.0, 0.0, 10008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 8, 99999, 'P', 40008, 'Vy', 30008, 'Vz', 20008, 'My', 10008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170008, 70008, 170008, 8, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121008, 121008, 21008, 8, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170009, 0.0, 11.4, 0.0)
    ops.node(121009, 0.0, 11.4, 2.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 9, 170009, 121009, 0.1, 31610591.77548276, 13171079.90645115, 0.00127345, 0.00057292, 0.00146667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20009, 96.26598329, 0.00080552, 115.33779704, 0.02064053, 11.5337797, 0.07882708, -96.26598329, -0.00080552, -115.33779704, -0.02064053, -11.5337797, -0.07882708, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10009, 61.85341666, 0.00117564, 74.10755672, 0.01811579, 7.41075567, 0.05813774, -61.85341666, -0.00117564, -74.10755672, -0.01811579, -7.41075567, -0.05813774, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20009, 9, 0.0, 167.30054115, 0.01611043, 167.30054115, 0.0483313, 117.1103788, -2978.60963032, 0.05, 2, 0, 70009, 21009, 2, 3)
    ops.uniaxialMaterial('LimitState', 40009, 41.82513529, 0.00010289, 125.47540586, 0.00030866, 418.25135287, 0.00102887, -41.82513529, -0.00010289, -125.47540586, -0.00030866, -418.25135287, -0.00102887, 0.4, 0.3, 0.003, 0.0, 0.0, 20009, 2)
    ops.limitCurve('ThreePoint', 10009, 9, 0.0, 135.81429596, 0.0235128, 135.81429596, 0.07053841, 95.07000717, -1818.76056307, 0.05, 2, 0, 70009, 21009, 1, 3)
    ops.uniaxialMaterial('LimitState', 30009, 33.95357399, 8.352e-05, 101.86072197, 0.00025057, 339.5357399, 0.00083524, -33.95357399, -8.352e-05, -101.86072197, -0.00025057, -339.5357399, -0.00083524, 0.4, 0.3, 0.003, 0.0, 0.0, 10009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 9, 99999, 'P', 40009, 'Vy', 30009, 'Vz', 20009, 'My', 10009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170009, 70009, 170009, 9, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121009, 121009, 21009, 9, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170010, 2.9, 11.4, 0.0)
    ops.node(121010, 2.9, 11.4, 2.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 10, 170010, 121010, 0.165, 30834168.09717469, 12847570.04048946, 0.00326155, 0.00136125, 0.00457531, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20010, 251.35541782, 0.00067085, 301.79412733, 0.03825857, 30.17941273, 0.12796701, -251.35541782, -0.00067085, -301.79412733, -0.03825857, -30.17941273, -0.12796701, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10010, 169.89917961, 0.00098568, 203.99231928, 0.03113241, 20.39923193, 0.08429091, -169.89917961, -0.00098568, -203.99231928, -0.03113241, -20.39923193, -0.08429091, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20010, 10, 0.0, 409.08181812, 0.01341697, 409.08181812, 0.04025092, 286.35727268, -10053.58542189, 0.05, 2, 0, 70010, 21010, 2, 3)
    ops.uniaxialMaterial('LimitState', 40010, 102.27045453, 0.00015631, 306.81136359, 0.00046893, 1022.70454529, 0.00156311, -102.27045453, -0.00015631, -306.81136359, -0.00046893, -1022.70454529, -0.00156311, 0.4, 0.3, 0.003, 0.0, 0.0, 20010, 2)
    ops.limitCurve('ThreePoint', 10010, 10, 0.0, 261.18230097, 0.01971368, 261.18230097, 0.05914103, 182.82761068, -4578.90263176, 0.05, 2, 0, 70010, 21010, 1, 3)
    ops.uniaxialMaterial('LimitState', 30010, 65.29557524, 9.98e-05, 195.88672573, 0.0002994, 652.95575243, 0.00099798, -65.29557524, -9.98e-05, -195.88672573, -0.0002994, -652.95575243, -0.00099798, 0.4, 0.3, 0.003, 0.0, 0.0, 10010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 10, 99999, 'P', 40010, 'Vy', 30010, 'Vz', 20010, 'My', 10010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170010, 70010, 170010, 10, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121010, 121010, 21010, 10, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170011, 6.6, 11.4, 0.0)
    ops.node(121011, 6.6, 11.4, 2.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 11, 170011, 121011, 0.195, 30744531.39287541, 12810221.41369809, 0.00415543, 0.00160875, 0.00755219, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20011, 438.57082273, 0.00065609, 526.98725222, 0.04444989, 52.69872522, 0.13549804, -438.57082273, -0.00065609, -526.98725222, -0.04444989, -52.69872522, -0.13549804, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10011, 256.26231802, 0.00106792, 307.92512365, 0.03928133, 30.79251237, 0.10517607, -256.26231802, -0.00106792, -307.92512365, -0.03928133, -30.79251237, -0.10517607, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20011, 11, 0.0, 655.92883579, 0.01312178, 655.92883579, 0.03936533, 459.15018506, -22580.04578372, 0.05, 2, 0, 70011, 21011, 2, 3)
    ops.uniaxialMaterial('LimitState', 40011, 163.98220895, 0.00021269, 491.94662685, 0.00063808, 1639.82208949, 0.00212692, -163.98220895, -0.00021269, -491.94662685, -0.00063808, -1639.82208949, -0.00212692, 0.4, 0.3, 0.003, 0.0, 0.0, 20011, 2)
    ops.limitCurve('ThreePoint', 10011, 11, 0.0, 282.24917641, 0.02135838, 282.24917641, 0.06407514, 197.57442349, -4507.46198615, 0.05, 2, 0, 70011, 21011, 1, 3)
    ops.uniaxialMaterial('LimitState', 30011, 70.5622941, 9.152e-05, 211.68688231, 0.00027457, 705.62294103, 0.00091522, -70.5622941, -9.152e-05, -211.68688231, -0.00027457, -705.62294103, -0.00091522, 0.4, 0.3, 0.003, 0.0, 0.0, 10011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 11, 99999, 'P', 40011, 'Vy', 30011, 'Vz', 20011, 'My', 10011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170011, 70011, 170011, 11, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121011, 121011, 21011, 11, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170012, 10.3, 11.4, 0.0)
    ops.node(121012, 10.3, 11.4, 2.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 12, 170012, 121012, 0.125, 31615232.57031474, 13173013.57096447, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20012, 182.8760337, 0.00071044, 219.16850856, 0.02890182, 21.91685086, 0.10399444, -182.8760337, -0.00071044, -219.16850856, -0.02890182, -21.91685086, -0.10399444, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10012, 107.61377658, 0.00117693, 128.97015774, 0.02333358, 12.89701577, 0.06574156, -107.61377658, -0.00117693, -128.97015774, -0.02333358, -12.89701577, -0.06574156, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20012, 12, 0.0, 264.06443372, 0.01420884, 264.06443372, 0.04262652, 184.8451036, -5431.72249818, 0.05, 2, 0, 70012, 21012, 2, 3)
    ops.uniaxialMaterial('LimitState', 40012, 66.01610843, 0.0001299, 198.04832529, 0.00038969, 660.16108429, 0.00129897, -66.01610843, -0.0001299, -198.04832529, -0.00038969, -660.16108429, -0.00129897, 0.4, 0.3, 0.003, 0.0, 0.0, 20012, 2)
    ops.limitCurve('ThreePoint', 10012, 12, 0.0, 174.18205366, 0.02353862, 174.18205366, 0.07061585, 121.92743756, -2440.60739822, 0.05, 2, 0, 70012, 21012, 1, 3)
    ops.uniaxialMaterial('LimitState', 30012, 43.54551342, 8.568e-05, 130.63654025, 0.00025705, 435.45513416, 0.00085683, -43.54551342, -8.568e-05, -130.63654025, -0.00025705, -435.45513416, -0.00085683, 0.4, 0.3, 0.003, 0.0, 0.0, 10012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 12, 99999, 'P', 40012, 'Vy', 30012, 'Vz', 20012, 'My', 10012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170012, 70012, 170012, 12, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121012, 121012, 21012, 12, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170013, 0.0, 17.1, 0.0)
    ops.node(121013, 0.0, 17.1, 2.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 13, 170013, 121013, 0.1, 31392802.67323792, 13080334.44718247, 0.00127345, 0.00057292, 0.00146667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20013, 96.14817817, 0.00078472, 115.24988778, 0.02065804, 11.52498878, 0.07840021, -96.14817817, -0.00078472, -115.24988778, -0.02065804, -11.52498878, -0.07840021, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10013, 62.21740639, 0.00112602, 74.57810685, 0.01809888, 7.45781068, 0.05781518, -62.21740639, -0.00112602, -74.57810685, -0.01809888, -7.45781068, -0.05781518, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20013, 13, 0.0, 167.88535607, 0.01569439, 167.88535607, 0.04708318, 117.51974925, -3031.68809983, 0.05, 2, 0, 70013, 21013, 2, 3)
    ops.uniaxialMaterial('LimitState', 40013, 41.97133902, 0.00010396, 125.91401705, 0.00031189, 419.71339018, 0.00103963, -41.97133902, -0.00010396, -125.91401705, -0.00031189, -419.71339018, -0.00103963, 0.4, 0.3, 0.003, 0.0, 0.0, 20013, 2)
    ops.limitCurve('ThreePoint', 10013, 13, 0.0, 135.91789155, 0.0225203, 135.91789155, 0.0675609, 95.14252409, -1844.82032675, 0.05, 2, 0, 70013, 21013, 1, 3)
    ops.uniaxialMaterial('LimitState', 30013, 33.97947289, 8.417e-05, 101.93841867, 0.0002525, 339.79472889, 0.00084167, -33.97947289, -8.417e-05, -101.93841867, -0.0002525, -339.79472889, -0.00084167, 0.4, 0.3, 0.003, 0.0, 0.0, 10013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 13, 99999, 'P', 40013, 'Vy', 30013, 'Vz', 20013, 'My', 10013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170013, 70013, 170013, 13, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121013, 121013, 21013, 13, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170014, 2.9, 17.1, 0.0)
    ops.node(121014, 2.9, 17.1, 2.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 14, 170014, 121014, 0.165, 30302653.07040482, 12626105.44600201, 0.00326155, 0.00136125, 0.00457531, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20014, 254.45129039, 0.0006948, 305.80500657, 0.03799149, 30.58050066, 0.12591236, -254.45129039, -0.0006948, -305.80500657, -0.03799149, -30.58050066, -0.12591236, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10014, 169.36380248, 0.00104458, 203.54504255, 0.03095788, 20.35450425, 0.08305712, -169.36380248, -0.00104458, -203.54504255, -0.03095788, -20.35450425, -0.08305712, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20014, 14, 0.0, 404.14115358, 0.01389606, 404.14115358, 0.04168818, 282.89880751, -9971.4111188, 0.05, 2, 0, 70014, 21014, 2, 3)
    ops.uniaxialMaterial('LimitState', 40014, 101.0352884, 0.00015713, 303.10586519, 0.0004714, 1010.35288396, 0.00157132, -101.0352884, -0.00015713, -303.10586519, -0.0004714, -1010.35288396, -0.00157132, 0.4, 0.3, 0.003, 0.0, 0.0, 20014, 2)
    ops.limitCurve('ThreePoint', 10014, 14, 0.0, 257.68536828, 0.02089156, 257.68536828, 0.06267469, 180.3797578, -4549.1091895, 0.05, 2, 0, 70014, 21014, 1, 3)
    ops.uniaxialMaterial('LimitState', 30014, 64.42134207, 0.00010019, 193.26402621, 0.00030057, 644.21342071, 0.00100189, -64.42134207, -0.00010019, -193.26402621, -0.00030057, -644.21342071, -0.00100189, 0.4, 0.3, 0.003, 0.0, 0.0, 10014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 14, 99999, 'P', 40014, 'Vy', 30014, 'Vz', 20014, 'My', 10014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170014, 70014, 170014, 14, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121014, 121014, 21014, 14, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170015, 6.6, 17.1, 0.0)
    ops.node(121015, 6.6, 17.1, 2.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 15, 170015, 121015, 0.195, 31356027.21230935, 13065011.33846223, 0.00415543, 0.00160875, 0.00755219, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20015, 446.27665783, 0.00065897, 535.56208069, 0.04437737, 53.55620807, 0.13727671, -446.27665783, -0.00065897, -535.56208069, -0.04437737, -53.55620807, -0.13727671, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10015, 262.47423801, 0.00106723, 314.98678358, 0.03921485, 31.49867836, 0.10644936, -262.47423801, -0.00106723, -314.98678358, -0.03921485, -31.49867836, -0.10644936, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20015, 15, 0.0, 660.09953283, 0.01317943, 660.09953283, 0.0395383, 462.06967298, -22424.19291561, 0.05, 2, 0, 70015, 21015, 2, 3)
    ops.uniaxialMaterial('LimitState', 40015, 165.02488321, 0.00020987, 495.07464962, 0.00062961, 1650.24883207, 0.0020987, -165.02488321, -0.00020987, -495.07464962, -0.00062961, -1650.24883207, -0.0020987, 0.4, 0.3, 0.003, 0.0, 0.0, 20015, 2)
    ops.limitCurve('ThreePoint', 10015, 15, 0.0, 285.54823601, 0.02134466, 285.54823601, 0.06403397, 199.88376521, -4486.77476942, 0.05, 2, 0, 70015, 21015, 1, 3)
    ops.uniaxialMaterial('LimitState', 30015, 71.387059, 9.079e-05, 214.16117701, 0.00027236, 713.87059003, 0.00090786, -71.387059, -9.079e-05, -214.16117701, -0.00027236, -713.87059003, -0.00090786, 0.4, 0.3, 0.003, 0.0, 0.0, 10015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 15, 99999, 'P', 40015, 'Vy', 30015, 'Vz', 20015, 'My', 10015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170015, 70015, 170015, 15, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121015, 121015, 21015, 15, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170016, 10.3, 17.1, 0.0)
    ops.node(121016, 10.3, 17.1, 2.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 16, 170016, 121016, 0.125, 30490892.56382168, 12704538.56825903, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20016, 182.87676951, 0.00072199, 219.65985542, 0.02880185, 21.96598554, 0.10091984, -182.87676951, -0.00072199, -219.65985542, -0.02880185, -21.96598554, -0.10091984, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10016, 107.35996601, 0.0012068, 128.95391074, 0.0232758, 12.89539107, 0.06400388, -107.35996601, -0.0012068, -128.95391074, -0.0232758, -12.89539107, -0.06400388, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20016, 16, 0.0, 258.39218787, 0.01443982, 258.39218787, 0.04331946, 180.87453151, -5414.44005496, 0.05, 2, 0, 70016, 21016, 2, 3)
    ops.uniaxialMaterial('LimitState', 40016, 64.59804697, 0.00013179, 193.79414091, 0.00039538, 645.98046969, 0.00131794, -64.59804697, -0.00013179, -193.79414091, -0.00039538, -645.98046969, -0.00131794, 0.4, 0.3, 0.003, 0.0, 0.0, 20016, 2)
    ops.limitCurve('ThreePoint', 10016, 16, 0.0, 169.50815029, 0.02413597, 169.50815029, 0.07240792, 118.65570521, -2435.0974683, 0.05, 2, 0, 70016, 21016, 1, 3)
    ops.uniaxialMaterial('LimitState', 30016, 42.37703757, 8.646e-05, 127.13111272, 0.00025937, 423.77037573, 0.00086458, -42.37703757, -8.646e-05, -127.13111272, -0.00025937, -423.77037573, -0.00086458, 0.4, 0.3, 0.003, 0.0, 0.0, 10016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 16, 99999, 'P', 40016, 'Vy', 30016, 'Vz', 20016, 'My', 10016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170016, 70016, 170016, 16, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121016, 121016, 21016, 16, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170017, 0.0, 22.8, 0.0)
    ops.node(121017, 0.0, 22.8, 2.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 17, 170017, 121017, 0.0625, 32075593.81419361, 13364830.755914, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20017, 37.87559214, 0.00114884, 45.38612173, 0.01639009, 4.53861217, 0.06742898, -37.87559214, -0.00114884, -45.38612173, -0.01639009, -4.53861217, -0.06742898, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10017, 37.87559214, 0.00114884, 45.38612173, 0.01639009, 4.53861217, 0.06742898, -37.87559214, -0.00114884, -45.38612173, -0.01639009, -4.53861217, -0.06742898, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20017, 17, 0.0, 93.48890229, 0.02297675, 93.48890229, 0.06893025, 65.4422316, -1472.17760847, 0.05, 2, 0, 70017, 21017, 2, 3)
    ops.uniaxialMaterial('LimitState', 40017, 23.37222557, 9.066e-05, 70.11667672, 0.00027197, 233.72225573, 0.00090657, -23.37222557, -9.066e-05, -70.11667672, -0.00027197, -233.72225573, -0.00090657, 0.4, 0.3, 0.003, 0.0, 0.0, 20017, 2)
    ops.limitCurve('ThreePoint', 10017, 17, 0.0, 93.48890229, 0.02297675, 93.48890229, 0.06893025, 65.4422316, -1472.17760847, 0.05, 2, 0, 70017, 21017, 1, 3)
    ops.uniaxialMaterial('LimitState', 30017, 23.37222557, 9.066e-05, 70.11667672, 0.00027197, 233.72225573, 0.00090657, -23.37222557, -9.066e-05, -70.11667672, -0.00027197, -233.72225573, -0.00090657, 0.4, 0.3, 0.003, 0.0, 0.0, 10017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 17, 99999, 'P', 40017, 'Vy', 30017, 'Vz', 20017, 'My', 10017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170017, 70017, 170017, 17, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121017, 121017, 21017, 17, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170018, 2.9, 22.8, 0.0)
    ops.node(121018, 2.9, 22.8, 2.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 18, 170018, 121018, 0.12, 32329959.53314506, 13470816.47214377, 0.00194385, 0.00176, 0.00099, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20018, 147.21171874, 0.00103893, 176.32796255, 0.03948397, 17.63279626, 0.11457553, -147.21171874, -0.00103893, -176.32796255, -0.03948397, -17.63279626, -0.11457553, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10018, 164.78371627, 0.0008339, 197.37543451, 0.0436309, 19.73754345, 0.14047358, -164.78371627, -0.0008339, -197.37543451, -0.0436309, -19.73754345, -0.14047358, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20018, 18, 0.0, 224.74105423, 0.0207787, 224.74105423, 0.06233609, 157.31873796, -4895.98272085, 0.05, 2, 0, 70018, 21018, 2, 3)
    ops.uniaxialMaterial('LimitState', 40018, 56.18526356, 0.00011261, 168.55579067, 0.00033784, 561.85263558, 0.00112614, -56.18526356, -0.00011261, -168.55579067, -0.00033784, -561.85263558, -0.00112614, 0.4, 0.3, 0.003, 0.0, 0.0, 20018, 2)
    ops.limitCurve('ThreePoint', 10018, 18, 0.0, 266.6156, 0.01667792, 266.6156, 0.05003376, 186.63092, -7324.6479561, 0.05, 2, 0, 70018, 21018, 1, 3)
    ops.uniaxialMaterial('LimitState', 30018, 66.6539, 0.0001336, 199.9617, 0.00040079, 666.53900001, 0.00133597, -66.6539, -0.0001336, -199.9617, -0.00040079, -666.53900001, -0.00133597, 0.4, 0.3, 0.003, 0.0, 0.0, 10018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 18, 99999, 'P', 40018, 'Vy', 30018, 'Vz', 20018, 'My', 10018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170018, 70018, 170018, 18, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121018, 121018, 21018, 18, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170019, 6.6, 22.8, 0.0)
    ops.node(121019, 6.6, 22.8, 2.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 19, 170019, 121019, 0.1575, 31310448.18327602, 13046020.07636501, 0.00337604, 0.00292359, 0.00176859, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20019, 231.51446524, 0.00092513, 278.38403659, 0.03957303, 27.83840366, 0.10833253, -231.51446524, -0.00092513, -278.38403659, -0.03957303, -27.83840366, -0.10833253, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10019, 231.9508012, 0.00077763, 278.90870777, 0.04314601, 27.89087078, 0.128656, -231.9508012, -0.00077763, -278.90870777, -0.04314601, -27.89087078, -0.128656, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20019, 19, 0.0, 272.80726824, 0.01850263, 272.80726824, 0.05550788, 190.96508777, -6112.91342827, 0.05, 2, 0, 70019, 21019, 2, 3)
    ops.uniaxialMaterial('LimitState', 40019, 68.20181706, 0.00010754, 204.60545118, 0.00032263, 682.01817059, 0.00107543, -68.20181706, -0.00010754, -204.60545118, -0.00032263, -682.01817059, -0.00107543, 0.4, 0.3, 0.003, 0.0, 0.0, 20019, 2)
    ops.limitCurve('ThreePoint', 10019, 19, 0.0, 324.38242366, 0.01555262, 324.38242366, 0.04665787, 227.06769656, -8747.84595156, 0.05, 2, 0, 70019, 21019, 1, 3)
    ops.uniaxialMaterial('LimitState', 30019, 81.09560591, 0.00012787, 243.28681774, 0.00038362, 810.95605914, 0.00127874, -81.09560591, -0.00012787, -243.28681774, -0.00038362, -810.95605914, -0.00127874, 0.4, 0.3, 0.003, 0.0, 0.0, 10019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 19, 99999, 'P', 40019, 'Vy', 30019, 'Vz', 20019, 'My', 10019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170019, 70019, 170019, 19, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121019, 121019, 21019, 19, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170020, 10.3, 22.8, 0.0)
    ops.node(121020, 10.3, 22.8, 2.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 20, 170020, 121020, 0.075, 32299093.1946432, 13457955.497768, 0.00077515, 0.00061875, 0.00042969, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20020, 60.9175991, 0.00117444, 72.94582919, 0.02108985, 7.29458292, 0.07394151, -60.9175991, -0.00117444, -72.94582919, -0.02108985, -7.29458292, -0.07394151, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10020, 65.41539099, 0.00099859, 78.33171379, 0.02221126, 7.83317138, 0.08359713, -65.41539099, -0.00099859, -78.33171379, -0.02221126, -7.83317138, -0.08359713, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20020, 20, 0.0, 115.64795538, 0.02348878, 115.64795538, 0.07046635, 80.95356877, -1869.38989204, 0.05, 2, 0, 70020, 21020, 2, 3)
    ops.uniaxialMaterial('LimitState', 40020, 28.91198884, 9.281e-05, 86.73596653, 0.00027842, 289.11988845, 0.00092807, -28.91198884, -9.281e-05, -86.73596653, -0.00027842, -289.11988845, -0.00092807, 0.4, 0.3, 0.003, 0.0, 0.0, 20020, 2)
    ops.limitCurve('ThreePoint', 10020, 20, 0.0, 126.28253545, 0.01997189, 126.28253545, 0.05991567, 88.39777482, -2318.52440731, 0.05, 2, 0, 70020, 21020, 1, 3)
    ops.uniaxialMaterial('LimitState', 30020, 31.57063386, 0.00010134, 94.71190159, 0.00030402, 315.70633863, 0.00101342, -31.57063386, -0.00010134, -94.71190159, -0.00030402, -315.70633863, -0.00101342, 0.4, 0.3, 0.003, 0.0, 0.0, 10020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 20, 99999, 'P', 40020, 'Vy', 30020, 'Vz', 20020, 'My', 10020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170020, 70020, 170020, 20, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121020, 121020, 21020, 20, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171003, 6.6, 0.0, 2.975)
    ops.node(122003, 6.6, 0.0, 5.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1003, 171003, 122003, 0.135, 30028935.70045829, 12512056.54185762, 0.002377, 0.00250594, 0.00111375, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21003, 84.54876704, 0.00099649, 102.10161127, 0.021994, 10.21016113, 0.06200942, -84.54876704, -0.00099649, -102.10161127, -0.021994, -10.21016113, -0.06200942, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11003, 139.33993333, 0.00074618, 168.26776078, 0.02469427, 16.82677608, 0.07935578, -139.33993333, -0.00074618, -168.26776078, -0.02469427, -16.82677608, -0.07935578, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21003, 1003, 0.0, 156.87057644, 0.01992985, 156.87057644, 0.05978955, 109.80940351, -2196.75857384, 0.05, 2, 0, 71003, 22003, 2, 3)
    ops.uniaxialMaterial('LimitState', 41003, 39.21764411, 7.523e-05, 117.65293233, 0.00022568, 392.1764411, 0.00075225, -39.21764411, -7.523e-05, -117.65293233, -0.00022568, -392.1764411, -0.00075225, 0.4, 0.3, 0.003, 0.0, 0.0, 21003, 2)
    ops.limitCurve('ThreePoint', 11003, 1003, 0.0, 194.55647927, 0.0149236, 194.55647927, 0.04477079, 136.18953549, -3592.00273415, 0.05, 2, 0, 71003, 22003, 1, 3)
    ops.uniaxialMaterial('LimitState', 31003, 48.63911982, 9.33e-05, 145.91735945, 0.00027989, 486.39119817, 0.00093297, -48.63911982, -9.33e-05, -145.91735945, -0.00027989, -486.39119817, -0.00093297, 0.4, 0.3, 0.003, 0.0, 0.0, 11003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1003, 99999, 'P', 41003, 'Vy', 31003, 'Vz', 21003, 'My', 11003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171003, 71003, 171003, 1003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122003, 122003, 22003, 1003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171004, 10.3, 0.0, 2.95)
    ops.node(122004, 10.3, 0.0, 5.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1004, 171004, 122004, 0.075, 31336381.13659529, 13056825.47358137, 0.00077515, 0.00061875, 0.00042969, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21004, 42.84906532, 0.00113877, 51.57356154, 0.01673396, 5.15735615, 0.06362886, -42.84906532, -0.00113877, -51.57356154, -0.01673396, -5.15735615, -0.06362886, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11004, 57.00258463, 0.0009717, 68.60887826, 0.01753409, 6.86088783, 0.07162369, -57.00258463, -0.0009717, -68.60887826, -0.01753409, -6.86088783, -0.07162369, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21004, 1004, 0.0, 98.89707556, 0.02277538, 98.89707556, 0.06832614, 69.2279529, -1548.42331665, 0.05, 2, 0, 71004, 22004, 2, 3)
    ops.uniaxialMaterial('LimitState', 41004, 24.72426889, 8.18e-05, 74.17280667, 0.00024541, 247.24268891, 0.00081803, -24.72426889, -8.18e-05, -74.17280667, -0.00024541, -247.24268891, -0.00081803, 0.4, 0.3, 0.003, 0.0, 0.0, 21004, 2)
    ops.limitCurve('ThreePoint', 11004, 1004, 0.0, 107.52430637, 0.01943407, 107.52430637, 0.0583022, 75.26701446, -1941.37749736, 0.05, 2, 0, 71004, 22004, 1, 3)
    ops.uniaxialMaterial('LimitState', 31004, 26.88107659, 8.894e-05, 80.64322978, 0.00026682, 268.81076593, 0.00088939, -26.88107659, -8.894e-05, -80.64322978, -0.00026682, -268.81076593, -0.00088939, 0.4, 0.3, 0.003, 0.0, 0.0, 11004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1004, 99999, 'P', 41004, 'Vy', 31004, 'Vz', 21004, 'My', 11004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171004, 71004, 171004, 1004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122004, 122004, 22004, 1004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171005, 0.0, 5.7, 2.95)
    ops.node(122005, 0.0, 5.7, 5.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1005, 171005, 122005, 0.1, 29935044.88287506, 12472935.36786461, 0.00127345, 0.00057292, 0.00146667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21005, 90.71437691, 0.00078397, 109.40974859, 0.02202491, 10.94097486, 0.08267848, -90.71437691, -0.00078397, -109.40974859, -0.02202491, -10.94097486, -0.08267848, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11005, 50.59726738, 0.00112914, 61.02488373, 0.01927003, 6.10248837, 0.06098885, -50.59726738, -0.00112914, -61.02488373, -0.01927003, -6.10248837, -0.06098885, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21005, 1005, 0.0, 160.23322448, 0.0156793, 160.23322448, 0.0470379, 112.16325714, -3438.33841884, 0.05, 2, 0, 71005, 22005, 2, 3)
    ops.uniaxialMaterial('LimitState', 41005, 40.05830612, 0.00010406, 120.17491836, 0.00031217, 400.5830612, 0.00104056, -40.05830612, -0.00010406, -120.17491836, -0.00031217, -400.5830612, -0.00104056, 0.4, 0.3, 0.003, 0.0, 0.0, 21005, 2)
    ops.limitCurve('ThreePoint', 11005, 1005, 0.0, 127.13301904, 0.02258288, 127.13301904, 0.06774864, 88.99311333, -1929.42638274, 0.05, 2, 0, 71005, 22005, 1, 3)
    ops.uniaxialMaterial('LimitState', 31005, 31.78325476, 8.256e-05, 95.34976428, 0.00024768, 317.83254761, 0.00082561, -31.78325476, -8.256e-05, -95.34976428, -0.00024768, -317.83254761, -0.00082561, 0.4, 0.3, 0.003, 0.0, 0.0, 11005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1005, 99999, 'P', 41005, 'Vy', 31005, 'Vz', 21005, 'My', 11005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171005, 71005, 171005, 1005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122005, 122005, 22005, 1005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171006, 2.9, 5.7, 2.975)
    ops.node(122006, 2.9, 5.7, 5.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1006, 171006, 122006, 0.18, 31154246.17458325, 12980935.90607635, 0.00370786, 0.001485, 0.00594, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21006, 245.04293802, 0.00064568, 294.98051982, 0.0309169, 29.49805198, 0.10094032, -245.04293802, -0.00064568, -294.98051982, -0.0309169, -29.49805198, -0.10094032, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11006, 106.47017901, 0.00100438, 128.16785908, 0.02500689, 12.81678591, 0.06538998, -106.47017901, -0.00100438, -128.16785908, -0.02500689, -12.81678591, -0.06538998, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21006, 1006, 0.0, 361.23186635, 0.01291369, 361.23186635, 0.03874108, 252.86230644, -7049.31962065, 0.05, 2, 0, 71006, 22006, 2, 3)
    ops.uniaxialMaterial('LimitState', 41006, 90.30796659, 0.00012523, 270.92389976, 0.00037568, 903.07966587, 0.00125225, -90.30796659, -0.00012523, -270.92389976, -0.00037568, -903.07966587, -0.00125225, 0.4, 0.3, 0.003, 0.0, 0.0, 21006, 2)
    ops.limitCurve('ThreePoint', 11006, 1006, 0.0, 219.30446966, 0.02008766, 219.30446966, 0.06026299, 153.51312876, -2966.23103762, 0.05, 2, 0, 71006, 22006, 1, 3)
    ops.uniaxialMaterial('LimitState', 31006, 54.82611741, 7.602e-05, 164.47835224, 0.00022807, 548.26117414, 0.00076025, -54.82611741, -7.602e-05, -164.47835224, -0.00022807, -548.26117414, -0.00076025, 0.4, 0.3, 0.003, 0.0, 0.0, 11006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1006, 99999, 'P', 41006, 'Vy', 31006, 'Vz', 21006, 'My', 11006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171006, 71006, 171006, 1006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122006, 122006, 22006, 1006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171007, 6.6, 5.7, 2.975)
    ops.node(122007, 6.6, 5.7, 5.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1007, 171007, 122007, 0.195, 30124476.33149886, 12551865.13812453, 0.00415543, 0.00160875, 0.00755219, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21007, 324.05145326, 0.00063572, 391.02370659, 0.04270445, 39.10237066, 0.14027603, -324.05145326, -0.00063572, -391.02370659, -0.04270445, -39.10237066, -0.14027603, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11007, 122.93716445, 0.00101777, 148.34479289, 0.03289514, 14.83447929, 0.08342417, -122.93716445, -0.00101777, -148.34479289, -0.03289514, -14.83447929, -0.08342417, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21007, 1007, 0.0, 491.48159482, 0.01271449, 491.48159482, 0.03814347, 344.03711637, -14090.73783199, 0.05, 2, 0, 71007, 22007, 2, 3)
    ops.uniaxialMaterial('LimitState', 41007, 122.87039871, 0.00016265, 368.61119612, 0.00048794, 1228.70398705, 0.00162648, -122.87039871, -0.00016265, -368.61119612, -0.00048794, -1228.70398705, -0.00162648, 0.4, 0.3, 0.003, 0.0, 0.0, 21007, 2)
    ops.limitCurve('ThreePoint', 11007, 1007, 0.0, 266.84191394, 0.02035535, 266.84191394, 0.06106605, 186.78933976, -4718.89392677, 0.05, 2, 0, 71007, 22007, 1, 3)
    ops.uniaxialMaterial('LimitState', 31007, 66.71047848, 8.831e-05, 200.13143545, 0.00026492, 667.10478485, 0.00088307, -66.71047848, -8.831e-05, -200.13143545, -0.00026492, -667.10478485, -0.00088307, 0.4, 0.3, 0.003, 0.0, 0.0, 11007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1007, 99999, 'P', 41007, 'Vy', 31007, 'Vz', 21007, 'My', 11007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171007, 71007, 171007, 1007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122007, 122007, 22007, 1007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171008, 10.3, 5.7, 2.95)
    ops.node(122008, 10.3, 5.7, 5.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1008, 171008, 122008, 0.125, 30270924.68025571, 12612885.28343988, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21008, 137.179577, 0.0006899, 165.3905685, 0.02897012, 16.53905685, 0.10803159, -137.179577, -0.0006899, -165.3905685, -0.02897012, -16.53905685, -0.10803159, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11008, 65.00202085, 0.0011406, 78.36969188, 0.02336708, 7.83696919, 0.06801643, -65.00202085, -0.0011406, -78.36969188, -0.02336708, -7.83696919, -0.06801643, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21008, 1008, 0.0, 246.01043036, 0.01379796, 246.01043036, 0.04139389, 172.20730125, -5984.57036745, 0.05, 2, 0, 71008, 22008, 2, 3)
    ops.uniaxialMaterial('LimitState', 41008, 61.50260759, 0.00012639, 184.50782277, 0.00037917, 615.02607589, 0.0012639, -61.50260759, -0.00012639, -184.50782277, -0.00037917, -615.02607589, -0.0012639, 0.4, 0.3, 0.003, 0.0, 0.0, 21008, 2)
    ops.limitCurve('ThreePoint', 11008, 1008, 0.0, 159.91366815, 0.022812, 159.91366815, 0.068436, 111.9395677, -2435.85891122, 0.05, 2, 0, 71008, 22008, 1, 3)
    ops.uniaxialMaterial('LimitState', 31008, 39.97841704, 8.216e-05, 119.93525111, 0.00024647, 399.78417037, 0.00082157, -39.97841704, -8.216e-05, -119.93525111, -0.00024647, -399.78417037, -0.00082157, 0.4, 0.3, 0.003, 0.0, 0.0, 11008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1008, 99999, 'P', 41008, 'Vy', 31008, 'Vz', 21008, 'My', 11008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171008, 71008, 171008, 1008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122008, 122008, 22008, 1008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171009, 0.0, 11.4, 2.95)
    ops.node(122009, 0.0, 11.4, 5.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1009, 171009, 122009, 0.1, 31555036.01345144, 13147931.67227143, 0.00127345, 0.00057292, 0.00146667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21009, 89.48134832, 0.00077051, 107.55062487, 0.0170176, 10.75506249, 0.07003004, -89.48134832, -0.00077051, -107.55062487, -0.0170176, -10.75506249, -0.07003004, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11009, 50.01285374, 0.00111128, 60.11212138, 0.01510105, 6.01121214, 0.05227804, -50.01285374, -0.00111128, -60.11212138, -0.01510105, -6.01121214, -0.05227804, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21009, 1009, 0.0, 146.08907523, 0.01541017, 146.08907523, 0.04623052, 102.26235266, -2523.97267467, 0.05, 2, 0, 71009, 22009, 2, 3)
    ops.uniaxialMaterial('LimitState', 41009, 36.52226881, 9e-05, 109.56680642, 0.00027, 365.22268808, 0.00090001, -36.52226881, -9e-05, -109.56680642, -0.00027, -365.22268808, -0.00090001, 0.4, 0.3, 0.003, 0.0, 0.0, 21009, 2)
    ops.limitCurve('ThreePoint', 11009, 1009, 0.0, 120.12632834, 0.02222565, 120.12632834, 0.06667696, 84.08842984, -1492.85913864, 0.05, 2, 0, 71009, 22009, 1, 3)
    ops.uniaxialMaterial('LimitState', 31009, 30.03158208, 7.401e-05, 90.09474625, 0.00022202, 300.31582084, 0.00074006, -30.03158208, -7.401e-05, -90.09474625, -0.00022202, -300.31582084, -0.00074006, 0.4, 0.3, 0.003, 0.0, 0.0, 11009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1009, 99999, 'P', 41009, 'Vy', 31009, 'Vz', 21009, 'My', 11009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171009, 71009, 171009, 1009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122009, 122009, 22009, 1009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171010, 2.9, 11.4, 2.975)
    ops.node(122010, 2.9, 11.4, 5.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1010, 171010, 122010, 0.165, 30625221.39506496, 12760508.9146104, 0.00326155, 0.00136125, 0.00457531, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21010, 198.28685164, 0.00065687, 238.91143228, 0.02728978, 23.89114323, 0.09573127, -198.28685164, -0.00065687, -238.91143228, -0.02728978, -23.89114323, -0.09573127, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11010, 98.99739513, 0.00096057, 119.27976701, 0.02265815, 11.9279767, 0.06474885, -98.99739513, -0.00096057, -119.27976701, -0.02265815, -11.9279767, -0.06474885, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21010, 1010, 0.0, 314.78188228, 0.01313745, 314.78188228, 0.03941235, 220.3473176, -6385.82222147, 0.05, 2, 0, 71010, 22010, 2, 3)
    ops.uniaxialMaterial('LimitState', 41010, 78.69547057, 0.0001211, 236.08641171, 0.0003633, 786.95470571, 0.001211, -78.69547057, -0.0001211, -236.08641171, -0.0003633, -786.95470571, -0.001211, 0.4, 0.3, 0.003, 0.0, 0.0, 21010, 2)
    ops.limitCurve('ThreePoint', 11010, 1010, 0.0, 206.67320213, 0.01921134, 206.67320213, 0.05763403, 144.67124149, -2988.5409243, 0.05, 2, 0, 71010, 22010, 1, 3)
    ops.uniaxialMaterial('LimitState', 31010, 51.66830053, 7.951e-05, 155.0049016, 0.00023853, 516.68300532, 0.00079509, -51.66830053, -7.951e-05, -155.0049016, -0.00023853, -516.68300532, -0.00079509, 0.4, 0.3, 0.003, 0.0, 0.0, 11010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1010, 99999, 'P', 41010, 'Vy', 31010, 'Vz', 21010, 'My', 11010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171010, 71010, 171010, 1010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122010, 122010, 22010, 1010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171011, 6.6, 11.4, 2.975)
    ops.node(122011, 6.6, 11.4, 5.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1011, 171011, 122011, 0.195, 30177516.60486295, 12573965.25202623, 0.00415543, 0.00160875, 0.00755219, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21011, 321.35388654, 0.00063058, 387.73666871, 0.04282261, 38.77366687, 0.14061462, -321.35388654, -0.00063058, -387.73666871, -0.04282261, -38.77366687, -0.14061462, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11011, 121.97138442, 0.00100613, 147.16728271, 0.03297694, 14.71672827, 0.08362013, -121.97138442, -0.00100613, -147.16728271, -0.03297694, -14.71672827, -0.08362013, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21011, 1011, 0.0, 496.39084609, 0.01261152, 496.39084609, 0.03783455, 347.47359227, -14481.5836047, 0.05, 2, 0, 71011, 22011, 2, 3)
    ops.uniaxialMaterial('LimitState', 41011, 124.09771152, 0.00016398, 372.29313457, 0.00049195, 1240.97711523, 0.00163984, -124.09771152, -0.00016398, -372.29313457, -0.00049195, -1240.97711523, -0.00163984, 0.4, 0.3, 0.003, 0.0, 0.0, 21011, 2)
    ops.limitCurve('ThreePoint', 11011, 1011, 0.0, 269.17184491, 0.02012266, 269.17184491, 0.06036798, 188.42029144, -4820.05357581, 0.05, 2, 0, 71011, 22011, 1, 3)
    ops.uniaxialMaterial('LimitState', 31011, 67.29296123, 8.892e-05, 201.87888368, 0.00026677, 672.92961227, 0.00088922, -67.29296123, -8.892e-05, -201.87888368, -0.00026677, -672.92961227, -0.00088922, 0.4, 0.3, 0.003, 0.0, 0.0, 11011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1011, 99999, 'P', 41011, 'Vy', 31011, 'Vz', 21011, 'My', 11011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171011, 71011, 171011, 1011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122011, 122011, 22011, 1011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171012, 10.3, 11.4, 2.95)
    ops.node(122012, 10.3, 11.4, 5.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1012, 171012, 122012, 0.125, 30607664.87715465, 12753193.69881444, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21012, 136.59489418, 0.00068819, 164.57291107, 0.02192622, 16.45729111, 0.08436683, -136.59489418, -0.00068819, -164.57291107, -0.02192622, -16.45729111, -0.08436683, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11012, 64.68477027, 0.00114106, 77.93381304, 0.01807445, 7.7933813, 0.05456021, -64.68477027, -0.00114106, -77.93381304, -0.01807445, -7.7933813, -0.05456021, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21012, 1012, 0.0, 215.56262892, 0.01376376, 215.56262892, 0.04129128, 150.89384024, -4158.90128709, 0.05, 2, 0, 71012, 22012, 2, 3)
    ops.uniaxialMaterial('LimitState', 41012, 53.89065723, 0.00010953, 161.67197169, 0.00032859, 538.9065723, 0.00109529, -53.89065723, -0.00010953, -161.67197169, -0.00032859, -538.9065723, -0.00109529, 0.4, 0.3, 0.003, 0.0, 0.0, 21012, 2)
    ops.limitCurve('ThreePoint', 11012, 1012, 0.0, 145.1996285, 0.02282123, 145.1996285, 0.0684637, 101.63973995, -1840.80665855, 0.05, 2, 0, 71012, 22012, 1, 3)
    ops.uniaxialMaterial('LimitState', 31012, 36.29990712, 7.378e-05, 108.89972137, 0.00022133, 362.99907125, 0.00073777, -36.29990712, -7.378e-05, -108.89972137, -0.00022133, -362.99907125, -0.00073777, 0.4, 0.3, 0.003, 0.0, 0.0, 11012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1012, 99999, 'P', 41012, 'Vy', 31012, 'Vz', 21012, 'My', 11012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171012, 71012, 171012, 1012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122012, 122012, 22012, 1012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171013, 0.0, 17.1, 2.95)
    ops.node(122013, 0.0, 17.1, 5.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1013, 171013, 122013, 0.1, 30963576.5221842, 12901490.21757675, 0.00127345, 0.00057292, 0.00146667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21013, 89.58460498, 0.00078924, 107.82597922, 0.01702365, 10.78259792, 0.06922898, -89.58460498, -0.00078924, -107.82597922, -0.01702365, -10.78259792, -0.06922898, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11013, 50.08289263, 0.00115134, 60.28085899, 0.01513018, 6.0280859, 0.05174115, -50.08289263, -0.00115134, -60.28085899, -0.01513018, -6.0280859, -0.05174115, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21013, 1013, 0.0, 145.19697978, 0.01578489, 145.19697978, 0.04735467, 101.63788585, -2567.09898777, 0.05, 2, 0, 71013, 22013, 2, 3)
    ops.uniaxialMaterial('LimitState', 41013, 36.29924495, 9.116e-05, 108.89773484, 0.00027348, 362.99244946, 0.0009116, -36.29924495, -9.116e-05, -108.89773484, -0.00027348, -362.99244946, -0.0009116, 0.4, 0.3, 0.003, 0.0, 0.0, 21013, 2)
    ops.limitCurve('ThreePoint', 11013, 1013, 0.0, 118.8724957, 0.02302674, 118.8724957, 0.06908022, 83.21074699, -1513.74317445, 0.05, 2, 0, 71013, 22013, 1, 3)
    ops.uniaxialMaterial('LimitState', 31013, 29.71812392, 7.463e-05, 89.15437177, 0.0002239, 297.18123924, 0.00074632, -29.71812392, -7.463e-05, -89.15437177, -0.0002239, -297.18123924, -0.00074632, 0.4, 0.3, 0.003, 0.0, 0.0, 11013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1013, 99999, 'P', 41013, 'Vy', 31013, 'Vz', 21013, 'My', 11013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171013, 71013, 171013, 1013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122013, 122013, 22013, 1013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171014, 2.9, 17.1, 2.975)
    ops.node(122014, 2.9, 17.1, 5.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1014, 171014, 122014, 0.165, 31248152.84991597, 13020063.68746499, 0.00326155, 0.00136125, 0.00457531, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21014, 198.3951225, 0.00066708, 238.69905913, 0.03768516, 23.86990591, 0.13692319, -198.3951225, -0.00066708, -238.69905913, -0.03768516, -23.86990591, -0.13692319, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11014, 98.95041554, 0.00099185, 119.05217625, 0.0306817, 11.90521762, 0.08948715, -98.95041554, -0.00099185, -119.05217625, -0.0306817, -11.90521762, -0.08948715, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21014, 1014, 0.0, 395.43195923, 0.01334163, 395.43195923, 0.04002489, 276.80237146, -11434.86240033, 0.05, 2, 0, 71014, 22014, 2, 3)
    ops.uniaxialMaterial('LimitState', 41014, 98.85798981, 0.00014909, 296.57396942, 0.00044728, 988.57989807, 0.00149094, -98.85798981, -0.00014909, -296.57396942, -0.00044728, -988.57989807, -0.00149094, 0.4, 0.3, 0.003, 0.0, 0.0, 21014, 2)
    ops.limitCurve('ThreePoint', 11014, 1014, 0.0, 251.59963647, 0.01983702, 251.59963647, 0.05951107, 176.11974553, -4817.91426309, 0.05, 2, 0, 71014, 22014, 1, 3)
    ops.uniaxialMaterial('LimitState', 31014, 62.89990912, 9.486e-05, 188.69972735, 0.00028459, 628.99909118, 0.00094863, -62.89990912, -9.486e-05, -188.69972735, -0.00028459, -628.99909118, -0.00094863, 0.4, 0.3, 0.003, 0.0, 0.0, 11014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1014, 99999, 'P', 41014, 'Vy', 31014, 'Vz', 21014, 'My', 11014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171014, 71014, 171014, 1014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122014, 122014, 22014, 1014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171015, 6.6, 17.1, 2.975)
    ops.node(122015, 6.6, 17.1, 5.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1015, 171015, 122015, 0.195, 30548724.20806331, 12728635.08669305, 0.00415543, 0.00160875, 0.00755219, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21015, 321.23907037, 0.00062478, 387.28865186, 0.04292351, 38.72886519, 0.14167095, -321.23907037, -0.00062478, -387.28865186, -0.04292351, -38.72886519, -0.14167095, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11015, 122.02160364, 0.00098847, 147.11031979, 0.03304012, 14.71103198, 0.08417809, -122.02160364, -0.00098847, -147.11031979, -0.03304012, -14.71103198, -0.08417809, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21015, 1015, 0.0, 502.60803768, 0.01249569, 502.60803768, 0.03748706, 351.82562637, -14696.69882362, 0.05, 2, 0, 71015, 22015, 2, 3)
    ops.uniaxialMaterial('LimitState', 41015, 125.65200942, 0.00016402, 376.95602826, 0.00049206, 1256.52009419, 0.0016402, -125.65200942, -0.00016402, -376.95602826, -0.00049206, -1256.52009419, -0.0016402, 0.4, 0.3, 0.003, 0.0, 0.0, 21015, 2)
    ops.limitCurve('ThreePoint', 11015, 1015, 0.0, 272.69350836, 0.0197694, 272.69350836, 0.05930819, 190.88545585, -4878.00266823, 0.05, 2, 0, 71015, 22015, 1, 3)
    ops.uniaxialMaterial('LimitState', 31015, 68.17337709, 8.899e-05, 204.52013127, 0.00026697, 681.73377091, 0.0008899, -68.17337709, -8.899e-05, -204.52013127, -0.00026697, -681.73377091, -0.0008899, 0.4, 0.3, 0.003, 0.0, 0.0, 11015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1015, 99999, 'P', 41015, 'Vy', 31015, 'Vz', 21015, 'My', 11015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171015, 71015, 171015, 1015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122015, 122015, 22015, 1015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171016, 10.3, 17.1, 2.95)
    ops.node(122016, 10.3, 17.1, 5.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1016, 171016, 122016, 0.125, 31663722.74928774, 13193217.81220322, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21016, 138.94759702, 0.00068494, 166.99039961, 0.02890902, 16.69903996, 0.1109502, -138.94759702, -0.00068494, -166.99039961, -0.02890902, -16.69903996, -0.1109502, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11016, 65.99752727, 0.00112015, 79.31733753, 0.0233025, 7.93173375, 0.06963462, -65.99752727, -0.00112015, -79.31733753, -0.0233025, -7.93173375, -0.06963462, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21016, 1016, 0.0, 252.59276037, 0.0136988, 252.59276037, 0.04109641, 176.81493226, -6000.45831606, 0.05, 2, 0, 71016, 22016, 2, 3)
    ops.uniaxialMaterial('LimitState', 41016, 63.14819009, 0.00012406, 189.44457028, 0.00037219, 631.48190092, 0.00124064, -63.14819009, -0.00012406, -189.44457028, -0.00037219, -631.48190092, -0.00124064, 0.4, 0.3, 0.003, 0.0, 0.0, 21016, 2)
    ops.limitCurve('ThreePoint', 11016, 1016, 0.0, 165.41120701, 0.02240296, 165.41120701, 0.06720888, 115.78784491, -2439.82128355, 0.05, 2, 0, 71016, 22016, 1, 3)
    ops.uniaxialMaterial('LimitState', 31016, 41.35280175, 8.124e-05, 124.05840526, 0.00024373, 413.52801754, 0.00081244, -41.35280175, -8.124e-05, -124.05840526, -0.00024373, -413.52801754, -0.00081244, 0.4, 0.3, 0.003, 0.0, 0.0, 11016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1016, 99999, 'P', 41016, 'Vy', 31016, 'Vz', 21016, 'My', 11016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171016, 71016, 171016, 1016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122016, 122016, 22016, 1016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171017, 0.0, 22.8, 2.95)
    ops.node(122017, 0.0, 22.8, 5.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1017, 171017, 122017, 0.0625, 31284154.91546357, 13035064.54810982, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21017, 33.59769859, 0.00110214, 40.44843347, 0.01690326, 4.04484335, 0.07111389, -33.59769859, -0.00110214, -40.44843347, -0.01690326, -4.04484335, -0.07111389, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11017, 33.59769859, 0.00110214, 40.44843347, 0.01690326, 4.04484335, 0.07111389, -33.59769859, -0.00110214, -40.44843347, -0.01690326, -4.04484335, -0.07111389, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21017, 1017, 0.0, 88.35339986, 0.02204275, 88.35339986, 0.06612825, 61.8473799, -1577.29085128, 0.05, 2, 0, 71017, 22017, 2, 3)
    ops.uniaxialMaterial('LimitState', 41017, 22.08834997, 8.784e-05, 66.2650499, 0.00026353, 220.88349966, 0.00087845, -22.08834997, -8.784e-05, -66.2650499, -0.00026353, -220.88349966, -0.00087845, 0.4, 0.3, 0.003, 0.0, 0.0, 21017, 2)
    ops.limitCurve('ThreePoint', 11017, 1017, 0.0, 88.35339986, 0.02204275, 88.35339986, 0.06612825, 61.8473799, -1577.29085128, 0.05, 2, 0, 71017, 22017, 1, 3)
    ops.uniaxialMaterial('LimitState', 31017, 22.08834997, 8.784e-05, 66.2650499, 0.00026353, 220.88349966, 0.00087845, -22.08834997, -8.784e-05, -66.2650499, -0.00026353, -220.88349966, -0.00087845, 0.4, 0.3, 0.003, 0.0, 0.0, 11017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1017, 99999, 'P', 41017, 'Vy', 31017, 'Vz', 21017, 'My', 11017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171017, 71017, 171017, 1017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122017, 122017, 22017, 1017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171018, 2.9, 22.8, 2.975)
    ops.node(122018, 2.9, 22.8, 5.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1018, 171018, 122018, 0.12, 31336359.05442608, 13056816.27267753, 0.00194385, 0.00176, 0.00099, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21018, 91.84717313, 0.00102602, 110.57514851, 0.02998551, 11.05751485, 0.0862847, -91.84717313, -0.00102602, -110.57514851, -0.02998551, -11.05751485, -0.0862847, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11018, 116.17537747, 0.00081716, 139.86396292, 0.03284008, 13.98639629, 0.1043048, -116.17537747, -0.00081716, -139.86396292, -0.03284008, -13.98639629, -0.1043048, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21018, 1018, 0.0, 176.20616961, 0.02052044, 176.20616961, 0.06156133, 123.34431872, -3378.18135883, 0.05, 2, 0, 71018, 22018, 2, 3)
    ops.uniaxialMaterial('LimitState', 41018, 44.0515424, 9.109e-05, 132.1546272, 0.00027328, 440.51542402, 0.00091094, -44.0515424, -9.109e-05, -132.1546272, -0.00027328, -440.51542402, -0.00091094, 0.4, 0.3, 0.003, 0.0, 0.0, 21018, 2)
    ops.limitCurve('ThreePoint', 11018, 1018, 0.0, 205.41197896, 0.01634323, 205.41197896, 0.04902968, 143.78838527, -5034.05384207, 0.05, 2, 0, 71018, 22018, 1, 3)
    ops.uniaxialMaterial('LimitState', 31018, 51.35299474, 0.00010619, 154.05898422, 0.00031858, 513.5299474, 0.00106192, -51.35299474, -0.00010619, -154.05898422, -0.00031858, -513.5299474, -0.00106192, 0.4, 0.3, 0.003, 0.0, 0.0, 11018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1018, 99999, 'P', 41018, 'Vy', 31018, 'Vz', 21018, 'My', 11018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171018, 71018, 171018, 1018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122018, 122018, 22018, 1018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171019, 6.6, 22.8, 2.975)
    ops.node(122019, 6.6, 22.8, 5.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1019, 171019, 122019, 0.1575, 31055081.00501032, 12939617.08542097, 0.00337604, 0.00292359, 0.00176859, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21019, 108.83282272, 0.00087866, 131.25308958, 0.02828847, 13.12530896, 0.08084468, -108.83282272, -0.00087866, -131.25308958, -0.02828847, -13.12530896, -0.08084468, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11019, 156.66832435, 0.0007428, 188.94301459, 0.03059994, 18.89430146, 0.09497663, -156.66832435, -0.0007428, -188.94301459, -0.03059994, -18.89430146, -0.09497663, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21019, 1019, 0.0, 208.60175012, 0.01757318, 208.60175012, 0.05271955, 146.02122508, -3737.32984892, 0.05, 2, 0, 71019, 22019, 2, 3)
    ops.uniaxialMaterial('LimitState', 41019, 52.15043753, 8.291e-05, 156.45131259, 0.00024873, 521.50437529, 0.00082909, -52.15043753, -8.291e-05, -156.45131259, -0.00024873, -521.50437529, -0.00082909, 0.4, 0.3, 0.003, 0.0, 0.0, 21019, 2)
    ops.limitCurve('ThreePoint', 11019, 1019, 0.0, 243.80185747, 0.01485599, 243.80185747, 0.04456796, 170.66130023, -5280.22601887, 0.05, 2, 0, 71019, 22019, 1, 3)
    ops.uniaxialMaterial('LimitState', 31019, 60.95046437, 9.69e-05, 182.8513931, 0.0002907, 609.50464367, 0.00096899, -60.95046437, -9.69e-05, -182.8513931, -0.0002907, -609.50464367, -0.00096899, 0.4, 0.3, 0.003, 0.0, 0.0, 11019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1019, 99999, 'P', 41019, 'Vy', 31019, 'Vz', 21019, 'My', 11019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171019, 71019, 171019, 1019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122019, 122019, 22019, 1019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171020, 10.3, 22.8, 2.95)
    ops.node(122020, 10.3, 22.8, 5.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1020, 171020, 122020, 0.075, 32103288.56730719, 13376370.236378, 0.00077515, 0.00061875, 0.00042969, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21020, 45.52036455, 0.00113131, 54.67778744, 0.01646006, 5.46777874, 0.06412479, -45.52036455, -0.00113131, -54.67778744, -0.01646006, -5.46777874, -0.06412479, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11020, 51.52402267, 0.00096315, 61.88921349, 0.01724257, 6.18892135, 0.07222011, -51.52402267, -0.00096315, -61.88921349, -0.01724257, -6.18892135, -0.07222011, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21020, 1020, 0.0, 99.41765995, 0.0226263, 99.41765995, 0.0678789, 69.59236197, -1492.25002481, 0.05, 2, 0, 71020, 22020, 2, 3)
    ops.uniaxialMaterial('LimitState', 41020, 24.85441499, 8.027e-05, 74.56324496, 0.00024081, 248.54414988, 0.00080269, -24.85441499, -8.027e-05, -74.56324496, -0.00024081, -248.54414988, -0.00080269, 0.4, 0.3, 0.003, 0.0, 0.0, 21020, 2)
    ops.limitCurve('ThreePoint', 11020, 1020, 0.0, 107.78254525, 0.019263, 107.78254525, 0.057789, 75.44778167, -1865.79152523, 0.05, 2, 0, 71020, 22020, 1, 3)
    ops.uniaxialMaterial('LimitState', 31020, 26.94563631, 8.702e-05, 80.83690894, 0.00026107, 269.45636312, 0.00087023, -26.94563631, -8.702e-05, -80.83690894, -0.00026107, -269.45636312, -0.00087023, 0.4, 0.3, 0.003, 0.0, 0.0, 11020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1020, 99999, 'P', 41020, 'Vy', 31020, 'Vz', 21020, 'My', 11020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171020, 71020, 171020, 1020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122020, 122020, 22020, 1020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172003, 6.6, 0.0, 5.675)
    ops.node(123003, 6.6, 0.0, 7.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2003, 172003, 123003, 0.0875, 31514330.31366819, 13130970.96402841, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22003, 51.74949297, 0.00115369, 62.2963325, 0.01591317, 6.22963325, 0.05339364, -51.74949297, -0.00115369, -62.2963325, -0.01591317, -6.22963325, -0.05339364, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12003, 75.79740663, 0.00086897, 91.24534705, 0.0172437, 9.12453471, 0.0651944, -75.79740663, -0.00086897, -91.24534705, -0.0172437, -9.12453471, -0.0651944, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22003, 2003, 0.0, 94.01211609, 0.02307388, 94.01211609, 0.06922164, 65.80848126, -1191.43481629, 0.05, 2, 0, 72003, 23003, 2, 3)
    ops.uniaxialMaterial('LimitState', 42003, 23.50302902, 6.628e-05, 70.50908707, 0.00019883, 235.03029023, 0.00066277, -23.50302902, -6.628e-05, -70.50908707, -0.00019883, -235.03029023, -0.00066277, 0.4, 0.3, 0.003, 0.0, 0.0, 22003, 2)
    ops.limitCurve('ThreePoint', 12003, 2003, 0.0, 112.5595366, 0.0173793, 112.5595366, 0.0521379, 78.79167562, -1747.64125793, 0.05, 2, 0, 72003, 23003, 1, 3)
    ops.uniaxialMaterial('LimitState', 32003, 28.13988415, 7.935e-05, 84.41965245, 0.00023806, 281.3988415, 0.00079353, -28.13988415, -7.935e-05, -84.41965245, -0.00023806, -281.3988415, -0.00079353, 0.4, 0.3, 0.003, 0.0, 0.0, 12003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2003, 99999, 'P', 42003, 'Vy', 32003, 'Vz', 22003, 'My', 12003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172003, 72003, 172003, 2003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123003, 123003, 23003, 2003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172004, 10.3, 0.0, 5.65)
    ops.node(123004, 10.3, 0.0, 7.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2004, 172004, 123004, 0.0625, 30411888.6663686, 12671620.27765359, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22004, 30.23081268, 0.00109148, 36.54234589, 0.01793117, 3.65423459, 0.07427797, -30.23081268, -0.00109148, -36.54234589, -0.01793117, -3.65423459, -0.07427797, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12004, 30.23081268, 0.00109148, 36.54234589, 0.01793117, 3.65423459, 0.07427797, -30.23081268, -0.00109148, -36.54234589, -0.01793117, -3.65423459, -0.07427797, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22004, 2004, 0.0, 84.63438544, 0.02182956, 84.63438544, 0.06548867, 59.24406981, -1773.79558443, 0.05, 2, 0, 72004, 23004, 2, 3)
    ops.uniaxialMaterial('LimitState', 42004, 21.15859636, 8.656e-05, 63.47578908, 0.00025968, 211.5859636, 0.0008656, -21.15859636, -8.656e-05, -63.47578908, -0.00025968, -211.5859636, -0.0008656, 0.4, 0.3, 0.003, 0.0, 0.0, 22004, 2)
    ops.limitCurve('ThreePoint', 12004, 2004, 0.0, 84.63438544, 0.02182956, 84.63438544, 0.06548867, 59.24406981, -1773.79558443, 0.05, 2, 0, 72004, 23004, 1, 3)
    ops.uniaxialMaterial('LimitState', 32004, 21.15859636, 8.656e-05, 63.47578908, 0.00025968, 211.5859636, 0.0008656, -21.15859636, -8.656e-05, -63.47578908, -0.00025968, -211.5859636, -0.0008656, 0.4, 0.3, 0.003, 0.0, 0.0, 12004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2004, 99999, 'P', 42004, 'Vy', 32004, 'Vz', 22004, 'My', 12004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172004, 72004, 172004, 2004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123004, 123004, 23004, 2004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172005, 0.0, 5.7, 5.65)
    ops.node(123005, 0.0, 5.7, 7.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2005, 172005, 123005, 0.0875, 31822774.57256261, 13259489.40523442, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22005, 66.57229356, 0.00083052, 80.12057401, 0.01752761, 8.0120574, 0.07414865, -66.57229356, -0.00083052, -80.12057401, -0.01752761, -8.0120574, -0.07414865, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12005, 42.29648894, 0.00109098, 50.90434461, 0.01606421, 5.09043446, 0.05978791, -42.29648894, -0.00109098, -50.90434461, -0.01606421, -5.09043446, -0.05978791, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22005, 2005, 0.0, 124.25103298, 0.0166103, 124.25103298, 0.04983091, 86.97572309, -2400.8407808, 0.05, 2, 0, 72005, 23005, 2, 3)
    ops.uniaxialMaterial('LimitState', 42005, 31.06275825, 8.675e-05, 93.18827474, 0.00026024, 310.62758245, 0.00086746, -31.06275825, -8.675e-05, -93.18827474, -0.00026024, -310.62758245, -0.00086746, 0.4, 0.3, 0.003, 0.0, 0.0, 22005, 2)
    ops.limitCurve('ThreePoint', 12005, 2005, 0.0, 107.04312434, 0.02181968, 107.04312434, 0.06545903, 74.93018703, -1554.82004825, 0.05, 2, 0, 72005, 23005, 1, 3)
    ops.uniaxialMaterial('LimitState', 32005, 26.76078108, 7.473e-05, 80.28234325, 0.0002242, 267.60781084, 0.00074732, -26.76078108, -7.473e-05, -80.28234325, -0.0002242, -267.60781084, -0.00074732, 0.4, 0.3, 0.003, 0.0, 0.0, 12005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2005, 99999, 'P', 42005, 'Vy', 32005, 'Vz', 22005, 'My', 12005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172005, 72005, 172005, 2005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123005, 123005, 23005, 2005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172006, 2.9, 5.7, 5.675)
    ops.node(123006, 2.9, 5.7, 7.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2006, 172006, 123006, 0.125, 33068103.77205007, 13778376.57168753, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22006, 152.32760178, 0.00068481, 182.50031064, 0.02529669, 18.25003106, 0.09300985, -152.32760178, -0.00068481, -182.50031064, -0.02529669, -18.25003106, -0.09300985, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12006, 67.39034256, 0.00112773, 80.73887009, 0.02075113, 8.07388701, 0.06031778, -67.39034256, -0.00112773, -80.73887009, -0.02075113, -8.07388701, -0.06031778, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22006, 2006, 0.0, 220.65126609, 0.01369611, 220.65126609, 0.04108833, 154.45588626, -4167.8432778, 0.05, 2, 0, 72006, 23006, 2, 3)
    ops.uniaxialMaterial('LimitState', 42006, 55.16281652, 0.00010377, 165.48844957, 0.00031132, 551.62816522, 0.00103773, -55.16281652, -0.00010377, -165.48844957, -0.00031132, -551.62816522, -0.00103773, 0.4, 0.3, 0.003, 0.0, 0.0, 22006, 2)
    ops.limitCurve('ThreePoint', 12006, 2006, 0.0, 150.6803025, 0.0225545, 150.6803025, 0.06766351, 105.47621175, -1786.52619814, 0.05, 2, 0, 72006, 23006, 1, 3)
    ops.uniaxialMaterial('LimitState', 32006, 37.67007562, 7.087e-05, 113.01022687, 0.0002126, 376.70075624, 0.00070865, -37.67007562, -7.087e-05, -113.01022687, -0.0002126, -376.70075624, -0.00070865, 0.4, 0.3, 0.003, 0.0, 0.0, 12006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2006, 99999, 'P', 42006, 'Vy', 32006, 'Vz', 22006, 'My', 12006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172006, 72006, 172006, 2006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123006, 123006, 23006, 2006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172007, 6.6, 5.7, 5.675)
    ops.node(123007, 6.6, 5.7, 7.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2007, 172007, 123007, 0.1375, 31324040.71323092, 13051683.63051288, 0.00204719, 0.00078776, 0.00381276, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22007, 171.0571851, 0.00066216, 206.01280136, 0.0343213, 20.60128014, 0.11879411, -171.0571851, -0.00066216, -206.01280136, -0.0343213, -20.60128014, -0.11879411, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12007, 78.71272909, 0.00115486, 94.79771231, 0.02681655, 9.47977123, 0.07120215, -78.71272909, -0.00115486, -94.79771231, -0.02681655, -9.47977123, -0.07120215, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22007, 2007, 0.0, 286.72763993, 0.01324315, 286.72763993, 0.03972946, 200.70934795, -7404.79669908, 0.05, 2, 0, 72007, 23007, 2, 3)
    ops.uniaxialMaterial('LimitState', 42007, 71.68190998, 0.00012942, 215.04572994, 0.00038825, 716.81909981, 0.00129415, -71.68190998, -0.00012942, -215.04572994, -0.00038825, -716.81909981, -0.00129415, 0.4, 0.3, 0.003, 0.0, 0.0, 22007, 2)
    ops.limitCurve('ThreePoint', 12007, 2007, 0.0, 171.25231393, 0.02309721, 171.25231393, 0.06929164, 119.87661975, -2529.43162251, 0.05, 2, 0, 72007, 23007, 1, 3)
    ops.uniaxialMaterial('LimitState', 32007, 42.81307848, 7.73e-05, 128.43923545, 0.00023189, 428.13078483, 0.00077295, -42.81307848, -7.73e-05, -128.43923545, -0.00023189, -428.13078483, -0.00077295, 0.4, 0.3, 0.003, 0.0, 0.0, 12007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2007, 99999, 'P', 42007, 'Vy', 32007, 'Vz', 22007, 'My', 12007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172007, 72007, 172007, 2007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123007, 123007, 23007, 2007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172008, 10.3, 5.7, 5.65)
    ops.node(123008, 10.3, 5.7, 7.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2008, 172008, 123008, 0.1, 32495598.19316168, 13539832.58048403, 0.00127345, 0.00057292, 0.00146667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22008, 80.55323925, 0.00075751, 96.74894071, 0.0172272, 9.67489407, 0.07433734, -80.55323925, -0.00075751, -96.74894071, -0.0172272, -9.67489407, -0.07433734, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12008, 44.64190247, 0.00109522, 53.61741894, 0.01527665, 5.36174189, 0.05532731, -44.64190247, -0.00109522, -53.61741894, -0.01527665, -5.36174189, -0.05532731, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22008, 2008, 0.0, 144.68512524, 0.01515022, 144.68512524, 0.04545065, 101.27958767, -2744.69263991, 0.05, 2, 0, 72008, 23008, 2, 3)
    ops.uniaxialMaterial('LimitState', 42008, 36.17128131, 8.656e-05, 108.51384393, 0.00025967, 361.7128131, 0.00086556, -36.17128131, -8.656e-05, -108.51384393, -0.00025967, -361.7128131, -0.00086556, 0.4, 0.3, 0.003, 0.0, 0.0, 22008, 2)
    ops.limitCurve('ThreePoint', 12008, 2008, 0.0, 118.74966791, 0.02190431, 118.74966791, 0.06571292, 83.12476753, -1522.2431556, 0.05, 2, 0, 72008, 23008, 1, 3)
    ops.uniaxialMaterial('LimitState', 32008, 29.68741698, 7.104e-05, 89.06225093, 0.00021312, 296.87416977, 0.0007104, -29.68741698, -7.104e-05, -89.06225093, -0.00021312, -296.87416977, -0.0007104, 0.4, 0.3, 0.003, 0.0, 0.0, 12008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2008, 99999, 'P', 42008, 'Vy', 32008, 'Vz', 22008, 'My', 12008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172008, 72008, 172008, 2008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123008, 123008, 23008, 2008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172009, 0.0, 11.4, 5.65)
    ops.node(123009, 0.0, 11.4, 7.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2009, 172009, 123009, 0.0875, 30942893.27039208, 12892872.1959967, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22009, 64.87243239, 0.00084615, 78.28406202, 0.0175181, 7.8284062, 0.07379705, -64.87243239, -0.00084615, -78.28406202, -0.0175181, -7.8284062, -0.07379705, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12009, 41.20388002, 0.00112136, 49.72230854, 0.01607204, 4.97223085, 0.05953158, -41.20388002, -0.00112136, -49.72230854, -0.01607204, -4.97223085, -0.05953158, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22009, 2009, 0.0, 121.1138923, 0.01692291, 121.1138923, 0.05076872, 84.77972461, -2448.97984533, 0.05, 2, 0, 72009, 23009, 2, 3)
    ops.uniaxialMaterial('LimitState', 42009, 30.27847308, 8.696e-05, 90.83541923, 0.00026088, 302.78473075, 0.0008696, -30.27847308, -8.696e-05, -90.83541923, -0.00026088, -302.78473075, -0.0008696, 0.4, 0.3, 0.003, 0.0, 0.0, 22009, 2)
    ops.limitCurve('ThreePoint', 12009, 2009, 0.0, 103.93208593, 0.02242718, 103.93208593, 0.06728153, 72.75246015, -1572.425872, 0.05, 2, 0, 72009, 23009, 1, 3)
    ops.uniaxialMaterial('LimitState', 32009, 25.98302148, 7.462e-05, 77.94906445, 0.00022387, 259.83021483, 0.00074624, -25.98302148, -7.462e-05, -77.94906445, -0.00022387, -259.83021483, -0.00074624, 0.4, 0.3, 0.003, 0.0, 0.0, 12009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2009, 99999, 'P', 42009, 'Vy', 32009, 'Vz', 22009, 'My', 12009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172009, 72009, 172009, 2009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123009, 123009, 23009, 2009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172010, 2.9, 11.4, 5.675)
    ops.node(123010, 2.9, 11.4, 7.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2010, 172010, 123010, 0.125, 31483339.01953378, 13118057.92480574, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22010, 129.32968433, 0.00067555, 155.71553784, 0.02959512, 15.57155378, 0.11469439, -129.32968433, -0.00067555, -155.71553784, -0.02959512, -15.57155378, -0.11469439, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12010, 61.24542387, 0.00109954, 73.74072061, 0.0238285, 7.37407206, 0.07188766, -61.24542387, -0.00109954, -73.74072061, -0.0238285, -7.37407206, -0.07188766, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22010, 2010, 0.0, 251.36426251, 0.01351094, 251.36426251, 0.04053282, 175.95498375, -6899.90917097, 0.05, 2, 0, 72010, 23010, 2, 3)
    ops.uniaxialMaterial('LimitState', 42010, 62.84106563, 0.00012417, 188.52319688, 0.0003725, 628.41065626, 0.00124168, -62.84106563, -0.00012417, -188.52319688, -0.0003725, -628.41065626, -0.00124168, 0.4, 0.3, 0.003, 0.0, 0.0, 22010, 2)
    ops.limitCurve('ThreePoint', 12010, 2010, 0.0, 162.98205431, 0.02199076, 162.98205431, 0.06597229, 114.08743802, -2621.35417553, 0.05, 2, 0, 72010, 23010, 1, 3)
    ops.uniaxialMaterial('LimitState', 32010, 40.74551358, 8.051e-05, 122.23654073, 0.00024153, 407.45513577, 0.00080509, -40.74551358, -8.051e-05, -122.23654073, -0.00024153, -407.45513577, -0.00080509, 0.4, 0.3, 0.003, 0.0, 0.0, 12010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2010, 99999, 'P', 42010, 'Vy', 32010, 'Vz', 22010, 'My', 12010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172010, 72010, 172010, 2010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123010, 123010, 23010, 2010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172011, 6.6, 11.4, 5.675)
    ops.node(123011, 6.6, 11.4, 7.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2011, 172011, 123011, 0.1375, 31152873.39708161, 12980363.91545067, 0.00204719, 0.00078776, 0.00381276, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22011, 190.23515828, 0.00065998, 229.2132553, 0.03427001, 22.92132553, 0.11848427, -190.23515828, -0.00065998, -229.2132553, -0.03427001, -22.92132553, -0.11848427, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12011, 73.41957921, 0.00113963, 88.46283151, 0.02676388, 8.84628315, 0.07101363, -73.41957921, -0.00113963, -88.46283151, -0.02676388, -8.84628315, -0.07101363, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22011, 2011, 0.0, 281.07671488, 0.01319966, 281.07671488, 0.03959898, 196.75370042, -7083.75824449, 0.05, 2, 0, 72011, 23011, 2, 3)
    ops.uniaxialMaterial('LimitState', 42011, 70.26917872, 0.00012756, 210.80753616, 0.00038269, 702.69178721, 0.00127562, -70.26917872, -0.00012756, -210.80753616, -0.00038269, -702.69178721, -0.00127562, 0.4, 0.3, 0.003, 0.0, 0.0, 22011, 2)
    ops.limitCurve('ThreePoint', 12011, 2011, 0.0, 168.36247604, 0.02279266, 168.36247604, 0.06837797, 117.85373323, -2442.41367766, 0.05, 2, 0, 72011, 23011, 1, 3)
    ops.uniaxialMaterial('LimitState', 32011, 42.09061901, 7.641e-05, 126.27185703, 0.00022923, 420.90619011, 0.00076408, -42.09061901, -7.641e-05, -126.27185703, -0.00022923, -420.90619011, -0.00076408, 0.4, 0.3, 0.003, 0.0, 0.0, 12011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2011, 99999, 'P', 42011, 'Vy', 32011, 'Vz', 22011, 'My', 12011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172011, 72011, 172011, 2011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123011, 123011, 23011, 2011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172012, 10.3, 11.4, 5.65)
    ops.node(123012, 10.3, 11.4, 7.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2012, 172012, 123012, 0.1, 31174754.26200213, 12989480.94250089, 0.00127345, 0.00057292, 0.00146667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22012, 81.27757575, 0.00077059, 97.98029471, 0.01738535, 9.79802947, 0.07318944, -81.27757575, -0.00077059, -97.98029471, -0.01738535, -9.79802947, -0.07318944, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12012, 44.95008313, 0.00111521, 54.18742319, 0.01542156, 5.41874232, 0.0545563, -44.95008313, -0.00111521, -54.18742319, -0.01542156, -5.41874232, -0.0545563, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22012, 2012, 0.0, 141.733838, 0.01541179, 141.733838, 0.04623536, 99.2136866, -2814.19555336, 0.05, 2, 0, 72012, 23012, 2, 3)
    ops.uniaxialMaterial('LimitState', 42012, 35.4334595, 8.838e-05, 106.3003785, 0.00026515, 354.334595, 0.00088383, -35.4334595, -8.838e-05, -106.3003785, -0.00026515, -354.334595, -0.00088383, 0.4, 0.3, 0.003, 0.0, 0.0, 22012, 2)
    ops.limitCurve('ThreePoint', 12012, 2012, 0.0, 115.3360017, 0.02230413, 115.3360017, 0.06691239, 80.73520119, -1553.97191064, 0.05, 2, 0, 72012, 23012, 1, 3)
    ops.uniaxialMaterial('LimitState', 32012, 28.83400042, 7.192e-05, 86.50200127, 0.00021576, 288.34000425, 0.00071921, -28.83400042, -7.192e-05, -86.50200127, -0.00021576, -288.34000425, -0.00071921, 0.4, 0.3, 0.003, 0.0, 0.0, 12012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2012, 99999, 'P', 42012, 'Vy', 32012, 'Vz', 22012, 'My', 12012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172012, 72012, 172012, 2012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123012, 123012, 23012, 2012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172013, 0.0, 17.1, 5.65)
    ops.node(123013, 0.0, 17.1, 7.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2013, 172013, 123013, 0.0875, 32047012.6643503, 13352921.94347929, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22013, 65.10389137, 0.00082238, 78.3278234, 0.01726485, 7.83278234, 0.07463143, -65.10389137, -0.00082238, -78.3278234, -0.01726485, -7.83278234, -0.07463143, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12013, 41.31615012, 0.00107958, 49.70830533, 0.01582446, 4.97083053, 0.06012389, -41.31615012, -0.00107958, -49.70830533, -0.01582446, -4.97083053, -0.06012389, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22013, 2013, 0.0, 124.66600792, 0.01644768, 124.66600792, 0.04934304, 87.26620554, -2479.84153165, 0.05, 2, 0, 72013, 23013, 2, 3)
    ops.uniaxialMaterial('LimitState', 42013, 31.16650198, 8.643e-05, 93.49950594, 0.00025928, 311.6650198, 0.00086427, -31.16650198, -8.643e-05, -93.49950594, -0.00025928, -311.6650198, -0.00086427, 0.4, 0.3, 0.003, 0.0, 0.0, 22013, 2)
    ops.limitCurve('ThreePoint', 12013, 2013, 0.0, 107.32902188, 0.02159153, 107.32902188, 0.06477459, 75.13031531, -1590.08366557, 0.05, 2, 0, 72013, 23013, 1, 3)
    ops.uniaxialMaterial('LimitState', 32013, 26.83225547, 7.441e-05, 80.49676641, 0.00022322, 268.3225547, 0.00074408, -26.83225547, -7.441e-05, -80.49676641, -0.00022322, -268.3225547, -0.00074408, 0.4, 0.3, 0.003, 0.0, 0.0, 12013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2013, 99999, 'P', 42013, 'Vy', 32013, 'Vz', 22013, 'My', 12013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172013, 72013, 172013, 2013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123013, 123013, 23013, 2013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172014, 2.9, 17.1, 5.675)
    ops.node(123014, 2.9, 17.1, 7.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2014, 172014, 123014, 0.125, 31408112.04309945, 13086713.35129144, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22014, 119.06640316, 0.00066869, 143.38654388, 0.02918944, 14.33865439, 0.11416025, -119.06640316, -0.00066869, -143.38654388, -0.02918944, -14.33865439, -0.11416025, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12014, 64.30339785, 0.0010828, 77.43781396, 0.02349832, 7.7437814, 0.07148492, -64.30339785, -0.0010828, -77.43781396, -0.02349832, -7.7437814, -0.07148492, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22014, 2014, 0.0, 246.12431646, 0.01337386, 246.12431646, 0.04012157, 172.28702152, -6542.15423029, 0.05, 2, 0, 72014, 23014, 2, 3)
    ops.uniaxialMaterial('LimitState', 42014, 61.53107911, 0.00012187, 184.59323734, 0.00036561, 615.31079114, 0.00121871, -61.53107911, -0.00012187, -184.59323734, -0.00036561, -615.31079114, -0.00121871, 0.4, 0.3, 0.003, 0.0, 0.0, 22014, 2)
    ops.limitCurve('ThreePoint', 12014, 2014, 0.0, 160.24217115, 0.02165609, 160.24217115, 0.06496826, 112.1695198, -2510.8225002, 0.05, 2, 0, 72014, 23014, 1, 3)
    ops.uniaxialMaterial('LimitState', 32014, 40.06054279, 7.935e-05, 120.18162836, 0.00023804, 400.60542787, 0.00079345, -40.06054279, -7.935e-05, -120.18162836, -0.00023804, -400.60542787, -0.00079345, 0.4, 0.3, 0.003, 0.0, 0.0, 12014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2014, 99999, 'P', 42014, 'Vy', 32014, 'Vz', 22014, 'My', 12014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172014, 72014, 172014, 2014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123014, 123014, 23014, 2014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172015, 6.6, 17.1, 5.675)
    ops.node(123015, 6.6, 17.1, 7.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2015, 172015, 123015, 0.1375, 32945460.92006255, 13727275.3833594, 0.00204719, 0.00078776, 0.00381276, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22015, 173.68187049, 0.0006643, 208.21867813, 0.03337084, 20.82186781, 0.12048735, -173.68187049, -0.0006643, -208.21867813, -0.03337084, -20.82186781, -0.12048735, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12015, 79.84598457, 0.00115995, 95.7234357, 0.02609538, 9.57234357, 0.07187009, -79.84598457, -0.00115995, -95.7234357, -0.02609538, -9.57234357, -0.07187009, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22015, 2015, 0.0, 293.51221574, 0.01328606, 293.51221574, 0.03985817, 205.45855102, -7244.6530437, 0.05, 2, 0, 72015, 23015, 2, 3)
    ops.uniaxialMaterial('LimitState', 42015, 73.37805394, 0.00012596, 220.13416181, 0.00037787, 733.78053935, 0.00125958, -73.37805394, -0.00012596, -220.13416181, -0.00037787, -733.78053935, -0.00125958, 0.4, 0.3, 0.003, 0.0, 0.0, 22015, 2)
    ops.limitCurve('ThreePoint', 12015, 2015, 0.0, 177.19624035, 0.02319897, 177.19624035, 0.0695969, 124.03736824, -2485.30267459, 0.05, 2, 0, 72015, 23015, 1, 3)
    ops.uniaxialMaterial('LimitState', 32015, 44.29906009, 7.604e-05, 132.89718026, 0.00022813, 442.99060087, 0.00076042, -44.29906009, -7.604e-05, -132.89718026, -0.00022813, -442.99060087, -0.00076042, 0.4, 0.3, 0.003, 0.0, 0.0, 12015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2015, 99999, 'P', 42015, 'Vy', 32015, 'Vz', 22015, 'My', 12015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172015, 72015, 172015, 2015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123015, 123015, 23015, 2015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172016, 10.3, 17.1, 5.65)
    ops.node(123016, 10.3, 17.1, 7.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2016, 172016, 123016, 0.1, 31428542.7167109, 13095226.13196287, 0.00127345, 0.00057292, 0.00146667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22016, 82.61910164, 0.00076257, 99.53150565, 0.01670763, 9.95315056, 0.07278322, -82.61910164, -0.00076257, -99.53150565, -0.01670763, -9.95315056, -0.07278322, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12016, 45.62960218, 0.00108937, 54.97013302, 0.01481907, 5.4970133, 0.05414421, -45.62960218, -0.00108937, -54.97013302, -0.01481907, -5.4970133, -0.05414421, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22016, 2016, 0.0, 138.85524144, 0.01525133, 138.85524144, 0.045754, 97.19866901, -2616.84335679, 0.05, 2, 0, 72016, 23016, 2, 3)
    ops.uniaxialMaterial('LimitState', 42016, 34.71381036, 8.589e-05, 104.14143108, 0.00025767, 347.13810359, 0.00085888, -34.71381036, -8.589e-05, -104.14143108, -0.00025767, -347.13810359, -0.00085888, 0.4, 0.3, 0.003, 0.0, 0.0, 22016, 2)
    ops.limitCurve('ThreePoint', 12016, 2016, 0.0, 113.83305352, 0.02178742, 113.83305352, 0.06536226, 79.68313746, -1462.04999972, 0.05, 2, 0, 72016, 23016, 1, 3)
    ops.uniaxialMaterial('LimitState', 32016, 28.45826338, 7.041e-05, 85.37479014, 0.00021123, 284.5826338, 0.00070411, -28.45826338, -7.041e-05, -85.37479014, -0.00021123, -284.5826338, -0.00070411, 0.4, 0.3, 0.003, 0.0, 0.0, 12016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2016, 99999, 'P', 42016, 'Vy', 32016, 'Vz', 22016, 'My', 12016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172016, 72016, 172016, 2016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123016, 123016, 23016, 2016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172017, 0.0, 22.8, 5.65)
    ops.node(123017, 0.0, 22.8, 7.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2017, 172017, 123017, 0.0625, 30043662.11403469, 12518192.54751446, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22017, 29.17734514, 0.00109385, 35.33876716, 0.01793979, 3.53387672, 0.07577325, -29.17734514, -0.00109385, -35.33876716, -0.01793979, -3.53387672, -0.07577325, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12017, 29.17734514, 0.00109385, 35.33876716, 0.01793979, 3.53387672, 0.07577325, -29.17734514, -0.00109385, -35.33876716, -0.01793979, -3.53387672, -0.07577325, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22017, 2017, 0.0, 81.63348566, 0.02187709, 81.63348566, 0.06563126, 57.14343996, -1884.1798405, 0.05, 2, 0, 72017, 23017, 2, 3)
    ops.uniaxialMaterial('LimitState', 42017, 20.40837141, 8.451e-05, 61.22511424, 0.00025354, 204.08371414, 0.00084515, -20.40837141, -8.451e-05, -61.22511424, -0.00025354, -204.08371414, -0.00084515, 0.4, 0.3, 0.003, 0.0, 0.0, 22017, 2)
    ops.limitCurve('ThreePoint', 12017, 2017, 0.0, 81.63348566, 0.02187709, 81.63348566, 0.06563126, 57.14343996, -1884.1798405, 0.05, 2, 0, 72017, 23017, 1, 3)
    ops.uniaxialMaterial('LimitState', 32017, 20.40837141, 8.451e-05, 61.22511424, 0.00025354, 204.08371414, 0.00084515, -20.40837141, -8.451e-05, -61.22511424, -0.00025354, -204.08371414, -0.00084515, 0.4, 0.3, 0.003, 0.0, 0.0, 12017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2017, 99999, 'P', 42017, 'Vy', 32017, 'Vz', 22017, 'My', 12017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172017, 72017, 172017, 2017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123017, 123017, 23017, 2017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172018, 2.9, 22.8, 5.675)
    ops.node(123018, 2.9, 22.8, 7.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2018, 172018, 123018, 0.0875, 31004692.3099101, 12918621.79579588, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22018, 51.68824984, 0.0011346, 62.34787147, 0.02510207, 6.23478715, 0.07622064, -51.68824984, -0.0011346, -62.34787147, -0.02510207, -6.23478715, -0.07622064, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12018, 75.50694631, 0.00086321, 91.07867645, 0.0277415, 9.10786765, 0.09483185, -75.50694631, -0.00086321, -91.07867645, -0.0277415, -9.10786765, -0.09483185, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22018, 2018, 0.0, 115.22555431, 0.02269201, 115.22555431, 0.06807602, 80.65788801, -2061.10450058, 0.05, 2, 0, 72018, 23018, 2, 3)
    ops.uniaxialMaterial('LimitState', 42018, 28.80638858, 8.257e-05, 86.41916573, 0.0002477, 288.06388576, 0.00082568, -28.80638858, -8.257e-05, -86.41916573, -0.0002477, -288.06388576, -0.00082568, 0.4, 0.3, 0.003, 0.0, 0.0, 22018, 2)
    ops.limitCurve('ThreePoint', 12018, 2018, 0.0, 136.65891842, 0.01726423, 136.65891842, 0.0517927, 95.6612429, -3294.13822972, 0.05, 2, 0, 72018, 23018, 1, 3)
    ops.uniaxialMaterial('LimitState', 32018, 34.16472961, 9.793e-05, 102.49418882, 0.00029378, 341.64729606, 0.00097926, -34.16472961, -9.793e-05, -102.49418882, -0.00029378, -341.64729606, -0.00097926, 0.4, 0.3, 0.003, 0.0, 0.0, 12018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2018, 99999, 'P', 42018, 'Vy', 32018, 'Vz', 22018, 'My', 12018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172018, 72018, 172018, 2018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123018, 123018, 23018, 2018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172019, 6.6, 22.8, 5.675)
    ops.node(123019, 6.6, 22.8, 7.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2019, 172019, 123019, 0.0875, 32316821.6758344, 13465342.364931, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22019, 52.56066403, 0.0011445, 63.13269468, 0.0201418, 6.31326947, 0.06351186, -52.56066403, -0.0011445, -63.13269468, -0.0201418, -6.31326947, -0.06351186, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12019, 76.87867878, 0.00086546, 92.34202506, 0.02204993, 9.23420251, 0.07821301, -76.87867878, -0.00086546, -92.34202506, -0.02204993, -9.23420251, -0.07821301, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22019, 2019, 0.0, 110.01925307, 0.02288996, 110.01925307, 0.06866987, 77.01347715, -1543.41618108, 0.05, 2, 0, 72019, 23019, 2, 3)
    ops.uniaxialMaterial('LimitState', 42019, 27.50481327, 7.564e-05, 82.5144398, 0.00022691, 275.04813267, 0.00075636, -27.50481327, -7.564e-05, -82.5144398, -0.00022691, -275.04813267, -0.00075636, 0.4, 0.3, 0.003, 0.0, 0.0, 22019, 2)
    ops.limitCurve('ThreePoint', 12019, 2019, 0.0, 127.39499664, 0.01730921, 127.39499664, 0.05192764, 89.17649765, -2350.46901158, 0.05, 2, 0, 72019, 23019, 1, 3)
    ops.uniaxialMaterial('LimitState', 32019, 31.84874916, 8.758e-05, 95.54624748, 0.00026274, 318.48749161, 0.00087581, -31.84874916, -8.758e-05, -95.54624748, -0.00026274, -318.48749161, -0.00087581, 0.4, 0.3, 0.003, 0.0, 0.0, 12019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2019, 99999, 'P', 42019, 'Vy', 32019, 'Vz', 22019, 'My', 12019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172019, 72019, 172019, 2019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123019, 123019, 23019, 2019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172020, 10.3, 22.8, 5.65)
    ops.node(123020, 10.3, 22.8, 7.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2020, 172020, 123020, 0.0625, 31101968.76518072, 12959153.65215863, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22020, 29.78015267, 0.00108141, 35.93506687, 0.01812635, 3.59350669, 0.07517729, -29.78015267, -0.00108141, -35.93506687, -0.01812635, -3.59350669, -0.07517729, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12020, 29.78015267, 0.00108141, 35.93506687, 0.01812635, 3.59350669, 0.07517729, -29.78015267, -0.00108141, -35.93506687, -0.01812635, -3.59350669, -0.07517729, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22020, 2020, 0.0, 86.53203906, 0.02162815, 86.53203906, 0.06488444, 60.57242734, -1807.9300562, 0.05, 2, 0, 72020, 23020, 2, 3)
    ops.uniaxialMaterial('LimitState', 42020, 21.63300977, 8.654e-05, 64.8990293, 0.00025961, 216.33009766, 0.00086538, -21.63300977, -8.654e-05, -64.8990293, -0.00025961, -216.33009766, -0.00086538, 0.4, 0.3, 0.003, 0.0, 0.0, 22020, 2)
    ops.limitCurve('ThreePoint', 12020, 2020, 0.0, 86.53203906, 0.02162815, 86.53203906, 0.06488444, 60.57242734, -1807.9300562, 0.05, 2, 0, 72020, 23020, 1, 3)
    ops.uniaxialMaterial('LimitState', 32020, 21.63300977, 8.654e-05, 64.8990293, 0.00025961, 216.33009766, 0.00086538, -21.63300977, -8.654e-05, -64.8990293, -0.00025961, -216.33009766, -0.00086538, 0.4, 0.3, 0.003, 0.0, 0.0, 12020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2020, 99999, 'P', 42020, 'Vy', 32020, 'Vz', 22020, 'My', 12020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172020, 72020, 172020, 2020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123020, 123020, 23020, 2020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173003, 6.6, 0.0, 8.375)
    ops.node(124003, 6.6, 0.0, 10.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3003, 173003, 124003, 0.0875, 29567543.18400541, 12319809.66000226, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23003, 41.61120228, 0.00112108, 50.5985651, 0.02109665, 5.05985651, 0.06933249, -41.61120228, -0.00112108, -50.5985651, -0.02109665, -5.05985651, -0.06933249, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13003, 61.44053808, 0.00084905, 74.71072441, 0.02312441, 7.47107244, 0.08558855, -61.44053808, -0.00084905, -74.71072441, -0.02312441, -7.47107244, -0.08558855, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23003, 3003, 0.0, 91.3598357, 0.02242157, 91.3598357, 0.06726472, 63.95188499, -2449.44376203, 0.05, 2, 0, 73003, 24003, 2, 3)
    ops.uniaxialMaterial('LimitState', 43003, 22.83995893, 6.865e-05, 68.51987678, 0.00020594, 228.39958925, 0.00068648, -22.83995893, -6.865e-05, -68.51987678, -0.00020594, -228.39958925, -0.00068648, 0.4, 0.3, 0.003, 0.0, 0.0, 23003, 2)
    ops.limitCurve('ThreePoint', 13003, 3003, 0.0, 108.00594651, 0.01698103, 108.00594651, 0.0509431, 75.60416256, -4324.11590946, 0.05, 2, 0, 73003, 24003, 1, 3)
    ops.uniaxialMaterial('LimitState', 33003, 27.00148663, 8.116e-05, 81.00445988, 0.00024347, 270.01486628, 0.00081156, -27.00148663, -8.116e-05, -81.00445988, -0.00024347, -270.01486628, -0.00081156, 0.4, 0.3, 0.003, 0.0, 0.0, 13003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3003, 99999, 'P', 43003, 'Vy', 33003, 'Vz', 23003, 'My', 13003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173003, 73003, 173003, 3003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124003, 124003, 24003, 3003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173004, 10.3, 0.0, 8.35)
    ops.node(124004, 10.3, 0.0, 10.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3004, 173004, 124004, 0.0625, 30688354.94502965, 12786814.56042902, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23004, 23.62724971, 0.0010204, 28.65849037, 0.01879671, 2.86584904, 0.08282812, -23.62724971, -0.0010204, -28.65849037, -0.01879671, -2.86584904, -0.08282812, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13004, 23.62724971, 0.0010204, 28.65849037, 0.01879671, 2.86584904, 0.08282812, -23.62724971, -0.0010204, -28.65849037, -0.01879671, -2.86584904, -0.08282812, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23004, 3004, 0.0, 78.8087675, 0.02040793, 78.8087675, 0.0612238, 55.16613725, -4015.67274287, 0.05, 2, 0, 73004, 24004, 2, 3)
    ops.uniaxialMaterial('LimitState', 43004, 19.70219188, 7.988e-05, 59.10657563, 0.00023963, 197.02191875, 0.00079876, -19.70219188, -7.988e-05, -59.10657563, -0.00023963, -197.02191875, -0.00079876, 0.4, 0.3, 0.003, 0.0, 0.0, 23004, 2)
    ops.limitCurve('ThreePoint', 13004, 3004, 0.0, 78.8087675, 0.02040793, 78.8087675, 0.0612238, 55.16613725, -4015.67274287, 0.05, 2, 0, 73004, 24004, 1, 3)
    ops.uniaxialMaterial('LimitState', 33004, 19.70219188, 7.988e-05, 59.10657563, 0.00023963, 197.02191875, 0.00079876, -19.70219188, -7.988e-05, -59.10657563, -0.00023963, -197.02191875, -0.00079876, 0.4, 0.3, 0.003, 0.0, 0.0, 13004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3004, 99999, 'P', 43004, 'Vy', 33004, 'Vz', 23004, 'My', 13004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173004, 73004, 173004, 3004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124004, 124004, 24004, 3004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173005, 0.0, 5.7, 8.35)
    ops.node(124005, 0.0, 5.7, 10.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3005, 173005, 124005, 0.0875, 29948019.45604256, 12478341.44001773, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23005, 53.65580927, 0.00081595, 65.16593805, 0.01909852, 6.5165938, 0.08136461, -53.65580927, -0.00081595, -65.16593805, -0.01909852, -6.5165938, -0.08136461, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13005, 33.26384953, 0.00107202, 40.39953897, 0.01746702, 4.0399539, 0.06554993, -33.26384953, -0.00107202, -40.39953897, -0.01746702, -4.0399539, -0.06554993, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23005, 3005, 0.0, 111.93171977, 0.01631906, 111.93171977, 0.04895719, 78.35220384, -4370.48559987, 0.05, 2, 0, 73005, 24005, 2, 3)
    ops.uniaxialMaterial('LimitState', 43005, 27.98292994, 8.304e-05, 83.94878983, 0.00024911, 279.82929943, 0.00083037, -27.98292994, -8.304e-05, -83.94878983, -0.00024911, -279.82929943, -0.00083037, 0.4, 0.3, 0.003, 0.0, 0.0, 23005, 2)
    ops.limitCurve('ThreePoint', 13005, 3005, 0.0, 94.55475636, 0.02144041, 94.55475636, 0.06432124, 66.18832945, -2485.59380934, 0.05, 2, 0, 73005, 24005, 1, 3)
    ops.uniaxialMaterial('LimitState', 33005, 23.63868909, 7.015e-05, 70.91606727, 0.00021044, 236.3868909, 0.00070146, -23.63868909, -7.015e-05, -70.91606727, -0.00021044, -236.3868909, -0.00070146, 0.4, 0.3, 0.003, 0.0, 0.0, 13005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3005, 99999, 'P', 43005, 'Vy', 33005, 'Vz', 23005, 'My', 13005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173005, 73005, 173005, 3005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124005, 124005, 24005, 3005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173006, 2.9, 5.7, 8.375)
    ops.node(124006, 2.9, 5.7, 10.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3006, 173006, 124006, 0.125, 33767245.88513639, 14069685.7854735, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23006, 121.02204167, 0.0006698, 145.17459222, 0.01725382, 14.51745922, 0.07219285, -121.02204167, -0.0006698, -145.17459222, -0.01725382, -14.51745922, -0.07219285, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13006, 52.0057772, 0.00111471, 62.38464824, 0.01465943, 6.23846482, 0.04864754, -52.0057772, -0.00111471, -62.38464824, -0.01465943, -6.23846482, -0.04864754, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23006, 3006, 0.0, 174.53430055, 0.01339598, 174.53430055, 0.04018795, 122.17401039, -3956.29706998, 0.05, 2, 0, 73006, 24006, 2, 3)
    ops.uniaxialMaterial('LimitState', 43006, 43.63357514, 8.038e-05, 130.90072542, 0.00024115, 436.33575139, 0.00080384, -43.63357514, -8.038e-05, -130.90072542, -0.00024115, -436.33575139, -0.00080384, 0.4, 0.3, 0.003, 0.0, 0.0, 23006, 2)
    ops.limitCurve('ThreePoint', 13006, 3006, 0.0, 118.28864068, 0.02229422, 118.28864068, 0.06688266, 82.80204848, -1391.98093546, 0.05, 2, 0, 73006, 24006, 1, 3)
    ops.uniaxialMaterial('LimitState', 33006, 29.57216017, 5.448e-05, 88.71648051, 0.00016344, 295.72160171, 0.0005448, -29.57216017, -5.448e-05, -88.71648051, -0.00016344, -295.72160171, -0.0005448, 0.4, 0.3, 0.003, 0.0, 0.0, 13006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3006, 99999, 'P', 43006, 'Vy', 33006, 'Vz', 23006, 'My', 13006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173006, 73006, 173006, 3006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124006, 124006, 24006, 3006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173007, 6.6, 5.7, 8.375)
    ops.node(124007, 6.6, 5.7, 10.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3007, 173007, 124007, 0.1375, 33150804.88457468, 13812835.36857278, 0.00204719, 0.00078776, 0.00381276, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23007, 157.50864495, 0.00063526, 189.41163127, 0.01827236, 18.94116313, 0.07343236, -157.50864495, -0.00063526, -189.41163127, -0.01827236, -18.94116313, -0.07343236, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13007, 59.05268395, 0.00107094, 71.01365897, 0.01513174, 7.1013659, 0.04735502, -59.05268395, -0.00107094, -71.01365897, -0.01513174, -7.1013659, -0.04735502, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23007, 3007, 0.0, 198.74115748, 0.01270516, 198.74115748, 0.03811549, 139.11881023, -4767.77093918, 0.05, 2, 0, 73007, 24007, 2, 3)
    ops.uniaxialMaterial('LimitState', 43007, 49.68528937, 8.476e-05, 149.05586811, 0.00025428, 496.85289369, 0.00084759, -49.68528937, -8.476e-05, -149.05586811, -0.00025428, -496.85289369, -0.00084759, 0.4, 0.3, 0.003, 0.0, 0.0, 23007, 2)
    ops.limitCurve('ThreePoint', 13007, 3007, 0.0, 125.84208107, 0.02141877, 125.84208107, 0.06425632, 88.08945675, -1417.17877144, 0.05, 2, 0, 73007, 24007, 1, 3)
    ops.uniaxialMaterial('LimitState', 33007, 31.46052027, 5.367e-05, 94.3815608, 0.00016101, 314.60520268, 0.00053669, -31.46052027, -5.367e-05, -94.3815608, -0.00016101, -314.60520268, -0.00053669, 0.4, 0.3, 0.003, 0.0, 0.0, 13007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3007, 99999, 'P', 43007, 'Vy', 33007, 'Vz', 23007, 'My', 13007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173007, 73007, 173007, 3007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124007, 124007, 24007, 3007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173008, 10.3, 5.7, 8.35)
    ops.node(124008, 10.3, 5.7, 10.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3008, 173008, 124008, 0.1, 32125868.56503624, 13385778.5687651, 0.00127345, 0.00057292, 0.00146667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23008, 62.27458672, 0.00072022, 75.17564071, 0.01827888, 7.51756407, 0.08219567, -62.27458672, -0.00072022, -75.17564071, -0.01827888, -7.51756407, -0.08219567, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13008, 33.35969805, 0.00102226, 40.27062734, 0.01614136, 4.02706273, 0.06096545, -33.35969805, -0.00102226, -40.27062734, -0.01614136, -4.02706273, -0.06096545, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23008, 3008, 0.0, 133.81054392, 0.01440438, 133.81054392, 0.04321313, 93.66738074, -5908.93971503, 0.05, 2, 0, 73008, 24008, 2, 3)
    ops.uniaxialMaterial('LimitState', 43008, 33.45263598, 8.097e-05, 100.35790794, 0.00024291, 334.52635979, 0.00080971, -33.45263598, -8.097e-05, -100.35790794, -0.00024291, -334.52635979, -0.00080971, 0.4, 0.3, 0.003, 0.0, 0.0, 23008, 2)
    ops.limitCurve('ThreePoint', 13008, 3008, 0.0, 107.6204067, 0.02044513, 107.6204067, 0.0613354, 75.33428469, -2638.34261722, 0.05, 2, 0, 73008, 24008, 1, 3)
    ops.uniaxialMaterial('LimitState', 33008, 26.90510168, 6.512e-05, 80.71530503, 0.00019537, 269.05101676, 0.00065123, -26.90510168, -6.512e-05, -80.71530503, -0.00019537, -269.05101676, -0.00065123, 0.4, 0.3, 0.003, 0.0, 0.0, 13008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3008, 99999, 'P', 43008, 'Vy', 33008, 'Vz', 23008, 'My', 13008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173008, 73008, 173008, 3008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124008, 124008, 24008, 3008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173009, 0.0, 11.4, 8.35)
    ops.node(124009, 0.0, 11.4, 10.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3009, 173009, 124009, 0.0875, 31567460.13475573, 13153108.38948155, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23009, 52.0274019, 0.00082672, 62.93134118, 0.01828159, 6.29313412, 0.08240525, -52.0274019, -0.00082672, -62.93134118, -0.01828159, -6.29313412, -0.08240525, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13009, 32.22406941, 0.00109477, 38.97761242, 0.01674753, 3.89776124, 0.06626489, -32.22406941, -0.00109477, -38.97761242, -0.01674753, -3.89776124, -0.06626489, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23009, 3009, 0.0, 113.3036648, 0.0165343, 113.3036648, 0.04960291, 79.31256536, -5427.48010445, 0.05, 2, 0, 73009, 24009, 2, 3)
    ops.uniaxialMaterial('LimitState', 43009, 28.3259162, 7.974e-05, 84.9777486, 0.00023923, 283.25916199, 0.00079743, -28.3259162, -7.974e-05, -84.9777486, -0.00023923, -283.25916199, -0.00079743, 0.4, 0.3, 0.003, 0.0, 0.0, 23009, 2)
    ops.limitCurve('ThreePoint', 13009, 3009, 0.0, 96.36020213, 0.02189538, 96.36020213, 0.06568615, 67.45214149, -3007.38555498, 0.05, 2, 0, 73009, 24009, 1, 3)
    ops.uniaxialMaterial('LimitState', 33009, 24.09005053, 6.782e-05, 72.2701516, 0.00020345, 240.90050534, 0.00067818, -24.09005053, -6.782e-05, -72.2701516, -0.00020345, -240.90050534, -0.00067818, 0.4, 0.3, 0.003, 0.0, 0.0, 13009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3009, 99999, 'P', 43009, 'Vy', 33009, 'Vz', 23009, 'My', 13009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173009, 73009, 173009, 3009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124009, 124009, 24009, 3009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173010, 2.9, 11.4, 8.375)
    ops.node(124010, 2.9, 11.4, 10.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3010, 173010, 124010, 0.125, 32010235.18021073, 13337597.99175447, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23010, 109.32504043, 0.00066098, 131.98629039, 0.01780526, 13.19862904, 0.08115433, -109.32504043, -0.00066098, -131.98629039, -0.01780526, -13.19862904, -0.08115433, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13010, 43.64397022, 0.00107731, 52.69063432, 0.01492168, 5.26906343, 0.05307224, -43.64397022, -0.00107731, -52.69063432, -0.01492168, -5.26906343, -0.05307224, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23010, 3010, 0.0, 180.98921464, 0.01321963, 180.98921464, 0.03965889, 126.69245025, -6308.97521591, 0.05, 2, 0, 73010, 24010, 2, 3)
    ops.uniaxialMaterial('LimitState', 43010, 45.24730366, 8.793e-05, 135.74191098, 0.0002638, 452.47303659, 0.00087933, -45.24730366, -8.793e-05, -135.74191098, -0.0002638, -452.47303659, -0.00087933, 0.4, 0.3, 0.003, 0.0, 0.0, 23010, 2)
    ops.limitCurve('ThreePoint', 13010, 3010, 0.0, 123.28516401, 0.02154613, 123.28516401, 0.0646384, 86.2996148, -2033.05567365, 0.05, 2, 0, 73010, 24010, 1, 3)
    ops.uniaxialMaterial('LimitState', 33010, 30.821291, 5.99e-05, 92.463873, 0.00017969, 308.21291002, 0.00059897, -30.821291, -5.99e-05, -92.463873, -0.00017969, -308.21291002, -0.00059897, 0.4, 0.3, 0.003, 0.0, 0.0, 13010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3010, 99999, 'P', 43010, 'Vy', 33010, 'Vz', 23010, 'My', 13010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173010, 73010, 173010, 3010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124010, 124010, 24010, 3010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173011, 6.6, 11.4, 8.375)
    ops.node(124011, 6.6, 11.4, 10.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3011, 173011, 124011, 0.1375, 30437284.81080484, 12682202.00450202, 0.00204719, 0.00078776, 0.00381276, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23011, 153.88737292, 0.00065581, 186.65753494, 0.01945871, 18.66575349, 0.07371807, -153.88737292, -0.00065581, -186.65753494, -0.01945871, -18.66575349, -0.07371807, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13011, 57.23301813, 0.00115168, 69.42073205, 0.01614189, 6.9420732, 0.04783903, -57.23301813, -0.00115168, -69.42073205, -0.01614189, -6.9420732, -0.04783903, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23011, 3011, 0.0, 185.69629011, 0.01311625, 185.69629011, 0.03934874, 129.98740307, -4987.1803109, 0.05, 2, 0, 73011, 24011, 2, 3)
    ops.uniaxialMaterial('LimitState', 43011, 46.42407253, 8.626e-05, 139.27221758, 0.00025877, 464.24072526, 0.00086256, -46.42407253, -8.626e-05, -139.27221758, -0.00025877, -464.24072526, -0.00086256, 0.4, 0.3, 0.003, 0.0, 0.0, 23011, 2)
    ops.limitCurve('ThreePoint', 13011, 3011, 0.0, 116.74400295, 0.0230335, 116.74400295, 0.06910051, 81.72080207, -1470.39720617, 0.05, 2, 0, 73011, 24011, 1, 3)
    ops.uniaxialMaterial('LimitState', 33011, 29.18600074, 5.423e-05, 87.55800222, 0.00016268, 291.86000739, 0.00054228, -29.18600074, -5.423e-05, -87.55800222, -0.00016268, -291.86000739, -0.00054228, 0.4, 0.3, 0.003, 0.0, 0.0, 13011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3011, 99999, 'P', 43011, 'Vy', 33011, 'Vz', 23011, 'My', 13011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173011, 73011, 173011, 3011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124011, 124011, 24011, 3011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173012, 10.3, 11.4, 8.35)
    ops.node(124012, 10.3, 11.4, 10.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3012, 173012, 124012, 0.1, 30816431.0851094, 12840179.61879558, 0.00127345, 0.00057292, 0.00146667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23012, 61.57317436, 0.00074352, 74.63368634, 0.01826965, 7.46336863, 0.08176214, -61.57317436, -0.00074352, -74.63368634, -0.01826965, -7.46336863, -0.08176214, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13012, 33.00321671, 0.00107603, 40.00365012, 0.01616713, 4.00036501, 0.06069366, -33.00321671, -0.00107603, -40.00365012, -0.01616713, -4.00036501, -0.06069366, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23012, 3012, 0.0, 126.22096301, 0.01487031, 126.22096301, 0.04461094, 88.35467411, -5402.95042733, 0.05, 2, 0, 73012, 24012, 2, 3)
    ops.uniaxialMaterial('LimitState', 43012, 31.55524075, 7.962e-05, 94.66572226, 0.00023887, 315.55240753, 0.00079624, -31.55524075, -7.962e-05, -94.66572226, -0.00023887, -315.55240753, -0.00079624, 0.4, 0.3, 0.003, 0.0, 0.0, 23012, 2)
    ops.limitCurve('ThreePoint', 13012, 3012, 0.0, 101.37221976, 0.02152057, 101.37221976, 0.06456172, 70.96055383, -2426.02572622, 0.05, 2, 0, 73012, 24012, 1, 3)
    ops.uniaxialMaterial('LimitState', 33012, 25.34305494, 6.395e-05, 76.02916482, 0.00019185, 253.4305494, 0.00063949, -25.34305494, -6.395e-05, -76.02916482, -0.00019185, -253.4305494, -0.00063949, 0.4, 0.3, 0.003, 0.0, 0.0, 13012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3012, 99999, 'P', 43012, 'Vy', 33012, 'Vz', 23012, 'My', 13012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173012, 73012, 173012, 3012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124012, 124012, 24012, 3012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173013, 0.0, 17.1, 8.35)
    ops.node(124013, 0.0, 17.1, 10.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3013, 173013, 124013, 0.0875, 31380797.09414742, 13075332.12256142, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23013, 52.30425823, 0.0008005, 63.30332635, 0.01842165, 6.33033263, 0.08249022, -52.30425823, -0.0008005, -63.30332635, -0.01842165, -6.33033263, -0.08249022, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13013, 32.27465739, 0.00104532, 39.06169858, 0.01684719, 3.90616986, 0.066322, -32.27465739, -0.00104532, -39.06169858, -0.01684719, -3.90616986, -0.066322, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23013, 3013, 0.0, 112.99717477, 0.01600995, 112.99717477, 0.04802984, 79.09802234, -5458.87455783, 0.05, 2, 0, 73013, 24013, 2, 3)
    ops.uniaxialMaterial('LimitState', 43013, 28.24929369, 8e-05, 84.74788108, 0.00024, 282.49293693, 0.0008, -28.24929369, -8e-05, -84.74788108, -0.00024, -282.49293693, -0.0008, 0.4, 0.3, 0.003, 0.0, 0.0, 23013, 2)
    ops.limitCurve('ThreePoint', 13013, 3013, 0.0, 95.99901814, 0.0209063, 95.99901814, 0.06271891, 67.1993127, -3024.07704111, 0.05, 2, 0, 73013, 24013, 1, 3)
    ops.uniaxialMaterial('LimitState', 33013, 23.99975453, 6.797e-05, 71.9992636, 0.0002039, 239.99754535, 0.00067966, -23.99975453, -6.797e-05, -71.9992636, -0.0002039, -239.99754535, -0.00067966, 0.4, 0.3, 0.003, 0.0, 0.0, 13013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3013, 99999, 'P', 43013, 'Vy', 33013, 'Vz', 23013, 'My', 13013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173013, 73013, 173013, 3013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124013, 124013, 24013, 3013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173014, 2.9, 17.1, 8.375)
    ops.node(124014, 2.9, 17.1, 10.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3014, 173014, 124014, 0.125, 30980573.51540961, 12908572.29808734, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23014, 107.63468581, 0.00065931, 130.36020141, 0.01835672, 13.03602014, 0.08130441, -107.63468581, -0.00065931, -130.36020141, -0.01835672, -13.03602014, -0.08130441, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13014, 42.9488563, 0.0010776, 52.0168895, 0.01536864, 5.20168895, 0.05327748, -42.9488563, -0.0010776, -52.0168895, -0.01536864, -5.20168895, -0.05327748, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23014, 3014, 0.0, 176.12140547, 0.01318621, 176.12140547, 0.03955864, 123.28498383, -6282.5122168, 0.05, 2, 0, 73014, 24014, 2, 3)
    ops.uniaxialMaterial('LimitState', 43014, 44.03035137, 8.841e-05, 132.0910541, 0.00026523, 440.30351367, 0.00088412, -44.03035137, -8.841e-05, -132.0910541, -0.00026523, -440.30351367, -0.00088412, 0.4, 0.3, 0.003, 0.0, 0.0, 23014, 2)
    ops.limitCurve('ThreePoint', 13014, 3014, 0.0, 119.24939454, 0.02155193, 119.24939454, 0.06465579, 83.47457618, -2025.54361985, 0.05, 2, 0, 73014, 24014, 1, 3)
    ops.uniaxialMaterial('LimitState', 33014, 29.81234864, 5.986e-05, 89.43704591, 0.00017959, 298.12348636, 0.00059862, -29.81234864, -5.986e-05, -89.43704591, -0.00017959, -298.12348636, -0.00059862, 0.4, 0.3, 0.003, 0.0, 0.0, 13014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3014, 99999, 'P', 43014, 'Vy', 33014, 'Vz', 23014, 'My', 13014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173014, 73014, 173014, 3014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124014, 124014, 24014, 3014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173015, 6.6, 17.1, 8.375)
    ops.node(124015, 6.6, 17.1, 10.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3015, 173015, 124015, 0.1375, 29777018.84654119, 12407091.18605883, 0.00204719, 0.00078776, 0.00381276, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23015, 156.43134288, 0.00065716, 190.08328287, 0.01911829, 19.00832829, 0.07310118, -156.43134288, -0.00065716, -190.08328287, -0.01911829, -19.00832829, -0.07310118, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13015, 58.24109024, 0.00113769, 70.77007348, 0.01585542, 7.07700735, 0.04739106, -58.24109024, -0.00113769, -70.77007348, -0.01585542, -7.07700735, -0.04739106, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23015, 3015, 0.0, 180.28083583, 0.01314315, 180.28083583, 0.03942945, 126.19658508, -4786.68989578, 0.05, 2, 0, 73015, 24015, 2, 3)
    ops.uniaxialMaterial('LimitState', 43015, 45.07020896, 8.56e-05, 135.21062687, 0.00025679, 450.70208957, 0.00085598, -45.07020896, -8.56e-05, -135.21062687, -0.00025679, -450.70208957, -0.00085598, 0.4, 0.3, 0.003, 0.0, 0.0, 23015, 2)
    ops.limitCurve('ThreePoint', 13015, 3015, 0.0, 110.13520874, 0.02275372, 110.13520874, 0.06826115, 77.09464612, -1420.83099468, 0.05, 2, 0, 73015, 24015, 1, 3)
    ops.uniaxialMaterial('LimitState', 33015, 27.53380219, 5.229e-05, 82.60140656, 0.00015688, 275.33802185, 0.00052292, -27.53380219, -5.229e-05, -82.60140656, -0.00015688, -275.33802185, -0.00052292, 0.4, 0.3, 0.003, 0.0, 0.0, 13015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3015, 99999, 'P', 43015, 'Vy', 33015, 'Vz', 23015, 'My', 13015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173015, 73015, 173015, 3015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124015, 124015, 24015, 3015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173016, 10.3, 17.1, 8.35)
    ops.node(124016, 10.3, 17.1, 10.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3016, 173016, 124016, 0.1, 33384676.62131044, 13910281.92554602, 0.00127345, 0.00057292, 0.00146667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23016, 61.93326343, 0.00073628, 74.43823311, 0.0174149, 7.44382331, 0.0816995, -61.93326343, -0.00073628, -74.43823311, -0.0174149, -7.44382331, -0.0816995, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13016, 33.28246219, 0.00106423, 40.00253728, 0.01542557, 4.00025373, 0.06050759, -33.28246219, -0.00106423, -40.00253728, -0.01542557, -4.00025373, -0.06050759, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23016, 3016, 0.0, 135.13734784, 0.0147256, 135.13734784, 0.0441768, 94.59614349, -5544.52759828, 0.05, 2, 0, 73016, 24016, 2, 3)
    ops.uniaxialMaterial('LimitState', 43016, 33.78433696, 7.869e-05, 101.35301088, 0.00023607, 337.8433696, 0.00078691, -33.78433696, -7.869e-05, -101.35301088, -0.00023607, -337.8433696, -0.00078691, 0.4, 0.3, 0.003, 0.0, 0.0, 23016, 2)
    ops.limitCurve('ThreePoint', 13016, 3016, 0.0, 109.92093889, 0.02128462, 109.92093889, 0.06385387, 76.94465722, -2485.29320442, 0.05, 2, 0, 73016, 24016, 1, 3)
    ops.uniaxialMaterial('LimitState', 33016, 27.48023472, 6.401e-05, 82.44070417, 0.00019202, 274.80234723, 0.00064007, -27.48023472, -6.401e-05, -82.44070417, -0.00019202, -274.80234723, -0.00064007, 0.4, 0.3, 0.003, 0.0, 0.0, 13016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3016, 99999, 'P', 43016, 'Vy', 33016, 'Vz', 23016, 'My', 13016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173016, 73016, 173016, 3016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124016, 124016, 24016, 3016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173017, 0.0, 22.8, 8.35)
    ops.node(124017, 0.0, 22.8, 10.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3017, 173017, 124017, 0.0625, 31185685.79842636, 12994035.74934432, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23017, 22.47250628, 0.00107597, 27.22561497, 0.01897947, 2.7225615, 0.08376171, -22.47250628, -0.00107597, -27.22561497, -0.01897947, -2.7225615, -0.08376171, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13017, 22.47250628, 0.00107597, 27.22561497, 0.01897947, 2.7225615, 0.08376171, -22.47250628, -0.00107597, -27.22561497, -0.01897947, -2.7225615, -0.08376171, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23017, 3017, 0.0, 79.54822528, 0.02151942, 79.54822528, 0.06455826, 55.68375769, -4998.13285586, 0.05, 2, 0, 73017, 24017, 2, 3)
    ops.uniaxialMaterial('LimitState', 43017, 19.88705632, 7.934e-05, 59.66116896, 0.00023802, 198.87056319, 0.0007934, -19.88705632, -7.934e-05, -59.66116896, -0.00023802, -198.87056319, -0.0007934, 0.4, 0.3, 0.003, 0.0, 0.0, 23017, 2)
    ops.limitCurve('ThreePoint', 13017, 3017, 0.0, 79.54822528, 0.02151942, 79.54822528, 0.06455826, 55.68375769, -4998.13285586, 0.05, 2, 0, 73017, 24017, 1, 3)
    ops.uniaxialMaterial('LimitState', 33017, 19.88705632, 7.934e-05, 59.66116896, 0.00023802, 198.87056319, 0.0007934, -19.88705632, -7.934e-05, -59.66116896, -0.00023802, -198.87056319, -0.0007934, 0.4, 0.3, 0.003, 0.0, 0.0, 13017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3017, 99999, 'P', 43017, 'Vy', 33017, 'Vz', 23017, 'My', 13017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173017, 73017, 173017, 3017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124017, 124017, 24017, 3017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173018, 2.9, 22.8, 8.375)
    ops.node(124018, 2.9, 22.8, 10.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3018, 173018, 124018, 0.0875, 31333445.74991001, 13055602.39579584, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23018, 40.62024933, 0.0010819, 49.1589766, 0.02186299, 4.91589766, 0.07101146, -40.62024933, -0.0010819, -49.1589766, -0.02186299, -4.91589766, -0.07101146, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13018, 59.96324335, 0.00082259, 72.56803504, 0.02399622, 7.2568035, 0.08764218, -59.96324335, -0.00082259, -72.56803504, -0.02399622, -7.2568035, -0.08764218, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23018, 3018, 0.0, 96.72418227, 0.02163801, 96.72418227, 0.06491402, 67.70692759, -2790.18367866, 0.05, 2, 0, 73018, 24018, 2, 3)
    ops.uniaxialMaterial('LimitState', 43018, 24.18104557, 6.858e-05, 72.5431367, 0.00020575, 241.81045567, 0.00068583, -24.18104557, -6.858e-05, -72.5431367, -0.00020575, -241.81045567, -0.00068583, 0.4, 0.3, 0.003, 0.0, 0.0, 23018, 2)
    ops.limitCurve('ThreePoint', 13018, 3018, 0.0, 113.86790696, 0.01645184, 113.86790696, 0.04935551, 79.70753488, -4988.54859471, 0.05, 2, 0, 73018, 24018, 1, 3)
    ops.uniaxialMaterial('LimitState', 33018, 28.46697674, 8.074e-05, 85.40093022, 0.00024222, 284.66976741, 0.00080739, -28.46697674, -8.074e-05, -85.40093022, -0.00024222, -284.66976741, -0.00080739, 0.4, 0.3, 0.003, 0.0, 0.0, 13018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3018, 99999, 'P', 43018, 'Vy', 33018, 'Vz', 23018, 'My', 13018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173018, 73018, 173018, 3018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124018, 124018, 24018, 3018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173019, 6.6, 22.8, 8.375)
    ops.node(124019, 6.6, 22.8, 10.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3019, 173019, 124019, 0.0875, 30896740.23048757, 12873641.76270315, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23019, 40.8195782, 0.00114093, 49.45404379, 0.02162849, 4.94540438, 0.07032204, -40.8195782, -0.00114093, -49.45404379, -0.02162849, -4.94540438, -0.07032204, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13019, 60.51066146, 0.00085541, 73.31033375, 0.02370171, 7.33103338, 0.08675857, -60.51066146, -0.00085541, -73.31033375, -0.02370171, -7.33103338, -0.08675857, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23019, 3019, 0.0, 96.00062311, 0.02281867, 96.00062311, 0.068456, 67.20043618, -2565.17848568, 0.05, 2, 0, 73019, 24019, 2, 3)
    ops.uniaxialMaterial('LimitState', 43019, 24.00015578, 6.903e-05, 72.00046733, 0.0002071, 240.00155777, 0.00069032, -24.00015578, -6.903e-05, -72.00046733, -0.0002071, -240.00155777, -0.00069032, 0.4, 0.3, 0.003, 0.0, 0.0, 23019, 2)
    ops.limitCurve('ThreePoint', 13019, 3019, 0.0, 113.11982675, 0.01710824, 113.11982675, 0.05132471, 79.18387872, -4539.53077597, 0.05, 2, 0, 73019, 24019, 1, 3)
    ops.uniaxialMaterial('LimitState', 33019, 28.27995669, 8.134e-05, 84.83987006, 0.00024403, 282.79956687, 0.00081342, -28.27995669, -8.134e-05, -84.83987006, -0.00024403, -282.79956687, -0.00081342, 0.4, 0.3, 0.003, 0.0, 0.0, 13019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3019, 99999, 'P', 43019, 'Vy', 33019, 'Vz', 23019, 'My', 13019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173019, 73019, 173019, 3019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124019, 124019, 24019, 3019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173020, 10.3, 22.8, 8.35)
    ops.node(124020, 10.3, 22.8, 10.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3020, 173020, 124020, 0.0625, 30724527.35772214, 12801886.39905089, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23020, 23.79009217, 0.0010226, 28.85293058, 0.01921173, 2.88529306, 0.08325431, -23.79009217, -0.0010226, -28.85293058, -0.01921173, -2.88529306, -0.08325431, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13020, 23.79009217, 0.0010226, 28.85293058, 0.01921173, 2.88529306, 0.08325431, -23.79009217, -0.0010226, -28.85293058, -0.01921173, -2.88529306, -0.08325431, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23020, 3020, 0.0, 80.55371671, 0.02045202, 80.55371671, 0.06135606, 56.3876017, -4309.07366032, 0.05, 2, 0, 73020, 24020, 2, 3)
    ops.uniaxialMaterial('LimitState', 43020, 20.13842918, 8.155e-05, 60.41528753, 0.00024465, 201.38429178, 0.00081549, -20.13842918, -8.155e-05, -60.41528753, -0.00024465, -201.38429178, -0.00081549, 0.4, 0.3, 0.003, 0.0, 0.0, 23020, 2)
    ops.limitCurve('ThreePoint', 13020, 3020, 0.0, 80.55371671, 0.02045202, 80.55371671, 0.06135606, 56.3876017, -4309.07366032, 0.05, 2, 0, 73020, 24020, 1, 3)
    ops.uniaxialMaterial('LimitState', 33020, 20.13842918, 8.155e-05, 60.41528753, 0.00024465, 201.38429178, 0.00081549, -20.13842918, -8.155e-05, -60.41528753, -0.00024465, -201.38429178, -0.00081549, 0.4, 0.3, 0.003, 0.0, 0.0, 13020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3020, 99999, 'P', 43020, 'Vy', 33020, 'Vz', 23020, 'My', 13020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173020, 73020, 173020, 3020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124020, 124020, 24020, 3020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170001, 0.0, 0.0, 0.0)
    ops.node(124021, 0.0, 0.0, 1.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4052, 170001, 124021, 0.0625, 31055074.27362947, 12939614.28067895, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24052, 46.38921944, 0.00082302, 55.73208161, 0.02886722, 5.57320816, 0.10538195, -46.38921944, -0.00082302, -55.73208161, -0.02886722, -5.57320816, -0.10538195, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14052, 42.92142691, 0.00082302, 51.56587018, 0.02886722, 5.15658702, 0.10538195, -42.92142691, -0.00082302, -51.56587018, -0.02886722, -5.15658702, -0.10538195, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24052, 4052, 0.0, 128.79479166, 0.01646039, 128.79479166, 0.04938116, 90.15635416, -5653.88102727, 0.05, 2, 0, 70001, 24021, 2, 3)
    ops.uniaxialMaterial('LimitState', 44052, 32.19869791, 6.45e-05, 96.59609374, 0.0001935, 321.98697915, 0.00064499, -32.19869791, -6.45e-05, -96.59609374, -0.0001935, -321.98697915, -0.00064499, 0.4, 0.3, 0.003, 0.0, 0.0, 24052, 2)
    ops.limitCurve('ThreePoint', 14052, 4052, 0.0, 128.79479166, 0.01646039, 128.79479166, 0.04938116, 90.15635416, -5653.88102727, 0.05, 2, 0, 70001, 24021, 1, 3)
    ops.uniaxialMaterial('LimitState', 34052, 32.19869791, 6.45e-05, 96.59609374, 0.0001935, 321.98697915, 0.00064499, -32.19869791, -6.45e-05, -96.59609374, -0.0001935, -321.98697915, -0.00064499, 0.4, 0.3, 0.003, 0.0, 0.0, 14052, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4052, 99999, 'P', 44052, 'Vy', 34052, 'Vz', 24052, 'My', 14052, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170001, 70001, 170001, 4052, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124021, 124021, 24021, 4052, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174021, 0.0, 0.0, 1.55)
    ops.node(121001, 0.0, 0.0, 2.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4053, 174021, 121001, 0.0625, 32241364.15806303, 13433901.73252626, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24053, 44.65969997, 0.00081367, 53.58477359, 0.02946659, 5.35847736, 0.11230859, -44.65969997, -0.00081367, -53.58477359, -0.02946659, -5.35847736, -0.11230859, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14053, 41.14554666, 0.00081367, 49.36832992, 0.02946659, 4.93683299, 0.11230859, -41.14554666, -0.00081367, -49.36832992, -0.02946659, -4.93683299, -0.11230859, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24053, 4053, 0.0, 128.94176401, 0.01627337, 128.94176401, 0.04882011, 90.25923481, -6091.73963813, 0.05, 2, 0, 74021, 21001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44053, 32.235441, 6.22e-05, 96.70632301, 0.00018659, 322.35441002, 0.00062197, -32.235441, -6.22e-05, -96.70632301, -0.00018659, -322.35441002, -0.00062197, 0.4, 0.3, 0.003, 0.0, 0.0, 24053, 2)
    ops.limitCurve('ThreePoint', 14053, 4053, 0.0, 128.94176401, 0.01627337, 128.94176401, 0.04882011, 90.25923481, -6091.73963813, 0.05, 2, 0, 74021, 21001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34053, 32.235441, 6.22e-05, 96.70632301, 0.00018659, 322.35441002, 0.00062197, -32.235441, -6.22e-05, -96.70632301, -0.00018659, -322.35441002, -0.00062197, 0.4, 0.3, 0.003, 0.0, 0.0, 14053, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4053, 99999, 'P', 44053, 'Vy', 34053, 'Vz', 24053, 'My', 14053, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174021, 74021, 174021, 4053, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121001, 121001, 21001, 4053, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170002, 2.9, 0.0, 0.0)
    ops.node(124022, 2.9, 0.0, 1.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4054, 170002, 124022, 0.12, 31924882.2026888, 13302034.25112033, 0.00194385, 0.00176, 0.00099, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24054, 149.3924768, 0.00079395, 179.02480148, 0.04506668, 17.90248015, 0.14506668, -149.3924768, -0.00079395, -179.02480148, -0.04506668, -17.90248015, -0.14506668, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14054, 168.31710248, 0.00068826, 201.70316807, 0.04301224, 20.17031681, 0.13721564, -168.31710248, -0.00068826, -201.70316807, -0.04301224, -20.17031681, -0.13721564, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24054, 4054, 0.0, 266.28711831, 0.01587895, 266.28711831, 0.04763684, 186.40098282, -9594.54631981, 0.05, 2, 0, 70002, 24022, 2, 3)
    ops.uniaxialMaterial('LimitState', 44054, 66.57177958, 6.756e-05, 199.71533873, 0.00020269, 665.71779577, 0.00067563, -66.57177958, -6.756e-05, -199.71533873, -0.00020269, -665.71779577, -0.00067563, 0.4, 0.3, 0.003, 0.0, 0.0, 24054, 2)
    ops.limitCurve('ThreePoint', 14054, 4054, 0.0, 438.74215037, 0.01376522, 438.74215037, 0.04129567, 307.11950526, -26307.18098229, 0.05, 2, 0, 70002, 24022, 1, 3)
    ops.uniaxialMaterial('LimitState', 34054, 109.68553759, 0.00011132, 329.05661278, 0.00033395, 1096.85537593, 0.00111318, -109.68553759, -0.00011132, -329.05661278, -0.00033395, -1096.85537593, -0.00111318, 0.4, 0.3, 0.003, 0.0, 0.0, 14054, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4054, 99999, 'P', 44054, 'Vy', 34054, 'Vz', 24054, 'My', 14054, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170002, 70002, 170002, 4054, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124022, 124022, 24022, 4054, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174022, 2.9, 0.0, 1.55)
    ops.node(121002, 2.9, 0.0, 2.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4055, 174022, 121002, 0.12, 31036334.67733297, 12931806.1155554, 0.00194385, 0.00176, 0.00099, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24055, 82.42109679, 0.00076012, 99.05553323, 0.0426996, 9.90555332, 0.1426996, -82.42109679, -0.00076012, -99.05553323, -0.0426996, -9.90555332, -0.1426996, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14055, 112.95965528, 0.00066367, 135.75746165, 0.04075709, 13.57574617, 0.13485339, -112.95965528, -0.00066367, -135.75746165, -0.04075709, -13.57574617, -0.13485339, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24055, 4055, 0.0, 259.89175357, 0.01520241, 259.89175357, 0.04560723, 181.9242275, -10042.96851503, 0.05, 2, 0, 74022, 21002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44055, 64.97293839, 6.783e-05, 194.91881518, 0.00020348, 649.72938393, 0.00067828, -64.97293839, -6.783e-05, -194.91881518, -0.00020348, -649.72938393, -0.00067828, 0.4, 0.3, 0.003, 0.0, 0.0, 24055, 2)
    ops.limitCurve('ThreePoint', 14055, 4055, 0.0, 431.19537057, 0.01327336, 431.19537057, 0.03982009, 301.8367594, -28293.13653932, 0.05, 2, 0, 74022, 21002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34055, 107.79884264, 0.00011254, 323.39652792, 0.00033761, 1077.98842641, 0.00112535, -107.79884264, -0.00011254, -323.39652792, -0.00033761, -1077.98842641, -0.00112535, 0.4, 0.3, 0.003, 0.0, 0.0, 14055, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4055, 99999, 'P', 44055, 'Vy', 34055, 'Vz', 24055, 'My', 14055, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174022, 74022, 174022, 4055, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121002, 121002, 21002, 4055, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171001, 0.0, 0.0, 2.95)
    ops.node(124023, 0.0, 0.0, 3.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4057, 171001, 124023, 0.0625, 29300788.37672226, 12208661.82363428, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24057, 42.21529975, 0.00084211, 51.02796703, 0.03056374, 5.1027967, 0.10906321, -42.21529975, -0.00084211, -51.02796703, -0.03056374, -5.1027967, -0.10906321, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14057, 38.94365368, 0.00084211, 47.07334753, 0.03056374, 4.70733475, 0.10906321, -38.94365368, -0.00084211, -47.07334753, -0.03056374, -4.70733475, -0.10906321, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24057, 4057, 0.0, 121.75867301, 0.01684226, 121.75867301, 0.05052677, 85.23107111, -6470.73600108, 0.05, 2, 0, 71001, 24023, 2, 3)
    ops.uniaxialMaterial('LimitState', 44057, 30.43966825, 6.463e-05, 91.31900476, 0.00019388, 304.39668252, 0.00064626, -30.43966825, -6.463e-05, -91.31900476, -0.00019388, -304.39668252, -0.00064626, 0.4, 0.3, 0.003, 0.0, 0.0, 24057, 2)
    ops.limitCurve('ThreePoint', 14057, 4057, 0.0, 121.75867301, 0.01684226, 121.75867301, 0.05052677, 85.23107111, -6470.73600108, 0.05, 2, 0, 71001, 24023, 1, 3)
    ops.uniaxialMaterial('LimitState', 34057, 30.43966825, 6.463e-05, 91.31900476, 0.00019388, 304.39668252, 0.00064626, -30.43966825, -6.463e-05, -91.31900476, -0.00019388, -304.39668252, -0.00064626, 0.4, 0.3, 0.003, 0.0, 0.0, 14057, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4057, 99999, 'P', 44057, 'Vy', 34057, 'Vz', 24057, 'My', 14057, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171001, 71001, 171001, 4057, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124023, 124023, 24023, 4057, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174023, 0.0, 0.0, 4.25)
    ops.node(122001, 0.0, 0.0, 5.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4058, 174023, 122001, 0.0625, 32116081.30672419, 13381700.54446841, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24058, 40.28993929, 0.00079232, 48.46499311, 0.03058514, 4.84649931, 0.11880968, -40.28993929, -0.00079232, -48.46499311, -0.03058514, -4.84649931, -0.11880968, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14058, 36.91098545, 0.00079232, 44.40043065, 0.03058514, 4.44004307, 0.11880968, -36.91098545, -0.00079232, -44.40043065, -0.03058514, -4.44004307, -0.11880968, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24058, 4058, 0.0, 124.69766237, 0.01584635, 124.69766237, 0.04753905, 87.28836366, -7318.46571532, 0.05, 2, 0, 74023, 22001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44058, 31.17441559, 6.038e-05, 93.52324678, 0.00018115, 311.74415592, 0.00060384, -31.17441559, -6.038e-05, -93.52324678, -0.00018115, -311.74415592, -0.00060384, 0.4, 0.3, 0.003, 0.0, 0.0, 24058, 2)
    ops.limitCurve('ThreePoint', 14058, 4058, 0.0, 124.69766237, 0.01584635, 124.69766237, 0.04753905, 87.28836366, -7318.46571532, 0.05, 2, 0, 74023, 22001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34058, 31.17441559, 6.038e-05, 93.52324678, 0.00018115, 311.74415592, 0.00060384, -31.17441559, -6.038e-05, -93.52324678, -0.00018115, -311.74415592, -0.00060384, 0.4, 0.3, 0.003, 0.0, 0.0, 14058, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4058, 99999, 'P', 44058, 'Vy', 34058, 'Vz', 24058, 'My', 14058, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174023, 74023, 174023, 4058, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122001, 122001, 22001, 4058, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171002, 2.9, 0.0, 2.975)
    ops.node(124024, 2.9, 0.0, 3.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4059, 171002, 124024, 0.12, 30751702.89166789, 12813209.53819495, 0.00194385, 0.00176, 0.00099, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24059, 76.33278198, 0.0007319, 91.96970254, 0.03762879, 9.19697025, 0.11419915, -76.33278198, -0.0007319, -91.96970254, -0.03762879, -9.19697025, -0.11419915, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14059, 104.54112582, 0.00064565, 125.9565811, 0.04171925, 12.59565811, 0.14046908, -104.54112582, -0.00064565, -125.9565811, -0.04171925, -12.59565811, -0.14046908, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24059, 4059, 0.0, 250.98407034, 0.01463807, 250.98407034, 0.04391421, 175.68884924, -10821.23509639, 0.05, 2, 0, 71002, 24024, 2, 3)
    ops.uniaxialMaterial('LimitState', 44059, 62.74601759, 6.611e-05, 188.23805276, 0.00019833, 627.46017585, 0.00066109, -62.74601759, -6.611e-05, -188.23805276, -0.00019833, -627.46017585, -0.00066109, 0.4, 0.3, 0.003, 0.0, 0.0, 24059, 2)
    ops.limitCurve('ThreePoint', 14059, 4059, 0.0, 334.64542712, 0.01291308, 334.64542712, 0.03873923, 234.25179899, -16655.26810729, 0.05, 2, 0, 71002, 24024, 1, 3)
    ops.uniaxialMaterial('LimitState', 34059, 83.66135678, 8.815e-05, 250.98407034, 0.00026444, 836.6135678, 0.00088146, -83.66135678, -8.815e-05, -250.98407034, -0.00026444, -836.6135678, -0.00088146, 0.4, 0.3, 0.003, 0.0, 0.0, 14059, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4059, 99999, 'P', 44059, 'Vy', 34059, 'Vz', 24059, 'My', 14059, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171002, 71002, 171002, 4059, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124024, 124024, 24024, 4059, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174024, 2.9, 0.0, 4.25)
    ops.node(122002, 2.9, 0.0, 5.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4060, 174024, 122002, 0.12, 31520819.19874612, 13133674.66614422, 0.00194385, 0.00176, 0.00099, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24060, 71.61254638, 0.0007433, 86.19867508, 0.03830307, 8.61986751, 0.11837392, -71.61254638, -0.0007433, -86.19867508, -0.03830307, -8.61986751, -0.11837392, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14060, 98.56128682, 0.00065002, 118.63636705, 0.04246154, 11.8636367, 0.14246154, -98.56128682, -0.00065002, -118.63636705, -0.04246154, -11.8636367, -0.14246154, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24060, 4060, 0.0, 254.26502976, 0.01486592, 254.26502976, 0.04459777, 177.98552083, -11807.48377709, 0.05, 2, 0, 74024, 22002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44060, 63.56625744, 6.534e-05, 190.69877232, 0.00019602, 635.66257439, 0.00065339, -63.56625744, -6.534e-05, -190.69877232, -0.00019602, -635.66257439, -0.00065339, 0.4, 0.3, 0.003, 0.0, 0.0, 24060, 2)
    ops.limitCurve('ThreePoint', 14060, 4060, 0.0, 339.02003967, 0.01300034, 339.02003967, 0.03900101, 237.31402777, -18448.46394941, 0.05, 2, 0, 74024, 22002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34060, 84.75500992, 8.712e-05, 254.26502976, 0.00026136, 847.55009918, 0.00087119, -84.75500992, -8.712e-05, -254.26502976, -0.00026136, -847.55009918, -0.00087119, 0.4, 0.3, 0.003, 0.0, 0.0, 14060, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4060, 99999, 'P', 44060, 'Vy', 34060, 'Vz', 24060, 'My', 14060, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174024, 74024, 174024, 4060, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122002, 122002, 22002, 4060, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172001, 0.0, 0.0, 5.65)
    ops.node(124025, 0.0, 0.0, 6.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4062, 172001, 124025, 0.0625, 29543582.66215923, 12309826.10923301, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24062, 29.69785606, 0.00077388, 35.98608262, 0.02324325, 3.59860826, 0.09065324, -29.69785606, -0.00077388, -35.98608262, -0.02324325, -3.59860826, -0.09065324, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14062, 29.69785606, 0.00077388, 35.98608262, 0.02324325, 3.59860826, 0.09065324, -29.69785606, -0.00077388, -35.98608262, -0.02324325, -3.59860826, -0.09065324, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24062, 4062, 0.0, 100.95486068, 0.01547765, 100.95486068, 0.04643294, 70.66840248, -5186.72502432, 0.05, 2, 0, 72001, 24025, 2, 3)
    ops.uniaxialMaterial('LimitState', 44062, 25.23871517, 5.314e-05, 75.71614551, 0.00015943, 252.38715171, 0.00053144, -25.23871517, -5.314e-05, -75.71614551, -0.00015943, -252.38715171, -0.00053144, 0.4, 0.3, 0.003, 0.0, 0.0, 24062, 2)
    ops.limitCurve('ThreePoint', 14062, 4062, 0.0, 100.95486068, 0.01547765, 100.95486068, 0.04643294, 70.66840248, -5186.72502432, 0.05, 2, 0, 72001, 24025, 1, 3)
    ops.uniaxialMaterial('LimitState', 34062, 25.23871517, 5.314e-05, 75.71614551, 0.00015943, 252.38715171, 0.00053144, -25.23871517, -5.314e-05, -75.71614551, -0.00015943, -252.38715171, -0.00053144, 0.4, 0.3, 0.003, 0.0, 0.0, 14062, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4062, 99999, 'P', 44062, 'Vy', 34062, 'Vz', 24062, 'My', 14062, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172001, 72001, 172001, 4062, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124025, 124025, 24025, 4062, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174025, 0.0, 0.0, 6.925)
    ops.node(123001, 0.0, 0.0, 7.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4063, 174025, 123001, 0.0625, 31719754.5251003, 13216564.38545846, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24063, 25.47946691, 0.00075306, 30.76117592, 0.01839799, 3.07611759, 0.07992801, -25.47946691, -0.00075306, -30.76117592, -0.01839799, -3.07611759, -0.07992801, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14063, 25.47946691, 0.00075306, 30.76117592, 0.01839799, 3.07611759, 0.07992801, -25.47946691, -0.00075306, -30.76117592, -0.01839799, -3.07611759, -0.07992801, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24063, 4063, 0.0, 91.43511349, 0.01506119, 91.43511349, 0.04518356, 64.00457944, -4797.7927167, 0.05, 2, 0, 74025, 23001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44063, 22.85877837, 4.483e-05, 68.57633512, 0.00013449, 228.58778372, 0.0004483, -22.85877837, -4.483e-05, -68.57633512, -0.00013449, -228.58778372, -0.0004483, 0.4, 0.3, 0.003, 0.0, 0.0, 24063, 2)
    ops.limitCurve('ThreePoint', 14063, 4063, 0.0, 91.43511349, 0.01506119, 91.43511349, 0.04518356, 64.00457944, -4797.7927167, 0.05, 2, 0, 74025, 23001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34063, 22.85877837, 4.483e-05, 68.57633512, 0.00013449, 228.58778372, 0.0004483, -22.85877837, -4.483e-05, -68.57633512, -0.00013449, -228.58778372, -0.0004483, 0.4, 0.3, 0.003, 0.0, 0.0, 14063, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4063, 99999, 'P', 44063, 'Vy', 34063, 'Vz', 24063, 'My', 14063, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174025, 74025, 174025, 4063, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123001, 123001, 23001, 4063, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172002, 2.9, 0.0, 5.675)
    ops.node(124026, 2.9, 0.0, 6.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4064, 172002, 124026, 0.0875, 31056615.85430542, 12940256.60596059, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24064, 53.30117571, 0.00083844, 64.23347092, 0.03052736, 6.42334709, 0.09349291, -53.30117571, -0.00083844, -64.23347092, -0.03052736, -6.42334709, -0.09349291, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14064, 77.94244943, 0.00069168, 93.92877347, 0.03419578, 9.39287735, 0.11807333, -77.94244943, -0.00069168, -93.92877347, -0.03419578, -9.39287735, -0.11807333, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24064, 4064, 0.0, 144.9198534, 0.01676872, 144.9198534, 0.05030616, 101.44389738, -5653.82337695, 0.05, 2, 0, 72002, 24026, 2, 3)
    ops.uniaxialMaterial('LimitState', 44064, 36.22996335, 5.184e-05, 108.68989005, 0.00015551, 362.29963349, 0.00051836, -36.22996335, -5.184e-05, -108.68989005, -0.00015551, -362.29963349, -0.00051836, 0.4, 0.3, 0.003, 0.0, 0.0, 24064, 2)
    ops.limitCurve('ThreePoint', 14064, 4064, 0.0, 202.88779476, 0.01383369, 202.88779476, 0.04150108, 142.02145633, -9213.73029729, 0.05, 2, 0, 72002, 24026, 1, 3)
    ops.uniaxialMaterial('LimitState', 34064, 50.72194869, 7.257e-05, 152.16584607, 0.00021771, 507.21948689, 0.0007257, -50.72194869, -7.257e-05, -152.16584607, -0.00021771, -507.21948689, -0.0007257, 0.4, 0.3, 0.003, 0.0, 0.0, 14064, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4064, 99999, 'P', 44064, 'Vy', 34064, 'Vz', 24064, 'My', 14064, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172002, 72002, 172002, 4064, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124026, 124026, 24026, 4064, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174026, 2.9, 0.0, 6.925)
    ops.node(123002, 2.9, 0.0, 7.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4065, 174026, 123002, 0.0875, 31317128.95899792, 13048803.7329158, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24065, 47.71675308, 0.00083288, 57.54456555, 0.03136359, 5.75445655, 0.09730955, -47.71675308, -0.00083288, -57.54456555, -0.03136359, -5.75445655, -0.09730955, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14065, 70.24081249, 0.0006811, 84.70771327, 0.03513514, 8.47077133, 0.12298295, -70.24081249, -0.0006811, -84.70771327, -0.03513514, -8.47077133, -0.12298295, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24065, 4065, 0.0, 142.11067015, 0.01665769, 142.11067015, 0.04997306, 99.47746911, -6175.47894548, 0.05, 2, 0, 74026, 23002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44065, 35.52766754, 5.041e-05, 106.58300261, 0.00015123, 355.27667538, 0.00050408, -35.52766754, -5.041e-05, -106.58300261, -0.00015123, -355.27667538, -0.00050408, 0.4, 0.3, 0.003, 0.0, 0.0, 24065, 2)
    ops.limitCurve('ThreePoint', 14065, 4065, 0.0, 198.95493821, 0.01362198, 198.95493821, 0.04086595, 139.26845675, -10352.5568465, 0.05, 2, 0, 74026, 23002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34065, 49.73873455, 7.057e-05, 149.21620366, 0.00021172, 497.38734553, 0.00070572, -49.73873455, -7.057e-05, -149.21620366, -0.00021172, -497.38734553, -0.00070572, 0.4, 0.3, 0.003, 0.0, 0.0, 14065, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4065, 99999, 'P', 44065, 'Vy', 34065, 'Vz', 24065, 'My', 14065, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174026, 74026, 174026, 4065, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123002, 123002, 23002, 4065, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173001, 0.0, 0.0, 8.35)
    ops.node(124027, 0.0, 0.0, 9.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4067, 173001, 124027, 0.0625, 31122684.38147728, 12967785.15894887, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24067, 24.54439118, 0.00075704, 29.70995023, 0.01839245, 2.97099502, 0.08114155, -24.54439118, -0.00075704, -29.70995023, -0.01839245, -2.97099502, -0.08114155, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14067, 24.54439118, 0.00075704, 29.70995023, 0.01839245, 2.97099502, 0.08114155, -24.54439118, -0.00075704, -29.70995023, -0.01839245, -2.97099502, -0.08114155, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24067, 4067, 0.0, 88.05732091, 0.01514071, 88.05732091, 0.04542212, 61.64012464, -5856.11084106, 0.05, 2, 0, 73001, 24027, 2, 3)
    ops.uniaxialMaterial('LimitState', 44067, 22.01433023, 4.4e-05, 66.04299069, 0.00013201, 220.14330229, 0.00044002, -22.01433023, -4.4e-05, -66.04299069, -0.00013201, -220.14330229, -0.00044002, 0.4, 0.3, 0.003, 0.0, 0.0, 24067, 2)
    ops.limitCurve('ThreePoint', 14067, 4067, 0.0, 88.05732091, 0.01514071, 88.05732091, 0.04542212, 61.64012464, -5856.11084106, 0.05, 2, 0, 73001, 24027, 1, 3)
    ops.uniaxialMaterial('LimitState', 34067, 22.01433023, 4.4e-05, 66.04299069, 0.00013201, 220.14330229, 0.00044002, -22.01433023, -4.4e-05, -66.04299069, -0.00013201, -220.14330229, -0.00044002, 0.4, 0.3, 0.003, 0.0, 0.0, 14067, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4067, 99999, 'P', 44067, 'Vy', 34067, 'Vz', 24067, 'My', 14067, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173001, 73001, 173001, 4067, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124027, 124027, 24027, 4067, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174027, 0.0, 0.0, 9.625)
    ops.node(124001, 0.0, 0.0, 10.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4068, 174027, 124001, 0.0625, 30966197.938402, 12902582.47433417, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24068, 21.24439805, 0.0007284, 25.77804568, 0.0188235, 2.57780457, 0.08529222, -21.24439805, -0.0007284, -25.77804568, -0.0188235, -2.57780457, -0.08529222, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14068, 21.24439805, 0.0007284, 25.77804568, 0.0188235, 2.57780457, 0.08529222, -21.24439805, -0.0007284, -25.77804568, -0.0188235, -2.57780457, -0.08529222, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24068, 4068, 0.0, 83.69408807, 0.01456791, 83.69408807, 0.04370373, 58.58586165, -40377.97703903, 0.05, 2, 0, 74027, 24001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44068, 20.92352202, 4.203e-05, 62.77056605, 0.0001261, 209.23522018, 0.00042033, -20.92352202, -4.203e-05, -62.77056605, -0.0001261, -209.23522018, -0.00042033, 0.4, 0.3, 0.003, 0.0, 0.0, 24068, 2)
    ops.limitCurve('ThreePoint', 14068, 4068, 0.0, 83.69408807, 0.01456791, 83.69408807, 0.04370373, 58.58586165, -40377.97703903, 0.05, 2, 0, 74027, 24001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34068, 20.92352202, 4.203e-05, 62.77056605, 0.0001261, 209.23522018, 0.00042033, -20.92352202, -4.203e-05, -62.77056605, -0.0001261, -209.23522018, -0.00042033, 0.4, 0.3, 0.003, 0.0, 0.0, 14068, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4068, 99999, 'P', 44068, 'Vy', 34068, 'Vz', 24068, 'My', 14068, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174027, 74027, 174027, 4068, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124001, 124001, 24001, 4068, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173002, 2.9, 0.0, 8.375)
    ops.node(124028, 2.9, 0.0, 9.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4069, 173002, 124028, 0.0875, 31444661.40631235, 13101942.25263015, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24069, 41.56912581, 0.00081472, 50.25313928, 0.01732757, 5.02531393, 0.05955152, -41.56912581, -0.00081472, -50.25313928, -0.01732757, -5.02531393, -0.05955152, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14069, 61.55145141, 0.00066908, 74.40987994, 0.01898908, 7.44098799, 0.07300835, -61.55145141, -0.00066908, -74.40987994, -0.01898908, -7.44098799, -0.07300835, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24069, 4069, 0.0, 98.69291289, 0.01629446, 98.69291289, 0.04888337, 69.08503903, -3304.57869447, 0.05, 2, 0, 73002, 24028, 2, 3)
    ops.uniaxialMaterial('LimitState', 44069, 24.67322822, 3.487e-05, 74.01968467, 0.0001046, 246.73228224, 0.00034866, -24.67322822, -3.487e-05, -74.01968467, -0.0001046, -246.73228224, -0.00034866, 0.4, 0.3, 0.003, 0.0, 0.0, 24069, 2)
    ops.limitCurve('ThreePoint', 14069, 4069, 0.0, 142.21037233, 0.01338155, 142.21037233, 0.04014464, 99.54726063, -5602.15673505, 0.05, 2, 0, 73002, 24028, 1, 3)
    ops.uniaxialMaterial('LimitState', 34069, 35.55259308, 5.024e-05, 106.65777925, 0.00015072, 355.52593083, 0.00050239, -35.55259308, -5.024e-05, -106.65777925, -0.00015072, -355.52593083, -0.00050239, 0.4, 0.3, 0.003, 0.0, 0.0, 14069, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4069, 99999, 'P', 44069, 'Vy', 34069, 'Vz', 24069, 'My', 14069, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173002, 73002, 173002, 4069, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124028, 124028, 24028, 4069, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174028, 2.9, 0.0, 9.625)
    ops.node(124002, 2.9, 0.0, 10.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4070, 174028, 124002, 0.0875, 33186641.13703529, 13827767.14043137, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24070, 40.32116468, 0.00078325, 48.521401, 0.01681436, 4.8521401, 0.06099641, -40.32116468, -0.00078325, -48.521401, -0.01681436, -4.8521401, -0.06099641, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14070, 59.59164427, 0.00065278, 71.7109759, 0.01843831, 7.17109759, 0.07496268, -59.59164427, -0.00065278, -71.7109759, -0.01843831, -7.17109759, -0.07496268, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24070, 4070, 0.0, 99.95690765, 0.01566508, 99.95690765, 0.04699525, 69.96983536, -5482.14025056, 0.05, 2, 0, 74028, 24002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44070, 24.98922691, 3.346e-05, 74.96768074, 0.00010038, 249.89226914, 0.00033459, -24.98922691, -3.346e-05, -74.96768074, -0.00010038, -249.89226914, -0.00033459, 0.4, 0.3, 0.003, 0.0, 0.0, 24070, 2)
    ops.limitCurve('ThreePoint', 14070, 4070, 0.0, 144.44522137, 0.01305554, 144.44522137, 0.03916662, 101.11165496, -9983.49811997, 0.05, 2, 0, 74028, 24002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34070, 36.11130534, 4.835e-05, 108.33391603, 0.00014505, 361.11305343, 0.0004835, -36.11130534, -4.835e-05, -108.33391603, -0.00014505, -361.11305343, -0.0004835, 0.4, 0.3, 0.003, 0.0, 0.0, 14070, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4070, 99999, 'P', 44070, 'Vy', 34070, 'Vz', 24070, 'My', 14070, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174028, 74028, 174028, 4070, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124002, 124002, 24002, 4070, '-orient', 0, 0, 1, 0, 1, 0)
