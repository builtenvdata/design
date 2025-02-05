import openseespy.opensees as ops


def add_columns() -> None:
    """Add components of all columns to ops domain (plastic hinges, column elements and nodes)
    """
    # Create elastic column element nodes
    ops.node(170003, 7.9, 0.0, 0.0)
    ops.node(121003, 7.9, 0.0, 3.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3, 170003, 121003, 0.12, 24520856.79682912, 10217023.66534547, 0.00194385, 0.00176, 0.00099, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20003, 80.43441646, 0.00083147, 97.55691579, 0.04208477, 9.75569158, 0.1012998, -80.43441646, -0.00083147, -97.55691579, -0.04208477, -9.75569158, -0.1012998, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10003, 86.2538813, 0.00067372, 104.61520087, 0.04659688, 10.46152009, 0.1229642, -86.2538813, -0.00067372, -104.61520087, -0.04659688, -10.46152009, -0.1229642, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20003, 3, 0.0, 127.48173065, 0.01662949, 127.48173065, 0.04988847, 89.23721146, -1676.86585619, 0.05, 2, 0, 70003, 21003, 2, 3)
    ops.uniaxialMaterial('LimitState', 40003, 31.87043266, 0.00010918, 95.61129799, 0.00032753, 318.70432663, 0.00109177, -31.87043266, -0.00010918, -95.61129799, -0.00032753, -318.70432663, -0.00109177, 0.4, 0.3, 0.003, 0.0, 0.0, 20003, 2)
    ops.limitCurve('ThreePoint', 10003, 3, 0.0, 148.11683622, 0.01347442, 148.11683622, 0.04042325, 103.68178536, -2369.41498836, 0.05, 2, 0, 70003, 21003, 1, 3)
    ops.uniaxialMaterial('LimitState', 30003, 37.02920906, 0.00012685, 111.08762717, 0.00038055, 370.29209056, 0.00126849, -37.02920906, -0.00012685, -111.08762717, -0.00038055, -370.29209056, -0.00126849, 0.4, 0.3, 0.003, 0.0, 0.0, 10003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3, 99999, 'P', 40003, 'Vy', 30003, 'Vz', 20003, 'My', 10003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170003, 70003, 170003, 3, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121003, 121003, 21003, 3, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170004, 12.9, 0.0, 0.0)
    ops.node(121004, 12.9, 0.0, 3.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4, 170004, 121004, 0.075, 29540107.76323263, 12308378.23468026, 0.00077515, 0.00061875, 0.00042969, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20004, 32.71094079, 0.00093424, 39.53760007, 0.02364007, 3.95376001, 0.06880593, -32.71094079, -0.00093424, -39.53760007, -0.02364007, -3.95376001, -0.06880593, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10004, 37.10511936, 0.00079788, 44.84882838, 0.02491189, 4.48488284, 0.07700718, -37.10511936, -0.00079788, -44.84882838, -0.02491189, -4.48488284, -0.07700718, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20004, 4, 0.0, 75.81393875, 0.01868486, 75.81393875, 0.05605459, 53.06975712, -657.27121439, 0.05, 2, 0, 70004, 21004, 2, 3)
    ops.uniaxialMaterial('LimitState', 40004, 18.95348469, 8.623e-05, 56.86045406, 0.0002587, 189.53484687, 0.00086234, -18.95348469, -8.623e-05, -56.86045406, -0.0002587, -189.53484687, -0.00086234, 0.4, 0.3, 0.003, 0.0, 0.0, 20004, 2)
    ops.limitCurve('ThreePoint', 10004, 4, 0.0, 80.73311818, 0.01595758, 80.73311818, 0.04787275, 56.51318273, -786.11044618, 0.05, 2, 0, 70004, 21004, 1, 3)
    ops.uniaxialMaterial('LimitState', 30004, 20.18327954, 9.183e-05, 60.54983863, 0.00027549, 201.83279545, 0.00091829, -20.18327954, -9.183e-05, -60.54983863, -0.00027549, -201.83279545, -0.00091829, 0.4, 0.3, 0.003, 0.0, 0.0, 10004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4, 99999, 'P', 40004, 'Vy', 30004, 'Vz', 20004, 'My', 10004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170004, 70004, 170004, 4, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121004, 121004, 21004, 4, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170005, 0.0, 4.05, 0.0)
    ops.node(121005, 0.0, 4.05, 3.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 5, 170005, 121005, 0.075, 28785177.65048363, 11993824.02103484, 0.00077515, 0.00042969, 0.00061875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20005, 41.72755191, 0.00086611, 50.37287855, 0.01811002, 5.03728785, 0.06527732, -41.72755191, -0.00086611, -50.37287855, -0.01811002, -5.03728785, -0.06527732, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10005, 36.45944847, 0.00102488, 44.01330262, 0.0172618, 4.40133026, 0.05815516, -36.45944847, -0.00102488, -44.01330262, -0.0172618, -4.40133026, -0.05815516, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20005, 5, 0.0, 73.35579723, 0.01732214, 73.35579723, 0.05196643, 51.34905806, -612.21958437, 0.05, 2, 0, 70005, 21005, 2, 3)
    ops.uniaxialMaterial('LimitState', 40005, 18.33894931, 8.563e-05, 55.01684792, 0.00025688, 183.38949307, 0.00085626, -18.33894931, -8.563e-05, -55.01684792, -0.00025688, -183.38949307, -0.00085626, 0.4, 0.3, 0.003, 0.0, 0.0, 20005, 2)
    ops.limitCurve('ThreePoint', 10005, 5, 0.0, 58.95848413, 0.02049755, 58.95848413, 0.06149265, 41.27093889, -537.83060823, 0.05, 2, 0, 70005, 21005, 1, 3)
    ops.uniaxialMaterial('LimitState', 30005, 14.73962103, 6.882e-05, 44.2188631, 0.00020646, 147.39621033, 0.0006882, -14.73962103, -6.882e-05, -44.2188631, -0.00020646, -147.39621033, -0.0006882, 0.4, 0.3, 0.003, 0.0, 0.0, 10005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 5, 99999, 'P', 40005, 'Vy', 30005, 'Vz', 20005, 'My', 10005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170005, 70005, 170005, 5, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121005, 121005, 21005, 5, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170006, 2.9, 4.05, 0.0)
    ops.node(121006, 2.9, 4.05, 3.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 6, 170006, 121006, 0.1575, 28686608.45040868, 11952753.52100362, 0.00337604, 0.00176859, 0.00292359, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20006, 146.52207877, 0.00065901, 177.360658, 0.05592142, 17.7360658, 0.13870228, -146.52207877, -0.00065901, -177.360658, -0.05592142, -17.7360658, -0.13870228, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10006, 140.66767033, 0.00078508, 170.27406912, 0.05119475, 17.02740691, 0.11775973, -140.66767033, -0.00078508, -170.27406912, -0.05119475, -17.02740691, -0.11775973, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20006, 6, 0.0, 231.52267586, 0.01318029, 231.52267586, 0.03954087, 162.0658731, -3947.73810876, 0.05, 2, 0, 70006, 21006, 2, 3)
    ops.uniaxialMaterial('LimitState', 40006, 57.88066896, 0.00012913, 173.64200689, 0.0003874, 578.80668964, 0.00129132, -57.88066896, -0.00012913, -173.64200689, -0.0003874, -578.80668964, -0.00129132, 0.4, 0.3, 0.003, 0.0, 0.0, 20006, 2)
    ops.limitCurve('ThreePoint', 10006, 6, 0.0, 203.08537938, 0.01570153, 203.08537938, 0.0471046, 142.15976557, -2836.95984601, 0.05, 2, 0, 70006, 21006, 1, 3)
    ops.uniaxialMaterial('LimitState', 30006, 50.77134485, 0.00011327, 152.31403454, 0.00033981, 507.71344845, 0.00113271, -50.77134485, -0.00011327, -152.31403454, -0.00033981, -507.71344845, -0.00113271, 0.4, 0.3, 0.003, 0.0, 0.0, 10006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 6, 99999, 'P', 40006, 'Vy', 30006, 'Vz', 20006, 'My', 10006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170006, 70006, 170006, 6, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121006, 121006, 21006, 6, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170007, 7.9, 4.05, 0.0)
    ops.node(121007, 7.9, 4.05, 3.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 7, 170007, 121007, 0.175, 28078584.09733596, 11699410.04055665, 0.00405757, 0.0019651, 0.00401042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20007, 181.25744707, 0.00059274, 219.64867885, 0.05651152, 21.96486788, 0.13813456, -181.25744707, -0.00059274, -219.64867885, -0.05651152, -21.96486788, -0.13813456, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10007, 163.38073665, 0.00074959, 197.98559196, 0.0498831, 19.7985592, 0.10993805, -163.38073665, -0.00074959, -197.98559196, -0.0498831, -19.7985592, -0.10993805, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20007, 7, 0.0, 228.36508358, 0.01185473, 228.36508358, 0.03556419, 159.85555851, -3407.45945286, 0.05, 2, 0, 70007, 21007, 2, 3)
    ops.uniaxialMaterial('LimitState', 40007, 57.0912709, 0.00011712, 171.27381269, 0.00035135, 570.91270896, 0.00117116, -57.0912709, -0.00011712, -171.27381269, -0.00035135, -570.91270896, -0.00117116, 0.4, 0.3, 0.003, 0.0, 0.0, 20007, 2)
    ops.limitCurve('ThreePoint', 10007, 7, 0.0, 193.26541918, 0.01499178, 193.26541918, 0.04497533, 135.28579342, -2213.43329404, 0.05, 2, 0, 70007, 21007, 1, 3)
    ops.uniaxialMaterial('LimitState', 30007, 48.31635479, 9.912e-05, 144.94906438, 0.00029735, 483.16354794, 0.00099115, -48.31635479, -9.912e-05, -144.94906438, -0.00029735, -483.16354794, -0.00099115, 0.4, 0.3, 0.003, 0.0, 0.0, 10007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 7, 99999, 'P', 40007, 'Vy', 30007, 'Vz', 20007, 'My', 10007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170007, 70007, 170007, 7, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121007, 121007, 21007, 7, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170008, 12.9, 4.05, 0.0)
    ops.node(121008, 12.9, 4.05, 3.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 8, 170008, 121008, 0.12, 27119536.29249544, 11299806.78853977, 0.00194385, 0.00099, 0.00176, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20008, 88.81042021, 0.0006753, 107.6940713, 0.0388691, 10.76940713, 0.10135878, -88.81042021, -0.0006753, -107.6940713, -0.0388691, -10.76940713, -0.10135878, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10008, 82.87697273, 0.00083204, 100.49900213, 0.03537207, 10.04990021, 0.08460082, -82.87697273, -0.00083204, -100.49900213, -0.03537207, -10.04990021, -0.08460082, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20008, 8, 0.0, 138.98168091, 0.01350599, 138.98168091, 0.04051796, 97.28717664, -1794.15346267, 0.05, 2, 0, 70008, 21008, 2, 3)
    ops.uniaxialMaterial('LimitState', 40008, 34.74542023, 0.00010762, 104.23626068, 0.00032286, 347.45420227, 0.0010762, -34.74542023, -0.00010762, -104.23626068, -0.00032286, -347.45420227, -0.0010762, 0.4, 0.3, 0.003, 0.0, 0.0, 20008, 2)
    ops.limitCurve('ThreePoint', 10008, 8, 0.0, 122.65942268, 0.01664077, 122.65942268, 0.0499223, 85.86159587, -1304.86509872, 0.05, 2, 0, 70008, 21008, 1, 3)
    ops.uniaxialMaterial('LimitState', 30008, 30.66485567, 9.498e-05, 91.99456701, 0.00028494, 306.64855669, 0.00094981, -30.66485567, -9.498e-05, -91.99456701, -0.00028494, -306.64855669, -0.00094981, 0.4, 0.3, 0.003, 0.0, 0.0, 10008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 8, 99999, 'P', 40008, 'Vy', 30008, 'Vz', 20008, 'My', 10008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170008, 70008, 170008, 8, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121008, 121008, 21008, 8, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170009, 0.0, 8.1, 0.0)
    ops.node(121009, 0.0, 8.1, 3.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 9, 170009, 121009, 0.075, 30019199.04575292, 12507999.60239705, 0.00077515, 0.00042969, 0.00061875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20009, 38.31926454, 0.0008536, 46.24752733, 0.02282561, 4.62475273, 0.0747664, -38.31926454, -0.0008536, -46.24752733, -0.02282561, -4.62475273, -0.0747664, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10009, 33.4092144, 0.00101353, 40.32158692, 0.02170244, 4.03215869, 0.06673435, -33.4092144, -0.00101353, -40.32158692, -0.02170244, -4.03215869, -0.06673435, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20009, 9, 0.0, 77.58652948, 0.01707198, 77.58652948, 0.05121594, 54.31057064, -659.269218, 0.05, 2, 0, 70009, 21009, 2, 3)
    ops.uniaxialMaterial('LimitState', 40009, 19.39663237, 8.684e-05, 58.18989711, 0.00026052, 193.9663237, 0.00086841, -19.39663237, -8.684e-05, -58.18989711, -0.00026052, -193.9663237, -0.00086841, 0.4, 0.3, 0.003, 0.0, 0.0, 20009, 2)
    ops.limitCurve('ThreePoint', 10009, 9, 0.0, 73.49716684, 0.02027068, 73.49716684, 0.06081203, 51.44801679, -563.82465619, 0.05, 2, 0, 70009, 21009, 1, 3)
    ops.uniaxialMaterial('LimitState', 30009, 18.37429171, 8.226e-05, 55.12287513, 0.00024679, 183.74291711, 0.00082264, -18.37429171, -8.226e-05, -55.12287513, -0.00024679, -183.74291711, -0.00082264, 0.4, 0.3, 0.003, 0.0, 0.0, 10009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 9, 99999, 'P', 40009, 'Vy', 30009, 'Vz', 20009, 'My', 10009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170009, 70009, 170009, 9, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121009, 121009, 21009, 9, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170010, 2.9, 8.1, 0.0)
    ops.node(121010, 2.9, 8.1, 3.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 10, 170010, 121010, 0.12, 27861078.81376244, 11608782.83906768, 0.00194385, 0.00099, 0.00176, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20010, 100.59683339, 0.00064313, 121.75417041, 0.05692852, 12.17541704, 0.14576608, -100.59683339, -0.00064313, -121.75417041, -0.05692852, -12.17541704, -0.14576608, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10010, 89.94400635, 0.00078931, 108.8608608, 0.05135112, 10.88608608, 0.12023554, -89.94400635, -0.00078931, -108.8608608, -0.05135112, -10.88608608, -0.12023554, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20010, 10, 0.0, 175.7262379, 0.01286256, 175.7262379, 0.03858768, 123.00836653, -2891.53637101, 0.05, 2, 0, 70010, 21010, 2, 3)
    ops.uniaxialMaterial('LimitState', 40010, 43.93155947, 0.00013245, 131.79467842, 0.00039736, 439.31559475, 0.00132452, -43.93155947, -0.00013245, -131.79467842, -0.00039736, -439.31559475, -0.00132452, 0.4, 0.3, 0.003, 0.0, 0.0, 20010, 2)
    ops.limitCurve('ThreePoint', 10010, 10, 0.0, 151.3221004, 0.0157862, 151.3221004, 0.04735859, 105.92547028, -2016.88562817, 0.05, 2, 0, 70010, 21010, 1, 3)
    ops.uniaxialMaterial('LimitState', 30010, 37.8305251, 0.00011406, 113.4915753, 0.00034217, 378.30525099, 0.00114057, -37.8305251, -0.00011406, -113.4915753, -0.00034217, -378.30525099, -0.00114057, 0.4, 0.3, 0.003, 0.0, 0.0, 10010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 10, 99999, 'P', 40010, 'Vy', 30010, 'Vz', 20010, 'My', 10010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170010, 70010, 170010, 10, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121010, 121010, 21010, 10, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170011, 7.9, 8.1, 0.0)
    ops.node(121011, 7.9, 8.1, 3.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 11, 170011, 121011, 0.175, 27618803.2028485, 11507834.66785354, 0.00405757, 0.0019651, 0.00401042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20011, 178.59976901, 0.00058468, 216.55505216, 0.05634867, 21.65550522, 0.13663861, -178.59976901, -0.00058468, -216.55505216, -0.05634867, -21.65550522, -0.13663861, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10011, 161.71610293, 0.00073646, 196.08333929, 0.04973395, 19.60833393, 0.10880806, -161.71610293, -0.00073646, -196.08333929, -0.04973395, -19.60833393, -0.10880806, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20011, 11, 0.0, 227.05406743, 0.01169362, 227.05406743, 0.03508086, 158.9378472, -3446.90385363, 0.05, 2, 0, 70011, 21011, 2, 3)
    ops.uniaxialMaterial('LimitState', 40011, 56.76351686, 0.00011838, 170.29055057, 0.00035515, 567.63516858, 0.00118382, -56.76351686, -0.00011838, -170.29055057, -0.00035515, -567.63516858, -0.00118382, 0.4, 0.3, 0.003, 0.0, 0.0, 20011, 2)
    ops.limitCurve('ThreePoint', 10011, 11, 0.0, 191.64120111, 0.01472911, 191.64120111, 0.04418733, 134.14884077, -2235.67852628, 0.05, 2, 0, 70011, 21011, 1, 3)
    ops.uniaxialMaterial('LimitState', 30011, 47.91030028, 9.992e-05, 143.73090083, 0.00029976, 479.10300277, 0.00099919, -47.91030028, -9.992e-05, -143.73090083, -0.00029976, -479.10300277, -0.00099919, 0.4, 0.3, 0.003, 0.0, 0.0, 10011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 11, 99999, 'P', 40011, 'Vy', 30011, 'Vz', 20011, 'My', 10011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170011, 70011, 170011, 11, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121011, 121011, 21011, 11, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170012, 12.9, 8.1, 0.0)
    ops.node(121012, 12.9, 8.1, 3.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 12, 170012, 121012, 0.12, 30032422.4676846, 12513509.36153525, 0.00194385, 0.00099, 0.00176, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20012, 87.36275731, 0.00064322, 105.47528452, 0.03708399, 10.54752845, 0.10601195, -87.36275731, -0.00064322, -105.47528452, -0.03708399, -10.54752845, -0.10601195, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10012, 80.5074815, 0.00079002, 97.19873523, 0.03374472, 9.71987352, 0.08804548, -80.5074815, -0.00079002, -97.19873523, -0.03374472, -9.71987352, -0.08804548, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20012, 12, 0.0, 141.02890317, 0.01286443, 141.02890317, 0.0385933, 98.72023222, -1533.86891778, 0.05, 2, 0, 70012, 21012, 2, 3)
    ops.uniaxialMaterial('LimitState', 40012, 35.25722579, 9.861e-05, 105.77167738, 0.00029584, 352.57225793, 0.00098614, -35.25722579, -9.861e-05, -105.77167738, -0.00029584, -352.57225793, -0.00098614, 0.4, 0.3, 0.003, 0.0, 0.0, 20012, 2)
    ops.limitCurve('ThreePoint', 10012, 12, 0.0, 126.79637154, 0.01580035, 126.79637154, 0.04740104, 88.75746008, -1137.59882439, 0.05, 2, 0, 70012, 21012, 1, 3)
    ops.uniaxialMaterial('LimitState', 30012, 31.69909289, 8.866e-05, 95.09727866, 0.00026598, 316.99092886, 0.00088662, -31.69909289, -8.866e-05, -95.09727866, -0.00026598, -316.99092886, -0.00088662, 0.4, 0.3, 0.003, 0.0, 0.0, 10012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 12, 99999, 'P', 40012, 'Vy', 30012, 'Vz', 20012, 'My', 10012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170012, 70012, 170012, 12, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121012, 121012, 21012, 12, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170013, 0.0, 12.15, 0.0)
    ops.node(121013, 0.0, 12.15, 3.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 13, 170013, 121013, 0.075, 29402989.7337582, 12251245.72239925, 0.00077515, 0.00042969, 0.00061875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20013, 37.71418354, 0.00075155, 45.57035414, 0.02249163, 4.55703541, 0.07349746, -37.71418354, -0.00075155, -45.57035414, -0.02249163, -4.55703541, -0.07349746, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10013, 33.50925731, 0.00087042, 40.48950763, 0.02134094, 4.04895076, 0.06556225, -33.50925731, -0.00087042, -40.48950763, -0.02134094, -4.04895076, -0.06556225, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20013, 13, 0.0, 77.52030266, 0.01503102, 77.52030266, 0.04509305, 54.26421186, -692.26945258, 0.05, 2, 0, 70013, 21013, 2, 3)
    ops.uniaxialMaterial('LimitState', 40013, 19.38007566, 8.859e-05, 58.14022699, 0.00026576, 193.80075664, 0.00088586, -19.38007566, -8.859e-05, -58.14022699, -0.00026576, -193.80075664, -0.00088586, 0.4, 0.3, 0.003, 0.0, 0.0, 20013, 2)
    ops.limitCurve('ThreePoint', 10013, 13, 0.0, 71.22853424, 0.01740845, 71.22853424, 0.05222536, 49.85997397, -589.22570818, 0.05, 2, 0, 70013, 21013, 1, 3)
    ops.uniaxialMaterial('LimitState', 30013, 17.80713356, 8.14e-05, 53.42140068, 0.00024419, 178.0713356, 0.00081396, -17.80713356, -8.14e-05, -53.42140068, -0.00024419, -178.0713356, -0.00081396, 0.4, 0.3, 0.003, 0.0, 0.0, 10013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 13, 99999, 'P', 40013, 'Vy', 30013, 'Vz', 20013, 'My', 10013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170013, 70013, 170013, 13, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121013, 121013, 21013, 13, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170014, 2.9, 12.15, 0.0)
    ops.node(121014, 2.9, 12.15, 3.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 14, 170014, 121014, 0.12, 26444976.34040719, 11018740.14183633, 0.00194385, 0.00099, 0.00176, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20014, 106.86299789, 0.00077518, 129.48274708, 0.05465497, 12.94827471, 0.13787613, -106.86299789, -0.00077518, -129.48274708, -0.05465497, -12.94827471, -0.13787613, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10014, 92.14578848, 0.00099554, 111.6503379, 0.04939637, 11.16503379, 0.11392585, -92.14578848, -0.00099554, -111.6503379, -0.04939637, -11.16503379, -0.11392585, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20014, 14, 0.0, 165.73750696, 0.01550352, 165.73750696, 0.04651056, 116.01625487, -2698.28154795, 0.05, 2, 0, 70014, 21014, 2, 3)
    ops.uniaxialMaterial('LimitState', 40014, 41.43437674, 0.00013161, 124.30313022, 0.00039484, 414.34376739, 0.00131612, -41.43437674, -0.00013161, -124.30313022, -0.00039484, -414.34376739, -0.00131612, 0.4, 0.3, 0.003, 0.0, 0.0, 20014, 2)
    ops.limitCurve('ThreePoint', 10014, 14, 0.0, 142.59169064, 0.01991077, 142.59169064, 0.05973232, 99.81418345, -1895.62129535, 0.05, 2, 0, 70014, 21014, 1, 3)
    ops.uniaxialMaterial('LimitState', 30014, 35.64792266, 0.00011323, 106.94376798, 0.0003397, 356.4792266, 0.00113232, -35.64792266, -0.00011323, -106.94376798, -0.0003397, -356.4792266, -0.00113232, 0.4, 0.3, 0.003, 0.0, 0.0, 10014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 14, 99999, 'P', 40014, 'Vy', 30014, 'Vz', 20014, 'My', 10014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170014, 70014, 170014, 14, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121014, 121014, 21014, 14, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170015, 7.9, 12.15, 0.0)
    ops.node(121015, 7.9, 12.15, 3.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 15, 170015, 121015, 0.175, 29299777.32280904, 12208240.55117043, 0.00405757, 0.0019651, 0.00401042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20015, 193.03274775, 0.00060566, 233.46210579, 0.05709041, 23.34621058, 0.14191783, -193.03274775, -0.00060566, -233.46210579, -0.05709041, -23.34621058, -0.14191783, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10015, 177.41313207, 0.00076101, 214.57107093, 0.05039181, 21.45710709, 0.11280441, -177.41313207, -0.00076101, -214.57107093, -0.05039181, -21.45710709, -0.11280441, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20015, 15, 0.0, 238.70989268, 0.01211318, 238.70989268, 0.03633954, 167.09692488, -3559.2097201, 0.05, 2, 0, 70015, 21015, 2, 3)
    ops.uniaxialMaterial('LimitState', 40015, 59.67747317, 0.00011732, 179.03241951, 0.00035196, 596.77473171, 0.00117319, -59.67747317, -0.00011732, -179.03241951, -0.00035196, -596.77473171, -0.00117319, 0.4, 0.3, 0.003, 0.0, 0.0, 20015, 2)
    ops.limitCurve('ThreePoint', 10015, 15, 0.0, 202.41496537, 0.01522023, 202.41496537, 0.04566069, 141.69047576, -2298.924799, 0.05, 2, 0, 70015, 21015, 1, 3)
    ops.uniaxialMaterial('LimitState', 30015, 50.60374134, 9.948e-05, 151.81122403, 0.00029844, 506.03741342, 0.00099481, -50.60374134, -9.948e-05, -151.81122403, -0.00029844, -506.03741342, -0.00099481, 0.4, 0.3, 0.003, 0.0, 0.0, 10015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 15, 99999, 'P', 40015, 'Vy', 30015, 'Vz', 20015, 'My', 10015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170015, 70015, 170015, 15, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121015, 121015, 21015, 15, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170016, 12.9, 12.15, 0.0)
    ops.node(121016, 12.9, 12.15, 3.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 16, 170016, 121016, 0.12, 26940871.1526863, 11225362.98028596, 0.00194385, 0.00099, 0.00176, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20016, 88.00982312, 0.00068658, 106.74016928, 0.03556368, 10.67401693, 0.09758163, -88.00982312, -0.00068658, -106.74016928, -0.03556368, -10.67401693, -0.09758163, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10016, 80.94598592, 0.00085347, 98.17299857, 0.0323941, 9.81729986, 0.08125122, -80.94598592, -0.00085347, -98.17299857, -0.0323941, -9.81729986, -0.08125122, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20016, 16, 0.0, 128.09850093, 0.01373154, 128.09850093, 0.04119463, 89.66895065, -1477.39233271, 0.05, 2, 0, 70016, 21016, 2, 3)
    ops.uniaxialMaterial('LimitState', 40016, 32.02462523, 9.985e-05, 96.0738757, 0.00029955, 320.24625234, 0.00099851, -32.02462523, -9.985e-05, -96.0738757, -0.00029955, -320.24625234, -0.00099851, 0.4, 0.3, 0.003, 0.0, 0.0, 20016, 2)
    ops.limitCurve('ThreePoint', 10016, 16, 0.0, 114.34230672, 0.01706932, 114.34230672, 0.05120796, 80.0396147, -1101.0767278, 0.05, 2, 0, 70016, 21016, 1, 3)
    ops.uniaxialMaterial('LimitState', 30016, 28.58557668, 8.913e-05, 85.75673004, 0.00026738, 285.85576679, 0.00089128, -28.58557668, -8.913e-05, -85.75673004, -0.00026738, -285.85576679, -0.00089128, 0.4, 0.3, 0.003, 0.0, 0.0, 10016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 16, 99999, 'P', 40016, 'Vy', 30016, 'Vz', 20016, 'My', 10016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170016, 70016, 170016, 16, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121016, 121016, 21016, 16, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170017, 0.0, 16.2, 0.0)
    ops.node(121017, 0.0, 16.2, 3.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 17, 170017, 121017, 0.0625, 31363558.90270912, 13068149.54279547, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20017, 22.14881695, 0.00092766, 26.7032649, 0.02081467, 2.67032649, 0.07782656, -22.14881695, -0.00092766, -26.7032649, -0.02081467, -2.67032649, -0.07782656, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10017, 22.14881695, 0.00092766, 26.7032649, 0.02081467, 2.67032649, 0.07782656, -22.14881695, -0.00092766, -26.7032649, -0.02081467, -2.67032649, -0.07782656, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20017, 17, 0.0, 58.09266758, 0.01855317, 58.09266758, 0.05565951, 40.66486731, -525.96612292, 0.05, 2, 0, 70017, 21017, 2, 3)
    ops.uniaxialMaterial('LimitState', 40017, 14.52316689, 7.468e-05, 43.56950068, 0.00022405, 145.23166895, 0.00074682, -14.52316689, -7.468e-05, -43.56950068, -0.00022405, -145.23166895, -0.00074682, 0.4, 0.3, 0.003, 0.0, 0.0, 20017, 2)
    ops.limitCurve('ThreePoint', 10017, 17, 0.0, 58.09266758, 0.01855317, 58.09266758, 0.05565951, 40.66486731, -525.96612292, 0.05, 2, 0, 70017, 21017, 1, 3)
    ops.uniaxialMaterial('LimitState', 30017, 14.52316689, 7.468e-05, 43.56950068, 0.00022405, 145.23166895, 0.00074682, -14.52316689, -7.468e-05, -43.56950068, -0.00022405, -145.23166895, -0.00074682, 0.4, 0.3, 0.003, 0.0, 0.0, 10017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 17, 99999, 'P', 40017, 'Vy', 30017, 'Vz', 20017, 'My', 10017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170017, 70017, 170017, 17, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121017, 121017, 21017, 17, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170018, 2.9, 16.2, 0.0)
    ops.node(121018, 2.9, 16.2, 3.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 18, 170018, 121018, 0.105, 32115649.147615, 13381520.47817292, 0.00152551, 0.00117906, 0.00086625, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20018, 67.93673077, 0.0007618, 81.64053788, 0.04610667, 8.16405379, 0.13711582, -67.93673077, -0.0007618, -81.64053788, -0.04610667, -8.16405379, -0.13711582, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10018, 65.3967954, 0.00067995, 78.58826133, 0.04873133, 7.85882613, 0.14873133, -65.3967954, -0.00067995, -78.58826133, -0.04873133, -7.85882613, -0.14873133, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20018, 18, 0.0, 137.11592944, 0.01523594, 137.11592944, 0.04570782, 95.98115061, -1605.72100449, 0.05, 2, 0, 70018, 21018, 2, 3)
    ops.uniaxialMaterial('LimitState', 40018, 34.27898236, 0.00010247, 102.83694708, 0.0003074, 342.7898236, 0.00102467, -34.27898236, -0.00010247, -102.83694708, -0.0003074, -342.7898236, -0.00102467, 0.4, 0.3, 0.003, 0.0, 0.0, 20018, 2)
    ops.limitCurve('ThreePoint', 10018, 18, 0.0, 146.72372071, 0.01359903, 146.72372071, 0.04079708, 102.7066045, -1946.16444164, 0.05, 2, 0, 70018, 21018, 1, 3)
    ops.uniaxialMaterial('LimitState', 30018, 36.68093018, 0.00010965, 110.04279053, 0.00032894, 366.80930178, 0.00109647, -36.68093018, -0.00010965, -110.04279053, -0.00032894, -366.80930178, -0.00109647, 0.4, 0.3, 0.003, 0.0, 0.0, 10018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 18, 99999, 'P', 40018, 'Vy', 30018, 'Vz', 20018, 'My', 10018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170018, 70018, 170018, 18, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121018, 121018, 21018, 18, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170019, 7.9, 16.2, 0.0)
    ops.node(121019, 7.9, 16.2, 3.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 19, 170019, 121019, 0.14, 29172192.74851615, 12155080.31188173, 0.00271929, 0.00205333, 0.00157208, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20019, 106.82253674, 0.00072219, 129.3013286, 0.0525588, 12.93013286, 0.12907878, -106.82253674, -0.00072219, -129.3013286, -0.0525588, -12.93013286, -0.12907878, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10019, 102.51158898, 0.00065739, 124.08322305, 0.05511169, 12.4083223, 0.14111731, -102.51158898, -0.00065739, -124.08322305, -0.05511169, -12.4083223, -0.14111731, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20019, 19, 0.0, 184.08646569, 0.01444376, 184.08646569, 0.04333128, 128.86052598, -2716.50389102, 0.05, 2, 0, 70019, 21019, 2, 3)
    ops.uniaxialMaterial('LimitState', 40019, 46.02161642, 0.00011359, 138.06484926, 0.00034076, 460.21616421, 0.00113586, -46.02161642, -0.00011359, -138.06484926, -0.00034076, -460.21616421, -0.00113586, 0.4, 0.3, 0.003, 0.0, 0.0, 20019, 2)
    ops.limitCurve('ThreePoint', 10019, 19, 0.0, 197.20346498, 0.01314788, 197.20346498, 0.03944363, 138.04242548, -3251.59184725, 0.05, 2, 0, 70019, 21019, 1, 3)
    ops.uniaxialMaterial('LimitState', 30019, 49.30086624, 0.00012168, 147.90259873, 0.00036504, 493.00866244, 0.0012168, -49.30086624, -0.00012168, -147.90259873, -0.00036504, -493.00866244, -0.0012168, 0.4, 0.3, 0.003, 0.0, 0.0, 10019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 19, 99999, 'P', 40019, 'Vy', 30019, 'Vz', 20019, 'My', 10019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170019, 70019, 170019, 19, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121019, 121019, 21019, 19, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170020, 12.9, 16.2, 0.0)
    ops.node(121020, 12.9, 16.2, 3.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 20, 170020, 121020, 0.09, 32023751.7498505, 13343229.89577104, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20020, 40.8060046, 0.00077317, 49.08850411, 0.02937375, 4.90885041, 0.08829391, -40.8060046, -0.00077317, -49.08850411, -0.02937375, -4.90885041, -0.08829391, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10020, 37.9983275, 0.00077317, 45.71094558, 0.02937375, 4.57109456, 0.08829391, -37.9983275, -0.00077317, -45.71094558, -0.02937375, -4.57109456, -0.08829391, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20020, 20, 0.0, 100.52481885, 0.01546337, 100.52481885, 0.04639012, 70.36737319, -923.86736391, 0.05, 2, 0, 70020, 21020, 2, 3)
    ops.uniaxialMaterial('LimitState', 40020, 25.13120471, 8.789e-05, 75.39361413, 0.00026368, 251.31204712, 0.00087894, -25.13120471, -8.789e-05, -75.39361413, -0.00026368, -251.31204712, -0.00087894, 0.4, 0.3, 0.003, 0.0, 0.0, 20020, 2)
    ops.limitCurve('ThreePoint', 10020, 20, 0.0, 100.52481885, 0.01546337, 100.52481885, 0.04639012, 70.36737319, -923.86736391, 0.05, 2, 0, 70020, 21020, 1, 3)
    ops.uniaxialMaterial('LimitState', 30020, 25.13120471, 8.789e-05, 75.39361413, 0.00026368, 251.31204712, 0.00087894, -25.13120471, -8.789e-05, -75.39361413, -0.00026368, -251.31204712, -0.00087894, 0.4, 0.3, 0.003, 0.0, 0.0, 10020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 20, 99999, 'P', 40020, 'Vy', 30020, 'Vz', 20020, 'My', 10020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170020, 70020, 170020, 20, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121020, 121020, 21020, 20, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171003, 7.9, 0.0, 3.75)
    ops.node(122003, 7.9, 0.0, 6.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1003, 171003, 122003, 0.12, 25734814.47518941, 10722839.36466226, 0.00194385, 0.00176, 0.00099, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21003, 45.36461528, 0.00071971, 55.24744445, 0.02380678, 5.52474445, 0.06464378, -45.36461528, -0.00071971, -55.24744445, -0.02380678, -5.52474445, -0.06464378, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11003, 70.17983241, 0.00059598, 85.46873744, 0.02597518, 8.54687374, 0.07709255, -70.17983241, -0.00059598, -85.46873744, -0.02597518, -8.54687374, -0.07709255, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21003, 1003, 0.0, 93.36774303, 0.01439426, 93.36774303, 0.04318277, 65.35742012, -932.35354989, 0.05, 2, 0, 71003, 22003, 2, 3)
    ops.uniaxialMaterial('LimitState', 41003, 23.34193576, 6.313e-05, 70.02580727, 0.00018939, 233.41935757, 0.00063128, -23.34193576, -6.313e-05, -70.02580727, -0.00018939, -233.41935757, -0.00063128, 0.4, 0.3, 0.003, 0.0, 0.0, 21003, 2)
    ops.limitCurve('ThreePoint', 11003, 1003, 0.0, 102.97632337, 0.01191958, 102.97632337, 0.03575873, 72.08342636, -1239.05641148, 0.05, 2, 0, 71003, 22003, 1, 3)
    ops.uniaxialMaterial('LimitState', 31003, 25.74408084, 6.963e-05, 77.23224253, 0.00020888, 257.44080842, 0.00069625, -25.74408084, -6.963e-05, -77.23224253, -0.00020888, -257.44080842, -0.00069625, 0.4, 0.3, 0.003, 0.0, 0.0, 11003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1003, 99999, 'P', 41003, 'Vy', 31003, 'Vz', 21003, 'My', 11003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171003, 71003, 171003, 1003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122003, 122003, 22003, 1003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171004, 12.9, 0.0, 3.75)
    ops.node(122004, 12.9, 0.0, 6.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1004, 171004, 122004, 0.075, 29244738.61612004, 12185307.75671668, 0.00077515, 0.00061875, 0.00042969, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21004, 30.37791878, 0.00085613, 36.82928192, 0.03055034, 3.68292819, 0.08803797, -30.37791878, -0.00085613, -36.82928192, -0.03055034, -3.68292819, -0.08803797, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11004, 34.17041097, 0.00073948, 41.42718624, 0.03236792, 4.14271862, 0.09913834, -34.17041097, -0.00073948, -41.42718624, -0.03236792, -4.14271862, -0.09913834, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21004, 1004, 0.0, 78.05005195, 0.01712265, 78.05005195, 0.05136796, 54.63503637, -1033.82610222, 0.05, 2, 0, 71004, 22004, 2, 3)
    ops.uniaxialMaterial('LimitState', 41004, 19.51251299, 7.43e-05, 58.53753896, 0.0002229, 195.12512988, 0.00074301, -19.51251299, -7.43e-05, -58.53753896, -0.0002229, -195.12512988, -0.00074301, 0.4, 0.3, 0.003, 0.0, 0.0, 21004, 2)
    ops.limitCurve('ThreePoint', 11004, 1004, 0.0, 84.19547012, 0.01478956, 84.19547012, 0.04436869, 58.93682909, -1299.81585352, 0.05, 2, 0, 71004, 22004, 1, 3)
    ops.uniaxialMaterial('LimitState', 31004, 21.04886753, 8.015e-05, 63.14660259, 0.00024045, 210.48867531, 0.00080151, -21.04886753, -8.015e-05, -63.14660259, -0.00024045, -210.48867531, -0.00080151, 0.4, 0.3, 0.003, 0.0, 0.0, 11004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1004, 99999, 'P', 41004, 'Vy', 31004, 'Vz', 21004, 'My', 11004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171004, 71004, 171004, 1004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122004, 122004, 22004, 1004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171005, 0.0, 4.05, 3.775)
    ops.node(122005, 0.0, 4.05, 6.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1005, 171005, 122005, 0.075, 25494175.00065444, 10622572.91693935, 0.00077515, 0.00042969, 0.00061875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21005, 36.28683118, 0.00074659, 44.08935676, 0.03178728, 4.40893568, 0.08637756, -36.28683118, -0.00074659, -44.08935676, -0.03178728, -4.40893568, -0.08637756, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11005, 32.25057296, 0.00086377, 39.18520771, 0.03000618, 3.91852077, 0.07700701, -32.25057296, -0.00086377, -39.18520771, -0.03000618, -3.91852077, -0.07700701, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21005, 1005, 0.0, 83.47334168, 0.01493183, 83.47334168, 0.04479548, 58.43133917, -1410.44002211, 0.05, 2, 0, 71005, 22005, 2, 3)
    ops.uniaxialMaterial('LimitState', 41005, 20.86833542, 9.115e-05, 62.60500626, 0.00027346, 208.68335419, 0.00091154, -20.86833542, -9.115e-05, -62.60500626, -0.00027346, -208.68335419, -0.00091154, 0.4, 0.3, 0.003, 0.0, 0.0, 21005, 2)
    ops.limitCurve('ThreePoint', 11005, 1005, 0.0, 76.52633831, 0.01727549, 76.52633831, 0.05182647, 53.56843682, -1137.11314827, 0.05, 2, 0, 71005, 22005, 1, 3)
    ops.uniaxialMaterial('LimitState', 31005, 19.13158458, 8.357e-05, 57.39475373, 0.0002507, 191.31584577, 0.00083568, -19.13158458, -8.357e-05, -57.39475373, -0.0002507, -191.31584577, -0.00083568, 0.4, 0.3, 0.003, 0.0, 0.0, 11005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1005, 99999, 'P', 41005, 'Vy', 31005, 'Vz', 21005, 'My', 11005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171005, 71005, 171005, 1005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122005, 122005, 22005, 1005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171006, 2.9, 4.05, 3.775)
    ops.node(122006, 2.9, 4.05, 6.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1006, 171006, 122006, 0.1575, 28737763.31358175, 11974068.04732573, 0.00337604, 0.00176859, 0.00292359, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21006, 101.0530689, 0.00057772, 122.61452381, 0.03964789, 12.26145238, 0.10270782, -101.0530689, -0.00057772, -122.61452381, -0.03964789, -12.26145238, -0.10270782, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11006, 71.21521482, 0.00067849, 86.4102372, 0.03654616, 8.64102372, 0.08802738, -71.21521482, -0.00067849, -86.4102372, -0.03654616, -8.64102372, -0.08802738, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21006, 1006, 0.0, 162.956489, 0.01155446, 162.956489, 0.03466339, 114.0695423, -2195.82884221, 0.05, 2, 0, 71006, 22006, 2, 3)
    ops.uniaxialMaterial('LimitState', 41006, 40.73912225, 7.517e-05, 122.21736675, 0.00022552, 407.39122251, 0.00075174, -40.73912225, -7.517e-05, -122.21736675, -0.00022552, -407.39122251, -0.00075174, 0.4, 0.3, 0.003, 0.0, 0.0, 21006, 2)
    ops.limitCurve('ThreePoint', 11006, 1006, 0.0, 148.41250053, 0.01356979, 148.41250053, 0.04070937, 103.88875037, -1646.58212721, 0.05, 2, 0, 71006, 22006, 1, 3)
    ops.uniaxialMaterial('LimitState', 31006, 37.10312513, 6.846e-05, 111.3093754, 0.00020539, 371.03125133, 0.00068465, -37.10312513, -6.846e-05, -111.3093754, -0.00020539, -371.03125133, -0.00068465, 0.4, 0.3, 0.003, 0.0, 0.0, 11006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1006, 99999, 'P', 41006, 'Vy', 31006, 'Vz', 21006, 'My', 11006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171006, 71006, 171006, 1006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122006, 122006, 22006, 1006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171007, 7.9, 4.05, 3.775)
    ops.node(122007, 7.9, 4.05, 6.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1007, 171007, 122007, 0.175, 25981231.94203364, 10825513.30918068, 0.00405757, 0.0019651, 0.00401042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21007, 124.9217002, 0.00057099, 152.20234817, 0.03155091, 15.22023482, 0.078084, -124.9217002, -0.00057099, -152.20234817, -0.03155091, -15.22023482, -0.078084, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11007, 78.15868276, 0.0007028, 95.2271305, 0.02840341, 9.52271305, 0.06408955, -78.15868276, -0.0007028, -95.2271305, -0.02840341, -9.52271305, -0.06408955, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21007, 1007, 0.0, 159.76106857, 0.01141976, 159.76106857, 0.03425929, 111.832748, -1813.94136543, 0.05, 2, 0, 71007, 22007, 2, 3)
    ops.uniaxialMaterial('LimitState', 41007, 39.94026714, 7.337e-05, 119.82080143, 0.0002201, 399.40267142, 0.00073367, -39.94026714, -7.337e-05, -119.82080143, -0.0002201, -399.40267142, -0.00073367, 0.4, 0.3, 0.003, 0.0, 0.0, 21007, 2)
    ops.limitCurve('ThreePoint', 11007, 1007, 0.0, 133.23619408, 0.01405603, 133.23619408, 0.04216808, 93.26533586, -1268.0181204, 0.05, 2, 0, 71007, 22007, 1, 3)
    ops.uniaxialMaterial('LimitState', 31007, 33.30904852, 6.119e-05, 99.92714556, 0.00018356, 333.0904852, 0.00061186, -33.30904852, -6.119e-05, -99.92714556, -0.00018356, -333.0904852, -0.00061186, 0.4, 0.3, 0.003, 0.0, 0.0, 11007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1007, 99999, 'P', 41007, 'Vy', 31007, 'Vz', 21007, 'My', 11007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171007, 71007, 171007, 1007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122007, 122007, 22007, 1007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171008, 12.9, 4.05, 3.775)
    ops.node(122008, 12.9, 4.05, 6.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1008, 171008, 122008, 0.12, 26361995.65576933, 10984164.85657055, 0.00194385, 0.00099, 0.00176, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21008, 68.13019516, 0.00059784, 82.95665742, 0.03502299, 8.29566574, 0.10214763, -68.13019516, -0.00059784, -82.95665742, -0.03502299, -8.29566574, -0.10214763, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11008, 44.25362137, 0.00072706, 53.88407444, 0.03185896, 5.38840744, 0.08473909, -44.25362137, -0.00072706, -53.88407444, -0.03185896, -5.38840744, -0.08473909, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21008, 1008, 0.0, 115.53759194, 0.0119568, 115.53759194, 0.03587039, 80.87631436, -1655.4492018, 0.05, 2, 0, 71008, 22008, 2, 3)
    ops.uniaxialMaterial('LimitState', 41008, 28.88439798, 7.626e-05, 86.65319395, 0.00022878, 288.84397984, 0.0007626, -28.88439798, -7.626e-05, -86.65319395, -0.00022878, -288.84397984, -0.0007626, 0.4, 0.3, 0.003, 0.0, 0.0, 21008, 2)
    ops.limitCurve('ThreePoint', 11008, 1008, 0.0, 103.18211406, 0.01454113, 103.18211406, 0.04362338, 72.22747984, -1195.13055503, 0.05, 2, 0, 71008, 22008, 1, 3)
    ops.uniaxialMaterial('LimitState', 31008, 25.79552852, 6.81e-05, 77.38658555, 0.00020431, 257.95528515, 0.00068104, -25.79552852, -6.81e-05, -77.38658555, -0.00020431, -257.95528515, -0.00068104, 0.4, 0.3, 0.003, 0.0, 0.0, 11008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1008, 99999, 'P', 41008, 'Vy', 31008, 'Vz', 21008, 'My', 11008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171008, 71008, 171008, 1008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122008, 122008, 22008, 1008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171009, 0.0, 8.1, 3.775)
    ops.node(122009, 0.0, 8.1, 6.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1009, 171009, 122009, 0.075, 29861200.40900388, 12442166.83708495, 0.00077515, 0.00042969, 0.00061875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21009, 32.16997236, 0.00068173, 38.93348192, 0.03374996, 3.89334819, 0.10051616, -32.16997236, -0.00068173, -38.93348192, -0.03374996, -3.89334819, -0.10051616, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11009, 28.37694835, 0.00078817, 34.34300138, 0.03183412, 3.43430014, 0.08931811, -28.37694835, -0.00078817, -34.34300138, -0.03183412, -3.43430014, -0.08931811, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21009, 1009, 0.0, 87.30612409, 0.01363466, 87.30612409, 0.04090397, 61.11428686, -1324.36920696, 0.05, 2, 0, 71009, 22009, 2, 3)
    ops.uniaxialMaterial('LimitState', 41009, 21.82653102, 8.14e-05, 65.47959307, 0.00024419, 218.26531022, 0.00081397, -21.82653102, -8.14e-05, -65.47959307, -0.00024419, -218.26531022, -0.00081397, 0.4, 0.3, 0.003, 0.0, 0.0, 21009, 2)
    ops.limitCurve('ThreePoint', 11009, 1009, 0.0, 80.97239171, 0.01576341, 80.97239171, 0.04729024, 56.6806742, -1056.93858627, 0.05, 2, 0, 71009, 22009, 1, 3)
    ops.uniaxialMaterial('LimitState', 31009, 20.24309793, 7.549e-05, 60.72929379, 0.00022647, 202.43097929, 0.00075492, -20.24309793, -7.549e-05, -60.72929379, -0.00022647, -202.43097929, -0.00075492, 0.4, 0.3, 0.003, 0.0, 0.0, 11009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1009, 99999, 'P', 41009, 'Vy', 31009, 'Vz', 21009, 'My', 11009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171009, 71009, 171009, 1009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122009, 122009, 22009, 1009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171010, 2.9, 8.1, 3.775)
    ops.node(122010, 2.9, 8.1, 6.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1010, 171010, 122010, 0.12, 27298509.3396631, 11374378.89152629, 0.00194385, 0.00099, 0.00176, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21010, 70.15593815, 0.00062521, 85.24535349, 0.04124676, 8.52453535, 0.108456, -70.15593815, -0.00062521, -85.24535349, -0.04124676, -8.52453535, -0.108456, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11010, 51.28913448, 0.00075837, 62.32060342, 0.03749391, 6.23206034, 0.09044068, -51.28913448, -0.00075837, -62.32060342, -0.03749391, -6.23206034, -0.09044068, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21010, 1010, 0.0, 132.27224593, 0.01250417, 132.27224593, 0.03751252, 92.59057215, -2108.06199378, 0.05, 2, 0, 71010, 22010, 2, 3)
    ops.uniaxialMaterial('LimitState', 41010, 33.06806148, 8.431e-05, 99.20418445, 0.00025293, 330.68061482, 0.0008431, -33.06806148, -8.431e-05, -99.20418445, -0.00025293, -330.68061482, -0.0008431, 0.4, 0.3, 0.003, 0.0, 0.0, 21010, 2)
    ops.limitCurve('ThreePoint', 11010, 1010, 0.0, 116.91378814, 0.01516743, 116.91378814, 0.04550228, 81.8396517, -1499.49611453, 0.05, 2, 0, 71010, 22010, 1, 3)
    ops.uniaxialMaterial('LimitState', 31010, 29.22844703, 7.452e-05, 87.6853411, 0.00022356, 292.28447034, 0.00074521, -29.22844703, -7.452e-05, -87.6853411, -0.00022356, -292.28447034, -0.00074521, 0.4, 0.3, 0.003, 0.0, 0.0, 11010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1010, 99999, 'P', 41010, 'Vy', 31010, 'Vz', 21010, 'My', 11010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171010, 71010, 171010, 1010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122010, 122010, 22010, 1010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171011, 7.9, 8.1, 3.775)
    ops.node(122011, 7.9, 8.1, 6.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1011, 171011, 122011, 0.175, 26118709.45970115, 10882795.60820881, 0.00405757, 0.0019651, 0.00401042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21011, 120.73939961, 0.00054823, 147.08744531, 0.03256762, 14.70874453, 0.0793238, -120.73939961, -0.00054823, -147.08744531, -0.03256762, -14.70874453, -0.0793238, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11011, 75.68761226, 0.00066951, 92.20434725, 0.02929957, 9.22043473, 0.06515678, -75.68761226, -0.00066951, -92.20434725, -0.02929957, -9.22043473, -0.06515678, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21011, 1011, 0.0, 166.14246539, 0.01096452, 166.14246539, 0.03289355, 116.29972577, -2019.3743675, 0.05, 2, 0, 71011, 22011, 2, 3)
    ops.uniaxialMaterial('LimitState', 41011, 41.53561635, 7.59e-05, 124.60684904, 0.00022769, 415.35616348, 0.00075896, -41.53561635, -7.59e-05, -124.60684904, -0.00022769, -415.35616348, -0.00075896, 0.4, 0.3, 0.003, 0.0, 0.0, 21011, 2)
    ops.limitCurve('ThreePoint', 11011, 1011, 0.0, 137.85467842, 0.01339028, 137.85467842, 0.04017083, 96.4982749, -1387.72516385, 0.05, 2, 0, 71011, 22011, 1, 3)
    ops.uniaxialMaterial('LimitState', 31011, 34.46366961, 6.297e-05, 103.39100882, 0.00018892, 344.63669605, 0.00062974, -34.46366961, -6.297e-05, -103.39100882, -0.00018892, -344.63669605, -0.00062974, 0.4, 0.3, 0.003, 0.0, 0.0, 11011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1011, 99999, 'P', 41011, 'Vy', 31011, 'Vz', 21011, 'My', 11011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171011, 71011, 171011, 1011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122011, 122011, 22011, 1011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171012, 12.9, 8.1, 3.775)
    ops.node(122012, 12.9, 8.1, 6.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1012, 171012, 122012, 0.12, 27251588.00656459, 11354828.33606858, 0.00194385, 0.00099, 0.00176, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21012, 59.25086369, 0.00059214, 72.06767816, 0.03796335, 7.20676782, 0.10700303, -59.25086369, -0.00059214, -72.06767816, -0.03796335, -7.20676782, -0.10700303, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11012, 48.52103052, 0.00072267, 59.01682766, 0.03451881, 5.90168277, 0.08890758, -48.52103052, -0.00072267, -59.01682766, -0.03451881, -5.90168277, -0.08890758, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21012, 1012, 0.0, 128.53720599, 0.01184281, 128.53720599, 0.03552844, 89.9760442, -2082.42612696, 0.05, 2, 0, 71012, 22012, 2, 3)
    ops.uniaxialMaterial('LimitState', 41012, 32.1343015, 8.207e-05, 96.4029045, 0.00024621, 321.34301499, 0.0008207, -32.1343015, -8.207e-05, -96.4029045, -0.00024621, -321.34301499, -0.0008207, 0.4, 0.3, 0.003, 0.0, 0.0, 21012, 2)
    ops.limitCurve('ThreePoint', 11012, 1012, 0.0, 113.68378943, 0.01445339, 113.68378943, 0.04336016, 79.5786526, -1465.39339298, 0.05, 2, 0, 71012, 22012, 1, 3)
    ops.uniaxialMaterial('LimitState', 31012, 28.42094736, 7.259e-05, 85.26284207, 0.00021776, 284.20947357, 0.00072587, -28.42094736, -7.259e-05, -85.26284207, -0.00021776, -284.20947357, -0.00072587, 0.4, 0.3, 0.003, 0.0, 0.0, 11012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1012, 99999, 'P', 41012, 'Vy', 31012, 'Vz', 21012, 'My', 11012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171012, 71012, 171012, 1012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122012, 122012, 22012, 1012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171013, 0.0, 12.15, 3.775)
    ops.node(122013, 0.0, 12.15, 6.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1013, 171013, 122013, 0.075, 28213344.97119724, 11755560.40466552, 0.00077515, 0.00042969, 0.00061875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21013, 32.78236328, 0.00076626, 39.80210137, 0.03375071, 3.98021014, 0.0979913, -32.78236328, -0.00076626, -39.80210137, -0.03375071, -3.98021014, -0.0979913, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11013, 28.5894166, 0.00090415, 34.71131254, 0.03187144, 3.47113125, 0.08718096, -28.5894166, -0.00090415, -34.71131254, -0.03187144, -3.47113125, -0.08718096, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21013, 1013, 0.0, 86.69374022, 0.0153251, 86.69374022, 0.04597531, 60.68561816, -1463.69608757, 0.05, 2, 0, 71013, 22013, 2, 3)
    ops.uniaxialMaterial('LimitState', 41013, 21.67343506, 8.555e-05, 65.02030517, 0.00025664, 216.73435055, 0.00085547, -21.67343506, -8.555e-05, -65.02030517, -0.00025664, -216.73435055, -0.00085547, 0.4, 0.3, 0.003, 0.0, 0.0, 21013, 2)
    ops.limitCurve('ThreePoint', 11013, 1013, 0.0, 79.85239069, 0.01808296, 79.85239069, 0.05424888, 55.89667348, -1160.48711998, 0.05, 2, 0, 71013, 22013, 1, 3)
    ops.uniaxialMaterial('LimitState', 31013, 19.96309767, 7.88e-05, 59.88929302, 0.00023639, 199.63097672, 0.00078796, -19.96309767, -7.88e-05, -59.88929302, -0.00023639, -199.63097672, -0.00078796, 0.4, 0.3, 0.003, 0.0, 0.0, 11013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1013, 99999, 'P', 41013, 'Vy', 31013, 'Vz', 21013, 'My', 11013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171013, 71013, 171013, 1013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122013, 122013, 22013, 1013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171014, 2.9, 12.15, 3.775)
    ops.node(122014, 2.9, 12.15, 6.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1014, 171014, 122014, 0.12, 28998415.78698892, 12082673.24457872, 0.00194385, 0.00099, 0.00176, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21014, 70.05452448, 0.00068146, 84.89402209, 0.03850356, 8.48940221, 0.10907108, -70.05452448, -0.00068146, -84.89402209, -0.03850356, -8.48940221, -0.10907108, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11014, 50.81864557, 0.00085641, 61.58344877, 0.0350603, 6.15834488, 0.09065269, -50.81864557, -0.00085641, -61.58344877, -0.0350603, -6.15834488, -0.09065269, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21014, 1014, 0.0, 132.35268831, 0.01362922, 132.35268831, 0.04088766, 92.64688182, -1863.41645152, 0.05, 2, 0, 71014, 22014, 2, 3)
    ops.uniaxialMaterial('LimitState', 41014, 33.08817208, 7.942e-05, 99.26451623, 0.00023825, 330.88172077, 0.00079416, -33.08817208, -7.942e-05, -99.26451623, -0.00023825, -330.88172077, -0.00079416, 0.4, 0.3, 0.003, 0.0, 0.0, 21014, 2)
    ops.limitCurve('ThreePoint', 11014, 1014, 0.0, 118.46076606, 0.01712813, 118.46076606, 0.0513844, 82.92253624, -1344.21819719, 0.05, 2, 0, 71014, 22014, 1, 3)
    ops.uniaxialMaterial('LimitState', 31014, 29.61519151, 7.108e-05, 88.84557454, 0.00021324, 296.15191514, 0.0007108, -29.61519151, -7.108e-05, -88.84557454, -0.00021324, -296.15191514, -0.0007108, 0.4, 0.3, 0.003, 0.0, 0.0, 11014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1014, 99999, 'P', 41014, 'Vy', 31014, 'Vz', 21014, 'My', 11014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171014, 71014, 171014, 1014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122014, 122014, 22014, 1014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171015, 7.9, 12.15, 3.775)
    ops.node(122015, 7.9, 12.15, 6.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1015, 171015, 122015, 0.175, 27094457.19584191, 11289357.16493413, 0.00405757, 0.0019651, 0.00401042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21015, 119.86511701, 0.00052697, 145.85705667, 0.03482718, 14.58570567, 0.08305606, -119.86511701, -0.00052697, -145.85705667, -0.03482718, -14.58570567, -0.08305606, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11015, 75.2442702, 0.00063515, 91.56048111, 0.03130458, 9.15604811, 0.06829122, -75.2442702, -0.00063515, -91.56048111, -0.03130458, -9.15604811, -0.06829122, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21015, 1015, 0.0, 178.41508505, 0.01053938, 178.41508505, 0.03161814, 124.89055954, -2289.08608039, 0.05, 2, 0, 71015, 22015, 2, 3)
    ops.uniaxialMaterial('LimitState', 41015, 44.60377126, 7.857e-05, 133.81131379, 0.0002357, 446.03771263, 0.00078568, -44.60377126, -7.857e-05, -133.81131379, -0.0002357, -446.03771263, -0.00078568, 0.4, 0.3, 0.003, 0.0, 0.0, 21015, 2)
    ops.limitCurve('ThreePoint', 11015, 1015, 0.0, 147.5342571, 0.01270302, 147.5342571, 0.03810907, 103.27397997, -1543.47188987, 0.05, 2, 0, 71015, 22015, 1, 3)
    ops.uniaxialMaterial('LimitState', 31015, 36.88356427, 6.497e-05, 110.65069282, 0.00019491, 368.83564274, 0.00064969, -36.88356427, -6.497e-05, -110.65069282, -0.00019491, -368.83564274, -0.00064969, 0.4, 0.3, 0.003, 0.0, 0.0, 11015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1015, 99999, 'P', 41015, 'Vy', 31015, 'Vz', 21015, 'My', 11015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171015, 71015, 171015, 1015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122015, 122015, 22015, 1015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171016, 12.9, 12.15, 3.775)
    ops.node(122016, 12.9, 12.15, 6.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1016, 171016, 122016, 0.12, 30170822.10710206, 12571175.87795919, 0.00194385, 0.00099, 0.00176, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21016, 63.32671085, 0.0005883, 76.60625448, 0.03694989, 7.66062545, 0.11093452, -63.32671085, -0.0005883, -76.60625448, -0.03694989, -7.66062545, -0.11093452, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11016, 52.83941457, 0.00070667, 63.91978338, 0.03358977, 6.39197834, 0.09187413, -52.83941457, -0.00070667, -63.91978338, -0.03358977, -6.39197834, -0.09187413, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21016, 1016, 0.0, 132.14997826, 0.0117659, 132.14997826, 0.0352977, 92.50498478, -1792.07166038, 0.05, 2, 0, 71016, 22016, 2, 3)
    ops.uniaxialMaterial('LimitState', 41016, 33.03749456, 7.621e-05, 99.11248369, 0.00022864, 330.37494564, 0.00076213, -33.03749456, -7.621e-05, -99.11248369, -0.00022864, -330.37494564, -0.00076213, 0.4, 0.3, 0.003, 0.0, 0.0, 21016, 2)
    ops.limitCurve('ThreePoint', 11016, 1016, 0.0, 118.96344134, 0.01413339, 118.96344134, 0.04240016, 83.27440894, -1281.991009, 0.05, 2, 0, 71016, 22016, 1, 3)
    ops.uniaxialMaterial('LimitState', 31016, 29.74086034, 6.861e-05, 89.22258101, 0.00020582, 297.40860336, 0.00068608, -29.74086034, -6.861e-05, -89.22258101, -0.00020582, -297.40860336, -0.00068608, 0.4, 0.3, 0.003, 0.0, 0.0, 11016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1016, 99999, 'P', 41016, 'Vy', 31016, 'Vz', 21016, 'My', 11016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171016, 71016, 171016, 1016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122016, 122016, 22016, 1016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171017, 0.0, 16.2, 3.75)
    ops.node(122017, 0.0, 16.2, 6.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1017, 171017, 122017, 0.0625, 29098761.50959595, 12124483.96233165, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21017, 20.21297134, 0.00078345, 24.54676101, 0.01967826, 2.4546761, 0.07746822, -20.21297134, -0.00078345, -24.54676101, -0.01967826, -2.4546761, -0.07746822, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11017, 20.21297134, 0.00078345, 24.54676101, 0.01967826, 2.4546761, 0.07746822, -20.21297134, -0.00078345, -24.54676101, -0.01967826, -2.4546761, -0.07746822, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21017, 1017, 0.0, 44.60446698, 0.01566893, 44.60446698, 0.04700678, 31.22312688, -642.40200155, 0.05, 2, 0, 71017, 22017, 2, 3)
    ops.uniaxialMaterial('LimitState', 41017, 11.15111674, 5.121e-05, 33.45335023, 0.00015363, 111.51116744, 0.0005121, -11.15111674, -5.121e-05, -33.45335023, -0.00015363, -111.51116744, -0.0005121, 0.4, 0.3, 0.003, 0.0, 0.0, 21017, 2)
    ops.limitCurve('ThreePoint', 11017, 1017, 0.0, 44.60446698, 0.01566893, 44.60446698, 0.04700678, 31.22312688, -642.40200155, 0.05, 2, 0, 71017, 22017, 1, 3)
    ops.uniaxialMaterial('LimitState', 31017, 11.15111674, 5.121e-05, 33.45335023, 0.00015363, 111.51116744, 0.0005121, -11.15111674, -5.121e-05, -33.45335023, -0.00015363, -111.51116744, -0.0005121, 0.4, 0.3, 0.003, 0.0, 0.0, 11017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1017, 99999, 'P', 41017, 'Vy', 31017, 'Vz', 21017, 'My', 11017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171017, 71017, 171017, 1017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122017, 122017, 22017, 1017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171018, 2.9, 16.2, 3.75)
    ops.node(122018, 2.9, 16.2, 6.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1018, 171018, 122018, 0.105, 29244676.79148157, 12185281.99645066, 0.00152551, 0.00117906, 0.00086625, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21018, 42.203562, 0.00075426, 51.17852497, 0.03798634, 5.1178525, 0.10255822, -42.203562, -0.00075426, -51.17852497, -0.03798634, -5.1178525, -0.10255822, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11018, 45.64089793, 0.00066196, 55.34684097, 0.03998164, 5.5346841, 0.11347442, -45.64089793, -0.00066196, -55.34684097, -0.03998164, -5.5346841, -0.11347442, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21018, 1018, 0.0, 118.27261367, 0.01508518, 118.27261367, 0.04525553, 82.79082957, -1881.66876139, 0.05, 2, 0, 71018, 22018, 2, 3)
    ops.uniaxialMaterial('LimitState', 41018, 29.56815342, 8.042e-05, 88.70446025, 0.00024127, 295.68153417, 0.00080423, -29.56815342, -8.042e-05, -88.70446025, -0.00024127, -295.68153417, -0.00080423, 0.4, 0.3, 0.003, 0.0, 0.0, 21018, 2)
    ops.limitCurve('ThreePoint', 11018, 1018, 0.0, 127.01732851, 0.01323912, 127.01732851, 0.03971736, 88.91212996, -2319.45955536, 0.05, 2, 0, 71018, 22018, 1, 3)
    ops.uniaxialMaterial('LimitState', 31018, 31.75433213, 8.637e-05, 95.26299639, 0.00025911, 317.54332129, 0.00086369, -31.75433213, -8.637e-05, -95.26299639, -0.00025911, -317.54332129, -0.00086369, 0.4, 0.3, 0.003, 0.0, 0.0, 11018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1018, 99999, 'P', 41018, 'Vy', 31018, 'Vz', 21018, 'My', 11018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171018, 71018, 171018, 1018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122018, 122018, 22018, 1018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171019, 7.9, 16.2, 3.75)
    ops.node(122019, 7.9, 16.2, 6.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1019, 171019, 122019, 0.14, 28464215.64329259, 11860089.85137191, 0.00271929, 0.00205333, 0.00157208, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21019, 64.48372105, 0.00068354, 78.34074413, 0.02837408, 7.83407441, 0.07426933, -64.48372105, -0.00068354, -78.34074413, -0.02837408, -7.83407441, -0.07426933, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11019, 78.78023365, 0.00062677, 95.7094601, 0.02953805, 9.57094601, 0.08037865, -78.78023365, -0.00062677, -95.7094601, -0.02953805, -9.57094601, -0.08037865, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21019, 1019, 0.0, 116.6935836, 0.01367075, 116.6935836, 0.04101226, 81.68550852, -1055.74977056, 0.05, 2, 0, 71019, 22019, 2, 3)
    ops.uniaxialMaterial('LimitState', 41019, 29.1733959, 6.114e-05, 87.5201877, 0.00018343, 291.73395899, 0.00061143, -29.1733959, -6.114e-05, -87.5201877, -0.00018343, -291.73395899, -0.00061143, 0.4, 0.3, 0.003, 0.0, 0.0, 21019, 2)
    ops.limitCurve('ThreePoint', 11019, 1019, 0.0, 121.38732692, 0.01253549, 121.38732692, 0.03760648, 84.97112884, -1208.87029688, 0.05, 2, 0, 71019, 22019, 1, 3)
    ops.uniaxialMaterial('LimitState', 31019, 30.34683173, 6.36e-05, 91.04049519, 0.00019081, 303.46831729, 0.00063603, -30.34683173, -6.36e-05, -91.04049519, -0.00019081, -303.46831729, -0.00063603, 0.4, 0.3, 0.003, 0.0, 0.0, 11019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1019, 99999, 'P', 41019, 'Vy', 31019, 'Vz', 21019, 'My', 11019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171019, 71019, 171019, 1019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122019, 122019, 22019, 1019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171020, 12.9, 16.2, 3.75)
    ops.node(122020, 12.9, 16.2, 6.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1020, 171020, 122020, 0.09, 31444868.96803074, 13102028.73667948, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21020, 35.04743753, 0.00068779, 42.29846213, 0.0275414, 4.22984621, 0.08880388, -35.04743753, -0.00068779, -42.29846213, -0.0275414, -4.22984621, -0.08880388, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11020, 32.53600362, 0.00068779, 39.26743334, 0.0275414, 3.92674333, 0.08880388, -32.53600362, -0.00068779, -39.26743334, -0.0275414, -3.92674333, -0.08880388, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21020, 1020, 0.0, 90.60694947, 0.01375572, 90.60694947, 0.04126716, 63.42486463, -984.19672167, 0.05, 2, 0, 71020, 22020, 2, 3)
    ops.uniaxialMaterial('LimitState', 41020, 22.65173737, 6.685e-05, 67.9552121, 0.00020055, 226.51737367, 0.0006685, -22.65173737, -6.685e-05, -67.9552121, -0.00020055, -226.51737367, -0.0006685, 0.4, 0.3, 0.003, 0.0, 0.0, 21020, 2)
    ops.limitCurve('ThreePoint', 11020, 1020, 0.0, 90.60694947, 0.01375572, 90.60694947, 0.04126716, 63.42486463, -984.19672167, 0.05, 2, 0, 71020, 22020, 1, 3)
    ops.uniaxialMaterial('LimitState', 31020, 22.65173737, 6.685e-05, 67.9552121, 0.00020055, 226.51737367, 0.0006685, -22.65173737, -6.685e-05, -67.9552121, -0.00020055, -226.51737367, -0.0006685, 0.4, 0.3, 0.003, 0.0, 0.0, 11020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1020, 99999, 'P', 41020, 'Vy', 31020, 'Vz', 21020, 'My', 11020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171020, 71020, 171020, 1020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122020, 122020, 22020, 1020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172003, 7.9, 0.0, 6.65)
    ops.node(123003, 7.9, 0.0, 9.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2003, 172003, 123003, 0.0875, 29745787.41546452, 12394078.08977688, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22003, 26.38115737, 0.00075682, 31.96915527, 0.02389395, 3.19691553, 0.07625093, -26.38115737, -0.00075682, -31.96915527, -0.02389395, -3.19691553, -0.07625093, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12003, 41.27144737, 0.00059441, 50.01347328, 0.02654152, 5.00134733, 0.09525722, -41.27144737, -0.00059441, -50.01347328, -0.02654152, -5.00134733, -0.09525722, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22003, 2003, 0.0, 77.22318745, 0.01513637, 77.22318745, 0.04540911, 54.05623122, -698.9378102, 0.05, 2, 0, 72003, 23003, 2, 3)
    ops.uniaxialMaterial('LimitState', 42003, 19.30579686, 6.195e-05, 57.91739059, 0.00018585, 193.05796863, 0.0006195, -19.30579686, -6.195e-05, -57.91739059, -0.00018585, -193.05796863, -0.0006195, 0.4, 0.3, 0.003, 0.0, 0.0, 22003, 2)
    ops.limitCurve('ThreePoint', 12003, 2003, 0.0, 85.92274704, 0.01188821, 85.92274704, 0.03566464, 60.14592292, -1013.97227616, 0.05, 2, 0, 72003, 23003, 1, 3)
    ops.uniaxialMaterial('LimitState', 32003, 21.48068676, 6.893e-05, 64.44206028, 0.00020679, 214.80686759, 0.00068929, -21.48068676, -6.893e-05, -64.44206028, -0.00020679, -214.80686759, -0.00068929, 0.4, 0.3, 0.003, 0.0, 0.0, 12003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2003, 99999, 'P', 42003, 'Vy', 32003, 'Vz', 22003, 'My', 12003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172003, 72003, 172003, 2003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123003, 123003, 23003, 2003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172004, 12.9, 0.0, 6.65)
    ops.node(123004, 12.9, 0.0, 9.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2004, 172004, 123004, 0.0625, 26731996.61718854, 11138331.92382856, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22004, 19.00741673, 0.00079169, 23.19301381, 0.02410671, 2.31930138, 0.07997572, -19.00741673, -0.00079169, -23.19301381, -0.02410671, -2.31930138, -0.07997572, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12004, 19.00741673, 0.00079169, 23.19301381, 0.02410671, 2.31930138, 0.07997572, -19.00741673, -0.00079169, -23.19301381, -0.02410671, -2.31930138, -0.07997572, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22004, 2004, 0.0, 53.47899086, 0.01583385, 53.47899086, 0.04750154, 37.4352936, -754.12433407, 0.05, 2, 0, 72004, 23004, 2, 3)
    ops.uniaxialMaterial('LimitState', 42004, 13.36974772, 6.683e-05, 40.10924315, 0.0002005, 133.69747716, 0.00066835, -13.36974772, -6.683e-05, -40.10924315, -0.0002005, -133.69747716, -0.00066835, 0.4, 0.3, 0.003, 0.0, 0.0, 22004, 2)
    ops.limitCurve('ThreePoint', 12004, 2004, 0.0, 53.47899086, 0.01583385, 53.47899086, 0.04750154, 37.4352936, -754.12433407, 0.05, 2, 0, 72004, 23004, 1, 3)
    ops.uniaxialMaterial('LimitState', 32004, 13.36974772, 6.683e-05, 40.10924315, 0.0002005, 133.69747716, 0.00066835, -13.36974772, -6.683e-05, -40.10924315, -0.0002005, -133.69747716, -0.00066835, 0.4, 0.3, 0.003, 0.0, 0.0, 12004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2004, 99999, 'P', 42004, 'Vy', 32004, 'Vz', 22004, 'My', 12004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172004, 72004, 172004, 2004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123004, 123004, 23004, 2004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172005, 0.0, 4.05, 6.675)
    ops.node(123005, 0.0, 4.05, 9.025)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2005, 172005, 123005, 0.0625, 30627768.00123139, 12761570.00051308, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22005, 20.99981774, 0.00077056, 25.37602438, 0.0250957, 2.53760244, 0.08202175, -20.99981774, -0.00077056, -25.37602438, -0.0250957, -2.53760244, -0.08202175, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12005, 20.99981774, 0.00077056, 25.37602438, 0.0250957, 2.53760244, 0.08202175, -20.99981774, -0.00077056, -25.37602438, -0.0250957, -2.53760244, -0.08202175, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22005, 2005, 0.0, 65.91974117, 0.01541127, 65.91974117, 0.04623382, 46.14381882, -783.84255068, 0.05, 2, 0, 72005, 23005, 2, 3)
    ops.uniaxialMaterial('LimitState', 42005, 16.47993529, 7.19e-05, 49.43980588, 0.00021571, 164.79935292, 0.00071904, -16.47993529, -7.19e-05, -49.43980588, -0.00021571, -164.79935292, -0.00071904, 0.4, 0.3, 0.003, 0.0, 0.0, 22005, 2)
    ops.limitCurve('ThreePoint', 12005, 2005, 0.0, 65.91974117, 0.01541127, 65.91974117, 0.04623382, 46.14381882, -783.84255068, 0.05, 2, 0, 72005, 23005, 1, 3)
    ops.uniaxialMaterial('LimitState', 32005, 16.47993529, 7.19e-05, 49.43980588, 0.00021571, 164.79935292, 0.00071904, -16.47993529, -7.19e-05, -49.43980588, -0.00021571, -164.79935292, -0.00071904, 0.4, 0.3, 0.003, 0.0, 0.0, 12005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2005, 99999, 'P', 42005, 'Vy', 32005, 'Vz', 22005, 'My', 12005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172005, 72005, 172005, 2005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123005, 123005, 23005, 2005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172006, 2.9, 4.05, 6.675)
    ops.node(123006, 2.9, 4.05, 9.025)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2006, 172006, 123006, 0.0875, 34366008.81888516, 14319170.34120215, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22006, 51.37754658, 0.00060548, 61.33354614, 0.02964493, 6.13335461, 0.10030859, -51.37754658, -0.00060548, -61.33354614, -0.02964493, -6.13335461, -0.10030859, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12006, 35.37620993, 0.00077178, 42.23145223, 0.02666637, 4.22314522, 0.08050756, -35.37620993, -0.00077178, -42.23145223, -0.02666637, -4.22314522, -0.08050756, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22006, 2006, 0.0, 101.26531421, 0.01210962, 101.26531421, 0.03632886, 70.88571995, -971.8507035, 0.05, 2, 0, 72006, 23006, 2, 3)
    ops.uniaxialMaterial('LimitState', 42006, 25.31632855, 7.032e-05, 75.94898566, 0.00021095, 253.16328552, 0.00070316, -25.31632855, -7.032e-05, -75.94898566, -0.00021095, -253.16328552, -0.00070316, 0.4, 0.3, 0.003, 0.0, 0.0, 22006, 2)
    ops.limitCurve('ThreePoint', 12006, 2006, 0.0, 92.63760056, 0.01543561, 92.63760056, 0.04630683, 64.84632039, -703.52165211, 0.05, 2, 0, 72006, 23006, 1, 3)
    ops.uniaxialMaterial('LimitState', 32006, 23.15940014, 6.433e-05, 69.47820042, 0.00019298, 231.59400141, 0.00064325, -23.15940014, -6.433e-05, -69.47820042, -0.00019298, -231.59400141, -0.00064325, 0.4, 0.3, 0.003, 0.0, 0.0, 12006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2006, 99999, 'P', 42006, 'Vy', 32006, 'Vz', 22006, 'My', 12006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172006, 72006, 172006, 2006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123006, 123006, 23006, 2006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172007, 7.9, 4.05, 6.675)
    ops.node(123007, 7.9, 4.05, 9.025)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2007, 172007, 123007, 0.1, 29210202.04807768, 12170917.52003237, 0.00127345, 0.00057292, 0.00146667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22007, 59.05111156, 0.00057648, 71.55182857, 0.03364295, 7.15518286, 0.09912369, -59.05111156, -0.00057648, -71.55182857, -0.03364295, -7.15518286, -0.09912369, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12007, 35.03096386, 0.00080797, 42.44677966, 0.02904848, 4.24467797, 0.07408753, -35.03096386, -0.00080797, -42.44677966, -0.02904848, -4.24467797, -0.07408753, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22007, 2007, 0.0, 105.0564083, 0.01152968, 105.0564083, 0.03458903, 73.53948581, -1352.80362835, 0.05, 2, 0, 72007, 23007, 2, 3)
    ops.uniaxialMaterial('LimitState', 42007, 26.26410208, 7.51e-05, 78.79230623, 0.00022529, 262.64102076, 0.00075096, -26.26410208, -7.51e-05, -78.79230623, -0.00022529, -262.64102076, -0.00075096, 0.4, 0.3, 0.003, 0.0, 0.0, 22007, 2)
    ops.limitCurve('ThreePoint', 12007, 2007, 0.0, 89.69948683, 0.01615937, 89.69948683, 0.0484781, 62.78964078, -825.83892827, 0.05, 2, 0, 72007, 23007, 1, 3)
    ops.uniaxialMaterial('LimitState', 32007, 22.42487171, 6.412e-05, 67.27461512, 0.00019236, 224.24871708, 0.00064119, -22.42487171, -6.412e-05, -67.27461512, -0.00019236, -224.24871708, -0.00064119, 0.4, 0.3, 0.003, 0.0, 0.0, 12007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2007, 99999, 'P', 42007, 'Vy', 32007, 'Vz', 22007, 'My', 12007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172007, 72007, 172007, 2007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123007, 123007, 23007, 2007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172008, 12.9, 4.05, 6.675)
    ops.node(123008, 12.9, 4.05, 9.025)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2008, 172008, 123008, 0.0875, 32611804.47918451, 13588251.86632688, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22008, 40.33438308, 0.00060541, 48.5012987, 0.02542984, 4.85012987, 0.08532901, -40.33438308, -0.00060541, -48.5012987, -0.02542984, -4.85012987, -0.08532901, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12008, 25.98780668, 0.0007858, 31.24982405, 0.02304726, 3.1249824, 0.0693024, -25.98780668, -0.0007858, -31.24982405, -0.02304726, -3.1249824, -0.0693024, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22008, 2008, 0.0, 97.43550486, 0.01210813, 97.43550486, 0.03632439, 68.2048534, -1193.71657777, 0.05, 2, 0, 72008, 23008, 2, 3)
    ops.uniaxialMaterial('LimitState', 42008, 24.35887621, 7.13e-05, 73.07662864, 0.00021389, 243.58876214, 0.00071296, -24.35887621, -7.13e-05, -73.07662864, -0.00021389, -243.58876214, -0.00071296, 0.4, 0.3, 0.003, 0.0, 0.0, 22008, 2)
    ops.limitCurve('ThreePoint', 12008, 2008, 0.0, 87.5604136, 0.0157159, 87.5604136, 0.04714771, 61.29228952, -801.38714606, 0.05, 2, 0, 72008, 23008, 1, 3)
    ops.uniaxialMaterial('LimitState', 32008, 21.8901034, 6.407e-05, 65.6703102, 0.00019221, 218.90103401, 0.0006407, -21.8901034, -6.407e-05, -65.6703102, -0.00019221, -218.90103401, -0.0006407, 0.4, 0.3, 0.003, 0.0, 0.0, 12008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2008, 99999, 'P', 42008, 'Vy', 32008, 'Vz', 22008, 'My', 12008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172008, 72008, 172008, 2008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123008, 123008, 23008, 2008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172009, 0.0, 8.1, 6.675)
    ops.node(123009, 0.0, 8.1, 9.025)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2009, 172009, 123009, 0.0625, 28156844.32712845, 11732018.46963686, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22009, 18.46503495, 0.00083641, 22.46695658, 0.02324799, 2.24669566, 0.08005212, -18.46503495, -0.00083641, -22.46695658, -0.02324799, -2.24669566, -0.08005212, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12009, 18.46503495, 0.00083641, 22.46695658, 0.02324799, 2.24669566, 0.08005212, -18.46503495, -0.00083641, -22.46695658, -0.02324799, -2.24669566, -0.08005212, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22009, 2009, 0.0, 54.585527, 0.01672817, 54.585527, 0.05018452, 38.2098689, -766.56872322, 0.05, 2, 0, 72009, 23009, 2, 3)
    ops.uniaxialMaterial('LimitState', 42009, 13.64638175, 6.477e-05, 40.93914525, 0.0001943, 136.46381749, 0.00064766, -13.64638175, -6.477e-05, -40.93914525, -0.0001943, -136.46381749, -0.00064766, 0.4, 0.3, 0.003, 0.0, 0.0, 22009, 2)
    ops.limitCurve('ThreePoint', 12009, 2009, 0.0, 54.585527, 0.01672817, 54.585527, 0.05018452, 38.2098689, -766.56872322, 0.05, 2, 0, 72009, 23009, 1, 3)
    ops.uniaxialMaterial('LimitState', 32009, 13.64638175, 6.477e-05, 40.93914525, 0.0001943, 136.46381749, 0.00064766, -13.64638175, -6.477e-05, -40.93914525, -0.0001943, -136.46381749, -0.00064766, 0.4, 0.3, 0.003, 0.0, 0.0, 12009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2009, 99999, 'P', 42009, 'Vy', 32009, 'Vz', 22009, 'My', 12009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172009, 72009, 172009, 2009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123009, 123009, 23009, 2009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172010, 2.9, 8.1, 6.675)
    ops.node(123010, 2.9, 8.1, 9.025)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2010, 172010, 123010, 0.0875, 29658117.37699134, 12357548.90707973, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22010, 50.05967299, 0.00065336, 60.63953911, 0.03542047, 6.06395391, 0.10283262, -50.05967299, -0.00065336, -60.63953911, -0.03542047, -6.06395391, -0.10283262, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12010, 34.3243313, 0.00084223, 41.57861021, 0.03184419, 4.15786102, 0.08320795, -34.3243313, -0.00084223, -41.57861021, -0.03184419, -4.15786102, -0.08320795, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22010, 2010, 0.0, 96.1528829, 0.01306715, 96.1528829, 0.03920145, 67.30701803, -1380.61344016, 0.05, 2, 0, 72010, 23010, 2, 3)
    ops.uniaxialMaterial('LimitState', 42010, 24.03822072, 7.736e-05, 72.11466217, 0.00023209, 240.38220724, 0.00077364, -24.03822072, -7.736e-05, -72.11466217, -0.00023209, -240.38220724, -0.00077364, 0.4, 0.3, 0.003, 0.0, 0.0, 22010, 2)
    ops.limitCurve('ThreePoint', 12010, 2010, 0.0, 84.74517717, 0.0168446, 84.74517717, 0.05053379, 59.32162402, -926.18923474, 0.05, 2, 0, 72010, 23010, 1, 3)
    ops.uniaxialMaterial('LimitState', 32010, 21.18629429, 6.819e-05, 63.55888287, 0.00020456, 211.86294291, 0.00068186, -21.18629429, -6.819e-05, -63.55888287, -0.00020456, -211.86294291, -0.00068186, 0.4, 0.3, 0.003, 0.0, 0.0, 12010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2010, 99999, 'P', 42010, 'Vy', 32010, 'Vz', 22010, 'My', 12010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172010, 72010, 172010, 2010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123010, 123010, 23010, 2010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172011, 7.9, 8.1, 6.675)
    ops.node(123011, 7.9, 8.1, 9.025)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2011, 172011, 123011, 0.1, 28733964.58742575, 11972485.24476073, 0.00127345, 0.00057292, 0.00146667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22011, 60.1185992, 0.00056938, 72.91140784, 0.03259304, 7.29114078, 0.09732366, -60.1185992, -0.00056938, -72.91140784, -0.03259304, -7.29114078, -0.09732366, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12011, 35.8928113, 0.00078325, 43.53054526, 0.02813315, 4.35305453, 0.07265625, -35.8928113, -0.00078325, -43.53054526, -0.02813315, -4.35305453, -0.07265625, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22011, 2011, 0.0, 97.27825888, 0.01138766, 97.27825888, 0.03416297, 68.09478122, -1118.55863794, 0.05, 2, 0, 72011, 23011, 2, 3)
    ops.uniaxialMaterial('LimitState', 42011, 24.31956472, 7.069e-05, 72.95869416, 0.00021207, 243.19564721, 0.00070689, -24.31956472, -7.069e-05, -72.95869416, -0.00021207, -243.19564721, -0.00070689, 0.4, 0.3, 0.003, 0.0, 0.0, 22011, 2)
    ops.limitCurve('ThreePoint', 12011, 2011, 0.0, 84.3096452, 0.01566507, 84.3096452, 0.04699522, 59.01675164, -710.36382473, 0.05, 2, 0, 72011, 23011, 1, 3)
    ops.uniaxialMaterial('LimitState', 32011, 21.0774113, 6.126e-05, 63.2322339, 0.00018379, 210.774113, 0.00061265, -21.0774113, -6.126e-05, -63.2322339, -0.00018379, -210.774113, -0.00061265, 0.4, 0.3, 0.003, 0.0, 0.0, 12011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2011, 99999, 'P', 42011, 'Vy', 32011, 'Vz', 22011, 'My', 12011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172011, 72011, 172011, 2011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123011, 123011, 23011, 2011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172012, 12.9, 8.1, 6.675)
    ops.node(123012, 12.9, 8.1, 9.025)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2012, 172012, 123012, 0.0875, 28794552.80576825, 11997730.33573677, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22012, 42.32513924, 0.00064989, 51.40550313, 0.02568147, 5.14055031, 0.08225106, -42.32513924, -0.00064989, -51.40550313, -0.02568147, -5.14055031, -0.08225106, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12012, 27.04605699, 0.00084766, 32.84847239, 0.02329488, 3.28484724, 0.06697885, -27.04605699, -0.00084766, -32.84847239, -0.02329488, -3.28484724, -0.06697885, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22012, 2012, 0.0, 90.21848932, 0.01299789, 90.21848932, 0.03899367, 63.15294252, -1325.39706134, 0.05, 2, 0, 72012, 23012, 2, 3)
    ops.uniaxialMaterial('LimitState', 42012, 22.55462233, 7.477e-05, 67.66386699, 0.0002243, 225.54622329, 0.00074767, -22.55462233, -7.477e-05, -67.66386699, -0.0002243, -225.54622329, -0.00074767, 0.4, 0.3, 0.003, 0.0, 0.0, 22012, 2)
    ops.limitCurve('ThreePoint', 12012, 2012, 0.0, 79.50447801, 0.01695312, 79.50447801, 0.05085937, 55.65313461, -878.19488435, 0.05, 2, 0, 72012, 23012, 1, 3)
    ops.uniaxialMaterial('LimitState', 32012, 19.8761195, 6.589e-05, 59.62835851, 0.00019766, 198.76119503, 0.00065888, -19.8761195, -6.589e-05, -59.62835851, -0.00019766, -198.76119503, -0.00065888, 0.4, 0.3, 0.003, 0.0, 0.0, 12012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2012, 99999, 'P', 42012, 'Vy', 32012, 'Vz', 22012, 'My', 12012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172012, 72012, 172012, 2012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123012, 123012, 23012, 2012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172013, 0.0, 12.15, 6.675)
    ops.node(123013, 0.0, 12.15, 9.025)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2013, 172013, 123013, 0.0625, 31279793.52608627, 13033247.30253595, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22013, 18.56442149, 0.00073279, 22.42168836, 0.02206236, 2.24216884, 0.08169393, -18.56442149, -0.00073279, -22.42168836, -0.02206236, -2.24216884, -0.08169393, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12013, 18.56442149, 0.00073279, 22.42168836, 0.02206236, 2.24216884, 0.08169393, -18.56442149, -0.00073279, -22.42168836, -0.02206236, -2.24216884, -0.08169393, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22013, 2013, 0.0, 57.61396576, 0.01465578, 57.61396576, 0.04396733, 40.32977603, -794.60038913, 0.05, 2, 0, 72013, 23013, 2, 3)
    ops.uniaxialMaterial('LimitState', 42013, 14.40349144, 6.153e-05, 43.21047432, 0.0001846, 144.03491439, 0.00061534, -14.40349144, -6.153e-05, -43.21047432, -0.0001846, -144.03491439, -0.00061534, 0.4, 0.3, 0.003, 0.0, 0.0, 22013, 2)
    ops.limitCurve('ThreePoint', 12013, 2013, 0.0, 57.61396576, 0.01465578, 57.61396576, 0.04396733, 40.32977603, -794.60038913, 0.05, 2, 0, 72013, 23013, 1, 3)
    ops.uniaxialMaterial('LimitState', 32013, 14.40349144, 6.153e-05, 43.21047432, 0.0001846, 144.03491439, 0.00061534, -14.40349144, -6.153e-05, -43.21047432, -0.0001846, -144.03491439, -0.00061534, 0.4, 0.3, 0.003, 0.0, 0.0, 12013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2013, 99999, 'P', 42013, 'Vy', 32013, 'Vz', 22013, 'My', 12013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172013, 72013, 172013, 2013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123013, 123013, 23013, 2013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172014, 2.9, 12.15, 6.675)
    ops.node(123014, 2.9, 12.15, 9.025)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2014, 172014, 123014, 0.0875, 29446027.70072994, 12269178.20863747, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22014, 48.21227102, 0.00061928, 58.42861801, 0.03138795, 5.8428618, 0.09851427, -48.21227102, -0.00061928, -58.42861801, -0.03138795, -5.8428618, -0.09851427, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12014, 33.14039524, 0.00078991, 40.16295962, 0.02822645, 4.01629596, 0.07937242, -33.14039524, -0.00078991, -40.16295962, -0.02822645, -4.01629596, -0.07937242, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22014, 2014, 0.0, 86.30218553, 0.01238558, 86.30218553, 0.03715674, 60.41152987, -1003.44490907, 0.05, 2, 0, 72014, 23014, 2, 3)
    ops.uniaxialMaterial('LimitState', 42014, 21.57554638, 6.994e-05, 64.72663915, 0.00020982, 215.75546384, 0.00069939, -21.57554638, -6.994e-05, -64.72663915, -0.00020982, -215.75546384, -0.00069939, 0.4, 0.3, 0.003, 0.0, 0.0, 22014, 2)
    ops.limitCurve('ThreePoint', 12014, 2014, 0.0, 77.55082612, 0.0157983, 77.55082612, 0.04739489, 54.28557829, -703.28356937, 0.05, 2, 0, 72014, 23014, 1, 3)
    ops.uniaxialMaterial('LimitState', 32014, 19.38770653, 6.285e-05, 58.16311959, 0.00018854, 193.87706531, 0.00062847, -19.38770653, -6.285e-05, -58.16311959, -0.00018854, -193.87706531, -0.00062847, 0.4, 0.3, 0.003, 0.0, 0.0, 12014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2014, 99999, 'P', 42014, 'Vy', 32014, 'Vz', 22014, 'My', 12014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172014, 72014, 172014, 2014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123014, 123014, 23014, 2014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172015, 7.9, 12.15, 6.675)
    ops.node(123015, 7.9, 12.15, 9.025)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2015, 172015, 123015, 0.1, 33985055.64515547, 14160439.85214812, 0.00127345, 0.00057292, 0.00146667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22015, 63.09653267, 0.00059576, 75.45051914, 0.02957572, 7.54505191, 0.10058598, -63.09653267, -0.00059576, -75.45051914, -0.02957572, -7.54505191, -0.10058598, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12015, 37.40282786, 0.00084117, 44.72611505, 0.02559159, 4.47261151, 0.07443395, -37.40282786, -0.00084117, -44.72611505, -0.02559159, -4.47261151, -0.07443395, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22015, 2015, 0.0, 116.12426053, 0.01191527, 116.12426053, 0.03574582, 81.28698237, -1209.75240027, 0.05, 2, 0, 72015, 23015, 2, 3)
    ops.uniaxialMaterial('LimitState', 42015, 29.03106513, 7.135e-05, 87.0931954, 0.00021404, 290.31065133, 0.00071345, -29.03106513, -7.135e-05, -87.0931954, -0.00021404, -290.31065133, -0.00071345, 0.4, 0.3, 0.003, 0.0, 0.0, 22015, 2)
    ops.limitCurve('ThreePoint', 12015, 2015, 0.0, 102.19861412, 0.01682334, 102.19861412, 0.05047003, 71.53902989, -755.59281042, 0.05, 2, 0, 72015, 23015, 1, 3)
    ops.uniaxialMaterial('LimitState', 32015, 25.54965353, 6.279e-05, 76.64896059, 0.00018837, 255.49653531, 0.0006279, -25.54965353, -6.279e-05, -76.64896059, -0.00018837, -255.49653531, -0.0006279, 0.4, 0.3, 0.003, 0.0, 0.0, 12015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2015, 99999, 'P', 42015, 'Vy', 32015, 'Vz', 22015, 'My', 12015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172015, 72015, 172015, 2015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123015, 123015, 23015, 2015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172016, 12.9, 12.15, 6.675)
    ops.node(123016, 12.9, 12.15, 9.025)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2016, 172016, 123016, 0.0875, 29503528.15808418, 12293136.73253507, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22016, 45.01851606, 0.000633, 54.59401711, 0.01920381, 5.45940171, 0.07652014, -45.01851606, -0.000633, -54.59401711, -0.01920381, -5.45940171, -0.07652014, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12016, 28.55914049, 0.00080321, 34.63370943, 0.01745669, 3.46337094, 0.06171732, -28.55914049, -0.00080321, -34.63370943, -0.01745669, -3.46337094, -0.06171732, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22016, 2016, 0.0, 80.14366264, 0.01266001, 80.14366264, 0.03798004, 56.10056385, -834.29151011, 0.05, 2, 0, 72016, 23016, 2, 3)
    ops.uniaxialMaterial('LimitState', 42016, 20.03591566, 6.482e-05, 60.10774698, 0.00019446, 200.35915661, 0.00064821, -20.03591566, -6.482e-05, -60.10774698, -0.00019446, -200.35915661, -0.00064821, 0.4, 0.3, 0.003, 0.0, 0.0, 22016, 2)
    ops.limitCurve('ThreePoint', 12016, 2016, 0.0, 61.39103779, 0.01606413, 61.39103779, 0.04819238, 42.97372646, -588.62371169, 0.05, 2, 0, 72016, 23016, 1, 3)
    ops.uniaxialMaterial('LimitState', 32016, 15.34775945, 4.965e-05, 46.04327835, 0.00014896, 153.47759449, 0.00049654, -15.34775945, -4.965e-05, -46.04327835, -0.00014896, -153.47759449, -0.00049654, 0.4, 0.3, 0.003, 0.0, 0.0, 12016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2016, 99999, 'P', 42016, 'Vy', 32016, 'Vz', 22016, 'My', 12016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172016, 72016, 172016, 2016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123016, 123016, 23016, 2016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172017, 0.0, 16.2, 6.65)
    ops.node(123017, 0.0, 16.2, 9.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2017, 172017, 123017, 0.0625, 25772694.67954928, 10738622.78314553, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22017, 18.55739325, 0.00083904, 22.72756051, 0.02205843, 2.27275605, 0.08068718, -18.55739325, -0.00083904, -22.72756051, -0.02205843, -2.27275605, -0.08068718, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12017, 18.55739325, 0.00083904, 22.72756051, 0.02205843, 2.27275605, 0.08068718, -18.55739325, -0.00083904, -22.72756051, -0.02205843, -2.27275605, -0.08068718, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22017, 2017, 0.0, 42.04332064, 0.01678072, 42.04332064, 0.05034215, 29.43032445, -722.8745481, 0.05, 2, 0, 72017, 23017, 2, 3)
    ops.uniaxialMaterial('LimitState', 42017, 10.51083016, 5.45e-05, 31.53249048, 0.0001635, 105.10830159, 0.00054499, -10.51083016, -5.45e-05, -31.53249048, -0.0001635, -105.10830159, -0.00054499, 0.4, 0.3, 0.003, 0.0, 0.0, 22017, 2)
    ops.limitCurve('ThreePoint', 12017, 2017, 0.0, 42.04332064, 0.01678072, 42.04332064, 0.05034215, 29.43032445, -722.8745481, 0.05, 2, 0, 72017, 23017, 1, 3)
    ops.uniaxialMaterial('LimitState', 32017, 10.51083016, 5.45e-05, 31.53249048, 0.0001635, 105.10830159, 0.00054499, -10.51083016, -5.45e-05, -31.53249048, -0.0001635, -105.10830159, -0.00054499, 0.4, 0.3, 0.003, 0.0, 0.0, 12017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2017, 99999, 'P', 42017, 'Vy', 32017, 'Vz', 22017, 'My', 12017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172017, 72017, 172017, 2017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123017, 123017, 23017, 2017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172018, 2.9, 16.2, 6.65)
    ops.node(123018, 2.9, 16.2, 9.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2018, 172018, 123018, 0.0625, 28325885.74358239, 11802452.39315933, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22018, 22.04095196, 0.00077131, 26.77206896, 0.02426889, 2.6772069, 0.07895114, -22.04095196, -0.00077131, -26.77206896, -0.02426889, -2.6772069, -0.07895114, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12018, 22.04095196, 0.00077131, 26.77206896, 0.02426889, 2.6772069, 0.07895114, -22.04095196, -0.00077131, -26.77206896, -0.02426889, -2.6772069, -0.07895114, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22018, 2018, 0.0, 60.48835469, 0.01542629, 60.48835469, 0.04627888, 42.34184828, -755.06857369, 0.05, 2, 0, 72018, 23018, 2, 3)
    ops.uniaxialMaterial('LimitState', 42018, 15.12208867, 7.134e-05, 45.36626602, 0.00021402, 151.22088673, 0.00071341, -15.12208867, -7.134e-05, -45.36626602, -0.00021402, -151.22088673, -0.00071341, 0.4, 0.3, 0.003, 0.0, 0.0, 22018, 2)
    ops.limitCurve('ThreePoint', 12018, 2018, 0.0, 60.48835469, 0.01542629, 60.48835469, 0.04627888, 42.34184828, -755.06857369, 0.05, 2, 0, 72018, 23018, 1, 3)
    ops.uniaxialMaterial('LimitState', 32018, 15.12208867, 7.134e-05, 45.36626602, 0.00021402, 151.22088673, 0.00071341, -15.12208867, -7.134e-05, -45.36626602, -0.00021402, -151.22088673, -0.00071341, 0.4, 0.3, 0.003, 0.0, 0.0, 12018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2018, 99999, 'P', 42018, 'Vy', 32018, 'Vz', 22018, 'My', 12018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172018, 72018, 172018, 2018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123018, 123018, 23018, 2018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172019, 7.9, 16.2, 6.65)
    ops.node(123019, 7.9, 16.2, 9.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2019, 172019, 123019, 0.0875, 32076512.75034245, 13365213.64597602, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22019, 33.08488536, 0.00079344, 39.84490503, 0.0404641, 3.9844905, 0.10878137, -33.08488536, -0.00079344, -39.84490503, -0.0404641, -3.9844905, -0.10878137, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12019, 48.18905152, 0.00062177, 58.03520731, 0.04539029, 5.80352073, 0.13639697, -48.18905152, -0.00062177, -58.03520731, -0.04539029, -5.80352073, -0.13639697, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22019, 2019, 0.0, 104.40618511, 0.01586874, 104.40618511, 0.04760622, 73.08432957, -1556.7542809, 0.05, 2, 0, 72019, 23019, 2, 3)
    ops.uniaxialMaterial('LimitState', 42019, 26.10154628, 7.767e-05, 78.30463883, 0.00023301, 261.01546276, 0.00077671, -26.10154628, -7.767e-05, -78.30463883, -0.00023301, -261.01546276, -0.00077671, 0.4, 0.3, 0.003, 0.0, 0.0, 22019, 2)
    ops.limitCurve('ThreePoint', 12019, 2019, 0.0, 121.48635218, 0.01243536, 121.48635218, 0.03730607, 85.04044652, -2506.8589342, 0.05, 2, 0, 72019, 23019, 1, 3)
    ops.uniaxialMaterial('LimitState', 32019, 30.37158804, 9.038e-05, 91.11476413, 0.00027113, 303.71588044, 0.00090378, -30.37158804, -9.038e-05, -91.11476413, -0.00027113, -303.71588044, -0.00090378, 0.4, 0.3, 0.003, 0.0, 0.0, 12019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2019, 99999, 'P', 42019, 'Vy', 32019, 'Vz', 22019, 'My', 12019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172019, 72019, 172019, 2019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123019, 123019, 23019, 2019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172020, 12.9, 16.2, 6.65)
    ops.node(123020, 12.9, 16.2, 9.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2020, 172020, 123020, 0.0625, 28593338.41509072, 11913891.0062878, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22020, 17.86105886, 0.00074945, 21.72193548, 0.02695423, 2.17219355, 0.08489135, -17.86105886, -0.00074945, -21.72193548, -0.02695423, -2.17219355, -0.08489135, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12020, 17.86105886, 0.00074945, 21.72193548, 0.02695423, 2.17219355, 0.08489135, -17.86105886, -0.00074945, -21.72193548, -0.02695423, -2.17219355, -0.08489135, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22020, 2020, 0.0, 60.57309222, 0.01498906, 60.57309222, 0.04496719, 42.40116455, -879.97932205, 0.05, 2, 0, 72020, 23020, 2, 3)
    ops.uniaxialMaterial('LimitState', 42020, 15.14327305, 7.077e-05, 45.42981916, 0.00021232, 151.43273054, 0.00070773, -15.14327305, -7.077e-05, -45.42981916, -0.00021232, -151.43273054, -0.00070773, 0.4, 0.3, 0.003, 0.0, 0.0, 22020, 2)
    ops.limitCurve('ThreePoint', 12020, 2020, 0.0, 60.57309222, 0.01498906, 60.57309222, 0.04496719, 42.40116455, -879.97932205, 0.05, 2, 0, 72020, 23020, 1, 3)
    ops.uniaxialMaterial('LimitState', 32020, 15.14327305, 7.077e-05, 45.42981916, 0.00021232, 151.43273054, 0.00070773, -15.14327305, -7.077e-05, -45.42981916, -0.00021232, -151.43273054, -0.00070773, 0.4, 0.3, 0.003, 0.0, 0.0, 12020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2020, 99999, 'P', 42020, 'Vy', 32020, 'Vz', 22020, 'My', 12020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172020, 72020, 172020, 2020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123020, 123020, 23020, 2020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173003, 7.9, 0.0, 9.55)
    ops.node(124003, 7.9, 0.0, 12.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3003, 173003, 124003, 0.0875, 24566706.71106451, 10236127.79627688, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23003, 20.16011809, 0.00077555, 24.79153613, 0.02002836, 2.47915361, 0.06769296, -20.16011809, -0.00077555, -24.79153613, -0.02002836, -2.47915361, -0.06769296, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13003, 32.811475, 0.00061138, 40.34931067, 0.02208077, 4.03493107, 0.08380517, -32.811475, -0.00061138, -40.34931067, -0.02208077, -4.03493107, -0.08380517, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23003, 3003, 0.0, 43.02447582, 0.01551098, 43.02447582, 0.04653293, 30.11713308, -797.70418632, 0.05, 2, 0, 73003, 24003, 2, 3)
    ops.uniaxialMaterial('LimitState', 43003, 10.75611896, 4.179e-05, 32.26835687, 0.00012538, 107.56118956, 0.00041792, -10.75611896, -4.179e-05, -32.26835687, -0.00012538, -107.56118956, -0.00041792, 0.4, 0.3, 0.003, 0.0, 0.0, 23003, 2)
    ops.limitCurve('ThreePoint', 13003, 3003, 0.0, 61.43671005, 0.01222755, 61.43671005, 0.03668264, 43.00569703, -1356.66588578, 0.05, 2, 0, 73003, 24003, 1, 3)
    ops.uniaxialMaterial('LimitState', 33003, 15.35917751, 5.968e-05, 46.07753254, 0.00017903, 153.59177512, 0.00059677, -15.35917751, -5.968e-05, -46.07753254, -0.00017903, -153.59177512, -0.00059677, 0.4, 0.3, 0.003, 0.0, 0.0, 13003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3003, 99999, 'P', 43003, 'Vy', 33003, 'Vz', 23003, 'My', 13003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173003, 73003, 173003, 3003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124003, 124003, 24003, 3003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173004, 12.9, 0.0, 9.55)
    ops.node(124004, 12.9, 0.0, 12.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3004, 173004, 124004, 0.0625, 27467684.32445956, 11444868.46852482, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23004, 14.18410029, 0.00069971, 17.35868743, 0.02374597, 1.73586874, 0.08794008, -14.18410029, -0.00069971, -17.35868743, -0.02374597, -1.73586874, -0.08794008, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13004, 14.18410029, 0.00069971, 17.35868743, 0.02374597, 1.73586874, 0.08794008, -14.18410029, -0.00069971, -17.35868743, -0.02374597, -1.73586874, -0.08794008, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23004, 3004, 0.0, 42.12871085, 0.01399415, 42.12871085, 0.04198246, 29.4900976, -1333.20435772, 0.05, 2, 0, 73004, 24004, 2, 3)
    ops.uniaxialMaterial('LimitState', 43004, 10.53217771, 5.124e-05, 31.59653314, 0.00015372, 105.32177714, 0.0005124, -10.53217771, -5.124e-05, -31.59653314, -0.00015372, -105.32177714, -0.0005124, 0.4, 0.3, 0.003, 0.0, 0.0, 23004, 2)
    ops.limitCurve('ThreePoint', 13004, 3004, 0.0, 42.12871085, 0.01399415, 42.12871085, 0.04198246, 29.4900976, -1333.20435772, 0.05, 2, 0, 73004, 24004, 1, 3)
    ops.uniaxialMaterial('LimitState', 33004, 10.53217771, 5.124e-05, 31.59653314, 0.00015372, 105.32177714, 0.0005124, -10.53217771, -5.124e-05, -31.59653314, -0.00015372, -105.32177714, -0.0005124, 0.4, 0.3, 0.003, 0.0, 0.0, 13004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3004, 99999, 'P', 43004, 'Vy', 33004, 'Vz', 23004, 'My', 13004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173004, 73004, 173004, 3004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124004, 124004, 24004, 3004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173005, 0.0, 4.05, 9.575)
    ops.node(124005, 0.0, 4.05, 11.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3005, 173005, 124005, 0.0625, 25527338.74841982, 10636391.14517492, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23005, 15.70265532, 0.00079666, 19.25576877, 0.02868784, 1.92557688, 0.08867646, -15.70265532, -0.00079666, -19.25576877, -0.02868784, -1.92557688, -0.08867646, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13005, 15.70265532, 0.00079666, 19.25576877, 0.02868784, 1.92557688, 0.08867646, -15.70265532, -0.00079666, -19.25576877, -0.02868784, -1.92557688, -0.08867646, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23005, 3005, 0.0, 53.83556322, 0.01593327, 53.83556322, 0.04779982, 37.68489425, -1290.19441249, 0.05, 2, 0, 73005, 24005, 2, 3)
    ops.uniaxialMaterial('LimitState', 43005, 13.4588908, 7.046e-05, 40.37667241, 0.00021137, 134.58890805, 0.00070455, -13.4588908, -7.046e-05, -40.37667241, -0.00021137, -134.58890805, -0.00070455, 0.4, 0.3, 0.003, 0.0, 0.0, 23005, 2)
    ops.limitCurve('ThreePoint', 13005, 3005, 0.0, 53.83556322, 0.01593327, 53.83556322, 0.04779982, 37.68489425, -1290.19441249, 0.05, 2, 0, 73005, 24005, 1, 3)
    ops.uniaxialMaterial('LimitState', 33005, 13.4588908, 7.046e-05, 40.37667241, 0.00021137, 134.58890805, 0.00070455, -13.4588908, -7.046e-05, -40.37667241, -0.00021137, -134.58890805, -0.00070455, 0.4, 0.3, 0.003, 0.0, 0.0, 13005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3005, 99999, 'P', 43005, 'Vy', 33005, 'Vz', 23005, 'My', 13005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173005, 73005, 173005, 3005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124005, 124005, 24005, 3005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173006, 2.9, 4.05, 9.575)
    ops.node(124006, 2.9, 4.05, 11.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3006, 173006, 124006, 0.0875, 36592168.11400838, 15246736.71417016, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23006, 38.81659044, 0.00062845, 46.03176319, 0.01830214, 4.60317632, 0.07423249, -38.81659044, -0.00062845, -46.03176319, -0.01830214, -4.60317632, -0.07423249, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13006, 26.2404299, 0.00083071, 31.11796377, 0.016761, 3.11179638, 0.06047875, -26.2404299, -0.00083071, -31.11796377, -0.016761, -3.11179638, -0.06047875, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23006, 3006, 0.0, 86.82377586, 0.01256896, 86.82377586, 0.03770687, 60.7766431, -788.30687454, 0.05, 2, 0, 73006, 24006, 2, 3)
    ops.uniaxialMaterial('LimitState', 43006, 21.70594396, 5.662e-05, 65.11783189, 0.00016986, 217.05943965, 0.0005662, -21.70594396, -5.662e-05, -65.11783189, -0.00016986, -217.05943965, -0.0005662, 0.4, 0.3, 0.003, 0.0, 0.0, 23006, 2)
    ops.limitCurve('ThreePoint', 13006, 3006, 0.0, 69.50605306, 0.01661422, 69.50605306, 0.04984265, 48.65423714, -510.42549167, 0.05, 2, 0, 73006, 24006, 1, 3)
    ops.uniaxialMaterial('LimitState', 33006, 17.37651326, 4.533e-05, 52.12953979, 0.00013598, 173.76513264, 0.00045327, -17.37651326, -4.533e-05, -52.12953979, -0.00013598, -173.76513264, -0.00045327, 0.4, 0.3, 0.003, 0.0, 0.0, 13006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3006, 99999, 'P', 43006, 'Vy', 33006, 'Vz', 23006, 'My', 13006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173006, 73006, 173006, 3006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124006, 124006, 24006, 3006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173007, 7.9, 4.05, 9.575)
    ops.node(124007, 7.9, 4.05, 11.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3007, 173007, 124007, 0.1, 34624495.45849802, 14426873.10770751, 0.00127345, 0.00057292, 0.00146667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23007, 50.13090726, 0.00055315, 59.96550015, 0.02184648, 5.99655002, 0.07776999, -50.13090726, -0.00055315, -59.96550015, -0.02184648, -5.99655002, -0.07776999, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13007, 29.86729797, 0.00074381, 35.72661177, 0.01921417, 3.57266118, 0.05912352, -29.86729797, -0.00074381, -35.72661177, -0.01921417, -3.57266118, -0.05912352, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23007, 3007, 0.0, 97.90740087, 0.01106307, 97.90740087, 0.03318922, 68.53518061, -1065.07001694, 0.05, 2, 0, 73007, 24007, 2, 3)
    ops.uniaxialMaterial('LimitState', 43007, 24.47685022, 5.904e-05, 73.43055065, 0.00017713, 244.76850218, 0.00059042, -24.47685022, -5.904e-05, -73.43055065, -0.00017713, -244.76850218, -0.00059042, 0.4, 0.3, 0.003, 0.0, 0.0, 23007, 2)
    ops.limitCurve('ThreePoint', 13007, 3007, 0.0, 75.82897138, 0.01487627, 75.82897138, 0.0446288, 53.08027997, -559.31684433, 0.05, 2, 0, 73007, 24007, 1, 3)
    ops.uniaxialMaterial('LimitState', 33007, 18.95724285, 4.573e-05, 56.87172854, 0.00013718, 189.57242845, 0.00045728, -18.95724285, -4.573e-05, -56.87172854, -0.00013718, -189.57242845, -0.00045728, 0.4, 0.3, 0.003, 0.0, 0.0, 13007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3007, 99999, 'P', 43007, 'Vy', 33007, 'Vz', 23007, 'My', 13007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173007, 73007, 173007, 3007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124007, 124007, 24007, 3007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173008, 12.9, 4.05, 9.575)
    ops.node(124008, 12.9, 4.05, 11.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3008, 173008, 124008, 0.0875, 31511266.33273635, 13129694.30530681, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23008, 32.12114859, 0.00056659, 38.86974368, 0.02644883, 3.88697437, 0.09103606, -32.12114859, -0.00056659, -38.86974368, -0.02644883, -3.88697437, -0.09103606, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13008, 19.89063784, 0.0007113, 24.06962479, 0.02392135, 2.40696248, 0.07379668, -19.89063784, -0.0007113, -24.06962479, -0.02392135, -2.40696248, -0.07379668, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23008, 3008, 0.0, 89.22959884, 0.01133188, 89.22959884, 0.03399563, 62.46071919, -2421.0927054, 0.05, 2, 0, 73008, 24008, 2, 3)
    ops.uniaxialMaterial('LimitState', 43008, 22.30739971, 6.757e-05, 66.92219913, 0.00020272, 223.07399709, 0.00067572, -22.30739971, -6.757e-05, -66.92219913, -0.00020272, -223.07399709, -0.00067572, 0.4, 0.3, 0.003, 0.0, 0.0, 23008, 2)
    ops.limitCurve('ThreePoint', 13008, 3008, 0.0, 78.9543473, 0.01422597, 78.9543473, 0.04267791, 55.26804311, -1375.85647278, 0.05, 2, 0, 73008, 24008, 1, 3)
    ops.uniaxialMaterial('LimitState', 33008, 19.73858682, 5.979e-05, 59.21576047, 0.00017937, 197.38586824, 0.00059791, -19.73858682, -5.979e-05, -59.21576047, -0.00017937, -197.38586824, -0.00059791, 0.4, 0.3, 0.003, 0.0, 0.0, 13008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3008, 99999, 'P', 43008, 'Vy', 33008, 'Vz', 23008, 'My', 13008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173008, 73008, 173008, 3008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124008, 124008, 24008, 3008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173009, 0.0, 8.1, 9.575)
    ops.node(124009, 0.0, 8.1, 11.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3009, 173009, 124009, 0.0625, 29896485.92744083, 12456869.13643368, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23009, 15.08537711, 0.00088717, 18.34702292, 0.02323496, 1.83470229, 0.08785214, -15.08537711, -0.00088717, -18.34702292, -0.02323496, -1.83470229, -0.08785214, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13009, 15.08537711, 0.00088717, 18.34702292, 0.02323496, 1.83470229, 0.08785214, -15.08537711, -0.00088717, -18.34702292, -0.02323496, -1.83470229, -0.08785214, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23009, 3009, 0.0, 53.48270253, 0.01774332, 53.48270253, 0.05322996, 37.43789177, -1387.23361364, 0.05, 2, 0, 73009, 24009, 2, 3)
    ops.uniaxialMaterial('LimitState', 43009, 13.37067563, 5.976e-05, 40.1120269, 0.00017929, 133.70675632, 0.00059765, -13.37067563, -5.976e-05, -40.1120269, -0.00017929, -133.70675632, -0.00059765, 0.4, 0.3, 0.003, 0.0, 0.0, 23009, 2)
    ops.limitCurve('ThreePoint', 13009, 3009, 0.0, 53.48270253, 0.01774332, 53.48270253, 0.05322996, 37.43789177, -1387.23361364, 0.05, 2, 0, 73009, 24009, 1, 3)
    ops.uniaxialMaterial('LimitState', 33009, 13.37067563, 5.976e-05, 40.1120269, 0.00017929, 133.70675632, 0.00059765, -13.37067563, -5.976e-05, -40.1120269, -0.00017929, -133.70675632, -0.00059765, 0.4, 0.3, 0.003, 0.0, 0.0, 13009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3009, 99999, 'P', 43009, 'Vy', 33009, 'Vz', 23009, 'My', 13009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173009, 73009, 173009, 3009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124009, 124009, 24009, 3009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173010, 2.9, 8.1, 9.575)
    ops.node(124010, 2.9, 8.1, 11.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3010, 173010, 124010, 0.0875, 31172226.01967587, 12988427.50819828, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23010, 41.98450379, 0.00068799, 50.8420168, 0.02324907, 5.08420168, 0.07860568, -41.98450379, -0.00068799, -50.8420168, -0.02324907, -5.08420168, -0.07860568, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13010, 28.34369105, 0.00090368, 34.32338807, 0.02123925, 3.43233881, 0.06450853, -28.34369105, -0.00090368, -34.32338807, -0.02123925, -3.43233881, -0.06450853, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23010, 3010, 0.0, 79.13562668, 0.01375988, 79.13562668, 0.04127964, 55.39493868, -1214.34632998, 0.05, 2, 0, 73010, 24010, 2, 3)
    ops.uniaxialMaterial('LimitState', 43010, 19.78390667, 6.058e-05, 59.35172001, 0.00018174, 197.83906671, 0.0006058, -19.78390667, -6.058e-05, -59.35172001, -0.00018174, -197.83906671, -0.0006058, 0.4, 0.3, 0.003, 0.0, 0.0, 23010, 2)
    ops.limitCurve('ThreePoint', 13010, 3010, 0.0, 60.58476787, 0.01807369, 60.58476787, 0.05422108, 42.40933751, -733.74516906, 0.05, 2, 0, 73010, 24010, 1, 3)
    ops.uniaxialMaterial('LimitState', 33010, 15.14619197, 4.638e-05, 45.4385759, 0.00013914, 151.46191967, 0.00046379, -15.14619197, -4.638e-05, -45.4385759, -0.00013914, -151.46191967, -0.00046379, 0.4, 0.3, 0.003, 0.0, 0.0, 13010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3010, 99999, 'P', 43010, 'Vy', 33010, 'Vz', 23010, 'My', 13010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173010, 73010, 173010, 3010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124010, 124010, 24010, 3010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173011, 7.9, 8.1, 9.575)
    ops.node(124011, 7.9, 8.1, 11.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3011, 173011, 124011, 0.1, 26799022.0559676, 11166259.1899865, 0.00127345, 0.00057292, 0.00146667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23011, 46.29183744, 0.00062493, 56.65476988, 0.02755338, 5.66547699, 0.08074378, -46.29183744, -0.00062493, -56.65476988, -0.02755338, -5.66547699, -0.08074378, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13011, 26.75677124, 0.00090987, 32.74656615, 0.02426828, 3.27465662, 0.06222716, -26.75677124, -0.00090987, -32.74656615, -0.02426828, -3.27465662, -0.06222716, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23011, 3011, 0.0, 79.48595029, 0.01249857, 79.48595029, 0.03749572, 55.6401652, -1392.74305511, 0.05, 2, 0, 73011, 24011, 2, 3)
    ops.uniaxialMaterial('LimitState', 43011, 19.87148757, 6.193e-05, 59.61446272, 0.00018579, 198.71487572, 0.0006193, -19.87148757, -6.193e-05, -59.61446272, -0.00018579, -198.71487572, -0.0006193, 0.4, 0.3, 0.003, 0.0, 0.0, 23011, 2)
    ops.limitCurve('ThreePoint', 13011, 3011, 0.0, 61.67835931, 0.01819738, 61.67835931, 0.05459215, 43.17485152, -706.35922325, 0.05, 2, 0, 73011, 24011, 1, 3)
    ops.uniaxialMaterial('LimitState', 33011, 15.41958983, 4.806e-05, 46.25876949, 0.00014417, 154.19589828, 0.00048056, -15.41958983, -4.806e-05, -46.25876949, -0.00014417, -154.19589828, -0.00048056, 0.4, 0.3, 0.003, 0.0, 0.0, 13011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3011, 99999, 'P', 43011, 'Vy', 33011, 'Vz', 23011, 'My', 13011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173011, 73011, 173011, 3011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124011, 124011, 24011, 3011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173012, 12.9, 8.1, 9.575)
    ops.node(124012, 12.9, 8.1, 11.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3012, 173012, 124012, 0.0875, 27813026.13951048, 11588760.8914627, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23012, 31.23424989, 0.00064117, 38.17689077, 0.02334427, 3.81768908, 0.08674766, -31.23424989, -0.00064117, -38.17689077, -0.02334427, -3.81768908, -0.08674766, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13012, 19.56309659, 0.0008487, 23.91151395, 0.02120786, 2.39115139, 0.070169, -19.56309659, -0.0008487, -23.91151395, -0.02120786, -2.39115139, -0.070169, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23012, 3012, 0.0, 69.32435637, 0.0128233, 69.32435637, 0.03846991, 48.52704946, -1362.59946476, 0.05, 2, 0, 73012, 24012, 2, 3)
    ops.uniaxialMaterial('LimitState', 43012, 17.33108909, 5.948e-05, 51.99326728, 0.00017844, 173.31089092, 0.00059479, -17.33108909, -5.948e-05, -51.99326728, -0.00017844, -173.31089092, -0.00059479, 0.4, 0.3, 0.003, 0.0, 0.0, 23012, 2)
    ops.limitCurve('ThreePoint', 13012, 3012, 0.0, 56.71731398, 0.01697409, 56.71731398, 0.05092228, 39.70211979, -801.63242183, 0.05, 2, 0, 73012, 24012, 1, 3)
    ops.uniaxialMaterial('LimitState', 33012, 14.1793285, 4.866e-05, 42.53798549, 0.00014599, 141.79328495, 0.00048662, -14.1793285, -4.866e-05, -42.53798549, -0.00014599, -141.79328495, -0.00048662, 0.4, 0.3, 0.003, 0.0, 0.0, 13012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3012, 99999, 'P', 43012, 'Vy', 33012, 'Vz', 23012, 'My', 13012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173012, 73012, 173012, 3012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124012, 124012, 24012, 3012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173013, 0.0, 12.15, 9.575)
    ops.node(124013, 0.0, 12.15, 11.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3013, 173013, 124013, 0.0625, 29369268.79381506, 12237195.33075627, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23013, 15.11656026, 0.00074999, 18.41138665, 0.02379254, 1.84113866, 0.08827018, -15.11656026, -0.00074999, -18.41138665, -0.02379254, -1.84113866, -0.08827018, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13013, 15.11656026, 0.00074999, 18.41138665, 0.02379254, 1.84113866, 0.08827018, -15.11656026, -0.00074999, -18.41138665, -0.02379254, -1.84113866, -0.08827018, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23013, 3013, 0.0, 51.46182124, 0.0149997, 51.46182124, 0.04499911, 36.02327487, -1408.57149289, 0.05, 2, 0, 73013, 24013, 2, 3)
    ops.uniaxialMaterial('LimitState', 43013, 12.86545531, 5.854e-05, 38.59636593, 0.00017562, 128.65455311, 0.00058539, -12.86545531, -5.854e-05, -38.59636593, -0.00017562, -128.65455311, -0.00058539, 0.4, 0.3, 0.003, 0.0, 0.0, 23013, 2)
    ops.limitCurve('ThreePoint', 13013, 3013, 0.0, 51.46182124, 0.0149997, 51.46182124, 0.04499911, 36.02327487, -1408.57149289, 0.05, 2, 0, 73013, 24013, 1, 3)
    ops.uniaxialMaterial('LimitState', 33013, 12.86545531, 5.854e-05, 38.59636593, 0.00017562, 128.65455311, 0.00058539, -12.86545531, -5.854e-05, -38.59636593, -0.00017562, -128.65455311, -0.00058539, 0.4, 0.3, 0.003, 0.0, 0.0, 13013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3013, 99999, 'P', 43013, 'Vy', 33013, 'Vz', 23013, 'My', 13013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173013, 73013, 173013, 3013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124013, 124013, 24013, 3013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173014, 2.9, 12.15, 9.575)
    ops.node(124014, 2.9, 12.15, 11.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3014, 173014, 124014, 0.0875, 28259832.3644033, 11774930.15183471, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23014, 38.90174756, 0.00067481, 47.47727741, 0.02604393, 4.74772774, 0.08039643, -38.90174756, -0.00067481, -47.47727741, -0.02604393, -4.74772774, -0.08039643, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13014, 26.18798056, 0.00089061, 31.96087826, 0.02375722, 3.19608783, 0.06624164, -26.18798056, -0.00089061, -31.96087826, -0.02375722, -3.19608783, -0.06624164, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23014, 3014, 0.0, 71.93211225, 0.01349625, 71.93211225, 0.04048876, 50.35247858, -1234.66294186, 0.05, 2, 0, 73014, 24014, 2, 3)
    ops.uniaxialMaterial('LimitState', 43014, 17.98302806, 6.074e-05, 53.94908419, 0.00018222, 179.83028064, 0.0006074, -17.98302806, -6.074e-05, -53.94908419, -0.00018222, -179.83028064, -0.0006074, 0.4, 0.3, 0.003, 0.0, 0.0, 23014, 2)
    ops.limitCurve('ThreePoint', 13014, 3014, 0.0, 56.70457183, 0.01781224, 56.70457183, 0.05343672, 39.69320028, -745.02177698, 0.05, 2, 0, 73014, 24014, 1, 3)
    ops.uniaxialMaterial('LimitState', 33014, 14.17614296, 4.788e-05, 42.52842887, 0.00014365, 141.76142957, 0.00047882, -14.17614296, -4.788e-05, -42.52842887, -0.00014365, -141.76142957, -0.00047882, 0.4, 0.3, 0.003, 0.0, 0.0, 13014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3014, 99999, 'P', 43014, 'Vy', 33014, 'Vz', 23014, 'My', 13014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173014, 73014, 173014, 3014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124014, 124014, 24014, 3014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173015, 7.9, 12.15, 9.575)
    ops.node(124015, 7.9, 12.15, 11.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3015, 173015, 124015, 0.1, 25092554.09734902, 10455230.87389543, 0.00127345, 0.00057292, 0.00146667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23015, 49.6654587, 0.00063217, 60.95816375, 0.02258297, 6.09581637, 0.0746474, -49.6654587, -0.00063217, -60.95816375, -0.02258297, -6.09581637, -0.0746474, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13015, 29.09096071, 0.0008926, 35.70553042, 0.01993326, 3.57055304, 0.05708861, -29.09096071, -0.0008926, -35.70553042, -0.01993326, -3.57055304, -0.05708861, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23015, 3015, 0.0, 68.91280237, 0.01264349, 68.91280237, 0.03793046, 48.23896166, -1009.89343779, 0.05, 2, 0, 73015, 24015, 2, 3)
    ops.uniaxialMaterial('LimitState', 43015, 17.22820059, 5.734e-05, 51.68460178, 0.00017203, 172.28200593, 0.00057344, -17.22820059, -5.734e-05, -51.68460178, -0.00017203, -172.28200593, -0.00057344, 0.4, 0.3, 0.003, 0.0, 0.0, 23015, 2)
    ops.limitCurve('ThreePoint', 13015, 3015, 0.0, 43.95553366, 0.01785205, 43.95553366, 0.05355615, 30.76887356, -534.28065334, 0.05, 2, 0, 73015, 24015, 1, 3)
    ops.uniaxialMaterial('LimitState', 33015, 10.98888342, 3.658e-05, 32.96665025, 0.00010973, 109.88883415, 0.00036576, -10.98888342, -3.658e-05, -32.96665025, -0.00010973, -109.88883415, -0.00036576, 0.4, 0.3, 0.003, 0.0, 0.0, 13015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3015, 99999, 'P', 43015, 'Vy', 33015, 'Vz', 23015, 'My', 13015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173015, 73015, 173015, 3015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124015, 124015, 24015, 3015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173016, 12.9, 12.15, 9.575)
    ops.node(124016, 12.9, 12.15, 11.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3016, 173016, 124016, 0.0875, 35362482.30750161, 14734367.62812567, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23016, 32.10041695, 0.00062551, 38.2947704, 0.02061828, 3.82947704, 0.08594854, -32.10041695, -0.00062551, -38.2947704, -0.02061828, -3.82947704, -0.08594854, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13016, 20.3226123, 0.0008267, 24.24422627, 0.01875533, 2.42442263, 0.06920445, -20.3226123, -0.0008267, -24.24422627, -0.01875533, -2.42442263, -0.06920445, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23016, 3016, 0.0, 91.8074085, 0.01251024, 91.8074085, 0.03753071, 64.26518595, -1572.03321711, 0.05, 2, 0, 73016, 24016, 2, 3)
    ops.uniaxialMaterial('LimitState', 43016, 22.95185212, 6.195e-05, 68.85555637, 0.00018586, 229.51852125, 0.00061952, -22.95185212, -6.195e-05, -68.85555637, -0.00018586, -229.51852125, -0.00061952, 0.4, 0.3, 0.003, 0.0, 0.0, 23016, 2)
    ops.limitCurve('ThreePoint', 13016, 3016, 0.0, 80.3958475, 0.016534, 80.3958475, 0.04960199, 56.27709325, -916.09252938, 0.05, 2, 0, 73016, 24016, 1, 3)
    ops.uniaxialMaterial('LimitState', 33016, 20.09896188, 5.425e-05, 60.29688563, 0.00016276, 200.98961875, 0.00054252, -20.09896188, -5.425e-05, -60.29688563, -0.00016276, -200.98961875, -0.00054252, 0.4, 0.3, 0.003, 0.0, 0.0, 13016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3016, 99999, 'P', 43016, 'Vy', 33016, 'Vz', 23016, 'My', 13016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173016, 73016, 173016, 3016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124016, 124016, 24016, 3016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173017, 0.0, 16.2, 9.55)
    ops.node(124017, 0.0, 16.2, 12.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3017, 173017, 124017, 0.0625, 28824854.15998087, 12010355.89999203, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23017, 12.81428743, 0.00084272, 15.63875364, 0.02613792, 1.56387536, 0.09162087, -12.81428743, -0.00084272, -15.63875364, -0.02613792, -1.56387536, -0.09162087, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13017, 12.81428743, 0.00084272, 15.63875364, 0.02613792, 1.56387536, 0.09162087, -12.81428743, -0.00084272, -15.63875364, -0.02613792, -1.56387536, -0.09162087, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23017, 3017, 0.0, 53.3426338, 0.01685441, 53.3426338, 0.05056322, 37.33984366, -2300.72747749, 0.05, 2, 0, 73017, 24017, 2, 3)
    ops.uniaxialMaterial('LimitState', 43017, 13.33565845, 6.182e-05, 40.00697535, 0.00018547, 133.35658449, 0.00061824, -13.33565845, -6.182e-05, -40.00697535, -0.00018547, -133.35658449, -0.00061824, 0.4, 0.3, 0.003, 0.0, 0.0, 23017, 2)
    ops.limitCurve('ThreePoint', 13017, 3017, 0.0, 53.3426338, 0.01685441, 53.3426338, 0.05056322, 37.33984366, -2300.72747749, 0.05, 2, 0, 73017, 24017, 1, 3)
    ops.uniaxialMaterial('LimitState', 33017, 13.33565845, 6.182e-05, 40.00697535, 0.00018547, 133.35658449, 0.00061824, -13.33565845, -6.182e-05, -40.00697535, -0.00018547, -133.35658449, -0.00061824, 0.4, 0.3, 0.003, 0.0, 0.0, 13017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3017, 99999, 'P', 43017, 'Vy', 33017, 'Vz', 23017, 'My', 13017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173017, 73017, 173017, 3017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124017, 124017, 24017, 3017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173018, 2.9, 16.2, 9.55)
    ops.node(124018, 2.9, 16.2, 12.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3018, 173018, 124018, 0.0625, 29236521.01994664, 12181883.7583111, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23018, 14.41466258, 0.00068844, 17.55596857, 0.02811526, 1.75559686, 0.09182737, -14.41466258, -0.00068844, -17.55596857, -0.02811526, -1.75559686, -0.09182737, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13018, 14.41466258, 0.00068844, 17.55596857, 0.02811526, 1.75559686, 0.09182737, -14.41466258, -0.00068844, -17.55596857, -0.02811526, -1.75559686, -0.09182737, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23018, 3018, 0.0, 57.48198758, 0.01376885, 57.48198758, 0.04130656, 40.23739131, -1413.37793059, 0.05, 2, 0, 73018, 24018, 2, 3)
    ops.uniaxialMaterial('LimitState', 43018, 14.3704969, 6.568e-05, 43.11149069, 0.00019705, 143.70496896, 0.00065684, -14.3704969, -6.568e-05, -43.11149069, -0.00019705, -143.70496896, -0.00065684, 0.4, 0.3, 0.003, 0.0, 0.0, 23018, 2)
    ops.limitCurve('ThreePoint', 13018, 3018, 0.0, 57.48198758, 0.01376885, 57.48198758, 0.04130656, 40.23739131, -1413.37793059, 0.05, 2, 0, 73018, 24018, 1, 3)
    ops.uniaxialMaterial('LimitState', 33018, 14.3704969, 6.568e-05, 43.11149069, 0.00019705, 143.70496896, 0.00065684, -14.3704969, -6.568e-05, -43.11149069, -0.00019705, -143.70496896, -0.00065684, 0.4, 0.3, 0.003, 0.0, 0.0, 13018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3018, 99999, 'P', 43018, 'Vy', 33018, 'Vz', 23018, 'My', 13018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173018, 73018, 173018, 3018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124018, 124018, 24018, 3018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173019, 7.9, 16.2, 9.55)
    ops.node(124019, 7.9, 16.2, 12.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3019, 173019, 124019, 0.0875, 28031039.67788171, 11679599.86578405, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23019, 24.17836075, 0.00086675, 29.53861828, 0.02265703, 2.95386183, 0.06571199, -24.17836075, -0.00086675, -29.53861828, -0.02265703, -2.95386183, -0.06571199, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13019, 36.01463559, 0.00065567, 43.99895362, 0.02483067, 4.39989536, 0.07991308, -36.01463559, -0.00065567, -43.99895362, -0.02483067, -4.39989536, -0.07991308, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23019, 3019, 0.0, 48.8727621, 0.01733495, 48.8727621, 0.05200485, 34.21093347, -808.71319142, 0.05, 2, 0, 73019, 24019, 2, 3)
    ops.uniaxialMaterial('LimitState', 43019, 12.21819053, 4.161e-05, 36.65457158, 0.00012482, 122.18190526, 0.00041605, -12.21819053, -4.161e-05, -36.65457158, -0.00012482, -122.18190526, -0.00041605, 0.4, 0.3, 0.003, 0.0, 0.0, 23019, 2)
    ops.limitCurve('ThreePoint', 13019, 3019, 0.0, 69.86650795, 0.01311333, 69.86650795, 0.03933999, 48.90655557, -1376.77074469, 0.05, 2, 0, 73019, 24019, 1, 3)
    ops.uniaxialMaterial('LimitState', 33019, 17.46662699, 5.948e-05, 52.39988096, 0.00017843, 174.66626988, 0.00059477, -17.46662699, -5.948e-05, -52.39988096, -0.00017843, -174.66626988, -0.00059477, 0.4, 0.3, 0.003, 0.0, 0.0, 13019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3019, 99999, 'P', 43019, 'Vy', 33019, 'Vz', 23019, 'My', 13019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173019, 73019, 173019, 3019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124019, 124019, 24019, 3019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173020, 12.9, 16.2, 9.55)
    ops.node(124020, 12.9, 16.2, 12.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3020, 173020, 124020, 0.0625, 27564927.46444438, 11485386.44351849, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23020, 14.59662291, 0.00071163, 17.85964906, 0.02850226, 1.78596491, 0.09272792, -14.59662291, -0.00071163, -17.85964906, -0.02850226, -1.78596491, -0.09272792, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13020, 14.59662291, 0.00071163, 17.85964906, 0.02850226, 1.78596491, 0.09272792, -14.59662291, -0.00071163, -17.85964906, -0.02850226, -1.78596491, -0.09272792, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23020, 3020, 0.0, 56.31314209, 0.01423267, 56.31314209, 0.04269802, 39.41919946, -2216.81327618, 0.05, 2, 0, 73020, 24020, 2, 3)
    ops.uniaxialMaterial('LimitState', 43020, 14.07828552, 6.825e-05, 42.23485656, 0.00020475, 140.78285521, 0.0006825, -14.07828552, -6.825e-05, -42.23485656, -0.00020475, -140.78285521, -0.0006825, 0.4, 0.3, 0.003, 0.0, 0.0, 23020, 2)
    ops.limitCurve('ThreePoint', 13020, 3020, 0.0, 56.31314209, 0.01423267, 56.31314209, 0.04269802, 39.41919946, -2216.81327618, 0.05, 2, 0, 73020, 24020, 1, 3)
    ops.uniaxialMaterial('LimitState', 33020, 14.07828552, 6.825e-05, 42.23485656, 0.00020475, 140.78285521, 0.0006825, -14.07828552, -6.825e-05, -42.23485656, -0.00020475, -140.78285521, -0.0006825, 0.4, 0.3, 0.003, 0.0, 0.0, 13020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3020, 99999, 'P', 43020, 'Vy', 33020, 'Vz', 23020, 'My', 13020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173020, 73020, 173020, 3020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124020, 124020, 24020, 3020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170001, 0.0, 0.0, 0.0)
    ops.node(124021, 0.0, 0.0, 1.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4052, 170001, 124021, 0.0625, 28464197.13391232, 11860082.13913013, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24052, 29.0885103, 0.00066006, 35.20914824, 0.03522362, 3.52091482, 0.1116797, -29.0885103, -0.00066006, -35.20914824, -0.03522362, -3.52091482, -0.1116797, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14052, 27.0554284, 0.00066006, 32.74827688, 0.03522362, 3.27482769, 0.1116797, -27.0554284, -0.00066006, -32.74827688, -0.03522362, -3.27482769, -0.1116797, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24052, 4052, 0.0, 74.01028414, 0.01320119, 74.01028414, 0.03960356, 51.8071989, -1796.19839881, 0.05, 2, 0, 70001, 24021, 2, 3)
    ops.uniaxialMaterial('LimitState', 44052, 18.50257104, 5.242e-05, 55.50771311, 0.00015726, 185.02571036, 0.00052418, -18.50257104, -5.242e-05, -55.50771311, -0.00015726, -185.02571036, -0.00052418, 0.4, 0.3, 0.003, 0.0, 0.0, 24052, 2)
    ops.limitCurve('ThreePoint', 14052, 4052, 0.0, 74.01028414, 0.01320119, 74.01028414, 0.03960356, 51.8071989, -1796.19839881, 0.05, 2, 0, 70001, 24021, 1, 3)
    ops.uniaxialMaterial('LimitState', 34052, 18.50257104, 5.242e-05, 55.50771311, 0.00015726, 185.02571036, 0.00052418, -18.50257104, -5.242e-05, -55.50771311, -0.00015726, -185.02571036, -0.00052418, 0.4, 0.3, 0.003, 0.0, 0.0, 14052, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4052, 99999, 'P', 44052, 'Vy', 34052, 'Vz', 24052, 'My', 14052, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170001, 70001, 170001, 4052, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124021, 124021, 24021, 4052, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174021, 0.0, 0.0, 1.95)
    ops.node(121001, 0.0, 0.0, 3.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4053, 174021, 121001, 0.0625, 31852347.73594449, 13271811.55664354, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24053, 29.67426747, 0.00067224, 35.70947409, 0.05243137, 3.57094741, 0.15243137, -29.67426747, -0.00067224, -35.70947409, -0.05243137, -3.57094741, -0.15243137, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14053, 27.41030379, 0.00067224, 32.98506136, 0.05243137, 3.29850614, 0.15243137, -27.41030379, -0.00067224, -32.98506136, -0.05243137, -3.29850614, -0.15243137, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24053, 4053, 0.0, 97.48615295, 0.0134448, 97.48615295, 0.04033439, 68.24030706, -3414.98898641, 0.05, 2, 0, 74021, 21001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44053, 24.37153824, 6.17e-05, 73.11461471, 0.0001851, 243.71538237, 0.00061701, -24.37153824, -6.17e-05, -73.11461471, -0.0001851, -243.71538237, -0.00061701, 0.4, 0.3, 0.003, 0.0, 0.0, 24053, 2)
    ops.limitCurve('ThreePoint', 14053, 4053, 0.0, 97.48615295, 0.0134448, 97.48615295, 0.04033439, 68.24030706, -3414.98898641, 0.05, 2, 0, 74021, 21001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34053, 24.37153824, 6.17e-05, 73.11461471, 0.0001851, 243.71538237, 0.00061701, -24.37153824, -6.17e-05, -73.11461471, -0.0001851, -243.71538237, -0.00061701, 0.4, 0.3, 0.003, 0.0, 0.0, 14053, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4053, 99999, 'P', 44053, 'Vy', 34053, 'Vz', 24053, 'My', 14053, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174021, 74021, 174021, 4053, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121001, 121001, 21001, 4053, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170002, 2.9, 0.0, 0.0)
    ops.node(124022, 2.9, 0.0, 1.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4054, 170002, 124022, 0.14, 30923534.85695134, 12884806.19039639, 0.00271929, 0.00205333, 0.00157208, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24054, 103.93712808, 0.00058718, 125.33784568, 0.05339523, 12.53378457, 0.15339523, -103.93712808, -0.00058718, -125.33784568, -0.05339523, -12.53378457, -0.15339523, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14054, 102.93051204, 0.00055432, 124.12396678, 0.04819442, 12.41239668, 0.13795073, -102.93051204, -0.00055432, -124.12396678, -0.04819442, -12.41239668, -0.13795073, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24054, 4054, 0.0, 192.60698164, 0.01174351, 192.60698164, 0.03523053, 134.82488715, -3546.4825111, 0.05, 2, 0, 70002, 24022, 2, 3)
    ops.uniaxialMaterial('LimitState', 44054, 48.15174541, 5.606e-05, 144.45523623, 0.00016817, 481.5174541, 0.00056056, -48.15174541, -5.606e-05, -144.45523623, -0.00016817, -481.5174541, -0.00056056, 0.4, 0.3, 0.003, 0.0, 0.0, 24054, 2)
    ops.limitCurve('ThreePoint', 14054, 4054, 0.0, 257.27297473, 0.01108649, 257.27297473, 0.03325946, 180.09108231, -7078.02688523, 0.05, 2, 0, 70002, 24022, 1, 3)
    ops.uniaxialMaterial('LimitState', 34054, 64.31824368, 7.488e-05, 192.95473105, 0.00022463, 643.18243682, 0.00074877, -64.31824368, -7.488e-05, -192.95473105, -0.00022463, -643.18243682, -0.00074877, 0.4, 0.3, 0.003, 0.0, 0.0, 14054, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4054, 99999, 'P', 44054, 'Vy', 34054, 'Vz', 24054, 'My', 14054, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170002, 70002, 170002, 4054, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124022, 124022, 24022, 4054, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174022, 2.9, 0.0, 1.95)
    ops.node(121002, 2.9, 0.0, 3.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4055, 174022, 121002, 0.14, 28412699.67988437, 11838624.86661849, 0.00271929, 0.00205333, 0.00157208, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24055, 79.68159509, 0.00058247, 96.65523629, 0.05734476, 9.66552363, 0.15734476, -79.68159509, -0.00058247, -96.65523629, -0.05734476, -9.66552363, -0.15734476, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14055, 84.43711118, 0.00054924, 102.42376452, 0.0517566, 10.24237645, 0.13802313, -84.43711118, -0.00054924, -102.42376452, -0.0517566, -10.24237645, -0.13802313, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24055, 4055, 0.0, 186.67060758, 0.01164947, 186.67060758, 0.0349484, 130.66942531, -4302.47251573, 0.05, 2, 0, 74022, 21002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44055, 46.6676519, 5.913e-05, 140.00295569, 0.00017739, 466.67651895, 0.0005913, -46.6676519, -5.913e-05, -140.00295569, -0.00017739, -466.67651895, -0.0005913, 0.4, 0.3, 0.003, 0.0, 0.0, 24055, 2)
    ops.limitCurve('ThreePoint', 14055, 4055, 0.0, 256.15747242, 0.01098481, 256.15747242, 0.03295442, 179.31023069, -9090.89773702, 0.05, 2, 0, 74022, 21002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34055, 64.0393681, 8.114e-05, 192.11810431, 0.00024342, 640.39368104, 0.0008114, -64.0393681, -8.114e-05, -192.11810431, -0.00024342, -640.39368104, -0.0008114, 0.4, 0.3, 0.003, 0.0, 0.0, 14055, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4055, 99999, 'P', 44055, 'Vy', 34055, 'Vz', 24055, 'My', 14055, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174022, 74022, 174022, 4055, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121002, 121002, 21002, 4055, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171001, 0.0, 0.0, 3.75)
    ops.node(124023, 0.0, 0.0, 4.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4057, 171001, 124023, 0.0625, 23907773.84928371, 9961572.43720154, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24057, 20.67430487, 0.00068969, 25.18619357, 0.02852305, 2.51861936, 0.08257753, -20.67430487, -0.00068969, -25.18619357, -0.02852305, -2.51861936, -0.08257753, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14057, 20.67430487, 0.00068969, 25.18619357, 0.02852305, 2.51861936, 0.08257753, -20.67430487, -0.00068969, -25.18619357, -0.02852305, -2.51861936, -0.08257753, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24057, 4057, 0.0, 61.24001273, 0.01379373, 61.24001273, 0.04138118, 42.86800891, -1832.25306019, 0.05, 2, 0, 71001, 24023, 2, 3)
    ops.uniaxialMaterial('LimitState', 44057, 15.31000318, 4.279e-05, 45.93000954, 0.00012836, 153.10003182, 0.00042787, -15.31000318, -4.279e-05, -45.93000954, -0.00012836, -153.10003182, -0.00042787, 0.4, 0.3, 0.003, 0.0, 0.0, 24057, 2)
    ops.limitCurve('ThreePoint', 14057, 4057, 0.0, 61.24001273, 0.01379373, 61.24001273, 0.04138118, 42.86800891, -1832.25306019, 0.05, 2, 0, 71001, 24023, 1, 3)
    ops.uniaxialMaterial('LimitState', 34057, 15.31000318, 4.279e-05, 45.93000954, 0.00012836, 153.10003182, 0.00042787, -15.31000318, -4.279e-05, -45.93000954, -0.00012836, -153.10003182, -0.00042787, 0.4, 0.3, 0.003, 0.0, 0.0, 14057, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4057, 99999, 'P', 44057, 'Vy', 34057, 'Vz', 24057, 'My', 14057, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171001, 71001, 171001, 4057, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124023, 124023, 24023, 4057, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174023, 0.0, 0.0, 5.125)
    ops.node(122001, 0.0, 0.0, 6.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4058, 174023, 122001, 0.0625, 31482475.05311035, 13117697.93879598, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24058, 19.75197148, 0.00058259, 23.83490345, 0.02207127, 2.38349035, 0.08131178, -19.75197148, -0.00058259, -23.83490345, -0.02207127, -2.38349035, -0.08131178, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14058, 19.75197148, 0.00058259, 23.83490345, 0.02207127, 2.38349035, 0.08131178, -19.75197148, -0.00058259, -23.83490345, -0.02207127, -2.38349035, -0.08131178, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24058, 4058, 0.0, 64.33498585, 0.01165183, 64.33498585, 0.03495549, 45.0344901, -1362.60277151, 0.05, 2, 0, 74023, 22001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44058, 16.08374646, 3.413e-05, 48.25123939, 0.0001024, 160.83746463, 0.00034135, -16.08374646, -3.413e-05, -48.25123939, -0.0001024, -160.83746463, -0.00034135, 0.4, 0.3, 0.003, 0.0, 0.0, 24058, 2)
    ops.limitCurve('ThreePoint', 14058, 4058, 0.0, 64.33498585, 0.01165183, 64.33498585, 0.03495549, 45.0344901, -1362.60277151, 0.05, 2, 0, 74023, 22001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34058, 16.08374646, 3.413e-05, 48.25123939, 0.0001024, 160.83746463, 0.00034135, -16.08374646, -3.413e-05, -48.25123939, -0.0001024, -160.83746463, -0.00034135, 0.4, 0.3, 0.003, 0.0, 0.0, 14058, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4058, 99999, 'P', 44058, 'Vy', 34058, 'Vz', 24058, 'My', 14058, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174023, 74023, 174023, 4058, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122001, 122001, 22001, 4058, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171002, 2.9, 0.0, 3.75)
    ops.node(124024, 2.9, 0.0, 4.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4059, 171002, 124024, 0.14, 27638134.87680968, 11515889.53200403, 0.00271929, 0.00205333, 0.00157208, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24059, 63.20210437, 0.0005243, 76.88575652, 0.0471614, 7.68857565, 0.12605704, -63.20210437, -0.0005243, -76.88575652, -0.0471614, -7.68857565, -0.12605704, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14059, 77.33310918, 0.00050653, 94.07621254, 0.04949874, 9.40762125, 0.13817452, -77.33310918, -0.00050653, -94.07621254, -0.04949874, -9.40762125, -0.13817452, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24059, 4059, 0.0, 190.91707016, 0.01048599, 190.91707016, 0.03145797, 133.64194911, -4712.45220052, 0.05, 2, 0, 71002, 24024, 2, 3)
    ops.uniaxialMaterial('LimitState', 44059, 47.72926754, 5.151e-05, 143.18780262, 0.00015454, 477.2926754, 0.00051512, -47.72926754, -5.151e-05, -143.18780262, -0.00015454, -477.2926754, -0.00051512, 0.4, 0.3, 0.003, 0.0, 0.0, 24059, 2)
    ops.limitCurve('ThreePoint', 14059, 4059, 0.0, 218.19093733, 0.01013053, 218.19093733, 0.0303916, 152.73365613, -5637.35332319, 0.05, 2, 0, 71002, 24024, 1, 3)
    ops.uniaxialMaterial('LimitState', 34059, 54.54773433, 5.887e-05, 163.64320299, 0.00017661, 545.47734332, 0.00058871, -54.54773433, -5.887e-05, -163.64320299, -0.00017661, -545.47734332, -0.00058871, 0.4, 0.3, 0.003, 0.0, 0.0, 14059, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4059, 99999, 'P', 44059, 'Vy', 34059, 'Vz', 24059, 'My', 14059, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171002, 71002, 171002, 4059, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124024, 124024, 24024, 4059, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174024, 2.9, 0.0, 5.125)
    ops.node(122002, 2.9, 0.0, 6.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4060, 174024, 122002, 0.14, 29764165.41108885, 12401735.58795369, 0.00271929, 0.00205333, 0.00157208, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24060, 58.34445257, 0.00054689, 70.7320321, 0.05102235, 7.07320321, 0.135278, -58.34445257, -0.00054689, -70.7320321, -0.05102235, -7.07320321, -0.135278, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14060, 71.03921479, 0.00052257, 86.12212128, 0.05354697, 8.61221213, 0.1482472, -71.03921479, -0.00052257, -86.12212128, -0.05354697, -8.61221213, -0.1482472, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24060, 4060, 0.0, 217.49488852, 0.01093787, 217.49488852, 0.03281361, 152.24642196, -6697.35289216, 0.05, 2, 0, 74024, 22002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44060, 54.37372213, 5.449e-05, 163.12116639, 0.00016347, 543.73722129, 0.00054491, -54.37372213, -5.449e-05, -163.12116639, -0.00016347, -543.73722129, -0.00054491, 0.4, 0.3, 0.003, 0.0, 0.0, 24060, 2)
    ops.limitCurve('ThreePoint', 14060, 4060, 0.0, 248.56558688, 0.01045148, 248.56558688, 0.03135443, 173.99591081, -8167.20562341, 0.05, 2, 0, 74024, 22002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34060, 62.14139672, 6.228e-05, 186.42419016, 0.00018683, 621.41396719, 0.00062276, -62.14139672, -6.228e-05, -186.42419016, -0.00018683, -621.41396719, -0.00062276, 0.4, 0.3, 0.003, 0.0, 0.0, 14060, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4060, 99999, 'P', 44060, 'Vy', 34060, 'Vz', 24060, 'My', 14060, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174024, 74024, 174024, 4060, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122002, 122002, 22002, 4060, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172001, 0.0, 0.0, 6.65)
    ops.node(124025, 0.0, 0.0, 7.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4062, 172001, 124025, 0.0625, 24507031.04931766, 10211262.93721569, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24062, 19.22206141, 0.00060058, 23.51076814, 0.03111388, 2.35107681, 0.09397979, -19.22206141, -0.00060058, -23.51076814, -0.03111388, -2.35107681, -0.09397979, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14062, 19.22206141, 0.00060058, 23.51076814, 0.03111388, 2.35107681, 0.09397979, -19.22206141, -0.00060058, -23.51076814, -0.03111388, -2.35107681, -0.09397979, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24062, 4062, 0.0, 60.76568428, 0.01201158, 60.76568428, 0.03603475, 42.53597899, -2171.08797573, 0.05, 2, 0, 72001, 24025, 2, 3)
    ops.uniaxialMaterial('LimitState', 44062, 15.19142107, 4.142e-05, 45.57426321, 0.00012425, 151.9142107, 0.00041418, -15.19142107, -4.142e-05, -45.57426321, -0.00012425, -151.9142107, -0.00041418, 0.4, 0.3, 0.003, 0.0, 0.0, 24062, 2)
    ops.limitCurve('ThreePoint', 14062, 4062, 0.0, 60.76568428, 0.01201158, 60.76568428, 0.03603475, 42.53597899, -2171.08797573, 0.05, 2, 0, 72001, 24025, 1, 3)
    ops.uniaxialMaterial('LimitState', 34062, 15.19142107, 4.142e-05, 45.57426321, 0.00012425, 151.9142107, 0.00041418, -15.19142107, -4.142e-05, -45.57426321, -0.00012425, -151.9142107, -0.00041418, 0.4, 0.3, 0.003, 0.0, 0.0, 14062, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4062, 99999, 'P', 44062, 'Vy', 34062, 'Vz', 24062, 'My', 14062, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172001, 72001, 172001, 4062, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124025, 124025, 24025, 4062, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174025, 0.0, 0.0, 8.025)
    ops.node(123001, 0.0, 0.0, 9.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4063, 174025, 123001, 0.0625, 30331275.57485059, 12638031.48952108, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24063, 14.7225425, 0.00054919, 17.85972326, 0.02813359, 1.78597233, 0.09033049, -14.7225425, -0.00054919, -17.85972326, -0.02813359, -1.78597233, -0.09033049, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14063, 14.7225425, 0.00054919, 17.85972326, 0.02813359, 1.78597233, 0.09033049, -14.7225425, -0.00054919, -17.85972326, -0.02813359, -1.78597233, -0.09033049, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24063, 4063, 0.0, 64.53039677, 0.01098389, 64.53039677, 0.03295166, 45.17127774, -2029.73571563, 0.05, 2, 0, 74025, 23001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44063, 16.13259919, 3.554e-05, 48.39779758, 0.00010661, 161.32599193, 0.00035538, -16.13259919, -3.554e-05, -48.39779758, -0.00010661, -161.32599193, -0.00035538, 0.4, 0.3, 0.003, 0.0, 0.0, 24063, 2)
    ops.limitCurve('ThreePoint', 14063, 4063, 0.0, 64.53039677, 0.01098389, 64.53039677, 0.03295166, 45.17127774, -2029.73571563, 0.05, 2, 0, 74025, 23001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34063, 16.13259919, 3.554e-05, 48.39779758, 0.00010661, 161.32599193, 0.00035538, -16.13259919, -3.554e-05, -48.39779758, -0.00010661, -161.32599193, -0.00035538, 0.4, 0.3, 0.003, 0.0, 0.0, 14063, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4063, 99999, 'P', 44063, 'Vy', 34063, 'Vz', 24063, 'My', 14063, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174025, 74025, 174025, 4063, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123001, 123001, 23001, 4063, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172002, 2.9, 0.0, 6.65)
    ops.node(124026, 2.9, 0.0, 7.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4064, 172002, 124026, 0.0875, 28468436.25124107, 11861848.43801711, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24064, 35.35279766, 0.00065687, 42.93897584, 0.04868171, 4.29389758, 0.13872021, -35.35279766, -0.00065687, -42.93897584, -0.04868171, -4.29389758, -0.13872021, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14064, 51.45172886, 0.00055909, 62.49249532, 0.05513624, 6.24924953, 0.15513624, -51.45172886, -0.00055909, -62.49249532, -0.05513624, -6.24924953, -0.15513624, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24064, 4064, 0.0, 105.26257322, 0.01313738, 105.26257322, 0.03941215, 73.68380125, -3470.2405534, 0.05, 2, 0, 72002, 24026, 2, 3)
    ops.uniaxialMaterial('LimitState', 44064, 26.3156433, 4.412e-05, 78.94692991, 0.00013235, 263.15643304, 0.00044117, -26.3156433, -4.412e-05, -78.94692991, -0.00013235, -263.15643304, -0.00044117, 0.4, 0.3, 0.003, 0.0, 0.0, 24064, 2)
    ops.limitCurve('ThreePoint', 14064, 4064, 0.0, 147.3676025, 0.01118176, 147.3676025, 0.03354528, 103.15732175, -5613.57384437, 0.05, 2, 0, 72002, 24026, 1, 3)
    ops.uniaxialMaterial('LimitState', 34064, 36.84190063, 6.176e-05, 110.52570188, 0.00018529, 368.41900625, 0.00061763, -36.84190063, -6.176e-05, -110.52570188, -0.00018529, -368.41900625, -0.00061763, 0.4, 0.3, 0.003, 0.0, 0.0, 14064, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4064, 99999, 'P', 44064, 'Vy', 34064, 'Vz', 24064, 'My', 14064, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172002, 72002, 172002, 4064, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124026, 124026, 24026, 4064, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174026, 2.9, 0.0, 8.025)
    ops.node(123002, 2.9, 0.0, 9.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4065, 174026, 123002, 0.0875, 29190870.3283054, 12162862.63679392, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24065, 27.34902142, 0.00062675, 33.2134183, 0.05116696, 3.32134183, 0.14619942, -27.34902142, -0.00062675, -33.2134183, -0.05116696, -3.32134183, -0.14619942, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14065, 40.31214931, 0.00052355, 48.95620422, 0.05795925, 4.89562042, 0.15795925, -40.31214931, -0.00052355, -48.95620422, -0.05795925, -4.89562042, -0.15795925, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24065, 4065, 0.0, 103.80505609, 0.01253503, 103.80505609, 0.03760509, 72.66353926, -3692.14463898, 0.05, 2, 0, 74026, 23002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44065, 25.95126402, 4.243e-05, 77.85379206, 0.00012729, 259.51264021, 0.00042429, -25.95126402, -4.243e-05, -77.85379206, -0.00012729, -259.51264021, -0.00042429, 0.4, 0.3, 0.003, 0.0, 0.0, 24065, 2)
    ops.limitCurve('ThreePoint', 14065, 4065, 0.0, 145.32707852, 0.01047108, 145.32707852, 0.03141323, 101.72895496, -6144.83446044, 0.05, 2, 0, 74026, 23002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34065, 36.33176963, 5.94e-05, 108.99530889, 0.0001782, 363.3176963, 0.00059401, -36.33176963, -5.94e-05, -108.99530889, -0.0001782, -363.3176963, -0.00059401, 0.4, 0.3, 0.003, 0.0, 0.0, 14065, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4065, 99999, 'P', 44065, 'Vy', 34065, 'Vz', 24065, 'My', 14065, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174026, 74026, 174026, 4065, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123002, 123002, 23002, 4065, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173001, 0.0, 0.0, 9.55)
    ops.node(124027, 0.0, 0.0, 10.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4067, 173001, 124027, 0.0625, 28650510.67090354, 11937712.77954314, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24067, 14.93967567, 0.00057911, 18.21532003, 0.02520698, 1.821532, 0.08798822, -14.93967567, -0.00057911, -18.21532003, -0.02520698, -1.821532, -0.08798822, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14067, 14.93967567, 0.00057911, 18.21532003, 0.02520698, 1.821532, 0.08798822, -14.93967567, -0.00057911, -18.21532003, -0.02520698, -1.821532, -0.08798822, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24067, 4067, 0.0, 57.37328059, 0.01158213, 57.37328059, 0.03474639, 40.16129642, -2009.57965293, 0.05, 2, 0, 73001, 24027, 2, 3)
    ops.uniaxialMaterial('LimitState', 44067, 14.34332015, 3.345e-05, 43.02996045, 0.00010035, 143.43320149, 0.0003345, -14.34332015, -3.345e-05, -43.02996045, -0.00010035, -143.43320149, -0.0003345, 0.4, 0.3, 0.003, 0.0, 0.0, 24067, 2)
    ops.limitCurve('ThreePoint', 14067, 4067, 0.0, 57.37328059, 0.01158213, 57.37328059, 0.03474639, 40.16129642, -2009.57965293, 0.05, 2, 0, 73001, 24027, 1, 3)
    ops.uniaxialMaterial('LimitState', 34067, 14.34332015, 3.345e-05, 43.02996045, 0.00010035, 143.43320149, 0.0003345, -14.34332015, -3.345e-05, -43.02996045, -0.00010035, -143.43320149, -0.0003345, 0.4, 0.3, 0.003, 0.0, 0.0, 14067, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4067, 99999, 'P', 44067, 'Vy', 34067, 'Vz', 24067, 'My', 14067, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173001, 73001, 173001, 4067, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124027, 124027, 24027, 4067, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174027, 0.0, 0.0, 10.925)
    ops.node(124001, 0.0, 0.0, 12.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4068, 174027, 124001, 0.0625, 28220511.31210559, 11758546.380044, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24068, 12.29078824, 0.00053243, 15.03082513, 0.02426311, 1.50308251, 0.09068751, -12.29078824, -0.00053243, -15.03082513, -0.02426311, -1.50308251, -0.09068751, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14068, 12.29078824, 0.00053243, 15.03082513, 0.02426311, 1.50308251, 0.09068751, -12.29078824, -0.00053243, -15.03082513, -0.02426311, -1.50308251, -0.09068751, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24068, 4068, 0.0, 46.02047339, 0.01064858, 46.02047339, 0.03194573, 32.21433138, -9984.02218032, 0.05, 2, 0, 74027, 24001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44068, 11.50511835, 2.724e-05, 34.51535505, 8.172e-05, 115.05118348, 0.0002724, -11.50511835, -2.724e-05, -34.51535505, -8.172e-05, -115.05118348, -0.0002724, 0.4, 0.3, 0.003, 0.0, 0.0, 24068, 2)
    ops.limitCurve('ThreePoint', 14068, 4068, 0.0, 46.02047339, 0.01064858, 46.02047339, 0.03194573, 32.21433138, -9984.02218032, 0.05, 2, 0, 74027, 24001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34068, 11.50511835, 2.724e-05, 34.51535505, 8.172e-05, 115.05118348, 0.0002724, -11.50511835, -2.724e-05, -34.51535505, -8.172e-05, -115.05118348, -0.0002724, 0.4, 0.3, 0.003, 0.0, 0.0, 14068, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4068, 99999, 'P', 44068, 'Vy', 34068, 'Vz', 24068, 'My', 14068, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174027, 74027, 174027, 4068, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124001, 124001, 24001, 4068, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173002, 2.9, 0.0, 9.55)
    ops.node(124028, 2.9, 0.0, 10.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4069, 173002, 124028, 0.0875, 29548945.67779272, 12312060.6990803, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24069, 23.99901299, 0.00062392, 29.1913245, 0.03245259, 2.91913245, 0.09000367, -23.99901299, -0.00062392, -29.1913245, -0.03245259, -2.91913245, -0.09000367, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14069, 35.65328254, 0.00052344, 43.367056, 0.03621766, 4.3367056, 0.11175034, -35.65328254, -0.00052344, -43.367056, -0.03621766, -4.3367056, -0.11175034, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24069, 4069, 0.0, 80.65010736, 0.01247837, 80.65010736, 0.03743511, 56.45507515, -2360.75974983, 0.05, 2, 0, 73002, 24028, 2, 3)
    ops.uniaxialMaterial('LimitState', 44069, 20.16252684, 3.257e-05, 60.48758052, 9.77e-05, 201.62526841, 0.00032565, -20.16252684, -3.257e-05, -60.48758052, -9.77e-05, -201.62526841, -0.00032565, 0.4, 0.3, 0.003, 0.0, 0.0, 24069, 2)
    ops.limitCurve('ThreePoint', 14069, 4069, 0.0, 112.91015031, 0.01046882, 112.91015031, 0.03140646, 79.03710522, -4029.52958118, 0.05, 2, 0, 73002, 24028, 1, 3)
    ops.uniaxialMaterial('LimitState', 34069, 28.22753758, 4.559e-05, 84.68261273, 0.00013677, 282.27537577, 0.00045591, -28.22753758, -4.559e-05, -84.68261273, -0.00013677, -282.27537577, -0.00045591, 0.4, 0.3, 0.003, 0.0, 0.0, 14069, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4069, 99999, 'P', 44069, 'Vy', 34069, 'Vz', 24069, 'My', 14069, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173002, 73002, 173002, 4069, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124028, 124028, 24028, 4069, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174028, 2.9, 0.0, 10.925)
    ops.node(124002, 2.9, 0.0, 12.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4070, 174028, 124002, 0.0875, 34736904.85322023, 14473710.35550843, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24070, 26.33838835, 0.00059127, 31.51476217, 0.02818315, 3.15147622, 0.08852231, -26.33838835, -0.00059127, -31.51476217, -0.02818315, -3.15147622, -0.08852231, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14070, 38.73535522, 0.00051312, 46.34814747, 0.031456, 4.63481475, 0.11064789, -38.73535522, -0.00051312, -46.34814747, -0.031456, -4.63481475, -0.11064789, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24070, 4070, 0.0, 91.95909757, 0.01182534, 91.95909757, 0.03547602, 64.3713683, -3905.97865164, 0.05, 2, 0, 74028, 24002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44070, 22.98977439, 3.159e-05, 68.96932318, 9.476e-05, 229.89774392, 0.00031586, -22.98977439, -3.159e-05, -68.96932318, -9.476e-05, -229.89774392, -0.00031586, 0.4, 0.3, 0.003, 0.0, 0.0, 24070, 2)
    ops.limitCurve('ThreePoint', 14070, 4070, 0.0, 128.7427366, 0.01026249, 128.7427366, 0.03078747, 90.11991562, -7160.39222704, 0.05, 2, 0, 74028, 24002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34070, 32.18568415, 4.422e-05, 96.55705245, 0.00013266, 321.85684149, 0.00044221, -32.18568415, -4.422e-05, -96.55705245, -0.00013266, -321.85684149, -0.00044221, 0.4, 0.3, 0.003, 0.0, 0.0, 14070, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4070, 99999, 'P', 44070, 'Vy', 34070, 'Vz', 24070, 'My', 14070, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174028, 74028, 174028, 4070, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124002, 124002, 24002, 4070, '-orient', 0, 0, 1, 0, 1, 0)
