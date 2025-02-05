import openseespy.opensees as ops


def add_columns() -> None:
    """Add components of all columns to ops domain (plastic hinges, column elements and nodes)
    """
    # Create elastic column element nodes
    ops.node(170001, 0.0, 0.0, 0.0)
    ops.node(121001, 0.0, 0.0, 2.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1, 170001, 121001, 0.09, 27822730.79933828, 11592804.49972428, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20001, 43.47513206, 0.00072332, 52.71037643, 0.03230465, 5.27103764, 0.09769081, -43.47513206, -0.00072332, -52.71037643, -0.03230465, -5.27103764, -0.09769081, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10001, 49.23188312, 0.00072332, 59.69001054, 0.03230465, 5.96900105, 0.09769081, -49.23188312, -0.00072332, -59.69001054, -0.03230465, -5.96900105, -0.09769081, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20001, 1, 0.0, 105.66211545, 0.01446649, 105.66211545, 0.04339948, 73.96348082, -1548.127622, 0.05, 2, 0, 70001, 21001, 2, 3)
    ops.uniaxialMaterial('LimitState', 40001, 26.41552886, 9.418e-05, 79.24658659, 0.00028255, 264.15528863, 0.00094183, -26.41552886, -9.418e-05, -79.24658659, -0.00028255, -264.15528863, -0.00094183, 0.4, 0.3, 0.003, 0.0, 0.0, 20001, 2)
    ops.limitCurve('ThreePoint', 10001, 1, 0.0, 105.66211545, 0.01446649, 105.66211545, 0.04339948, 73.96348082, -1548.127622, 0.05, 2, 0, 70001, 21001, 1, 3)
    ops.uniaxialMaterial('LimitState', 30001, 26.41552886, 9.418e-05, 79.24658659, 0.00028255, 264.15528863, 0.00094183, -26.41552886, -9.418e-05, -79.24658659, -0.00028255, -264.15528863, -0.00094183, 0.4, 0.3, 0.003, 0.0, 0.0, 10001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1, 99999, 'P', 40001, 'Vy', 30001, 'Vz', 20001, 'My', 10001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170001, 70001, 170001, 1, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121001, 121001, 21001, 1, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170002, 4.25, 0.0, 0.0)
    ops.node(121002, 4.25, 0.0, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2, 170002, 121002, 0.1225, 29604556.89257659, 12335232.03857358, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20002, 78.33835906, 0.00066099, 94.54222647, 0.04316039, 9.45422265, 0.12478665, -78.33835906, -0.00066099, -94.54222647, -0.04316039, -9.45422265, -0.12478665, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10002, 84.76342585, 0.00066099, 102.2962837, 0.04316039, 10.22962837, 0.12478665, -84.76342585, -0.00066099, -102.2962837, -0.04316039, -10.22962837, -0.12478665, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20002, 2, 0.0, 176.47140121, 0.01321988, 176.47140121, 0.03965963, 123.52998085, -2877.66355645, 0.05, 2, 0, 70002, 21002, 2, 3)
    ops.uniaxialMaterial('LimitState', 40002, 44.1178503, 0.00010861, 132.35355091, 0.00032583, 441.17850303, 0.00108611, -44.1178503, -0.00010861, -132.35355091, -0.00032583, -441.17850303, -0.00108611, 0.4, 0.3, 0.003, 0.0, 0.0, 20002, 2)
    ops.limitCurve('ThreePoint', 10002, 2, 0.0, 176.47140121, 0.01321988, 176.47140121, 0.03965963, 123.52998085, -2877.66355645, 0.05, 2, 0, 70002, 21002, 1, 3)
    ops.uniaxialMaterial('LimitState', 30002, 44.1178503, 0.00010861, 132.35355091, 0.00032583, 441.17850303, 0.00108611, -44.1178503, -0.00010861, -132.35355091, -0.00032583, -441.17850303, -0.00108611, 0.4, 0.3, 0.003, 0.0, 0.0, 10002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2, 99999, 'P', 40002, 'Vy', 30002, 'Vz', 20002, 'My', 10002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170002, 70002, 170002, 2, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121002, 121002, 21002, 2, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170005, 15.6, 0.0, 0.0)
    ops.node(121005, 15.6, 0.0, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 5, 170005, 121005, 0.1225, 29350185.11536952, 12229243.79807063, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20005, 79.11263663, 0.00065575, 95.51815364, 0.04318081, 9.55181536, 0.12411678, -79.11263663, -0.00065575, -95.51815364, -0.04318081, -9.55181536, -0.12411678, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10005, 85.89987133, 0.00065575, 103.71285115, 0.04318081, 10.37128511, 0.12411678, -85.89987133, -0.00065575, -103.71285115, -0.04318081, -10.37128511, -0.12411678, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20005, 5, 0.0, 174.50250424, 0.01311507, 174.50250424, 0.0393452, 122.15175296, -2836.88941034, 0.05, 2, 0, 70005, 21005, 2, 3)
    ops.uniaxialMaterial('LimitState', 40005, 43.62562606, 0.00010833, 130.87687818, 0.00032499, 436.25626059, 0.0010833, -43.62562606, -0.00010833, -130.87687818, -0.00032499, -436.25626059, -0.0010833, 0.4, 0.3, 0.003, 0.0, 0.0, 20005, 2)
    ops.limitCurve('ThreePoint', 10005, 5, 0.0, 174.50250424, 0.01311507, 174.50250424, 0.0393452, 122.15175296, -2836.88941034, 0.05, 2, 0, 70005, 21005, 1, 3)
    ops.uniaxialMaterial('LimitState', 30005, 43.62562606, 0.00010833, 130.87687818, 0.00032499, 436.25626059, 0.0010833, -43.62562606, -0.00010833, -130.87687818, -0.00032499, -436.25626059, -0.0010833, 0.4, 0.3, 0.003, 0.0, 0.0, 10005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 5, 99999, 'P', 40005, 'Vy', 30005, 'Vz', 20005, 'My', 10005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170005, 70005, 170005, 5, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121005, 121005, 21005, 5, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170006, 19.85, 0.0, 0.0)
    ops.node(121006, 19.85, 0.0, 2.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 6, 170006, 121006, 0.09, 29316645.48374938, 12215268.95156224, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20006, 44.80182485, 0.00070291, 54.19157699, 0.03237006, 5.4191577, 0.10091448, -44.80182485, -0.00070291, -54.19157699, -0.03237006, -5.4191577, -0.10091448, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10006, 51.27419041, 0.00070291, 62.02044774, 0.03237006, 6.20204477, 0.10091448, -51.27419041, -0.00070291, -62.02044774, -0.03237006, -6.20204477, -0.10091448, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20006, 6, 0.0, 110.71388528, 0.01405822, 110.71388528, 0.04217465, 77.49971969, -1588.76725499, 0.05, 2, 0, 70006, 21006, 2, 3)
    ops.uniaxialMaterial('LimitState', 40006, 27.67847132, 9.366e-05, 83.03541396, 0.00028097, 276.7847132, 0.00093657, -27.67847132, -9.366e-05, -83.03541396, -0.00028097, -276.7847132, -0.00093657, 0.4, 0.3, 0.003, 0.0, 0.0, 20006, 2)
    ops.limitCurve('ThreePoint', 10006, 6, 0.0, 110.71388528, 0.01405822, 110.71388528, 0.04217465, 77.49971969, -1588.76725499, 0.05, 2, 0, 70006, 21006, 1, 3)
    ops.uniaxialMaterial('LimitState', 30006, 27.67847132, 9.366e-05, 83.03541396, 0.00028097, 276.7847132, 0.00093657, -27.67847132, -9.366e-05, -83.03541396, -0.00028097, -276.7847132, -0.00093657, 0.4, 0.3, 0.003, 0.0, 0.0, 10006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 6, 99999, 'P', 40006, 'Vy', 30006, 'Vz', 20006, 'My', 10006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170006, 70006, 170006, 6, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121006, 121006, 21006, 6, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170007, 0.0, 5.5, 0.0)
    ops.node(121007, 0.0, 5.5, 2.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 7, 170007, 121007, 0.1225, 29108038.54940441, 12128349.39558517, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20007, 102.79383077, 0.00067525, 124.08719488, 0.04165821, 12.40871949, 0.12055511, -102.79383077, -0.00067525, -124.08719488, -0.04165821, -12.40871949, -0.12055511, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10007, 106.65109349, 0.00067525, 128.74347539, 0.04165821, 12.87434754, 0.12055511, -106.65109349, -0.00067525, -128.74347539, -0.04165821, -12.87434754, -0.12055511, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20007, 7, 0.0, 174.09560193, 0.01350496, 174.09560193, 0.04051489, 121.86692135, -2777.2855472, 0.05, 2, 0, 70007, 21007, 2, 3)
    ops.uniaxialMaterial('LimitState', 40007, 43.52390048, 0.00010898, 130.57170145, 0.00032693, 435.23900484, 0.00108977, -43.52390048, -0.00010898, -130.57170145, -0.00032693, -435.23900484, -0.00108977, 0.4, 0.3, 0.003, 0.0, 0.0, 20007, 2)
    ops.limitCurve('ThreePoint', 10007, 7, 0.0, 174.09560193, 0.01350496, 174.09560193, 0.04051489, 121.86692135, -2777.2855472, 0.05, 2, 0, 70007, 21007, 1, 3)
    ops.uniaxialMaterial('LimitState', 30007, 43.52390048, 0.00010898, 130.57170145, 0.00032693, 435.23900484, 0.00108977, -43.52390048, -0.00010898, -130.57170145, -0.00032693, -435.23900484, -0.00108977, 0.4, 0.3, 0.003, 0.0, 0.0, 10007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 7, 99999, 'P', 40007, 'Vy', 30007, 'Vz', 20007, 'My', 10007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170007, 70007, 170007, 7, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121007, 121007, 21007, 7, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170008, 4.25, 5.5, 0.0)
    ops.node(121008, 4.25, 5.5, 2.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 8, 170008, 121008, 0.16, 28772788.93017679, 11988662.05424033, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20008, 170.16758411, 0.00063378, 205.35485713, 0.04176296, 20.53548571, 0.10946794, -170.16758411, -0.00063378, -205.35485713, -0.04176296, -20.53548571, -0.10946794, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10008, 175.12414735, 0.00063378, 211.33633911, 0.04176296, 21.13363391, 0.10946794, -175.12414735, -0.00063378, -211.33633911, -0.04176296, -21.13363391, -0.10946794, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20008, 8, 0.0, 211.55474763, 0.01267551, 211.55474763, 0.03802652, 148.08832334, -3009.08873551, 0.05, 2, 0, 70008, 21008, 2, 3)
    ops.uniaxialMaterial('LimitState', 40008, 52.88868691, 0.00010257, 158.66606072, 0.00030771, 528.88686908, 0.00102569, -52.88868691, -0.00010257, -158.66606072, -0.00030771, -528.88686908, -0.00102569, 0.4, 0.3, 0.003, 0.0, 0.0, 20008, 2)
    ops.limitCurve('ThreePoint', 10008, 8, 0.0, 211.55474763, 0.01267551, 211.55474763, 0.03802652, 148.08832334, -3009.08873551, 0.05, 2, 0, 70008, 21008, 1, 3)
    ops.uniaxialMaterial('LimitState', 30008, 52.88868691, 0.00010257, 158.66606072, 0.00030771, 528.88686908, 0.00102569, -52.88868691, -0.00010257, -158.66606072, -0.00030771, -528.88686908, -0.00102569, 0.4, 0.3, 0.003, 0.0, 0.0, 10008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 8, 99999, 'P', 40008, 'Vy', 30008, 'Vz', 20008, 'My', 10008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170008, 70008, 170008, 8, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121008, 121008, 21008, 8, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170009, 8.5, 5.5, 0.0)
    ops.node(121009, 8.5, 5.5, 2.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 9, 170009, 121009, 0.16, 29763744.8946366, 12401560.37276525, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20009, 172.30491835, 0.00062711, 207.6910833, 0.0422145, 20.76910833, 0.11319976, -172.30491835, -0.00062711, -207.6910833, -0.0422145, -20.76910833, -0.11319976, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10009, 167.51030911, 0.00062711, 201.91180784, 0.0422145, 20.19118078, 0.11319976, -167.51030911, -0.00062711, -201.91180784, -0.0422145, -20.19118078, -0.11319976, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20009, 9, 0.0, 217.76874509, 0.0125422, 217.76874509, 0.03762659, 152.43812156, -3092.93205672, 0.05, 2, 0, 70009, 21009, 2, 3)
    ops.uniaxialMaterial('LimitState', 40009, 54.44218627, 0.00010207, 163.32655882, 0.0003062, 544.42186272, 0.00102066, -54.44218627, -0.00010207, -163.32655882, -0.0003062, -544.42186272, -0.00102066, 0.4, 0.3, 0.003, 0.0, 0.0, 20009, 2)
    ops.limitCurve('ThreePoint', 10009, 9, 0.0, 217.76874509, 0.0125422, 217.76874509, 0.03762659, 152.43812156, -3092.93205672, 0.05, 2, 0, 70009, 21009, 1, 3)
    ops.uniaxialMaterial('LimitState', 30009, 54.44218627, 0.00010207, 163.32655882, 0.0003062, 544.42186272, 0.00102066, -54.44218627, -0.00010207, -163.32655882, -0.0003062, -544.42186272, -0.00102066, 0.4, 0.3, 0.003, 0.0, 0.0, 10009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 9, 99999, 'P', 40009, 'Vy', 30009, 'Vz', 20009, 'My', 10009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170009, 70009, 170009, 9, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121009, 121009, 21009, 9, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170010, 11.35, 5.5, 0.0)
    ops.node(121010, 11.35, 5.5, 2.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 10, 170010, 121010, 0.16, 29032683.72199382, 12096951.55083076, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20010, 167.77465773, 0.00064564, 202.46210104, 0.04237157, 20.2462101, 0.11145726, -167.77465773, -0.00064564, -202.46210104, -0.04237157, -20.2462101, -0.11145726, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10010, 163.38729185, 0.00064564, 197.16764641, 0.04237157, 19.71676464, 0.11145726, -163.38729185, -0.00064564, -197.16764641, -0.04237157, -19.71676464, -0.11145726, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20010, 10, 0.0, 215.7327538, 0.01291279, 215.7327538, 0.03873838, 151.01292766, -3147.52632237, 0.05, 2, 0, 70010, 21010, 2, 3)
    ops.uniaxialMaterial('LimitState', 40010, 53.93318845, 0.00010366, 161.79956535, 0.00031097, 539.33188451, 0.00103658, -53.93318845, -0.00010366, -161.79956535, -0.00031097, -539.33188451, -0.00103658, 0.4, 0.3, 0.003, 0.0, 0.0, 20010, 2)
    ops.limitCurve('ThreePoint', 10010, 10, 0.0, 215.7327538, 0.01291279, 215.7327538, 0.03873838, 151.01292766, -3147.52632237, 0.05, 2, 0, 70010, 21010, 1, 3)
    ops.uniaxialMaterial('LimitState', 30010, 53.93318845, 0.00010366, 161.79956535, 0.00031097, 539.33188451, 0.00103658, -53.93318845, -0.00010366, -161.79956535, -0.00031097, -539.33188451, -0.00103658, 0.4, 0.3, 0.003, 0.0, 0.0, 10010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 10, 99999, 'P', 40010, 'Vy', 30010, 'Vz', 20010, 'My', 10010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170010, 70010, 170010, 10, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121010, 121010, 21010, 10, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170011, 15.6, 5.5, 0.0)
    ops.node(121011, 15.6, 5.5, 2.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 11, 170011, 121011, 0.16, 28948284.03663175, 12061785.01526323, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20011, 165.39611038, 0.00064442, 199.55096853, 0.04192221, 19.95509685, 0.1101196, -165.39611038, -0.00064442, -199.55096853, -0.04192221, -19.95509685, -0.1101196, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10011, 169.87301247, 0.00064442, 204.95236609, 0.04192221, 20.49523661, 0.1101196, -169.87301247, -0.00064442, -204.95236609, -0.04192221, -20.49523661, -0.1101196, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20011, 11, 0.0, 212.85999091, 0.01288834, 212.85999091, 0.03866503, 149.00199364, -3024.31830052, 0.05, 2, 0, 70011, 21011, 2, 3)
    ops.uniaxialMaterial('LimitState', 40011, 53.21499773, 0.00010258, 159.64499318, 0.00030773, 532.14997727, 0.00102576, -53.21499773, -0.00010258, -159.64499318, -0.00030773, -532.14997727, -0.00102576, 0.4, 0.3, 0.003, 0.0, 0.0, 20011, 2)
    ops.limitCurve('ThreePoint', 10011, 11, 0.0, 212.85999091, 0.01288834, 212.85999091, 0.03866503, 149.00199364, -3024.31830052, 0.05, 2, 0, 70011, 21011, 1, 3)
    ops.uniaxialMaterial('LimitState', 30011, 53.21499773, 0.00010258, 159.64499318, 0.00030773, 532.14997727, 0.00102576, -53.21499773, -0.00010258, -159.64499318, -0.00030773, -532.14997727, -0.00102576, 0.4, 0.3, 0.003, 0.0, 0.0, 10011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 11, 99999, 'P', 40011, 'Vy', 30011, 'Vz', 20011, 'My', 10011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170011, 70011, 170011, 11, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121011, 121011, 21011, 11, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170012, 19.85, 5.5, 0.0)
    ops.node(121012, 19.85, 5.5, 2.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 12, 170012, 121012, 0.1225, 29768114.55131588, 12403381.06304828, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20012, 101.85131866, 0.00067321, 122.81724198, 0.04171561, 12.2817242, 0.12248116, -101.85131866, -0.00067321, -122.81724198, -0.04171561, -12.2817242, -0.12248116, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10012, 105.55786076, 0.00067321, 127.28676956, 0.04171561, 12.72867696, 0.12248116, -105.55786076, -0.00067321, -127.28676956, -0.04171561, -12.72867696, -0.12248116, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20012, 12, 0.0, 175.18105912, 0.01346415, 175.18105912, 0.04039245, 122.62674139, -2723.87440319, 0.05, 2, 0, 70012, 21012, 2, 3)
    ops.uniaxialMaterial('LimitState', 40012, 43.79526478, 0.00010722, 131.38579434, 0.00032167, 437.95264781, 0.00107224, -43.79526478, -0.00010722, -131.38579434, -0.00032167, -437.95264781, -0.00107224, 0.4, 0.3, 0.003, 0.0, 0.0, 20012, 2)
    ops.limitCurve('ThreePoint', 10012, 12, 0.0, 175.18105912, 0.01346415, 175.18105912, 0.04039245, 122.62674139, -2723.87440319, 0.05, 2, 0, 70012, 21012, 1, 3)
    ops.uniaxialMaterial('LimitState', 30012, 43.79526478, 0.00010722, 131.38579434, 0.00032167, 437.95264781, 0.00107224, -43.79526478, -0.00010722, -131.38579434, -0.00032167, -437.95264781, -0.00107224, 0.4, 0.3, 0.003, 0.0, 0.0, 10012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 12, 99999, 'P', 40012, 'Vy', 30012, 'Vz', 20012, 'My', 10012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170012, 70012, 170012, 12, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121012, 121012, 21012, 12, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170013, 0.0, 11.0, 0.0)
    ops.node(121013, 0.0, 11.0, 2.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 13, 170013, 121013, 0.09, 29558680.10729924, 12316116.71137469, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20013, 43.26534366, 0.00070099, 52.30912361, 0.0326506, 5.23091236, 0.10165551, -43.26534366, -0.00070099, -52.30912361, -0.0326506, -5.23091236, -0.10165551, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10013, 48.93288777, 0.00070099, 59.16135776, 0.0326506, 5.91613578, 0.10165551, -48.93288777, -0.00070099, -59.16135776, -0.0326506, -5.91613578, -0.10165551, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20013, 13, 0.0, 111.48033423, 0.0140199, 111.48033423, 0.04205969, 78.03623396, -1592.96894657, 0.05, 2, 0, 70013, 21013, 2, 3)
    ops.uniaxialMaterial('LimitState', 40013, 27.87008356, 9.353e-05, 83.61025067, 0.0002806, 278.70083557, 0.00093533, -27.87008356, -9.353e-05, -83.61025067, -0.0002806, -278.70083557, -0.00093533, 0.4, 0.3, 0.003, 0.0, 0.0, 20013, 2)
    ops.limitCurve('ThreePoint', 10013, 13, 0.0, 111.48033423, 0.0140199, 111.48033423, 0.04205969, 78.03623396, -1592.96894657, 0.05, 2, 0, 70013, 21013, 1, 3)
    ops.uniaxialMaterial('LimitState', 30013, 27.87008356, 9.353e-05, 83.61025067, 0.0002806, 278.70083557, 0.00093533, -27.87008356, -9.353e-05, -83.61025067, -0.0002806, -278.70083557, -0.00093533, 0.4, 0.3, 0.003, 0.0, 0.0, 10013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 13, 99999, 'P', 40013, 'Vy', 30013, 'Vz', 20013, 'My', 10013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170013, 70013, 170013, 13, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121013, 121013, 21013, 13, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170014, 4.25, 11.0, 0.0)
    ops.node(121014, 4.25, 11.0, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 14, 170014, 121014, 0.1225, 28532222.42798179, 11888426.01165908, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20014, 87.94301238, 0.00067253, 106.30970787, 0.0427727, 10.63097079, 0.12134878, -87.94301238, -0.00067253, -106.30970787, -0.0427727, -10.63097079, -0.12134878, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10014, 91.70867259, 0.00067253, 110.86181754, 0.0427727, 11.08618175, 0.12134878, -91.70867259, -0.00067253, -110.86181754, -0.0427727, -11.08618175, -0.12134878, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20014, 14, 0.0, 171.97067775, 0.01345058, 171.97067775, 0.04035175, 120.37947442, -2856.92985454, 0.05, 2, 0, 70014, 21014, 2, 3)
    ops.uniaxialMaterial('LimitState', 40014, 42.99266944, 0.00010982, 128.97800831, 0.00032946, 429.92669437, 0.00109819, -42.99266944, -0.00010982, -128.97800831, -0.00032946, -429.92669437, -0.00109819, 0.4, 0.3, 0.003, 0.0, 0.0, 20014, 2)
    ops.limitCurve('ThreePoint', 10014, 14, 0.0, 171.97067775, 0.01345058, 171.97067775, 0.04035175, 120.37947442, -2856.92985454, 0.05, 2, 0, 70014, 21014, 1, 3)
    ops.uniaxialMaterial('LimitState', 30014, 42.99266944, 0.00010982, 128.97800831, 0.00032946, 429.92669437, 0.00109819, -42.99266944, -0.00010982, -128.97800831, -0.00032946, -429.92669437, -0.00109819, 0.4, 0.3, 0.003, 0.0, 0.0, 10014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 14, 99999, 'P', 40014, 'Vy', 30014, 'Vz', 20014, 'My', 10014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170014, 70014, 170014, 14, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121014, 121014, 21014, 14, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170015, 8.5, 11.0, 0.0)
    ops.node(121015, 8.5, 11.0, 2.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 15, 170015, 121015, 0.09, 29524053.25041422, 12301688.85433926, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20015, 57.28628715, 0.00075623, 69.05573801, 0.03379314, 6.9055738, 0.09677362, -57.28628715, -0.00075623, -69.05573801, -0.03379314, -6.9055738, -0.09677362, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10015, 60.28671623, 0.00075623, 72.67260436, 0.03379314, 7.26726044, 0.09677362, -60.28671623, -0.00075623, -72.67260436, -0.03379314, -7.26726044, -0.09677362, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20015, 15, 0.0, 114.42949681, 0.01512459, 114.42949681, 0.04537377, 80.10064777, -1473.2153345, 0.05, 2, 0, 70015, 21015, 2, 3)
    ops.uniaxialMaterial('LimitState', 40015, 28.6073742, 9.612e-05, 85.82212261, 0.00028836, 286.07374204, 0.0009612, -28.6073742, -9.612e-05, -85.82212261, -0.00028836, -286.07374204, -0.0009612, 0.4, 0.3, 0.003, 0.0, 0.0, 20015, 2)
    ops.limitCurve('ThreePoint', 10015, 15, 0.0, 114.42949681, 0.01512459, 114.42949681, 0.04537377, 80.10064777, -1473.2153345, 0.05, 2, 0, 70015, 21015, 1, 3)
    ops.uniaxialMaterial('LimitState', 30015, 28.6073742, 9.612e-05, 85.82212261, 0.00028836, 286.07374204, 0.0009612, -28.6073742, -9.612e-05, -85.82212261, -0.00028836, -286.07374204, -0.0009612, 0.4, 0.3, 0.003, 0.0, 0.0, 10015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 15, 99999, 'P', 40015, 'Vy', 30015, 'Vz', 20015, 'My', 10015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170015, 70015, 170015, 15, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121015, 121015, 21015, 15, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170016, 11.35, 11.0, 0.0)
    ops.node(121016, 11.35, 11.0, 2.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 16, 170016, 121016, 0.09, 28709464.04057002, 11962276.68357084, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20016, 57.60960638, 0.00076444, 69.52532425, 0.03376408, 6.95253243, 0.09473153, -57.60960638, -0.00076444, -69.52532425, -0.03376408, -6.95253243, -0.09473153, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10016, 60.69108406, 0.00076444, 73.24416124, 0.03376408, 7.32441612, 0.09473153, -60.69108406, -0.00076444, -73.24416124, -0.03376408, -7.32441612, -0.09473153, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20016, 16, 0.0, 112.99528257, 0.01528875, 112.99528257, 0.04586626, 79.0966978, -1499.02556951, 0.05, 2, 0, 70016, 21016, 2, 3)
    ops.uniaxialMaterial('LimitState', 40016, 28.24882064, 9.761e-05, 84.74646193, 0.00029283, 282.48820643, 0.00097608, -28.24882064, -9.761e-05, -84.74646193, -0.00029283, -282.48820643, -0.00097608, 0.4, 0.3, 0.003, 0.0, 0.0, 20016, 2)
    ops.limitCurve('ThreePoint', 10016, 16, 0.0, 112.99528257, 0.01528875, 112.99528257, 0.04586626, 79.0966978, -1499.02556951, 0.05, 2, 0, 70016, 21016, 1, 3)
    ops.uniaxialMaterial('LimitState', 30016, 28.24882064, 9.761e-05, 84.74646193, 0.00029283, 282.48820643, 0.00097608, -28.24882064, -9.761e-05, -84.74646193, -0.00029283, -282.48820643, -0.00097608, 0.4, 0.3, 0.003, 0.0, 0.0, 10016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 16, 99999, 'P', 40016, 'Vy', 30016, 'Vz', 20016, 'My', 10016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170016, 70016, 170016, 16, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121016, 121016, 21016, 16, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170017, 15.6, 11.0, 0.0)
    ops.node(121017, 15.6, 11.0, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 17, 170017, 121017, 0.1225, 30201579.21782729, 12583991.34076137, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20017, 87.6241922, 0.00068055, 105.63068466, 0.04275117, 10.56306847, 0.12592135, -87.6241922, -0.00068055, -105.63068466, -0.04275117, -10.56306847, -0.12592135, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10017, 91.11397319, 0.00068055, 109.83760454, 0.04275117, 10.98376045, 0.12592135, -91.11397319, -0.00068055, -109.83760454, -0.04275117, -10.98376045, -0.12592135, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20017, 17, 0.0, 177.08565515, 0.01361098, 177.08565515, 0.04083295, 123.9599586, -2812.05804536, 0.05, 2, 0, 70017, 21017, 2, 3)
    ops.uniaxialMaterial('LimitState', 40017, 44.27141379, 0.00010683, 132.81424136, 0.0003205, 442.71413786, 0.00106835, -44.27141379, -0.00010683, -132.81424136, -0.0003205, -442.71413786, -0.00106835, 0.4, 0.3, 0.003, 0.0, 0.0, 20017, 2)
    ops.limitCurve('ThreePoint', 10017, 17, 0.0, 177.08565515, 0.01361098, 177.08565515, 0.04083295, 123.9599586, -2812.05804536, 0.05, 2, 0, 70017, 21017, 1, 3)
    ops.uniaxialMaterial('LimitState', 30017, 44.27141379, 0.00010683, 132.81424136, 0.0003205, 442.71413786, 0.00106835, -44.27141379, -0.00010683, -132.81424136, -0.0003205, -442.71413786, -0.00106835, 0.4, 0.3, 0.003, 0.0, 0.0, 10017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 17, 99999, 'P', 40017, 'Vy', 30017, 'Vz', 20017, 'My', 10017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170017, 70017, 170017, 17, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121017, 121017, 21017, 17, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170018, 19.85, 11.0, 0.0)
    ops.node(121018, 19.85, 11.0, 2.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 18, 170018, 121018, 0.09, 30441083.63528915, 12683784.84803715, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20018, 44.18556351, 0.00072081, 53.32321023, 0.03236363, 5.33232102, 0.10293922, -44.18556351, -0.00072081, -53.32321023, -0.03236363, -5.33232102, -0.10293922, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10018, 49.83614798, 0.00072081, 60.1423448, 0.03236363, 6.01423448, 0.10293922, -49.83614798, -0.00072081, -60.1423448, -0.03236363, -6.01423448, -0.10293922, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20018, 18, 0.0, 114.19417469, 0.01441612, 114.19417469, 0.04324837, 79.93592229, -1604.20901298, 0.05, 2, 0, 70018, 21018, 2, 3)
    ops.uniaxialMaterial('LimitState', 40018, 28.54854367, 9.303e-05, 85.64563102, 0.0002791, 285.48543674, 0.00093033, -28.54854367, -9.303e-05, -85.64563102, -0.0002791, -285.48543674, -0.00093033, 0.4, 0.3, 0.003, 0.0, 0.0, 20018, 2)
    ops.limitCurve('ThreePoint', 10018, 18, 0.0, 114.19417469, 0.01441612, 114.19417469, 0.04324837, 79.93592229, -1604.20901298, 0.05, 2, 0, 70018, 21018, 1, 3)
    ops.uniaxialMaterial('LimitState', 30018, 28.54854367, 9.303e-05, 85.64563102, 0.0002791, 285.48543674, 0.00093033, -28.54854367, -9.303e-05, -85.64563102, -0.0002791, -285.48543674, -0.00093033, 0.4, 0.3, 0.003, 0.0, 0.0, 10018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 18, 99999, 'P', 40018, 'Vy', 30018, 'Vz', 20018, 'My', 10018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170018, 70018, 170018, 18, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121018, 121018, 21018, 18, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171001, 0.0, 0.0, 3.375)
    ops.node(122001, 0.0, 0.0, 5.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1001, 171001, 122001, 0.09, 29481137.17334965, 12283807.15556235, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21001, 34.42190701, 0.0007143, 41.71984828, 0.03284736, 4.17198483, 0.10662797, -34.42190701, -0.0007143, -41.71984828, -0.03284736, -4.17198483, -0.10662797, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11001, 36.92790394, 0.0007143, 44.75715274, 0.03284736, 4.47571527, 0.10662797, -36.92790394, -0.0007143, -44.75715274, -0.03284736, -4.47571527, -0.10662797, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21001, 1001, 0.0, 107.7566076, 0.01428605, 107.7566076, 0.04285816, 75.42962532, -1769.51437006, 0.05, 2, 0, 71001, 22001, 2, 3)
    ops.uniaxialMaterial('LimitState', 41001, 26.9391519, 9.065e-05, 80.8174557, 0.00027194, 269.39151901, 0.00090647, -26.9391519, -9.065e-05, -80.8174557, -0.00027194, -269.39151901, -0.00090647, 0.4, 0.3, 0.003, 0.0, 0.0, 21001, 2)
    ops.limitCurve('ThreePoint', 11001, 1001, 0.0, 107.7566076, 0.01428605, 107.7566076, 0.04285816, 75.42962532, -1769.51437006, 0.05, 2, 0, 71001, 22001, 1, 3)
    ops.uniaxialMaterial('LimitState', 31001, 26.9391519, 9.065e-05, 80.8174557, 0.00027194, 269.39151901, 0.00090647, -26.9391519, -9.065e-05, -80.8174557, -0.00027194, -269.39151901, -0.00090647, 0.4, 0.3, 0.003, 0.0, 0.0, 11001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1001, 99999, 'P', 41001, 'Vy', 31001, 'Vz', 21001, 'My', 11001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171001, 71001, 171001, 1001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122001, 122001, 22001, 1001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171002, 4.25, 0.0, 3.3)
    ops.node(122002, 4.25, 0.0, 6.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1002, 171002, 122002, 0.1225, 30412020.66071639, 12671675.27529849, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21002, 70.26350225, 0.00064552, 84.87683786, 0.04471821, 8.48768379, 0.13483743, -70.26350225, -0.00064552, -84.87683786, -0.04471821, -8.48768379, -0.13483743, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11002, 76.74943594, 0.00064552, 92.71170981, 0.04471821, 9.27117098, 0.13483743, -76.74943594, -0.00064552, -92.71170981, -0.04471821, -9.27117098, -0.13483743, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21002, 1002, 0.0, 174.24512249, 0.01291036, 174.24512249, 0.03873107, 121.97158574, -3231.38806112, 0.05, 2, 0, 71002, 22002, 2, 3)
    ops.uniaxialMaterial('LimitState', 41002, 43.56128062, 0.00010439, 130.68384187, 0.00031318, 435.61280622, 0.00104393, -43.56128062, -0.00010439, -130.68384187, -0.00031318, -435.61280622, -0.00104393, 0.4, 0.3, 0.003, 0.0, 0.0, 21002, 2)
    ops.limitCurve('ThreePoint', 11002, 1002, 0.0, 174.24512249, 0.01291036, 174.24512249, 0.03873107, 121.97158574, -3231.38806112, 0.05, 2, 0, 71002, 22002, 1, 3)
    ops.uniaxialMaterial('LimitState', 31002, 43.56128062, 0.00010439, 130.68384187, 0.00031318, 435.61280622, 0.00104393, -43.56128062, -0.00010439, -130.68384187, -0.00031318, -435.61280622, -0.00104393, 0.4, 0.3, 0.003, 0.0, 0.0, 11002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1002, 99999, 'P', 41002, 'Vy', 31002, 'Vz', 21002, 'My', 11002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171002, 71002, 171002, 1002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122002, 122002, 22002, 1002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171005, 15.6, 0.0, 3.3)
    ops.node(122005, 15.6, 0.0, 6.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1005, 171005, 122005, 0.1225, 28274496.97854435, 11781040.40772681, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21005, 69.30071951, 0.00065716, 84.06732629, 0.04532254, 8.40673263, 0.13080643, -69.30071951, -0.00065716, -84.06732629, -0.04532254, -8.40673263, -0.13080643, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11005, 75.67589736, 0.00065716, 91.8009279, 0.04532254, 9.18009279, 0.13080643, -75.67589736, -0.00065716, -91.8009279, -0.04532254, -9.18009279, -0.13080643, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21005, 1005, 0.0, 166.86495343, 0.01314317, 166.86495343, 0.03942951, 116.8054674, -3254.14216823, 0.05, 2, 0, 71005, 22005, 2, 3)
    ops.uniaxialMaterial('LimitState', 41005, 41.71623836, 0.00010753, 125.14871507, 0.00032259, 417.16238358, 0.0010753, -41.71623836, -0.00010753, -125.14871507, -0.00032259, -417.16238358, -0.0010753, 0.4, 0.3, 0.003, 0.0, 0.0, 21005, 2)
    ops.limitCurve('ThreePoint', 11005, 1005, 0.0, 166.86495343, 0.01314317, 166.86495343, 0.03942951, 116.8054674, -3254.14216823, 0.05, 2, 0, 71005, 22005, 1, 3)
    ops.uniaxialMaterial('LimitState', 31005, 41.71623836, 0.00010753, 125.14871507, 0.00032259, 417.16238358, 0.0010753, -41.71623836, -0.00010753, -125.14871507, -0.00032259, -417.16238358, -0.0010753, 0.4, 0.3, 0.003, 0.0, 0.0, 11005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1005, 99999, 'P', 41005, 'Vy', 31005, 'Vz', 21005, 'My', 11005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171005, 71005, 171005, 1005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122005, 122005, 22005, 1005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171006, 19.85, 0.0, 3.375)
    ops.node(122006, 19.85, 0.0, 5.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1006, 171006, 122006, 0.09, 29505554.99546578, 12293981.24811074, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21006, 34.27720332, 0.00068359, 41.54226131, 0.03324119, 4.15422613, 0.1070572, -34.27720332, -0.00068359, -41.54226131, -0.03324119, -4.15422613, -0.1070572, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11006, 36.97155839, 0.00068359, 44.80768531, 0.03324119, 4.48076853, 0.1070572, -36.97155839, -0.00068359, -44.80768531, -0.03324119, -4.48076853, -0.1070572, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21006, 1006, 0.0, 108.3277485, 0.01367176, 108.3277485, 0.04101528, 75.82942395, -1793.8516411, 0.05, 2, 0, 71006, 22006, 2, 3)
    ops.uniaxialMaterial('LimitState', 41006, 27.08193713, 9.105e-05, 81.24581138, 0.00027315, 270.81937126, 0.00091052, -27.08193713, -9.105e-05, -81.24581138, -0.00027315, -270.81937126, -0.00091052, 0.4, 0.3, 0.003, 0.0, 0.0, 21006, 2)
    ops.limitCurve('ThreePoint', 11006, 1006, 0.0, 108.3277485, 0.01367176, 108.3277485, 0.04101528, 75.82942395, -1793.8516411, 0.05, 2, 0, 71006, 22006, 1, 3)
    ops.uniaxialMaterial('LimitState', 31006, 27.08193713, 9.105e-05, 81.24581138, 0.00027315, 270.81937126, 0.00091052, -27.08193713, -9.105e-05, -81.24581138, -0.00027315, -270.81937126, -0.00091052, 0.4, 0.3, 0.003, 0.0, 0.0, 11006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1006, 99999, 'P', 41006, 'Vy', 31006, 'Vz', 21006, 'My', 11006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171006, 71006, 171006, 1006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122006, 122006, 22006, 1006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171007, 0.0, 5.5, 3.375)
    ops.node(122007, 0.0, 5.5, 5.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1007, 171007, 122007, 0.1225, 28186091.72620538, 11744204.88591891, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21007, 58.31178286, 0.00062944, 70.71657667, 0.03056293, 7.07165767, 0.09004128, -58.31178286, -0.00062944, -70.71657667, -0.03056293, -7.07165767, -0.09004128, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11007, 65.59407088, 0.00062944, 79.54804184, 0.03056293, 7.95480418, 0.09004128, -65.59407088, -0.00062944, -79.54804184, -0.03056293, -7.95480418, -0.09004128, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21007, 1007, 0.0, 136.17791555, 0.01258884, 136.17791555, 0.03776653, 95.32454089, -1854.61732536, 0.05, 2, 0, 71007, 22007, 2, 3)
    ops.uniaxialMaterial('LimitState', 41007, 34.04447889, 8.803e-05, 102.13343666, 0.00026409, 340.44478888, 0.0008803, -34.04447889, -8.803e-05, -102.13343666, -0.00026409, -340.44478888, -0.0008803, 0.4, 0.3, 0.003, 0.0, 0.0, 21007, 2)
    ops.limitCurve('ThreePoint', 11007, 1007, 0.0, 136.17791555, 0.01258884, 136.17791555, 0.03776653, 95.32454089, -1854.61732536, 0.05, 2, 0, 71007, 22007, 1, 3)
    ops.uniaxialMaterial('LimitState', 31007, 34.04447889, 8.803e-05, 102.13343666, 0.00026409, 340.44478888, 0.0008803, -34.04447889, -8.803e-05, -102.13343666, -0.00026409, -340.44478888, -0.0008803, 0.4, 0.3, 0.003, 0.0, 0.0, 11007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1007, 99999, 'P', 41007, 'Vy', 31007, 'Vz', 21007, 'My', 11007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171007, 71007, 171007, 1007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122007, 122007, 22007, 1007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171008, 4.25, 5.5, 3.325)
    ops.node(122008, 4.25, 5.5, 6.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1008, 171008, 122008, 0.16, 29334061.25741038, 12222525.52392099, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21008, 105.22809695, 0.00059298, 127.27538052, 0.03178121, 12.72753805, 0.08577144, -105.22809695, -0.00059298, -127.27538052, -0.03178121, -12.72753805, -0.08577144, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11008, 96.69785766, 0.00059298, 116.95789419, 0.03178121, 11.69578942, 0.08577144, -96.69785766, -0.00059298, -116.95789419, -0.03178121, -11.69578942, -0.08577144, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21008, 1008, 0.0, 176.31385629, 0.01185969, 176.31385629, 0.03557906, 123.4196994, -2085.6361869, 0.05, 2, 0, 71008, 22008, 2, 3)
    ops.uniaxialMaterial('LimitState', 41008, 44.07846407, 8.385e-05, 132.23539221, 0.00025154, 440.78464072, 0.00083847, -44.07846407, -8.385e-05, -132.23539221, -0.00025154, -440.78464072, -0.00083847, 0.4, 0.3, 0.003, 0.0, 0.0, 21008, 2)
    ops.limitCurve('ThreePoint', 11008, 1008, 0.0, 176.31385629, 0.01185969, 176.31385629, 0.03557906, 123.4196994, -2085.6361869, 0.05, 2, 0, 71008, 22008, 1, 3)
    ops.uniaxialMaterial('LimitState', 31008, 44.07846407, 8.385e-05, 132.23539221, 0.00025154, 440.78464072, 0.00083847, -44.07846407, -8.385e-05, -132.23539221, -0.00025154, -440.78464072, -0.00083847, 0.4, 0.3, 0.003, 0.0, 0.0, 11008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1008, 99999, 'P', 41008, 'Vy', 31008, 'Vz', 21008, 'My', 11008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171008, 71008, 171008, 1008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122008, 122008, 22008, 1008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171009, 8.5, 5.5, 3.325)
    ops.node(122009, 8.5, 5.5, 6.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1009, 171009, 122009, 0.16, 28364455.65409087, 11818523.18920453, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21009, 106.01930608, 0.00059927, 128.46361866, 0.0407686, 12.84636187, 0.11479683, -106.01930608, -0.00059927, -128.46361866, -0.0407686, -12.84636187, -0.11479683, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11009, 97.06294533, 0.00059927, 117.61119418, 0.0407686, 11.76111942, 0.11479683, -97.06294533, -0.00059927, -117.61119418, -0.0407686, -11.76111942, -0.11479683, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21009, 1009, 0.0, 203.9928574, 0.01198531, 203.9928574, 0.03595592, 142.79500018, -3324.06041559, 0.05, 2, 0, 71009, 22009, 2, 3)
    ops.uniaxialMaterial('LimitState', 41009, 50.99821435, 0.00010033, 152.99464305, 0.00030098, 509.9821435, 0.00100326, -50.99821435, -0.00010033, -152.99464305, -0.00030098, -509.9821435, -0.00100326, 0.4, 0.3, 0.003, 0.0, 0.0, 21009, 2)
    ops.limitCurve('ThreePoint', 11009, 1009, 0.0, 203.9928574, 0.01198531, 203.9928574, 0.03595592, 142.79500018, -3324.06041559, 0.05, 2, 0, 71009, 22009, 1, 3)
    ops.uniaxialMaterial('LimitState', 31009, 50.99821435, 0.00010033, 152.99464305, 0.00030098, 509.9821435, 0.00100326, -50.99821435, -0.00010033, -152.99464305, -0.00030098, -509.9821435, -0.00100326, 0.4, 0.3, 0.003, 0.0, 0.0, 11009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1009, 99999, 'P', 41009, 'Vy', 31009, 'Vz', 21009, 'My', 11009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171009, 71009, 171009, 1009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122009, 122009, 22009, 1009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171010, 11.35, 5.5, 3.325)
    ops.node(122010, 11.35, 5.5, 6.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1010, 171010, 122010, 0.16, 28502347.76707625, 11875978.23628177, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21010, 105.63819009, 0.00059898, 127.97465273, 0.04092265, 12.79746527, 0.11527431, -105.63819009, -0.00059898, -127.97465273, -0.04092265, -12.79746527, -0.11527431, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11010, 96.79625459, 0.00059898, 117.2631513, 0.04092265, 11.72631513, 0.11527431, -96.79625459, -0.00059898, -117.2631513, -0.04092265, -11.72631513, -0.11527431, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21010, 1010, 0.0, 205.41003031, 0.01197956, 205.41003031, 0.03593867, 143.78702121, -3356.32772784, 0.05, 2, 0, 71010, 22010, 2, 3)
    ops.uniaxialMaterial('LimitState', 41010, 51.35250758, 0.00010053, 154.05752273, 0.0003016, 513.52507577, 0.00100535, -51.35250758, -0.00010053, -154.05752273, -0.0003016, -513.52507577, -0.00100535, 0.4, 0.3, 0.003, 0.0, 0.0, 21010, 2)
    ops.limitCurve('ThreePoint', 11010, 1010, 0.0, 205.41003031, 0.01197956, 205.41003031, 0.03593867, 143.78702121, -3356.32772784, 0.05, 2, 0, 71010, 22010, 1, 3)
    ops.uniaxialMaterial('LimitState', 31010, 51.35250758, 0.00010053, 154.05752273, 0.0003016, 513.52507577, 0.00100535, -51.35250758, -0.00010053, -154.05752273, -0.0003016, -513.52507577, -0.00100535, 0.4, 0.3, 0.003, 0.0, 0.0, 11010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1010, 99999, 'P', 41010, 'Vy', 31010, 'Vz', 21010, 'My', 11010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171010, 71010, 171010, 1010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122010, 122010, 22010, 1010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171011, 15.6, 5.5, 3.325)
    ops.node(122011, 15.6, 5.5, 6.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1011, 171011, 122011, 0.16, 29711434.97458602, 12379764.57274417, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21011, 106.35998537, 0.00058769, 128.5512731, 0.0316235, 12.85512731, 0.08617476, -106.35998537, -0.00058769, -128.5512731, -0.0316235, -12.85512731, -0.08617476, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11011, 97.51637373, 0.00058769, 117.86250203, 0.0316235, 11.7862502, 0.08617476, -97.51637373, -0.00058769, -117.86250203, -0.0316235, -11.7862502, -0.08617476, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21011, 1011, 0.0, 177.64924352, 0.01175372, 177.64924352, 0.03526117, 124.35447046, -2069.50768707, 0.05, 2, 0, 71011, 22011, 2, 3)
    ops.uniaxialMaterial('LimitState', 41011, 44.41231088, 8.341e-05, 133.23693264, 0.00025023, 444.12310879, 0.00083409, -44.41231088, -8.341e-05, -133.23693264, -0.00025023, -444.12310879, -0.00083409, 0.4, 0.3, 0.003, 0.0, 0.0, 21011, 2)
    ops.limitCurve('ThreePoint', 11011, 1011, 0.0, 177.64924352, 0.01175372, 177.64924352, 0.03526117, 124.35447046, -2069.50768707, 0.05, 2, 0, 71011, 22011, 1, 3)
    ops.uniaxialMaterial('LimitState', 31011, 44.41231088, 8.341e-05, 133.23693264, 0.00025023, 444.12310879, 0.00083409, -44.41231088, -8.341e-05, -133.23693264, -0.00025023, -444.12310879, -0.00083409, 0.4, 0.3, 0.003, 0.0, 0.0, 11011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1011, 99999, 'P', 41011, 'Vy', 31011, 'Vz', 21011, 'My', 11011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171011, 71011, 171011, 1011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122011, 122011, 22011, 1011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171012, 19.85, 5.5, 3.375)
    ops.node(122012, 19.85, 5.5, 5.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1012, 171012, 122012, 0.1225, 28835944.71810736, 12014976.96587807, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21012, 58.4762113, 0.00063271, 70.84071195, 0.03059845, 7.0840712, 0.09121968, -58.4762113, -0.00063271, -70.84071195, -0.03059845, -7.0840712, -0.09121968, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11012, 65.61104269, 0.00063271, 79.48416753, 0.03059845, 7.94841675, 0.09121968, -65.61104269, -0.00063271, -79.48416753, -0.03059845, -7.94841675, -0.09121968, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21012, 1012, 0.0, 137.88219951, 0.01265412, 137.88219951, 0.03796236, 96.51753966, -1830.82784373, 0.05, 2, 0, 71012, 22012, 2, 3)
    ops.uniaxialMaterial('LimitState', 41012, 34.47054988, 8.712e-05, 103.41164963, 0.00026137, 344.70549877, 0.00087123, -34.47054988, -8.712e-05, -103.41164963, -0.00026137, -344.70549877, -0.00087123, 0.4, 0.3, 0.003, 0.0, 0.0, 21012, 2)
    ops.limitCurve('ThreePoint', 11012, 1012, 0.0, 137.88219951, 0.01265412, 137.88219951, 0.03796236, 96.51753966, -1830.82784373, 0.05, 2, 0, 71012, 22012, 1, 3)
    ops.uniaxialMaterial('LimitState', 31012, 34.47054988, 8.712e-05, 103.41164963, 0.00026137, 344.70549877, 0.00087123, -34.47054988, -8.712e-05, -103.41164963, -0.00026137, -344.70549877, -0.00087123, 0.4, 0.3, 0.003, 0.0, 0.0, 11012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1012, 99999, 'P', 41012, 'Vy', 31012, 'Vz', 21012, 'My', 11012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171012, 71012, 171012, 1012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122012, 122012, 22012, 1012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171013, 0.0, 11.0, 3.375)
    ops.node(122013, 0.0, 11.0, 5.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1013, 171013, 122013, 0.09, 28414397.05274494, 11839332.10531039, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21013, 39.06239366, 0.00070182, 47.44509856, 0.03415154, 4.74450986, 0.10627247, -39.06239366, -0.00070182, -47.44509856, -0.03415154, -4.74450986, -0.10627247, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11013, 44.90188943, 0.00070182, 54.53773744, 0.03415154, 5.45377374, 0.10627247, -44.90188943, -0.00070182, -54.53773744, -0.03415154, -5.45377374, -0.10627247, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21013, 1013, 0.0, 105.61352909, 0.01403645, 105.61352909, 0.04210935, 73.92947036, -1802.36113829, 0.05, 2, 0, 71013, 22013, 2, 3)
    ops.uniaxialMaterial('LimitState', 41013, 26.40338227, 9.218e-05, 79.21014681, 0.00027654, 264.03382271, 0.00092179, -26.40338227, -9.218e-05, -79.21014681, -0.00027654, -264.03382271, -0.00092179, 0.4, 0.3, 0.003, 0.0, 0.0, 21013, 2)
    ops.limitCurve('ThreePoint', 11013, 1013, 0.0, 105.61352909, 0.01403645, 105.61352909, 0.04210935, 73.92947036, -1802.36113829, 0.05, 2, 0, 71013, 22013, 1, 3)
    ops.uniaxialMaterial('LimitState', 31013, 26.40338227, 9.218e-05, 79.21014681, 0.00027654, 264.03382271, 0.00092179, -26.40338227, -9.218e-05, -79.21014681, -0.00027654, -264.03382271, -0.00092179, 0.4, 0.3, 0.003, 0.0, 0.0, 11013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1013, 99999, 'P', 41013, 'Vy', 31013, 'Vz', 21013, 'My', 11013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171013, 71013, 171013, 1013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122013, 122013, 22013, 1013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171014, 4.25, 11.0, 3.3)
    ops.node(122014, 4.25, 11.0, 6.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1014, 171014, 122014, 0.1225, 28819413.93867648, 12008089.1411152, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21014, 75.5049305, 0.00065908, 91.50896533, 0.04474276, 9.15089653, 0.13152675, -75.5049305, -0.00065908, -91.50896533, -0.04474276, -9.15089653, -0.13152675, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11014, 86.53285415, 0.00065908, 104.8743691, 0.04474276, 10.48743691, 0.13152675, -86.53285415, -0.00065908, -104.8743691, -0.04474276, -10.48743691, -0.13152675, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21014, 1014, 0.0, 166.8189974, 0.01318157, 166.8189974, 0.0395447, 116.77329818, -3153.60549894, 0.05, 2, 0, 71014, 22014, 2, 3)
    ops.uniaxialMaterial('LimitState', 41014, 41.70474935, 0.00010547, 125.11424805, 0.0003164, 417.0474935, 0.00105467, -41.70474935, -0.00010547, -125.11424805, -0.0003164, -417.0474935, -0.00105467, 0.4, 0.3, 0.003, 0.0, 0.0, 21014, 2)
    ops.limitCurve('ThreePoint', 11014, 1014, 0.0, 166.8189974, 0.01318157, 166.8189974, 0.0395447, 116.77329818, -3153.60549894, 0.05, 2, 0, 71014, 22014, 1, 3)
    ops.uniaxialMaterial('LimitState', 31014, 41.70474935, 0.00010547, 125.11424805, 0.0003164, 417.0474935, 0.00105467, -41.70474935, -0.00010547, -125.11424805, -0.0003164, -417.0474935, -0.00105467, 0.4, 0.3, 0.003, 0.0, 0.0, 11014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1014, 99999, 'P', 41014, 'Vy', 31014, 'Vz', 21014, 'My', 11014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171014, 71014, 171014, 1014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122014, 122014, 22014, 1014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171015, 8.5, 11.0, 3.275)
    ops.node(122015, 8.5, 11.0, 6.025)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1015, 171015, 122015, 0.09, 29154531.46772906, 12147721.44488711, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21015, 54.17583608, 0.0007376, 65.55420304, 0.04733327, 6.5554203, 0.14489783, -54.17583608, -0.0007376, -65.55420304, -0.04733327, -6.5554203, -0.14489783, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11015, 60.04430114, 0.0007376, 72.65520189, 0.04733327, 7.26552019, 0.14489783, -60.04430114, -0.0007376, -72.65520189, -0.04733327, -7.26552019, -0.14489783, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21015, 1015, 0.0, 136.90133532, 0.01475195, 136.90133532, 0.04425586, 95.83093472, -2792.5984097, 0.05, 2, 0, 71015, 22015, 2, 3)
    ops.uniaxialMaterial('LimitState', 41015, 34.22533383, 0.00011645, 102.67600149, 0.00034936, 342.2533383, 0.00116454, -34.22533383, -0.00011645, -102.67600149, -0.00034936, -342.2533383, -0.00116454, 0.4, 0.3, 0.003, 0.0, 0.0, 21015, 2)
    ops.limitCurve('ThreePoint', 11015, 1015, 0.0, 136.90133532, 0.01475195, 136.90133532, 0.04425586, 95.83093472, -2792.5984097, 0.05, 2, 0, 71015, 22015, 1, 3)
    ops.uniaxialMaterial('LimitState', 31015, 34.22533383, 0.00011645, 102.67600149, 0.00034936, 342.2533383, 0.00116454, -34.22533383, -0.00011645, -102.67600149, -0.00034936, -342.2533383, -0.00116454, 0.4, 0.3, 0.003, 0.0, 0.0, 11015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1015, 99999, 'P', 41015, 'Vy', 31015, 'Vz', 21015, 'My', 11015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171015, 71015, 171015, 1015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122015, 122015, 22015, 1015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171016, 11.35, 11.0, 3.275)
    ops.node(122016, 11.35, 11.0, 6.025)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1016, 171016, 122016, 0.09, 29422481.4410108, 12259367.26708784, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21016, 55.2270916, 0.00073326, 66.79321552, 0.04708821, 6.67932155, 0.14538864, -55.2270916, -0.00073326, -66.79321552, -0.04708821, -6.67932155, -0.14538864, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11016, 61.44751273, 0.00073326, 74.31636978, 0.04708821, 7.43163698, 0.14538864, -61.44751273, -0.00073326, -74.31636978, -0.04708821, -7.43163698, -0.14538864, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21016, 1016, 0.0, 136.57991029, 0.01466528, 136.57991029, 0.04399585, 95.6059372, -2739.27602003, 0.05, 2, 0, 71016, 22016, 2, 3)
    ops.uniaxialMaterial('LimitState', 41016, 34.14497757, 0.00011512, 102.43493272, 0.00034537, 341.44977573, 0.00115122, -34.14497757, -0.00011512, -102.43493272, -0.00034537, -341.44977573, -0.00115122, 0.4, 0.3, 0.003, 0.0, 0.0, 21016, 2)
    ops.limitCurve('ThreePoint', 11016, 1016, 0.0, 136.57991029, 0.01466528, 136.57991029, 0.04399585, 95.6059372, -2739.27602003, 0.05, 2, 0, 71016, 22016, 1, 3)
    ops.uniaxialMaterial('LimitState', 31016, 34.14497757, 0.00011512, 102.43493272, 0.00034537, 341.44977573, 0.00115122, -34.14497757, -0.00011512, -102.43493272, -0.00034537, -341.44977573, -0.00115122, 0.4, 0.3, 0.003, 0.0, 0.0, 11016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1016, 99999, 'P', 41016, 'Vy', 31016, 'Vz', 21016, 'My', 11016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171016, 71016, 171016, 1016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122016, 122016, 22016, 1016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171017, 15.6, 11.0, 3.3)
    ops.node(122017, 15.6, 11.0, 6.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1017, 171017, 122017, 0.1225, 28763916.87455272, 11984965.36439697, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21017, 74.83304948, 0.00066851, 90.70364131, 0.04482623, 9.07036413, 0.13148179, -74.83304948, -0.00066851, -90.70364131, -0.04482623, -9.07036413, -0.13148179, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11017, 85.30903949, 0.00066851, 103.40137909, 0.04482623, 10.34013791, 0.13148179, -85.30903949, -0.00066851, -103.40137909, -0.04482623, -10.34013791, -0.13148179, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21017, 1017, 0.0, 166.71314656, 0.01337016, 166.71314656, 0.04011048, 116.69920259, -3158.33267057, 0.05, 2, 0, 71017, 22017, 2, 3)
    ops.uniaxialMaterial('LimitState', 41017, 41.67828664, 0.0001056, 125.03485992, 0.00031681, 416.78286639, 0.00105604, -41.67828664, -0.0001056, -125.03485992, -0.00031681, -416.78286639, -0.00105604, 0.4, 0.3, 0.003, 0.0, 0.0, 21017, 2)
    ops.limitCurve('ThreePoint', 11017, 1017, 0.0, 166.71314656, 0.01337016, 166.71314656, 0.04011048, 116.69920259, -3158.33267057, 0.05, 2, 0, 71017, 22017, 1, 3)
    ops.uniaxialMaterial('LimitState', 31017, 41.67828664, 0.0001056, 125.03485992, 0.00031681, 416.78286639, 0.00105604, -41.67828664, -0.0001056, -125.03485992, -0.00031681, -416.78286639, -0.00105604, 0.4, 0.3, 0.003, 0.0, 0.0, 11017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1017, 99999, 'P', 41017, 'Vy', 31017, 'Vz', 21017, 'My', 11017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171017, 71017, 171017, 1017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122017, 122017, 22017, 1017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171018, 19.85, 11.0, 3.375)
    ops.node(122018, 19.85, 11.0, 5.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1018, 171018, 122018, 0.09, 29813771.69456388, 12422404.87273495, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21018, 38.36225069, 0.00069033, 46.46124807, 0.03358225, 4.64612481, 0.10783578, -38.36225069, -0.00069033, -46.46124807, -0.03358225, -4.64612481, -0.10783578, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11018, 43.78859732, 0.00069033, 53.0331992, 0.03358225, 5.30331992, 0.10783578, -43.78859732, -0.00069033, -53.0331992, -0.03358225, -5.30331992, -0.10783578, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21018, 1018, 0.0, 108.22965827, 0.01380655, 108.22965827, 0.04141965, 75.76076079, -1749.39707259, 0.05, 2, 0, 71018, 22018, 2, 3)
    ops.uniaxialMaterial('LimitState', 41018, 27.05741457, 9.003e-05, 81.1722437, 0.00027009, 270.57414566, 0.00090029, -27.05741457, -9.003e-05, -81.1722437, -0.00027009, -270.57414566, -0.00090029, 0.4, 0.3, 0.003, 0.0, 0.0, 21018, 2)
    ops.limitCurve('ThreePoint', 11018, 1018, 0.0, 108.22965827, 0.01380655, 108.22965827, 0.04141965, 75.76076079, -1749.39707259, 0.05, 2, 0, 71018, 22018, 1, 3)
    ops.uniaxialMaterial('LimitState', 31018, 27.05741457, 9.003e-05, 81.1722437, 0.00027009, 270.57414566, 0.00090029, -27.05741457, -9.003e-05, -81.1722437, -0.00027009, -270.57414566, -0.00090029, 0.4, 0.3, 0.003, 0.0, 0.0, 11018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1018, 99999, 'P', 41018, 'Vy', 31018, 'Vz', 21018, 'My', 11018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171018, 71018, 171018, 1018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122018, 122018, 22018, 1018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172001, 0.0, 0.0, 6.475)
    ops.node(123001, 0.0, 0.0, 9.025)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2001, 172001, 123001, 0.0625, 29456380.08809245, 12273491.70337186, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22001, 23.17726671, 0.00078991, 28.1138763, 0.02314141, 2.81138763, 0.08064181, -23.17726671, -0.00078991, -28.1138763, -0.02314141, -2.81138763, -0.08064181, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12001, 25.28956802, 0.00078991, 30.67608428, 0.02314141, 3.06760843, 0.08064181, -25.28956802, -0.00078991, -30.67608428, -0.02314141, -3.06760843, -0.08064181, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22001, 2001, 0.0, 64.5867023, 0.01579822, 64.5867023, 0.04739466, 45.21069161, -853.27261167, 0.05, 2, 0, 72001, 23001, 2, 3)
    ops.uniaxialMaterial('LimitState', 42001, 16.14667558, 7.83e-05, 48.44002673, 0.00023491, 161.46675576, 0.00078303, -16.14667558, -7.83e-05, -48.44002673, -0.00023491, -161.46675576, -0.00078303, 0.4, 0.3, 0.003, 0.0, 0.0, 22001, 2)
    ops.limitCurve('ThreePoint', 12001, 2001, 0.0, 64.5867023, 0.01579822, 64.5867023, 0.04739466, 45.21069161, -853.27261167, 0.05, 2, 0, 72001, 23001, 1, 3)
    ops.uniaxialMaterial('LimitState', 32001, 16.14667558, 7.83e-05, 48.44002673, 0.00023491, 161.46675576, 0.00078303, -16.14667558, -7.83e-05, -48.44002673, -0.00023491, -161.46675576, -0.00078303, 0.4, 0.3, 0.003, 0.0, 0.0, 12001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2001, 99999, 'P', 42001, 'Vy', 32001, 'Vz', 22001, 'My', 12001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172001, 72001, 172001, 2001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123001, 123001, 23001, 2001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172002, 4.25, 0.0, 6.4)
    ops.node(123002, 4.25, 0.0, 9.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2002, 172002, 123002, 0.0625, 29505534.20344594, 12293972.58476914, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22002, 32.40558381, 0.00088554, 39.16458209, 0.03216011, 3.91645821, 0.09431395, -32.40558381, -0.00088554, -39.16458209, -0.03216011, -3.91645821, -0.09431395, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12002, 32.40558381, 0.00088554, 39.16458209, 0.03216011, 3.91645821, 0.09431395, -32.40558381, -0.00088554, -39.16458209, -0.03216011, -3.91645821, -0.09431395, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22002, 2002, 0.0, 74.82629916, 0.01771075, 74.82629916, 0.05313225, 52.37840941, -984.23242653, 0.05, 2, 0, 72002, 23002, 2, 3)
    ops.uniaxialMaterial('LimitState', 42002, 18.70657479, 9.057e-05, 56.11972437, 0.0002717, 187.0657479, 0.00090566, -18.70657479, -9.057e-05, -56.11972437, -0.0002717, -187.0657479, -0.00090566, 0.4, 0.3, 0.003, 0.0, 0.0, 22002, 2)
    ops.limitCurve('ThreePoint', 12002, 2002, 0.0, 74.82629916, 0.01771075, 74.82629916, 0.05313225, 52.37840941, -984.23242653, 0.05, 2, 0, 72002, 23002, 1, 3)
    ops.uniaxialMaterial('LimitState', 32002, 18.70657479, 9.057e-05, 56.11972437, 0.0002717, 187.0657479, 0.00090566, -18.70657479, -9.057e-05, -56.11972437, -0.0002717, -187.0657479, -0.00090566, 0.4, 0.3, 0.003, 0.0, 0.0, 12002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2002, 99999, 'P', 42002, 'Vy', 32002, 'Vz', 22002, 'My', 12002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172002, 72002, 172002, 2002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123002, 123002, 23002, 2002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172005, 15.6, 0.0, 6.4)
    ops.node(123005, 15.6, 0.0, 9.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2005, 172005, 123005, 0.0625, 29240689.8067724, 12183620.75282183, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22005, 32.5544168, 0.00087062, 39.36335202, 0.03179071, 3.9363352, 0.09345963, -32.5544168, -0.00087062, -39.36335202, -0.03179071, -3.9363352, -0.09345963, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12005, 32.5544168, 0.00087062, 39.36335202, 0.03179071, 3.9363352, 0.09345963, -32.5544168, -0.00087062, -39.36335202, -0.03179071, -3.9363352, -0.09345963, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22005, 2005, 0.0, 73.78120342, 0.01741239, 73.78120342, 0.05223717, 51.6468424, -965.10482858, 0.05, 2, 0, 72005, 23005, 2, 3)
    ops.uniaxialMaterial('LimitState', 42005, 18.44530086, 9.011e-05, 55.33590257, 0.00027033, 184.45300856, 0.0009011, -18.44530086, -9.011e-05, -55.33590257, -0.00027033, -184.45300856, -0.0009011, 0.4, 0.3, 0.003, 0.0, 0.0, 22005, 2)
    ops.limitCurve('ThreePoint', 12005, 2005, 0.0, 73.78120342, 0.01741239, 73.78120342, 0.05223717, 51.6468424, -965.10482858, 0.05, 2, 0, 72005, 23005, 1, 3)
    ops.uniaxialMaterial('LimitState', 32005, 18.44530086, 9.011e-05, 55.33590257, 0.00027033, 184.45300856, 0.0009011, -18.44530086, -9.011e-05, -55.33590257, -0.00027033, -184.45300856, -0.0009011, 0.4, 0.3, 0.003, 0.0, 0.0, 12005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2005, 99999, 'P', 42005, 'Vy', 32005, 'Vz', 22005, 'My', 12005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172005, 72005, 172005, 2005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123005, 123005, 23005, 2005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172006, 19.85, 0.0, 6.475)
    ops.node(123006, 19.85, 0.0, 9.025)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2006, 172006, 123006, 0.0625, 30227655.90669308, 12594856.62778878, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22006, 23.11419154, 0.00084061, 27.98627717, 0.02262729, 2.79862772, 0.08085405, -23.11419154, -0.00084061, -27.98627717, -0.02262729, -2.79862772, -0.08085405, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12006, 24.91877177, 0.00084061, 30.17123278, 0.02262729, 3.01712328, 0.08085405, -24.91877177, -0.00084061, -30.17123278, -0.02262729, -3.01712328, -0.08085405, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22006, 2006, 0.0, 65.4629717, 0.01681221, 65.4629717, 0.05043664, 45.82408019, -829.36093557, 0.05, 2, 0, 72006, 23006, 2, 3)
    ops.uniaxialMaterial('LimitState', 42006, 16.36574292, 7.734e-05, 49.09722877, 0.00023202, 163.65742924, 0.0007734, -16.36574292, -7.734e-05, -49.09722877, -0.00023202, -163.65742924, -0.0007734, 0.4, 0.3, 0.003, 0.0, 0.0, 22006, 2)
    ops.limitCurve('ThreePoint', 12006, 2006, 0.0, 65.4629717, 0.01681221, 65.4629717, 0.05043664, 45.82408019, -829.36093557, 0.05, 2, 0, 72006, 23006, 1, 3)
    ops.uniaxialMaterial('LimitState', 32006, 16.36574292, 7.734e-05, 49.09722877, 0.00023202, 163.65742924, 0.0007734, -16.36574292, -7.734e-05, -49.09722877, -0.00023202, -163.65742924, -0.0007734, 0.4, 0.3, 0.003, 0.0, 0.0, 12006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2006, 99999, 'P', 42006, 'Vy', 32006, 'Vz', 22006, 'My', 12006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172006, 72006, 172006, 2006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123006, 123006, 23006, 2006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172007, 0.0, 5.5, 6.475)
    ops.node(123007, 0.0, 5.5, 9.025)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2007, 172007, 123007, 0.0625, 29673107.50280973, 12363794.79283739, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22007, 24.97603606, 0.00082279, 30.16540612, 0.02119961, 3.01654061, 0.07270268, -24.97603606, -0.00082279, -30.16540612, -0.02119961, -3.01654061, -0.07270268, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12007, 24.97603606, 0.00082279, 30.16540612, 0.02119961, 3.01654061, 0.07270268, -24.97603606, -0.00082279, -30.16540612, -0.02119961, -3.01654061, -0.07270268, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22007, 2007, 0.0, 69.57987466, 0.01645573, 69.57987466, 0.04936719, 48.70591226, -784.50932895, 0.05, 2, 0, 72007, 23007, 2, 3)
    ops.uniaxialMaterial('LimitState', 42007, 17.39496866, 8.374e-05, 52.18490599, 0.00025122, 173.94968665, 0.0008374, -17.39496866, -8.374e-05, -52.18490599, -0.00025122, -173.94968665, -0.0008374, 0.4, 0.3, 0.003, 0.0, 0.0, 22007, 2)
    ops.limitCurve('ThreePoint', 12007, 2007, 0.0, 69.57987466, 0.01645573, 69.57987466, 0.04936719, 48.70591226, -784.50932895, 0.05, 2, 0, 72007, 23007, 1, 3)
    ops.uniaxialMaterial('LimitState', 32007, 17.39496866, 8.374e-05, 52.18490599, 0.00025122, 173.94968665, 0.0008374, -17.39496866, -8.374e-05, -52.18490599, -0.00025122, -173.94968665, -0.0008374, 0.4, 0.3, 0.003, 0.0, 0.0, 12007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2007, 99999, 'P', 42007, 'Vy', 32007, 'Vz', 22007, 'My', 12007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172007, 72007, 172007, 2007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123007, 123007, 23007, 2007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172008, 4.25, 5.5, 6.4)
    ops.node(123008, 4.25, 5.5, 9.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2008, 172008, 123008, 0.1225, 28635075.94096793, 11931281.64206997, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22008, 68.29823507, 0.00063877, 82.83453008, 0.0337992, 8.28345301, 0.0955364, -68.29823507, -0.00063877, -82.83453008, -0.0337992, -8.28345301, -0.0955364, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12008, 64.62560897, 0.00063877, 78.38023844, 0.0337992, 7.83802384, 0.0955364, -64.62560897, -0.00063877, -78.38023844, -0.0337992, -7.83802384, -0.0955364, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22008, 2008, 0.0, 135.25926673, 0.01277541, 135.25926673, 0.03832623, 94.68148671, -1857.84033046, 0.05, 2, 0, 72008, 23008, 2, 3)
    ops.uniaxialMaterial('LimitState', 42008, 33.81481668, 8.607e-05, 101.44445005, 0.0002582, 338.14816683, 0.00086065, -33.81481668, -8.607e-05, -101.44445005, -0.0002582, -338.14816683, -0.00086065, 0.4, 0.3, 0.003, 0.0, 0.0, 22008, 2)
    ops.limitCurve('ThreePoint', 12008, 2008, 0.0, 135.25926673, 0.01277541, 135.25926673, 0.03832623, 94.68148671, -1857.84033046, 0.05, 2, 0, 72008, 23008, 1, 3)
    ops.uniaxialMaterial('LimitState', 32008, 33.81481668, 8.607e-05, 101.44445005, 0.0002582, 338.14816683, 0.00086065, -33.81481668, -8.607e-05, -101.44445005, -0.0002582, -338.14816683, -0.00086065, 0.4, 0.3, 0.003, 0.0, 0.0, 12008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2008, 99999, 'P', 42008, 'Vy', 32008, 'Vz', 22008, 'My', 12008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172008, 72008, 172008, 2008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123008, 123008, 23008, 2008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172009, 8.5, 5.5, 6.4)
    ops.node(123009, 8.5, 5.5, 9.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2009, 172009, 123009, 0.1225, 29963530.92484351, 12484804.55201813, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22009, 68.45092945, 0.00063358, 82.80090814, 0.03366461, 8.28009081, 0.09739539, -68.45092945, -0.00063358, -82.80090814, -0.03366461, -8.28009081, -0.09739539, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12009, 64.80656304, 0.00063358, 78.39254071, 0.03366461, 7.83925407, 0.09739539, -64.80656304, -0.00063358, -78.39254071, -0.03366461, -7.83925407, -0.09739539, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22009, 2009, 0.0, 141.7892399, 0.01267155, 141.7892399, 0.03801464, 99.25246793, -1926.86392655, 0.05, 2, 0, 72009, 23009, 2, 3)
    ops.uniaxialMaterial('LimitState', 42009, 35.44730997, 8.622e-05, 106.34192992, 0.00025866, 354.47309974, 0.0008622, -35.44730997, -8.622e-05, -106.34192992, -0.00025866, -354.47309974, -0.0008622, 0.4, 0.3, 0.003, 0.0, 0.0, 22009, 2)
    ops.limitCurve('ThreePoint', 12009, 2009, 0.0, 141.7892399, 0.01267155, 141.7892399, 0.03801464, 99.25246793, -1926.86392655, 0.05, 2, 0, 72009, 23009, 1, 3)
    ops.uniaxialMaterial('LimitState', 32009, 35.44730997, 8.622e-05, 106.34192992, 0.00025866, 354.47309974, 0.0008622, -35.44730997, -8.622e-05, -106.34192992, -0.00025866, -354.47309974, -0.0008622, 0.4, 0.3, 0.003, 0.0, 0.0, 12009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2009, 99999, 'P', 42009, 'Vy', 32009, 'Vz', 22009, 'My', 12009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172009, 72009, 172009, 2009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123009, 123009, 23009, 2009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172010, 11.35, 5.5, 6.4)
    ops.node(123010, 11.35, 5.5, 9.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2010, 172010, 123010, 0.1225, 31136101.84242232, 12973375.76767597, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22010, 67.21167077, 0.00063347, 81.07165693, 0.03341702, 8.10716569, 0.09862734, -67.21167077, -0.00063347, -81.07165693, -0.03341702, -8.10716569, -0.09862734, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12010, 63.83302094, 0.00063347, 76.99628227, 0.03341702, 7.69962823, 0.09862734, -63.83302094, -0.00063347, -76.99628227, -0.03341702, -7.69962823, -0.09862734, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22010, 2010, 0.0, 145.59897426, 0.01266942, 145.59897426, 0.03800826, 101.91928198, -1903.79045842, 0.05, 2, 0, 72010, 23010, 2, 3)
    ops.uniaxialMaterial('LimitState', 42010, 36.39974356, 8.52e-05, 109.19923069, 0.00025561, 363.99743565, 0.00085202, -36.39974356, -8.52e-05, -109.19923069, -0.00025561, -363.99743565, -0.00085202, 0.4, 0.3, 0.003, 0.0, 0.0, 22010, 2)
    ops.limitCurve('ThreePoint', 12010, 2010, 0.0, 145.59897426, 0.01266942, 145.59897426, 0.03800826, 101.91928198, -1903.79045842, 0.05, 2, 0, 72010, 23010, 1, 3)
    ops.uniaxialMaterial('LimitState', 32010, 36.39974356, 8.52e-05, 109.19923069, 0.00025561, 363.99743565, 0.00085202, -36.39974356, -8.52e-05, -109.19923069, -0.00025561, -363.99743565, -0.00085202, 0.4, 0.3, 0.003, 0.0, 0.0, 12010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2010, 99999, 'P', 42010, 'Vy', 32010, 'Vz', 22010, 'My', 12010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172010, 72010, 172010, 2010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123010, 123010, 23010, 2010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172011, 15.6, 5.5, 6.4)
    ops.node(123011, 15.6, 5.5, 9.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2011, 172011, 123011, 0.1225, 29493935.56057769, 12289139.81690737, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22011, 67.17222648, 0.00063664, 81.33461332, 0.03409533, 8.13346133, 0.09713684, -67.17222648, -0.00063664, -81.33461332, -0.03409533, -8.13346133, -0.09713684, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12011, 63.71652657, 0.00063664, 77.1503242, 0.03409533, 7.71503242, 0.09713684, -63.71652657, -0.00063664, -77.1503242, -0.03409533, -7.71503242, -0.09713684, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22011, 2011, 0.0, 139.21107008, 0.01273272, 139.21107008, 0.03819817, 97.44774906, -1890.40446662, 0.05, 2, 0, 72011, 23011, 2, 3)
    ops.uniaxialMaterial('LimitState', 42011, 34.80276752, 8.6e-05, 104.40830256, 0.000258, 348.0276752, 0.00086, -34.80276752, -8.6e-05, -104.40830256, -0.000258, -348.0276752, -0.00086, 0.4, 0.3, 0.003, 0.0, 0.0, 22011, 2)
    ops.limitCurve('ThreePoint', 12011, 2011, 0.0, 139.21107008, 0.01273272, 139.21107008, 0.03819817, 97.44774906, -1890.40446662, 0.05, 2, 0, 72011, 23011, 1, 3)
    ops.uniaxialMaterial('LimitState', 32011, 34.80276752, 8.6e-05, 104.40830256, 0.000258, 348.0276752, 0.00086, -34.80276752, -8.6e-05, -104.40830256, -0.000258, -348.0276752, -0.00086, 0.4, 0.3, 0.003, 0.0, 0.0, 12011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2011, 99999, 'P', 42011, 'Vy', 32011, 'Vz', 22011, 'My', 12011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172011, 72011, 172011, 2011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123011, 123011, 23011, 2011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172012, 19.85, 5.5, 6.475)
    ops.node(123012, 19.85, 5.5, 9.025)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2012, 172012, 123012, 0.0625, 30597044.86677891, 12748768.69449121, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22012, 25.12039317, 0.00080768, 30.28226345, 0.02113124, 3.02822635, 0.07396331, -25.12039317, -0.00080768, -30.28226345, -0.02113124, -3.02822635, -0.07396331, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12012, 25.12039317, 0.00080768, 30.28226345, 0.02113124, 3.02822635, 0.07396331, -25.12039317, -0.00080768, -30.28226345, -0.02113124, -3.02822635, -0.07396331, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22012, 2012, 0.0, 71.20327874, 0.01615358, 71.20327874, 0.04846075, 49.84229512, -779.81193346, 0.05, 2, 0, 72012, 23012, 2, 3)
    ops.uniaxialMaterial('LimitState', 42012, 17.80081969, 8.311e-05, 53.40245906, 0.00024932, 178.00819685, 0.00083106, -17.80081969, -8.311e-05, -53.40245906, -0.00024932, -178.00819685, -0.00083106, 0.4, 0.3, 0.003, 0.0, 0.0, 22012, 2)
    ops.limitCurve('ThreePoint', 12012, 2012, 0.0, 71.20327874, 0.01615358, 71.20327874, 0.04846075, 49.84229512, -779.81193346, 0.05, 2, 0, 72012, 23012, 1, 3)
    ops.uniaxialMaterial('LimitState', 32012, 17.80081969, 8.311e-05, 53.40245906, 0.00024932, 178.00819685, 0.00083106, -17.80081969, -8.311e-05, -53.40245906, -0.00024932, -178.00819685, -0.00083106, 0.4, 0.3, 0.003, 0.0, 0.0, 12012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2012, 99999, 'P', 42012, 'Vy', 32012, 'Vz', 22012, 'My', 12012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172012, 72012, 172012, 2012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123012, 123012, 23012, 2012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172013, 0.0, 11.0, 6.475)
    ops.node(123013, 0.0, 11.0, 9.025)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2013, 172013, 123013, 0.0625, 29135056.63365114, 12139606.93068798, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22013, 23.22524835, 0.00080494, 28.19196825, 0.02338971, 2.81919683, 0.08056542, -23.22524835, -0.00080494, -28.19196825, -0.02338971, -2.81919683, -0.08056542, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12013, 25.29876782, 0.00080494, 30.70890991, 0.02338971, 3.07089099, 0.08056542, -25.29876782, -0.00080494, -30.70890991, -0.02338971, -3.07089099, -0.08056542, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22013, 2013, 0.0, 64.32624766, 0.01609875, 64.32624766, 0.04829626, 45.02837336, -867.55134336, 0.05, 2, 0, 72013, 23013, 2, 3)
    ops.uniaxialMaterial('LimitState', 42013, 16.08156192, 7.885e-05, 48.24468575, 0.00023654, 160.81561916, 0.00078847, -16.08156192, -7.885e-05, -48.24468575, -0.00023654, -160.81561916, -0.00078847, 0.4, 0.3, 0.003, 0.0, 0.0, 22013, 2)
    ops.limitCurve('ThreePoint', 12013, 2013, 0.0, 64.32624766, 0.01609875, 64.32624766, 0.04829626, 45.02837336, -867.55134336, 0.05, 2, 0, 72013, 23013, 1, 3)
    ops.uniaxialMaterial('LimitState', 32013, 16.08156192, 7.885e-05, 48.24468575, 0.00023654, 160.81561916, 0.00078847, -16.08156192, -7.885e-05, -48.24468575, -0.00023654, -160.81561916, -0.00078847, 0.4, 0.3, 0.003, 0.0, 0.0, 12013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2013, 99999, 'P', 42013, 'Vy', 32013, 'Vz', 22013, 'My', 12013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172013, 72013, 172013, 2013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123013, 123013, 23013, 2013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172014, 4.25, 11.0, 6.4)
    ops.node(123014, 4.25, 11.0, 9.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2014, 172014, 123014, 0.0625, 29643926.87312956, 12351636.19713732, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22014, 33.22550427, 0.00087762, 40.14503282, 0.03033944, 4.01450328, 0.09274072, -33.22550427, -0.00087762, -40.14503282, -0.03033944, -4.01450328, -0.09274072, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12014, 33.22550427, 0.00087762, 40.14503282, 0.03033944, 4.01450328, 0.09274072, -33.22550427, -0.00087762, -40.14503282, -0.03033944, -4.01450328, -0.09274072, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22014, 2014, 0.0, 74.12862417, 0.01755232, 74.12862417, 0.05265695, 51.89003692, -950.63552038, 0.05, 2, 0, 72014, 23014, 2, 3)
    ops.uniaxialMaterial('LimitState', 42014, 18.53215604, 8.93e-05, 55.59646812, 0.00026791, 185.32156041, 0.00089303, -18.53215604, -8.93e-05, -55.59646812, -0.00026791, -185.32156041, -0.00089303, 0.4, 0.3, 0.003, 0.0, 0.0, 22014, 2)
    ops.limitCurve('ThreePoint', 12014, 2014, 0.0, 74.12862417, 0.01755232, 74.12862417, 0.05265695, 51.89003692, -950.63552038, 0.05, 2, 0, 72014, 23014, 1, 3)
    ops.uniaxialMaterial('LimitState', 32014, 18.53215604, 8.93e-05, 55.59646812, 0.00026791, 185.32156041, 0.00089303, -18.53215604, -8.93e-05, -55.59646812, -0.00026791, -185.32156041, -0.00089303, 0.4, 0.3, 0.003, 0.0, 0.0, 12014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2014, 99999, 'P', 42014, 'Vy', 32014, 'Vz', 22014, 'My', 12014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172014, 72014, 172014, 2014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123014, 123014, 23014, 2014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172015, 8.5, 11.0, 6.375)
    ops.node(123015, 8.5, 11.0, 9.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2015, 172015, 123015, 0.0625, 29332768.68434987, 12221986.95181245, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22015, 30.71840725, 0.00087402, 37.19221293, 0.0311057, 3.71922129, 0.09573256, -30.71840725, -0.00087402, -37.19221293, -0.0311057, -3.71922129, -0.09573256, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12015, 30.71840725, 0.00087402, 37.19221293, 0.0311057, 3.71922129, 0.09573256, -30.71840725, -0.00087402, -37.19221293, -0.0311057, -3.71922129, -0.09573256, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22015, 2015, 0.0, 72.8487735, 0.01748031, 72.8487735, 0.05244093, 50.99414145, -1017.36126049, 0.05, 2, 0, 72015, 23015, 2, 3)
    ops.uniaxialMaterial('LimitState', 42015, 18.21219338, 8.869e-05, 54.63658013, 0.00026608, 182.12193376, 0.00088692, -18.21219338, -8.869e-05, -54.63658013, -0.00026608, -182.12193376, -0.00088692, 0.4, 0.3, 0.003, 0.0, 0.0, 22015, 2)
    ops.limitCurve('ThreePoint', 12015, 2015, 0.0, 72.8487735, 0.01748031, 72.8487735, 0.05244093, 50.99414145, -1017.36126049, 0.05, 2, 0, 72015, 23015, 1, 3)
    ops.uniaxialMaterial('LimitState', 32015, 18.21219338, 8.869e-05, 54.63658013, 0.00026608, 182.12193376, 0.00088692, -18.21219338, -8.869e-05, -54.63658013, -0.00026608, -182.12193376, -0.00088692, 0.4, 0.3, 0.003, 0.0, 0.0, 12015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2015, 99999, 'P', 42015, 'Vy', 32015, 'Vz', 22015, 'My', 12015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172015, 72015, 172015, 2015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123015, 123015, 23015, 2015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172016, 11.35, 11.0, 6.375)
    ops.node(123016, 11.35, 11.0, 9.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2016, 172016, 123016, 0.0625, 29353371.1610828, 12230571.31711783, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22016, 31.50106202, 0.00083379, 38.13826207, 0.0313158, 3.81382621, 0.09597557, -31.50106202, -0.00083379, -38.13826207, -0.0313158, -3.81382621, -0.09597557, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12016, 31.50106202, 0.00083379, 38.13826207, 0.0313158, 3.81382621, 0.09597557, -31.50106202, -0.00083379, -38.13826207, -0.0313158, -3.81382621, -0.09597557, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22016, 2016, 0.0, 72.84966059, 0.01667579, 72.84966059, 0.05002737, 50.99476241, -1015.88074808, 0.05, 2, 0, 72016, 23016, 2, 3)
    ops.uniaxialMaterial('LimitState', 42016, 18.21241515, 8.863e-05, 54.63724544, 0.00026589, 182.12415147, 0.00088631, -18.21241515, -8.863e-05, -54.63724544, -0.00026589, -182.12415147, -0.00088631, 0.4, 0.3, 0.003, 0.0, 0.0, 22016, 2)
    ops.limitCurve('ThreePoint', 12016, 2016, 0.0, 72.84966059, 0.01667579, 72.84966059, 0.05002737, 50.99476241, -1015.88074808, 0.05, 2, 0, 72016, 23016, 1, 3)
    ops.uniaxialMaterial('LimitState', 32016, 18.21241515, 8.863e-05, 54.63724544, 0.00026589, 182.12415147, 0.00088631, -18.21241515, -8.863e-05, -54.63724544, -0.00026589, -182.12415147, -0.00088631, 0.4, 0.3, 0.003, 0.0, 0.0, 12016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2016, 99999, 'P', 42016, 'Vy', 32016, 'Vz', 22016, 'My', 12016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172016, 72016, 172016, 2016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123016, 123016, 23016, 2016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172017, 15.6, 11.0, 6.4)
    ops.node(123017, 15.6, 11.0, 9.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2017, 172017, 123017, 0.0625, 30174667.91990622, 12572778.29996092, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22017, 33.60470139, 0.00085368, 40.55994384, 0.03069602, 4.05599438, 0.09400973, -33.60470139, -0.00085368, -40.55994384, -0.03069602, -4.05599438, -0.09400973, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12017, 33.60470139, 0.00085368, 40.55994384, 0.03069602, 4.05599438, 0.09400973, -33.60470139, -0.00085368, -40.55994384, -0.03069602, -4.05599438, -0.09400973, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22017, 2017, 0.0, 76.76472409, 0.01707366, 76.76472409, 0.05122099, 53.73530686, -1007.75650139, 0.05, 2, 0, 72017, 23017, 2, 3)
    ops.uniaxialMaterial('LimitState', 42017, 19.19118102, 9.085e-05, 57.57354306, 0.00027256, 191.91181022, 0.00090852, -19.19118102, -9.085e-05, -57.57354306, -0.00027256, -191.91181022, -0.00090852, 0.4, 0.3, 0.003, 0.0, 0.0, 22017, 2)
    ops.limitCurve('ThreePoint', 12017, 2017, 0.0, 76.76472409, 0.01707366, 76.76472409, 0.05122099, 53.73530686, -1007.75650139, 0.05, 2, 0, 72017, 23017, 1, 3)
    ops.uniaxialMaterial('LimitState', 32017, 19.19118102, 9.085e-05, 57.57354306, 0.00027256, 191.91181022, 0.00090852, -19.19118102, -9.085e-05, -57.57354306, -0.00027256, -191.91181022, -0.00090852, 0.4, 0.3, 0.003, 0.0, 0.0, 12017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2017, 99999, 'P', 42017, 'Vy', 32017, 'Vz', 22017, 'My', 12017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172017, 72017, 172017, 2017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123017, 123017, 23017, 2017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172018, 19.85, 11.0, 6.475)
    ops.node(123018, 19.85, 11.0, 9.025)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2018, 172018, 123018, 0.0625, 29573095.02816795, 12322122.92840331, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22018, 23.2861793, 0.00079862, 28.2385232, 0.02324781, 2.82385232, 0.08086283, -23.2861793, -0.00079862, -28.2385232, -0.02324781, -2.82385232, -0.08086283, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12018, 25.3820453, 0.00079862, 30.78012352, 0.02324781, 3.07801235, 0.08086283, -25.3820453, -0.00079862, -30.78012352, -0.02324781, -3.07801235, -0.08086283, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22018, 2018, 0.0, 64.57364807, 0.01597238, 64.57364807, 0.04791713, 45.20155365, -843.48393713, 0.05, 2, 0, 72018, 23018, 2, 3)
    ops.uniaxialMaterial('LimitState', 42018, 16.14341202, 7.798e-05, 48.43023605, 0.00023393, 161.43412017, 0.00077978, -16.14341202, -7.798e-05, -48.43023605, -0.00023393, -161.43412017, -0.00077978, 0.4, 0.3, 0.003, 0.0, 0.0, 22018, 2)
    ops.limitCurve('ThreePoint', 12018, 2018, 0.0, 64.57364807, 0.01597238, 64.57364807, 0.04791713, 45.20155365, -843.48393713, 0.05, 2, 0, 72018, 23018, 1, 3)
    ops.uniaxialMaterial('LimitState', 32018, 16.14341202, 7.798e-05, 48.43023605, 0.00023393, 161.43412017, 0.00077978, -16.14341202, -7.798e-05, -48.43023605, -0.00023393, -161.43412017, -0.00077978, 0.4, 0.3, 0.003, 0.0, 0.0, 12018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2018, 99999, 'P', 42018, 'Vy', 32018, 'Vz', 22018, 'My', 12018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172018, 72018, 172018, 2018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123018, 123018, 23018, 2018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173001, 0.0, 0.0, 9.575)
    ops.node(124001, 0.0, 0.0, 12.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3001, 173001, 124001, 0.0625, 31020624.39152125, 12925260.16313385, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23001, 14.54304018, 0.00071962, 17.62810639, 0.02266746, 1.76281064, 0.08742515, -14.54304018, -0.00071962, -17.62810639, -0.02266746, -1.76281064, -0.08742515, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13001, 14.54304018, 0.00071962, 17.62810639, 0.02266746, 1.76281064, 0.08742515, -14.54304018, -0.00071962, -17.62810639, -0.02266746, -1.76281064, -0.08742515, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23001, 3001, 0.0, 62.14733144, 0.01439235, 62.14733144, 0.04317705, 43.503132, -1729.09770772, 0.05, 2, 0, 73001, 24001, 2, 3)
    ops.uniaxialMaterial('LimitState', 43001, 15.53683286, 7.155e-05, 46.61049858, 0.00021464, 155.36832859, 0.00071546, -15.53683286, -7.155e-05, -46.61049858, -0.00021464, -155.36832859, -0.00071546, 0.4, 0.3, 0.003, 0.0, 0.0, 23001, 2)
    ops.limitCurve('ThreePoint', 13001, 3001, 0.0, 62.14733144, 0.01439235, 62.14733144, 0.04317705, 43.503132, -1729.09770772, 0.05, 2, 0, 73001, 24001, 1, 3)
    ops.uniaxialMaterial('LimitState', 33001, 15.53683286, 7.155e-05, 46.61049858, 0.00021464, 155.36832859, 0.00071546, -15.53683286, -7.155e-05, -46.61049858, -0.00021464, -155.36832859, -0.00071546, 0.4, 0.3, 0.003, 0.0, 0.0, 13001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3001, 99999, 'P', 43001, 'Vy', 33001, 'Vz', 23001, 'My', 13001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173001, 73001, 173001, 3001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124001, 124001, 24001, 3001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173002, 4.25, 0.0, 9.5)
    ops.node(124002, 4.25, 0.0, 12.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3002, 173002, 124002, 0.0625, 29592332.04092986, 12330138.35038744, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23002, 24.34408597, 0.00085031, 29.59379731, 0.04296862, 2.95937973, 0.13827212, -24.34408597, -0.00085031, -29.59379731, -0.04296862, -2.95937973, -0.13827212, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13002, 24.34408597, 0.00085031, 29.59379731, 0.04296862, 2.95937973, 0.13827212, -24.34408597, -0.00085031, -29.59379731, -0.04296862, -2.95937973, -0.13827212, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23002, 3002, 0.0, 77.5848996, 0.01700624, 77.5848996, 0.05101872, 54.30942972, -2536.03231063, 0.05, 2, 0, 73002, 24002, 2, 3)
    ops.uniaxialMaterial('LimitState', 43002, 19.3962249, 9.363e-05, 58.1886747, 0.00028089, 193.962249, 0.00093629, -19.3962249, -9.363e-05, -58.1886747, -0.00028089, -193.962249, -0.00093629, 0.4, 0.3, 0.003, 0.0, 0.0, 23002, 2)
    ops.limitCurve('ThreePoint', 13002, 3002, 0.0, 77.5848996, 0.01700624, 77.5848996, 0.05101872, 54.30942972, -2536.03231063, 0.05, 2, 0, 73002, 24002, 1, 3)
    ops.uniaxialMaterial('LimitState', 33002, 19.3962249, 9.363e-05, 58.1886747, 0.00028089, 193.962249, 0.00093629, -19.3962249, -9.363e-05, -58.1886747, -0.00028089, -193.962249, -0.00093629, 0.4, 0.3, 0.003, 0.0, 0.0, 13002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3002, 99999, 'P', 43002, 'Vy', 33002, 'Vz', 23002, 'My', 13002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173002, 73002, 173002, 3002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124002, 124002, 24002, 3002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173005, 15.6, 0.0, 9.5)
    ops.node(124005, 15.6, 0.0, 12.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3005, 173005, 124005, 0.0625, 28288363.00231304, 11786817.91763043, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23005, 25.17260413, 0.00080847, 30.69671866, 0.04404742, 3.06967187, 0.13819255, -25.17260413, -0.00080847, -30.69671866, -0.04404742, -3.06967187, -0.13819255, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13005, 25.17260413, 0.00080847, 30.69671866, 0.04404742, 3.06967187, 0.13819255, -25.17260413, -0.00080847, -30.69671866, -0.04404742, -3.06967187, -0.13819255, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23005, 3005, 0.0, 76.12748131, 0.01616946, 76.12748131, 0.04850838, 53.28923691, -2630.43169894, 0.05, 2, 0, 73005, 24005, 2, 3)
    ops.uniaxialMaterial('LimitState', 43005, 19.03187033, 9.611e-05, 57.09561098, 0.00028832, 190.31870326, 0.00096105, -19.03187033, -9.611e-05, -57.09561098, -0.00028832, -190.31870326, -0.00096105, 0.4, 0.3, 0.003, 0.0, 0.0, 23005, 2)
    ops.limitCurve('ThreePoint', 13005, 3005, 0.0, 76.12748131, 0.01616946, 76.12748131, 0.04850838, 53.28923691, -2630.43169894, 0.05, 2, 0, 73005, 24005, 1, 3)
    ops.uniaxialMaterial('LimitState', 33005, 19.03187033, 9.611e-05, 57.09561098, 0.00028832, 190.31870326, 0.00096105, -19.03187033, -9.611e-05, -57.09561098, -0.00028832, -190.31870326, -0.00096105, 0.4, 0.3, 0.003, 0.0, 0.0, 13005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3005, 99999, 'P', 43005, 'Vy', 33005, 'Vz', 23005, 'My', 13005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173005, 73005, 173005, 3005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124005, 124005, 24005, 3005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173006, 19.85, 0.0, 9.575)
    ops.node(124006, 19.85, 0.0, 12.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3006, 173006, 124006, 0.0625, 29193245.06808516, 12163852.11170215, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23006, 14.30491078, 0.00074242, 17.42954872, 0.02404542, 1.74295487, 0.08832249, -14.30491078, -0.00074242, -17.42954872, -0.02404542, -1.74295487, -0.08832249, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13006, 14.30491078, 0.00074242, 17.42954872, 0.02404542, 1.74295487, 0.08832249, -14.30491078, -0.00074242, -17.42954872, -0.02404542, -1.74295487, -0.08832249, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23006, 3006, 0.0, 59.83149041, 0.01484844, 59.83149041, 0.04454532, 41.88204328, -1858.4256157, 0.05, 2, 0, 73006, 24006, 2, 3)
    ops.uniaxialMaterial('LimitState', 43006, 14.9578726, 7.319e-05, 44.8736178, 0.00021957, 149.57872602, 0.00073192, -14.9578726, -7.319e-05, -44.8736178, -0.00021957, -149.57872602, -0.00073192, 0.4, 0.3, 0.003, 0.0, 0.0, 23006, 2)
    ops.limitCurve('ThreePoint', 13006, 3006, 0.0, 59.83149041, 0.01484844, 59.83149041, 0.04454532, 41.88204328, -1858.4256157, 0.05, 2, 0, 73006, 24006, 1, 3)
    ops.uniaxialMaterial('LimitState', 33006, 14.9578726, 7.319e-05, 44.8736178, 0.00021957, 149.57872602, 0.00073192, -14.9578726, -7.319e-05, -44.8736178, -0.00021957, -149.57872602, -0.00073192, 0.4, 0.3, 0.003, 0.0, 0.0, 13006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3006, 99999, 'P', 43006, 'Vy', 33006, 'Vz', 23006, 'My', 13006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173006, 73006, 173006, 3006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124006, 124006, 24006, 3006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173007, 0.0, 5.5, 9.575)
    ops.node(124007, 0.0, 5.5, 12.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3007, 173007, 124007, 0.0625, 30428713.35648407, 12678630.5652017, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23007, 16.24648867, 0.00075274, 19.70654976, 0.02285307, 1.97065498, 0.08542498, -16.24648867, -0.00075274, -19.70654976, -0.02285307, -1.97065498, -0.08542498, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13007, 16.24648867, 0.00075274, 19.70654976, 0.02285307, 1.97065498, 0.08542498, -16.24648867, -0.00075274, -19.70654976, -0.02285307, -1.97065498, -0.08542498, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23007, 3007, 0.0, 62.87521576, 0.01505476, 62.87521576, 0.04516429, 44.01265103, -1142.72767284, 0.05, 2, 0, 73007, 24007, 2, 3)
    ops.uniaxialMaterial('LimitState', 43007, 15.71880394, 7.379e-05, 47.15641182, 0.00022138, 157.1880394, 0.00073792, -15.71880394, -7.379e-05, -47.15641182, -0.00022138, -157.1880394, -0.00073792, 0.4, 0.3, 0.003, 0.0, 0.0, 23007, 2)
    ops.limitCurve('ThreePoint', 13007, 3007, 0.0, 62.87521576, 0.01505476, 62.87521576, 0.04516429, 44.01265103, -1142.72767284, 0.05, 2, 0, 73007, 24007, 1, 3)
    ops.uniaxialMaterial('LimitState', 33007, 15.71880394, 7.379e-05, 47.15641182, 0.00022138, 157.1880394, 0.00073792, -15.71880394, -7.379e-05, -47.15641182, -0.00022138, -157.1880394, -0.00073792, 0.4, 0.3, 0.003, 0.0, 0.0, 13007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3007, 99999, 'P', 43007, 'Vy', 33007, 'Vz', 23007, 'My', 13007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173007, 73007, 173007, 3007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124007, 124007, 24007, 3007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173008, 4.25, 5.5, 9.5)
    ops.node(124008, 4.25, 5.5, 12.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3008, 173008, 124008, 0.1225, 29284838.15243782, 12202015.89684909, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23008, 51.10817239, 0.0006205, 62.19725896, 0.02088892, 6.2197259, 0.06324005, -51.10817239, -0.0006205, -62.19725896, -0.02088892, -6.2197259, -0.06324005, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13008, 47.88015795, 0.0006205, 58.26885297, 0.02088892, 5.8268853, 0.06324005, -47.88015795, -0.0006205, -58.26885297, -0.02088892, -5.8268853, -0.06324005, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23008, 3008, 0.0, 98.18135968, 0.01240993, 98.18135968, 0.03722979, 68.72695178, -1086.57142582, 0.05, 2, 0, 73008, 24008, 2, 3)
    ops.uniaxialMaterial('LimitState', 43008, 24.54533992, 6.109e-05, 73.63601976, 0.00018326, 245.45339921, 0.00061086, -24.54533992, -6.109e-05, -73.63601976, -0.00018326, -245.45339921, -0.00061086, 0.4, 0.3, 0.003, 0.0, 0.0, 23008, 2)
    ops.limitCurve('ThreePoint', 13008, 3008, 0.0, 98.18135968, 0.01240993, 98.18135968, 0.03722979, 68.72695178, -1086.57142582, 0.05, 2, 0, 73008, 24008, 1, 3)
    ops.uniaxialMaterial('LimitState', 33008, 24.54533992, 6.109e-05, 73.63601976, 0.00018326, 245.45339921, 0.00061086, -24.54533992, -6.109e-05, -73.63601976, -0.00018326, -245.45339921, -0.00061086, 0.4, 0.3, 0.003, 0.0, 0.0, 13008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3008, 99999, 'P', 43008, 'Vy', 33008, 'Vz', 23008, 'My', 13008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173008, 73008, 173008, 3008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124008, 124008, 24008, 3008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173009, 8.5, 5.5, 9.475)
    ops.node(124009, 8.5, 5.5, 12.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3009, 173009, 124009, 0.1225, 27840061.29149565, 11600025.53812319, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23009, 51.69540994, 0.00060357, 63.10923702, 0.02164221, 6.3109237, 0.06316101, -51.69540994, -0.00060357, -63.10923702, -0.02164221, -6.3109237, -0.06316101, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13009, 48.26833271, 0.00060357, 58.92549557, 0.02164221, 5.89254956, 0.06316101, -48.26833271, -0.00060357, -58.92549557, -0.02164221, -5.89254956, -0.06316101, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23009, 3009, 0.0, 93.69580529, 0.01207137, 93.69580529, 0.0362141, 65.58706371, -1054.00432558, 0.05, 2, 0, 73009, 24009, 2, 3)
    ops.uniaxialMaterial('LimitState', 43009, 23.42395132, 6.132e-05, 70.27185397, 0.00018396, 234.23951324, 0.00061321, -23.42395132, -6.132e-05, -70.27185397, -0.00018396, -234.23951324, -0.00061321, 0.4, 0.3, 0.003, 0.0, 0.0, 23009, 2)
    ops.limitCurve('ThreePoint', 13009, 3009, 0.0, 93.69580529, 0.01207137, 93.69580529, 0.0362141, 65.58706371, -1054.00432558, 0.05, 2, 0, 73009, 24009, 1, 3)
    ops.uniaxialMaterial('LimitState', 33009, 23.42395132, 6.132e-05, 70.27185397, 0.00018396, 234.23951324, 0.00061321, -23.42395132, -6.132e-05, -70.27185397, -0.00018396, -234.23951324, -0.00061321, 0.4, 0.3, 0.003, 0.0, 0.0, 13009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3009, 99999, 'P', 43009, 'Vy', 33009, 'Vz', 23009, 'My', 13009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173009, 73009, 173009, 3009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124009, 124009, 24009, 3009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173010, 11.35, 5.5, 9.475)
    ops.node(124010, 11.35, 5.5, 12.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3010, 173010, 124010, 0.1225, 28895389.69429726, 12039745.70595719, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23010, 51.90393999, 0.00061126, 63.21300925, 0.02081412, 6.32130092, 0.06276435, -51.90393999, -0.00061126, -63.21300925, -0.02081412, -6.32130092, -0.06276435, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13010, 48.55998845, 0.00061126, 59.14046216, 0.02081412, 5.91404622, 0.06276435, -48.55998845, -0.00061126, -59.14046216, -0.02081412, -5.91404622, -0.06276435, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23010, 3010, 0.0, 96.90493707, 0.01222523, 96.90493707, 0.03667568, 67.83345595, -1030.66838685, 0.05, 2, 0, 73010, 24010, 2, 3)
    ops.uniaxialMaterial('LimitState', 43010, 24.22623427, 6.11e-05, 72.6787028, 0.00018331, 242.26234267, 0.00061105, -24.22623427, -6.11e-05, -72.6787028, -0.00018331, -242.26234267, -0.00061105, 0.4, 0.3, 0.003, 0.0, 0.0, 23010, 2)
    ops.limitCurve('ThreePoint', 13010, 3010, 0.0, 96.90493707, 0.01222523, 96.90493707, 0.03667568, 67.83345595, -1030.66838685, 0.05, 2, 0, 73010, 24010, 1, 3)
    ops.uniaxialMaterial('LimitState', 33010, 24.22623427, 6.11e-05, 72.6787028, 0.00018331, 242.26234267, 0.00061105, -24.22623427, -6.11e-05, -72.6787028, -0.00018331, -242.26234267, -0.00061105, 0.4, 0.3, 0.003, 0.0, 0.0, 13010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3010, 99999, 'P', 43010, 'Vy', 33010, 'Vz', 23010, 'My', 13010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173010, 73010, 173010, 3010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124010, 124010, 24010, 3010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173011, 15.6, 5.5, 9.5)
    ops.node(124011, 15.6, 5.5, 12.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3011, 173011, 124011, 0.1225, 28198308.26073333, 11749295.10863889, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23011, 50.86713169, 0.0006141, 62.06430321, 0.02111122, 6.20643032, 0.06307291, -50.86713169, -0.0006141, -62.06430321, -0.02111122, -6.20643032, -0.06307291, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13011, 47.56860076, 0.0006141, 58.0396803, 0.02111122, 5.80396803, 0.06307291, -47.56860076, -0.0006141, -58.0396803, -0.02111122, -5.80396803, -0.06307291, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23011, 3011, 0.0, 94.20152312, 0.01228205, 94.20152312, 0.03684615, 65.94106619, -1078.69829784, 0.05, 2, 0, 73011, 24011, 2, 3)
    ops.uniaxialMaterial('LimitState', 43011, 23.55038078, 6.087e-05, 70.65114234, 0.00018261, 235.50380781, 0.00060869, -23.55038078, -6.087e-05, -70.65114234, -0.00018261, -235.50380781, -0.00060869, 0.4, 0.3, 0.003, 0.0, 0.0, 23011, 2)
    ops.limitCurve('ThreePoint', 13011, 3011, 0.0, 94.20152312, 0.01228205, 94.20152312, 0.03684615, 65.94106619, -1078.69829784, 0.05, 2, 0, 73011, 24011, 1, 3)
    ops.uniaxialMaterial('LimitState', 33011, 23.55038078, 6.087e-05, 70.65114234, 0.00018261, 235.50380781, 0.00060869, -23.55038078, -6.087e-05, -70.65114234, -0.00018261, -235.50380781, -0.00060869, 0.4, 0.3, 0.003, 0.0, 0.0, 13011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3011, 99999, 'P', 43011, 'Vy', 33011, 'Vz', 23011, 'My', 13011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173011, 73011, 173011, 3011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124011, 124011, 24011, 3011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173012, 19.85, 5.5, 9.575)
    ops.node(124012, 19.85, 5.5, 12.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3012, 173012, 124012, 0.0625, 31794396.62053964, 13247665.25855818, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23012, 16.24765349, 0.00072718, 19.62785172, 0.02233115, 1.96278517, 0.0854811, -16.24765349, -0.00072718, -19.62785172, -0.02233115, -1.96278517, -0.0854811, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13012, 16.24765349, 0.00072718, 19.62785172, 0.02233115, 1.96278517, 0.0854811, -16.24765349, -0.00072718, -19.62785172, -0.02233115, -1.96278517, -0.0854811, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23012, 3012, 0.0, 65.16377988, 0.01454352, 65.16377988, 0.04363057, 45.61464592, -1121.78787295, 0.05, 2, 0, 73012, 24012, 2, 3)
    ops.uniaxialMaterial('LimitState', 43012, 16.29094497, 7.319e-05, 48.87283491, 0.00021958, 162.9094497, 0.00073193, -16.29094497, -7.319e-05, -48.87283491, -0.00021958, -162.9094497, -0.00073193, 0.4, 0.3, 0.003, 0.0, 0.0, 23012, 2)
    ops.limitCurve('ThreePoint', 13012, 3012, 0.0, 65.16377988, 0.01454352, 65.16377988, 0.04363057, 45.61464592, -1121.78787295, 0.05, 2, 0, 73012, 24012, 1, 3)
    ops.uniaxialMaterial('LimitState', 33012, 16.29094497, 7.319e-05, 48.87283491, 0.00021958, 162.9094497, 0.00073193, -16.29094497, -7.319e-05, -48.87283491, -0.00021958, -162.9094497, -0.00073193, 0.4, 0.3, 0.003, 0.0, 0.0, 13012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3012, 99999, 'P', 43012, 'Vy', 33012, 'Vz', 23012, 'My', 13012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173012, 73012, 173012, 3012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124012, 124012, 24012, 3012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173013, 0.0, 11.0, 9.575)
    ops.node(124013, 0.0, 11.0, 12.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3013, 173013, 124013, 0.0625, 31213971.14753272, 13005821.31147197, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23013, 14.54944995, 0.00074401, 17.62533959, 0.02821754, 1.76253396, 0.10599025, -14.54944995, -0.00074401, -17.62533959, -0.02821754, -1.76253396, -0.10599025, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13013, 14.54944995, 0.00074401, 17.62533959, 0.02821754, 1.76253396, 0.10599025, -14.54944995, -0.00074401, -17.62533959, -0.02821754, -1.76253396, -0.10599025, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23013, 3013, 0.0, 68.69309422, 0.01488016, 68.69309422, 0.04464048, 48.08516596, -2547.61707263, 0.05, 2, 0, 73013, 24013, 2, 3)
    ops.uniaxialMaterial('LimitState', 43013, 17.17327356, 7.859e-05, 51.51982067, 0.00023578, 171.73273556, 0.00078592, -17.17327356, -7.859e-05, -51.51982067, -0.00023578, -171.73273556, -0.00078592, 0.4, 0.3, 0.003, 0.0, 0.0, 23013, 2)
    ops.limitCurve('ThreePoint', 13013, 3013, 0.0, 68.69309422, 0.01488016, 68.69309422, 0.04464048, 48.08516596, -2547.61707263, 0.05, 2, 0, 73013, 24013, 1, 3)
    ops.uniaxialMaterial('LimitState', 33013, 17.17327356, 7.859e-05, 51.51982067, 0.00023578, 171.73273556, 0.00078592, -17.17327356, -7.859e-05, -51.51982067, -0.00023578, -171.73273556, -0.00078592, 0.4, 0.3, 0.003, 0.0, 0.0, 13013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3013, 99999, 'P', 43013, 'Vy', 33013, 'Vz', 23013, 'My', 13013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173013, 73013, 173013, 3013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124013, 124013, 24013, 3013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173014, 4.25, 11.0, 9.5)
    ops.node(124014, 4.25, 11.0, 12.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3014, 173014, 124014, 0.0625, 30248916.66944319, 12603715.27893466, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23014, 28.55817056, 0.00082542, 34.65612947, 0.04196334, 3.46561295, 0.1377754, -28.55817056, -0.00082542, -34.65612947, -0.04196334, -3.46561295, -0.1377754, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13014, 30.56706123, 0.00082542, 37.09397382, 0.04196334, 3.70939738, 0.1377754, -30.56706123, -0.00082542, -37.09397382, -0.04196334, -3.70939738, -0.1377754, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23014, 3014, 0.0, 78.85403454, 0.01650847, 78.85403454, 0.04952542, 55.19782418, -2541.8939892, 0.05, 2, 0, 73014, 24014, 2, 3)
    ops.uniaxialMaterial('LimitState', 43014, 19.71350864, 9.31e-05, 59.14052591, 0.00027929, 197.13508636, 0.00093095, -19.71350864, -9.31e-05, -59.14052591, -0.00027929, -197.13508636, -0.00093095, 0.4, 0.3, 0.003, 0.0, 0.0, 23014, 2)
    ops.limitCurve('ThreePoint', 13014, 3014, 0.0, 78.85403454, 0.01650847, 78.85403454, 0.04952542, 55.19782418, -2541.8939892, 0.05, 2, 0, 73014, 24014, 1, 3)
    ops.uniaxialMaterial('LimitState', 33014, 19.71350864, 9.31e-05, 59.14052591, 0.00027929, 197.13508636, 0.00093095, -19.71350864, -9.31e-05, -59.14052591, -0.00027929, -197.13508636, -0.00093095, 0.4, 0.3, 0.003, 0.0, 0.0, 13014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3014, 99999, 'P', 43014, 'Vy', 33014, 'Vz', 23014, 'My', 13014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173014, 73014, 173014, 3014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124014, 124014, 24014, 3014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173015, 8.5, 11.0, 9.475)
    ops.node(124015, 8.5, 11.0, 12.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3015, 173015, 124015, 0.0625, 29723133.21736702, 12384638.84056959, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23015, 23.7971459, 0.00081007, 28.93229164, 0.04183066, 2.89322916, 0.13854236, -23.7971459, -0.00081007, -28.93229164, -0.04183066, -2.89322916, -0.13854236, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13015, 23.7971459, 0.00081007, 28.93229164, 0.04183066, 2.89322916, 0.13854236, -23.7971459, -0.00081007, -28.93229164, -0.04183066, -2.89322916, -0.13854236, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23015, 3015, 0.0, 78.1112508, 0.01620133, 78.1112508, 0.048604, 54.67787556, -3052.30251337, 0.05, 2, 0, 73015, 24015, 2, 3)
    ops.uniaxialMaterial('LimitState', 43015, 19.5278127, 9.385e-05, 58.5834381, 0.00028155, 195.278127, 0.0009385, -19.5278127, -9.385e-05, -58.5834381, -0.00028155, -195.278127, -0.0009385, 0.4, 0.3, 0.003, 0.0, 0.0, 23015, 2)
    ops.limitCurve('ThreePoint', 13015, 3015, 0.0, 78.1112508, 0.01620133, 78.1112508, 0.048604, 54.67787556, -3052.30251337, 0.05, 2, 0, 73015, 24015, 1, 3)
    ops.uniaxialMaterial('LimitState', 33015, 19.5278127, 9.385e-05, 58.5834381, 0.00028155, 195.278127, 0.0009385, -19.5278127, -9.385e-05, -58.5834381, -0.00028155, -195.278127, -0.0009385, 0.4, 0.3, 0.003, 0.0, 0.0, 13015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3015, 99999, 'P', 43015, 'Vy', 33015, 'Vz', 23015, 'My', 13015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173015, 73015, 173015, 3015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124015, 124015, 24015, 3015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173016, 11.35, 11.0, 9.475)
    ops.node(124016, 11.35, 11.0, 12.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3016, 173016, 124016, 0.0625, 30140039.15801616, 12558349.6491734, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23016, 24.44272052, 0.00080142, 29.68362912, 0.04156799, 2.96836291, 0.13854674, -24.44272052, -0.00080142, -29.68362912, -0.04156799, -2.96836291, -0.13854674, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13016, 24.44272052, 0.00080142, 29.68362912, 0.04156799, 2.96836291, 0.13854674, -24.44272052, -0.00080142, -29.68362912, -0.04156799, -2.96836291, -0.13854674, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23016, 3016, 0.0, 79.58745205, 0.01602837, 79.58745205, 0.0480851, 55.71121643, -3142.17405506, 0.05, 2, 0, 73016, 24016, 2, 3)
    ops.uniaxialMaterial('LimitState', 43016, 19.89686301, 9.43e-05, 59.69058904, 0.0002829, 198.96863012, 0.00094301, -19.89686301, -9.43e-05, -59.69058904, -0.0002829, -198.96863012, -0.00094301, 0.4, 0.3, 0.003, 0.0, 0.0, 23016, 2)
    ops.limitCurve('ThreePoint', 13016, 3016, 0.0, 79.58745205, 0.01602837, 79.58745205, 0.0480851, 55.71121643, -3142.17405506, 0.05, 2, 0, 73016, 24016, 1, 3)
    ops.uniaxialMaterial('LimitState', 33016, 19.89686301, 9.43e-05, 59.69058904, 0.0002829, 198.96863012, 0.00094301, -19.89686301, -9.43e-05, -59.69058904, -0.0002829, -198.96863012, -0.00094301, 0.4, 0.3, 0.003, 0.0, 0.0, 13016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3016, 99999, 'P', 43016, 'Vy', 33016, 'Vz', 23016, 'My', 13016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173016, 73016, 173016, 3016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124016, 124016, 24016, 3016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173017, 15.6, 11.0, 9.5)
    ops.node(124017, 15.6, 11.0, 12.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3017, 173017, 124017, 0.0625, 28658988.31722701, 11941245.13217792, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23017, 28.54220423, 0.0008249, 34.77648417, 0.04322601, 3.47764842, 0.13772228, -28.54220423, -0.0008249, -34.77648417, -0.04322601, -3.47764842, -0.13772228, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13017, 30.62599711, 0.0008249, 37.31542579, 0.04322601, 3.73154258, 0.13772228, -30.62599711, -0.0008249, -37.31542579, -0.04322601, -3.73154258, -0.13772228, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23017, 3017, 0.0, 76.77996489, 0.01649807, 76.77996489, 0.0494942, 53.74597542, -2629.33157055, 0.05, 2, 0, 73017, 24017, 2, 3)
    ops.uniaxialMaterial('LimitState', 43017, 19.19499122, 9.568e-05, 57.58497367, 0.00028703, 191.94991223, 0.00095676, -19.19499122, -9.568e-05, -57.58497367, -0.00028703, -191.94991223, -0.00095676, 0.4, 0.3, 0.003, 0.0, 0.0, 23017, 2)
    ops.limitCurve('ThreePoint', 13017, 3017, 0.0, 76.77996489, 0.01649807, 76.77996489, 0.0494942, 53.74597542, -2629.33157055, 0.05, 2, 0, 73017, 24017, 1, 3)
    ops.uniaxialMaterial('LimitState', 33017, 19.19499122, 9.568e-05, 57.58497367, 0.00028703, 191.94991223, 0.00095676, -19.19499122, -9.568e-05, -57.58497367, -0.00028703, -191.94991223, -0.00095676, 0.4, 0.3, 0.003, 0.0, 0.0, 13017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3017, 99999, 'P', 43017, 'Vy', 33017, 'Vz', 23017, 'My', 13017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173017, 73017, 173017, 3017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124017, 124017, 24017, 3017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173018, 19.85, 11.0, 9.575)
    ops.node(124018, 19.85, 11.0, 12.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3018, 173018, 124018, 0.0625, 29015982.99376784, 12089992.91406994, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23018, 14.39744893, 0.00073349, 17.55034835, 0.02937675, 1.75503483, 0.10645541, -14.39744893, -0.00073349, -17.55034835, -0.02937675, -1.75503483, -0.10645541, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13018, 14.39744893, 0.00073349, 17.55034835, 0.02937675, 1.75503483, 0.10645541, -14.39744893, -0.00073349, -17.55034835, -0.02937675, -1.75503483, -0.10645541, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23018, 3018, 0.0, 64.24218593, 0.01466989, 64.24218593, 0.04400967, 44.96953015, -2491.57895727, 0.05, 2, 0, 73018, 24018, 2, 3)
    ops.uniaxialMaterial('LimitState', 43018, 16.06054648, 7.907e-05, 48.18163945, 0.0002372, 160.60546484, 0.00079067, -16.06054648, -7.907e-05, -48.18163945, -0.0002372, -160.60546484, -0.00079067, 0.4, 0.3, 0.003, 0.0, 0.0, 23018, 2)
    ops.limitCurve('ThreePoint', 13018, 3018, 0.0, 64.24218593, 0.01466989, 64.24218593, 0.04400967, 44.96953015, -2491.57895727, 0.05, 2, 0, 73018, 24018, 1, 3)
    ops.uniaxialMaterial('LimitState', 33018, 16.06054648, 7.907e-05, 48.18163945, 0.0002372, 160.60546484, 0.00079067, -16.06054648, -7.907e-05, -48.18163945, -0.0002372, -160.60546484, -0.00079067, 0.4, 0.3, 0.003, 0.0, 0.0, 13018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3018, 99999, 'P', 43018, 'Vy', 33018, 'Vz', 23018, 'My', 13018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173018, 73018, 173018, 3018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124018, 124018, 24018, 3018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170003, 8.5, 0.0, 0.0)
    ops.node(124019, 8.5, 0.0, 1.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4046, 170003, 124019, 0.1225, 29547375.95342891, 12311406.64726205, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24046, 115.42713133, 0.00053302, 139.20927952, 0.05142484, 13.92092795, 0.15142484, -115.42713133, -0.00053302, -139.20927952, -0.05142484, -13.92092795, -0.15142484, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14046, 107.61458658, 0.00053302, 129.78706904, 0.04413057, 12.9787069, 0.12375445, -107.61458658, -0.00053302, -129.78706904, -0.04413057, -12.9787069, -0.12375445, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24046, 4046, 0.0, 215.65404305, 0.01066048, 215.65404305, 0.03198143, 150.95783013, -5543.6158493, 0.05, 2, 0, 70003, 24019, 2, 3)
    ops.uniaxialMaterial('LimitState', 44046, 53.91351076, 6.649e-05, 161.74053229, 0.00019947, 539.13510762, 0.00066492, -53.91351076, -6.649e-05, -161.74053229, -0.00019947, -539.13510762, -0.00066492, 0.4, 0.3, 0.003, 0.0, 0.0, 24046, 2)
    ops.limitCurve('ThreePoint', 14046, 4046, 0.0, 259.73728742, 0.01066048, 259.73728742, 0.03198143, 181.81610119, -9405.74099841, 0.05, 2, 0, 70003, 24019, 1, 3)
    ops.uniaxialMaterial('LimitState', 34046, 64.93432185, 8.008e-05, 194.80296556, 0.00024025, 649.34321855, 0.00080084, -64.93432185, -8.008e-05, -194.80296556, -0.00024025, -649.34321855, -0.00080084, 0.4, 0.3, 0.003, 0.0, 0.0, 14046, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4046, 99999, 'P', 44046, 'Vy', 34046, 'Vz', 24046, 'My', 14046, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170003, 70003, 170003, 4046, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124019, 124019, 24019, 4046, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174019, 8.5, 0.0, 1.8)
    ops.node(121003, 8.5, 0.0, 2.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4047, 174019, 121003, 0.1225, 29170535.41267037, 12154389.75527932, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24047, 76.69384215, 0.0005277, 92.64950486, 0.04873597, 9.26495049, 0.14873597, -76.69384215, -0.0005277, -92.64950486, -0.04873597, -9.26495049, -0.14873597, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14047, 73.25941066, 0.0005277, 88.50056189, 0.04182633, 8.85005619, 0.12290499, -73.25941066, -0.0005277, -88.50056189, -0.04182633, -8.85005619, -0.12290499, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24047, 4047, 0.0, 211.10156057, 0.01055396, 211.10156057, 0.03166189, 147.7710924, -5718.48296789, 0.05, 2, 0, 74019, 21003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44047, 52.77539014, 6.593e-05, 158.32617043, 0.00019779, 527.75390142, 0.00065929, -52.77539014, -6.593e-05, -158.32617043, -0.00019779, -527.75390142, -0.00065929, 0.4, 0.3, 0.003, 0.0, 0.0, 24047, 2)
    ops.limitCurve('ThreePoint', 14047, 4047, 0.0, 255.43711886, 0.01055396, 255.43711886, 0.03166189, 178.8059832, -9892.4124589, 0.05, 2, 0, 74019, 21003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34047, 63.85927971, 7.978e-05, 191.57783914, 0.00023933, 638.59279714, 0.00079775, -63.85927971, -7.978e-05, -191.57783914, -0.00023933, -638.59279714, -0.00079775, 0.4, 0.3, 0.003, 0.0, 0.0, 14047, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4047, 99999, 'P', 44047, 'Vy', 34047, 'Vz', 24047, 'My', 14047, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174019, 74019, 174019, 4047, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121003, 121003, 21003, 4047, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170004, 11.35, 0.0, 0.0)
    ops.node(124020, 11.35, 0.0, 1.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4048, 170004, 124020, 0.1225, 28037298.35132778, 11682207.64638657, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24048, 114.508413, 0.00055044, 138.38044315, 0.05111963, 13.83804432, 0.15111963, -114.508413, -0.00055044, -138.38044315, -0.05111963, -13.83804432, -0.15111963, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14048, 106.92102767, 0.00055044, 129.21128505, 0.0438716, 12.9211285, 0.11883191, -106.92102767, -0.00055044, -129.21128505, -0.0438716, -12.9211285, -0.11883191, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24048, 4048, 0.0, 207.06281797, 0.01100879, 207.06281797, 0.03302638, 144.94397258, -5507.4434239, 0.05, 2, 0, 70004, 24020, 2, 3)
    ops.uniaxialMaterial('LimitState', 44048, 51.76570449, 6.728e-05, 155.29711348, 0.00020184, 517.65704492, 0.00067281, -51.76570449, -6.728e-05, -155.29711348, -0.00020184, -517.65704492, -0.00067281, 0.4, 0.3, 0.003, 0.0, 0.0, 24048, 2)
    ops.limitCurve('ThreePoint', 14048, 4048, 0.0, 250.9080019, 0.01100879, 250.9080019, 0.03302638, 175.63560133, -9335.08303981, 0.05, 2, 0, 70004, 24020, 1, 3)
    ops.uniaxialMaterial('LimitState', 34048, 62.72700047, 8.153e-05, 188.18100142, 0.00024458, 627.27000474, 0.00081528, -62.72700047, -8.153e-05, -188.18100142, -0.00024458, -627.27000474, -0.00081528, 0.4, 0.3, 0.003, 0.0, 0.0, 14048, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4048, 99999, 'P', 44048, 'Vy', 34048, 'Vz', 24048, 'My', 14048, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170004, 70004, 170004, 4048, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124020, 124020, 24020, 4048, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174020, 11.35, 0.0, 1.8)
    ops.node(121004, 11.35, 0.0, 2.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4049, 174020, 121004, 0.1225, 31434178.94242973, 13097574.55934572, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24049, 78.57852848, 0.00051522, 94.4877818, 0.04801585, 9.44877818, 0.14801585, -78.57852848, -0.00051522, -94.4877818, -0.04801585, -9.44877818, -0.14801585, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14049, 74.91452268, 0.00051522, 90.08194998, 0.04120764, 9.008195, 0.12778847, -74.91452268, -0.00051522, -90.08194998, -0.04120764, -9.008195, -0.12778847, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24049, 4049, 0.0, 223.38792003, 0.0103045, 223.38792003, 0.03091349, 156.37154402, -5707.97299063, 0.05, 2, 0, 74020, 21004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44049, 55.84698001, 6.474e-05, 167.54094002, 0.00019423, 558.46980008, 0.00064742, -55.84698001, -6.474e-05, -167.54094002, -0.00019423, -558.46980008, -0.00064742, 0.4, 0.3, 0.003, 0.0, 0.0, 24049, 2)
    ops.limitCurve('ThreePoint', 14049, 4049, 0.0, 267.65883141, 0.0103045, 267.65883141, 0.03091349, 187.36118199, -9871.67881324, 0.05, 2, 0, 74020, 21004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34049, 66.91470785, 7.757e-05, 200.74412356, 0.00023272, 669.14707852, 0.00077572, -66.91470785, -7.757e-05, -200.74412356, -0.00023272, -669.14707852, -0.00077572, 0.4, 0.3, 0.003, 0.0, 0.0, 14049, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4049, 99999, 'P', 44049, 'Vy', 34049, 'Vz', 24049, 'My', 14049, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174020, 74020, 174020, 4049, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121004, 121004, 21004, 4049, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171003, 8.5, 0.0, 3.275)
    ops.node(124021, 8.5, 0.0, 4.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4051, 171003, 124021, 0.1225, 29363664.02316358, 12234860.00965149, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24051, 70.95048256, 0.00051192, 85.83907511, 0.05012403, 8.58390751, 0.15012403, -70.95048256, -0.00051192, -85.83907511, -0.05012403, -8.58390751, -0.15012403, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14051, 67.41847734, 0.00051192, 81.56589683, 0.04301319, 8.15658968, 0.12914211, -67.41847734, -0.00051192, -81.56589683, -0.04301319, -8.15658968, -0.12914211, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24051, 4051, 0.0, 209.79237544, 0.0102385, 209.79237544, 0.03071549, 146.85466281, -6377.55598305, 0.05, 2, 0, 71003, 24021, 2, 3)
    ops.uniaxialMaterial('LimitState', 44051, 52.44809386, 6.509e-05, 157.34428158, 0.00019527, 524.4809386, 0.00065089, -52.44809386, -6.509e-05, -157.34428158, -0.00019527, -524.4809386, -0.00065089, 0.4, 0.3, 0.003, 0.0, 0.0, 24051, 2)
    ops.limitCurve('ThreePoint', 14051, 4051, 0.0, 255.65294452, 0.0102385, 255.65294452, 0.03071549, 178.95706116, -11487.33187417, 0.05, 2, 0, 71003, 24021, 1, 3)
    ops.uniaxialMaterial('LimitState', 34051, 63.91323613, 7.932e-05, 191.73970839, 0.00023795, 639.1323613, 0.00079317, -63.91323613, -7.932e-05, -191.73970839, -0.00023795, -639.1323613, -0.00079317, 0.4, 0.3, 0.003, 0.0, 0.0, 14051, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4051, 99999, 'P', 44051, 'Vy', 34051, 'Vz', 24051, 'My', 14051, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171003, 71003, 171003, 4051, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124021, 124021, 24021, 4051, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174021, 8.5, 0.0, 4.9)
    ops.node(122003, 8.5, 0.0, 6.025)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4052, 174021, 122003, 0.1225, 29502791.1085671, 12292829.62856962, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24052, 68.57507142, 0.000509, 83.02854615, 0.05054717, 8.30285461, 0.15054717, -68.57507142, -0.000509, -83.02854615, -0.05054717, -8.30285461, -0.15054717, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14052, 64.91290142, 0.000509, 78.59450555, 0.04337525, 7.85945055, 0.13252221, -64.91290142, -0.000509, -78.59450555, -0.04337525, -7.85945055, -0.13252221, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24052, 4052, 0.0, 204.05604369, 0.01017994, 204.05604369, 0.03053983, 142.83923059, -6410.85370983, 0.05, 2, 0, 74021, 22003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44052, 51.01401092, 6.301e-05, 153.04203277, 0.00018903, 510.14010924, 0.00063011, -51.01401092, -6.301e-05, -153.04203277, -0.00018903, -510.14010924, -0.00063011, 0.4, 0.3, 0.003, 0.0, 0.0, 24052, 2)
    ops.limitCurve('ThreePoint', 14052, 4052, 0.0, 248.30006116, 0.01017994, 248.30006116, 0.03053983, 173.81004282, -11739.7067952, 0.05, 2, 0, 74021, 22003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34052, 62.07501529, 7.667e-05, 186.22504587, 0.00023002, 620.75015291, 0.00076673, -62.07501529, -7.667e-05, -186.22504587, -0.00023002, -620.75015291, -0.00076673, 0.4, 0.3, 0.003, 0.0, 0.0, 14052, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4052, 99999, 'P', 44052, 'Vy', 34052, 'Vz', 24052, 'My', 14052, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174021, 74021, 174021, 4052, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122003, 122003, 22003, 4052, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171004, 11.35, 0.0, 3.275)
    ops.node(124022, 11.35, 0.0, 4.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4053, 171004, 124022, 0.1225, 29091600.08226525, 12121500.03427719, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24053, 70.7731585, 0.00051446, 85.66765637, 0.05016681, 8.56676564, 0.15016681, -70.7731585, -0.00051446, -85.66765637, -0.05016681, -8.56676564, -0.15016681, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14053, 67.27410311, 0.00051446, 81.4322106, 0.04305019, 8.14322106, 0.12853734, -67.27410311, -0.00051446, -81.4322106, -0.04305019, -8.14322106, -0.12853734, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24053, 4053, 0.0, 206.8425842, 0.01028912, 206.8425842, 0.03086735, 144.78980894, -6235.11939862, 0.05, 2, 0, 71004, 24022, 2, 3)
    ops.uniaxialMaterial('LimitState', 44053, 51.71064605, 6.477e-05, 155.13193815, 0.00019432, 517.1064605, 0.00064774, -51.71064605, -6.477e-05, -155.13193815, -0.00019432, -517.1064605, -0.00064774, 0.4, 0.3, 0.003, 0.0, 0.0, 24053, 2)
    ops.limitCurve('ThreePoint', 14053, 4053, 0.0, 251.95040696, 0.01028912, 251.95040696, 0.03086735, 176.36528487, -11200.77777826, 0.05, 2, 0, 71004, 24022, 1, 3)
    ops.uniaxialMaterial('LimitState', 34053, 62.98760174, 7.89e-05, 188.96280522, 0.0002367, 629.8760174, 0.000789, -62.98760174, -7.89e-05, -188.96280522, -0.0002367, -629.8760174, -0.000789, 0.4, 0.3, 0.003, 0.0, 0.0, 14053, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4053, 99999, 'P', 44053, 'Vy', 34053, 'Vz', 24053, 'My', 14053, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171004, 71004, 171004, 4053, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124022, 124022, 24022, 4053, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174022, 11.35, 0.0, 4.9)
    ops.node(122004, 11.35, 0.0, 6.025)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4054, 174022, 122004, 0.1225, 28929448.73600231, 12053936.9733343, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24054, 66.94876892, 0.0005132, 81.15096763, 0.05100436, 8.11509676, 0.15100436, -66.94876892, -0.0005132, -81.15096763, -0.05100436, -8.11509676, -0.15100436, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14054, 63.53524565, 0.0005132, 77.0133155, 0.04376752, 7.70133155, 0.13170012, -63.53524565, -0.0005132, -77.0133155, -0.04376752, -7.70133155, -0.13170012, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24054, 4054, 0.0, 201.31403148, 0.01026409, 201.31403148, 0.03079226, 140.91982203, -6439.54642108, 0.05, 2, 0, 74022, 22004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44054, 50.32850787, 6.34e-05, 150.98552361, 0.00019019, 503.28507869, 0.00063396, -50.32850787, -6.34e-05, -150.98552361, -0.00019019, -503.28507869, -0.00063396, 0.4, 0.3, 0.003, 0.0, 0.0, 24054, 2)
    ops.limitCurve('ThreePoint', 14054, 4054, 0.0, 245.6980435, 0.01026409, 245.6980435, 0.03079226, 171.98863045, -11797.95547992, 0.05, 2, 0, 74022, 22004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34054, 61.42451087, 7.737e-05, 184.27353262, 0.00023212, 614.24510874, 0.00077373, -61.42451087, -7.737e-05, -184.27353262, -0.00023212, -614.24510874, -0.00077373, 0.4, 0.3, 0.003, 0.0, 0.0, 14054, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4054, 99999, 'P', 44054, 'Vy', 34054, 'Vz', 24054, 'My', 14054, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174022, 74022, 174022, 4054, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122004, 122004, 22004, 4054, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172003, 8.5, 0.0, 6.375)
    ops.node(124023, 8.5, 0.0, 7.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4056, 172003, 124023, 0.0625, 29240683.46867206, 12183618.11194669, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24056, 34.87319198, 0.00062576, 42.11253144, 0.04797499, 4.21125314, 0.14797499, -34.87319198, -0.00062576, -42.11253144, -0.04797499, -4.21125314, -0.14797499, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14056, 34.87319198, 0.00062576, 42.11253144, 0.04797499, 4.21125314, 0.14797499, -34.87319198, -0.00062576, -42.11253144, -0.04797499, -4.21125314, -0.14797499, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24056, 4056, 0.0, 109.41302443, 0.01251528, 109.41302443, 0.03754584, 76.5891171, -4632.59261762, 0.05, 2, 0, 72003, 24023, 2, 3)
    ops.uniaxialMaterial('LimitState', 44056, 27.35325611, 6.681e-05, 82.05976832, 0.00020044, 273.53256107, 0.00066814, -27.35325611, -6.681e-05, -82.05976832, -0.00020044, -273.53256107, -0.00066814, 0.4, 0.3, 0.003, 0.0, 0.0, 24056, 2)
    ops.limitCurve('ThreePoint', 14056, 4056, 0.0, 109.41302443, 0.01251528, 109.41302443, 0.03754584, 76.5891171, -4632.59261762, 0.05, 2, 0, 72003, 24023, 1, 3)
    ops.uniaxialMaterial('LimitState', 34056, 27.35325611, 6.681e-05, 82.05976832, 0.00020044, 273.53256107, 0.00066814, -27.35325611, -6.681e-05, -82.05976832, -0.00020044, -273.53256107, -0.00066814, 0.4, 0.3, 0.003, 0.0, 0.0, 14056, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4056, 99999, 'P', 44056, 'Vy', 34056, 'Vz', 24056, 'My', 14056, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172003, 72003, 172003, 4056, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124023, 124023, 24023, 4056, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174023, 8.5, 0.0, 7.95)
    ops.node(123003, 8.5, 0.0, 9.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4057, 174023, 123003, 0.0625, 30357664.43954884, 12649026.84981202, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24057, 32.04239708, 0.00061519, 38.69306353, 0.03776149, 3.86930635, 0.12128892, -32.04239708, -0.00061519, -38.69306353, -0.03776149, -3.86930635, -0.12128892, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14057, 32.04239708, 0.00061519, 38.69306353, 0.03776149, 3.86930635, 0.12128892, -32.04239708, -0.00061519, -38.69306353, -0.03776149, -3.86930635, -0.12128892, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24057, 4057, 0.0, 86.87446579, 0.01230376, 86.87446579, 0.03691127, 60.81212605, -2845.7982994, 0.05, 2, 0, 74023, 23003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44057, 21.71861645, 5.11e-05, 65.15584934, 0.0001533, 217.18616448, 0.00051098, -21.71861645, -5.11e-05, -65.15584934, -0.0001533, -217.18616448, -0.00051098, 0.4, 0.3, 0.003, 0.0, 0.0, 24057, 2)
    ops.limitCurve('ThreePoint', 14057, 4057, 0.0, 86.87446579, 0.01230376, 86.87446579, 0.03691127, 60.81212605, -2845.7982994, 0.05, 2, 0, 74023, 23003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34057, 21.71861645, 5.11e-05, 65.15584934, 0.0001533, 217.18616448, 0.00051098, -21.71861645, -5.11e-05, -65.15584934, -0.0001533, -217.18616448, -0.00051098, 0.4, 0.3, 0.003, 0.0, 0.0, 14057, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4057, 99999, 'P', 44057, 'Vy', 34057, 'Vz', 24057, 'My', 14057, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174023, 74023, 174023, 4057, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123003, 123003, 23003, 4057, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172004, 11.35, 0.0, 6.375)
    ops.node(124024, 11.35, 0.0, 7.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4058, 172004, 124024, 0.0625, 30059672.92295786, 12524863.71789911, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24058, 34.8609416, 0.00063749, 42.0365856, 0.04771471, 4.20365856, 0.14771471, -34.8609416, -0.00063749, -42.0365856, -0.04771471, -4.20365856, -0.14771471, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14058, 34.8609416, 0.00063749, 42.0365856, 0.04771471, 4.20365856, 0.14771471, -34.8609416, -0.00063749, -42.0365856, -0.04771471, -4.20365856, -0.14771471, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24058, 4058, 0.0, 111.36353221, 0.01274982, 111.36353221, 0.03824947, 77.95447254, -4666.05937364, 0.05, 2, 0, 72004, 24024, 2, 3)
    ops.uniaxialMaterial('LimitState', 44058, 27.84088305, 6.615e-05, 83.52264915, 0.00019846, 278.40883051, 0.00066152, -27.84088305, -6.615e-05, -83.52264915, -0.00019846, -278.40883051, -0.00066152, 0.4, 0.3, 0.003, 0.0, 0.0, 24058, 2)
    ops.limitCurve('ThreePoint', 14058, 4058, 0.0, 111.36353221, 0.01274982, 111.36353221, 0.03824947, 77.95447254, -4666.05937364, 0.05, 2, 0, 72004, 24024, 1, 3)
    ops.uniaxialMaterial('LimitState', 34058, 27.84088305, 6.615e-05, 83.52264915, 0.00019846, 278.40883051, 0.00066152, -27.84088305, -6.615e-05, -83.52264915, -0.00019846, -278.40883051, -0.00066152, 0.4, 0.3, 0.003, 0.0, 0.0, 14058, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4058, 99999, 'P', 44058, 'Vy', 34058, 'Vz', 24058, 'My', 14058, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172004, 72004, 172004, 4058, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124024, 124024, 24024, 4058, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174024, 11.35, 0.0, 7.95)
    ops.node(123004, 11.35, 0.0, 9.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4059, 174024, 123004, 0.0625, 29223038.73213694, 12176266.13839039, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24059, 31.78129051, 0.00061834, 38.46797523, 0.03801924, 3.84679752, 0.11923459, -31.78129051, -0.00061834, -38.46797523, -0.03801924, -3.84679752, -0.11923459, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14059, 31.78129051, 0.00061834, 38.46797523, 0.03801924, 3.84679752, 0.11923459, -31.78129051, -0.00061834, -38.46797523, -0.03801924, -3.84679752, -0.11923459, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24059, 4059, 0.0, 84.59399023, 0.01236689, 84.59399023, 0.03710068, 59.21579316, -2840.06146562, 0.05, 2, 0, 74024, 23004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44059, 21.14849756, 5.169e-05, 63.44549267, 0.00015507, 211.48497557, 0.00051689, -21.14849756, -5.169e-05, -63.44549267, -0.00015507, -211.48497557, -0.00051689, 0.4, 0.3, 0.003, 0.0, 0.0, 24059, 2)
    ops.limitCurve('ThreePoint', 14059, 4059, 0.0, 84.59399023, 0.01236689, 84.59399023, 0.03710068, 59.21579316, -2840.06146562, 0.05, 2, 0, 74024, 23004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34059, 21.14849756, 5.169e-05, 63.44549267, 0.00015507, 211.48497557, 0.00051689, -21.14849756, -5.169e-05, -63.44549267, -0.00015507, -211.48497557, -0.00051689, 0.4, 0.3, 0.003, 0.0, 0.0, 14059, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4059, 99999, 'P', 44059, 'Vy', 34059, 'Vz', 24059, 'My', 14059, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174024, 74024, 174024, 4059, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123004, 123004, 23004, 4059, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173003, 8.5, 0.0, 9.475)
    ops.node(124025, 8.5, 0.0, 10.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4061, 173003, 124025, 0.0625, 27588891.6174261, 11495371.50726088, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24061, 26.34655643, 0.00060621, 32.12981834, 0.03364482, 3.21298183, 0.10361135, -26.34655643, -0.00060621, -32.12981834, -0.03364482, -3.21298183, -0.10361135, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14061, 26.34655643, 0.00060621, 32.12981834, 0.03364482, 3.21298183, 0.10361135, -26.34655643, -0.00060621, -32.12981834, -0.03364482, -3.21298183, -0.10361135, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24061, 4061, 0.0, 67.69006318, 0.01212422, 67.69006318, 0.03637265, 47.38304422, -2732.7011119, 0.05, 2, 0, 73003, 24025, 2, 3)
    ops.uniaxialMaterial('LimitState', 44061, 16.92251579, 4.381e-05, 50.76754738, 0.00013143, 169.22515794, 0.0004381, -16.92251579, -4.381e-05, -50.76754738, -0.00013143, -169.22515794, -0.0004381, 0.4, 0.3, 0.003, 0.0, 0.0, 24061, 2)
    ops.limitCurve('ThreePoint', 14061, 4061, 0.0, 67.69006318, 0.01212422, 67.69006318, 0.03637265, 47.38304422, -2732.7011119, 0.05, 2, 0, 73003, 24025, 1, 3)
    ops.uniaxialMaterial('LimitState', 34061, 16.92251579, 4.381e-05, 50.76754738, 0.00013143, 169.22515794, 0.0004381, -16.92251579, -4.381e-05, -50.76754738, -0.00013143, -169.22515794, -0.0004381, 0.4, 0.3, 0.003, 0.0, 0.0, 14061, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4061, 99999, 'P', 44061, 'Vy', 34061, 'Vz', 24061, 'My', 14061, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173003, 73003, 173003, 4061, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124025, 124025, 24025, 4061, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174025, 8.5, 0.0, 11.05)
    ops.node(124003, 8.5, 0.0, 12.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4062, 174025, 124003, 0.0625, 30239701.23109622, 12599875.51295676, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24062, 23.54621015, 0.00056649, 28.60281861, 0.03356288, 2.86028186, 0.11068896, -23.54621015, -0.00056649, -28.60281861, -0.03356288, -2.86028186, -0.11068896, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14062, 23.54621015, 0.00056649, 28.60281861, 0.03356288, 2.86028186, 0.11068896, -23.54621015, -0.00056649, -28.60281861, -0.03356288, -2.86028186, -0.11068896, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24062, 4062, 0.0, 68.84549933, 0.01132971, 68.84549933, 0.03398914, 48.19184953, -4785.6361348, 0.05, 2, 0, 74025, 24003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44062, 17.21137483, 4.065e-05, 51.63412449, 0.00012196, 172.11374831, 0.00040652, -17.21137483, -4.065e-05, -51.63412449, -0.00012196, -172.11374831, -0.00040652, 0.4, 0.3, 0.003, 0.0, 0.0, 24062, 2)
    ops.limitCurve('ThreePoint', 14062, 4062, 0.0, 68.84549933, 0.01132971, 68.84549933, 0.03398914, 48.19184953, -4785.6361348, 0.05, 2, 0, 74025, 24003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34062, 17.21137483, 4.065e-05, 51.63412449, 0.00012196, 172.11374831, 0.00040652, -17.21137483, -4.065e-05, -51.63412449, -0.00012196, -172.11374831, -0.00040652, 0.4, 0.3, 0.003, 0.0, 0.0, 14062, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4062, 99999, 'P', 44062, 'Vy', 34062, 'Vz', 24062, 'My', 14062, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174025, 74025, 174025, 4062, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124003, 124003, 24003, 4062, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173004, 11.35, 0.0, 9.475)
    ops.node(124026, 11.35, 0.0, 10.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4063, 173004, 124026, 0.0625, 28955036.54104822, 12064598.55877009, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24063, 26.22788339, 0.0006049, 31.89516083, 0.0332136, 3.18951608, 0.10463489, -26.22788339, -0.0006049, -31.89516083, -0.0332136, -3.18951608, -0.10463489, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14063, 26.22788339, 0.0006049, 31.89516083, 0.0332136, 3.18951608, 0.10463489, -26.22788339, -0.0006049, -31.89516083, -0.0332136, -3.18951608, -0.10463489, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24063, 4063, 0.0, 70.20706099, 0.01209798, 70.20706099, 0.03629394, 49.1449427, -2731.77713952, 0.05, 2, 0, 73004, 24026, 2, 3)
    ops.uniaxialMaterial('LimitState', 44063, 17.55176525, 4.33e-05, 52.65529575, 0.00012989, 175.51765249, 0.00043295, -17.55176525, -4.33e-05, -52.65529575, -0.00012989, -175.51765249, -0.00043295, 0.4, 0.3, 0.003, 0.0, 0.0, 24063, 2)
    ops.limitCurve('ThreePoint', 14063, 4063, 0.0, 70.20706099, 0.01209798, 70.20706099, 0.03629394, 49.1449427, -2731.77713952, 0.05, 2, 0, 73004, 24026, 1, 3)
    ops.uniaxialMaterial('LimitState', 34063, 17.55176525, 4.33e-05, 52.65529575, 0.00012989, 175.51765249, 0.00043295, -17.55176525, -4.33e-05, -52.65529575, -0.00012989, -175.51765249, -0.00043295, 0.4, 0.3, 0.003, 0.0, 0.0, 14063, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4063, 99999, 'P', 44063, 'Vy', 34063, 'Vz', 24063, 'My', 14063, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173004, 73004, 173004, 4063, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124026, 124026, 24026, 4063, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174026, 11.35, 0.0, 11.05)
    ops.node(124004, 11.35, 0.0, 12.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4064, 174026, 124004, 0.0625, 29679217.27517597, 12366340.53132332, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24064, 23.73054654, 0.00056847, 28.87169233, 0.03391602, 2.88716923, 0.1108395, -23.73054654, -0.00056847, -28.87169233, -0.03391602, -2.88716923, -0.1108395, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14064, 23.73054654, 0.00056847, 28.87169233, 0.03391602, 2.88716923, 0.1108395, -23.73054654, -0.00056847, -28.87169233, -0.03391602, -2.88716923, -0.1108395, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24064, 4064, 0.0, 66.95251907, 0.01136944, 66.95251907, 0.03410833, 46.86676335, -4569.27395971, 0.05, 2, 0, 74026, 24004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44064, 16.73812977, 4.028e-05, 50.2143893, 0.00012084, 167.38129768, 0.00040281, -16.73812977, -4.028e-05, -50.2143893, -0.00012084, -167.38129768, -0.00040281, 0.4, 0.3, 0.003, 0.0, 0.0, 24064, 2)
    ops.limitCurve('ThreePoint', 14064, 4064, 0.0, 66.95251907, 0.01136944, 66.95251907, 0.03410833, 46.86676335, -4569.27395971, 0.05, 2, 0, 74026, 24004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34064, 16.73812977, 4.028e-05, 50.2143893, 0.00012084, 167.38129768, 0.00040281, -16.73812977, -4.028e-05, -50.2143893, -0.00012084, -167.38129768, -0.00040281, 0.4, 0.3, 0.003, 0.0, 0.0, 14064, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4064, 99999, 'P', 44064, 'Vy', 34064, 'Vz', 24064, 'My', 14064, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174026, 74026, 174026, 4064, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124004, 124004, 24004, 4064, '-orient', 0, 0, 1, 0, 1, 0)
