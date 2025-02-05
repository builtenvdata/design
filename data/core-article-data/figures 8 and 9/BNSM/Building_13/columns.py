import openseespy.opensees as ops


def add_columns() -> None:
    """Add components of all columns to ops domain (plastic hinges, column elements and nodes)
    """
    # Create elastic column element nodes
    ops.node(170001, 0.0, 0.0, 0.0)
    ops.node(121001, 0.0, 0.0, 2.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1, 170001, 121001, 0.0875, 24563224.2069678, 10234676.75290325, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20001, 38.05783006, 0.00090856, 46.216902, 0.02278553, 4.6216902, 0.05556086, -38.05783006, -0.00090856, -46.216902, -0.02278553, -4.6216902, -0.05556086, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10001, 49.05938512, 0.00068623, 59.57703817, 0.0250819, 5.95770382, 0.06752508, -49.05938512, -0.00068623, -59.57703817, -0.0250819, -5.95770382, -0.06752508, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20001, 1, 0.0, 71.21830032, 0.0181712, 71.21830032, 0.05451359, 49.85281022, -793.60721215, 0.05, 2, 0, 70001, 21001, 2, 3)
    ops.uniaxialMaterial('LimitState', 40001, 17.80457508, 6.919e-05, 53.41372524, 0.00020756, 178.04575079, 0.00069188, -17.80457508, -6.919e-05, -53.41372524, -0.00020756, -178.04575079, -0.00069188, 0.4, 0.3, 0.003, 0.0, 0.0, 20001, 2)
    ops.limitCurve('ThreePoint', 10001, 1, 0.0, 80.91144361, 0.01372455, 80.91144361, 0.04117364, 56.63801053, -1090.63089702, 0.05, 2, 0, 70001, 21001, 1, 3)
    ops.uniaxialMaterial('LimitState', 30001, 20.2278609, 7.86e-05, 60.68358271, 0.00023581, 202.27860903, 0.00078604, -20.2278609, -7.86e-05, -60.68358271, -0.00023581, -202.27860903, -0.00078604, 0.4, 0.3, 0.003, 0.0, 0.0, 10001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1, 99999, 'P', 40001, 'Vy', 30001, 'Vz', 20001, 'My', 10001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170001, 70001, 170001, 1, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121001, 121001, 21001, 1, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170002, 5.3, 0.0, 0.0)
    ops.node(121002, 5.3, 0.0, 2.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2, 170002, 121002, 0.1925, 27810128.47716095, 11587553.5321504, 0.00475217, 0.00533786, 0.00216161, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20002, 103.2339698, 0.00065439, 125.42574325, 0.04066282, 12.54257432, 0.09945532, -103.2339698, -0.00065439, -125.42574325, -0.04066282, -12.54257432, -0.09945532, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10002, 136.45774185, 0.00051769, 165.79149021, 0.04759154, 16.57914902, 0.13406023, -136.45774185, -0.00051769, -165.79149021, -0.04759154, -16.57914902, -0.13406023, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20002, 2, 0.0, 187.25566964, 0.01308786, 187.25566964, 0.03926359, 131.07896874, -2374.8390975, 0.05, 2, 0, 70002, 21002, 2, 3)
    ops.uniaxialMaterial('LimitState', 40002, 46.81391741, 7.304e-05, 140.44175223, 0.00021911, 468.13917409, 0.00073035, -46.81391741, -7.304e-05, -140.44175223, -0.00021911, -468.13917409, -0.00073035, 0.4, 0.3, 0.003, 0.0, 0.0, 20002, 2)
    ops.limitCurve('ThreePoint', 10002, 2, 0.0, 253.20739314, 0.01035372, 253.20739314, 0.03106117, 177.2451752, -4175.21006165, 0.05, 2, 0, 70002, 21002, 1, 3)
    ops.uniaxialMaterial('LimitState', 30002, 63.30184829, 9.876e-05, 189.90554486, 0.00029627, 633.01848286, 0.00098758, -63.30184829, -9.876e-05, -189.90554486, -0.00029627, -633.01848286, -0.00098758, 0.4, 0.3, 0.003, 0.0, 0.0, 10002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2, 99999, 'P', 40002, 'Vy', 30002, 'Vz', 20002, 'My', 10002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170002, 70002, 170002, 2, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121002, 121002, 21002, 2, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170005, 18.75, 0.0, 0.0)
    ops.node(121005, 18.75, 0.0, 2.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 5, 170005, 121005, 0.1925, 27334274.68746622, 11389281.11977759, 0.00475217, 0.00533786, 0.00216161, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20005, 100.30104353, 0.00063464, 121.9461996, 0.04120998, 12.19461996, 0.09919554, -100.30104353, -0.00063464, -121.9461996, -0.04120998, -12.19461996, -0.09919554, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10005, 132.63130798, 0.00050529, 161.25339664, 0.04824618, 16.12533966, 0.13352805, -132.63130798, -0.00050529, -161.25339664, -0.04824618, -16.12533966, -0.13352805, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20005, 5, 0.0, 188.03173928, 0.01269281, 188.03173928, 0.03807842, 131.6222175, -2503.82822746, 0.05, 2, 0, 70005, 21005, 2, 3)
    ops.uniaxialMaterial('LimitState', 40005, 47.00793482, 7.461e-05, 141.02380446, 0.00022384, 470.07934821, 0.00074615, -47.00793482, -7.461e-05, -141.02380446, -0.00022384, -470.07934821, -0.00074615, 0.4, 0.3, 0.003, 0.0, 0.0, 20005, 2)
    ops.limitCurve('ThreePoint', 10005, 5, 0.0, 255.36707282, 0.0101058, 255.36707282, 0.03031741, 178.75695097, -4444.63121781, 0.05, 2, 0, 70005, 21005, 1, 3)
    ops.uniaxialMaterial('LimitState', 30005, 63.8417682, 0.00010133, 191.52530461, 0.000304, 638.41768205, 0.00101334, -63.8417682, -0.00010133, -191.52530461, -0.000304, -638.41768205, -0.00101334, 0.4, 0.3, 0.003, 0.0, 0.0, 10005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 5, 99999, 'P', 40005, 'Vy', 30005, 'Vz', 20005, 'My', 10005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170005, 70005, 170005, 5, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121005, 121005, 21005, 5, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170006, 24.05, 0.0, 0.0)
    ops.node(121006, 24.05, 0.0, 2.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 6, 170006, 121006, 0.0875, 27271838.44193284, 11363266.01747202, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20006, 39.79331872, 0.00083921, 48.26741799, 0.02364583, 4.8267418, 0.06112647, -39.79331872, -0.00083921, -48.26741799, -0.02364583, -4.8267418, -0.06112647, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10006, 50.53865253, 0.00065002, 61.30100089, 0.02608237, 6.13010009, 0.07461881, -50.53865253, -0.00065002, -61.30100089, -0.02608237, -6.13010009, -0.07461881, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20006, 6, 0.0, 78.9641946, 0.01678426, 78.9641946, 0.05035279, 55.27493622, -824.29135163, 0.05, 2, 0, 70006, 21006, 2, 3)
    ops.uniaxialMaterial('LimitState', 40006, 19.74104865, 6.909e-05, 59.22314595, 0.00020728, 197.4104865, 0.00069094, -19.74104865, -6.909e-05, -59.22314595, -0.00020728, -197.4104865, -0.00069094, 0.4, 0.3, 0.003, 0.0, 0.0, 20006, 2)
    ops.limitCurve('ThreePoint', 10006, 6, 0.0, 89.08825878, 0.01300046, 89.08825878, 0.03900139, 62.36178115, -1141.0827772, 0.05, 2, 0, 70006, 21006, 1, 3)
    ops.uniaxialMaterial('LimitState', 30006, 22.27206469, 7.795e-05, 66.81619408, 0.00023386, 222.72064695, 0.00077952, -22.27206469, -7.795e-05, -66.81619408, -0.00023386, -222.72064695, -0.00077952, 0.4, 0.3, 0.003, 0.0, 0.0, 10006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 6, 99999, 'P', 40006, 'Vy', 30006, 'Vz', 20006, 'My', 10006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170006, 70006, 170006, 6, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121006, 121006, 21006, 6, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170007, 0.0, 4.25, 0.0)
    ops.node(121007, 0.0, 4.25, 2.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 7, 170007, 121007, 0.22, 26885105.66811134, 11202127.36171306, 0.00648267, 0.00322667, 0.00610042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20007, 183.49507524, 0.00053947, 223.46378044, 0.05158889, 22.34637804, 0.12886356, -183.49507524, -0.00053947, -223.46378044, -0.05158889, -22.34637804, -0.12886356, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10007, 166.18467634, 0.00063398, 202.38284858, 0.04621227, 20.23828486, 0.10526668, -166.18467634, -0.00063398, -202.38284858, -0.04621227, -20.23828486, -0.10526668, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20007, 7, 0.0, 262.16282272, 0.01078938, 262.16282272, 0.03236813, 183.51397591, -4168.46226098, 0.05, 2, 0, 70007, 21007, 2, 3)
    ops.uniaxialMaterial('LimitState', 40007, 65.54070568, 9.255e-05, 196.62211704, 0.00027764, 655.40705681, 0.00092548, -65.54070568, -9.255e-05, -196.62211704, -0.00027764, -655.40705681, -0.00092548, 0.4, 0.3, 0.003, 0.0, 0.0, 20007, 2)
    ops.limitCurve('ThreePoint', 10007, 7, 0.0, 204.99528893, 0.01267968, 204.99528893, 0.03803904, 143.49670225, -2774.08953823, 0.05, 2, 0, 70007, 21007, 1, 3)
    ops.uniaxialMaterial('LimitState', 30007, 51.24882223, 7.237e-05, 153.7464667, 0.0002171, 512.48822233, 0.00072367, -51.24882223, -7.237e-05, -153.7464667, -0.0002171, -512.48822233, -0.00072367, 0.4, 0.3, 0.003, 0.0, 0.0, 10007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 7, 99999, 'P', 40007, 'Vy', 30007, 'Vz', 20007, 'My', 10007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170007, 70007, 170007, 7, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121007, 121007, 21007, 7, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170008, 5.3, 4.25, 0.0)
    ops.node(121008, 5.3, 4.25, 2.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 8, 170008, 121008, 0.315, 26269377.68789311, 10945574.03662213, 0.01277375, 0.00584719, 0.01414875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20008, 371.64534796, 0.00050817, 453.05155416, 0.05135976, 45.30515542, 0.12044769, -371.64534796, -0.00050817, -453.05155416, -0.05135976, -45.30515542, -0.12044769, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10008, 333.77605294, 0.00060393, 406.88726593, 0.05079855, 40.68872659, 0.11778796, -333.77605294, -0.00060393, -406.88726593, -0.05079855, -40.68872659, -0.11778796, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20008, 8, 0.0, 488.20793913, 0.01016331, 488.20793913, 0.03048994, 341.74555739, -9753.03389064, 0.05, 2, 0, 70008, 21008, 2, 3)
    ops.uniaxialMaterial('LimitState', 40008, 122.05198478, 0.00012319, 366.15595435, 0.00036957, 1220.51984782, 0.0012319, -122.05198478, -0.00012319, -366.15595435, -0.00036957, -1220.51984782, -0.0012319, 0.4, 0.3, 0.003, 0.0, 0.0, 20008, 2)
    ops.limitCurve('ThreePoint', 10008, 8, 0.0, 266.21729254, 0.01207862, 266.21729254, 0.03623585, 186.35210477, -3184.41013409, 0.05, 2, 0, 70008, 21008, 1, 3)
    ops.uniaxialMaterial('LimitState', 30008, 66.55432313, 6.717e-05, 199.6629694, 0.00020152, 665.54323134, 0.00067175, -66.55432313, -6.717e-05, -199.6629694, -0.00020152, -665.54323134, -0.00067175, 0.4, 0.3, 0.003, 0.0, 0.0, 10008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 8, 99999, 'P', 40008, 'Vy', 30008, 'Vz', 20008, 'My', 10008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170008, 70008, 170008, 8, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121008, 121008, 21008, 8, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170009, 10.6, 4.25, 0.0)
    ops.node(121009, 10.6, 4.25, 2.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 9, 170009, 121009, 0.24, 28110010.77032863, 11712504.48763693, 0.00751249, 0.00352, 0.00792, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20009, 248.08351848, 0.00052935, 301.27889291, 0.05358847, 30.12788929, 0.13122248, -248.08351848, -0.00052935, -301.27889291, -0.05358847, -30.12788929, -0.13122248, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10009, 215.03327868, 0.00063963, 261.14184665, 0.04661969, 26.11418466, 0.10189489, -215.03327868, -0.00063963, -261.14184665, -0.04661969, -26.11418466, -0.10189489, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20009, 9, 0.0, 336.05100475, 0.01058707, 336.05100475, 0.03176122, 235.23570333, -5310.55550669, 0.05, 2, 0, 70009, 21009, 2, 3)
    ops.uniaxialMaterial('LimitState', 40009, 84.01275119, 0.00010401, 252.03825357, 0.00031202, 840.12751189, 0.00104007, -84.01275119, -0.00010401, -252.03825357, -0.00031202, -840.12751189, -0.00104007, 0.4, 0.3, 0.003, 0.0, 0.0, 20009, 2)
    ops.limitCurve('ThreePoint', 10009, 9, 0.0, 241.04373996, 0.0127926, 241.04373996, 0.03837779, 168.73061797, -3176.37010927, 0.05, 2, 0, 70009, 21009, 1, 3)
    ops.uniaxialMaterial('LimitState', 30009, 60.26093499, 7.46e-05, 180.78280497, 0.00022381, 602.6093499, 0.00074603, -60.26093499, -7.46e-05, -180.78280497, -0.00022381, -602.6093499, -0.00074603, 0.4, 0.3, 0.003, 0.0, 0.0, 10009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 9, 99999, 'P', 40009, 'Vy', 30009, 'Vz', 20009, 'My', 10009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170009, 70009, 170009, 9, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121009, 121009, 21009, 9, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170010, 13.45, 4.25, 0.0)
    ops.node(121010, 13.45, 4.25, 2.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 10, 170010, 121010, 0.24, 26746085.64158459, 11144202.35066025, 0.00751249, 0.00352, 0.00792, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20010, 238.88991695, 0.00052371, 290.66701963, 0.05218034, 29.06670196, 0.12673684, -238.88991695, -0.00052371, -290.66701963, -0.05218034, -29.06670196, -0.12673684, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10010, 206.1107167, 0.00063329, 250.78324151, 0.04539799, 25.07832415, 0.09848201, -206.1107167, -0.00063329, -250.78324151, -0.04539799, -25.07832415, -0.09848201, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20010, 10, 0.0, 307.59638742, 0.01047412, 307.59638742, 0.03142237, 215.31747119, -4535.63960937, 0.05, 2, 0, 70010, 21010, 2, 3)
    ops.uniaxialMaterial('LimitState', 40010, 76.89909685, 0.00010006, 230.69729056, 0.00030017, 768.99096854, 0.00100055, -76.89909685, -0.00010006, -230.69729056, -0.00030017, -768.99096854, -0.00100055, 0.4, 0.3, 0.003, 0.0, 0.0, 20010, 2)
    ops.limitCurve('ThreePoint', 10010, 10, 0.0, 220.97623091, 0.01266588, 220.97623091, 0.03799763, 154.68336163, -2774.65852081, 0.05, 2, 0, 70010, 21010, 1, 3)
    ops.uniaxialMaterial('LimitState', 30010, 55.24405773, 7.188e-05, 165.73217318, 0.00021564, 552.44057727, 0.00071879, -55.24405773, -7.188e-05, -165.73217318, -0.00021564, -552.44057727, -0.00071879, 0.4, 0.3, 0.003, 0.0, 0.0, 10010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 10, 99999, 'P', 40010, 'Vy', 30010, 'Vz', 20010, 'My', 10010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170010, 70010, 170010, 10, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121010, 121010, 21010, 10, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170011, 18.75, 4.25, 0.0)
    ops.node(121011, 18.75, 4.25, 2.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 11, 170011, 121011, 0.315, 26590806.84649917, 11079502.85270799, 0.01277375, 0.00584719, 0.01414875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20011, 362.70160127, 0.00049941, 441.97847515, 0.05280736, 44.19784752, 0.12255655, -362.70160127, -0.00049941, -441.97847515, -0.05280736, -44.19784752, -0.12255655, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10011, 322.80395934, 0.00059208, 393.36027528, 0.05222424, 39.33602753, 0.11985482, -322.80395934, -0.00059208, -393.36027528, -0.05222424, -39.33602753, -0.11985482, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20011, 11, 0.0, 495.72126052, 0.00998826, 495.72126052, 0.02996477, 347.00488236, -9957.59206092, 0.05, 2, 0, 70011, 21011, 2, 3)
    ops.uniaxialMaterial('LimitState', 40011, 123.93031513, 0.00012357, 371.79094539, 0.00037072, 1239.3031513, 0.00123574, -123.93031513, -0.00012357, -371.79094539, -0.00037072, -1239.3031513, -0.00123574, 0.4, 0.3, 0.003, 0.0, 0.0, 20011, 2)
    ops.limitCurve('ThreePoint', 10011, 11, 0.0, 270.38800513, 0.01184159, 270.38800513, 0.03552476, 189.27160359, -3234.43903611, 0.05, 2, 0, 70011, 21011, 1, 3)
    ops.uniaxialMaterial('LimitState', 30011, 67.59700128, 6.74e-05, 202.79100385, 0.00020221, 675.97001283, 0.00067402, -67.59700128, -6.74e-05, -202.79100385, -0.00020221, -675.97001283, -0.00067402, 0.4, 0.3, 0.003, 0.0, 0.0, 10011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 11, 99999, 'P', 40011, 'Vy', 30011, 'Vz', 20011, 'My', 10011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170011, 70011, 170011, 11, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121011, 121011, 21011, 11, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170012, 24.05, 4.25, 0.0)
    ops.node(121012, 24.05, 4.25, 2.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 12, 170012, 121012, 0.22, 28118265.11555659, 11715943.79814858, 0.00648267, 0.00322667, 0.00610042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20012, 178.82496176, 0.0005145, 217.3628973, 0.05391432, 21.73628973, 0.13368498, -178.82496176, -0.0005145, -217.3628973, -0.05391432, -21.73628973, -0.13368498, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10012, 162.42750002, 0.00059763, 197.43167652, 0.04827441, 19.74316765, 0.10923629, -162.42750002, -0.00059763, -197.43167652, -0.04827441, -19.74316765, -0.10923629, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20012, 12, 0.0, 298.03820664, 0.01028997, 298.03820664, 0.03086991, 208.62674465, -5582.69477615, 0.05, 2, 0, 70012, 21012, 2, 3)
    ops.uniaxialMaterial('LimitState', 40012, 74.50955166, 0.0001006, 223.52865498, 0.0003018, 745.09551661, 0.00100598, -74.50955166, -0.0001006, -223.52865498, -0.0003018, -745.09551661, -0.00100598, 0.4, 0.3, 0.003, 0.0, 0.0, 20012, 2)
    ops.limitCurve('ThreePoint', 10012, 12, 0.0, 231.99270596, 0.01195259, 231.99270596, 0.03585777, 162.39489417, -3606.50820751, 0.05, 2, 0, 70012, 21012, 1, 3)
    ops.uniaxialMaterial('LimitState', 30012, 57.99817649, 7.831e-05, 173.99452947, 0.00023492, 579.9817649, 0.00078306, -57.99817649, -7.831e-05, -173.99452947, -0.00023492, -579.9817649, -0.00078306, 0.4, 0.3, 0.003, 0.0, 0.0, 10012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 12, 99999, 'P', 40012, 'Vy', 30012, 'Vz', 20012, 'My', 10012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170012, 70012, 170012, 12, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121012, 121012, 21012, 12, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170013, 0.0, 8.5, 0.0)
    ops.node(121013, 0.0, 8.5, 2.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 13, 170013, 121013, 0.22, 27724003.17264619, 11551667.98860258, 0.00648267, 0.00322667, 0.00610042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20013, 182.40268525, 0.00053314, 221.85885453, 0.05224078, 22.18588545, 0.13125706, -182.40268525, -0.00053314, -221.85885453, -0.05224078, -22.18588545, -0.13125706, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10013, 164.33974501, 0.00062592, 199.88865588, 0.04679188, 19.98886559, 0.10717725, -164.33974501, -0.00062592, -199.88865588, -0.04679188, -19.98886559, -0.10717725, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20013, 13, 0.0, 282.0551067, 0.01066277, 282.0551067, 0.03198832, 197.43857469, -4865.33075315, 0.05, 2, 0, 70013, 21013, 2, 3)
    ops.uniaxialMaterial('LimitState', 40013, 70.51377667, 9.656e-05, 211.54133002, 0.00028967, 705.13776675, 0.00096557, -70.51377667, -9.656e-05, -211.54133002, -0.00028967, -705.13776675, -0.00096557, 0.4, 0.3, 0.003, 0.0, 0.0, 20013, 2)
    ops.limitCurve('ThreePoint', 10013, 13, 0.0, 220.07624129, 0.0125184, 220.07624129, 0.03755521, 154.0533689, -3185.80441618, 0.05, 2, 0, 70013, 21013, 1, 3)
    ops.uniaxialMaterial('LimitState', 30013, 55.01906032, 7.534e-05, 165.05718097, 0.00022602, 550.19060322, 0.0007534, -55.01906032, -7.534e-05, -165.05718097, -0.00022602, -550.19060322, -0.0007534, 0.4, 0.3, 0.003, 0.0, 0.0, 10013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 13, 99999, 'P', 40013, 'Vy', 30013, 'Vz', 20013, 'My', 10013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170013, 70013, 170013, 13, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121013, 121013, 21013, 13, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170014, 5.3, 8.5, 0.0)
    ops.node(121014, 5.3, 8.5, 2.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 14, 170014, 121014, 0.315, 25831942.59450376, 10763309.41437657, 0.01277375, 0.00584719, 0.01414875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20014, 356.01947269, 0.00049615, 434.20445375, 0.05255869, 43.42044538, 0.12069951, -356.01947269, -0.00049615, -434.20445375, -0.05255869, -43.42044538, -0.12069951, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10014, 317.83640411, 0.00058694, 387.63605032, 0.05197687, 38.76360503, 0.11804792, -317.83640411, -0.00058694, -387.63605032, -0.05197687, -38.76360503, -0.11804792, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20014, 14, 0.0, 501.96723677, 0.00992291, 501.96723677, 0.02976873, 351.37706574, -11054.60315395, 0.05, 2, 0, 70014, 21014, 2, 3)
    ops.uniaxialMaterial('LimitState', 40014, 125.49180919, 0.00012881, 376.47542758, 0.00038642, 1254.91809193, 0.00128807, -125.49180919, -0.00012881, -376.47542758, -0.00038642, -1254.91809193, -0.00128807, 0.4, 0.3, 0.003, 0.0, 0.0, 20014, 2)
    ops.limitCurve('ThreePoint', 10014, 14, 0.0, 270.83141044, 0.01173873, 270.83141044, 0.0352162, 189.58198731, -3500.654696, 0.05, 2, 0, 70014, 21014, 1, 3)
    ops.uniaxialMaterial('LimitState', 30014, 67.70785261, 6.95e-05, 203.12355783, 0.00020849, 677.0785261, 0.00069496, -67.70785261, -6.95e-05, -203.12355783, -0.00020849, -677.0785261, -0.00069496, 0.4, 0.3, 0.003, 0.0, 0.0, 10014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 14, 99999, 'P', 40014, 'Vy', 30014, 'Vz', 20014, 'My', 10014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170014, 70014, 170014, 14, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121014, 121014, 21014, 14, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170015, 10.6, 8.5, 0.0)
    ops.node(121015, 10.6, 8.5, 2.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 15, 170015, 121015, 0.175, 27659086.01206975, 11524619.17169573, 0.00405757, 0.0019651, 0.00401042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20015, 125.18584422, 0.00053861, 151.91779504, 0.03360028, 15.1917795, 0.09193873, -125.18584422, -0.00053861, -151.91779504, -0.03360028, -15.1917795, -0.09193873, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10015, 105.05175286, 0.0006538, 127.4843075, 0.02997731, 12.74843075, 0.07386553, -105.05175286, -0.0006538, -127.4843075, -0.02997731, -12.74843075, -0.07386553, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20015, 15, 0.0, 186.67058146, 0.01077223, 186.67058146, 0.03231668, 130.66940703, -2215.42250305, 0.05, 2, 0, 70015, 21015, 2, 3)
    ops.uniaxialMaterial('LimitState', 40015, 46.66764537, 8.052e-05, 140.0029361, 0.00024157, 466.67645366, 0.00080525, -46.66764537, -8.052e-05, -140.0029361, -0.00024157, -466.67645366, -0.00080525, 0.4, 0.3, 0.003, 0.0, 0.0, 20015, 2)
    ops.limitCurve('ThreePoint', 10015, 15, 0.0, 155.03625536, 0.01307606, 155.03625536, 0.03922819, 108.52537875, -1555.66048373, 0.05, 2, 0, 70015, 21015, 1, 3)
    ops.uniaxialMaterial('LimitState', 30015, 38.75906384, 6.688e-05, 116.27719152, 0.00020064, 387.59063839, 0.00066879, -38.75906384, -6.688e-05, -116.27719152, -0.00020064, -387.59063839, -0.00066879, 0.4, 0.3, 0.003, 0.0, 0.0, 10015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 15, 99999, 'P', 40015, 'Vy', 30015, 'Vz', 20015, 'My', 10015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170015, 70015, 170015, 15, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121015, 121015, 21015, 15, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170016, 13.45, 8.5, 0.0)
    ops.node(121016, 13.45, 8.5, 2.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 16, 170016, 121016, 0.175, 26153874.46889042, 10897447.69537101, 0.00405757, 0.0019651, 0.00401042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20016, 125.20093279, 0.00054493, 152.16713563, 0.03472474, 15.21671356, 0.08981389, -125.20093279, -0.00054493, -152.16713563, -0.03472474, -15.21671356, -0.08981389, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10016, 105.98456366, 0.00066117, 128.81187954, 0.0309764, 12.88118795, 0.07242014, -105.98456366, -0.00066117, -128.81187954, -0.0309764, -12.88118795, -0.07242014, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20016, 16, 0.0, 181.89034239, 0.01089869, 181.89034239, 0.03269607, 127.32323967, -2339.9297348, 0.05, 2, 0, 70016, 21016, 2, 3)
    ops.uniaxialMaterial('LimitState', 40016, 45.4725856, 8.298e-05, 136.41775679, 0.00024894, 454.72585597, 0.00082979, -45.4725856, -8.298e-05, -136.41775679, -0.00024894, -454.72585597, -0.00082979, 0.4, 0.3, 0.003, 0.0, 0.0, 20016, 2)
    ops.limitCurve('ThreePoint', 10016, 16, 0.0, 149.97885324, 0.01322346, 149.97885324, 0.03967038, 104.98519727, -1628.52955849, 0.05, 2, 0, 70016, 21016, 1, 3)
    ops.uniaxialMaterial('LimitState', 30016, 37.49471331, 6.842e-05, 112.48413993, 0.00020526, 374.9471331, 0.00068421, -37.49471331, -6.842e-05, -112.48413993, -0.00020526, -374.9471331, -0.00068421, 0.4, 0.3, 0.003, 0.0, 0.0, 10016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 16, 99999, 'P', 40016, 'Vy', 30016, 'Vz', 20016, 'My', 10016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170016, 70016, 170016, 16, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121016, 121016, 21016, 16, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170017, 18.75, 8.5, 0.0)
    ops.node(121017, 18.75, 8.5, 2.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 17, 170017, 121017, 0.315, 28943108.3151231, 12059628.46463462, 0.01277375, 0.00584719, 0.01414875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20017, 374.72647737, 0.00049427, 454.85848429, 0.05074088, 45.48584843, 0.12455721, -374.72647737, -0.00049427, -454.85848429, -0.05074088, -45.48584843, -0.12455721, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10017, 336.34990949, 0.0005805, 408.27542023, 0.05017796, 40.82754202, 0.12175213, -336.34990949, -0.0005805, -408.27542023, -0.05017796, -40.82754202, -0.12175213, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20017, 17, 0.0, 515.78367079, 0.00988536, 515.78367079, 0.02965609, 361.04856955, -9150.07352956, 0.05, 2, 0, 70017, 21017, 2, 3)
    ops.uniaxialMaterial('LimitState', 40017, 128.9459177, 0.00011813, 386.83775309, 0.00035438, 1289.45917698, 0.00118125, -128.9459177, -0.00011813, -386.83775309, -0.00035438, -1289.45917698, -0.00118125, 0.4, 0.3, 0.003, 0.0, 0.0, 20017, 2)
    ops.limitCurve('ThreePoint', 10017, 17, 0.0, 286.15323143, 0.01161006, 286.15323143, 0.03483018, 200.307262, -3036.16344325, 0.05, 2, 0, 70017, 21017, 1, 3)
    ops.uniaxialMaterial('LimitState', 30017, 71.53830786, 6.554e-05, 214.61492357, 0.00019661, 715.38307858, 0.00065535, -71.53830786, -6.554e-05, -214.61492357, -0.00019661, -715.38307858, -0.00065535, 0.4, 0.3, 0.003, 0.0, 0.0, 10017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 17, 99999, 'P', 40017, 'Vy', 30017, 'Vz', 20017, 'My', 10017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170017, 70017, 170017, 17, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121017, 121017, 21017, 17, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170018, 24.05, 8.5, 0.0)
    ops.node(121018, 24.05, 8.5, 2.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 18, 170018, 121018, 0.22, 29403977.48437407, 12251657.28515586, 0.00648267, 0.00322667, 0.00610042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20018, 181.45204074, 0.00052085, 220.00135801, 0.0520581, 22.0001358, 0.13403636, -181.45204074, -0.00052085, -220.00135801, -0.0520581, -22.0001358, -0.13403636, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10018, 162.84817991, 0.00060873, 197.44512425, 0.04662257, 19.74451242, 0.10927152, -162.84817991, -0.00060873, -197.44512425, -0.04662257, -19.74451242, -0.10927152, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20018, 18, 0.0, 292.23742658, 0.01041694, 292.23742658, 0.03125083, 204.56619861, -4711.76932624, 0.05, 2, 0, 70018, 21018, 2, 3)
    ops.uniaxialMaterial('LimitState', 40018, 73.05935665, 9.433e-05, 219.17806994, 0.00028298, 730.59356646, 0.00094327, -73.05935665, -9.433e-05, -219.17806994, -0.00028298, -730.59356646, -0.00094327, 0.4, 0.3, 0.003, 0.0, 0.0, 20018, 2)
    ops.limitCurve('ThreePoint', 10018, 18, 0.0, 228.74472924, 0.01217456, 228.74472924, 0.03652367, 160.12131047, -3095.35928656, 0.05, 2, 0, 70018, 21018, 1, 3)
    ops.uniaxialMaterial('LimitState', 30018, 57.18618231, 7.383e-05, 171.55854693, 0.0002215, 571.8618231, 0.00073833, -57.18618231, -7.383e-05, -171.55854693, -0.0002215, -571.8618231, -0.00073833, 0.4, 0.3, 0.003, 0.0, 0.0, 10018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 18, 99999, 'P', 40018, 'Vy', 30018, 'Vz', 20018, 'My', 10018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170018, 70018, 170018, 18, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121018, 121018, 21018, 18, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170019, 0.0, 12.75, 0.0)
    ops.node(121019, 0.0, 12.75, 2.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 19, 170019, 121019, 0.0875, 27578734.12184899, 11491139.21743708, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20019, 42.26116319, 0.00088211, 51.24344721, 0.02590695, 5.12434472, 0.07081661, -42.26116319, -0.00088211, -51.24344721, -0.02590695, -5.12434472, -0.07081661, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10019, 53.32754472, 0.00068222, 64.66190272, 0.0287463, 6.46619027, 0.0876878, -53.32754472, -0.00068222, -64.66190272, -0.0287463, -6.46619027, -0.0876878, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20019, 19, 0.0, 80.91766412, 0.01764214, 80.91766412, 0.05292642, 56.64236488, -858.39427917, 0.05, 2, 0, 70019, 21019, 2, 3)
    ops.uniaxialMaterial('LimitState', 40019, 20.22941603, 7.002e-05, 60.68824809, 0.00021005, 202.2941603, 0.00070015, -20.22941603, -7.002e-05, -60.68824809, -0.00021005, -202.2941603, -0.00070015, 0.4, 0.3, 0.003, 0.0, 0.0, 20019, 2)
    ops.limitCurve('ThreePoint', 10019, 19, 0.0, 91.51135435, 0.01364432, 91.51135435, 0.04093296, 64.05794805, -1197.36521632, 0.05, 2, 0, 70019, 21019, 1, 3)
    ops.uniaxialMaterial('LimitState', 30019, 22.87783859, 7.918e-05, 68.63351576, 0.00023754, 228.77838588, 0.00079181, -22.87783859, -7.918e-05, -68.63351576, -0.00023754, -228.77838588, -0.00079181, 0.4, 0.3, 0.003, 0.0, 0.0, 10019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 19, 99999, 'P', 40019, 'Vy', 30019, 'Vz', 20019, 'My', 10019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170019, 70019, 170019, 19, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121019, 121019, 21019, 19, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170020, 5.3, 12.75, 0.0)
    ops.node(121020, 5.3, 12.75, 2.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 20, 170020, 121020, 0.1925, 29347858.64705681, 12228274.43627367, 0.00475217, 0.00533786, 0.00216161, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20020, 117.14008976, 0.00066612, 141.92870248, 0.0397868, 14.19287025, 0.10087649, -117.14008976, -0.00066612, -141.92870248, -0.0397868, -14.19287025, -0.10087649, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10020, 149.98612878, 0.00052709, 181.72545959, 0.04655643, 18.17254596, 0.13640368, -149.98612878, -0.00052709, -181.72545959, -0.04655643, -18.17254596, -0.13640368, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20020, 20, 0.0, 192.88931634, 0.01332231, 192.88931634, 0.03996694, 135.02252144, -2262.43258376, 0.05, 2, 0, 70020, 21020, 2, 3)
    ops.uniaxialMaterial('LimitState', 40020, 48.22232908, 7.129e-05, 144.66698725, 0.00021387, 482.22329084, 0.0007129, -48.22232908, -7.129e-05, -144.66698725, -0.00021387, -482.22329084, -0.0007129, 0.4, 0.3, 0.003, 0.0, 0.0, 20020, 2)
    ops.limitCurve('ThreePoint', 10020, 20, 0.0, 258.95707353, 0.01054175, 258.95707353, 0.03162525, 181.26995147, -3941.52421518, 0.05, 2, 0, 70020, 21020, 1, 3)
    ops.uniaxialMaterial('LimitState', 30020, 64.73926838, 9.571e-05, 194.21780515, 0.00028713, 647.39268382, 0.00095709, -64.73926838, -9.571e-05, -194.21780515, -0.00028713, -647.39268382, -0.00095709, 0.4, 0.3, 0.003, 0.0, 0.0, 10020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 20, 99999, 'P', 40020, 'Vy', 30020, 'Vz', 20020, 'My', 10020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170020, 70020, 170020, 20, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121020, 121020, 21020, 20, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170021, 10.6, 12.75, 0.0)
    ops.node(121021, 10.6, 12.75, 2.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 21, 170021, 121021, 0.135, 25367381.45314012, 10569742.27214172, 0.002377, 0.00250594, 0.00111375, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20021, 71.42387561, 0.00076796, 86.90631792, 0.04613627, 8.69063179, 0.10793554, -71.42387561, -0.00076796, -86.90631792, -0.04613627, -8.69063179, -0.10793554, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10021, 90.96746592, 0.000589, 110.68634187, 0.0532933, 11.06863419, 0.14147758, -90.96746592, -0.000589, -110.68634187, -0.0532933, -11.06863419, -0.14147758, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20021, 21, 0.0, 153.85557145, 0.0153592, 153.85557145, 0.0460776, 107.69890002, -2884.59649883, 0.05, 2, 0, 70021, 21021, 2, 3)
    ops.uniaxialMaterial('LimitState', 40021, 38.46389286, 9.381e-05, 115.39167859, 0.00028142, 384.63892863, 0.00093807, -38.46389286, -9.381e-05, -115.39167859, -0.00028142, -384.63892863, -0.00093807, 0.4, 0.3, 0.003, 0.0, 0.0, 20021, 2)
    ops.limitCurve('ThreePoint', 10021, 21, 0.0, 194.36378286, 0.01177996, 194.36378286, 0.03533988, 136.054648, -5088.81703838, 0.05, 2, 0, 70021, 21021, 1, 3)
    ops.uniaxialMaterial('LimitState', 30021, 48.59094571, 0.0001185, 145.77283714, 0.00035551, 485.90945714, 0.00118505, -48.59094571, -0.0001185, -145.77283714, -0.00035551, -485.90945714, -0.00118505, 0.4, 0.3, 0.003, 0.0, 0.0, 10021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 21, 99999, 'P', 40021, 'Vy', 30021, 'Vz', 20021, 'My', 10021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170021, 70021, 170021, 21, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121021, 121021, 21021, 21, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170022, 13.45, 12.75, 0.0)
    ops.node(121022, 13.45, 12.75, 2.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 22, 170022, 121022, 0.135, 27624437.34542678, 11510182.22726116, 0.002377, 0.00250594, 0.00111375, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20022, 70.99790321, 0.00074445, 86.2095823, 0.04506922, 8.62095823, 0.11247747, -70.99790321, -0.00074445, -86.2095823, -0.04506922, -8.62095823, -0.11247747, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10022, 91.01213082, 0.00057333, 110.51196482, 0.05206537, 11.05119648, 0.14825336, -91.01213082, -0.00057333, -110.51196482, -0.05206537, -11.05119648, -0.14825336, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20022, 22, 0.0, 149.83527259, 0.01488891, 149.83527259, 0.04466672, 104.88469082, -2325.20642781, 0.05, 2, 0, 70022, 21022, 2, 3)
    ops.uniaxialMaterial('LimitState', 40022, 37.45881815, 8.389e-05, 112.37645445, 0.00025167, 374.58818149, 0.00083891, -37.45881815, -8.389e-05, -112.37645445, -0.00025167, -374.58818149, -0.00083891, 0.4, 0.3, 0.003, 0.0, 0.0, 20022, 2)
    ops.limitCurve('ThreePoint', 10022, 22, 0.0, 184.03768798, 0.0114667, 184.03768798, 0.03440009, 128.82638159, -3982.09926632, 0.05, 2, 0, 70022, 21022, 1, 3)
    ops.uniaxialMaterial('LimitState', 30022, 46.00942199, 0.00010304, 138.02826598, 0.00030912, 460.09421995, 0.00103041, -46.00942199, -0.00010304, -138.02826598, -0.00030912, -460.09421995, -0.00103041, 0.4, 0.3, 0.003, 0.0, 0.0, 10022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 22, 99999, 'P', 40022, 'Vy', 30022, 'Vz', 20022, 'My', 10022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170022, 70022, 170022, 22, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121022, 121022, 21022, 22, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170023, 18.75, 12.75, 0.0)
    ops.node(121023, 18.75, 12.75, 2.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 23, 170023, 121023, 0.1925, 25208998.17220958, 10503749.23842066, 0.00475217, 0.00533786, 0.00216161, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20023, 112.64887591, 0.00066976, 137.2370417, 0.04194073, 13.72370417, 0.0956525, -112.64887591, -0.00066976, -137.2370417, -0.04194073, -13.72370417, -0.0956525, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10023, 143.34852512, 0.00052882, 174.63758392, 0.04908818, 17.46375839, 0.1280844, -143.34852512, -0.00052882, -174.63758392, -0.04908818, -17.46375839, -0.1280844, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20023, 23, 0.0, 176.27332369, 0.0133953, 176.27332369, 0.04018589, 123.39132659, -2490.62411445, 0.05, 2, 0, 70023, 21023, 2, 3)
    ops.uniaxialMaterial('LimitState', 40023, 44.06833092, 7.585e-05, 132.20499277, 0.00022754, 440.68330923, 0.00075846, -44.06833092, -7.585e-05, -132.20499277, -0.00022754, -440.68330923, -0.00075846, 0.4, 0.3, 0.003, 0.0, 0.0, 20023, 2)
    ops.limitCurve('ThreePoint', 10023, 23, 0.0, 240.97160273, 0.01057632, 240.97160273, 0.03172897, 168.68012191, -4416.99259192, 0.05, 2, 0, 70023, 21023, 1, 3)
    ops.uniaxialMaterial('LimitState', 30023, 60.24290068, 0.00010368, 180.72870205, 0.00031105, 602.42900682, 0.00103684, -60.24290068, -0.00010368, -180.72870205, -0.00031105, -602.42900682, -0.00103684, 0.4, 0.3, 0.003, 0.0, 0.0, 10023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 23, 99999, 'P', 40023, 'Vy', 30023, 'Vz', 20023, 'My', 10023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170023, 70023, 170023, 23, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121023, 121023, 21023, 23, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170024, 24.05, 12.75, 0.0)
    ops.node(121024, 24.05, 12.75, 2.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 24, 170024, 121024, 0.0875, 27304250.14761152, 11376770.89483813, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20024, 41.3431643, 0.00086857, 50.14560574, 0.02583212, 5.01456057, 0.07027258, -41.3431643, -0.00086857, -50.14560574, -0.02583212, -5.01456057, -0.07027258, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10024, 52.28630131, 0.00067185, 63.41866414, 0.02866719, 6.34186641, 0.08699289, -52.28630131, -0.00067185, -63.41866414, -0.02866719, -6.34186641, -0.08699289, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20024, 24, 0.0, 80.12332274, 0.0173714, 80.12332274, 0.05211421, 56.08632592, -855.54989053, 0.05, 2, 0, 70024, 21024, 2, 3)
    ops.uniaxialMaterial('LimitState', 40024, 20.03083069, 7.002e-05, 60.09249206, 0.00021007, 200.30830685, 0.00070025, -20.03083069, -7.002e-05, -60.09249206, -0.00021007, -200.30830685, -0.00070025, 0.4, 0.3, 0.003, 0.0, 0.0, 20024, 2)
    ops.limitCurve('ThreePoint', 10024, 24, 0.0, 90.67820415, 0.01343696, 90.67820415, 0.04031087, 63.4747429, -1192.66281089, 0.05, 2, 0, 70024, 21024, 1, 3)
    ops.uniaxialMaterial('LimitState', 30024, 22.66955104, 7.925e-05, 68.00865311, 0.00023775, 226.69551037, 0.00079249, -22.66955104, -7.925e-05, -68.00865311, -0.00023775, -226.69551037, -0.00079249, 0.4, 0.3, 0.003, 0.0, 0.0, 10024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 24, 99999, 'P', 40024, 'Vy', 30024, 'Vz', 20024, 'My', 10024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170024, 70024, 170024, 24, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121024, 121024, 21024, 24, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171001, 0.0, 0.0, 3.175)
    ops.node(122001, 0.0, 0.0, 5.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1001, 171001, 122001, 0.0875, 25529056.92288116, 10637107.05120048, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21001, 46.65421065, 0.00096336, 56.87113929, 0.04074498, 5.68711393, 0.09863797, -46.65421065, -0.00096336, -56.87113929, -0.04074498, -5.68711393, -0.09863797, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11001, 55.33965815, 0.00072015, 67.45863586, 0.04561388, 6.74586359, 0.12273418, -55.33965815, -0.00072015, -67.45863586, -0.04561388, -6.74586359, -0.12273418, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21001, 1001, 0.0, 89.57841974, 0.01926728, 89.57841974, 0.05780183, 62.70489382, -1557.12142788, 0.05, 2, 0, 71001, 22001, 2, 3)
    ops.uniaxialMaterial('LimitState', 41001, 22.39460493, 8.373e-05, 67.1838148, 0.0002512, 223.94604934, 0.00083732, -22.39460493, -8.373e-05, -67.1838148, -0.0002512, -223.94604934, -0.00083732, 0.4, 0.3, 0.003, 0.0, 0.0, 21001, 2)
    ops.limitCurve('ThreePoint', 11001, 1001, 0.0, 107.08231527, 0.01440291, 107.08231527, 0.04320872, 74.95762069, -2481.47357958, 0.05, 2, 0, 71001, 22001, 1, 3)
    ops.uniaxialMaterial('LimitState', 31001, 26.77057882, 0.00010009, 80.31173645, 0.00030028, 267.70578818, 0.00100093, -26.77057882, -0.00010009, -80.31173645, -0.00030028, -267.70578818, -0.00100093, 0.4, 0.3, 0.003, 0.0, 0.0, 11001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1001, 99999, 'P', 41001, 'Vy', 31001, 'Vz', 21001, 'My', 11001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171001, 71001, 171001, 1001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122001, 122001, 22001, 1001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171002, 5.3, 0.0, 3.175)
    ops.node(122002, 5.3, 0.0, 5.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1002, 171002, 122002, 0.1925, 25777876.2481099, 10740781.77004579, 0.00475217, 0.00533786, 0.00216161, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21002, 70.65567368, 0.00065447, 86.28897992, 0.02432161, 8.62889799, 0.05969765, -70.65567368, -0.00065447, -86.28897992, -0.02432161, -8.62889799, -0.05969765, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11002, 138.78417248, 0.00051788, 169.4916211, 0.02773842, 16.94916211, 0.07703489, -138.78417248, -0.00051788, -169.4916211, -0.02773842, -16.94916211, -0.07703489, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21002, 1002, 0.0, 137.2532885, 0.01308939, 137.2532885, 0.03926817, 96.07730195, -1276.03059812, 0.05, 2, 0, 71002, 22002, 2, 3)
    ops.uniaxialMaterial('LimitState', 41002, 34.31332213, 5.775e-05, 102.93996638, 0.00017326, 343.13322126, 0.00057753, -34.31332213, -5.775e-05, -102.93996638, -0.00017326, -343.13322126, -0.00057753, 0.4, 0.3, 0.003, 0.0, 0.0, 21002, 2)
    ops.limitCurve('ThreePoint', 11002, 1002, 0.0, 180.80421501, 0.01035752, 180.80421501, 0.03107257, 126.56295051, -2114.02591633, 0.05, 2, 0, 71002, 22002, 1, 3)
    ops.uniaxialMaterial('LimitState', 31002, 45.20105375, 7.608e-05, 135.60316126, 0.00022824, 452.01053753, 0.00076078, -45.20105375, -7.608e-05, -135.60316126, -0.00022824, -452.01053753, -0.00076078, 0.4, 0.3, 0.003, 0.0, 0.0, 11002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1002, 99999, 'P', 41002, 'Vy', 31002, 'Vz', 21002, 'My', 11002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171002, 71002, 171002, 1002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122002, 122002, 22002, 1002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171005, 18.75, 0.0, 3.175)
    ops.node(122005, 18.75, 0.0, 5.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1005, 171005, 122005, 0.1925, 28011290.64789016, 11671371.10328757, 0.00475217, 0.00533786, 0.00216161, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21005, 70.82777635, 0.00062051, 86.21016147, 0.02558982, 8.62101615, 0.06286877, -70.82777635, -0.00062051, -86.21016147, -0.02558982, -8.62101615, -0.06286877, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11005, 139.12515591, 0.00049945, 169.34037426, 0.02921767, 16.93403743, 0.08116586, -139.12515591, -0.00049945, -169.34037426, -0.02921767, -16.93403743, -0.08116586, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21005, 1005, 0.0, 152.3371846, 0.01241011, 152.3371846, 0.03723034, 106.63602922, -1377.48764301, 0.05, 2, 0, 71005, 22005, 2, 3)
    ops.uniaxialMaterial('LimitState', 41005, 38.08429615, 5.899e-05, 114.25288845, 0.00017697, 380.84296149, 0.00058989, -38.08429615, -5.899e-05, -114.25288845, -0.00017697, -380.84296149, -0.00058989, 0.4, 0.3, 0.003, 0.0, 0.0, 21005, 2)
    ops.limitCurve('ThreePoint', 11005, 1005, 0.0, 200.21545934, 0.00998907, 200.21545934, 0.0299672, 140.15082154, -2320.10413, 0.05, 2, 0, 71005, 22005, 1, 3)
    ops.uniaxialMaterial('LimitState', 31005, 50.05386484, 7.753e-05, 150.16159451, 0.00023259, 500.53864835, 0.00077529, -50.05386484, -7.753e-05, -150.16159451, -0.00023259, -500.53864835, -0.00077529, 0.4, 0.3, 0.003, 0.0, 0.0, 11005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1005, 99999, 'P', 41005, 'Vy', 31005, 'Vz', 21005, 'My', 11005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171005, 71005, 171005, 1005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122005, 122005, 22005, 1005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171006, 24.05, 0.0, 3.175)
    ops.node(122006, 24.05, 0.0, 5.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1006, 171006, 122006, 0.0875, 26384825.93716229, 10993677.47381762, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21006, 44.74779509, 0.00087053, 54.50380713, 0.03916082, 5.45038071, 0.09881017, -44.74779509, -0.00087053, -54.50380713, -0.03916082, -5.45038071, -0.09881017, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11006, 52.7015053, 0.00066267, 64.1916026, 0.04387344, 6.41916026, 0.12333341, -52.7015053, -0.00066267, -64.1916026, -0.04387344, -6.41916026, -0.12333341, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21006, 1006, 0.0, 86.38927433, 0.01741051, 86.38927433, 0.05223152, 60.47249203, -1321.44010408, 0.05, 2, 0, 71006, 22006, 2, 3)
    ops.uniaxialMaterial('LimitState', 41006, 21.59731858, 7.813e-05, 64.79195575, 0.0002344, 215.97318583, 0.00078132, -21.59731858, -7.813e-05, -64.79195575, -0.0002344, -215.97318583, -0.00078132, 0.4, 0.3, 0.003, 0.0, 0.0, 21006, 2)
    ops.limitCurve('ThreePoint', 11006, 1006, 0.0, 101.79097378, 0.01325336, 101.79097378, 0.03976008, 71.25368164, -2066.8049767, 0.05, 2, 0, 71006, 22006, 1, 3)
    ops.uniaxialMaterial('LimitState', 31006, 25.44774344, 9.206e-05, 76.34323033, 0.00027618, 254.47743444, 0.00092061, -25.44774344, -9.206e-05, -76.34323033, -0.00027618, -254.47743444, -0.00092061, 0.4, 0.3, 0.003, 0.0, 0.0, 11006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1006, 99999, 'P', 41006, 'Vy', 31006, 'Vz', 21006, 'My', 11006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171006, 71006, 171006, 1006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122006, 122006, 22006, 1006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171007, 0.0, 4.25, 3.15)
    ops.node(122007, 0.0, 4.25, 5.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1007, 171007, 122007, 0.22, 25619034.26883273, 10674597.61201364, 0.00648267, 0.00322667, 0.00610042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21007, 127.28970297, 0.00052315, 155.62065185, 0.05127744, 15.56206518, 0.13127332, -127.28970297, -0.00052315, -155.62065185, -0.05127744, -15.56206518, -0.13127332, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11007, 103.23563744, 0.00061059, 126.2128579, 0.05301509, 12.62128579, 0.13931887, -103.23563744, -0.00061059, -126.2128579, -0.05301509, -12.62128579, -0.13931887, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21007, 1007, 0.0, 304.53355563, 0.01046308, 304.53355563, 0.03138924, 213.17348894, -9195.2294158, 0.05, 2, 0, 71007, 22007, 2, 3)
    ops.uniaxialMaterial('LimitState', 41007, 76.13338891, 0.00011282, 228.40016672, 0.00033846, 761.33388908, 0.00112818, -76.13338891, -0.00011282, -228.40016672, -0.00033846, -761.33388908, -0.00112818, 0.4, 0.3, 0.003, 0.0, 0.0, 21007, 2)
    ops.limitCurve('ThreePoint', 11007, 1007, 0.0, 192.17808344, 0.01221184, 192.17808344, 0.03663552, 134.52465841, -3099.05579954, 0.05, 2, 0, 71007, 22007, 1, 3)
    ops.uniaxialMaterial('LimitState', 31007, 48.04452086, 7.119e-05, 144.13356258, 0.00021358, 480.4452086, 0.00071195, -48.04452086, -7.119e-05, -144.13356258, -0.00021358, -480.4452086, -0.00071195, 0.4, 0.3, 0.003, 0.0, 0.0, 11007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1007, 99999, 'P', 41007, 'Vy', 31007, 'Vz', 21007, 'My', 11007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171007, 71007, 171007, 1007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122007, 122007, 22007, 1007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171008, 5.3, 4.25, 3.15)
    ops.node(122008, 5.3, 4.25, 5.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1008, 171008, 122008, 0.315, 26354583.35465271, 10981076.39777196, 0.01277375, 0.00584719, 0.01414875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21008, 291.34875161, 0.00047977, 355.89163408, 0.02145247, 35.58916341, 0.05369899, -291.34875161, -0.00047977, -355.89163408, -0.02145247, -35.58916341, -0.05369899, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11008, 146.54691621, 0.00056122, 179.01165249, 0.01937072, 17.90116525, 0.04427864, -146.54691621, -0.00056122, -179.01165249, -0.01937072, -17.90116525, -0.04427864, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21008, 1008, 0.0, 299.01103275, 0.00959548, 299.01103275, 0.02878644, 209.30772293, -1630.24493153, 0.05, 2, 0, 71008, 22008, 2, 3)
    ops.uniaxialMaterial('LimitState', 41008, 74.75275819, 7.521e-05, 224.25827456, 0.00022562, 747.52758188, 0.00075206, -74.75275819, -7.521e-05, -224.25827456, -0.00022562, -747.52758188, -0.00075206, 0.4, 0.3, 0.003, 0.0, 0.0, 21008, 2)
    ops.limitCurve('ThreePoint', 11008, 1008, 0.0, 193.33014257, 0.01122443, 193.33014257, 0.03367328, 135.3310998, -1121.95643653, 0.05, 2, 0, 71008, 22008, 1, 3)
    ops.uniaxialMaterial('LimitState', 31008, 48.33253564, 4.863e-05, 144.99760693, 0.00014588, 483.32535643, 0.00048625, -48.33253564, -4.863e-05, -144.99760693, -0.00014588, -483.32535643, -0.00048625, 0.4, 0.3, 0.003, 0.0, 0.0, 11008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1008, 99999, 'P', 41008, 'Vy', 31008, 'Vz', 21008, 'My', 11008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171008, 71008, 171008, 1008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122008, 122008, 22008, 1008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171009, 10.6, 4.25, 3.15)
    ops.node(122009, 10.6, 4.25, 5.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1009, 171009, 122009, 0.24, 26971058.91961571, 11237941.21650655, 0.00751249, 0.00352, 0.00792, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21009, 181.21119298, 0.00049051, 220.92854226, 0.03316039, 22.09285423, 0.078867, -181.21119298, -0.00049051, -220.92854226, -0.03316039, -22.09285423, -0.078867, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11009, 102.22150825, 0.00058151, 124.62612509, 0.02951209, 12.46261251, 0.06376954, -102.22150825, -0.00058151, -124.62612509, -0.02951209, -12.46261251, -0.06376954, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21009, 1009, 0.0, 244.60989971, 0.00981027, 244.60989971, 0.02943082, 171.2269298, -2414.57970663, 0.05, 2, 0, 71009, 22009, 2, 3)
    ops.uniaxialMaterial('LimitState', 41009, 61.15247493, 7.89e-05, 183.45742478, 0.00023671, 611.52474928, 0.00078903, -61.15247493, -7.89e-05, -183.45742478, -0.00023671, -611.52474928, -0.00078903, 0.4, 0.3, 0.003, 0.0, 0.0, 21009, 2)
    ops.limitCurve('ThreePoint', 11009, 1009, 0.0, 178.30231251, 0.01163023, 178.30231251, 0.0348907, 124.81161875, -1555.28172838, 0.05, 2, 0, 71009, 22009, 1, 3)
    ops.uniaxialMaterial('LimitState', 31009, 44.57557813, 5.751e-05, 133.72673438, 0.00017254, 445.75578126, 0.00057515, -44.57557813, -5.751e-05, -133.72673438, -0.00017254, -445.75578126, -0.00057515, 0.4, 0.3, 0.003, 0.0, 0.0, 11009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1009, 99999, 'P', 41009, 'Vy', 31009, 'Vz', 21009, 'My', 11009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171009, 71009, 171009, 1009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122009, 122009, 22009, 1009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171010, 13.45, 4.25, 3.15)
    ops.node(122010, 13.45, 4.25, 5.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1010, 171010, 122010, 0.24, 27469101.87824628, 11445459.11593595, 0.00751249, 0.00352, 0.00792, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21010, 187.49642881, 0.0005063, 228.41019833, 0.03287099, 22.84101983, 0.07909393, -187.49642881, -0.0005063, -228.41019833, -0.03287099, -22.84101983, -0.07909393, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11010, 105.65000603, 0.0006059, 128.70399178, 0.02926621, 12.87039918, 0.06391066, -105.65000603, -0.0006059, -128.70399178, -0.02926621, -12.87039918, -0.06391066, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21010, 1010, 0.0, 248.10086228, 0.01012608, 248.10086228, 0.03037823, 173.67060359, -2376.80733195, 0.05, 2, 0, 71010, 22010, 2, 3)
    ops.uniaxialMaterial('LimitState', 41010, 62.02521557, 7.858e-05, 186.07564671, 0.00023574, 620.25215569, 0.00078578, -62.02521557, -7.858e-05, -186.07564671, -0.00023574, -620.25215569, -0.00078578, 0.4, 0.3, 0.003, 0.0, 0.0, 21010, 2)
    ops.limitCurve('ThreePoint', 11010, 1010, 0.0, 181.02395427, 0.01211794, 181.02395427, 0.03635383, 126.71676799, -1535.05821626, 0.05, 2, 0, 71010, 22010, 1, 3)
    ops.uniaxialMaterial('LimitState', 31010, 45.25598857, 5.733e-05, 135.7679657, 0.000172, 452.55988568, 0.00057334, -45.25598857, -5.733e-05, -135.7679657, -0.000172, -452.55988568, -0.00057334, 0.4, 0.3, 0.003, 0.0, 0.0, 11010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1010, 99999, 'P', 41010, 'Vy', 31010, 'Vz', 21010, 'My', 11010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171010, 71010, 171010, 1010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122010, 122010, 22010, 1010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171011, 18.75, 4.25, 3.15)
    ops.node(122011, 18.75, 4.25, 5.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1011, 171011, 122011, 0.315, 26253179.92213515, 10938824.96755631, 0.01277375, 0.00584719, 0.01414875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21011, 300.87508588, 0.00048632, 367.58149451, 0.02029765, 36.75814945, 0.05247191, -300.87508588, -0.00048632, -367.58149451, -0.02029765, -36.75814945, -0.05247191, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11011, 150.59183067, 0.00056885, 183.97924181, 0.01833677, 18.39792418, 0.04318887, -150.59183067, -0.00056885, -183.97924181, -0.01833677, -18.39792418, -0.04318887, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21011, 1011, 0.0, 295.22868422, 0.0097265, 295.22868422, 0.02917949, 206.66007895, -1556.47190941, 0.05, 2, 0, 71011, 22011, 2, 3)
    ops.uniaxialMaterial('LimitState', 41011, 73.80717105, 7.454e-05, 221.42151316, 0.00022362, 738.07171055, 0.00074541, -73.80717105, -7.454e-05, -221.42151316, -0.00022362, -738.07171055, -0.00074541, 0.4, 0.3, 0.003, 0.0, 0.0, 21011, 2)
    ops.limitCurve('ThreePoint', 11011, 1011, 0.0, 190.89259317, 0.01137705, 190.89259317, 0.03413114, 133.62481522, -1082.51036048, 0.05, 2, 0, 71011, 22011, 1, 3)
    ops.uniaxialMaterial('LimitState', 31011, 47.72314829, 4.82e-05, 143.16944488, 0.00014459, 477.23148292, 0.00048198, -47.72314829, -4.82e-05, -143.16944488, -0.00014459, -477.23148292, -0.00048198, 0.4, 0.3, 0.003, 0.0, 0.0, 11011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1011, 99999, 'P', 41011, 'Vy', 31011, 'Vz', 21011, 'My', 11011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171011, 71011, 171011, 1011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122011, 122011, 22011, 1011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171012, 24.05, 4.25, 3.15)
    ops.node(122012, 24.05, 4.25, 5.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1012, 171012, 122012, 0.22, 28204584.60188689, 11751910.25078621, 0.00648267, 0.00322667, 0.00610042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21012, 127.23681545, 0.00051104, 154.91455055, 0.05147596, 15.49145505, 0.13585037, -127.23681545, -0.00051104, -154.91455055, -0.05147596, -15.49145505, -0.13585037, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11012, 102.64721736, 0.00059448, 124.97599445, 0.05321647, 12.49759944, 0.14424404, -102.64721736, -0.00059448, -124.97599445, -0.05321647, -12.49759944, -0.14424404, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21012, 1012, 0.0, 331.27098531, 0.01022074, 331.27098531, 0.03066221, 231.88968972, -9857.59856007, 0.05, 2, 0, 71012, 22012, 2, 3)
    ops.uniaxialMaterial('LimitState', 41012, 82.81774633, 0.00011147, 248.45323898, 0.00033442, 828.17746327, 0.00111473, -82.81774633, -0.00011147, -248.45323898, -0.00033442, -828.17746327, -0.00111473, 0.4, 0.3, 0.003, 0.0, 0.0, 21012, 2)
    ops.limitCurve('ThreePoint', 11012, 1012, 0.0, 211.65400903, 0.01188956, 211.65400903, 0.03566867, 148.15780632, -3284.96164076, 0.05, 2, 0, 71012, 22012, 1, 3)
    ops.uniaxialMaterial('LimitState', 31012, 52.91350226, 7.122e-05, 158.74050677, 0.00021367, 529.13502258, 0.00071222, -52.91350226, -7.122e-05, -158.74050677, -0.00021367, -529.13502258, -0.00071222, 0.4, 0.3, 0.003, 0.0, 0.0, 11012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1012, 99999, 'P', 41012, 'Vy', 31012, 'Vz', 21012, 'My', 11012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171012, 71012, 171012, 1012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122012, 122012, 22012, 1012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171013, 0.0, 8.5, 3.15)
    ops.node(122013, 0.0, 8.5, 5.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1013, 171013, 122013, 0.22, 27532434.52446334, 11471847.71852639, 0.00648267, 0.00322667, 0.00610042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21013, 126.55156522, 0.00051339, 154.27629255, 0.05017036, 15.42762926, 0.1335543, -126.55156522, -0.00051339, -154.27629255, -0.05017036, -15.42762926, -0.1335543, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11013, 102.00907223, 0.0005983, 124.35706696, 0.05186981, 12.4357067, 0.14182881, -102.00907223, -0.0005983, -124.35706696, -0.05186981, -12.4357067, -0.14182881, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21013, 1013, 0.0, 306.0467285, 0.01026773, 306.0467285, 0.03080319, 214.23270995, -8138.76671313, 0.05, 2, 0, 71013, 22013, 2, 3)
    ops.uniaxialMaterial('LimitState', 41013, 76.51168212, 0.0001055, 229.53504637, 0.0003165, 765.11682124, 0.001055, -76.51168212, -0.0001055, -229.53504637, -0.0003165, -765.11682124, -0.001055, 0.4, 0.3, 0.003, 0.0, 0.0, 21013, 2)
    ops.limitCurve('ThreePoint', 11013, 1013, 0.0, 197.69360621, 0.01196597, 197.69360621, 0.03589791, 138.38552435, -2800.1931133, 0.05, 2, 0, 71013, 22013, 1, 3)
    ops.uniaxialMaterial('LimitState', 31013, 49.42340155, 6.815e-05, 148.27020466, 0.00020445, 494.23401553, 0.00068148, -49.42340155, -6.815e-05, -148.27020466, -0.00020445, -494.23401553, -0.00068148, 0.4, 0.3, 0.003, 0.0, 0.0, 11013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1013, 99999, 'P', 41013, 'Vy', 31013, 'Vz', 21013, 'My', 11013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171013, 71013, 171013, 1013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122013, 122013, 22013, 1013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171014, 5.3, 8.5, 3.15)
    ops.node(122014, 5.3, 8.5, 5.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1014, 171014, 122014, 0.315, 27624398.41257858, 11510166.00524108, 0.01277375, 0.00584719, 0.01414875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21014, 293.63336545, 0.00047764, 357.93727602, 0.02111919, 35.7937276, 0.0541881, -293.63336545, -0.00047764, -357.93727602, -0.02111919, -35.7937276, -0.0541881, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11014, 147.99281757, 0.00055768, 180.40233919, 0.01907019, 18.04023392, 0.04461334, -147.99281757, -0.00055768, -180.40233919, -0.01907019, -18.04023392, -0.04461334, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21014, 1014, 0.0, 317.54226456, 0.00955272, 317.54226456, 0.02865815, 222.27958519, -1670.91730064, 0.05, 2, 0, 71014, 22014, 2, 3)
    ops.uniaxialMaterial('LimitState', 41014, 79.38556614, 7.62e-05, 238.15669842, 0.00022859, 793.85566139, 0.00076195, -79.38556614, -7.62e-05, -238.15669842, -0.00022859, -793.85566139, -0.00076195, 0.4, 0.3, 0.003, 0.0, 0.0, 21014, 2)
    ops.limitCurve('ThreePoint', 11014, 1014, 0.0, 205.31993135, 0.01115369, 205.31993135, 0.03346106, 143.72395195, -1143.61715589, 0.05, 2, 0, 71014, 22014, 1, 3)
    ops.uniaxialMaterial('LimitState', 31014, 51.32998284, 4.927e-05, 153.98994852, 0.0001478, 513.29982838, 0.00049267, -51.32998284, -4.927e-05, -153.98994852, -0.0001478, -513.29982838, -0.00049267, 0.4, 0.3, 0.003, 0.0, 0.0, 11014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1014, 99999, 'P', 41014, 'Vy', 31014, 'Vz', 21014, 'My', 11014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171014, 71014, 171014, 1014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122014, 122014, 22014, 1014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171015, 10.6, 8.5, 3.15)
    ops.node(122015, 10.6, 8.5, 5.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1015, 171015, 122015, 0.175, 27130705.82017782, 11304460.75840742, 0.00405757, 0.0019651, 0.00401042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21015, 127.13803434, 0.00051548, 154.80177242, 0.02948524, 15.48017724, 0.07872574, -127.13803434, -0.00051548, -154.80177242, -0.02948524, -15.48017724, -0.07872574, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11015, 71.39448838, 0.0006158, 86.92908774, 0.02651902, 8.69290877, 0.06428147, -71.39448838, -0.0006158, -86.92908774, -0.02651902, -8.69290877, -0.06428147, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21015, 1015, 0.0, 167.80695879, 0.01030969, 167.80695879, 0.03092908, 117.46487115, -1967.4805338, 0.05, 2, 0, 71015, 22015, 2, 3)
    ops.uniaxialMaterial('LimitState', 41015, 41.9517397, 7.38e-05, 125.85521909, 0.00022139, 419.51739697, 0.00073797, -41.9517397, -7.38e-05, -125.85521909, -0.00022139, -419.51739697, -0.00073797, 0.4, 0.3, 0.003, 0.0, 0.0, 21015, 2)
    ops.limitCurve('ThreePoint', 11015, 1015, 0.0, 139.78895752, 0.01231601, 139.78895752, 0.03694803, 97.85227027, -1339.53925152, 0.05, 2, 0, 71015, 22015, 1, 3)
    ops.uniaxialMaterial('LimitState', 31015, 34.94723938, 6.148e-05, 104.84171814, 0.00018443, 349.47239381, 0.00061476, -34.94723938, -6.148e-05, -104.84171814, -0.00018443, -349.47239381, -0.00061476, 0.4, 0.3, 0.003, 0.0, 0.0, 11015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1015, 99999, 'P', 41015, 'Vy', 31015, 'Vz', 21015, 'My', 11015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171015, 71015, 171015, 1015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122015, 122015, 22015, 1015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171016, 13.45, 8.5, 3.15)
    ops.node(122016, 13.45, 8.5, 5.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1016, 171016, 122016, 0.175, 28993110.08850084, 12080462.53687535, 0.00405757, 0.0019651, 0.00401042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21016, 127.61798183, 0.00051386, 154.88219111, 0.02945241, 15.48821911, 0.08086785, -127.61798183, -0.00051386, -154.88219111, -0.02945241, -15.48821911, -0.08086785, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11016, 72.04455351, 0.00061477, 87.43609752, 0.02649009, 8.74360975, 0.06592049, -72.04455351, -0.00061477, -87.43609752, -0.02649009, -8.74360975, -0.06592049, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21016, 1016, 0.0, 180.49094405, 0.0102771, 180.49094405, 0.03083131, 126.34366083, -2057.82074222, 0.05, 2, 0, 71016, 22016, 2, 3)
    ops.uniaxialMaterial('LimitState', 41016, 45.12273601, 7.428e-05, 135.36820804, 0.00022283, 451.22736012, 0.00074277, -45.12273601, -7.428e-05, -135.36820804, -0.00022283, -451.22736012, -0.00074277, 0.4, 0.3, 0.003, 0.0, 0.0, 21016, 2)
    ops.limitCurve('ThreePoint', 11016, 1016, 0.0, 150.80534384, 0.01229531, 150.80534384, 0.03688592, 105.56374068, -1391.63015023, 0.05, 2, 0, 71016, 22016, 1, 3)
    ops.uniaxialMaterial('LimitState', 31016, 37.70133596, 6.206e-05, 113.10400788, 0.00018618, 377.01335959, 0.0006206, -37.70133596, -6.206e-05, -113.10400788, -0.00018618, -377.01335959, -0.0006206, 0.4, 0.3, 0.003, 0.0, 0.0, 11016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1016, 99999, 'P', 41016, 'Vy', 31016, 'Vz', 21016, 'My', 11016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171016, 71016, 171016, 1016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122016, 122016, 22016, 1016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171017, 18.75, 8.5, 3.15)
    ops.node(122017, 18.75, 8.5, 5.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1017, 171017, 122017, 0.315, 27939068.65764095, 11641278.60735039, 0.01277375, 0.00584719, 0.01414875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21017, 287.8372561, 0.00048137, 350.66464153, 0.02253775, 35.06646415, 0.05578885, -287.8372561, -0.00048137, -350.66464153, -0.02253775, -35.06646415, -0.05578885, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11017, 146.30718087, 0.0005686, 178.24223253, 0.02035001, 17.82422325, 0.04603389, -146.30718087, -0.0005686, -178.24223253, -0.02035001, -17.82422325, -0.04603389, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21017, 1017, 0.0, 325.77642165, 0.0096273, 325.77642165, 0.02888191, 228.04349515, -1794.07696581, 0.05, 2, 0, 71017, 22017, 2, 3)
    ops.uniaxialMaterial('LimitState', 41017, 81.44410541, 7.729e-05, 244.33231624, 0.00023187, 814.44105412, 0.00077291, -81.44410541, -7.729e-05, -244.33231624, -0.00023187, -814.44105412, -0.00077291, 0.4, 0.3, 0.003, 0.0, 0.0, 21017, 2)
    ops.limitCurve('ThreePoint', 11017, 1017, 0.0, 210.6327119, 0.01137194, 210.6327119, 0.03411582, 147.44289833, -1208.85823103, 0.05, 2, 0, 71017, 22017, 1, 3)
    ops.uniaxialMaterial('LimitState', 31017, 52.65817797, 4.997e-05, 157.97453392, 0.00014992, 526.58177974, 0.00049973, -52.65817797, -4.997e-05, -157.97453392, -0.00014992, -526.58177974, -0.00049973, 0.4, 0.3, 0.003, 0.0, 0.0, 11017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1017, 99999, 'P', 41017, 'Vy', 31017, 'Vz', 21017, 'My', 11017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171017, 71017, 171017, 1017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122017, 122017, 22017, 1017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171018, 24.05, 8.5, 3.15)
    ops.node(122018, 24.05, 8.5, 5.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1018, 171018, 122018, 0.22, 26018517.25641327, 10841048.85683887, 0.00648267, 0.00322667, 0.00610042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21018, 121.2675641, 0.00050686, 148.18381293, 0.05151369, 14.81838129, 0.13229488, -121.2675641, -0.00050686, -148.18381293, -0.05151369, -14.81838129, -0.13229488, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11018, 97.26157463, 0.0005915, 118.84951337, 0.05325675, 11.88495134, 0.14040777, -97.26157463, -0.0005915, -118.84951337, -0.05325675, -11.88495134, -0.14040777, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21018, 1018, 0.0, 316.02738127, 0.01013728, 316.02738127, 0.03041184, 221.21916689, -9953.9144863, 0.05, 2, 0, 71018, 22018, 2, 3)
    ops.uniaxialMaterial('LimitState', 41018, 79.00684532, 0.00011528, 237.02053595, 0.00034584, 790.06845318, 0.00115279, -79.00684532, -0.00011528, -237.02053595, -0.00034584, -790.06845318, -0.00115279, 0.4, 0.3, 0.003, 0.0, 0.0, 21018, 2)
    ops.limitCurve('ThreePoint', 11018, 1018, 0.0, 198.73148717, 0.01182998, 198.73148717, 0.03548994, 139.11204102, -3311.90890518, 0.05, 2, 0, 71018, 22018, 1, 3)
    ops.uniaxialMaterial('LimitState', 31018, 49.68287179, 7.249e-05, 149.04861538, 0.00021748, 496.82871793, 0.00072492, -49.68287179, -7.249e-05, -149.04861538, -0.00021748, -496.82871793, -0.00072492, 0.4, 0.3, 0.003, 0.0, 0.0, 11018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1018, 99999, 'P', 41018, 'Vy', 31018, 'Vz', 21018, 'My', 11018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171018, 71018, 171018, 1018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122018, 122018, 22018, 1018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171019, 0.0, 12.75, 3.175)
    ops.node(122019, 0.0, 12.75, 5.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1019, 171019, 122019, 0.0875, 28488648.32723416, 11870270.13634757, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21019, 48.68391202, 0.000868, 59.11517575, 0.03851196, 5.91151757, 0.10172638, -48.68391202, -0.000868, -59.11517575, -0.03851196, -5.91151757, -0.10172638, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11019, 56.3772322, 0.00066852, 68.45690602, 0.0431499, 6.8456906, 0.12735897, -56.3772322, -0.00066852, -68.45690602, -0.0431499, -6.8456906, -0.12735897, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21019, 1019, 0.0, 90.81432229, 0.01735996, 90.81432229, 0.05207989, 63.5700256, -1286.24419594, 0.05, 2, 0, 71019, 22019, 2, 3)
    ops.uniaxialMaterial('LimitState', 41019, 22.70358057, 7.607e-05, 68.11074171, 0.00022821, 227.03580571, 0.00076069, -22.70358057, -7.607e-05, -68.11074171, -0.00022821, -227.03580571, -0.00076069, 0.4, 0.3, 0.003, 0.0, 0.0, 21019, 2)
    ops.limitCurve('ThreePoint', 11019, 1019, 0.0, 105.88645334, 0.01337031, 105.88645334, 0.04011093, 74.12051734, -2005.23117145, 0.05, 2, 0, 71019, 22019, 1, 3)
    ops.uniaxialMaterial('LimitState', 31019, 26.47161334, 8.869e-05, 79.41484001, 0.00026608, 264.71613336, 0.00088693, -26.47161334, -8.869e-05, -79.41484001, -0.00026608, -264.71613336, -0.00088693, 0.4, 0.3, 0.003, 0.0, 0.0, 11019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1019, 99999, 'P', 41019, 'Vy', 31019, 'Vz', 21019, 'My', 11019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171019, 71019, 171019, 1019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122019, 122019, 22019, 1019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171020, 5.3, 12.75, 3.175)
    ops.node(122020, 5.3, 12.75, 5.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1020, 171020, 122020, 0.1925, 30761984.08654795, 12817493.36939498, 0.00475217, 0.00533786, 0.00216161, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21020, 69.07864132, 0.00057972, 83.55683911, 0.03094439, 8.35568391, 0.07883179, -69.07864132, -0.00057972, -83.55683911, -0.03094439, -8.35568391, -0.07883179, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11020, 134.85684413, 0.00047433, 163.12150055, 0.03576688, 16.31215005, 0.10418219, -134.85684413, -0.00047433, -163.12150055, -0.03576688, -16.31215005, -0.10418219, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21020, 1020, 0.0, 175.92448277, 0.01159435, 175.92448277, 0.03478304, 123.14713794, -1657.84954872, 0.05, 2, 0, 71020, 22020, 2, 3)
    ops.uniaxialMaterial('LimitState', 41020, 43.98112069, 6.203e-05, 131.94336208, 0.00018609, 439.81120692, 0.00062031, -43.98112069, -6.203e-05, -131.94336208, -0.00018609, -439.81120692, -0.00062031, 0.4, 0.3, 0.003, 0.0, 0.0, 21020, 2)
    ops.limitCurve('ThreePoint', 11020, 1020, 0.0, 231.69667073, 0.00948651, 231.69667073, 0.02845954, 162.18766951, -2897.45623981, 0.05, 2, 0, 71020, 22020, 1, 3)
    ops.uniaxialMaterial('LimitState', 31020, 57.92416768, 8.17e-05, 173.77250305, 0.00024509, 579.24167682, 0.00081697, -57.92416768, -8.17e-05, -173.77250305, -0.00024509, -579.24167682, -0.00081697, 0.4, 0.3, 0.003, 0.0, 0.0, 11020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1020, 99999, 'P', 41020, 'Vy', 31020, 'Vz', 21020, 'My', 11020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171020, 71020, 171020, 1020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122020, 122020, 22020, 1020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171021, 10.6, 12.75, 3.175)
    ops.node(122021, 10.6, 12.75, 5.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1021, 171021, 122021, 0.135, 27602684.34676113, 11501118.47781714, 0.002377, 0.00250594, 0.00111375, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21021, 63.97603119, 0.00070628, 77.87907316, 0.04637861, 7.78790732, 0.11892642, -63.97603119, -0.00070628, -77.87907316, -0.04637861, -7.78790732, -0.11892642, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11021, 80.41233882, 0.00055092, 97.88726029, 0.05360839, 9.78872603, 0.15360839, -80.41233882, -0.00055092, -97.88726029, -0.05360839, -9.78872603, -0.15360839, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21021, 1021, 0.0, 144.76543619, 0.01412561, 144.76543619, 0.04237682, 101.33580533, -2567.06246511, 0.05, 2, 0, 71021, 22021, 2, 3)
    ops.uniaxialMaterial('LimitState', 41021, 36.19135905, 8.112e-05, 108.57407714, 0.00024335, 361.91359046, 0.00081117, -36.19135905, -8.112e-05, -108.57407714, -0.00024335, -361.91359046, -0.00081117, 0.4, 0.3, 0.003, 0.0, 0.0, 21021, 2)
    ops.limitCurve('ThreePoint', 11021, 1021, 0.0, 178.89932541, 0.0110183, 178.89932541, 0.03305491, 125.22952778, -4647.03257979, 0.05, 2, 0, 71021, 22021, 1, 3)
    ops.uniaxialMaterial('LimitState', 31021, 44.72483135, 0.00010024, 134.17449405, 0.00030073, 447.24831352, 0.00100243, -44.72483135, -0.00010024, -134.17449405, -0.00030073, -447.24831352, -0.00100243, 0.4, 0.3, 0.003, 0.0, 0.0, 11021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1021, 99999, 'P', 41021, 'Vy', 31021, 'Vz', 21021, 'My', 11021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171021, 71021, 171021, 1021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122021, 122021, 22021, 1021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171022, 13.45, 12.75, 3.175)
    ops.node(122022, 13.45, 12.75, 5.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1022, 171022, 122022, 0.135, 29706044.79564267, 12377518.66485111, 0.002377, 0.00250594, 0.00111375, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21022, 63.13985926, 0.00067861, 76.54045517, 0.04756069, 7.65404552, 0.12317896, -63.13985926, -0.00067861, -76.54045517, -0.04756069, -7.65404552, -0.12317896, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11022, 79.62289865, 0.00053326, 96.52180058, 0.05499611, 9.65218006, 0.15499611, -79.62289865, -0.00053326, -96.52180058, -0.05499611, -9.65218006, -0.15499611, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21022, 1022, 0.0, 158.09921308, 0.01357225, 158.09921308, 0.04071676, 110.66944916, -2837.06142397, 0.05, 2, 0, 71022, 22022, 2, 3)
    ops.uniaxialMaterial('LimitState', 41022, 39.52480327, 8.232e-05, 118.57440981, 0.00024695, 395.2480327, 0.00082315, -39.52480327, -8.232e-05, -118.57440981, -0.00024695, -395.2480327, -0.00082315, 0.4, 0.3, 0.003, 0.0, 0.0, 21022, 2)
    ops.limitCurve('ThreePoint', 11022, 1022, 0.0, 194.7662724, 0.01066527, 194.7662724, 0.0319958, 136.33639068, -5193.50485937, 0.05, 2, 0, 71022, 22022, 1, 3)
    ops.uniaxialMaterial('LimitState', 31022, 48.6915681, 0.00010141, 146.0747043, 0.00030422, 486.91568099, 0.00101406, -48.6915681, -0.00010141, -146.0747043, -0.00030422, -486.91568099, -0.00101406, 0.4, 0.3, 0.003, 0.0, 0.0, 11022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1022, 99999, 'P', 41022, 'Vy', 31022, 'Vz', 21022, 'My', 11022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171022, 71022, 171022, 1022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122022, 122022, 22022, 1022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171023, 18.75, 12.75, 3.175)
    ops.node(122023, 18.75, 12.75, 5.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1023, 171023, 122023, 0.1925, 26935038.34657495, 11222932.64440623, 0.00475217, 0.00533786, 0.00216161, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21023, 69.69909742, 0.00060253, 84.99045458, 0.0326805, 8.49904546, 0.07746739, -69.69909742, -0.00060253, -84.99045458, -0.0326805, -8.49904546, -0.07746739, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11023, 137.55279611, 0.00049029, 167.73064647, 0.0377742, 16.77306465, 0.1017599, -137.55279611, -0.00049029, -167.73064647, -0.0377742, -16.77306465, -0.1017599, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21023, 1023, 0.0, 157.98859266, 0.0120507, 157.98859266, 0.03615209, 110.59201486, -1790.62272129, 0.05, 2, 0, 71023, 22023, 2, 3)
    ops.uniaxialMaterial('LimitState', 41023, 39.49714816, 6.362e-05, 118.49144449, 0.00019087, 394.97148165, 0.00063622, -39.49714816, -6.362e-05, -118.49144449, -0.00019087, -394.97148165, -0.00063622, 0.4, 0.3, 0.003, 0.0, 0.0, 21023, 2)
    ops.limitCurve('ThreePoint', 11023, 1023, 0.0, 211.19185489, 0.0098059, 211.19185489, 0.02941769, 147.83429843, -3174.28800771, 0.05, 2, 0, 71023, 22023, 1, 3)
    ops.uniaxialMaterial('LimitState', 31023, 52.79796372, 8.505e-05, 158.39389117, 0.00025514, 527.97963723, 0.00085047, -52.79796372, -8.505e-05, -158.39389117, -0.00025514, -527.97963723, -0.00085047, 0.4, 0.3, 0.003, 0.0, 0.0, 11023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1023, 99999, 'P', 41023, 'Vy', 31023, 'Vz', 21023, 'My', 11023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171023, 71023, 171023, 1023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122023, 122023, 22023, 1023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171024, 24.05, 12.75, 3.175)
    ops.node(122024, 24.05, 12.75, 5.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1024, 171024, 122024, 0.0875, 27884144.93644137, 11618393.72351724, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21024, 47.82610435, 0.00090595, 58.1342785, 0.03940644, 5.81342785, 0.10169446, -47.82610435, -0.00090595, -58.1342785, -0.03940644, -5.81342785, -0.10169446, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11024, 56.16737814, 0.00068843, 68.27338434, 0.0441364, 6.82733843, 0.12711139, -56.16737814, -0.00068843, -68.27338434, -0.0441364, -6.82733843, -0.12711139, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21024, 1024, 0.0, 90.48495496, 0.01811906, 90.48495496, 0.05435719, 63.33946847, -1337.80917224, 0.05, 2, 0, 71024, 22024, 2, 3)
    ops.uniaxialMaterial('LimitState', 41024, 22.62123874, 7.744e-05, 67.86371622, 0.00023231, 226.2123874, 0.00077436, -22.62123874, -7.744e-05, -67.86371622, -0.00023231, -226.2123874, -0.00077436, 0.4, 0.3, 0.003, 0.0, 0.0, 21024, 2)
    ops.limitCurve('ThreePoint', 11024, 1024, 0.0, 106.03843543, 0.01376853, 106.03843543, 0.04130559, 74.2269048, -2095.47563251, 0.05, 2, 0, 71024, 22024, 1, 3)
    ops.uniaxialMaterial('LimitState', 31024, 26.50960886, 9.075e-05, 79.52882657, 0.00027224, 265.09608857, 0.00090746, -26.50960886, -9.075e-05, -79.52882657, -0.00027224, -265.09608857, -0.00090746, 0.4, 0.3, 0.003, 0.0, 0.0, 11024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1024, 99999, 'P', 41024, 'Vy', 31024, 'Vz', 21024, 'My', 11024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171024, 71024, 171024, 1024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122024, 122024, 22024, 1024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172001, 0.0, 0.0, 6.075)
    ops.node(123001, 0.0, 0.0, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2001, 172001, 123001, 0.0625, 27301843.93728144, 11375768.3072006, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22001, 19.21565824, 0.00081665, 23.40680946, 0.02291644, 2.34068095, 0.07811464, -19.21565824, -0.00081665, -23.40680946, -0.02291644, -2.34068095, -0.07811464, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12001, 19.21565824, 0.00081665, 23.40680946, 0.02291644, 2.34068095, 0.07811464, -19.21565824, -0.00081665, -23.40680946, -0.02291644, -2.34068095, -0.07811464, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22001, 2001, 0.0, 50.90305664, 0.01633297, 50.90305664, 0.04899891, 35.63213965, -675.77750682, 0.05, 2, 0, 72001, 23001, 2, 3)
    ops.uniaxialMaterial('LimitState', 42001, 12.72576416, 6.229e-05, 38.17729248, 0.00018686, 127.25764161, 0.00062288, -12.72576416, -6.229e-05, -38.17729248, -0.00018686, -127.25764161, -0.00062288, 0.4, 0.3, 0.003, 0.0, 0.0, 22001, 2)
    ops.limitCurve('ThreePoint', 12001, 2001, 0.0, 50.90305664, 0.01633297, 50.90305664, 0.04899891, 35.63213965, -675.77750682, 0.05, 2, 0, 72001, 23001, 1, 3)
    ops.uniaxialMaterial('LimitState', 32001, 12.72576416, 6.229e-05, 38.17729248, 0.00018686, 127.25764161, 0.00062288, -12.72576416, -6.229e-05, -38.17729248, -0.00018686, -127.25764161, -0.00062288, 0.4, 0.3, 0.003, 0.0, 0.0, 12001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2001, 99999, 'P', 42001, 'Vy', 32001, 'Vz', 22001, 'My', 12001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172001, 72001, 172001, 2001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123001, 123001, 23001, 2001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172002, 5.3, 0.0, 6.075)
    ops.node(123002, 5.3, 0.0, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2002, 172002, 123002, 0.125, 27340209.43542022, 11391753.93142509, 0.00178813, 0.00286458, 0.00071615, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22002, 37.45926252, 0.00082023, 45.66385556, 0.03528542, 4.56638556, 0.08435846, -37.45926252, -0.00082023, -45.66385556, -0.03528542, -4.56638556, -0.08435846, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12002, 69.69647651, 0.00052544, 84.96189254, 0.04437779, 8.49618925, 0.13127237, -69.69647651, -0.00052544, -84.96189254, -0.04437779, -8.49618925, -0.13127237, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22002, 2002, 0.0, 110.65543541, 0.01640469, 110.65543541, 0.04921407, 77.45880478, -1480.21825749, 0.05, 2, 0, 72002, 23002, 2, 3)
    ops.uniaxialMaterial('LimitState', 42002, 27.66385885, 6.761e-05, 82.99157655, 0.00020282, 276.63858852, 0.00067607, -27.66385885, -6.761e-05, -82.99157655, -0.00020282, -276.63858852, -0.00067607, 0.4, 0.3, 0.003, 0.0, 0.0, 22002, 2)
    ops.limitCurve('ThreePoint', 12002, 2002, 0.0, 160.24481373, 0.01050889, 160.24481373, 0.03152666, 112.17136961, -3974.27825504, 0.05, 2, 0, 72002, 23002, 1, 3)
    ops.uniaxialMaterial('LimitState', 32002, 40.06120343, 9.79e-05, 120.18361029, 0.00029371, 400.61203431, 0.00097904, -40.06120343, -9.79e-05, -120.18361029, -0.00029371, -400.61203431, -0.00097904, 0.4, 0.3, 0.003, 0.0, 0.0, 12002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2002, 99999, 'P', 42002, 'Vy', 32002, 'Vz', 22002, 'My', 12002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172002, 72002, 172002, 2002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123002, 123002, 23002, 2002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172005, 18.75, 0.0, 6.075)
    ops.node(123005, 18.75, 0.0, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2005, 172005, 123005, 0.125, 28891551.43561214, 12038146.43150506, 0.00178813, 0.00286458, 0.00071615, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22005, 36.0135798, 0.00079465, 43.77069517, 0.03121645, 4.37706952, 0.08169305, -36.0135798, -0.00079465, -43.77069517, -0.03121645, -4.37706952, -0.08169305, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12005, 67.65763631, 0.00050915, 82.23069717, 0.03921683, 8.22306972, 0.12859672, -67.65763631, -0.00050915, -82.23069717, -0.03921683, -8.22306972, -0.12859672, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22005, 2005, 0.0, 107.1118058, 0.01589302, 107.1118058, 0.04767906, 74.97826406, -1103.52622608, 0.05, 2, 0, 72005, 23005, 2, 3)
    ops.uniaxialMaterial('LimitState', 42005, 26.77795145, 6.193e-05, 80.33385435, 0.00018578, 267.77951449, 0.00061928, -26.77795145, -6.193e-05, -80.33385435, -0.00018578, -267.77951449, -0.00061928, 0.4, 0.3, 0.003, 0.0, 0.0, 22005, 2)
    ops.limitCurve('ThreePoint', 12005, 2005, 0.0, 148.17739038, 0.01018308, 148.17739038, 0.03054925, 103.72417326, -2759.75791363, 0.05, 2, 0, 72005, 23005, 1, 3)
    ops.uniaxialMaterial('LimitState', 32005, 37.04434759, 8.567e-05, 111.13304278, 0.00025701, 370.44347594, 0.00085671, -37.04434759, -8.567e-05, -111.13304278, -0.00025701, -370.44347594, -0.00085671, 0.4, 0.3, 0.003, 0.0, 0.0, 12005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2005, 99999, 'P', 42005, 'Vy', 32005, 'Vz', 22005, 'My', 12005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172005, 72005, 172005, 2005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123005, 123005, 23005, 2005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172006, 24.05, 0.0, 6.075)
    ops.node(123006, 24.05, 0.0, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2006, 172006, 123006, 0.0625, 27751050.16911313, 11562937.57046381, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22006, 18.93559799, 0.00082108, 23.04859817, 0.02717521, 2.30485982, 0.08294013, -18.93559799, -0.00082108, -23.04859817, -0.02717521, -2.30485982, -0.08294013, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12006, 18.93559799, 0.00082108, 23.04859817, 0.02717521, 2.30485982, 0.08294013, -18.93559799, -0.00082108, -23.04859817, -0.02717521, -2.30485982, -0.08294013, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22006, 2006, 0.0, 60.2580927, 0.01642167, 60.2580927, 0.04926501, 42.18066489, -864.35191276, 0.05, 2, 0, 72006, 23006, 2, 3)
    ops.uniaxialMaterial('LimitState', 42006, 15.06452318, 7.254e-05, 45.19356953, 0.00021762, 150.64523176, 0.00072541, -15.06452318, -7.254e-05, -45.19356953, -0.00021762, -150.64523176, -0.00072541, 0.4, 0.3, 0.003, 0.0, 0.0, 22006, 2)
    ops.limitCurve('ThreePoint', 12006, 2006, 0.0, 60.2580927, 0.01642167, 60.2580927, 0.04926501, 42.18066489, -864.35191276, 0.05, 2, 0, 72006, 23006, 1, 3)
    ops.uniaxialMaterial('LimitState', 32006, 15.06452318, 7.254e-05, 45.19356953, 0.00021762, 150.64523176, 0.00072541, -15.06452318, -7.254e-05, -45.19356953, -0.00021762, -150.64523176, -0.00072541, 0.4, 0.3, 0.003, 0.0, 0.0, 12006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2006, 99999, 'P', 42006, 'Vy', 32006, 'Vz', 22006, 'My', 12006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172006, 72006, 172006, 2006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123006, 123006, 23006, 2006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172007, 0.0, 4.25, 6.05)
    ops.node(123007, 0.0, 4.25, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2007, 172007, 123007, 0.175, 30534227.3739001, 12722594.73912504, 0.00405757, 0.0019651, 0.00401042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22007, 99.88436323, 0.00052017, 121.0542205, 0.05310401, 12.10542205, 0.15310401, -99.88436323, -0.00052017, -121.0542205, -0.05310401, -12.10542205, -0.15310401, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12007, 67.8883601, 0.00062574, 82.27686744, 0.04682898, 8.22768674, 0.12075677, -67.8883601, -0.00062574, -82.27686744, -0.04682898, -8.22768674, -0.12075677, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22007, 2007, 0.0, 231.35085971, 0.01040335, 231.35085971, 0.03121006, 161.9456018, -6243.19058688, 0.05, 2, 0, 72007, 23007, 2, 3)
    ops.uniaxialMaterial('LimitState', 42007, 57.83771493, 9.04e-05, 173.51314479, 0.00027121, 578.37714929, 0.00090402, -57.83771493, -9.04e-05, -173.51314479, -0.00027121, -578.37714929, -0.00090402, 0.4, 0.3, 0.003, 0.0, 0.0, 22007, 2)
    ops.limitCurve('ThreePoint', 12007, 2007, 0.0, 186.37619568, 0.01251485, 186.37619568, 0.03754455, 130.46333697, -3538.89491158, 0.05, 2, 0, 72007, 23007, 1, 3)
    ops.uniaxialMaterial('LimitState', 32007, 46.59404892, 7.283e-05, 139.78214676, 0.00021848, 465.94048919, 0.00072828, -46.59404892, -7.283e-05, -139.78214676, -0.00021848, -465.94048919, -0.00072828, 0.4, 0.3, 0.003, 0.0, 0.0, 12007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2007, 99999, 'P', 42007, 'Vy', 32007, 'Vz', 22007, 'My', 12007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172007, 72007, 172007, 2007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123007, 123007, 23007, 2007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172008, 5.3, 4.25, 6.05)
    ops.node(123008, 5.3, 4.25, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2008, 172008, 123008, 0.21, 27787165.49197738, 11577985.62165724, 0.00545409, 0.00235812, 0.00693, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22008, 169.85017986, 0.00050106, 207.0354014, 0.02427248, 20.70354014, 0.06379182, -169.85017986, -0.00050106, -207.0354014, -0.02427248, -20.70354014, -0.06379182, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12008, 81.4480991, 0.00064595, 99.27949387, 0.02122944, 9.92794939, 0.04931408, -81.4480991, -0.00064595, -99.27949387, -0.02122944, -9.92794939, -0.04931408, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22008, 2008, 0.0, 200.08465997, 0.01002123, 200.08465997, 0.03006369, 140.05926198, -1585.3369267, 0.05, 2, 0, 72008, 23008, 2, 3)
    ops.uniaxialMaterial('LimitState', 42008, 50.02116499, 7.159e-05, 150.06349497, 0.00021478, 500.21164991, 0.00071595, -50.02116499, -7.159e-05, -150.06349497, -0.00021478, -500.21164991, -0.00071595, 0.4, 0.3, 0.003, 0.0, 0.0, 22008, 2)
    ops.limitCurve('ThreePoint', 12008, 2008, 0.0, 142.8306112, 0.01291894, 142.8306112, 0.03875682, 99.98142784, -913.38757553, 0.05, 2, 0, 72008, 23008, 1, 3)
    ops.uniaxialMaterial('LimitState', 32008, 35.7076528, 5.111e-05, 107.1229584, 0.00015332, 357.076528, 0.00051108, -35.7076528, -5.111e-05, -107.1229584, -0.00015332, -357.076528, -0.00051108, 0.4, 0.3, 0.003, 0.0, 0.0, 12008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2008, 99999, 'P', 42008, 'Vy', 32008, 'Vz', 22008, 'My', 12008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172008, 72008, 172008, 2008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123008, 123008, 23008, 2008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172009, 10.6, 4.25, 6.05)
    ops.node(123009, 10.6, 4.25, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2009, 172009, 123009, 0.175, 25392268.25933572, 10580111.77472322, 0.00405757, 0.0019651, 0.00401042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22009, 106.00417751, 0.0005363, 129.6106368, 0.02888476, 12.96106368, 0.0709995, -106.00417751, -0.0005363, -129.6106368, -0.02888476, -12.96106368, -0.0709995, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12009, 65.6410353, 0.00065166, 80.25887833, 0.02617922, 8.02588783, 0.05902319, -65.6410353, -0.00065166, -80.25887833, -0.02617922, -8.02588783, -0.05902319, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22009, 2009, 0.0, 142.46057512, 0.01072593, 142.46057512, 0.03217779, 99.72240259, -1616.60022347, 0.05, 2, 0, 72009, 23009, 2, 3)
    ops.uniaxialMaterial('LimitState', 42009, 35.61514378, 6.694e-05, 106.84543134, 0.00020082, 356.15143781, 0.0006694, -35.61514378, -6.694e-05, -106.84543134, -0.00020082, -356.15143781, -0.0006694, 0.4, 0.3, 0.003, 0.0, 0.0, 22009, 2)
    ops.limitCurve('ThreePoint', 12009, 2009, 0.0, 119.14120358, 0.01303313, 119.14120358, 0.03909939, 83.39884251, -1086.86445621, 0.05, 2, 0, 72009, 23009, 1, 3)
    ops.uniaxialMaterial('LimitState', 32009, 29.78530089, 5.598e-05, 89.35590268, 0.00016795, 297.85300895, 0.00055983, -29.78530089, -5.598e-05, -89.35590268, -0.00016795, -297.85300895, -0.00055983, 0.4, 0.3, 0.003, 0.0, 0.0, 12009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2009, 99999, 'P', 42009, 'Vy', 32009, 'Vz', 22009, 'My', 12009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172009, 72009, 172009, 2009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123009, 123009, 23009, 2009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172010, 13.45, 4.25, 6.05)
    ops.node(123010, 13.45, 4.25, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2010, 172010, 123010, 0.175, 27042734.91592156, 11267806.21496732, 0.00405757, 0.0019651, 0.00401042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22010, 108.77738485, 0.00055842, 132.70239083, 0.02624976, 13.27023908, 0.07003114, -108.77738485, -0.00055842, -132.70239083, -0.02624976, -13.27023908, -0.07003114, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12010, 67.45081901, 0.00068975, 82.28626711, 0.02382459, 8.22862671, 0.05796832, -67.45081901, -0.00068975, -82.28626711, -0.02382459, -8.22862671, -0.05796832, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22010, 2010, 0.0, 144.74374038, 0.01116834, 144.74374038, 0.03350501, 101.32061827, -1368.00282278, 0.05, 2, 0, 72010, 23010, 2, 3)
    ops.uniaxialMaterial('LimitState', 42010, 36.1859351, 6.386e-05, 108.55780529, 0.00019159, 361.85935096, 0.00063862, -36.1859351, -6.386e-05, -108.55780529, -0.00019159, -361.85935096, -0.00063862, 0.4, 0.3, 0.003, 0.0, 0.0, 22010, 2)
    ops.limitCurve('ThreePoint', 12010, 2010, 0.0, 122.54003693, 0.01379493, 122.54003693, 0.04138479, 85.77802585, -943.307766, 0.05, 2, 0, 72010, 23010, 1, 3)
    ops.uniaxialMaterial('LimitState', 32010, 30.63500923, 5.407e-05, 91.9050277, 0.0001622, 306.35009234, 0.00054065, -30.63500923, -5.407e-05, -91.9050277, -0.0001622, -306.35009234, -0.00054065, 0.4, 0.3, 0.003, 0.0, 0.0, 12010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2010, 99999, 'P', 42010, 'Vy', 32010, 'Vz', 22010, 'My', 12010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172010, 72010, 172010, 2010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123010, 123010, 23010, 2010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172011, 18.75, 4.25, 6.05)
    ops.node(123011, 18.75, 4.25, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2011, 172011, 123011, 0.21, 29380084.67565384, 12241701.9481891, 0.00545409, 0.00235812, 0.00693, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22011, 163.89517352, 0.00049637, 199.09668894, 0.02216318, 19.90966889, 0.06261809, -163.89517352, -0.00049637, -199.09668894, -0.02216318, -19.90966889, -0.06261809, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12011, 79.0582332, 0.00064794, 96.03841361, 0.01940907, 9.60384136, 0.04815858, -79.0582332, -0.00064794, -96.03841361, -0.01940907, -9.60384136, -0.04815858, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22011, 2011, 0.0, 207.39045085, 0.00992747, 207.39045085, 0.02978242, 145.17331559, -1383.72018205, 0.05, 2, 0, 72011, 23011, 2, 3)
    ops.uniaxialMaterial('LimitState', 42011, 51.84761271, 7.019e-05, 155.54283813, 0.00021056, 518.47612712, 0.00070185, -51.84761271, -7.019e-05, -155.54283813, -0.00021056, -518.47612712, -0.00070185, 0.4, 0.3, 0.003, 0.0, 0.0, 22011, 2)
    ops.limitCurve('ThreePoint', 12011, 2011, 0.0, 149.28883342, 0.01295889, 149.28883342, 0.03887668, 104.5021834, -823.41416812, 0.05, 2, 0, 72011, 23011, 1, 3)
    ops.uniaxialMaterial('LimitState', 32011, 37.32220836, 5.052e-05, 111.96662507, 0.00015157, 373.22208355, 0.00050523, -37.32220836, -5.052e-05, -111.96662507, -0.00015157, -373.22208355, -0.00050523, 0.4, 0.3, 0.003, 0.0, 0.0, 12011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2011, 99999, 'P', 42011, 'Vy', 32011, 'Vz', 22011, 'My', 12011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172011, 72011, 172011, 2011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123011, 123011, 23011, 2011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172012, 24.05, 4.25, 6.05)
    ops.node(123012, 24.05, 4.25, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2012, 172012, 123012, 0.175, 27212692.94175111, 11338622.05906296, 0.00405757, 0.0019651, 0.00401042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22012, 97.0473442, 0.00052473, 118.52026506, 0.05455815, 11.85202651, 0.15119797, -97.0473442, -0.00052473, -118.52026506, -0.05455815, -11.85202651, -0.15119797, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12012, 65.89336016, 0.00063353, 80.47307813, 0.04811045, 8.04730781, 0.11921413, -65.89336016, -0.00063353, -80.47307813, -0.04811045, -8.04730781, -0.11921413, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22012, 2012, 0.0, 213.88438263, 0.0104947, 213.88438263, 0.0314841, 149.71906784, -6343.62770575, 0.05, 2, 0, 72012, 23012, 2, 3)
    ops.uniaxialMaterial('LimitState', 42012, 53.47109566, 9.378e-05, 160.41328697, 0.00028133, 534.71095658, 0.00093778, -53.47109566, -9.378e-05, -160.41328697, -0.00028133, -534.71095658, -0.00093778, 0.4, 0.3, 0.003, 0.0, 0.0, 22012, 2)
    ops.limitCurve('ThreePoint', 12012, 2012, 0.0, 170.32071798, 0.01267058, 170.32071798, 0.03801174, 119.22450259, -3591.8126267, 0.05, 2, 0, 72012, 23012, 1, 3)
    ops.uniaxialMaterial('LimitState', 32012, 42.5801795, 7.468e-05, 127.74053849, 0.00022403, 425.80179496, 0.00074677, -42.5801795, -7.468e-05, -127.74053849, -0.00022403, -425.80179496, -0.00074677, 0.4, 0.3, 0.003, 0.0, 0.0, 12012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2012, 99999, 'P', 42012, 'Vy', 32012, 'Vz', 22012, 'My', 12012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172012, 72012, 172012, 2012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123012, 123012, 23012, 2012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172013, 0.0, 8.5, 6.05)
    ops.node(123013, 0.0, 8.5, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2013, 172013, 123013, 0.175, 24593834.09550582, 10247430.87312743, 0.00405757, 0.0019651, 0.00401042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22013, 94.65148749, 0.00054293, 116.0391734, 0.05729065, 11.60391734, 0.1493081, -94.65148749, -0.00054293, -116.0391734, -0.05729065, -11.60391734, -0.1493081, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12013, 63.93316716, 0.00066548, 78.37966488, 0.05052734, 7.83796649, 0.11823007, -63.93316716, -0.00066548, -78.37966488, -0.05052734, -7.83796649, -0.11823007, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22013, 2013, 0.0, 207.35154374, 0.01085867, 207.35154374, 0.03257601, 145.14608062, -7014.60134714, 0.05, 2, 0, 72013, 23013, 2, 3)
    ops.uniaxialMaterial('LimitState', 42013, 51.83788594, 0.00010059, 155.51365781, 0.00030178, 518.37885935, 0.00100594, -51.83788594, -0.00010059, -155.51365781, -0.00030178, -518.37885935, -0.00100594, 0.4, 0.3, 0.003, 0.0, 0.0, 22013, 2)
    ops.limitCurve('ThreePoint', 12013, 2013, 0.0, 162.93119104, 0.01330962, 162.93119104, 0.03992886, 114.05183373, -3944.61363188, 0.05, 2, 0, 72013, 23013, 1, 3)
    ops.uniaxialMaterial('LimitState', 32013, 40.73279776, 7.904e-05, 122.19839328, 0.00023713, 407.3279776, 0.00079044, -40.73279776, -7.904e-05, -122.19839328, -0.00023713, -407.3279776, -0.00079044, 0.4, 0.3, 0.003, 0.0, 0.0, 12013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2013, 99999, 'P', 42013, 'Vy', 32013, 'Vz', 22013, 'My', 12013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172013, 72013, 172013, 2013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123013, 123013, 23013, 2013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172014, 5.3, 8.5, 6.05)
    ops.node(123014, 5.3, 8.5, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2014, 172014, 123014, 0.21, 26493722.11040679, 11039050.87933616, 0.00545409, 0.00235812, 0.00693, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22014, 161.73739084, 0.00049887, 197.58474878, 0.02510219, 19.75847488, 0.06369354, -161.73739084, -0.00049887, -197.58474878, -0.02510219, -19.75847488, -0.06369354, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12014, 77.67178749, 0.00065017, 94.88690611, 0.021954, 9.48869061, 0.04937915, -77.67178749, -0.00065017, -94.88690611, -0.021954, -9.48869061, -0.04937915, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22014, 2014, 0.0, 191.909866, 0.00997737, 191.909866, 0.02993212, 134.3369062, -1657.28639505, 0.05, 2, 0, 72014, 23014, 2, 3)
    ops.uniaxialMaterial('LimitState', 42014, 47.9774665, 7.202e-05, 143.9323995, 0.00021607, 479.774665, 0.00072022, -47.9774665, -7.202e-05, -143.9323995, -0.00021607, -479.774665, -0.00072022, 0.4, 0.3, 0.003, 0.0, 0.0, 22014, 2)
    ops.limitCurve('ThreePoint', 12014, 2014, 0.0, 136.3358328, 0.01300332, 136.3358328, 0.03900995, 95.43508296, -945.16320851, 0.05, 2, 0, 72014, 23014, 1, 3)
    ops.uniaxialMaterial('LimitState', 32014, 34.0839582, 5.117e-05, 102.2518746, 0.0001535, 340.839582, 0.00051166, -34.0839582, -5.117e-05, -102.2518746, -0.0001535, -340.839582, -0.00051166, 0.4, 0.3, 0.003, 0.0, 0.0, 12014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2014, 99999, 'P', 42014, 'Vy', 32014, 'Vz', 22014, 'My', 12014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172014, 72014, 172014, 2014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123014, 123014, 23014, 2014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172015, 10.6, 8.5, 6.05)
    ops.node(123015, 10.6, 8.5, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2015, 172015, 123015, 0.1, 25230855.28809975, 10512856.37004156, 0.00127345, 0.00057292, 0.00146667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22015, 55.96225456, 0.000614, 68.21447377, 0.02232649, 6.82144738, 0.0716119, -55.96225456, -0.000614, -68.21447377, -0.02232649, -6.82144738, -0.0716119, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12015, 31.04222764, 0.00085952, 37.83852598, 0.01955534, 3.7838526, 0.05411861, -31.04222764, -0.00085952, -37.83852598, -0.01955534, -3.7838526, -0.05411861, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22015, 2015, 0.0, 86.23571751, 0.01227998, 86.23571751, 0.03683993, 60.36500225, -1122.39976976, 0.05, 2, 0, 72015, 23015, 2, 3)
    ops.uniaxialMaterial('LimitState', 42015, 21.55892938, 7.137e-05, 64.67678813, 0.0002141, 215.58929377, 0.00071365, -21.55892938, -7.137e-05, -64.67678813, -0.0002141, -215.58929377, -0.00071365, 0.4, 0.3, 0.003, 0.0, 0.0, 22015, 2)
    ops.limitCurve('ThreePoint', 12015, 2015, 0.0, 71.86025512, 0.01719049, 71.86025512, 0.05157146, 50.30217859, -699.60823298, 0.05, 2, 0, 72015, 23015, 1, 3)
    ops.uniaxialMaterial('LimitState', 32015, 17.96506378, 5.947e-05, 53.89519134, 0.00017841, 179.65063781, 0.00059469, -17.96506378, -5.947e-05, -53.89519134, -0.00017841, -179.65063781, -0.00059469, 0.4, 0.3, 0.003, 0.0, 0.0, 12015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2015, 99999, 'P', 42015, 'Vy', 32015, 'Vz', 22015, 'My', 12015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172015, 72015, 172015, 2015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123015, 123015, 23015, 2015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172016, 13.45, 8.5, 6.05)
    ops.node(123016, 13.45, 8.5, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2016, 172016, 123016, 0.1, 32076504.83906619, 13365210.34961091, 0.00127345, 0.00057292, 0.00146667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22016, 54.86997217, 0.00057612, 66.04575691, 0.02515687, 6.60457569, 0.08349688, -54.86997217, -0.00057612, -66.04575691, -0.02515687, -6.60457569, -0.08349688, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12016, 30.73808137, 0.00080536, 36.99874029, 0.02197094, 3.69987403, 0.06288409, -30.73808137, -0.00080536, -36.99874029, -0.02197094, -3.69987403, -0.06288409, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22016, 2016, 0.0, 112.48013767, 0.01152232, 112.48013767, 0.03456696, 78.73609637, -1360.63957515, 0.05, 2, 0, 72016, 23016, 2, 3)
    ops.uniaxialMaterial('LimitState', 42016, 28.12003442, 7.322e-05, 84.36010325, 0.00021965, 281.20034417, 0.00073218, -28.12003442, -7.322e-05, -84.36010325, -0.00021965, -281.20034417, -0.00073218, 0.4, 0.3, 0.003, 0.0, 0.0, 22016, 2)
    ops.limitCurve('ThreePoint', 12016, 2016, 0.0, 97.25065788, 0.01610724, 97.25065788, 0.04832173, 68.07546052, -815.9873036, 0.05, 2, 0, 72016, 23016, 1, 3)
    ops.uniaxialMaterial('LimitState', 32016, 24.31266447, 6.33e-05, 72.93799341, 0.00018991, 243.12664471, 0.00063305, -24.31266447, -6.33e-05, -72.93799341, -0.00018991, -243.12664471, -0.00063305, 0.4, 0.3, 0.003, 0.0, 0.0, 12016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2016, 99999, 'P', 42016, 'Vy', 32016, 'Vz', 22016, 'My', 12016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172016, 72016, 172016, 2016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123016, 123016, 23016, 2016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172017, 18.75, 8.5, 6.05)
    ops.node(123017, 18.75, 8.5, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2017, 172017, 123017, 0.21, 30916043.81580766, 12881684.92325319, 0.00545409, 0.00235812, 0.00693, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22017, 165.43724718, 0.0004841, 200.17187927, 0.02089125, 20.01718793, 0.06207685, -165.43724718, -0.0004841, -200.17187927, -0.02089125, -20.01718793, -0.06207685, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12017, 79.81066046, 0.00061967, 96.56743063, 0.01829006, 9.65674306, 0.04755884, -79.81066046, -0.00061967, -96.56743063, -0.01829006, -9.65674306, -0.04755884, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22017, 2017, 0.0, 217.25441405, 0.00968209, 217.25441405, 0.02904628, 152.07808984, -1283.02024432, 0.05, 2, 0, 72017, 23017, 2, 3)
    ops.uniaxialMaterial('LimitState', 42017, 54.31360351, 6.987e-05, 162.94081054, 0.00020961, 543.13603514, 0.00069871, -54.31360351, -6.987e-05, -162.94081054, -0.00020961, -543.13603514, -0.00069871, 0.4, 0.3, 0.003, 0.0, 0.0, 22017, 2)
    ops.limitCurve('ThreePoint', 12017, 2017, 0.0, 157.23381163, 0.0123934, 157.23381163, 0.03718019, 110.06366814, -777.89164473, 0.05, 2, 0, 72017, 23017, 1, 3)
    ops.uniaxialMaterial('LimitState', 32017, 39.30845291, 5.057e-05, 117.92535873, 0.0001517, 393.08452909, 0.00050568, -39.30845291, -5.057e-05, -117.92535873, -0.0001517, -393.08452909, -0.00050568, 0.4, 0.3, 0.003, 0.0, 0.0, 12017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2017, 99999, 'P', 42017, 'Vy', 32017, 'Vz', 22017, 'My', 12017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172017, 72017, 172017, 2017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123017, 123017, 23017, 2017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172018, 24.05, 8.5, 6.05)
    ops.node(123018, 24.05, 8.5, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2018, 172018, 123018, 0.175, 29033909.31000108, 12097462.21250045, 0.00405757, 0.0019651, 0.00401042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22018, 94.0550815, 0.00050383, 114.42775695, 0.0533542, 11.4427757, 0.15231461, -94.0550815, -0.00050383, -114.42775695, -0.0533542, -11.4427757, -0.15231461, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12018, 63.85725343, 0.00060394, 77.68896862, 0.04704136, 7.76889686, 0.11985245, -63.85725343, -0.00060394, -77.68896862, -0.04704136, -7.76889686, -0.11985245, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22018, 2018, 0.0, 205.64082312, 0.0100766, 205.64082312, 0.0302298, 143.94857618, -4778.22197219, 0.05, 2, 0, 72018, 23018, 2, 3)
    ops.uniaxialMaterial('LimitState', 42018, 51.41020578, 8.451e-05, 154.23061734, 0.00025352, 514.1020578, 0.00084508, -51.41020578, -8.451e-05, -154.23061734, -0.00025352, -514.1020578, -0.00084508, 0.4, 0.3, 0.003, 0.0, 0.0, 22018, 2)
    ops.limitCurve('ThreePoint', 12018, 2018, 0.0, 166.61458078, 0.01207879, 166.61458078, 0.03623636, 116.63020655, -2763.20394263, 0.05, 2, 0, 72018, 23018, 1, 3)
    ops.uniaxialMaterial('LimitState', 32018, 41.6536452, 6.847e-05, 124.96093559, 0.00020541, 416.53645196, 0.0006847, -41.6536452, -6.847e-05, -124.96093559, -0.00020541, -416.53645196, -0.0006847, 0.4, 0.3, 0.003, 0.0, 0.0, 12018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2018, 99999, 'P', 42018, 'Vy', 32018, 'Vz', 22018, 'My', 12018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172018, 72018, 172018, 2018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123018, 123018, 23018, 2018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172019, 0.0, 12.75, 6.075)
    ops.node(123019, 0.0, 12.75, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2019, 172019, 123019, 0.0625, 28033352.68480995, 11680563.61867081, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22019, 19.57145674, 0.00077698, 23.81070039, 0.02508551, 2.38107004, 0.08118948, -19.57145674, -0.00077698, -23.81070039, -0.02508551, -2.38107004, -0.08118948, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12019, 19.57145674, 0.00077698, 23.81070039, 0.02508551, 2.38107004, 0.08118948, -19.57145674, -0.00077698, -23.81070039, -0.02508551, -2.38107004, -0.08118948, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22019, 2019, 0.0, 59.03659618, 0.01553964, 59.03659618, 0.04661893, 41.32561732, -788.58888862, 0.05, 2, 0, 72019, 23019, 2, 3)
    ops.uniaxialMaterial('LimitState', 42019, 14.75914904, 7.036e-05, 44.27744713, 0.00021107, 147.59149044, 0.00070355, -14.75914904, -7.036e-05, -44.27744713, -0.00021107, -147.59149044, -0.00070355, 0.4, 0.3, 0.003, 0.0, 0.0, 22019, 2)
    ops.limitCurve('ThreePoint', 12019, 2019, 0.0, 59.03659618, 0.01553964, 59.03659618, 0.04661893, 41.32561732, -788.58888862, 0.05, 2, 0, 72019, 23019, 1, 3)
    ops.uniaxialMaterial('LimitState', 32019, 14.75914904, 7.036e-05, 44.27744713, 0.00021107, 147.59149044, 0.00070355, -14.75914904, -7.036e-05, -44.27744713, -0.00021107, -147.59149044, -0.00070355, 0.4, 0.3, 0.003, 0.0, 0.0, 12019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2019, 99999, 'P', 42019, 'Vy', 32019, 'Vz', 22019, 'My', 12019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172019, 72019, 172019, 2019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123019, 123019, 23019, 2019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172020, 5.3, 12.75, 6.075)
    ops.node(123020, 5.3, 12.75, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2020, 172020, 123020, 0.125, 28825276.99785455, 12010532.0824394, 0.00178813, 0.00286458, 0.00071615, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22020, 38.26862453, 0.00082174, 46.51808652, 0.03171314, 4.65180865, 0.08213562, -38.26862453, -0.00082174, -46.51808652, -0.03171314, -4.65180865, -0.08213562, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12020, 71.14926909, 0.00052718, 86.48672107, 0.03983237, 8.64867211, 0.12911641, -71.14926909, -0.00052718, -86.48672107, -0.03983237, -8.64867211, -0.12911641, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22020, 2020, 0.0, 108.06800297, 0.01643479, 108.06800297, 0.04930438, 75.64760208, -1149.94602072, 0.05, 2, 0, 72020, 23020, 2, 3)
    ops.uniaxialMaterial('LimitState', 42020, 27.01700074, 6.262e-05, 81.05100223, 0.00018787, 270.17000742, 0.00062624, -27.01700074, -6.262e-05, -81.05100223, -0.00018787, -270.17000742, -0.00062624, 0.4, 0.3, 0.003, 0.0, 0.0, 22020, 2)
    ops.limitCurve('ThreePoint', 12020, 2020, 0.0, 150.30604146, 0.01054369, 150.30604146, 0.03163107, 105.21422902, -2906.97556588, 0.05, 2, 0, 72020, 23020, 1, 3)
    ops.uniaxialMaterial('LimitState', 32020, 37.57651037, 8.71e-05, 112.7295311, 0.0002613, 375.76510365, 0.00087101, -37.57651037, -8.71e-05, -112.7295311, -0.0002613, -375.76510365, -0.00087101, 0.4, 0.3, 0.003, 0.0, 0.0, 12020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2020, 99999, 'P', 42020, 'Vy', 32020, 'Vz', 22020, 'My', 12020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172020, 72020, 172020, 2020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123020, 123020, 23020, 2020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172021, 10.6, 12.75, 6.075)
    ops.node(123021, 10.6, 12.75, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2021, 172021, 123021, 0.0875, 26061990.11829871, 10859162.54929113, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22021, 28.1622033, 0.00082513, 34.37115395, 0.02950609, 3.4371154, 0.07872713, -28.1622033, -0.00082513, -34.37115395, -0.02950609, -3.4371154, -0.07872713, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12021, 37.56266798, 0.0006401, 45.844149, 0.03280433, 4.5844149, 0.09740428, -37.56266798, -0.0006401, -45.844149, -0.03280433, -4.5844149, -0.09740428, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22021, 2021, 0.0, 74.43408443, 0.01650261, 74.43408443, 0.04950784, 52.1038591, -981.03417518, 0.05, 2, 0, 72021, 23021, 2, 3)
    ops.uniaxialMaterial('LimitState', 42021, 18.60852111, 6.815e-05, 55.82556332, 0.00020446, 186.08521107, 0.00068153, -18.60852111, -6.815e-05, -55.82556332, -0.00020446, -186.08521107, -0.00068153, 0.4, 0.3, 0.003, 0.0, 0.0, 22021, 2)
    ops.limitCurve('ThreePoint', 12021, 2021, 0.0, 86.07002668, 0.01280207, 86.07002668, 0.0384062, 60.24901868, -1517.2383762, 0.05, 2, 0, 72021, 23021, 1, 3)
    ops.uniaxialMaterial('LimitState', 32021, 21.51750667, 7.881e-05, 64.55252001, 0.00023642, 215.1750667, 0.00078807, -21.51750667, -7.881e-05, -64.55252001, -0.00023642, -215.1750667, -0.00078807, 0.4, 0.3, 0.003, 0.0, 0.0, 12021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2021, 99999, 'P', 42021, 'Vy', 32021, 'Vz', 22021, 'My', 12021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172021, 72021, 172021, 2021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123021, 123021, 23021, 2021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172022, 13.45, 12.75, 6.075)
    ops.node(123022, 13.45, 12.75, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2022, 172022, 123022, 0.0875, 26715323.71560545, 11131384.88150227, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22022, 27.70422566, 0.00082138, 33.78355642, 0.02812659, 3.37835564, 0.07820545, -27.70422566, -0.00082138, -33.78355642, -0.02812659, -3.37835564, -0.07820545, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12022, 37.11253415, 0.00063502, 45.25639542, 0.03125642, 4.52563954, 0.09698222, -37.11253415, -0.00063502, -45.25639542, -0.03125642, -4.52563954, -0.09698222, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22022, 2022, 0.0, 75.88896642, 0.01642754, 75.88896642, 0.04928262, 53.1222765, -975.91610514, 0.05, 2, 0, 72022, 23022, 2, 3)
    ops.uniaxialMaterial('LimitState', 42022, 18.97224161, 6.779e-05, 56.91672482, 0.00020336, 189.72241606, 0.00067786, -18.97224161, -6.779e-05, -56.91672482, -0.00020336, -189.72241606, -0.00067786, 0.4, 0.3, 0.003, 0.0, 0.0, 22022, 2)
    ops.limitCurve('ThreePoint', 12022, 2022, 0.0, 87.47500612, 0.01270048, 87.47500612, 0.03810144, 61.23250428, -1508.32899216, 0.05, 2, 0, 72022, 23022, 1, 3)
    ops.uniaxialMaterial('LimitState', 32022, 21.86875153, 7.814e-05, 65.60625459, 0.00023441, 218.68751529, 0.00078135, -21.86875153, -7.814e-05, -65.60625459, -0.00023441, -218.68751529, -0.00078135, 0.4, 0.3, 0.003, 0.0, 0.0, 12022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2022, 99999, 'P', 42022, 'Vy', 32022, 'Vz', 22022, 'My', 12022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172022, 72022, 172022, 2022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123022, 123022, 23022, 2022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172023, 18.75, 12.75, 6.075)
    ops.node(123023, 18.75, 12.75, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2023, 172023, 123023, 0.125, 27702802.19409181, 11542834.24753826, 0.00178813, 0.00286458, 0.00071615, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22023, 37.19072974, 0.00072569, 45.30787205, 0.03560717, 4.5307872, 0.08503533, -37.19072974, -0.00072569, -45.30787205, -0.03560717, -4.5307872, -0.08503533, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12023, 67.40179543, 0.00049112, 82.11271854, 0.04487313, 8.21127185, 0.13239654, -67.40179543, -0.00049112, -82.11271854, -0.04487313, -8.21127185, -0.13239654, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22023, 2023, 0.0, 114.5130989, 0.01451385, 114.5130989, 0.04354155, 80.15916923, -1596.92157416, 0.05, 2, 0, 72023, 23023, 2, 3)
    ops.uniaxialMaterial('LimitState', 42023, 28.62827473, 6.905e-05, 85.88482418, 0.00020714, 286.28274725, 0.00069048, -28.62827473, -6.905e-05, -85.88482418, -0.00020714, -286.28274725, -0.00069048, 0.4, 0.3, 0.003, 0.0, 0.0, 22023, 2)
    ops.limitCurve('ThreePoint', 12023, 2023, 0.0, 166.81150642, 0.00982238, 166.81150642, 0.02946715, 116.7680545, -4358.33274219, 0.05, 2, 0, 72023, 23023, 1, 3)
    ops.uniaxialMaterial('LimitState', 32023, 41.70287661, 0.00010058, 125.10862982, 0.00030175, 417.02876606, 0.00100583, -41.70287661, -0.00010058, -125.10862982, -0.00030175, -417.02876606, -0.00100583, 0.4, 0.3, 0.003, 0.0, 0.0, 12023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2023, 99999, 'P', 42023, 'Vy', 32023, 'Vz', 22023, 'My', 12023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172023, 72023, 172023, 2023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123023, 123023, 23023, 2023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172024, 24.05, 12.75, 6.075)
    ops.node(123024, 24.05, 12.75, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2024, 172024, 123024, 0.0625, 27000677.76734246, 11250282.40305936, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22024, 19.33178338, 0.00079836, 23.55908146, 0.02676821, 2.35590815, 0.08156673, -19.33178338, -0.00079836, -23.55908146, -0.02676821, -2.35590815, -0.08156673, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12024, 19.33178338, 0.00079836, 23.55908146, 0.02676821, 2.35590815, 0.08156673, -19.33178338, -0.00079836, -23.55908146, -0.02676821, -2.35590815, -0.08156673, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22024, 2024, 0.0, 59.52880173, 0.01596721, 59.52880173, 0.04790163, 41.67016121, -891.37924909, 0.05, 2, 0, 72024, 23024, 2, 3)
    ops.uniaxialMaterial('LimitState', 42024, 14.88220043, 7.366e-05, 44.6466013, 0.00022097, 148.82200432, 0.00073655, -14.88220043, -7.366e-05, -44.6466013, -0.00022097, -148.82200432, -0.00073655, 0.4, 0.3, 0.003, 0.0, 0.0, 22024, 2)
    ops.limitCurve('ThreePoint', 12024, 2024, 0.0, 59.52880173, 0.01596721, 59.52880173, 0.04790163, 41.67016121, -891.37924909, 0.05, 2, 0, 72024, 23024, 1, 3)
    ops.uniaxialMaterial('LimitState', 32024, 14.88220043, 7.366e-05, 44.6466013, 0.00022097, 148.82200432, 0.00073655, -14.88220043, -7.366e-05, -44.6466013, -0.00022097, -148.82200432, -0.00073655, 0.4, 0.3, 0.003, 0.0, 0.0, 12024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2024, 99999, 'P', 42024, 'Vy', 32024, 'Vz', 22024, 'My', 12024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172024, 72024, 172024, 2024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123024, 123024, 23024, 2024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173001, 0.0, 0.0, 8.975)
    ops.node(124001, 0.0, 0.0, 11.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3001, 173001, 124001, 0.0625, 24943545.87512372, 10393144.11463489, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23001, 14.64171201, 0.00074528, 18.00084833, 0.02796598, 1.80008483, 0.09053812, -14.64171201, -0.00074528, -18.00084833, -0.02796598, -1.80008483, -0.09053812, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13001, 14.64171201, 0.00074528, 18.00084833, 0.02796598, 1.80008483, 0.09053812, -14.64171201, -0.00074528, -18.00084833, -0.02796598, -1.80008483, -0.09053812, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23001, 3001, 0.0, 49.20372838, 0.01490552, 49.20372838, 0.04471657, 34.44260987, -1595.11798685, 0.05, 2, 0, 73001, 24001, 2, 3)
    ops.uniaxialMaterial('LimitState', 43001, 12.3009321, 6.59e-05, 36.90279629, 0.0001977, 123.00932095, 0.00065901, -12.3009321, -6.59e-05, -36.90279629, -0.0001977, -123.00932095, -0.00065901, 0.4, 0.3, 0.003, 0.0, 0.0, 23001, 2)
    ops.limitCurve('ThreePoint', 13001, 3001, 0.0, 49.20372838, 0.01490552, 49.20372838, 0.04471657, 34.44260987, -1595.11798685, 0.05, 2, 0, 73001, 24001, 1, 3)
    ops.uniaxialMaterial('LimitState', 33001, 12.3009321, 6.59e-05, 36.90279629, 0.0001977, 123.00932095, 0.00065901, -12.3009321, -6.59e-05, -36.90279629, -0.0001977, -123.00932095, -0.00065901, 0.4, 0.3, 0.003, 0.0, 0.0, 13001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3001, 99999, 'P', 43001, 'Vy', 33001, 'Vz', 23001, 'My', 13001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173001, 73001, 173001, 3001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124001, 124001, 24001, 3001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173002, 5.3, 0.0, 8.975)
    ops.node(124002, 5.3, 0.0, 11.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3002, 173002, 124002, 0.125, 31353794.47060417, 13064081.02941841, 0.00178813, 0.00286458, 0.00071615, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23002, 24.67095137, 0.00071543, 29.87524313, 0.0207566, 2.98752431, 0.05986768, -24.67095137, -0.00071543, -29.87524313, -0.0207566, -2.98752431, -0.05986768, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13002, 62.1285942, 0.00047991, 75.23450674, 0.02529803, 7.52345067, 0.09024203, -62.1285942, -0.00047991, -75.23450674, -0.02529803, -7.52345067, -0.09024203, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23002, 3002, 0.0, 97.46973081, 0.0143087, 97.46973081, 0.04292609, 68.22881156, -1018.77197311, 0.05, 2, 0, 73002, 24002, 2, 3)
    ops.uniaxialMaterial('LimitState', 43002, 24.3674327, 5.193e-05, 73.10229811, 0.00015578, 243.67432702, 0.00051928, -24.3674327, -5.193e-05, -73.10229811, -0.00015578, -243.67432702, -0.00051928, 0.4, 0.3, 0.003, 0.0, 0.0, 23002, 2)
    ops.limitCurve('ThreePoint', 13002, 3002, 0.0, 127.86367111, 0.00959817, 127.86367111, 0.02879451, 89.50456978, -3181.87170244, 0.05, 2, 0, 73002, 24002, 1, 3)
    ops.uniaxialMaterial('LimitState', 33002, 31.96591778, 6.812e-05, 95.89775333, 0.00020436, 319.65917777, 0.0006812, -31.96591778, -6.812e-05, -95.89775333, -0.00020436, -319.65917777, -0.0006812, 0.4, 0.3, 0.003, 0.0, 0.0, 13002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3002, 99999, 'P', 43002, 'Vy', 33002, 'Vz', 23002, 'My', 13002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173002, 73002, 173002, 3002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124002, 124002, 24002, 3002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173005, 18.75, 0.0, 8.975)
    ops.node(124005, 18.75, 0.0, 11.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3005, 173005, 124005, 0.125, 27359386.6769002, 11399744.44870842, 0.00178813, 0.00286458, 0.00071615, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23005, 24.9486587, 0.00073511, 30.53441852, 0.01979236, 3.05344185, 0.05822713, -24.9486587, -0.00073511, -30.53441852, -0.01979236, -3.05344185, -0.05822713, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13005, 63.26561042, 0.0004923, 77.43015966, 0.02409198, 7.74301597, 0.08791297, -63.26561042, -0.0004923, -77.43015966, -0.02409198, -7.74301597, -0.08791297, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23005, 3005, 0.0, 75.56140593, 0.0147023, 75.56140593, 0.0441069, 52.89298415, -847.79366734, 0.05, 2, 0, 73005, 24005, 2, 3)
    ops.uniaxialMaterial('LimitState', 43005, 18.89035148, 4.613e-05, 56.67105445, 0.0001384, 188.90351483, 0.00046133, -18.89035148, -4.613e-05, -56.67105445, -0.0001384, -188.90351483, -0.00046133, 0.4, 0.3, 0.003, 0.0, 0.0, 23005, 2)
    ops.limitCurve('ThreePoint', 13005, 3005, 0.0, 106.6634139, 0.00984603, 106.6634139, 0.02953809, 74.66438973, -2581.19476407, 0.05, 2, 0, 73005, 24005, 1, 3)
    ops.uniaxialMaterial('LimitState', 33005, 26.66585347, 6.512e-05, 79.99756042, 0.00019537, 266.65853474, 0.00065122, -26.66585347, -6.512e-05, -79.99756042, -0.00019537, -266.65853474, -0.00065122, 0.4, 0.3, 0.003, 0.0, 0.0, 13005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3005, 99999, 'P', 43005, 'Vy', 33005, 'Vz', 23005, 'My', 13005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173005, 73005, 173005, 3005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124005, 124005, 24005, 3005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173006, 24.05, 0.0, 8.975)
    ops.node(124006, 24.05, 0.0, 11.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3006, 173006, 124006, 0.0625, 27619262.23555664, 11508025.93148193, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23006, 14.06909819, 0.00075392, 17.20810235, 0.02430644, 1.72081023, 0.0881076, -14.06909819, -0.00075392, -17.20810235, -0.02430644, -1.72081023, -0.0881076, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13006, 14.06909819, 0.00075392, 17.20810235, 0.02430644, 1.72081023, 0.0881076, -14.06909819, -0.00075392, -17.20810235, -0.02430644, -1.72081023, -0.0881076, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23006, 3006, 0.0, 45.56566337, 0.01507848, 45.56566337, 0.04523544, 31.89596436, -1233.3394704, 0.05, 2, 0, 73006, 24006, 2, 3)
    ops.uniaxialMaterial('LimitState', 43006, 11.39141584, 5.512e-05, 34.17424753, 0.00016535, 113.91415842, 0.00055116, -11.39141584, -5.512e-05, -34.17424753, -0.00016535, -113.91415842, -0.00055116, 0.4, 0.3, 0.003, 0.0, 0.0, 23006, 2)
    ops.limitCurve('ThreePoint', 13006, 3006, 0.0, 45.56566337, 0.01507848, 45.56566337, 0.04523544, 31.89596436, -1233.3394704, 0.05, 2, 0, 73006, 24006, 1, 3)
    ops.uniaxialMaterial('LimitState', 33006, 11.39141584, 5.512e-05, 34.17424753, 0.00016535, 113.91415842, 0.00055116, -11.39141584, -5.512e-05, -34.17424753, -0.00016535, -113.91415842, -0.00055116, 0.4, 0.3, 0.003, 0.0, 0.0, 13006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3006, 99999, 'P', 43006, 'Vy', 33006, 'Vz', 23006, 'My', 13006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173006, 73006, 173006, 3006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124006, 124006, 24006, 3006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173007, 0.0, 4.25, 8.95)
    ops.node(124007, 0.0, 4.25, 11.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3007, 173007, 124007, 0.175, 26854748.06555718, 11189478.36064883, 0.00405757, 0.0019651, 0.00401042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23007, 79.52544429, 0.00051027, 97.47627068, 0.04646327, 9.74762707, 0.12072653, -79.52544429, -0.00051027, -97.47627068, -0.04646327, -9.74762707, -0.12072653, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13007, 47.42014601, 0.00062104, 58.12402596, 0.04137831, 5.8124026, 0.09724681, -47.42014601, -0.00062104, -58.12402596, -0.04137831, -5.8124026, -0.09724681, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23007, 3007, 0.0, 176.878017, 0.01020543, 176.878017, 0.0306163, 123.8146119, -10030.02902926, 0.05, 2, 0, 73007, 24007, 2, 3)
    ops.uniaxialMaterial('LimitState', 43007, 44.21950425, 7.859e-05, 132.65851275, 0.00023576, 442.1950425, 0.00078586, -44.21950425, -7.859e-05, -132.65851275, -0.00023576, -442.1950425, -0.00078586, 0.4, 0.3, 0.003, 0.0, 0.0, 23007, 2)
    ops.limitCurve('ThreePoint', 13007, 3007, 0.0, 142.20434306, 0.01242088, 142.20434306, 0.03726264, 99.54304014, -5240.09868138, 0.05, 2, 0, 73007, 24007, 1, 3)
    ops.uniaxialMaterial('LimitState', 33007, 35.55108577, 6.318e-05, 106.6532573, 0.00018954, 355.51085765, 0.00063181, -35.55108577, -6.318e-05, -106.6532573, -0.00018954, -355.51085765, -0.00063181, 0.4, 0.3, 0.003, 0.0, 0.0, 13007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3007, 99999, 'P', 43007, 'Vy', 33007, 'Vz', 23007, 'My', 13007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173007, 73007, 173007, 3007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124007, 124007, 24007, 3007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173008, 5.3, 4.25, 8.95)
    ops.node(124008, 5.3, 4.25, 11.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3008, 173008, 124008, 0.21, 26556215.30374904, 11065089.70989543, 0.00545409, 0.00235812, 0.00693, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23008, 128.87593027, 0.0004823, 157.99170022, 0.02633527, 15.79917002, 0.0693456, -128.87593027, -0.0004823, -157.99170022, -0.02633527, -15.79917002, -0.0693456, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13008, 59.91893404, 0.00062693, 73.4558753, 0.02301283, 7.34558753, 0.05357835, -59.91893404, -0.00062693, -73.4558753, -0.02301283, -7.34558753, -0.05357835, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23008, 3008, 0.0, 177.30447981, 0.00964601, 177.30447981, 0.02893803, 124.11313587, -2551.73362129, 0.05, 2, 0, 73008, 24008, 2, 3)
    ops.uniaxialMaterial('LimitState', 43008, 44.32611995, 6.638e-05, 132.97835986, 0.00019915, 443.26119953, 0.00066384, -44.32611995, -6.638e-05, -132.97835986, -0.00019915, -443.26119953, -0.00066384, 0.4, 0.3, 0.003, 0.0, 0.0, 23008, 2)
    ops.limitCurve('ThreePoint', 13008, 3008, 0.0, 125.44155741, 0.01253857, 125.44155741, 0.0376157, 87.80909019, -1122.25871524, 0.05, 2, 0, 73008, 24008, 1, 3)
    ops.uniaxialMaterial('LimitState', 33008, 31.36038935, 4.697e-05, 94.08116806, 0.0001409, 313.60389353, 0.00046966, -31.36038935, -4.697e-05, -94.08116806, -0.0001409, -313.60389353, -0.00046966, 0.4, 0.3, 0.003, 0.0, 0.0, 13008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3008, 99999, 'P', 43008, 'Vy', 33008, 'Vz', 23008, 'My', 13008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173008, 73008, 173008, 3008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124008, 124008, 24008, 3008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173009, 10.6, 4.25, 8.95)
    ops.node(124009, 10.6, 4.25, 11.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3009, 173009, 124009, 0.175, 27130694.05868257, 11304455.8577844, 0.00405757, 0.0019651, 0.00401042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23009, 86.02097218, 0.00051681, 105.29495513, 0.0265992, 10.52949551, 0.06933867, -86.02097218, -0.00051681, -105.29495513, -0.0265992, -10.52949551, -0.06933867, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13009, 52.08656886, 0.00062426, 63.75716052, 0.02425793, 6.37571605, 0.05808505, -52.08656886, -0.00062426, -63.75716052, -0.02425793, -6.37571605, -0.05808505, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23009, 3009, 0.0, 138.03728089, 0.01033612, 138.03728089, 0.03100836, 96.62609663, -2209.27642519, 0.05, 2, 0, 73009, 24009, 2, 3)
    ops.uniaxialMaterial('LimitState', 43009, 34.50932022, 6.071e-05, 103.52796067, 0.00018212, 345.09320223, 0.00060705, -34.50932022, -6.071e-05, -103.52796067, -0.00018212, -345.09320223, -0.00060705, 0.4, 0.3, 0.003, 0.0, 0.0, 23009, 2)
    ops.limitCurve('ThreePoint', 13009, 3009, 0.0, 115.81375707, 0.01248521, 115.81375707, 0.03745564, 81.06962995, -1282.16824885, 0.05, 2, 0, 73009, 24009, 1, 3)
    ops.uniaxialMaterial('LimitState', 33009, 28.95343927, 5.093e-05, 86.8603178, 0.0001528, 289.53439268, 0.00050932, -28.95343927, -5.093e-05, -86.8603178, -0.0001528, -289.53439268, -0.00050932, 0.4, 0.3, 0.003, 0.0, 0.0, 13009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3009, 99999, 'P', 43009, 'Vy', 33009, 'Vz', 23009, 'My', 13009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173009, 73009, 173009, 3009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124009, 124009, 24009, 3009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173010, 13.45, 4.25, 8.95)
    ops.node(124010, 13.45, 4.25, 11.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3010, 173010, 124010, 0.175, 29243043.96823517, 12184601.65343132, 0.00405757, 0.0019651, 0.00401042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23010, 83.98171819, 0.00049458, 102.29191092, 0.02490414, 10.22919109, 0.06821114, -83.98171819, -0.00049458, -102.29191092, -0.02490414, -10.22919109, -0.06821114, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13010, 50.97152078, 0.00059065, 62.08463432, 0.02270854, 6.20846343, 0.05698485, -50.97152078, -0.00059065, -62.08463432, -0.02270854, -6.20846343, -0.05698485, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23010, 3010, 0.0, 143.46797508, 0.00989154, 143.46797508, 0.02967461, 100.42758256, -1757.81522039, 0.05, 2, 0, 73010, 24010, 2, 3)
    ops.uniaxialMaterial('LimitState', 43010, 35.86699377, 5.854e-05, 107.60098131, 0.00017561, 358.66993771, 0.00058536, -35.86699377, -5.854e-05, -107.60098131, -0.00017561, -358.66993771, -0.00058536, 0.4, 0.3, 0.003, 0.0, 0.0, 23010, 2)
    ops.limitCurve('ThreePoint', 13010, 3010, 0.0, 121.99807379, 0.01181294, 121.99807379, 0.03543883, 85.39865165, -1040.30332538, 0.05, 2, 0, 73010, 24010, 1, 3)
    ops.uniaxialMaterial('LimitState', 33010, 30.49951845, 4.978e-05, 91.49855534, 0.00014933, 304.99518447, 0.00049776, -30.49951845, -4.978e-05, -91.49855534, -0.00014933, -304.99518447, -0.00049776, 0.4, 0.3, 0.003, 0.0, 0.0, 13010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3010, 99999, 'P', 43010, 'Vy', 33010, 'Vz', 23010, 'My', 13010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173010, 73010, 173010, 3010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124010, 124010, 24010, 3010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173011, 18.75, 4.25, 8.95)
    ops.node(124011, 18.75, 4.25, 11.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3011, 173011, 124011, 0.21, 28671760.90721378, 11946567.04467241, 0.00545409, 0.00235812, 0.00693, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23011, 143.20784267, 0.00048374, 174.73164466, 0.02189749, 17.47316447, 0.06542816, -143.20784267, -0.00048374, -174.73164466, -0.02189749, -17.47316447, -0.06542816, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13011, 66.48383558, 0.00061261, 81.11867141, 0.01915462, 8.11186714, 0.05008993, -66.48383558, -0.00061261, -81.11867141, -0.01915462, -8.11186714, -0.05008993, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23011, 3011, 0.0, 185.278823, 0.00967473, 185.278823, 0.0290242, 129.6951761, -1892.54292365, 0.05, 2, 0, 73011, 24011, 2, 3)
    ops.uniaxialMaterial('LimitState', 43011, 46.31970575, 6.425e-05, 138.95911725, 0.00019275, 463.19705749, 0.00064251, -46.31970575, -6.425e-05, -138.95911725, -0.00019275, -463.19705749, -0.00064251, 0.4, 0.3, 0.003, 0.0, 0.0, 23011, 2)
    ops.limitCurve('ThreePoint', 13011, 3011, 0.0, 132.9164671, 0.01225218, 132.9164671, 0.03675655, 93.04152697, -864.9594636, 0.05, 2, 0, 73011, 24011, 1, 3)
    ops.uniaxialMaterial('LimitState', 33011, 33.22911678, 4.609e-05, 99.68735033, 0.00013828, 332.29116776, 0.00046093, -33.22911678, -4.609e-05, -99.68735033, -0.00013828, -332.29116776, -0.00046093, 0.4, 0.3, 0.003, 0.0, 0.0, 13011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3011, 99999, 'P', 43011, 'Vy', 33011, 'Vz', 23011, 'My', 13011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173011, 73011, 173011, 3011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124011, 124011, 24011, 3011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173012, 24.05, 4.25, 8.95)
    ops.node(124012, 24.05, 4.25, 11.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3012, 173012, 124012, 0.175, 27097960.93096611, 11290817.05456921, 0.00405757, 0.0019651, 0.00401042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23012, 82.28380062, 0.0005091, 100.80467802, 0.04422521, 10.0804678, 0.11857235, -82.28380062, -0.0005091, -100.80467802, -0.04422521, -10.0804678, -0.11857235, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13012, 48.97823599, 0.00061472, 60.00251899, 0.03938802, 6.0002519, 0.09531962, -48.97823599, -0.00061472, -60.00251899, -0.03938802, -6.0002519, -0.09531962, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23012, 3012, 0.0, 165.51493443, 0.0101819, 165.51493443, 0.03054571, 115.8604541, -7534.40164141, 0.05, 2, 0, 73012, 24012, 2, 3)
    ops.uniaxialMaterial('LimitState', 43012, 41.37873361, 7.288e-05, 124.13620082, 0.00021863, 413.78733608, 0.00072877, -41.37873361, -7.288e-05, -124.13620082, -0.00021863, -413.78733608, -0.00072877, 0.4, 0.3, 0.003, 0.0, 0.0, 23012, 2)
    ops.limitCurve('ThreePoint', 13012, 3012, 0.0, 134.51631488, 0.01229441, 134.51631488, 0.03688323, 94.16142042, -3974.56546127, 0.05, 2, 0, 73012, 24012, 1, 3)
    ops.uniaxialMaterial('LimitState', 33012, 33.62907872, 5.923e-05, 100.88723616, 0.00017769, 336.29078721, 0.00059229, -33.62907872, -5.923e-05, -100.88723616, -0.00017769, -336.29078721, -0.00059229, 0.4, 0.3, 0.003, 0.0, 0.0, 13012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3012, 99999, 'P', 43012, 'Vy', 33012, 'Vz', 23012, 'My', 13012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173012, 73012, 173012, 3012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124012, 124012, 24012, 3012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173013, 0.0, 8.5, 8.95)
    ops.node(124013, 0.0, 8.5, 11.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3013, 173013, 124013, 0.175, 24152070.68565962, 10063362.78569151, 0.00405757, 0.0019651, 0.00401042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23013, 84.36543709, 0.00052609, 103.91852129, 0.04784377, 10.39185213, 0.12091569, -84.36543709, -0.00052609, -103.91852129, -0.04784377, -10.39185213, -0.12091569, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13013, 50.01551593, 0.00063716, 61.60743826, 0.04260481, 6.16074383, 0.09757706, -50.01551593, -0.00063716, -61.60743826, -0.04260481, -6.16074383, -0.09757706, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23013, 3013, 0.0, 160.54632585, 0.01052173, 160.54632585, 0.03156518, 112.3824281, -9504.91546585, 0.05, 2, 0, 73013, 24013, 2, 3)
    ops.uniaxialMaterial('LimitState', 43013, 40.13658146, 7.931e-05, 120.40974439, 0.00023794, 401.36581463, 0.00079312, -40.13658146, -7.931e-05, -120.40974439, -0.00023794, -401.36581463, -0.00079312, 0.4, 0.3, 0.003, 0.0, 0.0, 23013, 2)
    ops.limitCurve('ThreePoint', 13013, 3013, 0.0, 127.92317053, 0.01274325, 127.92317053, 0.03822976, 89.54621937, -4974.29925505, 0.05, 2, 0, 73013, 24013, 1, 3)
    ops.uniaxialMaterial('LimitState', 33013, 31.98079263, 6.32e-05, 95.9423779, 0.00018959, 319.80792633, 0.00063196, -31.98079263, -6.32e-05, -95.9423779, -0.00018959, -319.80792633, -0.00063196, 0.4, 0.3, 0.003, 0.0, 0.0, 13013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3013, 99999, 'P', 43013, 'Vy', 33013, 'Vz', 23013, 'My', 13013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173013, 73013, 173013, 3013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124013, 124013, 24013, 3013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173014, 5.3, 8.5, 8.95)
    ops.node(124014, 5.3, 8.5, 11.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3014, 173014, 124014, 0.21, 29016221.44054347, 12090092.26689311, 0.00545409, 0.00235812, 0.00693, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23014, 134.67820734, 0.00047665, 164.18118767, 0.02409607, 16.41811877, 0.06769698, -134.67820734, -0.00047665, -164.18118767, -0.02409607, -16.41811877, -0.06769698, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13014, 62.66052229, 0.0006091, 76.38710949, 0.02106099, 7.63871095, 0.0520462, -62.66052229, -0.0006091, -76.38710949, -0.02106099, -7.63871095, -0.0520462, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23014, 3014, 0.0, 192.57519758, 0.00953292, 192.57519758, 0.02859876, 134.80263831, -2234.69518344, 0.05, 2, 0, 73014, 24014, 2, 3)
    ops.uniaxialMaterial('LimitState', 43014, 48.1437994, 6.599e-05, 144.43139819, 0.00019797, 481.43799395, 0.00065989, -48.1437994, -6.599e-05, -144.43139819, -0.00019797, -481.43799395, -0.00065989, 0.4, 0.3, 0.003, 0.0, 0.0, 23014, 2)
    ops.limitCurve('ThreePoint', 13014, 3014, 0.0, 137.64584051, 0.01218195, 137.64584051, 0.03654584, 96.35208836, -999.12197703, 0.05, 2, 0, 73014, 24014, 1, 3)
    ops.uniaxialMaterial('LimitState', 33014, 34.41146013, 4.717e-05, 103.23438038, 0.0001415, 344.11460128, 0.00047166, -34.41146013, -4.717e-05, -103.23438038, -0.0001415, -344.11460128, -0.00047166, 0.4, 0.3, 0.003, 0.0, 0.0, 13014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3014, 99999, 'P', 43014, 'Vy', 33014, 'Vz', 23014, 'My', 13014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173014, 73014, 173014, 3014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124014, 124014, 24014, 3014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173015, 10.6, 8.5, 8.95)
    ops.node(124015, 10.6, 8.5, 11.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3015, 173015, 124015, 0.1, 26603213.48738837, 11084672.28641182, 0.00127345, 0.00057292, 0.00146667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23015, 39.19038617, 0.00055978, 47.98938477, 0.02419914, 4.79893848, 0.08572995, -39.19038617, -0.00055978, -47.98938477, -0.02419914, -4.79893848, -0.08572995, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13015, 21.10323972, 0.00077709, 25.84132462, 0.02113207, 2.58413246, 0.06428289, -21.10323972, -0.00077709, -25.84132462, -0.02113207, -2.58413246, -0.06428289, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23015, 3015, 0.0, 79.64301769, 0.01119552, 79.64301769, 0.03358657, 55.75011238, -1506.97895679, 0.05, 2, 0, 73015, 24015, 2, 3)
    ops.uniaxialMaterial('LimitState', 43015, 19.91075442, 6.251e-05, 59.73226327, 0.00018753, 199.10754423, 0.00062509, -19.91075442, -6.251e-05, -59.73226327, -0.00018753, -199.10754423, -0.00062509, 0.4, 0.3, 0.003, 0.0, 0.0, 23015, 2)
    ops.limitCurve('ThreePoint', 13015, 3015, 0.0, 63.70371887, 0.01554188, 63.70371887, 0.04662563, 44.59260321, -751.92603138, 0.05, 2, 0, 73015, 24015, 1, 3)
    ops.uniaxialMaterial('LimitState', 33015, 15.92592972, 5e-05, 47.77778915, 0.00015, 159.25929717, 0.00049999, -15.92592972, -5e-05, -47.77778915, -0.00015, -159.25929717, -0.00049999, 0.4, 0.3, 0.003, 0.0, 0.0, 13015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3015, 99999, 'P', 43015, 'Vy', 33015, 'Vz', 23015, 'My', 13015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173015, 73015, 173015, 3015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124015, 124015, 24015, 3015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173016, 13.45, 8.5, 8.95)
    ops.node(124016, 13.45, 8.5, 11.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3016, 173016, 124016, 0.1, 27950575.30038399, 11646073.04182666, 0.00127345, 0.00057292, 0.00146667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23016, 40.07081508, 0.00054607, 48.93268486, 0.0236296, 4.89326849, 0.08595331, -40.07081508, -0.00054607, -48.93268486, -0.0236296, -4.89326849, -0.08595331, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13016, 21.58308321, 0.00074345, 26.35629465, 0.02061982, 2.63562946, 0.0643267, -21.58308321, -0.00074345, -26.35629465, -0.02061982, -2.63562946, -0.0643267, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23016, 3016, 0.0, 83.38302201, 0.01092137, 83.38302201, 0.03276411, 58.36811541, -1506.90564851, 0.05, 2, 0, 73016, 24016, 2, 3)
    ops.uniaxialMaterial('LimitState', 43016, 20.8457555, 6.229e-05, 62.53726651, 0.00018687, 208.45755503, 0.0006229, -20.8457555, -6.229e-05, -62.53726651, -0.00018687, -208.45755503, -0.0006229, 0.4, 0.3, 0.003, 0.0, 0.0, 23016, 2)
    ops.limitCurve('ThreePoint', 13016, 3016, 0.0, 66.85091687, 0.01486905, 66.85091687, 0.04460714, 46.79564181, -751.89366697, 0.05, 2, 0, 73016, 24016, 1, 3)
    ops.uniaxialMaterial('LimitState', 33016, 16.71272922, 4.994e-05, 50.13818765, 0.00014982, 167.12729217, 0.0004994, -16.71272922, -4.994e-05, -50.13818765, -0.00014982, -167.12729217, -0.0004994, 0.4, 0.3, 0.003, 0.0, 0.0, 13016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3016, 99999, 'P', 43016, 'Vy', 33016, 'Vz', 23016, 'My', 13016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173016, 73016, 173016, 3016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124016, 124016, 24016, 3016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173017, 18.75, 8.5, 8.95)
    ops.node(124017, 18.75, 8.5, 11.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3017, 173017, 124017, 0.21, 24553990.24856355, 10230829.27023481, 0.00545409, 0.00235812, 0.00693, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23017, 131.59019826, 0.00049066, 161.8891643, 0.02362667, 16.18891643, 0.06595741, -131.59019826, -0.00049066, -161.8891643, -0.02362667, -16.18891643, -0.06595741, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13017, 60.8587673, 0.00063717, 74.87164781, 0.02067047, 7.48716478, 0.05075304, -60.8587673, -0.00063717, -74.87164781, -0.02067047, -7.48716478, -0.05075304, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23017, 3017, 0.0, 153.11848395, 0.00981318, 153.11848395, 0.02943954, 107.18293876, -1823.59933791, 0.05, 2, 0, 73017, 24017, 2, 3)
    ops.uniaxialMaterial('LimitState', 43017, 38.27962099, 6.2e-05, 114.83886296, 0.00018601, 382.79620987, 0.00062004, -38.27962099, -6.2e-05, -114.83886296, -0.00018601, -382.79620987, -0.00062004, 0.4, 0.3, 0.003, 0.0, 0.0, 23017, 2)
    ops.limitCurve('ThreePoint', 13017, 3017, 0.0, 108.79440375, 0.01274336, 108.79440375, 0.03823007, 76.15608263, -837.7363473, 0.05, 2, 0, 73017, 24017, 1, 3)
    ops.uniaxialMaterial('LimitState', 33017, 27.19860094, 4.406e-05, 81.59580281, 0.00013217, 271.98600938, 0.00044055, -27.19860094, -4.406e-05, -81.59580281, -0.00013217, -271.98600938, -0.00044055, 0.4, 0.3, 0.003, 0.0, 0.0, 13017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3017, 99999, 'P', 43017, 'Vy', 33017, 'Vz', 23017, 'My', 13017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173017, 73017, 173017, 3017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124017, 124017, 24017, 3017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173018, 24.05, 8.5, 8.95)
    ops.node(124018, 24.05, 8.5, 11.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3018, 173018, 124018, 0.175, 28304493.96892123, 11793539.15371718, 0.00405757, 0.0019651, 0.00401042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23018, 83.45428684, 0.00050373, 101.95432222, 0.04265525, 10.19543222, 0.11737511, -83.45428684, -0.00050373, -101.95432222, -0.04265525, -10.19543222, -0.11737511, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13018, 49.70752991, 0.00060492, 60.72662907, 0.03799053, 6.07266291, 0.09420253, -49.70752991, -0.00060492, -60.72662907, -0.03799053, -6.07266291, -0.09420253, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23018, 3018, 0.0, 168.36194251, 0.01007464, 168.36194251, 0.03022391, 117.85335975, -6877.67260959, 0.05, 2, 0, 73018, 24018, 2, 3)
    ops.uniaxialMaterial('LimitState', 43018, 42.09048563, 7.097e-05, 126.27145688, 0.00021291, 420.90485626, 0.00070971, -42.09048563, -7.097e-05, -126.27145688, -0.00021291, -420.90485626, -0.00070971, 0.4, 0.3, 0.003, 0.0, 0.0, 23018, 2)
    ops.limitCurve('ThreePoint', 13018, 3018, 0.0, 137.85284852, 0.01209843, 137.85284852, 0.03629529, 96.49699396, -3640.3987848, 0.05, 2, 0, 73018, 24018, 1, 3)
    ops.uniaxialMaterial('LimitState', 33018, 34.46321213, 5.811e-05, 103.38963639, 0.00017433, 344.63212129, 0.0005811, -34.46321213, -5.811e-05, -103.38963639, -0.00017433, -344.63212129, -0.0005811, 0.4, 0.3, 0.003, 0.0, 0.0, 13018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3018, 99999, 'P', 43018, 'Vy', 33018, 'Vz', 23018, 'My', 13018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173018, 73018, 173018, 3018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124018, 124018, 24018, 3018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173019, 0.0, 12.75, 8.975)
    ops.node(124019, 0.0, 12.75, 11.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3019, 173019, 124019, 0.0625, 27133387.67270502, 11305578.19696043, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23019, 14.09053483, 0.00074303, 17.25256695, 0.02872908, 1.7252567, 0.09234352, -14.09053483, -0.00074303, -17.25256695, -0.02872908, -1.7252567, -0.09234352, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13019, 14.09053483, 0.00074303, 17.25256695, 0.02872908, 1.7252567, 0.09234352, -14.09053483, -0.00074303, -17.25256695, -0.02872908, -1.7252567, -0.09234352, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23019, 3019, 0.0, 53.79447143, 0.01486069, 53.79447143, 0.04458207, 37.65613, -1706.543588, 0.05, 2, 0, 73019, 24019, 2, 3)
    ops.uniaxialMaterial('LimitState', 43019, 13.44861786, 6.623e-05, 40.34585357, 0.0001987, 134.48617858, 0.00066234, -13.44861786, -6.623e-05, -40.34585357, -0.0001987, -134.48617858, -0.00066234, 0.4, 0.3, 0.003, 0.0, 0.0, 23019, 2)
    ops.limitCurve('ThreePoint', 13019, 3019, 0.0, 53.79447143, 0.01486069, 53.79447143, 0.04458207, 37.65613, -1706.543588, 0.05, 2, 0, 73019, 24019, 1, 3)
    ops.uniaxialMaterial('LimitState', 33019, 13.44861786, 6.623e-05, 40.34585357, 0.0001987, 134.48617858, 0.00066234, -13.44861786, -6.623e-05, -40.34585357, -0.0001987, -134.48617858, -0.00066234, 0.4, 0.3, 0.003, 0.0, 0.0, 13019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3019, 99999, 'P', 43019, 'Vy', 33019, 'Vz', 23019, 'My', 13019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173019, 73019, 173019, 3019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124019, 124019, 24019, 3019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173020, 5.3, 12.75, 8.975)
    ops.node(124020, 5.3, 12.75, 11.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3020, 173020, 124020, 0.125, 27590504.44164147, 11496043.51735061, 0.00178813, 0.00286458, 0.00071615, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23020, 24.79059161, 0.00079777, 30.32548046, 0.01995692, 3.03254805, 0.05844249, -24.79059161, -0.00079777, -30.32548046, -0.01995692, -3.03254805, -0.05844249, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13020, 62.48927573, 0.00050939, 76.44098776, 0.02423525, 7.64409878, 0.08814061, -62.48927573, -0.00050939, -76.44098776, -0.02423525, -7.64409878, -0.08814061, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23020, 3020, 0.0, 77.93987226, 0.01595548, 77.93987226, 0.04786644, 54.55791058, -870.29385837, 0.05, 2, 0, 73020, 24020, 2, 3)
    ops.uniaxialMaterial('LimitState', 43020, 19.48496807, 4.719e-05, 58.4549042, 0.00014156, 194.84968066, 0.00047187, -19.48496807, -4.719e-05, -58.4549042, -0.00014156, -194.84968066, -0.00047187, 0.4, 0.3, 0.003, 0.0, 0.0, 23020, 2)
    ops.limitCurve('ThreePoint', 13020, 3020, 0.0, 108.260743, 0.01018778, 108.260743, 0.03056334, 75.7825201, -2659.79016176, 0.05, 2, 0, 73020, 24020, 1, 3)
    ops.uniaxialMaterial('LimitState', 33020, 27.06518575, 6.554e-05, 81.19555725, 0.00019663, 270.6518575, 0.00065544, -27.06518575, -6.554e-05, -81.19555725, -0.00019663, -270.6518575, -0.00065544, 0.4, 0.3, 0.003, 0.0, 0.0, 13020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3020, 99999, 'P', 43020, 'Vy', 33020, 'Vz', 23020, 'My', 13020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173020, 73020, 173020, 3020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124020, 124020, 24020, 3020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173021, 10.6, 12.75, 8.975)
    ops.node(124021, 10.6, 12.75, 11.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3021, 173021, 124021, 0.0875, 27248955.30484546, 11353731.37701894, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23021, 19.47499564, 0.00079425, 23.83690795, 0.02528932, 2.3836908, 0.07429182, -19.47499564, -0.00079425, -23.83690795, -0.02528932, -2.3836908, -0.07429182, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13021, 31.47774299, 0.00061504, 38.52797074, 0.02793024, 3.85279707, 0.09138717, -31.47774299, -0.00061504, -38.52797074, -0.02793024, -3.85279707, -0.09138717, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23021, 3021, 0.0, 65.93033089, 0.01588491, 65.93033089, 0.04765474, 46.15123162, -1275.93123428, 0.05, 2, 0, 73021, 24021, 2, 3)
    ops.uniaxialMaterial('LimitState', 43021, 16.48258272, 5.774e-05, 49.44774817, 0.00017321, 164.82582722, 0.00057737, -16.48258272, -5.774e-05, -49.44774817, -0.00017321, -164.82582722, -0.00057737, 0.4, 0.3, 0.003, 0.0, 0.0, 23021, 2)
    ops.limitCurve('ThreePoint', 13021, 3021, 0.0, 75.42776039, 0.01230078, 75.42776039, 0.03690234, 52.79943227, -2246.31576759, 0.05, 2, 0, 73021, 24021, 1, 3)
    ops.uniaxialMaterial('LimitState', 33021, 18.8569401, 6.605e-05, 56.57082029, 0.00019816, 188.56940097, 0.00066055, -18.8569401, -6.605e-05, -56.57082029, -0.00019816, -188.56940097, -0.00066055, 0.4, 0.3, 0.003, 0.0, 0.0, 13021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3021, 99999, 'P', 43021, 'Vy', 33021, 'Vz', 23021, 'My', 13021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173021, 73021, 173021, 3021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124021, 124021, 24021, 3021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173022, 13.45, 12.75, 8.975)
    ops.node(124022, 13.45, 12.75, 11.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3022, 173022, 124022, 0.0875, 26975625.92201541, 11239844.13417309, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23022, 19.60820482, 0.00074759, 24.01374801, 0.02257466, 2.4013748, 0.07148764, -19.60820482, -0.00074759, -24.01374801, -0.02257466, -2.4013748, -0.07148764, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13022, 31.83689636, 0.00059068, 38.98996434, 0.02493071, 3.89899643, 0.08827173, -31.83689636, -0.00059068, -38.98996434, -0.02493071, -3.89899643, -0.08827173, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23022, 3022, 0.0, 58.20131387, 0.01495171, 58.20131387, 0.04485514, 40.74091971, -953.76649796, 0.05, 2, 0, 73022, 24022, 2, 3)
    ops.uniaxialMaterial('LimitState', 43022, 14.55032847, 5.149e-05, 43.65098541, 0.00015446, 145.50328468, 0.00051485, -14.55032847, -5.149e-05, -43.65098541, -0.00015446, -145.50328468, -0.00051485, 0.4, 0.3, 0.003, 0.0, 0.0, 23022, 2)
    ops.limitCurve('ThreePoint', 13022, 3022, 0.0, 69.25898066, 0.01181365, 69.25898066, 0.03544096, 48.48128646, -1650.2619758, 0.05, 2, 0, 73022, 24022, 1, 3)
    ops.uniaxialMaterial('LimitState', 33022, 17.31474517, 6.127e-05, 51.9442355, 0.0001838, 173.14745166, 0.00061267, -17.31474517, -6.127e-05, -51.9442355, -0.0001838, -173.14745166, -0.00061267, 0.4, 0.3, 0.003, 0.0, 0.0, 13022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3022, 99999, 'P', 43022, 'Vy', 33022, 'Vz', 23022, 'My', 13022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173022, 73022, 173022, 3022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124022, 124022, 24022, 3022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173023, 18.75, 12.75, 8.975)
    ops.node(124023, 18.75, 12.75, 11.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3023, 173023, 124023, 0.125, 27815675.0894088, 11589864.620587, 0.00178813, 0.00286458, 0.00071615, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23023, 25.08034439, 0.00081929, 30.66430408, 0.02378308, 3.06643041, 0.06231648, -25.08034439, -0.00081929, -30.66430408, -0.02378308, -3.06643041, -0.06231648, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13023, 63.05265924, 0.00051657, 77.09088385, 0.02895394, 7.70908839, 0.09293871, -63.05265924, -0.00051657, -77.09088385, -0.02895394, -7.70908839, -0.09293871, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23023, 3023, 0.0, 88.45150017, 0.01638586, 88.45150017, 0.04915757, 61.91605012, -1306.15228562, 0.05, 2, 0, 73023, 24023, 2, 3)
    ops.uniaxialMaterial('LimitState', 43023, 22.11287504, 5.312e-05, 66.33862513, 0.00015935, 221.12875043, 0.00053117, -22.11287504, -5.312e-05, -66.33862513, -0.00015935, -221.12875043, -0.00053117, 0.4, 0.3, 0.003, 0.0, 0.0, 23023, 2)
    ops.limitCurve('ThreePoint', 13023, 3023, 0.0, 121.41450046, 0.01033144, 121.41450046, 0.03099431, 84.99015032, -4205.92777011, 0.05, 2, 0, 73023, 24023, 1, 3)
    ops.uniaxialMaterial('LimitState', 33023, 30.35362512, 7.291e-05, 91.06087535, 0.00021874, 303.53625115, 0.00072912, -30.35362512, -7.291e-05, -91.06087535, -0.00021874, -303.53625115, -0.00072912, 0.4, 0.3, 0.003, 0.0, 0.0, 13023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3023, 99999, 'P', 43023, 'Vy', 33023, 'Vz', 23023, 'My', 13023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173023, 73023, 173023, 3023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124023, 124023, 24023, 3023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173024, 24.05, 12.75, 8.975)
    ops.node(124024, 24.05, 12.75, 11.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3024, 173024, 124024, 0.0625, 30982920.86371937, 12909550.35988307, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23024, 15.17275708, 0.000696, 18.39387468, 0.02798303, 1.83938747, 0.09276814, -15.17275708, -0.000696, -18.39387468, -0.02798303, -1.83938747, -0.09276814, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13024, 15.17275708, 0.000696, 18.39387468, 0.02798303, 1.83938747, 0.09276814, -15.17275708, -0.000696, -18.39387468, -0.02798303, -1.83938747, -0.09276814, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23024, 3024, 0.0, 62.78652598, 0.01392006, 62.78652598, 0.04176017, 43.95056819, -1969.22481179, 0.05, 2, 0, 73024, 24024, 2, 3)
    ops.uniaxialMaterial('LimitState', 43024, 15.6966315, 6.77e-05, 47.08989449, 0.0002031, 156.96631496, 0.00067701, -15.6966315, -6.77e-05, -47.08989449, -0.0002031, -156.96631496, -0.00067701, 0.4, 0.3, 0.003, 0.0, 0.0, 23024, 2)
    ops.limitCurve('ThreePoint', 13024, 3024, 0.0, 62.78652598, 0.01392006, 62.78652598, 0.04176017, 43.95056819, -1969.22481179, 0.05, 2, 0, 73024, 24024, 1, 3)
    ops.uniaxialMaterial('LimitState', 33024, 15.6966315, 6.77e-05, 47.08989449, 0.0002031, 156.96631496, 0.00067701, -15.6966315, -6.77e-05, -47.08989449, -0.0002031, -156.96631496, -0.00067701, 0.4, 0.3, 0.003, 0.0, 0.0, 13024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3024, 99999, 'P', 43024, 'Vy', 33024, 'Vz', 23024, 'My', 13024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173024, 73024, 173024, 3024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124024, 124024, 24024, 3024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170003, 10.6, 0.0, 0.0)
    ops.node(124025, 10.6, 0.0, 1.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4063, 170003, 124025, 0.175, 25666792.77718947, 10694496.99049561, 0.00405757, 0.00401042, 0.0019651, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24063, 102.78026237, 0.00057119, 125.09794748, 0.05266201, 12.50979475, 0.13511844, -102.78026237, -0.00057119, -125.09794748, -0.05266201, -12.50979475, -0.13511844, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14063, 130.09230083, 0.00052305, 158.34051638, 0.051673, 15.83405164, 0.13064027, -130.09230083, -0.00052305, -158.34051638, -0.051673, -15.83405164, -0.13064027, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24063, 4063, 0.0, 219.42695664, 0.01142389, 219.42695664, 0.03427167, 153.59886965, -4788.45132394, 0.05, 2, 0, 70003, 24025, 2, 3)
    ops.uniaxialMaterial('LimitState', 44063, 54.85673916, 5.1e-05, 164.57021748, 0.000153, 548.56739161, 0.00051001, -54.85673916, -5.1e-05, -164.57021748, -0.000153, -548.56739161, -0.00051001, 0.4, 0.3, 0.003, 0.0, 0.0, 24063, 2)
    ops.limitCurve('ThreePoint', 14063, 4063, 0.0, 345.71053362, 0.01046102, 345.71053362, 0.03138306, 241.99737353, -13229.23953601, 0.05, 2, 0, 70003, 24025, 1, 3)
    ops.uniaxialMaterial('LimitState', 34063, 86.4276334, 8.035e-05, 259.28290021, 0.00024106, 864.27633404, 0.00080353, -86.4276334, -8.035e-05, -259.28290021, -0.00024106, -864.27633404, -0.00080353, 0.4, 0.3, 0.003, 0.0, 0.0, 14063, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4063, 99999, 'P', 44063, 'Vy', 34063, 'Vz', 24063, 'My', 14063, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170003, 70003, 170003, 4063, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124025, 124025, 24025, 4063, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174025, 10.6, 0.0, 1.65)
    ops.node(121003, 10.6, 0.0, 2.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4064, 174025, 121003, 0.175, 26808357.15137665, 11170148.81307361, 0.00405757, 0.00401042, 0.0019651, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24064, 84.50350816, 0.00054902, 102.83384713, 0.0551882, 10.28338471, 0.14344072, -84.50350816, -0.00054902, -102.83384713, -0.0551882, -10.28338471, -0.14344072, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14064, 113.50935732, 0.00050839, 138.13158948, 0.05416067, 13.81315895, 0.13867876, -113.50935732, -0.00050839, -138.13158948, -0.05416067, -13.81315895, -0.13867876, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24064, 4064, 0.0, 243.82763378, 0.01098048, 243.82763378, 0.03294144, 170.67934365, -6477.8492927, 0.05, 2, 0, 74025, 21003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44064, 60.95690845, 5.426e-05, 182.87072534, 0.00016278, 609.56908445, 0.00054259, -60.95690845, -5.426e-05, -182.87072534, -0.00016278, -609.56908445, -0.00054259, 0.4, 0.3, 0.003, 0.0, 0.0, 24064, 2)
    ops.limitCurve('ThreePoint', 14064, 4064, 0.0, 393.05486019, 0.01016771, 393.05486019, 0.03050313, 275.13840213, -19787.92695618, 0.05, 2, 0, 74025, 21003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34064, 98.26371505, 8.747e-05, 294.79114514, 0.0002624, 982.63715047, 0.00087467, -98.26371505, -8.747e-05, -294.79114514, -0.0002624, -982.63715047, -0.00087467, 0.4, 0.3, 0.003, 0.0, 0.0, 14064, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4064, 99999, 'P', 44064, 'Vy', 34064, 'Vz', 24064, 'My', 14064, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174025, 74025, 174025, 4064, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121003, 121003, 21003, 4064, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170004, 13.45, 0.0, 0.0)
    ops.node(124026, 13.45, 0.0, 1.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4065, 170004, 124026, 0.175, 24880890.57703248, 10367037.7404302, 0.00405757, 0.00401042, 0.0019651, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24065, 100.95510974, 0.00057303, 122.92131366, 0.0536048, 12.29213137, 0.13319307, -100.95510974, -0.00057303, -122.92131366, -0.0536048, -12.29213137, -0.13319307, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14065, 128.04100962, 0.00052361, 155.90066858, 0.05259752, 15.59006686, 0.128818, -128.04100962, -0.00052361, -155.90066858, -0.05259752, -15.59006686, -0.128818, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24065, 4065, 0.0, 222.45582707, 0.01146057, 222.45582707, 0.03438171, 155.71907895, -5487.88247588, 0.05, 2, 0, 70004, 24026, 2, 3)
    ops.uniaxialMaterial('LimitState', 44065, 55.61395677, 5.334e-05, 166.84187031, 0.00016002, 556.13956769, 0.00053338, -55.61395677, -5.334e-05, -166.84187031, -0.00016002, -556.13956769, -0.00053338, 0.4, 0.3, 0.003, 0.0, 0.0, 24065, 2)
    ops.limitCurve('ThreePoint', 14065, 4065, 0.0, 357.13597613, 0.01047226, 357.13597613, 0.03141679, 249.99518329, -15744.98376458, 0.05, 2, 0, 70004, 24026, 1, 3)
    ops.uniaxialMaterial('LimitState', 34065, 89.28399403, 8.563e-05, 267.8519821, 0.00025689, 892.83994032, 0.00085631, -89.28399403, -8.563e-05, -267.8519821, -0.00025689, -892.83994032, -0.00085631, 0.4, 0.3, 0.003, 0.0, 0.0, 14065, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4065, 99999, 'P', 44065, 'Vy', 34065, 'Vz', 24065, 'My', 14065, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170004, 70004, 170004, 4065, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124026, 124026, 24026, 4065, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174026, 13.45, 0.0, 1.65)
    ops.node(121004, 13.45, 0.0, 2.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4066, 174026, 121004, 0.175, 28680485.7933369, 11950202.41389037, 0.00405757, 0.00401042, 0.0019651, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24066, 86.63147575, 0.00054939, 105.12153284, 0.05395675, 10.51215328, 0.14688481, -86.63147575, -0.00054939, -105.12153284, -0.05395675, -10.51215328, -0.14688481, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14066, 116.42505931, 0.00050904, 141.27406455, 0.05295175, 14.12740645, 0.14194755, -116.42505931, -0.00050904, -141.27406455, -0.05295175, -14.12740645, -0.14194755, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24066, 4066, 0.0, 254.94266516, 0.01098775, 254.94266516, 0.03296326, 178.45986562, -6161.84935144, 0.05, 2, 0, 74026, 21004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44066, 63.73566629, 5.303e-05, 191.20699887, 0.00015909, 637.35666291, 0.0005303, -63.73566629, -5.303e-05, -191.20699887, -0.00015909, -637.35666291, -0.0005303, 0.4, 0.3, 0.003, 0.0, 0.0, 24066, 2)
    ops.limitCurve('ThreePoint', 14066, 4066, 0.0, 404.52405036, 0.01018072, 404.52405036, 0.03054216, 283.16683525, -18607.78069811, 0.05, 2, 0, 74026, 21004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34066, 101.13101259, 8.414e-05, 303.39303777, 0.00025243, 1011.31012591, 0.00084143, -101.13101259, -8.414e-05, -303.39303777, -0.00025243, -1011.31012591, -0.00084143, 0.4, 0.3, 0.003, 0.0, 0.0, 14066, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4066, 99999, 'P', 44066, 'Vy', 34066, 'Vz', 24066, 'My', 14066, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174026, 74026, 174026, 4066, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121004, 121004, 21004, 4066, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171003, 10.6, 0.0, 3.175)
    ops.node(124027, 10.6, 0.0, 4.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4068, 171003, 124027, 0.175, 28282769.70136286, 11784487.37556786, 0.00405757, 0.00401042, 0.0019651, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24068, 78.93313675, 0.00054472, 95.98420175, 0.05556065, 9.59842018, 0.15155886, -78.93313675, -0.00054472, -95.98420175, -0.05556065, -9.59842018, -0.15155886, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14068, 105.98856979, 0.0005049, 128.88412503, 0.05452713, 12.8884125, 0.14646315, -105.98856979, -0.0005049, -128.88412503, -0.05452713, -12.8884125, -0.14646315, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24068, 4068, 0.0, 241.86732842, 0.01089439, 241.86732842, 0.03268317, 169.30712989, -6246.73560001, 0.05, 2, 0, 71003, 24027, 2, 3)
    ops.uniaxialMaterial('LimitState', 44068, 60.4668321, 5.102e-05, 181.40049631, 0.00015305, 604.66832105, 0.00051017, -60.4668321, -5.102e-05, -181.40049631, -0.00015305, -604.66832105, -0.00051017, 0.4, 0.3, 0.003, 0.0, 0.0, 24068, 2)
    ops.limitCurve('ThreePoint', 14068, 4068, 0.0, 384.37250765, 0.01009794, 384.37250765, 0.03029382, 269.06075536, -19844.68277718, 0.05, 2, 0, 71003, 24027, 1, 3)
    ops.uniaxialMaterial('LimitState', 34068, 96.09312691, 8.108e-05, 288.27938074, 0.00024323, 960.93126913, 0.00081076, -96.09312691, -8.108e-05, -288.27938074, -0.00024323, -960.93126913, -0.00081076, 0.4, 0.3, 0.003, 0.0, 0.0, 14068, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4068, 99999, 'P', 44068, 'Vy', 34068, 'Vz', 24068, 'My', 14068, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171003, 71003, 171003, 4068, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124027, 124027, 24027, 4068, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174027, 10.6, 0.0, 4.55)
    ops.node(122003, 10.6, 0.0, 5.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4069, 174027, 122003, 0.175, 26324114.902863, 10968381.20952625, 0.00405757, 0.00401042, 0.0019651, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24069, 75.09363965, 0.00055714, 91.67552404, 0.05633522, 9.1675524, 0.1503548, -75.09363965, -0.00055714, -91.67552404, -0.05633522, -9.1675524, -0.1503548, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14069, 100.77650795, 0.00051267, 123.02958307, 0.05528328, 12.30295831, 0.14532441, -100.77650795, -0.00051267, -123.02958307, -0.05528328, -12.30295831, -0.14532441, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24069, 4069, 0.0, 219.73671425, 0.0111427, 219.73671425, 0.03342811, 153.81569997, -6103.85799225, 0.05, 2, 0, 74027, 22003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44069, 54.93417856, 4.98e-05, 164.80253569, 0.00014939, 549.34178562, 0.00049798, -54.93417856, -4.98e-05, -164.80253569, -0.00014939, -549.34178562, -0.00049798, 0.4, 0.3, 0.003, 0.0, 0.0, 24069, 2)
    ops.limitCurve('ThreePoint', 14069, 4069, 0.0, 352.1493008, 0.01025339, 352.1493008, 0.03076016, 246.50451056, -19782.15422344, 0.05, 2, 0, 74027, 22003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34069, 88.0373252, 7.981e-05, 264.1119756, 0.00023942, 880.373252, 0.00079806, -88.0373252, -7.981e-05, -264.1119756, -0.00023942, -880.373252, -0.00079806, 0.4, 0.3, 0.003, 0.0, 0.0, 14069, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4069, 99999, 'P', 44069, 'Vy', 34069, 'Vz', 24069, 'My', 14069, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174027, 74027, 174027, 4069, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122003, 122003, 22003, 4069, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171004, 13.45, 0.0, 3.175)
    ops.node(124028, 13.45, 0.0, 4.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4070, 171004, 124028, 0.175, 27256701.24617767, 11356958.85257403, 0.00405757, 0.00401042, 0.0019651, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24070, 79.07379626, 0.00056152, 96.32543973, 0.05495222, 9.63254397, 0.14880924, -79.07379626, -0.00056152, -96.32543973, -0.05495222, -9.63254397, -0.14880924, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14070, 106.45373876, 0.00051573, 129.67890352, 0.05392402, 12.96789035, 0.14380946, -106.45373876, -0.00051573, -129.67890352, -0.05392402, -12.96789035, -0.14380946, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24070, 4070, 0.0, 227.27603522, 0.01123045, 227.27603522, 0.03369135, 159.09322465, -5585.56752201, 0.05, 2, 0, 71004, 24028, 2, 3)
    ops.uniaxialMaterial('LimitState', 44070, 56.8190088, 4.974e-05, 170.45702641, 0.00014923, 568.19008804, 0.00049744, -56.8190088, -4.974e-05, -170.45702641, -0.00014923, -568.19008804, -0.00049744, 0.4, 0.3, 0.003, 0.0, 0.0, 24070, 2)
    ops.limitCurve('ThreePoint', 14070, 4070, 0.0, 359.82066184, 0.01031454, 359.82066184, 0.03094361, 251.87446328, -17333.73566582, 0.05, 2, 0, 71004, 24028, 1, 3)
    ops.uniaxialMaterial('LimitState', 34070, 89.95516546, 7.875e-05, 269.86549638, 0.00023626, 899.55165459, 0.00078754, -89.95516546, -7.875e-05, -269.86549638, -0.00023626, -899.55165459, -0.00078754, 0.4, 0.3, 0.003, 0.0, 0.0, 14070, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4070, 99999, 'P', 44070, 'Vy', 34070, 'Vz', 24070, 'My', 14070, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171004, 71004, 171004, 4070, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124028, 124028, 24028, 4070, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174028, 13.45, 0.0, 4.55)
    ops.node(122004, 13.45, 0.0, 5.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4071, 174028, 122004, 0.175, 28220159.65726018, 11758399.85719174, 0.00405757, 0.00401042, 0.0019651, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24071, 71.03488705, 0.00050969, 86.44897847, 0.05480406, 8.64489785, 0.15265251, -71.03488705, -0.00050969, -86.44897847, -0.05480406, -8.64489785, -0.15265251, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14071, 95.31892106, 0.00047992, 116.00248408, 0.05379361, 11.60024841, 0.14750159, -95.31892106, -0.00047992, -116.00248408, -0.05379361, -11.60024841, -0.14750159, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24071, 4071, 0.0, 228.49769506, 0.01019383, 228.49769506, 0.03058148, 159.94838654, -5513.32871298, 0.05, 2, 0, 74028, 22004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44071, 57.12442377, 4.83e-05, 171.3732713, 0.00014491, 571.24423765, 0.00048304, -57.12442377, -4.83e-05, -171.3732713, -0.00014491, -571.24423765, -0.00048304, 0.4, 0.3, 0.003, 0.0, 0.0, 24071, 2)
    ops.limitCurve('ThreePoint', 14071, 4071, 0.0, 358.69801214, 0.00959832, 358.69801214, 0.02879496, 251.0886085, -17515.09871288, 0.05, 2, 0, 74028, 22004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34071, 89.67450303, 7.583e-05, 269.0235091, 0.00022749, 896.74503035, 0.00075828, -89.67450303, -7.583e-05, -269.0235091, -0.00022749, -896.74503035, -0.00075828, 0.4, 0.3, 0.003, 0.0, 0.0, 14071, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4071, 99999, 'P', 44071, 'Vy', 34071, 'Vz', 24071, 'My', 14071, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174028, 74028, 174028, 4071, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122004, 122004, 22004, 4071, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172003, 10.6, 0.0, 6.075)
    ops.node(124029, 10.6, 0.0, 7.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4073, 172003, 124029, 0.1, 28301146.85745252, 11792144.52393855, 0.00127345, 0.00146667, 0.00057292, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24073, 35.18522176, 0.00062431, 42.75615383, 0.05101324, 4.27561538, 0.13124402, -35.18522176, -0.00062431, -42.75615383, -0.05101324, -4.27561538, -0.13124402, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14073, 59.12014542, 0.00051613, 71.84124201, 0.06067164, 7.1841242, 0.16067164, -59.12014542, -0.00051613, -71.84124201, -0.06067164, -7.1841242, -0.16067164, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24073, 4073, 0.0, 120.92075211, 0.0124863, 120.92075211, 0.0374589, 84.64452648, -4158.31668271, 0.05, 2, 0, 72003, 24029, 2, 3)
    ops.uniaxialMaterial('LimitState', 44073, 30.23018803, 4.461e-05, 90.69056408, 0.00013382, 302.30188027, 0.00044606, -30.23018803, -4.461e-05, -90.69056408, -0.00013382, -302.30188027, -0.00044606, 0.4, 0.3, 0.003, 0.0, 0.0, 24073, 2)
    ops.limitCurve('ThreePoint', 14073, 4073, 0.0, 193.47320337, 0.01032259, 193.47320337, 0.03096778, 135.43124236, -8324.28434048, 0.05, 2, 0, 72003, 24029, 1, 3)
    ops.uniaxialMaterial('LimitState', 34073, 48.36830084, 7.137e-05, 145.10490253, 0.00021411, 483.68300843, 0.0007137, -48.36830084, -7.137e-05, -145.10490253, -0.00021411, -483.68300843, -0.0007137, 0.4, 0.3, 0.003, 0.0, 0.0, 14073, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4073, 99999, 'P', 44073, 'Vy', 34073, 'Vz', 24073, 'My', 14073, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172003, 72003, 172003, 4073, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124029, 124029, 24029, 4073, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174029, 10.6, 0.0, 7.45)
    ops.node(123003, 10.6, 0.0, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4074, 174029, 123003, 0.1, 26069730.30643025, 10862387.62767927, 0.00127345, 0.00146667, 0.00057292, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24074, 42.84490234, 0.000701, 52.3204318, 0.05301404, 5.23204318, 0.1324927, -42.84490234, -0.000701, -52.3204318, -0.05301404, -5.23204318, -0.1324927, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14074, 66.00361476, 0.00055487, 80.6008985, 0.06300745, 8.06008985, 0.16300745, -66.00361476, -0.00055487, -80.6008985, -0.06300745, -8.06008985, -0.16300745, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24074, 4074, 0.0, 106.64109257, 0.01401993, 106.64109257, 0.0420598, 74.6487648, -3987.37841648, 0.05, 2, 0, 74029, 23003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44074, 26.66027314, 4.271e-05, 79.98081942, 0.00012812, 266.60273141, 0.00042706, -26.66027314, -4.271e-05, -79.98081942, -0.00012812, -266.60273141, -0.00042706, 0.4, 0.3, 0.003, 0.0, 0.0, 24074, 2)
    ops.limitCurve('ThreePoint', 14074, 4074, 0.0, 170.62574811, 0.01109743, 170.62574811, 0.0332923, 119.43802367, -8166.50952696, 0.05, 2, 0, 74029, 23003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34074, 42.65643703, 6.833e-05, 127.96931108, 0.00020499, 426.56437026, 0.0006833, -42.65643703, -6.833e-05, -127.96931108, -0.00020499, -426.56437026, -0.0006833, 0.4, 0.3, 0.003, 0.0, 0.0, 14074, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4074, 99999, 'P', 44074, 'Vy', 34074, 'Vz', 24074, 'My', 14074, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174029, 74029, 174029, 4074, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123003, 123003, 23003, 4074, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172004, 13.45, 0.0, 6.075)
    ops.node(124030, 13.45, 0.0, 7.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4075, 172004, 124030, 0.1, 29633603.57960831, 12347334.82483679, 0.00127345, 0.00146667, 0.00057292, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24075, 33.60197033, 0.00062491, 40.721881, 0.05001202, 4.0721881, 0.13245608, -33.60197033, -0.00062491, -40.721881, -0.05001202, -4.0721881, -0.13245608, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14075, 56.89741124, 0.00051045, 68.95338539, 0.05946997, 6.89533854, 0.15946997, -56.89741124, -0.00051045, -68.95338539, -0.05946997, -6.89533854, -0.15946997, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24075, 4075, 0.0, 122.2308951, 0.01249827, 122.2308951, 0.0374948, 85.56162657, -3850.7383938, 0.05, 2, 0, 72004, 24030, 2, 3)
    ops.uniaxialMaterial('LimitState', 44075, 30.55772377, 4.306e-05, 91.67317132, 0.00012919, 305.57723774, 0.00043062, -30.55772377, -4.306e-05, -91.67317132, -0.00012919, -305.57723774, -0.00043062, 0.4, 0.3, 0.003, 0.0, 0.0, 24075, 2)
    ops.limitCurve('ThreePoint', 14075, 4075, 0.0, 195.56943215, 0.01020908, 195.56943215, 0.03062725, 136.89860251, -7629.74419536, 0.05, 2, 0, 72004, 24030, 1, 3)
    ops.uniaxialMaterial('LimitState', 34075, 48.89235804, 6.89e-05, 146.67707411, 0.0002067, 488.92358038, 0.000689, -48.89235804, -6.89e-05, -146.67707411, -0.0002067, -488.92358038, -0.000689, 0.4, 0.3, 0.003, 0.0, 0.0, 14075, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4075, 99999, 'P', 44075, 'Vy', 34075, 'Vz', 24075, 'My', 14075, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172004, 72004, 172004, 4075, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124030, 124030, 24030, 4075, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174030, 13.45, 0.0, 7.45)
    ops.node(123004, 13.45, 0.0, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4076, 174030, 123004, 0.1, 28899976.44893827, 12041656.85372428, 0.00127345, 0.00146667, 0.00057292, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24076, 40.99637935, 0.00064455, 49.82092594, 0.0553143, 4.98209259, 0.13957186, -40.99637935, -0.00064455, -49.82092594, -0.0553143, -4.98209259, -0.13957186, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14076, 63.41542061, 0.0005207, 77.06570735, 0.06578677, 7.70657074, 0.16578677, -63.41542061, -0.0005207, -77.06570735, -0.06578677, -7.70657074, -0.16578677, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24076, 4076, 0.0, 127.77834125, 0.01289091, 127.77834125, 0.03867272, 89.44483888, -5516.14967965, 0.05, 2, 0, 74030, 23004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44076, 31.94458531, 4.616e-05, 95.83375594, 0.00013848, 319.44585313, 0.00046159, -31.94458531, -4.616e-05, -95.83375594, -0.00013848, -319.44585313, -0.00046159, 0.4, 0.3, 0.003, 0.0, 0.0, 24076, 2)
    ops.limitCurve('ThreePoint', 14076, 4076, 0.0, 204.445346, 0.010414, 204.445346, 0.03124199, 143.1117422, -11700.50934518, 0.05, 2, 0, 74030, 23004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34076, 51.1113365, 7.386e-05, 153.3340095, 0.00022157, 511.11336501, 0.00073855, -51.1113365, -7.386e-05, -153.3340095, -0.00022157, -511.11336501, -0.00073855, 0.4, 0.3, 0.003, 0.0, 0.0, 14076, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4076, 99999, 'P', 44076, 'Vy', 34076, 'Vz', 24076, 'My', 14076, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174030, 74030, 174030, 4076, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123004, 123004, 23004, 4076, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173003, 10.6, 0.0, 8.975)
    ops.node(124031, 10.6, 0.0, 9.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4078, 173003, 124031, 0.1, 25827459.38603004, 10761441.41084585, 0.00127345, 0.00146667, 0.00057292, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24078, 27.48528979, 0.00061773, 33.70104338, 0.03491132, 3.37010434, 0.08519352, -27.48528979, -0.00061773, -33.70104338, -0.03491132, -3.37010434, -0.08519352, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14078, 46.62292988, 0.00051212, 57.16662965, 0.04066605, 5.71666296, 0.11376964, -46.62292988, -0.00051212, -57.16662965, -0.04066605, -5.71666296, -0.11376964, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24078, 4078, 0.0, 80.13916266, 0.01235467, 80.13916266, 0.037064, 56.09741386, -2676.44833992, 0.05, 2, 0, 73003, 24031, 2, 3)
    ops.uniaxialMaterial('LimitState', 44078, 20.03479067, 3.239e-05, 60.104372, 9.718e-05, 200.34790666, 0.00032394, -20.03479067, -3.239e-05, -60.104372, -9.718e-05, -200.34790666, -0.00032394, 0.4, 0.3, 0.003, 0.0, 0.0, 24078, 2)
    ops.limitCurve('ThreePoint', 14078, 4078, 0.0, 128.22266026, 0.01024237, 128.22266026, 0.03072711, 89.75586218, -5711.53256569, 0.05, 2, 0, 73003, 24031, 1, 3)
    ops.uniaxialMaterial('LimitState', 34078, 32.05566507, 5.183e-05, 96.1669952, 0.00015549, 320.55665065, 0.0005183, -32.05566507, -5.183e-05, -96.1669952, -0.00015549, -320.55665065, -0.0005183, 0.4, 0.3, 0.003, 0.0, 0.0, 14078, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4078, 99999, 'P', 44078, 'Vy', 34078, 'Vz', 24078, 'My', 14078, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173003, 73003, 173003, 4078, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124031, 124031, 24031, 4078, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174031, 10.6, 0.0, 10.35)
    ops.node(124003, 10.6, 0.0, 11.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4079, 174031, 124003, 0.1, 29523567.54510473, 12301486.47712697, 0.00127345, 0.00146667, 0.00057292, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24079, 25.03618512, 0.00058925, 30.49074095, 0.03350817, 3.0490741, 0.08730493, -25.03618512, -0.00058925, -30.49074095, -0.03350817, -3.0490741, -0.08730493, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14079, 42.76675659, 0.00049392, 52.08421692, 0.03903827, 5.20842169, 0.11725156, -42.76675659, -0.00049392, -52.08421692, -0.03903827, -5.20842169, -0.11725156, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24079, 4079, 0.0, 86.17447436, 0.01178493, 86.17447436, 0.0353548, 60.32213205, -3861.04302294, 0.05, 2, 0, 74031, 24003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44079, 21.54361859, 3.047e-05, 64.63085577, 9.142e-05, 215.43618589, 0.00030473, -21.54361859, -3.047e-05, -64.63085577, -9.142e-05, -215.43618589, -0.00030473, 0.4, 0.3, 0.003, 0.0, 0.0, 24079, 2)
    ops.limitCurve('ThreePoint', 14079, 4079, 0.0, 137.87915897, 0.00987835, 137.87915897, 0.02963504, 96.51541128, -8952.76201688, 0.05, 2, 0, 74031, 24003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34079, 34.46978974, 4.876e-05, 103.40936923, 0.00014627, 344.69789742, 0.00048756, -34.46978974, -4.876e-05, -103.40936923, -0.00014627, -344.69789742, -0.00048756, 0.4, 0.3, 0.003, 0.0, 0.0, 14079, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4079, 99999, 'P', 44079, 'Vy', 34079, 'Vz', 24079, 'My', 14079, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174031, 74031, 174031, 4079, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124003, 124003, 24003, 4079, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173004, 13.45, 0.0, 8.975)
    ops.node(124032, 13.45, 0.0, 9.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4080, 173004, 124032, 0.1, 28736000.2699788, 11973333.4458245, 0.00127345, 0.00146667, 0.00057292, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24080, 26.07501482, 0.00061604, 31.78285688, 0.03472838, 3.17828569, 0.08645228, -26.07501482, -0.00061604, -31.78285688, -0.03472838, -3.17828569, -0.08645228, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14080, 44.80229978, 0.00050431, 54.60955982, 0.04044602, 5.46095598, 0.11564564, -44.80229978, -0.00050431, -54.60955982, -0.04044602, -5.46095598, -0.11564564, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24080, 4080, 0.0, 88.71103076, 0.01232083, 88.71103076, 0.03696249, 62.09772153, -2629.48764926, 0.05, 2, 0, 73004, 24032, 2, 3)
    ops.uniaxialMaterial('LimitState', 44080, 22.17775769, 3.223e-05, 66.53327307, 9.669e-05, 221.77757691, 0.00032229, -22.17775769, -3.223e-05, -66.53327307, -9.669e-05, -221.77757691, -0.00032229, 0.4, 0.3, 0.003, 0.0, 0.0, 24080, 2)
    ops.limitCurve('ThreePoint', 14080, 4080, 0.0, 141.93764922, 0.01008613, 141.93764922, 0.0302584, 99.35635445, -5601.81701048, 0.05, 2, 0, 73004, 24032, 1, 3)
    ops.uniaxialMaterial('LimitState', 34080, 35.48441231, 5.157e-05, 106.45323692, 0.0001547, 354.84412305, 0.00051567, -35.48441231, -5.157e-05, -106.45323692, -0.0001547, -354.84412305, -0.00051567, 0.4, 0.3, 0.003, 0.0, 0.0, 14080, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4080, 99999, 'P', 44080, 'Vy', 34080, 'Vz', 24080, 'My', 14080, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173004, 73004, 173004, 4080, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124032, 124032, 24032, 4080, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174032, 13.45, 0.0, 10.35)
    ops.node(124004, 13.45, 0.0, 11.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4081, 174032, 124004, 0.1, 29023520.9762869, 12093133.74011954, 0.00127345, 0.00146667, 0.00057292, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24081, 24.47632631, 0.00058136, 29.84883989, 0.03383387, 2.98488399, 0.08754597, -24.47632631, -0.00058136, -29.84883989, -0.03383387, -2.98488399, -0.08754597, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14081, 41.81022134, 0.00048893, 50.98749651, 0.03942388, 5.09874965, 0.11751408, -41.81022134, -0.00048893, -50.98749651, -0.03942388, -5.09874965, -0.11751408, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24081, 4081, 0.0, 85.34589994, 0.01162718, 85.34589994, 0.03488153, 59.74212995, -4055.9688233, 0.05, 2, 0, 74032, 24004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44081, 21.33647498, 3.07e-05, 64.00942495, 9.21e-05, 213.36474984, 0.000307, -21.33647498, -3.07e-05, -64.00942495, -9.21e-05, -213.36474984, -0.000307, 0.4, 0.3, 0.003, 0.0, 0.0, 24081, 2)
    ops.limitCurve('ThreePoint', 14081, 4081, 0.0, 136.5534399, 0.00977856, 136.5534399, 0.02933567, 95.58740793, -9427.9732768, 0.05, 2, 0, 74032, 24004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34081, 34.13835997, 4.912e-05, 102.41507992, 0.00014736, 341.38359974, 0.00049119, -34.13835997, -4.912e-05, -102.41507992, -0.00014736, -341.38359974, -0.00049119, 0.4, 0.3, 0.003, 0.0, 0.0, 14081, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4081, 99999, 'P', 44081, 'Vy', 34081, 'Vz', 24081, 'My', 14081, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174032, 74032, 174032, 4081, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124004, 124004, 24004, 4081, '-orient', 0, 0, 1, 0, 1, 0)
