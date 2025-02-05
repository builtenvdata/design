import openseespy.opensees as ops


def add_columns() -> None:
    """Add components of all columns to ops domain (plastic hinges, column elements and nodes)
    """
    # Create elastic column element nodes
    ops.node(170001, 0.0, 0.0, 0.0)
    ops.node(121001, 0.0, 0.0, 3.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1, 170001, 121001, 0.09, 27822730.79933828, 11592804.49972428, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20001, 41.1995443, 0.00079172, 50.01505011, 0.02578628, 5.00150501, 0.07928992, -41.1995443, -0.00079172, -50.01505011, -0.02578628, -5.00150501, -0.07928992, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10001, 46.87062354, 0.00079172, 56.89957558, 0.02578628, 5.68995756, 0.07928992, -46.87062354, -0.00079172, -56.89957558, -0.02578628, -5.68995756, -0.07928992, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20001, 1, 0.0, 91.71115139, 0.01583447, 91.71115139, 0.04750342, 64.19780598, -948.03190359, 0.05, 2, 0, 70001, 21001, 2, 3)
    ops.uniaxialMaterial('LimitState', 40001, 22.92778785, 9.757e-05, 68.78336355, 0.00029271, 229.27787849, 0.0009757, -22.92778785, -9.757e-05, -68.78336355, -0.00029271, -229.27787849, -0.0009757, 0.4, 0.3, 0.003, 0.0, 0.0, 20001, 2)
    ops.limitCurve('ThreePoint', 10001, 1, 0.0, 91.71115139, 0.01583447, 91.71115139, 0.04750342, 64.19780598, -948.03190359, 0.05, 2, 0, 70001, 21001, 1, 3)
    ops.uniaxialMaterial('LimitState', 30001, 22.92778785, 9.757e-05, 68.78336355, 0.00029271, 229.27787849, 0.0009757, -22.92778785, -9.757e-05, -68.78336355, -0.00029271, -229.27787849, -0.0009757, 0.4, 0.3, 0.003, 0.0, 0.0, 10001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1, 99999, 'P', 40001, 'Vy', 30001, 'Vz', 20001, 'My', 10001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170001, 70001, 170001, 1, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121001, 121001, 21001, 1, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170002, 4.15, 0.0, 0.0)
    ops.node(121002, 4.15, 0.0, 3.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2, 170002, 121002, 0.1225, 29604556.89257659, 12335232.03857358, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20002, 79.77625233, 0.00072283, 96.39415618, 0.03399683, 9.63941562, 0.09378506, -79.77625233, -0.00072283, -96.39415618, -0.03399683, -9.63941562, -0.09378506, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10002, 90.58754119, 0.00072283, 109.45750569, 0.03399683, 10.94575057, 0.09378506, -90.58754119, -0.00072283, -109.45750569, -0.03399683, -10.94575057, -0.09378506, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20002, 2, 0.0, 144.06112535, 0.01445658, 144.06112535, 0.04336975, 100.84278775, -1526.7222706, 0.05, 2, 0, 70002, 21002, 2, 3)
    ops.uniaxialMaterial('LimitState', 40002, 36.01528134, 0.00010582, 108.04584401, 0.00031747, 360.15281338, 0.00105825, -36.01528134, -0.00010582, -108.04584401, -0.00031747, -360.15281338, -0.00105825, 0.4, 0.3, 0.003, 0.0, 0.0, 20002, 2)
    ops.limitCurve('ThreePoint', 10002, 2, 0.0, 144.06112535, 0.01445658, 144.06112535, 0.04336975, 100.84278775, -1526.7222706, 0.05, 2, 0, 70002, 21002, 1, 3)
    ops.uniaxialMaterial('LimitState', 30002, 36.01528134, 0.00010582, 108.04584401, 0.00031747, 360.15281338, 0.00105825, -36.01528134, -0.00010582, -108.04584401, -0.00031747, -360.15281338, -0.00105825, 0.4, 0.3, 0.003, 0.0, 0.0, 10002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2, 99999, 'P', 40002, 'Vy', 30002, 'Vz', 20002, 'My', 10002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170002, 70002, 170002, 2, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121002, 121002, 21002, 2, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170005, 15.4, 0.0, 0.0)
    ops.node(121005, 15.4, 0.0, 3.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 5, 170005, 121005, 0.1225, 29350185.11536952, 12229243.79807063, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20005, 80.59627718, 0.00071655, 97.43076305, 0.03403554, 9.7430763, 0.09338062, -80.59627718, -0.00071655, -97.43076305, -0.03403554, -9.7430763, -0.09338062, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10005, 92.01377122, 0.00071655, 111.23307744, 0.03403554, 11.12330774, 0.09338062, -92.01377122, -0.00071655, -111.23307744, -0.03403554, -11.12330774, -0.09338062, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20005, 5, 0.0, 142.4392524, 0.01433104, 142.4392524, 0.04299313, 99.70747668, -1507.35170865, 0.05, 2, 0, 70005, 21005, 2, 3)
    ops.uniaxialMaterial('LimitState', 40005, 35.6098131, 0.00010554, 106.8294393, 0.00031662, 356.098131, 0.0010554, -35.6098131, -0.00010554, -106.8294393, -0.00031662, -356.098131, -0.0010554, 0.4, 0.3, 0.003, 0.0, 0.0, 20005, 2)
    ops.limitCurve('ThreePoint', 10005, 5, 0.0, 142.4392524, 0.01433104, 142.4392524, 0.04299313, 99.70747668, -1507.35170865, 0.05, 2, 0, 70005, 21005, 1, 3)
    ops.uniaxialMaterial('LimitState', 30005, 35.6098131, 0.00010554, 106.8294393, 0.00031662, 356.098131, 0.0010554, -35.6098131, -0.00010554, -106.8294393, -0.00031662, -356.098131, -0.0010554, 0.4, 0.3, 0.003, 0.0, 0.0, 10005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 5, 99999, 'P', 40005, 'Vy', 30005, 'Vz', 20005, 'My', 10005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170005, 70005, 170005, 5, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121005, 121005, 21005, 5, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170006, 19.55, 0.0, 0.0)
    ops.node(121006, 19.55, 0.0, 3.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 6, 170006, 121006, 0.09, 29316645.48374938, 12215268.95156224, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20006, 42.50564513, 0.00076926, 51.46918572, 0.02578072, 5.14691857, 0.08152906, -42.50564513, -0.00076926, -51.46918572, -0.02578072, -5.14691857, -0.08152906, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10006, 48.8860226, 0.00076926, 59.19504972, 0.02578072, 5.91950497, 0.08152906, -48.8860226, -0.00076926, -59.19504972, -0.02578072, -5.91950497, -0.08152906, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20006, 6, 0.0, 96.46721108, 0.01538529, 96.46721108, 0.04615587, 67.52704775, -971.41274333, 0.05, 2, 0, 70006, 21006, 2, 3)
    ops.uniaxialMaterial('LimitState', 40006, 24.11680277, 9.74e-05, 72.35040831, 0.0002922, 241.16802769, 0.000974, -24.11680277, -9.74e-05, -72.35040831, -0.0002922, -241.16802769, -0.000974, 0.4, 0.3, 0.003, 0.0, 0.0, 20006, 2)
    ops.limitCurve('ThreePoint', 10006, 6, 0.0, 96.46721108, 0.01538529, 96.46721108, 0.04615587, 67.52704775, -971.41274333, 0.05, 2, 0, 70006, 21006, 1, 3)
    ops.uniaxialMaterial('LimitState', 30006, 24.11680277, 9.74e-05, 72.35040831, 0.0002922, 241.16802769, 0.000974, -24.11680277, -9.74e-05, -72.35040831, -0.0002922, -241.16802769, -0.000974, 0.4, 0.3, 0.003, 0.0, 0.0, 10006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 6, 99999, 'P', 40006, 'Vy', 30006, 'Vz', 20006, 'My', 10006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170006, 70006, 170006, 6, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121006, 121006, 21006, 6, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170007, 0.0, 4.85, 0.0)
    ops.node(121007, 0.0, 4.85, 3.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 7, 170007, 121007, 0.1225, 29108038.54940441, 12128349.39558517, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20007, 93.59988072, 0.00074577, 113.17222587, 0.04479301, 11.31722259, 0.12759959, -93.59988072, -0.00074577, -113.17222587, -0.04479301, -11.31722259, -0.12759959, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10007, 104.68306119, 0.00074577, 126.57297162, 0.04479301, 12.65729716, 0.12759959, -104.68306119, -0.00074577, -126.57297162, -0.04479301, -12.65729716, -0.12759959, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20007, 7, 0.0, 170.92654333, 0.01491539, 170.92654333, 0.04474618, 119.64858033, -2425.38708939, 0.05, 2, 0, 70007, 21007, 2, 3)
    ops.uniaxialMaterial('LimitState', 40007, 42.73163583, 0.0001277, 128.19490749, 0.0003831, 427.31635831, 0.00127701, -42.73163583, -0.0001277, -128.19490749, -0.0003831, -427.31635831, -0.00127701, 0.4, 0.3, 0.003, 0.0, 0.0, 20007, 2)
    ops.limitCurve('ThreePoint', 10007, 7, 0.0, 170.92654333, 0.01491539, 170.92654333, 0.04474618, 119.64858033, -2425.38708939, 0.05, 2, 0, 70007, 21007, 1, 3)
    ops.uniaxialMaterial('LimitState', 30007, 42.73163583, 0.0001277, 128.19490749, 0.0003831, 427.31635831, 0.00127701, -42.73163583, -0.0001277, -128.19490749, -0.0003831, -427.31635831, -0.00127701, 0.4, 0.3, 0.003, 0.0, 0.0, 10007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 7, 99999, 'P', 40007, 'Vy', 30007, 'Vz', 20007, 'My', 10007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170007, 70007, 170007, 7, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121007, 121007, 21007, 7, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170008, 4.15, 4.85, 0.0)
    ops.node(121008, 4.15, 4.85, 3.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 8, 170008, 121008, 0.1225, 28772788.93017679, 11988662.05424033, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20008, 134.27964448, 0.00077685, 161.84511598, 0.0458085, 16.1845116, 0.11914389, -134.27964448, -0.00077685, -161.84511598, -0.0458085, -16.1845116, -0.11914389, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10008, 141.84181855, 0.00077685, 170.9596839, 0.0458085, 17.09596839, 0.11914389, -141.84181855, -0.00077685, -170.9596839, -0.0458085, -17.09596839, -0.11914389, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20008, 8, 0.0, 174.99412243, 0.01553692, 174.99412243, 0.04661076, 122.4958857, -2215.77028286, 0.05, 2, 0, 70008, 21008, 2, 3)
    ops.uniaxialMaterial('LimitState', 40008, 43.74853061, 0.00013226, 131.24559182, 0.00039679, 437.48530606, 0.00132263, -43.74853061, -0.00013226, -131.24559182, -0.00039679, -437.48530606, -0.00132263, 0.4, 0.3, 0.003, 0.0, 0.0, 20008, 2)
    ops.limitCurve('ThreePoint', 10008, 8, 0.0, 174.99412243, 0.01553692, 174.99412243, 0.04661076, 122.4958857, -2215.77028286, 0.05, 2, 0, 70008, 21008, 1, 3)
    ops.uniaxialMaterial('LimitState', 30008, 43.74853061, 0.00013226, 131.24559182, 0.00039679, 437.48530606, 0.00132263, -43.74853061, -0.00013226, -131.24559182, -0.00039679, -437.48530606, -0.00132263, 0.4, 0.3, 0.003, 0.0, 0.0, 10008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 8, 99999, 'P', 40008, 'Vy', 30008, 'Vz', 20008, 'My', 10008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170008, 70008, 170008, 8, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121008, 121008, 21008, 8, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170009, 8.3, 4.85, 0.0)
    ops.node(121009, 8.3, 4.85, 3.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 9, 170009, 121009, 0.1225, 29763744.8946366, 12401560.37276525, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20009, 133.44174839, 0.00077109, 160.61194715, 0.04614753, 16.06119472, 0.12253457, -133.44174839, -0.00077109, -160.61194715, -0.04614753, -16.06119472, -0.12253457, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10009, 140.76132953, 0.00077109, 169.42187504, 0.04614753, 16.9421875, 0.12253457, -140.76132953, -0.00077109, -169.42187504, -0.04614753, -16.9421875, -0.12253457, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20009, 9, 0.0, 180.73747058, 0.0154218, 180.73747058, 0.04626539, 126.51622941, -2268.60884608, 0.05, 2, 0, 70009, 21009, 2, 3)
    ops.uniaxialMaterial('LimitState', 40009, 45.18436765, 0.00013206, 135.55310294, 0.00039617, 451.84367646, 0.00132056, -45.18436765, -0.00013206, -135.55310294, -0.00039617, -451.84367646, -0.00132056, 0.4, 0.3, 0.003, 0.0, 0.0, 20009, 2)
    ops.limitCurve('ThreePoint', 10009, 9, 0.0, 180.73747058, 0.0154218, 180.73747058, 0.04626539, 126.51622941, -2268.60884608, 0.05, 2, 0, 70009, 21009, 1, 3)
    ops.uniaxialMaterial('LimitState', 30009, 45.18436765, 0.00013206, 135.55310294, 0.00039617, 451.84367646, 0.00132056, -45.18436765, -0.00013206, -135.55310294, -0.00039617, -451.84367646, -0.00132056, 0.4, 0.3, 0.003, 0.0, 0.0, 10009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 9, 99999, 'P', 40009, 'Vy', 30009, 'Vz', 20009, 'My', 10009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170009, 70009, 170009, 9, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121009, 121009, 21009, 9, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170010, 11.25, 4.85, 0.0)
    ops.node(121010, 11.25, 4.85, 3.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 10, 170010, 121010, 0.1225, 29032683.72199382, 12096951.55083076, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20010, 129.62253936, 0.00080151, 156.17411335, 0.04623887, 15.61741133, 0.12030267, -129.62253936, -0.00080151, -156.17411335, -0.04623887, -15.61741133, -0.12030267, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10010, 136.21185443, 0.00080151, 164.11316811, 0.04623887, 16.41131681, 0.12030267, -136.21185443, -0.00080151, -164.11316811, -0.04623887, -16.41131681, -0.12030267, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20010, 10, 0.0, 179.31820869, 0.01603028, 179.31820869, 0.04809083, 125.52274608, -2308.71634319, 0.05, 2, 0, 70010, 21010, 2, 3)
    ops.uniaxialMaterial('LimitState', 40010, 44.82955217, 0.00013432, 134.48865652, 0.00040296, 448.29552173, 0.00134318, -44.82955217, -0.00013432, -134.48865652, -0.00040296, -448.29552173, -0.00134318, 0.4, 0.3, 0.003, 0.0, 0.0, 20010, 2)
    ops.limitCurve('ThreePoint', 10010, 10, 0.0, 179.31820869, 0.01603028, 179.31820869, 0.04809083, 125.52274608, -2308.71634319, 0.05, 2, 0, 70010, 21010, 1, 3)
    ops.uniaxialMaterial('LimitState', 30010, 44.82955217, 0.00013432, 134.48865652, 0.00040296, 448.29552173, 0.00134318, -44.82955217, -0.00013432, -134.48865652, -0.00040296, -448.29552173, -0.00134318, 0.4, 0.3, 0.003, 0.0, 0.0, 10010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 10, 99999, 'P', 40010, 'Vy', 30010, 'Vz', 20010, 'My', 10010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170010, 70010, 170010, 10, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121010, 121010, 21010, 10, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170011, 15.4, 4.85, 0.0)
    ops.node(121011, 15.4, 4.85, 3.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 11, 170011, 121011, 0.1225, 28948284.03663175, 12061785.01526323, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20011, 129.92535779, 0.00079651, 156.56495173, 0.04600856, 15.65649517, 0.11993214, -129.92535779, -0.00079651, -156.56495173, -0.04600856, -15.65649517, -0.11993214, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10011, 136.64495486, 0.00079651, 164.6623194, 0.04600856, 16.46623194, 0.11993214, -136.64495486, -0.00079651, -164.6623194, -0.04600856, -16.46623194, -0.11993214, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20011, 11, 0.0, 176.04832442, 0.01593017, 176.04832442, 0.04779052, 123.2338271, -2227.16369752, 0.05, 2, 0, 70011, 21011, 2, 3)
    ops.uniaxialMaterial('LimitState', 40011, 44.01208111, 0.00013225, 132.03624332, 0.00039676, 440.12081106, 0.00132254, -44.01208111, -0.00013225, -132.03624332, -0.00039676, -440.12081106, -0.00132254, 0.4, 0.3, 0.003, 0.0, 0.0, 20011, 2)
    ops.limitCurve('ThreePoint', 10011, 11, 0.0, 176.04832442, 0.01593017, 176.04832442, 0.04779052, 123.2338271, -2227.16369752, 0.05, 2, 0, 70011, 21011, 1, 3)
    ops.uniaxialMaterial('LimitState', 30011, 44.01208111, 0.00013225, 132.03624332, 0.00039676, 440.12081106, 0.00132254, -44.01208111, -0.00013225, -132.03624332, -0.00039676, -440.12081106, -0.00132254, 0.4, 0.3, 0.003, 0.0, 0.0, 10011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 11, 99999, 'P', 40011, 'Vy', 30011, 'Vz', 20011, 'My', 10011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170011, 70011, 170011, 11, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121011, 121011, 21011, 11, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170012, 19.55, 4.85, 0.0)
    ops.node(121012, 19.55, 4.85, 3.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 12, 170012, 121012, 0.1225, 29768114.55131588, 12403381.06304828, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20012, 92.74941763, 0.0007432, 112.01025183, 0.04475948, 11.20102518, 0.12923255, -92.74941763, -0.0007432, -112.01025183, -0.04475948, -11.20102518, -0.12923255, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10012, 103.39361545, 0.0007432, 124.86488002, 0.04475948, 12.486488, 0.12923255, -103.39361545, -0.0007432, -124.86488002, -0.04475948, -12.486488, -0.12923255, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20012, 12, 0.0, 171.98457123, 0.01486402, 171.98457123, 0.04459205, 120.38919986, -2375.88230098, 0.05, 2, 0, 70012, 21012, 2, 3)
    ops.uniaxialMaterial('LimitState', 40012, 42.99614281, 0.00012564, 128.98842842, 0.00037693, 429.96142808, 0.00125642, -42.99614281, -0.00012564, -128.98842842, -0.00037693, -429.96142808, -0.00125642, 0.4, 0.3, 0.003, 0.0, 0.0, 20012, 2)
    ops.limitCurve('ThreePoint', 10012, 12, 0.0, 171.98457123, 0.01486402, 171.98457123, 0.04459205, 120.38919986, -2375.88230098, 0.05, 2, 0, 70012, 21012, 1, 3)
    ops.uniaxialMaterial('LimitState', 30012, 42.99614281, 0.00012564, 128.98842842, 0.00037693, 429.96142808, 0.00125642, -42.99614281, -0.00012564, -128.98842842, -0.00037693, -429.96142808, -0.00125642, 0.4, 0.3, 0.003, 0.0, 0.0, 10012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 12, 99999, 'P', 40012, 'Vy', 30012, 'Vz', 20012, 'My', 10012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170012, 70012, 170012, 12, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121012, 121012, 21012, 12, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170013, 0.0, 9.7, 0.0)
    ops.node(121013, 0.0, 9.7, 3.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 13, 170013, 121013, 0.09, 29558680.10729924, 12316116.71137469, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20013, 47.74639789, 0.00077678, 57.78751506, 0.02661304, 5.77875151, 0.08270325, -47.74639789, -0.00077678, -57.78751506, -0.02661304, -5.77875151, -0.08270325, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10013, 50.58421272, 0.00077678, 61.22212531, 0.02661304, 6.12221253, 0.08270325, -50.58421272, -0.00077678, -61.22212531, -0.02661304, -6.12221253, -0.08270325, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20013, 13, 0.0, 97.18653319, 0.01553555, 97.18653319, 0.04660665, 68.03057323, -974.02087122, 0.05, 2, 0, 70013, 21013, 2, 3)
    ops.uniaxialMaterial('LimitState', 40013, 24.2966333, 9.732e-05, 72.88989989, 0.00029197, 242.96633297, 0.00097322, -24.2966333, -9.732e-05, -72.88989989, -0.00029197, -242.96633297, -0.00097322, 0.4, 0.3, 0.003, 0.0, 0.0, 20013, 2)
    ops.limitCurve('ThreePoint', 10013, 13, 0.0, 97.18653319, 0.01553555, 97.18653319, 0.04660665, 68.03057323, -974.02087122, 0.05, 2, 0, 70013, 21013, 1, 3)
    ops.uniaxialMaterial('LimitState', 30013, 24.2966333, 9.732e-05, 72.88989989, 0.00029197, 242.96633297, 0.00097322, -24.2966333, -9.732e-05, -72.88989989, -0.00029197, -242.96633297, -0.00097322, 0.4, 0.3, 0.003, 0.0, 0.0, 10013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 13, 99999, 'P', 40013, 'Vy', 30013, 'Vz', 20013, 'My', 10013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170013, 70013, 170013, 13, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121013, 121013, 21013, 13, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170014, 4.15, 9.7, 0.0)
    ops.node(121014, 4.15, 9.7, 3.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 14, 170014, 121014, 0.1225, 28532222.42798179, 11888426.01165908, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20014, 96.60848893, 0.00073947, 116.94674523, 0.03491985, 11.69467452, 0.09277313, -96.60848893, -0.00073947, -116.94674523, -0.03491985, -11.69467452, -0.09277313, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10014, 100.38922862, 0.00073947, 121.52341552, 0.03491985, 12.15234155, 0.09277313, -100.38922862, -0.00073947, -121.52341552, -0.03491985, -12.15234155, -0.09277313, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20014, 14, 0.0, 139.73891366, 0.01478933, 139.73891366, 0.04436799, 97.81723956, -1517.16596207, 0.05, 2, 0, 70014, 21014, 2, 3)
    ops.uniaxialMaterial('LimitState', 40014, 34.93472841, 0.00010651, 104.80418524, 0.00031952, 349.34728415, 0.00106507, -34.93472841, -0.00010651, -104.80418524, -0.00031952, -349.34728415, -0.00106507, 0.4, 0.3, 0.003, 0.0, 0.0, 20014, 2)
    ops.limitCurve('ThreePoint', 10014, 14, 0.0, 139.73891366, 0.01478933, 139.73891366, 0.04436799, 97.81723956, -1517.16596207, 0.05, 2, 0, 70014, 21014, 1, 3)
    ops.uniaxialMaterial('LimitState', 30014, 34.93472841, 0.00010651, 104.80418524, 0.00031952, 349.34728415, 0.00106507, -34.93472841, -0.00010651, -104.80418524, -0.00031952, -349.34728415, -0.00106507, 0.4, 0.3, 0.003, 0.0, 0.0, 10014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 14, 99999, 'P', 40014, 'Vy', 30014, 'Vz', 20014, 'My', 10014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170014, 70014, 170014, 14, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121014, 121014, 21014, 14, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170015, 8.3, 9.7, 0.0)
    ops.node(121015, 8.3, 9.7, 3.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 15, 170015, 121015, 0.09, 29524053.25041422, 12301688.85433926, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20015, 54.81945826, 0.00082857, 66.15705483, 0.02793648, 6.61570548, 0.07925715, -54.81945826, -0.00082857, -66.15705483, -0.02793648, -6.61570548, -0.07925715, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10015, 57.77854886, 0.00082857, 69.7281357, 0.02793648, 6.97281357, 0.07925715, -57.77854886, -0.00082857, -69.7281357, -0.02793648, -6.97281357, -0.07925715, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20015, 15, 0.0, 100.52484823, 0.01657135, 100.52484823, 0.04971404, 70.36739376, -925.1063247, 0.05, 2, 0, 70015, 21015, 2, 3)
    ops.uniaxialMaterial('LimitState', 40015, 25.13121206, 0.00010078, 75.39363618, 0.00030235, 251.31212059, 0.00100783, -25.13121206, -0.00010078, -75.39363618, -0.00030235, -251.31212059, -0.00100783, 0.4, 0.3, 0.003, 0.0, 0.0, 20015, 2)
    ops.limitCurve('ThreePoint', 10015, 15, 0.0, 100.52484823, 0.01657135, 100.52484823, 0.04971404, 70.36739376, -925.1063247, 0.05, 2, 0, 70015, 21015, 1, 3)
    ops.uniaxialMaterial('LimitState', 30015, 25.13121206, 0.00010078, 75.39363618, 0.00030235, 251.31212059, 0.00100783, -25.13121206, -0.00010078, -75.39363618, -0.00030235, -251.31212059, -0.00100783, 0.4, 0.3, 0.003, 0.0, 0.0, 10015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 15, 99999, 'P', 40015, 'Vy', 30015, 'Vz', 20015, 'My', 10015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170015, 70015, 170015, 15, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121015, 121015, 21015, 15, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170016, 11.25, 9.7, 0.0)
    ops.node(121016, 11.25, 9.7, 3.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 16, 170016, 121016, 0.09, 28709464.04057002, 11962276.68357084, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20016, 55.14882964, 0.00083742, 66.63844714, 0.02797446, 6.66384471, 0.07781916, -55.14882964, -0.00083742, -66.63844714, -0.02797446, -6.66384471, -0.07781916, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10016, 58.18765462, 0.00083742, 70.31037597, 0.02797446, 7.0310376, 0.07781916, -58.18765462, -0.00083742, -70.31037597, -0.02797446, -7.0310376, -0.07781916, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20016, 16, 0.0, 98.90630387, 0.01674843, 98.90630387, 0.05024529, 69.23441271, -939.91510215, 0.05, 2, 0, 70016, 21016, 2, 3)
    ops.uniaxialMaterial('LimitState', 40016, 24.72657597, 0.00010197, 74.1797279, 0.00030592, 247.26575966, 0.00101974, -24.72657597, -0.00010197, -74.1797279, -0.00030592, -247.26575966, -0.00101974, 0.4, 0.3, 0.003, 0.0, 0.0, 20016, 2)
    ops.limitCurve('ThreePoint', 10016, 16, 0.0, 98.90630387, 0.01674843, 98.90630387, 0.05024529, 69.23441271, -939.91510215, 0.05, 2, 0, 70016, 21016, 1, 3)
    ops.uniaxialMaterial('LimitState', 30016, 24.72657597, 0.00010197, 74.1797279, 0.00030592, 247.26575966, 0.00101974, -24.72657597, -0.00010197, -74.1797279, -0.00030592, -247.26575966, -0.00101974, 0.4, 0.3, 0.003, 0.0, 0.0, 10016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 16, 99999, 'P', 40016, 'Vy', 30016, 'Vz', 20016, 'My', 10016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170016, 70016, 170016, 16, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121016, 121016, 21016, 16, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170017, 15.4, 9.7, 0.0)
    ops.node(121017, 15.4, 9.7, 3.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 17, 170017, 121017, 0.1225, 30201579.21782729, 12583991.34076137, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20017, 96.11892869, 0.00074995, 116.00386013, 0.03477668, 11.60038601, 0.09557769, -96.11892869, -0.00074995, -116.00386013, -0.03477668, -11.60038601, -0.09557769, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10017, 99.62684117, 0.00074995, 120.23748397, 0.03477668, 12.0237484, 0.09557769, -99.62684117, -0.00074995, -120.23748397, -0.03477668, -12.0237484, -0.09557769, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20017, 17, 0.0, 145.17334934, 0.01499896, 145.17334934, 0.04499687, 101.62134454, -1495.82057819, 0.05, 2, 0, 70017, 21017, 2, 3)
    ops.uniaxialMaterial('LimitState', 40017, 36.29333734, 0.00010453, 108.88001201, 0.0003136, 362.93337336, 0.00104533, -36.29333734, -0.00010453, -108.88001201, -0.0003136, -362.93337336, -0.00104533, 0.4, 0.3, 0.003, 0.0, 0.0, 20017, 2)
    ops.limitCurve('ThreePoint', 10017, 17, 0.0, 145.17334934, 0.01499896, 145.17334934, 0.04499687, 101.62134454, -1495.82057819, 0.05, 2, 0, 70017, 21017, 1, 3)
    ops.uniaxialMaterial('LimitState', 30017, 36.29333734, 0.00010453, 108.88001201, 0.0003136, 362.93337336, 0.00104533, -36.29333734, -0.00010453, -108.88001201, -0.0003136, -362.93337336, -0.00104533, 0.4, 0.3, 0.003, 0.0, 0.0, 10017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 17, 99999, 'P', 40017, 'Vy', 30017, 'Vz', 20017, 'My', 10017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170017, 70017, 170017, 17, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121017, 121017, 21017, 17, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170018, 19.55, 9.7, 0.0)
    ops.node(121018, 19.55, 9.7, 3.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 18, 170018, 121018, 0.09, 30441083.63528915, 12683784.84803715, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20018, 48.82848692, 0.0008004, 58.98243201, 0.02631057, 5.8982432, 0.08351, -48.82848692, -0.0008004, -58.98243201, -0.02631057, -5.8982432, -0.08351, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10018, 51.66056553, 0.0008004, 62.40344492, 0.02631057, 6.24034449, 0.08351, -51.66056553, -0.0008004, -62.40344492, -0.02631057, -6.24034449, -0.08351, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20018, 18, 0.0, 99.81115847, 0.01600808, 99.81115847, 0.04802425, 69.86781093, -980.48880874, 0.05, 2, 0, 70018, 21018, 2, 3)
    ops.uniaxialMaterial('LimitState', 40018, 24.95278962, 9.705e-05, 74.85836886, 0.00029116, 249.52789618, 0.00097053, -24.95278962, -9.705e-05, -74.85836886, -0.00029116, -249.52789618, -0.00097053, 0.4, 0.3, 0.003, 0.0, 0.0, 20018, 2)
    ops.limitCurve('ThreePoint', 10018, 18, 0.0, 99.81115847, 0.01600808, 99.81115847, 0.04802425, 69.86781093, -980.48880874, 0.05, 2, 0, 70018, 21018, 1, 3)
    ops.uniaxialMaterial('LimitState', 30018, 24.95278962, 9.705e-05, 74.85836886, 0.00029116, 249.52789618, 0.00097053, -24.95278962, -9.705e-05, -74.85836886, -0.00029116, -249.52789618, -0.00097053, 0.4, 0.3, 0.003, 0.0, 0.0, 10018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 18, 99999, 'P', 40018, 'Vy', 30018, 'Vz', 20018, 'My', 10018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170018, 70018, 170018, 18, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121018, 121018, 21018, 18, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171001, 0.0, 0.0, 3.95)
    ops.node(122001, 0.0, 0.0, 6.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1001, 171001, 122001, 0.09, 29481137.17334965, 12283807.15556235, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21001, 32.63527624, 0.00070758, 39.58522857, 0.02596592, 3.95852286, 0.08545405, -32.63527624, -0.00070758, -39.58522857, -0.02596592, -3.95852286, -0.08545405, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11001, 35.1097273, 0.00070758, 42.58663447, 0.02596592, 4.25866345, 0.08545405, -35.1097273, -0.00070758, -42.58663447, -0.02596592, -4.25866345, -0.08545405, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21001, 1001, 0.0, 93.77713192, 0.0141517, 93.77713192, 0.04245509, 65.64399234, -1263.13944102, 0.05, 2, 0, 71001, 22001, 2, 3)
    ops.uniaxialMaterial('LimitState', 41001, 23.44428298, 7.889e-05, 70.33284894, 0.00023666, 234.4428298, 0.00078887, -23.44428298, -7.889e-05, -70.33284894, -0.00023666, -234.4428298, -0.00078887, 0.4, 0.3, 0.003, 0.0, 0.0, 21001, 2)
    ops.limitCurve('ThreePoint', 11001, 1001, 0.0, 93.77713192, 0.0141517, 93.77713192, 0.04245509, 65.64399234, -1263.13944102, 0.05, 2, 0, 71001, 22001, 1, 3)
    ops.uniaxialMaterial('LimitState', 31001, 23.44428298, 7.889e-05, 70.33284894, 0.00023666, 234.4428298, 0.00078887, -23.44428298, -7.889e-05, -70.33284894, -0.00023666, -234.4428298, -0.00078887, 0.4, 0.3, 0.003, 0.0, 0.0, 11001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1001, 99999, 'P', 41001, 'Vy', 31001, 'Vz', 21001, 'My', 11001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171001, 71001, 171001, 1001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122001, 122001, 22001, 1001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171002, 4.15, 0.0, 3.9)
    ops.node(122002, 4.15, 0.0, 6.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1002, 171002, 122002, 0.1225, 30412020.66071639, 12671675.27529849, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21002, 62.97569474, 0.00063495, 76.13709241, 0.04374249, 7.61370924, 0.13614114, -62.97569474, -0.00063495, -76.13709241, -0.04374249, -7.61370924, -0.13614114, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11002, 66.539881, 0.00063495, 80.44616403, 0.04374249, 8.0446164, 0.13614114, -66.539881, -0.00063495, -80.44616403, -0.04374249, -8.0446164, -0.13614114, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21002, 1002, 0.0, 172.17013549, 0.01269903, 172.17013549, 0.03809709, 120.51909484, -3431.05094112, 0.05, 2, 0, 71002, 22002, 2, 3)
    ops.uniaxialMaterial('LimitState', 41002, 43.04253387, 0.00010315, 129.12760162, 0.00030945, 430.42533873, 0.0010315, -43.04253387, -0.00010315, -129.12760162, -0.00030945, -430.42533873, -0.0010315, 0.4, 0.3, 0.003, 0.0, 0.0, 21002, 2)
    ops.limitCurve('ThreePoint', 11002, 1002, 0.0, 172.17013549, 0.01269903, 172.17013549, 0.03809709, 120.51909484, -3431.05094112, 0.05, 2, 0, 71002, 22002, 1, 3)
    ops.uniaxialMaterial('LimitState', 31002, 43.04253387, 0.00010315, 129.12760162, 0.00030945, 430.42533873, 0.0010315, -43.04253387, -0.00010315, -129.12760162, -0.00030945, -430.42533873, -0.0010315, 0.4, 0.3, 0.003, 0.0, 0.0, 11002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1002, 99999, 'P', 41002, 'Vy', 31002, 'Vz', 21002, 'My', 11002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171002, 71002, 171002, 1002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122002, 122002, 22002, 1002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171005, 15.4, 0.0, 3.9)
    ops.node(122005, 15.4, 0.0, 6.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1005, 171005, 122005, 0.1225, 28274496.97854435, 11781040.40772681, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21005, 62.13045496, 0.00064596, 75.44978675, 0.04449179, 7.54497867, 0.13274194, -62.13045496, -0.00064596, -75.44978675, -0.04449179, -7.54497867, -0.13274194, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11005, 65.63096406, 0.00064596, 79.700724, 0.04449179, 7.9700724, 0.13274194, -65.63096406, -0.00064596, -79.700724, -0.04449179, -7.9700724, -0.13274194, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21005, 1005, 0.0, 164.83646829, 0.0129191, 164.83646829, 0.0387573, 115.3855278, -3456.19111049, 0.05, 2, 0, 71005, 22005, 2, 3)
    ops.uniaxialMaterial('LimitState', 41005, 41.20911707, 0.00010622, 123.62735121, 0.00031867, 412.09117071, 0.00106222, -41.20911707, -0.00010622, -123.62735121, -0.00031867, -412.09117071, -0.00106222, 0.4, 0.3, 0.003, 0.0, 0.0, 21005, 2)
    ops.limitCurve('ThreePoint', 11005, 1005, 0.0, 164.83646829, 0.0129191, 164.83646829, 0.0387573, 115.3855278, -3456.19111049, 0.05, 2, 0, 71005, 22005, 1, 3)
    ops.uniaxialMaterial('LimitState', 31005, 41.20911707, 0.00010622, 123.62735121, 0.00031867, 412.09117071, 0.00106222, -41.20911707, -0.00010622, -123.62735121, -0.00031867, -412.09117071, -0.00106222, 0.4, 0.3, 0.003, 0.0, 0.0, 11005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1005, 99999, 'P', 41005, 'Vy', 31005, 'Vz', 21005, 'My', 11005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171005, 71005, 171005, 1005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122005, 122005, 22005, 1005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171006, 19.55, 0.0, 3.95)
    ops.node(122006, 19.55, 0.0, 6.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1006, 171006, 122006, 0.09, 29505554.99546578, 12293981.24811074, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21006, 32.49130679, 0.00067718, 39.40842429, 0.02638228, 3.94084243, 0.08589514, -32.49130679, -0.00067718, -39.40842429, -0.02638228, -3.94084243, -0.08589514, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11006, 35.15131375, 0.00067718, 42.63472367, 0.02638228, 4.26347237, 0.08589514, -35.15131375, -0.00067718, -42.63472367, -0.02638228, -4.26347237, -0.08589514, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21006, 1006, 0.0, 94.22154359, 0.01354353, 94.22154359, 0.04063058, 65.95508051, -1279.7021844, 0.05, 2, 0, 71006, 22006, 2, 3)
    ops.uniaxialMaterial('LimitState', 41006, 23.5553859, 7.92e-05, 70.66615769, 0.00023759, 235.55385897, 0.00079195, -23.5553859, -7.92e-05, -70.66615769, -0.00023759, -235.55385897, -0.00079195, 0.4, 0.3, 0.003, 0.0, 0.0, 21006, 2)
    ops.limitCurve('ThreePoint', 11006, 1006, 0.0, 94.22154359, 0.01354353, 94.22154359, 0.04063058, 65.95508051, -1279.7021844, 0.05, 2, 0, 71006, 22006, 1, 3)
    ops.uniaxialMaterial('LimitState', 31006, 23.5553859, 7.92e-05, 70.66615769, 0.00023759, 235.55385897, 0.00079195, -23.5553859, -7.92e-05, -70.66615769, -0.00023759, -235.55385897, -0.00079195, 0.4, 0.3, 0.003, 0.0, 0.0, 11006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1006, 99999, 'P', 41006, 'Vy', 31006, 'Vz', 21006, 'My', 11006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171006, 71006, 171006, 1006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122006, 122006, 22006, 1006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171007, 0.0, 4.85, 3.95)
    ops.node(122007, 0.0, 4.85, 6.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1007, 171007, 122007, 0.1225, 28186091.72620538, 11744204.88591891, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21007, 65.91343223, 0.00063885, 80.04057041, 0.03432024, 8.00405704, 0.0961774, -65.91343223, -0.00063885, -80.04057041, -0.03432024, -8.00405704, -0.0961774, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11007, 62.38576767, 0.00063885, 75.7568262, 0.03432024, 7.57568262, 0.0961774, -62.38576767, -0.00063885, -75.7568262, -0.03432024, -7.57568262, -0.0961774, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21007, 1007, 0.0, 133.72735068, 0.01277694, 133.72735068, 0.03833081, 93.60914548, -1925.33164411, 0.05, 2, 0, 71007, 22007, 2, 3)
    ops.uniaxialMaterial('LimitState', 41007, 33.43183767, 8.645e-05, 100.29551301, 0.00025934, 334.3183767, 0.00086446, -33.43183767, -8.645e-05, -100.29551301, -0.00025934, -334.3183767, -0.00086446, 0.4, 0.3, 0.003, 0.0, 0.0, 21007, 2)
    ops.limitCurve('ThreePoint', 11007, 1007, 0.0, 133.72735068, 0.01277694, 133.72735068, 0.03833081, 93.60914548, -1925.33164411, 0.05, 2, 0, 71007, 22007, 1, 3)
    ops.uniaxialMaterial('LimitState', 31007, 33.43183767, 8.645e-05, 100.29551301, 0.00025934, 334.3183767, 0.00086446, -33.43183767, -8.645e-05, -100.29551301, -0.00025934, -334.3183767, -0.00086446, 0.4, 0.3, 0.003, 0.0, 0.0, 11007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1007, 99999, 'P', 41007, 'Vy', 31007, 'Vz', 21007, 'My', 11007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171007, 71007, 171007, 1007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122007, 122007, 22007, 1007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171008, 4.15, 4.85, 3.9)
    ops.node(122008, 4.15, 4.85, 6.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1008, 171008, 122008, 0.1225, 29334061.25741038, 12222525.52392099, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21008, 81.54851297, 0.00065573, 98.55438437, 0.03402515, 9.85543844, 0.09279942, -81.54851297, -0.00065573, -98.55438437, -0.03402515, -9.85543844, -0.09279942, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11008, 75.15255874, 0.00065573, 90.82463788, 0.03402515, 9.08246379, 0.09279942, -75.15255874, -0.00065573, -90.82463788, -0.03402515, -9.08246379, -0.09279942, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21008, 1008, 0.0, 144.19859554, 0.01311463, 144.19859554, 0.03934388, 100.93901688, -1832.25828484, 0.05, 2, 0, 71008, 22008, 2, 3)
    ops.uniaxialMaterial('LimitState', 41008, 36.04964888, 8.957e-05, 108.14894665, 0.0002687, 360.49648884, 0.00089567, -36.04964888, -8.957e-05, -108.14894665, -0.0002687, -360.49648884, -0.00089567, 0.4, 0.3, 0.003, 0.0, 0.0, 21008, 2)
    ops.limitCurve('ThreePoint', 11008, 1008, 0.0, 144.19859554, 0.01311463, 144.19859554, 0.03934388, 100.93901688, -1832.25828484, 0.05, 2, 0, 71008, 22008, 1, 3)
    ops.uniaxialMaterial('LimitState', 31008, 36.04964888, 8.957e-05, 108.14894665, 0.0002687, 360.49648884, 0.00089567, -36.04964888, -8.957e-05, -108.14894665, -0.0002687, -360.49648884, -0.00089567, 0.4, 0.3, 0.003, 0.0, 0.0, 11008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1008, 99999, 'P', 41008, 'Vy', 31008, 'Vz', 21008, 'My', 11008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171008, 71008, 171008, 1008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122008, 122008, 22008, 1008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171009, 8.3, 4.85, 3.9)
    ops.node(122009, 8.3, 4.85, 6.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1009, 171009, 122009, 0.1225, 28364455.65409087, 11818523.18920453, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21009, 83.45157406, 0.00066419, 100.99316083, 0.03365146, 10.09931608, 0.09030588, -83.45157406, -0.00066419, -100.99316083, -0.03365146, -10.09931608, -0.09030588, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11009, 76.67106426, 0.00066419, 92.78738251, 0.03365146, 9.27873825, 0.09030588, -76.67106426, -0.00066419, -92.78738251, -0.03365146, -9.27873825, -0.09030588, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21009, 1009, 0.0, 139.92109126, 0.01328384, 139.92109126, 0.03985153, 97.94476388, -1796.6240207, 0.05, 2, 0, 71009, 22009, 2, 3)
    ops.uniaxialMaterial('LimitState', 41009, 34.98027282, 8.988e-05, 104.94081845, 0.00026964, 349.80272815, 0.00089881, -34.98027282, -8.988e-05, -104.94081845, -0.00026964, -349.80272815, -0.00089881, 0.4, 0.3, 0.003, 0.0, 0.0, 21009, 2)
    ops.limitCurve('ThreePoint', 11009, 1009, 0.0, 139.92109126, 0.01328384, 139.92109126, 0.03985153, 97.94476388, -1796.6240207, 0.05, 2, 0, 71009, 22009, 1, 3)
    ops.uniaxialMaterial('LimitState', 31009, 34.98027282, 8.988e-05, 104.94081845, 0.00026964, 349.80272815, 0.00089881, -34.98027282, -8.988e-05, -104.94081845, -0.00026964, -349.80272815, -0.00089881, 0.4, 0.3, 0.003, 0.0, 0.0, 11009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1009, 99999, 'P', 41009, 'Vy', 31009, 'Vz', 21009, 'My', 11009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171009, 71009, 171009, 1009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122009, 122009, 22009, 1009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171010, 11.25, 4.85, 3.9)
    ops.node(122010, 11.25, 4.85, 6.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1010, 171010, 122010, 0.1225, 28502347.76707625, 11875978.23628177, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21010, 83.10854342, 0.00066417, 100.55867449, 0.0338528, 10.05586745, 0.09078843, -83.10854342, -0.00066417, -100.55867449, -0.0338528, -10.05586745, -0.09078843, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11010, 76.42658205, 0.00066417, 92.47371533, 0.0338528, 9.24737153, 0.09078843, -76.42658205, -0.00066417, -92.47371533, -0.0338528, -9.24737153, -0.09078843, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21010, 1010, 0.0, 140.87069709, 0.01328342, 140.87069709, 0.03985025, 98.60948796, -1811.45821922, 0.05, 2, 0, 71010, 22010, 2, 3)
    ops.uniaxialMaterial('LimitState', 41010, 35.21767427, 9.005e-05, 105.65302281, 0.00027016, 352.17674271, 0.00090053, -35.21767427, -9.005e-05, -105.65302281, -0.00027016, -352.17674271, -0.00090053, 0.4, 0.3, 0.003, 0.0, 0.0, 21010, 2)
    ops.limitCurve('ThreePoint', 11010, 1010, 0.0, 140.87069709, 0.01328342, 140.87069709, 0.03985025, 98.60948796, -1811.45821922, 0.05, 2, 0, 71010, 22010, 1, 3)
    ops.uniaxialMaterial('LimitState', 31010, 35.21767427, 9.005e-05, 105.65302281, 0.00027016, 352.17674271, 0.00090053, -35.21767427, -9.005e-05, -105.65302281, -0.00027016, -352.17674271, -0.00090053, 0.4, 0.3, 0.003, 0.0, 0.0, 11010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1010, 99999, 'P', 41010, 'Vy', 31010, 'Vz', 21010, 'My', 11010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171010, 71010, 171010, 1010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122010, 122010, 22010, 1010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171011, 15.4, 4.85, 3.9)
    ops.node(122011, 15.4, 4.85, 6.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1011, 171011, 122011, 0.1225, 29711434.97458602, 12379764.57274417, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21011, 82.58279102, 0.00064822, 99.73546136, 0.03387227, 9.97354614, 0.0933173, -82.58279102, -0.00064822, -99.73546136, -0.03387227, -9.97354614, -0.0933173, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11011, 75.90978784, 0.00064822, 91.67645726, 0.03387227, 9.16764573, 0.0933173, -75.90978784, -0.00064822, -91.67645726, -0.03387227, -9.16764573, -0.0933173, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21011, 1011, 0.0, 145.17515006, 0.01296446, 145.17515006, 0.03889338, 101.62260504, -1817.83017873, 0.05, 2, 0, 71011, 22011, 2, 3)
    ops.uniaxialMaterial('LimitState', 41011, 36.29378751, 8.903e-05, 108.88136254, 0.00026708, 362.93787514, 0.00089028, -36.29378751, -8.903e-05, -108.88136254, -0.00026708, -362.93787514, -0.00089028, 0.4, 0.3, 0.003, 0.0, 0.0, 21011, 2)
    ops.limitCurve('ThreePoint', 11011, 1011, 0.0, 145.17515006, 0.01296446, 145.17515006, 0.03889338, 101.62260504, -1817.83017873, 0.05, 2, 0, 71011, 22011, 1, 3)
    ops.uniaxialMaterial('LimitState', 31011, 36.29378751, 8.903e-05, 108.88136254, 0.00026708, 362.93787514, 0.00089028, -36.29378751, -8.903e-05, -108.88136254, -0.00026708, -362.93787514, -0.00089028, 0.4, 0.3, 0.003, 0.0, 0.0, 11011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1011, 99999, 'P', 41011, 'Vy', 31011, 'Vz', 21011, 'My', 11011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171011, 71011, 171011, 1011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122011, 122011, 22011, 1011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171012, 19.55, 4.85, 3.95)
    ops.node(122012, 19.55, 4.85, 6.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1012, 171012, 122012, 0.1225, 28835944.71810736, 12014976.96587807, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21012, 65.91240275, 0.00064204, 79.94666862, 0.03429067, 7.99466686, 0.09715578, -65.91240275, -0.00064204, -79.94666862, -0.03429067, -7.99466686, -0.09715578, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11012, 62.45653118, 0.00064204, 75.75496254, 0.03429067, 7.57549625, 0.09715578, -62.45653118, -0.00064204, -75.75496254, -0.03429067, -7.57549625, -0.09715578, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21012, 1012, 0.0, 135.41325391, 0.01284078, 135.41325391, 0.03852235, 94.78927773, -1899.03487978, 0.05, 2, 0, 71012, 22012, 2, 3)
    ops.uniaxialMaterial('LimitState', 41012, 33.85331348, 8.556e-05, 101.55994043, 0.00025669, 338.53313476, 0.00085563, -33.85331348, -8.556e-05, -101.55994043, -0.00025669, -338.53313476, -0.00085563, 0.4, 0.3, 0.003, 0.0, 0.0, 21012, 2)
    ops.limitCurve('ThreePoint', 11012, 1012, 0.0, 135.41325391, 0.01284078, 135.41325391, 0.03852235, 94.78927773, -1899.03487978, 0.05, 2, 0, 71012, 22012, 1, 3)
    ops.uniaxialMaterial('LimitState', 31012, 33.85331348, 8.556e-05, 101.55994043, 0.00025669, 338.53313476, 0.00085563, -33.85331348, -8.556e-05, -101.55994043, -0.00025669, -338.53313476, -0.00085563, 0.4, 0.3, 0.003, 0.0, 0.0, 11012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1012, 99999, 'P', 41012, 'Vy', 31012, 'Vz', 21012, 'My', 11012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171012, 71012, 171012, 1012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122012, 122012, 22012, 1012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171013, 0.0, 9.7, 3.95)
    ops.node(122013, 0.0, 9.7, 6.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1013, 171013, 122013, 0.09, 28414397.05274494, 11839332.10531039, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21013, 32.98930869, 0.00068513, 40.1040263, 0.02659259, 4.01040263, 0.08491919, -32.98930869, -0.00068513, -40.1040263, -0.02659259, -4.01040263, -0.08491919, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11013, 35.81556026, 0.00068513, 43.53980812, 0.02659259, 4.35398081, 0.08491919, -35.81556026, -0.00068513, -43.53980812, -0.02659259, -4.35398081, -0.08491919, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21013, 1013, 0.0, 91.47689464, 0.01370267, 91.47689464, 0.041108, 64.03382625, -1285.49209814, 0.05, 2, 0, 71013, 22013, 2, 3)
    ops.uniaxialMaterial('LimitState', 41013, 22.86922366, 7.984e-05, 68.60767098, 0.00023952, 228.6922366, 0.00079841, -22.86922366, -7.984e-05, -68.60767098, -0.00023952, -228.6922366, -0.00079841, 0.4, 0.3, 0.003, 0.0, 0.0, 21013, 2)
    ops.limitCurve('ThreePoint', 11013, 1013, 0.0, 91.47689464, 0.01370267, 91.47689464, 0.041108, 64.03382625, -1285.49209814, 0.05, 2, 0, 71013, 22013, 1, 3)
    ops.uniaxialMaterial('LimitState', 31013, 22.86922366, 7.984e-05, 68.60767098, 0.00023952, 228.6922366, 0.00079841, -22.86922366, -7.984e-05, -68.60767098, -0.00023952, -228.6922366, -0.00079841, 0.4, 0.3, 0.003, 0.0, 0.0, 11013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1013, 99999, 'P', 41013, 'Vy', 31013, 'Vz', 21013, 'My', 11013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171013, 71013, 171013, 1013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122013, 122013, 22013, 1013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171014, 4.15, 9.7, 3.875)
    ops.node(122014, 4.15, 9.7, 6.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1014, 171014, 122014, 0.1225, 28819413.93867648, 12008089.1411152, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21014, 62.38718325, 0.00064131, 75.68661771, 0.04409001, 7.56866177, 0.13350659, -62.38718325, -0.00064131, -75.68661771, -0.04409001, -7.56866177, -0.13350659, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11014, 65.92468482, 0.00064131, 79.97822882, 0.04409001, 7.99782288, 0.13350659, -65.92468482, -0.00064131, -79.97822882, -0.04409001, -7.99782288, -0.13350659, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21014, 1014, 0.0, 164.77809265, 0.01282622, 164.77809265, 0.03847866, 115.34466486, -3345.13917224, 0.05, 2, 0, 71014, 22014, 2, 3)
    ops.uniaxialMaterial('LimitState', 41014, 41.19452316, 0.00010418, 123.58356949, 0.00031253, 411.94523164, 0.00104177, -41.19452316, -0.00010418, -123.58356949, -0.00031253, -411.94523164, -0.00104177, 0.4, 0.3, 0.003, 0.0, 0.0, 21014, 2)
    ops.limitCurve('ThreePoint', 11014, 1014, 0.0, 164.77809265, 0.01282622, 164.77809265, 0.03847866, 115.34466486, -3345.13917224, 0.05, 2, 0, 71014, 22014, 1, 3)
    ops.uniaxialMaterial('LimitState', 31014, 41.19452316, 0.00010418, 123.58356949, 0.00031253, 411.94523164, 0.00104177, -41.19452316, -0.00010418, -123.58356949, -0.00031253, -411.94523164, -0.00104177, 0.4, 0.3, 0.003, 0.0, 0.0, 11014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1014, 99999, 'P', 41014, 'Vy', 31014, 'Vz', 21014, 'My', 11014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171014, 71014, 171014, 1014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122014, 122014, 22014, 1014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171015, 8.3, 9.7, 3.875)
    ops.node(122015, 8.3, 9.7, 6.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1015, 171015, 122015, 0.09, 29154531.46772906, 12147721.44488711, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21015, 44.18295408, 0.00071387, 53.50974612, 0.03564351, 5.35097461, 0.10583877, -44.18295408, -0.00071387, -53.50974612, -0.03564351, -5.35097461, -0.10583877, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11015, 44.18295408, 0.00071387, 53.50974612, 0.03564351, 5.35097461, 0.10583877, -44.18295408, -0.00071387, -53.50974612, -0.03564351, -5.35097461, -0.10583877, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21015, 1015, 0.0, 109.86762287, 0.01427742, 109.86762287, 0.04283226, 76.90733601, -1679.63218215, 0.05, 2, 0, 71015, 22015, 2, 3)
    ops.uniaxialMaterial('LimitState', 41015, 27.46690572, 9.346e-05, 82.40071716, 0.00028037, 274.66905719, 0.00093458, -27.46690572, -9.346e-05, -82.40071716, -0.00028037, -274.66905719, -0.00093458, 0.4, 0.3, 0.003, 0.0, 0.0, 21015, 2)
    ops.limitCurve('ThreePoint', 11015, 1015, 0.0, 109.86762287, 0.01427742, 109.86762287, 0.04283226, 76.90733601, -1679.63218215, 0.05, 2, 0, 71015, 22015, 1, 3)
    ops.uniaxialMaterial('LimitState', 31015, 27.46690572, 9.346e-05, 82.40071716, 0.00028037, 274.66905719, 0.00093458, -27.46690572, -9.346e-05, -82.40071716, -0.00028037, -274.66905719, -0.00093458, 0.4, 0.3, 0.003, 0.0, 0.0, 11015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1015, 99999, 'P', 41015, 'Vy', 31015, 'Vz', 21015, 'My', 11015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171015, 71015, 171015, 1015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122015, 122015, 22015, 1015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171016, 11.25, 9.7, 3.875)
    ops.node(122016, 11.25, 9.7, 6.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1016, 171016, 122016, 0.09, 29422481.4410108, 12259367.26708784, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21016, 45.06063234, 0.00071021, 54.54427481, 0.0353709, 5.45442748, 0.10603975, -45.06063234, -0.00071021, -54.54427481, -0.0353709, -5.45442748, -0.10603975, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11016, 45.06063234, 0.00071021, 54.54427481, 0.0353709, 5.45442748, 0.10603975, -45.06063234, -0.00071021, -54.54427481, -0.0353709, -5.45442748, -0.10603975, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21016, 1016, 0.0, 109.89090381, 0.01420424, 109.89090381, 0.04261272, 76.92363267, -1650.47572487, 0.05, 2, 0, 71016, 22016, 2, 3)
    ops.uniaxialMaterial('LimitState', 41016, 27.47272595, 9.263e-05, 82.41817786, 0.00027788, 274.72725953, 0.00092626, -27.47272595, -9.263e-05, -82.41817786, -0.00027788, -274.72725953, -0.00092626, 0.4, 0.3, 0.003, 0.0, 0.0, 21016, 2)
    ops.limitCurve('ThreePoint', 11016, 1016, 0.0, 109.89090381, 0.01420424, 109.89090381, 0.04261272, 76.92363267, -1650.47572487, 0.05, 2, 0, 71016, 22016, 1, 3)
    ops.uniaxialMaterial('LimitState', 31016, 27.47272595, 9.263e-05, 82.41817786, 0.00027788, 274.72725953, 0.00092626, -27.47272595, -9.263e-05, -82.41817786, -0.00027788, -274.72725953, -0.00092626, 0.4, 0.3, 0.003, 0.0, 0.0, 11016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1016, 99999, 'P', 41016, 'Vy', 31016, 'Vz', 21016, 'My', 11016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171016, 71016, 171016, 1016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122016, 122016, 22016, 1016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171017, 15.4, 9.7, 3.875)
    ops.node(122017, 15.4, 9.7, 6.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1017, 171017, 122017, 0.1225, 28763916.87455272, 11984965.36439697, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21017, 61.76221245, 0.00065002, 74.93631236, 0.0441761, 7.49363124, 0.13347757, -61.76221245, -0.00065002, -74.93631236, -0.0441761, -7.49363124, -0.13347757, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11017, 65.1199877, 0.00065002, 79.01031303, 0.0441761, 7.9010313, 0.13347757, -65.1199877, -0.00065002, -79.01031303, -0.0441761, -7.9010313, -0.13347757, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21017, 1017, 0.0, 164.67348828, 0.01300033, 164.67348828, 0.03900098, 115.27144179, -3350.35916597, 0.05, 2, 0, 71017, 22017, 2, 3)
    ops.uniaxialMaterial('LimitState', 41017, 41.16837207, 0.00010431, 123.50511621, 0.00031294, 411.68372069, 0.00104312, -41.16837207, -0.00010431, -123.50511621, -0.00031294, -411.68372069, -0.00104312, 0.4, 0.3, 0.003, 0.0, 0.0, 21017, 2)
    ops.limitCurve('ThreePoint', 11017, 1017, 0.0, 164.67348828, 0.01300033, 164.67348828, 0.03900098, 115.27144179, -3350.35916597, 0.05, 2, 0, 71017, 22017, 1, 3)
    ops.uniaxialMaterial('LimitState', 31017, 41.16837207, 0.00010431, 123.50511621, 0.00031294, 411.68372069, 0.00104312, -41.16837207, -0.00010431, -123.50511621, -0.00031294, -411.68372069, -0.00104312, 0.4, 0.3, 0.003, 0.0, 0.0, 11017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1017, 99999, 'P', 41017, 'Vy', 31017, 'Vz', 21017, 'My', 11017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171017, 71017, 171017, 1017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122017, 122017, 22017, 1017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171018, 19.55, 9.7, 3.95)
    ops.node(122018, 19.55, 9.7, 6.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1018, 171018, 122018, 0.09, 29813771.69456388, 12422404.87273495, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21018, 32.36756067, 0.00067399, 39.23037179, 0.0260375, 3.92303718, 0.08585596, -32.36756067, -0.00067399, -39.23037179, -0.0260375, -3.92303718, -0.08585596, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11018, 34.99378452, 0.00067399, 42.41342716, 0.0260375, 4.24134272, 0.08585596, -34.99378452, -0.00067399, -42.41342716, -0.0260375, -4.24134272, -0.08585596, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21018, 1018, 0.0, 94.35139065, 0.01347987, 94.35139065, 0.04043962, 66.04597346, -1249.44461071, 0.05, 2, 0, 71018, 22018, 2, 3)
    ops.uniaxialMaterial('LimitState', 41018, 23.58784766, 7.848e-05, 70.76354299, 0.00023545, 235.87847663, 0.00078484, -23.58784766, -7.848e-05, -70.76354299, -0.00023545, -235.87847663, -0.00078484, 0.4, 0.3, 0.003, 0.0, 0.0, 21018, 2)
    ops.limitCurve('ThreePoint', 11018, 1018, 0.0, 94.35139065, 0.01347987, 94.35139065, 0.04043962, 66.04597346, -1249.44461071, 0.05, 2, 0, 71018, 22018, 1, 3)
    ops.uniaxialMaterial('LimitState', 31018, 23.58784766, 7.848e-05, 70.76354299, 0.00023545, 235.87847663, 0.00078484, -23.58784766, -7.848e-05, -70.76354299, -0.00023545, -235.87847663, -0.00078484, 0.4, 0.3, 0.003, 0.0, 0.0, 11018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1018, 99999, 'P', 41018, 'Vy', 31018, 'Vz', 21018, 'My', 11018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171018, 71018, 171018, 1018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122018, 122018, 22018, 1018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172001, 0.0, 0.0, 7.05)
    ops.node(123001, 0.0, 0.0, 9.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2001, 172001, 123001, 0.0625, 29456380.08809245, 12273491.70337186, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22001, 22.28146517, 0.00078346, 27.04596147, 0.02910737, 2.70459615, 0.09955378, -22.28146517, -0.00078346, -27.04596147, -0.02910737, -2.70459615, -0.09955378, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12001, 24.37166135, 0.00078346, 29.58310904, 0.02910737, 2.9583109, 0.09955378, -24.37166135, -0.00078346, -29.58310904, -0.02910737, -2.9583109, -0.09955378, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22001, 2001, 0.0, 70.23164776, 0.01566928, 70.23164776, 0.04700785, 49.16215343, -1226.45534044, 0.05, 2, 0, 72001, 23001, 2, 3)
    ops.uniaxialMaterial('LimitState', 42001, 17.55791194, 8.515e-05, 52.67373582, 0.00025544, 175.57911939, 0.00085147, -17.55791194, -8.515e-05, -52.67373582, -0.00025544, -175.57911939, -0.00085147, 0.4, 0.3, 0.003, 0.0, 0.0, 22001, 2)
    ops.limitCurve('ThreePoint', 12001, 2001, 0.0, 70.23164776, 0.01566928, 70.23164776, 0.04700785, 49.16215343, -1226.45534044, 0.05, 2, 0, 72001, 23001, 1, 3)
    ops.uniaxialMaterial('LimitState', 32001, 17.55791194, 8.515e-05, 52.67373582, 0.00025544, 175.57911939, 0.00085147, -17.55791194, -8.515e-05, -52.67373582, -0.00025544, -175.57911939, -0.00085147, 0.4, 0.3, 0.003, 0.0, 0.0, 12001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2001, 99999, 'P', 42001, 'Vy', 32001, 'Vz', 22001, 'My', 12001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172001, 72001, 172001, 2001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123001, 123001, 23001, 2001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172002, 4.15, 0.0, 6.975)
    ops.node(123002, 4.15, 0.0, 9.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2002, 172002, 123002, 0.0625, 29505534.20344594, 12293972.58476914, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22002, 30.90402023, 0.00087487, 37.39357374, 0.03129368, 3.73935737, 0.09565446, -30.90402023, -0.00087487, -37.39357374, -0.03129368, -3.73935737, -0.09565446, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12002, 30.90402023, 0.00087487, 37.39357374, 0.03129368, 3.73935737, 0.09565446, -30.90402023, -0.00087487, -37.39357374, -0.03129368, -3.73935737, -0.09565446, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22002, 2002, 0.0, 73.54919232, 0.0174974, 73.54919232, 0.05249219, 51.48443462, -1011.05262193, 0.05, 2, 0, 72002, 23002, 2, 3)
    ops.uniaxialMaterial('LimitState', 42002, 18.38729808, 8.902e-05, 55.16189424, 0.00026706, 183.8729808, 0.0008902, -18.38729808, -8.902e-05, -55.16189424, -0.00026706, -183.8729808, -0.0008902, 0.4, 0.3, 0.003, 0.0, 0.0, 22002, 2)
    ops.limitCurve('ThreePoint', 12002, 2002, 0.0, 73.54919232, 0.0174974, 73.54919232, 0.05249219, 51.48443462, -1011.05262193, 0.05, 2, 0, 72002, 23002, 1, 3)
    ops.uniaxialMaterial('LimitState', 32002, 18.38729808, 8.902e-05, 55.16189424, 0.00026706, 183.8729808, 0.0008902, -18.38729808, -8.902e-05, -55.16189424, -0.00026706, -183.8729808, -0.0008902, 0.4, 0.3, 0.003, 0.0, 0.0, 12002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2002, 99999, 'P', 42002, 'Vy', 32002, 'Vz', 22002, 'My', 12002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172002, 72002, 172002, 2002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123002, 123002, 23002, 2002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172005, 15.4, 0.0, 6.975)
    ops.node(123005, 15.4, 0.0, 9.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2005, 172005, 123005, 0.0625, 29240689.8067724, 12183620.75282183, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22005, 31.05197676, 0.00086011, 37.5919855, 0.03095103, 3.75919855, 0.0948777, -31.05197676, -0.00086011, -37.5919855, -0.03095103, -3.75919855, -0.0948777, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12005, 31.05197676, 0.00086011, 37.5919855, 0.03095103, 3.75919855, 0.0948777, -31.05197676, -0.00086011, -37.5919855, -0.03095103, -3.75919855, -0.0948777, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22005, 2005, 0.0, 72.50809122, 0.01720225, 72.50809122, 0.05160674, 50.75566386, -990.20334871, 0.05, 2, 0, 72005, 23005, 2, 3)
    ops.uniaxialMaterial('LimitState', 42005, 18.12702281, 8.855e-05, 54.38106842, 0.00026566, 181.27022806, 0.00088555, -18.12702281, -8.855e-05, -54.38106842, -0.00026566, -181.27022806, -0.00088555, 0.4, 0.3, 0.003, 0.0, 0.0, 22005, 2)
    ops.limitCurve('ThreePoint', 12005, 2005, 0.0, 72.50809122, 0.01720225, 72.50809122, 0.05160674, 50.75566386, -990.20334871, 0.05, 2, 0, 72005, 23005, 1, 3)
    ops.uniaxialMaterial('LimitState', 32005, 18.12702281, 8.855e-05, 54.38106842, 0.00026566, 181.27022806, 0.00088555, -18.12702281, -8.855e-05, -54.38106842, -0.00026566, -181.27022806, -0.00088555, 0.4, 0.3, 0.003, 0.0, 0.0, 12005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2005, 99999, 'P', 42005, 'Vy', 32005, 'Vz', 22005, 'My', 12005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172005, 72005, 172005, 2005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123005, 123005, 23005, 2005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172006, 19.55, 0.0, 7.05)
    ops.node(123006, 19.55, 0.0, 9.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2006, 172006, 123006, 0.0625, 30227655.90669308, 12594856.62778878, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22006, 22.21783419, 0.0008338, 26.9180462, 0.02851418, 2.69180462, 0.09972928, -22.21783419, -0.0008338, -26.9180462, -0.02851418, -2.69180462, -0.09972928, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12006, 24.00397358, 0.0008338, 29.08204573, 0.02851418, 2.90820457, 0.09972928, -24.00397358, -0.0008338, -29.08204573, -0.02851418, -2.90820457, -0.09972928, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22006, 2006, 0.0, 70.96212368, 0.01667595, 70.96212368, 0.05002784, 49.67348658, -1187.94825796, 0.05, 2, 0, 72006, 23006, 2, 3)
    ops.uniaxialMaterial('LimitState', 42006, 17.74053092, 8.384e-05, 53.22159276, 0.00025151, 177.4053092, 0.00083837, -17.74053092, -8.384e-05, -53.22159276, -0.00025151, -177.4053092, -0.00083837, 0.4, 0.3, 0.003, 0.0, 0.0, 22006, 2)
    ops.limitCurve('ThreePoint', 12006, 2006, 0.0, 70.96212368, 0.01667595, 70.96212368, 0.05002784, 49.67348658, -1187.94825796, 0.05, 2, 0, 72006, 23006, 1, 3)
    ops.uniaxialMaterial('LimitState', 32006, 17.74053092, 8.384e-05, 53.22159276, 0.00025151, 177.4053092, 0.00083837, -17.74053092, -8.384e-05, -53.22159276, -0.00025151, -177.4053092, -0.00083837, 0.4, 0.3, 0.003, 0.0, 0.0, 12006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2006, 99999, 'P', 42006, 'Vy', 32006, 'Vz', 22006, 'My', 12006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172006, 72006, 172006, 2006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123006, 123006, 23006, 2006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172007, 0.0, 4.85, 7.05)
    ops.node(123007, 0.0, 4.85, 9.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2007, 172007, 123007, 0.0625, 29673107.50280973, 12363794.79283739, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22007, 31.79214588, 0.00085979, 38.44868213, 0.02593065, 3.84486821, 0.07951053, -31.79214588, -0.00085979, -38.44868213, -0.02593065, -3.84486821, -0.07951053, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12007, 31.79214588, 0.00085979, 38.44868213, 0.02593065, 3.84486821, 0.07951053, -31.79214588, -0.00085979, -38.44868213, -0.02593065, -3.84486821, -0.07951053, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22007, 2007, 0.0, 68.11228383, 0.01719586, 68.11228383, 0.05158758, 47.67859868, -793.24360531, 0.05, 2, 0, 72007, 23007, 2, 3)
    ops.uniaxialMaterial('LimitState', 42007, 17.02807096, 8.197e-05, 51.08421288, 0.00024592, 170.28070958, 0.00081974, -17.02807096, -8.197e-05, -51.08421288, -0.00024592, -170.28070958, -0.00081974, 0.4, 0.3, 0.003, 0.0, 0.0, 22007, 2)
    ops.limitCurve('ThreePoint', 12007, 2007, 0.0, 68.11228383, 0.01719586, 68.11228383, 0.05158758, 47.67859868, -793.24360531, 0.05, 2, 0, 72007, 23007, 1, 3)
    ops.uniaxialMaterial('LimitState', 32007, 17.02807096, 8.197e-05, 51.08421288, 0.00024592, 170.28070958, 0.00081974, -17.02807096, -8.197e-05, -51.08421288, -0.00024592, -170.28070958, -0.00081974, 0.4, 0.3, 0.003, 0.0, 0.0, 12007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2007, 99999, 'P', 42007, 'Vy', 32007, 'Vz', 22007, 'My', 12007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172007, 72007, 172007, 2007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123007, 123007, 23007, 2007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172008, 4.15, 4.85, 6.975)
    ops.node(123008, 4.15, 4.85, 9.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2008, 172008, 123008, 0.0625, 28635075.94096793, 11931281.64206997, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22008, 36.52646994, 0.00088327, 44.08969065, 0.02534491, 4.40896907, 0.07181209, -36.52646994, -0.00088327, -44.08969065, -0.02534491, -4.40896907, -0.07181209, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12008, 36.52646994, 0.00088327, 44.08969065, 0.02534491, 4.40896907, 0.07181209, -36.52646994, -0.00088327, -44.08969065, -0.02534491, -4.40896907, -0.07181209, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22008, 2008, 0.0, 68.79348486, 0.01766531, 68.79348486, 0.05299594, 48.1554394, -761.10682754, 0.05, 2, 0, 72008, 23008, 2, 3)
    ops.uniaxialMaterial('LimitState', 42008, 17.19837122, 8.58e-05, 51.59511365, 0.00025739, 171.98371215, 0.00085795, -17.19837122, -8.58e-05, -51.59511365, -0.00025739, -171.98371215, -0.00085795, 0.4, 0.3, 0.003, 0.0, 0.0, 22008, 2)
    ops.limitCurve('ThreePoint', 12008, 2008, 0.0, 68.79348486, 0.01766531, 68.79348486, 0.05299594, 48.1554394, -761.10682754, 0.05, 2, 0, 72008, 23008, 1, 3)
    ops.uniaxialMaterial('LimitState', 32008, 17.19837122, 8.58e-05, 51.59511365, 0.00025739, 171.98371215, 0.00085795, -17.19837122, -8.58e-05, -51.59511365, -0.00025739, -171.98371215, -0.00085795, 0.4, 0.3, 0.003, 0.0, 0.0, 12008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2008, 99999, 'P', 42008, 'Vy', 32008, 'Vz', 22008, 'My', 12008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172008, 72008, 172008, 2008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123008, 123008, 23008, 2008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172009, 8.3, 4.85, 6.975)
    ops.node(123009, 8.3, 4.85, 9.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2009, 172009, 123009, 0.0625, 29963530.92484351, 12484804.55201813, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22009, 37.16140297, 0.00087733, 44.75025851, 0.02540758, 4.47502585, 0.0737729, -37.16140297, -0.00087733, -44.75025851, -0.02540758, -4.47502585, -0.0737729, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12009, 37.16140297, 0.00087733, 44.75025851, 0.02540758, 4.47502585, 0.0737729, -37.16140297, -0.00087733, -44.75025851, -0.02540758, -4.47502585, -0.0737729, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22009, 2009, 0.0, 72.48339343, 0.01754651, 72.48339343, 0.05263954, 50.7383754, -783.92808744, 0.05, 2, 0, 72009, 23009, 2, 3)
    ops.uniaxialMaterial('LimitState', 42009, 18.12084836, 8.639e-05, 54.36254507, 0.00025917, 181.20848357, 0.00086389, -18.12084836, -8.639e-05, -54.36254507, -0.00025917, -181.20848357, -0.00086389, 0.4, 0.3, 0.003, 0.0, 0.0, 22009, 2)
    ops.limitCurve('ThreePoint', 12009, 2009, 0.0, 72.48339343, 0.01754651, 72.48339343, 0.05263954, 50.7383754, -783.92808744, 0.05, 2, 0, 72009, 23009, 1, 3)
    ops.uniaxialMaterial('LimitState', 32009, 18.12084836, 8.639e-05, 54.36254507, 0.00025917, 181.20848357, 0.00086389, -18.12084836, -8.639e-05, -54.36254507, -0.00025917, -181.20848357, -0.00086389, 0.4, 0.3, 0.003, 0.0, 0.0, 12009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2009, 99999, 'P', 42009, 'Vy', 32009, 'Vz', 22009, 'My', 12009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172009, 72009, 172009, 2009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123009, 123009, 23009, 2009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172010, 11.25, 4.85, 6.975)
    ops.node(123010, 11.25, 4.85, 9.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2010, 172010, 123010, 0.0625, 31136101.84242232, 12973375.76767597, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22010, 36.35809406, 0.00088556, 43.68251663, 0.025504, 4.36825166, 0.07579508, -36.35809406, -0.00088556, -43.68251663, -0.025504, -4.36825166, -0.07579508, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12010, 36.35809406, 0.00088556, 43.68251663, 0.025504, 4.36825166, 0.07579508, -36.35809406, -0.00088556, -43.68251663, -0.025504, -4.36825166, -0.07579508, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22010, 2010, 0.0, 74.54442038, 0.01771111, 74.54442038, 0.05313333, 52.18109427, -777.15243965, 0.05, 2, 0, 72010, 23010, 2, 3)
    ops.uniaxialMaterial('LimitState', 42010, 18.63610509, 8.55e-05, 55.90831528, 0.0002565, 186.36105095, 0.000855, -18.63610509, -8.55e-05, -55.90831528, -0.0002565, -186.36105095, -0.000855, 0.4, 0.3, 0.003, 0.0, 0.0, 22010, 2)
    ops.limitCurve('ThreePoint', 12010, 2010, 0.0, 74.54442038, 0.01771111, 74.54442038, 0.05313333, 52.18109427, -777.15243965, 0.05, 2, 0, 72010, 23010, 1, 3)
    ops.uniaxialMaterial('LimitState', 32010, 18.63610509, 8.55e-05, 55.90831528, 0.0002565, 186.36105095, 0.000855, -18.63610509, -8.55e-05, -55.90831528, -0.0002565, -186.36105095, -0.000855, 0.4, 0.3, 0.003, 0.0, 0.0, 12010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2010, 99999, 'P', 42010, 'Vy', 32010, 'Vz', 22010, 'My', 12010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172010, 72010, 172010, 2010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123010, 123010, 23010, 2010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172011, 15.4, 4.85, 6.975)
    ops.node(123011, 15.4, 4.85, 9.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2011, 172011, 123011, 0.0625, 29493935.56057769, 12289139.81690737, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22011, 35.81358013, 0.00088637, 43.17727695, 0.02596351, 4.31772769, 0.07404985, -35.81358013, -0.00088637, -43.17727695, -0.02596351, -4.31772769, -0.07404985, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12011, 35.81358013, 0.00088637, 43.17727695, 0.02596351, 4.31772769, 0.07404985, -35.81358013, -0.00088637, -43.17727695, -0.02596351, -4.31772769, -0.07404985, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22011, 2011, 0.0, 70.79216565, 0.01772736, 70.79216565, 0.05318207, 49.55451596, -770.86577433, 0.05, 2, 0, 72011, 23011, 2, 3)
    ops.uniaxialMaterial('LimitState', 42011, 17.69804141, 8.572e-05, 53.09412424, 0.00025715, 176.98041413, 0.00085717, -17.69804141, -8.572e-05, -53.09412424, -0.00025715, -176.98041413, -0.00085717, 0.4, 0.3, 0.003, 0.0, 0.0, 22011, 2)
    ops.limitCurve('ThreePoint', 12011, 2011, 0.0, 70.79216565, 0.01772736, 70.79216565, 0.05318207, 49.55451596, -770.86577433, 0.05, 2, 0, 72011, 23011, 1, 3)
    ops.uniaxialMaterial('LimitState', 32011, 17.69804141, 8.572e-05, 53.09412424, 0.00025715, 176.98041413, 0.00085717, -17.69804141, -8.572e-05, -53.09412424, -0.00025715, -176.98041413, -0.00085717, 0.4, 0.3, 0.003, 0.0, 0.0, 12011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2011, 99999, 'P', 42011, 'Vy', 32011, 'Vz', 22011, 'My', 12011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172011, 72011, 172011, 2011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123011, 123011, 23011, 2011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172012, 19.55, 4.85, 7.05)
    ops.node(123012, 19.55, 4.85, 9.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2012, 172012, 123012, 0.0625, 30597044.86677891, 12748768.69449121, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22012, 32.03624646, 0.00084248, 38.66549024, 0.02578522, 3.86654902, 0.08053698, -32.03624646, -0.00084248, -38.66549024, -0.02578522, -3.86654902, -0.08053698, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12012, 32.03624646, 0.00084248, 38.66549024, 0.02578522, 3.86654902, 0.08053698, -32.03624646, -0.00084248, -38.66549024, -0.02578522, -3.86654902, -0.08053698, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22012, 2012, 0.0, 69.72006716, 0.01684965, 69.72006716, 0.05054895, 48.80404701, -788.11859984, 0.05, 2, 0, 72012, 23012, 2, 3)
    ops.uniaxialMaterial('LimitState', 42012, 17.43001679, 8.138e-05, 52.29005037, 0.00024413, 174.3001679, 0.00081375, -17.43001679, -8.138e-05, -52.29005037, -0.00024413, -174.3001679, -0.00081375, 0.4, 0.3, 0.003, 0.0, 0.0, 22012, 2)
    ops.limitCurve('ThreePoint', 12012, 2012, 0.0, 69.72006716, 0.01684965, 69.72006716, 0.05054895, 48.80404701, -788.11859984, 0.05, 2, 0, 72012, 23012, 1, 3)
    ops.uniaxialMaterial('LimitState', 32012, 17.43001679, 8.138e-05, 52.29005037, 0.00024413, 174.3001679, 0.00081375, -17.43001679, -8.138e-05, -52.29005037, -0.00024413, -174.3001679, -0.00081375, 0.4, 0.3, 0.003, 0.0, 0.0, 12012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2012, 99999, 'P', 42012, 'Vy', 32012, 'Vz', 22012, 'My', 12012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172012, 72012, 172012, 2012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123012, 123012, 23012, 2012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172013, 0.0, 9.7, 7.05)
    ops.node(123013, 0.0, 9.7, 9.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2013, 172013, 123013, 0.0625, 29135056.63365114, 12139606.93068798, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22013, 22.33092995, 0.00079835, 27.12583939, 0.02938642, 2.71258394, 0.0994888, -22.33092995, -0.00079835, -27.12583939, -0.02938642, -2.71258394, -0.0994888, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12013, 24.38279074, 0.00079835, 29.61827685, 0.02938642, 2.96182768, 0.0994888, -24.38279074, -0.00079835, -29.61827685, -0.02938642, -2.96182768, -0.0994888, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22013, 2013, 0.0, 70.05645811, 0.01596692, 70.05645811, 0.04790076, 49.03952068, -1249.48107407, 0.05, 2, 0, 72013, 23013, 2, 3)
    ops.uniaxialMaterial('LimitState', 42013, 17.51411453, 8.587e-05, 52.54234358, 0.00025761, 175.14114528, 0.00085871, -17.51411453, -8.587e-05, -52.54234358, -0.00025761, -175.14114528, -0.00085871, 0.4, 0.3, 0.003, 0.0, 0.0, 22013, 2)
    ops.limitCurve('ThreePoint', 12013, 2013, 0.0, 70.05645811, 0.01596692, 70.05645811, 0.04790076, 49.03952068, -1249.48107407, 0.05, 2, 0, 72013, 23013, 1, 3)
    ops.uniaxialMaterial('LimitState', 32013, 17.51411453, 8.587e-05, 52.54234358, 0.00025761, 175.14114528, 0.00085871, -17.51411453, -8.587e-05, -52.54234358, -0.00025761, -175.14114528, -0.00085871, 0.4, 0.3, 0.003, 0.0, 0.0, 12013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2013, 99999, 'P', 42013, 'Vy', 32013, 'Vz', 22013, 'My', 12013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172013, 72013, 172013, 2013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123013, 123013, 23013, 2013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172014, 4.15, 9.7, 6.975)
    ops.node(123014, 4.15, 9.7, 9.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2014, 172014, 123014, 0.0625, 29643926.87312956, 12351636.19713732, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22014, 31.71757278, 0.00086726, 38.36724899, 0.03086787, 3.8367249, 0.09544999, -31.71757278, -0.00086726, -38.36724899, -0.03086787, -3.8367249, -0.09544999, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12014, 31.71757278, 0.00086726, 38.36724899, 0.03086787, 3.8367249, 0.09544999, -31.71757278, -0.00086726, -38.36724899, -0.03086787, -3.8367249, -0.09544999, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22014, 2014, 0.0, 72.84945307, 0.01734525, 72.84945307, 0.05203576, 50.99461715, -974.44015375, 0.05, 2, 0, 72014, 23014, 2, 3)
    ops.uniaxialMaterial('LimitState', 42014, 18.21236327, 8.776e-05, 54.63708981, 0.00026328, 182.12363269, 0.00087762, -18.21236327, -8.776e-05, -54.63708981, -0.00026328, -182.12363269, -0.00087762, 0.4, 0.3, 0.003, 0.0, 0.0, 22014, 2)
    ops.limitCurve('ThreePoint', 12014, 2014, 0.0, 72.84945307, 0.01734525, 72.84945307, 0.05203576, 50.99461715, -974.44015375, 0.05, 2, 0, 72014, 23014, 1, 3)
    ops.uniaxialMaterial('LimitState', 32014, 18.21236327, 8.776e-05, 54.63708981, 0.00026328, 182.12363269, 0.00087762, -18.21236327, -8.776e-05, -54.63708981, -0.00026328, -182.12363269, -0.00087762, 0.4, 0.3, 0.003, 0.0, 0.0, 12014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2014, 99999, 'P', 42014, 'Vy', 32014, 'Vz', 22014, 'My', 12014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172014, 72014, 172014, 2014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123014, 123014, 23014, 2014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172015, 8.3, 9.7, 6.975)
    ops.node(123015, 8.3, 9.7, 9.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2015, 172015, 123015, 0.0625, 29332768.68434987, 12221986.95181245, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22015, 29.71073782, 0.00086676, 36.00076212, 0.03147841, 3.60007621, 0.0976536, -29.71073782, -0.00086676, -36.00076212, -0.03147841, -3.60007621, -0.0976536, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12015, 29.71073782, 0.00086676, 36.00076212, 0.03147841, 3.60007621, 0.0976536, -29.71073782, -0.00086676, -36.00076212, -0.03147841, -3.60007621, -0.0976536, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22015, 2015, 0.0, 71.97166471, 0.01733527, 71.97166471, 0.0520058, 50.3801653, -1048.67236715, 0.05, 2, 0, 72015, 23015, 2, 3)
    ops.uniaxialMaterial('LimitState', 42015, 17.99291618, 8.762e-05, 53.97874853, 0.00026287, 179.92916177, 0.00087624, -17.99291618, -8.762e-05, -53.97874853, -0.00026287, -179.92916177, -0.00087624, 0.4, 0.3, 0.003, 0.0, 0.0, 22015, 2)
    ops.limitCurve('ThreePoint', 12015, 2015, 0.0, 71.97166471, 0.01733527, 71.97166471, 0.0520058, 50.3801653, -1048.67236715, 0.05, 2, 0, 72015, 23015, 1, 3)
    ops.uniaxialMaterial('LimitState', 32015, 17.99291618, 8.762e-05, 53.97874853, 0.00026287, 179.92916177, 0.00087624, -17.99291618, -8.762e-05, -53.97874853, -0.00026287, -179.92916177, -0.00087624, 0.4, 0.3, 0.003, 0.0, 0.0, 12015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2015, 99999, 'P', 42015, 'Vy', 32015, 'Vz', 22015, 'My', 12015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172015, 72015, 172015, 2015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123015, 123015, 23015, 2015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172016, 11.25, 9.7, 6.975)
    ops.node(123016, 11.25, 9.7, 9.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2016, 172016, 123016, 0.0625, 29353371.1610828, 12230571.31711783, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22016, 30.48687696, 0.00082697, 36.93964919, 0.03169119, 3.69396492, 0.0978964, -30.48687696, -0.00082697, -36.93964919, -0.03169119, -3.69396492, -0.0978964, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12016, 30.48687696, 0.00082697, 36.93964919, 0.03169119, 3.69396492, 0.0978964, -30.48687696, -0.00082697, -36.93964919, -0.03169119, -3.69396492, -0.0978964, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22016, 2016, 0.0, 71.9723584, 0.01653938, 71.9723584, 0.04961814, 50.38065088, -1047.08019632, 0.05, 2, 0, 72016, 23016, 2, 3)
    ops.uniaxialMaterial('LimitState', 42016, 17.9930896, 8.756e-05, 53.9792688, 0.00026269, 179.930896, 0.00087563, -17.9930896, -8.756e-05, -53.9792688, -0.00026269, -179.930896, -0.00087563, 0.4, 0.3, 0.003, 0.0, 0.0, 22016, 2)
    ops.limitCurve('ThreePoint', 12016, 2016, 0.0, 71.9723584, 0.01653938, 71.9723584, 0.04961814, 50.38065088, -1047.08019632, 0.05, 2, 0, 72016, 23016, 1, 3)
    ops.uniaxialMaterial('LimitState', 32016, 17.9930896, 8.756e-05, 53.9792688, 0.00026269, 179.930896, 0.00087563, -17.9930896, -8.756e-05, -53.9792688, -0.00026269, -179.930896, -0.00087563, 0.4, 0.3, 0.003, 0.0, 0.0, 12016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2016, 99999, 'P', 42016, 'Vy', 32016, 'Vz', 22016, 'My', 12016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172016, 72016, 172016, 2016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123016, 123016, 23016, 2016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172017, 15.4, 9.7, 6.975)
    ops.node(123017, 15.4, 9.7, 9.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2017, 172017, 123017, 0.0625, 30174667.91990622, 12572778.29996092, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22017, 32.0899156, 0.00084376, 38.77373278, 0.03120023, 3.87737328, 0.09659751, -32.0899156, -0.00084376, -38.77373278, -0.03120023, -3.87737328, -0.09659751, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12017, 32.0899156, 0.00084376, 38.77373278, 0.03120023, 3.87737328, 0.09659751, -32.0899156, -0.00084376, -38.77373278, -0.03120023, -3.87737328, -0.09659751, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22017, 2017, 0.0, 75.47778058, 0.01687522, 75.47778058, 0.05062567, 52.83444641, -1036.71112929, 0.05, 2, 0, 72017, 23017, 2, 3)
    ops.uniaxialMaterial('LimitState', 42017, 18.86944515, 8.933e-05, 56.60833544, 0.00026799, 188.69445146, 0.00089329, -18.86944515, -8.933e-05, -56.60833544, -0.00026799, -188.69445146, -0.00089329, 0.4, 0.3, 0.003, 0.0, 0.0, 22017, 2)
    ops.limitCurve('ThreePoint', 12017, 2017, 0.0, 75.47778058, 0.01687522, 75.47778058, 0.05062567, 52.83444641, -1036.71112929, 0.05, 2, 0, 72017, 23017, 1, 3)
    ops.uniaxialMaterial('LimitState', 32017, 18.86944515, 8.933e-05, 56.60833544, 0.00026799, 188.69445146, 0.00089329, -18.86944515, -8.933e-05, -56.60833544, -0.00026799, -188.69445146, -0.00089329, 0.4, 0.3, 0.003, 0.0, 0.0, 12017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2017, 99999, 'P', 42017, 'Vy', 32017, 'Vz', 22017, 'My', 12017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172017, 72017, 172017, 2017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123017, 123017, 23017, 2017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172018, 19.55, 9.7, 7.05)
    ops.node(123018, 19.55, 9.7, 9.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2018, 172018, 123018, 0.0625, 29573095.02816795, 12322122.92840331, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22018, 22.38997269, 0.00079214, 27.17024438, 0.02920466, 2.71702444, 0.09977246, -22.38997269, -0.00079214, -27.17024438, -0.02920466, -2.71702444, -0.09977246, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12018, 24.46409435, 0.00079214, 29.68719218, 0.02920466, 2.96871922, 0.09977246, -24.46409435, -0.00079214, -29.68719218, -0.02920466, -2.96871922, -0.09977246, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22018, 2018, 0.0, 70.16047055, 0.01584274, 70.16047055, 0.04752823, 49.11232939, -1210.68369203, 0.05, 2, 0, 72018, 23018, 2, 3)
    ops.uniaxialMaterial('LimitState', 42018, 17.54011764, 8.472e-05, 52.62035291, 0.00025417, 175.40117638, 0.00084725, -17.54011764, -8.472e-05, -52.62035291, -0.00025417, -175.40117638, -0.00084725, 0.4, 0.3, 0.003, 0.0, 0.0, 22018, 2)
    ops.limitCurve('ThreePoint', 12018, 2018, 0.0, 70.16047055, 0.01584274, 70.16047055, 0.04752823, 49.11232939, -1210.68369203, 0.05, 2, 0, 72018, 23018, 1, 3)
    ops.uniaxialMaterial('LimitState', 32018, 17.54011764, 8.472e-05, 52.62035291, 0.00025417, 175.40117638, 0.00084725, -17.54011764, -8.472e-05, -52.62035291, -0.00025417, -175.40117638, -0.00084725, 0.4, 0.3, 0.003, 0.0, 0.0, 12018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2018, 99999, 'P', 42018, 'Vy', 32018, 'Vz', 22018, 'My', 12018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172018, 72018, 172018, 2018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123018, 123018, 23018, 2018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173001, 0.0, 0.0, 10.15)
    ops.node(124001, 0.0, 0.0, 12.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3001, 173001, 124001, 0.0625, 31020624.39152125, 12925260.16313385, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23001, 14.27004241, 0.00071743, 17.29998643, 0.02272101, 1.72999864, 0.08779076, -14.27004241, -0.00071743, -17.29998643, -0.02272101, -1.72999864, -0.08779076, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13001, 14.27004241, 0.00071743, 17.29998643, 0.02272101, 1.72999864, 0.08779076, -14.27004241, -0.00071743, -17.29998643, -0.02272101, -1.72999864, -0.08779076, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23001, 3001, 0.0, 61.88801529, 0.01434868, 61.88801529, 0.04304603, 43.32161071, -1948.92964024, 0.05, 2, 0, 73001, 24001, 2, 3)
    ops.uniaxialMaterial('LimitState', 43001, 15.47200382, 7.125e-05, 46.41601147, 0.00021374, 154.72003824, 0.00071248, -15.47200382, -7.125e-05, -46.41601147, -0.00021374, -154.72003824, -0.00071248, 0.4, 0.3, 0.003, 0.0, 0.0, 23001, 2)
    ops.limitCurve('ThreePoint', 13001, 3001, 0.0, 61.88801529, 0.01434868, 61.88801529, 0.04304603, 43.32161071, -1948.92964024, 0.05, 2, 0, 73001, 24001, 1, 3)
    ops.uniaxialMaterial('LimitState', 33001, 15.47200382, 7.125e-05, 46.41601147, 0.00021374, 154.72003824, 0.00071248, -15.47200382, -7.125e-05, -46.41601147, -0.00021374, -154.72003824, -0.00071248, 0.4, 0.3, 0.003, 0.0, 0.0, 13001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3001, 99999, 'P', 43001, 'Vy', 33001, 'Vz', 23001, 'My', 13001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173001, 73001, 173001, 3001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124001, 124001, 24001, 3001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173002, 4.15, 0.0, 10.1)
    ops.node(124002, 4.15, 0.0, 12.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3002, 173002, 124002, 0.0625, 29592332.04092986, 12330138.35038744, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23002, 23.84517872, 0.00084638, 28.99805217, 0.04130023, 2.89980522, 0.1376629, -23.84517872, -0.00084638, -28.99805217, -0.04130023, -2.89980522, -0.1376629, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13002, 23.84517872, 0.00084638, 28.99805217, 0.04130023, 2.89980522, 0.1376629, -23.84517872, -0.00084638, -28.99805217, -0.04130023, -2.89980522, -0.1376629, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23002, 3002, 0.0, 77.09896438, 0.0169277, 77.09896438, 0.05078309, 53.96927506, -2846.8501352, 0.05, 2, 0, 73002, 24002, 2, 3)
    ops.uniaxialMaterial('LimitState', 43002, 19.27474109, 9.304e-05, 57.82422328, 0.00027913, 192.74741094, 0.00093043, -19.27474109, -9.304e-05, -57.82422328, -0.00027913, -192.74741094, -0.00093043, 0.4, 0.3, 0.003, 0.0, 0.0, 23002, 2)
    ops.limitCurve('ThreePoint', 13002, 3002, 0.0, 77.09896438, 0.0169277, 77.09896438, 0.05078309, 53.96927506, -2846.8501352, 0.05, 2, 0, 73002, 24002, 1, 3)
    ops.uniaxialMaterial('LimitState', 33002, 19.27474109, 9.304e-05, 57.82422328, 0.00027913, 192.74741094, 0.00093043, -19.27474109, -9.304e-05, -57.82422328, -0.00027913, -192.74741094, -0.00093043, 0.4, 0.3, 0.003, 0.0, 0.0, 13002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3002, 99999, 'P', 43002, 'Vy', 33002, 'Vz', 23002, 'My', 13002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173002, 73002, 173002, 3002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124002, 124002, 24002, 3002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173005, 15.4, 0.0, 10.1)
    ops.node(124005, 15.4, 0.0, 12.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3005, 173005, 124005, 0.0625, 28288363.00231304, 11786817.91763043, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23005, 24.6704518, 0.0008047, 30.09733438, 0.04237417, 3.00973344, 0.13773626, -24.6704518, -0.0008047, -30.09733438, -0.04237417, -3.00973344, -0.13773626, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13005, 24.6704518, 0.0008047, 30.09733438, 0.04237417, 3.00973344, 0.13773626, -24.6704518, -0.0008047, -30.09733438, -0.04237417, -3.00973344, -0.13773626, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23005, 3005, 0.0, 75.64478368, 0.016094, 75.64478368, 0.048282, 52.95134858, -2955.13184642, 0.05, 2, 0, 73005, 24005, 2, 3)
    ops.uniaxialMaterial('LimitState', 43005, 18.91119592, 9.55e-05, 56.73358776, 0.00028649, 189.1119592, 0.00095496, -18.91119592, -9.55e-05, -56.73358776, -0.00028649, -189.1119592, -0.00095496, 0.4, 0.3, 0.003, 0.0, 0.0, 23005, 2)
    ops.limitCurve('ThreePoint', 13005, 3005, 0.0, 75.64478368, 0.016094, 75.64478368, 0.048282, 52.95134858, -2955.13184642, 0.05, 2, 0, 73005, 24005, 1, 3)
    ops.uniaxialMaterial('LimitState', 33005, 18.91119592, 9.55e-05, 56.73358776, 0.00028649, 189.1119592, 0.00095496, -18.91119592, -9.55e-05, -56.73358776, -0.00028649, -189.1119592, -0.00095496, 0.4, 0.3, 0.003, 0.0, 0.0, 13005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3005, 99999, 'P', 43005, 'Vy', 33005, 'Vz', 23005, 'My', 13005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173005, 73005, 173005, 3005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124005, 124005, 24005, 3005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173006, 19.55, 0.0, 10.15)
    ops.node(124006, 19.55, 0.0, 12.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3006, 173006, 124006, 0.0625, 29193245.06808516, 12163852.11170215, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23006, 14.03417718, 0.00074008, 17.10305511, 0.02411555, 1.71030551, 0.08877205, -14.03417718, -0.00074008, -17.10305511, -0.02411555, -1.71030551, -0.08877205, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13006, 14.03417718, 0.00074008, 17.10305511, 0.02411555, 1.71030551, 0.08877205, -14.03417718, -0.00074008, -17.10305511, -0.02411555, -1.71030551, -0.08877205, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23006, 3006, 0.0, 59.57341384, 0.01480165, 59.57341384, 0.04440495, 41.70138968, -2097.44830271, 0.05, 2, 0, 73006, 24006, 2, 3)
    ops.uniaxialMaterial('LimitState', 43006, 14.89335346, 7.288e-05, 44.68006038, 0.00021863, 148.93353459, 0.00072876, -14.89335346, -7.288e-05, -44.68006038, -0.00021863, -148.93353459, -0.00072876, 0.4, 0.3, 0.003, 0.0, 0.0, 23006, 2)
    ops.limitCurve('ThreePoint', 13006, 3006, 0.0, 59.57341384, 0.01480165, 59.57341384, 0.04440495, 41.70138968, -2097.44830271, 0.05, 2, 0, 73006, 24006, 1, 3)
    ops.uniaxialMaterial('LimitState', 33006, 14.89335346, 7.288e-05, 44.68006038, 0.00021863, 148.93353459, 0.00072876, -14.89335346, -7.288e-05, -44.68006038, -0.00021863, -148.93353459, -0.00072876, 0.4, 0.3, 0.003, 0.0, 0.0, 13006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3006, 99999, 'P', 43006, 'Vy', 33006, 'Vz', 23006, 'My', 13006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173006, 73006, 173006, 3006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124006, 124006, 24006, 3006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173007, 0.0, 4.85, 10.15)
    ops.node(124007, 0.0, 4.85, 12.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3007, 173007, 124007, 0.0625, 30428713.35648407, 12678630.5652017, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23007, 24.59924805, 0.00080287, 29.8484691, 0.02336093, 2.98484691, 0.07816807, -24.59924805, -0.00080287, -29.8484691, -0.02336093, -2.98484691, -0.07816807, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13007, 24.59924805, 0.00080287, 29.8484691, 0.02336093, 2.98484691, 0.07816807, -24.59924805, -0.00080287, -29.8484691, -0.02336093, -2.98484691, -0.07816807, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23007, 3007, 0.0, 56.70852331, 0.01605735, 56.70852331, 0.04817204, 39.69596631, -942.5655504, 0.05, 2, 0, 73007, 24007, 2, 3)
    ops.uniaxialMaterial('LimitState', 43007, 14.17713083, 6.655e-05, 42.53139248, 0.00019966, 141.77130827, 0.00066555, -14.17713083, -6.655e-05, -42.53139248, -0.00019966, -141.77130827, -0.00066555, 0.4, 0.3, 0.003, 0.0, 0.0, 23007, 2)
    ops.limitCurve('ThreePoint', 13007, 3007, 0.0, 56.70852331, 0.01605735, 56.70852331, 0.04817204, 39.69596631, -942.5655504, 0.05, 2, 0, 73007, 24007, 1, 3)
    ops.uniaxialMaterial('LimitState', 33007, 14.17713083, 6.655e-05, 42.53139248, 0.00019966, 141.77130827, 0.00066555, -14.17713083, -6.655e-05, -42.53139248, -0.00019966, -141.77130827, -0.00066555, 0.4, 0.3, 0.003, 0.0, 0.0, 13007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3007, 99999, 'P', 43007, 'Vy', 33007, 'Vz', 23007, 'My', 13007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173007, 73007, 173007, 3007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124007, 124007, 24007, 3007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173008, 4.15, 4.85, 10.1)
    ops.node(124008, 4.15, 4.85, 12.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3008, 173008, 124008, 0.0625, 29284838.15243782, 12202015.89684909, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23008, 26.62291257, 0.00084838, 32.35227456, 0.02418736, 3.23522746, 0.0760705, -26.62291257, -0.00084838, -32.35227456, -0.02418736, -3.23522746, -0.0760705, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13008, 26.62291257, 0.00084838, 32.35227456, 0.02418736, 3.23522746, 0.0760705, -26.62291257, -0.00084838, -32.35227456, -0.02418736, -3.23522746, -0.0760705, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23008, 3008, 0.0, 56.58651379, 0.01696765, 56.58651379, 0.05090295, 39.61055965, -731.57636138, 0.05, 2, 0, 73008, 24008, 2, 3)
    ops.uniaxialMaterial('LimitState', 43008, 14.14662845, 6.901e-05, 42.43988534, 0.00020702, 141.46628446, 0.00069006, -14.14662845, -6.901e-05, -42.43988534, -0.00020702, -141.46628446, -0.00069006, 0.4, 0.3, 0.003, 0.0, 0.0, 23008, 2)
    ops.limitCurve('ThreePoint', 13008, 3008, 0.0, 56.58651379, 0.01696765, 56.58651379, 0.05090295, 39.61055965, -731.57636138, 0.05, 2, 0, 73008, 24008, 1, 3)
    ops.uniaxialMaterial('LimitState', 33008, 14.14662845, 6.901e-05, 42.43988534, 0.00020702, 141.46628446, 0.00069006, -14.14662845, -6.901e-05, -42.43988534, -0.00020702, -141.46628446, -0.00069006, 0.4, 0.3, 0.003, 0.0, 0.0, 13008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3008, 99999, 'P', 43008, 'Vy', 33008, 'Vz', 23008, 'My', 13008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173008, 73008, 173008, 3008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124008, 124008, 24008, 3008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173009, 8.3, 4.85, 10.1)
    ops.node(124009, 8.3, 4.85, 12.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3009, 173009, 124009, 0.0625, 27840061.29149565, 11600025.53812319, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23009, 27.47693189, 0.00081538, 33.47135148, 0.02477579, 3.34713515, 0.07458793, -27.47693189, -0.00081538, -33.47135148, -0.02477579, -3.34713515, -0.07458793, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13009, 27.47693189, 0.00081538, 33.47135148, 0.02477579, 3.34713515, 0.07458793, -27.47693189, -0.00081538, -33.47135148, -0.02477579, -3.34713515, -0.07458793, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23009, 3009, 0.0, 56.03697315, 0.0163076, 56.03697315, 0.0489228, 39.22588121, -701.28392029, 0.05, 2, 0, 73009, 24009, 2, 3)
    ops.uniaxialMaterial('LimitState', 43009, 14.00924329, 7.188e-05, 42.02772986, 0.00021565, 140.09243288, 0.00071882, -14.00924329, -7.188e-05, -42.02772986, -0.00021565, -140.09243288, -0.00071882, 0.4, 0.3, 0.003, 0.0, 0.0, 23009, 2)
    ops.limitCurve('ThreePoint', 13009, 3009, 0.0, 56.03697315, 0.0163076, 56.03697315, 0.0489228, 39.22588121, -701.28392029, 0.05, 2, 0, 73009, 24009, 1, 3)
    ops.uniaxialMaterial('LimitState', 33009, 14.00924329, 7.188e-05, 42.02772986, 0.00021565, 140.09243288, 0.00071882, -14.00924329, -7.188e-05, -42.02772986, -0.00021565, -140.09243288, -0.00071882, 0.4, 0.3, 0.003, 0.0, 0.0, 13009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3009, 99999, 'P', 43009, 'Vy', 33009, 'Vz', 23009, 'My', 13009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173009, 73009, 173009, 3009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124009, 124009, 24009, 3009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173010, 11.25, 4.85, 10.1)
    ops.node(124010, 11.25, 4.85, 12.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3010, 173010, 124010, 0.0625, 28895389.69429726, 12039745.70595719, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23010, 27.48934652, 0.00083117, 33.41517852, 0.02393086, 3.34151785, 0.07463914, -27.48934652, -0.00083117, -33.41517852, -0.02393086, -3.34151785, -0.07463914, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13010, 27.48934652, 0.00083117, 33.41517852, 0.02393086, 3.34151785, 0.07463914, -27.48934652, -0.00083117, -33.41517852, -0.02393086, -3.34151785, -0.07463914, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23010, 3010, 0.0, 55.39194236, 0.01662343, 55.39194236, 0.0498703, 38.77435965, -686.78483799, 0.05, 2, 0, 73010, 24010, 2, 3)
    ops.uniaxialMaterial('LimitState', 43010, 13.84798559, 6.846e-05, 41.54395677, 0.00020538, 138.47985591, 0.00068459, -13.84798559, -6.846e-05, -41.54395677, -0.00020538, -138.47985591, -0.00068459, 0.4, 0.3, 0.003, 0.0, 0.0, 23010, 2)
    ops.limitCurve('ThreePoint', 13010, 3010, 0.0, 55.39194236, 0.01662343, 55.39194236, 0.0498703, 38.77435965, -686.78483799, 0.05, 2, 0, 73010, 24010, 1, 3)
    ops.uniaxialMaterial('LimitState', 33010, 13.84798559, 6.846e-05, 41.54395677, 0.00020538, 138.47985591, 0.00068459, -13.84798559, -6.846e-05, -41.54395677, -0.00020538, -138.47985591, -0.00068459, 0.4, 0.3, 0.003, 0.0, 0.0, 13010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3010, 99999, 'P', 43010, 'Vy', 33010, 'Vz', 23010, 'My', 13010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173010, 73010, 173010, 3010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124010, 124010, 24010, 3010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173011, 15.4, 4.85, 10.1)
    ops.node(124011, 15.4, 4.85, 12.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3011, 173011, 124011, 0.0625, 28198308.26073333, 11749295.10863889, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23011, 26.56463938, 0.00083503, 32.35877568, 0.02436495, 3.23587757, 0.07547253, -26.56463938, -0.00083503, -32.35877568, -0.02436495, -3.23587757, -0.07547253, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13011, 26.56463938, 0.00083503, 32.35877568, 0.02436495, 3.23587757, 0.07547253, -26.56463938, -0.00083503, -32.35877568, -0.02436495, -3.23587757, -0.07547253, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23011, 3011, 0.0, 53.80912268, 0.0167006, 53.80912268, 0.05010179, 37.66638588, -726.51641387, 0.05, 2, 0, 73011, 24011, 2, 3)
    ops.uniaxialMaterial('LimitState', 43011, 13.45228067, 6.815e-05, 40.35684201, 0.00020444, 134.52280671, 0.00068147, -13.45228067, -6.815e-05, -40.35684201, -0.00020444, -134.52280671, -0.00068147, 0.4, 0.3, 0.003, 0.0, 0.0, 23011, 2)
    ops.limitCurve('ThreePoint', 13011, 3011, 0.0, 53.80912268, 0.0167006, 53.80912268, 0.05010179, 37.66638588, -726.51641387, 0.05, 2, 0, 73011, 24011, 1, 3)
    ops.uniaxialMaterial('LimitState', 33011, 13.45228067, 6.815e-05, 40.35684201, 0.00020444, 134.52280671, 0.00068147, -13.45228067, -6.815e-05, -40.35684201, -0.00020444, -134.52280671, -0.00068147, 0.4, 0.3, 0.003, 0.0, 0.0, 13011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3011, 99999, 'P', 43011, 'Vy', 33011, 'Vz', 23011, 'My', 13011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173011, 73011, 173011, 3011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124011, 124011, 24011, 3011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173012, 19.55, 4.85, 10.15)
    ops.node(124012, 19.55, 4.85, 12.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3012, 173012, 124012, 0.0625, 31794396.62053964, 13247665.25855818, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23012, 24.62736655, 0.00077267, 29.75972659, 0.02280555, 2.97597266, 0.07804197, -24.62736655, -0.00077267, -29.75972659, -0.02280555, -2.97597266, -0.07804197, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13012, 24.62736655, 0.00077267, 29.75972659, 0.02280555, 2.97597266, 0.07804197, -24.62736655, -0.00077267, -29.75972659, -0.02280555, -2.97597266, -0.07804197, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23012, 3012, 0.0, 58.60920234, 0.01545338, 58.60920234, 0.04636014, 41.02644164, -925.35983678, 0.05, 2, 0, 73012, 24012, 2, 3)
    ops.uniaxialMaterial('LimitState', 43012, 14.65230058, 6.583e-05, 43.95690175, 0.00019749, 146.52300584, 0.00065831, -14.65230058, -6.583e-05, -43.95690175, -0.00019749, -146.52300584, -0.00065831, 0.4, 0.3, 0.003, 0.0, 0.0, 23012, 2)
    ops.limitCurve('ThreePoint', 13012, 3012, 0.0, 58.60920234, 0.01545338, 58.60920234, 0.04636014, 41.02644164, -925.35983678, 0.05, 2, 0, 73012, 24012, 1, 3)
    ops.uniaxialMaterial('LimitState', 33012, 14.65230058, 6.583e-05, 43.95690175, 0.00019749, 146.52300584, 0.00065831, -14.65230058, -6.583e-05, -43.95690175, -0.00019749, -146.52300584, -0.00065831, 0.4, 0.3, 0.003, 0.0, 0.0, 13012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3012, 99999, 'P', 43012, 'Vy', 33012, 'Vz', 23012, 'My', 13012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173012, 73012, 173012, 3012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124012, 124012, 24012, 3012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173013, 0.0, 9.7, 10.15)
    ops.node(124013, 0.0, 9.7, 12.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3013, 173013, 124013, 0.0625, 31213971.14753272, 13005821.31147197, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23013, 14.27706579, 0.00074177, 17.29810318, 0.02261353, 1.72981032, 0.08772117, -14.27706579, -0.00074177, -17.29810318, -0.02261353, -1.72981032, -0.08772117, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13013, 14.27706579, 0.00074177, 17.29810318, 0.02261353, 1.72981032, 0.08772117, -14.27706579, -0.00074177, -17.29810318, -0.02261353, -1.72981032, -0.08772117, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23013, 3013, 0.0, 62.14265859, 0.01483537, 62.14265859, 0.04450612, 43.49986101, -1933.78422713, 0.05, 2, 0, 73013, 24013, 2, 3)
    ops.uniaxialMaterial('LimitState', 43013, 15.53566465, 7.11e-05, 46.60699394, 0.00021329, 155.35664646, 0.00071098, -15.53566465, -7.11e-05, -46.60699394, -0.00021329, -155.35664646, -0.00071098, 0.4, 0.3, 0.003, 0.0, 0.0, 23013, 2)
    ops.limitCurve('ThreePoint', 13013, 3013, 0.0, 62.14265859, 0.01483537, 62.14265859, 0.04450612, 43.49986101, -1933.78422713, 0.05, 2, 0, 73013, 24013, 1, 3)
    ops.uniaxialMaterial('LimitState', 33013, 15.53566465, 7.11e-05, 46.60699394, 0.00021329, 155.35664646, 0.00071098, -15.53566465, -7.11e-05, -46.60699394, -0.00021329, -155.35664646, -0.00071098, 0.4, 0.3, 0.003, 0.0, 0.0, 13013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3013, 99999, 'P', 43013, 'Vy', 33013, 'Vz', 23013, 'My', 13013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173013, 73013, 173013, 3013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124013, 124013, 24013, 3013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173014, 4.15, 9.7, 10.1)
    ops.node(124014, 4.15, 9.7, 12.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3014, 173014, 124014, 0.0625, 30248916.66944319, 12603715.27893466, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23014, 24.4558275, 0.00080331, 29.68805196, 0.03307678, 2.9688052, 0.10875314, -24.4558275, -0.00080331, -29.68805196, -0.03307678, -2.9688052, -0.10875314, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13014, 24.4558275, 0.00080331, 29.68805196, 0.03307678, 2.9688052, 0.10875314, -24.4558275, -0.00080331, -29.68805196, -0.03307678, -2.9688052, -0.10875314, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23014, 3014, 0.0, 67.92042491, 0.01606615, 67.92042491, 0.04819846, 47.54429744, -1742.61114397, 0.05, 2, 0, 73014, 24014, 2, 3)
    ops.uniaxialMaterial('LimitState', 43014, 16.98010623, 8.019e-05, 50.94031869, 0.00024056, 169.80106229, 0.00080187, -16.98010623, -8.019e-05, -50.94031869, -0.00024056, -169.80106229, -0.00080187, 0.4, 0.3, 0.003, 0.0, 0.0, 23014, 2)
    ops.limitCurve('ThreePoint', 13014, 3014, 0.0, 67.92042491, 0.01606615, 67.92042491, 0.04819846, 47.54429744, -1742.61114397, 0.05, 2, 0, 73014, 24014, 1, 3)
    ops.uniaxialMaterial('LimitState', 33014, 16.98010623, 8.019e-05, 50.94031869, 0.00024056, 169.80106229, 0.00080187, -16.98010623, -8.019e-05, -50.94031869, -0.00024056, -169.80106229, -0.00080187, 0.4, 0.3, 0.003, 0.0, 0.0, 13014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3014, 99999, 'P', 43014, 'Vy', 33014, 'Vz', 23014, 'My', 13014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173014, 73014, 173014, 3014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124014, 124014, 24014, 3014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173015, 8.3, 9.7, 10.1)
    ops.node(124015, 8.3, 9.7, 12.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3015, 173015, 124015, 0.0625, 29723133.21736702, 12384638.84056959, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23015, 23.50397193, 0.00080785, 28.5819396, 0.03401985, 2.85819396, 0.11010753, -23.50397193, -0.00080785, -28.5819396, -0.03401985, -2.85819396, -0.11010753, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13015, 23.50397193, 0.00080785, 28.5819396, 0.03401985, 2.85819396, 0.11010753, -23.50397193, -0.00080785, -28.5819396, -0.03401985, -2.85819396, -0.11010753, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23015, 3015, 0.0, 67.16850367, 0.01615693, 67.16850367, 0.04847078, 47.01795257, -2006.7680987, 0.05, 2, 0, 73015, 24015, 2, 3)
    ops.uniaxialMaterial('LimitState', 43015, 16.79212592, 8.07e-05, 50.37637775, 0.00024211, 167.92125918, 0.00080702, -16.79212592, -8.07e-05, -50.37637775, -0.00024211, -167.92125918, -0.00080702, 0.4, 0.3, 0.003, 0.0, 0.0, 23015, 2)
    ops.limitCurve('ThreePoint', 13015, 3015, 0.0, 67.16850367, 0.01615693, 67.16850367, 0.04847078, 47.01795257, -2006.7680987, 0.05, 2, 0, 73015, 24015, 1, 3)
    ops.uniaxialMaterial('LimitState', 33015, 16.79212592, 8.07e-05, 50.37637775, 0.00024211, 167.92125918, 0.00080702, -16.79212592, -8.07e-05, -50.37637775, -0.00024211, -167.92125918, -0.00080702, 0.4, 0.3, 0.003, 0.0, 0.0, 13015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3015, 99999, 'P', 43015, 'Vy', 33015, 'Vz', 23015, 'My', 13015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173015, 73015, 173015, 3015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124015, 124015, 24015, 3015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173016, 11.25, 9.7, 10.1)
    ops.node(124016, 11.25, 9.7, 12.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3016, 173016, 124016, 0.0625, 30140039.15801616, 12558349.6491734, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23016, 24.14793862, 0.00079927, 29.33160304, 0.03380407, 2.9331603, 0.11007989, -24.14793862, -0.00079927, -29.33160304, -0.03380407, -2.9331603, -0.11007989, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13016, 24.14793862, 0.00079927, 29.33160304, 0.03380407, 2.9331603, 0.11007989, -24.14793862, -0.00079927, -29.33160304, -0.03380407, -2.9331603, -0.11007989, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23016, 3016, 0.0, 68.46743866, 0.01598539, 68.46743866, 0.04795616, 47.92720706, -2064.51088313, 0.05, 2, 0, 73016, 24016, 2, 3)
    ops.uniaxialMaterial('LimitState', 43016, 17.11685967, 8.112e-05, 51.350579, 0.00024337, 171.16859666, 0.00081125, -17.11685967, -8.112e-05, -51.350579, -0.00024337, -171.16859666, -0.00081125, 0.4, 0.3, 0.003, 0.0, 0.0, 23016, 2)
    ops.limitCurve('ThreePoint', 13016, 3016, 0.0, 68.46743866, 0.01598539, 68.46743866, 0.04795616, 47.92720706, -2064.51088313, 0.05, 2, 0, 73016, 24016, 1, 3)
    ops.uniaxialMaterial('LimitState', 33016, 17.11685967, 8.112e-05, 51.350579, 0.00024337, 171.16859666, 0.00081125, -17.11685967, -8.112e-05, -51.350579, -0.00024337, -171.16859666, -0.00081125, 0.4, 0.3, 0.003, 0.0, 0.0, 13016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3016, 99999, 'P', 43016, 'Vy', 33016, 'Vz', 23016, 'My', 13016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173016, 73016, 173016, 3016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124016, 124016, 24016, 3016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173017, 15.4, 9.7, 10.1)
    ops.node(124017, 15.4, 9.7, 12.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3017, 173017, 124017, 0.0625, 28658988.31722701, 11941245.13217792, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23017, 24.48911067, 0.00080273, 29.85041376, 0.03419395, 2.98504138, 0.10898239, -24.48911067, -0.00080273, -29.85041376, -0.03419395, -2.98504138, -0.10898239, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13017, 24.48911067, 0.00080273, 29.85041376, 0.03419395, 2.98504138, 0.10898239, -24.48911067, -0.00080273, -29.85041376, -0.03419395, -2.98504138, -0.10898239, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23017, 3017, 0.0, 65.64195971, 0.01605456, 65.64195971, 0.04816367, 45.9493718, -1801.37420961, 0.05, 2, 0, 73017, 24017, 2, 3)
    ops.uniaxialMaterial('LimitState', 43017, 16.41048993, 8.18e-05, 49.23146978, 0.00024539, 164.10489927, 0.00081797, -16.41048993, -8.18e-05, -49.23146978, -0.00024539, -164.10489927, -0.00081797, 0.4, 0.3, 0.003, 0.0, 0.0, 23017, 2)
    ops.limitCurve('ThreePoint', 13017, 3017, 0.0, 65.64195971, 0.01605456, 65.64195971, 0.04816367, 45.9493718, -1801.37420961, 0.05, 2, 0, 73017, 24017, 1, 3)
    ops.uniaxialMaterial('LimitState', 33017, 16.41048993, 8.18e-05, 49.23146978, 0.00024539, 164.10489927, 0.00081797, -16.41048993, -8.18e-05, -49.23146978, -0.00024539, -164.10489927, -0.00081797, 0.4, 0.3, 0.003, 0.0, 0.0, 13017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3017, 99999, 'P', 43017, 'Vy', 33017, 'Vz', 23017, 'My', 13017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173017, 73017, 173017, 3017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124017, 124017, 24017, 3017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173018, 19.55, 9.7, 10.15)
    ops.node(124018, 19.55, 9.7, 12.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3018, 173018, 124018, 0.0625, 29015982.99376784, 12089992.91406994, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23018, 14.12639021, 0.00073118, 17.22340056, 0.0235709, 1.72234006, 0.0881813, -14.12639021, -0.00073118, -17.22340056, -0.0235709, -1.72234006, -0.0881813, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13018, 14.12639021, 0.00073118, 17.22340056, 0.0235709, 1.72234006, 0.0881813, -14.12639021, -0.00073118, -17.22340056, -0.0235709, -1.72234006, -0.0881813, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23018, 3018, 0.0, 57.77084333, 0.01462363, 57.77084333, 0.04387088, 40.43959033, -1891.54819832, 0.05, 2, 0, 73018, 24018, 2, 3)
    ops.uniaxialMaterial('LimitState', 43018, 14.44271083, 7.11e-05, 43.32813249, 0.00021331, 144.42710831, 0.00071103, -14.44271083, -7.11e-05, -43.32813249, -0.00021331, -144.42710831, -0.00071103, 0.4, 0.3, 0.003, 0.0, 0.0, 23018, 2)
    ops.limitCurve('ThreePoint', 13018, 3018, 0.0, 57.77084333, 0.01462363, 57.77084333, 0.04387088, 40.43959033, -1891.54819832, 0.05, 2, 0, 73018, 24018, 1, 3)
    ops.uniaxialMaterial('LimitState', 33018, 14.44271083, 7.11e-05, 43.32813249, 0.00021331, 144.42710831, 0.00071103, -14.44271083, -7.11e-05, -43.32813249, -0.00021331, -144.42710831, -0.00071103, 0.4, 0.3, 0.003, 0.0, 0.0, 13018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3018, 99999, 'P', 43018, 'Vy', 33018, 'Vz', 23018, 'My', 13018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173018, 73018, 173018, 3018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124018, 124018, 24018, 3018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170003, 8.3, 0.0, 0.0)
    ops.node(124019, 8.3, 0.0, 1.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4046, 170003, 124019, 0.1225, 29547375.95342891, 12311406.64726205, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24046, 144.50689141, 0.00056199, 174.45852916, 0.05738508, 17.44585292, 0.15738508, -144.50689141, -0.00056199, -174.45852916, -0.05738508, -17.44585292, -0.15738508, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14046, 130.2950695, 0.00056199, 157.30105298, 0.04924069, 15.7301053, 0.13132491, -130.2950695, -0.00056199, -157.30105298, -0.04924069, -15.7301053, -0.13132491, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24046, 4046, 0.0, 192.45711907, 0.0112398, 192.45711907, 0.03371939, 134.71998335, -4756.21544755, 0.05, 2, 0, 70003, 24019, 2, 3)
    ops.uniaxialMaterial('LimitState', 44046, 48.11427977, 7.082e-05, 144.3428393, 0.00021247, 481.14279768, 0.00070824, -48.11427977, -7.082e-05, -144.3428393, -0.00021247, -481.14279768, -0.00070824, 0.4, 0.3, 0.003, 0.0, 0.0, 24046, 2)
    ops.limitCurve('ThreePoint', 14046, 4046, 0.0, 236.54036344, 0.0112398, 236.54036344, 0.03371939, 165.57825441, -8218.72203021, 0.05, 2, 0, 70003, 24019, 1, 3)
    ops.uniaxialMaterial('LimitState', 34046, 59.13509086, 8.705e-05, 177.40527258, 0.00026114, 591.35090861, 0.00087047, -59.13509086, -8.705e-05, -177.40527258, -0.00026114, -591.35090861, -0.00087047, 0.4, 0.3, 0.003, 0.0, 0.0, 14046, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4046, 99999, 'P', 44046, 'Vy', 34046, 'Vz', 24046, 'My', 14046, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170003, 70003, 170003, 4046, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124019, 124019, 24019, 4046, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174019, 8.3, 0.0, 2.1)
    ops.node(121003, 8.3, 0.0, 3.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4047, 174019, 121003, 0.1225, 29170535.41267037, 12154389.75527932, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24047, 94.09350569, 0.00055315, 113.78455882, 0.05268271, 11.37845588, 0.15268271, -94.09350569, -0.00055315, -113.78455882, -0.05268271, -11.37845588, -0.15268271, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14047, 81.69445534, 0.00055315, 98.79074534, 0.04521104, 9.87907453, 0.12878183, -81.69445534, -0.00055315, -98.79074534, -0.04521104, -9.87907453, -0.12878183, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24047, 4047, 0.0, 188.79620598, 0.01106301, 188.79620598, 0.03318902, 132.15734418, -4940.24130815, 0.05, 2, 0, 74019, 21003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44047, 47.19905149, 7.037e-05, 141.59715448, 0.00021112, 471.99051494, 0.00070375, -47.19905149, -7.037e-05, -141.59715448, -0.00021112, -471.99051494, -0.00070375, 0.4, 0.3, 0.003, 0.0, 0.0, 24047, 2)
    ops.limitCurve('ThreePoint', 14047, 4047, 0.0, 233.13176427, 0.01106301, 233.13176427, 0.03318902, 163.19223499, -8706.79896411, 0.05, 2, 0, 74019, 21003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34047, 58.28294107, 8.69e-05, 174.8488232, 0.0002607, 582.82941066, 0.00086901, -58.28294107, -8.69e-05, -174.8488232, -0.0002607, -582.82941066, -0.00086901, 0.4, 0.3, 0.003, 0.0, 0.0, 14047, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4047, 99999, 'P', 44047, 'Vy', 34047, 'Vz', 24047, 'My', 14047, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174019, 74019, 174019, 4047, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121003, 121003, 21003, 4047, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170004, 11.25, 0.0, 0.0)
    ops.node(124020, 11.25, 0.0, 1.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4048, 170004, 124020, 0.1225, 28037298.35132778, 11682207.64638657, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24048, 143.16825065, 0.00058186, 173.22562, 0.05721821, 17.322562, 0.15721821, -143.16825065, -0.00058186, -173.22562, -0.05721821, -17.322562, -0.15721821, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14048, 129.35000468, 0.00058186, 156.50631098, 0.04910058, 15.6506311, 0.12682779, -129.35000468, -0.00058186, -156.50631098, -0.04910058, -15.6506311, -0.12682779, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24048, 4048, 0.0, 185.23457893, 0.01163728, 185.23457893, 0.03491183, 129.66420525, -4723.95557322, 0.05, 2, 0, 70004, 24020, 2, 3)
    ops.uniaxialMaterial('LimitState', 44048, 46.30864473, 7.184e-05, 138.92593419, 0.00021551, 463.08644731, 0.00071838, -46.30864473, -7.184e-05, -138.92593419, -0.00021551, -463.08644731, -0.00071838, 0.4, 0.3, 0.003, 0.0, 0.0, 24048, 2)
    ops.limitCurve('ThreePoint', 14048, 4048, 0.0, 229.07976285, 0.01163728, 229.07976285, 0.03491183, 160.355834, -8155.12731174, 0.05, 2, 0, 70004, 24020, 1, 3)
    ops.uniaxialMaterial('LimitState', 34048, 57.26994071, 8.884e-05, 171.80982214, 0.00026653, 572.69940713, 0.00088842, -57.26994071, -8.884e-05, -171.80982214, -0.00026653, -572.69940713, -0.00088842, 0.4, 0.3, 0.003, 0.0, 0.0, 14048, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4048, 99999, 'P', 44048, 'Vy', 34048, 'Vz', 24048, 'My', 14048, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170004, 70004, 170004, 4048, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124020, 124020, 24020, 4048, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174020, 11.25, 0.0, 2.1)
    ops.node(121004, 11.25, 0.0, 3.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4049, 174020, 121004, 0.1225, 31434178.94242973, 13097574.55934572, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24049, 96.92511682, 0.00053925, 116.64118004, 0.05172302, 11.664118, 0.15172302, -96.92511682, -0.00053925, -116.64118004, -0.05172302, -11.664118, -0.15172302, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14049, 83.70587816, 0.00053925, 100.73294441, 0.04438691, 10.07329444, 0.13303521, -83.70587816, -0.00053925, -100.73294441, -0.04438691, -10.07329444, -0.13303521, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24049, 4049, 0.0, 199.00171601, 0.01078494, 199.00171601, 0.03235482, 139.30120121, -4930.80740809, 0.05, 2, 0, 74020, 21004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44049, 49.750429, 6.884e-05, 149.25128701, 0.00020651, 497.50429002, 0.00068837, -49.750429, -6.884e-05, -149.25128701, -0.00020651, -497.50429002, -0.00068837, 0.4, 0.3, 0.003, 0.0, 0.0, 24049, 2)
    ops.limitCurve('ThreePoint', 14049, 4049, 0.0, 243.27262739, 0.01078494, 243.27262739, 0.03235482, 170.29083917, -8688.01398354, 0.05, 2, 0, 74020, 21004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34049, 60.81815685, 8.415e-05, 182.45447054, 0.00025245, 608.18156846, 0.00084151, -60.81815685, -8.415e-05, -182.45447054, -0.00025245, -608.18156846, -0.00084151, 0.4, 0.3, 0.003, 0.0, 0.0, 14049, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4049, 99999, 'P', 44049, 'Vy', 34049, 'Vz', 24049, 'My', 14049, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174020, 74020, 174020, 4049, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121004, 121004, 21004, 4049, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171003, 8.3, 0.0, 3.9)
    ops.node(124021, 8.3, 0.0, 5.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4051, 171003, 124021, 0.1225, 29363664.02316358, 12234860.00965149, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24051, 74.6205289, 0.00051143, 90.35175992, 0.05256006, 9.03517599, 0.15256006, -74.6205289, -0.00051143, -90.35175992, -0.05256006, -9.03517599, -0.15256006, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14051, 68.35254751, 0.00051143, 82.76238528, 0.04509998, 8.27623853, 0.13331469, -68.35254751, -0.00051143, -82.76238528, -0.04509998, -8.27623853, -0.13331469, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24051, 4051, 0.0, 207.31730618, 0.01022866, 207.31730618, 0.03068599, 145.12211433, -6648.1758278, 0.05, 2, 0, 71003, 24021, 2, 3)
    ops.uniaxialMaterial('LimitState', 44051, 51.82932655, 6.432e-05, 155.48797964, 0.00019296, 518.29326546, 0.00064321, -51.82932655, -6.432e-05, -155.48797964, -0.00019296, -518.29326546, -0.00064321, 0.4, 0.3, 0.003, 0.0, 0.0, 24051, 2)
    ops.limitCurve('ThreePoint', 14051, 4051, 0.0, 253.17787526, 0.01022866, 253.17787526, 0.03068599, 177.22451268, -12176.39402112, 0.05, 2, 0, 71003, 24021, 1, 3)
    ops.uniaxialMaterial('LimitState', 34051, 63.29446882, 7.855e-05, 189.88340645, 0.00023565, 632.94468816, 0.0007855, -63.29446882, -7.855e-05, -189.88340645, -0.00023565, -632.94468816, -0.0007855, 0.4, 0.3, 0.003, 0.0, 0.0, 14051, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4051, 99999, 'P', 44051, 'Vy', 34051, 'Vz', 24051, 'My', 14051, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171003, 71003, 171003, 4051, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124021, 124021, 24021, 4051, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174021, 8.3, 0.0, 5.5)
    ops.node(122003, 8.3, 0.0, 6.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4052, 174021, 122003, 0.1225, 29502791.1085671, 12292829.62856962, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24052, 72.72610847, 0.00050887, 88.11794072, 0.05293648, 8.81179407, 0.15293648, -72.72610847, -0.00050887, -88.11794072, -0.05293648, -8.81179407, -0.15293648, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14052, 66.21872093, 0.00050887, 80.23332265, 0.04542209, 8.02333227, 0.13650388, -66.21872093, -0.00050887, -80.23332265, -0.04542209, -8.02333227, -0.13650388, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24052, 4052, 0.0, 201.73373263, 0.0101773, 201.73373263, 0.0305319, 141.21361284, -6731.07789303, 0.05, 2, 0, 74021, 22003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44052, 50.43343316, 6.229e-05, 151.30029947, 0.00018688, 504.33433157, 0.00062294, -50.43343316, -6.229e-05, -151.30029947, -0.00018688, -504.33433157, -0.00062294, 0.4, 0.3, 0.003, 0.0, 0.0, 24052, 2)
    ops.limitCurve('ThreePoint', 14052, 4052, 0.0, 245.9777501, 0.0101773, 245.9777501, 0.0305319, 172.18442507, -12533.29041433, 0.05, 2, 0, 74021, 22003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34052, 61.49443752, 7.596e-05, 184.48331257, 0.00022787, 614.94437525, 0.00075956, -61.49443752, -7.596e-05, -184.48331257, -0.00022787, -614.94437525, -0.00075956, 0.4, 0.3, 0.003, 0.0, 0.0, 14052, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4052, 99999, 'P', 44052, 'Vy', 34052, 'Vz', 24052, 'My', 14052, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174021, 74021, 174021, 4052, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122003, 122003, 22003, 4052, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171004, 11.25, 0.0, 3.9)
    ops.node(124022, 11.25, 0.0, 5.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4053, 171004, 124022, 0.1225, 29091600.08226525, 12121500.03427719, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24053, 74.41604647, 0.00051397, 90.1518214, 0.05262554, 9.01518214, 0.15262554, -74.41604647, -0.00051397, -90.1518214, -0.05262554, -9.01518214, -0.15262554, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14053, 68.20632633, 0.00051397, 82.62901405, 0.04515644, 8.2629014, 0.13277988, -68.20632633, -0.00051397, -82.62901405, -0.04515644, -8.2629014, -0.13277988, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24053, 4053, 0.0, 204.37519658, 0.01027939, 204.37519658, 0.03083816, 143.06263761, -6494.84026358, 0.05, 2, 0, 71004, 24022, 2, 3)
    ops.uniaxialMaterial('LimitState', 44053, 51.09379914, 6.4e-05, 153.28139743, 0.000192, 510.93799145, 0.00064001, -51.09379914, -6.4e-05, -153.28139743, -0.000192, -510.93799145, -0.00064001, 0.4, 0.3, 0.003, 0.0, 0.0, 24053, 2)
    ops.limitCurve('ThreePoint', 14053, 4053, 0.0, 249.48301934, 0.01027939, 249.48301934, 0.03083816, 174.63811354, -11865.31722069, 0.05, 2, 0, 71004, 24022, 1, 3)
    ops.uniaxialMaterial('LimitState', 34053, 62.37075484, 7.813e-05, 187.11226451, 0.00023438, 623.70754835, 0.00078127, -62.37075484, -7.813e-05, -187.11226451, -0.00023438, -623.70754835, -0.00078127, 0.4, 0.3, 0.003, 0.0, 0.0, 14053, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4053, 99999, 'P', 44053, 'Vy', 34053, 'Vz', 24053, 'My', 14053, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171004, 71004, 171004, 4053, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124022, 124022, 24022, 4053, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174022, 11.25, 0.0, 5.5)
    ops.node(122004, 11.25, 0.0, 6.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4054, 174022, 122004, 0.1225, 28929448.73600231, 12053936.9733343, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24054, 70.82872785, 0.00051309, 85.92005016, 0.05345585, 8.59200502, 0.15345585, -70.82872785, -0.00051309, -85.92005016, -0.05345585, -8.59200502, -0.15345585, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14054, 64.76278395, 0.00051309, 78.56164885, 0.04586762, 7.85616488, 0.1358392, -64.76278395, -0.00051309, -78.56164885, -0.04586762, -7.85616488, -0.1358392, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24054, 4054, 0.0, 199.00561426, 0.01026175, 199.00561426, 0.03078526, 139.30392998, -6762.17084132, 0.05, 2, 0, 74022, 22004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44054, 49.75140357, 6.267e-05, 149.2542107, 0.00018801, 497.51403566, 0.00062669, -49.75140357, -6.267e-05, -149.2542107, -0.00018801, -497.51403566, -0.00062669, 0.4, 0.3, 0.003, 0.0, 0.0, 24054, 2)
    ops.limitCurve('ThreePoint', 14054, 4054, 0.0, 243.38962628, 0.01026175, 243.38962628, 0.03078526, 170.3727384, -12596.9396324, 0.05, 2, 0, 74022, 22004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34054, 60.84740657, 7.665e-05, 182.54221971, 0.00022994, 608.47406571, 0.00076646, -60.84740657, -7.665e-05, -182.54221971, -0.00022994, -608.47406571, -0.00076646, 0.4, 0.3, 0.003, 0.0, 0.0, 14054, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4054, 99999, 'P', 44054, 'Vy', 34054, 'Vz', 24054, 'My', 14054, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174022, 74022, 174022, 4054, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122004, 122004, 22004, 4054, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172003, 8.3, 0.0, 6.975)
    ops.node(124023, 8.3, 0.0, 8.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4056, 172003, 124023, 0.0625, 29240683.46867206, 12183618.11194669, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24056, 33.59477162, 0.00062063, 40.61061587, 0.05101767, 4.06106159, 0.15101767, -33.59477162, -0.00062063, -40.61061587, -0.05101767, -4.06106159, -0.15101767, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14056, 33.59477162, 0.00062063, 40.61061587, 0.05101767, 4.06106159, 0.15101767, -33.59477162, -0.00062063, -40.61061587, -0.05101767, -4.06106159, -0.15101767, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24056, 4056, 0.0, 108.32601986, 0.01241269, 108.32601986, 0.03723808, 75.8282139, -4849.66219721, 0.05, 2, 0, 72003, 24023, 2, 3)
    ops.uniaxialMaterial('LimitState', 44056, 27.08150497, 6.615e-05, 81.2445149, 0.00019845, 270.81504966, 0.0006615, -27.08150497, -6.615e-05, -81.2445149, -0.00019845, -270.81504966, -0.0006615, 0.4, 0.3, 0.003, 0.0, 0.0, 24056, 2)
    ops.limitCurve('ThreePoint', 14056, 4056, 0.0, 108.32601986, 0.01241269, 108.32601986, 0.03723808, 75.8282139, -4849.66219721, 0.05, 2, 0, 72003, 24023, 1, 3)
    ops.uniaxialMaterial('LimitState', 34056, 27.08150497, 6.615e-05, 81.2445149, 0.00019845, 270.81504966, 0.0006615, -27.08150497, -6.615e-05, -81.2445149, -0.00019845, -270.81504966, -0.0006615, 0.4, 0.3, 0.003, 0.0, 0.0, 14056, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4056, 99999, 'P', 44056, 'Vy', 34056, 'Vz', 24056, 'My', 14056, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172003, 72003, 172003, 4056, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124023, 124023, 24023, 4056, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174023, 8.3, 0.0, 8.55)
    ops.node(123003, 8.3, 0.0, 9.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4057, 174023, 123003, 0.0625, 30357664.43954884, 12649026.84981202, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24057, 30.91960574, 0.00061069, 37.3665848, 0.05206937, 3.73665848, 0.15206937, -30.91960574, -0.00061069, -37.3665848, -0.05206937, -3.73665848, -0.15206937, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14057, 30.91960574, 0.00061069, 37.3665848, 0.05206937, 3.73665848, 0.15206937, -30.91960574, -0.00061069, -37.3665848, -0.05206937, -3.73665848, -0.15206937, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24057, 4057, 0.0, 106.92713932, 0.01221373, 106.92713932, 0.03664119, 74.84899752, -5384.37057357, 0.05, 2, 0, 74023, 23003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44057, 26.73178483, 6.289e-05, 80.19535449, 0.00018868, 267.3178483, 0.00062893, -26.73178483, -6.289e-05, -80.19535449, -0.00018868, -267.3178483, -0.00062893, 0.4, 0.3, 0.003, 0.0, 0.0, 24057, 2)
    ops.limitCurve('ThreePoint', 14057, 4057, 0.0, 106.92713932, 0.01221373, 106.92713932, 0.03664119, 74.84899752, -5384.37057357, 0.05, 2, 0, 74023, 23003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34057, 26.73178483, 6.289e-05, 80.19535449, 0.00018868, 267.3178483, 0.00062893, -26.73178483, -6.289e-05, -80.19535449, -0.00018868, -267.3178483, -0.00062893, 0.4, 0.3, 0.003, 0.0, 0.0, 14057, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4057, 99999, 'P', 44057, 'Vy', 34057, 'Vz', 24057, 'My', 14057, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174023, 74023, 174023, 4057, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123003, 123003, 23003, 4057, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172004, 11.25, 0.0, 6.975)
    ops.node(124024, 11.25, 0.0, 8.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4058, 172004, 124024, 0.0625, 30059672.92295786, 12524863.71789911, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24058, 33.58050688, 0.00063232, 40.53072504, 0.05066836, 4.0530725, 0.15066836, -33.58050688, -0.00063232, -40.53072504, -0.05066836, -4.0530725, -0.15066836, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14058, 33.58050688, 0.00063232, 40.53072504, 0.05066836, 4.0530725, 0.15066836, -33.58050688, -0.00063232, -40.53072504, -0.05066836, -4.0530725, -0.15066836, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24058, 4058, 0.0, 110.26517897, 0.01264647, 110.26517897, 0.03793941, 77.18562528, -4885.7881741, 0.05, 2, 0, 72004, 24024, 2, 3)
    ops.uniaxialMaterial('LimitState', 44058, 27.56629474, 6.55e-05, 82.69888422, 0.0001965, 275.66294741, 0.000655, -27.56629474, -6.55e-05, -82.69888422, -0.0001965, -275.66294741, -0.000655, 0.4, 0.3, 0.003, 0.0, 0.0, 24058, 2)
    ops.limitCurve('ThreePoint', 14058, 4058, 0.0, 110.26517897, 0.01264647, 110.26517897, 0.03793941, 77.18562528, -4885.7881741, 0.05, 2, 0, 72004, 24024, 1, 3)
    ops.uniaxialMaterial('LimitState', 34058, 27.56629474, 6.55e-05, 82.69888422, 0.0001965, 275.66294741, 0.000655, -27.56629474, -6.55e-05, -82.69888422, -0.0001965, -275.66294741, -0.000655, 0.4, 0.3, 0.003, 0.0, 0.0, 14058, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4058, 99999, 'P', 44058, 'Vy', 34058, 'Vz', 24058, 'My', 14058, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172004, 72004, 172004, 4058, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124024, 124024, 24024, 4058, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174024, 11.25, 0.0, 8.55)
    ops.node(123004, 11.25, 0.0, 9.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4059, 174024, 123004, 0.0625, 29223038.73213694, 12176266.13839039, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24059, 30.66360985, 0.0006137, 37.14827339, 0.05250931, 3.71482734, 0.15250931, -30.66360985, -0.0006137, -37.14827339, -0.05250931, -3.71482734, -0.15250931, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14059, 30.66360985, 0.0006137, 37.14827339, 0.05250931, 3.71482734, 0.15250931, -30.66360985, -0.0006137, -37.14827339, -0.05250931, -3.71482734, -0.15250931, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24059, 4059, 0.0, 104.62701416, 0.01227402, 104.62701416, 0.03682206, 73.23890991, -5371.80356321, 0.05, 2, 0, 74024, 23004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44059, 26.15675354, 6.393e-05, 78.47026062, 0.00019179, 261.56753539, 0.0006393, -26.15675354, -6.393e-05, -78.47026062, -0.00019179, -261.56753539, -0.0006393, 0.4, 0.3, 0.003, 0.0, 0.0, 24059, 2)
    ops.limitCurve('ThreePoint', 14059, 4059, 0.0, 104.62701416, 0.01227402, 104.62701416, 0.03682206, 73.23890991, -5371.80356321, 0.05, 2, 0, 74024, 23004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34059, 26.15675354, 6.393e-05, 78.47026062, 0.00019179, 261.56753539, 0.0006393, -26.15675354, -6.393e-05, -78.47026062, -0.00019179, -261.56753539, -0.0006393, 0.4, 0.3, 0.003, 0.0, 0.0, 14059, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4059, 99999, 'P', 44059, 'Vy', 34059, 'Vz', 24059, 'My', 14059, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174024, 74024, 174024, 4059, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123004, 123004, 23004, 4059, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173003, 8.3, 0.0, 10.1)
    ops.node(124025, 8.3, 0.0, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4061, 173003, 124025, 0.0625, 27588891.6174261, 11495371.50726088, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24061, 25.89652619, 0.00060413, 31.59447182, 0.02949159, 3.15944718, 0.08853482, -25.89652619, -0.00060413, -31.59447182, -0.02949159, -3.15944718, -0.08853482, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14061, 25.89652619, 0.00060413, 31.59447182, 0.02949159, 3.15944718, 0.08853482, -25.89652619, -0.00060413, -31.59447182, -0.02949159, -3.15944718, -0.08853482, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24061, 4061, 0.0, 60.67775891, 0.01208253, 60.67775891, 0.0362476, 42.47443123, -2051.31144639, 0.05, 2, 0, 73003, 24025, 2, 3)
    ops.uniaxialMaterial('LimitState', 44061, 15.16943973, 3.927e-05, 45.50831918, 0.00011782, 151.69439726, 0.00039272, -15.16943973, -3.927e-05, -45.50831918, -0.00011782, -151.69439726, -0.00039272, 0.4, 0.3, 0.003, 0.0, 0.0, 24061, 2)
    ops.limitCurve('ThreePoint', 14061, 4061, 0.0, 60.67775891, 0.01208253, 60.67775891, 0.0362476, 42.47443123, -2051.31144639, 0.05, 2, 0, 73003, 24025, 1, 3)
    ops.uniaxialMaterial('LimitState', 34061, 15.16943973, 3.927e-05, 45.50831918, 0.00011782, 151.69439726, 0.00039272, -15.16943973, -3.927e-05, -45.50831918, -0.00011782, -151.69439726, -0.00039272, 0.4, 0.3, 0.003, 0.0, 0.0, 14061, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4061, 99999, 'P', 44061, 'Vy', 34061, 'Vz', 24061, 'My', 14061, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173003, 73003, 173003, 4061, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124025, 124025, 24025, 4061, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174025, 8.3, 0.0, 11.625)
    ops.node(124003, 8.3, 0.0, 12.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4062, 174025, 124003, 0.0625, 30239701.23109622, 12599875.51295676, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24062, 23.3147523, 0.00056549, 28.32609184, 0.02925233, 2.83260918, 0.09381613, -23.3147523, -0.00056549, -28.32609184, -0.02925233, -2.83260918, -0.09381613, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14062, 23.3147523, 0.00056549, 28.32609184, 0.02925233, 2.83260918, 0.09381613, -23.3147523, -0.00056549, -28.32609184, -0.02925233, -2.83260918, -0.09381613, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24062, 4062, 0.0, 62.19862629, 0.01130984, 62.19862629, 0.03392952, 43.53903841, -3542.4894349, 0.05, 2, 0, 74025, 24003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44062, 15.54965657, 3.673e-05, 46.64896972, 0.00011018, 155.49656573, 0.00036727, -15.54965657, -3.673e-05, -46.64896972, -0.00011018, -155.49656573, -0.00036727, 0.4, 0.3, 0.003, 0.0, 0.0, 24062, 2)
    ops.limitCurve('ThreePoint', 14062, 4062, 0.0, 62.19862629, 0.01130984, 62.19862629, 0.03392952, 43.53903841, -3542.4894349, 0.05, 2, 0, 74025, 24003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34062, 15.54965657, 3.673e-05, 46.64896972, 0.00011018, 155.49656573, 0.00036727, -15.54965657, -3.673e-05, -46.64896972, -0.00011018, -155.49656573, -0.00036727, 0.4, 0.3, 0.003, 0.0, 0.0, 14062, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4062, 99999, 'P', 44062, 'Vy', 34062, 'Vz', 24062, 'My', 14062, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174025, 74025, 174025, 4062, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124003, 124003, 24003, 4062, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173004, 11.25, 0.0, 10.1)
    ops.node(124026, 11.25, 0.0, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4063, 173004, 124026, 0.0625, 28955036.54104822, 12064598.55877009, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24063, 25.77660827, 0.00060287, 31.35775398, 0.02907856, 3.1357754, 0.08923554, -25.77660827, -0.00060287, -31.35775398, -0.02907856, -3.1357754, -0.08923554, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14063, 25.77660827, 0.00060287, 31.35775398, 0.02907856, 3.1357754, 0.08923554, -25.77660827, -0.00060287, -31.35775398, -0.02907856, -3.1357754, -0.08923554, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24063, 4063, 0.0, 63.19181222, 0.01205736, 63.19181222, 0.03617207, 44.23426856, -2050.63939347, 0.05, 2, 0, 73004, 24026, 2, 3)
    ops.uniaxialMaterial('LimitState', 44063, 15.79795306, 3.897e-05, 47.39385917, 0.00011691, 157.97953056, 0.00038969, -15.79795306, -3.897e-05, -47.39385917, -0.00011691, -157.97953056, -0.00038969, 0.4, 0.3, 0.003, 0.0, 0.0, 24063, 2)
    ops.limitCurve('ThreePoint', 14063, 4063, 0.0, 63.19181222, 0.01205736, 63.19181222, 0.03617207, 44.23426856, -2050.63939347, 0.05, 2, 0, 73004, 24026, 1, 3)
    ops.uniaxialMaterial('LimitState', 34063, 15.79795306, 3.897e-05, 47.39385917, 0.00011691, 157.97953056, 0.00038969, -15.79795306, -3.897e-05, -47.39385917, -0.00011691, -157.97953056, -0.00038969, 0.4, 0.3, 0.003, 0.0, 0.0, 14063, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4063, 99999, 'P', 44063, 'Vy', 34063, 'Vz', 24063, 'My', 14063, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173004, 73004, 173004, 4063, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124026, 124026, 24026, 4063, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174026, 11.25, 0.0, 11.625)
    ops.node(124004, 11.25, 0.0, 12.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4064, 174026, 124004, 0.0625, 29679217.27517597, 12366340.53132332, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24064, 23.49919577, 0.00056747, 28.59498774, 0.02957302, 2.85949877, 0.09398657, -23.49919577, -0.00056747, -28.59498774, -0.02957302, -2.85949877, -0.09398657, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14064, 23.49919577, 0.00056747, 28.59498774, 0.02957302, 2.85949877, 0.09398657, -23.49919577, -0.00056747, -28.59498774, -0.02957302, -2.85949877, -0.09398657, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24064, 4064, 0.0, 60.47139189, 0.01134938, 60.47139189, 0.03404813, 42.32997432, -3384.23417995, 0.05, 2, 0, 74026, 24004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44064, 15.11784797, 3.638e-05, 45.35354391, 0.00010914, 151.17847972, 0.00036382, -15.11784797, -3.638e-05, -45.35354391, -0.00010914, -151.17847972, -0.00036382, 0.4, 0.3, 0.003, 0.0, 0.0, 24064, 2)
    ops.limitCurve('ThreePoint', 14064, 4064, 0.0, 60.47139189, 0.01134938, 60.47139189, 0.03404813, 42.32997432, -3384.23417995, 0.05, 2, 0, 74026, 24004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34064, 15.11784797, 3.638e-05, 45.35354391, 0.00010914, 151.17847972, 0.00036382, -15.11784797, -3.638e-05, -45.35354391, -0.00010914, -151.17847972, -0.00036382, 0.4, 0.3, 0.003, 0.0, 0.0, 14064, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4064, 99999, 'P', 44064, 'Vy', 34064, 'Vz', 24064, 'My', 14064, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174026, 74026, 174026, 4064, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124004, 124004, 24004, 4064, '-orient', 0, 0, 1, 0, 1, 0)
