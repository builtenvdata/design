import openseespy.opensees as ops


def add_columns() -> None:
    """Add components of all columns to ops domain (plastic hinges, column elements and nodes)
    """
    # Create elastic column element nodes
    ops.node(170001, 0.0, 0.0, 0.0)
    ops.node(121001, 0.0, 0.0, 3.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1, 170001, 121001, 0.0875, 26119670.70288791, 10883196.1262033, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20001, 47.27492918, 0.00164433, 57.26877936, 0.01801963, 5.72687794, 0.05141798, -47.27492918, -0.00164433, -57.26877936, -0.01801963, -5.72687794, -0.05141798, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10001, 64.10948902, 0.00116652, 77.66214028, 0.01942712, 7.76621403, 0.06267708, -64.10948902, -0.00116652, -77.66214028, -0.01942712, -7.76621403, -0.06267708, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20001, 1, 0.0, 93.40673541, 0.03288656, 93.40673541, 0.09865968, 65.38471478, -1036.38769468, 0.05, 2, 0, 70001, 21001, 2, 3)
    ops.uniaxialMaterial('LimitState', 40001, 23.35168385, 0.00010741, 70.05505155, 0.00032222, 233.51683851, 0.00107406, -23.35168385, -0.00010741, -70.05505155, -0.00032222, -233.51683851, -0.00107406, 0.4, 0.3, 0.003, 0.0, 0.0, 20001, 2)
    ops.limitCurve('ThreePoint', 10001, 1, 0.0, 109.62879302, 0.02333033, 109.62879302, 0.06999098, 76.74015511, -1510.72622858, 0.05, 2, 0, 70001, 21001, 1, 3)
    ops.uniaxialMaterial('LimitState', 30001, 27.40719825, 0.00012606, 82.22159476, 0.00037818, 274.07198254, 0.00126059, -27.40719825, -0.00012606, -82.22159476, -0.00037818, -274.07198254, -0.00126059, 0.4, 0.3, 0.003, 0.0, 0.0, 10001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1, 99999, 'P', 40001, 'Vy', 30001, 'Vz', 20001, 'My', 10001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170001, 70001, 170001, 1, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121001, 121001, 21001, 1, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170002, 5.8, 0.0, 0.0)
    ops.node(121002, 5.8, 0.0, 3.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2, 170002, 121002, 0.1925, 29572314.77056647, 12321797.82106936, 0.00475217, 0.00533786, 0.00216161, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20002, 153.02933383, 0.00106659, 185.08171865, 0.02636898, 18.50817186, 0.06929958, -153.02933383, -0.00106659, -185.08171865, -0.02636898, -18.50817186, -0.06929958, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10002, 198.67972555, 0.00076833, 240.29370151, 0.03017704, 24.02937015, 0.09151072, -198.67972555, -0.00076833, -240.29370151, -0.03017704, -24.02937015, -0.09151072, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20002, 2, 0.0, 212.5038652, 0.02133186, 212.5038652, 0.06399558, 148.75270564, -2151.83782405, 0.05, 2, 0, 70002, 21002, 2, 3)
    ops.uniaxialMaterial('LimitState', 40002, 53.1259663, 9.81e-05, 159.3778989, 0.0002943, 531.25966299, 0.00098102, -53.1259663, -9.81e-05, -159.3778989, -0.0002943, -531.25966299, -0.00098102, 0.4, 0.3, 0.003, 0.0, 0.0, 20002, 2)
    ops.limitCurve('ThreePoint', 10002, 2, 0.0, 260.0340569, 0.01536666, 260.0340569, 0.04609997, 182.02383983, -3743.32284546, 0.05, 2, 0, 70002, 21002, 1, 3)
    ops.uniaxialMaterial('LimitState', 30002, 65.00851422, 0.00012004, 195.02554267, 0.00036013, 650.08514224, 0.00120044, -65.00851422, -0.00012004, -195.02554267, -0.00036013, -650.08514224, -0.00120044, 0.4, 0.3, 0.003, 0.0, 0.0, 10002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2, 99999, 'P', 40002, 'Vy', 30002, 'Vz', 20002, 'My', 10002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170002, 70002, 170002, 2, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121002, 121002, 21002, 2, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170003, 11.6, 0.0, 0.0)
    ops.node(121003, 11.6, 0.0, 3.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3, 170003, 121003, 0.1925, 29066308.54822284, 12110961.89509285, 0.00475217, 0.00533786, 0.00216161, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20003, 155.27263154, 0.00108435, 187.97478821, 0.0266781, 18.79747882, 0.06902942, -155.27263154, -0.00108435, -187.97478821, -0.0266781, -18.79747882, -0.06902942, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10003, 200.76086128, 0.00078063, 243.04334902, 0.03052798, 24.3043349, 0.09103406, -200.76086128, -0.00078063, -243.04334902, -0.03052798, -24.3043349, -0.09103406, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20003, 3, 0.0, 216.92277791, 0.02168709, 216.92277791, 0.06506127, 151.84594453, -2369.132457, 0.05, 2, 0, 70003, 21003, 2, 3)
    ops.uniaxialMaterial('LimitState', 40003, 54.23069448, 0.00010188, 162.69208343, 0.00030565, 542.30694477, 0.00101885, -54.23069448, -0.00010188, -162.69208343, -0.00030565, -542.30694477, -0.00101885, 0.4, 0.3, 0.003, 0.0, 0.0, 20003, 2)
    ops.limitCurve('ThreePoint', 10003, 3, 0.0, 268.64926713, 0.01561265, 268.64926713, 0.04683795, 188.05448699, -4195.76398462, 0.05, 2, 0, 70003, 21003, 1, 3)
    ops.uniaxialMaterial('LimitState', 30003, 67.16231678, 0.00012618, 201.48695035, 0.00037854, 671.62316782, 0.0012618, -67.16231678, -0.00012618, -201.48695035, -0.00037854, -671.62316782, -0.0012618, 0.4, 0.3, 0.003, 0.0, 0.0, 10003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3, 99999, 'P', 40003, 'Vy', 30003, 'Vz', 20003, 'My', 10003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170003, 70003, 170003, 3, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121003, 121003, 21003, 3, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170006, 26.0, 0.0, 0.0)
    ops.node(121006, 26.0, 0.0, 3.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 6, 170006, 121006, 0.1925, 28999916.03559846, 12083298.34816602, 0.00475217, 0.00533786, 0.00216161, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20006, 155.43586737, 0.00111057, 188.19477004, 0.0261644, 18.819477, 0.06843705, -155.43586737, -0.00111057, -188.19477004, -0.0261644, -18.819477, -0.06843705, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10006, 202.07696977, 0.00079422, 244.66572292, 0.02991404, 24.46657229, 0.09030772, -202.07696977, -0.00079422, -244.66572292, -0.02991404, -24.46657229, -0.09030772, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20006, 6, 0.0, 211.60838001, 0.02221136, 211.60838001, 0.06663409, 148.12586601, -2222.01788708, 0.05, 2, 0, 70006, 21006, 2, 3)
    ops.uniaxialMaterial('LimitState', 40006, 52.902095, 9.962e-05, 158.70628501, 0.00029885, 529.02095003, 0.00099616, -52.902095, -9.962e-05, -158.70628501, -0.00029885, -529.02095003, -0.00099616, 0.4, 0.3, 0.003, 0.0, 0.0, 20006, 2)
    ops.limitCurve('ThreePoint', 10006, 6, 0.0, 260.51610812, 0.01588438, 260.51610812, 0.04765313, 182.36127568, -3889.00246773, 0.05, 2, 0, 70006, 21006, 1, 3)
    ops.uniaxialMaterial('LimitState', 30006, 65.12902703, 0.00012264, 195.38708109, 0.00036792, 651.2902703, 0.0012264, -65.12902703, -0.00012264, -195.38708109, -0.00036792, -651.2902703, -0.0012264, 0.4, 0.3, 0.003, 0.0, 0.0, 10006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 6, 99999, 'P', 40006, 'Vy', 30006, 'Vz', 20006, 'My', 10006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170006, 70006, 170006, 6, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121006, 121006, 21006, 6, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170007, 31.8, 0.0, 0.0)
    ops.node(121007, 31.8, 0.0, 3.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 7, 170007, 121007, 0.1925, 28588677.97429515, 11911949.15595631, 0.00475217, 0.00533786, 0.00216161, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20007, 147.53583848, 0.00110485, 178.75496935, 0.02917479, 17.87549693, 0.07094575, -147.53583848, -0.00110485, -178.75496935, -0.02917479, -17.87549693, -0.07094575, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10007, 195.12524624, 0.00078242, 236.41447237, 0.03340783, 23.64144724, 0.09308476, -195.12524624, -0.00078242, -236.41447237, -0.03340783, -23.64144724, -0.09308476, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20007, 7, 0.0, 222.0839585, 0.02209703, 222.0839585, 0.06629109, 155.45877095, -2614.40084792, 0.05, 2, 0, 70007, 21007, 2, 3)
    ops.uniaxialMaterial('LimitState', 40007, 55.52098963, 0.00010605, 166.56296888, 0.00031816, 555.20989625, 0.00106052, -55.52098963, -0.00010605, -166.56296888, -0.00031816, -555.20989625, -0.00106052, 0.4, 0.3, 0.003, 0.0, 0.0, 20007, 2)
    ops.limitCurve('ThreePoint', 10007, 7, 0.0, 278.3218556, 0.01564835, 278.3218556, 0.04694505, 194.82529892, -4710.96463081, 0.05, 2, 0, 70007, 21007, 1, 3)
    ops.uniaxialMaterial('LimitState', 30007, 69.5804639, 0.00013291, 208.7413917, 0.00039872, 695.804639, 0.00132907, -69.5804639, -0.00013291, -208.7413917, -0.00039872, -695.804639, -0.00132907, 0.4, 0.3, 0.003, 0.0, 0.0, 10007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 7, 99999, 'P', 40007, 'Vy', 30007, 'Vz', 20007, 'My', 10007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170007, 70007, 170007, 7, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121007, 121007, 21007, 7, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170008, 37.6, 0.0, 0.0)
    ops.node(121008, 37.6, 0.0, 3.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 8, 170008, 121008, 0.0875, 27933934.44590719, 11639139.35246133, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20008, 48.50621556, 0.00171933, 58.68674777, 0.01523449, 5.86867478, 0.05169116, -48.50621556, -0.00171933, -58.68674777, -0.01523449, -5.86867478, -0.05169116, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10008, 66.02993978, 0.00120741, 79.88836846, 0.01627858, 7.98883685, 0.063489, -66.02993978, -0.00120741, -79.88836846, -0.01627858, -7.98883685, -0.063489, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20008, 8, 0.0, 83.29572114, 0.03438662, 83.29572114, 0.10315987, 58.3070048, -852.01439296, 0.05, 2, 0, 70008, 21008, 2, 3)
    ops.uniaxialMaterial('LimitState', 40008, 20.82393029, 8.956e-05, 62.47179086, 0.00026868, 208.23930286, 0.00089559, -20.82393029, -8.956e-05, -62.47179086, -0.00026868, -208.23930286, -0.00089559, 0.4, 0.3, 0.003, 0.0, 0.0, 20008, 2)
    ops.limitCurve('ThreePoint', 10008, 8, 0.0, 104.03626635, 0.02414821, 104.03626635, 0.07244462, 72.82538645, -1201.51631905, 0.05, 2, 0, 70008, 21008, 1, 3)
    ops.uniaxialMaterial('LimitState', 30008, 26.00906659, 0.00011186, 78.02719976, 0.00033558, 260.09066588, 0.00111859, -26.00906659, -0.00011186, -78.02719976, -0.00033558, -260.09066588, -0.00111859, 0.4, 0.3, 0.003, 0.0, 0.0, 10008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 8, 99999, 'P', 40008, 'Vy', 30008, 'Vz', 20008, 'My', 10008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170008, 70008, 170008, 8, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121008, 121008, 21008, 8, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170009, 0.0, 4.75, 0.0)
    ops.node(121009, 0.0, 4.75, 3.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 9, 170009, 121009, 0.1925, 29891199.07830913, 12454666.28262881, 0.00475217, 0.00216161, 0.00533786, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20009, 267.51829179, 0.00081636, 323.42959737, 0.0301013, 32.34295974, 0.07956713, -267.51829179, -0.00081636, -323.42959737, -0.0301013, -32.34295974, -0.07956713, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10009, 210.04107333, 0.00115772, 253.93964399, 0.02661978, 25.3939644, 0.06211735, -210.04107333, -0.00115772, -253.93964399, -0.02661978, -25.3939644, -0.06211735, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20009, 9, 0.0, 243.31342317, 0.01632725, 243.31342317, 0.04898175, 170.31939622, -3135.25254296, 0.05, 2, 0, 70009, 21009, 2, 3)
    ops.uniaxialMaterial('LimitState', 40009, 60.82835579, 0.00011113, 182.48506737, 0.00033338, 608.28355791, 0.00111126, -60.82835579, -0.00011113, -182.48506737, -0.00033338, -608.28355791, -0.00111126, 0.4, 0.3, 0.003, 0.0, 0.0, 20009, 2)
    ops.limitCurve('ThreePoint', 10009, 9, 0.0, 202.18217321, 0.02315449, 202.18217321, 0.06946347, 141.52752125, -1844.35782075, 0.05, 2, 0, 70009, 21009, 1, 3)
    ops.uniaxialMaterial('LimitState', 30009, 50.5455433, 9.234e-05, 151.63662991, 0.00027702, 505.45543303, 0.00092341, -50.5455433, -9.234e-05, -151.63662991, -0.00027702, -505.45543303, -0.00092341, 0.4, 0.3, 0.003, 0.0, 0.0, 10009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 9, 99999, 'P', 40009, 'Vy', 30009, 'Vz', 20009, 'My', 10009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170009, 70009, 170009, 9, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121009, 121009, 21009, 9, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170010, 5.8, 4.75, 0.0)
    ops.node(121010, 5.8, 4.75, 3.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 10, 170010, 121010, 0.35, 28440848.95627252, 11850353.73178022, 0.01632638, 0.00802083, 0.01572083, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20010, 592.36550261, 0.00071853, 719.32306212, 0.04827599, 71.93230621, 0.11395732, -592.36550261, -0.00071853, -719.32306212, -0.04827599, -71.93230621, -0.11395732, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10010, 604.65457971, 0.00088005, 734.24597126, 0.04328722, 73.42459713, 0.0933322, -604.65457971, -0.00088005, -734.24597126, -0.04328722, -73.42459713, -0.0933322, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20010, 10, 0.0, 556.70851429, 0.01437057, 556.70851429, 0.0431117, 389.69596, -10429.08806631, 0.05, 2, 0, 70010, 21010, 2, 3)
    ops.uniaxialMaterial('LimitState', 40010, 139.17712857, 0.00014697, 417.53138571, 0.00044092, 1391.77128572, 0.00146975, -139.17712857, -0.00014697, -417.53138571, -0.00044092, -1391.77128572, -0.00146975, 0.4, 0.3, 0.003, 0.0, 0.0, 20010, 2)
    ops.limitCurve('ThreePoint', 10010, 10, 0.0, 423.81936201, 0.01760101, 423.81936201, 0.05280303, 296.67355341, -6380.77364436, 0.05, 2, 0, 70010, 21010, 1, 3)
    ops.uniaxialMaterial('LimitState', 30010, 105.9548405, 0.00011189, 317.86452151, 0.00033567, 1059.54840502, 0.00111891, -105.9548405, -0.00011189, -317.86452151, -0.00033567, -1059.54840502, -0.00111891, 0.4, 0.3, 0.003, 0.0, 0.0, 10010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 10, 99999, 'P', 40010, 'Vy', 30010, 'Vz', 20010, 'My', 10010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170010, 70010, 170010, 10, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121010, 121010, 21010, 10, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170011, 11.6, 4.75, 0.0)
    ops.node(121011, 11.6, 4.75, 3.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 11, 170011, 121011, 0.35, 28275730.93428167, 11781554.55595069, 0.01632638, 0.00802083, 0.01572083, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20011, 608.66868361, 0.00077754, 739.33785489, 0.04929852, 73.93378549, 0.11472098, -608.66868361, -0.00077754, -739.33785489, -0.04929852, -73.93378549, -0.11472098, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10011, 572.92719554, 0.00097137, 695.92337369, 0.04423771, 69.59233737, 0.09408544, -572.92719554, -0.00097137, -695.92337369, -0.04423771, -69.59233737, -0.09408544, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20011, 11, 0.0, 532.74163303, 0.01555085, 532.74163303, 0.04665254, 372.91914312, -9286.27808232, 0.05, 2, 0, 70011, 21011, 2, 3)
    ops.uniaxialMaterial('LimitState', 40011, 133.18540826, 0.00014147, 399.55622477, 0.00042441, 1331.85408258, 0.00141469, -133.18540826, -0.00014147, -399.55622477, -0.00042441, -1331.85408258, -0.00141469, 0.4, 0.3, 0.003, 0.0, 0.0, 20011, 2)
    ops.limitCurve('ThreePoint', 10011, 11, 0.0, 406.49289386, 0.01942737, 406.49289386, 0.05828211, 284.5450257, -5740.66780595, 0.05, 2, 0, 70011, 21011, 1, 3)
    ops.uniaxialMaterial('LimitState', 30011, 101.62322347, 0.00010794, 304.8696704, 0.00032383, 1016.23223466, 0.00107943, -101.62322347, -0.00010794, -304.8696704, -0.00032383, -1016.23223466, -0.00107943, 0.4, 0.3, 0.003, 0.0, 0.0, 10011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 11, 99999, 'P', 40011, 'Vy', 30011, 'Vz', 20011, 'My', 10011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170011, 70011, 170011, 11, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121011, 121011, 21011, 11, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170012, 17.4, 4.75, 0.0)
    ops.node(121012, 17.4, 4.75, 3.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 12, 170012, 121012, 0.24, 29899976.45938116, 12458323.52474215, 0.00751249, 0.00352, 0.00792, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20012, 416.63005536, 0.00083516, 503.75318483, 0.04854819, 50.37531848, 0.12733453, -416.63005536, -0.00083516, -503.75318483, -0.04854819, -50.37531848, -0.12733453, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10012, 368.98121544, 0.0011363, 446.14031088, 0.04248354, 44.61403109, 0.0985792, -368.98121544, -0.0011363, -446.14031088, -0.04248354, -44.61403109, -0.0985792, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20012, 12, 0.0, 382.24992585, 0.01670311, 382.24992585, 0.05010933, 267.5749481, -6884.01438189, 0.05, 2, 0, 70012, 21012, 2, 3)
    ops.uniaxialMaterial('LimitState', 40012, 95.56248146, 0.00013999, 286.68744439, 0.00041996, 955.62481463, 0.00139988, -95.56248146, -0.00013999, -286.68744439, -0.00041996, -955.62481463, -0.00139988, 0.4, 0.3, 0.003, 0.0, 0.0, 20012, 2)
    ops.limitCurve('ThreePoint', 10012, 12, 0.0, 303.17837379, 0.02272607, 303.17837379, 0.0681782, 212.22486165, -3936.29454246, 0.05, 2, 0, 70012, 21012, 1, 3)
    ops.uniaxialMaterial('LimitState', 30012, 75.79459345, 0.00011103, 227.38378034, 0.00033309, 757.94593448, 0.0011103, -75.79459345, -0.00011103, -227.38378034, -0.00033309, -757.94593448, -0.0011103, 0.4, 0.3, 0.003, 0.0, 0.0, 10012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 12, 99999, 'P', 40012, 'Vy', 30012, 'Vz', 20012, 'My', 10012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170012, 70012, 170012, 12, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121012, 121012, 21012, 12, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170013, 20.2, 4.75, 0.0)
    ops.node(121013, 20.2, 4.75, 3.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 13, 170013, 121013, 0.24, 29480732.14386581, 12283638.39327742, 0.00751249, 0.00352, 0.00792, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20013, 427.00642269, 0.00084154, 516.74720968, 0.04749264, 51.67472097, 0.12548723, -427.00642269, -0.00084154, -516.74720968, -0.04749264, -51.67472097, -0.12548723, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10013, 387.28524073, 0.00113351, 468.6781202, 0.0415605, 46.86781202, 0.09709243, -387.28524073, -0.00113351, -468.6781202, -0.0415605, -46.86781202, -0.09709243, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20013, 13, 0.0, 373.31348568, 0.01683081, 373.31348568, 0.05049244, 261.31943998, -6613.79922384, 0.05, 2, 0, 70013, 21013, 2, 3)
    ops.uniaxialMaterial('LimitState', 40013, 93.32837142, 0.00013866, 279.98511426, 0.00041598, 933.2837142, 0.00138659, -93.32837142, -0.00013866, -279.98511426, -0.00041598, -933.2837142, -0.00138659, 0.4, 0.3, 0.003, 0.0, 0.0, 20013, 2)
    ops.limitCurve('ThreePoint', 10013, 13, 0.0, 296.31437544, 0.02267025, 296.31437544, 0.06801076, 207.42006281, -3799.91297516, 0.05, 2, 0, 70013, 21013, 1, 3)
    ops.uniaxialMaterial('LimitState', 30013, 74.07859386, 0.00011006, 222.23578158, 0.00033018, 740.78593861, 0.0011006, -74.07859386, -0.00011006, -222.23578158, -0.00033018, -740.78593861, -0.0011006, 0.4, 0.3, 0.003, 0.0, 0.0, 10013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 13, 99999, 'P', 40013, 'Vy', 30013, 'Vz', 20013, 'My', 10013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170013, 70013, 170013, 13, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121013, 121013, 21013, 13, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170014, 26.0, 4.75, 0.0)
    ops.node(121014, 26.0, 4.75, 3.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 14, 170014, 121014, 0.35, 27468781.31711004, 11445325.54879585, 0.01632638, 0.00802083, 0.01572083, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20014, 606.74239321, 0.00077922, 737.9601036, 0.04762864, 73.79601036, 0.11170326, -606.74239321, -0.00077922, -737.9601036, -0.04762864, -73.79601036, -0.11170326, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10014, 575.75994342, 0.00097145, 700.27720537, 0.04274726, 70.02772054, 0.09156802, -575.75994342, -0.00097145, -700.27720537, -0.04274726, -70.02772054, -0.09156802, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20014, 14, 0.0, 493.38310891, 0.01558432, 493.38310891, 0.04675295, 345.36817623, -7857.57562758, 0.05, 2, 0, 70014, 21014, 2, 3)
    ops.uniaxialMaterial('LimitState', 40014, 123.34577723, 0.00013487, 370.03733168, 0.0004046, 1233.45777226, 0.00134866, -123.34577723, -0.00013487, -370.03733168, -0.0004046, -1233.45777226, -0.00134866, 0.4, 0.3, 0.003, 0.0, 0.0, 20014, 2)
    ops.limitCurve('ThreePoint', 10014, 14, 0.0, 377.37716147, 0.01942892, 377.37716147, 0.05828676, 264.16401303, -4935.23344458, 0.05, 2, 0, 70014, 21014, 1, 3)
    ops.uniaxialMaterial('LimitState', 30014, 94.34429037, 0.00010316, 283.0328711, 0.00030947, 943.44290366, 0.00103156, -94.34429037, -0.00010316, -283.0328711, -0.00030947, -943.44290366, -0.00103156, 0.4, 0.3, 0.003, 0.0, 0.0, 10014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 14, 99999, 'P', 40014, 'Vy', 30014, 'Vz', 20014, 'My', 10014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170014, 70014, 170014, 14, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121014, 121014, 21014, 14, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170015, 31.8, 4.75, 0.0)
    ops.node(121015, 31.8, 4.75, 3.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 15, 170015, 121015, 0.35, 29411701.51323947, 12254875.63051645, 0.01632638, 0.00802083, 0.01572083, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20015, 601.54930254, 0.00073327, 729.07963562, 0.04686641, 72.90796356, 0.11396379, -601.54930254, -0.00073327, -729.07963562, -0.04686641, -72.90796356, -0.11396379, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10015, 601.72684863, 0.00090619, 729.29482203, 0.04204328, 72.9294822, 0.0931672, -601.72684863, -0.00090619, -729.29482203, -0.04204328, -72.9294822, -0.0931672, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20015, 15, 0.0, 539.34825414, 0.01466536, 539.34825414, 0.04399609, 377.5437779, -8898.54078334, 0.05, 2, 0, 70015, 21015, 2, 3)
    ops.uniaxialMaterial('LimitState', 40015, 134.83706353, 0.00013769, 404.5111906, 0.00041307, 1348.37063535, 0.00137691, -134.83706353, -0.00013769, -404.5111906, -0.00041307, -1348.37063535, -0.00137691, 0.4, 0.3, 0.003, 0.0, 0.0, 20015, 2)
    ops.limitCurve('ThreePoint', 10015, 15, 0.0, 412.6524828, 0.01812379, 412.6524828, 0.05437137, 288.85673796, -5522.69940994, 0.05, 2, 0, 70015, 21015, 1, 3)
    ops.uniaxialMaterial('LimitState', 30015, 103.1631207, 0.00010535, 309.4893621, 0.00031604, 1031.631207, 0.00105347, -103.1631207, -0.00010535, -309.4893621, -0.00031604, -1031.631207, -0.00105347, 0.4, 0.3, 0.003, 0.0, 0.0, 10015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 15, 99999, 'P', 40015, 'Vy', 30015, 'Vz', 20015, 'My', 10015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170015, 70015, 170015, 15, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121015, 121015, 21015, 15, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170016, 37.6, 4.75, 0.0)
    ops.node(121016, 37.6, 4.75, 3.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 16, 170016, 121016, 0.1925, 27811112.37580542, 11587963.48991892, 0.00475217, 0.00216161, 0.00533786, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20016, 265.33687129, 0.0008361, 321.96712495, 0.02750538, 32.1967125, 0.07418701, -265.33687129, -0.0008361, -321.96712495, -0.02750538, -32.1967125, -0.07418701, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10016, 209.07990804, 0.00119089, 253.70336414, 0.02437874, 25.37033641, 0.05787832, -209.07990804, -0.00119089, -253.70336414, -0.02437874, -25.37033641, -0.05787832, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20016, 16, 0.0, 216.03008713, 0.01672196, 216.03008713, 0.05016588, 151.22106099, -2612.17832934, 0.05, 2, 0, 70016, 21016, 2, 3)
    ops.uniaxialMaterial('LimitState', 40016, 54.00752178, 0.00010605, 162.02256535, 0.00031814, 540.07521782, 0.00106045, -54.00752178, -0.00010605, -162.02256535, -0.00031814, -540.07521782, -0.00106045, 0.4, 0.3, 0.003, 0.0, 0.0, 20016, 2)
    ops.limitCurve('ThreePoint', 10016, 16, 0.0, 180.49744138, 0.02381787, 180.49744138, 0.07145362, 126.34820897, -1587.0727366, 0.05, 2, 0, 70016, 21016, 1, 3)
    ops.uniaxialMaterial('LimitState', 30016, 45.12436035, 8.86e-05, 135.37308104, 0.00026581, 451.24360346, 0.00088603, -45.12436035, -8.86e-05, -135.37308104, -0.00026581, -451.24360346, -0.00088603, 0.4, 0.3, 0.003, 0.0, 0.0, 10016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 16, 99999, 'P', 40016, 'Vy', 30016, 'Vz', 20016, 'My', 10016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170016, 70016, 170016, 16, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121016, 121016, 21016, 16, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170017, 0.0, 9.5, 0.0)
    ops.node(121017, 0.0, 9.5, 3.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 17, 170017, 121017, 0.0875, 30777085.77421134, 12823785.73925472, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20017, 50.18427804, 0.00151603, 60.42997841, 0.01912782, 6.04299784, 0.0592749, -50.18427804, -0.00151603, -60.42997841, -0.01912782, -6.04299784, -0.0592749, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10017, 67.43738353, 0.0011012, 81.20550478, 0.02074065, 8.12055048, 0.07273005, -67.43738353, -0.0011012, -81.20550478, -0.02074065, -8.12055048, -0.07273005, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20017, 17, 0.0, 106.65391896, 0.03032057, 106.65391896, 0.09096171, 74.65774327, -1064.10004393, 0.05, 2, 0, 70017, 21017, 2, 3)
    ops.uniaxialMaterial('LimitState', 40017, 26.66347974, 0.00010408, 79.99043922, 0.00031224, 266.63479739, 0.0010408, -26.66347974, -0.00010408, -79.99043922, -0.00031224, -266.63479739, -0.0010408, 0.4, 0.3, 0.003, 0.0, 0.0, 20017, 2)
    ops.limitCurve('ThreePoint', 10017, 17, 0.0, 123.29161604, 0.022024, 123.29161604, 0.06607199, 86.30413123, -1557.61729007, 0.05, 2, 0, 70017, 21017, 1, 3)
    ops.uniaxialMaterial('LimitState', 30017, 30.82290401, 0.00012032, 92.46871203, 0.00036095, 308.22904011, 0.00120316, -30.82290401, -0.00012032, -92.46871203, -0.00036095, -308.22904011, -0.00120316, 0.4, 0.3, 0.003, 0.0, 0.0, 10017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 17, 99999, 'P', 40017, 'Vy', 30017, 'Vz', 20017, 'My', 10017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170017, 70017, 170017, 17, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121017, 121017, 21017, 17, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170018, 5.8, 9.5, 0.0)
    ops.node(121018, 5.8, 9.5, 3.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 18, 170018, 121018, 0.1925, 31267157.87698254, 13027982.44874272, 0.00475217, 0.00533786, 0.00216161, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20018, 168.05129459, 0.00104918, 202.46787951, 0.02844697, 20.24678795, 0.07308018, -168.05129459, -0.00104918, -202.46787951, -0.02844697, -20.24678795, -0.07308018, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10018, 212.73710462, 0.00075858, 256.30525829, 0.03260277, 25.63052583, 0.09636891, -212.73710462, -0.00075858, -256.30525829, -0.03260277, -25.63052583, -0.09636891, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20018, 18, 0.0, 236.20262547, 0.02098354, 236.20262547, 0.06295061, 165.34183783, -2565.36051522, 0.05, 2, 0, 70018, 21018, 2, 3)
    ops.uniaxialMaterial('LimitState', 40018, 59.05065637, 0.00010313, 177.1519691, 0.00030939, 590.50656368, 0.00103131, -59.05065637, -0.00010313, -177.1519691, -0.00030939, -590.50656368, -0.00103131, 0.4, 0.3, 0.003, 0.0, 0.0, 20018, 2)
    ops.limitCurve('ThreePoint', 10018, 18, 0.0, 291.55599581, 0.01517166, 291.55599581, 0.04551499, 204.08919706, -4607.60143982, 0.05, 2, 0, 70018, 21018, 1, 3)
    ops.uniaxialMaterial('LimitState', 30018, 72.88899895, 0.0001273, 218.66699685, 0.0003819, 728.88998951, 0.001273, -72.88899895, -0.0001273, -218.66699685, -0.0003819, -728.88998951, -0.001273, 0.4, 0.3, 0.003, 0.0, 0.0, 10018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 18, 99999, 'P', 40018, 'Vy', 30018, 'Vz', 20018, 'My', 10018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170018, 70018, 170018, 18, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121018, 121018, 21018, 18, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170019, 11.6, 9.5, 0.0)
    ops.node(121019, 11.6, 9.5, 3.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 19, 170019, 121019, 0.1925, 29326258.13271105, 12219274.22196294, 0.00475217, 0.00533786, 0.00216161, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20019, 168.82941183, 0.00110846, 204.28858364, 0.02827333, 20.42885836, 0.07092667, -168.82941183, -0.00110846, -204.28858364, -0.02827333, -20.42885836, -0.07092667, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10019, 214.42990003, 0.00079217, 259.46652359, 0.03236562, 25.94665236, 0.09330319, -214.42990003, -0.00079217, -259.46652359, -0.03236562, -25.94665236, -0.09330319, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20019, 19, 0.0, 218.73450239, 0.02216921, 218.73450239, 0.06650764, 153.11415167, -2378.62389372, 0.05, 2, 0, 70019, 21019, 2, 3)
    ops.uniaxialMaterial('LimitState', 40019, 54.6836256, 0.00010183, 164.05087679, 0.00030548, 546.83625597, 0.00101825, -54.6836256, -0.00010183, -164.05087679, -0.00030548, -546.83625597, -0.00101825, 0.4, 0.3, 0.003, 0.0, 0.0, 20019, 2)
    ops.limitCurve('ThreePoint', 10019, 19, 0.0, 270.63980315, 0.01584336, 270.63980315, 0.04753008, 189.44786221, -4215.61651843, 0.05, 2, 0, 70019, 21019, 1, 3)
    ops.uniaxialMaterial('LimitState', 30019, 67.65995079, 0.00012599, 202.97985236, 0.00037796, 676.59950788, 0.00125988, -67.65995079, -0.00012599, -202.97985236, -0.00037796, -676.59950788, -0.00125988, 0.4, 0.3, 0.003, 0.0, 0.0, 10019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 19, 99999, 'P', 40019, 'Vy', 30019, 'Vz', 20019, 'My', 10019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170019, 70019, 170019, 19, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121019, 121019, 21019, 19, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170020, 17.4, 9.5, 0.0)
    ops.node(121020, 17.4, 9.5, 3.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 20, 170020, 121020, 0.12, 31207483.07457853, 13003117.94774106, 0.00194385, 0.00176, 0.00099, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20020, 83.01904549, 0.00122194, 99.91630003, 0.01495315, 9.99163, 0.05234555, -83.01904549, -0.00122194, -99.91630003, -0.01495315, -9.99163, -0.05234555, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10020, 99.25508586, 0.00096175, 119.45693761, 0.01597732, 11.94569376, 0.06220464, -99.25508586, -0.00096175, -119.45693761, -0.01597732, -11.94569376, -0.06220464, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20020, 20, 0.0, 131.86315441, 0.02443884, 131.86315441, 0.07331651, 92.30420809, -1081.80867425, 0.05, 2, 0, 70020, 21020, 2, 3)
    ops.uniaxialMaterial('LimitState', 40020, 32.9657886, 9.254e-05, 98.89736581, 0.00027761, 329.65788602, 0.00092536, -32.9657886, -9.254e-05, -98.89736581, -0.00027761, -329.65788602, -0.00092536, 0.4, 0.3, 0.003, 0.0, 0.0, 20020, 2)
    ops.limitCurve('ThreePoint', 10020, 20, 0.0, 145.91972733, 0.01923504, 145.91972733, 0.05770512, 102.14380913, -1442.31024763, 0.05, 2, 0, 70020, 21020, 1, 3)
    ops.uniaxialMaterial('LimitState', 30020, 36.47993183, 0.0001024, 109.4397955, 0.0003072, 364.79931833, 0.001024, -36.47993183, -0.0001024, -109.4397955, -0.0003072, -364.79931833, -0.001024, 0.4, 0.3, 0.003, 0.0, 0.0, 10020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 20, 99999, 'P', 40020, 'Vy', 30020, 'Vz', 20020, 'My', 10020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170020, 70020, 170020, 20, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121020, 121020, 21020, 20, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170021, 20.2, 9.5, 0.0)
    ops.node(121021, 20.2, 9.5, 3.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 21, 170021, 121021, 0.12, 26974783.30074484, 11239493.04197701, 0.00194385, 0.00176, 0.00099, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20021, 83.87657991, 0.0012998, 101.6437069, 0.01515579, 10.16437069, 0.04758686, -83.87657991, -0.0012998, -101.6437069, -0.01515579, -10.16437069, -0.04758686, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10021, 99.51756166, 0.00102041, 120.5978341, 0.01617243, 12.05978341, 0.05626617, -99.51756166, -0.00102041, -120.5978341, -0.01617243, -12.05978341, -0.05626617, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20021, 21, 0.0, 118.29620835, 0.02599598, 118.29620835, 0.07798794, 82.80734584, -1124.39404079, 0.05, 2, 0, 70021, 21021, 2, 3)
    ops.uniaxialMaterial('LimitState', 40021, 29.57405209, 9.604e-05, 88.72215626, 0.00028812, 295.74052086, 0.00096041, -29.57405209, -9.604e-05, -88.72215626, -0.00028812, -295.74052086, -0.00096041, 0.4, 0.3, 0.003, 0.0, 0.0, 20021, 2)
    ops.limitCurve('ThreePoint', 10021, 21, 0.0, 132.94331936, 0.02040812, 132.94331936, 0.06122436, 93.06032356, -1507.97032871, 0.05, 2, 0, 70021, 21021, 1, 3)
    ops.uniaxialMaterial('LimitState', 30021, 33.23582984, 0.00010793, 99.70748952, 0.0003238, 332.35829841, 0.00107933, -33.23582984, -0.00010793, -99.70748952, -0.0003238, -332.35829841, -0.00107933, 0.4, 0.3, 0.003, 0.0, 0.0, 10021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 21, 99999, 'P', 40021, 'Vy', 30021, 'Vz', 20021, 'My', 10021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170021, 70021, 170021, 21, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121021, 121021, 21021, 21, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170022, 26.0, 9.5, 0.0)
    ops.node(121022, 26.0, 9.5, 3.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 22, 170022, 121022, 0.1925, 29374857.33694636, 12239523.89039432, 0.00475217, 0.00533786, 0.00216161, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20022, 169.85864899, 0.00107561, 205.51497733, 0.0285921, 20.55149773, 0.07130086, -169.85864899, -0.00107561, -205.51497733, -0.0285921, -20.55149773, -0.07130086, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10022, 213.44245889, 0.00077641, 258.24779815, 0.03275856, 25.82477982, 0.0937753, -213.44245889, -0.00077641, -258.24779815, -0.03275856, -25.82477982, -0.0937753, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20022, 22, 0.0, 229.34020323, 0.02151214, 229.34020323, 0.06453642, 160.53814226, -2702.43008322, 0.05, 2, 0, 70022, 21022, 2, 3)
    ops.uniaxialMaterial('LimitState', 40022, 57.33505081, 0.00010659, 172.00515242, 0.00031976, 573.35050807, 0.00106586, -57.33505081, -0.00010659, -172.00515242, -0.00031976, -573.35050807, -0.00106586, 0.4, 0.3, 0.003, 0.0, 0.0, 20022, 2)
    ops.limitCurve('ThreePoint', 10022, 22, 0.0, 287.14529508, 0.01552819, 287.14529508, 0.04658458, 201.00170656, -4896.91777823, 0.05, 2, 0, 70022, 21022, 1, 3)
    ops.uniaxialMaterial('LimitState', 30022, 71.78632377, 0.00013345, 215.35897131, 0.00040035, 717.8632377, 0.00133451, -71.78632377, -0.00013345, -215.35897131, -0.00040035, -717.8632377, -0.00133451, 0.4, 0.3, 0.003, 0.0, 0.0, 10022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 22, 99999, 'P', 40022, 'Vy', 30022, 'Vz', 20022, 'My', 10022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170022, 70022, 170022, 22, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121022, 121022, 21022, 22, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170023, 31.8, 9.5, 0.0)
    ops.node(121023, 31.8, 9.5, 3.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 23, 170023, 121023, 0.1925, 26806364.07744209, 11169318.36560087, 0.00475217, 0.00533786, 0.00216161, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20023, 176.40812553, 0.00119896, 214.22878318, 0.02551798, 21.42287832, 0.06479899, -176.40812553, -0.00119896, -214.22878318, -0.02551798, -21.42287832, -0.06479899, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10023, 221.43002068, 0.00085038, 268.90305506, 0.02911614, 26.89030551, 0.08523576, -221.43002068, -0.00085038, -268.90305506, -0.02911614, -26.89030551, -0.08523576, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20023, 23, 0.0, 197.08422668, 0.02397925, 197.08422668, 0.07193775, 137.95895868, -2157.89536307, 0.05, 2, 0, 70023, 21023, 2, 3)
    ops.uniaxialMaterial('LimitState', 40023, 49.27105667, 0.00010037, 147.81317001, 0.00030111, 492.7105667, 0.00100371, -49.27105667, -0.00010037, -147.81317001, -0.00030111, -492.7105667, -0.00100371, 0.4, 0.3, 0.003, 0.0, 0.0, 20023, 2)
    ops.limitCurve('ThreePoint', 10023, 23, 0.0, 244.73419684, 0.01700768, 244.73419684, 0.05102304, 171.31393779, -3755.87947737, 0.05, 2, 0, 70023, 21023, 1, 3)
    ops.uniaxialMaterial('LimitState', 30023, 61.18354921, 0.00012464, 183.55064763, 0.00037391, 611.83549209, 0.00124638, -61.18354921, -0.00012464, -183.55064763, -0.00037391, -611.83549209, -0.00124638, 0.4, 0.3, 0.003, 0.0, 0.0, 10023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 23, 99999, 'P', 40023, 'Vy', 30023, 'Vz', 20023, 'My', 10023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170023, 70023, 170023, 23, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121023, 121023, 21023, 23, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170024, 37.6, 9.5, 0.0)
    ops.node(121024, 37.6, 9.5, 3.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 24, 170024, 121024, 0.0875, 29034381.50609666, 12097658.96087361, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20024, 52.7317446, 0.00160263, 63.70619973, 0.0155566, 6.37061997, 0.05358486, -52.7317446, -0.00160263, -63.70619973, -0.0155566, -6.37061997, -0.05358486, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10024, 70.3447671, 0.00116883, 84.98481924, 0.01672932, 8.49848192, 0.06597491, -70.3447671, -0.00116883, -84.98481924, -0.01672932, -8.49848192, -0.06597491, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20024, 24, 0.0, 92.17118655, 0.03205259, 92.17118655, 0.09615776, 64.51983058, -876.05363472, 0.05, 2, 0, 70024, 21024, 2, 3)
    ops.uniaxialMaterial('LimitState', 40024, 23.04279664, 9.535e-05, 69.12838991, 0.00028604, 230.42796637, 0.00095345, -23.04279664, -9.535e-05, -69.12838991, -0.00028604, -230.42796637, -0.00095345, 0.4, 0.3, 0.003, 0.0, 0.0, 20024, 2)
    ops.limitCurve('ThreePoint', 10024, 24, 0.0, 108.31399832, 0.02337655, 108.31399832, 0.07012964, 75.81979882, -1241.53201304, 0.05, 2, 0, 70024, 21024, 1, 3)
    ops.uniaxialMaterial('LimitState', 30024, 27.07849958, 0.00011204, 81.23549874, 0.00033613, 270.7849958, 0.00112044, -27.07849958, -0.00011204, -81.23549874, -0.00033613, -270.7849958, -0.00112044, 0.4, 0.3, 0.003, 0.0, 0.0, 10024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 24, 99999, 'P', 40024, 'Vy', 30024, 'Vz', 20024, 'My', 10024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170024, 70024, 170024, 24, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121024, 121024, 21024, 24, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171001, 0.0, 0.0, 3.95)
    ops.node(122001, 0.0, 0.0, 6.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1001, 171001, 122001, 0.0875, 27146703.3221064, 11311126.384211, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21001, 73.43301241, 0.00144513, 89.23728575, 0.02623486, 8.92372857, 0.07275104, -73.43301241, -0.00144513, -89.23728575, -0.02623486, -8.92372857, -0.07275104, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11001, 85.33835908, 0.00105511, 103.70490443, 0.02885552, 10.37049044, 0.08990549, -85.33835908, -0.00105511, -103.70490443, -0.02885552, -10.37049044, -0.08990549, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21001, 1001, 0.0, 102.62542276, 0.02890259, 102.62542276, 0.08670778, 71.83779593, -1888.16060948, 0.05, 2, 0, 71001, 22001, 2, 3)
    ops.uniaxialMaterial('LimitState', 41001, 25.65635569, 8.71e-05, 76.96906707, 0.0002613, 256.5635569, 0.000871, -25.65635569, -8.71e-05, -76.96906707, -0.0002613, -256.5635569, -0.000871, 0.4, 0.3, 0.003, 0.0, 0.0, 21001, 2)
    ops.limitCurve('ThreePoint', 11001, 1001, 0.0, 123.13103716, 0.02110217, 123.13103716, 0.06330651, 86.19172601, -3008.19490403, 0.05, 2, 0, 71001, 22001, 1, 3)
    ops.uniaxialMaterial('LimitState', 31001, 30.78275929, 0.0001045, 92.34827787, 0.00031351, 307.8275929, 0.00104504, -30.78275929, -0.0001045, -92.34827787, -0.00031351, -307.8275929, -0.00104504, 0.4, 0.3, 0.003, 0.0, 0.0, 11001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1001, 99999, 'P', 41001, 'Vy', 31001, 'Vz', 21001, 'My', 11001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171001, 71001, 171001, 1001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122001, 122001, 22001, 1001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171002, 5.8, 0.0, 3.95)
    ops.node(122002, 5.8, 0.0, 6.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1002, 171002, 122002, 0.1925, 27411289.06153249, 11421370.4423052, 0.00475217, 0.00533786, 0.00216161, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21002, 105.61008319, 0.00095674, 128.52831915, 0.01487362, 12.85283191, 0.04553517, -105.61008319, -0.00095674, -128.52831915, -0.01487362, -12.85283191, -0.04553517, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11002, 211.14927105, 0.00071576, 256.97035811, 0.01657673, 25.69703581, 0.05838867, -211.14927105, -0.00071576, -256.97035811, -0.01657673, -25.69703581, -0.05838867, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21002, 1002, 0.0, 159.52081635, 0.01913474, 159.52081635, 0.05740421, 111.66457145, -1662.04159282, 0.05, 2, 0, 71002, 22002, 2, 3)
    ops.uniaxialMaterial('LimitState', 41002, 39.88020409, 6.095e-05, 119.64061226, 0.00018284, 398.80204088, 0.00060946, -39.88020409, -6.095e-05, -119.64061226, -0.00018284, -398.80204088, -0.00060946, 0.4, 0.3, 0.003, 0.0, 0.0, 21002, 2)
    ops.limitCurve('ThreePoint', 11002, 1002, 0.0, 216.23048845, 0.01431517, 216.23048845, 0.04294552, 151.36134192, -2780.58298783, 0.05, 2, 0, 71002, 22002, 1, 3)
    ops.uniaxialMaterial('LimitState', 31002, 54.05762211, 8.261e-05, 162.17286634, 0.00024784, 540.57622113, 0.00082613, -54.05762211, -8.261e-05, -162.17286634, -0.00024784, -540.57622113, -0.00082613, 0.4, 0.3, 0.003, 0.0, 0.0, 11002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1002, 99999, 'P', 41002, 'Vy', 31002, 'Vz', 21002, 'My', 11002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171002, 71002, 171002, 1002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122002, 122002, 22002, 1002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171003, 11.6, 0.0, 3.95)
    ops.node(122003, 11.6, 0.0, 6.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1003, 171003, 122003, 0.1925, 29786223.56417813, 12410926.48507422, 0.00475217, 0.00533786, 0.00216161, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21003, 106.38588283, 0.00093461, 128.88570002, 0.01571931, 12.88857, 0.04799593, -106.38588283, -0.00093461, -128.88570002, -0.01571931, -12.88857, -0.04799593, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11003, 211.56714933, 0.00070125, 256.31201638, 0.01755128, 25.63120164, 0.06156562, -211.56714933, -0.00070125, -256.31201638, -0.01755128, -25.63120164, -0.06156562, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21003, 1003, 0.0, 176.46467417, 0.01869212, 176.46467417, 0.05607637, 123.52527192, -1787.85713924, 0.05, 2, 0, 71003, 22003, 2, 3)
    ops.uniaxialMaterial('LimitState', 41003, 44.11616854, 6.204e-05, 132.34850562, 0.00018613, 441.16168541, 0.00062044, -44.11616854, -6.204e-05, -132.34850562, -0.00018613, -441.16168541, -0.00062044, 0.4, 0.3, 0.003, 0.0, 0.0, 21003, 2)
    ops.limitCurve('ThreePoint', 11003, 1003, 0.0, 238.66669114, 0.01402507, 238.66669114, 0.04207522, 167.0666838, -3037.31213341, 0.05, 2, 0, 71003, 22003, 1, 3)
    ops.uniaxialMaterial('LimitState', 31003, 59.66667278, 8.391e-05, 179.00001835, 0.00025174, 596.66672785, 0.00083914, -59.66667278, -8.391e-05, -179.00001835, -0.00025174, -596.66672785, -0.00083914, 0.4, 0.3, 0.003, 0.0, 0.0, 11003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1003, 99999, 'P', 41003, 'Vy', 31003, 'Vz', 21003, 'My', 11003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171003, 71003, 171003, 1003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122003, 122003, 22003, 1003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171006, 26.0, 0.0, 3.95)
    ops.node(122006, 26.0, 0.0, 6.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1006, 171006, 122006, 0.1925, 28056698.06312323, 11690290.85963468, 0.00475217, 0.00533786, 0.00216161, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21006, 107.17452505, 0.00095777, 130.29510464, 0.01730782, 13.02951046, 0.04845887, -107.17452505, -0.00095777, -130.29510464, -0.01730782, -13.02951046, -0.04845887, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11006, 214.46430374, 0.00071778, 260.73032638, 0.01935182, 26.07303264, 0.06183126, -214.46430374, -0.00071778, -260.73032638, -0.01935182, -26.07303264, -0.06183126, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21006, 1006, 0.0, 171.61784296, 0.0191555, 171.61784296, 0.05746649, 120.13249007, -1966.90164102, 0.05, 2, 0, 71006, 22006, 2, 3)
    ops.uniaxialMaterial('LimitState', 41006, 42.90446074, 6.406e-05, 128.71338222, 0.00019218, 429.0446074, 0.0006406, -42.90446074, -6.406e-05, -128.71338222, -0.00019218, -429.0446074, -0.0006406, 0.4, 0.3, 0.003, 0.0, 0.0, 21006, 2)
    ops.limitCurve('ThreePoint', 11006, 1006, 0.0, 234.12242342, 0.01435566, 234.12242342, 0.04306699, 163.8856964, -3405.83057436, 0.05, 2, 0, 71006, 22006, 1, 3)
    ops.uniaxialMaterial('LimitState', 31006, 58.53060586, 8.739e-05, 175.59181757, 0.00026217, 585.30605856, 0.00087391, -58.53060586, -8.739e-05, -175.59181757, -0.00026217, -585.30605856, -0.00087391, 0.4, 0.3, 0.003, 0.0, 0.0, 11006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1006, 99999, 'P', 41006, 'Vy', 31006, 'Vz', 21006, 'My', 11006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171006, 71006, 171006, 1006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122006, 122006, 22006, 1006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171007, 31.8, 0.0, 3.95)
    ops.node(122007, 31.8, 0.0, 6.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1007, 171007, 122007, 0.1925, 27242382.07450357, 11350992.53104316, 0.00475217, 0.00533786, 0.00216161, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21007, 108.34052831, 0.0009683, 131.88453942, 0.01528276, 13.18845394, 0.04580917, -108.34052831, -0.0009683, -131.88453942, -0.01528276, -13.18845394, -0.04580917, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11007, 217.92363606, 0.00072721, 265.28168931, 0.0170413, 26.52816893, 0.05866895, -217.92363606, -0.00072721, -265.28168931, -0.0170413, -26.52816893, -0.05866895, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21007, 1007, 0.0, 163.5664232, 0.01936607, 163.5664232, 0.05809821, 114.49649624, -1836.25276715, 0.05, 2, 0, 71007, 22007, 2, 3)
    ops.uniaxialMaterial('LimitState', 41007, 40.8916058, 6.288e-05, 122.6748174, 0.00018864, 408.91605799, 0.00062879, -40.8916058, -6.288e-05, -122.6748174, -0.00018864, -408.91605799, -0.00062879, 0.4, 0.3, 0.003, 0.0, 0.0, 21007, 2)
    ops.limitCurve('ThreePoint', 11007, 1007, 0.0, 222.87777945, 0.01454427, 222.87777945, 0.0436328, 156.01444562, -3136.57229772, 0.05, 2, 0, 71007, 22007, 1, 3)
    ops.uniaxialMaterial('LimitState', 31007, 55.71944486, 8.568e-05, 167.15833459, 0.00025704, 557.19444863, 0.0008568, -55.71944486, -8.568e-05, -167.15833459, -0.00025704, -557.19444863, -0.0008568, 0.4, 0.3, 0.003, 0.0, 0.0, 11007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1007, 99999, 'P', 41007, 'Vy', 31007, 'Vz', 21007, 'My', 11007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171007, 71007, 171007, 1007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122007, 122007, 22007, 1007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171008, 37.6, 0.0, 3.95)
    ops.node(122008, 37.6, 0.0, 6.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1008, 171008, 122008, 0.0875, 28024539.16208893, 11676891.31753705, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21008, 73.64879752, 0.0014294, 89.39220463, 0.02454387, 8.93922046, 0.07236375, -73.64879752, -0.0014294, -89.39220463, -0.02454387, -8.93922046, -0.07236375, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11008, 85.76851207, 0.0010445, 104.10266888, 0.0269662, 10.41026689, 0.0897272, -85.76851207, -0.0010445, -104.10266888, -0.0269662, -10.41026689, -0.0897272, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21008, 1008, 0.0, 100.56638564, 0.02858794, 100.56638564, 0.08576382, 70.39646995, -1687.4567555, 0.05, 2, 0, 71008, 22008, 2, 3)
    ops.uniaxialMaterial('LimitState', 41008, 25.14159641, 8.268e-05, 75.42478923, 0.00024804, 251.41596409, 0.00082679, -25.14159641, -8.268e-05, -75.42478923, -0.00024804, -251.41596409, -0.00082679, 0.4, 0.3, 0.003, 0.0, 0.0, 21008, 2)
    ops.limitCurve('ThreePoint', 11008, 1008, 0.0, 119.3628061, 0.02089008, 119.3628061, 0.06267025, 83.55396427, -2654.61820399, 0.05, 2, 0, 71008, 22008, 1, 3)
    ops.uniaxialMaterial('LimitState', 31008, 29.84070153, 9.813e-05, 89.52210458, 0.0002944, 298.40701526, 0.00098133, -29.84070153, -9.813e-05, -89.52210458, -0.0002944, -298.40701526, -0.00098133, 0.4, 0.3, 0.003, 0.0, 0.0, 11008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1008, 99999, 'P', 41008, 'Vy', 31008, 'Vz', 21008, 'My', 11008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171008, 71008, 171008, 1008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122008, 122008, 22008, 1008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171009, 0.0, 4.75, 3.975)
    ops.node(122009, 0.0, 4.75, 6.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1009, 171009, 122009, 0.1925, 28680077.64586187, 11950032.35244245, 0.00475217, 0.00216161, 0.00533786, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21009, 223.08808023, 0.0007359, 270.96356787, 0.02645798, 27.09635679, 0.07780167, -223.08808023, -0.0007359, -270.96356787, -0.02645798, -27.09635679, -0.07780167, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11009, 118.57148443, 0.00099019, 144.01734255, 0.02335448, 14.40173425, 0.06019964, -118.57148443, -0.00099019, -144.01734255, -0.02335448, -14.40173425, -0.06019964, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21009, 1009, 0.0, 234.02390686, 0.01471804, 234.02390686, 0.04415412, 163.8167348, -3270.54266019, 0.05, 2, 0, 71009, 22009, 2, 3)
    ops.uniaxialMaterial('LimitState', 41009, 58.50597671, 8.546e-05, 175.51793014, 0.00025637, 585.05976714, 0.00085455, -58.50597671, -8.546e-05, -175.51793014, -0.00025637, -585.05976714, -0.00085455, 0.4, 0.3, 0.003, 0.0, 0.0, 21009, 2)
    ops.limitCurve('ThreePoint', 11009, 1009, 0.0, 172.10744753, 0.01980379, 172.10744753, 0.05941136, 120.47521327, -1889.91127734, 0.05, 2, 0, 71009, 22009, 1, 3)
    ops.uniaxialMaterial('LimitState', 31009, 43.02686188, 6.285e-05, 129.08058565, 0.00018854, 430.26861883, 0.00062846, -43.02686188, -6.285e-05, -129.08058565, -0.00018854, -430.26861883, -0.00062846, 0.4, 0.3, 0.003, 0.0, 0.0, 11009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1009, 99999, 'P', 41009, 'Vy', 31009, 'Vz', 21009, 'My', 11009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171009, 71009, 171009, 1009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122009, 122009, 22009, 1009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171010, 5.8, 4.75, 3.975)
    ops.node(122010, 5.8, 4.75, 6.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1010, 171010, 122010, 0.35, 29209679.05183822, 12170699.60493259, 0.01632638, 0.00802083, 0.01572083, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21010, 443.00781455, 0.00063023, 538.0606188, 0.01686624, 53.80606188, 0.04826635, -443.00781455, -0.00063023, -538.0606188, -0.01686624, -53.80606188, -0.04826635, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11010, 247.43870077, 0.00073665, 300.52973352, 0.01570863, 30.05297335, 0.04161662, -247.43870077, -0.00073665, -300.52973352, -0.01570863, -30.05297335, -0.04161662, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21010, 1010, 0.0, 421.7869849, 0.01260464, 421.7869849, 0.03781392, 295.25088943, -2932.70162835, 0.05, 2, 0, 71010, 22010, 2, 3)
    ops.uniaxialMaterial('LimitState', 41010, 105.44674622, 8.317e-05, 316.34023867, 0.00024952, 1054.46746225, 0.00083174, -105.44674622, -8.317e-05, -316.34023867, -0.00024952, -1054.46746225, -0.00083174, 0.4, 0.3, 0.003, 0.0, 0.0, 21010, 2)
    ops.limitCurve('ThreePoint', 11010, 1010, 0.0, 301.27641779, 0.014733, 301.27641779, 0.04419901, 210.89349245, -2064.30250759, 0.05, 2, 0, 71010, 22010, 1, 3)
    ops.uniaxialMaterial('LimitState', 31010, 75.31910445, 5.941e-05, 225.95731334, 0.00017823, 753.19104446, 0.0005941, -75.31910445, -5.941e-05, -225.95731334, -0.00017823, -753.19104446, -0.0005941, 0.4, 0.3, 0.003, 0.0, 0.0, 11010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1010, 99999, 'P', 41010, 'Vy', 31010, 'Vz', 21010, 'My', 11010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171010, 71010, 171010, 1010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122010, 122010, 22010, 1010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171011, 11.6, 4.75, 3.975)
    ops.node(122011, 11.6, 4.75, 6.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1011, 171011, 122011, 0.35, 27916710.31017665, 11631962.62924027, 0.01632638, 0.00802083, 0.01572083, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21011, 462.24045498, 0.00068876, 562.91839056, 0.01903143, 56.29183906, 0.04975303, -462.24045498, -0.00068876, -562.91839056, -0.01903143, -56.29183906, -0.04975303, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11011, 274.15822314, 0.00082145, 333.87104929, 0.01773609, 33.38710493, 0.04308424, -274.15822314, -0.00082145, -333.87104929, -0.01773609, -33.38710493, -0.04308424, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21011, 1011, 0.0, 396.11583744, 0.01377511, 396.11583744, 0.04132532, 277.28108621, -2755.32577887, 0.05, 2, 0, 71011, 22011, 2, 3)
    ops.uniaxialMaterial('LimitState', 41011, 99.02895936, 8.173e-05, 297.08687808, 0.00024519, 990.28959359, 0.0008173, -99.02895936, -8.173e-05, -297.08687808, -0.00024519, -990.28959359, -0.0008173, 0.4, 0.3, 0.003, 0.0, 0.0, 21011, 2)
    ops.limitCurve('ThreePoint', 11011, 1011, 0.0, 282.93988388, 0.01642906, 282.93988388, 0.04928717, 198.05791872, -1957.75956094, 0.05, 2, 0, 71011, 22011, 1, 3)
    ops.uniaxialMaterial('LimitState', 31011, 70.73497097, 5.838e-05, 212.20491291, 0.00017514, 707.34970971, 0.00058378, -70.73497097, -5.838e-05, -212.20491291, -0.00017514, -707.34970971, -0.00058378, 0.4, 0.3, 0.003, 0.0, 0.0, 11011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1011, 99999, 'P', 41011, 'Vy', 31011, 'Vz', 21011, 'My', 11011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171011, 71011, 171011, 1011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122011, 122011, 22011, 1011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171012, 17.4, 4.75, 3.975)
    ops.node(122012, 17.4, 4.75, 6.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1012, 171012, 122012, 0.24, 29991765.57221067, 12496568.98842111, 0.00751249, 0.00352, 0.00792, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21012, 230.84139983, 0.00068705, 279.5805147, 0.04715343, 27.95805147, 0.13063272, -230.84139983, -0.00068705, -279.5805147, -0.04715343, -27.95805147, -0.13063272, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11012, 173.1605683, 0.00087505, 209.72113688, 0.04114197, 20.97211369, 0.100579, -173.1605683, -0.00087505, -209.72113688, -0.04114197, -20.97211369, -0.100579, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21012, 1012, 0.0, 445.59870638, 0.01374095, 445.59870638, 0.04122286, 311.91909446, -12419.30073971, 0.05, 2, 0, 71012, 22012, 2, 3)
    ops.uniaxialMaterial('LimitState', 41012, 111.39967659, 0.0001248, 334.19902978, 0.00037441, 1113.99676594, 0.00124802, -111.39967659, -0.0001248, -334.19902978, -0.00037441, -1113.99676594, -0.00124802, 0.4, 0.3, 0.003, 0.0, 0.0, 21012, 2)
    ops.limitCurve('ThreePoint', 11012, 1012, 0.0, 310.25384306, 0.01750099, 310.25384306, 0.05250296, 217.17769014, -6649.74617481, 0.05, 2, 0, 71012, 22012, 1, 3)
    ops.uniaxialMaterial('LimitState', 31012, 77.56346077, 8.689e-05, 232.6903823, 0.00026068, 775.63460765, 0.00086895, -77.56346077, -8.689e-05, -232.6903823, -0.00026068, -775.63460765, -0.00086895, 0.4, 0.3, 0.003, 0.0, 0.0, 11012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1012, 99999, 'P', 41012, 'Vy', 31012, 'Vz', 21012, 'My', 11012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171012, 71012, 171012, 1012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122012, 122012, 22012, 1012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171013, 20.2, 4.75, 3.975)
    ops.node(122013, 20.2, 4.75, 6.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1013, 171013, 122013, 0.24, 29277024.7654951, 12198760.31895629, 0.00751249, 0.00352, 0.00792, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21013, 228.97685902, 0.00068049, 277.77211727, 0.04654468, 27.77721173, 0.12897038, -228.97685902, -0.00068049, -277.77211727, -0.04654468, -27.77721173, -0.12897038, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11013, 172.74280301, 0.00086223, 209.5545128, 0.0406073, 20.95545128, 0.09929418, -172.74280301, -0.00086223, -209.5545128, -0.0406073, -20.95545128, -0.09929418, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21013, 1013, 0.0, 422.23785355, 0.01360972, 422.23785355, 0.04082916, 295.56649749, -11064.51597944, 0.05, 2, 0, 71013, 22013, 2, 3)
    ops.uniaxialMaterial('LimitState', 41013, 105.55946339, 0.00012115, 316.67839016, 0.00036344, 1055.59463388, 0.00121146, -105.55946339, -0.00012115, -316.67839016, -0.00036344, -1055.59463388, -0.00121146, 0.4, 0.3, 0.003, 0.0, 0.0, 21013, 2)
    ops.limitCurve('ThreePoint', 11013, 1013, 0.0, 294.24225778, 0.01724462, 294.24225778, 0.05173385, 205.96958045, -5987.15373723, 0.05, 2, 0, 71013, 22013, 1, 3)
    ops.uniaxialMaterial('LimitState', 31013, 73.56056445, 8.442e-05, 220.68169334, 0.00025327, 735.60564446, 0.00084422, -73.56056445, -8.442e-05, -220.68169334, -0.00025327, -735.60564446, -0.00084422, 0.4, 0.3, 0.003, 0.0, 0.0, 11013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1013, 99999, 'P', 41013, 'Vy', 31013, 'Vz', 21013, 'My', 11013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171013, 71013, 171013, 1013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122013, 122013, 22013, 1013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171014, 26.0, 4.75, 3.975)
    ops.node(122014, 26.0, 4.75, 6.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1014, 171014, 122014, 0.35, 29374815.93712174, 12239506.64046739, 0.01632638, 0.00802083, 0.01572083, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21014, 475.13254451, 0.00068434, 576.86089542, 0.0181436, 57.68608954, 0.0496222, -475.13254451, -0.00068434, -576.86089542, -0.0181436, -57.68608954, -0.0496222, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11014, 281.67729723, 0.00081224, 341.98587274, 0.01691224, 34.19858727, 0.04288499, -281.67729723, -0.00081224, -341.98587274, -0.01691224, -34.19858727, -0.04288499, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21014, 1014, 0.0, 417.31940513, 0.01368686, 417.31940513, 0.04106059, 292.12358359, -2665.242848, 0.05, 2, 0, 71014, 22014, 2, 3)
    ops.uniaxialMaterial('LimitState', 41014, 104.32985128, 8.183e-05, 312.98955385, 0.00024549, 1043.29851283, 0.00081831, -104.32985128, -8.183e-05, -312.98955385, -0.00024549, -1043.29851283, -0.00081831, 0.4, 0.3, 0.003, 0.0, 0.0, 21014, 2)
    ops.limitCurve('ThreePoint', 11014, 1014, 0.0, 298.08528938, 0.01624484, 298.08528938, 0.04873452, 208.65970257, -1903.45227271, 0.05, 2, 0, 71014, 22014, 1, 3)
    ops.uniaxialMaterial('LimitState', 31014, 74.52132235, 5.845e-05, 223.56396704, 0.00017535, 745.21322345, 0.0005845, -74.52132235, -5.845e-05, -223.56396704, -0.00017535, -745.21322345, -0.0005845, 0.4, 0.3, 0.003, 0.0, 0.0, 11014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1014, 99999, 'P', 41014, 'Vy', 31014, 'Vz', 21014, 'My', 11014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171014, 71014, 171014, 1014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122014, 122014, 22014, 1014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171015, 31.8, 4.75, 3.975)
    ops.node(122015, 31.8, 4.75, 6.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1015, 171015, 122015, 0.35, 28849840.55794065, 12020766.89914194, 0.01632638, 0.00802083, 0.01572083, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21015, 457.72071143, 0.00066781, 556.37094868, 0.0188545, 55.63709487, 0.05007747, -457.72071143, -0.00066781, -556.37094868, -0.0188545, -55.63709487, -0.05007747, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11015, 256.38586558, 0.0007927, 311.64341857, 0.01756349, 31.16434186, 0.04332532, -256.38586558, -0.0007927, -311.64341857, -0.01756349, -31.16434186, -0.04332532, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21015, 1015, 0.0, 427.75280163, 0.01335627, 427.75280163, 0.0400688, 299.42696114, -3401.90695827, 0.05, 2, 0, 71015, 22015, 2, 3)
    ops.uniaxialMaterial('LimitState', 41015, 106.93820041, 8.54e-05, 320.81460123, 0.00025621, 1069.38200409, 0.00085403, -106.93820041, -8.54e-05, -320.81460123, -0.00025621, -1069.38200409, -0.00085403, 0.4, 0.3, 0.003, 0.0, 0.0, 21015, 2)
    ops.limitCurve('ThreePoint', 11015, 1015, 0.0, 305.53771545, 0.01585391, 305.53771545, 0.04756172, 213.87640082, -2343.93469876, 0.05, 2, 0, 71015, 22015, 1, 3)
    ops.uniaxialMaterial('LimitState', 31015, 76.38442886, 6.1e-05, 229.15328659, 0.00018301, 763.84428863, 0.00061002, -76.38442886, -6.1e-05, -229.15328659, -0.00018301, -763.84428863, -0.00061002, 0.4, 0.3, 0.003, 0.0, 0.0, 11015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1015, 99999, 'P', 41015, 'Vy', 31015, 'Vz', 21015, 'My', 11015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171015, 71015, 171015, 1015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122015, 122015, 22015, 1015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171016, 37.6, 4.75, 3.975)
    ops.node(122016, 37.6, 4.75, 6.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1016, 171016, 122016, 0.1925, 30830255.90546865, 12845939.96061194, 0.00475217, 0.00216161, 0.00533786, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21016, 219.67383753, 0.000721, 265.49746486, 0.02790954, 26.54974649, 0.08122394, -219.67383753, -0.000721, -265.49746486, -0.02790954, -26.54974649, -0.08122394, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11016, 117.27392384, 0.00097344, 141.73708541, 0.02461277, 14.17370854, 0.06287214, -117.27392384, -0.00097344, -141.73708541, -0.02461277, -14.17370854, -0.06287214, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21016, 1016, 0.0, 265.43139005, 0.01441996, 265.43139005, 0.04325989, 185.80197304, -4092.39156012, 0.05, 2, 0, 71016, 22016, 2, 3)
    ops.uniaxialMaterial('LimitState', 41016, 66.35784751, 9.016e-05, 199.07354254, 0.00027049, 663.57847513, 0.00090164, -66.35784751, -9.016e-05, -199.07354254, -0.00027049, -663.57847513, -0.00090164, 0.4, 0.3, 0.003, 0.0, 0.0, 21016, 2)
    ops.limitCurve('ThreePoint', 11016, 1016, 0.0, 194.56429903, 0.01946889, 194.56429903, 0.05840668, 136.19500932, -2283.85124254, 0.05, 2, 0, 71016, 22016, 1, 3)
    ops.uniaxialMaterial('LimitState', 31016, 48.64107476, 6.609e-05, 145.92322427, 0.00019827, 486.41074756, 0.00066092, -48.64107476, -6.609e-05, -145.92322427, -0.00019827, -486.41074756, -0.00066092, 0.4, 0.3, 0.003, 0.0, 0.0, 11016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1016, 99999, 'P', 41016, 'Vy', 31016, 'Vz', 21016, 'My', 11016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171016, 71016, 171016, 1016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122016, 122016, 22016, 1016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171017, 0.0, 9.5, 3.95)
    ops.node(122017, 0.0, 9.5, 6.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1017, 171017, 122017, 0.0875, 29709425.23400282, 12378927.18083451, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21017, 74.7225482, 0.00129462, 90.41704189, 0.02487829, 9.04170419, 0.07483316, -74.7225482, -0.00129462, -90.41704189, -0.02487829, -9.04170419, -0.07483316, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11017, 85.3277239, 0.00096712, 103.24969601, 0.027415, 10.3249696, 0.09297806, -85.3277239, -0.00096712, -103.24969601, -0.027415, -10.3249696, -0.09297806, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21017, 1017, 0.0, 105.90234334, 0.02589246, 105.90234334, 0.07767737, 74.13164034, -1732.14584453, 0.05, 2, 0, 71017, 22017, 2, 3)
    ops.uniaxialMaterial('LimitState', 41017, 26.47558584, 8.213e-05, 79.42675751, 0.00024639, 264.75585836, 0.00082128, -26.47558584, -8.213e-05, -79.42675751, -0.00024639, -264.75585836, -0.00082128, 0.4, 0.3, 0.003, 0.0, 0.0, 21017, 2)
    ops.limitCurve('ThreePoint', 11017, 1017, 0.0, 125.08777569, 0.01934247, 125.08777569, 0.05802742, 87.56144298, -2733.14970443, 0.05, 2, 0, 71017, 22017, 1, 3)
    ops.uniaxialMaterial('LimitState', 31017, 31.27194392, 9.701e-05, 93.81583177, 0.00029102, 312.71943922, 0.00097007, -31.27194392, -9.701e-05, -93.81583177, -0.00029102, -312.71943922, -0.00097007, 0.4, 0.3, 0.003, 0.0, 0.0, 11017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1017, 99999, 'P', 41017, 'Vy', 31017, 'Vz', 21017, 'My', 11017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171017, 71017, 171017, 1017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122017, 122017, 22017, 1017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171018, 5.8, 9.5, 3.95)
    ops.node(122018, 5.8, 9.5, 6.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1018, 171018, 122018, 0.1925, 27667178.2657157, 11527990.94404821, 0.00475217, 0.00533786, 0.00216161, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21018, 104.06709594, 0.00096187, 126.59978906, 0.01454747, 12.65997891, 0.04540809, -104.06709594, -0.00096187, -126.59978906, -0.01454747, -12.65997891, -0.04540809, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11018, 206.62181552, 0.00071399, 251.35974079, 0.01619741, 25.13597408, 0.05828081, -206.62181552, -0.00071399, -251.35974079, -0.01619741, -25.13597408, -0.05828081, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21018, 1018, 0.0, 158.9433373, 0.01923732, 158.9433373, 0.05771196, 111.26033611, -1594.98026297, 0.05, 2, 0, 71018, 22018, 2, 3)
    ops.uniaxialMaterial('LimitState', 41018, 39.73583432, 6.016e-05, 119.20750297, 0.00018049, 397.35834325, 0.00060164, -39.73583432, -6.016e-05, -119.20750297, -0.00018049, -397.35834325, -0.00060164, 0.4, 0.3, 0.003, 0.0, 0.0, 21018, 2)
    ops.limitCurve('ThreePoint', 11018, 1018, 0.0, 214.8817668, 0.01427979, 214.8817668, 0.04283936, 150.41723676, -2644.57897672, 0.05, 2, 0, 71018, 22018, 1, 3)
    ops.uniaxialMaterial('LimitState', 31018, 53.7204417, 8.134e-05, 161.1613251, 0.00024401, 537.204417, 0.00081338, -53.7204417, -8.134e-05, -161.1613251, -0.00024401, -537.204417, -0.00081338, 0.4, 0.3, 0.003, 0.0, 0.0, 11018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1018, 99999, 'P', 41018, 'Vy', 31018, 'Vz', 21018, 'My', 11018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171018, 71018, 171018, 1018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122018, 122018, 22018, 1018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171019, 11.6, 9.5, 3.95)
    ops.node(122019, 11.6, 9.5, 6.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1019, 171019, 122019, 0.1925, 30293828.9700036, 12622428.7375015, 0.00475217, 0.00533786, 0.00216161, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21019, 104.17972918, 0.00090441, 126.06098528, 0.01758909, 12.60609853, 0.05015133, -104.17972918, -0.00090441, -126.06098528, -0.01758909, -12.60609853, -0.05015133, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11019, 206.59013258, 0.00068183, 249.9810267, 0.01969724, 24.99810267, 0.06410106, -206.59013258, -0.00068183, -249.9810267, -0.01969724, -24.99810267, -0.06410106, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21019, 1019, 0.0, 186.05452228, 0.0180883, 186.05452228, 0.0542649, 130.23816559, -2031.5951509, 0.05, 2, 0, 71019, 22019, 2, 3)
    ops.uniaxialMaterial('LimitState', 41019, 46.51363057, 6.432e-05, 139.54089171, 0.00019296, 465.13630569, 0.0006432, -46.51363057, -6.432e-05, -139.54089171, -0.00019296, -465.13630569, -0.0006432, 0.4, 0.3, 0.003, 0.0, 0.0, 21019, 2)
    ops.limitCurve('ThreePoint', 11019, 1019, 0.0, 252.81358487, 0.01363665, 252.81358487, 0.04090996, 176.96950941, -3539.81592876, 0.05, 2, 0, 71019, 22019, 1, 3)
    ops.uniaxialMaterial('LimitState', 31019, 63.20339622, 8.74e-05, 189.61018865, 0.0002622, 632.03396217, 0.00087399, -63.20339622, -8.74e-05, -189.61018865, -0.0002622, -632.03396217, -0.00087399, 0.4, 0.3, 0.003, 0.0, 0.0, 11019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1019, 99999, 'P', 41019, 'Vy', 31019, 'Vz', 21019, 'My', 11019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171019, 71019, 171019, 1019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122019, 122019, 22019, 1019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171020, 17.4, 9.5, 3.95)
    ops.node(122020, 17.4, 9.5, 6.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1020, 171020, 122020, 0.12, 32711214.44554438, 13629672.68564349, 0.00194385, 0.00176, 0.00099, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21020, 73.60310804, 0.00101046, 88.39119596, 0.02089588, 8.8391196, 0.06897048, -73.60310804, -0.00101046, -88.39119596, -0.02089588, -8.8391196, -0.06897048, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11020, 87.68840023, 0.0008138, 105.3064575, 0.02267349, 10.53064575, 0.08285047, -87.68840023, -0.0008138, -105.3064575, -0.02267349, -10.53064575, -0.08285047, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21020, 1020, 0.0, 143.51628368, 0.02020915, 143.51628368, 0.06062744, 100.46139857, -1872.97062383, 0.05, 2, 0, 71020, 22020, 2, 3)
    ops.uniaxialMaterial('LimitState', 41020, 35.87907092, 7.371e-05, 107.63721276, 0.00022112, 358.79070919, 0.00073708, -35.87907092, -7.371e-05, -107.63721276, -0.00022112, -358.79070919, -0.00073708, 0.4, 0.3, 0.003, 0.0, 0.0, 21020, 2)
    ops.limitCurve('ThreePoint', 11020, 1020, 0.0, 161.43385478, 0.01627601, 161.43385478, 0.04882804, 113.00369834, -2706.59835937, 0.05, 2, 0, 71020, 22020, 1, 3)
    ops.uniaxialMaterial('LimitState', 31020, 40.35846369, 8.291e-05, 121.07539108, 0.00024873, 403.58463694, 0.0008291, -40.35846369, -8.291e-05, -121.07539108, -0.00024873, -403.58463694, -0.0008291, 0.4, 0.3, 0.003, 0.0, 0.0, 11020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1020, 99999, 'P', 41020, 'Vy', 31020, 'Vz', 21020, 'My', 11020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171020, 71020, 171020, 1020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122020, 122020, 22020, 1020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171021, 20.2, 9.5, 3.95)
    ops.node(122021, 20.2, 9.5, 6.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1021, 171021, 122021, 0.12, 29351725.96147385, 12229885.81728077, 0.00194385, 0.00176, 0.00099, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21021, 74.60069978, 0.00103068, 90.37149062, 0.02312898, 9.03714906, 0.0683757, -74.60069978, -0.00103068, -90.37149062, -0.02312898, -9.03714906, -0.0683757, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11021, 87.82963488, 0.00083256, 106.39705858, 0.02512483, 10.63970586, 0.08176202, -87.82963488, -0.00083256, -106.39705858, -0.02512483, -10.63970586, -0.08176202, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21021, 1021, 0.0, 135.44509894, 0.02061358, 135.44509894, 0.06184075, 94.81156926, -2061.57524941, 0.05, 2, 0, 71021, 22021, 2, 3)
    ops.uniaxialMaterial('LimitState', 41021, 33.86127473, 7.752e-05, 101.5838242, 0.00023257, 338.61274734, 0.00077524, -33.86127473, -7.752e-05, -101.5838242, -0.00023257, -338.61274734, -0.00077524, 0.4, 0.3, 0.003, 0.0, 0.0, 21021, 2)
    ops.limitCurve('ThreePoint', 11021, 1021, 0.0, 154.81480276, 0.01665113, 154.81480276, 0.0499534, 108.37036193, -3009.68924227, 0.05, 2, 0, 71021, 22021, 1, 3)
    ops.uniaxialMaterial('LimitState', 31021, 38.70370069, 8.861e-05, 116.11110207, 0.00026583, 387.03700689, 0.00088611, -38.70370069, -8.861e-05, -116.11110207, -0.00026583, -387.03700689, -0.00088611, 0.4, 0.3, 0.003, 0.0, 0.0, 11021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1021, 99999, 'P', 41021, 'Vy', 31021, 'Vz', 21021, 'My', 11021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171021, 71021, 171021, 1021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122021, 122021, 22021, 1021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171022, 26.0, 9.5, 3.95)
    ops.node(122022, 26.0, 9.5, 6.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1022, 171022, 122022, 0.1925, 31588365.65630184, 13161819.0234591, 0.00475217, 0.00533786, 0.00216161, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21022, 102.31773532, 0.0008495, 123.383194, 0.01556959, 12.3383194, 0.04878283, -102.31773532, -0.0008495, -123.383194, -0.01556959, -12.3383194, -0.04878283, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11022, 202.9299598, 0.0006504, 244.70974189, 0.01742678, 24.47097419, 0.06271835, -202.9299598, -0.0006504, -244.70974189, -0.01742678, -24.47097419, -0.06271835, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21022, 1022, 0.0, 188.00548379, 0.01699009, 188.00548379, 0.05097027, 131.60383865, -1822.71336668, 0.05, 2, 0, 71022, 22022, 2, 3)
    ops.uniaxialMaterial('LimitState', 41022, 47.00137095, 6.233e-05, 141.00411284, 0.00018699, 470.01370947, 0.00062331, -47.00137095, -6.233e-05, -141.00411284, -0.00018699, -470.01370947, -0.00062331, 0.4, 0.3, 0.003, 0.0, 0.0, 21022, 2)
    ops.limitCurve('ThreePoint', 11022, 1022, 0.0, 253.48255249, 0.01300802, 253.48255249, 0.03902406, 177.43778674, -3108.77562133, 0.05, 2, 0, 71022, 22022, 1, 3)
    ops.uniaxialMaterial('LimitState', 31022, 63.37063812, 8.404e-05, 190.11191437, 0.00025212, 633.70638122, 0.00084039, -63.37063812, -8.404e-05, -190.11191437, -0.00025212, -633.70638122, -0.00084039, 0.4, 0.3, 0.003, 0.0, 0.0, 11022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1022, 99999, 'P', 41022, 'Vy', 31022, 'Vz', 21022, 'My', 11022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171022, 71022, 171022, 1022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122022, 122022, 22022, 1022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171023, 31.8, 9.5, 3.95)
    ops.node(122023, 31.8, 9.5, 6.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1023, 171023, 122023, 0.1925, 28641774.63244529, 11934072.76351887, 0.00475217, 0.00533786, 0.00216161, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21023, 107.94312923, 0.00094142, 131.08880535, 0.01446053, 13.10888053, 0.04602089, -107.94312923, -0.00094142, -131.08880535, -0.01446053, -13.10888053, -0.04602089, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11023, 216.42031903, 0.00071021, 262.82618707, 0.01611784, 26.28261871, 0.05915544, -216.42031903, -0.00071021, -262.82618707, -0.01611784, -26.28261871, -0.05915544, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21023, 1023, 0.0, 165.27144628, 0.01882845, 165.27144628, 0.05648534, 115.6900124, -1625.57158653, 0.05, 2, 0, 71023, 22023, 2, 3)
    ops.uniaxialMaterial('LimitState', 41023, 41.31786157, 6.043e-05, 123.95358471, 0.00018129, 413.17861571, 0.00060431, -41.31786157, -6.043e-05, -123.95358471, -0.00018129, -413.17861571, -0.00060431, 0.4, 0.3, 0.003, 0.0, 0.0, 21023, 2)
    ops.limitCurve('ThreePoint', 11023, 1023, 0.0, 223.12277438, 0.01420411, 223.12277438, 0.04261234, 156.18594207, -2706.54417682, 0.05, 2, 0, 71023, 22023, 1, 3)
    ops.uniaxialMaterial('LimitState', 31023, 55.7806936, 8.158e-05, 167.34208079, 0.00024475, 557.80693595, 0.00081584, -55.7806936, -8.158e-05, -167.34208079, -0.00024475, -557.80693595, -0.00081584, 0.4, 0.3, 0.003, 0.0, 0.0, 11023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1023, 99999, 'P', 41023, 'Vy', 31023, 'Vz', 21023, 'My', 11023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171023, 71023, 171023, 1023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122023, 122023, 22023, 1023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171024, 37.6, 9.5, 3.95)
    ops.node(122024, 37.6, 9.5, 6.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1024, 171024, 122024, 0.0875, 29651021.27614199, 12354592.1983925, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21024, 69.69602799, 0.00129126, 84.34513709, 0.02429218, 8.43451371, 0.07418026, -69.69602799, -0.00129126, -84.34513709, -0.02429218, -8.43451371, -0.07418026, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11024, 81.39507161, 0.00095269, 98.50315249, 0.02674704, 9.85031525, 0.09222244, -81.39507161, -0.00095269, -98.50315249, -0.02674704, -9.85031525, -0.09222244, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21024, 1024, 0.0, 103.36604418, 0.02582525, 103.36604418, 0.07747575, 72.35623093, -1623.70178342, 0.05, 2, 0, 71024, 22024, 2, 3)
    ops.uniaxialMaterial('LimitState', 41024, 25.84151105, 8.032e-05, 77.52453314, 0.00024096, 258.41511046, 0.00080319, -25.84151105, -8.032e-05, -77.52453314, -0.00024096, -258.41511046, -0.00080319, 0.4, 0.3, 0.003, 0.0, 0.0, 21024, 2)
    ops.limitCurve('ThreePoint', 11024, 1024, 0.0, 121.59845815, 0.01905378, 121.59845815, 0.05716134, 85.11892071, -2542.79276001, 0.05, 2, 0, 71024, 22024, 1, 3)
    ops.uniaxialMaterial('LimitState', 31024, 30.39961454, 9.449e-05, 91.19884362, 0.00028346, 303.99614539, 0.00094487, -30.39961454, -9.449e-05, -91.19884362, -0.00028346, -303.99614539, -0.00094487, 0.4, 0.3, 0.003, 0.0, 0.0, 11024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1024, 99999, 'P', 41024, 'Vy', 31024, 'Vz', 21024, 'My', 11024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171024, 71024, 171024, 1024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122024, 122024, 22024, 1024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172001, 0.0, 0.0, 6.75)
    ops.node(123001, 0.0, 0.0, 8.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2001, 172001, 123001, 0.0625, 29031822.8264651, 12096592.84436046, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22001, 28.68661004, 0.00126894, 34.79812669, 0.02121997, 3.47981267, 0.07680423, -28.68661004, -0.00126894, -34.79812669, -0.02121997, -3.47981267, -0.07680423, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12001, 28.68661004, 0.00126894, 34.79812669, 0.02121997, 3.47981267, 0.07680423, -28.68661004, -0.00126894, -34.79812669, -0.02121997, -3.47981267, -0.07680423, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22001, 2001, 0.0, 79.67411878, 0.02537879, 79.67411878, 0.07613637, 55.77188315, -1661.74226506, 0.05, 2, 0, 72001, 23001, 2, 3)
    ops.uniaxialMaterial('LimitState', 42001, 19.9185297, 8.852e-05, 59.75558909, 0.00026557, 199.18529696, 0.00088522, -19.9185297, -8.852e-05, -59.75558909, -0.00026557, -199.18529696, -0.00088522, 0.4, 0.3, 0.003, 0.0, 0.0, 22001, 2)
    ops.limitCurve('ThreePoint', 12001, 2001, 0.0, 79.67411878, 0.02537879, 79.67411878, 0.07613637, 55.77188315, -1661.74226506, 0.05, 2, 0, 72001, 23001, 1, 3)
    ops.uniaxialMaterial('LimitState', 32001, 19.9185297, 8.852e-05, 59.75558909, 0.00026557, 199.18529696, 0.00088522, -19.9185297, -8.852e-05, -59.75558909, -0.00026557, -199.18529696, -0.00088522, 0.4, 0.3, 0.003, 0.0, 0.0, 12001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2001, 99999, 'P', 42001, 'Vy', 32001, 'Vz', 22001, 'My', 12001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172001, 72001, 172001, 2001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123001, 123001, 23001, 2001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172002, 5.8, 0.0, 6.75)
    ops.node(123002, 5.8, 0.0, 8.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2002, 172002, 123002, 0.125, 29072619.35094796, 12113591.39622832, 0.00178813, 0.00286458, 0.00071615, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22002, 52.33515463, 0.00119639, 63.52299846, 0.01786864, 6.35229985, 0.05206122, -52.33515463, -0.00119639, -63.52299846, -0.01786864, -6.35229985, -0.05206122, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12002, 111.33645814, 0.00071298, 135.13718854, 0.02135917, 13.51371885, 0.07813602, -111.33645814, -0.00071298, -135.13718854, -0.02135917, -13.51371885, -0.07813602, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22002, 2002, 0.0, 118.97679698, 0.02392782, 118.97679698, 0.07178347, 83.28375789, -1466.92646748, 0.05, 2, 0, 72002, 23002, 2, 3)
    ops.uniaxialMaterial('LimitState', 42002, 29.74419924, 6.6e-05, 89.23259773, 0.00019801, 297.44199245, 0.00066002, -29.74419924, -6.6e-05, -89.23259773, -0.00019801, -297.44199245, -0.00066002, 0.4, 0.3, 0.003, 0.0, 0.0, 22002, 2)
    ops.limitCurve('ThreePoint', 12002, 2002, 0.0, 172.41985932, 0.01425958, 172.41985932, 0.04277873, 120.69390152, -3729.3530791, 0.05, 2, 0, 72002, 23002, 1, 3)
    ops.uniaxialMaterial('LimitState', 32002, 43.10496483, 9.565e-05, 129.31489449, 0.00028695, 431.0496483, 0.0009565, -43.10496483, -9.565e-05, -129.31489449, -0.00028695, -431.0496483, -0.0009565, 0.4, 0.3, 0.003, 0.0, 0.0, 12002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2002, 99999, 'P', 42002, 'Vy', 32002, 'Vz', 22002, 'My', 12002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172002, 72002, 172002, 2002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123002, 123002, 23002, 2002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172003, 11.6, 0.0, 6.75)
    ops.node(123003, 11.6, 0.0, 8.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2003, 172003, 123003, 0.125, 30722261.99766035, 12800942.49902515, 0.00178813, 0.00286458, 0.00071615, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22003, 54.02832835, 0.00114054, 65.32317469, 0.01473402, 6.53231747, 0.04988633, -54.02832835, -0.00114054, -65.32317469, -0.01473402, -6.53231747, -0.04988633, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12003, 113.97675907, 0.00069807, 137.80407372, 0.01753165, 13.78040737, 0.07590212, -113.97675907, -0.00069807, -137.80407372, -0.01753165, -13.78040737, -0.07590212, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22003, 2003, 0.0, 112.07388562, 0.02281075, 112.07388562, 0.06843226, 78.45171993, -1144.20178142, 0.05, 2, 0, 72003, 23003, 2, 3)
    ops.uniaxialMaterial('LimitState', 42003, 28.0184714, 5.883e-05, 84.05541421, 0.0001765, 280.18471404, 0.00058834, -28.0184714, -5.883e-05, -84.05541421, -0.0001765, -280.18471404, -0.00058834, 0.4, 0.3, 0.003, 0.0, 0.0, 22003, 2)
    ops.limitCurve('ThreePoint', 12003, 2003, 0.0, 162.75619403, 0.01396139, 162.75619403, 0.04188416, 113.92933582, -2716.45071976, 0.05, 2, 0, 72003, 23003, 1, 3)
    ops.uniaxialMaterial('LimitState', 32003, 40.68904851, 8.544e-05, 122.06714552, 0.00025632, 406.89048508, 0.00085441, -40.68904851, -8.544e-05, -122.06714552, -0.00025632, -406.89048508, -0.00085441, 0.4, 0.3, 0.003, 0.0, 0.0, 12003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2003, 99999, 'P', 42003, 'Vy', 32003, 'Vz', 22003, 'My', 12003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172003, 72003, 172003, 2003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123003, 123003, 23003, 2003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172006, 26.0, 0.0, 6.75)
    ops.node(123006, 26.0, 0.0, 8.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2006, 172006, 123006, 0.125, 29509492.97083487, 12295622.07118119, 0.00178813, 0.00286458, 0.00071615, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22006, 55.86896455, 0.00124853, 67.7478908, 0.01592184, 6.77478908, 0.05038872, -55.86896455, -0.00124853, -67.7478908, -0.01592184, -6.77478908, -0.05038872, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12006, 118.42244742, 0.00074559, 143.60157021, 0.01891639, 14.36015702, 0.07614869, -118.42244742, -0.00074559, -143.60157021, -0.01891639, -14.36015702, -0.07614869, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22006, 2006, 0.0, 114.91073601, 0.02497069, 114.91073601, 0.07491206, 80.43751521, -1243.24204041, 0.05, 2, 0, 72006, 23006, 2, 3)
    ops.uniaxialMaterial('LimitState', 42006, 28.727684, 6.28e-05, 86.18305201, 0.00018841, 287.27684003, 0.00062803, -28.727684, -6.28e-05, -86.18305201, -0.00018841, -287.27684003, -0.00062803, 0.4, 0.3, 0.003, 0.0, 0.0, 22006, 2)
    ops.limitCurve('ThreePoint', 12006, 2006, 0.0, 162.90523336, 0.01491188, 162.90523336, 0.04473563, 114.03366335, -3023.5429438, 0.05, 2, 0, 72006, 23006, 1, 3)
    ops.uniaxialMaterial('LimitState', 32006, 40.72630834, 8.903e-05, 122.17892502, 0.0002671, 407.26308339, 0.00089034, -40.72630834, -8.903e-05, -122.17892502, -0.0002671, -407.26308339, -0.00089034, 0.4, 0.3, 0.003, 0.0, 0.0, 12006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2006, 99999, 'P', 42006, 'Vy', 32006, 'Vz', 22006, 'My', 12006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172006, 72006, 172006, 2006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123006, 123006, 23006, 2006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172007, 31.8, 0.0, 6.75)
    ops.node(123007, 31.8, 0.0, 8.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2007, 172007, 123007, 0.125, 32469025.9492538, 13528760.81218908, 0.00178813, 0.00286458, 0.00071615, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22007, 52.24439596, 0.00125298, 62.84894725, 0.01392677, 6.28489472, 0.04989951, -52.24439596, -0.00125298, -62.84894725, -0.01392677, -6.28489472, -0.04989951, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12007, 111.81403527, 0.00072042, 134.51001345, 0.0164151, 13.45100134, 0.0761479, -111.81403527, -0.00072042, -134.51001345, -0.0164151, -13.45100134, -0.0761479, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22007, 2007, 0.0, 115.82250364, 0.02505952, 115.82250364, 0.07517855, 81.07575255, -1158.08721286, 0.05, 2, 0, 72007, 23007, 2, 3)
    ops.uniaxialMaterial('LimitState', 42007, 28.95562591, 5.753e-05, 86.86687773, 0.00017259, 289.5562591, 0.00057531, -28.95562591, -5.753e-05, -86.86687773, -0.00017259, -289.5562591, -0.00057531, 0.4, 0.3, 0.003, 0.0, 0.0, 22007, 2)
    ops.limitCurve('ThreePoint', 12007, 2007, 0.0, 171.24517571, 0.01440831, 171.24517571, 0.04322494, 119.871623, -2759.27884901, 0.05, 2, 0, 72007, 23007, 1, 3)
    ops.uniaxialMaterial('LimitState', 32007, 42.81129393, 8.506e-05, 128.43388178, 0.00025518, 428.11293927, 0.00085061, -42.81129393, -8.506e-05, -128.43388178, -0.00025518, -428.11293927, -0.00085061, 0.4, 0.3, 0.003, 0.0, 0.0, 12007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2007, 99999, 'P', 42007, 'Vy', 32007, 'Vz', 22007, 'My', 12007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172007, 72007, 172007, 2007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123007, 123007, 23007, 2007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172008, 37.6, 0.0, 6.75)
    ops.node(123008, 37.6, 0.0, 8.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2008, 172008, 123008, 0.0625, 29547896.73788899, 12311623.64078708, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22008, 28.8372213, 0.00131858, 34.94298988, 0.01874419, 3.49429899, 0.0749212, -28.8372213, -0.00131858, -34.94298988, -0.01874419, -3.49429899, -0.0749212, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12008, 28.8372213, 0.00131858, 34.94298988, 0.01874419, 3.49429899, 0.0749212, -28.8372213, -0.00131858, -34.94298988, -0.01874419, -3.49429899, -0.0749212, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22008, 2008, 0.0, 75.62198887, 0.02637162, 75.62198887, 0.07911485, 52.93539221, -1382.83469324, 0.05, 2, 0, 72008, 23008, 2, 3)
    ops.uniaxialMaterial('LimitState', 42008, 18.90549722, 8.255e-05, 56.71649165, 0.00024766, 189.05497216, 0.00082553, -18.90549722, -8.255e-05, -56.71649165, -0.00024766, -189.05497216, -0.00082553, 0.4, 0.3, 0.003, 0.0, 0.0, 22008, 2)
    ops.limitCurve('ThreePoint', 12008, 2008, 0.0, 75.62198887, 0.02637162, 75.62198887, 0.07911485, 52.93539221, -1382.83469324, 0.05, 2, 0, 72008, 23008, 1, 3)
    ops.uniaxialMaterial('LimitState', 32008, 18.90549722, 8.255e-05, 56.71649165, 0.00024766, 189.05497216, 0.00082553, -18.90549722, -8.255e-05, -56.71649165, -0.00024766, -189.05497216, -0.00082553, 0.4, 0.3, 0.003, 0.0, 0.0, 12008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2008, 99999, 'P', 42008, 'Vy', 32008, 'Vz', 22008, 'My', 12008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172008, 72008, 172008, 2008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123008, 123008, 23008, 2008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172009, 0.0, 4.75, 6.775)
    ops.node(123009, 0.0, 4.75, 8.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2009, 172009, 123009, 0.125, 27001247.05718, 11250519.60715833, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22009, 130.70723949, 0.00077436, 159.27205682, 0.03372077, 15.92720568, 0.09928098, -130.70723949, -0.00077436, -159.27205682, -0.03372077, -15.92720568, -0.09928098, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12009, 56.68192352, 0.00134074, 69.0692159, 0.02760938, 6.90692159, 0.065918, -56.68192352, -0.00134074, -69.0692159, -0.02760938, -6.90692159, -0.065918, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22009, 2009, 0.0, 178.58294592, 0.01548724, 178.58294592, 0.04646171, 125.00806215, -4882.98720123, 0.05, 2, 0, 72009, 23009, 2, 3)
    ops.uniaxialMaterial('LimitState', 42009, 44.64573648, 0.00010667, 133.93720944, 0.00032001, 446.45736481, 0.00106669, -44.64573648, -0.00010667, -133.93720944, -0.00032001, -446.45736481, -0.00106669, 0.4, 0.3, 0.003, 0.0, 0.0, 22009, 2)
    ops.limitCurve('ThreePoint', 12009, 2009, 0.0, 118.68489887, 0.02681475, 118.68489887, 0.08044424, 83.07942921, -1812.01391609, 0.05, 2, 0, 72009, 23009, 1, 3)
    ops.uniaxialMaterial('LimitState', 32009, 29.67122472, 7.089e-05, 89.01367415, 0.00021267, 296.71224717, 0.00070891, -29.67122472, -7.089e-05, -89.01367415, -0.00021267, -296.71224717, -0.00070891, 0.4, 0.3, 0.003, 0.0, 0.0, 12009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2009, 99999, 'P', 42009, 'Vy', 32009, 'Vz', 22009, 'My', 12009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172009, 72009, 172009, 2009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123009, 123009, 23009, 2009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172010, 5.8, 4.75, 6.775)
    ops.node(123010, 5.8, 4.75, 8.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2010, 172010, 123010, 0.24, 28756295.38523661, 11981789.74384859, 0.00751249, 0.00352, 0.00792, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22010, 253.86212277, 0.00067679, 308.75093243, 0.01969836, 30.87509324, 0.05605729, -253.86212277, -0.00067679, -308.75093243, -0.01969836, -30.87509324, -0.05605729, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12010, 139.69384492, 0.00085345, 169.89775553, 0.01796837, 16.98977555, 0.04626926, -139.69384492, -0.00085345, -169.89775553, -0.01796837, -16.98977555, -0.04626926, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22010, 2010, 0.0, 270.96601334, 0.01353587, 270.96601334, 0.0406076, 189.67620933, -2963.26008488, 0.05, 2, 0, 72010, 23010, 2, 3)
    ops.uniaxialMaterial('LimitState', 42010, 67.74150333, 7.915e-05, 203.22451, 0.00023746, 677.41503334, 0.00079152, -67.74150333, -7.915e-05, -203.22451, -0.00023746, -677.41503334, -0.00079152, 0.4, 0.3, 0.003, 0.0, 0.0, 22010, 2)
    ops.limitCurve('ThreePoint', 12010, 2010, 0.0, 192.5452699, 0.01706891, 192.5452699, 0.05120674, 134.78168893, -1811.0214696, 0.05, 2, 0, 72010, 23010, 1, 3)
    ops.uniaxialMaterial('LimitState', 32010, 48.13631748, 5.624e-05, 144.40895243, 0.00016873, 481.36317476, 0.00056244, -48.13631748, -5.624e-05, -144.40895243, -0.00016873, -481.36317476, -0.00056244, 0.4, 0.3, 0.003, 0.0, 0.0, 12010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2010, 99999, 'P', 42010, 'Vy', 32010, 'Vz', 22010, 'My', 12010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172010, 72010, 172010, 2010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123010, 123010, 23010, 2010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172011, 11.6, 4.75, 6.775)
    ops.node(123011, 11.6, 4.75, 8.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2011, 172011, 123011, 0.24, 31241751.10258349, 13017396.29274312, 0.00751249, 0.00352, 0.00792, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22011, 267.07306072, 0.00071604, 322.78674357, 0.02140407, 32.27867436, 0.05892514, -267.07306072, -0.00071604, -322.78674357, -0.02140407, -32.27867436, -0.05892514, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12011, 159.56188308, 0.00091854, 192.8478316, 0.01953288, 19.28478316, 0.04873836, -159.56188308, -0.00091854, -192.8478316, -0.01953288, -19.28478316, -0.04873836, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22011, 2011, 0.0, 293.667853, 0.01432087, 293.667853, 0.0429626, 205.5674971, -2883.72290966, 0.05, 2, 0, 72011, 23011, 2, 3)
    ops.uniaxialMaterial('LimitState', 42011, 73.41696325, 7.896e-05, 220.25088975, 0.00023688, 734.16963251, 0.00078959, -73.41696325, -7.896e-05, -220.25088975, -0.00023688, -734.16963251, -0.00078959, 0.4, 0.3, 0.003, 0.0, 0.0, 22011, 2)
    ops.limitCurve('ThreePoint', 12011, 2011, 0.0, 209.20258959, 0.01837078, 209.20258959, 0.05511235, 146.44181271, -1769.52697108, 0.05, 2, 0, 72011, 23011, 1, 3)
    ops.uniaxialMaterial('LimitState', 32011, 52.3006474, 5.625e-05, 156.90194219, 0.00016875, 523.00647397, 0.00056249, -52.3006474, -5.625e-05, -156.90194219, -0.00016875, -523.00647397, -0.00056249, 0.4, 0.3, 0.003, 0.0, 0.0, 12011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2011, 99999, 'P', 42011, 'Vy', 32011, 'Vz', 22011, 'My', 12011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172011, 72011, 172011, 2011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123011, 123011, 23011, 2011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172012, 17.4, 4.75, 6.775)
    ops.node(123012, 17.4, 4.75, 8.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2012, 172012, 123012, 0.175, 28937022.7861094, 12057092.82754558, 0.00405757, 0.0019651, 0.00401042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22012, 165.8154409, 0.00078565, 201.43205595, 0.02726863, 20.1432056, 0.07992652, -165.8154409, -0.00078565, -201.43205595, -0.02726863, -20.1432056, -0.07992652, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12012, 101.8169848, 0.00100733, 123.68694054, 0.02468702, 12.36869405, 0.06507025, -101.8169848, -0.00100733, -123.68694054, -0.02468702, -12.36869405, -0.06507025, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22012, 2012, 0.0, 206.27538701, 0.0157129, 206.27538701, 0.04713871, 144.39277091, -3458.03630251, 0.05, 2, 0, 72012, 23012, 2, 3)
    ops.uniaxialMaterial('LimitState', 42012, 51.56884675, 8.212e-05, 154.70654026, 0.00024636, 515.68846752, 0.00082119, -51.56884675, -8.212e-05, -154.70654026, -0.00024636, -515.68846752, -0.00082119, 0.4, 0.3, 0.003, 0.0, 0.0, 22012, 2)
    ops.limitCurve('ThreePoint', 12012, 2012, 0.0, 165.31336037, 0.02014657, 165.31336037, 0.06043971, 115.71935226, -2152.44986618, 0.05, 2, 0, 72012, 23012, 1, 3)
    ops.uniaxialMaterial('LimitState', 32012, 41.32834009, 6.581e-05, 123.98502028, 0.00019744, 413.28340092, 0.00065812, -41.32834009, -6.581e-05, -123.98502028, -0.00019744, -413.28340092, -0.00065812, 0.4, 0.3, 0.003, 0.0, 0.0, 12012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2012, 99999, 'P', 42012, 'Vy', 32012, 'Vz', 22012, 'My', 12012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172012, 72012, 172012, 2012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123012, 123012, 23012, 2012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172013, 20.2, 4.75, 6.775)
    ops.node(123013, 20.2, 4.75, 8.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2013, 172013, 123013, 0.175, 26152220.18426416, 10896758.41011007, 0.00405757, 0.0019651, 0.00401042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22013, 162.46713762, 0.00077189, 198.2953998, 0.02945727, 19.82953998, 0.0790279, -162.46713762, -0.00077189, -198.2953998, -0.02945727, -19.82953998, -0.0790279, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12013, 99.6080936, 0.00097969, 121.574289, 0.02662864, 12.1574289, 0.06464426, -99.6080936, -0.00097969, -121.574289, -0.02662864, -12.1574289, -0.06464426, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22013, 2013, 0.0, 198.30104634, 0.01543774, 198.30104634, 0.04631323, 138.81073244, -3910.23715175, 0.05, 2, 0, 72013, 23013, 2, 3)
    ops.uniaxialMaterial('LimitState', 42013, 49.57526159, 8.735e-05, 148.72578476, 0.00026205, 495.75261586, 0.00087351, -49.57526159, -8.735e-05, -148.72578476, -0.00026205, -495.75261586, -0.00087351, 0.4, 0.3, 0.003, 0.0, 0.0, 22013, 2)
    ops.limitCurve('ThreePoint', 12013, 2013, 0.0, 156.96848946, 0.01959376, 156.96848946, 0.05878128, 109.87794262, -2401.32102257, 0.05, 2, 0, 72013, 23013, 1, 3)
    ops.uniaxialMaterial('LimitState', 32013, 39.24212236, 6.914e-05, 117.72636709, 0.00020743, 392.42122365, 0.00069144, -39.24212236, -6.914e-05, -117.72636709, -0.00020743, -392.42122365, -0.00069144, 0.4, 0.3, 0.003, 0.0, 0.0, 12013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2013, 99999, 'P', 42013, 'Vy', 32013, 'Vz', 22013, 'My', 12013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172013, 72013, 172013, 2013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123013, 123013, 23013, 2013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172014, 26.0, 4.75, 6.775)
    ops.node(123014, 26.0, 4.75, 8.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2014, 172014, 123014, 0.24, 28172494.4326057, 11738539.34691904, 0.00751249, 0.00352, 0.00792, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22014, 267.46109618, 0.0007618, 325.68484922, 0.02102011, 32.56848492, 0.05704531, -267.46109618, -0.0007618, -325.68484922, -0.02102011, -32.56848492, -0.05704531, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12014, 159.2503744, 0.00099401, 193.91767594, 0.01922172, 19.39176759, 0.04726284, -159.2503744, -0.00099401, -193.91767594, -0.01922172, -19.39176759, -0.04726284, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22014, 2014, 0.0, 258.30513911, 0.01523602, 258.30513911, 0.04570805, 180.81359737, -2629.97462278, 0.05, 2, 0, 72014, 23014, 2, 3)
    ops.uniaxialMaterial('LimitState', 42014, 64.57628478, 7.702e-05, 193.72885433, 0.00023105, 645.76284777, 0.00077017, -64.57628478, -7.702e-05, -193.72885433, -0.00023105, -645.76284777, -0.00077017, 0.4, 0.3, 0.003, 0.0, 0.0, 22014, 2)
    ops.limitCurve('ThreePoint', 12014, 2014, 0.0, 183.75868779, 0.0198803, 183.75868779, 0.05964089, 128.63108145, -1636.55796707, 0.05, 2, 0, 72014, 23014, 1, 3)
    ops.uniaxialMaterial('LimitState', 32014, 45.93967195, 5.479e-05, 137.81901584, 0.00016437, 459.39671948, 0.0005479, -45.93967195, -5.479e-05, -137.81901584, -0.00016437, -459.39671948, -0.0005479, 0.4, 0.3, 0.003, 0.0, 0.0, 12014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2014, 99999, 'P', 42014, 'Vy', 32014, 'Vz', 22014, 'My', 12014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172014, 72014, 172014, 2014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123014, 123014, 23014, 2014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172015, 31.8, 4.75, 6.775)
    ops.node(123015, 31.8, 4.75, 8.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2015, 172015, 123015, 0.24, 26829606.16751771, 11179002.56979905, 0.00751249, 0.00352, 0.00792, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22015, 255.02520495, 0.00071801, 311.28907098, 0.01777828, 31.1289071, 0.0529256, -255.02520495, -0.00071801, -311.28907098, -0.01777828, -31.1289071, -0.0529256, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12015, 140.25331364, 0.00092334, 171.19611261, 0.01627356, 17.11961126, 0.04363137, -140.25331364, -0.00092334, -171.19611261, -0.01627356, -17.11961126, -0.04363137, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22015, 2015, 0.0, 246.71070406, 0.01436026, 246.71070406, 0.04308078, 172.69749284, -2669.46262498, 0.05, 2, 0, 72015, 23015, 2, 3)
    ops.uniaxialMaterial('LimitState', 42015, 61.67767601, 7.724e-05, 185.03302804, 0.00023173, 616.77676014, 0.00077242, -61.67767601, -7.724e-05, -185.03302804, -0.00023173, -616.77676014, -0.00077242, 0.4, 0.3, 0.003, 0.0, 0.0, 22015, 2)
    ops.limitCurve('ThreePoint', 12015, 2015, 0.0, 175.25023294, 0.01846688, 175.25023294, 0.05540064, 122.67516306, -1657.31250858, 0.05, 2, 0, 72015, 23015, 1, 3)
    ops.uniaxialMaterial('LimitState', 32015, 43.81255823, 5.487e-05, 131.4376747, 0.00016461, 438.12558234, 0.00054869, -43.81255823, -5.487e-05, -131.4376747, -0.00016461, -438.12558234, -0.00054869, 0.4, 0.3, 0.003, 0.0, 0.0, 12015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2015, 99999, 'P', 42015, 'Vy', 32015, 'Vz', 22015, 'My', 12015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172015, 72015, 172015, 2015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123015, 123015, 23015, 2015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172016, 37.6, 4.75, 6.775)
    ops.node(123016, 37.6, 4.75, 8.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2016, 172016, 123016, 0.125, 34109029.68749252, 14212095.70312188, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22016, 134.08776672, 0.00073343, 160.4251409, 0.03097291, 16.04251409, 0.1041588, -134.08776672, -0.00073343, -160.4251409, -0.03097291, -16.04251409, -0.1041588, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12016, 58.41841296, 0.0012546, 69.89289447, 0.02536498, 6.98928945, 0.06812949, -58.41841296, -0.0012546, -69.89289447, -0.02536498, -6.98928945, -0.06812949, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22016, 2016, 0.0, 211.94773173, 0.01466859, 211.94773173, 0.04400577, 148.36341221, -5084.51111319, 0.05, 2, 0, 72016, 23016, 2, 3)
    ops.uniaxialMaterial('LimitState', 42016, 52.98693293, 0.00010022, 158.9607988, 0.00030065, 529.86932932, 0.00100217, -52.98693293, -0.00010022, -158.9607988, -0.00030065, -529.86932932, -0.00100217, 0.4, 0.3, 0.003, 0.0, 0.0, 22016, 2)
    ops.limitCurve('ThreePoint', 12016, 2016, 0.0, 146.89715711, 0.02509207, 146.89715711, 0.07527622, 102.82800997, -1873.28378905, 0.05, 2, 0, 72016, 23016, 1, 3)
    ops.uniaxialMaterial('LimitState', 32016, 36.72428928, 6.946e-05, 110.17286783, 0.00020838, 367.24289277, 0.00069458, -36.72428928, -6.946e-05, -110.17286783, -0.00020838, -367.24289277, -0.00069458, 0.4, 0.3, 0.003, 0.0, 0.0, 12016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2016, 99999, 'P', 42016, 'Vy', 32016, 'Vz', 22016, 'My', 12016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172016, 72016, 172016, 2016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123016, 123016, 23016, 2016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172017, 0.0, 9.5, 6.75)
    ops.node(123017, 0.0, 9.5, 8.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2017, 172017, 123017, 0.0625, 32875036.15571297, 13697931.73154707, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22017, 28.79110194, 0.00121708, 34.57427082, 0.01974286, 3.45742708, 0.07894695, -28.79110194, -0.00121708, -34.57427082, -0.01974286, -3.45742708, -0.07894695, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12017, 28.79110194, 0.00121708, 34.57427082, 0.01974286, 3.45742708, 0.07894695, -28.79110194, -0.00121708, -34.57427082, -0.01974286, -3.45742708, -0.07894695, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22017, 2017, 0.0, 86.10713598, 0.0243416, 86.10713598, 0.0730248, 60.27499518, -1607.87109207, 0.05, 2, 0, 72017, 23017, 2, 3)
    ops.uniaxialMaterial('LimitState', 42017, 21.52678399, 8.449e-05, 64.58035198, 0.00025346, 215.26783994, 0.00084486, -21.52678399, -8.449e-05, -64.58035198, -0.00025346, -215.26783994, -0.00084486, 0.4, 0.3, 0.003, 0.0, 0.0, 22017, 2)
    ops.limitCurve('ThreePoint', 12017, 2017, 0.0, 86.10713598, 0.0243416, 86.10713598, 0.0730248, 60.27499518, -1607.87109207, 0.05, 2, 0, 72017, 23017, 1, 3)
    ops.uniaxialMaterial('LimitState', 32017, 21.52678399, 8.449e-05, 64.58035198, 0.00025346, 215.26783994, 0.00084486, -21.52678399, -8.449e-05, -64.58035198, -0.00025346, -215.26783994, -0.00084486, 0.4, 0.3, 0.003, 0.0, 0.0, 12017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2017, 99999, 'P', 42017, 'Vy', 32017, 'Vz', 22017, 'My', 12017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172017, 72017, 172017, 2017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123017, 123017, 23017, 2017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172018, 5.8, 9.5, 6.75)
    ops.node(123018, 5.8, 9.5, 8.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2018, 172018, 123018, 0.125, 30873640.36597519, 12864016.81915633, 0.00178813, 0.00286458, 0.00071615, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22018, 52.51594893, 0.00123852, 63.46926466, 0.01701731, 6.34692647, 0.052248, -52.51594893, -0.00123852, -63.46926466, -0.01701731, -6.34692647, -0.052248, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12018, 112.24272535, 0.00072218, 135.65332795, 0.02026195, 13.56533279, 0.07876257, -112.24272535, -0.00072218, -135.65332795, -0.02026195, -13.56533279, -0.07876257, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22018, 2018, 0.0, 122.58688609, 0.02477043, 122.58688609, 0.0743113, 85.81082026, -1341.18771872, 0.05, 2, 0, 72018, 23018, 2, 3)
    ops.uniaxialMaterial('LimitState', 42018, 30.64672152, 6.404e-05, 91.94016457, 0.00019211, 306.46721522, 0.00064038, -30.64672152, -6.404e-05, -91.94016457, -0.00019211, -306.46721522, -0.00064038, 0.4, 0.3, 0.003, 0.0, 0.0, 22018, 2)
    ops.limitCurve('ThreePoint', 12018, 2018, 0.0, 173.85918036, 0.01444354, 173.85918036, 0.04333061, 121.70142625, -3330.66767454, 0.05, 2, 0, 72018, 23018, 1, 3)
    ops.uniaxialMaterial('LimitState', 32018, 43.46479509, 9.082e-05, 130.39438527, 0.00027247, 434.6479509, 0.00090822, -43.46479509, -9.082e-05, -130.39438527, -0.00027247, -434.6479509, -0.00090822, 0.4, 0.3, 0.003, 0.0, 0.0, 12018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2018, 99999, 'P', 42018, 'Vy', 32018, 'Vz', 22018, 'My', 12018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172018, 72018, 172018, 2018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123018, 123018, 23018, 2018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172019, 11.6, 9.5, 6.75)
    ops.node(123019, 11.6, 9.5, 8.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2019, 172019, 123019, 0.125, 29809683.56008601, 12420701.48336917, 0.00178813, 0.00286458, 0.00071615, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22019, 55.86937822, 0.00125124, 67.70187516, 0.01415303, 6.77018752, 0.0487996, -55.86937822, -0.00125124, -67.70187516, -0.01415303, -6.77018752, -0.0487996, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12019, 118.51578795, 0.00074572, 143.61607979, 0.01672274, 14.36160798, 0.07425342, -118.51578795, -0.00074572, -143.61607979, -0.01672274, -14.36160798, -0.07425342, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22019, 2019, 0.0, 105.92549275, 0.02502476, 105.92549275, 0.07507428, 74.14784492, -1120.8754315, 0.05, 2, 0, 72019, 23019, 2, 3)
    ops.uniaxialMaterial('LimitState', 42019, 26.48137319, 5.731e-05, 79.44411956, 0.00017193, 264.81373187, 0.00057309, -26.48137319, -5.731e-05, -79.44411956, -0.00017193, -264.81373187, -0.00057309, 0.4, 0.3, 0.003, 0.0, 0.0, 22019, 2)
    ops.limitCurve('ThreePoint', 12019, 2019, 0.0, 157.53250566, 0.01491432, 157.53250566, 0.04474295, 110.27275396, -2644.67799718, 0.05, 2, 0, 72019, 23019, 1, 3)
    ops.uniaxialMaterial('LimitState', 32019, 39.38312641, 8.523e-05, 118.14937924, 0.00025569, 393.83126415, 0.0008523, -39.38312641, -8.523e-05, -118.14937924, -0.00025569, -393.83126415, -0.0008523, 0.4, 0.3, 0.003, 0.0, 0.0, 12019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2019, 99999, 'P', 42019, 'Vy', 32019, 'Vz', 22019, 'My', 12019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172019, 72019, 172019, 2019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123019, 123019, 23019, 2019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172020, 17.4, 9.5, 6.75)
    ops.node(123020, 17.4, 9.5, 8.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2020, 172020, 123020, 0.0875, 30651788.08610618, 12771578.36921091, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22020, 40.16144027, 0.00119109, 48.55436703, 0.02004787, 4.8554367, 0.06474722, -40.16144027, -0.00119109, -48.55436703, -0.02004787, -4.8554367, -0.06474722, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12020, 63.93059345, 0.00090465, 77.29079132, 0.02193242, 7.72907913, 0.07981689, -63.93059345, -0.00090465, -77.29079132, -0.02193242, -7.72907913, -0.07981689, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22020, 2020, 0.0, 104.73010159, 0.02382184, 104.73010159, 0.07146552, 73.31107112, -1798.7038707, 0.05, 2, 0, 72020, 23020, 2, 3)
    ops.uniaxialMaterial('LimitState', 42020, 26.1825254, 7.872e-05, 78.5475762, 0.00023617, 261.82525399, 0.00078722, -26.1825254, -7.872e-05, -78.5475762, -0.00023617, -261.82525399, -0.00078722, 0.4, 0.3, 0.003, 0.0, 0.0, 22020, 2)
    ops.limitCurve('ThreePoint', 12020, 2020, 0.0, 123.37764998, 0.01809305, 123.37764998, 0.05427915, 86.36435498, -2920.49985375, 0.05, 2, 0, 72020, 23020, 1, 3)
    ops.uniaxialMaterial('LimitState', 32020, 30.84441249, 9.274e-05, 92.53323748, 0.00027822, 308.44412494, 0.00092739, -30.84441249, -9.274e-05, -92.53323748, -0.00027822, -308.44412494, -0.00092739, 0.4, 0.3, 0.003, 0.0, 0.0, 12020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2020, 99999, 'P', 42020, 'Vy', 32020, 'Vz', 22020, 'My', 12020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172020, 72020, 172020, 2020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123020, 123020, 23020, 2020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172021, 20.2, 9.5, 6.75)
    ops.node(123021, 20.2, 9.5, 8.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2021, 172021, 123021, 0.0875, 27713405.78159033, 11547252.40899597, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22021, 38.99795117, 0.00126661, 47.44004652, 0.01606031, 4.74400465, 0.05823867, -38.99795117, -0.00126661, -47.44004652, -0.01606031, -4.74400465, -0.05823867, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12021, 62.10360216, 0.00094765, 75.54750152, 0.01744455, 7.55475015, 0.07206441, -62.10360216, -0.00094765, -75.54750152, -0.01744455, -7.55475015, -0.07206441, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22021, 2021, 0.0, 76.47697222, 0.02533218, 76.47697222, 0.07599654, 53.53388056, -1156.85412435, 0.05, 2, 0, 72021, 23021, 2, 3)
    ops.uniaxialMaterial('LimitState', 42021, 19.11924306, 6.358e-05, 57.35772917, 0.00019074, 191.19243056, 0.0006358, -19.11924306, -6.358e-05, -57.35772917, -0.00019074, -191.19243056, -0.0006358, 0.4, 0.3, 0.003, 0.0, 0.0, 22021, 2)
    ops.limitCurve('ThreePoint', 12021, 2021, 0.0, 96.93694255, 0.01895291, 96.93694255, 0.05685874, 67.85585979, -1787.90707346, 0.05, 2, 0, 72021, 23021, 1, 3)
    ops.uniaxialMaterial('LimitState', 32021, 24.23423564, 8.059e-05, 72.70270692, 0.00024177, 242.34235639, 0.0008059, -24.23423564, -8.059e-05, -72.70270692, -0.00024177, -242.34235639, -0.0008059, 0.4, 0.3, 0.003, 0.0, 0.0, 12021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2021, 99999, 'P', 42021, 'Vy', 32021, 'Vz', 22021, 'My', 12021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172021, 72021, 172021, 2021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123021, 123021, 23021, 2021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172022, 26.0, 9.5, 6.75)
    ops.node(123022, 26.0, 9.5, 8.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2022, 172022, 123022, 0.125, 28408137.80361635, 11836724.08484015, 0.00178813, 0.00286458, 0.00071615, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22022, 50.77649807, 0.00125519, 61.71309421, 0.01839247, 6.17130942, 0.05213675, -50.77649807, -0.00125519, -61.71309421, -0.01839247, -6.17130942, -0.05213675, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12022, 108.75873565, 0.00072482, 132.18395035, 0.02194691, 13.21839504, 0.07797932, -108.75873565, -0.00072482, -132.18395035, -0.02194691, -13.21839504, -0.07797932, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22022, 2022, 0.0, 116.44793955, 0.02510376, 116.44793955, 0.07531129, 81.51355769, -1462.66116959, 0.05, 2, 0, 72022, 23022, 2, 3)
    ops.uniaxialMaterial('LimitState', 42022, 29.11198489, 6.611e-05, 87.33595467, 0.00019833, 291.11984889, 0.0006611, -29.11198489, -6.611e-05, -87.33595467, -0.00019833, -291.11984889, -0.0006611, 0.4, 0.3, 0.003, 0.0, 0.0, 22022, 2)
    ops.limitCurve('ThreePoint', 12022, 2022, 0.0, 169.44053721, 0.01449649, 169.44053721, 0.04348947, 118.60837605, -3715.75393668, 0.05, 2, 0, 72022, 23022, 1, 3)
    ops.uniaxialMaterial('LimitState', 32022, 42.3601343, 9.62e-05, 127.08040291, 0.00028859, 423.60134304, 0.00096196, -42.3601343, -9.62e-05, -127.08040291, -0.00028859, -423.60134304, -0.00096196, 0.4, 0.3, 0.003, 0.0, 0.0, 12022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2022, 99999, 'P', 42022, 'Vy', 32022, 'Vz', 22022, 'My', 12022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172022, 72022, 172022, 2022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123022, 123022, 23022, 2022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172023, 31.8, 9.5, 6.75)
    ops.node(123023, 31.8, 9.5, 8.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2023, 172023, 123023, 0.125, 29458187.76720933, 12274244.90300389, 0.00178813, 0.00286458, 0.00071615, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22023, 52.2228866, 0.00124645, 63.33383609, 0.01623346, 6.33338361, 0.05066893, -52.2228866, -0.00124645, -63.33383609, -0.01623346, -6.33338361, -0.05066893, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12023, 111.62143161, 0.00072704, 135.3700248, 0.01928632, 13.53700248, 0.07646645, -111.62143161, -0.00072704, -135.3700248, -0.01928632, -13.53700248, -0.07646645, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22023, 2023, 0.0, 115.70516737, 0.02492904, 115.70516737, 0.07478713, 80.99361716, -1280.69897415, 0.05, 2, 0, 72023, 23023, 2, 3)
    ops.uniaxialMaterial('LimitState', 42023, 28.92629184, 6.335e-05, 86.77887553, 0.00019004, 289.26291843, 0.00063347, -28.92629184, -6.335e-05, -86.77887553, -0.00019004, -289.26291843, -0.00063347, 0.4, 0.3, 0.003, 0.0, 0.0, 22023, 2)
    ops.limitCurve('ThreePoint', 12023, 2023, 0.0, 164.65711119, 0.01454083, 164.65711119, 0.0436225, 115.25997784, -3140.61462548, 0.05, 2, 0, 72023, 23023, 1, 3)
    ops.uniaxialMaterial('LimitState', 32023, 41.1642778, 9.015e-05, 123.4928334, 0.00027044, 411.64277799, 0.00090148, -41.1642778, -9.015e-05, -123.4928334, -0.00027044, -411.64277799, -0.00090148, 0.4, 0.3, 0.003, 0.0, 0.0, 12023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2023, 99999, 'P', 42023, 'Vy', 32023, 'Vz', 22023, 'My', 12023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172023, 72023, 172023, 2023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123023, 123023, 23023, 2023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172024, 37.6, 9.5, 6.75)
    ops.node(123024, 37.6, 9.5, 8.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2024, 172024, 123024, 0.0625, 28711573.28921484, 11963155.53717285, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22024, 30.48289052, 0.00128114, 37.00032043, 0.02069565, 3.70003204, 0.07589193, -30.48289052, -0.00128114, -37.00032043, -0.02069565, -3.70003204, -0.07589193, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12024, 30.48289052, 0.00128114, 37.00032043, 0.02069565, 3.70003204, 0.07589193, -30.48289052, -0.00128114, -37.00032043, -0.02069565, -3.70003204, -0.07589193, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22024, 2024, 0.0, 78.96234798, 0.02562288, 78.96234798, 0.07686865, 55.27364359, -1654.55982062, 0.05, 2, 0, 72024, 23024, 2, 3)
    ops.uniaxialMaterial('LimitState', 42024, 19.740587, 8.871e-05, 59.22176099, 0.00026613, 197.40586995, 0.0008871, -19.740587, -8.871e-05, -59.22176099, -0.00026613, -197.40586995, -0.0008871, 0.4, 0.3, 0.003, 0.0, 0.0, 22024, 2)
    ops.limitCurve('ThreePoint', 12024, 2024, 0.0, 78.96234798, 0.02562288, 78.96234798, 0.07686865, 55.27364359, -1654.55982062, 0.05, 2, 0, 72024, 23024, 1, 3)
    ops.uniaxialMaterial('LimitState', 32024, 19.740587, 8.871e-05, 59.22176099, 0.00026613, 197.40586995, 0.0008871, -19.740587, -8.871e-05, -59.22176099, -0.00026613, -197.40586995, -0.0008871, 0.4, 0.3, 0.003, 0.0, 0.0, 12024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2024, 99999, 'P', 42024, 'Vy', 32024, 'Vz', 22024, 'My', 12024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172024, 72024, 172024, 2024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123024, 123024, 23024, 2024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173001, 0.0, 0.0, 9.55)
    ops.node(124001, 0.0, 0.0, 11.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3001, 173001, 124001, 0.0625, 26524091.41939091, 11051704.75807955, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23001, 22.76236306, 0.00127328, 27.89444667, 0.02290398, 2.78944467, 0.08553643, -22.76236306, -0.00127328, -27.89444667, -0.02290398, -2.78944467, -0.08553643, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13001, 22.76236306, 0.00127328, 27.89444667, 0.02290398, 2.78944467, 0.08553643, -22.76236306, -0.00127328, -27.89444667, -0.02290398, -2.78944467, -0.08553643, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23001, 3001, 0.0, 67.79189562, 0.02546555, 67.79189562, 0.07639666, 47.45432693, -3556.5400256, 0.05, 2, 0, 73001, 24001, 2, 3)
    ops.uniaxialMaterial('LimitState', 43001, 16.9479739, 8.244e-05, 50.84392171, 0.00024733, 169.47973904, 0.00082442, -16.9479739, -8.244e-05, -50.84392171, -0.00024733, -169.47973904, -0.00082442, 0.4, 0.3, 0.003, 0.0, 0.0, 23001, 2)
    ops.limitCurve('ThreePoint', 13001, 3001, 0.0, 67.79189562, 0.02546555, 67.79189562, 0.07639666, 47.45432693, -3556.5400256, 0.05, 2, 0, 73001, 24001, 1, 3)
    ops.uniaxialMaterial('LimitState', 33001, 16.9479739, 8.244e-05, 50.84392171, 0.00024733, 169.47973904, 0.00082442, -16.9479739, -8.244e-05, -50.84392171, -0.00024733, -169.47973904, -0.00082442, 0.4, 0.3, 0.003, 0.0, 0.0, 13001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3001, 99999, 'P', 43001, 'Vy', 33001, 'Vz', 23001, 'My', 13001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173001, 73001, 173001, 3001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124001, 124001, 24001, 3001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173002, 5.8, 0.0, 9.55)
    ops.node(124002, 5.8, 0.0, 11.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3002, 173002, 124002, 0.125, 33340524.8414375, 13891885.35059896, 0.00178813, 0.00286458, 0.00071615, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23002, 39.93956229, 0.00113077, 48.02877274, 0.01493545, 4.80287727, 0.05406001, -39.93956229, -0.00113077, -48.02877274, -0.01493545, -4.80287727, -0.05406001, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13002, 100.84268091, 0.00068049, 121.26698256, 0.01777563, 12.12669826, 0.08274201, -100.84268091, -0.00068049, -121.26698256, -0.01777563, -12.12669826, -0.08274201, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23002, 3002, 0.0, 114.02095769, 0.02261536, 114.02095769, 0.06784608, 79.81467038, -1718.62068876, 0.05, 2, 0, 73002, 24002, 2, 3)
    ops.uniaxialMaterial('LimitState', 43002, 28.50523942, 5.516e-05, 85.51571826, 0.00016547, 285.05239421, 0.00055156, -28.50523942, -5.516e-05, -85.51571826, -0.00016547, -285.05239421, -0.00055156, 0.4, 0.3, 0.003, 0.0, 0.0, 23002, 2)
    ops.limitCurve('ThreePoint', 13002, 3002, 0.0, 161.47043889, 0.01360984, 161.47043889, 0.04082951, 113.02930722, -5562.95926917, 0.05, 2, 0, 73002, 24002, 1, 3)
    ops.uniaxialMaterial('LimitState', 33002, 40.36760972, 7.811e-05, 121.10282917, 0.00023433, 403.67609723, 0.00078109, -40.36760972, -7.811e-05, -121.10282917, -0.00023433, -403.67609723, -0.00078109, 0.4, 0.3, 0.003, 0.0, 0.0, 13002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3002, 99999, 'P', 43002, 'Vy', 33002, 'Vz', 23002, 'My', 13002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173002, 73002, 173002, 3002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124002, 124002, 24002, 3002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173003, 11.6, 0.0, 9.55)
    ops.node(124003, 11.6, 0.0, 11.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3003, 173003, 124003, 0.125, 29093011.75661206, 12122088.23192169, 0.00178813, 0.00286458, 0.00071615, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23003, 38.16120854, 0.00110609, 46.49937863, 0.0168117, 4.64993786, 0.05526733, -38.16120854, -0.00110609, -46.49937863, -0.0168117, -4.64993786, -0.05526733, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13003, 97.00106044, 0.00067301, 118.19565496, 0.02012217, 11.8195655, 0.08397779, -97.00106044, -0.00067301, -118.19565496, -0.02012217, -11.8195655, -0.08397779, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23003, 3003, 0.0, 103.05574691, 0.02212184, 103.05574691, 0.06636551, 72.13902284, -2011.77915746, 0.05, 2, 0, 73003, 24003, 2, 3)
    ops.uniaxialMaterial('LimitState', 43003, 25.76393673, 5.713e-05, 77.29181018, 0.00017139, 257.63936728, 0.0005713, -25.76393673, -5.713e-05, -77.29181018, -0.00017139, -257.63936728, -0.0005713, 0.4, 0.3, 0.003, 0.0, 0.0, 23003, 2)
    ops.limitCurve('ThreePoint', 13003, 3003, 0.0, 149.88889474, 0.01346018, 149.88889474, 0.04038055, 104.92222632, -6622.45540088, 0.05, 2, 0, 73003, 24003, 1, 3)
    ops.uniaxialMaterial('LimitState', 33003, 37.47222369, 8.309e-05, 112.41667106, 0.00024928, 374.72223686, 0.00083092, -37.47222369, -8.309e-05, -112.41667106, -0.00024928, -374.72223686, -0.00083092, 0.4, 0.3, 0.003, 0.0, 0.0, 13003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3003, 99999, 'P', 43003, 'Vy', 33003, 'Vz', 23003, 'My', 13003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173003, 73003, 173003, 3003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124003, 124003, 24003, 3003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173006, 26.0, 0.0, 9.55)
    ops.node(124006, 26.0, 0.0, 11.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3006, 173006, 124006, 0.125, 29369354.30670407, 12237230.96112669, 0.00178813, 0.00286458, 0.00071615, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23006, 39.11857881, 0.00119242, 47.63175698, 0.01614909, 4.7631757, 0.0546611, -39.11857881, -0.00119242, -47.63175698, -0.01614909, -4.7631757, -0.0546611, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13006, 99.12844926, 0.00070345, 120.70127156, 0.01922514, 12.07012716, 0.08317441, -99.12844926, -0.00070345, -120.70127156, -0.01922514, -12.07012716, -0.08317441, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23006, 3006, 0.0, 99.7471805, 0.02384836, 99.7471805, 0.07154509, 69.82302635, -1797.9713394, 0.05, 2, 0, 73006, 24006, 2, 3)
    ops.uniaxialMaterial('LimitState', 43006, 24.93679512, 5.478e-05, 74.81038537, 0.00016433, 249.36795124, 0.00054776, -24.93679512, -5.478e-05, -74.81038537, -0.00016433, -249.36795124, -0.00054776, 0.4, 0.3, 0.003, 0.0, 0.0, 23006, 2)
    ops.limitCurve('ThreePoint', 13006, 3006, 0.0, 146.12744745, 0.0140689, 146.12744745, 0.0422067, 102.28921322, -5848.8434938, 0.05, 2, 0, 73006, 24006, 1, 3)
    ops.uniaxialMaterial('LimitState', 33006, 36.53186186, 8.024e-05, 109.59558559, 0.00024073, 365.31861863, 0.00080245, -36.53186186, -8.024e-05, -109.59558559, -0.00024073, -365.31861863, -0.00080245, 0.4, 0.3, 0.003, 0.0, 0.0, 13006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3006, 99999, 'P', 43006, 'Vy', 33006, 'Vz', 23006, 'My', 13006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173006, 73006, 173006, 3006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124006, 124006, 24006, 3006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173007, 31.8, 0.0, 9.55)
    ops.node(124007, 31.8, 0.0, 11.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3007, 173007, 124007, 0.125, 28556396.76498147, 11898498.65207561, 0.00178813, 0.00286458, 0.00071615, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23007, 39.56087078, 0.00116281, 48.26945434, 0.01897333, 4.82694543, 0.05731283, -39.56087078, -0.00116281, -48.26945434, -0.01897333, -4.82694543, -0.05731283, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13007, 100.71568879, 0.00070004, 122.8863583, 0.02275582, 12.28863583, 0.08641862, -100.71568879, -0.00070004, -122.8863583, -0.02275582, -12.28863583, -0.08641862, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23007, 3007, 0.0, 105.61371144, 0.02325615, 105.61371144, 0.06976844, 73.92959801, -2368.31553724, 0.05, 2, 0, 73007, 24007, 2, 3)
    ops.uniaxialMaterial('LimitState', 43007, 26.40342786, 5.965e-05, 79.21028358, 0.00017894, 264.0342786, 0.00059648, -26.40342786, -5.965e-05, -79.21028358, -0.00017894, -264.0342786, -0.00059648, 0.4, 0.3, 0.003, 0.0, 0.0, 23007, 2)
    ops.limitCurve('ThreePoint', 13007, 3007, 0.0, 155.31965966, 0.0140007, 155.31965966, 0.04200211, 108.72376176, -7921.61095378, 0.05, 2, 0, 73007, 24007, 1, 3)
    ops.uniaxialMaterial('LimitState', 33007, 38.82991492, 8.772e-05, 116.48974475, 0.00026316, 388.29914916, 0.00087721, -38.82991492, -8.772e-05, -116.48974475, -0.00026316, -388.29914916, -0.00087721, 0.4, 0.3, 0.003, 0.0, 0.0, 13007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3007, 99999, 'P', 43007, 'Vy', 33007, 'Vz', 23007, 'My', 13007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173007, 73007, 173007, 3007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124007, 124007, 24007, 3007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173008, 37.6, 0.0, 9.55)
    ops.node(124008, 37.6, 0.0, 11.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3008, 173008, 124008, 0.0625, 28238947.50153174, 11766228.12563823, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23008, 22.86251199, 0.00116554, 27.91470112, 0.0232905, 2.79147011, 0.08671381, -22.86251199, -0.00116554, -27.91470112, -0.0232905, -2.79147011, -0.08671381, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13008, 22.86251199, 0.00116554, 27.91470112, 0.0232905, 2.79147011, 0.08671381, -22.86251199, -0.00116554, -27.91470112, -0.0232905, -2.79147011, -0.08671381, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23008, 3008, 0.0, 75.48025268, 0.02331075, 75.48025268, 0.06993224, 52.83617687, -4378.91656551, 0.05, 2, 0, 73008, 24008, 2, 3)
    ops.uniaxialMaterial('LimitState', 43008, 18.87006317, 8.622e-05, 56.61018951, 0.00025865, 188.70063169, 0.00086217, -18.87006317, -8.622e-05, -56.61018951, -0.00025865, -188.70063169, -0.00086217, 0.4, 0.3, 0.003, 0.0, 0.0, 23008, 2)
    ops.limitCurve('ThreePoint', 13008, 3008, 0.0, 75.48025268, 0.02331075, 75.48025268, 0.06993224, 52.83617687, -4378.91656551, 0.05, 2, 0, 73008, 24008, 1, 3)
    ops.uniaxialMaterial('LimitState', 33008, 18.87006317, 8.622e-05, 56.61018951, 0.00025865, 188.70063169, 0.00086217, -18.87006317, -8.622e-05, -56.61018951, -0.00025865, -188.70063169, -0.00086217, 0.4, 0.3, 0.003, 0.0, 0.0, 13008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3008, 99999, 'P', 43008, 'Vy', 33008, 'Vz', 23008, 'My', 13008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173008, 73008, 173008, 3008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124008, 124008, 24008, 3008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173009, 0.0, 4.75, 9.575)
    ops.node(124009, 0.0, 4.75, 11.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3009, 173009, 124009, 0.125, 28849828.05117931, 12020761.68799138, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23009, 113.61573415, 0.0007397, 138.52518004, 0.02015096, 13.852518, 0.07543063, -113.61573415, -0.0007397, -138.52518004, -0.02015096, -13.852518, -0.07543063, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13009, 48.48220559, 0.00125334, 59.11158616, 0.01710716, 5.91115862, 0.05130601, -48.48220559, -0.00125334, -59.11158616, -0.01710716, -5.91115862, -0.05130601, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23009, 3009, 0.0, 137.4908315, 0.014794, 137.4908315, 0.04438199, 96.24358205, -4886.39189187, 0.05, 2, 0, 73009, 24009, 2, 3)
    ops.uniaxialMaterial('LimitState', 43009, 34.37270788, 7.686e-05, 103.11812363, 0.00023059, 343.72707876, 0.00076862, -34.37270788, -7.686e-05, -103.11812363, -0.00023059, -343.72707876, -0.00076862, 0.4, 0.3, 0.003, 0.0, 0.0, 23009, 2)
    ops.limitCurve('ThreePoint', 13009, 3009, 0.0, 76.10639685, 0.02506686, 76.10639685, 0.07520057, 53.2744778, -1530.47145047, 0.05, 2, 0, 73009, 24009, 1, 3)
    ops.uniaxialMaterial('LimitState', 33009, 19.02659921, 4.255e-05, 57.07979764, 0.00012764, 190.26599213, 0.00042546, -19.02659921, -4.255e-05, -57.07979764, -0.00012764, -190.26599213, -0.00042546, 0.4, 0.3, 0.003, 0.0, 0.0, 13009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3009, 99999, 'P', 43009, 'Vy', 33009, 'Vz', 23009, 'My', 13009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173009, 73009, 173009, 3009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124009, 124009, 24009, 3009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173010, 5.8, 4.75, 9.575)
    ops.node(124010, 5.8, 4.75, 11.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3010, 173010, 124010, 0.24, 31096026.82304648, 12956677.84293604, 0.00751249, 0.00352, 0.00792, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23010, 214.76772811, 0.00065, 260.26405129, 0.02006283, 26.02640513, 0.06012765, -214.76772811, -0.00065, -260.26405129, -0.02006283, -26.02640513, -0.06012765, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13010, 115.60144503, 0.00081782, 140.09041621, 0.01828479, 14.00904162, 0.04947026, -115.60144503, -0.00081782, -140.09041621, -0.01828479, -14.00904162, -0.04947026, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23010, 3010, 0.0, 281.84683228, 0.01300006, 281.84683228, 0.03900019, 197.2927826, -6017.23866361, 0.05, 2, 0, 73010, 24010, 2, 3)
    ops.uniaxialMaterial('LimitState', 43010, 70.46170807, 7.614e-05, 211.38512421, 0.00022841, 704.61708071, 0.00076136, -70.46170807, -7.614e-05, -211.38512421, -0.00022841, -704.61708071, -0.00076136, 0.4, 0.3, 0.003, 0.0, 0.0, 23010, 2)
    ops.limitCurve('ThreePoint', 13010, 3010, 0.0, 200.08675064, 0.01635648, 200.08675064, 0.04906945, 140.06072545, -3060.28447945, 0.05, 2, 0, 73010, 24010, 1, 3)
    ops.uniaxialMaterial('LimitState', 33010, 50.02168766, 5.405e-05, 150.06506298, 0.00016215, 500.21687661, 0.0005405, -50.02168766, -5.405e-05, -150.06506298, -0.00016215, -500.21687661, -0.0005405, 0.4, 0.3, 0.003, 0.0, 0.0, 13010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3010, 99999, 'P', 43010, 'Vy', 33010, 'Vz', 23010, 'My', 13010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173010, 73010, 173010, 3010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124010, 124010, 24010, 3010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173011, 11.6, 4.75, 9.575)
    ops.node(124011, 11.6, 4.75, 11.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3011, 173011, 124011, 0.24, 30488544.4621688, 12703560.19257033, 0.00751249, 0.00352, 0.00792, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23011, 216.94087492, 0.00066848, 263.3781748, 0.01448606, 26.33781748, 0.04781178, -216.94087492, -0.00066848, -263.3781748, -0.01448606, -26.33781748, -0.04781178, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13011, 127.80574633, 0.00084796, 155.16321767, 0.01343344, 15.51632177, 0.04013661, -127.80574633, -0.00084796, -155.16321767, -0.01343344, -15.51632177, -0.04013661, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23011, 3011, 0.0, 240.49739702, 0.01336966, 240.49739702, 0.04010899, 168.34817791, -2539.62843823, 0.05, 2, 0, 73011, 24011, 2, 3)
    ops.uniaxialMaterial('LimitState', 43011, 60.12434926, 6.626e-05, 180.37304777, 0.00019878, 601.24349255, 0.0006626, -60.12434926, -6.626e-05, -180.37304777, -0.00019878, -601.24349255, -0.0006626, 0.4, 0.3, 0.003, 0.0, 0.0, 23011, 2)
    ops.limitCurve('ThreePoint', 13011, 3011, 0.0, 165.95434079, 0.01695923, 165.95434079, 0.05087769, 116.16803855, -1384.0196138, 0.05, 2, 0, 73011, 24011, 1, 3)
    ops.uniaxialMaterial('LimitState', 33011, 41.4885852, 4.572e-05, 124.46575559, 0.00013717, 414.88585197, 0.00045723, -41.4885852, -4.572e-05, -124.46575559, -0.00013717, -414.88585197, -0.00045723, 0.4, 0.3, 0.003, 0.0, 0.0, 13011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3011, 99999, 'P', 43011, 'Vy', 33011, 'Vz', 23011, 'My', 13011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173011, 73011, 173011, 3011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124011, 124011, 24011, 3011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173012, 17.4, 4.75, 9.575)
    ops.node(124012, 17.4, 4.75, 11.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3012, 173012, 124012, 0.175, 28815020.79176477, 12006258.66323532, 0.00405757, 0.0019651, 0.00401042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23012, 132.32911348, 0.00072858, 161.32517533, 0.01786722, 16.13251753, 0.06082765, -132.32911348, -0.00072858, -161.32517533, -0.01786722, -16.13251753, -0.06082765, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13012, 79.82185194, 0.00092829, 97.31248038, 0.01645789, 9.73124804, 0.05045989, -79.82185194, -0.00092829, -97.31248038, -0.01645789, -9.73124804, -0.05045989, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23012, 3012, 0.0, 163.12019335, 0.01457155, 163.12019335, 0.04371464, 114.18413534, -3085.82215864, 0.05, 2, 0, 73012, 24012, 2, 3)
    ops.uniaxialMaterial('LimitState', 43012, 40.78004834, 6.521e-05, 122.34014501, 0.00019564, 407.80048336, 0.00065214, -40.78004834, -6.521e-05, -122.34014501, -0.00019564, -407.80048336, -0.00065214, 0.4, 0.3, 0.003, 0.0, 0.0, 23012, 2)
    ops.limitCurve('ThreePoint', 13012, 3012, 0.0, 132.83904426, 0.01856584, 132.83904426, 0.05569752, 92.98733098, -1764.8069653, 0.05, 2, 0, 73012, 24012, 1, 3)
    ops.uniaxialMaterial('LimitState', 33012, 33.20976107, 5.311e-05, 99.6292832, 0.00015932, 332.09761066, 0.00053108, -33.20976107, -5.311e-05, -99.6292832, -0.00015932, -332.09761066, -0.00053108, 0.4, 0.3, 0.003, 0.0, 0.0, 13012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3012, 99999, 'P', 43012, 'Vy', 33012, 'Vz', 23012, 'My', 13012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173012, 73012, 173012, 3012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124012, 124012, 24012, 3012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173013, 20.2, 4.75, 9.575)
    ops.node(124013, 20.2, 4.75, 11.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3013, 173013, 124013, 0.175, 25682464.47562659, 10701026.86484441, 0.00405757, 0.0019651, 0.00401042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23013, 140.07075327, 0.00076357, 171.88230911, 0.02017675, 17.18823091, 0.06205627, -140.07075327, -0.00076357, -171.88230911, -0.02017675, -17.18823091, -0.06205627, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13013, 84.22972599, 0.00096739, 103.35919142, 0.01855797, 10.33591914, 0.05170447, -84.22972599, -0.00096739, -103.35919142, -0.01855797, -10.33591914, -0.05170447, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23013, 3013, 0.0, 151.94564783, 0.01527144, 151.94564783, 0.04581433, 106.36195348, -3659.20938929, 0.05, 2, 0, 73013, 24013, 2, 3)
    ops.uniaxialMaterial('LimitState', 43013, 37.98641196, 6.816e-05, 113.95923587, 0.00020447, 379.86411957, 0.00068156, -37.98641196, -6.816e-05, -113.95923587, -0.00020447, -379.86411957, -0.00068156, 0.4, 0.3, 0.003, 0.0, 0.0, 23013, 2)
    ops.limitCurve('ThreePoint', 13013, 3013, 0.0, 121.97847679, 0.01934772, 121.97847679, 0.05804316, 85.38493375, -2067.38097115, 0.05, 2, 0, 73013, 24013, 1, 3)
    ops.uniaxialMaterial('LimitState', 33013, 30.4946192, 5.471e-05, 91.48385759, 0.00016414, 304.94619197, 0.00054714, -30.4946192, -5.471e-05, -91.48385759, -0.00016414, -304.94619197, -0.00054714, 0.4, 0.3, 0.003, 0.0, 0.0, 13013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3013, 99999, 'P', 43013, 'Vy', 33013, 'Vz', 23013, 'My', 13013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173013, 73013, 173013, 3013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124013, 124013, 24013, 3013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173014, 26.0, 4.75, 9.575)
    ops.node(124014, 26.0, 4.75, 11.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3014, 173014, 124014, 0.24, 30854831.70625789, 12856179.87760746, 0.00751249, 0.00352, 0.00792, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23014, 217.54869691, 0.00066588, 263.82836548, 0.01515168, 26.38283655, 0.04852362, -217.54869691, -0.00066588, -263.82836548, -0.01515168, -26.38283655, -0.04852362, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13014, 128.21680667, 0.00084336, 155.49268284, 0.01403748, 15.54926828, 0.04077768, -128.21680667, -0.00084336, -155.49268284, -0.01403748, -15.54926828, -0.04077768, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23014, 3014, 0.0, 245.87082391, 0.01331767, 245.87082391, 0.03995302, 172.10957673, -2678.16047155, 0.05, 2, 0, 73014, 24014, 2, 3)
    ops.uniaxialMaterial('LimitState', 43014, 61.46770598, 6.694e-05, 184.40311793, 0.00020081, 614.67705977, 0.00066937, -61.46770598, -6.694e-05, -184.40311793, -0.00020081, -614.67705977, -0.00066937, 0.4, 0.3, 0.003, 0.0, 0.0, 23014, 2)
    ops.limitCurve('ThreePoint', 13014, 3014, 0.0, 174.97817751, 0.01686718, 174.97817751, 0.05060155, 122.48472425, -1452.10998672, 0.05, 2, 0, 73014, 24014, 1, 3)
    ops.uniaxialMaterial('LimitState', 33014, 43.74454438, 4.764e-05, 131.23363313, 0.00014291, 437.44544376, 0.00047637, -43.74454438, -4.764e-05, -131.23363313, -0.00014291, -437.44544376, -0.00047637, 0.4, 0.3, 0.003, 0.0, 0.0, 13014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3014, 99999, 'P', 43014, 'Vy', 33014, 'Vz', 23014, 'My', 13014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173014, 73014, 173014, 3014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124014, 124014, 24014, 3014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173015, 31.8, 4.75, 9.575)
    ops.node(124015, 31.8, 4.75, 11.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3015, 173015, 124015, 0.24, 28288923.7208566, 11787051.55035692, 0.00751249, 0.00352, 0.00792, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23015, 230.62018504, 0.00069176, 281.62664079, 0.01942969, 28.16266408, 0.05900354, -230.62018504, -0.00069176, -281.62664079, -0.01942969, -28.16266408, -0.05900354, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13015, 123.27325882, 0.00087357, 150.53770673, 0.01773329, 15.05377067, 0.04853659, -123.27325882, -0.00087357, -150.53770673, -0.01773329, -15.05377067, -0.04853659, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23015, 3015, 0.0, 250.61081575, 0.01383526, 250.61081575, 0.04150579, 175.42757102, -5530.7361912, 0.05, 2, 0, 73015, 24015, 2, 3)
    ops.uniaxialMaterial('LimitState', 43015, 62.65270394, 7.442e-05, 187.95811181, 0.00022325, 626.52703937, 0.00074415, -62.65270394, -7.442e-05, -187.95811181, -0.00022325, -626.52703937, -0.00074415, 0.4, 0.3, 0.003, 0.0, 0.0, 23015, 2)
    ops.limitCurve('ThreePoint', 13015, 3015, 0.0, 177.57078445, 0.01747139, 177.57078445, 0.05241416, 124.29954912, -2828.66651727, 0.05, 2, 0, 73015, 24015, 1, 3)
    ops.uniaxialMaterial('LimitState', 33015, 44.39269611, 5.273e-05, 133.17808834, 0.00015818, 443.92696113, 0.00052727, -44.39269611, -5.273e-05, -133.17808834, -0.00015818, -443.92696113, -0.00052727, 0.4, 0.3, 0.003, 0.0, 0.0, 13015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3015, 99999, 'P', 43015, 'Vy', 33015, 'Vz', 23015, 'My', 13015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173015, 73015, 173015, 3015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124015, 124015, 24015, 3015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173016, 37.6, 4.75, 9.575)
    ops.node(124016, 37.6, 4.75, 11.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3016, 173016, 124016, 0.125, 29721660.9941299, 12384025.41422079, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23016, 112.14644921, 0.00072772, 136.42314396, 0.02058429, 13.6423144, 0.07611902, -112.14644921, -0.00072772, -136.42314396, -0.02058429, -13.6423144, -0.07611902, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13016, 47.82267368, 0.00123309, 58.17499833, 0.01745061, 5.81749983, 0.05180725, -47.82267368, -0.00123309, -58.17499833, -0.01745061, -5.81749983, -0.05180725, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23016, 3016, 0.0, 141.53302415, 0.01455447, 141.53302415, 0.04366342, 99.0731169, -4945.72135883, 0.05, 2, 0, 73016, 24016, 2, 3)
    ops.uniaxialMaterial('LimitState', 43016, 35.38325604, 7.68e-05, 106.14976811, 0.0002304, 353.83256036, 0.00076801, -35.38325604, -7.68e-05, -106.14976811, -0.0002304, -353.83256036, -0.00076801, 0.4, 0.3, 0.003, 0.0, 0.0, 23016, 2)
    ops.limitCurve('ThreePoint', 13016, 3016, 0.0, 82.72232235, 0.02466185, 82.72232235, 0.07398556, 57.90562564, -1547.06805443, 0.05, 2, 0, 73016, 24016, 1, 3)
    ops.uniaxialMaterial('LimitState', 33016, 20.68058059, 4.489e-05, 62.04174176, 0.00013466, 206.80580587, 0.00044888, -20.68058059, -4.489e-05, -62.04174176, -0.00013466, -206.80580587, -0.00044888, 0.4, 0.3, 0.003, 0.0, 0.0, 13016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3016, 99999, 'P', 43016, 'Vy', 33016, 'Vz', 23016, 'My', 13016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173016, 73016, 173016, 3016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124016, 124016, 24016, 3016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173017, 0.0, 9.5, 9.55)
    ops.node(124017, 0.0, 9.5, 11.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3017, 173017, 124017, 0.0625, 26109851.63553866, 10879104.84814111, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23017, 23.72202476, 0.00120197, 29.09312783, 0.02478445, 2.90931278, 0.08719266, -23.72202476, -0.00120197, -29.09312783, -0.02478445, -2.90931278, -0.08719266, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13017, 23.72202476, 0.00120197, 29.09312783, 0.02478445, 2.90931278, 0.08719266, -23.72202476, -0.00120197, -29.09312783, -0.02478445, -2.90931278, -0.08719266, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23017, 3017, 0.0, 74.21787683, 0.02403939, 74.21787683, 0.07211818, 51.95251378, -4834.21620839, 0.05, 2, 0, 73017, 24017, 2, 3)
    ops.uniaxialMaterial('LimitState', 43017, 18.55446921, 9.169e-05, 55.66340763, 0.00027507, 185.54469208, 0.00091688, -18.55446921, -9.169e-05, -55.66340763, -0.00027507, -185.54469208, -0.00091688, 0.4, 0.3, 0.003, 0.0, 0.0, 23017, 2)
    ops.limitCurve('ThreePoint', 13017, 3017, 0.0, 74.21787683, 0.02403939, 74.21787683, 0.07211818, 51.95251378, -4834.21620839, 0.05, 2, 0, 73017, 24017, 1, 3)
    ops.uniaxialMaterial('LimitState', 33017, 18.55446921, 9.169e-05, 55.66340763, 0.00027507, 185.54469208, 0.00091688, -18.55446921, -9.169e-05, -55.66340763, -0.00027507, -185.54469208, -0.00091688, 0.4, 0.3, 0.003, 0.0, 0.0, 13017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3017, 99999, 'P', 43017, 'Vy', 33017, 'Vz', 23017, 'My', 13017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173017, 73017, 173017, 3017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124017, 124017, 24017, 3017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173018, 5.8, 9.5, 9.55)
    ops.node(124018, 5.8, 9.5, 11.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3018, 173018, 124018, 0.125, 30098005.68731456, 12540835.70304773, 0.00178813, 0.00286458, 0.00071615, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23018, 39.79756395, 0.00117561, 48.36253185, 0.01832158, 4.83625319, 0.05697212, -39.79756395, -0.00117561, -48.36253185, -0.01832158, -4.83625319, -0.05697212, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13018, 100.94756342, 0.00070085, 122.67282884, 0.02193369, 12.26728288, 0.08611298, -100.94756342, -0.00070085, -122.67282884, -0.02193369, -12.26728288, -0.08611298, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23018, 3018, 0.0, 111.0490835, 0.02351217, 111.0490835, 0.07053652, 77.73435845, -2352.06864005, 0.05, 2, 0, 73018, 24018, 2, 3)
    ops.uniaxialMaterial('LimitState', 43018, 27.76227088, 5.951e-05, 83.28681263, 0.00017852, 277.62270875, 0.00059506, -27.76227088, -5.951e-05, -83.28681263, -0.00017852, -277.62270875, -0.00059506, 0.4, 0.3, 0.003, 0.0, 0.0, 23018, 2)
    ops.limitCurve('ThreePoint', 13018, 3018, 0.0, 161.3880116, 0.01401708, 161.3880116, 0.04205123, 112.97160812, -7862.19303053, 0.05, 2, 0, 73018, 24018, 1, 3)
    ops.uniaxialMaterial('LimitState', 33018, 40.3470029, 8.648e-05, 121.0410087, 0.00025944, 403.47002899, 0.0008648, -40.3470029, -8.648e-05, -121.0410087, -0.00025944, -403.47002899, -0.0008648, 0.4, 0.3, 0.003, 0.0, 0.0, 13018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3018, 99999, 'P', 43018, 'Vy', 33018, 'Vz', 23018, 'My', 13018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173018, 73018, 173018, 3018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124018, 124018, 24018, 3018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173019, 11.6, 9.5, 9.55)
    ops.node(124019, 11.6, 9.5, 11.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3019, 173019, 124019, 0.125, 28852692.34581239, 12021955.1440885, 0.00178813, 0.00286458, 0.00071615, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23019, 38.81951017, 0.00124476, 47.33030565, 0.01767912, 4.73303056, 0.05608385, -38.81951017, -0.00124476, -47.33030565, -0.01767912, -4.73303056, -0.05608385, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13019, 97.9214584, 0.00071707, 119.38977426, 0.02106868, 11.93897743, 0.08483979, -97.9214584, -0.00071707, -119.38977426, -0.02106868, -11.93897743, -0.08483979, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23019, 3019, 0.0, 104.70681003, 0.02489518, 104.70681003, 0.07468555, 73.29476702, -2180.81033114, 0.05, 2, 0, 73019, 24019, 2, 3)
    ops.uniaxialMaterial('LimitState', 43019, 26.17670251, 5.853e-05, 78.53010752, 0.00017559, 261.76702508, 0.00058529, -26.17670251, -5.853e-05, -78.53010752, -0.00017559, -261.76702508, -0.00058529, 0.4, 0.3, 0.003, 0.0, 0.0, 23019, 2)
    ops.limitCurve('ThreePoint', 13019, 3019, 0.0, 152.59580598, 0.01434144, 152.59580598, 0.04302431, 106.81706419, -7237.08214481, 0.05, 2, 0, 73019, 24019, 1, 3)
    ops.uniaxialMaterial('LimitState', 33019, 38.1489515, 8.53e-05, 114.44685449, 0.00025589, 381.48951496, 0.00085298, -38.1489515, -8.53e-05, -114.44685449, -0.00025589, -381.48951496, -0.00085298, 0.4, 0.3, 0.003, 0.0, 0.0, 13019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3019, 99999, 'P', 43019, 'Vy', 33019, 'Vz', 23019, 'My', 13019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173019, 73019, 173019, 3019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124019, 124019, 24019, 3019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173020, 17.4, 9.5, 9.55)
    ops.node(124020, 17.4, 9.5, 11.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3020, 173020, 124020, 0.0875, 29338774.27776011, 12224489.28240005, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23020, 30.41034318, 0.00122903, 37.02933502, 0.0191987, 3.7029335, 0.06849288, -30.41034318, -0.00122903, -37.02933502, -0.0191987, -3.7029335, -0.06849288, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13020, 49.14733501, 0.00090896, 59.84454442, 0.02094749, 5.98445444, 0.08478214, -49.14733501, -0.00090896, -59.84454442, -0.02094749, -5.98445444, -0.08478214, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23020, 3020, 0.0, 86.04431914, 0.02458053, 86.04431914, 0.0737416, 60.23102339, -2707.36961112, 0.05, 2, 0, 73020, 24020, 2, 3)
    ops.uniaxialMaterial('LimitState', 43020, 21.51107978, 6.757e-05, 64.53323935, 0.00020271, 215.11079784, 0.00067571, -21.51107978, -6.757e-05, -64.53323935, -0.00020271, -215.11079784, -0.00067571, 0.4, 0.3, 0.003, 0.0, 0.0, 23020, 2)
    ops.limitCurve('ThreePoint', 13020, 3020, 0.0, 101.36916826, 0.01817926, 101.36916826, 0.05453779, 70.95841778, -4901.30999309, 0.05, 2, 0, 73020, 24020, 1, 3)
    ops.uniaxialMaterial('LimitState', 33020, 25.34229207, 7.961e-05, 76.0268762, 0.00023882, 253.42292065, 0.00079606, -25.34229207, -7.961e-05, -76.0268762, -0.00023882, -253.42292065, -0.00079606, 0.4, 0.3, 0.003, 0.0, 0.0, 13020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3020, 99999, 'P', 43020, 'Vy', 33020, 'Vz', 23020, 'My', 13020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173020, 73020, 173020, 3020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124020, 124020, 24020, 3020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173021, 20.2, 9.5, 9.55)
    ops.node(124021, 20.2, 9.5, 11.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3021, 173021, 124021, 0.0875, 28975582.9105846, 12073159.54607692, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23021, 30.70975308, 0.00117811, 37.42884384, 0.01696579, 3.74288438, 0.06616066, -30.70975308, -0.00117811, -37.42884384, -0.01696579, -3.74288438, -0.06616066, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13021, 49.8931394, 0.0008847, 60.80942814, 0.01849003, 6.08094281, 0.08219607, -49.8931394, -0.0008847, -60.80942814, -0.01849003, -6.08094281, -0.08219607, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23021, 3021, 0.0, 72.12049983, 0.02356211, 72.12049983, 0.07068634, 50.48434988, -2126.89314211, 0.05, 2, 0, 73021, 24021, 2, 3)
    ops.uniaxialMaterial('LimitState', 43021, 18.03012496, 5.735e-05, 54.09037488, 0.00017204, 180.30124959, 0.00057347, -18.03012496, -5.735e-05, -54.09037488, -0.00017204, -180.30124959, -0.00057347, 0.4, 0.3, 0.003, 0.0, 0.0, 23021, 2)
    ops.limitCurve('ThreePoint', 13021, 3021, 0.0, 93.39029137, 0.01769399, 93.39029137, 0.05308198, 65.37320396, -3810.53893031, 0.05, 2, 0, 73021, 24021, 1, 3)
    ops.uniaxialMaterial('LimitState', 33021, 23.34757284, 7.426e-05, 70.04271853, 0.00022278, 233.47572844, 0.0007426, -23.34757284, -7.426e-05, -70.04271853, -0.00022278, -233.47572844, -0.0007426, 0.4, 0.3, 0.003, 0.0, 0.0, 13021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3021, 99999, 'P', 43021, 'Vy', 33021, 'Vz', 23021, 'My', 13021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173021, 73021, 173021, 3021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124021, 124021, 24021, 3021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173022, 26.0, 9.5, 9.55)
    ops.node(124022, 26.0, 9.5, 11.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3022, 173022, 124022, 0.125, 28684934.03595847, 11952055.84831603, 0.00178813, 0.00286458, 0.00071615, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23022, 39.56619059, 0.00116861, 48.26077467, 0.01529806, 4.82607747, 0.0536662, -39.56619059, -0.00116861, -48.26077467, -0.01529806, -4.82607747, -0.0536662, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13022, 100.68418244, 0.00070145, 122.80931192, 0.01819876, 12.28093119, 0.08190912, -100.68418244, -0.00070145, -122.80931192, -0.01819876, -12.28093119, -0.08190912, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23022, 3022, 0.0, 90.90842326, 0.02337222, 90.90842326, 0.07011665, 63.63589628, -1753.8929133, 0.05, 2, 0, 73022, 24022, 2, 3)
    ops.uniaxialMaterial('LimitState', 43022, 22.72710582, 5.111e-05, 68.18131745, 0.00015334, 227.27105815, 0.00051113, -22.72710582, -5.111e-05, -68.18131745, -0.00015334, -227.27105815, -0.00051113, 0.4, 0.3, 0.003, 0.0, 0.0, 23022, 2)
    ops.limitCurve('ThreePoint', 13022, 3022, 0.0, 142.25657214, 0.01402906, 142.25657214, 0.04208717, 99.5796005, -5689.94998289, 0.05, 2, 0, 73022, 24022, 1, 3)
    ops.uniaxialMaterial('LimitState', 33022, 35.56414303, 7.998e-05, 106.6924291, 0.00023995, 355.64143034, 0.00079983, -35.56414303, -7.998e-05, -106.6924291, -0.00023995, -355.64143034, -0.00079983, 0.4, 0.3, 0.003, 0.0, 0.0, 13022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3022, 99999, 'P', 43022, 'Vy', 33022, 'Vz', 23022, 'My', 13022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173022, 73022, 173022, 3022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124022, 124022, 24022, 3022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173023, 31.8, 9.5, 9.55)
    ops.node(124023, 31.8, 9.5, 11.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3023, 173023, 124023, 0.125, 29578212.84340128, 12324255.3514172, 0.00178813, 0.00286458, 0.00071615, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23023, 40.11408589, 0.00107901, 48.81682613, 0.0190628, 4.88168261, 0.05761599, -40.11408589, -0.00107901, -48.81682613, -0.0190628, -4.88168261, -0.05761599, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13023, 102.0023363, 0.00067358, 124.13171598, 0.02294394, 12.4131716, 0.08696157, -102.0023363, -0.00067358, -124.13171598, -0.02294394, -12.4131716, -0.08696157, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23023, 3023, 0.0, 109.91551028, 0.02158024, 109.91551028, 0.06474071, 76.9408572, -2427.97004516, 0.05, 2, 0, 73023, 24023, 2, 3)
    ops.uniaxialMaterial('LimitState', 43023, 27.47887757, 5.993e-05, 82.43663271, 0.0001798, 274.7887757, 0.00059933, -27.47887757, -5.993e-05, -82.43663271, -0.0001798, -274.7887757, -0.00059933, 0.4, 0.3, 0.003, 0.0, 0.0, 23023, 2)
    ops.limitCurve('ThreePoint', 13023, 3023, 0.0, 160.75872736, 0.01347164, 160.75872736, 0.04041492, 112.53110916, -8139.94067585, 0.05, 2, 0, 73023, 24023, 1, 3)
    ops.uniaxialMaterial('LimitState', 33023, 40.18968184, 8.766e-05, 120.56904552, 0.00026297, 401.89681841, 0.00087656, -40.18968184, -8.766e-05, -120.56904552, -0.00026297, -401.89681841, -0.00087656, 0.4, 0.3, 0.003, 0.0, 0.0, 13023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3023, 99999, 'P', 43023, 'Vy', 33023, 'Vz', 23023, 'My', 13023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173023, 73023, 173023, 3023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124023, 124023, 24023, 3023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173024, 37.6, 9.5, 9.55)
    ops.node(124024, 37.6, 9.5, 11.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3024, 173024, 124024, 0.0625, 32946150.86175956, 13727562.85906648, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23024, 23.35409971, 0.00116793, 28.12316544, 0.02073578, 2.81231654, 0.08555119, -23.35409971, -0.00116793, -28.12316544, -0.02073578, -2.81231654, -0.08555119, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13024, 23.35409971, 0.00116793, 28.12316544, 0.02073578, 2.81231654, 0.08555119, -23.35409971, -0.00116793, -28.12316544, -0.02073578, -2.81231654, -0.08555119, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23024, 3024, 0.0, 80.53885347, 0.02335859, 80.53885347, 0.07007576, 56.37719743, -3719.39843453, 0.05, 2, 0, 73024, 24024, 2, 3)
    ops.uniaxialMaterial('LimitState', 43024, 20.13471337, 7.885e-05, 60.4041401, 0.00023656, 201.34713366, 0.00078852, -20.13471337, -7.885e-05, -60.4041401, -0.00023656, -201.34713366, -0.00078852, 0.4, 0.3, 0.003, 0.0, 0.0, 23024, 2)
    ops.limitCurve('ThreePoint', 13024, 3024, 0.0, 80.53885347, 0.02335859, 80.53885347, 0.07007576, 56.37719743, -3719.39843453, 0.05, 2, 0, 73024, 24024, 1, 3)
    ops.uniaxialMaterial('LimitState', 33024, 20.13471337, 7.885e-05, 60.4041401, 0.00023656, 201.34713366, 0.00078852, -20.13471337, -7.885e-05, -60.4041401, -0.00023656, -201.34713366, -0.00078852, 0.4, 0.3, 0.003, 0.0, 0.0, 13024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3024, 99999, 'P', 43024, 'Vy', 33024, 'Vz', 23024, 'My', 13024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173024, 73024, 173024, 3024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124024, 124024, 24024, 3024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170004, 17.4, 0.0, 0.0)
    ops.node(124025, 17.4, 0.0, 1.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4062, 170004, 124025, 0.175, 27293166.79645327, 11372152.83185553, 0.00405757, 0.00401042, 0.0019651, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24062, 166.7608432, 0.00084067, 202.3974217, 0.04077128, 20.23974217, 0.10018937, -166.7608432, -0.00084067, -202.3974217, -0.04077128, -20.23974217, -0.10018937, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14062, 187.87633791, 0.00069839, 228.02527057, 0.04614337, 22.80252706, 0.12690083, -187.87633791, -0.00069839, -228.02527057, -0.04614337, -22.80252706, -0.12690083, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24062, 4062, 0.0, 274.34484901, 0.01681337, 274.34484901, 0.05044011, 192.04139431, -8860.07715174, 0.05, 2, 0, 70004, 24025, 2, 3)
    ops.uniaxialMaterial('LimitState', 44062, 68.58621225, 7.547e-05, 205.75863676, 0.00022642, 685.86212253, 0.00075474, -68.58621225, -7.547e-05, -205.75863676, -0.00022642, -685.86212253, -0.00075474, 0.4, 0.3, 0.003, 0.0, 0.0, 24062, 2)
    ops.limitCurve('ThreePoint', 14062, 4062, 0.0, 391.92121287, 0.01396781, 391.92121287, 0.04190342, 274.34484901, -15026.91218056, 0.05, 2, 0, 70004, 24025, 1, 3)
    ops.uniaxialMaterial('LimitState', 34062, 97.98030322, 0.00010782, 293.94090966, 0.00032346, 979.80303219, 0.00107821, -97.98030322, -0.00010782, -293.94090966, -0.00032346, -979.80303219, -0.00107821, 0.4, 0.3, 0.003, 0.0, 0.0, 14062, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4062, 99999, 'P', 44062, 'Vy', 34062, 'Vz', 24062, 'My', 14062, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170004, 70004, 170004, 4062, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124025, 124025, 24025, 4062, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174025, 17.4, 0.0, 2.025)
    ops.node(121004, 17.4, 0.0, 3.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4063, 174025, 121004, 0.175, 28507066.29469013, 11877944.28945422, 0.00405757, 0.00401042, 0.0019651, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24063, 131.68581049, 0.00079552, 159.6781982, 0.03942402, 15.96781982, 0.10266091, -131.68581049, -0.00079552, -159.6781982, -0.03942402, -15.96781982, -0.10266091, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14063, 157.26610443, 0.00066692, 190.69608259, 0.04462997, 19.06960826, 0.13057771, -157.26610443, -0.00066692, -190.69608259, -0.04462997, -19.06960826, -0.13057771, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24063, 4063, 0.0, 274.38864693, 0.01591038, 274.38864693, 0.04773114, 192.07205285, -8725.48759732, 0.05, 2, 0, 74025, 21004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44063, 68.59716173, 7.227e-05, 205.7914852, 0.00021682, 685.97161733, 0.00072272, -68.59716173, -7.227e-05, -205.7914852, -0.00021682, -685.97161733, -0.00072272, 0.4, 0.3, 0.003, 0.0, 0.0, 24063, 2)
    ops.limitCurve('ThreePoint', 14063, 4063, 0.0, 391.98378133, 0.01333842, 391.98378133, 0.04001526, 274.38864693, -14898.71566336, 0.05, 2, 0, 74025, 21004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34063, 97.99594533, 0.00010325, 293.987836, 0.00030974, 979.95945333, 0.00103246, -97.99594533, -0.00010325, -293.987836, -0.00030974, -979.95945333, -0.00103246, 0.4, 0.3, 0.003, 0.0, 0.0, 14063, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4063, 99999, 'P', 44063, 'Vy', 34063, 'Vz', 24063, 'My', 14063, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174025, 74025, 174025, 4063, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121004, 121004, 21004, 4063, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170005, 20.2, 0.0, 0.0)
    ops.node(124026, 20.2, 0.0, 1.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4064, 170005, 124026, 0.175, 26457465.97396301, 11023944.15581792, 0.00405757, 0.00401042, 0.0019651, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24064, 166.69856124, 0.00088182, 202.48370324, 0.03669117, 20.24837032, 0.09418305, -166.69856124, -0.00088182, -202.48370324, -0.03669117, -20.24837032, -0.09418305, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14064, 189.27650401, 0.00072396, 229.90844781, 0.04147854, 22.99084478, 0.11961802, -189.27650401, -0.00072396, -229.90844781, -0.04147854, -22.99084478, -0.11961802, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24064, 4064, 0.0, 241.98065454, 0.01763647, 241.98065454, 0.0529094, 169.38645818, -6657.94854702, 0.05, 2, 0, 70005, 24026, 2, 3)
    ops.uniaxialMaterial('LimitState', 44064, 60.49516363, 6.867e-05, 181.4854909, 0.00020602, 604.95163635, 0.00068674, -60.49516363, -6.867e-05, -181.4854909, -0.00020602, -604.95163635, -0.00068674, 0.4, 0.3, 0.003, 0.0, 0.0, 24064, 2)
    ops.limitCurve('ThreePoint', 14064, 4064, 0.0, 345.68664934, 0.01447928, 345.68664934, 0.04343785, 241.98065454, -10958.28670744, 0.05, 2, 0, 70005, 24026, 1, 3)
    ops.uniaxialMaterial('LimitState', 34064, 86.42166234, 9.811e-05, 259.26498701, 0.00029432, 864.21662336, 0.00098105, -86.42166234, -9.811e-05, -259.26498701, -0.00029432, -864.21662336, -0.00098105, 0.4, 0.3, 0.003, 0.0, 0.0, 14064, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4064, 99999, 'P', 44064, 'Vy', 34064, 'Vz', 24064, 'My', 14064, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170005, 70005, 170005, 4064, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124026, 124026, 24026, 4064, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174026, 20.2, 0.0, 2.025)
    ops.node(121005, 20.2, 0.0, 3.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4065, 174026, 121005, 0.175, 30497822.19991756, 12707425.91663232, 0.00405757, 0.00401042, 0.0019651, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24065, 133.78710366, 0.00076967, 161.57430913, 0.03794383, 16.15743091, 0.10430628, -133.78710366, -0.00076967, -161.57430913, -0.03794383, -16.15743091, -0.10430628, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14065, 159.13973099, 0.00065106, 192.19260591, 0.04295892, 19.21926059, 0.13315475, -159.13973099, -0.00065106, -192.19260591, -0.04295892, -19.21926059, -0.13315475, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24065, 4065, 0.0, 277.2753064, 0.01539336, 277.2753064, 0.04618007, 194.09271448, -7855.47366038, 0.05, 2, 0, 74026, 21005, 2, 3)
    ops.uniaxialMaterial('LimitState', 44065, 69.3188266, 6.827e-05, 207.9564798, 0.0002048, 693.18826601, 0.00068265, -69.3188266, -6.827e-05, -207.9564798, -0.0002048, -693.18826601, -0.00068265, 0.4, 0.3, 0.003, 0.0, 0.0, 24065, 2)
    ops.limitCurve('ThreePoint', 14065, 4065, 0.0, 396.10758057, 0.01302127, 396.10758057, 0.03906382, 277.2753064, -13278.61076177, 0.05, 2, 0, 74026, 21005, 1, 3)
    ops.uniaxialMaterial('LimitState', 34065, 99.02689514, 9.752e-05, 297.08068543, 0.00029257, 990.26895144, 0.00097522, -99.02689514, -9.752e-05, -297.08068543, -0.00029257, -990.26895144, -0.00097522, 0.4, 0.3, 0.003, 0.0, 0.0, 14065, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4065, 99999, 'P', 44065, 'Vy', 34065, 'Vz', 24065, 'My', 14065, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174026, 74026, 174026, 4065, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121005, 121005, 21005, 4065, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171004, 17.4, 0.0, 3.95)
    ops.node(124027, 17.4, 0.0, 4.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4067, 171004, 124027, 0.175, 30074904.86349335, 12531210.3597889, 0.00405757, 0.00401042, 0.0019651, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24067, 124.90729572, 0.00073752, 151.20599043, 0.02977498, 15.12059904, 0.07928558, -124.90729572, -0.00073752, -151.20599043, -0.02977498, -15.12059904, -0.07928558, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14067, 148.6881683, 0.00064593, 179.99382362, 0.03338509, 17.99938236, 0.0991971, -148.6881683, -0.00064593, -179.99382362, -0.03338509, -17.99938236, -0.0991971, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24067, 4067, 0.0, 281.20279708, 0.01475043, 281.20279708, 0.0442513, 196.84195796, -7780.29245485, 0.05, 2, 0, 71004, 24027, 2, 3)
    ops.uniaxialMaterial('LimitState', 44067, 70.30069927, 5.386e-05, 210.90209781, 0.00016157, 703.0069927, 0.00053856, -70.30069927, -5.386e-05, -210.90209781, -0.00016157, -703.0069927, -0.00053856, 0.4, 0.3, 0.003, 0.0, 0.0, 24067, 2)
    ops.limitCurve('ThreePoint', 14067, 4067, 0.0, 369.24936472, 0.01291863, 369.24936472, 0.03875588, 258.47455531, -13094.51018945, 0.05, 2, 0, 71004, 24027, 1, 3)
    ops.uniaxialMaterial('LimitState', 34067, 92.31234118, 7.072e-05, 276.93702354, 0.00021216, 923.12341181, 0.00070719, -92.31234118, -7.072e-05, -276.93702354, -0.00021216, -923.12341181, -0.00070719, 0.4, 0.3, 0.003, 0.0, 0.0, 14067, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4067, 99999, 'P', 44067, 'Vy', 34067, 'Vz', 24067, 'My', 14067, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171004, 71004, 171004, 4067, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124027, 124027, 24027, 4067, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174027, 17.4, 0.0, 5.225)
    ops.node(122004, 17.4, 0.0, 6.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4068, 174027, 122004, 0.175, 27992140.07958784, 11663391.69982827, 0.00405757, 0.00401042, 0.0019651, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24068, 121.17157339, 0.00075018, 147.41732881, 0.02825197, 14.74173288, 0.0767394, -121.17157339, -0.00075018, -147.41732881, -0.02825197, -14.74173288, -0.0767394, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14068, 142.83913757, 0.00065481, 173.77808607, 0.03166253, 17.37780861, 0.09611448, -142.83913757, -0.00065481, -173.77808607, -0.03166253, -17.37780861, -0.09611448, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24068, 4068, 0.0, 245.5987703, 0.01500363, 245.5987703, 0.04501089, 171.91913921, -6466.01800314, 0.05, 2, 0, 74027, 22004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44068, 61.39969257, 5.054e-05, 184.19907772, 0.00015161, 613.99692575, 0.00050537, -61.39969257, -5.054e-05, -184.19907772, -0.00015161, -613.99692575, -0.00050537, 0.4, 0.3, 0.003, 0.0, 0.0, 24068, 2)
    ops.limitCurve('ThreePoint', 14068, 4068, 0.0, 322.02877424, 0.01309613, 322.02877424, 0.03928839, 225.42014197, -10805.09731374, 0.05, 2, 0, 74027, 22004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34068, 80.50719356, 6.626e-05, 241.52158068, 0.00019879, 805.07193561, 0.00066265, -80.50719356, -6.626e-05, -241.52158068, -0.00019879, -805.07193561, -0.00066265, 0.4, 0.3, 0.003, 0.0, 0.0, 14068, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4068, 99999, 'P', 44068, 'Vy', 34068, 'Vz', 24068, 'My', 14068, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174027, 74027, 174027, 4068, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122004, 122004, 22004, 4068, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171005, 20.2, 0.0, 3.95)
    ops.node(124028, 20.2, 0.0, 4.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4069, 171005, 124028, 0.175, 28983819.67279368, 12076591.5303307, 0.00405757, 0.00401042, 0.0019651, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24069, 123.94398483, 0.00073222, 150.40039876, 0.02605093, 15.04003988, 0.07454065, -123.94398483, -0.00073222, -150.40039876, -0.02605093, -15.04003988, -0.07454065, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14069, 146.67353735, 0.00064301, 177.98167886, 0.02918935, 17.79816789, 0.09364435, -146.67353735, -0.00064301, -177.98167886, -0.02918935, -17.79816789, -0.09364435, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24069, 4069, 0.0, 254.43792031, 0.01464441, 254.43792031, 0.04393323, 178.10654422, -5978.82627951, 0.05, 2, 0, 71005, 24028, 2, 3)
    ops.uniaxialMaterial('LimitState', 44069, 63.60948008, 5.056e-05, 190.82844023, 0.00015169, 636.09480078, 0.00050565, -63.60948008, -5.056e-05, -190.82844023, -0.00015169, -636.09480078, -0.00050565, 0.4, 0.3, 0.003, 0.0, 0.0, 24069, 2)
    ops.limitCurve('ThreePoint', 14069, 4069, 0.0, 332.63715406, 0.01286017, 332.63715406, 0.03858052, 232.84600784, -9778.0389153, 0.05, 2, 0, 71005, 24028, 1, 3)
    ops.uniaxialMaterial('LimitState', 34069, 83.15928851, 6.611e-05, 249.47786554, 0.00019832, 831.59288514, 0.00066106, -83.15928851, -6.611e-05, -249.47786554, -0.00019832, -831.59288514, -0.00066106, 0.4, 0.3, 0.003, 0.0, 0.0, 14069, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4069, 99999, 'P', 44069, 'Vy', 34069, 'Vz', 24069, 'My', 14069, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171005, 71005, 171005, 4069, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124028, 124028, 24028, 4069, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174028, 20.2, 0.0, 5.225)
    ops.node(122005, 20.2, 0.0, 6.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4070, 174028, 122005, 0.175, 30008327.53956894, 12503469.80815372, 0.00405757, 0.00401042, 0.0019651, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24070, 122.37494459, 0.00076543, 148.25080357, 0.02548569, 14.82508036, 0.07581133, -122.37494459, -0.00076543, -148.25080357, -0.02548569, -14.82508036, -0.07581133, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14070, 146.48820131, 0.00066287, 177.46274477, 0.02853447, 17.74627448, 0.09542988, -146.48820131, -0.00066287, -177.46274477, -0.02853447, -17.74627448, -0.09542988, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24070, 4070, 0.0, 257.61955434, 0.01530854, 257.61955434, 0.04592561, 180.33368804, -5999.29264191, 0.05, 2, 0, 74028, 22005, 2, 3)
    ops.uniaxialMaterial('LimitState', 44070, 64.40488859, 4.945e-05, 193.21466576, 0.00014835, 644.04888586, 0.00049449, -64.40488859, -4.945e-05, -193.21466576, -0.00014835, -644.04888586, -0.00049449, 0.4, 0.3, 0.003, 0.0, 0.0, 24070, 2)
    ops.limitCurve('ThreePoint', 14070, 4070, 0.0, 336.24560393, 0.01325731, 336.24560393, 0.03977192, 235.37192275, -9944.88925789, 0.05, 2, 0, 74028, 22005, 1, 3)
    ops.uniaxialMaterial('LimitState', 34070, 84.06140098, 6.454e-05, 252.18420295, 0.00019362, 840.61400984, 0.00064541, -84.06140098, -6.454e-05, -252.18420295, -0.00019362, -840.61400984, -0.00064541, 0.4, 0.3, 0.003, 0.0, 0.0, 14070, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4070, 99999, 'P', 44070, 'Vy', 34070, 'Vz', 24070, 'My', 14070, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174028, 74028, 174028, 4070, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122005, 122005, 22005, 4070, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172004, 17.4, 0.0, 6.75)
    ops.node(124029, 17.4, 0.0, 7.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4072, 172004, 124029, 0.1, 30094446.48642823, 12539352.70267843, 0.00127345, 0.00146667, 0.00057292, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24072, 46.16358974, 0.00094114, 55.84669151, 0.0196577, 5.58466915, 0.06597116, -46.16358974, -0.00094114, -55.84669151, -0.0196577, -5.58466915, -0.06597116, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14072, 71.60515745, 0.00070746, 86.62478722, 0.02262244, 8.66247872, 0.089956, -71.60515745, -0.00070746, -86.62478722, -0.02262244, -8.66247872, -0.089956, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24072, 4072, 0.0, 117.79640979, 0.01882288, 117.79640979, 0.05646864, 82.45748685, -2924.40429175, 0.05, 2, 0, 72004, 24029, 2, 3)
    ops.uniaxialMaterial('LimitState', 44072, 29.44910245, 3.946e-05, 88.34730734, 0.00011837, 294.49102448, 0.00039455, -29.44910245, -3.946e-05, -88.34730734, -0.00011837, -294.49102448, -0.00039455, 0.4, 0.3, 0.003, 0.0, 0.0, 24072, 2)
    ops.limitCurve('ThreePoint', 14072, 4072, 0.0, 188.47425567, 0.01414918, 188.47425567, 0.04244753, 131.93197897, -5415.97503906, 0.05, 2, 0, 72004, 24029, 1, 3)
    ops.uniaxialMaterial('LimitState', 34072, 47.11856392, 6.313e-05, 141.35569175, 0.00018939, 471.18563917, 0.00063129, -47.11856392, -6.313e-05, -141.35569175, -0.00018939, -471.18563917, -0.00063129, 0.4, 0.3, 0.003, 0.0, 0.0, 14072, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4072, 99999, 'P', 44072, 'Vy', 34072, 'Vz', 24072, 'My', 14072, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172004, 72004, 172004, 4072, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124029, 124029, 24029, 4072, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174029, 17.4, 0.0, 8.025)
    ops.node(123004, 17.4, 0.0, 8.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4073, 174029, 123004, 0.1, 27721636.42604771, 11550681.84418655, 0.00127345, 0.00146667, 0.00057292, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24073, 54.91261895, 0.00094719, 66.83338126, 0.02142781, 6.68333813, 0.06722351, -54.91261895, -0.00094719, -66.83338126, -0.02142781, -6.68333813, -0.06722351, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14073, 78.45205299, 0.00071936, 95.48289753, 0.02469987, 9.54828975, 0.09128068, -78.45205299, -0.00071936, -95.48289753, -0.02469987, -9.54828975, -0.09128068, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24073, 4073, 0.0, 110.77716896, 0.01894381, 110.77716896, 0.05683142, 77.54401827, -3428.66910297, 0.05, 2, 0, 74029, 23004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44073, 27.69429224, 4.028e-05, 83.08287672, 0.00012084, 276.94292241, 0.0004028, -27.69429224, -4.028e-05, -83.08287672, -0.00012084, -276.94292241, -0.0004028, 0.4, 0.3, 0.003, 0.0, 0.0, 24073, 2)
    ops.limitCurve('ThreePoint', 14073, 4073, 0.0, 177.24347034, 0.01438729, 177.24347034, 0.04316187, 124.07042924, -6733.44021755, 0.05, 2, 0, 74029, 23004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34073, 44.31086759, 6.445e-05, 132.93260276, 0.00019335, 443.10867585, 0.00064448, -44.31086759, -6.445e-05, -132.93260276, -0.00019335, -443.10867585, -0.00064448, 0.4, 0.3, 0.003, 0.0, 0.0, 14073, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4073, 99999, 'P', 44073, 'Vy', 34073, 'Vz', 24073, 'My', 14073, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174029, 74029, 174029, 4073, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123004, 123004, 23004, 4073, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172005, 20.2, 0.0, 6.75)
    ops.node(124030, 20.2, 0.0, 7.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4074, 172005, 124030, 0.1, 31511334.20911921, 13129722.58713301, 0.00127345, 0.00146667, 0.00057292, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24074, 46.11723145, 0.00095896, 55.59018332, 0.02226566, 5.55901833, 0.06975709, -46.11723145, -0.00095896, -55.59018332, -0.02226566, -5.55901833, -0.06975709, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14074, 72.02598211, 0.00071259, 86.82085683, 0.02566033, 8.68208568, 0.09470652, -72.02598211, -0.00071259, -86.82085683, -0.02566033, -8.68208568, -0.09470652, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24074, 4074, 0.0, 131.67173133, 0.01917929, 131.67173133, 0.05753788, 92.17021193, -3715.73813506, 0.05, 2, 0, 72005, 24030, 2, 3)
    ops.uniaxialMaterial('LimitState', 44074, 32.91793283, 4.212e-05, 98.7537985, 0.00012636, 329.17932832, 0.0004212, -32.91793283, -4.212e-05, -98.7537985, -0.00012636, -329.17932832, -0.0004212, 0.4, 0.3, 0.003, 0.0, 0.0, 24074, 2)
    ops.limitCurve('ThreePoint', 14074, 4074, 0.0, 210.67477012, 0.01425188, 210.67477012, 0.04275565, 147.47233909, -7157.13588294, 0.05, 2, 0, 72005, 24030, 1, 3)
    ops.uniaxialMaterial('LimitState', 34074, 52.66869253, 6.739e-05, 158.00607759, 0.00020218, 526.68692531, 0.00067392, -52.66869253, -6.739e-05, -158.00607759, -0.00020218, -526.68692531, -0.00067392, 0.4, 0.3, 0.003, 0.0, 0.0, 14074, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4074, 99999, 'P', 44074, 'Vy', 34074, 'Vz', 24074, 'My', 14074, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172005, 72005, 172005, 4074, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124030, 124030, 24030, 4074, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174030, 20.2, 0.0, 8.025)
    ops.node(123005, 20.2, 0.0, 8.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4075, 174030, 123005, 0.1, 30731220.86119926, 12804675.35883303, 0.00127345, 0.00146667, 0.00057292, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24075, 52.86682651, 0.00079409, 63.92518262, 0.02101085, 6.39251826, 0.06937814, -52.86682651, -0.00079409, -63.92518262, -0.02101085, -6.39251826, -0.06937814, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14075, 74.40064983, 0.00063326, 89.96331805, 0.02430482, 8.9963318, 0.09462438, -74.40064983, -0.00063326, -89.96331805, -0.02430482, -8.9963318, -0.09462438, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24075, 4075, 0.0, 120.64309835, 0.0158817, 120.64309835, 0.0476451, 84.45016884, -3401.54856915, 0.05, 2, 0, 74030, 23005, 2, 3)
    ops.uniaxialMaterial('LimitState', 44075, 30.16077459, 3.957e-05, 90.48232376, 0.00011871, 301.60774587, 0.00039572, -30.16077459, -3.957e-05, -90.48232376, -0.00011871, -301.60774587, -0.00039572, 0.4, 0.3, 0.003, 0.0, 0.0, 24075, 2)
    ops.limitCurve('ThreePoint', 14075, 4075, 0.0, 193.02895736, 0.01266524, 193.02895736, 0.03799573, 135.12027015, -6672.64747844, 0.05, 2, 0, 74030, 23005, 1, 3)
    ops.uniaxialMaterial('LimitState', 34075, 48.25723934, 6.331e-05, 144.77171802, 0.00018994, 482.57239339, 0.00063315, -48.25723934, -6.331e-05, -144.77171802, -0.00018994, -482.57239339, -0.00063315, 0.4, 0.3, 0.003, 0.0, 0.0, 14075, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4075, 99999, 'P', 44075, 'Vy', 34075, 'Vz', 24075, 'My', 14075, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174030, 74030, 174030, 4075, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123005, 123005, 23005, 4075, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173004, 17.4, 0.0, 9.55)
    ops.node(124031, 17.4, 0.0, 10.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4077, 173004, 124031, 0.1, 27464014.03053401, 11443339.17938917, 0.00127345, 0.00146667, 0.00057292, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24077, 33.75612766, 0.00089331, 41.25100913, 0.01908141, 4.12510091, 0.0621742, -33.75612766, -0.00089331, -41.25100913, -0.01908141, -4.12510091, -0.0621742, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14077, 63.20839081, 0.00068508, 77.24256564, 0.02180793, 7.72425656, 0.08325598, -63.20839081, -0.00068508, -77.24256564, -0.02180793, -7.72425656, -0.08325598, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24077, 4077, 0.0, 97.69364949, 0.01786626, 97.69364949, 0.05359879, 68.38555464, -4126.62729866, 0.05, 2, 0, 73004, 24031, 2, 3)
    ops.uniaxialMaterial('LimitState', 44077, 24.42341237, 3.586e-05, 73.27023712, 0.00010757, 244.23412373, 0.00035856, -24.42341237, -3.586e-05, -73.27023712, -0.00010757, -244.23412373, -0.00035856, 0.4, 0.3, 0.003, 0.0, 0.0, 24077, 2)
    ops.limitCurve('ThreePoint', 14077, 4077, 0.0, 156.30983918, 0.01370155, 156.30983918, 0.04110464, 109.41688743, -9034.57972103, 0.05, 2, 0, 73004, 24031, 1, 3)
    ops.uniaxialMaterial('LimitState', 34077, 39.0774598, 5.737e-05, 117.23237939, 0.00017211, 390.77459796, 0.0005737, -39.0774598, -5.737e-05, -117.23237939, -0.00017211, -390.77459796, -0.0005737, 0.4, 0.3, 0.003, 0.0, 0.0, 14077, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4077, 99999, 'P', 44077, 'Vy', 34077, 'Vz', 24077, 'My', 14077, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173004, 73004, 173004, 4077, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124031, 124031, 24031, 4077, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174031, 17.4, 0.0, 10.825)
    ops.node(124004, 17.4, 0.0, 11.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4078, 174031, 124004, 0.1, 31394325.75117134, 13080969.06298806, 0.00127345, 0.00146667, 0.00057292, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24078, 36.14540831, 0.00085119, 43.77146386, 0.02062442, 4.37714639, 0.07449362, -36.14540831, -0.00085119, -43.77146386, -0.02062442, -4.37714639, -0.07449362, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14078, 54.60265474, 0.00066311, 66.12286984, 0.02381534, 6.61228698, 0.10213395, -54.60265474, -0.00066311, -66.12286984, -0.02381534, -6.61228698, -0.10213395, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24078, 4078, 0.0, 109.73474351, 0.01702383, 109.73474351, 0.05107149, 76.81432046, -7679.81155684, 0.05, 2, 0, 74031, 24004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44078, 27.43368588, 3.523e-05, 82.30105763, 0.0001057, 274.33685878, 0.00035233, -27.43368588, -3.523e-05, -82.30105763, -0.0001057, -274.33685878, -0.00035233, 0.4, 0.3, 0.003, 0.0, 0.0, 24078, 2)
    ops.limitCurve('ThreePoint', 14078, 4078, 0.0, 175.57558962, 0.01326223, 175.57558962, 0.03978669, 122.90291273, -18208.82545179, 0.05, 2, 0, 74031, 24004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34078, 43.89389741, 5.637e-05, 131.68169222, 0.00016912, 438.93897405, 0.00056373, -43.89389741, -5.637e-05, -131.68169222, -0.00016912, -438.93897405, -0.00056373, 0.4, 0.3, 0.003, 0.0, 0.0, 14078, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4078, 99999, 'P', 44078, 'Vy', 34078, 'Vz', 24078, 'My', 14078, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174031, 74031, 174031, 4078, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124004, 124004, 24004, 4078, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173005, 20.2, 0.0, 9.55)
    ops.node(124032, 20.2, 0.0, 10.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4079, 173005, 124032, 0.1, 30556854.34638626, 12732022.64432761, 0.00127345, 0.00146667, 0.00057292, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24079, 33.07411333, 0.00083158, 40.11238656, 0.01983922, 4.01123866, 0.06405132, -33.07411333, -0.00083158, -40.11238656, -0.01983922, -4.01123866, -0.06405132, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14079, 61.70515632, 0.00064734, 74.83620372, 0.02272197, 7.48362037, 0.08576611, -61.70515632, -0.00064734, -74.83620372, -0.02272197, -7.48362037, -0.08576611, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24079, 4079, 0.0, 109.80075046, 0.01663151, 109.80075046, 0.04989452, 76.86052532, -4444.40399383, 0.05, 2, 0, 73005, 24032, 2, 3)
    ops.uniaxialMaterial('LimitState', 44079, 27.45018761, 3.622e-05, 82.35056284, 0.00010866, 274.50187614, 0.00036221, -27.45018761, -3.622e-05, -82.35056284, -0.00010866, -274.50187614, -0.00036221, 0.4, 0.3, 0.003, 0.0, 0.0, 24079, 2)
    ops.limitCurve('ThreePoint', 14079, 4079, 0.0, 175.68120073, 0.01294678, 175.68120073, 0.03884035, 122.97684051, -9788.02722405, 0.05, 2, 0, 73005, 24032, 1, 3)
    ops.uniaxialMaterial('LimitState', 34079, 43.92030018, 5.795e-05, 131.76090055, 0.00017386, 439.20300182, 0.00057953, -43.92030018, -5.795e-05, -131.76090055, -0.00017386, -439.20300182, -0.00057953, 0.4, 0.3, 0.003, 0.0, 0.0, 14079, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4079, 99999, 'P', 44079, 'Vy', 34079, 'Vz', 24079, 'My', 14079, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173005, 73005, 173005, 4079, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124032, 124032, 24032, 4079, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174032, 20.2, 0.0, 10.825)
    ops.node(124005, 20.2, 0.0, 11.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4080, 174032, 124005, 0.1, 30862593.77642816, 12859414.07351173, 0.00127345, 0.00146667, 0.00057292, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24080, 34.26113695, 0.0008142, 41.55847517, 0.02551464, 4.15584752, 0.07930331, -34.26113695, -0.0008142, -41.55847517, -0.02551464, -4.15584752, -0.07930331, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14080, 51.7862223, 0.00063967, 62.81625845, 0.02956112, 6.28162584, 0.10776263, -51.7862223, -0.00063967, -62.81625845, -0.02956112, -6.28162584, -0.10776263, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24080, 4080, 0.0, 120.50175486, 0.01628391, 120.50175486, 0.04885172, 84.3512284, -12427.68064392, 0.05, 2, 0, 74032, 24005, 2, 3)
    ops.uniaxialMaterial('LimitState', 44080, 30.12543872, 3.936e-05, 90.37631615, 0.00011807, 301.25438716, 0.00039357, -30.12543872, -3.936e-05, -90.37631615, -0.00011807, -301.25438716, -0.00039357, 0.4, 0.3, 0.003, 0.0, 0.0, 24080, 2)
    ops.limitCurve('ThreePoint', 14080, 4080, 0.0, 192.80280778, 0.01279339, 192.80280778, 0.03838018, 134.96196545, -29960.85392017, 0.05, 2, 0, 74032, 24005, 1, 3)
    ops.uniaxialMaterial('LimitState', 34080, 48.20070195, 6.297e-05, 144.60210584, 0.00018891, 482.00701945, 0.00062971, -48.20070195, -6.297e-05, -144.60210584, -0.00018891, -482.00701945, -0.00062971, 0.4, 0.3, 0.003, 0.0, 0.0, 14080, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4080, 99999, 'P', 44080, 'Vy', 34080, 'Vz', 24080, 'My', 14080, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174032, 74032, 174032, 4080, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124005, 124005, 24005, 4080, '-orient', 0, 0, 1, 0, 1, 0)
