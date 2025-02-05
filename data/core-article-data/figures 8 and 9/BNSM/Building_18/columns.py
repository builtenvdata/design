import openseespy.opensees as ops


def add_columns() -> None:
    """Add components of all columns to ops domain (plastic hinges, column elements and nodes)
    """
    # Create elastic column element nodes
    ops.node(170001, 0.0, 0.0, 0.0)
    ops.node(121001, 0.0, 0.0, 3.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1, 170001, 121001, 0.0625, 27740401.98307873, 11558500.8262828, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20001, 30.28207743, 0.00099634, 36.58745903, 0.02125352, 3.6587459, 0.06592906, -30.28207743, -0.00099634, -36.58745903, -0.02125352, -3.6587459, -0.06592906, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10001, 32.41409849, 0.00099634, 39.16341285, 0.02125352, 3.91634128, 0.06592906, -32.41409849, -0.00099634, -39.16341285, -0.02125352, -3.91634128, -0.06592906, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20001, 1, 0.0, 57.72748224, 0.01992677, 57.72748224, 0.05978031, 40.40923757, -552.31047334, 0.05, 2, 0, 70001, 21001, 2, 3)
    ops.uniaxialMaterial('LimitState', 40001, 14.43187056, 8.391e-05, 43.29561168, 0.00025172, 144.31870559, 0.00083905, -14.43187056, -8.391e-05, -43.29561168, -0.00025172, -144.31870559, -0.00083905, 0.4, 0.3, 0.003, 0.0, 0.0, 20001, 2)
    ops.limitCurve('ThreePoint', 10001, 1, 0.0, 57.72748224, 0.01992677, 57.72748224, 0.05978031, 40.40923757, -552.31047334, 0.05, 2, 0, 70001, 21001, 1, 3)
    ops.uniaxialMaterial('LimitState', 30001, 14.43187056, 8.391e-05, 43.29561168, 0.00025172, 144.31870559, 0.00083905, -14.43187056, -8.391e-05, -43.29561168, -0.00025172, -144.31870559, -0.00083905, 0.4, 0.3, 0.003, 0.0, 0.0, 10001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1, 99999, 'P', 40001, 'Vy', 30001, 'Vz', 20001, 'My', 10001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170001, 70001, 170001, 1, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121001, 121001, 21001, 1, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170002, 4.95, 0.0, 0.0)
    ops.node(121002, 4.95, 0.0, 3.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2, 170002, 121002, 0.09, 31407283.37034314, 13086368.07097631, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20002, 53.89469453, 0.00081673, 64.63658415, 0.03511678, 6.46365842, 0.09933093, -53.89469453, -0.00081673, -64.63658415, -0.03511678, -6.46365842, -0.09933093, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10002, 59.7364027, 0.00081673, 71.64261814, 0.03511678, 7.16426181, 0.09933093, -59.7364027, -0.00081673, -71.64261814, -0.03511678, -7.16426181, -0.09933093, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20002, 2, 0.0, 119.80469, 0.01633467, 119.80469, 0.049004, 83.863283, -1237.71633943, 0.05, 2, 0, 70002, 21002, 2, 3)
    ops.uniaxialMaterial('LimitState', 40002, 29.9511725, 0.00010681, 89.8535175, 0.00032042, 299.51172499, 0.00106807, -29.9511725, -0.00010681, -89.8535175, -0.00032042, -299.51172499, -0.00106807, 0.4, 0.3, 0.003, 0.0, 0.0, 20002, 2)
    ops.limitCurve('ThreePoint', 10002, 2, 0.0, 119.80469, 0.01633467, 119.80469, 0.049004, 83.863283, -1237.71633943, 0.05, 2, 0, 70002, 21002, 1, 3)
    ops.uniaxialMaterial('LimitState', 30002, 29.9511725, 0.00010681, 89.8535175, 0.00032042, 299.51172499, 0.00106807, -29.9511725, -0.00010681, -89.8535175, -0.00032042, -299.51172499, -0.00106807, 0.4, 0.3, 0.003, 0.0, 0.0, 10002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2, 99999, 'P', 40002, 'Vy', 30002, 'Vz', 20002, 'My', 10002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170002, 70002, 170002, 2, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121002, 121002, 21002, 2, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170005, 17.85, 0.0, 0.0)
    ops.node(121005, 17.85, 0.0, 3.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 5, 170005, 121005, 0.09, 30869879.35122587, 12862449.72967745, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20005, 54.73373309, 0.00080122, 65.71547517, 0.03545008, 6.57154752, 0.09848527, -54.73373309, -0.00080122, -65.71547517, -0.03545008, -6.57154752, -0.09848527, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10005, 61.37236143, 0.00080122, 73.68607377, 0.03545008, 7.36860738, 0.09848527, -61.37236143, -0.00080122, -73.68607377, -0.03545008, -7.36860738, -0.09848527, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20005, 5, 0.0, 117.54527934, 0.01602446, 117.54527934, 0.04807337, 82.28169554, -1219.94196368, 0.05, 2, 0, 70005, 21005, 2, 3)
    ops.uniaxialMaterial('LimitState', 40005, 29.38631983, 0.00010662, 88.1589595, 0.00031985, 293.86319834, 0.00106617, -29.38631983, -0.00010662, -88.1589595, -0.00031985, -293.86319834, -0.00106617, 0.4, 0.3, 0.003, 0.0, 0.0, 20005, 2)
    ops.limitCurve('ThreePoint', 10005, 5, 0.0, 117.54527934, 0.01602446, 117.54527934, 0.04807337, 82.28169554, -1219.94196368, 0.05, 2, 0, 70005, 21005, 1, 3)
    ops.uniaxialMaterial('LimitState', 30005, 29.38631983, 0.00010662, 88.1589595, 0.00031985, 293.86319834, 0.00106617, -29.38631983, -0.00010662, -88.1589595, -0.00031985, -293.86319834, -0.00106617, 0.4, 0.3, 0.003, 0.0, 0.0, 10005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 5, 99999, 'P', 40005, 'Vy', 30005, 'Vz', 20005, 'My', 10005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170005, 70005, 170005, 5, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121005, 121005, 21005, 5, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170006, 22.8, 0.0, 0.0)
    ops.node(121006, 22.8, 0.0, 3.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 6, 170006, 121006, 0.0625, 30799367.16867132, 12833069.65361305, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20006, 32.49895133, 0.00092641, 39.08854566, 0.02256131, 3.90885457, 0.07288544, -32.49895133, -0.00092641, -39.08854566, -0.02256131, -3.90885457, -0.07288544, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10006, 35.30943044, 0.00092641, 42.46888677, 0.02256131, 4.24688868, 0.07288544, -35.30943044, -0.00092641, -42.46888677, -0.02256131, -4.24688868, -0.07288544, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20006, 6, 0.0, 69.74861381, 0.01852828, 69.74861381, 0.05558484, 48.82402967, -598.60818689, 0.05, 2, 0, 70006, 21006, 2, 3)
    ops.uniaxialMaterial('LimitState', 40006, 17.43715345, 9.131e-05, 52.31146036, 0.00027393, 174.37153452, 0.00091309, -17.43715345, -9.131e-05, -52.31146036, -0.00027393, -174.37153452, -0.00091309, 0.4, 0.3, 0.003, 0.0, 0.0, 20006, 2)
    ops.limitCurve('ThreePoint', 10006, 6, 0.0, 69.74861381, 0.01852828, 69.74861381, 0.05558484, 48.82402967, -598.60818689, 0.05, 2, 0, 70006, 21006, 1, 3)
    ops.uniaxialMaterial('LimitState', 30006, 17.43715345, 9.131e-05, 52.31146036, 0.00027393, 174.37153452, 0.00091309, -17.43715345, -9.131e-05, -52.31146036, -0.00027393, -174.37153452, -0.00091309, 0.4, 0.3, 0.003, 0.0, 0.0, 10006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 6, 99999, 'P', 40006, 'Vy', 30006, 'Vz', 20006, 'My', 10006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170006, 70006, 170006, 6, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121006, 121006, 21006, 6, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170007, 0.0, 4.6, 0.0)
    ops.node(121007, 0.0, 4.6, 3.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 7, 170007, 121007, 0.09, 30362611.69571528, 12651088.20654804, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20007, 64.41859711, 0.00086267, 77.42883588, 0.03446817, 7.74288359, 0.09663621, -64.41859711, -0.00086267, -77.42883588, -0.03446817, -7.74288359, -0.09663621, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10007, 70.40817772, 0.00086267, 84.62809627, 0.03446817, 8.46280963, 0.09663621, -70.40817772, -0.00086267, -84.62809627, -0.03446817, -8.46280963, -0.09663621, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20007, 7, 0.0, 111.96242195, 0.01725344, 111.96242195, 0.05176032, 78.37369537, -1123.04893983, 0.05, 2, 0, 70007, 21007, 2, 3)
    ops.uniaxialMaterial('LimitState', 40007, 27.99060549, 0.00010325, 83.97181647, 0.00030975, 279.90605489, 0.0010325, -27.99060549, -0.00010325, -83.97181647, -0.00030975, -279.90605489, -0.0010325, 0.4, 0.3, 0.003, 0.0, 0.0, 20007, 2)
    ops.limitCurve('ThreePoint', 10007, 7, 0.0, 111.96242195, 0.01725344, 111.96242195, 0.05176032, 78.37369537, -1123.04893983, 0.05, 2, 0, 70007, 21007, 1, 3)
    ops.uniaxialMaterial('LimitState', 30007, 27.99060549, 0.00010325, 83.97181647, 0.00030975, 279.90605489, 0.0010325, -27.99060549, -0.00010325, -83.97181647, -0.00030975, -279.90605489, -0.0010325, 0.4, 0.3, 0.003, 0.0, 0.0, 10007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 7, 99999, 'P', 40007, 'Vy', 30007, 'Vz', 20007, 'My', 10007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170007, 70007, 170007, 7, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121007, 121007, 21007, 7, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170008, 4.95, 4.6, 0.0)
    ops.node(121008, 4.95, 4.6, 3.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 8, 170008, 121008, 0.1225, 29667241.18818079, 12361350.49507533, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20008, 120.71564103, 0.0007876, 145.20521731, 0.04869604, 14.52052173, 0.12307447, -120.71564103, -0.0007876, -145.20521731, -0.04869604, -14.52052173, -0.12307447, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10008, 129.52775336, 0.0007876, 155.80504245, 0.04869604, 15.58050425, 0.12307447, -129.52775336, -0.0007876, -155.80504245, -0.04869604, -15.58050425, -0.12307447, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20008, 8, 0.0, 163.07407334, 0.01575198, 163.07407334, 0.04725593, 114.15185134, -1851.56594646, 0.05, 2, 0, 70008, 21008, 2, 3)
    ops.uniaxialMaterial('LimitState', 40008, 40.76851834, 0.00011308, 122.30555501, 0.00033923, 407.68518336, 0.00113076, -40.76851834, -0.00011308, -122.30555501, -0.00033923, -407.68518336, -0.00113076, 0.4, 0.3, 0.003, 0.0, 0.0, 20008, 2)
    ops.limitCurve('ThreePoint', 10008, 8, 0.0, 163.07407334, 0.01575198, 163.07407334, 0.04725593, 114.15185134, -1851.56594646, 0.05, 2, 0, 70008, 21008, 1, 3)
    ops.uniaxialMaterial('LimitState', 30008, 40.76851834, 0.00011308, 122.30555501, 0.00033923, 407.68518336, 0.00113076, -40.76851834, -0.00011308, -122.30555501, -0.00033923, -407.68518336, -0.00113076, 0.4, 0.3, 0.003, 0.0, 0.0, 10008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 8, 99999, 'P', 40008, 'Vy', 30008, 'Vz', 20008, 'My', 10008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170008, 70008, 170008, 8, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121008, 121008, 21008, 8, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170009, 9.9, 4.6, 0.0)
    ops.node(121009, 9.9, 4.6, 3.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 9, 170009, 121009, 0.1225, 31745954.51912984, 13227481.04963744, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20009, 120.07138308, 0.00076631, 143.97138094, 0.05224117, 14.39713809, 0.13428022, -120.07138308, -0.00076631, -143.97138094, -0.05224117, -14.39713809, -0.13428022, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10009, 134.72866854, 0.00076631, 161.54617332, 0.06085338, 16.15461733, 0.16085338, -134.72866854, -0.00076631, -161.54617332, -0.06085338, -16.15461733, -0.16085338, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20009, 9, 0.0, 213.79436392, 0.01532613, 213.79436392, 0.04597838, 149.65605475, -3259.65083198, 0.05, 2, 0, 70009, 21009, 2, 3)
    ops.uniaxialMaterial('LimitState', 40009, 53.44859098, 0.00013854, 160.34577294, 0.00041562, 534.48590981, 0.00138539, -53.44859098, -0.00013854, -160.34577294, -0.00041562, -534.48590981, -0.00138539, 0.4, 0.3, 0.003, 0.0, 0.0, 20009, 2)
    ops.limitCurve('ThreePoint', 10009, 9, 0.0, 175.83536106, 0.01532613, 175.83536106, 0.04597838, 123.08475274, -2030.06512072, 0.05, 2, 0, 70009, 21009, 1, 3)
    ops.uniaxialMaterial('LimitState', 30009, 43.95884026, 0.00011394, 131.87652079, 0.00034182, 439.58840264, 0.00113942, -43.95884026, -0.00011394, -131.87652079, -0.00034182, -439.58840264, -0.00113942, 0.4, 0.3, 0.003, 0.0, 0.0, 10009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 9, 99999, 'P', 40009, 'Vy', 30009, 'Vz', 20009, 'My', 10009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170009, 70009, 170009, 9, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121009, 121009, 21009, 9, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170010, 12.9, 4.6, 0.0)
    ops.node(121010, 12.9, 4.6, 3.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 10, 170010, 121010, 0.1225, 30205609.85479016, 12585670.77282923, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20010, 113.98277615, 0.00083437, 137.10371718, 0.05377978, 13.71037172, 0.13169536, -113.98277615, -0.00083437, -137.10371718, -0.05377978, -13.71037172, -0.13169536, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10010, 125.45822114, 0.00083437, 150.90690937, 0.06263803, 15.09069094, 0.16263803, -125.45822114, -0.00083437, -150.90690937, -0.06263803, -15.09069094, -0.16263803, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20010, 10, 0.0, 217.6519733, 0.01668745, 217.6519733, 0.05006235, 152.35638131, -3627.23607418, 0.05, 2, 0, 70010, 21010, 2, 3)
    ops.uniaxialMaterial('LimitState', 40010, 54.41299333, 0.00014823, 163.23897998, 0.00044469, 544.12993326, 0.00148231, -54.41299333, -0.00014823, -163.23897998, -0.00044469, -544.12993326, -0.00148231, 0.4, 0.3, 0.003, 0.0, 0.0, 20010, 2)
    ops.limitCurve('ThreePoint', 10010, 10, 0.0, 176.39946943, 0.01668745, 176.39946943, 0.05006235, 123.4796286, -2222.65439839, 0.05, 2, 0, 70010, 21010, 1, 3)
    ops.uniaxialMaterial('LimitState', 30010, 44.09986736, 0.00012014, 132.29960207, 0.00036041, 440.99867358, 0.00120136, -44.09986736, -0.00012014, -132.29960207, -0.00036041, -440.99867358, -0.00120136, 0.4, 0.3, 0.003, 0.0, 0.0, 10010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 10, 99999, 'P', 40010, 'Vy', 30010, 'Vz', 20010, 'My', 10010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170010, 70010, 170010, 10, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121010, 121010, 21010, 10, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170011, 17.85, 4.6, 0.0)
    ops.node(121011, 17.85, 4.6, 3.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 11, 170011, 121011, 0.1225, 30030246.22341901, 12512602.59309125, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20011, 113.61035026, 0.00082242, 136.58397588, 0.0493948, 13.65839759, 0.12491663, -113.61035026, -0.00082242, -136.58397588, -0.0493948, -13.65839759, -0.12491663, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10011, 120.42433842, 0.00082242, 144.77584917, 0.0493948, 14.47758492, 0.12491663, -120.42433842, -0.00082242, -144.77584917, -0.0493948, -14.47758492, -0.12491663, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20011, 11, 0.0, 166.22037272, 0.01644848, 166.22037272, 0.04934545, 116.3542609, -1897.86314201, 0.05, 2, 0, 70011, 21011, 2, 3)
    ops.uniaxialMaterial('LimitState', 40011, 41.55509318, 0.00011386, 124.66527954, 0.00034159, 415.5509318, 0.00113865, -41.55509318, -0.00011386, -124.66527954, -0.00034159, -415.5509318, -0.00113865, 0.4, 0.3, 0.003, 0.0, 0.0, 20011, 2)
    ops.limitCurve('ThreePoint', 10011, 11, 0.0, 166.22037272, 0.01644848, 166.22037272, 0.04934545, 116.3542609, -1897.86314201, 0.05, 2, 0, 70011, 21011, 1, 3)
    ops.uniaxialMaterial('LimitState', 30011, 41.55509318, 0.00011386, 124.66527954, 0.00034159, 415.5509318, 0.00113865, -41.55509318, -0.00011386, -124.66527954, -0.00034159, -415.5509318, -0.00113865, 0.4, 0.3, 0.003, 0.0, 0.0, 10011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 11, 99999, 'P', 40011, 'Vy', 30011, 'Vz', 20011, 'My', 10011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170011, 70011, 170011, 11, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121011, 121011, 21011, 11, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170012, 22.8, 4.6, 0.0)
    ops.node(121012, 22.8, 4.6, 3.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 12, 170012, 121012, 0.09, 31755276.53861723, 13231365.22442385, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20012, 63.30213613, 0.00085658, 75.87094348, 0.03449806, 7.58709435, 0.09971952, -63.30213613, -0.00085658, -75.87094348, -0.03449806, -7.58709435, -0.09971952, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10012, 68.67282124, 0.00085658, 82.3079924, 0.03449806, 8.23079924, 0.09971952, -68.67282124, -0.00085658, -82.3079924, -0.03449806, -8.23079924, -0.09971952, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20012, 12, 0.0, 114.28126219, 0.01713157, 114.28126219, 0.05139471, 79.99688353, -1082.08239189, 0.05, 2, 0, 70012, 21012, 2, 3)
    ops.uniaxialMaterial('LimitState', 40012, 28.57031555, 0.00010077, 85.71094664, 0.0003023, 285.70315548, 0.00100767, -28.57031555, -0.00010077, -85.71094664, -0.0003023, -285.70315548, -0.00100767, 0.4, 0.3, 0.003, 0.0, 0.0, 20012, 2)
    ops.limitCurve('ThreePoint', 10012, 12, 0.0, 114.28126219, 0.01713157, 114.28126219, 0.05139471, 79.99688353, -1082.08239189, 0.05, 2, 0, 70012, 21012, 1, 3)
    ops.uniaxialMaterial('LimitState', 30012, 28.57031555, 0.00010077, 85.71094664, 0.0003023, 285.70315548, 0.00100767, -28.57031555, -0.00010077, -85.71094664, -0.0003023, -285.70315548, -0.00100767, 0.4, 0.3, 0.003, 0.0, 0.0, 10012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 12, 99999, 'P', 40012, 'Vy', 30012, 'Vz', 20012, 'My', 10012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170012, 70012, 170012, 12, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121012, 121012, 21012, 12, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170013, 0.0, 9.2, 0.0)
    ops.node(121013, 0.0, 9.2, 3.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 13, 170013, 121013, 0.0625, 31310018.02162411, 13045840.84234338, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20013, 29.91313453, 0.00091064, 35.93813189, 0.02358867, 3.59381319, 0.07468467, -29.91313453, -0.00091064, -35.93813189, -0.02358867, -3.59381319, -0.07468467, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10013, 31.97901747, 0.00091064, 38.42011764, 0.02358867, 3.84201176, 0.07468467, -31.97901747, -0.00091064, -38.42011764, -0.02358867, -3.84201176, -0.07468467, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20013, 13, 0.0, 70.97021729, 0.01821289, 70.97021729, 0.05463866, 49.6791521, -603.41354824, 0.05, 2, 0, 70013, 21013, 2, 3)
    ops.uniaxialMaterial('LimitState', 40013, 17.74255432, 9.139e-05, 53.22766297, 0.00027418, 177.42554323, 0.00091393, -17.74255432, -9.139e-05, -53.22766297, -0.00027418, -177.42554323, -0.00091393, 0.4, 0.3, 0.003, 0.0, 0.0, 20013, 2)
    ops.limitCurve('ThreePoint', 10013, 13, 0.0, 70.97021729, 0.01821289, 70.97021729, 0.05463866, 49.6791521, -603.41354824, 0.05, 2, 0, 70013, 21013, 1, 3)
    ops.uniaxialMaterial('LimitState', 30013, 17.74255432, 9.139e-05, 53.22766297, 0.00027418, 177.42554323, 0.00091393, -17.74255432, -9.139e-05, -53.22766297, -0.00027418, -177.42554323, -0.00091393, 0.4, 0.3, 0.003, 0.0, 0.0, 10013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 13, 99999, 'P', 40013, 'Vy', 30013, 'Vz', 20013, 'My', 10013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170013, 70013, 170013, 13, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121013, 121013, 21013, 13, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170014, 4.95, 9.2, 0.0)
    ops.node(121014, 4.95, 9.2, 3.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 14, 170014, 121014, 0.09, 29173225.20600023, 12155510.50250009, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20014, 60.99906796, 0.00084254, 73.43619099, 0.03451103, 7.3436191, 0.09335935, -60.99906796, -0.00084254, -73.43619099, -0.03451103, -7.3436191, -0.09335935, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10014, 64.16647981, 0.00084254, 77.24940764, 0.03451103, 7.72494076, 0.09335935, -64.16647981, -0.00084254, -77.24940764, -0.03451103, -7.72494076, -0.09335935, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20014, 14, 0.0, 111.24944301, 0.01685086, 111.24944301, 0.05055258, 77.87461011, -1183.07188726, 0.05, 2, 0, 70014, 21014, 2, 3)
    ops.uniaxialMaterial('LimitState', 40014, 27.81236075, 0.00010678, 83.43708226, 0.00032033, 278.12360753, 0.00106775, -27.81236075, -0.00010678, -83.43708226, -0.00032033, -278.12360753, -0.00106775, 0.4, 0.3, 0.003, 0.0, 0.0, 20014, 2)
    ops.limitCurve('ThreePoint', 10014, 14, 0.0, 111.24944301, 0.01685086, 111.24944301, 0.05055258, 77.87461011, -1183.07188726, 0.05, 2, 0, 70014, 21014, 1, 3)
    ops.uniaxialMaterial('LimitState', 30014, 27.81236075, 0.00010678, 83.43708226, 0.00032033, 278.12360753, 0.00106775, -27.81236075, -0.00010678, -83.43708226, -0.00032033, -278.12360753, -0.00106775, 0.4, 0.3, 0.003, 0.0, 0.0, 10014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 14, 99999, 'P', 40014, 'Vy', 30014, 'Vz', 20014, 'My', 10014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170014, 70014, 170014, 14, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121014, 121014, 21014, 14, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170015, 9.9, 9.2, 0.0)
    ops.node(121015, 9.9, 9.2, 3.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 15, 170015, 121015, 0.09, 31236704.02526855, 13015293.3438619, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20015, 60.19779378, 0.00082108, 72.37380217, 0.04947281, 7.23738022, 0.14645497, -60.19779378, -0.00082108, -72.37380217, -0.04947281, -7.23738022, -0.14645497, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10015, 66.38816013, 0.00082108, 79.81627342, 0.04947281, 7.98162734, 0.14645497, -66.38816013, -0.00082108, -79.81627342, -0.04947281, -7.98162734, -0.14645497, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20015, 15, 0.0, 128.01020789, 0.01642154, 128.01020789, 0.04926462, 89.60714552, -1615.51713791, 0.05, 2, 0, 70015, 21015, 2, 3)
    ops.uniaxialMaterial('LimitState', 40015, 32.00255197, 0.00011475, 96.00765592, 0.00034424, 320.02551973, 0.00114746, -32.00255197, -0.00011475, -96.00765592, -0.00034424, -320.02551973, -0.00114746, 0.4, 0.3, 0.003, 0.0, 0.0, 20015, 2)
    ops.limitCurve('ThreePoint', 10015, 15, 0.0, 128.01020789, 0.01642154, 128.01020789, 0.04926462, 89.60714552, -1615.51713791, 0.05, 2, 0, 70015, 21015, 1, 3)
    ops.uniaxialMaterial('LimitState', 30015, 32.00255197, 0.00011475, 96.00765592, 0.00034424, 320.02551973, 0.00114746, -32.00255197, -0.00011475, -96.00765592, -0.00034424, -320.02551973, -0.00114746, 0.4, 0.3, 0.003, 0.0, 0.0, 10015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 15, 99999, 'P', 40015, 'Vy', 30015, 'Vz', 20015, 'My', 10015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170015, 70015, 170015, 15, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121015, 121015, 21015, 15, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170016, 12.9, 9.2, 0.0)
    ops.node(121016, 12.9, 9.2, 3.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 16, 170016, 121016, 0.09, 29536797.98176469, 12306999.15906862, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20016, 61.04652563, 0.0008446, 73.64422872, 0.05038409, 7.36442287, 0.14240357, -61.04652563, -0.0008446, -73.64422872, -0.05038409, -7.36442287, -0.14240357, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10016, 67.59440737, 0.0008446, 81.54334656, 0.05038409, 8.15433466, 0.14240357, -67.59440737, -0.0008446, -81.54334656, -0.05038409, -8.15433466, -0.14240357, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20016, 16, 0.0, 127.14045495, 0.01689196, 127.14045495, 0.05067588, 88.99831847, -1743.95706964, 0.05, 2, 0, 70016, 21016, 2, 3)
    ops.uniaxialMaterial('LimitState', 40016, 31.78511374, 0.00012053, 95.35534122, 0.00036158, 317.85113738, 0.00120525, -31.78511374, -0.00012053, -95.35534122, -0.00036158, -317.85113738, -0.00120525, 0.4, 0.3, 0.003, 0.0, 0.0, 20016, 2)
    ops.limitCurve('ThreePoint', 10016, 16, 0.0, 127.14045495, 0.01689196, 127.14045495, 0.05067588, 88.99831847, -1743.95706964, 0.05, 2, 0, 70016, 21016, 1, 3)
    ops.uniaxialMaterial('LimitState', 30016, 31.78511374, 0.00012053, 95.35534122, 0.00036158, 317.85113738, 0.00120525, -31.78511374, -0.00012053, -95.35534122, -0.00036158, -317.85113738, -0.00120525, 0.4, 0.3, 0.003, 0.0, 0.0, 10016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 16, 99999, 'P', 40016, 'Vy', 30016, 'Vz', 20016, 'My', 10016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170016, 70016, 170016, 16, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121016, 121016, 21016, 16, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170017, 17.85, 9.2, 0.0)
    ops.node(121017, 17.85, 9.2, 3.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 17, 170017, 121017, 0.09, 32686810.6782801, 13619504.44928337, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20017, 60.89696125, 0.0008763, 72.80912121, 0.03446082, 7.28091212, 0.10122878, -60.89696125, -0.0008763, -72.80912121, -0.03446082, -7.28091212, -0.10122878, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10017, 63.46729868, 0.0008763, 75.88224679, 0.03446082, 7.58822468, 0.10122878, -63.46729868, -0.0008763, -75.88224679, -0.03446082, -7.58822468, -0.10122878, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20017, 17, 0.0, 120.3396272, 0.01752596, 120.3396272, 0.05257789, 84.23773904, -1157.37988874, 0.05, 2, 0, 70017, 21017, 2, 3)
    ops.uniaxialMaterial('LimitState', 40017, 30.0849068, 0.00010308, 90.2547204, 0.00030925, 300.84906801, 0.00103085, -30.0849068, -0.00010308, -90.2547204, -0.00030925, -300.84906801, -0.00103085, 0.4, 0.3, 0.003, 0.0, 0.0, 20017, 2)
    ops.limitCurve('ThreePoint', 10017, 17, 0.0, 120.3396272, 0.01752596, 120.3396272, 0.05257789, 84.23773904, -1157.37988874, 0.05, 2, 0, 70017, 21017, 1, 3)
    ops.uniaxialMaterial('LimitState', 30017, 30.0849068, 0.00010308, 90.2547204, 0.00030925, 300.84906801, 0.00103085, -30.0849068, -0.00010308, -90.2547204, -0.00030925, -300.84906801, -0.00103085, 0.4, 0.3, 0.003, 0.0, 0.0, 10017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 17, 99999, 'P', 40017, 'Vy', 30017, 'Vz', 20017, 'My', 10017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170017, 70017, 170017, 17, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121017, 121017, 21017, 17, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170018, 22.8, 9.2, 0.0)
    ops.node(121018, 22.8, 9.2, 3.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 18, 170018, 121018, 0.0625, 33207291.86222024, 13836371.60925843, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20018, 31.3456224, 0.00098554, 37.47089696, 0.02321867, 3.7470897, 0.07683287, -31.3456224, -0.00098554, -37.47089696, -0.02321867, -3.7470897, -0.07683287, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10018, 33.3715452, 0.00098554, 39.89270704, 0.02321867, 3.9892707, 0.07683287, -33.3715452, -0.00098554, -39.89270704, -0.02321867, -3.9892707, -0.07683287, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20018, 18, 0.0, 75.64974337, 0.01971078, 75.64974337, 0.05913233, 52.95482036, -622.86798257, 0.05, 2, 0, 70018, 21018, 2, 3)
    ops.uniaxialMaterial('LimitState', 40018, 18.91243584, 9.185e-05, 56.73730753, 0.00027556, 189.12435843, 0.00091853, -18.91243584, -9.185e-05, -56.73730753, -0.00027556, -189.12435843, -0.00091853, 0.4, 0.3, 0.003, 0.0, 0.0, 20018, 2)
    ops.limitCurve('ThreePoint', 10018, 18, 0.0, 75.64974337, 0.01971078, 75.64974337, 0.05913233, 52.95482036, -622.86798257, 0.05, 2, 0, 70018, 21018, 1, 3)
    ops.uniaxialMaterial('LimitState', 30018, 18.91243584, 9.185e-05, 56.73730753, 0.00027556, 189.12435843, 0.00091853, -18.91243584, -9.185e-05, -56.73730753, -0.00027556, -189.12435843, -0.00091853, 0.4, 0.3, 0.003, 0.0, 0.0, 10018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 18, 99999, 'P', 40018, 'Vy', 30018, 'Vz', 20018, 'My', 10018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170018, 70018, 170018, 18, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121018, 121018, 21018, 18, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171001, 0.0, 0.0, 3.725)
    ops.node(122001, 0.0, 0.0, 5.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1001, 171001, 122001, 0.0625, 31145958.86428956, 12977482.86012065, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21001, 23.09664868, 0.00088113, 27.83181021, 0.03791547, 2.78318102, 0.1223258, -23.09664868, -0.00088113, -27.83181021, -0.03791547, -2.78318102, -0.1223258, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11001, 23.09664868, 0.00088113, 27.83181021, 0.03791547, 2.78318102, 0.1223258, -23.09664868, -0.00088113, -27.83181021, -0.03791547, -2.78318102, -0.1223258, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21001, 1001, 0.0, 82.12043152, 0.01762258, 82.12043152, 0.05286773, 57.48430207, -1365.37881154, 0.05, 2, 0, 71001, 22001, 2, 3)
    ops.uniaxialMaterial('LimitState', 41001, 20.53010788, 8.201e-05, 61.59032364, 0.00024603, 205.3010788, 0.0008201, -20.53010788, -8.201e-05, -61.59032364, -0.00024603, -205.3010788, -0.0008201, 0.4, 0.3, 0.003, 0.0, 0.0, 21001, 2)
    ops.limitCurve('ThreePoint', 11001, 1001, 0.0, 82.12043152, 0.01762258, 82.12043152, 0.05286773, 57.48430207, -1365.37881154, 0.05, 2, 0, 71001, 22001, 1, 3)
    ops.uniaxialMaterial('LimitState', 31001, 20.53010788, 8.201e-05, 61.59032364, 0.00024603, 205.3010788, 0.0008201, -20.53010788, -8.201e-05, -61.59032364, -0.00024603, -205.3010788, -0.0008201, 0.4, 0.3, 0.003, 0.0, 0.0, 11001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1001, 99999, 'P', 41001, 'Vy', 31001, 'Vz', 21001, 'My', 11001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171001, 71001, 171001, 1001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122001, 122001, 22001, 1001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171002, 4.95, 0.0, 3.725)
    ops.node(122002, 4.95, 0.0, 5.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1002, 171002, 122002, 0.09, 33143914.22527458, 13809964.26053108, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21002, 47.03571127, 0.00068747, 56.30399583, 0.02762092, 5.63039958, 0.0849228, -47.03571127, -0.00068747, -56.30399583, -0.02762092, -5.63039958, -0.0849228, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11002, 43.94979268, 0.00068747, 52.6100037, 0.02762092, 5.26100037, 0.0849228, -43.94979268, -0.00068747, -52.6100037, -0.02762092, -5.26100037, -0.0849228, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21002, 1002, 0.0, 109.52700714, 0.01374934, 109.52700714, 0.04124801, 76.668905, -1259.95382708, 0.05, 2, 0, 71002, 22002, 2, 3)
    ops.uniaxialMaterial('LimitState', 41002, 27.38175179, 7.138e-05, 82.14525536, 0.00021414, 273.81751786, 0.00071379, -27.38175179, -7.138e-05, -82.14525536, -0.00021414, -273.81751786, -0.00071379, 0.4, 0.3, 0.003, 0.0, 0.0, 21002, 2)
    ops.limitCurve('ThreePoint', 11002, 1002, 0.0, 109.52700714, 0.01374934, 109.52700714, 0.04124801, 76.668905, -1259.95382708, 0.05, 2, 0, 71002, 22002, 1, 3)
    ops.uniaxialMaterial('LimitState', 31002, 27.38175179, 7.138e-05, 82.14525536, 0.00021414, 273.81751786, 0.00071379, -27.38175179, -7.138e-05, -82.14525536, -0.00021414, -273.81751786, -0.00071379, 0.4, 0.3, 0.003, 0.0, 0.0, 11002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1002, 99999, 'P', 41002, 'Vy', 31002, 'Vz', 21002, 'My', 11002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171002, 71002, 171002, 1002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122002, 122002, 22002, 1002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171005, 17.85, 0.0, 3.725)
    ops.node(122005, 17.85, 0.0, 5.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1005, 171005, 122005, 0.09, 28648574.50466887, 11936906.04361203, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21005, 45.72608104, 0.00071935, 55.30161919, 0.02926416, 5.53016192, 0.08019881, -45.72608104, -0.00071935, -55.30161919, -0.02926416, -5.53016192, -0.08019881, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11005, 42.77703295, 0.00071935, 51.73500839, 0.02926416, 5.17350084, 0.08019881, -42.77703295, -0.00071935, -51.73500839, -0.02926416, -5.17350084, -0.08019881, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21005, 1005, 0.0, 98.08004665, 0.01438696, 98.08004665, 0.04316088, 68.65603266, -1301.42743507, 0.05, 2, 0, 71005, 22005, 2, 3)
    ops.uniaxialMaterial('LimitState', 41005, 24.52001166, 7.395e-05, 73.56003499, 0.00022185, 245.20011663, 0.00073949, -24.52001166, -7.395e-05, -73.56003499, -0.00022185, -245.20011663, -0.00073949, 0.4, 0.3, 0.003, 0.0, 0.0, 21005, 2)
    ops.limitCurve('ThreePoint', 11005, 1005, 0.0, 98.08004665, 0.01438696, 98.08004665, 0.04316088, 68.65603266, -1301.42743507, 0.05, 2, 0, 71005, 22005, 1, 3)
    ops.uniaxialMaterial('LimitState', 31005, 24.52001166, 7.395e-05, 73.56003499, 0.00022185, 245.20011663, 0.00073949, -24.52001166, -7.395e-05, -73.56003499, -0.00022185, -245.20011663, -0.00073949, 0.4, 0.3, 0.003, 0.0, 0.0, 11005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1005, 99999, 'P', 41005, 'Vy', 31005, 'Vz', 21005, 'My', 11005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171005, 71005, 171005, 1005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122005, 122005, 22005, 1005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171006, 22.8, 0.0, 3.725)
    ops.node(122006, 22.8, 0.0, 5.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1006, 171006, 122006, 0.0625, 31197573.65977765, 12998989.02490735, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21006, 23.03912148, 0.00077209, 27.75888114, 0.04012744, 2.77588811, 0.12462926, -23.03912148, -0.00077209, -27.75888114, -0.04012744, -2.77588811, -0.12462926, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11006, 23.03912148, 0.00077209, 27.75888114, 0.04012744, 2.77588811, 0.12462926, -23.03912148, -0.00077209, -27.75888114, -0.04012744, -2.77588811, -0.12462926, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21006, 1006, 0.0, 85.05501076, 0.01544178, 85.05501076, 0.04632533, 59.53850753, -1500.28920578, 0.05, 2, 0, 71006, 22006, 2, 3)
    ops.uniaxialMaterial('LimitState', 41006, 21.26375269, 8.48e-05, 63.79125807, 0.0002544, 212.63752691, 0.000848, -21.26375269, -8.48e-05, -63.79125807, -0.0002544, -212.63752691, -0.000848, 0.4, 0.3, 0.003, 0.0, 0.0, 21006, 2)
    ops.limitCurve('ThreePoint', 11006, 1006, 0.0, 85.05501076, 0.01544178, 85.05501076, 0.04632533, 59.53850753, -1500.28920578, 0.05, 2, 0, 71006, 22006, 1, 3)
    ops.uniaxialMaterial('LimitState', 31006, 21.26375269, 8.48e-05, 63.79125807, 0.0002544, 212.63752691, 0.000848, -21.26375269, -8.48e-05, -63.79125807, -0.0002544, -212.63752691, -0.000848, 0.4, 0.3, 0.003, 0.0, 0.0, 11006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1006, 99999, 'P', 41006, 'Vy', 31006, 'Vz', 21006, 'My', 11006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171006, 71006, 171006, 1006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122006, 122006, 22006, 1006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171007, 0.0, 4.6, 3.75)
    ops.node(122007, 0.0, 4.6, 5.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1007, 171007, 122007, 0.09, 28469704.83172237, 11862377.01321765, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21007, 44.91820521, 0.00069491, 54.34665935, 0.04951443, 5.43466594, 0.14160006, -44.91820521, -0.00069491, -54.34665935, -0.04951443, -5.43466594, -0.14160006, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11007, 41.93698338, 0.00069491, 50.7396709, 0.04951443, 5.07396709, 0.14160006, -41.93698338, -0.00069491, -50.7396709, -0.04951443, -5.07396709, -0.14160006, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21007, 1007, 0.0, 128.66805663, 0.01389829, 128.66805663, 0.04169486, 90.06763964, -2631.69999933, 0.05, 2, 0, 71007, 22007, 2, 3)
    ops.uniaxialMaterial('LimitState', 41007, 32.16701416, 9.762e-05, 96.50104247, 0.00029286, 321.67014158, 0.00097621, -32.16701416, -9.762e-05, -96.50104247, -0.00029286, -321.67014158, -0.00097621, 0.4, 0.3, 0.003, 0.0, 0.0, 21007, 2)
    ops.limitCurve('ThreePoint', 11007, 1007, 0.0, 128.66805663, 0.01389829, 128.66805663, 0.04169486, 90.06763964, -2631.69999933, 0.05, 2, 0, 71007, 22007, 1, 3)
    ops.uniaxialMaterial('LimitState', 31007, 32.16701416, 9.762e-05, 96.50104247, 0.00029286, 321.67014158, 0.00097621, -32.16701416, -9.762e-05, -96.50104247, -0.00029286, -321.67014158, -0.00097621, 0.4, 0.3, 0.003, 0.0, 0.0, 11007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1007, 99999, 'P', 41007, 'Vy', 31007, 'Vz', 21007, 'My', 11007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171007, 71007, 171007, 1007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122007, 122007, 22007, 1007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171008, 4.95, 4.6, 3.75)
    ops.node(122008, 4.95, 4.6, 5.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1008, 171008, 122008, 0.1225, 30835971.22915247, 12848321.34548019, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21008, 76.86810436, 0.00064034, 92.56507056, 0.03820218, 9.25650706, 0.09851455, -76.86810436, -0.00064034, -92.56507056, -0.03820218, -9.25650706, -0.09851455, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11008, 73.36735523, 0.00064034, 88.34944572, 0.03820218, 8.83494457, 0.09851455, -73.36735523, -0.00064034, -88.34944572, -0.03820218, -8.83494457, -0.09851455, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21008, 1008, 0.0, 147.11191106, 0.01280676, 147.11191106, 0.03842029, 102.97833774, -1942.59501068, 0.05, 2, 0, 71008, 22008, 2, 3)
    ops.uniaxialMaterial('LimitState', 41008, 36.77797776, 7.571e-05, 110.33393329, 0.00022713, 367.77977765, 0.00075709, -36.77797776, -7.571e-05, -110.33393329, -0.00022713, -367.77977765, -0.00075709, 0.4, 0.3, 0.003, 0.0, 0.0, 21008, 2)
    ops.limitCurve('ThreePoint', 11008, 1008, 0.0, 147.11191106, 0.01280676, 147.11191106, 0.03842029, 102.97833774, -1942.59501068, 0.05, 2, 0, 71008, 22008, 1, 3)
    ops.uniaxialMaterial('LimitState', 31008, 36.77797776, 7.571e-05, 110.33393329, 0.00022713, 367.77977765, 0.00075709, -36.77797776, -7.571e-05, -110.33393329, -0.00022713, -367.77977765, -0.00075709, 0.4, 0.3, 0.003, 0.0, 0.0, 11008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1008, 99999, 'P', 41008, 'Vy', 31008, 'Vz', 21008, 'My', 11008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171008, 71008, 171008, 1008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122008, 122008, 22008, 1008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171009, 9.9, 4.6, 3.75)
    ops.node(122009, 9.9, 4.6, 5.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1009, 171009, 122009, 0.1225, 28831162.20095946, 12012984.25039978, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21009, 84.50518899, 0.00066621, 102.20987901, 0.05075352, 10.2209879, 0.13253417, -84.50518899, -0.00066621, -102.20987901, -0.05075352, -10.2209879, -0.13253417, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11009, 77.48756125, 0.00066621, 93.72198743, 0.05075352, 9.37219874, 0.13253417, -77.48756125, -0.00066621, -93.72198743, -0.05075352, -9.37219874, -0.13253417, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21009, 1009, 0.0, 159.18131841, 0.01332418, 159.18131841, 0.03997255, 111.42692289, -2801.74923396, 0.05, 2, 0, 71009, 22009, 2, 3)
    ops.uniaxialMaterial('LimitState', 41009, 39.7953296, 8.762e-05, 119.38598881, 0.00026285, 397.95329602, 0.00087617, -39.7953296, -8.762e-05, -119.38598881, -0.00026285, -397.95329602, -0.00087617, 0.4, 0.3, 0.003, 0.0, 0.0, 21009, 2)
    ops.limitCurve('ThreePoint', 11009, 1009, 0.0, 159.18131841, 0.01332418, 159.18131841, 0.03997255, 111.42692289, -2801.74923396, 0.05, 2, 0, 71009, 22009, 1, 3)
    ops.uniaxialMaterial('LimitState', 31009, 39.7953296, 8.762e-05, 119.38598881, 0.00026285, 397.95329602, 0.00087617, -39.7953296, -8.762e-05, -119.38598881, -0.00026285, -397.95329602, -0.00087617, 0.4, 0.3, 0.003, 0.0, 0.0, 11009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1009, 99999, 'P', 41009, 'Vy', 31009, 'Vz', 21009, 'My', 11009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171009, 71009, 171009, 1009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122009, 122009, 22009, 1009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171010, 12.9, 4.6, 3.75)
    ops.node(122010, 12.9, 4.6, 5.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1010, 171010, 122010, 0.1225, 29112165.54338898, 12130068.97641208, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21010, 83.7525792, 0.00066419, 101.25353885, 0.05187644, 10.12535388, 0.13441281, -83.7525792, -0.00066419, -101.25353885, -0.05187644, -10.12535388, -0.13441281, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11010, 76.93448932, 0.00066419, 93.01073923, 0.05187644, 9.30107392, 0.13441281, -76.93448932, -0.00066419, -93.01073923, -0.05187644, -9.30107392, -0.13441281, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21010, 1010, 0.0, 165.17256749, 0.0132838, 165.17256749, 0.03985139, 115.62079724, -3027.29330577, 0.05, 2, 0, 71010, 22010, 2, 3)
    ops.uniaxialMaterial('LimitState', 41010, 41.29314187, 9.004e-05, 123.87942562, 0.00027011, 412.93141873, 0.00090038, -41.29314187, -9.004e-05, -123.87942562, -0.00027011, -412.93141873, -0.00090038, 0.4, 0.3, 0.003, 0.0, 0.0, 21010, 2)
    ops.limitCurve('ThreePoint', 11010, 1010, 0.0, 165.17256749, 0.0132838, 165.17256749, 0.03985139, 115.62079724, -3027.29330577, 0.05, 2, 0, 71010, 22010, 1, 3)
    ops.uniaxialMaterial('LimitState', 31010, 41.29314187, 9.004e-05, 123.87942562, 0.00027011, 412.93141873, 0.00090038, -41.29314187, -9.004e-05, -123.87942562, -0.00027011, -412.93141873, -0.00090038, 0.4, 0.3, 0.003, 0.0, 0.0, 11010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1010, 99999, 'P', 41010, 'Vy', 31010, 'Vz', 21010, 'My', 11010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171010, 71010, 171010, 1010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122010, 122010, 22010, 1010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171011, 17.85, 4.6, 3.75)
    ops.node(122011, 17.85, 4.6, 5.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1011, 171011, 122011, 0.1225, 31634465.25138603, 13181027.18807751, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21011, 78.65483982, 0.0006269, 94.53587643, 0.03729738, 9.45358764, 0.09883504, -78.65483982, -0.0006269, -94.53587643, -0.03729738, -9.45358764, -0.09883504, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11011, 74.85094535, 0.0006269, 89.96394546, 0.03729738, 8.99639455, 0.09883504, -74.85094535, -0.0006269, -89.96394546, -0.03729738, -8.99639455, -0.09883504, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21011, 1011, 0.0, 147.94185618, 0.0125379, 147.94185618, 0.03761371, 103.55929933, -1862.37085889, 0.05, 2, 0, 71011, 22011, 2, 3)
    ops.uniaxialMaterial('LimitState', 41011, 36.98546405, 7.421e-05, 110.95639214, 0.00022264, 369.85464046, 0.00074215, -36.98546405, -7.421e-05, -110.95639214, -0.00022264, -369.85464046, -0.00074215, 0.4, 0.3, 0.003, 0.0, 0.0, 21011, 2)
    ops.limitCurve('ThreePoint', 11011, 1011, 0.0, 147.94185618, 0.0125379, 147.94185618, 0.03761371, 103.55929933, -1862.37085889, 0.05, 2, 0, 71011, 22011, 1, 3)
    ops.uniaxialMaterial('LimitState', 31011, 36.98546405, 7.421e-05, 110.95639214, 0.00022264, 369.85464046, 0.00074215, -36.98546405, -7.421e-05, -110.95639214, -0.00022264, -369.85464046, -0.00074215, 0.4, 0.3, 0.003, 0.0, 0.0, 11011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1011, 99999, 'P', 41011, 'Vy', 31011, 'Vz', 21011, 'My', 11011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171011, 71011, 171011, 1011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122011, 122011, 22011, 1011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171012, 22.8, 4.6, 3.75)
    ops.node(122012, 22.8, 4.6, 5.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1012, 171012, 122012, 0.09, 29797622.31469679, 12415675.96445699, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21012, 44.98860613, 0.00070297, 54.31229167, 0.05003209, 5.43122917, 0.14620386, -44.98860613, -0.00070297, -54.31229167, -0.05003209, -5.43122917, -0.14620386, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11012, 42.15287348, 0.00070297, 50.88886623, 0.05003209, 5.08888662, 0.14620386, -42.15287348, -0.00070297, -50.88886623, -0.05003209, -5.08888662, -0.14620386, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21012, 1012, 0.0, 131.98519634, 0.01405937, 131.98519634, 0.04217811, 92.38963744, -2617.0344133, 0.05, 2, 0, 71012, 22012, 2, 3)
    ops.uniaxialMaterial('LimitState', 41012, 32.99629908, 9.567e-05, 98.98889725, 0.00028702, 329.96299084, 0.00095675, -32.99629908, -9.567e-05, -98.98889725, -0.00028702, -329.96299084, -0.00095675, 0.4, 0.3, 0.003, 0.0, 0.0, 21012, 2)
    ops.limitCurve('ThreePoint', 11012, 1012, 0.0, 131.98519634, 0.01405937, 131.98519634, 0.04217811, 92.38963744, -2617.0344133, 0.05, 2, 0, 71012, 22012, 1, 3)
    ops.uniaxialMaterial('LimitState', 31012, 32.99629908, 9.567e-05, 98.98889725, 0.00028702, 329.96299084, 0.00095675, -32.99629908, -9.567e-05, -98.98889725, -0.00028702, -329.96299084, -0.00095675, 0.4, 0.3, 0.003, 0.0, 0.0, 11012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1012, 99999, 'P', 41012, 'Vy', 31012, 'Vz', 21012, 'My', 11012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171012, 71012, 171012, 1012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122012, 122012, 22012, 1012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171013, 0.0, 9.2, 3.725)
    ops.node(122013, 0.0, 9.2, 5.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1013, 171013, 122013, 0.0625, 28932777.84087041, 12055324.10036267, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21013, 23.88515995, 0.00080039, 28.91776997, 0.04116342, 2.891777, 0.12107105, -23.88515995, -0.00080039, -28.91776997, -0.04116342, -2.891777, -0.12107105, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11013, 23.88515995, 0.00080039, 28.91776997, 0.04116342, 2.891777, 0.12107105, -23.88515995, -0.00080039, -28.91776997, -0.04116342, -2.891777, -0.12107105, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21013, 1013, 0.0, 82.19311406, 0.01600776, 82.19311406, 0.04802327, 57.53517984, -1572.01185668, 0.05, 2, 0, 71013, 22013, 2, 3)
    ops.uniaxialMaterial('LimitState', 41013, 20.54827851, 8.836e-05, 61.64483554, 0.00026508, 205.48278515, 0.00088361, -20.54827851, -8.836e-05, -61.64483554, -0.00026508, -205.48278515, -0.00088361, 0.4, 0.3, 0.003, 0.0, 0.0, 21013, 2)
    ops.limitCurve('ThreePoint', 11013, 1013, 0.0, 82.19311406, 0.01600776, 82.19311406, 0.04802327, 57.53517984, -1572.01185668, 0.05, 2, 0, 71013, 22013, 1, 3)
    ops.uniaxialMaterial('LimitState', 31013, 20.54827851, 8.836e-05, 61.64483554, 0.00026508, 205.48278515, 0.00088361, -20.54827851, -8.836e-05, -61.64483554, -0.00026508, -205.48278515, -0.00088361, 0.4, 0.3, 0.003, 0.0, 0.0, 11013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1013, 99999, 'P', 41013, 'Vy', 31013, 'Vz', 21013, 'My', 11013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171013, 71013, 171013, 1013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122013, 122013, 22013, 1013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171014, 4.95, 9.2, 3.725)
    ops.node(122014, 4.95, 9.2, 5.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1014, 171014, 122014, 0.09, 29763467.94681929, 12401444.97784137, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21014, 46.13353417, 0.00070569, 55.69075142, 0.02633114, 5.56907514, 0.07916326, -46.13353417, -0.00070569, -55.69075142, -0.02633114, -5.56907514, -0.07916326, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11014, 43.10585577, 0.00070569, 52.0358464, 0.02633114, 5.20358464, 0.07916326, -43.10585577, -0.00070569, -52.0358464, -0.02633114, -5.20358464, -0.07916326, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21014, 1014, 0.0, 96.1118488, 0.01411385, 96.1118488, 0.04234156, 67.27829416, -1132.73687998, 0.05, 2, 0, 71014, 22014, 2, 3)
    ops.uniaxialMaterial('LimitState', 41014, 24.0279622, 6.975e-05, 72.0838866, 0.00020925, 240.279622, 0.0006975, -24.0279622, -6.975e-05, -72.0838866, -0.00020925, -240.279622, -0.0006975, 0.4, 0.3, 0.003, 0.0, 0.0, 21014, 2)
    ops.limitCurve('ThreePoint', 11014, 1014, 0.0, 96.1118488, 0.01411385, 96.1118488, 0.04234156, 67.27829416, -1132.73687998, 0.05, 2, 0, 71014, 22014, 1, 3)
    ops.uniaxialMaterial('LimitState', 31014, 24.0279622, 6.975e-05, 72.0838866, 0.00020925, 240.279622, 0.0006975, -24.0279622, -6.975e-05, -72.0838866, -0.00020925, -240.279622, -0.0006975, 0.4, 0.3, 0.003, 0.0, 0.0, 11014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1014, 99999, 'P', 41014, 'Vy', 31014, 'Vz', 21014, 'My', 11014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171014, 71014, 171014, 1014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122014, 122014, 22014, 1014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171015, 9.9, 9.2, 3.725)
    ops.node(122015, 9.9, 9.2, 5.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1015, 171015, 122015, 0.09, 30459682.73689429, 12691534.47370596, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21015, 40.92227951, 0.00066378, 49.41341713, 0.03817285, 4.94134171, 0.11008744, -40.92227951, -0.00066378, -49.41341713, -0.03817285, -4.94134171, -0.11008744, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11015, 38.07441271, 0.00066378, 45.97463436, 0.03817285, 4.59746344, 0.11008744, -38.07441271, -0.00066378, -45.97463436, -0.03817285, -4.59746344, -0.11008744, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21015, 1015, 0.0, 110.87932894, 0.01327556, 110.87932894, 0.03982668, 77.61553026, -1776.67298593, 0.05, 2, 0, 71015, 22015, 2, 3)
    ops.uniaxialMaterial('LimitState', 41015, 27.71983223, 7.863e-05, 83.1594967, 0.00023588, 277.19832235, 0.00078628, -27.71983223, -7.863e-05, -83.1594967, -0.00023588, -277.19832235, -0.00078628, 0.4, 0.3, 0.003, 0.0, 0.0, 21015, 2)
    ops.limitCurve('ThreePoint', 11015, 1015, 0.0, 110.87932894, 0.01327556, 110.87932894, 0.03982668, 77.61553026, -1776.67298593, 0.05, 2, 0, 71015, 22015, 1, 3)
    ops.uniaxialMaterial('LimitState', 31015, 27.71983223, 7.863e-05, 83.1594967, 0.00023588, 277.19832235, 0.00078628, -27.71983223, -7.863e-05, -83.1594967, -0.00023588, -277.19832235, -0.00078628, 0.4, 0.3, 0.003, 0.0, 0.0, 11015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1015, 99999, 'P', 41015, 'Vy', 31015, 'Vz', 21015, 'My', 11015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171015, 71015, 171015, 1015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122015, 122015, 22015, 1015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171016, 12.9, 9.2, 3.725)
    ops.node(122016, 12.9, 9.2, 5.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1016, 171016, 122016, 0.09, 31022146.02594959, 12925894.177479, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21016, 42.54303898, 0.00066283, 51.3007535, 0.03649215, 5.13007535, 0.10926141, -42.54303898, -0.00066283, -51.3007535, -0.03649215, -5.13007535, -0.10926141, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11016, 39.35495933, 0.00066283, 47.45639042, 0.03649215, 4.74563904, 0.10926141, -39.35495933, -0.00066283, -47.45639042, -0.03649215, -4.74563904, -0.10926141, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21016, 1016, 0.0, 109.15447142, 0.01325661, 109.15447142, 0.03976983, 76.40812999, -1630.28468925, 0.05, 2, 0, 71016, 22016, 2, 3)
    ops.uniaxialMaterial('LimitState', 41016, 27.28861786, 7.6e-05, 81.86585357, 0.00022801, 272.88617855, 0.00076002, -27.28861786, -7.6e-05, -81.86585357, -0.00022801, -272.88617855, -0.00076002, 0.4, 0.3, 0.003, 0.0, 0.0, 21016, 2)
    ops.limitCurve('ThreePoint', 11016, 1016, 0.0, 109.15447142, 0.01325661, 109.15447142, 0.03976983, 76.40812999, -1630.28468925, 0.05, 2, 0, 71016, 22016, 1, 3)
    ops.uniaxialMaterial('LimitState', 31016, 27.28861786, 7.6e-05, 81.86585357, 0.00022801, 272.88617855, 0.00076002, -27.28861786, -7.6e-05, -81.86585357, -0.00022801, -272.88617855, -0.00076002, 0.4, 0.3, 0.003, 0.0, 0.0, 11016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1016, 99999, 'P', 41016, 'Vy', 31016, 'Vz', 21016, 'My', 11016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171016, 71016, 171016, 1016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122016, 122016, 22016, 1016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171017, 17.85, 9.2, 3.725)
    ops.node(122017, 17.85, 9.2, 5.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1017, 171017, 122017, 0.09, 29648948.29106077, 12353728.45460865, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21017, 45.07456541, 0.00073137, 54.42398496, 0.02695886, 5.4423985, 0.07960714, -45.07456541, -0.00073137, -54.42398496, -0.02695886, -5.4423985, -0.07960714, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11017, 42.43824955, 0.00073137, 51.24084135, 0.02695886, 5.12408413, 0.07960714, -42.43824955, -0.00073137, -51.24084135, -0.02695886, -5.12408413, -0.07960714, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21017, 1017, 0.0, 96.41139528, 0.01462742, 96.41139528, 0.04388227, 67.48797669, -1152.81460498, 0.05, 2, 0, 71017, 22017, 2, 3)
    ops.uniaxialMaterial('LimitState', 41017, 24.10284882, 7.024e-05, 72.30854646, 0.00021071, 241.0284882, 0.00070238, -24.10284882, -7.024e-05, -72.30854646, -0.00021071, -241.0284882, -0.00070238, 0.4, 0.3, 0.003, 0.0, 0.0, 21017, 2)
    ops.limitCurve('ThreePoint', 11017, 1017, 0.0, 96.41139528, 0.01462742, 96.41139528, 0.04388227, 67.48797669, -1152.81460498, 0.05, 2, 0, 71017, 22017, 1, 3)
    ops.uniaxialMaterial('LimitState', 31017, 24.10284882, 7.024e-05, 72.30854646, 0.00021071, 241.0284882, 0.00070238, -24.10284882, -7.024e-05, -72.30854646, -0.00021071, -241.0284882, -0.00070238, 0.4, 0.3, 0.003, 0.0, 0.0, 11017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1017, 99999, 'P', 41017, 'Vy', 31017, 'Vz', 21017, 'My', 11017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171017, 71017, 171017, 1017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122017, 122017, 22017, 1017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171018, 22.8, 9.2, 3.725)
    ops.node(122018, 22.8, 9.2, 5.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1018, 171018, 122018, 0.0625, 31852761.18597458, 13271983.82748941, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21018, 22.84074388, 0.00076193, 27.47235217, 0.03792324, 2.74723522, 0.12353947, -22.84074388, -0.00076193, -27.47235217, -0.03792324, -2.74723522, -0.12353947, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11018, 22.84074388, 0.00076193, 27.47235217, 0.03792324, 2.74723522, 0.12353947, -22.84074388, -0.00076193, -27.47235217, -0.03792324, -2.74723522, -0.12353947, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21018, 1018, 0.0, 82.40283416, 0.01523851, 82.40283416, 0.04571554, 57.68198391, -1314.63375082, 0.05, 2, 0, 71018, 22018, 2, 3)
    ops.uniaxialMaterial('LimitState', 41018, 20.60070854, 8.047e-05, 61.80212562, 0.0002414, 206.00708539, 0.00080466, -20.60070854, -8.047e-05, -61.80212562, -0.0002414, -206.00708539, -0.00080466, 0.4, 0.3, 0.003, 0.0, 0.0, 21018, 2)
    ops.limitCurve('ThreePoint', 11018, 1018, 0.0, 82.40283416, 0.01523851, 82.40283416, 0.04571554, 57.68198391, -1314.63375082, 0.05, 2, 0, 71018, 22018, 1, 3)
    ops.uniaxialMaterial('LimitState', 31018, 20.60070854, 8.047e-05, 61.80212562, 0.0002414, 206.00708539, 0.00080466, -20.60070854, -8.047e-05, -61.80212562, -0.0002414, -206.00708539, -0.00080466, 0.4, 0.3, 0.003, 0.0, 0.0, 11018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1018, 99999, 'P', 41018, 'Vy', 31018, 'Vz', 21018, 'My', 11018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171018, 71018, 171018, 1018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122018, 122018, 22018, 1018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172001, 0.0, 0.0, 6.425)
    ops.node(123001, 0.0, 0.0, 8.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2001, 172001, 123001, 0.0625, 31093670.5558692, 12955696.0649455, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22001, 19.13607731, 0.00072325, 23.12233942, 0.03155391, 2.31223394, 0.10278445, -19.13607731, -0.00072325, -23.12233942, -0.03155391, -2.31223394, -0.10278445, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12001, 19.13607731, 0.00072325, 23.12233942, 0.03155391, 2.31223394, 0.10278445, -19.13607731, -0.00072325, -23.12233942, -0.03155391, -2.31223394, -0.10278445, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22001, 2001, 0.0, 71.43228453, 0.01446494, 71.43228453, 0.04339482, 50.00259917, -1214.55184507, 0.05, 2, 0, 72001, 23001, 2, 3)
    ops.uniaxialMaterial('LimitState', 42001, 17.85807113, 7.146e-05, 53.5742134, 0.00021437, 178.58071132, 0.00071456, -17.85807113, -7.146e-05, -53.5742134, -0.00021437, -178.58071132, -0.00071456, 0.4, 0.3, 0.003, 0.0, 0.0, 22001, 2)
    ops.limitCurve('ThreePoint', 12001, 2001, 0.0, 71.43228453, 0.01446494, 71.43228453, 0.04339482, 50.00259917, -1214.55184507, 0.05, 2, 0, 72001, 23001, 1, 3)
    ops.uniaxialMaterial('LimitState', 32001, 17.85807113, 7.146e-05, 53.5742134, 0.00021437, 178.58071132, 0.00071456, -17.85807113, -7.146e-05, -53.5742134, -0.00021437, -178.58071132, -0.00071456, 0.4, 0.3, 0.003, 0.0, 0.0, 12001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2001, 99999, 'P', 42001, 'Vy', 32001, 'Vz', 22001, 'My', 12001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172001, 72001, 172001, 2001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123001, 123001, 23001, 2001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172002, 4.95, 0.0, 6.425)
    ops.node(123002, 4.95, 0.0, 8.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2002, 172002, 123002, 0.0625, 31197529.69108484, 12998970.70461868, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22002, 23.45744036, 0.00081231, 28.25544198, 0.02442218, 2.8255442, 0.07903414, -23.45744036, -0.00081231, -28.25544198, -0.02442218, -2.8255442, -0.07903414, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12002, 23.45744036, 0.00081231, 28.25544198, 0.02442218, 2.8255442, 0.07903414, -23.45744036, -0.00081231, -28.25544198, -0.02442218, -2.8255442, -0.07903414, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22002, 2002, 0.0, 69.49953012, 0.01624617, 69.49953012, 0.04873851, 48.64967109, -824.13782294, 0.05, 2, 0, 72002, 23002, 2, 3)
    ops.uniaxialMaterial('LimitState', 42002, 17.37488253, 6.929e-05, 52.12464759, 0.00020787, 173.74882531, 0.00069291, -17.37488253, -6.929e-05, -52.12464759, -0.00020787, -173.74882531, -0.00069291, 0.4, 0.3, 0.003, 0.0, 0.0, 22002, 2)
    ops.limitCurve('ThreePoint', 12002, 2002, 0.0, 69.49953012, 0.01624617, 69.49953012, 0.04873851, 48.64967109, -824.13782294, 0.05, 2, 0, 72002, 23002, 1, 3)
    ops.uniaxialMaterial('LimitState', 32002, 17.37488253, 6.929e-05, 52.12464759, 0.00020787, 173.74882531, 0.00069291, -17.37488253, -6.929e-05, -52.12464759, -0.00020787, -173.74882531, -0.00069291, 0.4, 0.3, 0.003, 0.0, 0.0, 12002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2002, 99999, 'P', 42002, 'Vy', 32002, 'Vz', 22002, 'My', 12002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172002, 72002, 172002, 2002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123002, 123002, 23002, 2002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172005, 17.85, 0.0, 6.425)
    ops.node(123005, 17.85, 0.0, 8.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2005, 172005, 123005, 0.0625, 30639979.47479929, 12766658.1144997, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22005, 23.54780996, 0.00078397, 28.40231667, 0.02165963, 2.84023167, 0.07558702, -23.54780996, -0.00078397, -28.40231667, -0.02165963, -2.84023167, -0.07558702, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12005, 23.54780996, 0.00078397, 28.40231667, 0.02165963, 2.84023167, 0.07558702, -23.54780996, -0.00078397, -28.40231667, -0.02165963, -2.84023167, -0.07558702, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22005, 2005, 0.0, 62.03523685, 0.01567944, 62.03523685, 0.04703831, 43.42466579, -727.64006097, 0.05, 2, 0, 72005, 23005, 2, 3)
    ops.uniaxialMaterial('LimitState', 42005, 15.50880921, 6.297e-05, 46.52642764, 0.00018892, 155.08809212, 0.00062975, -15.50880921, -6.297e-05, -46.52642764, -0.00018892, -155.08809212, -0.00062975, 0.4, 0.3, 0.003, 0.0, 0.0, 22005, 2)
    ops.limitCurve('ThreePoint', 12005, 2005, 0.0, 62.03523685, 0.01567944, 62.03523685, 0.04703831, 43.42466579, -727.64006097, 0.05, 2, 0, 72005, 23005, 1, 3)
    ops.uniaxialMaterial('LimitState', 32005, 15.50880921, 6.297e-05, 46.52642764, 0.00018892, 155.08809212, 0.00062975, -15.50880921, -6.297e-05, -46.52642764, -0.00018892, -155.08809212, -0.00062975, 0.4, 0.3, 0.003, 0.0, 0.0, 12005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2005, 99999, 'P', 42005, 'Vy', 32005, 'Vz', 22005, 'My', 12005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172005, 72005, 172005, 2005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123005, 123005, 23005, 2005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172006, 22.8, 0.0, 6.425)
    ops.node(123006, 22.8, 0.0, 8.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2006, 172006, 123006, 0.0625, 32743280.02781167, 13643033.34492153, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22006, 18.90310733, 0.00083059, 22.72738093, 0.02907255, 2.27273809, 0.10167354, -18.90310733, -0.00083059, -22.72738093, -0.02907255, -2.27273809, -0.10167354, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12006, 18.90310733, 0.00083059, 22.72738093, 0.02907255, 2.27273809, 0.10167354, -18.90310733, -0.00083059, -22.72738093, -0.02907255, -2.27273809, -0.10167354, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22006, 2006, 0.0, 72.15731112, 0.01661174, 72.15731112, 0.04983523, 50.51011778, -1079.13678388, 0.05, 2, 0, 72006, 23006, 2, 3)
    ops.uniaxialMaterial('LimitState', 42006, 18.03932778, 6.854e-05, 54.11798334, 0.00020563, 180.3932778, 0.00068545, -18.03932778, -6.854e-05, -54.11798334, -0.00020563, -180.3932778, -0.00068545, 0.4, 0.3, 0.003, 0.0, 0.0, 22006, 2)
    ops.limitCurve('ThreePoint', 12006, 2006, 0.0, 72.15731112, 0.01661174, 72.15731112, 0.04983523, 50.51011778, -1079.13678388, 0.05, 2, 0, 72006, 23006, 1, 3)
    ops.uniaxialMaterial('LimitState', 32006, 18.03932778, 6.854e-05, 54.11798334, 0.00020563, 180.3932778, 0.00068545, -18.03932778, -6.854e-05, -54.11798334, -0.00020563, -180.3932778, -0.00068545, 0.4, 0.3, 0.003, 0.0, 0.0, 12006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2006, 99999, 'P', 42006, 'Vy', 32006, 'Vz', 22006, 'My', 12006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172006, 72006, 172006, 2006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123006, 123006, 23006, 2006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172007, 0.0, 4.6, 6.45)
    ops.node(123007, 0.0, 4.6, 8.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2007, 172007, 123007, 0.0625, 31552901.56802548, 13147042.32001062, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22007, 24.10582669, 0.00078395, 29.01232288, 0.03058814, 2.90123229, 0.09678194, -24.10582669, -0.00078395, -29.01232288, -0.03058814, -2.90123229, -0.09678194, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12007, 24.10582669, 0.00078395, 29.01232288, 0.03058814, 2.90123229, 0.09678194, -24.10582669, -0.00078395, -29.01232288, -0.03058814, -2.90123229, -0.09678194, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22007, 2007, 0.0, 77.57364284, 0.01567895, 77.57364284, 0.04703684, 54.30154999, -1112.73325559, 0.05, 2, 0, 72007, 23007, 2, 3)
    ops.uniaxialMaterial('LimitState', 42007, 19.39341071, 7.647e-05, 58.18023213, 0.00022941, 193.9341071, 0.0007647, -19.39341071, -7.647e-05, -58.18023213, -0.00022941, -193.9341071, -0.0007647, 0.4, 0.3, 0.003, 0.0, 0.0, 22007, 2)
    ops.limitCurve('ThreePoint', 12007, 2007, 0.0, 77.57364284, 0.01567895, 77.57364284, 0.04703684, 54.30154999, -1112.73325559, 0.05, 2, 0, 72007, 23007, 1, 3)
    ops.uniaxialMaterial('LimitState', 32007, 19.39341071, 7.647e-05, 58.18023213, 0.00022941, 193.9341071, 0.0007647, -19.39341071, -7.647e-05, -58.18023213, -0.00022941, -193.9341071, -0.0007647, 0.4, 0.3, 0.003, 0.0, 0.0, 12007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2007, 99999, 'P', 42007, 'Vy', 32007, 'Vz', 22007, 'My', 12007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172007, 72007, 172007, 2007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123007, 123007, 23007, 2007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172008, 4.95, 4.6, 6.45)
    ops.node(123008, 4.95, 4.6, 8.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2008, 172008, 123008, 0.0625, 29383932.72866164, 12243305.30360902, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22008, 38.14088145, 0.0008691, 45.95572698, 0.03209499, 4.5955727, 0.08826936, -38.14088145, -0.0008691, -45.95572698, -0.03209499, -4.5955727, -0.08826936, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12008, 38.14088145, 0.0008691, 45.95572698, 0.03209499, 4.5955727, 0.08826936, -38.14088145, -0.0008691, -45.95572698, -0.03209499, -4.5955727, -0.08826936, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22008, 2008, 0.0, 72.34513322, 0.01738194, 72.34513322, 0.05214582, 50.64159325, -922.53418663, 0.05, 2, 0, 72008, 23008, 2, 3)
    ops.uniaxialMaterial('LimitState', 42008, 18.0862833, 7.658e-05, 54.25884991, 0.00022974, 180.86283304, 0.0007658, -18.0862833, -7.658e-05, -54.25884991, -0.00022974, -180.86283304, -0.0007658, 0.4, 0.3, 0.003, 0.0, 0.0, 22008, 2)
    ops.limitCurve('ThreePoint', 12008, 2008, 0.0, 72.34513322, 0.01738194, 72.34513322, 0.05214582, 50.64159325, -922.53418663, 0.05, 2, 0, 72008, 23008, 1, 3)
    ops.uniaxialMaterial('LimitState', 32008, 18.0862833, 7.658e-05, 54.25884991, 0.00022974, 180.86283304, 0.0007658, -18.0862833, -7.658e-05, -54.25884991, -0.00022974, -180.86283304, -0.0007658, 0.4, 0.3, 0.003, 0.0, 0.0, 12008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2008, 99999, 'P', 42008, 'Vy', 32008, 'Vz', 22008, 'My', 12008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172008, 72008, 172008, 2008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123008, 123008, 23008, 2008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172009, 9.9, 4.6, 6.45)
    ops.node(123009, 9.9, 4.6, 8.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2009, 172009, 123009, 0.0625, 32173567.68366997, 13405653.20152915, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22009, 37.78508046, 0.00084021, 45.29000297, 0.0344653, 4.5290003, 0.09684652, -37.78508046, -0.00084021, -45.29000297, -0.0344653, -4.5290003, -0.09684652, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12009, 37.78508046, 0.00084021, 45.29000297, 0.0344653, 4.5290003, 0.09684652, -37.78508046, -0.00084021, -45.29000297, -0.0344653, -4.5290003, -0.09684652, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22009, 2009, 0.0, 80.19567312, 0.01680422, 80.19567312, 0.05041265, 56.13697119, -1011.77645593, 0.05, 2, 0, 72009, 23009, 2, 3)
    ops.uniaxialMaterial('LimitState', 42009, 20.04891828, 7.753e-05, 60.14675484, 0.00023259, 200.4891828, 0.0007753, -20.04891828, -7.753e-05, -60.14675484, -0.00023259, -200.4891828, -0.0007753, 0.4, 0.3, 0.003, 0.0, 0.0, 22009, 2)
    ops.limitCurve('ThreePoint', 12009, 2009, 0.0, 80.19567312, 0.01680422, 80.19567312, 0.05041265, 56.13697119, -1011.77645593, 0.05, 2, 0, 72009, 23009, 1, 3)
    ops.uniaxialMaterial('LimitState', 32009, 20.04891828, 7.753e-05, 60.14675484, 0.00023259, 200.4891828, 0.0007753, -20.04891828, -7.753e-05, -60.14675484, -0.00023259, -200.4891828, -0.0007753, 0.4, 0.3, 0.003, 0.0, 0.0, 12009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2009, 99999, 'P', 42009, 'Vy', 32009, 'Vz', 22009, 'My', 12009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172009, 72009, 172009, 2009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123009, 123009, 23009, 2009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172010, 12.9, 4.6, 6.45)
    ops.node(123010, 12.9, 4.6, 8.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2010, 172010, 123010, 0.0625, 34740952.45671548, 14475396.85696478, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22010, 36.08785639, 0.00084354, 42.91753085, 0.03410982, 4.29175308, 0.10015914, -36.08785639, -0.00084354, -42.91753085, -0.03410982, -4.29175308, -0.10015914, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12010, 36.08785639, 0.00084354, 42.91753085, 0.03410982, 4.29175308, 0.10015914, -36.08785639, -0.00084354, -42.91753085, -0.03410982, -4.29175308, -0.10015914, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22010, 2010, 0.0, 85.27851039, 0.01687085, 85.27851039, 0.05061256, 59.69495727, -1004.18436663, 0.05, 2, 0, 72010, 23010, 2, 3)
    ops.uniaxialMaterial('LimitState', 42010, 21.3196276, 7.635e-05, 63.95888279, 0.00022905, 213.19627598, 0.00076351, -21.3196276, -7.635e-05, -63.95888279, -0.00022905, -213.19627598, -0.00076351, 0.4, 0.3, 0.003, 0.0, 0.0, 22010, 2)
    ops.limitCurve('ThreePoint', 12010, 2010, 0.0, 85.27851039, 0.01687085, 85.27851039, 0.05061256, 59.69495727, -1004.18436663, 0.05, 2, 0, 72010, 23010, 1, 3)
    ops.uniaxialMaterial('LimitState', 32010, 21.3196276, 7.635e-05, 63.95888279, 0.00022905, 213.19627598, 0.00076351, -21.3196276, -7.635e-05, -63.95888279, -0.00022905, -213.19627598, -0.00076351, 0.4, 0.3, 0.003, 0.0, 0.0, 12010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2010, 99999, 'P', 42010, 'Vy', 32010, 'Vz', 22010, 'My', 12010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172010, 72010, 172010, 2010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123010, 123010, 23010, 2010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172011, 17.85, 4.6, 6.45)
    ops.node(123011, 17.85, 4.6, 8.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2011, 172011, 123011, 0.0625, 31173006.9773976, 12988752.907249, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22011, 36.60429812, 0.0008613, 43.96154518, 0.03520766, 4.39615452, 0.0950943, -36.60429812, -0.0008613, -43.96154518, -0.03520766, -4.39615452, -0.0950943, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12011, 36.60429812, 0.0008613, 43.96154518, 0.03520766, 4.39615452, 0.0950943, -36.60429812, -0.0008613, -43.96154518, -0.03520766, -4.39615452, -0.0950943, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22011, 2011, 0.0, 79.58405591, 0.01722599, 79.58405591, 0.05167797, 55.70883914, -1042.41700439, 0.05, 2, 0, 72011, 23011, 2, 3)
    ops.uniaxialMaterial('LimitState', 42011, 19.89601398, 7.941e-05, 59.68804193, 0.00023822, 198.96013978, 0.00079408, -19.89601398, -7.941e-05, -59.68804193, -0.00023822, -198.96013978, -0.00079408, 0.4, 0.3, 0.003, 0.0, 0.0, 22011, 2)
    ops.limitCurve('ThreePoint', 12011, 2011, 0.0, 79.58405591, 0.01722599, 79.58405591, 0.05167797, 55.70883914, -1042.41700439, 0.05, 2, 0, 72011, 23011, 1, 3)
    ops.uniaxialMaterial('LimitState', 32011, 19.89601398, 7.941e-05, 59.68804193, 0.00023822, 198.96013978, 0.00079408, -19.89601398, -7.941e-05, -59.68804193, -0.00023822, -198.96013978, -0.00079408, 0.4, 0.3, 0.003, 0.0, 0.0, 12011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2011, 99999, 'P', 42011, 'Vy', 32011, 'Vz', 22011, 'My', 12011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172011, 72011, 172011, 2011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123011, 123011, 23011, 2011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172012, 22.8, 4.6, 6.45)
    ops.node(123012, 22.8, 4.6, 8.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2012, 172012, 123012, 0.0625, 33548430.65450311, 13978512.77270963, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22012, 24.35802532, 0.00075304, 29.14296016, 0.02993897, 2.91429602, 0.09854657, -24.35802532, -0.00075304, -29.14296016, -0.02993897, -2.91429602, -0.09854657, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12012, 24.35802532, 0.00075304, 29.14296016, 0.02993897, 2.91429602, 0.09854657, -24.35802532, -0.00075304, -29.14296016, -0.02993897, -2.91429602, -0.09854657, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22012, 2012, 0.0, 81.23372134, 0.01506083, 81.23372134, 0.04518248, 56.86360494, -1099.1065063, 0.05, 2, 0, 72012, 23012, 2, 3)
    ops.uniaxialMaterial('LimitState', 42012, 20.30843034, 7.531e-05, 60.92529101, 0.00022594, 203.08430335, 0.00075315, -20.30843034, -7.531e-05, -60.92529101, -0.00022594, -203.08430335, -0.00075315, 0.4, 0.3, 0.003, 0.0, 0.0, 22012, 2)
    ops.limitCurve('ThreePoint', 12012, 2012, 0.0, 81.23372134, 0.01506083, 81.23372134, 0.04518248, 56.86360494, -1099.1065063, 0.05, 2, 0, 72012, 23012, 1, 3)
    ops.uniaxialMaterial('LimitState', 32012, 20.30843034, 7.531e-05, 60.92529101, 0.00022594, 203.08430335, 0.00075315, -20.30843034, -7.531e-05, -60.92529101, -0.00022594, -203.08430335, -0.00075315, 0.4, 0.3, 0.003, 0.0, 0.0, 12012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2012, 99999, 'P', 42012, 'Vy', 32012, 'Vz', 22012, 'My', 12012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172012, 72012, 172012, 2012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123012, 123012, 23012, 2012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172013, 0.0, 9.2, 6.425)
    ops.node(123013, 0.0, 9.2, 8.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2013, 172013, 123013, 0.0625, 30419003.01311731, 12674584.58879888, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22013, 19.23545048, 0.00075419, 23.28430068, 0.03332595, 2.32843007, 0.10390886, -19.23545048, -0.00075419, -23.28430068, -0.03332595, -2.32843007, -0.10390886, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12013, 19.23545048, 0.00075419, 23.28430068, 0.03332595, 2.32843007, 0.10390886, -19.23545048, -0.00075419, -23.28430068, -0.03332595, -2.32843007, -0.10390886, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22013, 2013, 0.0, 72.64146125, 0.01508383, 72.64146125, 0.0452515, 50.84902288, -1358.53850258, 0.05, 2, 0, 72013, 23013, 2, 3)
    ops.uniaxialMaterial('LimitState', 42013, 18.16036531, 7.428e-05, 54.48109594, 0.00022283, 181.60365313, 0.00074277, -18.16036531, -7.428e-05, -54.48109594, -0.00022283, -181.60365313, -0.00074277, 0.4, 0.3, 0.003, 0.0, 0.0, 22013, 2)
    ops.limitCurve('ThreePoint', 12013, 2013, 0.0, 72.64146125, 0.01508383, 72.64146125, 0.0452515, 50.84902288, -1358.53850258, 0.05, 2, 0, 72013, 23013, 1, 3)
    ops.uniaxialMaterial('LimitState', 32013, 18.16036531, 7.428e-05, 54.48109594, 0.00022283, 181.60365313, 0.00074277, -18.16036531, -7.428e-05, -54.48109594, -0.00022283, -181.60365313, -0.00074277, 0.4, 0.3, 0.003, 0.0, 0.0, 12013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2013, 99999, 'P', 42013, 'Vy', 32013, 'Vz', 22013, 'My', 12013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172013, 72013, 172013, 2013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123013, 123013, 23013, 2013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172014, 4.95, 9.2, 6.425)
    ops.node(123014, 4.95, 9.2, 8.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2014, 172014, 123014, 0.0625, 31490873.63180486, 13121197.34658536, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22014, 24.48780078, 0.00080383, 29.47450823, 0.02187307, 2.94745082, 0.07682763, -24.48780078, -0.00080383, -29.47450823, -0.02187307, -2.94745082, -0.07682763, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12014, 24.48780078, 0.00080383, 29.47450823, 0.02187307, 2.94745082, 0.07682763, -24.48780078, -0.00080383, -29.47450823, -0.02187307, -2.94745082, -0.07682763, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22014, 2014, 0.0, 66.58908977, 0.01607654, 66.58908977, 0.04822963, 46.61236284, -721.13387404, 0.05, 2, 0, 72014, 23014, 2, 3)
    ops.uniaxialMaterial('LimitState', 42014, 16.64727244, 6.577e-05, 49.94181732, 0.00019731, 166.47272441, 0.00065771, -16.64727244, -6.577e-05, -49.94181732, -0.00019731, -166.47272441, -0.00065771, 0.4, 0.3, 0.003, 0.0, 0.0, 22014, 2)
    ops.limitCurve('ThreePoint', 12014, 2014, 0.0, 66.58908977, 0.01607654, 66.58908977, 0.04822963, 46.61236284, -721.13387404, 0.05, 2, 0, 72014, 23014, 1, 3)
    ops.uniaxialMaterial('LimitState', 32014, 16.64727244, 6.577e-05, 49.94181732, 0.00019731, 166.47272441, 0.00065771, -16.64727244, -6.577e-05, -49.94181732, -0.00019731, -166.47272441, -0.00065771, 0.4, 0.3, 0.003, 0.0, 0.0, 12014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2014, 99999, 'P', 42014, 'Vy', 32014, 'Vz', 22014, 'My', 12014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172014, 72014, 172014, 2014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123014, 123014, 23014, 2014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172015, 9.9, 9.2, 6.425)
    ops.node(123015, 9.9, 9.2, 8.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2015, 172015, 123015, 0.0625, 30833253.78289012, 12847189.07620422, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22015, 21.46487091, 0.0008016, 25.91534786, 0.02891059, 2.59153479, 0.09675842, -21.46487091, -0.0008016, -25.91534786, -0.02891059, -2.59153479, -0.09675842, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12015, 21.46487091, 0.0008016, 25.91534786, 0.02891059, 2.59153479, 0.09675842, -21.46487091, -0.0008016, -25.91534786, -0.02891059, -2.59153479, -0.09675842, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22015, 2015, 0.0, 70.87663603, 0.01603208, 70.87663603, 0.04809624, 49.61364522, -1004.9012878, 0.05, 2, 0, 72015, 23015, 2, 3)
    ops.uniaxialMaterial('LimitState', 42015, 17.71915901, 7.15e-05, 53.15747703, 0.0002145, 177.19159009, 0.00071499, -17.71915901, -7.15e-05, -53.15747703, -0.0002145, -177.19159009, -0.00071499, 0.4, 0.3, 0.003, 0.0, 0.0, 22015, 2)
    ops.limitCurve('ThreePoint', 12015, 2015, 0.0, 70.87663603, 0.01603208, 70.87663603, 0.04809624, 49.61364522, -1004.9012878, 0.05, 2, 0, 72015, 23015, 1, 3)
    ops.uniaxialMaterial('LimitState', 32015, 17.71915901, 7.15e-05, 53.15747703, 0.0002145, 177.19159009, 0.00071499, -17.71915901, -7.15e-05, -53.15747703, -0.0002145, -177.19159009, -0.00071499, 0.4, 0.3, 0.003, 0.0, 0.0, 12015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2015, 99999, 'P', 42015, 'Vy', 32015, 'Vz', 22015, 'My', 12015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172015, 72015, 172015, 2015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123015, 123015, 23015, 2015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172016, 12.9, 9.2, 6.425)
    ops.node(123016, 12.9, 9.2, 8.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2016, 172016, 123016, 0.0625, 30876581.74064044, 12865242.39193352, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22016, 22.18974918, 0.00073537, 26.78757833, 0.0305879, 2.67875783, 0.09848932, -22.18974918, -0.00073537, -26.78757833, -0.0305879, -2.67875783, -0.09848932, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12016, 22.18974918, 0.00073537, 26.78757833, 0.0305879, 2.67875783, 0.09848932, -22.18974918, -0.00073537, -26.78757833, -0.0305879, -2.67875783, -0.09848932, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22016, 2016, 0.0, 72.05744954, 0.01470743, 72.05744954, 0.04412229, 50.44021468, -1053.50426944, 0.05, 2, 0, 72016, 23016, 2, 3)
    ops.uniaxialMaterial('LimitState', 42016, 18.01436239, 7.259e-05, 54.04308716, 0.00021776, 180.14362386, 0.00072588, -18.01436239, -7.259e-05, -54.04308716, -0.00021776, -180.14362386, -0.00072588, 0.4, 0.3, 0.003, 0.0, 0.0, 22016, 2)
    ops.limitCurve('ThreePoint', 12016, 2016, 0.0, 72.05744954, 0.01470743, 72.05744954, 0.04412229, 50.44021468, -1053.50426944, 0.05, 2, 0, 72016, 23016, 1, 3)
    ops.uniaxialMaterial('LimitState', 32016, 18.01436239, 7.259e-05, 54.04308716, 0.00021776, 180.14362386, 0.00072588, -18.01436239, -7.259e-05, -54.04308716, -0.00021776, -180.14362386, -0.00072588, 0.4, 0.3, 0.003, 0.0, 0.0, 12016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2016, 99999, 'P', 42016, 'Vy', 32016, 'Vz', 22016, 'My', 12016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172016, 72016, 172016, 2016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123016, 123016, 23016, 2016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172017, 17.85, 9.2, 6.425)
    ops.node(123017, 17.85, 9.2, 8.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2017, 172017, 123017, 0.0625, 32628585.07440268, 13595243.78100112, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22017, 24.83471161, 0.00076317, 29.79727498, 0.02487535, 2.9797275, 0.08105341, -24.83471161, -0.00076317, -29.79727498, -0.02487535, -2.9797275, -0.08105341, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12017, 24.83471161, 0.00076317, 29.79727498, 0.02487535, 2.9797275, 0.08105341, -24.83471161, -0.00076317, -29.79727498, -0.02487535, -2.9797275, -0.08105341, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22017, 2017, 0.0, 74.51421926, 0.01526342, 74.51421926, 0.04579027, 52.15995348, -903.31057432, 0.05, 2, 0, 72017, 23017, 2, 3)
    ops.uniaxialMaterial('LimitState', 42017, 18.62855482, 7.103e-05, 55.88566445, 0.0002131, 186.28554816, 0.00071033, -18.62855482, -7.103e-05, -55.88566445, -0.0002131, -186.28554816, -0.00071033, 0.4, 0.3, 0.003, 0.0, 0.0, 22017, 2)
    ops.limitCurve('ThreePoint', 12017, 2017, 0.0, 74.51421926, 0.01526342, 74.51421926, 0.04579027, 52.15995348, -903.31057432, 0.05, 2, 0, 72017, 23017, 1, 3)
    ops.uniaxialMaterial('LimitState', 32017, 18.62855482, 7.103e-05, 55.88566445, 0.0002131, 186.28554816, 0.00071033, -18.62855482, -7.103e-05, -55.88566445, -0.0002131, -186.28554816, -0.00071033, 0.4, 0.3, 0.003, 0.0, 0.0, 12017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2017, 99999, 'P', 42017, 'Vy', 32017, 'Vz', 22017, 'My', 12017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172017, 72017, 172017, 2017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123017, 123017, 23017, 2017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172018, 22.8, 9.2, 6.425)
    ops.node(123018, 22.8, 9.2, 8.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2018, 172018, 123018, 0.0625, 31340563.46419737, 13058568.11008224, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22018, 19.33615828, 0.00074116, 23.3479106, 0.03256659, 2.33479106, 0.10402061, -19.33615828, -0.00074116, -23.3479106, -0.03256659, -2.33479106, -0.10402061, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12018, 19.33615828, 0.00074116, 23.3479106, 0.03256659, 2.33479106, 0.10402061, -19.33615828, -0.00074116, -23.3479106, -0.03256659, -2.33479106, -0.10402061, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22018, 2018, 0.0, 72.36201036, 0.01482321, 72.36201036, 0.04446964, 50.65340726, -1240.35562736, 0.05, 2, 0, 72018, 23018, 2, 3)
    ops.uniaxialMaterial('LimitState', 42018, 18.09050259, 7.182e-05, 54.27150777, 0.00021545, 180.90502591, 0.00071816, -18.09050259, -7.182e-05, -54.27150777, -0.00021545, -180.90502591, -0.00071816, 0.4, 0.3, 0.003, 0.0, 0.0, 22018, 2)
    ops.limitCurve('ThreePoint', 12018, 2018, 0.0, 72.36201036, 0.01482321, 72.36201036, 0.04446964, 50.65340726, -1240.35562736, 0.05, 2, 0, 72018, 23018, 1, 3)
    ops.uniaxialMaterial('LimitState', 32018, 18.09050259, 7.182e-05, 54.27150777, 0.00021545, 180.90502591, 0.00071816, -18.09050259, -7.182e-05, -54.27150777, -0.00021545, -180.90502591, -0.00071816, 0.4, 0.3, 0.003, 0.0, 0.0, 12018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2018, 99999, 'P', 42018, 'Vy', 32018, 'Vz', 22018, 'My', 12018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172018, 72018, 172018, 2018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123018, 123018, 23018, 2018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173001, 0.0, 0.0, 9.125)
    ops.node(124001, 0.0, 0.0, 11.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3001, 173001, 124001, 0.0625, 34483736.1112569, 14368223.37969038, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23001, 14.50342368, 0.00066657, 17.36742627, 0.03708623, 1.73674263, 0.13708623, -14.50342368, -0.00066657, -17.36742627, -0.03708623, -1.73674263, -0.13708623, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13001, 14.50342368, 0.00066657, 17.36742627, 0.03708623, 1.73674263, 0.13708623, -14.50342368, -0.00066657, -17.36742627, -0.03708623, -1.73674263, -0.13708623, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23001, 3001, 0.0, 78.73537423, 0.01333132, 78.73537423, 0.03999395, 55.11476196, -3737.49476763, 0.05, 2, 0, 73001, 24001, 2, 3)
    ops.uniaxialMaterial('LimitState', 43001, 19.68384356, 7.102e-05, 59.05153067, 0.00021306, 196.83843557, 0.00071019, -19.68384356, -7.102e-05, -59.05153067, -0.00021306, -196.83843557, -0.00071019, 0.4, 0.3, 0.003, 0.0, 0.0, 23001, 2)
    ops.limitCurve('ThreePoint', 13001, 3001, 0.0, 78.73537423, 0.01333132, 78.73537423, 0.03999395, 55.11476196, -3737.49476763, 0.05, 2, 0, 73001, 24001, 1, 3)
    ops.uniaxialMaterial('LimitState', 33001, 19.68384356, 7.102e-05, 59.05153067, 0.00021306, 196.83843557, 0.00071019, -19.68384356, -7.102e-05, -59.05153067, -0.00021306, -196.83843557, -0.00071019, 0.4, 0.3, 0.003, 0.0, 0.0, 13001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3001, 99999, 'P', 43001, 'Vy', 33001, 'Vz', 23001, 'My', 13001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173001, 73001, 173001, 3001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124001, 124001, 24001, 3001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173002, 4.95, 0.0, 9.125)
    ops.node(124002, 4.95, 0.0, 11.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3002, 173002, 124002, 0.0625, 31381350.19339714, 13075562.58058214, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23002, 15.2993623, 0.00080073, 18.50910073, 0.02277453, 1.85091007, 0.08607072, -15.2993623, -0.00080073, -18.50910073, -0.02277453, -1.85091007, -0.08607072, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13002, 15.2993623, 0.00080073, 18.50910073, 0.02277453, 1.85091007, 0.08607072, -15.2993623, -0.00080073, -18.50910073, -0.02277453, -1.85091007, -0.08607072, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23002, 3002, 0.0, 56.12064743, 0.01601459, 56.12064743, 0.04804378, 39.2844532, -996.02685394, 0.05, 2, 0, 73002, 24002, 2, 3)
    ops.uniaxialMaterial('LimitState', 43002, 14.03016186, 5.562e-05, 42.09048557, 0.00016687, 140.30161857, 0.00055625, -14.03016186, -5.562e-05, -42.09048557, -0.00016687, -140.30161857, -0.00055625, 0.4, 0.3, 0.003, 0.0, 0.0, 23002, 2)
    ops.limitCurve('ThreePoint', 13002, 3002, 0.0, 56.12064743, 0.01601459, 56.12064743, 0.04804378, 39.2844532, -996.02685394, 0.05, 2, 0, 73002, 24002, 1, 3)
    ops.uniaxialMaterial('LimitState', 33002, 14.03016186, 5.562e-05, 42.09048557, 0.00016687, 140.30161857, 0.00055625, -14.03016186, -5.562e-05, -42.09048557, -0.00016687, -140.30161857, -0.00055625, 0.4, 0.3, 0.003, 0.0, 0.0, 13002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3002, 99999, 'P', 43002, 'Vy', 33002, 'Vz', 23002, 'My', 13002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173002, 73002, 173002, 3002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124002, 124002, 24002, 3002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173005, 17.85, 0.0, 9.125)
    ops.node(124005, 17.85, 0.0, 11.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3005, 173005, 124005, 0.0625, 28676680.34297918, 11948616.80957466, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23005, 16.08350734, 0.00072441, 19.60104357, 0.0265232, 1.96010436, 0.08858852, -16.08350734, -0.00072441, -19.60104357, -0.0265232, -1.96010436, -0.08858852, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13005, 16.08350734, 0.00072441, 19.60104357, 0.0265232, 1.96010436, 0.08858852, -16.08350734, -0.00072441, -19.60104357, -0.0265232, -1.96010436, -0.08858852, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23005, 3005, 0.0, 57.21556823, 0.01448824, 57.21556823, 0.04346473, 40.05089776, -1195.6783647, 0.05, 2, 0, 73005, 24005, 2, 3)
    ops.uniaxialMaterial('LimitState', 43005, 14.30389206, 6.206e-05, 42.91167618, 0.00018618, 143.03892059, 0.00062059, -14.30389206, -6.206e-05, -42.91167618, -0.00018618, -143.03892059, -0.00062059, 0.4, 0.3, 0.003, 0.0, 0.0, 23005, 2)
    ops.limitCurve('ThreePoint', 13005, 3005, 0.0, 57.21556823, 0.01448824, 57.21556823, 0.04346473, 40.05089776, -1195.6783647, 0.05, 2, 0, 73005, 24005, 1, 3)
    ops.uniaxialMaterial('LimitState', 33005, 14.30389206, 6.206e-05, 42.91167618, 0.00018618, 143.03892059, 0.00062059, -14.30389206, -6.206e-05, -42.91167618, -0.00018618, -143.03892059, -0.00062059, 0.4, 0.3, 0.003, 0.0, 0.0, 13005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3005, 99999, 'P', 43005, 'Vy', 33005, 'Vz', 23005, 'My', 13005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173005, 73005, 173005, 3005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124005, 124005, 24005, 3005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173006, 22.8, 0.0, 9.125)
    ops.node(124006, 22.8, 0.0, 11.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3006, 173006, 124006, 0.0625, 30540629.80366812, 12725262.41819505, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23006, 14.06995152, 0.00071353, 17.08030066, 0.04472603, 1.70803007, 0.14414298, -14.06995152, -0.00071353, -17.08030066, -0.04472603, -1.70803007, -0.14414298, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13006, 14.06995152, 0.00071353, 17.08030066, 0.04472603, 1.70803007, 0.14414298, -14.06995152, -0.00071353, -17.08030066, -0.04472603, -1.70803007, -0.14414298, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23006, 3006, 0.0, 79.42467199, 0.01427062, 79.42467199, 0.04281187, 55.5972704, -5529.20762879, 0.05, 2, 0, 73006, 24006, 2, 3)
    ops.uniaxialMaterial('LimitState', 43006, 19.856168, 8.089e-05, 59.56850399, 0.00024267, 198.56167998, 0.0008089, -19.856168, -8.089e-05, -59.56850399, -0.00024267, -198.56167998, -0.0008089, 0.4, 0.3, 0.003, 0.0, 0.0, 23006, 2)
    ops.limitCurve('ThreePoint', 13006, 3006, 0.0, 79.42467199, 0.01427062, 79.42467199, 0.04281187, 55.5972704, -5529.20762879, 0.05, 2, 0, 73006, 24006, 1, 3)
    ops.uniaxialMaterial('LimitState', 33006, 19.856168, 8.089e-05, 59.56850399, 0.00024267, 198.56167998, 0.0008089, -19.856168, -8.089e-05, -59.56850399, -0.00024267, -198.56167998, -0.0008089, 0.4, 0.3, 0.003, 0.0, 0.0, 13006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3006, 99999, 'P', 43006, 'Vy', 33006, 'Vz', 23006, 'My', 13006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173006, 73006, 173006, 3006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124006, 124006, 24006, 3006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173007, 0.0, 4.6, 9.15)
    ops.node(124007, 0.0, 4.6, 11.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3007, 173007, 124007, 0.0625, 33180308.59191259, 13825128.57996358, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23007, 16.17726046, 0.00071819, 19.45442664, 0.04004752, 1.94544266, 0.13811621, -16.17726046, -0.00071819, -19.45442664, -0.04004752, -1.94544266, -0.13811621, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13007, 16.17726046, 0.00071819, 19.45442664, 0.04004752, 1.94544266, 0.13811621, -16.17726046, -0.00071819, -19.45442664, -0.04004752, -1.94544266, -0.13811621, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23007, 3007, 0.0, 80.85609256, 0.01436388, 80.85609256, 0.04309163, 56.5992648, -2710.59711378, 0.05, 2, 0, 73007, 24007, 2, 3)
    ops.uniaxialMaterial('LimitState', 43007, 20.21402314, 7.58e-05, 60.64206942, 0.00022739, 202.14023141, 0.00075796, -20.21402314, -7.58e-05, -60.64206942, -0.00022739, -202.14023141, -0.00075796, 0.4, 0.3, 0.003, 0.0, 0.0, 23007, 2)
    ops.limitCurve('ThreePoint', 13007, 3007, 0.0, 80.85609256, 0.01436388, 80.85609256, 0.04309163, 56.5992648, -2710.59711378, 0.05, 2, 0, 73007, 24007, 1, 3)
    ops.uniaxialMaterial('LimitState', 33007, 20.21402314, 7.58e-05, 60.64206942, 0.00022739, 202.14023141, 0.00075796, -20.21402314, -7.58e-05, -60.64206942, -0.00022739, -202.14023141, -0.00075796, 0.4, 0.3, 0.003, 0.0, 0.0, 13007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3007, 99999, 'P', 43007, 'Vy', 33007, 'Vz', 23007, 'My', 13007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173007, 73007, 173007, 3007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124007, 124007, 24007, 3007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173008, 4.95, 4.6, 9.15)
    ops.node(124008, 4.95, 4.6, 11.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3008, 173008, 124008, 0.0625, 30732571.37929501, 12805238.07470626, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23008, 27.25792109, 0.0008658, 32.99789619, 0.02526163, 3.29978962, 0.07785723, -27.25792109, -0.0008658, -32.99789619, -0.02526163, -3.29978962, -0.07785723, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13008, 27.25792109, 0.0008658, 32.99789619, 0.02526163, 3.29978962, 0.07785723, -27.25792109, -0.0008658, -32.99789619, -0.02526163, -3.29978962, -0.07785723, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23008, 3008, 0.0, 51.27642367, 0.01731591, 51.27642367, 0.05194772, 35.89349657, -728.52752111, 0.05, 2, 0, 73008, 24008, 2, 3)
    ops.uniaxialMaterial('LimitState', 43008, 12.81910592, 5.19e-05, 38.45731775, 0.00015569, 128.19105917, 0.00051896, -12.81910592, -5.19e-05, -38.45731775, -0.00015569, -128.19105917, -0.00051896, 0.4, 0.3, 0.003, 0.0, 0.0, 23008, 2)
    ops.limitCurve('ThreePoint', 13008, 3008, 0.0, 51.27642367, 0.01731591, 51.27642367, 0.05194772, 35.89349657, -728.52752111, 0.05, 2, 0, 73008, 24008, 1, 3)
    ops.uniaxialMaterial('LimitState', 33008, 12.81910592, 5.19e-05, 38.45731775, 0.00015569, 128.19105917, 0.00051896, -12.81910592, -5.19e-05, -38.45731775, -0.00015569, -128.19105917, -0.00051896, 0.4, 0.3, 0.003, 0.0, 0.0, 13008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3008, 99999, 'P', 43008, 'Vy', 33008, 'Vz', 23008, 'My', 13008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173008, 73008, 173008, 3008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124008, 124008, 24008, 3008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173009, 9.9, 4.6, 9.15)
    ops.node(124009, 9.9, 4.6, 11.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3009, 173009, 124009, 0.0625, 27774971.16689382, 11572904.65287242, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23009, 27.45761185, 0.00079114, 33.45989291, 0.03004746, 3.34598929, 0.08015794, -27.45761185, -0.00079114, -33.45989291, -0.03004746, -3.34598929, -0.08015794, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13009, 27.45761185, 0.00079114, 33.45989291, 0.03004746, 3.34598929, 0.08015794, -27.45761185, -0.00079114, -33.45989291, -0.03004746, -3.34598929, -0.08015794, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23009, 3009, 0.0, 54.74595746, 0.01582276, 54.74595746, 0.04746829, 38.32217022, -785.15108106, 0.05, 2, 0, 73009, 24009, 2, 3)
    ops.uniaxialMaterial('LimitState', 43009, 13.68648936, 6.131e-05, 41.05946809, 0.00018392, 136.86489365, 0.00061308, -13.68648936, -6.131e-05, -41.05946809, -0.00018392, -136.86489365, -0.00061308, 0.4, 0.3, 0.003, 0.0, 0.0, 23009, 2)
    ops.limitCurve('ThreePoint', 13009, 3009, 0.0, 54.74595746, 0.01582276, 54.74595746, 0.04746829, 38.32217022, -785.15108106, 0.05, 2, 0, 73009, 24009, 1, 3)
    ops.uniaxialMaterial('LimitState', 33009, 13.68648936, 6.131e-05, 41.05946809, 0.00018392, 136.86489365, 0.00061308, -13.68648936, -6.131e-05, -41.05946809, -0.00018392, -136.86489365, -0.00061308, 0.4, 0.3, 0.003, 0.0, 0.0, 13009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3009, 99999, 'P', 43009, 'Vy', 33009, 'Vz', 23009, 'My', 13009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173009, 73009, 173009, 3009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124009, 124009, 24009, 3009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173010, 12.9, 4.6, 9.15)
    ops.node(124010, 12.9, 4.6, 11.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3010, 173010, 124010, 0.0625, 29920603.87423344, 12466918.2809306, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23010, 27.70392589, 0.0008188, 33.60203122, 0.02542119, 3.36020312, 0.07717508, -27.70392589, -0.0008188, -33.60203122, -0.02542119, -3.36020312, -0.07717508, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13010, 27.70392589, 0.0008188, 33.60203122, 0.02542119, 3.36020312, 0.07717508, -27.70392589, -0.0008188, -33.60203122, -0.02542119, -3.36020312, -0.07717508, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23010, 3010, 0.0, 44.63730293, 0.01637596, 44.63730293, 0.04912788, 31.24611205, -654.00608192, 0.05, 2, 0, 73010, 24010, 2, 3)
    ops.uniaxialMaterial('LimitState', 43010, 11.15932573, 4.64e-05, 33.4779772, 0.00013921, 111.59325734, 0.00046403, -11.15932573, -4.64e-05, -33.4779772, -0.00013921, -111.59325734, -0.00046403, 0.4, 0.3, 0.003, 0.0, 0.0, 23010, 2)
    ops.limitCurve('ThreePoint', 13010, 3010, 0.0, 44.63730293, 0.01637596, 44.63730293, 0.04912788, 31.24611205, -654.00608192, 0.05, 2, 0, 73010, 24010, 1, 3)
    ops.uniaxialMaterial('LimitState', 33010, 11.15932573, 4.64e-05, 33.4779772, 0.00013921, 111.59325734, 0.00046403, -11.15932573, -4.64e-05, -33.4779772, -0.00013921, -111.59325734, -0.00046403, 0.4, 0.3, 0.003, 0.0, 0.0, 13010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3010, 99999, 'P', 43010, 'Vy', 33010, 'Vz', 23010, 'My', 13010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173010, 73010, 173010, 3010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124010, 124010, 24010, 3010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173011, 17.85, 4.6, 9.15)
    ops.node(124011, 17.85, 4.6, 11.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3011, 173011, 124011, 0.0625, 28494389.09857085, 11872662.12440452, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23011, 26.99519255, 0.00083875, 32.85862688, 0.02511198, 3.28586269, 0.07624328, -26.99519255, -0.00083875, -32.85862688, -0.02511198, -3.28586269, -0.07624328, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13011, 26.99519255, 0.00083875, 32.85862688, 0.02511198, 3.28586269, 0.07624328, -26.99519255, -0.00083875, -32.85862688, -0.02511198, -3.28586269, -0.07624328, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23011, 3011, 0.0, 42.93550386, 0.01677492, 42.93550386, 0.05032475, 30.05485271, -689.02798304, 0.05, 2, 0, 73011, 24011, 2, 3)
    ops.uniaxialMaterial('LimitState', 43011, 10.73387597, 4.687e-05, 32.2016279, 0.0001406, 107.33875966, 0.00046868, -10.73387597, -4.687e-05, -32.2016279, -0.0001406, -107.33875966, -0.00046868, 0.4, 0.3, 0.003, 0.0, 0.0, 23011, 2)
    ops.limitCurve('ThreePoint', 13011, 3011, 0.0, 42.93550386, 0.01677492, 42.93550386, 0.05032475, 30.05485271, -689.02798304, 0.05, 2, 0, 73011, 24011, 1, 3)
    ops.uniaxialMaterial('LimitState', 33011, 10.73387597, 4.687e-05, 32.2016279, 0.0001406, 107.33875966, 0.00046868, -10.73387597, -4.687e-05, -32.2016279, -0.0001406, -107.33875966, -0.00046868, 0.4, 0.3, 0.003, 0.0, 0.0, 13011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3011, 99999, 'P', 43011, 'Vy', 33011, 'Vz', 23011, 'My', 13011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173011, 73011, 173011, 3011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124011, 124011, 24011, 3011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173012, 22.8, 4.6, 9.15)
    ops.node(124012, 22.8, 4.6, 11.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3012, 173012, 124012, 0.0625, 36225502.4401664, 15093959.35006933, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23012, 16.04133371, 0.00066475, 19.05670988, 0.03681171, 1.90567099, 0.13605311, -16.04133371, -0.00066475, -19.05670988, -0.03681171, -1.90567099, -0.13605311, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13012, 16.04133371, 0.00066475, 19.05670988, 0.03681171, 1.90567099, 0.13605311, -16.04133371, -0.00066475, -19.05670988, -0.03681171, -1.90567099, -0.13605311, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23012, 3012, 0.0, 85.20469446, 0.01329496, 85.20469446, 0.03988489, 59.64328612, -2492.1842992, 0.05, 2, 0, 73012, 24012, 2, 3)
    ops.uniaxialMaterial('LimitState', 43012, 21.30117361, 7.316e-05, 63.90352084, 0.00021948, 213.01173614, 0.00073159, -21.30117361, -7.316e-05, -63.90352084, -0.00021948, -213.01173614, -0.00073159, 0.4, 0.3, 0.003, 0.0, 0.0, 23012, 2)
    ops.limitCurve('ThreePoint', 13012, 3012, 0.0, 85.20469446, 0.01329496, 85.20469446, 0.03988489, 59.64328612, -2492.1842992, 0.05, 2, 0, 73012, 24012, 1, 3)
    ops.uniaxialMaterial('LimitState', 33012, 21.30117361, 7.316e-05, 63.90352084, 0.00021948, 213.01173614, 0.00073159, -21.30117361, -7.316e-05, -63.90352084, -0.00021948, -213.01173614, -0.00073159, 0.4, 0.3, 0.003, 0.0, 0.0, 13012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3012, 99999, 'P', 43012, 'Vy', 33012, 'Vz', 23012, 'My', 13012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173012, 73012, 173012, 3012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124012, 124012, 24012, 3012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173013, 0.0, 9.2, 9.125)
    ops.node(124013, 0.0, 9.2, 11.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3013, 173013, 124013, 0.0625, 34914939.33983225, 14547891.39159677, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23013, 14.6613868, 0.00071592, 17.52581227, 0.03690906, 1.75258123, 0.13690906, -14.6613868, -0.00071592, -17.52581227, -0.03690906, -1.75258123, -0.13690906, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13013, 14.6613868, 0.00071592, 17.52581227, 0.03690906, 1.75258123, 0.13690906, -14.6613868, -0.00071592, -17.52581227, -0.03690906, -1.75258123, -0.13690906, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23013, 3013, 0.0, 79.79807839, 0.01431839, 79.79807839, 0.04295518, 55.85865487, -3773.79791796, 0.05, 2, 0, 73013, 24013, 2, 3)
    ops.uniaxialMaterial('LimitState', 43013, 19.9495196, 7.109e-05, 59.84855879, 0.00021326, 199.49519597, 0.00071088, -19.9495196, -7.109e-05, -59.84855879, -0.00021326, -199.49519597, -0.00071088, 0.4, 0.3, 0.003, 0.0, 0.0, 23013, 2)
    ops.limitCurve('ThreePoint', 13013, 3013, 0.0, 79.79807839, 0.01431839, 79.79807839, 0.04295518, 55.85865487, -3773.79791796, 0.05, 2, 0, 73013, 24013, 1, 3)
    ops.uniaxialMaterial('LimitState', 33013, 19.9495196, 7.109e-05, 59.84855879, 0.00021326, 199.49519597, 0.00071088, -19.9495196, -7.109e-05, -59.84855879, -0.00021326, -199.49519597, -0.00071088, 0.4, 0.3, 0.003, 0.0, 0.0, 13013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3013, 99999, 'P', 43013, 'Vy', 33013, 'Vz', 23013, 'My', 13013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173013, 73013, 173013, 3013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124013, 124013, 24013, 3013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173014, 4.95, 9.2, 9.125)
    ops.node(124014, 4.95, 9.2, 11.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3014, 173014, 124014, 0.0625, 32789356.50358199, 13662231.87649249, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23014, 15.8769635, 0.00071586, 19.11975653, 0.02264948, 1.91197565, 0.08643026, -15.8769635, -0.00071586, -19.11975653, -0.02264948, -1.91197565, -0.08643026, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13014, 15.8769635, 0.00071586, 19.11975653, 0.02264948, 1.91197565, 0.08643026, -15.8769635, -0.00071586, -19.11975653, -0.02264948, -1.91197565, -0.08643026, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23014, 3014, 0.0, 60.16537283, 0.01431718, 60.16537283, 0.04295154, 42.11576098, -1014.23534892, 0.05, 2, 0, 73014, 24014, 2, 3)
    ops.uniaxialMaterial('LimitState', 43014, 15.04134321, 5.707e-05, 45.12402962, 0.00017122, 150.41343207, 0.00057073, -15.04134321, -5.707e-05, -45.12402962, -0.00017122, -150.41343207, -0.00057073, 0.4, 0.3, 0.003, 0.0, 0.0, 23014, 2)
    ops.limitCurve('ThreePoint', 13014, 3014, 0.0, 60.16537283, 0.01431718, 60.16537283, 0.04295154, 42.11576098, -1014.23534892, 0.05, 2, 0, 73014, 24014, 1, 3)
    ops.uniaxialMaterial('LimitState', 33014, 15.04134321, 5.707e-05, 45.12402962, 0.00017122, 150.41343207, 0.00057073, -15.04134321, -5.707e-05, -45.12402962, -0.00017122, -150.41343207, -0.00057073, 0.4, 0.3, 0.003, 0.0, 0.0, 13014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3014, 99999, 'P', 43014, 'Vy', 33014, 'Vz', 23014, 'My', 13014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173014, 73014, 173014, 3014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124014, 124014, 24014, 3014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173015, 9.9, 9.2, 9.125)
    ops.node(124015, 9.9, 9.2, 11.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3015, 173015, 124015, 0.0625, 31659380.94517132, 13191408.72715472, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23015, 14.54171602, 0.0007207, 17.58400057, 0.02677736, 1.75840006, 0.09090148, -14.54171602, -0.0007207, -17.58400057, -0.02677736, -1.75840006, -0.09090148, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13015, 14.54171602, 0.0007207, 17.58400057, 0.02677736, 1.75840006, 0.09090148, -14.54171602, -0.0007207, -17.58400057, -0.02677736, -1.75840006, -0.09090148, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23015, 3015, 0.0, 62.76301912, 0.01441401, 62.76301912, 0.04324203, 43.93411338, -1443.31852527, 0.05, 2, 0, 73015, 24015, 2, 3)
    ops.uniaxialMaterial('LimitState', 43015, 15.69075478, 6.166e-05, 47.07226434, 0.00018499, 156.90754779, 0.00061662, -15.69075478, -6.166e-05, -47.07226434, -0.00018499, -156.90754779, -0.00061662, 0.4, 0.3, 0.003, 0.0, 0.0, 23015, 2)
    ops.limitCurve('ThreePoint', 13015, 3015, 0.0, 62.76301912, 0.01441401, 62.76301912, 0.04324203, 43.93411338, -1443.31852527, 0.05, 2, 0, 73015, 24015, 1, 3)
    ops.uniaxialMaterial('LimitState', 33015, 15.69075478, 6.166e-05, 47.07226434, 0.00018499, 156.90754779, 0.00061662, -15.69075478, -6.166e-05, -47.07226434, -0.00018499, -156.90754779, -0.00061662, 0.4, 0.3, 0.003, 0.0, 0.0, 13015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3015, 99999, 'P', 43015, 'Vy', 33015, 'Vz', 23015, 'My', 13015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173015, 73015, 173015, 3015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124015, 124015, 24015, 3015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173016, 12.9, 9.2, 9.125)
    ops.node(124016, 12.9, 9.2, 11.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3016, 173016, 124016, 0.0625, 32553738.24122203, 13564057.60050918, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23016, 15.32287926, 0.0007104, 18.47383409, 0.02680794, 1.84738341, 0.09117728, -15.32287926, -0.0007104, -18.47383409, -0.02680794, -1.84738341, -0.09117728, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13016, 15.32287926, 0.0007104, 18.47383409, 0.02680794, 1.84738341, 0.09117728, -15.32287926, -0.0007104, -18.47383409, -0.02680794, -1.84738341, -0.09117728, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23016, 3016, 0.0, 66.09280621, 0.014208, 66.09280621, 0.04262401, 46.26496435, -1607.1523603, 0.05, 2, 0, 73016, 24016, 2, 3)
    ops.uniaxialMaterial('LimitState', 43016, 16.52320155, 6.315e-05, 49.56960466, 0.00018945, 165.23201552, 0.00063149, -16.52320155, -6.315e-05, -49.56960466, -0.00018945, -165.23201552, -0.00063149, 0.4, 0.3, 0.003, 0.0, 0.0, 23016, 2)
    ops.limitCurve('ThreePoint', 13016, 3016, 0.0, 66.09280621, 0.014208, 66.09280621, 0.04262401, 46.26496435, -1607.1523603, 0.05, 2, 0, 73016, 24016, 1, 3)
    ops.uniaxialMaterial('LimitState', 33016, 16.52320155, 6.315e-05, 49.56960466, 0.00018945, 165.23201552, 0.00063149, -16.52320155, -6.315e-05, -49.56960466, -0.00018945, -165.23201552, -0.00063149, 0.4, 0.3, 0.003, 0.0, 0.0, 13016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3016, 99999, 'P', 43016, 'Vy', 33016, 'Vz', 23016, 'My', 13016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173016, 73016, 173016, 3016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124016, 124016, 24016, 3016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173017, 17.85, 9.2, 9.125)
    ops.node(124017, 17.85, 9.2, 11.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3017, 173017, 124017, 0.0625, 29433028.67200749, 12263761.94666979, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23017, 15.8577675, 0.00071762, 19.29007092, 0.02654266, 1.92900709, 0.0889996, -15.8577675, -0.00071762, -19.29007092, -0.02654266, -1.92900709, -0.0889996, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13017, 15.8577675, 0.00071762, 19.29007092, 0.02654266, 1.92900709, 0.0889996, -15.8577675, -0.00071762, -19.29007092, -0.02654266, -1.92900709, -0.0889996, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23017, 3017, 0.0, 58.67162074, 0.01435246, 58.67162074, 0.04305739, 41.07013452, -1202.6668878, 0.05, 2, 0, 73017, 24017, 2, 3)
    ops.uniaxialMaterial('LimitState', 43017, 14.66790518, 6.2e-05, 44.00371555, 0.00018601, 146.67905184, 0.00062003, -14.66790518, -6.2e-05, -44.00371555, -0.00018601, -146.67905184, -0.00062003, 0.4, 0.3, 0.003, 0.0, 0.0, 23017, 2)
    ops.limitCurve('ThreePoint', 13017, 3017, 0.0, 58.67162074, 0.01435246, 58.67162074, 0.04305739, 41.07013452, -1202.6668878, 0.05, 2, 0, 73017, 24017, 1, 3)
    ops.uniaxialMaterial('LimitState', 33017, 14.66790518, 6.2e-05, 44.00371555, 0.00018601, 146.67905184, 0.00062003, -14.66790518, -6.2e-05, -44.00371555, -0.00018601, -146.67905184, -0.00062003, 0.4, 0.3, 0.003, 0.0, 0.0, 13017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3017, 99999, 'P', 43017, 'Vy', 33017, 'Vz', 23017, 'My', 13017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173017, 73017, 173017, 3017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124017, 124017, 24017, 3017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173018, 22.8, 9.2, 9.125)
    ops.node(124018, 22.8, 9.2, 11.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3018, 173018, 124018, 0.0625, 30170868.96795686, 12571195.40331536, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23018, 14.23153334, 0.00069671, 17.29501497, 0.04098286, 1.7295015, 0.14026316, -14.23153334, -0.00069671, -17.29501497, -0.04098286, -1.7295015, -0.14026316, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13018, 14.23153334, 0.00069671, 17.29501497, 0.04098286, 1.7295015, 0.14026316, -14.23153334, -0.00069671, -17.29501497, -0.04098286, -1.7295015, -0.14026316, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23018, 3018, 0.0, 69.18474091, 0.01393424, 69.18474091, 0.04180271, 48.42931864, -3509.49003739, 0.05, 2, 0, 73018, 24018, 2, 3)
    ops.uniaxialMaterial('LimitState', 43018, 17.29618523, 7.132e-05, 51.88855569, 0.00021397, 172.96185228, 0.00071325, -17.29618523, -7.132e-05, -51.88855569, -0.00021397, -172.96185228, -0.00071325, 0.4, 0.3, 0.003, 0.0, 0.0, 23018, 2)
    ops.limitCurve('ThreePoint', 13018, 3018, 0.0, 69.18474091, 0.01393424, 69.18474091, 0.04180271, 48.42931864, -3509.49003739, 0.05, 2, 0, 73018, 24018, 1, 3)
    ops.uniaxialMaterial('LimitState', 33018, 17.29618523, 7.132e-05, 51.88855569, 0.00021397, 172.96185228, 0.00071325, -17.29618523, -7.132e-05, -51.88855569, -0.00021397, -172.96185228, -0.00071325, 0.4, 0.3, 0.003, 0.0, 0.0, 13018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3018, 99999, 'P', 43018, 'Vy', 33018, 'Vz', 23018, 'My', 13018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173018, 73018, 173018, 3018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124018, 124018, 24018, 3018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170003, 9.9, 0.0, 0.0)
    ops.node(124019, 9.9, 0.0, 1.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4046, 170003, 124019, 0.09, 31286074.76146504, 13035864.48394377, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24046, 78.22360279, 0.00062275, 93.82374512, 0.06161406, 9.38237451, 0.16161406, -78.22360279, -0.00062275, -93.82374512, -0.06161406, -9.38237451, -0.16161406, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14046, 78.22360279, 0.00062275, 93.82374512, 0.05274031, 9.38237451, 0.14356105, -78.22360279, -0.00062275, -93.82374512, -0.05274031, -9.38237451, -0.14356105, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24046, 4046, 0.0, 144.56009695, 0.01245507, 144.56009695, 0.0373652, 101.19206787, -3447.92878973, 0.05, 2, 0, 70003, 24019, 2, 3)
    ops.uniaxialMaterial('LimitState', 44046, 36.14002424, 6.469e-05, 108.42007272, 0.00019406, 361.40024239, 0.00064688, -36.14002424, -6.469e-05, -108.42007272, -0.00019406, -361.40024239, -0.00064688, 0.4, 0.3, 0.003, 0.0, 0.0, 24046, 2)
    ops.limitCurve('ThreePoint', 14046, 4046, 0.0, 176.60364125, 0.01245507, 176.60364125, 0.0373652, 123.62254887, -5611.9000653, 0.05, 2, 0, 70003, 24019, 1, 3)
    ops.uniaxialMaterial('LimitState', 34046, 44.15091031, 7.903e-05, 132.45273094, 0.00023708, 441.50910312, 0.00079027, -44.15091031, -7.903e-05, -132.45273094, -0.00023708, -441.50910312, -0.00079027, 0.4, 0.3, 0.003, 0.0, 0.0, 14046, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4046, 99999, 'P', 44046, 'Vy', 34046, 'Vz', 24046, 'My', 14046, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170003, 70003, 170003, 4046, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124019, 124019, 24019, 4046, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174019, 9.9, 0.0, 1.95)
    ops.node(121003, 9.9, 0.0, 3.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4047, 174019, 121003, 0.09, 30493132.69180626, 12705471.95491927, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24047, 59.51567758, 0.00064887, 71.57449338, 0.06097549, 7.15744934, 0.16097549, -59.51567758, -0.00064887, -71.57449338, -0.06097549, -7.15744934, -0.16097549, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14047, 56.99114835, 0.00064887, 68.53845467, 0.05219844, 6.85384547, 0.14342874, -56.99114835, -0.00064887, -68.53845467, -0.05219844, -6.85384547, -0.14342874, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24047, 4047, 0.0, 145.86003405, 0.01297747, 145.86003405, 0.03893241, 102.10202383, -3863.81615613, 0.05, 2, 0, 74019, 21003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44047, 36.46500851, 6.697e-05, 109.39502554, 0.0002009, 364.65008512, 0.00066967, -36.46500851, -6.697e-05, -109.39502554, -0.0002009, -364.65008512, -0.00066967, 0.4, 0.3, 0.003, 0.0, 0.0, 24047, 2)
    ops.limitCurve('ThreePoint', 14047, 4047, 0.0, 180.78942523, 0.01297747, 180.78942523, 0.03893241, 126.55259766, -6514.64583059, 0.05, 2, 0, 74019, 21003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34047, 45.19735631, 8.3e-05, 135.59206893, 0.00024901, 451.97356308, 0.00083004, -45.19735631, -8.3e-05, -135.59206893, -0.00024901, -451.97356308, -0.00083004, 0.4, 0.3, 0.003, 0.0, 0.0, 14047, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4047, 99999, 'P', 44047, 'Vy', 34047, 'Vz', 24047, 'My', 14047, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174019, 74019, 174019, 4047, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121003, 121003, 21003, 4047, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170004, 12.9, 0.0, 0.0)
    ops.node(124020, 12.9, 0.0, 1.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4048, 170004, 124020, 0.09, 28169917.09349846, 11737465.45562436, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24048, 77.04788952, 0.0006885, 92.82866592, 0.06085385, 9.28286659, 0.16085385, -77.04788952, -0.0006885, -92.82866592, -0.06085385, -9.28286659, -0.16085385, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14048, 77.04788952, 0.0006885, 92.82866592, 0.05210027, 9.28286659, 0.131473, -77.04788952, -0.0006885, -92.82866592, -0.05210027, -9.28286659, -0.131473, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24048, 4048, 0.0, 134.35379225, 0.01376994, 134.35379225, 0.04130981, 94.04765458, -3416.51251097, 0.05, 2, 0, 70004, 24020, 2, 3)
    ops.uniaxialMaterial('LimitState', 44048, 33.58844806, 6.677e-05, 100.76534419, 0.00020032, 335.88448063, 0.00066772, -33.58844806, -6.677e-05, -100.76534419, -0.00020032, -335.88448063, -0.00066772, 0.4, 0.3, 0.003, 0.0, 0.0, 24048, 2)
    ops.limitCurve('ThreePoint', 14048, 4048, 0.0, 166.13205516, 0.01376994, 166.13205516, 0.04130981, 116.29243861, -5551.80385005, 0.05, 2, 0, 70004, 24020, 1, 3)
    ops.uniaxialMaterial('LimitState', 34048, 41.53301379, 8.256e-05, 124.59904137, 0.00024769, 415.3301379, 0.00082565, -41.53301379, -8.256e-05, -124.59904137, -0.00024769, -415.3301379, -0.00082565, 0.4, 0.3, 0.003, 0.0, 0.0, 14048, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4048, 99999, 'P', 44048, 'Vy', 34048, 'Vz', 24048, 'My', 14048, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170004, 70004, 170004, 4048, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124020, 124020, 24020, 4048, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174020, 12.9, 0.0, 1.95)
    ops.node(121004, 12.9, 0.0, 3.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4049, 174020, 121004, 0.09, 35409311.70032092, 14753879.87513372, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24049, 63.21134644, 0.00060133, 74.96913618, 0.05647335, 7.49691362, 0.15647335, -63.21134644, -0.00060133, -74.96913618, -0.05647335, -7.49691362, -0.15647335, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14049, 60.18866707, 0.00060133, 71.38421553, 0.04834441, 7.13842155, 0.14834441, -60.18866707, -0.00060133, -71.38421553, -0.04834441, -7.13842155, -0.14834441, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24049, 4049, 0.0, 158.5208194, 0.01202663, 158.5208194, 0.03607988, 110.96457358, -3647.63125417, 0.05, 2, 0, 74020, 21004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44049, 39.63020485, 6.268e-05, 118.89061455, 0.00018803, 396.30204849, 0.00062675, -39.63020485, -6.268e-05, -118.89061455, -0.00018803, -396.30204849, -0.00062675, 0.4, 0.3, 0.003, 0.0, 0.0, 24049, 2)
    ops.limitCurve('ThreePoint', 14049, 4049, 0.0, 191.78977221, 0.01202663, 191.78977221, 0.03607988, 134.25284055, -6094.51687317, 0.05, 2, 0, 74020, 21004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34049, 47.94744305, 7.583e-05, 143.84232916, 0.00022749, 479.47443052, 0.00075829, -47.94744305, -7.583e-05, -143.84232916, -0.00022749, -479.47443052, -0.00075829, 0.4, 0.3, 0.003, 0.0, 0.0, 14049, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4049, 99999, 'P', 44049, 'Vy', 34049, 'Vz', 24049, 'My', 14049, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174020, 74020, 174020, 4049, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121004, 121004, 21004, 4049, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171003, 9.9, 0.0, 3.725)
    ops.node(124021, 9.9, 0.0, 4.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4051, 171003, 124021, 0.09, 30898239.49953636, 12874266.45814015, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24051, 49.06587915, 0.00056471, 59.07482095, 0.05258307, 5.90748209, 0.1505828, -49.06587915, -0.00056471, -59.07482095, -0.05258307, -5.90748209, -0.1505828, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14051, 49.06587915, 0.00056471, 59.07482095, 0.05258307, 5.90748209, 0.1505828, -49.06587915, -0.00056471, -59.07482095, -0.05258307, -5.90748209, -0.1505828, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24051, 4051, 0.0, 171.10799898, 0.01129425, 171.10799898, 0.03388274, 119.77559929, -5867.65413036, 0.05, 2, 0, 71003, 24021, 2, 3)
    ops.uniaxialMaterial('LimitState', 44051, 42.77699974, 5.981e-05, 128.33099923, 0.00017942, 427.76999745, 0.00059808, -42.77699974, -5.981e-05, -128.33099923, -0.00017942, -427.76999745, -0.00059808, 0.4, 0.3, 0.003, 0.0, 0.0, 24051, 2)
    ops.limitCurve('ThreePoint', 14051, 4051, 0.0, 171.10799898, 0.01129425, 171.10799898, 0.03388274, 119.77559929, -5867.65413036, 0.05, 2, 0, 71003, 24021, 1, 3)
    ops.uniaxialMaterial('LimitState', 34051, 42.77699974, 5.981e-05, 128.33099923, 0.00017942, 427.76999745, 0.00059808, -42.77699974, -5.981e-05, -128.33099923, -0.00017942, -427.76999745, -0.00059808, 0.4, 0.3, 0.003, 0.0, 0.0, 14051, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4051, 99999, 'P', 44051, 'Vy', 34051, 'Vz', 24051, 'My', 14051, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171003, 71003, 171003, 4051, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124021, 124021, 24021, 4051, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174021, 9.9, 0.0, 5.0)
    ops.node(122003, 9.9, 0.0, 5.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4052, 174021, 122003, 0.09, 31191729.16530515, 12996553.81887715, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24052, 48.48184995, 0.00056555, 58.39034302, 0.05146987, 5.8390343, 0.15146987, -48.48184995, -0.00056555, -58.39034302, -0.05146987, -5.8390343, -0.15146987, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14052, 48.48184995, 0.00056555, 58.39034302, 0.05146987, 5.8390343, 0.15146987, -48.48184995, -0.00056555, -58.39034302, -0.05146987, -5.8390343, -0.15146987, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24052, 4052, 0.0, 158.95072046, 0.01131106, 158.95072046, 0.03393317, 111.26550432, -5013.37636848, 0.05, 2, 0, 74021, 22003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44052, 39.73768012, 5.504e-05, 119.21304035, 0.00016511, 397.37680116, 0.00055036, -39.73768012, -5.504e-05, -119.21304035, -0.00016511, -397.37680116, -0.00055036, 0.4, 0.3, 0.003, 0.0, 0.0, 24052, 2)
    ops.limitCurve('ThreePoint', 14052, 4052, 0.0, 158.95072046, 0.01131106, 158.95072046, 0.03393317, 111.26550432, -5013.37636848, 0.05, 2, 0, 74021, 22003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34052, 39.73768012, 5.504e-05, 119.21304035, 0.00016511, 397.37680116, 0.00055036, -39.73768012, -5.504e-05, -119.21304035, -0.00016511, -397.37680116, -0.00055036, 0.4, 0.3, 0.003, 0.0, 0.0, 14052, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4052, 99999, 'P', 44052, 'Vy', 34052, 'Vz', 24052, 'My', 14052, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174021, 74021, 174021, 4052, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122003, 122003, 22003, 4052, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171004, 12.9, 0.0, 3.725)
    ops.node(124022, 12.9, 0.0, 4.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4053, 171004, 124022, 0.09, 30328327.43030292, 12636803.09595955, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24053, 48.80960899, 0.00057294, 58.83876538, 0.05272119, 5.88387654, 0.14919125, -48.80960899, -0.00057294, -58.83876538, -0.05272119, -5.88387654, -0.14919125, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14053, 48.80960899, 0.00057294, 58.83876538, 0.05272119, 5.88387654, 0.14919125, -48.80960899, -0.00057294, -58.83876538, -0.05272119, -5.88387654, -0.14919125, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24053, 4053, 0.0, 165.68514585, 0.01145886, 165.68514585, 0.03437659, 115.9796021, -5547.72232014, 0.05, 2, 0, 71004, 24022, 2, 3)
    ops.uniaxialMaterial('LimitState', 44053, 41.42128646, 5.9e-05, 124.26385939, 0.000177, 414.21286464, 0.00059001, -41.42128646, -5.9e-05, -124.26385939, -0.000177, -414.21286464, -0.00059001, 0.4, 0.3, 0.003, 0.0, 0.0, 24053, 2)
    ops.limitCurve('ThreePoint', 14053, 4053, 0.0, 165.68514585, 0.01145886, 165.68514585, 0.03437659, 115.9796021, -5547.72232014, 0.05, 2, 0, 71004, 24022, 1, 3)
    ops.uniaxialMaterial('LimitState', 34053, 41.42128646, 5.9e-05, 124.26385939, 0.000177, 414.21286464, 0.00059001, -41.42128646, -5.9e-05, -124.26385939, -0.000177, -414.21286464, -0.00059001, 0.4, 0.3, 0.003, 0.0, 0.0, 14053, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4053, 99999, 'P', 44053, 'Vy', 34053, 'Vz', 24053, 'My', 14053, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171004, 71004, 171004, 4053, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124022, 124022, 24022, 4053, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174022, 12.9, 0.0, 5.0)
    ops.node(122004, 12.9, 0.0, 5.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4054, 174022, 122004, 0.09, 29991180.37062142, 12496325.15442559, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24054, 45.99800053, 0.00057731, 55.55010961, 0.0534865, 5.55501096, 0.15230839, -45.99800053, -0.00057731, -55.55010961, -0.0534865, -5.55501096, -0.15230839, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14054, 45.99800053, 0.00057731, 55.55010961, 0.0534865, 5.55501096, 0.15230839, -45.99800053, -0.00057731, -55.55010961, -0.0534865, -5.55501096, -0.15230839, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24054, 4054, 0.0, 158.22208548, 0.01154613, 158.22208548, 0.0346384, 110.75545983, -5430.98061179, 0.05, 2, 0, 74022, 22004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44054, 39.55552137, 5.698e-05, 118.66656411, 0.00017093, 395.55521369, 0.00056977, -39.55552137, -5.698e-05, -118.66656411, -0.00017093, -395.55521369, -0.00056977, 0.4, 0.3, 0.003, 0.0, 0.0, 24054, 2)
    ops.limitCurve('ThreePoint', 14054, 4054, 0.0, 158.22208548, 0.01154613, 158.22208548, 0.0346384, 110.75545983, -5430.98061179, 0.05, 2, 0, 74022, 22004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34054, 39.55552137, 5.698e-05, 118.66656411, 0.00017093, 395.55521369, 0.00056977, -39.55552137, -5.698e-05, -118.66656411, -0.00017093, -395.55521369, -0.00056977, 0.4, 0.3, 0.003, 0.0, 0.0, 14054, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4054, 99999, 'P', 44054, 'Vy', 34054, 'Vz', 24054, 'My', 14054, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174022, 74022, 174022, 4054, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122004, 122004, 22004, 4054, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172003, 9.9, 0.0, 6.425)
    ops.node(124023, 9.9, 0.0, 7.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4056, 172003, 124023, 0.0625, 30639966.19199067, 12766652.57999611, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24056, 34.19244255, 0.00064206, 41.21657366, 0.05805397, 4.12165737, 0.15805397, -34.19244255, -0.00064206, -41.21657366, -0.05805397, -4.12165737, -0.15805397, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14056, 34.19244255, 0.00064206, 41.21657366, 0.05805397, 4.12165737, 0.15805397, -34.19244255, -0.00064206, -41.21657366, -0.05805397, -4.12165737, -0.15805397, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24056, 4056, 0.0, 114.8404321, 0.01284113, 114.8404321, 0.03852338, 80.38830247, -5161.24782241, 0.05, 2, 0, 72003, 24023, 2, 3)
    ops.uniaxialMaterial('LimitState', 44056, 28.71010803, 5.829e-05, 86.13032408, 0.00017487, 287.10108025, 0.0005829, -28.71010803, -5.829e-05, -86.13032408, -0.00017487, -287.10108025, -0.0005829, 0.4, 0.3, 0.003, 0.0, 0.0, 24056, 2)
    ops.limitCurve('ThreePoint', 14056, 4056, 0.0, 114.8404321, 0.01284113, 114.8404321, 0.03852338, 80.38830247, -5161.24782241, 0.05, 2, 0, 72003, 24023, 1, 3)
    ops.uniaxialMaterial('LimitState', 34056, 28.71010803, 5.829e-05, 86.13032408, 0.00017487, 287.10108025, 0.0005829, -28.71010803, -5.829e-05, -86.13032408, -0.00017487, -287.10108025, -0.0005829, 0.4, 0.3, 0.003, 0.0, 0.0, 14056, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4056, 99999, 'P', 44056, 'Vy', 34056, 'Vz', 24056, 'My', 14056, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172003, 72003, 172003, 4056, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124023, 124023, 24023, 4056, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174023, 9.9, 0.0, 7.7)
    ops.node(123003, 9.9, 0.0, 8.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4057, 174023, 123003, 0.0625, 33025542.08895647, 13760642.5370652, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24057, 31.74346736, 0.00062977, 38.07421848, 0.05635145, 3.80742185, 0.15635145, -31.74346736, -0.00062977, -38.07421848, -0.05635145, -3.80742185, -0.15635145, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14057, 31.74346736, 0.00062977, 38.07421848, 0.05635145, 3.80742185, 0.15635145, -31.74346736, -0.00062977, -38.07421848, -0.05635145, -3.80742185, -0.15635145, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24057, 4057, 0.0, 111.9746282, 0.01259541, 111.9746282, 0.03778623, 78.38223974, -5003.15375243, 0.05, 2, 0, 74023, 23003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44057, 27.99365705, 5.273e-05, 83.98097115, 0.00015819, 279.9365705, 0.0005273, -27.99365705, -5.273e-05, -83.98097115, -0.00015819, -279.9365705, -0.0005273, 0.4, 0.3, 0.003, 0.0, 0.0, 24057, 2)
    ops.limitCurve('ThreePoint', 14057, 4057, 0.0, 111.9746282, 0.01259541, 111.9746282, 0.03778623, 78.38223974, -5003.15375243, 0.05, 2, 0, 74023, 23003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34057, 27.99365705, 5.273e-05, 83.98097115, 0.00015819, 279.9365705, 0.0005273, -27.99365705, -5.273e-05, -83.98097115, -0.00015819, -279.9365705, -0.0005273, 0.4, 0.3, 0.003, 0.0, 0.0, 14057, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4057, 99999, 'P', 44057, 'Vy', 34057, 'Vz', 24057, 'My', 14057, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174023, 74023, 174023, 4057, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123003, 123003, 23003, 4057, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172004, 12.9, 0.0, 6.425)
    ops.node(124024, 12.9, 0.0, 7.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4058, 172004, 124024, 0.0625, 32380365.31471355, 13491818.88113065, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24058, 34.36383483, 0.00066703, 41.24000108, 0.05593045, 4.12400011, 0.15593045, -34.36383483, -0.00066703, -41.24000108, -0.05593045, -4.12400011, -0.15593045, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14058, 34.36383483, 0.00066703, 41.24000108, 0.05593045, 4.12400011, 0.15593045, -34.36383483, -0.00066703, -41.24000108, -0.05593045, -4.12400011, -0.15593045, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24058, 4058, 0.0, 117.4432302, 0.01334069, 117.4432302, 0.04002208, 82.21026114, -4986.64772915, 0.05, 2, 0, 72004, 24024, 2, 3)
    ops.uniaxialMaterial('LimitState', 44058, 29.36080755, 5.641e-05, 88.08242265, 0.00016922, 293.60807549, 0.00056407, -29.36080755, -5.641e-05, -88.08242265, -0.00016922, -293.60807549, -0.00056407, 0.4, 0.3, 0.003, 0.0, 0.0, 24058, 2)
    ops.limitCurve('ThreePoint', 14058, 4058, 0.0, 117.4432302, 0.01334069, 117.4432302, 0.04002208, 82.21026114, -4986.64772915, 0.05, 2, 0, 72004, 24024, 1, 3)
    ops.uniaxialMaterial('LimitState', 34058, 29.36080755, 5.641e-05, 88.08242265, 0.00016922, 293.60807549, 0.00056407, -29.36080755, -5.641e-05, -88.08242265, -0.00016922, -293.60807549, -0.00056407, 0.4, 0.3, 0.003, 0.0, 0.0, 14058, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4058, 99999, 'P', 44058, 'Vy', 34058, 'Vz', 24058, 'My', 14058, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172004, 72004, 172004, 4058, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124024, 124024, 24024, 4058, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174024, 12.9, 0.0, 7.7)
    ops.node(123004, 12.9, 0.0, 8.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4059, 174024, 123004, 0.0625, 30602999.13451618, 12751249.63938174, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24059, 31.13364428, 0.00063899, 37.59815322, 0.05803193, 3.75981532, 0.15803193, -31.13364428, -0.00063899, -37.59815322, -0.05803193, -3.75981532, -0.15803193, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14059, 31.13364428, 0.00063899, 37.59815322, 0.05803193, 3.75981532, 0.15803193, -31.13364428, -0.00063899, -37.59815322, -0.05803193, -3.75981532, -0.15803193, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24059, 4059, 0.0, 105.59493622, 0.01277973, 105.59493622, 0.0383392, 73.91645536, -4902.46215287, 0.05, 2, 0, 74024, 23004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44059, 26.39873406, 5.366e-05, 79.19620217, 0.00016099, 263.98734056, 0.00053662, -26.39873406, -5.366e-05, -79.19620217, -0.00016099, -263.98734056, -0.00053662, 0.4, 0.3, 0.003, 0.0, 0.0, 24059, 2)
    ops.limitCurve('ThreePoint', 14059, 4059, 0.0, 105.59493622, 0.01277973, 105.59493622, 0.0383392, 73.91645536, -4902.46215287, 0.05, 2, 0, 74024, 23004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34059, 26.39873406, 5.366e-05, 79.19620217, 0.00016099, 263.98734056, 0.00053662, -26.39873406, -5.366e-05, -79.19620217, -0.00016099, -263.98734056, -0.00053662, 0.4, 0.3, 0.003, 0.0, 0.0, 14059, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4059, 99999, 'P', 44059, 'Vy', 34059, 'Vz', 24059, 'My', 14059, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174024, 74024, 174024, 4059, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123004, 123004, 23004, 4059, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173003, 9.9, 0.0, 9.125)
    ops.node(124025, 9.9, 0.0, 10.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4061, 173003, 124025, 0.0625, 27276067.01378705, 11365027.92241127, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24061, 25.68868303, 0.00064711, 31.36318566, 0.03428495, 3.13631857, 0.09326276, -25.68868303, -0.00064711, -31.36318566, -0.03428495, -3.13631857, -0.09326276, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14061, 25.68868303, 0.00064711, 31.36318566, 0.03428495, 3.13631857, 0.09326276, -25.68868303, -0.00064711, -31.36318566, -0.03428495, -3.13631857, -0.09326276, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24061, 4061, 0.0, 65.32698925, 0.01294215, 65.32698925, 0.03882646, 45.72889247, -2436.47436142, 0.05, 2, 0, 73003, 24025, 2, 3)
    ops.uniaxialMaterial('LimitState', 44061, 16.33174731, 3.725e-05, 48.99524194, 0.00011174, 163.31747312, 0.00037248, -16.33174731, -3.725e-05, -48.99524194, -0.00011174, -163.31747312, -0.00037248, 0.4, 0.3, 0.003, 0.0, 0.0, 24061, 2)
    ops.limitCurve('ThreePoint', 14061, 4061, 0.0, 65.32698925, 0.01294215, 65.32698925, 0.03882646, 45.72889247, -2436.47436142, 0.05, 2, 0, 73003, 24025, 1, 3)
    ops.uniaxialMaterial('LimitState', 34061, 16.33174731, 3.725e-05, 48.99524194, 0.00011174, 163.31747312, 0.00037248, -16.33174731, -3.725e-05, -48.99524194, -0.00011174, -163.31747312, -0.00037248, 0.4, 0.3, 0.003, 0.0, 0.0, 14061, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4061, 99999, 'P', 44061, 'Vy', 34061, 'Vz', 24061, 'My', 14061, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173003, 73003, 173003, 4061, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124025, 124025, 24025, 4061, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174025, 9.9, 0.0, 10.4)
    ops.node(124003, 9.9, 0.0, 11.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4062, 174025, 124003, 0.0625, 32769380.76241527, 13653908.65100636, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24062, 23.19542272, 0.00056354, 27.95482472, 0.02570939, 2.79548247, 0.08218838, -23.19542272, -0.00056354, -27.95482472, -0.02570939, -2.79548247, -0.08218838, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14062, 23.19542272, 0.00056354, 27.95482472, 0.02570939, 2.79548247, 0.08218838, -23.19542272, -0.00056354, -27.95482472, -0.02570939, -2.79548247, -0.08218838, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24062, 4062, 0.0, 60.06157468, 0.01127083, 60.06157468, 0.03381249, 42.04310227, -2579.46150402, 0.05, 2, 0, 74025, 24003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44062, 15.01539367, 2.85e-05, 45.04618101, 8.551e-05, 150.15393669, 0.00028505, -15.01539367, -2.85e-05, -45.04618101, -8.551e-05, -150.15393669, -0.00028505, 0.4, 0.3, 0.003, 0.0, 0.0, 24062, 2)
    ops.limitCurve('ThreePoint', 14062, 4062, 0.0, 60.06157468, 0.01127083, 60.06157468, 0.03381249, 42.04310227, -2579.46150402, 0.05, 2, 0, 74025, 24003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34062, 15.01539367, 2.85e-05, 45.04618101, 8.551e-05, 150.15393669, 0.00028505, -15.01539367, -2.85e-05, -45.04618101, -8.551e-05, -150.15393669, -0.00028505, 0.4, 0.3, 0.003, 0.0, 0.0, 14062, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4062, 99999, 'P', 44062, 'Vy', 34062, 'Vz', 24062, 'My', 14062, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174025, 74025, 174025, 4062, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124003, 124003, 24003, 4062, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173004, 12.9, 0.0, 9.125)
    ops.node(124026, 12.9, 0.0, 10.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4063, 173004, 124026, 0.0625, 30044257.62528654, 12518440.67720272, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24063, 25.46405991, 0.00063694, 30.89771996, 0.03310362, 3.089772, 0.09417608, -25.46405991, -0.00063694, -30.89771996, -0.03310362, -3.089772, -0.09417608, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14063, 25.46405991, 0.00063694, 30.89771996, 0.03310362, 3.089772, 0.09417608, -25.46405991, -0.00063694, -30.89771996, -0.03310362, -3.089772, -0.09417608, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24063, 4063, 0.0, 71.0985745, 0.01273873, 71.0985745, 0.0382162, 49.76900215, -2417.50821551, 0.05, 2, 0, 73004, 24026, 2, 3)
    ops.uniaxialMaterial('LimitState', 44063, 17.77464363, 3.68e-05, 53.32393088, 0.00011041, 177.74643625, 0.00036803, -17.77464363, -3.68e-05, -53.32393088, -0.00011041, -177.74643625, -0.00036803, 0.4, 0.3, 0.003, 0.0, 0.0, 24063, 2)
    ops.limitCurve('ThreePoint', 14063, 4063, 0.0, 71.0985745, 0.01273873, 71.0985745, 0.0382162, 49.76900215, -2417.50821551, 0.05, 2, 0, 73004, 24026, 1, 3)
    ops.uniaxialMaterial('LimitState', 34063, 17.77464363, 3.68e-05, 53.32393088, 0.00011041, 177.74643625, 0.00036803, -17.77464363, -3.68e-05, -53.32393088, -0.00011041, -177.74643625, -0.00036803, 0.4, 0.3, 0.003, 0.0, 0.0, 14063, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4063, 99999, 'P', 44063, 'Vy', 34063, 'Vz', 24063, 'My', 14063, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173004, 73004, 173004, 4063, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124026, 124026, 24026, 4063, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174026, 12.9, 0.0, 10.4)
    ops.node(124004, 12.9, 0.0, 11.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4064, 174026, 124004, 0.0625, 31565896.55974474, 13152456.89989364, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24064, 23.59442609, 0.00057136, 28.55116183, 0.02677086, 2.85511618, 0.0830457, -23.59442609, -0.00057136, -28.55116183, -0.02677086, -2.85511618, -0.0830457, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14064, 23.59442609, 0.00057136, 28.55116183, 0.02677086, 2.85511618, 0.0830457, -23.59442609, -0.00057136, -28.55116183, -0.02677086, -2.85511618, -0.0830457, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24064, 4064, 0.0, 58.38166146, 0.01142715, 58.38166146, 0.03428146, 40.86716302, -2369.55672203, 0.05, 2, 0, 74026, 24004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44064, 14.59541536, 2.876e-05, 43.78624609, 8.629e-05, 145.95415364, 0.00028764, -14.59541536, -2.876e-05, -43.78624609, -8.629e-05, -145.95415364, -0.00028764, 0.4, 0.3, 0.003, 0.0, 0.0, 24064, 2)
    ops.limitCurve('ThreePoint', 14064, 4064, 0.0, 58.38166146, 0.01142715, 58.38166146, 0.03428146, 40.86716302, -2369.55672203, 0.05, 2, 0, 74026, 24004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34064, 14.59541536, 2.876e-05, 43.78624609, 8.629e-05, 145.95415364, 0.00028764, -14.59541536, -2.876e-05, -43.78624609, -8.629e-05, -145.95415364, -0.00028764, 0.4, 0.3, 0.003, 0.0, 0.0, 14064, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4064, 99999, 'P', 44064, 'Vy', 34064, 'Vz', 24064, 'My', 14064, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174026, 74026, 174026, 4064, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124004, 124004, 24004, 4064, '-orient', 0, 0, 1, 0, 1, 0)
