import openseespy.opensees as ops


def add_columns() -> None:
    """Add components of all columns to ops domain (plastic hinges, column elements and nodes)
    """
    # Create elastic column element nodes
    ops.node(170001, 0.0, 0.0, 0.0)
    ops.node(121001, 0.0, 0.0, 2.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1, 170001, 121001, 0.1225, 24563224.2069678, 10234676.75290325, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20001, 92.07016709, 0.00097981, 111.86719463, 0.01655359, 11.18671946, 0.0498436, -92.07016709, -0.00097981, -111.86719463, -0.01655359, -11.18671946, -0.0498436, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10001, 79.80484894, 0.00097981, 96.96457443, 0.01655359, 9.69645744, 0.0498436, -79.80484894, -0.00097981, -96.96457443, -0.01655359, -9.69645744, -0.0498436, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20001, 1, 0.0, 118.13110904, 0.01959629, 118.13110904, 0.05878886, 82.69177633, -1778.12007337, 0.05, 2, 0, 70001, 21001, 2, 3)
    ops.uniaxialMaterial('LimitState', 40001, 29.53277726, 7.915e-05, 88.59833178, 0.00023744, 295.3277726, 0.00079147, -29.53277726, -7.915e-05, -88.59833178, -0.00023744, -295.3277726, -0.00079147, 0.4, 0.3, 0.003, 0.0, 0.0, 20001, 2)
    ops.limitCurve('ThreePoint', 10001, 1, 0.0, 118.13110904, 0.01959629, 118.13110904, 0.05878886, 82.69177633, -1778.12007337, 0.05, 2, 0, 70001, 21001, 1, 3)
    ops.uniaxialMaterial('LimitState', 30001, 29.53277726, 7.915e-05, 88.59833178, 0.00023744, 295.3277726, 0.00079147, -29.53277726, -7.915e-05, -88.59833178, -0.00023744, -295.3277726, -0.00079147, 0.4, 0.3, 0.003, 0.0, 0.0, 10001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1, 99999, 'P', 40001, 'Vy', 30001, 'Vz', 20001, 'My', 10001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170001, 70001, 170001, 1, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121001, 121001, 21001, 1, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170004, 13.0, 0.0, 0.0)
    ops.node(121004, 13.0, 0.0, 2.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4, 170004, 121004, 0.1225, 27810128.47716095, 11587553.5321504, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20004, 93.26479156, 0.00095645, 113.09488045, 0.01563557, 11.30948805, 0.05428018, -93.26479156, -0.00095645, -113.09488045, -0.01563557, -11.30948805, -0.05428018, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10004, 81.35865718, 0.00095645, 98.65724733, 0.01563557, 9.86572473, 0.05428018, -81.35865718, -0.00095645, -98.65724733, -0.01563557, -9.86572473, -0.05428018, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20004, 4, 0.0, 124.68713313, 0.01912897, 124.68713313, 0.0573869, 87.28099319, -1609.69568104, 0.05, 2, 0, 70004, 21004, 2, 3)
    ops.uniaxialMaterial('LimitState', 40004, 31.17178328, 7.379e-05, 93.51534985, 0.00022136, 311.71783282, 0.00073786, -31.17178328, -7.379e-05, -93.51534985, -0.00022136, -311.71783282, -0.00073786, 0.4, 0.3, 0.003, 0.0, 0.0, 20004, 2)
    ops.limitCurve('ThreePoint', 10004, 4, 0.0, 124.68713313, 0.01912897, 124.68713313, 0.0573869, 87.28099319, -1609.69568104, 0.05, 2, 0, 70004, 21004, 1, 3)
    ops.uniaxialMaterial('LimitState', 30004, 31.17178328, 7.379e-05, 93.51534985, 0.00022136, 311.71783282, 0.00073786, -31.17178328, -7.379e-05, -93.51534985, -0.00022136, -311.71783282, -0.00073786, 0.4, 0.3, 0.003, 0.0, 0.0, 10004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4, 99999, 'P', 40004, 'Vy', 30004, 'Vz', 20004, 'My', 10004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170004, 70004, 170004, 4, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121004, 121004, 21004, 4, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170005, 0.0, 4.4, 0.0)
    ops.node(121005, 0.0, 4.4, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 5, 170005, 121005, 0.2025, 27334274.68746622, 11389281.11977759, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20005, 207.97072073, 0.00084244, 252.19425235, 0.01909546, 25.21942524, 0.0556928, -207.97072073, -0.00084244, -252.19425235, -0.01909546, -25.21942524, -0.0556928, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10005, 207.97072073, 0.00084244, 252.19425235, 0.01909546, 25.21942524, 0.0556928, -207.97072073, -0.00084244, -252.19425235, -0.01909546, -25.21942524, -0.0556928, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20005, 5, 0.0, 209.1462397, 0.0168488, 209.1462397, 0.05054639, 146.40236779, -2682.13910329, 0.05, 2, 0, 70005, 21005, 2, 3)
    ops.uniaxialMaterial('LimitState', 40005, 52.28655992, 7.617e-05, 156.85967977, 0.00022852, 522.86559924, 0.00076174, -52.28655992, -7.617e-05, -156.85967977, -0.00022852, -522.86559924, -0.00076174, 0.4, 0.3, 0.003, 0.0, 0.0, 20005, 2)
    ops.limitCurve('ThreePoint', 10005, 5, 0.0, 209.1462397, 0.0168488, 209.1462397, 0.05054639, 146.40236779, -2682.13910329, 0.05, 2, 0, 70005, 21005, 1, 3)
    ops.uniaxialMaterial('LimitState', 30005, 52.28655992, 7.617e-05, 156.85967977, 0.00022852, 522.86559924, 0.00076174, -52.28655992, -7.617e-05, -156.85967977, -0.00022852, -522.86559924, -0.00076174, 0.4, 0.3, 0.003, 0.0, 0.0, 10005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 5, 99999, 'P', 40005, 'Vy', 30005, 'Vz', 20005, 'My', 10005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170005, 70005, 170005, 5, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121005, 121005, 21005, 5, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170006, 5.05, 4.4, 0.0)
    ops.node(121006, 5.05, 4.4, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 6, 170006, 121006, 0.25, 27271838.44193284, 11363266.01747202, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20006, 272.54412705, 0.00086989, 330.54722509, 0.03473729, 33.05472251, 0.07668151, -272.54412705, -0.00086989, -330.54722509, -0.03473729, -33.05472251, -0.07668151, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10006, 306.32022151, 0.00086989, 371.51157981, 0.03473729, 37.15115798, 0.07668151, -306.32022151, -0.00086989, -371.51157981, -0.03473729, -37.15115798, -0.07668151, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20006, 6, 0.0, 307.95696483, 0.01739779, 307.95696483, 0.05219336, 215.56987538, -4546.74630496, 0.05, 2, 0, 70006, 21006, 2, 3)
    ops.uniaxialMaterial('LimitState', 40006, 76.98924121, 9.106e-05, 230.96772362, 0.00027318, 769.89241208, 0.0009106, -76.98924121, -9.106e-05, -230.96772362, -0.00027318, -769.89241208, -0.0009106, 0.4, 0.3, 0.003, 0.0, 0.0, 20006, 2)
    ops.limitCurve('ThreePoint', 10006, 6, 0.0, 307.95696483, 0.01739779, 307.95696483, 0.05219336, 215.56987538, -4546.74630496, 0.05, 2, 0, 70006, 21006, 1, 3)
    ops.uniaxialMaterial('LimitState', 30006, 76.98924121, 9.106e-05, 230.96772362, 0.00027318, 769.89241208, 0.0009106, -76.98924121, -9.106e-05, -230.96772362, -0.00027318, -769.89241208, -0.0009106, 0.4, 0.3, 0.003, 0.0, 0.0, 10006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 6, 99999, 'P', 40006, 'Vy', 30006, 'Vz', 20006, 'My', 10006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170006, 70006, 170006, 6, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121006, 121006, 21006, 6, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170007, 7.95, 4.4, 0.0)
    ops.node(121007, 7.95, 4.4, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 7, 170007, 121007, 0.25, 26885105.66811134, 11202127.36171306, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20007, 273.50221421, 0.0008701, 331.83063651, 0.03503508, 33.18306365, 0.07632029, -273.50221421, -0.0008701, -331.83063651, -0.03503508, -33.18306365, -0.07632029, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10007, 308.11758338, 0.0008701, 373.82824893, 0.03503508, 37.38282489, 0.07632029, -308.11758338, -0.0008701, -373.82824893, -0.03503508, -37.38282489, -0.07632029, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20007, 7, 0.0, 310.82744099, 0.01740209, 310.82744099, 0.05220628, 217.57920869, -4795.08521995, 0.05, 2, 0, 70007, 21007, 2, 3)
    ops.uniaxialMaterial('LimitState', 40007, 77.70686025, 9.323e-05, 233.12058074, 0.00027969, 777.06860248, 0.00093231, -77.70686025, -9.323e-05, -233.12058074, -0.00027969, -777.06860248, -0.00093231, 0.4, 0.3, 0.003, 0.0, 0.0, 20007, 2)
    ops.limitCurve('ThreePoint', 10007, 7, 0.0, 310.82744099, 0.01740209, 310.82744099, 0.05220628, 217.57920869, -4795.08521995, 0.05, 2, 0, 70007, 21007, 1, 3)
    ops.uniaxialMaterial('LimitState', 30007, 77.70686025, 9.323e-05, 233.12058074, 0.00027969, 777.06860248, 0.00093231, -77.70686025, -9.323e-05, -233.12058074, -0.00027969, -777.06860248, -0.00093231, 0.4, 0.3, 0.003, 0.0, 0.0, 10007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 7, 99999, 'P', 40007, 'Vy', 30007, 'Vz', 20007, 'My', 10007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170007, 70007, 170007, 7, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121007, 121007, 21007, 7, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170008, 13.0, 4.4, 0.0)
    ops.node(121008, 13.0, 4.4, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 8, 170008, 121008, 0.2025, 26269377.68789311, 10945574.03662213, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20008, 207.96632986, 0.00083077, 252.40831055, 0.01950203, 25.24083106, 0.05445417, -207.96632986, -0.00083077, -252.40831055, -0.01950203, -25.24083106, -0.05445417, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10008, 207.96632986, 0.00083077, 252.40831055, 0.01950203, 25.24083106, 0.05445417, -207.96632986, -0.00083077, -252.40831055, -0.01950203, -25.24083106, -0.05445417, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20008, 8, 0.0, 202.6592755, 0.01661533, 202.6592755, 0.049846, 141.86149285, -2677.91860271, 0.05, 2, 0, 70008, 21008, 2, 3)
    ops.uniaxialMaterial('LimitState', 40008, 50.66481887, 7.68e-05, 151.99445662, 0.00023041, 506.64818874, 0.00076804, -50.66481887, -7.68e-05, -151.99445662, -0.00023041, -506.64818874, -0.00076804, 0.4, 0.3, 0.003, 0.0, 0.0, 20008, 2)
    ops.limitCurve('ThreePoint', 10008, 8, 0.0, 202.6592755, 0.01661533, 202.6592755, 0.049846, 141.86149285, -2677.91860271, 0.05, 2, 0, 70008, 21008, 1, 3)
    ops.uniaxialMaterial('LimitState', 30008, 50.66481887, 7.68e-05, 151.99445662, 0.00023041, 506.64818874, 0.00076804, -50.66481887, -7.68e-05, -151.99445662, -0.00023041, -506.64818874, -0.00076804, 0.4, 0.3, 0.003, 0.0, 0.0, 10008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 8, 99999, 'P', 40008, 'Vy', 30008, 'Vz', 20008, 'My', 10008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170008, 70008, 170008, 8, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121008, 121008, 21008, 8, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170009, 0.0, 8.8, 0.0)
    ops.node(121009, 0.0, 8.8, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 9, 170009, 121009, 0.2025, 28110010.77032863, 11712504.48763693, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20009, 200.06336776, 0.00089493, 242.3796954, 0.02494451, 24.23796954, 0.06261585, -200.06336776, -0.00089493, -242.3796954, -0.02494451, -24.23796954, -0.06261585, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10009, 191.85705033, 0.00089493, 232.43762184, 0.02494451, 23.24376218, 0.06261585, -191.85705033, -0.00089493, -232.43762184, -0.02494451, -23.24376218, -0.06261585, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20009, 9, 0.0, 219.20440023, 0.01789862, 219.20440023, 0.05369586, 153.44308016, -2868.76158764, 0.05, 2, 0, 70009, 21009, 2, 3)
    ops.uniaxialMaterial('LimitState', 40009, 54.80110006, 7.763e-05, 164.40330017, 0.0002329, 548.01100057, 0.00077634, -54.80110006, -7.763e-05, -164.40330017, -0.0002329, -548.01100057, -0.00077634, 0.4, 0.3, 0.003, 0.0, 0.0, 20009, 2)
    ops.limitCurve('ThreePoint', 10009, 9, 0.0, 219.20440023, 0.01789862, 219.20440023, 0.05369586, 153.44308016, -2868.76158764, 0.05, 2, 0, 70009, 21009, 1, 3)
    ops.uniaxialMaterial('LimitState', 30009, 54.80110006, 7.763e-05, 164.40330017, 0.0002329, 548.01100057, 0.00077634, -54.80110006, -7.763e-05, -164.40330017, -0.0002329, -548.01100057, -0.00077634, 0.4, 0.3, 0.003, 0.0, 0.0, 10009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 9, 99999, 'P', 40009, 'Vy', 30009, 'Vz', 20009, 'My', 10009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170009, 70009, 170009, 9, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121009, 121009, 21009, 9, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170010, 5.05, 8.8, 0.0)
    ops.node(121010, 5.05, 8.8, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 10, 170010, 121010, 0.25, 26746085.64158459, 11144202.35066025, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20010, 299.76282638, 0.00086632, 363.88219563, 0.0358426, 36.38821956, 0.077385, -299.76282638, -0.00086632, -363.88219563, -0.0358426, -36.38821956, -0.077385, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10010, 316.03141514, 0.00086632, 383.630641, 0.0358426, 38.3630641, 0.077385, -316.03141514, -0.00086632, -383.630641, -0.0358426, -38.3630641, -0.077385, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20010, 10, 0.0, 312.29234714, 0.01732642, 312.29234714, 0.05197925, 218.604643, -5002.47813626, 0.05, 2, 0, 70010, 21010, 2, 3)
    ops.uniaxialMaterial('LimitState', 40010, 78.07308679, 9.416e-05, 234.21926036, 0.00028247, 780.73086785, 0.00094157, -78.07308679, -9.416e-05, -234.21926036, -0.00028247, -780.73086785, -0.00094157, 0.4, 0.3, 0.003, 0.0, 0.0, 20010, 2)
    ops.limitCurve('ThreePoint', 10010, 10, 0.0, 312.29234714, 0.01732642, 312.29234714, 0.05197925, 218.604643, -5002.47813626, 0.05, 2, 0, 70010, 21010, 1, 3)
    ops.uniaxialMaterial('LimitState', 30010, 78.07308679, 9.416e-05, 234.21926036, 0.00028247, 780.73086785, 0.00094157, -78.07308679, -9.416e-05, -234.21926036, -0.00028247, -780.73086785, -0.00094157, 0.4, 0.3, 0.003, 0.0, 0.0, 10010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 10, 99999, 'P', 40010, 'Vy', 30010, 'Vz', 20010, 'My', 10010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170010, 70010, 170010, 10, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121010, 121010, 21010, 10, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170011, 7.95, 8.8, 0.0)
    ops.node(121011, 7.95, 8.8, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 11, 170011, 121011, 0.25, 26590806.84649917, 11079502.85270799, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20011, 306.89916499, 0.00085768, 372.59260813, 0.03425607, 37.25926081, 0.0755271, -306.89916499, -0.00085768, -372.59260813, -0.03425607, -37.25926081, -0.0755271, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10011, 324.51662351, 0.00085768, 393.98117991, 0.03425607, 39.39811799, 0.0755271, -324.51662351, -0.00085768, -393.98117991, -0.03425607, -39.39811799, -0.0755271, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20011, 11, 0.0, 294.34052502, 0.01715363, 294.34052502, 0.05146089, 206.03836751, -4307.65263663, 0.05, 2, 0, 70011, 21011, 2, 3)
    ops.uniaxialMaterial('LimitState', 40011, 73.58513125, 8.926e-05, 220.75539376, 0.00026779, 735.85131254, 0.00089263, -73.58513125, -8.926e-05, -220.75539376, -0.00026779, -735.85131254, -0.00089263, 0.4, 0.3, 0.003, 0.0, 0.0, 20011, 2)
    ops.limitCurve('ThreePoint', 10011, 11, 0.0, 294.34052502, 0.01715363, 294.34052502, 0.05146089, 206.03836751, -4307.65263663, 0.05, 2, 0, 70011, 21011, 1, 3)
    ops.uniaxialMaterial('LimitState', 30011, 73.58513125, 8.926e-05, 220.75539376, 0.00026779, 735.85131254, 0.00089263, -73.58513125, -8.926e-05, -220.75539376, -0.00026779, -735.85131254, -0.00089263, 0.4, 0.3, 0.003, 0.0, 0.0, 10011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 11, 99999, 'P', 40011, 'Vy', 30011, 'Vz', 20011, 'My', 10011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170011, 70011, 170011, 11, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121011, 121011, 21011, 11, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170012, 13.0, 8.8, 0.0)
    ops.node(121012, 13.0, 8.8, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 12, 170012, 121012, 0.2025, 28118265.11555659, 11715943.79814858, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20012, 195.71666966, 0.00087959, 237.11095265, 0.02643962, 23.71109526, 0.06412186, -195.71666966, -0.00087959, -237.11095265, -0.02643962, -23.71109526, -0.06412186, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10012, 187.87540879, 0.00087959, 227.61125679, 0.02643962, 22.76112568, 0.06412186, -187.87540879, -0.00087959, -227.61125679, -0.02643962, -22.76112568, -0.06412186, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20012, 12, 0.0, 230.29953077, 0.01759186, 230.29953077, 0.05277557, 161.20967154, -3275.06012271, 0.05, 2, 0, 70012, 21012, 2, 3)
    ops.uniaxialMaterial('LimitState', 40012, 57.57488269, 8.154e-05, 172.72464808, 0.00024462, 575.74882692, 0.0008154, -57.57488269, -8.154e-05, -172.72464808, -0.00024462, -575.74882692, -0.0008154, 0.4, 0.3, 0.003, 0.0, 0.0, 20012, 2)
    ops.limitCurve('ThreePoint', 10012, 12, 0.0, 230.29953077, 0.01759186, 230.29953077, 0.05277557, 161.20967154, -3275.06012271, 0.05, 2, 0, 70012, 21012, 1, 3)
    ops.uniaxialMaterial('LimitState', 30012, 57.57488269, 8.154e-05, 172.72464808, 0.00024462, 575.74882692, 0.0008154, -57.57488269, -8.154e-05, -172.72464808, -0.00024462, -575.74882692, -0.0008154, 0.4, 0.3, 0.003, 0.0, 0.0, 10012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 12, 99999, 'P', 40012, 'Vy', 30012, 'Vz', 20012, 'My', 10012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170012, 70012, 170012, 12, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121012, 121012, 21012, 12, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170013, 0.0, 13.2, 0.0)
    ops.node(121013, 0.0, 13.2, 2.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 13, 170013, 121013, 0.1225, 27724003.17264619, 11551667.98860258, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20013, 95.90946117, 0.00097468, 116.31470681, 0.0187224, 11.63147068, 0.05725033, -95.90946117, -0.00097468, -116.31470681, -0.0187224, -11.63147068, -0.05725033, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10013, 83.28455513, 0.00097468, 101.00378517, 0.0187224, 10.10037852, 0.05725033, -83.28455513, -0.00097468, -101.00378517, -0.0187224, -10.10037852, -0.05725033, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20013, 13, 0.0, 137.78947857, 0.0194937, 137.78947857, 0.0584811, 96.452635, -2115.80377066, 0.05, 2, 0, 70013, 21013, 2, 3)
    ops.uniaxialMaterial('LimitState', 40013, 34.44736964, 8.179e-05, 103.34210893, 0.00024538, 344.47369643, 0.00081793, -34.44736964, -8.179e-05, -103.34210893, -0.00024538, -344.47369643, -0.00081793, 0.4, 0.3, 0.003, 0.0, 0.0, 20013, 2)
    ops.limitCurve('ThreePoint', 10013, 13, 0.0, 137.78947857, 0.0194937, 137.78947857, 0.0584811, 96.452635, -2115.80377066, 0.05, 2, 0, 70013, 21013, 1, 3)
    ops.uniaxialMaterial('LimitState', 30013, 34.44736964, 8.179e-05, 103.34210893, 0.00024538, 344.47369643, 0.00081793, -34.44736964, -8.179e-05, -103.34210893, -0.00024538, -344.47369643, -0.00081793, 0.4, 0.3, 0.003, 0.0, 0.0, 10013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 13, 99999, 'P', 40013, 'Vy', 30013, 'Vz', 20013, 'My', 10013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170013, 70013, 170013, 13, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121013, 121013, 21013, 13, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170014, 5.05, 13.2, 0.0)
    ops.node(121014, 5.05, 13.2, 2.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 14, 170014, 121014, 0.16, 25831942.59450376, 10763309.41437657, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20014, 142.57253629, 0.00089995, 173.02392167, 0.01828312, 17.30239217, 0.04971619, -142.57253629, -0.00089995, -173.02392167, -0.01828312, -17.30239217, -0.04971619, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10014, 142.57253629, 0.00089995, 173.02392167, 0.01828312, 17.30239217, 0.04971619, -142.57253629, -0.00089995, -173.02392167, -0.01828312, -17.30239217, -0.04971619, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20014, 14, 0.0, 156.98125308, 0.01799898, 156.98125308, 0.05399695, 109.88687715, -2148.86597372, 0.05, 2, 0, 70014, 21014, 2, 3)
    ops.uniaxialMaterial('LimitState', 40014, 39.24531327, 7.657e-05, 117.73593981, 0.00022971, 392.45313269, 0.0007657, -39.24531327, -7.657e-05, -117.73593981, -0.00022971, -392.45313269, -0.0007657, 0.4, 0.3, 0.003, 0.0, 0.0, 20014, 2)
    ops.limitCurve('ThreePoint', 10014, 14, 0.0, 156.98125308, 0.01799898, 156.98125308, 0.05399695, 109.88687715, -2148.86597372, 0.05, 2, 0, 70014, 21014, 1, 3)
    ops.uniaxialMaterial('LimitState', 30014, 39.24531327, 7.657e-05, 117.73593981, 0.00022971, 392.45313269, 0.0007657, -39.24531327, -7.657e-05, -117.73593981, -0.00022971, -392.45313269, -0.0007657, 0.4, 0.3, 0.003, 0.0, 0.0, 10014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 14, 99999, 'P', 40014, 'Vy', 30014, 'Vz', 20014, 'My', 10014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170014, 70014, 170014, 14, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121014, 121014, 21014, 14, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170015, 7.95, 13.2, 0.0)
    ops.node(121015, 7.95, 13.2, 2.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 15, 170015, 121015, 0.16, 27659086.01206975, 11524619.17169573, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20015, 148.12505351, 0.00088335, 179.51462305, 0.01733754, 17.95146231, 0.05144742, -148.12505351, -0.00088335, -179.51462305, -0.01733754, -17.95146231, -0.05144742, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10015, 148.12505351, 0.00088335, 179.51462305, 0.01733754, 17.95146231, 0.05144742, -148.12505351, -0.00088335, -179.51462305, -0.01733754, -17.95146231, -0.05144742, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20015, 15, 0.0, 166.22313822, 0.01766702, 166.22313822, 0.05300107, 116.35619675, -2178.04787715, 0.05, 2, 0, 70015, 21015, 2, 3)
    ops.uniaxialMaterial('LimitState', 40015, 41.55578455, 7.572e-05, 124.66735366, 0.00022717, 415.55784555, 0.00075722, -41.55578455, -7.572e-05, -124.66735366, -0.00022717, -415.55784555, -0.00075722, 0.4, 0.3, 0.003, 0.0, 0.0, 20015, 2)
    ops.limitCurve('ThreePoint', 10015, 15, 0.0, 166.22313822, 0.01766702, 166.22313822, 0.05300107, 116.35619675, -2178.04787715, 0.05, 2, 0, 70015, 21015, 1, 3)
    ops.uniaxialMaterial('LimitState', 30015, 41.55578455, 7.572e-05, 124.66735366, 0.00022717, 415.55784555, 0.00075722, -41.55578455, -7.572e-05, -124.66735366, -0.00022717, -415.55784555, -0.00075722, 0.4, 0.3, 0.003, 0.0, 0.0, 10015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 15, 99999, 'P', 40015, 'Vy', 30015, 'Vz', 20015, 'My', 10015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170015, 70015, 170015, 15, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121015, 121015, 21015, 15, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170016, 13.0, 13.2, 0.0)
    ops.node(121016, 13.0, 13.2, 2.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 16, 170016, 121016, 0.1225, 26153874.46889042, 10897447.69537101, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20016, 92.22584242, 0.00099081, 112.01360531, 0.01698854, 11.20136053, 0.05316183, -92.22584242, -0.00099081, -112.01360531, -0.01698854, -11.20136053, -0.05316183, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10016, 80.59391507, 0.00099081, 97.8859586, 0.01698854, 9.78859586, 0.05316183, -80.59391507, -0.00099081, -97.8859586, -0.01698854, -9.78859586, -0.05316183, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20016, 16, 0.0, 125.864741, 0.01981619, 125.864741, 0.05944858, 88.1053187, -1865.25910857, 0.05, 2, 0, 70016, 21016, 2, 3)
    ops.uniaxialMaterial('LimitState', 40016, 31.46618525, 7.92e-05, 94.39855575, 0.0002376, 314.66185251, 0.000792, -31.46618525, -7.92e-05, -94.39855575, -0.0002376, -314.66185251, -0.000792, 0.4, 0.3, 0.003, 0.0, 0.0, 20016, 2)
    ops.limitCurve('ThreePoint', 10016, 16, 0.0, 125.864741, 0.01981619, 125.864741, 0.05944858, 88.1053187, -1865.25910857, 0.05, 2, 0, 70016, 21016, 1, 3)
    ops.uniaxialMaterial('LimitState', 30016, 31.46618525, 7.92e-05, 94.39855575, 0.0002376, 314.66185251, 0.000792, -31.46618525, -7.92e-05, -94.39855575, -0.0002376, -314.66185251, -0.000792, 0.4, 0.3, 0.003, 0.0, 0.0, 10016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 16, 99999, 'P', 40016, 'Vy', 30016, 'Vz', 20016, 'My', 10016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170016, 70016, 170016, 16, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121016, 121016, 21016, 16, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171001, 0.0, 0.0, 3.075)
    ops.node(122001, 0.0, 0.0, 5.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1001, 171001, 122001, 0.1225, 28943108.3151231, 12059628.46463462, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21001, 98.05819394, 0.00098337, 118.98860374, 0.01945648, 11.89886037, 0.06249775, -98.05819394, -0.00098337, -118.98860374, -0.01945648, -11.89886037, -0.06249775, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11001, 81.98321247, 0.00098337, 99.48243578, 0.01945648, 9.94824358, 0.06249775, -81.98321247, -0.00098337, -99.48243578, -0.01945648, -9.94824358, -0.06249775, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21001, 1001, 0.0, 132.00703569, 0.01966735, 132.00703569, 0.05900205, 92.40492499, -2046.41214726, 0.05, 2, 0, 71001, 22001, 2, 3)
    ops.uniaxialMaterial('LimitState', 41001, 33.00175892, 7.506e-05, 99.00527677, 0.00022518, 330.01758923, 0.0007506, -33.00175892, -7.506e-05, -99.00527677, -0.00022518, -330.01758923, -0.0007506, 0.4, 0.3, 0.003, 0.0, 0.0, 21001, 2)
    ops.limitCurve('ThreePoint', 11001, 1001, 0.0, 132.00703569, 0.01966735, 132.00703569, 0.05900205, 92.40492499, -2046.41214726, 0.05, 2, 0, 71001, 22001, 1, 3)
    ops.uniaxialMaterial('LimitState', 31001, 33.00175892, 7.506e-05, 99.00527677, 0.00022518, 330.01758923, 0.0007506, -33.00175892, -7.506e-05, -99.00527677, -0.00022518, -330.01758923, -0.0007506, 0.4, 0.3, 0.003, 0.0, 0.0, 11001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1001, 99999, 'P', 41001, 'Vy', 31001, 'Vz', 21001, 'My', 11001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171001, 71001, 171001, 1001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122001, 122001, 22001, 1001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171004, 13.0, 0.0, 3.075)
    ops.node(122004, 13.0, 0.0, 5.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1004, 171004, 122004, 0.1225, 29403977.48437407, 12251657.28515586, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21004, 91.80745567, 0.00092463, 111.29708562, 0.02051784, 11.12970856, 0.06396553, -91.80745567, -0.00092463, -111.29708562, -0.02051784, -11.12970856, -0.06396553, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11004, 77.4218558, 0.00092463, 93.85759414, 0.02051784, 9.38575941, 0.06396553, -77.4218558, -0.00092463, -93.85759414, -0.02051784, -9.38575941, -0.06396553, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21004, 1004, 0.0, 135.83236508, 0.01849251, 135.83236508, 0.05547753, 95.08265556, -2148.49106689, 0.05, 2, 0, 71004, 22004, 2, 3)
    ops.uniaxialMaterial('LimitState', 41004, 33.95809127, 7.602e-05, 101.87427381, 0.00022807, 339.58091271, 0.00076024, -33.95809127, -7.602e-05, -101.87427381, -0.00022807, -339.58091271, -0.00076024, 0.4, 0.3, 0.003, 0.0, 0.0, 21004, 2)
    ops.limitCurve('ThreePoint', 11004, 1004, 0.0, 135.83236508, 0.01849251, 135.83236508, 0.05547753, 95.08265556, -2148.49106689, 0.05, 2, 0, 71004, 22004, 1, 3)
    ops.uniaxialMaterial('LimitState', 31004, 33.95809127, 7.602e-05, 101.87427381, 0.00022807, 339.58091271, 0.00076024, -33.95809127, -7.602e-05, -101.87427381, -0.00022807, -339.58091271, -0.00076024, 0.4, 0.3, 0.003, 0.0, 0.0, 11004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1004, 99999, 'P', 41004, 'Vy', 31004, 'Vz', 21004, 'My', 11004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171004, 71004, 171004, 1004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122004, 122004, 22004, 1004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171005, 0.0, 4.4, 3.1)
    ops.node(122005, 0.0, 4.4, 5.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1005, 171005, 122005, 0.2025, 27578734.12184899, 11491139.21743708, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21005, 168.98269423, 0.00076419, 205.45909547, 0.02162365, 20.54590955, 0.06192488, -168.98269423, -0.00076419, -205.45909547, -0.02162365, -20.54590955, -0.06192488, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11005, 138.28109547, 0.00076419, 168.13028651, 0.02162365, 16.81302865, 0.06192488, -138.28109547, -0.00076419, -168.13028651, -0.02162365, -16.81302865, -0.06192488, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21005, 1005, 0.0, 206.81285144, 0.01528373, 206.81285144, 0.04585118, 144.76899601, -2975.06579963, 0.05, 2, 0, 71005, 22005, 2, 3)
    ops.uniaxialMaterial('LimitState', 41005, 51.70321286, 7.466e-05, 155.10963858, 0.00022397, 517.0321286, 0.00074657, -51.70321286, -7.466e-05, -155.10963858, -0.00022397, -517.0321286, -0.00074657, 0.4, 0.3, 0.003, 0.0, 0.0, 21005, 2)
    ops.limitCurve('ThreePoint', 11005, 1005, 0.0, 206.81285144, 0.01528373, 206.81285144, 0.04585118, 144.76899601, -2975.06579963, 0.05, 2, 0, 71005, 22005, 1, 3)
    ops.uniaxialMaterial('LimitState', 31005, 51.70321286, 7.466e-05, 155.10963858, 0.00022397, 517.0321286, 0.00074657, -51.70321286, -7.466e-05, -155.10963858, -0.00022397, -517.0321286, -0.00074657, 0.4, 0.3, 0.003, 0.0, 0.0, 11005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1005, 99999, 'P', 41005, 'Vy', 31005, 'Vz', 21005, 'My', 11005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171005, 71005, 171005, 1005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122005, 122005, 22005, 1005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171006, 5.05, 4.4, 3.1)
    ops.node(122006, 5.05, 4.4, 5.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1006, 171006, 122006, 0.25, 29347858.64705681, 12228274.43627367, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21006, 249.60508987, 0.0008226, 302.50578098, 0.03324326, 30.2505781, 0.08137784, -249.60508987, -0.0008226, -302.50578098, -0.03324326, -30.2505781, -0.08137784, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11006, 232.50266142, 0.0008226, 281.77870575, 0.03324326, 28.17787058, 0.08137784, -232.50266142, -0.0008226, -281.77870575, -0.03324326, -28.17787058, -0.08137784, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21006, 1006, 0.0, 297.11356555, 0.01645208, 297.11356555, 0.04935623, 207.97949589, -4106.19795382, 0.05, 2, 0, 71006, 22006, 2, 3)
    ops.uniaxialMaterial('LimitState', 41006, 74.27839139, 8.164e-05, 222.83517417, 0.00024492, 742.78391389, 0.00081639, -74.27839139, -8.164e-05, -222.83517417, -0.00024492, -742.78391389, -0.00081639, 0.4, 0.3, 0.003, 0.0, 0.0, 21006, 2)
    ops.limitCurve('ThreePoint', 11006, 1006, 0.0, 297.11356555, 0.01645208, 297.11356555, 0.04935623, 207.97949589, -4106.19795382, 0.05, 2, 0, 71006, 22006, 1, 3)
    ops.uniaxialMaterial('LimitState', 31006, 74.27839139, 8.164e-05, 222.83517417, 0.00024492, 742.78391389, 0.00081639, -74.27839139, -8.164e-05, -222.83517417, -0.00024492, -742.78391389, -0.00081639, 0.4, 0.3, 0.003, 0.0, 0.0, 11006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1006, 99999, 'P', 41006, 'Vy', 31006, 'Vz', 21006, 'My', 11006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171006, 71006, 171006, 1006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122006, 122006, 22006, 1006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171007, 7.95, 4.4, 3.1)
    ops.node(122007, 7.95, 4.4, 5.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1007, 171007, 122007, 0.25, 25367381.45314012, 10569742.27214172, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21007, 232.96786027, 0.00083719, 283.91593371, 0.03686363, 28.39159337, 0.07968088, -232.96786027, -0.00083719, -283.91593371, -0.03686363, -28.39159337, -0.07968088, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11007, 217.33854343, 0.00083719, 264.86861929, 0.03686363, 26.48686193, 0.07968088, -217.33854343, -0.00083719, -264.86861929, -0.03686363, -26.48686193, -0.07968088, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21007, 1007, 0.0, 292.17614066, 0.01674373, 292.17614066, 0.05023119, 204.52329846, -5430.47038204, 0.05, 2, 0, 71007, 22007, 2, 3)
    ops.uniaxialMaterial('LimitState', 41007, 73.04403516, 9.288e-05, 219.13210549, 0.00027864, 730.44035164, 0.00092879, -73.04403516, -9.288e-05, -219.13210549, -0.00027864, -730.44035164, -0.00092879, 0.4, 0.3, 0.003, 0.0, 0.0, 21007, 2)
    ops.limitCurve('ThreePoint', 11007, 1007, 0.0, 292.17614066, 0.01674373, 292.17614066, 0.05023119, 204.52329846, -5430.47038204, 0.05, 2, 0, 71007, 22007, 1, 3)
    ops.uniaxialMaterial('LimitState', 31007, 73.04403516, 9.288e-05, 219.13210549, 0.00027864, 730.44035164, 0.00092879, -73.04403516, -9.288e-05, -219.13210549, -0.00027864, -730.44035164, -0.00092879, 0.4, 0.3, 0.003, 0.0, 0.0, 11007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1007, 99999, 'P', 41007, 'Vy', 31007, 'Vz', 21007, 'My', 11007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171007, 71007, 171007, 1007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122007, 122007, 22007, 1007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171008, 13.0, 4.4, 3.1)
    ops.node(122008, 13.0, 4.4, 5.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1008, 171008, 122008, 0.2025, 27624437.34542678, 11510182.22726116, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21008, 177.27799376, 0.00079786, 215.5301993, 0.02239686, 21.55301993, 0.06274878, -177.27799376, -0.00079786, -215.5301993, -0.02239686, -21.55301993, -0.06274878, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11008, 144.18350863, 0.00079786, 175.29474297, 0.02239686, 17.5294743, 0.06274878, -144.18350863, -0.00079786, -175.29474297, -0.02239686, -17.5294743, -0.06274878, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21008, 1008, 0.0, 212.22988587, 0.01595721, 212.22988587, 0.04787163, 148.56092011, -3198.0419833, 0.05, 2, 0, 71008, 22008, 2, 3)
    ops.uniaxialMaterial('LimitState', 41008, 53.05747147, 7.649e-05, 159.17241441, 0.00022946, 530.57471468, 0.00076485, -53.05747147, -7.649e-05, -159.17241441, -0.00022946, -530.57471468, -0.00076485, 0.4, 0.3, 0.003, 0.0, 0.0, 21008, 2)
    ops.limitCurve('ThreePoint', 11008, 1008, 0.0, 212.22988587, 0.01595721, 212.22988587, 0.04787163, 148.56092011, -3198.0419833, 0.05, 2, 0, 71008, 22008, 1, 3)
    ops.uniaxialMaterial('LimitState', 31008, 53.05747147, 7.649e-05, 159.17241441, 0.00022946, 530.57471468, 0.00076485, -53.05747147, -7.649e-05, -159.17241441, -0.00022946, -530.57471468, -0.00076485, 0.4, 0.3, 0.003, 0.0, 0.0, 11008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1008, 99999, 'P', 41008, 'Vy', 31008, 'Vz', 21008, 'My', 11008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171008, 71008, 171008, 1008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122008, 122008, 22008, 1008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171009, 0.0, 8.8, 3.1)
    ops.node(122009, 0.0, 8.8, 5.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1009, 171009, 122009, 0.2025, 25208998.17220958, 10503749.23842066, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21009, 183.31749012, 0.00086352, 223.44824564, 0.02425761, 22.34482456, 0.06147035, -183.31749012, -0.00086352, -223.44824564, -0.02425761, -22.34482456, -0.06147035, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11009, 159.05060225, 0.00086352, 193.86899754, 0.02425761, 19.38689975, 0.06147035, -159.05060225, -0.00086352, -193.86899754, -0.02425761, -19.38689975, -0.06147035, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21009, 1009, 0.0, 186.26531173, 0.01727036, 186.26531173, 0.05181108, 130.38571821, -2693.72508227, 0.05, 2, 0, 71009, 22009, 2, 3)
    ops.uniaxialMaterial('LimitState', 41009, 46.56632793, 7.356e-05, 139.69898379, 0.00022068, 465.66327932, 0.0007356, -46.56632793, -7.356e-05, -139.69898379, -0.00022068, -465.66327932, -0.0007356, 0.4, 0.3, 0.003, 0.0, 0.0, 21009, 2)
    ops.limitCurve('ThreePoint', 11009, 1009, 0.0, 186.26531173, 0.01727036, 186.26531173, 0.05181108, 130.38571821, -2693.72508227, 0.05, 2, 0, 71009, 22009, 1, 3)
    ops.uniaxialMaterial('LimitState', 31009, 46.56632793, 7.356e-05, 139.69898379, 0.00022068, 465.66327932, 0.0007356, -46.56632793, -7.356e-05, -139.69898379, -0.00022068, -465.66327932, -0.0007356, 0.4, 0.3, 0.003, 0.0, 0.0, 11009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1009, 99999, 'P', 41009, 'Vy', 31009, 'Vz', 21009, 'My', 11009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171009, 71009, 171009, 1009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122009, 122009, 22009, 1009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171010, 5.05, 8.8, 3.1)
    ops.node(122010, 5.05, 8.8, 5.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1010, 171010, 122010, 0.25, 27304250.14761152, 11376770.89483813, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21010, 234.23485119, 0.00080819, 284.98635234, 0.03499852, 28.49863523, 0.08120218, -234.23485119, -0.00080819, -284.98635234, -0.03499852, -28.49863523, -0.08120218, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11010, 218.26706843, 0.00080819, 265.55884128, 0.03499852, 26.55588413, 0.08120218, -218.26706843, -0.00080819, -265.55884128, -0.03499852, -26.55588413, -0.08120218, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21010, 1010, 0.0, 279.71577664, 0.01616371, 279.71577664, 0.04849113, 195.80104365, -4196.08637797, 0.05, 2, 0, 71010, 22010, 2, 3)
    ops.uniaxialMaterial('LimitState', 41010, 69.92894416, 8.261e-05, 209.78683248, 0.00024783, 699.2894416, 0.00082611, -69.92894416, -8.261e-05, -209.78683248, -0.00024783, -699.2894416, -0.00082611, 0.4, 0.3, 0.003, 0.0, 0.0, 21010, 2)
    ops.limitCurve('ThreePoint', 11010, 1010, 0.0, 279.71577664, 0.01616371, 279.71577664, 0.04849113, 195.80104365, -4196.08637797, 0.05, 2, 0, 71010, 22010, 1, 3)
    ops.uniaxialMaterial('LimitState', 31010, 69.92894416, 8.261e-05, 209.78683248, 0.00024783, 699.2894416, 0.00082611, -69.92894416, -8.261e-05, -209.78683248, -0.00024783, -699.2894416, -0.00082611, 0.4, 0.3, 0.003, 0.0, 0.0, 11010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1010, 99999, 'P', 41010, 'Vy', 31010, 'Vz', 21010, 'My', 11010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171010, 71010, 171010, 1010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122010, 122010, 22010, 1010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171011, 7.95, 8.8, 3.1)
    ops.node(122011, 7.95, 8.8, 5.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1011, 171011, 122011, 0.25, 25529056.92288116, 10637107.05120048, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21011, 228.74829228, 0.00087459, 278.85925624, 0.03413308, 27.88592562, 0.07776433, -228.74829228, -0.00087459, -278.85925624, -0.03413308, -27.88592562, -0.07776433, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11011, 214.19281346, 0.00087459, 261.1151675, 0.03413308, 26.11151675, 0.07776433, -214.19281346, -0.00087459, -261.1151675, -0.03413308, -26.11151675, -0.07776433, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21011, 1011, 0.0, 267.63304307, 0.0174917, 267.63304307, 0.0524751, 187.34313015, -4291.71764378, 0.05, 2, 0, 71011, 22011, 2, 3)
    ops.uniaxialMaterial('LimitState', 41011, 66.90826077, 8.454e-05, 200.7247823, 0.00025362, 669.08260767, 0.00084539, -66.90826077, -8.454e-05, -200.7247823, -0.00025362, -669.08260767, -0.00084539, 0.4, 0.3, 0.003, 0.0, 0.0, 21011, 2)
    ops.limitCurve('ThreePoint', 11011, 1011, 0.0, 267.63304307, 0.0174917, 267.63304307, 0.0524751, 187.34313015, -4291.71764378, 0.05, 2, 0, 71011, 22011, 1, 3)
    ops.uniaxialMaterial('LimitState', 31011, 66.90826077, 8.454e-05, 200.7247823, 0.00025362, 669.08260767, 0.00084539, -66.90826077, -8.454e-05, -200.7247823, -0.00025362, -669.08260767, -0.00084539, 0.4, 0.3, 0.003, 0.0, 0.0, 11011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1011, 99999, 'P', 41011, 'Vy', 31011, 'Vz', 21011, 'My', 11011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171011, 71011, 171011, 1011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122011, 122011, 22011, 1011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171012, 13.0, 8.8, 3.1)
    ops.node(122012, 13.0, 8.8, 5.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1012, 171012, 122012, 0.2025, 25777876.2481099, 10740781.77004579, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21012, 189.87047231, 0.00089842, 231.34189116, 0.02393104, 23.13418912, 0.06197477, -189.87047231, -0.00089842, -231.34189116, -0.02393104, -23.13418912, -0.06197477, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11012, 164.77526578, 0.00089842, 200.76540148, 0.02393104, 20.07654015, 0.06197477, -164.77526578, -0.00089842, -200.76540148, -0.02393104, -20.07654015, -0.06197477, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21012, 1012, 0.0, 187.54419852, 0.01796846, 187.54419852, 0.05390538, 131.28093896, -2614.87747771, 0.05, 2, 0, 71012, 22012, 2, 3)
    ops.uniaxialMaterial('LimitState', 41012, 46.88604963, 7.243e-05, 140.65814889, 0.00021729, 468.8604963, 0.00072431, -46.88604963, -7.243e-05, -140.65814889, -0.00021729, -468.8604963, -0.00072431, 0.4, 0.3, 0.003, 0.0, 0.0, 21012, 2)
    ops.limitCurve('ThreePoint', 11012, 1012, 0.0, 187.54419852, 0.01796846, 187.54419852, 0.05390538, 131.28093896, -2614.87747771, 0.05, 2, 0, 71012, 22012, 1, 3)
    ops.uniaxialMaterial('LimitState', 31012, 46.88604963, 7.243e-05, 140.65814889, 0.00021729, 468.8604963, 0.00072431, -46.88604963, -7.243e-05, -140.65814889, -0.00021729, -468.8604963, -0.00072431, 0.4, 0.3, 0.003, 0.0, 0.0, 11012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1012, 99999, 'P', 41012, 'Vy', 31012, 'Vz', 21012, 'My', 11012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171012, 71012, 171012, 1012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122012, 122012, 22012, 1012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171013, 0.0, 13.2, 3.075)
    ops.node(122013, 0.0, 13.2, 5.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1013, 171013, 122013, 0.1225, 28011290.64789016, 11671371.10328757, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21013, 87.65768321, 0.00091377, 106.55158467, 0.01899269, 10.65515847, 0.06113464, -87.65768321, -0.00091377, -106.55158467, -0.01899269, -10.65515847, -0.06113464, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11013, 74.76245457, 0.00091377, 90.87689426, 0.01899269, 9.08768943, 0.06113464, -74.76245457, -0.00091377, -90.87689426, -0.01899269, -9.08768943, -0.06113464, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21013, 1013, 0.0, 129.81389949, 0.01827533, 129.81389949, 0.054826, 90.86972965, -2099.63241768, 0.05, 2, 0, 71013, 22013, 2, 3)
    ops.uniaxialMaterial('LimitState', 41013, 32.45347487, 7.627e-05, 97.36042462, 0.0002288, 324.53474873, 0.00076268, -32.45347487, -7.627e-05, -97.36042462, -0.0002288, -324.53474873, -0.00076268, 0.4, 0.3, 0.003, 0.0, 0.0, 21013, 2)
    ops.limitCurve('ThreePoint', 11013, 1013, 0.0, 129.81389949, 0.01827533, 129.81389949, 0.054826, 90.86972965, -2099.63241768, 0.05, 2, 0, 71013, 22013, 1, 3)
    ops.uniaxialMaterial('LimitState', 31013, 32.45347487, 7.627e-05, 97.36042462, 0.0002288, 324.53474873, 0.00076268, -32.45347487, -7.627e-05, -97.36042462, -0.0002288, -324.53474873, -0.00076268, 0.4, 0.3, 0.003, 0.0, 0.0, 11013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1013, 99999, 'P', 41013, 'Vy', 31013, 'Vz', 21013, 'My', 11013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171013, 71013, 171013, 1013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122013, 122013, 22013, 1013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171014, 5.05, 13.2, 3.075)
    ops.node(122014, 5.05, 13.2, 5.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1014, 171014, 122014, 0.16, 26384825.93716229, 10993677.47381762, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21014, 129.51134527, 0.00090773, 157.67853521, 0.01542737, 15.76785352, 0.05125406, -129.51134527, -0.00090773, -157.67853521, -0.01542737, -15.76785352, -0.05125406, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11014, 108.14320759, 0.00090773, 131.66307963, 0.01542737, 13.16630796, 0.05125406, -108.14320759, -0.00090773, -131.66307963, -0.01542737, -13.16630796, -0.05125406, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21014, 1014, 0.0, 146.06336357, 0.01815453, 146.06336357, 0.0544636, 102.2443545, -1952.27325528, 0.05, 2, 0, 71014, 22014, 2, 3)
    ops.uniaxialMaterial('LimitState', 41014, 36.51584089, 6.975e-05, 109.54752268, 0.00020926, 365.15840893, 0.00069752, -36.51584089, -6.975e-05, -109.54752268, -0.00020926, -365.15840893, -0.00069752, 0.4, 0.3, 0.003, 0.0, 0.0, 21014, 2)
    ops.limitCurve('ThreePoint', 11014, 1014, 0.0, 146.06336357, 0.01815453, 146.06336357, 0.0544636, 102.2443545, -1952.27325528, 0.05, 2, 0, 71014, 22014, 1, 3)
    ops.uniaxialMaterial('LimitState', 31014, 36.51584089, 6.975e-05, 109.54752268, 0.00020926, 365.15840893, 0.00069752, -36.51584089, -6.975e-05, -109.54752268, -0.00020926, -365.15840893, -0.00069752, 0.4, 0.3, 0.003, 0.0, 0.0, 11014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1014, 99999, 'P', 41014, 'Vy', 31014, 'Vz', 21014, 'My', 11014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171014, 71014, 171014, 1014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122014, 122014, 22014, 1014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171015, 7.95, 13.2, 3.075)
    ops.node(122015, 7.95, 13.2, 5.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1015, 171015, 122015, 0.16, 25619034.26883273, 10674597.61201364, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21015, 126.30317869, 0.0009098, 153.87735778, 0.01770146, 15.38773578, 0.05254284, -126.30317869, -0.0009098, -153.87735778, -0.01770146, -15.38773578, -0.05254284, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11015, 105.91589353, 0.0009098, 129.03917394, 0.01770146, 12.90391739, 0.05254284, -105.91589353, -0.0009098, -129.03917394, -0.01770146, -12.90391739, -0.05254284, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21015, 1015, 0.0, 147.42252599, 0.01819602, 147.42252599, 0.05458807, 103.19576819, -2138.90886704, 0.05, 2, 0, 71015, 22015, 2, 3)
    ops.uniaxialMaterial('LimitState', 41015, 36.8556315, 7.251e-05, 110.56689449, 0.00021752, 368.55631497, 0.00072506, -36.8556315, -7.251e-05, -110.56689449, -0.00021752, -368.55631497, -0.00072506, 0.4, 0.3, 0.003, 0.0, 0.0, 21015, 2)
    ops.limitCurve('ThreePoint', 11015, 1015, 0.0, 147.42252599, 0.01819602, 147.42252599, 0.05458807, 103.19576819, -2138.90886704, 0.05, 2, 0, 71015, 22015, 1, 3)
    ops.uniaxialMaterial('LimitState', 31015, 36.8556315, 7.251e-05, 110.56689449, 0.00021752, 368.55631497, 0.00072506, -36.8556315, -7.251e-05, -110.56689449, -0.00021752, -368.55631497, -0.00072506, 0.4, 0.3, 0.003, 0.0, 0.0, 11015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1015, 99999, 'P', 41015, 'Vy', 31015, 'Vz', 21015, 'My', 11015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171015, 71015, 171015, 1015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122015, 122015, 22015, 1015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171016, 13.0, 13.2, 3.075)
    ops.node(122016, 13.0, 13.2, 5.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1016, 171016, 122016, 0.1225, 26354583.35465271, 10981076.39777196, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21016, 82.69926462, 0.00099037, 100.75946853, 0.01577018, 10.07594685, 0.05601576, -82.69926462, -0.00099037, -100.75946853, -0.01577018, -10.07594685, -0.05601576, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11016, 72.04433569, 0.00099037, 87.7776726, 0.01577018, 8.77776726, 0.05601576, -72.04433569, -0.00099037, -87.7776726, -0.01577018, -8.77776726, -0.05601576, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21016, 1016, 0.0, 115.55426823, 0.01980741, 115.55426823, 0.05942223, 80.88798776, -1715.88805194, 0.05, 2, 0, 71016, 22016, 2, 3)
    ops.uniaxialMaterial('LimitState', 41016, 28.88856706, 7.216e-05, 86.66570117, 0.00021647, 288.88567057, 0.00072158, -28.88856706, -7.216e-05, -86.66570117, -0.00021647, -288.88567057, -0.00072158, 0.4, 0.3, 0.003, 0.0, 0.0, 21016, 2)
    ops.limitCurve('ThreePoint', 11016, 1016, 0.0, 115.55426823, 0.01980741, 115.55426823, 0.05942223, 80.88798776, -1715.88805194, 0.05, 2, 0, 71016, 22016, 1, 3)
    ops.uniaxialMaterial('LimitState', 31016, 28.88856706, 7.216e-05, 86.66570117, 0.00021647, 288.88567057, 0.00072158, -28.88856706, -7.216e-05, -86.66570117, -0.00021647, -288.88567057, -0.00072158, 0.4, 0.3, 0.003, 0.0, 0.0, 11016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1016, 99999, 'P', 41016, 'Vy', 31016, 'Vz', 21016, 'My', 11016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171016, 71016, 171016, 1016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122016, 122016, 22016, 1016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172001, 0.0, 0.0, 5.875)
    ops.node(123001, 0.0, 0.0, 8.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2001, 172001, 123001, 0.0625, 26971058.91961571, 11237941.21650655, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22001, 39.33551479, 0.0013778, 47.81688195, 0.0178569, 4.78168819, 0.06860198, -39.33551479, -0.0013778, -47.81688195, -0.0178569, -4.78168819, -0.06860198, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12001, 36.12441261, 0.0013778, 43.91341469, 0.0178569, 4.39134147, 0.06860198, -36.12441261, -0.0013778, -43.91341469, -0.0178569, -4.39134147, -0.06860198, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22001, 2001, 0.0, 63.28342052, 0.02755606, 63.28342052, 0.08266818, 44.29839436, -1254.38490462, 0.05, 2, 0, 72001, 23001, 2, 3)
    ops.uniaxialMaterial('LimitState', 42001, 15.82085513, 7.568e-05, 47.46256539, 0.00022705, 158.2085513, 0.00075684, -15.82085513, -7.568e-05, -47.46256539, -0.00022705, -158.2085513, -0.00075684, 0.4, 0.3, 0.003, 0.0, 0.0, 22001, 2)
    ops.limitCurve('ThreePoint', 12001, 2001, 0.0, 63.28342052, 0.02755606, 63.28342052, 0.08266818, 44.29839436, -1254.38490462, 0.05, 2, 0, 72001, 23001, 1, 3)
    ops.uniaxialMaterial('LimitState', 32001, 15.82085513, 7.568e-05, 47.46256539, 0.00022705, 158.2085513, 0.00075684, -15.82085513, -7.568e-05, -47.46256539, -0.00022705, -158.2085513, -0.00075684, 0.4, 0.3, 0.003, 0.0, 0.0, 12001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2001, 99999, 'P', 42001, 'Vy', 32001, 'Vz', 22001, 'My', 12001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172001, 72001, 172001, 2001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123001, 123001, 23001, 2001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172004, 13.0, 0.0, 5.875)
    ops.node(123004, 13.0, 0.0, 8.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2004, 172004, 123004, 0.0625, 27469101.87824628, 11445459.11593595, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22004, 38.94594077, 0.00133084, 47.31397809, 0.02222863, 4.73139781, 0.0738124, -38.94594077, -0.00133084, -47.31397809, -0.02222863, -4.73139781, -0.0738124, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12004, 35.74109592, 0.00133084, 43.42053102, 0.02222863, 4.3420531, 0.0738124, -35.74109592, -0.00133084, -43.42053102, -0.02222863, -4.3420531, -0.0738124, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22004, 2004, 0.0, 78.27624948, 0.02661679, 78.27624948, 0.07985037, 54.79337464, -1581.77904614, 0.05, 2, 0, 72004, 23004, 2, 3)
    ops.uniaxialMaterial('LimitState', 42004, 19.56906237, 9.192e-05, 58.70718711, 0.00027575, 195.6906237, 0.00091917, -19.56906237, -9.192e-05, -58.70718711, -0.00027575, -195.6906237, -0.00091917, 0.4, 0.3, 0.003, 0.0, 0.0, 22004, 2)
    ops.limitCurve('ThreePoint', 12004, 2004, 0.0, 78.27624948, 0.02661679, 78.27624948, 0.07985037, 54.79337464, -1581.77904614, 0.05, 2, 0, 72004, 23004, 1, 3)
    ops.uniaxialMaterial('LimitState', 32004, 19.56906237, 9.192e-05, 58.70718711, 0.00027575, 195.6906237, 0.00091917, -19.56906237, -9.192e-05, -58.70718711, -0.00027575, -195.6906237, -0.00091917, 0.4, 0.3, 0.003, 0.0, 0.0, 12004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2004, 99999, 'P', 42004, 'Vy', 32004, 'Vz', 22004, 'My', 12004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172004, 72004, 172004, 2004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123004, 123004, 23004, 2004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172005, 0.0, 4.4, 5.9)
    ops.node(123005, 0.0, 4.4, 8.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2005, 172005, 123005, 0.1225, 26253179.92213515, 10938824.96755631, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22005, 83.06800189, 0.00090625, 101.14556535, 0.01662847, 10.11455653, 0.05587395, -83.06800189, -0.00090625, -101.14556535, -0.01662847, -10.11455653, -0.05587395, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12005, 71.73440006, 0.00090625, 87.34550349, 0.01662847, 8.73455035, 0.05587395, -71.73440006, -0.00090625, -87.34550349, -0.01662847, -8.73455035, -0.05587395, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22005, 2005, 0.0, 115.12718823, 0.01812496, 115.12718823, 0.05437489, 80.58903176, -1640.00004454, 0.05, 2, 0, 72005, 23005, 2, 3)
    ops.uniaxialMaterial('LimitState', 42005, 28.78179706, 7.217e-05, 86.34539117, 0.00021651, 287.81797057, 0.00072169, -28.78179706, -7.217e-05, -86.34539117, -0.00021651, -287.81797057, -0.00072169, 0.4, 0.3, 0.003, 0.0, 0.0, 22005, 2)
    ops.limitCurve('ThreePoint', 12005, 2005, 0.0, 115.12718823, 0.01812496, 115.12718823, 0.05437489, 80.58903176, -1640.00004454, 0.05, 2, 0, 72005, 23005, 1, 3)
    ops.uniaxialMaterial('LimitState', 32005, 28.78179706, 7.217e-05, 86.34539117, 0.00021651, 287.81797057, 0.00072169, -28.78179706, -7.217e-05, -86.34539117, -0.00021651, -287.81797057, -0.00072169, 0.4, 0.3, 0.003, 0.0, 0.0, 12005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2005, 99999, 'P', 42005, 'Vy', 32005, 'Vz', 22005, 'My', 12005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172005, 72005, 172005, 2005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123005, 123005, 23005, 2005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172006, 5.05, 4.4, 5.9)
    ops.node(123006, 5.05, 4.4, 8.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2006, 172006, 123006, 0.16, 28204584.60188689, 11751910.25078621, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22006, 134.61369419, 0.00095363, 163.4958927, 0.02710126, 16.34958927, 0.06500685, -134.61369419, -0.00095363, -163.4958927, -0.02710126, -16.34958927, -0.06500685, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12006, 134.61369419, 0.00095363, 163.4958927, 0.02710126, 16.34958927, 0.06500685, -134.61369419, -0.00095363, -163.4958927, -0.02710126, -16.34958927, -0.06500685, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22006, 2006, 0.0, 162.44899399, 0.0190725, 162.44899399, 0.05721751, 113.71429579, -2289.22593699, 0.05, 2, 0, 72006, 23006, 2, 3)
    ops.uniaxialMaterial('LimitState', 42006, 40.6122485, 7.257e-05, 121.83674549, 0.00021772, 406.12248498, 0.00072572, -40.6122485, -7.257e-05, -121.83674549, -0.00021772, -406.12248498, -0.00072572, 0.4, 0.3, 0.003, 0.0, 0.0, 22006, 2)
    ops.limitCurve('ThreePoint', 12006, 2006, 0.0, 162.44899399, 0.0190725, 162.44899399, 0.05721751, 113.71429579, -2289.22593699, 0.05, 2, 0, 72006, 23006, 1, 3)
    ops.uniaxialMaterial('LimitState', 32006, 40.6122485, 7.257e-05, 121.83674549, 0.00021772, 406.12248498, 0.00072572, -40.6122485, -7.257e-05, -121.83674549, -0.00021772, -406.12248498, -0.00072572, 0.4, 0.3, 0.003, 0.0, 0.0, 12006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2006, 99999, 'P', 42006, 'Vy', 32006, 'Vz', 22006, 'My', 12006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172006, 72006, 172006, 2006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123006, 123006, 23006, 2006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172007, 7.95, 4.4, 5.9)
    ops.node(123007, 7.95, 4.4, 8.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2007, 172007, 123007, 0.16, 27532434.52446334, 11471847.71852639, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22007, 134.83305938, 0.00097885, 163.93713849, 0.02474127, 16.39371385, 0.06197401, -134.83305938, -0.00097885, -163.93713849, -0.02474127, -16.39371385, -0.06197401, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12007, 134.83305938, 0.00097885, 163.93713849, 0.02474127, 16.39371385, 0.06197401, -134.83305938, -0.00097885, -163.93713849, -0.02474127, -16.39371385, -0.06197401, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22007, 2007, 0.0, 151.56953044, 0.01957696, 151.56953044, 0.05873088, 106.09867131, -1975.59058663, 0.05, 2, 0, 72007, 23007, 2, 3)
    ops.uniaxialMaterial('LimitState', 42007, 37.89238261, 6.936e-05, 113.67714783, 0.00020809, 378.92382611, 0.00069365, -37.89238261, -6.936e-05, -113.67714783, -0.00020809, -378.92382611, -0.00069365, 0.4, 0.3, 0.003, 0.0, 0.0, 22007, 2)
    ops.limitCurve('ThreePoint', 12007, 2007, 0.0, 151.56953044, 0.01957696, 151.56953044, 0.05873088, 106.09867131, -1975.59058663, 0.05, 2, 0, 72007, 23007, 1, 3)
    ops.uniaxialMaterial('LimitState', 32007, 37.89238261, 6.936e-05, 113.67714783, 0.00020809, 378.92382611, 0.00069365, -37.89238261, -6.936e-05, -113.67714783, -0.00020809, -378.92382611, -0.00069365, 0.4, 0.3, 0.003, 0.0, 0.0, 12007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2007, 99999, 'P', 42007, 'Vy', 32007, 'Vz', 22007, 'My', 12007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172007, 72007, 172007, 2007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123007, 123007, 23007, 2007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172008, 13.0, 4.4, 5.9)
    ops.node(123008, 13.0, 4.4, 8.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2008, 172008, 123008, 0.1225, 27624398.41257858, 11510166.00524108, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22008, 89.43458037, 0.00096361, 108.71254773, 0.0173698, 10.87125477, 0.05833997, -89.43458037, -0.00096361, -108.71254773, -0.0173698, -10.87125477, -0.05833997, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12008, 76.99844999, 0.00096361, 93.59576167, 0.0173698, 9.35957617, 0.05833997, -76.99844999, -0.00096361, -93.59576167, -0.0173698, -9.35957617, -0.05833997, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22008, 2008, 0.0, 125.9020564, 0.0192721, 125.9020564, 0.05781631, 88.13143948, -1890.8617496, 0.05, 2, 0, 72008, 23008, 2, 3)
    ops.uniaxialMaterial('LimitState', 42008, 31.4755141, 7.501e-05, 94.4265423, 0.00022502, 314.75514099, 0.00075006, -31.4755141, -7.501e-05, -94.4265423, -0.00022502, -314.75514099, -0.00075006, 0.4, 0.3, 0.003, 0.0, 0.0, 22008, 2)
    ops.limitCurve('ThreePoint', 12008, 2008, 0.0, 125.9020564, 0.0192721, 125.9020564, 0.05781631, 88.13143948, -1890.8617496, 0.05, 2, 0, 72008, 23008, 1, 3)
    ops.uniaxialMaterial('LimitState', 32008, 31.4755141, 7.501e-05, 94.4265423, 0.00022502, 314.75514099, 0.00075006, -31.4755141, -7.501e-05, -94.4265423, -0.00022502, -314.75514099, -0.00075006, 0.4, 0.3, 0.003, 0.0, 0.0, 12008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2008, 99999, 'P', 42008, 'Vy', 32008, 'Vz', 22008, 'My', 12008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172008, 72008, 172008, 2008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123008, 123008, 23008, 2008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172009, 0.0, 8.8, 5.9)
    ops.node(123009, 0.0, 8.8, 8.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2009, 172009, 123009, 0.1225, 27130705.82017782, 11304460.75840742, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22009, 94.69416499, 0.00104365, 115.18552204, 0.01775295, 11.5185522, 0.05319299, -94.69416499, -0.00104365, -115.18552204, -0.01775295, -11.5185522, -0.05319299, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12009, 88.93616708, 0.00104365, 108.18152138, 0.01775295, 10.81815214, 0.05319299, -88.93616708, -0.00104365, -108.18152138, -0.01775295, -10.81815214, -0.05319299, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22009, 2009, 0.0, 114.2113282, 0.02087292, 114.2113282, 0.06261877, 79.94792974, -1485.66331839, 0.05, 2, 0, 72009, 23009, 2, 3)
    ops.uniaxialMaterial('LimitState', 42009, 28.55283205, 6.928e-05, 85.65849615, 0.00020784, 285.5283205, 0.00069279, -28.55283205, -6.928e-05, -85.65849615, -0.00020784, -285.5283205, -0.00069279, 0.4, 0.3, 0.003, 0.0, 0.0, 22009, 2)
    ops.limitCurve('ThreePoint', 12009, 2009, 0.0, 114.2113282, 0.02087292, 114.2113282, 0.06261877, 79.94792974, -1485.66331839, 0.05, 2, 0, 72009, 23009, 1, 3)
    ops.uniaxialMaterial('LimitState', 32009, 28.55283205, 6.928e-05, 85.65849615, 0.00020784, 285.5283205, 0.00069279, -28.55283205, -6.928e-05, -85.65849615, -0.00020784, -285.5283205, -0.00069279, 0.4, 0.3, 0.003, 0.0, 0.0, 12009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2009, 99999, 'P', 42009, 'Vy', 32009, 'Vz', 22009, 'My', 12009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172009, 72009, 172009, 2009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123009, 123009, 23009, 2009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172010, 5.05, 8.8, 5.9)
    ops.node(123010, 5.05, 8.8, 8.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2010, 172010, 123010, 0.16, 28993110.08850084, 12080462.53687535, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22010, 137.45074304, 0.00095379, 166.76143666, 0.02928993, 16.67614367, 0.07525683, -137.45074304, -0.00095379, -166.76143666, -0.02928993, -16.67614367, -0.07525683, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12010, 137.45074304, 0.00095379, 166.76143666, 0.02928993, 16.67614367, 0.07525683, -137.45074304, -0.00095379, -166.76143666, -0.02928993, -16.67614367, -0.07525683, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22010, 2010, 0.0, 169.1220794, 0.0190759, 169.1220794, 0.0572277, 118.38545558, -2494.66383261, 0.05, 2, 0, 72010, 23010, 2, 3)
    ops.uniaxialMaterial('LimitState', 42010, 42.28051985, 7.35e-05, 126.84155955, 0.00022049, 422.80519851, 0.00073498, -42.28051985, -7.35e-05, -126.84155955, -0.00022049, -422.80519851, -0.00073498, 0.4, 0.3, 0.003, 0.0, 0.0, 22010, 2)
    ops.limitCurve('ThreePoint', 12010, 2010, 0.0, 169.1220794, 0.0190759, 169.1220794, 0.0572277, 118.38545558, -2494.66383261, 0.05, 2, 0, 72010, 23010, 1, 3)
    ops.uniaxialMaterial('LimitState', 32010, 42.28051985, 7.35e-05, 126.84155955, 0.00022049, 422.80519851, 0.00073498, -42.28051985, -7.35e-05, -126.84155955, -0.00022049, -422.80519851, -0.00073498, 0.4, 0.3, 0.003, 0.0, 0.0, 12010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2010, 99999, 'P', 42010, 'Vy', 32010, 'Vz', 22010, 'My', 12010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172010, 72010, 172010, 2010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123010, 123010, 23010, 2010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172011, 7.95, 8.8, 5.9)
    ops.node(123011, 7.95, 8.8, 8.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2011, 172011, 123011, 0.16, 27939068.65764095, 11641278.60735039, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22011, 138.53581861, 0.00098168, 168.40370846, 0.02894437, 16.84037085, 0.07381235, -138.53581861, -0.00098168, -168.40370846, -0.02894437, -16.84037085, -0.07381235, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12011, 138.53581861, 0.00098168, 168.40370846, 0.02894437, 16.84037085, 0.07381235, -138.53581861, -0.00098168, -168.40370846, -0.02894437, -16.84037085, -0.07381235, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22011, 2011, 0.0, 161.83182614, 0.01963354, 161.83182614, 0.05890062, 113.2822783, -2388.99242559, 0.05, 2, 0, 72011, 23011, 2, 3)
    ops.uniaxialMaterial('LimitState', 42011, 40.45795653, 7.298e-05, 121.3738696, 0.00021895, 404.57956535, 0.00072983, -40.45795653, -7.298e-05, -121.3738696, -0.00021895, -404.57956535, -0.00072983, 0.4, 0.3, 0.003, 0.0, 0.0, 22011, 2)
    ops.limitCurve('ThreePoint', 12011, 2011, 0.0, 161.83182614, 0.01963354, 161.83182614, 0.05890062, 113.2822783, -2388.99242559, 0.05, 2, 0, 72011, 23011, 1, 3)
    ops.uniaxialMaterial('LimitState', 32011, 40.45795653, 7.298e-05, 121.3738696, 0.00021895, 404.57956535, 0.00072983, -40.45795653, -7.298e-05, -121.3738696, -0.00021895, -404.57956535, -0.00072983, 0.4, 0.3, 0.003, 0.0, 0.0, 12011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2011, 99999, 'P', 42011, 'Vy', 32011, 'Vz', 22011, 'My', 12011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172011, 72011, 172011, 2011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123011, 123011, 23011, 2011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172012, 13.0, 8.8, 5.9)
    ops.node(123012, 13.0, 8.8, 8.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2012, 172012, 123012, 0.1225, 26018517.25641327, 10841048.85683887, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22012, 94.40121313, 0.00112598, 114.97048833, 0.01796581, 11.49704883, 0.05211945, -94.40121313, -0.00112598, -114.97048833, -0.01796581, -11.49704883, -0.05211945, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12012, 88.9443507, 0.00112598, 108.32461888, 0.01796581, 10.83246189, 0.05211945, -88.9443507, -0.00112598, -108.32461888, -0.01796581, -10.83246189, -0.05211945, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22012, 2012, 0.0, 110.01548225, 0.02251966, 110.01548225, 0.06755897, 77.01083758, -1471.3912836, 0.05, 2, 0, 72012, 23012, 2, 3)
    ops.uniaxialMaterial('LimitState', 42012, 27.50387056, 6.959e-05, 82.51161169, 0.00020876, 275.03870563, 0.00069587, -27.50387056, -6.959e-05, -82.51161169, -0.00020876, -275.03870563, -0.00069587, 0.4, 0.3, 0.003, 0.0, 0.0, 22012, 2)
    ops.limitCurve('ThreePoint', 12012, 2012, 0.0, 110.01548225, 0.02251966, 110.01548225, 0.06755897, 77.01083758, -1471.3912836, 0.05, 2, 0, 72012, 23012, 1, 3)
    ops.uniaxialMaterial('LimitState', 32012, 27.50387056, 6.959e-05, 82.51161169, 0.00020876, 275.03870563, 0.00069587, -27.50387056, -6.959e-05, -82.51161169, -0.00020876, -275.03870563, -0.00069587, 0.4, 0.3, 0.003, 0.0, 0.0, 12012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2012, 99999, 'P', 42012, 'Vy', 32012, 'Vz', 22012, 'My', 12012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172012, 72012, 172012, 2012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123012, 123012, 23012, 2012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172013, 0.0, 13.2, 5.875)
    ops.node(123013, 0.0, 13.2, 8.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2013, 172013, 123013, 0.0625, 28488648.32723416, 11870270.13634757, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22013, 41.73728558, 0.00130113, 50.62638863, 0.02226389, 5.06263886, 0.07540887, -41.73728558, -0.00130113, -50.62638863, -0.02226389, -5.06263886, -0.07540887, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12013, 37.88894762, 0.00130113, 45.95844125, 0.02226389, 4.59584412, 0.07540887, -37.88894762, -0.00130113, -45.95844125, -0.02226389, -4.59584412, -0.07540887, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22013, 2013, 0.0, 83.46725401, 0.02602254, 83.46725401, 0.07806761, 58.42707781, -1762.48112178, 0.05, 2, 0, 72013, 23013, 2, 3)
    ops.uniaxialMaterial('LimitState', 42013, 20.8668135, 9.451e-05, 62.60044051, 0.00028352, 208.66813503, 0.00094505, -20.8668135, -9.451e-05, -62.60044051, -0.00028352, -208.66813503, -0.00094505, 0.4, 0.3, 0.003, 0.0, 0.0, 22013, 2)
    ops.limitCurve('ThreePoint', 12013, 2013, 0.0, 83.46725401, 0.02602254, 83.46725401, 0.07806761, 58.42707781, -1762.48112178, 0.05, 2, 0, 72013, 23013, 1, 3)
    ops.uniaxialMaterial('LimitState', 32013, 20.8668135, 9.451e-05, 62.60044051, 0.00028352, 208.66813503, 0.00094505, -20.8668135, -9.451e-05, -62.60044051, -0.00028352, -208.66813503, -0.00094505, 0.4, 0.3, 0.003, 0.0, 0.0, 12013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2013, 99999, 'P', 42013, 'Vy', 32013, 'Vz', 22013, 'My', 12013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172013, 72013, 172013, 2013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123013, 123013, 23013, 2013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172014, 5.05, 13.2, 5.875)
    ops.node(123014, 5.05, 13.2, 8.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2014, 172014, 123014, 0.1225, 30761984.08654795, 12817493.36939498, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22014, 80.24392721, 0.00088553, 97.02808729, 0.01583105, 9.70280873, 0.06119545, -80.24392721, -0.00088553, -97.02808729, -0.01583105, -9.70280873, -0.06119545, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12014, 69.4272389, 0.00088553, 83.94893458, 0.01583105, 8.39489346, 0.06119545, -69.4272389, -0.00088553, -83.94893458, -0.01583105, -8.39489346, -0.06119545, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22014, 2014, 0.0, 126.78298793, 0.01771061, 126.78298793, 0.05313183, 88.74809155, -1646.61744672, 0.05, 2, 0, 72014, 23014, 2, 3)
    ops.uniaxialMaterial('LimitState', 42014, 31.69574698, 6.783e-05, 95.08724095, 0.00020348, 316.95746982, 0.00067827, -31.69574698, -6.783e-05, -95.08724095, -0.00020348, -316.95746982, -0.00067827, 0.4, 0.3, 0.003, 0.0, 0.0, 22014, 2)
    ops.limitCurve('ThreePoint', 12014, 2014, 0.0, 126.78298793, 0.01771061, 126.78298793, 0.05313183, 88.74809155, -1646.61744672, 0.05, 2, 0, 72014, 23014, 1, 3)
    ops.uniaxialMaterial('LimitState', 32014, 31.69574698, 6.783e-05, 95.08724095, 0.00020348, 316.95746982, 0.00067827, -31.69574698, -6.783e-05, -95.08724095, -0.00020348, -316.95746982, -0.00067827, 0.4, 0.3, 0.003, 0.0, 0.0, 12014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2014, 99999, 'P', 42014, 'Vy', 32014, 'Vz', 22014, 'My', 12014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172014, 72014, 172014, 2014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123014, 123014, 23014, 2014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172015, 7.95, 13.2, 5.875)
    ops.node(123015, 7.95, 13.2, 8.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2015, 172015, 123015, 0.1225, 27602684.34676113, 11501118.47781714, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22015, 80.40651149, 0.00094384, 97.89140334, 0.02028332, 9.78914033, 0.06314108, -80.40651149, -0.00094384, -97.89140334, -0.02028332, -9.78914033, -0.06314108, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12015, 69.53426416, 0.00094384, 84.65491877, 0.02028332, 8.46549188, 0.06314108, -69.53426416, -0.00094384, -84.65491877, -0.02028332, -8.46549188, -0.06314108, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22015, 2015, 0.0, 127.46392466, 0.01887674, 127.46392466, 0.05663021, 89.22474726, -2232.65135218, 0.05, 2, 0, 72015, 23015, 2, 3)
    ops.uniaxialMaterial('LimitState', 42015, 31.86598117, 7.6e-05, 95.5979435, 0.00022799, 318.65981166, 0.00075996, -31.86598117, -7.6e-05, -95.5979435, -0.00022799, -318.65981166, -0.00075996, 0.4, 0.3, 0.003, 0.0, 0.0, 22015, 2)
    ops.limitCurve('ThreePoint', 12015, 2015, 0.0, 127.46392466, 0.01887674, 127.46392466, 0.05663021, 89.22474726, -2232.65135218, 0.05, 2, 0, 72015, 23015, 1, 3)
    ops.uniaxialMaterial('LimitState', 32015, 31.86598117, 7.6e-05, 95.5979435, 0.00022799, 318.65981166, 0.00075996, -31.86598117, -7.6e-05, -95.5979435, -0.00022799, -318.65981166, -0.00075996, 0.4, 0.3, 0.003, 0.0, 0.0, 12015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2015, 99999, 'P', 42015, 'Vy', 32015, 'Vz', 22015, 'My', 12015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172015, 72015, 172015, 2015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123015, 123015, 23015, 2015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172016, 13.0, 13.2, 5.875)
    ops.node(123016, 13.0, 13.2, 8.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2016, 172016, 123016, 0.0625, 29706044.79564267, 12377518.66485111, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22016, 38.08464519, 0.00134155, 46.08817437, 0.01870794, 4.60881744, 0.07347434, -38.08464519, -0.00134155, -46.08817437, -0.01870794, -4.60881744, -0.07347434, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12016, 35.35625416, 0.00134155, 42.78640903, 0.01870794, 4.2786409, 0.07347434, -35.35625416, -0.00134155, -42.78640903, -0.01870794, -4.2786409, -0.07347434, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22016, 2016, 0.0, 73.39224805, 0.02683094, 73.39224805, 0.08049282, 51.37457364, -1301.17939453, 0.05, 2, 0, 72016, 23016, 2, 3)
    ops.uniaxialMaterial('LimitState', 42016, 18.34806201, 7.969e-05, 55.04418604, 0.00023908, 183.48062013, 0.00079692, -18.34806201, -7.969e-05, -55.04418604, -0.00023908, -183.48062013, -0.00079692, 0.4, 0.3, 0.003, 0.0, 0.0, 22016, 2)
    ops.limitCurve('ThreePoint', 12016, 2016, 0.0, 73.39224805, 0.02683094, 73.39224805, 0.08049282, 51.37457364, -1301.17939453, 0.05, 2, 0, 72016, 23016, 1, 3)
    ops.uniaxialMaterial('LimitState', 32016, 18.34806201, 7.969e-05, 55.04418604, 0.00023908, 183.48062013, 0.00079692, -18.34806201, -7.969e-05, -55.04418604, -0.00023908, -183.48062013, -0.00079692, 0.4, 0.3, 0.003, 0.0, 0.0, 12016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2016, 99999, 'P', 42016, 'Vy', 32016, 'Vz', 22016, 'My', 12016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172016, 72016, 172016, 2016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123016, 123016, 23016, 2016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173001, 0.0, 0.0, 8.675)
    ops.node(124001, 0.0, 0.0, 11.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3001, 173001, 124001, 0.0625, 26935038.34657495, 11222932.64440623, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23001, 44.6712251, 0.00134115, 54.67264384, 0.02495712, 5.46726438, 0.08692052, -44.6712251, -0.00134115, -54.67264384, -0.02495712, -5.46726438, -0.08692052, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13001, 37.28747361, 0.00134115, 45.63574784, 0.02495712, 4.56357478, 0.08692052, -37.28747361, -0.00134115, -45.63574784, -0.02495712, -4.56357478, -0.08692052, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23001, 3001, 0.0, 71.08890787, 0.02682309, 71.08890787, 0.08046928, 49.76223551, -3344.06462772, 0.05, 2, 0, 73001, 24001, 2, 3)
    ops.uniaxialMaterial('LimitState', 43001, 17.77222697, 8.513e-05, 53.3166809, 0.0002554, 177.72226967, 0.00085132, -17.77222697, -8.513e-05, -53.3166809, -0.0002554, -177.72226967, -0.00085132, 0.4, 0.3, 0.003, 0.0, 0.0, 23001, 2)
    ops.limitCurve('ThreePoint', 13001, 3001, 0.0, 71.08890787, 0.02682309, 71.08890787, 0.08046928, 49.76223551, -3344.06462772, 0.05, 2, 0, 73001, 24001, 1, 3)
    ops.uniaxialMaterial('LimitState', 33001, 17.77222697, 8.513e-05, 53.3166809, 0.0002554, 177.72226967, 0.00085132, -17.77222697, -8.513e-05, -53.3166809, -0.0002554, -177.72226967, -0.00085132, 0.4, 0.3, 0.003, 0.0, 0.0, 13001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3001, 99999, 'P', 43001, 'Vy', 33001, 'Vz', 23001, 'My', 13001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173001, 73001, 173001, 3001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124001, 124001, 24001, 3001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173004, 13.0, 0.0, 8.675)
    ops.node(124004, 13.0, 0.0, 11.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3004, 173004, 124004, 0.0625, 27884144.93644137, 11618393.72351724, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23004, 44.9233103, 0.00129418, 54.87225755, 0.02003535, 5.48722575, 0.08252327, -44.9233103, -0.00129418, -54.87225755, -0.02003535, -5.48722575, -0.08252327, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13004, 37.37192989, 0.00129418, 45.64850962, 0.02003535, 4.56485096, 0.08252327, -37.37192989, -0.00129418, -45.64850962, -0.02003535, -4.56485096, -0.08252327, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23004, 3004, 0.0, 59.64541281, 0.02588351, 59.64541281, 0.07765054, 41.75178897, -2387.68436573, 0.05, 2, 0, 73004, 24004, 2, 3)
    ops.uniaxialMaterial('LimitState', 43004, 14.9113532, 6.9e-05, 44.73405961, 0.00020699, 149.11353202, 0.00068997, -14.9113532, -6.9e-05, -44.73405961, -0.00020699, -149.11353202, -0.00068997, 0.4, 0.3, 0.003, 0.0, 0.0, 23004, 2)
    ops.limitCurve('ThreePoint', 13004, 3004, 0.0, 59.64541281, 0.02588351, 59.64541281, 0.07765054, 41.75178897, -2387.68436573, 0.05, 2, 0, 73004, 24004, 1, 3)
    ops.uniaxialMaterial('LimitState', 33004, 14.9113532, 6.9e-05, 44.73405961, 0.00020699, 149.11353202, 0.00068997, -14.9113532, -6.9e-05, -44.73405961, -0.00020699, -149.11353202, -0.00068997, 0.4, 0.3, 0.003, 0.0, 0.0, 13004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3004, 99999, 'P', 43004, 'Vy', 33004, 'Vz', 23004, 'My', 13004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173004, 73004, 173004, 3004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124004, 124004, 24004, 3004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173005, 0.0, 4.4, 8.7)
    ops.node(124005, 0.0, 4.4, 10.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3005, 173005, 124005, 0.1225, 27301843.93728144, 11375768.3072006, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23005, 95.09312854, 0.00096843, 116.29916973, 0.02527455, 11.62991697, 0.08215555, -95.09312854, -0.00096843, -116.29916973, -0.02527455, -11.62991697, -0.08215555, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13005, 74.66414306, 0.00096843, 91.31446172, 0.02527455, 9.13144617, 0.08215555, -74.66414306, -0.00096843, -91.31446172, -0.02527455, -9.13144617, -0.08215555, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23005, 3005, 0.0, 125.82895104, 0.01936857, 125.82895104, 0.05810572, 88.08026573, -4611.75735905, 0.05, 2, 0, 73005, 24005, 2, 3)
    ops.uniaxialMaterial('LimitState', 43005, 31.45723776, 7.585e-05, 94.37171328, 0.00022754, 314.5723776, 0.00075848, -31.45723776, -7.585e-05, -94.37171328, -0.00022754, -314.5723776, -0.00075848, 0.4, 0.3, 0.003, 0.0, 0.0, 23005, 2)
    ops.limitCurve('ThreePoint', 13005, 3005, 0.0, 125.82895104, 0.01936857, 125.82895104, 0.05810572, 88.08026573, -4611.75735905, 0.05, 2, 0, 73005, 24005, 1, 3)
    ops.uniaxialMaterial('LimitState', 33005, 31.45723776, 7.585e-05, 94.37171328, 0.00022754, 314.5723776, 0.00075848, -31.45723776, -7.585e-05, -94.37171328, -0.00022754, -314.5723776, -0.00075848, 0.4, 0.3, 0.003, 0.0, 0.0, 13005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3005, 99999, 'P', 43005, 'Vy', 33005, 'Vz', 23005, 'My', 13005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173005, 73005, 173005, 3005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124005, 124005, 24005, 3005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173006, 5.05, 4.4, 8.7)
    ops.node(124006, 5.05, 4.4, 10.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3006, 173006, 124006, 0.16, 27340209.43542022, 11391753.93142509, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23006, 112.66221169, 0.00094088, 137.72695511, 0.02801764, 13.77269551, 0.07120064, -112.66221169, -0.00094088, -137.72695511, -0.02801764, -13.77269551, -0.07120064, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13006, 112.66221169, 0.00094088, 137.72695511, 0.02801764, 13.77269551, 0.07120064, -112.66221169, -0.00094088, -137.72695511, -0.02801764, -13.77269551, -0.07120064, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23006, 3006, 0.0, 142.97812323, 0.01881759, 142.97812323, 0.05645276, 100.08468626, -3304.62127611, 0.05, 2, 0, 73006, 24006, 2, 3)
    ops.uniaxialMaterial('LimitState', 43006, 35.74453081, 6.589e-05, 107.23359242, 0.00019768, 357.44530808, 0.00065893, -35.74453081, -6.589e-05, -107.23359242, -0.00019768, -357.44530808, -0.00065893, 0.4, 0.3, 0.003, 0.0, 0.0, 23006, 2)
    ops.limitCurve('ThreePoint', 13006, 3006, 0.0, 142.97812323, 0.01881759, 142.97812323, 0.05645276, 100.08468626, -3304.62127611, 0.05, 2, 0, 73006, 24006, 1, 3)
    ops.uniaxialMaterial('LimitState', 33006, 35.74453081, 6.589e-05, 107.23359242, 0.00019768, 357.44530808, 0.00065893, -35.74453081, -6.589e-05, -107.23359242, -0.00019768, -357.44530808, -0.00065893, 0.4, 0.3, 0.003, 0.0, 0.0, 13006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3006, 99999, 'P', 43006, 'Vy', 33006, 'Vz', 23006, 'My', 13006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173006, 73006, 173006, 3006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124006, 124006, 24006, 3006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173007, 7.95, 4.4, 8.7)
    ops.node(124007, 7.95, 4.4, 10.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3007, 173007, 124007, 0.16, 28891551.43561214, 12038146.43150506, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23007, 114.7615528, 0.00093046, 139.80884533, 0.02496003, 13.98088453, 0.06875379, -114.7615528, -0.00093046, -139.80884533, -0.02496003, -13.98088453, -0.06875379, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13007, 114.7615528, 0.00093046, 139.80884533, 0.02496003, 13.98088453, 0.06875379, -114.7615528, -0.00093046, -139.80884533, -0.02496003, -13.98088453, -0.06875379, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23007, 3007, 0.0, 142.77416873, 0.01860917, 142.77416873, 0.0558275, 99.94191811, -2720.45280078, 0.05, 2, 0, 73007, 24007, 2, 3)
    ops.uniaxialMaterial('LimitState', 43007, 35.69354218, 6.227e-05, 107.08062655, 0.0001868, 356.93542182, 0.00062266, -35.69354218, -6.227e-05, -107.08062655, -0.0001868, -356.93542182, -0.00062266, 0.4, 0.3, 0.003, 0.0, 0.0, 23007, 2)
    ops.limitCurve('ThreePoint', 13007, 3007, 0.0, 142.77416873, 0.01860917, 142.77416873, 0.0558275, 99.94191811, -2720.45280078, 0.05, 2, 0, 73007, 24007, 1, 3)
    ops.uniaxialMaterial('LimitState', 33007, 35.69354218, 6.227e-05, 107.08062655, 0.0001868, 356.93542182, 0.00062266, -35.69354218, -6.227e-05, -107.08062655, -0.0001868, -356.93542182, -0.00062266, 0.4, 0.3, 0.003, 0.0, 0.0, 13007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3007, 99999, 'P', 43007, 'Vy', 33007, 'Vz', 23007, 'My', 13007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173007, 73007, 173007, 3007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124007, 124007, 24007, 3007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173008, 13.0, 4.4, 8.7)
    ops.node(124008, 13.0, 4.4, 10.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3008, 173008, 124008, 0.1225, 27751050.16911313, 11562937.57046381, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23008, 103.06598108, 0.00094909, 125.93000072, 0.02739098, 12.59300007, 0.08449365, -103.06598108, -0.00094909, -125.93000072, -0.02739098, -12.59300007, -0.08449365, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13008, 78.69423782, 0.00094909, 96.15166247, 0.02739098, 9.61516625, 0.08449365, -78.69423782, -0.00094909, -96.15166247, -0.02739098, -9.61516625, -0.08449365, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23008, 3008, 0.0, 134.57138743, 0.01898176, 134.57138743, 0.05694528, 94.1999712, -5534.00226528, 0.05, 2, 0, 73008, 24008, 2, 3)
    ops.uniaxialMaterial('LimitState', 43008, 33.64284686, 7.98e-05, 100.92854057, 0.00023941, 336.42846858, 0.00079805, -33.64284686, -7.98e-05, -100.92854057, -0.00023941, -336.42846858, -0.00079805, 0.4, 0.3, 0.003, 0.0, 0.0, 23008, 2)
    ops.limitCurve('ThreePoint', 13008, 3008, 0.0, 134.57138743, 0.01898176, 134.57138743, 0.05694528, 94.1999712, -5534.00226528, 0.05, 2, 0, 73008, 24008, 1, 3)
    ops.uniaxialMaterial('LimitState', 33008, 33.64284686, 7.98e-05, 100.92854057, 0.00023941, 336.42846858, 0.00079805, -33.64284686, -7.98e-05, -100.92854057, -0.00023941, -336.42846858, -0.00079805, 0.4, 0.3, 0.003, 0.0, 0.0, 13008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3008, 99999, 'P', 43008, 'Vy', 33008, 'Vz', 23008, 'My', 13008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173008, 73008, 173008, 3008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124008, 124008, 24008, 3008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173009, 0.0, 8.8, 8.7)
    ops.node(124009, 0.0, 8.8, 10.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3009, 173009, 124009, 0.1225, 30534227.3739001, 12722594.73912504, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23009, 104.74479771, 0.00095018, 127.08385464, 0.04047485, 12.70838546, 0.1138181, -104.74479771, -0.00095018, -127.08385464, -0.04047485, -12.70838546, -0.1138181, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13009, 88.50134883, 0.00095018, 107.37614465, 0.04047485, 10.73761447, 0.1138181, -88.50134883, -0.00095018, -107.37614465, -0.04047485, -10.73761447, -0.1138181, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23009, 3009, 0.0, 165.72248696, 0.01900358, 165.72248696, 0.05701074, 116.00574087, -8746.0053708, 0.05, 2, 0, 73009, 24009, 2, 3)
    ops.uniaxialMaterial('LimitState', 43009, 41.43062174, 8.932e-05, 124.29186522, 0.00026796, 414.30621741, 0.0008932, -41.43062174, -8.932e-05, -124.29186522, -0.00026796, -414.30621741, -0.0008932, 0.4, 0.3, 0.003, 0.0, 0.0, 23009, 2)
    ops.limitCurve('ThreePoint', 13009, 3009, 0.0, 165.72248696, 0.01900358, 165.72248696, 0.05701074, 116.00574087, -8746.0053708, 0.05, 2, 0, 73009, 24009, 1, 3)
    ops.uniaxialMaterial('LimitState', 33009, 41.43062174, 8.932e-05, 124.29186522, 0.00026796, 414.30621741, 0.0008932, -41.43062174, -8.932e-05, -124.29186522, -0.00026796, -414.30621741, -0.0008932, 0.4, 0.3, 0.003, 0.0, 0.0, 13009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3009, 99999, 'P', 43009, 'Vy', 33009, 'Vz', 23009, 'My', 13009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173009, 73009, 173009, 3009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124009, 124009, 24009, 3009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173010, 5.05, 8.8, 8.7)
    ops.node(124010, 5.05, 8.8, 10.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3010, 173010, 124010, 0.16, 27787165.49197738, 11577985.62165724, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23010, 112.58295939, 0.00093804, 137.54887944, 0.02786654, 13.75488794, 0.0716859, -112.58295939, -0.00093804, -137.54887944, -0.02786654, -13.75488794, -0.0716859, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13010, 112.58295939, 0.00093804, 137.54887944, 0.02786654, 13.75488794, 0.0716859, -112.58295939, -0.00093804, -137.54887944, -0.02786654, -13.75488794, -0.0716859, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23010, 3010, 0.0, 143.52891678, 0.01876083, 143.52891678, 0.0562825, 100.47024174, -3556.29047089, 0.05, 2, 0, 73010, 24010, 2, 3)
    ops.uniaxialMaterial('LimitState', 43010, 35.88222919, 6.508e-05, 107.64668758, 0.00019525, 358.82229194, 0.00065083, -35.88222919, -6.508e-05, -107.64668758, -0.00019525, -358.82229194, -0.00065083, 0.4, 0.3, 0.003, 0.0, 0.0, 23010, 2)
    ops.limitCurve('ThreePoint', 13010, 3010, 0.0, 143.52891678, 0.01876083, 143.52891678, 0.0562825, 100.47024174, -3556.29047089, 0.05, 2, 0, 73010, 24010, 1, 3)
    ops.uniaxialMaterial('LimitState', 33010, 35.88222919, 6.508e-05, 107.64668758, 0.00019525, 358.82229194, 0.00065083, -35.88222919, -6.508e-05, -107.64668758, -0.00019525, -358.82229194, -0.00065083, 0.4, 0.3, 0.003, 0.0, 0.0, 13010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3010, 99999, 'P', 43010, 'Vy', 33010, 'Vz', 23010, 'My', 13010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173010, 73010, 173010, 3010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124010, 124010, 24010, 3010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173011, 7.95, 8.8, 8.7)
    ops.node(124011, 7.95, 8.8, 10.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3011, 173011, 124011, 0.16, 25392268.25933572, 10580111.77472322, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23011, 112.1457968, 0.00099544, 137.63547786, 0.0280596, 13.76354779, 0.07083284, -112.1457968, -0.00099544, -137.63547786, -0.0280596, -13.76354779, -0.07083284, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13011, 112.1457968, 0.00099544, 137.63547786, 0.0280596, 13.76354779, 0.07083284, -112.1457968, -0.00099544, -137.63547786, -0.0280596, -13.76354779, -0.07083284, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23011, 3011, 0.0, 131.7990121, 0.01990882, 131.7990121, 0.05972646, 92.25930847, -3437.65453883, 0.05, 2, 0, 73011, 24011, 2, 3)
    ops.uniaxialMaterial('LimitState', 43011, 32.94975303, 6.54e-05, 98.84925908, 0.0001962, 329.49753026, 0.00065401, -32.94975303, -6.54e-05, -98.84925908, -0.0001962, -329.49753026, -0.00065401, 0.4, 0.3, 0.003, 0.0, 0.0, 23011, 2)
    ops.limitCurve('ThreePoint', 13011, 3011, 0.0, 131.7990121, 0.01990882, 131.7990121, 0.05972646, 92.25930847, -3437.65453883, 0.05, 2, 0, 73011, 24011, 1, 3)
    ops.uniaxialMaterial('LimitState', 33011, 32.94975303, 6.54e-05, 98.84925908, 0.0001962, 329.49753026, 0.00065401, -32.94975303, -6.54e-05, -98.84925908, -0.0001962, -329.49753026, -0.00065401, 0.4, 0.3, 0.003, 0.0, 0.0, 13011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3011, 99999, 'P', 43011, 'Vy', 33011, 'Vz', 23011, 'My', 13011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173011, 73011, 173011, 3011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124011, 124011, 24011, 3011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173012, 13.0, 8.8, 8.7)
    ops.node(124012, 13.0, 8.8, 10.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3012, 173012, 124012, 0.1225, 27042734.91592156, 11267806.21496732, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23012, 102.7199244, 0.0009747, 125.69291196, 0.04262826, 12.5692912, 0.11414319, -102.7199244, -0.0009747, -125.69291196, -0.04262826, -12.5692912, -0.11414319, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13012, 86.28988121, 0.0009747, 105.58834136, 0.04262826, 10.55883414, 0.11414319, -86.28988121, -0.0009747, -105.58834136, -0.04262826, -10.55883414, -0.11414319, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23012, 3012, 0.0, 157.60749724, 0.01949395, 157.60749724, 0.05848186, 110.32524807, -9463.67131567, 0.05, 2, 0, 73012, 24012, 2, 3)
    ops.uniaxialMaterial('LimitState', 43012, 39.40187431, 9.591e-05, 118.20562293, 0.00028774, 394.01874309, 0.00095914, -39.40187431, -9.591e-05, -118.20562293, -0.00028774, -394.01874309, -0.00095914, 0.4, 0.3, 0.003, 0.0, 0.0, 23012, 2)
    ops.limitCurve('ThreePoint', 13012, 3012, 0.0, 157.60749724, 0.01949395, 157.60749724, 0.05848186, 110.32524807, -9463.67131567, 0.05, 2, 0, 73012, 24012, 1, 3)
    ops.uniaxialMaterial('LimitState', 33012, 39.40187431, 9.591e-05, 118.20562293, 0.00028774, 394.01874309, 0.00095914, -39.40187431, -9.591e-05, -118.20562293, -0.00028774, -394.01874309, -0.00095914, 0.4, 0.3, 0.003, 0.0, 0.0, 13012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3012, 99999, 'P', 43012, 'Vy', 33012, 'Vz', 23012, 'My', 13012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173012, 73012, 173012, 3012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124012, 124012, 24012, 3012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173013, 0.0, 13.2, 8.675)
    ops.node(124013, 0.0, 13.2, 11.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3013, 173013, 124013, 0.0625, 29380084.67565384, 12241701.9481891, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23013, 41.43039056, 0.00124868, 50.42467951, 0.02010416, 5.04246795, 0.08328406, -41.43039056, -0.00124868, -50.42467951, -0.02010416, -5.04246795, -0.08328406, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13013, 35.10318971, 0.00124868, 42.72388135, 0.02010416, 4.27238814, 0.08328406, -35.10318971, -0.00124868, -42.72388135, -0.02010416, -4.27238814, -0.08328406, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23013, 3013, 0.0, 60.81261233, 0.02497366, 60.81261233, 0.07492097, 42.56882863, -2226.84674548, 0.05, 2, 0, 73013, 24013, 2, 3)
    ops.uniaxialMaterial('LimitState', 43013, 15.20315308, 6.677e-05, 45.60945925, 0.0002003, 152.03153082, 0.00066765, -15.20315308, -6.677e-05, -45.60945925, -0.0002003, -152.03153082, -0.00066765, 0.4, 0.3, 0.003, 0.0, 0.0, 23013, 2)
    ops.limitCurve('ThreePoint', 13013, 3013, 0.0, 60.81261233, 0.02497366, 60.81261233, 0.07492097, 42.56882863, -2226.84674548, 0.05, 2, 0, 73013, 24013, 1, 3)
    ops.uniaxialMaterial('LimitState', 33013, 15.20315308, 6.677e-05, 45.60945925, 0.0002003, 152.03153082, 0.00066765, -15.20315308, -6.677e-05, -45.60945925, -0.0002003, -152.03153082, -0.00066765, 0.4, 0.3, 0.003, 0.0, 0.0, 13013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3013, 99999, 'P', 43013, 'Vy', 33013, 'Vz', 23013, 'My', 13013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173013, 73013, 173013, 3013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124013, 124013, 24013, 3013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173014, 5.05, 13.2, 8.675)
    ops.node(124014, 5.05, 13.2, 11.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3014, 173014, 124014, 0.1225, 27212692.94175111, 11338622.05906296, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23014, 67.59864734, 0.00091277, 82.73347862, 0.01956482, 8.27334786, 0.06834487, -67.59864734, -0.00091277, -82.73347862, -0.01956482, -8.27334786, -0.06834487, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13014, 56.79859187, 0.00091277, 69.51537155, 0.01956482, 6.95153716, 0.06834487, -56.79859187, -0.00091277, -69.51537155, -0.01956482, -6.95153716, -0.06834487, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23014, 3014, 0.0, 111.17526915, 0.01825547, 111.17526915, 0.05476642, 77.82268841, -3723.75601997, 0.05, 2, 0, 73014, 24014, 2, 3)
    ops.uniaxialMaterial('LimitState', 43014, 27.79381729, 6.723e-05, 83.38145186, 0.0002017, 277.93817288, 0.00067234, -27.79381729, -6.723e-05, -83.38145186, -0.0002017, -277.93817288, -0.00067234, 0.4, 0.3, 0.003, 0.0, 0.0, 23014, 2)
    ops.limitCurve('ThreePoint', 13014, 3014, 0.0, 111.17526915, 0.01825547, 111.17526915, 0.05476642, 77.82268841, -3723.75601997, 0.05, 2, 0, 73014, 24014, 1, 3)
    ops.uniaxialMaterial('LimitState', 33014, 27.79381729, 6.723e-05, 83.38145186, 0.0002017, 277.93817288, 0.00067234, -27.79381729, -6.723e-05, -83.38145186, -0.0002017, -277.93817288, -0.00067234, 0.4, 0.3, 0.003, 0.0, 0.0, 13014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3014, 99999, 'P', 43014, 'Vy', 33014, 'Vz', 23014, 'My', 13014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173014, 73014, 173014, 3014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124014, 124014, 24014, 3014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173015, 7.95, 13.2, 8.675)
    ops.node(124015, 7.95, 13.2, 11.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3015, 173015, 124015, 0.1225, 24593834.09550582, 10247430.87312743, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23015, 65.58581742, 0.00094838, 80.64849, 0.01761646, 8.064849, 0.0652737, -65.58581742, -0.00094838, -80.64849, -0.01761646, -8.064849, -0.0652737, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13015, 55.25071071, 0.00094838, 67.93978586, 0.01761646, 6.79397859, 0.0652737, -55.25071071, -0.00094838, -67.93978586, -0.01761646, -6.79397859, -0.0652737, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23015, 3015, 0.0, 97.44827411, 0.01896759, 97.44827411, 0.05690277, 68.21379187, -3113.66684453, 0.05, 2, 0, 73015, 24015, 2, 3)
    ops.uniaxialMaterial('LimitState', 43015, 24.36206853, 6.521e-05, 73.08620558, 0.00019562, 243.62068527, 0.00065208, -24.36206853, -6.521e-05, -73.08620558, -0.00019562, -243.62068527, -0.00065208, 0.4, 0.3, 0.003, 0.0, 0.0, 23015, 2)
    ops.limitCurve('ThreePoint', 13015, 3015, 0.0, 97.44827411, 0.01896759, 97.44827411, 0.05690277, 68.21379187, -3113.66684453, 0.05, 2, 0, 73015, 24015, 1, 3)
    ops.uniaxialMaterial('LimitState', 33015, 24.36206853, 6.521e-05, 73.08620558, 0.00019562, 243.62068527, 0.00065208, -24.36206853, -6.521e-05, -73.08620558, -0.00019562, -243.62068527, -0.00065208, 0.4, 0.3, 0.003, 0.0, 0.0, 13015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3015, 99999, 'P', 43015, 'Vy', 33015, 'Vz', 23015, 'My', 13015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173015, 73015, 173015, 3015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124015, 124015, 24015, 3015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173016, 13.0, 13.2, 8.675)
    ops.node(124016, 13.0, 13.2, 11.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3016, 173016, 124016, 0.0625, 26493722.11040679, 11039050.87933616, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23016, 44.72183614, 0.00135332, 54.78086816, 0.02416301, 5.47808682, 0.08585578, -44.72183614, -0.00135332, -54.78086816, -0.02416301, -5.47808682, -0.08585578, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13016, 37.29844485, 0.00135332, 45.68777506, 0.02416301, 4.56877751, 0.08585578, -37.29844485, -0.00135332, -45.68777506, -0.02416301, -4.56877751, -0.08585578, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23016, 3016, 0.0, 69.13827398, 0.02706646, 69.13827398, 0.08119939, 48.39679179, -3172.75550219, 0.05, 2, 0, 73016, 24016, 2, 3)
    ops.uniaxialMaterial('LimitState', 43016, 17.2845685, 8.418e-05, 51.85370549, 0.00025253, 172.84568496, 0.00084176, -17.2845685, -8.418e-05, -51.85370549, -0.00025253, -172.84568496, -0.00084176, 0.4, 0.3, 0.003, 0.0, 0.0, 23016, 2)
    ops.limitCurve('ThreePoint', 13016, 3016, 0.0, 69.13827398, 0.02706646, 69.13827398, 0.08119939, 48.39679179, -3172.75550219, 0.05, 2, 0, 73016, 24016, 1, 3)
    ops.uniaxialMaterial('LimitState', 33016, 17.2845685, 8.418e-05, 51.85370549, 0.00025253, 172.84568496, 0.00084176, -17.2845685, -8.418e-05, -51.85370549, -0.00025253, -172.84568496, -0.00084176, 0.4, 0.3, 0.003, 0.0, 0.0, 13016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3016, 99999, 'P', 43016, 'Vy', 33016, 'Vz', 23016, 'My', 13016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173016, 73016, 173016, 3016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124016, 124016, 24016, 3016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170002, 5.05, 0.0, 0.0)
    ops.node(124017, 5.05, 0.0, 1.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4041, 170002, 124017, 0.16, 25230855.28809975, 10512856.37004156, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24041, 139.36694617, 0.00076748, 168.99608385, 0.02041277, 16.89960839, 0.05524107, -139.36694617, -0.00076748, -168.99608385, -0.02041277, -16.89960839, -0.05524107, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14041, 154.40801986, 0.00076748, 187.23486012, 0.02041277, 18.72348601, 0.05524107, -154.40801986, -0.00076748, -187.23486012, -0.02041277, -18.72348601, -0.05524107, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24041, 4041, 0.0, 243.15923023, 0.0153496, 243.15923023, 0.0460488, 170.21146116, -5121.4163023, 0.05, 2, 0, 70002, 24017, 2, 3)
    ops.uniaxialMaterial('LimitState', 44041, 60.78980756, 6.072e-05, 182.36942267, 0.00018215, 607.89807557, 0.00060715, -60.78980756, -6.072e-05, -182.36942267, -0.00018215, -607.89807557, -0.00060715, 0.4, 0.3, 0.003, 0.0, 0.0, 24041, 2)
    ops.limitCurve('ThreePoint', 14041, 4041, 0.0, 243.15923023, 0.0153496, 243.15923023, 0.0460488, 170.21146116, -5121.4163023, 0.05, 2, 0, 70002, 24017, 1, 3)
    ops.uniaxialMaterial('LimitState', 34041, 60.78980756, 6.072e-05, 182.36942267, 0.00018215, 607.89807557, 0.00060715, -60.78980756, -6.072e-05, -182.36942267, -0.00018215, -607.89807557, -0.00060715, 0.4, 0.3, 0.003, 0.0, 0.0, 14041, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4041, 99999, 'P', 44041, 'Vy', 34041, 'Vz', 24041, 'My', 14041, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170002, 70002, 170002, 4041, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124017, 124017, 24017, 4041, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174017, 5.05, 0.0, 1.6)
    ops.node(121002, 5.05, 0.0, 2.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4042, 174017, 121002, 0.16, 32076504.83906619, 13365210.34961091, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24042, 145.27234192, 0.00073425, 174.53904073, 0.02668009, 17.45390407, 0.08374035, -145.27234192, -0.00073425, -174.53904073, -0.02668009, -17.45390407, -0.08374035, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14042, 134.18994573, 0.00073425, 161.22397487, 0.02668009, 16.12239749, 0.08374035, -134.18994573, -0.00073425, -161.22397487, -0.02668009, -16.12239749, -0.08374035, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24042, 4042, 0.0, 316.87206298, 0.01468503, 316.87206298, 0.04405509, 221.81044408, -6534.73071892, 0.05, 2, 0, 74017, 21002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44042, 79.21801574, 6.224e-05, 237.65404723, 0.00018671, 792.18015744, 0.00062235, -79.21801574, -6.224e-05, -237.65404723, -0.00018671, -792.18015744, -0.00062235, 0.4, 0.3, 0.003, 0.0, 0.0, 24042, 2)
    ops.limitCurve('ThreePoint', 14042, 4042, 0.0, 316.87206298, 0.01468503, 316.87206298, 0.04405509, 221.81044408, -6534.73071892, 0.05, 2, 0, 74017, 21002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34042, 79.21801574, 6.224e-05, 237.65404723, 0.00018671, 792.18015744, 0.00062235, -79.21801574, -6.224e-05, -237.65404723, -0.00018671, -792.18015744, -0.00062235, 0.4, 0.3, 0.003, 0.0, 0.0, 14042, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4042, 99999, 'P', 44042, 'Vy', 34042, 'Vz', 24042, 'My', 14042, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174017, 74017, 174017, 4042, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121002, 121002, 21002, 4042, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170003, 7.95, 0.0, 0.0)
    ops.node(124018, 7.95, 0.0, 1.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4043, 170003, 124018, 0.16, 30916043.81580766, 12881684.92325319, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24043, 142.25311542, 0.0007026, 171.32615279, 0.01855436, 17.13261528, 0.06226486, -142.25311542, -0.0007026, -171.32615279, -0.01855436, -17.13261528, -0.06226486, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14043, 157.06587767, 0.0007026, 189.16627926, 0.01855436, 18.91662793, 0.06226486, -157.06587767, -0.0007026, -189.16627926, -0.01855436, -18.91662793, -0.06226486, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24043, 4043, 0.0, 282.91339485, 0.01405192, 282.91339485, 0.04215577, 198.0393764, -4456.32946942, 0.05, 2, 0, 70003, 24018, 2, 3)
    ops.uniaxialMaterial('LimitState', 44043, 70.72834871, 5.765e-05, 212.18504614, 0.00017295, 707.28348713, 0.00057651, -70.72834871, -5.765e-05, -212.18504614, -0.00017295, -707.28348713, -0.00057651, 0.4, 0.3, 0.003, 0.0, 0.0, 24043, 2)
    ops.limitCurve('ThreePoint', 14043, 4043, 0.0, 282.91339485, 0.01405192, 282.91339485, 0.04215577, 198.0393764, -4456.32946942, 0.05, 2, 0, 70003, 24018, 1, 3)
    ops.uniaxialMaterial('LimitState', 34043, 70.72834871, 5.765e-05, 212.18504614, 0.00017295, 707.28348713, 0.00057651, -70.72834871, -5.765e-05, -212.18504614, -0.00017295, -707.28348713, -0.00057651, 0.4, 0.3, 0.003, 0.0, 0.0, 14043, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4043, 99999, 'P', 44043, 'Vy', 34043, 'Vz', 24043, 'My', 14043, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170003, 70003, 170003, 4043, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124018, 124018, 24018, 4043, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174018, 7.95, 0.0, 1.6)
    ops.node(121003, 7.95, 0.0, 2.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4044, 174018, 121003, 0.16, 29033909.31000108, 12097462.21250045, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24044, 147.15655834, 0.00071534, 178.01353255, 0.02909766, 17.80135325, 0.0819895, -147.15655834, -0.00071534, -178.01353255, -0.02909766, -17.80135325, -0.0819895, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14044, 133.78289671, 0.00071534, 161.83557367, 0.02909766, 16.18355737, 0.0819895, -133.78289671, -0.00071534, -161.83557367, -0.02909766, -16.18355737, -0.0819895, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24044, 4044, 0.0, 296.48782513, 0.01430673, 296.48782513, 0.0429202, 207.54147759, -7154.43568893, 0.05, 2, 0, 74018, 21003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44044, 74.12195628, 6.433e-05, 222.36586885, 0.000193, 741.21956284, 0.00064334, -74.12195628, -6.433e-05, -222.36586885, -0.000193, -741.21956284, -0.00064334, 0.4, 0.3, 0.003, 0.0, 0.0, 24044, 2)
    ops.limitCurve('ThreePoint', 14044, 4044, 0.0, 296.48782513, 0.01430673, 296.48782513, 0.0429202, 207.54147759, -7154.43568893, 0.05, 2, 0, 74018, 21003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34044, 74.12195628, 6.433e-05, 222.36586885, 0.000193, 741.21956284, 0.00064334, -74.12195628, -6.433e-05, -222.36586885, -0.000193, -741.21956284, -0.00064334, 0.4, 0.3, 0.003, 0.0, 0.0, 14044, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4044, 99999, 'P', 44044, 'Vy', 34044, 'Vz', 24044, 'My', 14044, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174018, 74018, 174018, 4044, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121003, 121003, 21003, 4044, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171002, 5.05, 0.0, 3.075)
    ops.node(124019, 5.05, 0.0, 4.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4046, 171002, 124019, 0.16, 28033352.68480995, 11680563.61867081, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24046, 126.88003205, 0.00070546, 154.04047294, 0.02196518, 15.40404729, 0.0654822, -126.88003205, -0.00070546, -154.04047294, -0.02196518, -15.40404729, -0.0654822, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14046, 107.219842, 0.00070546, 130.17174494, 0.02196518, 13.01717449, 0.0654822, -107.219842, -0.00070546, -130.17174494, -0.02196518, -13.01717449, -0.0654822, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24046, 4046, 0.0, 254.25213756, 0.01410918, 254.25213756, 0.04232754, 177.97649629, -5351.43849485, 0.05, 2, 0, 71002, 24019, 2, 3)
    ops.uniaxialMaterial('LimitState', 44046, 63.56303439, 5.714e-05, 190.68910317, 0.00017142, 635.63034389, 0.00057139, -63.56303439, -5.714e-05, -190.68910317, -0.00017142, -635.63034389, -0.00057139, 0.4, 0.3, 0.003, 0.0, 0.0, 24046, 2)
    ops.limitCurve('ThreePoint', 14046, 4046, 0.0, 254.25213756, 0.01410918, 254.25213756, 0.04232754, 177.97649629, -5351.43849485, 0.05, 2, 0, 71002, 24019, 1, 3)
    ops.uniaxialMaterial('LimitState', 34046, 63.56303439, 5.714e-05, 190.68910317, 0.00017142, 635.63034389, 0.00057139, -63.56303439, -5.714e-05, -190.68910317, -0.00017142, -635.63034389, -0.00057139, 0.4, 0.3, 0.003, 0.0, 0.0, 14046, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4046, 99999, 'P', 44046, 'Vy', 34046, 'Vz', 24046, 'My', 14046, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171002, 71002, 171002, 4046, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124019, 124019, 24019, 4046, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174019, 5.05, 0.0, 4.4)
    ops.node(122002, 5.05, 0.0, 5.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4047, 174019, 122002, 0.16, 28825276.99785455, 12010532.0824394, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24047, 125.97740362, 0.0007074, 152.84754547, 0.01975047, 15.28475455, 0.06515385, -125.97740362, -0.0007074, -152.84754547, -0.01975047, -15.28475455, -0.06515385, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14047, 105.8702097, 0.0007074, 128.45162089, 0.01975047, 12.84516209, 0.06515385, -105.8702097, -0.0007074, -128.45162089, -0.01975047, -12.84516209, -0.06515385, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24047, 4047, 0.0, 250.46635401, 0.01414792, 250.46635401, 0.04244375, 175.32644781, -4859.78098913, 0.05, 2, 0, 74019, 22002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44047, 62.6165885, 5.474e-05, 187.84976551, 0.00016422, 626.16588503, 0.00054741, -62.6165885, -5.474e-05, -187.84976551, -0.00016422, -626.16588503, -0.00054741, 0.4, 0.3, 0.003, 0.0, 0.0, 24047, 2)
    ops.limitCurve('ThreePoint', 14047, 4047, 0.0, 250.46635401, 0.01414792, 250.46635401, 0.04244375, 175.32644781, -4859.78098913, 0.05, 2, 0, 74019, 22002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34047, 62.6165885, 5.474e-05, 187.84976551, 0.00016422, 626.16588503, 0.00054741, -62.6165885, -5.474e-05, -187.84976551, -0.00016422, -626.16588503, -0.00054741, 0.4, 0.3, 0.003, 0.0, 0.0, 14047, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4047, 99999, 'P', 44047, 'Vy', 34047, 'Vz', 24047, 'My', 14047, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174019, 74019, 174019, 4047, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122002, 122002, 22002, 4047, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171003, 7.95, 0.0, 3.075)
    ops.node(124020, 7.95, 0.0, 4.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4048, 171003, 124020, 0.16, 26061990.11829871, 10859162.54929113, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24048, 130.56758226, 0.00071981, 158.89179624, 0.0219381, 15.88917962, 0.06268621, -130.56758226, -0.00071981, -158.89179624, -0.0219381, -15.88917962, -0.06268621, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14048, 108.65100292, 0.00071981, 132.22082171, 0.0219381, 13.22208217, 0.06268621, -108.65100292, -0.00071981, -132.22082171, -0.0219381, -13.22208217, -0.06268621, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24048, 4048, 0.0, 240.27818174, 0.01439616, 240.27818174, 0.04318849, 168.19472722, -5563.79643197, 0.05, 2, 0, 71003, 24020, 2, 3)
    ops.uniaxialMaterial('LimitState', 44048, 60.06954544, 5.808e-05, 180.20863631, 0.00017425, 600.69545435, 0.00058083, -60.06954544, -5.808e-05, -180.20863631, -0.00017425, -600.69545435, -0.00058083, 0.4, 0.3, 0.003, 0.0, 0.0, 24048, 2)
    ops.limitCurve('ThreePoint', 14048, 4048, 0.0, 240.27818174, 0.01439616, 240.27818174, 0.04318849, 168.19472722, -5563.79643197, 0.05, 2, 0, 71003, 24020, 1, 3)
    ops.uniaxialMaterial('LimitState', 34048, 60.06954544, 5.808e-05, 180.20863631, 0.00017425, 600.69545435, 0.00058083, -60.06954544, -5.808e-05, -180.20863631, -0.00017425, -600.69545435, -0.00058083, 0.4, 0.3, 0.003, 0.0, 0.0, 14048, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4048, 99999, 'P', 44048, 'Vy', 34048, 'Vz', 24048, 'My', 14048, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171003, 71003, 171003, 4048, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124020, 124020, 24020, 4048, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174020, 7.95, 0.0, 4.4)
    ops.node(122003, 7.95, 0.0, 5.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4049, 174020, 122003, 0.16, 26715323.71560545, 11131384.88150227, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24049, 132.99292124, 0.00072489, 161.8919383, 0.02188165, 16.18919383, 0.06478365, -132.99292124, -0.00072489, -161.8919383, -0.02188165, -16.18919383, -0.06478365, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14049, 109.28904531, 0.00072489, 133.03727157, 0.02188165, 13.30372716, 0.06478365, -109.28904531, -0.00072489, -133.03727157, -0.02188165, -13.30372716, -0.06478365, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24049, 4049, 0.0, 240.498446, 0.01449777, 240.498446, 0.04349332, 168.3489122, -5557.49365061, 0.05, 2, 0, 74020, 22003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44049, 60.1246115, 5.671e-05, 180.3738345, 0.00017014, 601.24611501, 0.00056714, -60.1246115, -5.671e-05, -180.3738345, -0.00017014, -601.24611501, -0.00056714, 0.4, 0.3, 0.003, 0.0, 0.0, 24049, 2)
    ops.limitCurve('ThreePoint', 14049, 4049, 0.0, 240.498446, 0.01449777, 240.498446, 0.04349332, 168.3489122, -5557.49365061, 0.05, 2, 0, 74020, 22003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34049, 60.1246115, 5.671e-05, 180.3738345, 0.00017014, 601.24611501, 0.00056714, -60.1246115, -5.671e-05, -180.3738345, -0.00017014, -601.24611501, -0.00056714, 0.4, 0.3, 0.003, 0.0, 0.0, 14049, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4049, 99999, 'P', 44049, 'Vy', 34049, 'Vz', 24049, 'My', 14049, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174020, 74020, 174020, 4049, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122003, 122003, 22003, 4049, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172002, 5.05, 0.0, 5.875)
    ops.node(124021, 5.05, 0.0, 6.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4051, 172002, 124021, 0.1225, 27702802.19409181, 11542834.24753826, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24051, 83.40727694, 0.00077096, 101.45086906, 0.02089537, 10.14508691, 0.07062768, -83.40727694, -0.00077096, -101.45086906, -0.02089537, -10.14508691, -0.07062768, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14051, 72.54658698, 0.00077096, 88.24067355, 0.02089537, 8.82406736, 0.07062768, -72.54658698, -0.00077096, -88.24067355, -0.02089537, -8.82406736, -0.07062768, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24051, 4051, 0.0, 173.89922315, 0.01541918, 173.89922315, 0.04625753, 121.7294562, -4504.31017357, 0.05, 2, 0, 72002, 24021, 2, 3)
    ops.uniaxialMaterial('LimitState', 44051, 43.47480579, 5.165e-05, 130.42441736, 0.00015496, 434.74805786, 0.00051653, -43.47480579, -5.165e-05, -130.42441736, -0.00015496, -434.74805786, -0.00051653, 0.4, 0.3, 0.003, 0.0, 0.0, 24051, 2)
    ops.limitCurve('ThreePoint', 14051, 4051, 0.0, 173.89922315, 0.01541918, 173.89922315, 0.04625753, 121.7294562, -4504.31017357, 0.05, 2, 0, 72002, 24021, 1, 3)
    ops.uniaxialMaterial('LimitState', 34051, 43.47480579, 5.165e-05, 130.42441736, 0.00015496, 434.74805786, 0.00051653, -43.47480579, -5.165e-05, -130.42441736, -0.00015496, -434.74805786, -0.00051653, 0.4, 0.3, 0.003, 0.0, 0.0, 14051, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4051, 99999, 'P', 44051, 'Vy', 34051, 'Vz', 24051, 'My', 14051, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172002, 72002, 172002, 4051, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124021, 124021, 24021, 4051, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174021, 5.05, 0.0, 7.2)
    ops.node(123002, 5.05, 0.0, 8.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4052, 174021, 123002, 0.1225, 27000677.76734246, 11250282.40305936, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24052, 81.30194415, 0.0007395, 99.12281246, 0.02372804, 9.91228125, 0.07448314, -81.30194415, -0.0007395, -99.12281246, -0.02372804, -9.91228125, -0.07448314, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14052, 69.2902827, 0.0007395, 84.47827132, 0.02372804, 8.44782713, 0.07448314, -69.2902827, -0.0007395, -84.47827132, -0.02372804, -8.44782713, -0.07448314, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24052, 4052, 0.0, 169.28114319, 0.01479009, 169.28114319, 0.04437027, 118.49680024, -5151.13726428, 0.05, 2, 0, 74021, 23002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44052, 42.3202858, 5.159e-05, 126.9608574, 0.00015477, 423.20285799, 0.00051589, -42.3202858, -5.159e-05, -126.9608574, -0.00015477, -423.20285799, -0.00051589, 0.4, 0.3, 0.003, 0.0, 0.0, 24052, 2)
    ops.limitCurve('ThreePoint', 14052, 4052, 0.0, 169.28114319, 0.01479009, 169.28114319, 0.04437027, 118.49680024, -5151.13726428, 0.05, 2, 0, 74021, 23002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34052, 42.3202858, 5.159e-05, 126.9608574, 0.00015477, 423.20285799, 0.00051589, -42.3202858, -5.159e-05, -126.9608574, -0.00015477, -423.20285799, -0.00051589, 0.4, 0.3, 0.003, 0.0, 0.0, 14052, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4052, 99999, 'P', 44052, 'Vy', 34052, 'Vz', 24052, 'My', 14052, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174021, 74021, 174021, 4052, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123002, 123002, 23002, 4052, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172003, 7.95, 0.0, 5.875)
    ops.node(124022, 7.95, 0.0, 6.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4053, 172003, 124022, 0.1225, 24943545.87512372, 10393144.11463489, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24053, 86.03717214, 0.00080524, 104.97280814, 0.02479001, 10.49728081, 0.07037891, -86.03717214, -0.00080524, -104.97280814, -0.02479001, -10.49728081, -0.07037891, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14053, 73.79702402, 0.00080524, 90.03876639, 0.02479001, 9.00387664, 0.07037891, -73.79702402, -0.00080524, -90.03876639, -0.02479001, -9.00387664, -0.07037891, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24053, 4053, 0.0, 169.88049286, 0.01610485, 169.88049286, 0.04831455, 118.916345, -5659.40919451, 0.05, 2, 0, 72003, 24022, 2, 3)
    ops.uniaxialMaterial('LimitState', 44053, 42.47012321, 5.604e-05, 127.41036964, 0.00016812, 424.70123214, 0.00056042, -42.47012321, -5.604e-05, -127.41036964, -0.00016812, -424.70123214, -0.00056042, 0.4, 0.3, 0.003, 0.0, 0.0, 24053, 2)
    ops.limitCurve('ThreePoint', 14053, 4053, 0.0, 169.88049286, 0.01610485, 169.88049286, 0.04831455, 118.916345, -5659.40919451, 0.05, 2, 0, 72003, 24022, 1, 3)
    ops.uniaxialMaterial('LimitState', 34053, 42.47012321, 5.604e-05, 127.41036964, 0.00016812, 424.70123214, 0.00056042, -42.47012321, -5.604e-05, -127.41036964, -0.00016812, -424.70123214, -0.00056042, 0.4, 0.3, 0.003, 0.0, 0.0, 14053, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4053, 99999, 'P', 44053, 'Vy', 34053, 'Vz', 24053, 'My', 14053, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172003, 72003, 172003, 4053, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124022, 124022, 24022, 4053, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174022, 7.95, 0.0, 7.2)
    ops.node(123003, 7.95, 0.0, 8.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4054, 174022, 123003, 0.1225, 31353794.47060417, 13064081.02941841, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24054, 76.43317561, 0.00074369, 92.29759888, 0.02071717, 9.22975989, 0.0753456, -76.43317561, -0.00074369, -92.29759888, -0.02071717, -9.22975989, -0.0753456, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14054, 67.57650524, 0.00074369, 81.60264342, 0.02071717, 8.16026434, 0.0753456, -67.57650524, -0.00074369, -81.60264342, -0.02071717, -8.16026434, -0.0753456, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24054, 4054, 0.0, 191.39953328, 0.01487374, 191.39953328, 0.04462121, 133.9796733, -4815.02133115, 0.05, 2, 0, 74022, 23003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44054, 47.84988332, 5.023e-05, 143.54964996, 0.00015069, 478.49883321, 0.00050231, -47.84988332, -5.023e-05, -143.54964996, -0.00015069, -478.49883321, -0.00050231, 0.4, 0.3, 0.003, 0.0, 0.0, 24054, 2)
    ops.limitCurve('ThreePoint', 14054, 4054, 0.0, 191.39953328, 0.01487374, 191.39953328, 0.04462121, 133.9796733, -4815.02133115, 0.05, 2, 0, 74022, 23003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34054, 47.84988332, 5.023e-05, 143.54964996, 0.00015069, 478.49883321, 0.00050231, -47.84988332, -5.023e-05, -143.54964996, -0.00015069, -478.49883321, -0.00050231, 0.4, 0.3, 0.003, 0.0, 0.0, 14054, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4054, 99999, 'P', 44054, 'Vy', 34054, 'Vz', 24054, 'My', 14054, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174022, 74022, 174022, 4054, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123003, 123003, 23003, 4054, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173002, 5.05, 0.0, 8.675)
    ops.node(124023, 5.05, 0.0, 9.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4056, 173002, 124023, 0.1225, 27359386.6769002, 11399744.44870842, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24056, 65.66177611, 0.00075105, 80.28109015, 0.01903545, 8.02810901, 0.06684696, -65.66177611, -0.00075105, -80.28109015, -0.01903545, -8.02810901, -0.06684696, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14056, 56.58740766, 0.00075105, 69.18635232, 0.01903545, 6.91863523, 0.06684696, -56.58740766, -0.00075105, -69.18635232, -0.01903545, -6.91863523, -0.06684696, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24056, 4056, 0.0, 150.29385571, 0.01502104, 150.29385571, 0.04506311, 105.20569899, -6087.73602224, 0.05, 2, 0, 73002, 24023, 2, 3)
    ops.uniaxialMaterial('LimitState', 44056, 37.57346393, 4.52e-05, 112.72039178, 0.00013561, 375.73463927, 0.00045202, -37.57346393, -4.52e-05, -112.72039178, -0.00013561, -375.73463927, -0.00045202, 0.4, 0.3, 0.003, 0.0, 0.0, 24056, 2)
    ops.limitCurve('ThreePoint', 14056, 4056, 0.0, 150.29385571, 0.01502104, 150.29385571, 0.04506311, 105.20569899, -6087.73602224, 0.05, 2, 0, 73002, 24023, 1, 3)
    ops.uniaxialMaterial('LimitState', 34056, 37.57346393, 4.52e-05, 112.72039178, 0.00013561, 375.73463927, 0.00045202, -37.57346393, -4.52e-05, -112.72039178, -0.00013561, -375.73463927, -0.00045202, 0.4, 0.3, 0.003, 0.0, 0.0, 14056, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4056, 99999, 'P', 44056, 'Vy', 34056, 'Vz', 24056, 'My', 14056, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173002, 73002, 173002, 4056, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124023, 124023, 24023, 4056, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174023, 5.05, 0.0, 10.0)
    ops.node(124002, 5.05, 0.0, 11.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4057, 174023, 124002, 0.1225, 27619262.23555664, 11508025.93148193, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24057, 65.11434731, 0.00076195, 79.66493607, 0.01966959, 7.96649361, 0.06935834, -65.11434731, -0.00076195, -79.66493607, -0.01966959, -7.96649361, -0.06935834, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14057, 55.39164555, 0.00076195, 67.76957896, 0.01966959, 6.7769579, 0.06935834, -55.39164555, -0.00076195, -67.76957896, -0.01966959, -6.7769579, -0.06935834, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24057, 4057, 0.0, 149.42096795, 0.01523894, 149.42096795, 0.04571681, 104.59467757, -10390.25369911, 0.05, 2, 0, 74023, 24002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44057, 37.35524199, 4.452e-05, 112.06572596, 0.00013355, 373.55241988, 0.00044517, -37.35524199, -4.452e-05, -112.06572596, -0.00013355, -373.55241988, -0.00044517, 0.4, 0.3, 0.003, 0.0, 0.0, 24057, 2)
    ops.limitCurve('ThreePoint', 14057, 4057, 0.0, 149.42096795, 0.01523894, 149.42096795, 0.04571681, 104.59467757, -10390.25369911, 0.05, 2, 0, 74023, 24002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34057, 37.35524199, 4.452e-05, 112.06572596, 0.00013355, 373.55241988, 0.00044517, -37.35524199, -4.452e-05, -112.06572596, -0.00013355, -373.55241988, -0.00044517, 0.4, 0.3, 0.003, 0.0, 0.0, 14057, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4057, 99999, 'P', 44057, 'Vy', 34057, 'Vz', 24057, 'My', 14057, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174023, 74023, 174023, 4057, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124002, 124002, 24002, 4057, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173003, 7.95, 0.0, 8.675)
    ops.node(124024, 7.95, 0.0, 9.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4058, 173003, 124024, 0.1225, 26854748.06555718, 11189478.36064883, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24058, 69.39035704, 0.00074569, 84.925211, 0.01696264, 8.4925211, 0.06453567, -69.39035704, -0.00074569, -84.925211, -0.01696264, -8.4925211, -0.06453567, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14058, 58.71658252, 0.00074569, 71.8618317, 0.01696264, 7.18618317, 0.06453567, -58.71658252, -0.00074569, -71.8618317, -0.01696264, -7.18618317, -0.06453567, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24058, 4058, 0.0, 143.17821847, 0.01491387, 143.17821847, 0.04474161, 100.22475293, -5276.51873349, 0.05, 2, 0, 73003, 24024, 2, 3)
    ops.uniaxialMaterial('LimitState', 44058, 35.79455462, 4.387e-05, 107.38366385, 0.00013161, 357.94554618, 0.00043871, -35.79455462, -4.387e-05, -107.38366385, -0.00013161, -357.94554618, -0.00043871, 0.4, 0.3, 0.003, 0.0, 0.0, 24058, 2)
    ops.limitCurve('ThreePoint', 14058, 4058, 0.0, 143.17821847, 0.01491387, 143.17821847, 0.04474161, 100.22475293, -5276.51873349, 0.05, 2, 0, 73003, 24024, 1, 3)
    ops.uniaxialMaterial('LimitState', 34058, 35.79455462, 4.387e-05, 107.38366385, 0.00013161, 357.94554618, 0.00043871, -35.79455462, -4.387e-05, -107.38366385, -0.00013161, -357.94554618, -0.00043871, 0.4, 0.3, 0.003, 0.0, 0.0, 14058, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4058, 99999, 'P', 44058, 'Vy', 34058, 'Vz', 24058, 'My', 14058, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173003, 73003, 173003, 4058, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124024, 124024, 24024, 4058, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174024, 7.95, 0.0, 10.0)
    ops.node(124003, 7.95, 0.0, 11.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4059, 174024, 124003, 0.1225, 26556215.30374904, 11065089.70989543, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24059, 65.10536202, 0.00072958, 79.83600631, 0.02223781, 7.98360063, 0.07165234, -65.10536202, -0.00072958, -79.83600631, -0.02223781, -7.98360063, -0.07165234, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14059, 54.48340803, 0.00072958, 66.8107445, 0.02223781, 6.68107445, 0.07165234, -54.48340803, -0.00072958, -66.8107445, -0.02223781, -6.68107445, -0.07165234, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24059, 4059, 0.0, 149.46074122, 0.01459163, 149.46074122, 0.04377489, 104.62251886, -12489.92007662, 0.05, 2, 0, 74024, 24003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44059, 37.36518531, 4.631e-05, 112.09555592, 0.00013893, 373.65185306, 0.00046311, -37.36518531, -4.631e-05, -112.09555592, -0.00013893, -373.65185306, -0.00046311, 0.4, 0.3, 0.003, 0.0, 0.0, 24059, 2)
    ops.limitCurve('ThreePoint', 14059, 4059, 0.0, 149.46074122, 0.01459163, 149.46074122, 0.04377489, 104.62251886, -12489.92007662, 0.05, 2, 0, 74024, 24003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34059, 37.36518531, 4.631e-05, 112.09555592, 0.00013893, 373.65185306, 0.00046311, -37.36518531, -4.631e-05, -112.09555592, -0.00013893, -373.65185306, -0.00046311, 0.4, 0.3, 0.003, 0.0, 0.0, 14059, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4059, 99999, 'P', 44059, 'Vy', 34059, 'Vz', 24059, 'My', 14059, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174024, 74024, 174024, 4059, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124003, 124003, 24003, 4059, '-orient', 0, 0, 1, 0, 1, 0)
