import openseespy.opensees as ops


def add_columns() -> None:
    """Add components of all columns to ops domain (plastic hinges, column elements and nodes)
    """
    # Create elastic column element nodes
    ops.node(170001, 0.0, 0.0, 0.0)
    ops.node(121001, 0.0, 0.0, 2.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1, 170001, 121001, 0.09, 27740401.98307873, 11558500.8262828, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20001, 61.81531351, 0.00117405, 74.77598183, 0.01558229, 7.47759818, 0.05572128, -61.81531351, -0.00117405, -74.77598183, -0.01558229, -7.47759818, -0.05572128, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10001, 57.39188177, 0.00117405, 69.42509978, 0.01558229, 6.94250998, 0.05572128, -57.39188177, -0.00117405, -69.42509978, -0.01558229, -6.94250998, -0.05572128, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20001, 1, 0.0, 98.70816638, 0.02348095, 98.70816638, 0.07044286, 69.09571647, -1210.96448272, 0.05, 2, 0, 70001, 21001, 2, 3)
    ops.uniaxialMaterial('LimitState', 40001, 24.6770416, 8.682e-05, 74.03112479, 0.00026047, 246.77041596, 0.00086822, -24.6770416, -8.682e-05, -74.03112479, -0.00026047, -246.77041596, -0.00086822, 0.4, 0.3, 0.003, 0.0, 0.0, 20001, 2)
    ops.limitCurve('ThreePoint', 10001, 1, 0.0, 98.70816638, 0.02348095, 98.70816638, 0.07044286, 69.09571647, -1210.96448272, 0.05, 2, 0, 70001, 21001, 1, 3)
    ops.uniaxialMaterial('LimitState', 30001, 24.6770416, 8.682e-05, 74.03112479, 0.00026047, 246.77041596, 0.00086822, -24.6770416, -8.682e-05, -74.03112479, -0.00026047, -246.77041596, -0.00086822, 0.4, 0.3, 0.003, 0.0, 0.0, 10001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1, 99999, 'P', 40001, 'Vy', 30001, 'Vz', 20001, 'My', 10001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170001, 70001, 170001, 1, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121001, 121001, 21001, 1, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170002, 3.9, 0.0, 0.0)
    ops.node(121002, 3.9, 0.0, 2.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2, 170002, 121002, 0.1225, 31407283.37034314, 13086368.07097631, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20002, 97.4215177, 0.00098869, 116.86561803, 0.02121249, 11.6865618, 0.06628743, -97.4215177, -0.00098869, -116.86561803, -0.02121249, -11.6865618, -0.06628743, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10002, 108.7710013, 0.00098869, 130.48031473, 0.02121249, 13.04803147, 0.06628743, -108.7710013, -0.00098869, -130.48031473, -0.02121249, -13.04803147, -0.06628743, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20002, 2, 0.0, 167.02225666, 0.01977374, 167.02225666, 0.05932121, 116.91557966, -2066.07586778, 0.05, 2, 0, 70002, 21002, 2, 3)
    ops.uniaxialMaterial('LimitState', 40002, 41.75556416, 9.533e-05, 125.26669249, 0.000286, 417.55564165, 0.00095332, -41.75556416, -9.533e-05, -125.26669249, -0.000286, -417.55564165, -0.00095332, 0.4, 0.3, 0.003, 0.0, 0.0, 20002, 2)
    ops.limitCurve('ThreePoint', 10002, 2, 0.0, 167.02225666, 0.01977374, 167.02225666, 0.05932121, 116.91557966, -2066.07586778, 0.05, 2, 0, 70002, 21002, 1, 3)
    ops.uniaxialMaterial('LimitState', 30002, 41.75556416, 9.533e-05, 125.26669249, 0.000286, 417.55564165, 0.00095332, -41.75556416, -9.533e-05, -125.26669249, -0.000286, -417.55564165, -0.00095332, 0.4, 0.3, 0.003, 0.0, 0.0, 10002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2, 99999, 'P', 40002, 'Vy', 30002, 'Vz', 20002, 'My', 10002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170002, 70002, 170002, 2, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121002, 121002, 21002, 2, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170005, 14.7, 0.0, 0.0)
    ops.node(121005, 14.7, 0.0, 2.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 5, 170005, 121005, 0.1225, 30869879.35122587, 12862449.72967745, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20005, 98.96729967, 0.0009785, 118.85287213, 0.0215396, 11.88528721, 0.06580486, -98.96729967, -0.0009785, -118.85287213, -0.0215396, -11.88528721, -0.06580486, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10005, 111.6048694, 0.0009785, 134.02971805, 0.0215396, 13.4029718, 0.06580486, -111.6048694, -0.0009785, -134.02971805, -0.0215396, -13.4029718, -0.06580486, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20005, 5, 0.0, 163.88253411, 0.01956991, 163.88253411, 0.05870974, 114.71777388, -2034.98973292, 0.05, 2, 0, 70005, 21005, 2, 3)
    ops.uniaxialMaterial('LimitState', 40005, 40.97063353, 9.517e-05, 122.91190058, 0.00028551, 409.70633528, 0.00095169, -40.97063353, -9.517e-05, -122.91190058, -0.00028551, -409.70633528, -0.00095169, 0.4, 0.3, 0.003, 0.0, 0.0, 20005, 2)
    ops.limitCurve('ThreePoint', 10005, 5, 0.0, 163.88253411, 0.01956991, 163.88253411, 0.05870974, 114.71777388, -2034.98973292, 0.05, 2, 0, 70005, 21005, 1, 3)
    ops.uniaxialMaterial('LimitState', 30005, 40.97063353, 9.517e-05, 122.91190058, 0.00028551, 409.70633528, 0.00095169, -40.97063353, -9.517e-05, -122.91190058, -0.00028551, -409.70633528, -0.00095169, 0.4, 0.3, 0.003, 0.0, 0.0, 10005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 5, 99999, 'P', 40005, 'Vy', 30005, 'Vz', 20005, 'My', 10005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170005, 70005, 170005, 5, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121005, 121005, 21005, 5, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170006, 18.6, 0.0, 0.0)
    ops.node(121006, 18.6, 0.0, 2.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 6, 170006, 121006, 0.09, 30799367.16867132, 12833069.65361305, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20006, 66.97834868, 0.00110766, 80.6271195, 0.01667434, 8.06271195, 0.06141624, -66.97834868, -0.00110766, -80.6271195, -0.01667434, -8.06271195, -0.06141624, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10006, 61.42754609, 0.00110766, 73.94518075, 0.01667434, 7.39451807, 0.06141624, -61.42754609, -0.00110766, -73.94518075, -0.01667434, -7.39451807, -0.06141624, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20006, 6, 0.0, 111.23318403, 0.02215314, 111.23318403, 0.06645941, 77.86322882, -1339.81811864, 0.05, 2, 0, 70006, 21006, 2, 3)
    ops.uniaxialMaterial('LimitState', 40006, 27.80829601, 8.812e-05, 83.42488802, 0.00026436, 278.08296008, 0.00088122, -27.80829601, -8.812e-05, -83.42488802, -0.00026436, -278.08296008, -0.00088122, 0.4, 0.3, 0.003, 0.0, 0.0, 20006, 2)
    ops.limitCurve('ThreePoint', 10006, 6, 0.0, 111.23318403, 0.02215314, 111.23318403, 0.06645941, 77.86322882, -1339.81811864, 0.05, 2, 0, 70006, 21006, 1, 3)
    ops.uniaxialMaterial('LimitState', 30006, 27.80829601, 8.812e-05, 83.42488802, 0.00026436, 278.08296008, 0.00088122, -27.80829601, -8.812e-05, -83.42488802, -0.00026436, -278.08296008, -0.00088122, 0.4, 0.3, 0.003, 0.0, 0.0, 10006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 6, 99999, 'P', 40006, 'Vy', 30006, 'Vz', 20006, 'My', 10006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170006, 70006, 170006, 6, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121006, 121006, 21006, 6, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170007, 0.0, 5.35, 0.0)
    ops.node(121007, 0.0, 5.35, 2.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 7, 170007, 121007, 0.1225, 30362611.69571528, 12651088.20654804, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20007, 106.34175018, 0.0010348, 127.75486516, 0.01895669, 12.77548652, 0.06165521, -106.34175018, -0.0010348, -127.75486516, -0.01895669, -12.77548652, -0.06165521, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10007, 106.34175018, 0.0010348, 127.75486516, 0.01895669, 12.77548652, 0.06165521, -106.34175018, -0.0010348, -127.75486516, -0.01895669, -12.77548652, -0.06165521, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20007, 7, 0.0, 157.52390424, 0.02069606, 157.52390424, 0.06208819, 110.26673297, -1875.00266927, 0.05, 2, 0, 70007, 21007, 2, 3)
    ops.uniaxialMaterial('LimitState', 40007, 39.38097606, 9.3e-05, 118.14292818, 0.00027901, 393.8097606, 0.00093004, -39.38097606, -9.3e-05, -118.14292818, -0.00027901, -393.8097606, -0.00093004, 0.4, 0.3, 0.003, 0.0, 0.0, 20007, 2)
    ops.limitCurve('ThreePoint', 10007, 7, 0.0, 157.52390424, 0.02069606, 157.52390424, 0.06208819, 110.26673297, -1875.00266927, 0.05, 2, 0, 70007, 21007, 1, 3)
    ops.uniaxialMaterial('LimitState', 30007, 39.38097606, 9.3e-05, 118.14292818, 0.00027901, 393.8097606, 0.00093004, -39.38097606, -9.3e-05, -118.14292818, -0.00027901, -393.8097606, -0.00093004, 0.4, 0.3, 0.003, 0.0, 0.0, 10007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 7, 99999, 'P', 40007, 'Vy', 30007, 'Vz', 20007, 'My', 10007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170007, 70007, 170007, 7, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121007, 121007, 21007, 7, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170008, 3.9, 5.35, 0.0)
    ops.node(121008, 3.9, 5.35, 2.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 8, 170008, 121008, 0.16, 29667241.18818079, 12361350.49507533, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20008, 218.45997549, 0.00096525, 262.34509852, 0.02489387, 26.23450985, 0.06974592, -218.45997549, -0.00096525, -262.34509852, -0.02489387, -26.23450985, -0.06974592, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10008, 226.81192657, 0.00096525, 272.3748233, 0.02489387, 27.23748233, 0.06974592, -226.81192657, -0.00096525, -272.3748233, -0.02489387, -27.23748233, -0.06974592, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20008, 8, 0.0, 214.592305, 0.01930495, 214.592305, 0.05791486, 150.2146135, -2716.88391499, 0.05, 2, 0, 70008, 21008, 2, 3)
    ops.uniaxialMaterial('LimitState', 40008, 53.64807625, 9.928e-05, 160.94422875, 0.00029783, 536.48076251, 0.00099277, -53.64807625, -9.928e-05, -160.94422875, -0.00029783, -536.48076251, -0.00099277, 0.4, 0.3, 0.003, 0.0, 0.0, 20008, 2)
    ops.limitCurve('ThreePoint', 10008, 8, 0.0, 214.592305, 0.01930495, 214.592305, 0.05791486, 150.2146135, -2716.88391499, 0.05, 2, 0, 70008, 21008, 1, 3)
    ops.uniaxialMaterial('LimitState', 30008, 53.64807625, 9.928e-05, 160.94422875, 0.00029783, 536.48076251, 0.00099277, -53.64807625, -9.928e-05, -160.94422875, -0.00029783, -536.48076251, -0.00099277, 0.4, 0.3, 0.003, 0.0, 0.0, 10008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 8, 99999, 'P', 40008, 'Vy', 30008, 'Vz', 20008, 'My', 10008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170008, 70008, 170008, 8, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121008, 121008, 21008, 8, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170009, 7.8, 5.35, 0.0)
    ops.node(121009, 7.8, 5.35, 2.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 9, 170009, 121009, 0.16, 31745954.51912984, 13227481.04963744, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20009, 208.98520081, 0.00092684, 250.32509121, 0.0267451, 25.03250912, 0.07714135, -208.98520081, -0.00092684, -250.32509121, -0.0267451, -25.03250912, -0.07714135, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10009, 216.78668462, 0.00092684, 259.66980624, 0.0267451, 25.96698062, 0.07714135, -216.78668462, -0.00092684, -259.66980624, -0.0267451, -25.96698062, -0.07714135, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20009, 9, 0.0, 230.29807232, 0.01853674, 230.29807232, 0.05561023, 161.20865062, -2944.30573223, 0.05, 2, 0, 70009, 21009, 2, 3)
    ops.uniaxialMaterial('LimitState', 40009, 57.57451808, 9.957e-05, 172.72355424, 0.0002987, 575.7451808, 0.00099567, -57.57451808, -9.957e-05, -172.72355424, -0.0002987, -575.7451808, -0.00099567, 0.4, 0.3, 0.003, 0.0, 0.0, 20009, 2)
    ops.limitCurve('ThreePoint', 10009, 9, 0.0, 230.29807232, 0.01853674, 230.29807232, 0.05561023, 161.20865062, -2944.30573223, 0.05, 2, 0, 70009, 21009, 1, 3)
    ops.uniaxialMaterial('LimitState', 30009, 57.57451808, 9.957e-05, 172.72355424, 0.0002987, 575.7451808, 0.00099567, -57.57451808, -9.957e-05, -172.72355424, -0.0002987, -575.7451808, -0.00099567, 0.4, 0.3, 0.003, 0.0, 0.0, 10009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 9, 99999, 'P', 40009, 'Vy', 30009, 'Vz', 20009, 'My', 10009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170009, 70009, 170009, 9, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121009, 121009, 21009, 9, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170010, 10.8, 5.35, 0.0)
    ops.node(121010, 10.8, 5.35, 2.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 10, 170010, 121010, 0.16, 30205609.85479016, 12585670.77282923, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20010, 199.53888468, 0.00099622, 239.72260079, 0.0284735, 23.97226008, 0.07607216, -199.53888468, -0.00099622, -239.72260079, -0.0284735, -23.97226008, -0.07607216, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10010, 205.89283956, 0.00099622, 247.35613342, 0.0284735, 24.73561334, 0.07607216, -205.89283956, -0.00099622, -247.35613342, -0.0284735, -24.73561334, -0.07607216, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20010, 10, 0.0, 230.72457513, 0.01992444, 230.72457513, 0.05977333, 161.50720259, -3206.27072192, 0.05, 2, 0, 70010, 21010, 2, 3)
    ops.uniaxialMaterial('LimitState', 40010, 57.68114378, 0.00010484, 173.04343135, 0.00031451, 576.81143783, 0.00104838, -57.68114378, -0.00010484, -173.04343135, -0.00031451, -576.81143783, -0.00104838, 0.4, 0.3, 0.003, 0.0, 0.0, 20010, 2)
    ops.limitCurve('ThreePoint', 10010, 10, 0.0, 230.72457513, 0.01992444, 230.72457513, 0.05977333, 161.50720259, -3206.27072192, 0.05, 2, 0, 70010, 21010, 1, 3)
    ops.uniaxialMaterial('LimitState', 30010, 57.68114378, 0.00010484, 173.04343135, 0.00031451, 576.81143783, 0.00104838, -57.68114378, -0.00010484, -173.04343135, -0.00031451, -576.81143783, -0.00104838, 0.4, 0.3, 0.003, 0.0, 0.0, 10010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 10, 99999, 'P', 40010, 'Vy', 30010, 'Vz', 20010, 'My', 10010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170010, 70010, 170010, 10, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121010, 121010, 21010, 10, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170011, 14.7, 5.35, 0.0)
    ops.node(121011, 14.7, 5.35, 2.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 11, 170011, 121011, 0.16, 30030246.22341901, 12512602.59309125, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20011, 207.04821372, 0.0009926, 248.52166047, 0.02576768, 24.85216605, 0.07139842, -207.04821372, -0.0009926, -248.52166047, -0.02576768, -24.85216605, -0.07139842, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10011, 213.75237785, 0.0009926, 256.56872338, 0.02576768, 25.65687234, 0.07139842, -213.75237785, -0.0009926, -256.56872338, -0.02576768, -25.65687234, -0.07139842, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20011, 11, 0.0, 218.66138142, 0.01985195, 218.66138142, 0.05955586, 153.06296699, -2779.69777914, 0.05, 2, 0, 70011, 21011, 2, 3)
    ops.uniaxialMaterial('LimitState', 40011, 54.66534535, 9.994e-05, 163.99603606, 0.00029981, 546.65345354, 0.00099937, -54.66534535, -9.994e-05, -163.99603606, -0.00029981, -546.65345354, -0.00099937, 0.4, 0.3, 0.003, 0.0, 0.0, 20011, 2)
    ops.limitCurve('ThreePoint', 10011, 11, 0.0, 218.66138142, 0.01985195, 218.66138142, 0.05955586, 153.06296699, -2779.69777914, 0.05, 2, 0, 70011, 21011, 1, 3)
    ops.uniaxialMaterial('LimitState', 30011, 54.66534535, 9.994e-05, 163.99603606, 0.00029981, 546.65345354, 0.00099937, -54.66534535, -9.994e-05, -163.99603606, -0.00029981, -546.65345354, -0.00099937, 0.4, 0.3, 0.003, 0.0, 0.0, 10011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 11, 99999, 'P', 40011, 'Vy', 30011, 'Vz', 20011, 'My', 10011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170011, 70011, 170011, 11, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121011, 121011, 21011, 11, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170012, 18.6, 5.35, 0.0)
    ops.node(121012, 18.6, 5.35, 2.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 12, 170012, 121012, 0.1225, 31755276.53861723, 13231365.22442385, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20012, 104.44624915, 0.00101629, 125.13027236, 0.01904003, 12.51302724, 0.06392881, -104.44624915, -0.00101629, -125.13027236, -0.01904003, -12.51302724, -0.06392881, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10012, 104.44624915, 0.00101629, 125.13027236, 0.01904003, 12.51302724, 0.06392881, -104.44624915, -0.00101629, -125.13027236, -0.01904003, -12.51302724, -0.06392881, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20012, 12, 0.0, 160.53537573, 0.02032586, 160.53537573, 0.06097758, 112.37476301, -1805.61819763, 0.05, 2, 0, 70012, 21012, 2, 3)
    ops.uniaxialMaterial('LimitState', 40012, 40.13384393, 9.063e-05, 120.4015318, 0.00027188, 401.33843932, 0.00090626, -40.13384393, -9.063e-05, -120.4015318, -0.00027188, -401.33843932, -0.00090626, 0.4, 0.3, 0.003, 0.0, 0.0, 20012, 2)
    ops.limitCurve('ThreePoint', 10012, 12, 0.0, 160.53537573, 0.02032586, 160.53537573, 0.06097758, 112.37476301, -1805.61819763, 0.05, 2, 0, 70012, 21012, 1, 3)
    ops.uniaxialMaterial('LimitState', 30012, 40.13384393, 9.063e-05, 120.4015318, 0.00027188, 401.33843932, 0.00090626, -40.13384393, -9.063e-05, -120.4015318, -0.00027188, -401.33843932, -0.00090626, 0.4, 0.3, 0.003, 0.0, 0.0, 10012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 12, 99999, 'P', 40012, 'Vy', 30012, 'Vz', 20012, 'My', 10012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170012, 70012, 170012, 12, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121012, 121012, 21012, 12, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170013, 0.0, 10.7, 0.0)
    ops.node(121013, 0.0, 10.7, 2.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 13, 170013, 121013, 0.09, 31310018.02162411, 13045840.84234338, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20013, 60.67589534, 0.00105984, 72.95528535, 0.01760314, 7.29552854, 0.06297037, -60.67589534, -0.00105984, -72.95528535, -0.01760314, -7.29552854, -0.06297037, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10013, 56.41326377, 0.00105984, 67.82999629, 0.01760314, 6.78299963, 0.06297037, -56.41326377, -0.00105984, -67.82999629, -0.01760314, -6.78299963, -0.06297037, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20013, 13, 0.0, 113.1004257, 0.02119683, 113.1004257, 0.06359049, 79.17029799, -1353.26643408, 0.05, 2, 0, 70013, 21013, 2, 3)
    ops.uniaxialMaterial('LimitState', 40013, 28.27510642, 8.814e-05, 84.82531927, 0.00026442, 282.75106424, 0.0008814, -28.27510642, -8.814e-05, -84.82531927, -0.00026442, -282.75106424, -0.0008814, 0.4, 0.3, 0.003, 0.0, 0.0, 20013, 2)
    ops.limitCurve('ThreePoint', 10013, 13, 0.0, 113.1004257, 0.02119683, 113.1004257, 0.06359049, 79.17029799, -1353.26643408, 0.05, 2, 0, 70013, 21013, 1, 3)
    ops.uniaxialMaterial('LimitState', 30013, 28.27510642, 8.814e-05, 84.82531927, 0.00026442, 282.75106424, 0.0008814, -28.27510642, -8.814e-05, -84.82531927, -0.00026442, -282.75106424, -0.0008814, 0.4, 0.3, 0.003, 0.0, 0.0, 10013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 13, 99999, 'P', 40013, 'Vy', 30013, 'Vz', 20013, 'My', 10013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170013, 70013, 170013, 13, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121013, 121013, 21013, 13, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170014, 3.9, 10.7, 0.0)
    ops.node(121014, 3.9, 10.7, 2.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 14, 170014, 121014, 0.1225, 29173225.20600023, 12155510.50250009, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20014, 112.0930814, 0.00103066, 134.98732148, 0.02027086, 13.49873215, 0.061658, -112.0930814, -0.00103066, -134.98732148, -0.02027086, -13.49873215, -0.061658, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10014, 118.19051029, 0.00103066, 142.33010823, 0.02027086, 14.23301082, 0.061658, -118.19051029, -0.00103066, -142.33010823, -0.02027086, -14.23301082, -0.061658, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20014, 14, 0.0, 155.18301875, 0.02061316, 155.18301875, 0.06183948, 108.62811313, -1970.54168904, 0.05, 2, 0, 70014, 21014, 2, 3)
    ops.uniaxialMaterial('LimitState', 40014, 38.79575469, 9.536e-05, 116.38726406, 0.00028607, 387.95754688, 0.00095358, -38.79575469, -9.536e-05, -116.38726406, -0.00028607, -387.95754688, -0.00095358, 0.4, 0.3, 0.003, 0.0, 0.0, 20014, 2)
    ops.limitCurve('ThreePoint', 10014, 14, 0.0, 155.18301875, 0.02061316, 155.18301875, 0.06183948, 108.62811313, -1970.54168904, 0.05, 2, 0, 70014, 21014, 1, 3)
    ops.uniaxialMaterial('LimitState', 30014, 38.79575469, 9.536e-05, 116.38726406, 0.00028607, 387.95754688, 0.00095358, -38.79575469, -9.536e-05, -116.38726406, -0.00028607, -387.95754688, -0.00095358, 0.4, 0.3, 0.003, 0.0, 0.0, 10014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 14, 99999, 'P', 40014, 'Vy', 30014, 'Vz', 20014, 'My', 10014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170014, 70014, 170014, 14, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121014, 121014, 21014, 14, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170015, 7.8, 10.7, 0.0)
    ops.node(121015, 7.8, 10.7, 2.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 15, 170015, 121015, 0.1225, 31236704.02526855, 13015293.3438619, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20015, 99.64607061, 0.00099175, 119.72360906, 0.01956969, 11.97236091, 0.06604698, -99.64607061, -0.00099175, -119.72360906, -0.01956969, -11.97236091, -0.06604698, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10015, 99.64607061, 0.00099175, 119.72360906, 0.01956969, 11.97236091, 0.06604698, -99.64607061, -0.00099175, -119.72360906, -0.01956969, -11.97236091, -0.06604698, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20015, 15, 0.0, 152.959763, 0.01983495, 152.959763, 0.05950484, 107.0718341, -1748.11825387, 0.05, 2, 0, 70015, 21015, 2, 3)
    ops.uniaxialMaterial('LimitState', 40015, 38.23994075, 8.778e-05, 114.71982225, 0.00026335, 382.3994075, 0.00087783, -38.23994075, -8.778e-05, -114.71982225, -0.00026335, -382.3994075, -0.00087783, 0.4, 0.3, 0.003, 0.0, 0.0, 20015, 2)
    ops.limitCurve('ThreePoint', 10015, 15, 0.0, 152.959763, 0.01983495, 152.959763, 0.05950484, 107.0718341, -1748.11825387, 0.05, 2, 0, 70015, 21015, 1, 3)
    ops.uniaxialMaterial('LimitState', 30015, 38.23994075, 8.778e-05, 114.71982225, 0.00026335, 382.3994075, 0.00087783, -38.23994075, -8.778e-05, -114.71982225, -0.00026335, -382.3994075, -0.00087783, 0.4, 0.3, 0.003, 0.0, 0.0, 10015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 15, 99999, 'P', 40015, 'Vy', 30015, 'Vz', 20015, 'My', 10015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170015, 70015, 170015, 15, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121015, 121015, 21015, 15, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170016, 10.8, 10.7, 0.0)
    ops.node(121016, 10.8, 10.7, 2.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 16, 170016, 121016, 0.1225, 29536797.98176469, 12306999.15906862, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20016, 101.07348983, 0.00102905, 121.83615278, 0.02027018, 12.18361528, 0.06419499, -101.07348983, -0.00102905, -121.83615278, -0.02027018, -12.18361528, -0.06419499, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10016, 101.07348983, 0.00102905, 121.83615278, 0.02027018, 12.18361528, 0.06419499, -101.07348983, -0.00102905, -121.83615278, -0.02027018, -12.18361528, -0.06419499, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20016, 16, 0.0, 150.22303857, 0.020581, 150.22303857, 0.061743, 105.156127, -1862.7551122, 0.05, 2, 0, 70016, 21016, 2, 3)
    ops.uniaxialMaterial('LimitState', 40016, 37.55575964, 9.117e-05, 112.66727893, 0.00027352, 375.55759643, 0.00091174, -37.55575964, -9.117e-05, -112.66727893, -0.00027352, -375.55759643, -0.00091174, 0.4, 0.3, 0.003, 0.0, 0.0, 20016, 2)
    ops.limitCurve('ThreePoint', 10016, 16, 0.0, 150.22303857, 0.020581, 150.22303857, 0.061743, 105.156127, -1862.7551122, 0.05, 2, 0, 70016, 21016, 1, 3)
    ops.uniaxialMaterial('LimitState', 30016, 37.55575964, 9.117e-05, 112.66727893, 0.00027352, 375.55759643, 0.00091174, -37.55575964, -9.117e-05, -112.66727893, -0.00027352, -375.55759643, -0.00091174, 0.4, 0.3, 0.003, 0.0, 0.0, 10016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 16, 99999, 'P', 40016, 'Vy', 30016, 'Vz', 20016, 'My', 10016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170016, 70016, 170016, 16, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121016, 121016, 21016, 16, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170017, 14.7, 10.7, 0.0)
    ops.node(121017, 14.7, 10.7, 2.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 17, 170017, 121017, 0.1225, 32686810.6782801, 13619504.44928337, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20017, 111.97618737, 0.00105277, 133.90689239, 0.02026766, 13.39068924, 0.06709537, -111.97618737, -0.00105277, -133.90689239, -0.02026766, -13.39068924, -0.06709537, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10017, 117.14517345, 0.00105277, 140.08823219, 0.02026766, 14.00882322, 0.06709537, -117.14517345, -0.00105277, -140.08823219, -0.02026766, -14.00882322, -0.06709537, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20017, 17, 0.0, 167.42764093, 0.02105532, 167.42764093, 0.06316596, 117.19934865, -1925.66164985, 0.05, 2, 0, 70017, 21017, 2, 3)
    ops.uniaxialMaterial('LimitState', 40017, 41.85691023, 9.182e-05, 125.5707307, 0.00027547, 418.56910233, 0.00091823, -41.85691023, -9.182e-05, -125.5707307, -0.00027547, -418.56910233, -0.00091823, 0.4, 0.3, 0.003, 0.0, 0.0, 20017, 2)
    ops.limitCurve('ThreePoint', 10017, 17, 0.0, 167.42764093, 0.02105532, 167.42764093, 0.06316596, 117.19934865, -1925.66164985, 0.05, 2, 0, 70017, 21017, 1, 3)
    ops.uniaxialMaterial('LimitState', 30017, 41.85691023, 9.182e-05, 125.5707307, 0.00027547, 418.56910233, 0.00091823, -41.85691023, -9.182e-05, -125.5707307, -0.00027547, -418.56910233, -0.00091823, 0.4, 0.3, 0.003, 0.0, 0.0, 10017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 17, 99999, 'P', 40017, 'Vy', 30017, 'Vz', 20017, 'My', 10017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170017, 70017, 170017, 17, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121017, 121017, 21017, 17, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170018, 18.6, 10.7, 0.0)
    ops.node(121018, 18.6, 10.7, 2.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 18, 170018, 121018, 0.09, 33207291.86222024, 13836371.60925843, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20018, 63.64422272, 0.0011468, 76.1309731, 0.01732033, 7.61309731, 0.06472196, -63.64422272, -0.0011468, -76.1309731, -0.01732033, -7.61309731, -0.06472196, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10018, 59.35158577, 0.0011468, 70.99613738, 0.01732033, 7.09961374, 0.06472196, -59.35158577, -0.0011468, -70.99613738, -0.01732033, -7.09961374, -0.06472196, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20018, 18, 0.0, 120.27703856, 0.02293604, 120.27703856, 0.06880811, 84.19392699, -1407.84618028, 0.05, 2, 0, 70018, 21018, 2, 3)
    ops.uniaxialMaterial('LimitState', 40018, 30.06925964, 8.838e-05, 90.20777892, 0.00026513, 300.69259639, 0.00088377, -30.06925964, -8.838e-05, -90.20777892, -0.00026513, -300.69259639, -0.00088377, 0.4, 0.3, 0.003, 0.0, 0.0, 20018, 2)
    ops.limitCurve('ThreePoint', 10018, 18, 0.0, 120.27703856, 0.02293604, 120.27703856, 0.06880811, 84.19392699, -1407.84618028, 0.05, 2, 0, 70018, 21018, 1, 3)
    ops.uniaxialMaterial('LimitState', 30018, 30.06925964, 8.838e-05, 90.20777892, 0.00026513, 300.69259639, 0.00088377, -30.06925964, -8.838e-05, -90.20777892, -0.00026513, -300.69259639, -0.00088377, 0.4, 0.3, 0.003, 0.0, 0.0, 10018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 18, 99999, 'P', 40018, 'Vy', 30018, 'Vz', 20018, 'My', 10018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170018, 70018, 170018, 18, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121018, 121018, 21018, 18, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171001, 0.0, 0.0, 3.3)
    ops.node(122001, 0.0, 0.0, 5.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1001, 171001, 122001, 0.09, 31145958.86428956, 12977482.86012065, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21001, 55.30578633, 0.00122689, 66.68158926, 0.01722249, 6.66815893, 0.06569393, -55.30578633, -0.00122689, -66.68158926, -0.01722249, -6.66815893, -0.06569393, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11001, 51.80807672, 0.00122689, 62.46443855, 0.01722249, 6.24644386, 0.06569393, -51.80807672, -0.00122689, -62.46443855, -0.01722249, -6.24644386, -0.06569393, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21001, 1001, 0.0, 108.30249772, 0.02453771, 108.30249772, 0.07361313, 75.8117484, -1418.71356181, 0.05, 2, 0, 71001, 22001, 2, 3)
    ops.uniaxialMaterial('LimitState', 41001, 27.07562443, 8.485e-05, 81.22687329, 0.00025454, 270.75624429, 0.00084845, -27.07562443, -8.485e-05, -81.22687329, -0.00025454, -270.75624429, -0.00084845, 0.4, 0.3, 0.003, 0.0, 0.0, 21001, 2)
    ops.limitCurve('ThreePoint', 11001, 1001, 0.0, 108.30249772, 0.02453771, 108.30249772, 0.07361313, 75.8117484, -1418.71356181, 0.05, 2, 0, 71001, 22001, 1, 3)
    ops.uniaxialMaterial('LimitState', 31001, 27.07562443, 8.485e-05, 81.22687329, 0.00025454, 270.75624429, 0.00084845, -27.07562443, -8.485e-05, -81.22687329, -0.00025454, -270.75624429, -0.00084845, 0.4, 0.3, 0.003, 0.0, 0.0, 11001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1001, 99999, 'P', 41001, 'Vy', 31001, 'Vz', 21001, 'My', 11001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171001, 71001, 171001, 1001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122001, 122001, 22001, 1001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171002, 3.9, 0.0, 3.3)
    ops.node(122002, 3.9, 0.0, 5.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1002, 171002, 122002, 0.1225, 33143914.22527458, 13809964.26053108, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21002, 88.91516788, 0.00097915, 106.44791808, 0.02977778, 10.64479181, 0.09390496, -88.91516788, -0.00097915, -106.44791808, -0.02977778, -10.64479181, -0.09390496, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11002, 101.12533891, 0.00097915, 121.06575345, 0.02977778, 12.10657535, 0.09390496, -101.12533891, -0.00097915, -121.06575345, -0.02977778, -12.10657535, -0.09390496, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21002, 1002, 0.0, 193.68558328, 0.01958306, 193.68558328, 0.05874919, 135.5799083, -3208.82511399, 0.05, 2, 0, 71002, 22002, 2, 3)
    ops.uniaxialMaterial('LimitState', 41002, 48.42139582, 0.00010476, 145.26418746, 0.00031428, 484.2139582, 0.00104759, -48.42139582, -0.00010476, -145.26418746, -0.00031428, -484.2139582, -0.00104759, 0.4, 0.3, 0.003, 0.0, 0.0, 21002, 2)
    ops.limitCurve('ThreePoint', 11002, 1002, 0.0, 193.68558328, 0.01958306, 193.68558328, 0.05874919, 135.5799083, -3208.82511399, 0.05, 2, 0, 71002, 22002, 1, 3)
    ops.uniaxialMaterial('LimitState', 31002, 48.42139582, 0.00010476, 145.26418746, 0.00031428, 484.2139582, 0.00104759, -48.42139582, -0.00010476, -145.26418746, -0.00031428, -484.2139582, -0.00104759, 0.4, 0.3, 0.003, 0.0, 0.0, 11002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1002, 99999, 'P', 41002, 'Vy', 31002, 'Vz', 21002, 'My', 11002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171002, 71002, 171002, 1002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122002, 122002, 22002, 1002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171005, 14.7, 0.0, 3.3)
    ops.node(122005, 14.7, 0.0, 5.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1005, 171005, 122005, 0.1225, 28648574.50466887, 11936906.04361203, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21005, 86.51482809, 0.00103185, 104.65148517, 0.0315614, 10.46514852, 0.088685, -86.51482809, -0.00103185, -104.65148517, -0.0315614, -10.46514852, -0.088685, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11005, 98.25152622, 0.00103185, 118.84862244, 0.0315614, 11.88486224, 0.088685, -98.25152622, -0.00103185, -118.84862244, -0.0315614, -11.88486224, -0.088685, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21005, 1005, 0.0, 179.60074691, 0.02063692, 179.60074691, 0.06191076, 125.72052284, -3348.84768653, 0.05, 2, 0, 71005, 22005, 2, 3)
    ops.uniaxialMaterial('LimitState', 41005, 44.90018673, 0.00011238, 134.70056018, 0.00033715, 449.00186728, 0.00112383, -44.90018673, -0.00011238, -134.70056018, -0.00033715, -449.00186728, -0.00112383, 0.4, 0.3, 0.003, 0.0, 0.0, 21005, 2)
    ops.limitCurve('ThreePoint', 11005, 1005, 0.0, 179.60074691, 0.02063692, 179.60074691, 0.06191076, 125.72052284, -3348.84768653, 0.05, 2, 0, 71005, 22005, 1, 3)
    ops.uniaxialMaterial('LimitState', 31005, 44.90018673, 0.00011238, 134.70056018, 0.00033715, 449.00186728, 0.00112383, -44.90018673, -0.00011238, -134.70056018, -0.00033715, -449.00186728, -0.00112383, 0.4, 0.3, 0.003, 0.0, 0.0, 11005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1005, 99999, 'P', 41005, 'Vy', 31005, 'Vz', 21005, 'My', 11005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171005, 71005, 171005, 1005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122005, 122005, 22005, 1005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171006, 18.6, 0.0, 3.3)
    ops.node(122006, 18.6, 0.0, 5.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1006, 171006, 122006, 0.09, 31197573.65977765, 12998989.02490735, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21006, 55.10285852, 0.00107907, 66.42808297, 0.01931966, 6.6428083, 0.0678392, -55.10285852, -0.00107907, -66.42808297, -0.01931966, -6.6428083, -0.0678392, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11006, 50.91470087, 0.00107907, 61.37913829, 0.01931966, 6.13791383, 0.0678392, -50.91470087, -0.00107907, -61.37913829, -0.01931966, -6.13791383, -0.0678392, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21006, 1006, 0.0, 111.84754073, 0.02158148, 111.84754073, 0.06474445, 78.29327851, -1553.84489951, 0.05, 2, 0, 71006, 22006, 2, 3)
    ops.uniaxialMaterial('LimitState', 41006, 27.96188518, 8.748e-05, 83.88565554, 0.00026243, 279.61885182, 0.00087477, -27.96188518, -8.748e-05, -83.88565554, -0.00026243, -279.61885182, -0.00087477, 0.4, 0.3, 0.003, 0.0, 0.0, 21006, 2)
    ops.limitCurve('ThreePoint', 11006, 1006, 0.0, 111.84754073, 0.02158148, 111.84754073, 0.06474445, 78.29327851, -1553.84489951, 0.05, 2, 0, 71006, 22006, 1, 3)
    ops.uniaxialMaterial('LimitState', 31006, 27.96188518, 8.748e-05, 83.88565554, 0.00026243, 279.61885182, 0.00087477, -27.96188518, -8.748e-05, -83.88565554, -0.00026243, -279.61885182, -0.00087477, 0.4, 0.3, 0.003, 0.0, 0.0, 11006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1006, 99999, 'P', 41006, 'Vy', 31006, 'Vz', 21006, 'My', 11006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171006, 71006, 171006, 1006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122006, 122006, 22006, 1006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171007, 0.0, 5.35, 3.3)
    ops.node(122007, 0.0, 5.35, 5.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1007, 171007, 122007, 0.1225, 28469704.83172237, 11862377.01321765, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21007, 98.53311738, 0.00099827, 119.16008355, 0.01692352, 11.91600836, 0.05439364, -98.53311738, -0.00099827, -119.16008355, -0.01692352, -11.91600836, -0.05439364, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11007, 86.70076844, 0.00099827, 104.85074548, 0.01692352, 10.48507455, 0.05439364, -86.70076844, -0.00099827, -104.85074548, -0.01692352, -10.48507455, -0.05439364, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21007, 1007, 0.0, 135.72710389, 0.01996536, 135.72710389, 0.05989607, 95.00897272, -1639.37857753, 0.05, 2, 0, 71007, 22007, 2, 3)
    ops.uniaxialMaterial('LimitState', 41007, 33.93177597, 8.546e-05, 101.79532792, 0.00025639, 339.31775972, 0.00085463, -33.93177597, -8.546e-05, -101.79532792, -0.00025639, -339.31775972, -0.00085463, 0.4, 0.3, 0.003, 0.0, 0.0, 21007, 2)
    ops.limitCurve('ThreePoint', 11007, 1007, 0.0, 135.72710389, 0.01996536, 135.72710389, 0.05989607, 95.00897272, -1639.37857753, 0.05, 2, 0, 71007, 22007, 1, 3)
    ops.uniaxialMaterial('LimitState', 31007, 33.93177597, 8.546e-05, 101.79532792, 0.00025639, 339.31775972, 0.00085463, -33.93177597, -8.546e-05, -101.79532792, -0.00025639, -339.31775972, -0.00085463, 0.4, 0.3, 0.003, 0.0, 0.0, 11007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1007, 99999, 'P', 41007, 'Vy', 31007, 'Vz', 21007, 'My', 11007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171007, 71007, 171007, 1007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122007, 122007, 22007, 1007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171008, 3.9, 5.35, 3.3)
    ops.node(122008, 3.9, 5.35, 5.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1008, 171008, 122008, 0.16, 30835971.22915247, 12848321.34548019, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21008, 150.7249747, 0.00088281, 181.30893787, 0.02123914, 18.13089379, 0.06307835, -150.7249747, -0.00088281, -181.30893787, -0.02123914, -18.13089379, -0.06307835, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11008, 130.17363042, 0.00088281, 156.58747144, 0.02123914, 15.65874714, 0.06307835, -130.17363042, -0.00088281, -156.58747144, -0.02123914, -15.65874714, -0.06307835, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21008, 1008, 0.0, 202.38481221, 0.01765618, 202.38481221, 0.05296854, 141.66936854, -2453.97571405, 0.05, 2, 0, 71008, 22008, 2, 3)
    ops.uniaxialMaterial('LimitState', 41008, 50.59620305, 9.008e-05, 151.78860915, 0.00027024, 505.96203051, 0.00090081, -50.59620305, -9.008e-05, -151.78860915, -0.00027024, -505.96203051, -0.00090081, 0.4, 0.3, 0.003, 0.0, 0.0, 21008, 2)
    ops.limitCurve('ThreePoint', 11008, 1008, 0.0, 202.38481221, 0.01765618, 202.38481221, 0.05296854, 141.66936854, -2453.97571405, 0.05, 2, 0, 71008, 22008, 1, 3)
    ops.uniaxialMaterial('LimitState', 31008, 50.59620305, 9.008e-05, 151.78860915, 0.00027024, 505.96203051, 0.00090081, -50.59620305, -9.008e-05, -151.78860915, -0.00027024, -505.96203051, -0.00090081, 0.4, 0.3, 0.003, 0.0, 0.0, 11008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1008, 99999, 'P', 41008, 'Vy', 31008, 'Vz', 21008, 'My', 11008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171008, 71008, 171008, 1008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122008, 122008, 22008, 1008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171009, 7.8, 5.35, 3.3)
    ops.node(122009, 7.8, 5.35, 5.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1009, 171009, 122009, 0.16, 28831162.20095946, 12012984.25039978, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21009, 151.90569666, 0.00092087, 183.5343769, 0.01957797, 18.35343769, 0.0596616, -151.90569666, -0.00092087, -183.5343769, -0.01957797, -18.35343769, -0.0596616, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11009, 129.19477589, 0.00092087, 156.09475624, 0.01957797, 15.60947562, 0.0596616, -129.19477589, -0.00092087, -156.09475624, -0.01957797, -15.60947562, -0.0596616, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21009, 1009, 0.0, 183.31614949, 0.01841737, 183.31614949, 0.0552521, 128.32130465, -2241.37796304, 0.05, 2, 0, 71009, 22009, 2, 3)
    ops.uniaxialMaterial('LimitState', 41009, 45.82903737, 8.727e-05, 137.48711212, 0.0002618, 458.29037374, 0.00087267, -45.82903737, -8.727e-05, -137.48711212, -0.0002618, -458.29037374, -0.00087267, 0.4, 0.3, 0.003, 0.0, 0.0, 21009, 2)
    ops.limitCurve('ThreePoint', 11009, 1009, 0.0, 183.31614949, 0.01841737, 183.31614949, 0.0552521, 128.32130465, -2241.37796304, 0.05, 2, 0, 71009, 22009, 1, 3)
    ops.uniaxialMaterial('LimitState', 31009, 45.82903737, 8.727e-05, 137.48711212, 0.0002618, 458.29037374, 0.00087267, -45.82903737, -8.727e-05, -137.48711212, -0.0002618, -458.29037374, -0.00087267, 0.4, 0.3, 0.003, 0.0, 0.0, 11009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1009, 99999, 'P', 41009, 'Vy', 31009, 'Vz', 21009, 'My', 11009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171009, 71009, 171009, 1009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122009, 122009, 22009, 1009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171010, 10.8, 5.35, 3.3)
    ops.node(122010, 10.8, 5.35, 5.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1010, 171010, 122010, 0.16, 29112165.54338898, 12130068.97641208, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21010, 150.63435238, 0.0009165, 181.92179776, 0.02107361, 18.19217978, 0.06156884, -150.63435238, -0.0009165, -181.92179776, -0.02107361, -18.19217978, -0.06156884, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11010, 128.49382176, 0.0009165, 155.18257746, 0.02107361, 15.51825775, 0.06156884, -128.49382176, -0.0009165, -155.18257746, -0.02107361, -15.51825775, -0.06156884, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21010, 1010, 0.0, 189.39835169, 0.01833001, 189.39835169, 0.05499002, 132.57884618, -2390.97354788, 0.05, 2, 0, 71010, 22010, 2, 3)
    ops.uniaxialMaterial('LimitState', 41010, 47.34958792, 8.929e-05, 142.04876376, 0.00026788, 473.49587922, 0.00089292, -47.34958792, -8.929e-05, -142.04876376, -0.00026788, -473.49587922, -0.00089292, 0.4, 0.3, 0.003, 0.0, 0.0, 21010, 2)
    ops.limitCurve('ThreePoint', 11010, 1010, 0.0, 189.39835169, 0.01833001, 189.39835169, 0.05499002, 132.57884618, -2390.97354788, 0.05, 2, 0, 71010, 22010, 1, 3)
    ops.uniaxialMaterial('LimitState', 31010, 47.34958792, 8.929e-05, 142.04876376, 0.00026788, 473.49587922, 0.00089292, -47.34958792, -8.929e-05, -142.04876376, -0.00026788, -473.49587922, -0.00089292, 0.4, 0.3, 0.003, 0.0, 0.0, 11010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1010, 99999, 'P', 41010, 'Vy', 31010, 'Vz', 21010, 'My', 11010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171010, 71010, 171010, 1010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122010, 122010, 22010, 1010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171011, 14.7, 5.35, 3.3)
    ops.node(122011, 14.7, 5.35, 5.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1011, 171011, 122011, 0.16, 31634465.25138603, 13181027.18807751, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21011, 154.13188745, 0.00086583, 185.06950997, 0.02031468, 18.506951, 0.0631158, -154.13188745, -0.00086583, -185.06950997, -0.02031468, -18.506951, -0.0631158, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11011, 132.07314003, 0.00086583, 158.58309212, 0.02031468, 15.85830921, 0.0631158, -132.07314003, -0.00086583, -158.58309212, -0.02031468, -15.85830921, -0.0631158, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21011, 1011, 0.0, 203.22546426, 0.01731662, 203.22546426, 0.05194985, 142.25782498, -2354.20830885, 0.05, 2, 0, 71011, 22011, 2, 3)
    ops.uniaxialMaterial('LimitState', 41011, 50.80636606, 8.817e-05, 152.41909819, 0.00026452, 508.06366064, 0.00088172, -50.80636606, -8.817e-05, -152.41909819, -0.00026452, -508.06366064, -0.00088172, 0.4, 0.3, 0.003, 0.0, 0.0, 21011, 2)
    ops.limitCurve('ThreePoint', 11011, 1011, 0.0, 203.22546426, 0.01731662, 203.22546426, 0.05194985, 142.25782498, -2354.20830885, 0.05, 2, 0, 71011, 22011, 1, 3)
    ops.uniaxialMaterial('LimitState', 31011, 50.80636606, 8.817e-05, 152.41909819, 0.00026452, 508.06366064, 0.00088172, -50.80636606, -8.817e-05, -152.41909819, -0.00026452, -508.06366064, -0.00088172, 0.4, 0.3, 0.003, 0.0, 0.0, 11011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1011, 99999, 'P', 41011, 'Vy', 31011, 'Vz', 21011, 'My', 11011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171011, 71011, 171011, 1011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122011, 122011, 22011, 1011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171012, 18.6, 5.35, 3.3)
    ops.node(122012, 18.6, 5.35, 5.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1012, 171012, 122012, 0.1225, 29797622.31469679, 12415675.96445699, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21012, 98.72431964, 0.00100697, 119.13690621, 0.01752789, 11.91369062, 0.05673721, -98.72431964, -0.00100697, -119.13690621, -0.01752789, -11.91369062, -0.05673721, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11012, 87.33127688, 0.00100697, 105.38819797, 0.01752789, 10.5388198, 0.05673721, -87.33127688, -0.00100697, -105.38819797, -0.01752789, -10.5388198, -0.05673721, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21012, 1012, 0.0, 140.42845733, 0.02013936, 140.42845733, 0.06041807, 98.29992013, -1632.27397632, 0.05, 2, 0, 71012, 22012, 2, 3)
    ops.uniaxialMaterial('LimitState', 41012, 35.10711433, 8.448e-05, 105.321343, 0.00025345, 351.07114332, 0.00084483, -35.10711433, -8.448e-05, -105.321343, -0.00025345, -351.07114332, -0.00084483, 0.4, 0.3, 0.003, 0.0, 0.0, 21012, 2)
    ops.limitCurve('ThreePoint', 11012, 1012, 0.0, 140.42845733, 0.02013936, 140.42845733, 0.06041807, 98.29992013, -1632.27397632, 0.05, 2, 0, 71012, 22012, 1, 3)
    ops.uniaxialMaterial('LimitState', 31012, 35.10711433, 8.448e-05, 105.321343, 0.00025345, 351.07114332, 0.00084483, -35.10711433, -8.448e-05, -105.321343, -0.00025345, -351.07114332, -0.00084483, 0.4, 0.3, 0.003, 0.0, 0.0, 11012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1012, 99999, 'P', 41012, 'Vy', 31012, 'Vz', 21012, 'My', 11012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171012, 71012, 171012, 1012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122012, 122012, 22012, 1012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171013, 0.0, 10.7, 3.3)
    ops.node(122013, 0.0, 10.7, 5.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1013, 171013, 122013, 0.09, 28932777.84087041, 12055324.10036267, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21013, 57.7059886, 0.00113686, 69.91462971, 0.02012862, 6.99146297, 0.066228, -57.7059886, -0.00113686, -69.91462971, -0.02012862, -6.99146297, -0.066228, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11013, 52.93259821, 0.00113686, 64.13135089, 0.02012862, 6.41313509, 0.066228, -52.93259821, -0.00113686, -64.13135089, -0.02012862, -6.41313509, -0.066228, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21013, 1013, 0.0, 107.40375269, 0.02273726, 107.40375269, 0.06821178, 75.18262689, -1625.59991892, 0.05, 2, 0, 71013, 22013, 2, 3)
    ops.uniaxialMaterial('LimitState', 41013, 26.85093817, 9.058e-05, 80.55281452, 0.00027173, 268.50938174, 0.00090577, -26.85093817, -9.058e-05, -80.55281452, -0.00027173, -268.50938174, -0.00090577, 0.4, 0.3, 0.003, 0.0, 0.0, 21013, 2)
    ops.limitCurve('ThreePoint', 11013, 1013, 0.0, 107.40375269, 0.02273726, 107.40375269, 0.06821178, 75.18262689, -1625.59991892, 0.05, 2, 0, 71013, 22013, 1, 3)
    ops.uniaxialMaterial('LimitState', 31013, 26.85093817, 9.058e-05, 80.55281452, 0.00027173, 268.50938174, 0.00090577, -26.85093817, -9.058e-05, -80.55281452, -0.00027173, -268.50938174, -0.00090577, 0.4, 0.3, 0.003, 0.0, 0.0, 11013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1013, 99999, 'P', 41013, 'Vy', 31013, 'Vz', 21013, 'My', 11013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171013, 71013, 171013, 1013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122013, 122013, 22013, 1013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171014, 3.9, 10.7, 3.3)
    ops.node(122014, 3.9, 10.7, 5.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1014, 171014, 122014, 0.1225, 29763467.94681929, 12401444.97784137, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21014, 87.14055626, 0.00101024, 105.21023338, 0.02850111, 10.52102334, 0.08771339, -87.14055626, -0.00101024, -105.21023338, -0.02850111, -10.52102334, -0.08771339, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11014, 99.13170235, 0.00101024, 119.6878926, 0.02850111, 11.96878926, 0.08771339, -99.13170235, -0.00101024, -119.6878926, -0.02850111, -11.96878926, -0.08771339, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21014, 1014, 0.0, 170.75037123, 0.02020479, 170.75037123, 0.06061437, 119.52525986, -2784.10696529, 0.05, 2, 0, 71014, 22014, 2, 3)
    ops.uniaxialMaterial('LimitState', 41014, 42.68759281, 0.00010284, 128.06277842, 0.00030853, 426.87592807, 0.00102843, -42.68759281, -0.00010284, -128.06277842, -0.00030853, -426.87592807, -0.00102843, 0.4, 0.3, 0.003, 0.0, 0.0, 21014, 2)
    ops.limitCurve('ThreePoint', 11014, 1014, 0.0, 170.75037123, 0.02020479, 170.75037123, 0.06061437, 119.52525986, -2784.10696529, 0.05, 2, 0, 71014, 22014, 1, 3)
    ops.uniaxialMaterial('LimitState', 31014, 42.68759281, 0.00010284, 128.06277842, 0.00030853, 426.87592807, 0.00102843, -42.68759281, -0.00010284, -128.06277842, -0.00030853, -426.87592807, -0.00102843, 0.4, 0.3, 0.003, 0.0, 0.0, 11014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1014, 99999, 'P', 41014, 'Vy', 31014, 'Vz', 21014, 'My', 11014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171014, 71014, 171014, 1014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122014, 122014, 22014, 1014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171015, 7.8, 10.7, 3.3)
    ops.node(122015, 7.8, 10.7, 5.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1015, 171015, 122015, 0.1225, 30459682.73689429, 12691534.47370596, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21015, 81.07812057, 0.00095251, 97.84751765, 0.0237531, 9.78475176, 0.07307428, -81.07812057, -0.00095251, -97.84751765, -0.0237531, -9.78475176, -0.07307428, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11015, 92.50907678, 0.00095251, 111.64273986, 0.0237531, 11.16427399, 0.07307428, -92.50907678, -0.00095251, -111.64273986, -0.0237531, -11.16427399, -0.07307428, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21015, 1015, 0.0, 156.96350734, 0.01905015, 156.96350734, 0.05715046, 109.87445514, -2288.19236855, 0.05, 2, 0, 71015, 22015, 2, 3)
    ops.uniaxialMaterial('LimitState', 41015, 39.24087684, 9.238e-05, 117.72263051, 0.00027713, 392.40876836, 0.00092378, -39.24087684, -9.238e-05, -117.72263051, -0.00027713, -392.40876836, -0.00092378, 0.4, 0.3, 0.003, 0.0, 0.0, 21015, 2)
    ops.limitCurve('ThreePoint', 11015, 1015, 0.0, 156.96350734, 0.01905015, 156.96350734, 0.05715046, 109.87445514, -2288.19236855, 0.05, 2, 0, 71015, 22015, 1, 3)
    ops.uniaxialMaterial('LimitState', 31015, 39.24087684, 9.238e-05, 117.72263051, 0.00027713, 392.40876836, 0.00092378, -39.24087684, -9.238e-05, -117.72263051, -0.00027713, -392.40876836, -0.00092378, 0.4, 0.3, 0.003, 0.0, 0.0, 11015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1015, 99999, 'P', 41015, 'Vy', 31015, 'Vz', 21015, 'My', 11015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171015, 71015, 171015, 1015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122015, 122015, 22015, 1015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171016, 10.8, 10.7, 3.3)
    ops.node(122016, 10.8, 10.7, 5.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1016, 171016, 122016, 0.1225, 31022146.02594959, 12925894.177479, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21016, 83.85709929, 0.00095648, 101.0672097, 0.02211847, 10.10672097, 0.07207426, -83.85709929, -0.00095648, -101.0672097, -0.02211847, -10.10672097, -0.07207426, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11016, 96.4753568, 0.00095648, 116.27512995, 0.02211847, 11.62751299, 0.07207426, -96.4753568, -0.00095648, -116.27512995, -0.02211847, -11.62751299, -0.07207426, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21016, 1016, 0.0, 154.30441863, 0.01912958, 154.30441863, 0.05738874, 108.01309304, -2100.35337297, 0.05, 2, 0, 71016, 22016, 2, 3)
    ops.uniaxialMaterial('LimitState', 41016, 38.57610466, 8.917e-05, 115.72831397, 0.0002675, 385.76104658, 0.00089167, -38.57610466, -8.917e-05, -115.72831397, -0.0002675, -385.76104658, -0.00089167, 0.4, 0.3, 0.003, 0.0, 0.0, 21016, 2)
    ops.limitCurve('ThreePoint', 11016, 1016, 0.0, 154.30441863, 0.01912958, 154.30441863, 0.05738874, 108.01309304, -2100.35337297, 0.05, 2, 0, 71016, 22016, 1, 3)
    ops.uniaxialMaterial('LimitState', 31016, 38.57610466, 8.917e-05, 115.72831397, 0.0002675, 385.76104658, 0.00089167, -38.57610466, -8.917e-05, -115.72831397, -0.0002675, -385.76104658, -0.00089167, 0.4, 0.3, 0.003, 0.0, 0.0, 11016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1016, 99999, 'P', 41016, 'Vy', 31016, 'Vz', 21016, 'My', 11016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171016, 71016, 171016, 1016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122016, 122016, 22016, 1016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171017, 14.7, 10.7, 3.3)
    ops.node(122017, 14.7, 10.7, 5.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1017, 171017, 122017, 0.1225, 29648948.29106077, 12353728.45460865, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21017, 85.92861896, 0.00104318, 103.76929071, 0.02916039, 10.37692907, 0.08817037, -85.92861896, -0.00104318, -103.76929071, -0.02916039, -10.37692907, -0.08817037, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11017, 96.65401408, 0.00104318, 116.72151382, 0.02916039, 11.67215138, 0.08817037, -96.65401408, -0.00104318, -116.72151382, -0.02916039, -11.67215138, -0.08817037, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21017, 1017, 0.0, 171.91556001, 0.02086355, 171.91556001, 0.06259064, 120.34089201, -2850.62682416, 0.05, 2, 0, 71017, 22017, 2, 3)
    ops.uniaxialMaterial('LimitState', 41017, 42.97889, 0.00010394, 128.93667001, 0.00031183, 429.78890002, 0.00103945, -42.97889, -0.00010394, -128.93667001, -0.00031183, -429.78890002, -0.00103945, 0.4, 0.3, 0.003, 0.0, 0.0, 21017, 2)
    ops.limitCurve('ThreePoint', 11017, 1017, 0.0, 171.91556001, 0.02086355, 171.91556001, 0.06259064, 120.34089201, -2850.62682416, 0.05, 2, 0, 71017, 22017, 1, 3)
    ops.uniaxialMaterial('LimitState', 31017, 42.97889, 0.00010394, 128.93667001, 0.00031183, 429.78890002, 0.00103945, -42.97889, -0.00010394, -128.93667001, -0.00031183, -429.78890002, -0.00103945, 0.4, 0.3, 0.003, 0.0, 0.0, 11017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1017, 99999, 'P', 41017, 'Vy', 31017, 'Vz', 21017, 'My', 11017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171017, 71017, 171017, 1017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122017, 122017, 22017, 1017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171018, 18.6, 10.7, 3.3)
    ops.node(122018, 18.6, 10.7, 5.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1018, 171018, 122018, 0.09, 31852761.18597458, 13271983.82748941, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21018, 54.47415206, 0.00106061, 65.55434163, 0.01730887, 6.55543416, 0.06641376, -54.47415206, -0.00106061, -65.55434163, -0.01730887, -6.55543416, -0.06641376, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11018, 50.40652231, 0.00106061, 60.65934501, 0.01730887, 6.0659345, 0.06641376, -50.40652231, -0.00106061, -60.65934501, -0.01730887, -6.0659345, -0.06641376, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21018, 1018, 0.0, 108.96601856, 0.02121214, 108.96601856, 0.06363643, 76.276213, -1367.82623908, 0.05, 2, 0, 71018, 22018, 2, 3)
    ops.uniaxialMaterial('LimitState', 41018, 27.24150464, 8.347e-05, 81.72451392, 0.00025041, 272.41504641, 0.00083471, -27.24150464, -8.347e-05, -81.72451392, -0.00025041, -272.41504641, -0.00083471, 0.4, 0.3, 0.003, 0.0, 0.0, 21018, 2)
    ops.limitCurve('ThreePoint', 11018, 1018, 0.0, 108.96601856, 0.02121214, 108.96601856, 0.06363643, 76.276213, -1367.82623908, 0.05, 2, 0, 71018, 22018, 1, 3)
    ops.uniaxialMaterial('LimitState', 31018, 27.24150464, 8.347e-05, 81.72451392, 0.00025041, 272.41504641, 0.00083471, -27.24150464, -8.347e-05, -81.72451392, -0.00025041, -272.41504641, -0.00083471, 0.4, 0.3, 0.003, 0.0, 0.0, 11018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1018, 99999, 'P', 41018, 'Vy', 31018, 'Vz', 21018, 'My', 11018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171018, 71018, 171018, 1018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122018, 122018, 22018, 1018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172001, 0.0, 0.0, 6.35)
    ops.node(123001, 0.0, 0.0, 8.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2001, 172001, 123001, 0.0625, 31093670.5558692, 12955696.0649455, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22001, 29.59971838, 0.00122849, 35.7193232, 0.01999205, 3.57193232, 0.07709218, -29.59971838, -0.00122849, -35.7193232, -0.01999205, -3.57193232, -0.07709218, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12001, 29.59971838, 0.00122849, 35.7193232, 0.01999205, 3.57193232, 0.07709218, -29.59971838, -0.00122849, -35.7193232, -0.01999205, -3.57193232, -0.07709218, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22001, 2001, 0.0, 83.2453312, 0.02456972, 83.2453312, 0.07370917, 58.27173184, -1438.71482273, 0.05, 2, 0, 72001, 23001, 2, 3)
    ops.uniaxialMaterial('LimitState', 42001, 20.8113328, 9.407e-05, 62.4339984, 0.0002822, 208.11332801, 0.00094068, -20.8113328, -9.407e-05, -62.4339984, -0.0002822, -208.11332801, -0.00094068, 0.4, 0.3, 0.003, 0.0, 0.0, 22001, 2)
    ops.limitCurve('ThreePoint', 12001, 2001, 0.0, 83.2453312, 0.02456972, 83.2453312, 0.07370917, 58.27173184, -1438.71482273, 0.05, 2, 0, 72001, 23001, 1, 3)
    ops.uniaxialMaterial('LimitState', 32001, 20.8113328, 9.407e-05, 62.4339984, 0.0002822, 208.11332801, 0.00094068, -20.8113328, -9.407e-05, -62.4339984, -0.0002822, -208.11332801, -0.00094068, 0.4, 0.3, 0.003, 0.0, 0.0, 12001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2001, 99999, 'P', 42001, 'Vy', 32001, 'Vz', 22001, 'My', 12001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172001, 72001, 172001, 2001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123001, 123001, 23001, 2001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172002, 3.9, 0.0, 6.35)
    ops.node(123002, 3.9, 0.0, 8.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2002, 172002, 123002, 0.0625, 31197529.69108484, 12998970.70461868, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22002, 41.53471182, 0.00143185, 49.91253444, 0.02003106, 4.99125344, 0.07093967, -41.53471182, -0.00143185, -49.91253444, -0.02003106, -4.99125344, -0.07093967, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12002, 44.51414901, 0.00143185, 53.49294357, 0.02003106, 5.34929436, 0.07093967, -44.51414901, -0.00143185, -53.49294357, -0.02003106, -5.34929436, -0.07093967, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22002, 2002, 0.0, 88.45161685, 0.02863696, 88.45161685, 0.08591089, 61.9161318, -1236.73103347, 0.05, 2, 0, 72002, 23002, 2, 3)
    ops.uniaxialMaterial('LimitState', 42002, 22.11290421, 9.962e-05, 66.33871264, 0.00029885, 221.12904213, 0.00099618, -22.11290421, -9.962e-05, -66.33871264, -0.00029885, -221.12904213, -0.00099618, 0.4, 0.3, 0.003, 0.0, 0.0, 22002, 2)
    ops.limitCurve('ThreePoint', 12002, 2002, 0.0, 88.45161685, 0.02863696, 88.45161685, 0.08591089, 61.9161318, -1236.73103347, 0.05, 2, 0, 72002, 23002, 1, 3)
    ops.uniaxialMaterial('LimitState', 32002, 22.11290421, 9.962e-05, 66.33871264, 0.00029885, 221.12904213, 0.00099618, -22.11290421, -9.962e-05, -66.33871264, -0.00029885, -221.12904213, -0.00099618, 0.4, 0.3, 0.003, 0.0, 0.0, 12002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2002, 99999, 'P', 42002, 'Vy', 32002, 'Vz', 22002, 'My', 12002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172002, 72002, 172002, 2002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123002, 123002, 23002, 2002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172005, 14.7, 0.0, 6.35)
    ops.node(123005, 14.7, 0.0, 8.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2005, 172005, 123005, 0.0625, 30639979.47479929, 12766658.1144997, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22005, 41.54448217, 0.00137424, 49.98390096, 0.01718217, 4.9983901, 0.0672344, -41.54448217, -0.00137424, -49.98390096, -0.01718217, -4.9983901, -0.0672344, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12005, 44.8435142, 0.00137424, 53.95310413, 0.01718217, 5.39531041, 0.0672344, -44.8435142, -0.00137424, -53.95310413, -0.01718217, -5.39531041, -0.0672344, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22005, 2005, 0.0, 76.71266359, 0.02748482, 76.71266359, 0.08245447, 53.69886451, -1077.40451945, 0.05, 2, 0, 72005, 23005, 2, 3)
    ops.uniaxialMaterial('LimitState', 42005, 19.1781659, 8.797e-05, 57.53449769, 0.00026391, 191.78165897, 0.00087969, -19.1781659, -8.797e-05, -57.53449769, -0.00026391, -191.78165897, -0.00087969, 0.4, 0.3, 0.003, 0.0, 0.0, 22005, 2)
    ops.limitCurve('ThreePoint', 12005, 2005, 0.0, 76.71266359, 0.02748482, 76.71266359, 0.08245447, 53.69886451, -1077.40451945, 0.05, 2, 0, 72005, 23005, 1, 3)
    ops.uniaxialMaterial('LimitState', 32005, 19.1781659, 8.797e-05, 57.53449769, 0.00026391, 191.78165897, 0.00087969, -19.1781659, -8.797e-05, -57.53449769, -0.00026391, -191.78165897, -0.00087969, 0.4, 0.3, 0.003, 0.0, 0.0, 12005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2005, 99999, 'P', 42005, 'Vy', 32005, 'Vz', 22005, 'My', 12005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172005, 72005, 172005, 2005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123005, 123005, 23005, 2005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172006, 18.6, 0.0, 6.35)
    ops.node(123006, 18.6, 0.0, 8.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2006, 172006, 123006, 0.0625, 32743280.02781167, 13643033.34492153, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22006, 29.20928767, 0.00143576, 35.08028321, 0.01804535, 3.50802832, 0.07660127, -29.20928767, -0.00143576, -35.08028321, -0.01804535, -3.50802832, -0.07660127, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12006, 29.20928767, 0.00143576, 35.08028321, 0.01804535, 3.50802832, 0.07660127, -29.20928767, -0.00143576, -35.08028321, -0.01804535, -3.50802832, -0.07660127, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22006, 2006, 0.0, 83.16753182, 0.02871528, 83.16753182, 0.08614584, 58.21727228, -1277.86686332, 0.05, 2, 0, 72006, 23006, 2, 3)
    ops.uniaxialMaterial('LimitState', 42006, 20.79188296, 8.925e-05, 62.37564887, 0.00026774, 207.91882955, 0.00089245, -20.79188296, -8.925e-05, -62.37564887, -0.00026774, -207.91882955, -0.00089245, 0.4, 0.3, 0.003, 0.0, 0.0, 22006, 2)
    ops.limitCurve('ThreePoint', 12006, 2006, 0.0, 83.16753182, 0.02871528, 83.16753182, 0.08614584, 58.21727228, -1277.86686332, 0.05, 2, 0, 72006, 23006, 1, 3)
    ops.uniaxialMaterial('LimitState', 32006, 20.79188296, 8.925e-05, 62.37564887, 0.00026774, 207.91882955, 0.00089245, -20.79188296, -8.925e-05, -62.37564887, -0.00026774, -207.91882955, -0.00089245, 0.4, 0.3, 0.003, 0.0, 0.0, 12006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2006, 99999, 'P', 42006, 'Vy', 32006, 'Vz', 22006, 'My', 12006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172006, 72006, 172006, 2006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123006, 123006, 23006, 2006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172007, 0.0, 5.35, 6.35)
    ops.node(123007, 0.0, 5.35, 8.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2007, 172007, 123007, 0.0625, 31552901.56802548, 13147042.32001062, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22007, 37.44130927, 0.00134692, 44.94046139, 0.01924877, 4.49404614, 0.07013286, -37.44130927, -0.00134692, -44.94046139, -0.01924877, -4.49404614, -0.07013286, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12007, 37.44130927, 0.00134692, 44.94046139, 0.01924877, 4.49404614, 0.07013286, -37.44130927, -0.00134692, -44.94046139, -0.01924877, -4.49404614, -0.07013286, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22007, 2007, 0.0, 91.64757037, 0.02693833, 91.64757037, 0.08081499, 64.15329926, -1301.46141405, 0.05, 2, 0, 72007, 23007, 2, 3)
    ops.uniaxialMaterial('LimitState', 42007, 22.91189259, 0.00010205, 68.73567778, 0.00030616, 229.11892594, 0.00102055, -22.91189259, -0.00010205, -68.73567778, -0.00030616, -229.11892594, -0.00102055, 0.4, 0.3, 0.003, 0.0, 0.0, 22007, 2)
    ops.limitCurve('ThreePoint', 12007, 2007, 0.0, 91.64757037, 0.02693833, 91.64757037, 0.08081499, 64.15329926, -1301.46141405, 0.05, 2, 0, 72007, 23007, 1, 3)
    ops.uniaxialMaterial('LimitState', 32007, 22.91189259, 0.00010205, 68.73567778, 0.00030616, 229.11892594, 0.00102055, -22.91189259, -0.00010205, -68.73567778, -0.00030616, -229.11892594, -0.00102055, 0.4, 0.3, 0.003, 0.0, 0.0, 12007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2007, 99999, 'P', 42007, 'Vy', 32007, 'Vz', 22007, 'My', 12007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172007, 72007, 172007, 2007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123007, 123007, 23007, 2007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172008, 3.9, 5.35, 6.35)
    ops.node(123008, 3.9, 5.35, 8.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2008, 172008, 123008, 0.1225, 29383932.72866164, 12243305.30360902, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22008, 98.91338187, 0.00098644, 119.53441302, 0.020686, 11.9534413, 0.06744662, -98.91338187, -0.00098644, -119.53441302, -0.020686, -11.9534413, -0.06744662, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12008, 86.33622738, 0.00098644, 104.33522814, 0.020686, 10.43352281, 0.06744662, -86.33622738, -0.00098644, -104.33522814, -0.020686, -10.43352281, -0.06744662, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22008, 2008, 0.0, 145.76550275, 0.01972889, 145.76550275, 0.05918666, 102.03585193, -1913.63414195, 0.05, 2, 0, 72008, 23008, 2, 3)
    ops.uniaxialMaterial('LimitState', 42008, 36.44137569, 8.893e-05, 109.32412706, 0.00026679, 364.41375688, 0.00088929, -36.44137569, -8.893e-05, -109.32412706, -0.00026679, -364.41375688, -0.00088929, 0.4, 0.3, 0.003, 0.0, 0.0, 22008, 2)
    ops.limitCurve('ThreePoint', 12008, 2008, 0.0, 145.76550275, 0.01972889, 145.76550275, 0.05918666, 102.03585193, -1913.63414195, 0.05, 2, 0, 72008, 23008, 1, 3)
    ops.uniaxialMaterial('LimitState', 32008, 36.44137569, 8.893e-05, 109.32412706, 0.00026679, 364.41375688, 0.00088929, -36.44137569, -8.893e-05, -109.32412706, -0.00026679, -364.41375688, -0.00088929, 0.4, 0.3, 0.003, 0.0, 0.0, 12008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2008, 99999, 'P', 42008, 'Vy', 32008, 'Vz', 22008, 'My', 12008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172008, 72008, 172008, 2008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123008, 123008, 23008, 2008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172009, 7.8, 5.35, 6.35)
    ops.node(123009, 7.8, 5.35, 8.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2009, 172009, 123009, 0.1225, 32173567.68366997, 13405653.20152915, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22009, 85.04358138, 0.00095544, 102.16342626, 0.0214136, 10.21634263, 0.07222302, -85.04358138, -0.00095544, -102.16342626, -0.0214136, -10.21634263, -0.07222302, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12009, 97.40460284, 0.00095544, 117.01280448, 0.0214136, 11.70128045, 0.07222302, -97.40460284, -0.00095544, -117.01280448, -0.0214136, -11.70128045, -0.07222302, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22009, 2009, 0.0, 161.81087021, 0.01910884, 161.81087021, 0.05732653, 113.26760915, -2179.52677593, 0.05, 2, 0, 72009, 23009, 2, 3)
    ops.uniaxialMaterial('LimitState', 42009, 40.45271755, 9.016e-05, 121.35815266, 0.00027047, 404.52717552, 0.00090158, -40.45271755, -9.016e-05, -121.35815266, -0.00027047, -404.52717552, -0.00090158, 0.4, 0.3, 0.003, 0.0, 0.0, 22009, 2)
    ops.limitCurve('ThreePoint', 12009, 2009, 0.0, 161.81087021, 0.01910884, 161.81087021, 0.05732653, 113.26760915, -2179.52677593, 0.05, 2, 0, 72009, 23009, 1, 3)
    ops.uniaxialMaterial('LimitState', 32009, 40.45271755, 9.016e-05, 121.35815266, 0.00027047, 404.52717552, 0.00090158, -40.45271755, -9.016e-05, -121.35815266, -0.00027047, -404.52717552, -0.00090158, 0.4, 0.3, 0.003, 0.0, 0.0, 12009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2009, 99999, 'P', 42009, 'Vy', 32009, 'Vz', 22009, 'My', 12009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172009, 72009, 172009, 2009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123009, 123009, 23009, 2009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172010, 10.8, 5.35, 6.35)
    ops.node(123010, 10.8, 5.35, 8.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2010, 172010, 123010, 0.1225, 34740952.45671548, 14475396.85696478, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22010, 82.83042796, 0.00094009, 98.67701638, 0.0213546, 9.86770164, 0.07434743, -82.83042796, -0.00094009, -98.67701638, -0.0213546, -9.86770164, -0.07434743, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12010, 93.44800726, 0.00094009, 111.32588313, 0.0213546, 11.13258831, 0.07434743, -93.44800726, -0.00094009, -111.32588313, -0.0213546, -11.13258831, -0.07434743, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22010, 2010, 0.0, 171.51931629, 0.01880189, 171.51931629, 0.05640568, 120.0635214, -2159.17375684, 0.05, 2, 0, 72010, 23010, 2, 3)
    ops.uniaxialMaterial('LimitState', 42010, 42.87982907, 8.85e-05, 128.63948722, 0.00026551, 428.79829072, 0.00088505, -42.87982907, -8.85e-05, -128.63948722, -0.00026551, -428.79829072, -0.00088505, 0.4, 0.3, 0.003, 0.0, 0.0, 22010, 2)
    ops.limitCurve('ThreePoint', 12010, 2010, 0.0, 171.51931629, 0.01880189, 171.51931629, 0.05640568, 120.0635214, -2159.17375684, 0.05, 2, 0, 72010, 23010, 1, 3)
    ops.uniaxialMaterial('LimitState', 32010, 42.87982907, 8.85e-05, 128.63948722, 0.00026551, 428.79829072, 0.00088505, -42.87982907, -8.85e-05, -128.63948722, -0.00026551, -428.79829072, -0.00088505, 0.4, 0.3, 0.003, 0.0, 0.0, 12010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2010, 99999, 'P', 42010, 'Vy', 32010, 'Vz', 22010, 'My', 12010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172010, 72010, 172010, 2010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123010, 123010, 23010, 2010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172011, 14.7, 5.35, 6.35)
    ops.node(123011, 14.7, 5.35, 8.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2011, 172011, 123011, 0.1225, 31173006.9773976, 12988752.907249, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22011, 95.26903579, 0.00096231, 114.69675293, 0.02400269, 11.46967529, 0.073071, -95.26903579, -0.00096231, -114.69675293, -0.02400269, -11.46967529, -0.073071, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12011, 84.12786289, 0.00096231, 101.2836188, 0.02400269, 10.12836188, 0.073071, -84.12786289, -0.00096231, -101.2836188, -0.02400269, -10.12836188, -0.073071, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22011, 2011, 0.0, 161.20604433, 0.01924614, 161.20604433, 0.05773843, 112.84423103, -2228.12778534, 0.05, 2, 0, 72011, 23011, 2, 3)
    ops.uniaxialMaterial('LimitState', 42011, 40.30151108, 9.27e-05, 120.90453325, 0.00027811, 403.01511082, 0.00092704, -40.30151108, -9.27e-05, -120.90453325, -0.00027811, -403.01511082, -0.00092704, 0.4, 0.3, 0.003, 0.0, 0.0, 22011, 2)
    ops.limitCurve('ThreePoint', 12011, 2011, 0.0, 161.20604433, 0.01924614, 161.20604433, 0.05773843, 112.84423103, -2228.12778534, 0.05, 2, 0, 72011, 23011, 1, 3)
    ops.uniaxialMaterial('LimitState', 32011, 40.30151108, 9.27e-05, 120.90453325, 0.00027811, 403.01511082, 0.00092704, -40.30151108, -9.27e-05, -120.90453325, -0.00027811, -403.01511082, -0.00092704, 0.4, 0.3, 0.003, 0.0, 0.0, 12011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2011, 99999, 'P', 42011, 'Vy', 32011, 'Vz', 22011, 'My', 12011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172011, 72011, 172011, 2011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123011, 123011, 23011, 2011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172012, 18.6, 5.35, 6.35)
    ops.node(123012, 18.6, 5.35, 8.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2012, 172012, 123012, 0.0625, 33548430.65450311, 13978512.77270963, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22012, 37.84240772, 0.00128153, 45.17658646, 0.01902249, 4.51765865, 0.07255365, -37.84240772, -0.00128153, -45.17658646, -0.01902249, -4.51765865, -0.07255365, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12012, 37.84240772, 0.00128153, 45.17658646, 0.01902249, 4.51765865, 0.07255365, -37.84240772, -0.00128153, -45.17658646, -0.01902249, -4.51765865, -0.07255365, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22012, 2012, 0.0, 95.27673564, 0.02563056, 95.27673564, 0.07689169, 66.69371495, -1285.92338252, 0.05, 2, 0, 72012, 23012, 2, 3)
    ops.uniaxialMaterial('LimitState', 42012, 23.81918391, 9.979e-05, 71.45755173, 0.00029936, 238.19183911, 0.00099785, -23.81918391, -9.979e-05, -71.45755173, -0.00029936, -238.19183911, -0.00099785, 0.4, 0.3, 0.003, 0.0, 0.0, 22012, 2)
    ops.limitCurve('ThreePoint', 12012, 2012, 0.0, 95.27673564, 0.02563056, 95.27673564, 0.07689169, 66.69371495, -1285.92338252, 0.05, 2, 0, 72012, 23012, 1, 3)
    ops.uniaxialMaterial('LimitState', 32012, 23.81918391, 9.979e-05, 71.45755173, 0.00029936, 238.19183911, 0.00099785, -23.81918391, -9.979e-05, -71.45755173, -0.00029936, -238.19183911, -0.00099785, 0.4, 0.3, 0.003, 0.0, 0.0, 12012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2012, 99999, 'P', 42012, 'Vy', 32012, 'Vz', 22012, 'My', 12012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172012, 72012, 172012, 2012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123012, 123012, 23012, 2012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172013, 0.0, 10.7, 6.35)
    ops.node(123013, 0.0, 10.7, 8.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2013, 172013, 123013, 0.0625, 30419003.01311731, 12674584.58879888, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22013, 29.77107967, 0.00129218, 35.9873181, 0.02165134, 3.59873181, 0.07806661, -29.77107967, -0.00129218, -35.9873181, -0.02165134, -3.59873181, -0.07806661, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12013, 29.77107967, 0.00129218, 35.9873181, 0.02165134, 3.59873181, 0.07806661, -29.77107967, -0.00129218, -35.9873181, -0.02165134, -3.59873181, -0.07806661, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22013, 2013, 0.0, 85.27397147, 0.0258435, 85.27397147, 0.07753051, 59.69178003, -1609.77207779, 0.05, 2, 0, 72013, 23013, 2, 3)
    ops.uniaxialMaterial('LimitState', 42013, 21.31849287, 9.85e-05, 63.9554786, 0.00029549, 213.18492867, 0.00098497, -21.31849287, -9.85e-05, -63.9554786, -0.00029549, -213.18492867, -0.00098497, 0.4, 0.3, 0.003, 0.0, 0.0, 22013, 2)
    ops.limitCurve('ThreePoint', 12013, 2013, 0.0, 85.27397147, 0.0258435, 85.27397147, 0.07753051, 59.69178003, -1609.77207779, 0.05, 2, 0, 72013, 23013, 1, 3)
    ops.uniaxialMaterial('LimitState', 32013, 21.31849287, 9.85e-05, 63.9554786, 0.00029549, 213.18492867, 0.00098497, -21.31849287, -9.85e-05, -63.9554786, -0.00029549, -213.18492867, -0.00098497, 0.4, 0.3, 0.003, 0.0, 0.0, 12013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2013, 99999, 'P', 42013, 'Vy', 32013, 'Vz', 22013, 'My', 12013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172013, 72013, 172013, 2013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123013, 123013, 23013, 2013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172014, 3.9, 10.7, 6.35)
    ops.node(123014, 3.9, 10.7, 8.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2014, 172014, 123014, 0.0625, 31490873.63180486, 13121197.34658536, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22014, 43.49536148, 0.00141581, 52.23337511, 0.01750483, 5.22333751, 0.06884341, -43.49536148, -0.00141581, -52.23337511, -0.01750483, -5.22333751, -0.06884341, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12014, 47.10920174, 0.00141581, 56.5732189, 0.01750483, 5.65732189, 0.06884341, -47.10920174, -0.00141581, -56.5732189, -0.01750483, -5.65732189, -0.06884341, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22014, 2014, 0.0, 83.22852055, 0.02831626, 83.22852055, 0.08494878, 58.25996438, -1066.70195399, 0.05, 2, 0, 72014, 23014, 2, 3)
    ops.uniaxialMaterial('LimitState', 42014, 20.80713014, 9.286e-05, 62.42139041, 0.00027859, 208.07130137, 0.00092862, -20.80713014, -9.286e-05, -62.42139041, -0.00027859, -208.07130137, -0.00092862, 0.4, 0.3, 0.003, 0.0, 0.0, 22014, 2)
    ops.limitCurve('ThreePoint', 12014, 2014, 0.0, 83.22852055, 0.02831626, 83.22852055, 0.08494878, 58.25996438, -1066.70195399, 0.05, 2, 0, 72014, 23014, 1, 3)
    ops.uniaxialMaterial('LimitState', 32014, 20.80713014, 9.286e-05, 62.42139041, 0.00027859, 208.07130137, 0.00092862, -20.80713014, -9.286e-05, -62.42139041, -0.00027859, -208.07130137, -0.00092862, 0.4, 0.3, 0.003, 0.0, 0.0, 12014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2014, 99999, 'P', 42014, 'Vy', 32014, 'Vz', 22014, 'My', 12014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172014, 72014, 172014, 2014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123014, 123014, 23014, 2014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172015, 7.8, 10.7, 6.35)
    ops.node(123015, 7.8, 10.7, 8.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2015, 172015, 123015, 0.0625, 30833253.78289012, 12847189.07620422, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22015, 40.23153739, 0.00142964, 48.44125444, 0.01791627, 4.84412544, 0.07005022, -40.23153739, -0.00142964, -48.44125444, -0.01791627, -4.84412544, -0.07005022, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12015, 43.31229077, 0.00142964, 52.15067168, 0.01791627, 5.21506717, 0.07005022, -43.31229077, -0.00142964, -52.15067168, -0.01791627, -5.21506717, -0.07005022, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22015, 2015, 0.0, 81.37550114, 0.02859278, 81.37550114, 0.08577835, 56.9628508, -1163.36920088, 0.05, 2, 0, 72015, 23015, 2, 3)
    ops.uniaxialMaterial('LimitState', 42015, 20.34387528, 9.273e-05, 61.03162585, 0.00027819, 203.43875285, 0.00092731, -20.34387528, -9.273e-05, -61.03162585, -0.00027819, -203.43875285, -0.00092731, 0.4, 0.3, 0.003, 0.0, 0.0, 22015, 2)
    ops.limitCurve('ThreePoint', 12015, 2015, 0.0, 81.37550114, 0.02859278, 81.37550114, 0.08577835, 56.9628508, -1163.36920088, 0.05, 2, 0, 72015, 23015, 1, 3)
    ops.uniaxialMaterial('LimitState', 32015, 20.34387528, 9.273e-05, 61.03162585, 0.00027819, 203.43875285, 0.00092731, -20.34387528, -9.273e-05, -61.03162585, -0.00027819, -203.43875285, -0.00092731, 0.4, 0.3, 0.003, 0.0, 0.0, 12015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2015, 99999, 'P', 42015, 'Vy', 32015, 'Vz', 22015, 'My', 12015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172015, 72015, 172015, 2015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123015, 123015, 23015, 2015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172016, 10.8, 10.7, 6.35)
    ops.node(123016, 10.8, 10.7, 8.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2016, 172016, 123016, 0.0625, 30876581.74064044, 12865242.39193352, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22016, 41.31030841, 0.00129049, 49.73532948, 0.01946746, 4.97353295, 0.07166233, -41.31030841, -0.00129049, -49.73532948, -0.01946746, -4.97353295, -0.07166233, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12016, 45.29253862, 0.00129049, 54.52971469, 0.01946746, 5.45297147, 0.07166233, -45.29253862, -0.00129049, -54.52971469, -0.01946746, -5.45297147, -0.07166233, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22016, 2016, 0.0, 85.1765565, 0.02580975, 85.1765565, 0.07742926, 59.62358955, -1217.28542833, 0.05, 2, 0, 72016, 23016, 2, 3)
    ops.uniaxialMaterial('LimitState', 42016, 21.29413912, 9.693e-05, 63.88241737, 0.00029078, 212.94139124, 0.00096927, -21.29413912, -9.693e-05, -63.88241737, -0.00029078, -212.94139124, -0.00096927, 0.4, 0.3, 0.003, 0.0, 0.0, 22016, 2)
    ops.limitCurve('ThreePoint', 12016, 2016, 0.0, 85.1765565, 0.02580975, 85.1765565, 0.07742926, 59.62358955, -1217.28542833, 0.05, 2, 0, 72016, 23016, 1, 3)
    ops.uniaxialMaterial('LimitState', 32016, 21.29413912, 9.693e-05, 63.88241737, 0.00029078, 212.94139124, 0.00096927, -21.29413912, -9.693e-05, -63.88241737, -0.00029078, -212.94139124, -0.00096927, 0.4, 0.3, 0.003, 0.0, 0.0, 12016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2016, 99999, 'P', 42016, 'Vy', 32016, 'Vz', 22016, 'My', 12016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172016, 72016, 172016, 2016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123016, 123016, 23016, 2016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172017, 14.7, 10.7, 6.35)
    ops.node(123017, 14.7, 10.7, 8.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2017, 172017, 123017, 0.0625, 32628585.07440268, 13595243.78100112, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22017, 44.01839008, 0.00132891, 52.70727738, 0.02063391, 5.27072774, 0.07351556, -44.01839008, -0.00132891, -52.70727738, -0.02063391, -5.27072774, -0.07351556, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12017, 48.01521633, 0.00132891, 57.493046, 0.02063391, 5.7493046, 0.07351556, -48.01521633, -0.00132891, -57.493046, -0.02063391, -5.7493046, -0.07351556, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22017, 2017, 0.0, 94.97170497, 0.0265782, 94.97170497, 0.0797346, 66.48019348, -1368.18837111, 0.05, 2, 0, 72017, 23017, 2, 3)
    ops.uniaxialMaterial('LimitState', 42017, 23.74292624, 0.00010227, 71.22877873, 0.00030681, 237.42926243, 0.0010227, -23.74292624, -0.00010227, -71.22877873, -0.00030681, -237.42926243, -0.0010227, 0.4, 0.3, 0.003, 0.0, 0.0, 22017, 2)
    ops.limitCurve('ThreePoint', 12017, 2017, 0.0, 94.97170497, 0.0265782, 94.97170497, 0.0797346, 66.48019348, -1368.18837111, 0.05, 2, 0, 72017, 23017, 1, 3)
    ops.uniaxialMaterial('LimitState', 32017, 23.74292624, 0.00010227, 71.22877873, 0.00030681, 237.42926243, 0.0010227, -23.74292624, -0.00010227, -71.22877873, -0.00030681, -237.42926243, -0.0010227, 0.4, 0.3, 0.003, 0.0, 0.0, 12017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2017, 99999, 'P', 42017, 'Vy', 32017, 'Vz', 22017, 'My', 12017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172017, 72017, 172017, 2017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123017, 123017, 23017, 2017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172018, 18.6, 10.7, 6.35)
    ops.node(123018, 18.6, 10.7, 8.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2018, 172018, 123018, 0.0625, 31340563.46419737, 13058568.11008224, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22018, 29.93071644, 0.00126413, 36.09494487, 0.02106805, 3.60949449, 0.07840497, -29.93071644, -0.00126413, -36.09494487, -0.02106805, -3.60949449, -0.07840497, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12018, 29.93071644, 0.00126413, 36.09494487, 0.02106805, 3.60949449, 0.07840497, -29.93071644, -0.00126413, -36.09494487, -0.02106805, -3.60949449, -0.07840497, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22018, 2018, 0.0, 84.33101055, 0.02528261, 84.33101055, 0.07584784, 59.03170738, -1469.36794296, 0.05, 2, 0, 72018, 23018, 2, 3)
    ops.uniaxialMaterial('LimitState', 42018, 21.08275264, 9.454e-05, 63.24825791, 0.00028363, 210.82752637, 0.00094544, -21.08275264, -9.454e-05, -63.24825791, -0.00028363, -210.82752637, -0.00094544, 0.4, 0.3, 0.003, 0.0, 0.0, 22018, 2)
    ops.limitCurve('ThreePoint', 12018, 2018, 0.0, 84.33101055, 0.02528261, 84.33101055, 0.07584784, 59.03170738, -1469.36794296, 0.05, 2, 0, 72018, 23018, 1, 3)
    ops.uniaxialMaterial('LimitState', 32018, 21.08275264, 9.454e-05, 63.24825791, 0.00028363, 210.82752637, 0.00094544, -21.08275264, -9.454e-05, -63.24825791, -0.00028363, -210.82752637, -0.00094544, 0.4, 0.3, 0.003, 0.0, 0.0, 12018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2018, 99999, 'P', 42018, 'Vy', 32018, 'Vz', 22018, 'My', 12018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172018, 72018, 172018, 2018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123018, 123018, 23018, 2018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173001, 0.0, 0.0, 9.4)
    ops.node(124001, 0.0, 0.0, 12.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3001, 173001, 124001, 0.0625, 34483736.1112569, 14368223.37969038, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23001, 23.65415319, 0.00112363, 28.31715323, 0.01701829, 2.83171532, 0.08194724, -23.65415319, -0.00112363, -28.31715323, -0.01701829, -2.83171532, -0.08194724, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13001, 23.65415319, 0.00112363, 28.31715323, 0.01701829, 2.83171532, 0.08194724, -23.65415319, -0.00112363, -28.31715323, -0.01701829, -2.83171532, -0.08194724, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23001, 3001, 0.0, 72.0386065, 0.02247265, 72.0386065, 0.06741794, 50.42702455, -2562.07197397, 0.05, 2, 0, 73001, 24001, 2, 3)
    ops.uniaxialMaterial('LimitState', 43001, 18.00965163, 7.34e-05, 54.02895488, 0.0002202, 180.09651625, 0.00073401, -18.00965163, -7.34e-05, -54.02895488, -0.0002202, -180.09651625, -0.00073401, 0.4, 0.3, 0.003, 0.0, 0.0, 23001, 2)
    ops.limitCurve('ThreePoint', 13001, 3001, 0.0, 72.0386065, 0.02247265, 72.0386065, 0.06741794, 50.42702455, -2562.07197397, 0.05, 2, 0, 73001, 24001, 1, 3)
    ops.uniaxialMaterial('LimitState', 33001, 18.00965163, 7.34e-05, 54.02895488, 0.0002202, 180.09651625, 0.00073401, -18.00965163, -7.34e-05, -54.02895488, -0.0002202, -180.09651625, -0.00073401, 0.4, 0.3, 0.003, 0.0, 0.0, 13001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3001, 99999, 'P', 43001, 'Vy', 33001, 'Vz', 23001, 'My', 13001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173001, 73001, 173001, 3001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124001, 124001, 24001, 3001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173002, 3.9, 0.0, 9.4)
    ops.node(124002, 3.9, 0.0, 11.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3002, 173002, 124002, 0.0625, 31381350.19339714, 13075562.58058214, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23002, 24.70466875, 0.00139402, 29.8639274, 0.01790137, 2.98639274, 0.0797201, -24.70466875, -0.00139402, -29.8639274, -0.01790137, -2.98639274, -0.0797201, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13002, 24.70466875, 0.00139402, 29.8639274, 0.01790137, 2.98639274, 0.0797201, -24.70466875, -0.00139402, -29.8639274, -0.01790137, -2.98639274, -0.0797201, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23002, 3002, 0.0, 68.87064107, 0.02788039, 68.87064107, 0.08364118, 48.20944875, -1606.06025769, 0.05, 2, 0, 73002, 24002, 2, 3)
    ops.uniaxialMaterial('LimitState', 43002, 17.21766027, 7.711e-05, 51.6529808, 0.00023133, 172.17660268, 0.00077111, -17.21766027, -7.711e-05, -51.6529808, -0.00023133, -172.17660268, -0.00077111, 0.4, 0.3, 0.003, 0.0, 0.0, 23002, 2)
    ops.limitCurve('ThreePoint', 13002, 3002, 0.0, 68.87064107, 0.02788039, 68.87064107, 0.08364118, 48.20944875, -1606.06025769, 0.05, 2, 0, 73002, 24002, 1, 3)
    ops.uniaxialMaterial('LimitState', 33002, 17.21766027, 7.711e-05, 51.6529808, 0.00023133, 172.17660268, 0.00077111, -17.21766027, -7.711e-05, -51.6529808, -0.00023133, -172.17660268, -0.00077111, 0.4, 0.3, 0.003, 0.0, 0.0, 13002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3002, 99999, 'P', 43002, 'Vy', 33002, 'Vz', 23002, 'My', 13002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173002, 73002, 173002, 3002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124002, 124002, 24002, 3002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173005, 14.7, 0.0, 9.4)
    ops.node(124005, 14.7, 0.0, 11.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3005, 173005, 124005, 0.0625, 28676680.34297918, 11948616.80957466, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23005, 26.00896305, 0.00125164, 31.6633439, 0.02122553, 3.16633439, 0.08134248, -26.00896305, -0.00125164, -31.6633439, -0.02122553, -3.16633439, -0.08134248, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13005, 26.00896305, 0.00125164, 31.6633439, 0.02122553, 3.16633439, 0.08134248, -26.00896305, -0.00125164, -31.6633439, -0.02122553, -3.16633439, -0.08134248, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23005, 3005, 0.0, 74.01285286, 0.02503277, 74.01285286, 0.0750983, 51.808997, -1940.05262245, 0.05, 2, 0, 73005, 24005, 2, 3)
    ops.uniaxialMaterial('LimitState', 43005, 18.50321321, 9.068e-05, 55.50963964, 0.00027205, 185.03213214, 0.00090684, -18.50321321, -9.068e-05, -55.50963964, -0.00027205, -185.03213214, -0.00090684, 0.4, 0.3, 0.003, 0.0, 0.0, 23005, 2)
    ops.limitCurve('ThreePoint', 13005, 3005, 0.0, 74.01285286, 0.02503277, 74.01285286, 0.0750983, 51.808997, -1940.05262245, 0.05, 2, 0, 73005, 24005, 1, 3)
    ops.uniaxialMaterial('LimitState', 33005, 18.50321321, 9.068e-05, 55.50963964, 0.00027205, 185.03213214, 0.00090684, -18.50321321, -9.068e-05, -55.50963964, -0.00027205, -185.03213214, -0.00090684, 0.4, 0.3, 0.003, 0.0, 0.0, 13005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3005, 99999, 'P', 43005, 'Vy', 33005, 'Vz', 23005, 'My', 13005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173005, 73005, 173005, 3005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124005, 124005, 24005, 3005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173006, 18.6, 0.0, 9.4)
    ops.node(124006, 18.6, 0.0, 12.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3006, 173006, 124006, 0.0625, 30540629.80366812, 12725262.41819505, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23006, 22.93989508, 0.0012256, 27.83622573, 0.0228162, 2.78362257, 0.08676234, -22.93989508, -0.0012256, -27.83622573, -0.0228162, -2.78362257, -0.08676234, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13006, 22.93989508, 0.0012256, 27.83622573, 0.0228162, 2.78362257, 0.08676234, -22.93989508, -0.0012256, -27.83622573, -0.0228162, -2.78362257, -0.08676234, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23006, 3006, 0.0, 80.06421114, 0.02451198, 80.06421114, 0.07353594, 56.0449478, -3746.20431782, 0.05, 2, 0, 73006, 24006, 2, 3)
    ops.uniaxialMaterial('LimitState', 43006, 20.01605278, 9.211e-05, 60.04815835, 0.00027633, 200.16052785, 0.00092111, -20.01605278, -9.211e-05, -60.04815835, -0.00027633, -200.16052785, -0.00092111, 0.4, 0.3, 0.003, 0.0, 0.0, 23006, 2)
    ops.limitCurve('ThreePoint', 13006, 3006, 0.0, 80.06421114, 0.02451198, 80.06421114, 0.07353594, 56.0449478, -3746.20431782, 0.05, 2, 0, 73006, 24006, 1, 3)
    ops.uniaxialMaterial('LimitState', 33006, 20.01605278, 9.211e-05, 60.04815835, 0.00027633, 200.16052785, 0.00092111, -20.01605278, -9.211e-05, -60.04815835, -0.00027633, -200.16052785, -0.00092111, 0.4, 0.3, 0.003, 0.0, 0.0, 13006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3006, 99999, 'P', 43006, 'Vy', 33006, 'Vz', 23006, 'My', 13006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173006, 73006, 173006, 3006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124006, 124006, 24006, 3006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173007, 0.0, 5.35, 9.4)
    ops.node(124007, 0.0, 5.35, 12.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3007, 173007, 124007, 0.0625, 33180308.59191259, 13825128.57996358, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23007, 26.11561017, 0.00122666, 31.38580591, 0.01944451, 3.13858059, 0.0821076, -26.11561017, -0.00122666, -31.38580591, -0.01944451, -3.13858059, -0.0821076, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13007, 26.11561017, 0.00122666, 31.38580591, 0.01944451, 3.13858059, 0.0821076, -26.11561017, -0.00122666, -31.38580591, -0.01944451, -3.13858059, -0.0821076, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23007, 3007, 0.0, 82.09760274, 0.02453325, 82.09760274, 0.07359976, 57.46832192, -1906.26484073, 0.05, 2, 0, 73007, 24007, 2, 3)
    ops.uniaxialMaterial('LimitState', 43007, 20.52440069, 8.694e-05, 61.57320206, 0.00026081, 205.24400685, 0.00086937, -20.52440069, -8.694e-05, -61.57320206, -0.00026081, -205.24400685, -0.00086937, 0.4, 0.3, 0.003, 0.0, 0.0, 23007, 2)
    ops.limitCurve('ThreePoint', 13007, 3007, 0.0, 82.09760274, 0.02453325, 82.09760274, 0.07359976, 57.46832192, -1906.26484073, 0.05, 2, 0, 73007, 24007, 1, 3)
    ops.uniaxialMaterial('LimitState', 33007, 20.52440069, 8.694e-05, 61.57320206, 0.00026081, 205.24400685, 0.00086937, -20.52440069, -8.694e-05, -61.57320206, -0.00026081, -205.24400685, -0.00086937, 0.4, 0.3, 0.003, 0.0, 0.0, 13007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3007, 99999, 'P', 43007, 'Vy', 33007, 'Vz', 23007, 'My', 13007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173007, 73007, 173007, 3007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124007, 124007, 24007, 3007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173008, 3.9, 5.35, 9.4)
    ops.node(124008, 3.9, 5.35, 11.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3008, 173008, 124008, 0.1225, 30732571.37929501, 12805238.07470626, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23008, 75.47974627, 0.0009911, 91.44904481, 0.01787995, 9.14490448, 0.06588263, -75.47974627, -0.0009911, -91.44904481, -0.01787995, -9.14490448, -0.06588263, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13008, 64.76780239, 0.0009911, 78.47076807, 0.01787995, 7.84707681, 0.06588263, -64.76780239, -0.0009911, -78.47076807, -0.01787995, -7.84707681, -0.06588263, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23008, 3008, 0.0, 129.07769629, 0.01982208, 129.07769629, 0.05946625, 90.3543874, -2382.59885769, 0.05, 2, 0, 73008, 24008, 2, 3)
    ops.uniaxialMaterial('LimitState', 43008, 32.26942407, 7.529e-05, 96.80827222, 0.00022588, 322.69424073, 0.00075292, -32.26942407, -7.529e-05, -96.80827222, -0.00022588, -322.69424073, -0.00075292, 0.4, 0.3, 0.003, 0.0, 0.0, 23008, 2)
    ops.limitCurve('ThreePoint', 13008, 3008, 0.0, 129.07769629, 0.01982208, 129.07769629, 0.05946625, 90.3543874, -2382.59885769, 0.05, 2, 0, 73008, 24008, 1, 3)
    ops.uniaxialMaterial('LimitState', 33008, 32.26942407, 7.529e-05, 96.80827222, 0.00022588, 322.69424073, 0.00075292, -32.26942407, -7.529e-05, -96.80827222, -0.00022588, -322.69424073, -0.00075292, 0.4, 0.3, 0.003, 0.0, 0.0, 13008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3008, 99999, 'P', 43008, 'Vy', 33008, 'Vz', 23008, 'My', 13008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173008, 73008, 173008, 3008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124008, 124008, 24008, 3008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173009, 7.8, 5.35, 9.4)
    ops.node(124009, 7.8, 5.35, 11.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3009, 173009, 124009, 0.1225, 27774971.16689382, 11572904.65287242, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23009, 74.0958657, 0.00092281, 90.418864, 0.02136878, 9.0418864, 0.06788873, -74.0958657, -0.00092281, -90.418864, -0.02136878, -9.0418864, -0.06788873, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13009, 62.37144424, 0.00092281, 76.11160327, 0.02136878, 7.61116033, 0.06788873, -62.37144424, -0.00092281, -76.11160327, -0.02136878, -7.61116033, -0.06788873, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23009, 3009, 0.0, 122.65035023, 0.01845617, 122.65035023, 0.05536852, 85.85524516, -2643.23976451, 0.05, 2, 0, 73009, 24009, 2, 3)
    ops.uniaxialMaterial('LimitState', 43009, 30.66258756, 7.916e-05, 91.98776267, 0.00023748, 306.62587557, 0.00079161, -30.66258756, -7.916e-05, -91.98776267, -0.00023748, -306.62587557, -0.00079161, 0.4, 0.3, 0.003, 0.0, 0.0, 23009, 2)
    ops.limitCurve('ThreePoint', 13009, 3009, 0.0, 122.65035023, 0.01845617, 122.65035023, 0.05536852, 85.85524516, -2643.23976451, 0.05, 2, 0, 73009, 24009, 1, 3)
    ops.uniaxialMaterial('LimitState', 33009, 30.66258756, 7.916e-05, 91.98776267, 0.00023748, 306.62587557, 0.00079161, -30.66258756, -7.916e-05, -91.98776267, -0.00023748, -306.62587557, -0.00079161, 0.4, 0.3, 0.003, 0.0, 0.0, 13009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3009, 99999, 'P', 43009, 'Vy', 33009, 'Vz', 23009, 'My', 13009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173009, 73009, 173009, 3009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124009, 124009, 24009, 3009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173010, 10.8, 5.35, 9.4)
    ops.node(124010, 10.8, 5.35, 11.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3010, 173010, 124010, 0.1225, 29920603.87423344, 12466918.2809306, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23010, 75.32576772, 0.00094767, 91.46154663, 0.01696164, 9.14615466, 0.0645722, -75.32576772, -0.00094767, -91.46154663, -0.01696164, -9.14615466, -0.0645722, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13010, 63.97153092, 0.00094767, 77.67508165, 0.01696164, 7.76750817, 0.0645722, -63.97153092, -0.00094767, -77.67508165, -0.01696164, -7.76750817, -0.0645722, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23010, 3010, 0.0, 122.47066911, 0.01895338, 122.47066911, 0.05686014, 85.72946838, -2114.04131511, 0.05, 2, 0, 73010, 24010, 2, 3)
    ops.uniaxialMaterial('LimitState', 43010, 30.61766728, 7.338e-05, 91.85300183, 0.00022013, 306.17667277, 0.00073377, -30.61766728, -7.338e-05, -91.85300183, -0.00022013, -306.17667277, -0.00073377, 0.4, 0.3, 0.003, 0.0, 0.0, 23010, 2)
    ops.limitCurve('ThreePoint', 13010, 3010, 0.0, 122.47066911, 0.01895338, 122.47066911, 0.05686014, 85.72946838, -2114.04131511, 0.05, 2, 0, 73010, 24010, 1, 3)
    ops.uniaxialMaterial('LimitState', 33010, 30.61766728, 7.338e-05, 91.85300183, 0.00022013, 306.17667277, 0.00073377, -30.61766728, -7.338e-05, -91.85300183, -0.00022013, -306.17667277, -0.00073377, 0.4, 0.3, 0.003, 0.0, 0.0, 13010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3010, 99999, 'P', 43010, 'Vy', 33010, 'Vz', 23010, 'My', 13010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173010, 73010, 173010, 3010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124010, 124010, 24010, 3010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173011, 14.7, 5.35, 9.4)
    ops.node(124011, 14.7, 5.35, 11.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3011, 173011, 124011, 0.1225, 28494389.09857085, 11872662.12440452, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23011, 74.34891701, 0.00096847, 90.59300742, 0.01760182, 9.05930074, 0.06459539, -74.34891701, -0.00096847, -90.59300742, -0.01760182, -9.05930074, -0.06459539, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13011, 63.22404587, 0.00096847, 77.03752369, 0.01760182, 7.70375237, 0.06459539, -63.22404587, -0.00096847, -77.03752369, -0.01760182, -7.70375237, -0.06459539, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23011, 3011, 0.0, 118.73535486, 0.01936941, 118.73535486, 0.05810824, 83.11474841, -2228.07174755, 0.05, 2, 0, 73011, 24011, 2, 3)
    ops.uniaxialMaterial('LimitState', 43011, 29.68383872, 7.47e-05, 89.05151615, 0.0002241, 296.83838716, 0.00074699, -29.68383872, -7.47e-05, -89.05151615, -0.0002241, -296.83838716, -0.00074699, 0.4, 0.3, 0.003, 0.0, 0.0, 23011, 2)
    ops.limitCurve('ThreePoint', 13011, 3011, 0.0, 118.73535486, 0.01936941, 118.73535486, 0.05810824, 83.11474841, -2228.07174755, 0.05, 2, 0, 73011, 24011, 1, 3)
    ops.uniaxialMaterial('LimitState', 33011, 29.68383872, 7.47e-05, 89.05151615, 0.0002241, 296.83838716, 0.00074699, -29.68383872, -7.47e-05, -89.05151615, -0.0002241, -296.83838716, -0.00074699, 0.4, 0.3, 0.003, 0.0, 0.0, 13011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3011, 99999, 'P', 43011, 'Vy', 33011, 'Vz', 23011, 'My', 13011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173011, 73011, 173011, 3011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124011, 124011, 24011, 3011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173012, 18.6, 5.35, 9.4)
    ops.node(124012, 18.6, 5.35, 12.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3012, 173012, 124012, 0.0625, 36225502.4401664, 15093959.35006933, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23012, 25.88050079, 0.00111428, 30.73059095, 0.01774305, 3.07305909, 0.08146586, -25.88050079, -0.00111428, -30.73059095, -0.01774305, -3.07305909, -0.08146586, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13012, 25.88050079, 0.00111428, 30.73059095, 0.01774305, 3.07305909, 0.08146586, -25.88050079, -0.00111428, -30.73059095, -0.01774305, -3.07305909, -0.08146586, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23012, 3012, 0.0, 86.46074281, 0.02228553, 86.46074281, 0.06685658, 60.52251997, -1761.00421779, 0.05, 2, 0, 73012, 24012, 2, 3)
    ops.uniaxialMaterial('LimitState', 43012, 21.6151857, 8.386e-05, 64.84555711, 0.00025158, 216.15185703, 0.0008386, -21.6151857, -8.386e-05, -64.84555711, -0.00025158, -216.15185703, -0.0008386, 0.4, 0.3, 0.003, 0.0, 0.0, 23012, 2)
    ops.limitCurve('ThreePoint', 13012, 3012, 0.0, 86.46074281, 0.02228553, 86.46074281, 0.06685658, 60.52251997, -1761.00421779, 0.05, 2, 0, 73012, 24012, 1, 3)
    ops.uniaxialMaterial('LimitState', 33012, 21.6151857, 8.386e-05, 64.84555711, 0.00025158, 216.15185703, 0.0008386, -21.6151857, -8.386e-05, -64.84555711, -0.00025158, -216.15185703, -0.0008386, 0.4, 0.3, 0.003, 0.0, 0.0, 13012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3012, 99999, 'P', 43012, 'Vy', 33012, 'Vz', 23012, 'My', 13012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173012, 73012, 173012, 3012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124012, 124012, 24012, 3012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173013, 0.0, 10.7, 9.4)
    ops.node(124013, 0.0, 10.7, 12.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3013, 173013, 124013, 0.0625, 34914939.33983225, 14547891.39159677, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23013, 23.91944874, 0.00122121, 28.58488879, 0.01711007, 2.85848888, 0.0821196, -23.91944874, -0.00122121, -28.58488879, -0.01711007, -2.85848888, -0.0821196, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13013, 23.91944874, 0.00122121, 28.58488879, 0.01711007, 2.85848888, 0.0821196, -23.91944874, -0.00122121, -28.58488879, -0.01711007, -2.85848888, -0.0821196, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23013, 3013, 0.0, 76.72314769, 0.0244242, 76.72314769, 0.07327259, 53.70620338, -2586.13966438, 0.05, 2, 0, 73013, 24013, 2, 3)
    ops.uniaxialMaterial('LimitState', 43013, 19.18078692, 7.721e-05, 57.54236076, 0.00023163, 191.80786922, 0.00077209, -19.18078692, -7.721e-05, -57.54236076, -0.00023163, -191.80786922, -0.00077209, 0.4, 0.3, 0.003, 0.0, 0.0, 23013, 2)
    ops.limitCurve('ThreePoint', 13013, 3013, 0.0, 76.72314769, 0.0244242, 76.72314769, 0.07327259, 53.70620338, -2586.13966438, 0.05, 2, 0, 73013, 24013, 1, 3)
    ops.uniaxialMaterial('LimitState', 33013, 19.18078692, 7.721e-05, 57.54236076, 0.00023163, 191.80786922, 0.00077209, -19.18078692, -7.721e-05, -57.54236076, -0.00023163, -191.80786922, -0.00077209, 0.4, 0.3, 0.003, 0.0, 0.0, 13013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3013, 99999, 'P', 43013, 'Vy', 33013, 'Vz', 23013, 'My', 13013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173013, 73013, 173013, 3013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124013, 124013, 24013, 3013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173014, 3.9, 10.7, 9.4)
    ops.node(124014, 3.9, 10.7, 11.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3014, 173014, 124014, 0.0625, 32789356.50358199, 13662231.87649249, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23014, 32.16604294, 0.00126298, 38.70929647, 0.01839357, 3.87092965, 0.08088615, -32.16604294, -0.00126298, -38.70929647, -0.01839357, -3.87092965, -0.08088615, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13014, 35.39059567, 0.00126298, 42.58979144, 0.01839357, 4.25897914, 0.08088615, -35.39059567, -0.00126298, -42.58979144, -0.01839357, -4.25897914, -0.08088615, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23014, 3014, 0.0, 73.80648369, 0.02525962, 73.80648369, 0.07577886, 51.66453858, -1636.47609856, 0.05, 2, 0, 73014, 24014, 2, 3)
    ops.uniaxialMaterial('LimitState', 43014, 18.45162092, 7.909e-05, 55.35486277, 0.00023727, 184.51620922, 0.00079089, -18.45162092, -7.909e-05, -55.35486277, -0.00023727, -184.51620922, -0.00079089, 0.4, 0.3, 0.003, 0.0, 0.0, 23014, 2)
    ops.limitCurve('ThreePoint', 13014, 3014, 0.0, 73.80648369, 0.02525962, 73.80648369, 0.07577886, 51.66453858, -1636.47609856, 0.05, 2, 0, 73014, 24014, 1, 3)
    ops.uniaxialMaterial('LimitState', 33014, 18.45162092, 7.909e-05, 55.35486277, 0.00023727, 184.51620922, 0.00079089, -18.45162092, -7.909e-05, -55.35486277, -0.00023727, -184.51620922, -0.00079089, 0.4, 0.3, 0.003, 0.0, 0.0, 13014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3014, 99999, 'P', 43014, 'Vy', 33014, 'Vz', 23014, 'My', 13014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173014, 73014, 173014, 3014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124014, 124014, 24014, 3014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173015, 7.8, 10.7, 9.4)
    ops.node(124015, 7.8, 10.7, 11.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3015, 173015, 124015, 0.0625, 31659380.94517132, 13191408.72715472, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23015, 30.26280583, 0.00128173, 36.56548827, 0.02246891, 3.65654883, 0.08511456, -30.26280583, -0.00128173, -36.56548827, -0.02246891, -3.65654883, -0.08511456, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13015, 33.08982873, 0.00128173, 39.98128102, 0.02246891, 3.9981281, 0.08511456, -33.08982873, -0.00128173, -39.98128102, -0.02246891, -3.9981281, -0.08511456, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23015, 3015, 0.0, 80.05611408, 0.02563464, 80.05611408, 0.07690392, 56.03927986, -2242.36411237, 0.05, 2, 0, 73015, 24015, 2, 3)
    ops.uniaxialMaterial('LimitState', 43015, 20.01402852, 8.885e-05, 60.04208556, 0.00026654, 200.1402852, 0.00088847, -20.01402852, -8.885e-05, -60.04208556, -0.00026654, -200.1402852, -0.00088847, 0.4, 0.3, 0.003, 0.0, 0.0, 23015, 2)
    ops.limitCurve('ThreePoint', 13015, 3015, 0.0, 80.05611408, 0.02563464, 80.05611408, 0.07690392, 56.03927986, -2242.36411237, 0.05, 2, 0, 73015, 24015, 1, 3)
    ops.uniaxialMaterial('LimitState', 33015, 20.01402852, 8.885e-05, 60.04208556, 0.00026654, 200.1402852, 0.00088847, -20.01402852, -8.885e-05, -60.04208556, -0.00026654, -200.1402852, -0.00088847, 0.4, 0.3, 0.003, 0.0, 0.0, 13015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3015, 99999, 'P', 43015, 'Vy', 33015, 'Vz', 23015, 'My', 13015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173015, 73015, 173015, 3015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124015, 124015, 24015, 3015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173016, 10.8, 10.7, 9.4)
    ops.node(124016, 10.8, 10.7, 11.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3016, 173016, 124016, 0.0625, 32553738.24122203, 13564057.60050918, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23016, 31.77843981, 0.00125757, 38.28595842, 0.02262346, 3.82859584, 0.08563889, -31.77843981, -0.00125757, -38.28595842, -0.02262346, -3.82859584, -0.08563889, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13016, 35.08569526, 0.00125757, 42.27046634, 0.02262346, 4.22704663, 0.08563889, -35.08569526, -0.00125757, -42.27046634, -0.02262346, -4.22704663, -0.08563889, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23016, 3016, 0.0, 84.4592363, 0.02515142, 84.4592363, 0.07545425, 59.12146541, -2500.33764901, 0.05, 2, 0, 73016, 24016, 2, 3)
    ops.uniaxialMaterial('LimitState', 43016, 21.11480907, 9.116e-05, 63.34442722, 0.00027348, 211.14809074, 0.00091159, -21.11480907, -9.116e-05, -63.34442722, -0.00027348, -211.14809074, -0.00091159, 0.4, 0.3, 0.003, 0.0, 0.0, 23016, 2)
    ops.limitCurve('ThreePoint', 13016, 3016, 0.0, 84.4592363, 0.02515142, 84.4592363, 0.07545425, 59.12146541, -2500.33764901, 0.05, 2, 0, 73016, 24016, 1, 3)
    ops.uniaxialMaterial('LimitState', 33016, 21.11480907, 9.116e-05, 63.34442722, 0.00027348, 211.14809074, 0.00091159, -21.11480907, -9.116e-05, -63.34442722, -0.00027348, -211.14809074, -0.00091159, 0.4, 0.3, 0.003, 0.0, 0.0, 13016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3016, 99999, 'P', 43016, 'Vy', 33016, 'Vz', 23016, 'My', 13016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173016, 73016, 173016, 3016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124016, 124016, 24016, 3016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173017, 14.7, 10.7, 9.4)
    ops.node(124017, 14.7, 10.7, 11.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3017, 173017, 124017, 0.0625, 29433028.67200749, 12263761.94666979, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23017, 31.9579364, 0.00127612, 38.83688945, 0.02196867, 3.88368894, 0.08262554, -31.9579364, -0.00127612, -38.83688945, -0.02196867, -3.88368894, -0.08262554, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13017, 35.40420299, 0.00127612, 43.02496569, 0.02196867, 4.30249657, 0.08262554, -35.40420299, -0.00127612, -43.02496569, -0.02196867, -4.30249657, -0.08262554, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23017, 3017, 0.0, 75.53212865, 0.02552246, 75.53212865, 0.07656739, 52.87249006, -1951.76150892, 0.05, 2, 0, 73017, 24017, 2, 3)
    ops.uniaxialMaterial('LimitState', 43017, 18.88303216, 9.017e-05, 56.64909649, 0.0002705, 188.83032163, 0.00090167, -18.88303216, -9.017e-05, -56.64909649, -0.0002705, -188.83032163, -0.00090167, 0.4, 0.3, 0.003, 0.0, 0.0, 23017, 2)
    ops.limitCurve('ThreePoint', 13017, 3017, 0.0, 75.53212865, 0.02552246, 75.53212865, 0.07656739, 52.87249006, -1951.76150892, 0.05, 2, 0, 73017, 24017, 1, 3)
    ops.uniaxialMaterial('LimitState', 33017, 18.88303216, 9.017e-05, 56.64909649, 0.0002705, 188.83032163, 0.00090167, -18.88303216, -9.017e-05, -56.64909649, -0.0002705, -188.83032163, -0.00090167, 0.4, 0.3, 0.003, 0.0, 0.0, 13017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3017, 99999, 'P', 43017, 'Vy', 33017, 'Vz', 23017, 'My', 13017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173017, 73017, 173017, 3017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124017, 124017, 24017, 3017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173018, 18.6, 10.7, 9.4)
    ops.node(124018, 18.6, 10.7, 12.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3018, 173018, 124018, 0.0625, 30170868.96795686, 12571195.40331536, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23018, 23.20802269, 0.00119319, 28.19134369, 0.01890165, 2.81913437, 0.08272649, -23.20802269, -0.00119319, -28.19134369, -0.01890165, -2.81913437, -0.08272649, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13018, 23.20802269, 0.00119319, 28.19134369, 0.01890165, 2.81913437, 0.08272649, -23.20802269, -0.00119319, -28.19134369, -0.01890165, -2.81913437, -0.08272649, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23018, 3018, 0.0, 64.35207673, 0.02386388, 64.35207673, 0.07159164, 45.04645371, -2410.82297391, 0.05, 2, 0, 73018, 24018, 2, 3)
    ops.uniaxialMaterial('LimitState', 43018, 16.08801918, 7.494e-05, 48.26405755, 0.00022483, 160.88019182, 0.00074942, -16.08801918, -7.494e-05, -48.26405755, -0.00022483, -160.88019182, -0.00074942, 0.4, 0.3, 0.003, 0.0, 0.0, 23018, 2)
    ops.limitCurve('ThreePoint', 13018, 3018, 0.0, 64.35207673, 0.02386388, 64.35207673, 0.07159164, 45.04645371, -2410.82297391, 0.05, 2, 0, 73018, 24018, 1, 3)
    ops.uniaxialMaterial('LimitState', 33018, 16.08801918, 7.494e-05, 48.26405755, 0.00022483, 160.88019182, 0.00074942, -16.08801918, -7.494e-05, -48.26405755, -0.00022483, -160.88019182, -0.00074942, 0.4, 0.3, 0.003, 0.0, 0.0, 13018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3018, 99999, 'P', 43018, 'Vy', 33018, 'Vz', 23018, 'My', 13018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173018, 73018, 173018, 3018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124018, 124018, 24018, 3018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170003, 7.8, 0.0, 0.0)
    ops.node(124019, 7.8, 0.0, 1.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4046, 170003, 124019, 0.1225, 31286074.76146504, 13035864.48394377, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24046, 128.94199269, 0.00074485, 154.80596257, 0.04060475, 15.48059626, 0.12206247, -128.94199269, -0.00074485, -154.80596257, -0.04060475, -15.48059626, -0.12206247, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14046, 116.71297639, 0.00074485, 140.12397574, 0.04060475, 14.01239757, 0.12206247, -116.71297639, -0.00074485, -140.12397574, -0.04060475, -14.01239757, -0.12206247, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24046, 4046, 0.0, 267.8598308, 0.01489703, 267.8598308, 0.04469109, 187.50188156, -8463.3393036, 0.05, 2, 0, 70003, 24019, 2, 3)
    ops.uniaxialMaterial('LimitState', 44046, 66.9649577, 7.674e-05, 200.8948731, 0.00023022, 669.64957699, 0.0007674, -66.9649577, -7.674e-05, -200.8948731, -0.00023022, -669.64957699, -0.0007674, 0.4, 0.3, 0.003, 0.0, 0.0, 24046, 2)
    ops.limitCurve('ThreePoint', 14046, 4046, 0.0, 267.8598308, 0.01489703, 267.8598308, 0.04469109, 187.50188156, -8463.3393036, 0.05, 2, 0, 70003, 24019, 1, 3)
    ops.uniaxialMaterial('LimitState', 34046, 66.9649577, 7.674e-05, 200.8948731, 0.00023022, 669.64957699, 0.0007674, -66.9649577, -7.674e-05, -200.8948731, -0.00023022, -669.64957699, -0.0007674, 0.4, 0.3, 0.003, 0.0, 0.0, 14046, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4046, 99999, 'P', 44046, 'Vy', 34046, 'Vz', 24046, 'My', 14046, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170003, 70003, 170003, 4046, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124019, 124019, 24019, 4046, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174019, 7.8, 0.0, 1.725)
    ops.node(121003, 7.8, 0.0, 2.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4047, 174019, 121003, 0.1225, 30493132.69180626, 12705471.95491927, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24047, 100.37792331, 0.00077585, 120.82112662, 0.04235747, 12.08211266, 0.12395492, -100.37792331, -0.00077585, -120.82112662, -0.04235747, -12.08211266, -0.12395492, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14047, 90.16065877, 0.00077585, 108.52299002, 0.04235747, 10.852299, 0.12395492, -90.16065877, -0.00077585, -108.52299002, -0.04235747, -10.852299, -0.12395492, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24047, 4047, 0.0, 271.4777492, 0.01551699, 271.4777492, 0.04655096, 190.03442444, -9828.59622137, 0.05, 2, 0, 74019, 21003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44047, 67.8694373, 7.98e-05, 203.6083119, 0.0002394, 678.694373, 0.00079799, -67.8694373, -7.98e-05, -203.6083119, -0.0002394, -678.694373, -0.00079799, 0.4, 0.3, 0.003, 0.0, 0.0, 24047, 2)
    ops.limitCurve('ThreePoint', 14047, 4047, 0.0, 271.4777492, 0.01551699, 271.4777492, 0.04655096, 190.03442444, -9828.59622137, 0.05, 2, 0, 74019, 21003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34047, 67.8694373, 7.98e-05, 203.6083119, 0.0002394, 678.694373, 0.00079799, -67.8694373, -7.98e-05, -203.6083119, -0.0002394, -678.694373, -0.00079799, 0.4, 0.3, 0.003, 0.0, 0.0, 14047, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4047, 99999, 'P', 44047, 'Vy', 34047, 'Vz', 24047, 'My', 14047, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174019, 74019, 174019, 4047, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121003, 121003, 21003, 4047, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170004, 10.8, 0.0, 0.0)
    ops.node(124020, 10.8, 0.0, 1.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4048, 170004, 124020, 0.1225, 28169917.09349846, 11737465.45562436, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24048, 127.78242433, 0.00082359, 154.1650757, 0.0403548, 15.41650757, 0.11240577, -127.78242433, -0.00082359, -154.1650757, -0.0403548, -15.41650757, -0.11240577, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14048, 116.23315106, 0.00082359, 140.23127693, 0.0403548, 14.02312769, 0.11240577, -116.23315106, -0.00082359, -140.23127693, -0.0403548, -14.02312769, -0.11240577, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24048, 4048, 0.0, 249.34842784, 0.01647177, 249.34842784, 0.04941531, 174.54389949, -8371.29803731, 0.05, 2, 0, 70004, 24020, 2, 3)
    ops.uniaxialMaterial('LimitState', 44048, 62.33710696, 7.934e-05, 187.01132088, 0.00023802, 623.37106961, 0.00079339, -62.33710696, -7.934e-05, -187.01132088, -0.00023802, -623.37106961, -0.00079339, 0.4, 0.3, 0.003, 0.0, 0.0, 24048, 2)
    ops.limitCurve('ThreePoint', 14048, 4048, 0.0, 249.34842784, 0.01647177, 249.34842784, 0.04941531, 174.54389949, -8371.29803731, 0.05, 2, 0, 70004, 24020, 1, 3)
    ops.uniaxialMaterial('LimitState', 34048, 62.33710696, 7.934e-05, 187.01132088, 0.00023802, 623.37106961, 0.00079339, -62.33710696, -7.934e-05, -187.01132088, -0.00023802, -623.37106961, -0.00079339, 0.4, 0.3, 0.003, 0.0, 0.0, 14048, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4048, 99999, 'P', 44048, 'Vy', 34048, 'Vz', 24048, 'My', 14048, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170004, 70004, 170004, 4048, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124020, 124020, 24020, 4048, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174020, 10.8, 0.0, 1.725)
    ops.node(121004, 10.8, 0.0, 2.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4049, 174020, 121004, 0.1225, 35409311.70032092, 14753879.87513372, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24049, 106.04701056, 0.00072272, 125.83904981, 0.0383636, 12.58390498, 0.12984484, -106.04701056, -0.00072272, -125.83904981, -0.0383636, -12.58390498, -0.12984484, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14049, 94.17840046, 0.00072272, 111.75534664, 0.0383636, 11.17553466, 0.12984484, -94.17840046, -0.00072272, -111.75534664, -0.0383636, -11.17553466, -0.12984484, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24049, 4049, 0.0, 293.97591485, 0.01445433, 293.97591485, 0.04336299, 205.7831404, -9187.74767392, 0.05, 2, 0, 74020, 21004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44049, 73.49397871, 7.442e-05, 220.48193614, 0.00022325, 734.93978713, 0.00074415, -73.49397871, -7.442e-05, -220.48193614, -0.00022325, -734.93978713, -0.00074415, 0.4, 0.3, 0.003, 0.0, 0.0, 24049, 2)
    ops.limitCurve('ThreePoint', 14049, 4049, 0.0, 293.97591485, 0.01445433, 293.97591485, 0.04336299, 205.7831404, -9187.74767392, 0.05, 2, 0, 74020, 21004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34049, 73.49397871, 7.442e-05, 220.48193614, 0.00022325, 734.93978713, 0.00074415, -73.49397871, -7.442e-05, -220.48193614, -0.00022325, -734.93978713, -0.00074415, 0.4, 0.3, 0.003, 0.0, 0.0, 14049, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4049, 99999, 'P', 44049, 'Vy', 34049, 'Vz', 24049, 'My', 14049, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174020, 74020, 174020, 4049, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121004, 121004, 21004, 4049, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171003, 7.8, 0.0, 3.3)
    ops.node(124021, 7.8, 0.0, 4.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4051, 171003, 124021, 0.1225, 30898239.49953636, 12874266.45814015, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24051, 94.27095603, 0.00072916, 113.5812879, 0.03088592, 11.35812879, 0.09250835, -94.27095603, -0.00072916, -113.5812879, -0.03088592, -11.35812879, -0.09250835, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14051, 83.04472478, 0.00072916, 100.05549102, 0.03088592, 10.0055491, 0.09250835, -83.04472478, -0.00072916, -100.05549102, -0.03088592, -10.0055491, -0.09250835, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24051, 4051, 0.0, 229.69131645, 0.01458327, 229.69131645, 0.04374981, 160.78392152, -6826.64582126, 0.05, 2, 0, 71003, 24021, 2, 3)
    ops.uniaxialMaterial('LimitState', 44051, 57.42282911, 6.663e-05, 172.26848734, 0.00019989, 574.22829113, 0.00066631, -57.42282911, -6.663e-05, -172.26848734, -0.00019989, -574.22829113, -0.00066631, 0.4, 0.3, 0.003, 0.0, 0.0, 24051, 2)
    ops.limitCurve('ThreePoint', 14051, 4051, 0.0, 229.69131645, 0.01458327, 229.69131645, 0.04374981, 160.78392152, -6826.64582126, 0.05, 2, 0, 71003, 24021, 1, 3)
    ops.uniaxialMaterial('LimitState', 34051, 57.42282911, 6.663e-05, 172.26848734, 0.00019989, 574.22829113, 0.00066631, -57.42282911, -6.663e-05, -172.26848734, -0.00019989, -574.22829113, -0.00066631, 0.4, 0.3, 0.003, 0.0, 0.0, 14051, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4051, 99999, 'P', 44051, 'Vy', 34051, 'Vz', 24051, 'My', 14051, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171003, 71003, 171003, 4051, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124021, 124021, 24021, 4051, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174021, 7.8, 0.0, 4.775)
    ops.node(122003, 7.8, 0.0, 5.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4052, 174021, 122003, 0.1225, 31191729.16530515, 12996553.81887715, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24052, 94.84958194, 0.00073762, 114.29729329, 0.028578, 11.42972933, 0.09225773, -94.84958194, -0.00073762, -114.29729329, -0.028578, -11.42972933, -0.09225773, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14052, 82.48942998, 0.00073762, 99.40284796, 0.028578, 9.9402848, 0.09225773, -82.48942998, -0.00073762, -99.40284796, -0.028578, -9.9402848, -0.09225773, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24052, 4052, 0.0, 214.2024986, 0.01475244, 214.2024986, 0.04425732, 149.94174902, -5816.23307238, 0.05, 2, 0, 74021, 22003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44052, 53.55062465, 6.155e-05, 160.65187395, 0.00018466, 535.50624649, 0.00061553, -53.55062465, -6.155e-05, -160.65187395, -0.00018466, -535.50624649, -0.00061553, 0.4, 0.3, 0.003, 0.0, 0.0, 24052, 2)
    ops.limitCurve('ThreePoint', 14052, 4052, 0.0, 214.2024986, 0.01475244, 214.2024986, 0.04425732, 149.94174902, -5816.23307238, 0.05, 2, 0, 74021, 22003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34052, 53.55062465, 6.155e-05, 160.65187395, 0.00018466, 535.50624649, 0.00061553, -53.55062465, -6.155e-05, -160.65187395, -0.00018466, -535.50624649, -0.00061553, 0.4, 0.3, 0.003, 0.0, 0.0, 14052, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4052, 99999, 'P', 44052, 'Vy', 34052, 'Vz', 24052, 'My', 14052, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174021, 74021, 174021, 4052, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122003, 122003, 22003, 4052, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171004, 10.8, 0.0, 3.3)
    ops.node(124022, 10.8, 0.0, 4.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4053, 171004, 124022, 0.1225, 30328327.43030292, 12636803.09595955, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24053, 93.8218472, 0.00074029, 113.18473135, 0.03095987, 11.31847313, 0.09170208, -93.8218472, -0.00074029, -113.18473135, -0.03095987, -11.31847313, -0.09170208, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14053, 82.80343456, 0.00074029, 99.89234677, 0.03095987, 9.98923468, 0.09170208, -82.80343456, -0.00074029, -99.89234677, -0.03095987, -9.98923468, -0.09170208, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24053, 4053, 0.0, 222.43002102, 0.01480589, 222.43002102, 0.04441766, 155.70101471, -6449.47211449, 0.05, 2, 0, 71004, 24022, 2, 3)
    ops.uniaxialMaterial('LimitState', 44053, 55.60750525, 6.574e-05, 166.82251576, 0.00019721, 556.07505254, 0.00065737, -55.60750525, -6.574e-05, -166.82251576, -0.00019721, -556.07505254, -0.00065737, 0.4, 0.3, 0.003, 0.0, 0.0, 24053, 2)
    ops.limitCurve('ThreePoint', 14053, 4053, 0.0, 222.43002102, 0.01480589, 222.43002102, 0.04441766, 155.70101471, -6449.47211449, 0.05, 2, 0, 71004, 24022, 1, 3)
    ops.uniaxialMaterial('LimitState', 34053, 55.60750525, 6.574e-05, 166.82251576, 0.00019721, 556.07505254, 0.00065737, -55.60750525, -6.574e-05, -166.82251576, -0.00019721, -556.07505254, -0.00065737, 0.4, 0.3, 0.003, 0.0, 0.0, 14053, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4053, 99999, 'P', 44053, 'Vy', 34053, 'Vz', 24053, 'My', 14053, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171004, 71004, 171004, 4053, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124022, 124022, 24022, 4053, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174022, 10.8, 0.0, 4.775)
    ops.node(122004, 10.8, 0.0, 5.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4054, 174022, 122004, 0.1225, 29991180.37062142, 12496325.15442559, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24054, 89.7950625, 0.00074872, 108.51017571, 0.03111871, 10.85101757, 0.09311325, -89.7950625, -0.00074872, -108.51017571, -0.03111871, -10.85101757, -0.09311325, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14054, 79.09384093, 0.00074872, 95.57860241, 0.03111871, 9.55786024, 0.09311325, -79.09384093, -0.00074872, -95.57860241, -0.03111871, -9.55786024, -0.09311325, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24054, 4054, 0.0, 212.76587462, 0.01497445, 212.76587462, 0.04492334, 148.93611223, -6306.23532013, 0.05, 2, 0, 74022, 22004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44054, 53.19146865, 6.359e-05, 159.57440596, 0.00019076, 531.91468655, 0.00063588, -53.19146865, -6.359e-05, -159.57440596, -0.00019076, -531.91468655, -0.00063588, 0.4, 0.3, 0.003, 0.0, 0.0, 24054, 2)
    ops.limitCurve('ThreePoint', 14054, 4054, 0.0, 212.76587462, 0.01497445, 212.76587462, 0.04492334, 148.93611223, -6306.23532013, 0.05, 2, 0, 74022, 22004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34054, 53.19146865, 6.359e-05, 159.57440596, 0.00019076, 531.91468655, 0.00063588, -53.19146865, -6.359e-05, -159.57440596, -0.00019076, -531.91468655, -0.00063588, 0.4, 0.3, 0.003, 0.0, 0.0, 14054, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4054, 99999, 'P', 44054, 'Vy', 34054, 'Vz', 24054, 'My', 14054, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174022, 74022, 174022, 4054, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122004, 122004, 22004, 4054, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172003, 7.8, 0.0, 6.35)
    ops.node(124023, 7.8, 0.0, 7.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4056, 172003, 124023, 0.0625, 30639966.19199067, 12766652.57999611, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24056, 37.13180384, 0.00095131, 44.67503401, 0.03388832, 4.4675034, 0.1107386, -37.13180384, -0.00095131, -44.67503401, -0.03388832, -4.4675034, -0.1107386, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14056, 37.13180384, 0.00095131, 44.67503401, 0.03388832, 4.4675034, 0.1107386, -37.13180384, -0.00095131, -44.67503401, -0.03388832, -4.4675034, -0.1107386, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24056, 4056, 0.0, 117.85548678, 0.01902621, 117.85548678, 0.05707862, 82.49884075, -4854.56322394, 0.05, 2, 0, 72003, 24023, 2, 3)
    ops.uniaxialMaterial('LimitState', 44056, 29.46387169, 6.757e-05, 88.39161508, 0.00020272, 294.63871695, 0.00067575, -29.46387169, -6.757e-05, -88.39161508, -0.00020272, -294.63871695, -0.00067575, 0.4, 0.3, 0.003, 0.0, 0.0, 24056, 2)
    ops.limitCurve('ThreePoint', 14056, 4056, 0.0, 117.85548678, 0.01902621, 117.85548678, 0.05707862, 82.49884075, -4854.56322394, 0.05, 2, 0, 72003, 24023, 1, 3)
    ops.uniaxialMaterial('LimitState', 34056, 29.46387169, 6.757e-05, 88.39161508, 0.00020272, 294.63871695, 0.00067575, -29.46387169, -6.757e-05, -88.39161508, -0.00020272, -294.63871695, -0.00067575, 0.4, 0.3, 0.003, 0.0, 0.0, 14056, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4056, 99999, 'P', 44056, 'Vy', 34056, 'Vz', 24056, 'My', 14056, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172003, 72003, 172003, 4056, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124023, 124023, 24023, 4056, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174023, 7.8, 0.0, 7.825)
    ops.node(123003, 7.8, 0.0, 8.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4057, 174023, 123003, 0.0625, 33025542.08895647, 13760642.5370652, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24057, 34.19552325, 0.00093019, 40.96339286, 0.03192682, 4.09633929, 0.11779274, -34.19552325, -0.00093019, -40.96339286, -0.03192682, -4.09633929, -0.11779274, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14057, 34.19552325, 0.00093019, 40.96339286, 0.03192682, 4.09633929, 0.11779274, -34.19552325, -0.00093019, -40.96339286, -0.03192682, -4.09633929, -0.11779274, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24057, 4057, 0.0, 113.82513412, 0.01860387, 113.82513412, 0.05581162, 79.67759388, -4633.96070715, 0.05, 2, 0, 74023, 23003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44057, 28.45628353, 6.055e-05, 85.36885059, 0.00018165, 284.5628353, 0.00060549, -28.45628353, -6.055e-05, -85.36885059, -0.00018165, -284.5628353, -0.00060549, 0.4, 0.3, 0.003, 0.0, 0.0, 24057, 2)
    ops.limitCurve('ThreePoint', 14057, 4057, 0.0, 113.82513412, 0.01860387, 113.82513412, 0.05581162, 79.67759388, -4633.96070715, 0.05, 2, 0, 74023, 23003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34057, 28.45628353, 6.055e-05, 85.36885059, 0.00018165, 284.5628353, 0.00060549, -28.45628353, -6.055e-05, -85.36885059, -0.00018165, -284.5628353, -0.00060549, 0.4, 0.3, 0.003, 0.0, 0.0, 14057, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4057, 99999, 'P', 44057, 'Vy', 34057, 'Vz', 24057, 'My', 14057, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174023, 74023, 174023, 4057, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123003, 123003, 23003, 4057, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172004, 10.8, 0.0, 6.35)
    ops.node(124024, 10.8, 0.0, 7.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4058, 172004, 124024, 0.0625, 32380365.31471355, 13491818.88113065, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24058, 37.40640589, 0.00099254, 44.82068824, 0.03179897, 4.48206882, 0.11249955, -37.40640589, -0.00099254, -44.82068824, -0.03179897, -4.48206882, -0.11249955, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14058, 37.40640589, 0.00099254, 44.82068824, 0.03179897, 4.48206882, 0.11249955, -37.40640589, -0.00099254, -44.82068824, -0.03179897, -4.48206882, -0.11249955, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24058, 4058, 0.0, 119.8781215, 0.01985074, 119.8781215, 0.05955222, 83.91468505, -4695.62389959, 0.05, 2, 0, 72004, 24024, 2, 3)
    ops.uniaxialMaterial('LimitState', 44058, 29.96953037, 6.504e-05, 89.90859112, 0.00019512, 299.69530374, 0.0006504, -29.96953037, -6.504e-05, -89.90859112, -0.00019512, -299.69530374, -0.0006504, 0.4, 0.3, 0.003, 0.0, 0.0, 24058, 2)
    ops.limitCurve('ThreePoint', 14058, 4058, 0.0, 119.8781215, 0.01985074, 119.8781215, 0.05955222, 83.91468505, -4695.62389959, 0.05, 2, 0, 72004, 24024, 1, 3)
    ops.uniaxialMaterial('LimitState', 34058, 29.96953037, 6.504e-05, 89.90859112, 0.00019512, 299.69530374, 0.0006504, -29.96953037, -6.504e-05, -89.90859112, -0.00019512, -299.69530374, -0.0006504, 0.4, 0.3, 0.003, 0.0, 0.0, 14058, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4058, 99999, 'P', 44058, 'Vy', 34058, 'Vz', 24058, 'My', 14058, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172004, 72004, 172004, 4058, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124024, 124024, 24024, 4058, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174024, 10.8, 0.0, 7.825)
    ops.node(123004, 10.8, 0.0, 8.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4059, 174024, 123004, 0.0625, 30602999.13451618, 12751249.63938174, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24059, 33.59491155, 0.00094696, 40.50429649, 0.03257369, 4.05042965, 0.114092, -33.59491155, -0.00094696, -40.50429649, -0.03257369, -4.05042965, -0.114092, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14059, 33.59491155, 0.00094696, 40.50429649, 0.03257369, 4.05042965, 0.114092, -33.59491155, -0.00094696, -40.50429649, -0.03257369, -4.05042965, -0.114092, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24059, 4059, 0.0, 107.95502609, 0.01893911, 107.95502609, 0.05681733, 75.56851826, -4543.90362984, 0.05, 2, 0, 74024, 23004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44059, 26.98875652, 6.197e-05, 80.96626957, 0.00018592, 269.88756523, 0.00061973, -26.98875652, -6.197e-05, -80.96626957, -0.00018592, -269.88756523, -0.00061973, 0.4, 0.3, 0.003, 0.0, 0.0, 24059, 2)
    ops.limitCurve('ThreePoint', 14059, 4059, 0.0, 107.95502609, 0.01893911, 107.95502609, 0.05681733, 75.56851826, -4543.90362984, 0.05, 2, 0, 74024, 23004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34059, 26.98875652, 6.197e-05, 80.96626957, 0.00018592, 269.88756523, 0.00061973, -26.98875652, -6.197e-05, -80.96626957, -0.00018592, -269.88756523, -0.00061973, 0.4, 0.3, 0.003, 0.0, 0.0, 14059, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4059, 99999, 'P', 44059, 'Vy', 34059, 'Vz', 24059, 'My', 14059, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174024, 74024, 174024, 4059, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123004, 123004, 23004, 4059, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173003, 7.8, 0.0, 9.4)
    ops.node(124025, 7.8, 0.0, 10.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4061, 173003, 124025, 0.0625, 27276067.01378705, 11365027.92241127, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24061, 26.51497814, 0.00096256, 32.33810048, 0.02317869, 3.23381005, 0.08034269, -26.51497814, -0.00096256, -32.33810048, -0.02317869, -3.23381005, -0.08034269, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14061, 26.51497814, 0.00096256, 32.33810048, 0.02317869, 3.23381005, 0.08034269, -26.51497814, -0.00096256, -32.33810048, -0.02317869, -3.23381005, -0.08034269, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24061, 4061, 0.0, 79.70398614, 0.01925116, 79.70398614, 0.05775349, 55.7927903, -4213.56791597, 0.05, 2, 0, 73003, 24025, 2, 3)
    ops.uniaxialMaterial('LimitState', 44061, 19.92599654, 5.134e-05, 59.77798961, 0.00015401, 199.25996536, 0.00051336, -19.92599654, -5.134e-05, -59.77798961, -0.00015401, -199.25996536, -0.00051336, 0.4, 0.3, 0.003, 0.0, 0.0, 24061, 2)
    ops.limitCurve('ThreePoint', 14061, 4061, 0.0, 79.70398614, 0.01925116, 79.70398614, 0.05775349, 55.7927903, -4213.56791597, 0.05, 2, 0, 73003, 24025, 1, 3)
    ops.uniaxialMaterial('LimitState', 34061, 19.92599654, 5.134e-05, 59.77798961, 0.00015401, 199.25996536, 0.00051336, -19.92599654, -5.134e-05, -59.77798961, -0.00015401, -199.25996536, -0.00051336, 0.4, 0.3, 0.003, 0.0, 0.0, 14061, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4061, 99999, 'P', 44061, 'Vy', 34061, 'Vz', 24061, 'My', 14061, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173003, 73003, 173003, 4061, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124025, 124025, 24025, 4061, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174025, 7.8, 0.0, 10.85)
    ops.node(124003, 7.8, 0.0, 11.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4062, 174025, 124003, 0.0625, 32769380.76241527, 13653908.65100636, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24062, 23.3921867, 0.00081662, 28.18177307, 0.02016158, 2.81817731, 0.08460749, -23.3921867, -0.00081662, -28.18177307, -0.02016158, -2.81817731, -0.08460749, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14062, 23.3921867, 0.00081662, 28.18177307, 0.02016158, 2.81817731, 0.08460749, -23.3921867, -0.00081662, -28.18177307, -0.02016158, -2.81817731, -0.08460749, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24062, 4062, 0.0, 82.01004422, 0.01633243, 82.01004422, 0.04899728, 57.40703096, -5948.29259363, 0.05, 2, 0, 74025, 24003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44062, 20.50251106, 4.397e-05, 61.50753317, 0.0001319, 205.02511056, 0.00043966, -20.50251106, -4.397e-05, -61.50753317, -0.0001319, -205.02511056, -0.00043966, 0.4, 0.3, 0.003, 0.0, 0.0, 24062, 2)
    ops.limitCurve('ThreePoint', 14062, 4062, 0.0, 82.01004422, 0.01633243, 82.01004422, 0.04899728, 57.40703096, -5948.29259363, 0.05, 2, 0, 74025, 24003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34062, 20.50251106, 4.397e-05, 61.50753317, 0.0001319, 205.02511056, 0.00043966, -20.50251106, -4.397e-05, -61.50753317, -0.0001319, -205.02511056, -0.00043966, 0.4, 0.3, 0.003, 0.0, 0.0, 14062, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4062, 99999, 'P', 44062, 'Vy', 34062, 'Vz', 24062, 'My', 14062, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174025, 74025, 174025, 4062, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124003, 124003, 24003, 4062, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173004, 10.8, 0.0, 9.4)
    ops.node(124026, 10.8, 0.0, 10.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4063, 173004, 124026, 0.0625, 30044257.62528654, 12518440.67720272, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24063, 26.34258644, 0.00094155, 31.93945195, 0.02239044, 3.1939452, 0.0820962, -26.34258644, -0.00094155, -31.93945195, -0.02239044, -3.1939452, -0.0820962, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14063, 26.34258644, 0.00094155, 31.93945195, 0.02239044, 3.1939452, 0.0820962, -26.34258644, -0.00094155, -31.93945195, -0.02239044, -3.1939452, -0.0820962, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24063, 4063, 0.0, 84.72587088, 0.01883095, 84.72587088, 0.05649285, 59.30810962, -4178.54171566, 0.05, 2, 0, 73004, 24026, 2, 3)
    ops.uniaxialMaterial('LimitState', 44063, 21.18146772, 4.954e-05, 63.54440316, 0.00014863, 211.81467721, 0.00049542, -21.18146772, -4.954e-05, -63.54440316, -0.00014863, -211.81467721, -0.00049542, 0.4, 0.3, 0.003, 0.0, 0.0, 24063, 2)
    ops.limitCurve('ThreePoint', 14063, 4063, 0.0, 84.72587088, 0.01883095, 84.72587088, 0.05649285, 59.30810962, -4178.54171566, 0.05, 2, 0, 73004, 24026, 1, 3)
    ops.uniaxialMaterial('LimitState', 34063, 21.18146772, 4.954e-05, 63.54440316, 0.00014863, 211.81467721, 0.00049542, -21.18146772, -4.954e-05, -63.54440316, -0.00014863, -211.81467721, -0.00049542, 0.4, 0.3, 0.003, 0.0, 0.0, 14063, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4063, 99999, 'P', 44063, 'Vy', 34063, 'Vz', 24063, 'My', 14063, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173004, 73004, 173004, 4063, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124026, 124026, 24026, 4063, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174026, 10.8, 0.0, 10.85)
    ops.node(124004, 10.8, 0.0, 11.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4064, 174026, 124004, 0.0625, 31565896.55974474, 13152456.89989364, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24064, 23.76338925, 0.00083147, 28.74384787, 0.02110953, 2.87438479, 0.08523065, -23.76338925, -0.00083147, -28.74384787, -0.02110953, -2.87438479, -0.08523065, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14064, 23.76338925, 0.00083147, 28.74384787, 0.02110953, 2.87438479, 0.08523065, -23.76338925, -0.00083147, -28.74384787, -0.02110953, -2.87438479, -0.08523065, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24064, 4064, 0.0, 77.64745487, 0.01662934, 77.64745487, 0.04988801, 54.35321841, -5441.02979424, 0.05, 2, 0, 74026, 24004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44064, 19.41186372, 4.321e-05, 58.23559116, 0.00012964, 194.11863719, 0.00043215, -19.41186372, -4.321e-05, -58.23559116, -0.00012964, -194.11863719, -0.00043215, 0.4, 0.3, 0.003, 0.0, 0.0, 24064, 2)
    ops.limitCurve('ThreePoint', 14064, 4064, 0.0, 77.64745487, 0.01662934, 77.64745487, 0.04988801, 54.35321841, -5441.02979424, 0.05, 2, 0, 74026, 24004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34064, 19.41186372, 4.321e-05, 58.23559116, 0.00012964, 194.11863719, 0.00043215, -19.41186372, -4.321e-05, -58.23559116, -0.00012964, -194.11863719, -0.00043215, 0.4, 0.3, 0.003, 0.0, 0.0, 14064, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4064, 99999, 'P', 44064, 'Vy', 34064, 'Vz', 24064, 'My', 14064, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174026, 74026, 174026, 4064, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124004, 124004, 24004, 4064, '-orient', 0, 0, 1, 0, 1, 0)
