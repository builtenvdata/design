import openseespy.opensees as ops


def add_columns() -> None:
    """Add components of all columns to ops domain (plastic hinges, column elements and nodes)
    """
    # Create elastic column element nodes
    ops.node(170001, 0.0, 0.0, 0.0)
    ops.node(121001, 0.0, 0.0, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1, 170001, 121001, 0.1225, 23059682.11080355, 9608200.87950148, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20001, 92.95062305, 0.00110269, 113.04690079, 0.01348218, 11.30469008, 0.0413255, -92.95062305, -0.00110269, -113.04690079, -0.01348218, -11.30469008, -0.0413255, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10001, 87.58911847, 0.00110269, 106.52621856, 0.01348218, 10.65262186, 0.0413255, -87.58911847, -0.00110269, -106.52621856, -0.01348218, -10.65262186, -0.0413255, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20001, 1, 0.0, 86.50508784, 0.02205377, 86.50508784, 0.06616132, 60.55356149, -1161.24902292, 0.05, 2, 0, 70001, 21001, 2, 3)
    ops.uniaxialMaterial('LimitState', 40001, 21.62627196, 5.843e-05, 64.87881588, 0.00017529, 216.26271961, 0.00058429, -21.62627196, -5.843e-05, -64.87881588, -0.00017529, -216.26271961, -0.00058429, 0.4, 0.3, 0.003, 0.0, 0.0, 20001, 2)
    ops.limitCurve('ThreePoint', 10001, 1, 0.0, 86.50508784, 0.02205377, 86.50508784, 0.06616132, 60.55356149, -1161.24902292, 0.05, 2, 0, 70001, 21001, 1, 3)
    ops.uniaxialMaterial('LimitState', 30001, 21.62627196, 5.843e-05, 64.87881588, 0.00017529, 216.26271961, 0.00058429, -21.62627196, -5.843e-05, -64.87881588, -0.00017529, -216.26271961, -0.00058429, 0.4, 0.3, 0.003, 0.0, 0.0, 10001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1, 99999, 'P', 40001, 'Vy', 30001, 'Vz', 20001, 'My', 10001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170001, 70001, 170001, 1, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121001, 121001, 21001, 1, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170002, 7.3, 0.0, 0.0)
    ops.node(121002, 7.3, 0.0, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2, 170002, 121002, 0.2025, 27779840.65496076, 11574933.60623365, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20002, 180.54103236, 0.00077984, 218.97311577, 0.02004064, 21.89731158, 0.05804486, -180.54103236, -0.00077984, -218.97311577, -0.02004064, -21.89731158, -0.05804486, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10002, 211.57329242, 0.00077984, 256.61126699, 0.02004064, 25.6611267, 0.05804486, -211.57329242, -0.00077984, -256.61126699, -0.02004064, -25.6611267, -0.05804486, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20002, 2, 0.0, 218.12499564, 0.01559684, 218.12499564, 0.04679052, 152.68749695, -2880.45149428, 0.05, 2, 0, 70002, 21002, 2, 3)
    ops.uniaxialMaterial('LimitState', 40002, 54.53124891, 7.398e-05, 163.59374673, 0.00022195, 545.3124891, 0.00073983, -54.53124891, -7.398e-05, -163.59374673, -0.00022195, -545.3124891, -0.00073983, 0.4, 0.3, 0.003, 0.0, 0.0, 20002, 2)
    ops.limitCurve('ThreePoint', 10002, 2, 0.0, 218.12499564, 0.01559684, 218.12499564, 0.04679052, 152.68749695, -2880.45149428, 0.05, 2, 0, 70002, 21002, 1, 3)
    ops.uniaxialMaterial('LimitState', 30002, 54.53124891, 7.398e-05, 163.59374673, 0.00022195, 545.3124891, 0.00073983, -54.53124891, -7.398e-05, -163.59374673, -0.00022195, -545.3124891, -0.00073983, 0.4, 0.3, 0.003, 0.0, 0.0, 10002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2, 99999, 'P', 40002, 'Vy', 30002, 'Vz', 20002, 'My', 10002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170002, 70002, 170002, 2, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121002, 121002, 21002, 2, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170005, 24.95, 0.0, 0.0)
    ops.node(121005, 24.95, 0.0, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 5, 170005, 121005, 0.2025, 27069896.11427422, 11279123.38094759, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20005, 186.07674541, 0.0007829, 225.87438579, 0.02041628, 22.58743858, 0.05744994, -186.07674541, -0.0007829, -225.87438579, -0.02041628, -22.58743858, -0.05744994, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10005, 221.23070364, 0.0007829, 268.54698686, 0.02041628, 26.85469869, 0.05744994, -221.23070364, -0.0007829, -268.54698686, -0.02041628, -26.85469869, -0.05744994, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20005, 5, 0.0, 210.29003454, 0.01565799, 210.29003454, 0.04697397, 147.20302418, -2756.06067123, 0.05, 2, 0, 70005, 21005, 2, 3)
    ops.uniaxialMaterial('LimitState', 40005, 52.57250863, 7.32e-05, 157.7175259, 0.00021959, 525.72508635, 0.00073196, -52.57250863, -7.32e-05, -157.7175259, -0.00021959, -525.72508635, -0.00073196, 0.4, 0.3, 0.003, 0.0, 0.0, 20005, 2)
    ops.limitCurve('ThreePoint', 10005, 5, 0.0, 210.29003454, 0.01565799, 210.29003454, 0.04697397, 147.20302418, -2756.06067123, 0.05, 2, 0, 70005, 21005, 1, 3)
    ops.uniaxialMaterial('LimitState', 30005, 52.57250863, 7.32e-05, 157.7175259, 0.00021959, 525.72508635, 0.00073196, -52.57250863, -7.32e-05, -157.7175259, -0.00021959, -525.72508635, -0.00073196, 0.4, 0.3, 0.003, 0.0, 0.0, 10005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 5, 99999, 'P', 40005, 'Vy', 30005, 'Vz', 20005, 'My', 10005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170005, 70005, 170005, 5, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121005, 121005, 21005, 5, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170006, 32.25, 0.0, 0.0)
    ops.node(121006, 32.25, 0.0, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 6, 170006, 121006, 0.1225, 26977200.55969074, 11240500.23320447, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20006, 107.27000908, 0.00104158, 130.34345616, 0.01548387, 13.03434562, 0.0494518, -107.27000908, -0.00104158, -130.34345616, -0.01548387, -13.03434562, -0.0494518, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10006, 100.09535636, 0.00104158, 121.62555784, 0.01548387, 12.16255578, 0.0494518, -100.09535636, -0.00104158, -121.62555784, -0.01548387, -12.16255578, -0.0494518, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20006, 6, 0.0, 109.95824536, 0.02083164, 109.95824536, 0.06249493, 76.97077175, -1341.87459568, 0.05, 2, 0, 70006, 21006, 2, 3)
    ops.uniaxialMaterial('LimitState', 40006, 27.48956134, 6.349e-05, 82.46868402, 0.00019046, 274.89561341, 0.00063485, -27.48956134, -6.349e-05, -82.46868402, -0.00019046, -274.89561341, -0.00063485, 0.4, 0.3, 0.003, 0.0, 0.0, 20006, 2)
    ops.limitCurve('ThreePoint', 10006, 6, 0.0, 109.95824536, 0.02083164, 109.95824536, 0.06249493, 76.97077175, -1341.87459568, 0.05, 2, 0, 70006, 21006, 1, 3)
    ops.uniaxialMaterial('LimitState', 30006, 27.48956134, 6.349e-05, 82.46868402, 0.00019046, 274.89561341, 0.00063485, -27.48956134, -6.349e-05, -82.46868402, -0.00019046, -274.89561341, -0.00063485, 0.4, 0.3, 0.003, 0.0, 0.0, 10006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 6, 99999, 'P', 40006, 'Vy', 30006, 'Vz', 20006, 'My', 10006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170006, 70006, 170006, 6, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121006, 121006, 21006, 6, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170007, 0.0, 3.65, 0.0)
    ops.node(121007, 0.0, 3.65, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 7, 170007, 121007, 0.16, 26405407.80327706, 11002253.25136544, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20007, 174.60634735, 0.00104421, 211.87940292, 0.02582485, 21.18794029, 0.0640898, -174.60634735, -0.00104421, -211.87940292, -0.02582485, -21.18794029, -0.0640898, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10007, 162.83114215, 0.00104421, 197.59055555, 0.02582485, 19.75905555, 0.0640898, -162.83114215, -0.00104421, -197.59055555, -0.02582485, -19.75905555, -0.0640898, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20007, 7, 0.0, 157.00379909, 0.02088425, 157.00379909, 0.06265275, 109.90265937, -2190.12935324, 0.05, 2, 0, 70007, 21007, 2, 3)
    ops.uniaxialMaterial('LimitState', 40007, 39.25094977, 7.09e-05, 117.75284932, 0.00021271, 392.50949773, 0.00070905, -39.25094977, -7.09e-05, -117.75284932, -0.00021271, -392.50949773, -0.00070905, 0.4, 0.3, 0.003, 0.0, 0.0, 20007, 2)
    ops.limitCurve('ThreePoint', 10007, 7, 0.0, 157.00379909, 0.02088425, 157.00379909, 0.06265275, 109.90265937, -2190.12935324, 0.05, 2, 0, 70007, 21007, 1, 3)
    ops.uniaxialMaterial('LimitState', 30007, 39.25094977, 7.09e-05, 117.75284932, 0.00021271, 392.50949773, 0.00070905, -39.25094977, -7.09e-05, -117.75284932, -0.00021271, -392.50949773, -0.00070905, 0.4, 0.3, 0.003, 0.0, 0.0, 10007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 7, 99999, 'P', 40007, 'Vy', 30007, 'Vz', 20007, 'My', 10007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170007, 70007, 170007, 7, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121007, 121007, 21007, 7, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170008, 7.3, 3.65, 0.0)
    ops.node(121008, 7.3, 3.65, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 8, 170008, 121008, 0.2025, 25503508.75089377, 10626461.97953907, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20008, 255.63007091, 0.00094583, 309.56137193, 0.0265596, 30.95613719, 0.06532218, -255.63007091, -0.00094583, -309.56137193, -0.0265596, -30.95613719, -0.06532218, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10008, 305.16247393, 0.00094583, 369.54382462, 0.0265596, 36.95438246, 0.06532218, -305.16247393, -0.00094583, -369.54382462, -0.0265596, -36.95438246, -0.06532218, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20008, 8, 0.0, 215.13636648, 0.01891651, 215.13636648, 0.05674953, 150.59545654, -2996.10872493, 0.05, 2, 0, 70008, 21008, 2, 3)
    ops.uniaxialMaterial('LimitState', 40008, 53.78409162, 7.948e-05, 161.35227486, 0.00023845, 537.8409162, 0.00079482, -53.78409162, -7.948e-05, -161.35227486, -0.00023845, -537.8409162, -0.00079482, 0.4, 0.3, 0.003, 0.0, 0.0, 20008, 2)
    ops.limitCurve('ThreePoint', 10008, 8, 0.0, 215.13636648, 0.01891651, 215.13636648, 0.05674953, 150.59545654, -2996.10872493, 0.05, 2, 0, 70008, 21008, 1, 3)
    ops.uniaxialMaterial('LimitState', 30008, 53.78409162, 7.948e-05, 161.35227486, 0.00023845, 537.8409162, 0.00079482, -53.78409162, -7.948e-05, -161.35227486, -0.00023845, -537.8409162, -0.00079482, 0.4, 0.3, 0.003, 0.0, 0.0, 10008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 8, 99999, 'P', 40008, 'Vy', 30008, 'Vz', 20008, 'My', 10008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170008, 70008, 170008, 8, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121008, 121008, 21008, 8, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170009, 14.6, 3.65, 0.0)
    ops.node(121009, 14.6, 3.65, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 9, 170009, 121009, 0.16, 28230383.34066348, 11762659.72527645, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20009, 209.35546984, 0.00101088, 253.10414969, 0.02694625, 25.31041497, 0.06591159, -209.35546984, -0.00101088, -253.10414969, -0.02694625, -25.31041497, -0.06591159, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10009, 209.35546984, 0.00101088, 253.10414969, 0.02694625, 25.31041497, 0.06591159, -209.35546984, -0.00101088, -253.10414969, -0.02694625, -25.31041497, -0.06591159, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20009, 9, 0.0, 172.6812829, 0.02021766, 172.6812829, 0.06065297, 120.87689803, -2297.86452682, 0.05, 2, 0, 70009, 21009, 2, 3)
    ops.uniaxialMaterial('LimitState', 40009, 43.17032072, 7.294e-05, 129.51096217, 0.00021883, 431.70320724, 0.00072944, -43.17032072, -7.294e-05, -129.51096217, -0.00021883, -431.70320724, -0.00072944, 0.4, 0.3, 0.003, 0.0, 0.0, 20009, 2)
    ops.limitCurve('ThreePoint', 10009, 9, 0.0, 172.6812829, 0.02021766, 172.6812829, 0.06065297, 120.87689803, -2297.86452682, 0.05, 2, 0, 70009, 21009, 1, 3)
    ops.uniaxialMaterial('LimitState', 30009, 43.17032072, 7.294e-05, 129.51096217, 0.00021883, 431.70320724, 0.00072944, -43.17032072, -7.294e-05, -129.51096217, -0.00021883, -431.70320724, -0.00072944, 0.4, 0.3, 0.003, 0.0, 0.0, 10009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 9, 99999, 'P', 40009, 'Vy', 30009, 'Vz', 20009, 'My', 10009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170009, 70009, 170009, 9, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121009, 121009, 21009, 9, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170010, 17.65, 3.65, 0.0)
    ops.node(121010, 17.65, 3.65, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 10, 170010, 121010, 0.16, 26200863.45402438, 10917026.43917683, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20010, 188.67571812, 0.00115414, 228.43583236, 0.02874227, 22.84358324, 0.06404697, -188.67571812, -0.00115414, -228.43583236, -0.02874227, -22.84358324, -0.06404697, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10010, 188.67571812, 0.00115414, 228.43583236, 0.02874227, 22.84358324, 0.06404697, -188.67571812, -0.00115414, -228.43583236, -0.02874227, -22.84358324, -0.06404697, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20010, 10, 0.0, 171.94220241, 0.02308289, 171.94220241, 0.06924866, 120.35954169, -2602.97101706, 0.05, 2, 0, 70010, 21010, 2, 3)
    ops.uniaxialMaterial('LimitState', 40010, 42.9855506, 7.826e-05, 128.95665181, 0.00023477, 429.85550603, 0.00078257, -42.9855506, -7.826e-05, -128.95665181, -0.00023477, -429.85550603, -0.00078257, 0.4, 0.3, 0.003, 0.0, 0.0, 20010, 2)
    ops.limitCurve('ThreePoint', 10010, 10, 0.0, 171.94220241, 0.02308289, 171.94220241, 0.06924866, 120.35954169, -2602.97101706, 0.05, 2, 0, 70010, 21010, 1, 3)
    ops.uniaxialMaterial('LimitState', 30010, 42.9855506, 7.826e-05, 128.95665181, 0.00023477, 429.85550603, 0.00078257, -42.9855506, -7.826e-05, -128.95665181, -0.00023477, -429.85550603, -0.00078257, 0.4, 0.3, 0.003, 0.0, 0.0, 10010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 10, 99999, 'P', 40010, 'Vy', 30010, 'Vz', 20010, 'My', 10010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170010, 70010, 170010, 10, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121010, 121010, 21010, 10, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170011, 24.95, 3.65, 0.0)
    ops.node(121011, 24.95, 3.65, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 11, 170011, 121011, 0.2025, 25973024.81783127, 10822093.67409636, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20011, 234.06204933, 0.00095545, 283.44109241, 0.0280386, 28.34410924, 0.06792732, -234.06204933, -0.00095545, -283.44109241, -0.0280386, -28.34410924, -0.06792732, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10011, 269.86009749, 0.00095545, 326.79129764, 0.0280386, 32.67912976, 0.06792732, -269.86009749, -0.00095545, -326.79129764, -0.0280386, -32.67912976, -0.06792732, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20011, 11, 0.0, 221.08493031, 0.0191091, 221.08493031, 0.05732729, 154.75945121, -3100.10151609, 0.05, 2, 0, 70011, 21011, 2, 3)
    ops.uniaxialMaterial('LimitState', 40011, 55.27123258, 8.02e-05, 165.81369773, 0.00024061, 552.71232576, 0.00080203, -55.27123258, -8.02e-05, -165.81369773, -0.00024061, -552.71232576, -0.00080203, 0.4, 0.3, 0.003, 0.0, 0.0, 20011, 2)
    ops.limitCurve('ThreePoint', 10011, 11, 0.0, 221.08493031, 0.0191091, 221.08493031, 0.05732729, 154.75945121, -3100.10151609, 0.05, 2, 0, 70011, 21011, 1, 3)
    ops.uniaxialMaterial('LimitState', 30011, 55.27123258, 8.02e-05, 165.81369773, 0.00024061, 552.71232576, 0.00080203, -55.27123258, -8.02e-05, -165.81369773, -0.00024061, -552.71232576, -0.00080203, 0.4, 0.3, 0.003, 0.0, 0.0, 10011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 11, 99999, 'P', 40011, 'Vy', 30011, 'Vz', 20011, 'My', 10011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170011, 70011, 170011, 11, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121011, 121011, 21011, 11, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170012, 32.25, 3.65, 0.0)
    ops.node(121012, 32.25, 3.65, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 12, 170012, 121012, 0.16, 28242818.79137745, 11767841.16307394, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20012, 165.41322572, 0.00098738, 200.3469746, 0.02634655, 20.03469746, 0.0675436, -165.41322572, -0.00098738, -200.3469746, -0.02634655, -20.03469746, -0.0675436, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10012, 155.26347553, 0.00098738, 188.05369071, 0.02634655, 18.80536907, 0.0675436, -155.26347553, -0.00098738, -188.05369071, -0.02634655, -18.80536907, -0.0675436, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20012, 12, 0.0, 160.67044189, 0.01974756, 160.67044189, 0.05924269, 112.46930933, -2019.53033067, 0.05, 2, 0, 70012, 21012, 2, 3)
    ops.uniaxialMaterial('LimitState', 40012, 40.16761047, 6.784e-05, 120.50283142, 0.00020352, 401.67610474, 0.0006784, -40.16761047, -6.784e-05, -120.50283142, -0.00020352, -401.67610474, -0.0006784, 0.4, 0.3, 0.003, 0.0, 0.0, 20012, 2)
    ops.limitCurve('ThreePoint', 10012, 12, 0.0, 160.67044189, 0.01974756, 160.67044189, 0.05924269, 112.46930933, -2019.53033067, 0.05, 2, 0, 70012, 21012, 1, 3)
    ops.uniaxialMaterial('LimitState', 30012, 40.16761047, 6.784e-05, 120.50283142, 0.00020352, 401.67610474, 0.0006784, -40.16761047, -6.784e-05, -120.50283142, -0.00020352, -401.67610474, -0.0006784, 0.4, 0.3, 0.003, 0.0, 0.0, 10012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 12, 99999, 'P', 40012, 'Vy', 30012, 'Vz', 20012, 'My', 10012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170012, 70012, 170012, 12, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121012, 121012, 21012, 12, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170013, 0.0, 7.3, 0.0)
    ops.node(121013, 0.0, 7.3, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 13, 170013, 121013, 0.1225, 27650893.35929574, 11521205.56637323, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20013, 88.15092477, 0.00089922, 107.02317662, 0.01723689, 10.70231766, 0.05198955, -88.15092477, -0.00089922, -107.02317662, -0.01723689, -10.70231766, -0.05198955, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10013, 83.23005664, 0.00089922, 101.04879869, 0.01723689, 10.10487987, 0.05198955, -83.23005664, -0.00089922, -101.04879869, -0.01723689, -10.10487987, -0.05198955, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20013, 13, 0.0, 112.91693471, 0.01798447, 112.91693471, 0.0539534, 79.04185429, -1362.47545714, 0.05, 2, 0, 70013, 21013, 2, 3)
    ops.uniaxialMaterial('LimitState', 40013, 28.22923368, 6.361e-05, 84.68770103, 0.00019082, 282.29233677, 0.00063605, -28.22923368, -6.361e-05, -84.68770103, -0.00019082, -282.29233677, -0.00063605, 0.4, 0.3, 0.003, 0.0, 0.0, 20013, 2)
    ops.limitCurve('ThreePoint', 10013, 13, 0.0, 112.91693471, 0.01798447, 112.91693471, 0.0539534, 79.04185429, -1362.47545714, 0.05, 2, 0, 70013, 21013, 1, 3)
    ops.uniaxialMaterial('LimitState', 30013, 28.22923368, 6.361e-05, 84.68770103, 0.00019082, 282.29233677, 0.00063605, -28.22923368, -6.361e-05, -84.68770103, -0.00019082, -282.29233677, -0.00063605, 0.4, 0.3, 0.003, 0.0, 0.0, 10013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 13, 99999, 'P', 40013, 'Vy', 30013, 'Vz', 20013, 'My', 10013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170013, 70013, 170013, 13, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121013, 121013, 21013, 13, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170014, 7.3, 7.3, 0.0)
    ops.node(121014, 7.3, 7.3, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 14, 170014, 121014, 0.2025, 24869145.18893842, 10362143.82872434, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20014, 183.53575948, 0.00082718, 223.05893851, 0.01764152, 22.30589385, 0.05107708, -183.53575948, -0.00082718, -223.05893851, -0.01764152, -22.30589385, -0.05107708, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10014, 217.20497248, 0.00082718, 263.97858781, 0.01764152, 26.39785878, 0.05107708, -217.20497248, -0.00082718, -263.97858781, -0.01764152, -26.39785878, -0.05107708, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20014, 14, 0.0, 194.8682797, 0.01654364, 194.8682797, 0.04963092, 136.40779579, -2688.56268481, 0.05, 2, 0, 70014, 21014, 2, 3)
    ops.uniaxialMaterial('LimitState', 40014, 48.71706992, 7.383e-05, 146.15120977, 0.00022149, 487.17069925, 0.0007383, -48.71706992, -7.383e-05, -146.15120977, -0.00022149, -487.17069925, -0.0007383, 0.4, 0.3, 0.003, 0.0, 0.0, 20014, 2)
    ops.limitCurve('ThreePoint', 10014, 14, 0.0, 194.8682797, 0.01654364, 194.8682797, 0.04963092, 136.40779579, -2688.56268481, 0.05, 2, 0, 70014, 21014, 1, 3)
    ops.uniaxialMaterial('LimitState', 30014, 48.71706992, 7.383e-05, 146.15120977, 0.00022149, 487.17069925, 0.0007383, -48.71706992, -7.383e-05, -146.15120977, -0.00022149, -487.17069925, -0.0007383, 0.4, 0.3, 0.003, 0.0, 0.0, 10014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 14, 99999, 'P', 40014, 'Vy', 30014, 'Vz', 20014, 'My', 10014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170014, 70014, 170014, 14, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121014, 121014, 21014, 14, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170015, 14.6, 7.3, 0.0)
    ops.node(121015, 14.6, 7.3, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 15, 170015, 121015, 0.1225, 27553831.27838653, 11480763.03266105, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20015, 114.61754329, 0.00098298, 138.82898279, 0.01322267, 13.88289828, 0.04988282, -114.61754329, -0.00098298, -138.82898279, -0.01322267, -13.88289828, -0.04988282, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10015, 114.61754329, 0.00098298, 138.82898279, 0.01322267, 13.88289828, 0.04988282, -114.61754329, -0.00098298, -138.82898279, -0.01322267, -13.88289828, -0.04988282, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20015, 15, 0.0, 116.08523506, 0.01965969, 116.08523506, 0.05897907, 81.25966454, -1364.68486247, 0.05, 2, 0, 70015, 21015, 2, 3)
    ops.uniaxialMaterial('LimitState', 40015, 29.02130876, 6.562e-05, 87.06392629, 0.00019686, 290.21308764, 0.0006562, -29.02130876, -6.562e-05, -87.06392629, -0.00019686, -290.21308764, -0.0006562, 0.4, 0.3, 0.003, 0.0, 0.0, 20015, 2)
    ops.limitCurve('ThreePoint', 10015, 15, 0.0, 116.08523506, 0.01965969, 116.08523506, 0.05897907, 81.25966454, -1364.68486247, 0.05, 2, 0, 70015, 21015, 1, 3)
    ops.uniaxialMaterial('LimitState', 30015, 29.02130876, 6.562e-05, 87.06392629, 0.00019686, 290.21308764, 0.0006562, -29.02130876, -6.562e-05, -87.06392629, -0.00019686, -290.21308764, -0.0006562, 0.4, 0.3, 0.003, 0.0, 0.0, 10015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 15, 99999, 'P', 40015, 'Vy', 30015, 'Vz', 20015, 'My', 10015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170015, 70015, 170015, 15, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121015, 121015, 21015, 15, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170016, 17.65, 7.3, 0.0)
    ops.node(121016, 17.65, 7.3, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 16, 170016, 121016, 0.1225, 25335490.09793978, 10556454.20747491, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20016, 118.84402136, 0.00106081, 144.11418144, 0.01367375, 14.41141814, 0.04648379, -118.84402136, -0.00106081, -144.11418144, -0.01367375, -14.41141814, -0.04648379, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10016, 118.84402136, 0.00106081, 144.11418144, 0.01367375, 14.41141814, 0.04648379, -118.84402136, -0.00106081, -144.11418144, -0.01367375, -14.41141814, -0.04648379, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20016, 16, 0.0, 112.51245403, 0.0212162, 112.51245403, 0.06364861, 78.75871782, -1498.9977315, 0.05, 2, 0, 70016, 21016, 2, 3)
    ops.uniaxialMaterial('LimitState', 40016, 28.12811351, 6.917e-05, 84.38434053, 0.00020751, 281.28113509, 0.00069169, -28.12811351, -6.917e-05, -84.38434053, -0.00020751, -281.28113509, -0.00069169, 0.4, 0.3, 0.003, 0.0, 0.0, 20016, 2)
    ops.limitCurve('ThreePoint', 10016, 16, 0.0, 112.51245403, 0.0212162, 112.51245403, 0.06364861, 78.75871782, -1498.9977315, 0.05, 2, 0, 70016, 21016, 1, 3)
    ops.uniaxialMaterial('LimitState', 30016, 28.12811351, 6.917e-05, 84.38434053, 0.00020751, 281.28113509, 0.00069169, -28.12811351, -6.917e-05, -84.38434053, -0.00020751, -281.28113509, -0.00069169, 0.4, 0.3, 0.003, 0.0, 0.0, 10016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 16, 99999, 'P', 40016, 'Vy', 30016, 'Vz', 20016, 'My', 10016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170016, 70016, 170016, 16, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121016, 121016, 21016, 16, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170017, 24.95, 7.3, 0.0)
    ops.node(121017, 24.95, 7.3, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 17, 170017, 121017, 0.2025, 29494634.06406985, 12289430.8600291, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20017, 186.52047015, 0.00084255, 225.59452507, 0.01817208, 22.55945251, 0.05820284, -186.52047015, -0.00084255, -225.59452507, -0.01817208, -22.55945251, -0.05820284, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10017, 214.42223032, 0.00084255, 259.34140727, 0.01817208, 25.93414073, 0.05820284, -214.42223032, -0.00084255, -259.34140727, -0.01817208, -25.93414073, -0.05820284, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20017, 17, 0.0, 220.05158633, 0.01685106, 220.05158633, 0.05055319, 154.03611043, -2539.84379143, 0.05, 2, 0, 70017, 21017, 2, 3)
    ops.uniaxialMaterial('LimitState', 40017, 55.01289658, 7.03e-05, 165.03868975, 0.00021089, 550.12896582, 0.00070297, -55.01289658, -7.03e-05, -165.03868975, -0.00021089, -550.12896582, -0.00070297, 0.4, 0.3, 0.003, 0.0, 0.0, 20017, 2)
    ops.limitCurve('ThreePoint', 10017, 17, 0.0, 220.05158633, 0.01685106, 220.05158633, 0.05055319, 154.03611043, -2539.84379143, 0.05, 2, 0, 70017, 21017, 1, 3)
    ops.uniaxialMaterial('LimitState', 30017, 55.01289658, 7.03e-05, 165.03868975, 0.00021089, 550.12896582, 0.00070297, -55.01289658, -7.03e-05, -165.03868975, -0.00021089, -550.12896582, -0.00070297, 0.4, 0.3, 0.003, 0.0, 0.0, 10017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 17, 99999, 'P', 40017, 'Vy', 30017, 'Vz', 20017, 'My', 10017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170017, 70017, 170017, 17, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121017, 121017, 21017, 17, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170018, 32.25, 7.3, 0.0)
    ops.node(121018, 32.25, 7.3, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 18, 170018, 121018, 0.1225, 30201907.96195455, 12584128.31748106, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20018, 98.76347146, 0.00104956, 119.35358914, 0.01683769, 11.93535891, 0.05403275, -98.76347146, -0.00104956, -119.35358914, -0.01683769, -11.93535891, -0.05403275, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10018, 93.49706334, 0.00104956, 112.9892451, 0.01683769, 11.29892451, 0.05403275, -93.49706334, -0.00104956, -112.9892451, -0.01683769, -11.29892451, -0.05403275, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20018, 18, 0.0, 124.38553846, 0.02099118, 124.38553846, 0.06297354, 87.06987692, -1440.54663297, 0.05, 2, 0, 70018, 21018, 2, 3)
    ops.uniaxialMaterial('LimitState', 40018, 31.09638461, 6.415e-05, 93.28915384, 0.00019244, 310.96384614, 0.00064147, -31.09638461, -6.415e-05, -93.28915384, -0.00019244, -310.96384614, -0.00064147, 0.4, 0.3, 0.003, 0.0, 0.0, 20018, 2)
    ops.limitCurve('ThreePoint', 10018, 18, 0.0, 124.38553846, 0.02099118, 124.38553846, 0.06297354, 87.06987692, -1440.54663297, 0.05, 2, 0, 70018, 21018, 1, 3)
    ops.uniaxialMaterial('LimitState', 30018, 31.09638461, 6.415e-05, 93.28915384, 0.00019244, 310.96384614, 0.00064147, -31.09638461, -6.415e-05, -93.28915384, -0.00019244, -310.96384614, -0.00064147, 0.4, 0.3, 0.003, 0.0, 0.0, 10018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 18, 99999, 'P', 40018, 'Vy', 30018, 'Vz', 20018, 'My', 10018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170018, 70018, 170018, 18, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121018, 121018, 21018, 18, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171001, 0.0, 0.0, 3.0)
    ops.node(122001, 0.0, 0.0, 4.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1001, 171001, 122001, 0.1225, 27433849.34831724, 11430770.56179885, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21001, 113.7410726, 0.00124648, 138.49302013, 0.03536861, 13.84930201, 0.09880669, -113.7410726, -0.00124648, -138.49302013, -0.03536861, -13.84930201, -0.09880669, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11001, 101.44570227, 0.00124648, 123.52197289, 0.03536861, 12.35219729, 0.09880669, -101.44570227, -0.00124648, -123.52197289, -0.03536861, -12.35219729, -0.09880669, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21001, 1001, 0.0, 147.43355233, 0.02492963, 147.43355233, 0.0747889, 103.20348663, -3573.85802263, 0.05, 2, 0, 71001, 22001, 2, 3)
    ops.uniaxialMaterial('LimitState', 41001, 36.85838808, 8.371e-05, 110.57516425, 0.00025112, 368.58388082, 0.00083705, -36.85838808, -8.371e-05, -110.57516425, -0.00025112, -368.58388082, -0.00083705, 0.4, 0.3, 0.003, 0.0, 0.0, 21001, 2)
    ops.limitCurve('ThreePoint', 11001, 1001, 0.0, 147.43355233, 0.02492963, 147.43355233, 0.0747889, 103.20348663, -3573.85802263, 0.05, 2, 0, 71001, 22001, 1, 3)
    ops.uniaxialMaterial('LimitState', 31001, 36.85838808, 8.371e-05, 110.57516425, 0.00025112, 368.58388082, 0.00083705, -36.85838808, -8.371e-05, -110.57516425, -0.00025112, -368.58388082, -0.00083705, 0.4, 0.3, 0.003, 0.0, 0.0, 11001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1001, 99999, 'P', 41001, 'Vy', 31001, 'Vz', 21001, 'My', 11001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171001, 71001, 171001, 1001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122001, 122001, 22001, 1001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171002, 7.3, 0.0, 3.0)
    ops.node(122002, 7.3, 0.0, 4.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1002, 171002, 122002, 0.2025, 30115486.64328622, 12548119.43470259, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21002, 183.64020052, 0.00079794, 222.28704793, 0.01579316, 22.22870479, 0.05274089, -183.64020052, -0.00079794, -222.28704793, -0.01579316, -22.22870479, -0.05274089, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11002, 148.60932617, 0.00079794, 179.88397047, 0.01579316, 17.98839705, 0.05274089, -148.60932617, -0.00079794, -179.88397047, -0.01579316, -17.98839705, -0.05274089, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21002, 1002, 0.0, 213.15287336, 0.01595872, 213.15287336, 0.04787617, 149.20701135, -2527.72873898, 0.05, 2, 0, 71002, 22002, 2, 3)
    ops.uniaxialMaterial('LimitState', 41002, 53.28821834, 6.669e-05, 159.86465502, 0.00020007, 532.88218339, 0.00066689, -53.28821834, -6.669e-05, -159.86465502, -0.00020007, -532.88218339, -0.00066689, 0.4, 0.3, 0.003, 0.0, 0.0, 21002, 2)
    ops.limitCurve('ThreePoint', 11002, 1002, 0.0, 213.15287336, 0.01595872, 213.15287336, 0.04787617, 149.20701135, -2527.72873898, 0.05, 2, 0, 71002, 22002, 1, 3)
    ops.uniaxialMaterial('LimitState', 31002, 53.28821834, 6.669e-05, 159.86465502, 0.00020007, 532.88218339, 0.00066689, -53.28821834, -6.669e-05, -159.86465502, -0.00020007, -532.88218339, -0.00066689, 0.4, 0.3, 0.003, 0.0, 0.0, 11002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1002, 99999, 'P', 41002, 'Vy', 31002, 'Vz', 21002, 'My', 11002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171002, 71002, 171002, 1002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122002, 122002, 22002, 1002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171005, 24.95, 0.0, 3.0)
    ops.node(122005, 24.95, 0.0, 4.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1005, 171005, 122005, 0.2025, 24201301.1982156, 10083875.4992565, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21005, 175.11007532, 0.00085572, 213.71233169, 0.01709281, 21.37123317, 0.04828981, -175.11007532, -0.00085572, -213.71233169, -0.01709281, -21.37123317, -0.04828981, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11005, 141.82858742, 0.00085572, 173.09408417, 0.01709281, 17.30940842, 0.04828981, -141.82858742, -0.00085572, -173.09408417, -0.01709281, -17.30940842, -0.04828981, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21005, 1005, 0.0, 180.00977723, 0.01711446, 180.00977723, 0.05134339, 126.00684406, -2683.62824673, 0.05, 2, 0, 71005, 22005, 2, 3)
    ops.uniaxialMaterial('LimitState', 41005, 45.00244431, 7.008e-05, 135.00733292, 0.00021025, 450.02444308, 0.00070083, -45.00244431, -7.008e-05, -135.00733292, -0.00021025, -450.02444308, -0.00070083, 0.4, 0.3, 0.003, 0.0, 0.0, 21005, 2)
    ops.limitCurve('ThreePoint', 11005, 1005, 0.0, 180.00977723, 0.01711446, 180.00977723, 0.05134339, 126.00684406, -2683.62824673, 0.05, 2, 0, 71005, 22005, 1, 3)
    ops.uniaxialMaterial('LimitState', 31005, 45.00244431, 7.008e-05, 135.00733292, 0.00021025, 450.02444308, 0.00070083, -45.00244431, -7.008e-05, -135.00733292, -0.00021025, -450.02444308, -0.00070083, 0.4, 0.3, 0.003, 0.0, 0.0, 11005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1005, 99999, 'P', 41005, 'Vy', 31005, 'Vz', 21005, 'My', 11005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171005, 71005, 171005, 1005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122005, 122005, 22005, 1005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171006, 32.25, 0.0, 3.0)
    ops.node(122006, 32.25, 0.0, 4.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1006, 171006, 122006, 0.1225, 27502072.27622139, 11459196.78175891, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21006, 111.0426508, 0.00098227, 135.19257023, 0.03893818, 13.51925702, 0.1024787, -111.0426508, -0.00098227, -135.19257023, -0.03893818, -13.51925702, -0.1024787, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11006, 95.54280355, 0.00098227, 116.32176543, 0.03893818, 11.63217654, 0.1024787, -95.54280355, -0.00098227, -116.32176543, -0.03893818, -11.63217654, -0.1024787, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21006, 1006, 0.0, 156.53643639, 0.01964545, 156.53643639, 0.05893634, 109.57550547, -4194.32890573, 0.05, 2, 0, 71006, 22006, 2, 3)
    ops.uniaxialMaterial('LimitState', 41006, 39.1341091, 8.865e-05, 117.40232729, 0.00026596, 391.34109098, 0.00088653, -39.1341091, -8.865e-05, -117.40232729, -0.00026596, -391.34109098, -0.00088653, 0.4, 0.3, 0.003, 0.0, 0.0, 21006, 2)
    ops.limitCurve('ThreePoint', 11006, 1006, 0.0, 156.53643639, 0.01964545, 156.53643639, 0.05893634, 109.57550547, -4194.32890573, 0.05, 2, 0, 71006, 22006, 1, 3)
    ops.uniaxialMaterial('LimitState', 31006, 39.1341091, 8.865e-05, 117.40232729, 0.00026596, 391.34109098, 0.00088653, -39.1341091, -8.865e-05, -117.40232729, -0.00026596, -391.34109098, -0.00088653, 0.4, 0.3, 0.003, 0.0, 0.0, 11006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1006, 99999, 'P', 41006, 'Vy', 31006, 'Vz', 21006, 'My', 11006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171006, 71006, 171006, 1006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122006, 122006, 22006, 1006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171007, 0.0, 3.65, 3.0)
    ops.node(122007, 0.0, 3.65, 4.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1007, 171007, 122007, 0.16, 23975001.20258065, 9989583.83440861, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21007, 190.65148511, 0.00104147, 232.46052789, 0.03795938, 23.24605279, 0.08588713, -190.65148511, -0.00104147, -232.46052789, -0.03795938, -23.24605279, -0.08588713, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11007, 165.3954531, 0.00104147, 201.66595775, 0.03795938, 20.16659577, 0.08588713, -165.3954531, -0.00104147, -201.66595775, -0.03795938, -20.16659577, -0.08588713, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21007, 1007, 0.0, 172.52738555, 0.02082949, 172.52738555, 0.06248846, 120.76916988, -3865.28649708, 0.05, 2, 0, 71007, 22007, 2, 3)
    ops.uniaxialMaterial('LimitState', 41007, 43.13184639, 8.581e-05, 129.39553916, 0.00025744, 431.31846387, 0.00085814, -43.13184639, -8.581e-05, -129.39553916, -0.00025744, -431.31846387, -0.00085814, 0.4, 0.3, 0.003, 0.0, 0.0, 21007, 2)
    ops.limitCurve('ThreePoint', 11007, 1007, 0.0, 172.52738555, 0.02082949, 172.52738555, 0.06248846, 120.76916988, -3865.28649708, 0.05, 2, 0, 71007, 22007, 1, 3)
    ops.uniaxialMaterial('LimitState', 31007, 43.13184639, 8.581e-05, 129.39553916, 0.00025744, 431.31846387, 0.00085814, -43.13184639, -8.581e-05, -129.39553916, -0.00025744, -431.31846387, -0.00085814, 0.4, 0.3, 0.003, 0.0, 0.0, 11007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1007, 99999, 'P', 41007, 'Vy', 31007, 'Vz', 21007, 'My', 11007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171007, 71007, 171007, 1007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122007, 122007, 22007, 1007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171008, 7.3, 3.65, 3.0)
    ops.node(122008, 7.3, 3.65, 4.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1008, 171008, 122008, 0.2025, 27025307.15290509, 11260544.64704379, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21008, 188.17104389, 0.00081919, 228.59591213, 0.0203034, 22.85959121, 0.05258999, -188.17104389, -0.00081919, -228.59591213, -0.0203034, -22.85959121, -0.05258999, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11008, 165.280646, 0.00081919, 200.78795997, 0.0203034, 20.078796, 0.05258999, -165.280646, -0.00081919, -200.78795997, -0.0203034, -20.078796, -0.05258999, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21008, 1008, 0.0, 199.12400746, 0.01638374, 199.12400746, 0.04915122, 139.38680522, -2440.96926657, 0.05, 2, 0, 71008, 22008, 2, 3)
    ops.uniaxialMaterial('LimitState', 41008, 49.78100186, 6.942e-05, 149.34300559, 0.00020827, 497.81001865, 0.00069423, -49.78100186, -6.942e-05, -149.34300559, -0.00020827, -497.81001865, -0.00069423, 0.4, 0.3, 0.003, 0.0, 0.0, 21008, 2)
    ops.limitCurve('ThreePoint', 11008, 1008, 0.0, 199.12400746, 0.01638374, 199.12400746, 0.04915122, 139.38680522, -2440.96926657, 0.05, 2, 0, 71008, 22008, 1, 3)
    ops.uniaxialMaterial('LimitState', 31008, 49.78100186, 6.942e-05, 149.34300559, 0.00020827, 497.81001865, 0.00069423, -49.78100186, -6.942e-05, -149.34300559, -0.00020827, -497.81001865, -0.00069423, 0.4, 0.3, 0.003, 0.0, 0.0, 11008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1008, 99999, 'P', 41008, 'Vy', 31008, 'Vz', 21008, 'My', 11008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171008, 71008, 171008, 1008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122008, 122008, 22008, 1008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171009, 14.6, 3.65, 3.0)
    ops.node(122009, 14.6, 3.65, 4.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1009, 171009, 122009, 0.16, 24433034.88105787, 10180431.20044078, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21009, 148.79039796, 0.00107654, 180.96868667, 0.02616416, 18.09686867, 0.06259354, -148.79039796, -0.00107654, -180.96868667, -0.02616416, -18.09686867, -0.06259354, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11009, 148.79039796, 0.00107654, 180.96868667, 0.02616416, 18.09686867, 0.06259354, -148.79039796, -0.00107654, -180.96868667, -0.02616416, -18.09686867, -0.06259354, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21009, 1009, 0.0, 150.35402057, 0.02153085, 150.35402057, 0.06459256, 105.2478144, -2398.03298342, 0.05, 2, 0, 71009, 22009, 2, 3)
    ops.uniaxialMaterial('LimitState', 41009, 37.58850514, 7.338e-05, 112.76551543, 0.00022015, 375.88505142, 0.00073383, -37.58850514, -7.338e-05, -112.76551543, -0.00022015, -375.88505142, -0.00073383, 0.4, 0.3, 0.003, 0.0, 0.0, 21009, 2)
    ops.limitCurve('ThreePoint', 11009, 1009, 0.0, 150.35402057, 0.02153085, 150.35402057, 0.06459256, 105.2478144, -2398.03298342, 0.05, 2, 0, 71009, 22009, 1, 3)
    ops.uniaxialMaterial('LimitState', 31009, 37.58850514, 7.338e-05, 112.76551543, 0.00022015, 375.88505142, 0.00073383, -37.58850514, -7.338e-05, -112.76551543, -0.00022015, -375.88505142, -0.00073383, 0.4, 0.3, 0.003, 0.0, 0.0, 11009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1009, 99999, 'P', 41009, 'Vy', 31009, 'Vz', 21009, 'My', 11009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171009, 71009, 171009, 1009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122009, 122009, 22009, 1009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171010, 17.65, 3.65, 3.0)
    ops.node(122010, 17.65, 3.65, 4.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1010, 171010, 122010, 0.16, 24791109.24488717, 10329628.85203632, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21010, 146.28605603, 0.00105847, 177.9222033, 0.02837124, 17.79222033, 0.0655264, -146.28605603, -0.00105847, -177.9222033, -0.02837124, -17.79222033, -0.0655264, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11010, 146.28605603, 0.00105847, 177.9222033, 0.02837124, 17.79222033, 0.0655264, -146.28605603, -0.00105847, -177.9222033, -0.02837124, -17.79222033, -0.0655264, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21010, 1010, 0.0, 157.91436562, 0.0211695, 157.91436562, 0.06350849, 110.54005593, -2644.42782946, 0.05, 2, 0, 71010, 22010, 2, 3)
    ops.uniaxialMaterial('LimitState', 41010, 39.47859141, 7.596e-05, 118.43577422, 0.00022788, 394.78591405, 0.0007596, -39.47859141, -7.596e-05, -118.43577422, -0.00022788, -394.78591405, -0.0007596, 0.4, 0.3, 0.003, 0.0, 0.0, 21010, 2)
    ops.limitCurve('ThreePoint', 11010, 1010, 0.0, 157.91436562, 0.0211695, 157.91436562, 0.06350849, 110.54005593, -2644.42782946, 0.05, 2, 0, 71010, 22010, 1, 3)
    ops.uniaxialMaterial('LimitState', 31010, 39.47859141, 7.596e-05, 118.43577422, 0.00022788, 394.78591405, 0.0007596, -39.47859141, -7.596e-05, -118.43577422, -0.00022788, -394.78591405, -0.0007596, 0.4, 0.3, 0.003, 0.0, 0.0, 11010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1010, 99999, 'P', 41010, 'Vy', 31010, 'Vz', 21010, 'My', 11010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171010, 71010, 171010, 1010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122010, 122010, 22010, 1010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171011, 24.95, 3.65, 3.0)
    ops.node(122011, 24.95, 3.65, 4.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1011, 171011, 122011, 0.2025, 28081799.69338064, 11700749.87224193, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21011, 195.575557, 0.00080153, 237.26461585, 0.01909045, 23.72646159, 0.05253072, -195.575557, -0.00080153, -237.26461585, -0.01909045, -23.72646159, -0.05253072, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11011, 170.40220575, 0.00080153, 206.72529077, 0.01909045, 20.67252908, 0.05253072, -170.40220575, -0.00080153, -206.72529077, -0.01909045, -20.67252908, -0.05253072, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21011, 1011, 0.0, 201.6298669, 0.01603057, 201.6298669, 0.04809172, 141.14090683, -2290.93518779, 0.05, 2, 0, 71011, 22011, 2, 3)
    ops.uniaxialMaterial('LimitState', 41011, 50.40746673, 6.765e-05, 151.22240018, 0.00020296, 504.07466726, 0.00067652, -50.40746673, -6.765e-05, -151.22240018, -0.00020296, -504.07466726, -0.00067652, 0.4, 0.3, 0.003, 0.0, 0.0, 21011, 2)
    ops.limitCurve('ThreePoint', 11011, 1011, 0.0, 201.6298669, 0.01603057, 201.6298669, 0.04809172, 141.14090683, -2290.93518779, 0.05, 2, 0, 71011, 22011, 1, 3)
    ops.uniaxialMaterial('LimitState', 31011, 50.40746673, 6.765e-05, 151.22240018, 0.00020296, 504.07466726, 0.00067652, -50.40746673, -6.765e-05, -151.22240018, -0.00020296, -504.07466726, -0.00067652, 0.4, 0.3, 0.003, 0.0, 0.0, 11011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1011, 99999, 'P', 41011, 'Vy', 31011, 'Vz', 21011, 'My', 11011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171011, 71011, 171011, 1011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122011, 122011, 22011, 1011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171012, 32.25, 3.65, 3.0)
    ops.node(122012, 32.25, 3.65, 4.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1012, 171012, 122012, 0.16, 25671816.96329775, 10696590.40137406, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21012, 192.13348312, 0.00104882, 234.10203471, 0.0394413, 23.41020347, 0.09109109, -192.13348312, -0.00104882, -234.10203471, -0.0394413, -23.41020347, -0.09109109, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11012, 167.84471996, 0.00104882, 204.50777148, 0.0394413, 20.45077715, 0.09109109, -167.84471996, -0.00104882, -204.50777148, -0.0394413, -20.45077715, -0.09109109, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21012, 1012, 0.0, 177.32688786, 0.02097635, 177.32688786, 0.06292905, 124.1288215, -3726.0198195, 0.05, 2, 0, 71012, 22012, 2, 3)
    ops.uniaxialMaterial('LimitState', 41012, 44.33172197, 8.237e-05, 132.9951659, 0.00024711, 443.31721966, 0.00082371, -44.33172197, -8.237e-05, -132.9951659, -0.00024711, -443.31721966, -0.00082371, 0.4, 0.3, 0.003, 0.0, 0.0, 21012, 2)
    ops.limitCurve('ThreePoint', 11012, 1012, 0.0, 177.32688786, 0.02097635, 177.32688786, 0.06292905, 124.1288215, -3726.0198195, 0.05, 2, 0, 71012, 22012, 1, 3)
    ops.uniaxialMaterial('LimitState', 31012, 44.33172197, 8.237e-05, 132.9951659, 0.00024711, 443.31721966, 0.00082371, -44.33172197, -8.237e-05, -132.9951659, -0.00024711, -443.31721966, -0.00082371, 0.4, 0.3, 0.003, 0.0, 0.0, 11012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1012, 99999, 'P', 41012, 'Vy', 31012, 'Vz', 21012, 'My', 11012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171012, 71012, 171012, 1012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122012, 122012, 22012, 1012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171013, 0.0, 7.3, 3.0)
    ops.node(122013, 0.0, 7.3, 4.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1013, 171013, 122013, 0.1225, 24562320.24335422, 10234300.10139759, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21013, 123.4616844, 0.00111918, 150.80213613, 0.03934301, 15.08021361, 0.09748353, -123.4616844, -0.00111918, -150.80213613, -0.03934301, -15.08021361, -0.09748353, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11013, 104.52781916, 0.00111918, 127.67538765, 0.03934301, 12.76753877, 0.09748353, -104.52781916, -0.00111918, -127.67538765, -0.03934301, -12.76753877, -0.09748353, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21013, 1013, 0.0, 151.41876128, 0.02238352, 151.41876128, 0.06715057, 105.9931329, -4549.01479466, 0.05, 2, 0, 71013, 22013, 2, 3)
    ops.uniaxialMaterial('LimitState', 41013, 37.85469032, 9.602e-05, 113.56407096, 0.00028805, 378.54690321, 0.00096018, -37.85469032, -9.602e-05, -113.56407096, -0.00028805, -378.54690321, -0.00096018, 0.4, 0.3, 0.003, 0.0, 0.0, 21013, 2)
    ops.limitCurve('ThreePoint', 11013, 1013, 0.0, 151.41876128, 0.02238352, 151.41876128, 0.06715057, 105.9931329, -4549.01479466, 0.05, 2, 0, 71013, 22013, 1, 3)
    ops.uniaxialMaterial('LimitState', 31013, 37.85469032, 9.602e-05, 113.56407096, 0.00028805, 378.54690321, 0.00096018, -37.85469032, -9.602e-05, -113.56407096, -0.00028805, -378.54690321, -0.00096018, 0.4, 0.3, 0.003, 0.0, 0.0, 11013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1013, 99999, 'P', 41013, 'Vy', 31013, 'Vz', 21013, 'My', 11013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171013, 71013, 171013, 1013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122013, 122013, 22013, 1013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171014, 7.3, 7.3, 3.0)
    ops.node(122014, 7.3, 7.3, 4.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1014, 171014, 122014, 0.2025, 25627691.6281012, 10678204.84504217, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21014, 177.37097494, 0.00083099, 216.29419208, 0.01310895, 21.62941921, 0.04612961, -177.37097494, -0.00083099, -216.29419208, -0.01310895, -21.62941921, -0.04612961, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11014, 143.31325771, 0.00083099, 174.76267074, 0.01310895, 17.47626707, 0.04612961, -143.31325771, -0.00083099, -174.76267074, -0.01310895, -17.47626707, -0.04612961, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21014, 1014, 0.0, 174.24258659, 0.01661987, 174.24258659, 0.04985962, 121.96981062, -2105.39595486, 0.05, 2, 0, 71014, 22014, 2, 3)
    ops.uniaxialMaterial('LimitState', 41014, 43.56064665, 6.406e-05, 130.68193995, 0.00019218, 435.60646648, 0.00064062, -43.56064665, -6.406e-05, -130.68193995, -0.00019218, -435.60646648, -0.00064062, 0.4, 0.3, 0.003, 0.0, 0.0, 21014, 2)
    ops.limitCurve('ThreePoint', 11014, 1014, 0.0, 174.24258659, 0.01661987, 174.24258659, 0.04985962, 121.96981062, -2105.39595486, 0.05, 2, 0, 71014, 22014, 1, 3)
    ops.uniaxialMaterial('LimitState', 31014, 43.56064665, 6.406e-05, 130.68193995, 0.00019218, 435.60646648, 0.00064062, -43.56064665, -6.406e-05, -130.68193995, -0.00019218, -435.60646648, -0.00064062, 0.4, 0.3, 0.003, 0.0, 0.0, 11014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1014, 99999, 'P', 41014, 'Vy', 31014, 'Vz', 21014, 'My', 11014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171014, 71014, 171014, 1014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122014, 122014, 22014, 1014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171015, 14.6, 7.3, 3.0)
    ops.node(122015, 14.6, 7.3, 4.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1015, 171015, 122015, 0.1225, 26532138.40400457, 11055057.66833524, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21015, 85.31209697, 0.00090856, 103.79897123, 0.01832189, 10.37989712, 0.05739023, -85.31209697, -0.00090856, -103.79897123, -0.01832189, -10.37989712, -0.05739023, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11015, 73.94777553, 0.00090856, 89.9720356, 0.01832189, 8.99720356, 0.05739023, -73.94777553, -0.00090856, -89.9720356, -0.01832189, -8.99720356, -0.05739023, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21015, 1015, 0.0, 122.82864345, 0.01817125, 122.82864345, 0.05451375, 85.98005041, -1976.06410418, 0.05, 2, 0, 71015, 22015, 2, 3)
    ops.uniaxialMaterial('LimitState', 41015, 30.70716086, 7.211e-05, 92.12148258, 0.00021632, 307.07160861, 0.00072106, -30.70716086, -7.211e-05, -92.12148258, -0.00021632, -307.07160861, -0.00072106, 0.4, 0.3, 0.003, 0.0, 0.0, 21015, 2)
    ops.limitCurve('ThreePoint', 11015, 1015, 0.0, 122.82864345, 0.01817125, 122.82864345, 0.05451375, 85.98005041, -1976.06410418, 0.05, 2, 0, 71015, 22015, 1, 3)
    ops.uniaxialMaterial('LimitState', 31015, 30.70716086, 7.211e-05, 92.12148258, 0.00021632, 307.07160861, 0.00072106, -30.70716086, -7.211e-05, -92.12148258, -0.00021632, -307.07160861, -0.00072106, 0.4, 0.3, 0.003, 0.0, 0.0, 11015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1015, 99999, 'P', 41015, 'Vy', 31015, 'Vz', 21015, 'My', 11015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171015, 71015, 171015, 1015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122015, 122015, 22015, 1015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171016, 17.65, 7.3, 3.0)
    ops.node(122016, 17.65, 7.3, 4.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1016, 171016, 122016, 0.1225, 27270427.59172032, 11362678.1632168, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21016, 92.22521743, 0.00093234, 112.11306035, 0.01588922, 11.21130604, 0.05592594, -92.22521743, -0.00093234, -112.11306035, -0.01588922, -11.21130604, -0.05592594, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11016, 78.96577797, 0.00093234, 95.99429828, 0.01588922, 9.59942983, 0.05592594, -78.96577797, -0.00093234, -95.99429828, -0.01588922, -9.59942983, -0.05592594, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21016, 1016, 0.0, 119.67850472, 0.01864671, 119.67850472, 0.05594013, 83.7749533, -1731.92896859, 0.05, 2, 0, 71016, 22016, 2, 3)
    ops.uniaxialMaterial('LimitState', 41016, 29.91962618, 6.835e-05, 89.75887854, 0.00020506, 299.19626179, 0.00068354, -29.91962618, -6.835e-05, -89.75887854, -0.00020506, -299.19626179, -0.00068354, 0.4, 0.3, 0.003, 0.0, 0.0, 21016, 2)
    ops.limitCurve('ThreePoint', 11016, 1016, 0.0, 119.67850472, 0.01864671, 119.67850472, 0.05594013, 83.7749533, -1731.92896859, 0.05, 2, 0, 71016, 22016, 1, 3)
    ops.uniaxialMaterial('LimitState', 31016, 29.91962618, 6.835e-05, 89.75887854, 0.00020506, 299.19626179, 0.00068354, -29.91962618, -6.835e-05, -89.75887854, -0.00020506, -299.19626179, -0.00068354, 0.4, 0.3, 0.003, 0.0, 0.0, 11016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1016, 99999, 'P', 41016, 'Vy', 31016, 'Vz', 21016, 'My', 11016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171016, 71016, 171016, 1016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122016, 122016, 22016, 1016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171017, 24.95, 7.3, 3.0)
    ops.node(122017, 24.95, 7.3, 4.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1017, 171017, 122017, 0.2025, 25479924.09391183, 10616635.03912993, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21017, 170.72634101, 0.00085953, 208.21705614, 0.01392806, 20.82170561, 0.04677557, -170.72634101, -0.00085953, -208.21705614, -0.01392806, -20.82170561, -0.04677557, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11017, 140.83009698, 0.00085953, 171.75573515, 0.01392806, 17.17557351, 0.04677557, -140.83009698, -0.00085953, -171.75573515, -0.01392806, -17.17557351, -0.04677557, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21017, 1017, 0.0, 174.67320553, 0.01719062, 174.67320553, 0.05157187, 122.27124387, -2156.09035944, 0.05, 2, 0, 71017, 22017, 2, 3)
    ops.uniaxialMaterial('LimitState', 41017, 43.66830138, 6.459e-05, 131.00490415, 0.00019378, 436.68301383, 0.00064592, -43.66830138, -6.459e-05, -131.00490415, -0.00019378, -436.68301383, -0.00064592, 0.4, 0.3, 0.003, 0.0, 0.0, 21017, 2)
    ops.limitCurve('ThreePoint', 11017, 1017, 0.0, 174.67320553, 0.01719062, 174.67320553, 0.05157187, 122.27124387, -2156.09035944, 0.05, 2, 0, 71017, 22017, 1, 3)
    ops.uniaxialMaterial('LimitState', 31017, 43.66830138, 6.459e-05, 131.00490415, 0.00019378, 436.68301383, 0.00064592, -43.66830138, -6.459e-05, -131.00490415, -0.00019378, -436.68301383, -0.00064592, 0.4, 0.3, 0.003, 0.0, 0.0, 11017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1017, 99999, 'P', 41017, 'Vy', 31017, 'Vz', 21017, 'My', 11017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171017, 71017, 171017, 1017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122017, 122017, 22017, 1017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171018, 32.25, 7.3, 3.0)
    ops.node(122018, 32.25, 7.3, 4.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1018, 171018, 122018, 0.1225, 28372971.32706002, 11822071.38627501, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21018, 108.01557891, 0.00094538, 131.30598865, 0.03591967, 13.13059887, 0.10068902, -108.01557891, -0.00094538, -131.30598865, -0.03591967, -13.13059887, -0.10068902, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11018, 93.25412586, 0.00094538, 113.36165871, 0.03591967, 11.33616587, 0.10068902, -93.25412586, -0.00094538, -113.36165871, -0.03591967, -11.33616587, -0.10068902, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21018, 1018, 0.0, 146.78066066, 0.01890756, 146.78066066, 0.05672267, 102.74646246, -3313.47618947, 0.05, 2, 0, 71018, 22018, 2, 3)
    ops.uniaxialMaterial('LimitState', 41018, 36.69516517, 8.058e-05, 110.0854955, 0.00024173, 366.95165166, 0.00080576, -36.69516517, -8.058e-05, -110.0854955, -0.00024173, -366.95165166, -0.00080576, 0.4, 0.3, 0.003, 0.0, 0.0, 21018, 2)
    ops.limitCurve('ThreePoint', 11018, 1018, 0.0, 146.78066066, 0.01890756, 146.78066066, 0.05672267, 102.74646246, -3313.47618947, 0.05, 2, 0, 71018, 22018, 1, 3)
    ops.uniaxialMaterial('LimitState', 31018, 36.69516517, 8.058e-05, 110.0854955, 0.00024173, 366.95165166, 0.00080576, -36.69516517, -8.058e-05, -110.0854955, -0.00024173, -366.95165166, -0.00080576, 0.4, 0.3, 0.003, 0.0, 0.0, 11018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1018, 99999, 'P', 41018, 'Vy', 31018, 'Vz', 21018, 'My', 11018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171018, 71018, 171018, 1018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122018, 122018, 22018, 1018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172001, 0.0, 0.0, 5.65)
    ops.node(123001, 0.0, 0.0, 7.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2001, 172001, 123001, 0.0625, 27364793.8075369, 11401997.41980704, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22001, 42.42143875, 0.00129067, 51.5957946, 0.02041573, 5.15957946, 0.06636234, -42.42143875, -0.00129067, -51.5957946, -0.02041573, -5.15957946, -0.06636234, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12001, 42.42143875, 0.00129067, 51.5957946, 0.02041573, 5.15957946, 0.06636234, -42.42143875, -0.00129067, -51.5957946, -0.02041573, -5.15957946, -0.06636234, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22001, 2001, 0.0, 48.21102811, 0.02581331, 48.21102811, 0.07743992, 33.74771968, -1247.89060778, 0.05, 2, 0, 72001, 23001, 2, 3)
    ops.uniaxialMaterial('LimitState', 42001, 12.05275703, 5.378e-05, 36.15827109, 0.00016135, 120.52757029, 0.00053784, -12.05275703, -5.378e-05, -36.15827109, -0.00016135, -120.52757029, -0.00053784, 0.4, 0.3, 0.003, 0.0, 0.0, 22001, 2)
    ops.limitCurve('ThreePoint', 12001, 2001, 0.0, 48.21102811, 0.02581331, 48.21102811, 0.07743992, 33.74771968, -1247.89060778, 0.05, 2, 0, 72001, 23001, 1, 3)
    ops.uniaxialMaterial('LimitState', 32001, 12.05275703, 5.378e-05, 36.15827109, 0.00016135, 120.52757029, 0.00053784, -12.05275703, -5.378e-05, -36.15827109, -0.00016135, -120.52757029, -0.00053784, 0.4, 0.3, 0.003, 0.0, 0.0, 12001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2001, 99999, 'P', 42001, 'Vy', 32001, 'Vz', 22001, 'My', 12001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172001, 72001, 172001, 2001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123001, 123001, 23001, 2001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172002, 7.3, 0.0, 5.65)
    ops.node(123002, 7.3, 0.0, 7.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2002, 172002, 123002, 0.1225, 27502014.1356547, 11459172.55652279, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22002, 80.45003497, 0.00096756, 97.8773834, 0.01797698, 9.78773834, 0.05966595, -80.45003497, -0.00096756, -97.8773834, -0.01797698, -9.78773834, -0.05966595, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12002, 70.91232374, 0.00096756, 86.27358212, 0.01797698, 8.62735821, 0.05966595, -70.91232374, -0.00096756, -86.27358212, -0.01797698, -8.62735821, -0.05966595, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22002, 2002, 0.0, 122.96797164, 0.01935121, 122.96797164, 0.05805363, 86.07758015, -1983.41210816, 0.05, 2, 0, 72002, 23002, 2, 3)
    ops.uniaxialMaterial('LimitState', 42002, 30.74199291, 6.964e-05, 92.22597873, 0.00020893, 307.41992911, 0.00069642, -30.74199291, -6.964e-05, -92.22597873, -0.00020893, -307.41992911, -0.00069642, 0.4, 0.3, 0.003, 0.0, 0.0, 22002, 2)
    ops.limitCurve('ThreePoint', 12002, 2002, 0.0, 122.96797164, 0.01935121, 122.96797164, 0.05805363, 86.07758015, -1983.41210816, 0.05, 2, 0, 72002, 23002, 1, 3)
    ops.uniaxialMaterial('LimitState', 32002, 30.74199291, 6.964e-05, 92.22597873, 0.00020893, 307.41992911, 0.00069642, -30.74199291, -6.964e-05, -92.22597873, -0.00020893, -307.41992911, -0.00069642, 0.4, 0.3, 0.003, 0.0, 0.0, 12002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2002, 99999, 'P', 42002, 'Vy', 32002, 'Vz', 22002, 'My', 12002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172002, 72002, 172002, 2002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123002, 123002, 23002, 2002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172005, 24.95, 0.0, 5.65)
    ops.node(123005, 24.95, 0.0, 7.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2005, 172005, 123005, 0.1225, 26768059.92980502, 11153358.30408542, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22005, 80.58014027, 0.00092097, 98.13672731, 0.01392146, 9.81367273, 0.0547727, -80.58014027, -0.00092097, -98.13672731, -0.01392146, -9.81367273, -0.0547727, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12005, 70.15319854, 0.00092097, 85.4379912, 0.01392146, 8.54379912, 0.0547727, -70.15319854, -0.00092097, -85.4379912, -0.01392146, -8.54379912, -0.0547727, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22005, 2005, 0.0, 111.97656819, 0.01841934, 111.97656819, 0.05525801, 78.38359773, -1602.10543373, 0.05, 2, 0, 72005, 23005, 2, 3)
    ops.uniaxialMaterial('LimitState', 42005, 27.99414205, 6.516e-05, 83.98242614, 0.00019547, 279.94142047, 0.00065156, -27.99414205, -6.516e-05, -83.98242614, -0.00019547, -279.94142047, -0.00065156, 0.4, 0.3, 0.003, 0.0, 0.0, 22005, 2)
    ops.limitCurve('ThreePoint', 12005, 2005, 0.0, 111.97656819, 0.01841934, 111.97656819, 0.05525801, 78.38359773, -1602.10543373, 0.05, 2, 0, 72005, 23005, 1, 3)
    ops.uniaxialMaterial('LimitState', 32005, 27.99414205, 6.516e-05, 83.98242614, 0.00019547, 279.94142047, 0.00065156, -27.99414205, -6.516e-05, -83.98242614, -0.00019547, -279.94142047, -0.00065156, 0.4, 0.3, 0.003, 0.0, 0.0, 12005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2005, 99999, 'P', 42005, 'Vy', 32005, 'Vz', 22005, 'My', 12005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172005, 72005, 172005, 2005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123005, 123005, 23005, 2005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172006, 32.25, 0.0, 5.65)
    ops.node(123006, 32.25, 0.0, 7.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2006, 172006, 123006, 0.0625, 29571098.93943129, 12321291.22476304, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22006, 41.98579204, 0.00177215, 50.86351233, 0.01786366, 5.08635123, 0.06632165, -41.98579204, -0.00177215, -50.86351233, -0.01786366, -5.08635123, -0.06632165, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12006, 41.98579204, 0.00177215, 50.86351233, 0.01786366, 5.08635123, 0.06632165, -41.98579204, -0.00177215, -50.86351233, -0.01786366, -5.08635123, -0.06632165, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22006, 2006, 0.0, 41.05532536, 0.03544304, 41.05532536, 0.10632912, 28.73872775, -1036.96711151, 0.05, 2, 0, 72006, 23006, 2, 3)
    ops.uniaxialMaterial('LimitState', 42006, 10.26383134, 4.238e-05, 30.79149402, 0.00012715, 102.6383134, 0.00042384, -10.26383134, -4.238e-05, -30.79149402, -0.00012715, -102.6383134, -0.00042384, 0.4, 0.3, 0.003, 0.0, 0.0, 22006, 2)
    ops.limitCurve('ThreePoint', 12006, 2006, 0.0, 41.05532536, 0.03544304, 41.05532536, 0.10632912, 28.73872775, -1036.96711151, 0.05, 2, 0, 72006, 23006, 1, 3)
    ops.uniaxialMaterial('LimitState', 32006, 10.26383134, 4.238e-05, 30.79149402, 0.00012715, 102.6383134, 0.00042384, -10.26383134, -4.238e-05, -30.79149402, -0.00012715, -102.6383134, -0.00042384, 0.4, 0.3, 0.003, 0.0, 0.0, 12006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2006, 99999, 'P', 42006, 'Vy', 32006, 'Vz', 22006, 'My', 12006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172006, 72006, 172006, 2006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123006, 123006, 23006, 2006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172007, 0.0, 3.65, 5.65)
    ops.node(123007, 0.0, 3.65, 7.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2007, 172007, 123007, 0.1225, 27973264.05106907, 11655526.68794545, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22007, 131.50262267, 0.00111563, 160.00352429, 0.03404444, 16.00035243, 0.08528046, -131.50262267, -0.00111563, -160.00352429, -0.03404444, -16.00035243, -0.08528046, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12007, 121.08265783, 0.00111563, 147.32521366, 0.03404444, 14.73252137, 0.08528046, -121.08265783, -0.00111563, -147.32521366, -0.03404444, -14.73252137, -0.08528046, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22007, 2007, 0.0, 142.7638903, 0.0223127, 142.7638903, 0.0669381, 99.93472321, -3211.91786982, 0.05, 2, 0, 72007, 23007, 2, 3)
    ops.uniaxialMaterial('LimitState', 42007, 35.69097258, 7.949e-05, 107.07291773, 0.00023847, 356.90972576, 0.00079491, -35.69097258, -7.949e-05, -107.07291773, -0.00023847, -356.90972576, -0.00079491, 0.4, 0.3, 0.003, 0.0, 0.0, 22007, 2)
    ops.limitCurve('ThreePoint', 12007, 2007, 0.0, 142.7638903, 0.0223127, 142.7638903, 0.0669381, 99.93472321, -3211.91786982, 0.05, 2, 0, 72007, 23007, 1, 3)
    ops.uniaxialMaterial('LimitState', 32007, 35.69097258, 7.949e-05, 107.07291773, 0.00023847, 356.90972576, 0.00079491, -35.69097258, -7.949e-05, -107.07291773, -0.00023847, -356.90972576, -0.00079491, 0.4, 0.3, 0.003, 0.0, 0.0, 12007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2007, 99999, 'P', 42007, 'Vy', 32007, 'Vz', 22007, 'My', 12007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172007, 72007, 172007, 2007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123007, 123007, 23007, 2007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172008, 7.3, 3.65, 5.65)
    ops.node(123008, 7.3, 3.65, 7.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2008, 172008, 123008, 0.1225, 25139062.19864048, 10474609.24943353, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22008, 103.12523769, 0.00106203, 125.37590137, 0.01430566, 12.53759014, 0.04504268, -103.12523769, -0.00106203, -125.37590137, -0.01430566, -12.53759014, -0.04504268, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12008, 96.58639003, 0.00106203, 117.42620897, 0.01430566, 11.7426209, 0.04504268, -96.58639003, -0.00106203, -117.42620897, -0.01430566, -11.7426209, -0.04504268, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22008, 2008, 0.0, 102.96525741, 0.02124053, 102.96525741, 0.06372158, 72.07568019, -1289.23405334, 0.05, 2, 0, 72008, 23008, 2, 3)
    ops.uniaxialMaterial('LimitState', 42008, 25.74131435, 6.379e-05, 77.22394306, 0.00019138, 257.41314353, 0.00063795, -25.74131435, -6.379e-05, -77.22394306, -0.00019138, -257.41314353, -0.00063795, 0.4, 0.3, 0.003, 0.0, 0.0, 22008, 2)
    ops.limitCurve('ThreePoint', 12008, 2008, 0.0, 102.96525741, 0.02124053, 102.96525741, 0.06372158, 72.07568019, -1289.23405334, 0.05, 2, 0, 72008, 23008, 1, 3)
    ops.uniaxialMaterial('LimitState', 32008, 25.74131435, 6.379e-05, 77.22394306, 0.00019138, 257.41314353, 0.00063795, -25.74131435, -6.379e-05, -77.22394306, -0.00019138, -257.41314353, -0.00063795, 0.4, 0.3, 0.003, 0.0, 0.0, 12008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2008, 99999, 'P', 42008, 'Vy', 32008, 'Vz', 22008, 'My', 12008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172008, 72008, 172008, 2008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123008, 123008, 23008, 2008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172009, 14.6, 3.65, 5.65)
    ops.node(123009, 14.6, 3.65, 7.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2009, 172009, 123009, 0.1225, 28802688.24714015, 12001120.10297506, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22009, 113.84224143, 0.00106319, 138.10613576, 0.02447783, 13.81061358, 0.0667106, -113.84224143, -0.00106319, -138.10613576, -0.02447783, -13.81061358, -0.0667106, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12009, 113.84224143, 0.00106319, 138.10613576, 0.02447783, 13.81061358, 0.0667106, -113.84224143, -0.00106319, -138.10613576, -0.02447783, -13.81061358, -0.0667106, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22009, 2009, 0.0, 128.48937944, 0.02126383, 128.48937944, 0.06379148, 89.94256561, -1926.03499352, 0.05, 2, 0, 72009, 23009, 2, 3)
    ops.uniaxialMaterial('LimitState', 42009, 32.12234486, 6.948e-05, 96.36703458, 0.00020845, 321.2234486, 0.00069483, -32.12234486, -6.948e-05, -96.36703458, -0.00020845, -321.2234486, -0.00069483, 0.4, 0.3, 0.003, 0.0, 0.0, 22009, 2)
    ops.limitCurve('ThreePoint', 12009, 2009, 0.0, 128.48937944, 0.02126383, 128.48937944, 0.06379148, 89.94256561, -1926.03499352, 0.05, 2, 0, 72009, 23009, 1, 3)
    ops.uniaxialMaterial('LimitState', 32009, 32.12234486, 6.948e-05, 96.36703458, 0.00020845, 321.2234486, 0.00069483, -32.12234486, -6.948e-05, -96.36703458, -0.00020845, -321.2234486, -0.00069483, 0.4, 0.3, 0.003, 0.0, 0.0, 12009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2009, 99999, 'P', 42009, 'Vy', 32009, 'Vz', 22009, 'My', 12009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172009, 72009, 172009, 2009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123009, 123009, 23009, 2009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172010, 17.65, 3.65, 5.65)
    ops.node(123010, 17.65, 3.65, 7.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2010, 172010, 123010, 0.1225, 32318170.82684648, 13465904.51118603, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22010, 104.30952177, 0.00099728, 125.44900286, 0.02482408, 12.54490029, 0.06986836, -104.30952177, -0.00099728, -125.44900286, -0.02482408, -12.54490029, -0.06986836, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12010, 104.30952177, 0.00099728, 125.44900286, 0.02482408, 12.54490029, 0.06986836, -104.30952177, -0.00099728, -125.44900286, -0.02482408, -12.54490029, -0.06986836, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22010, 2010, 0.0, 140.08397081, 0.01994566, 140.08397081, 0.05983698, 98.05877957, -1858.03088668, 0.05, 2, 0, 72010, 23010, 2, 3)
    ops.uniaxialMaterial('LimitState', 42010, 35.0209927, 6.751e-05, 105.06297811, 0.00020254, 350.20992702, 0.00067512, -35.0209927, -6.751e-05, -105.06297811, -0.00020254, -350.20992702, -0.00067512, 0.4, 0.3, 0.003, 0.0, 0.0, 22010, 2)
    ops.limitCurve('ThreePoint', 12010, 2010, 0.0, 140.08397081, 0.01994566, 140.08397081, 0.05983698, 98.05877957, -1858.03088668, 0.05, 2, 0, 72010, 23010, 1, 3)
    ops.uniaxialMaterial('LimitState', 32010, 35.0209927, 6.751e-05, 105.06297811, 0.00020254, 350.20992702, 0.00067512, -35.0209927, -6.751e-05, -105.06297811, -0.00020254, -350.20992702, -0.00067512, 0.4, 0.3, 0.003, 0.0, 0.0, 12010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2010, 99999, 'P', 42010, 'Vy', 32010, 'Vz', 22010, 'My', 12010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172010, 72010, 172010, 2010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123010, 123010, 23010, 2010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172011, 24.95, 3.65, 5.65)
    ops.node(123011, 24.95, 3.65, 7.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2011, 172011, 123011, 0.1225, 27469593.70963404, 11445664.04568085, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22011, 95.81435604, 0.00098748, 116.28780352, 0.01957375, 11.62878035, 0.05353008, -95.81435604, -0.00098748, -116.28780352, -0.01957375, -11.62878035, -0.05353008, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12011, 90.41650256, 0.00098748, 109.73654595, 0.01957375, 10.97365459, 0.05353008, -90.41650256, -0.00098748, -109.73654595, -0.01957375, -10.97365459, -0.05353008, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22011, 2011, 0.0, 118.38643613, 0.01974969, 118.38643613, 0.05924908, 82.87050529, -1544.59098747, 0.05, 2, 0, 72011, 23011, 2, 3)
    ops.uniaxialMaterial('LimitState', 42011, 29.59660903, 6.713e-05, 88.7898271, 0.00020138, 295.96609032, 0.00067126, -29.59660903, -6.713e-05, -88.7898271, -0.00020138, -295.96609032, -0.00067126, 0.4, 0.3, 0.003, 0.0, 0.0, 22011, 2)
    ops.limitCurve('ThreePoint', 12011, 2011, 0.0, 118.38643613, 0.01974969, 118.38643613, 0.05924908, 82.87050529, -1544.59098747, 0.05, 2, 0, 72011, 23011, 1, 3)
    ops.uniaxialMaterial('LimitState', 32011, 29.59660903, 6.713e-05, 88.7898271, 0.00020138, 295.96609032, 0.00067126, -29.59660903, -6.713e-05, -88.7898271, -0.00020138, -295.96609032, -0.00067126, 0.4, 0.3, 0.003, 0.0, 0.0, 12011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2011, 99999, 'P', 42011, 'Vy', 32011, 'Vz', 22011, 'My', 12011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172011, 72011, 172011, 2011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123011, 123011, 23011, 2011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172012, 32.25, 3.65, 5.65)
    ops.node(123012, 32.25, 3.65, 7.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2012, 172012, 123012, 0.1225, 30668497.86614798, 12778540.77756166, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22012, 133.10591093, 0.00102713, 160.99192109, 0.03346076, 16.09919211, 0.08716239, -133.10591093, -0.00102713, -160.99192109, -0.03346076, -16.09919211, -0.08716239, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12012, 122.33794185, 0.00102713, 147.96803645, 0.03346076, 14.79680364, 0.08716239, -122.33794185, -0.00102713, -147.96803645, -0.03346076, -14.79680364, -0.08716239, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22012, 2012, 0.0, 150.78402799, 0.02054264, 150.78402799, 0.06162791, 105.54881959, -3101.51120922, 0.05, 2, 0, 72012, 23012, 2, 3)
    ops.uniaxialMaterial('LimitState', 42012, 37.696007, 7.658e-05, 113.08802099, 0.00022973, 376.96006997, 0.00076578, -37.696007, -7.658e-05, -113.08802099, -0.00022973, -376.96006997, -0.00076578, 0.4, 0.3, 0.003, 0.0, 0.0, 22012, 2)
    ops.limitCurve('ThreePoint', 12012, 2012, 0.0, 150.78402799, 0.02054264, 150.78402799, 0.06162791, 105.54881959, -3101.51120922, 0.05, 2, 0, 72012, 23012, 1, 3)
    ops.uniaxialMaterial('LimitState', 32012, 37.696007, 7.658e-05, 113.08802099, 0.00022973, 376.96006997, 0.00076578, -37.696007, -7.658e-05, -113.08802099, -0.00022973, -376.96006997, -0.00076578, 0.4, 0.3, 0.003, 0.0, 0.0, 12012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2012, 99999, 'P', 42012, 'Vy', 32012, 'Vz', 22012, 'My', 12012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172012, 72012, 172012, 2012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123012, 123012, 23012, 2012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172013, 0.0, 7.3, 5.65)
    ops.node(123013, 0.0, 7.3, 7.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2013, 172013, 123013, 0.0625, 26479004.57992667, 11032918.57496945, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22013, 43.191951, 0.00142914, 52.59176309, 0.02265666, 5.25917631, 0.06737547, -43.191951, -0.00142914, -52.59176309, -0.02265666, -5.25917631, -0.06737547, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12013, 43.191951, 0.00142914, 52.59176309, 0.02265666, 5.25917631, 0.06737547, -43.191951, -0.00142914, -52.59176309, -0.02265666, -5.25917631, -0.06737547, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22013, 2013, 0.0, 65.09586243, 0.02858278, 65.09586243, 0.08574835, 45.5671037, -1474.39593014, 0.05, 2, 0, 72013, 23013, 2, 3)
    ops.uniaxialMaterial('LimitState', 42013, 16.27396561, 7.505e-05, 48.82189682, 0.00022515, 162.73965608, 0.0007505, -16.27396561, -7.505e-05, -48.82189682, -0.00022515, -162.73965608, -0.0007505, 0.4, 0.3, 0.003, 0.0, 0.0, 22013, 2)
    ops.limitCurve('ThreePoint', 12013, 2013, 0.0, 65.09586243, 0.02858278, 65.09586243, 0.08574835, 45.5671037, -1474.39593014, 0.05, 2, 0, 72013, 23013, 1, 3)
    ops.uniaxialMaterial('LimitState', 32013, 16.27396561, 7.505e-05, 48.82189682, 0.00022515, 162.73965608, 0.0007505, -16.27396561, -7.505e-05, -48.82189682, -0.00022515, -162.73965608, -0.0007505, 0.4, 0.3, 0.003, 0.0, 0.0, 12013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2013, 99999, 'P', 42013, 'Vy', 32013, 'Vz', 22013, 'My', 12013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172013, 72013, 172013, 2013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123013, 123013, 23013, 2013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172014, 7.3, 7.3, 5.65)
    ops.node(123014, 7.3, 7.3, 7.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2014, 172014, 123014, 0.1225, 27890818.18734644, 11621174.24472768, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22014, 88.8535586, 0.00099497, 108.0342095, 0.01419578, 10.80342095, 0.05629679, -88.8535586, -0.00099497, -108.0342095, -0.01419578, -10.80342095, -0.05629679, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12014, 76.82011753, 0.00099497, 93.4031321, 0.01419578, 9.34031321, 0.05629679, -76.82011753, -0.00099497, -93.4031321, -0.01419578, -9.34031321, -0.05629679, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22014, 2014, 0.0, 114.00516292, 0.0198995, 114.00516292, 0.05969849, 79.80361404, -1522.89780835, 0.05, 2, 0, 72014, 23014, 2, 3)
    ops.uniaxialMaterial('LimitState', 42014, 28.50129073, 6.367e-05, 85.50387219, 0.000191, 285.0129073, 0.00063666, -28.50129073, -6.367e-05, -85.50387219, -0.000191, -285.0129073, -0.00063666, 0.4, 0.3, 0.003, 0.0, 0.0, 22014, 2)
    ops.limitCurve('ThreePoint', 12014, 2014, 0.0, 114.00516292, 0.0198995, 114.00516292, 0.05969849, 79.80361404, -1522.89780835, 0.05, 2, 0, 72014, 23014, 1, 3)
    ops.uniaxialMaterial('LimitState', 32014, 28.50129073, 6.367e-05, 85.50387219, 0.000191, 285.0129073, 0.00063666, -28.50129073, -6.367e-05, -85.50387219, -0.000191, -285.0129073, -0.00063666, 0.4, 0.3, 0.003, 0.0, 0.0, 12014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2014, 99999, 'P', 42014, 'Vy', 32014, 'Vz', 22014, 'My', 12014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172014, 72014, 172014, 2014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123014, 123014, 23014, 2014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172015, 14.6, 7.3, 5.65)
    ops.node(123015, 14.6, 7.3, 7.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2015, 172015, 123015, 0.0625, 27021734.7892512, 11259056.162188, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22015, 31.12821948, 0.00138469, 37.78859102, 0.01565578, 3.7788591, 0.0645568, -31.12821948, -0.00138469, -37.78859102, -0.01565578, -3.7788591, -0.0645568, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12015, 31.12821948, 0.00138469, 37.78859102, 0.01565578, 3.7788591, 0.0645568, -31.12821948, -0.00138469, -37.78859102, -0.01565578, -3.7788591, -0.0645568, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22015, 2015, 0.0, 56.96193524, 0.02769387, 56.96193524, 0.08308161, 39.87335467, -1282.93519435, 0.05, 2, 0, 72015, 23015, 2, 3)
    ops.uniaxialMaterial('LimitState', 42015, 14.24048381, 6.435e-05, 42.72145143, 0.00019306, 142.40483811, 0.00064353, -14.24048381, -6.435e-05, -42.72145143, -0.00019306, -142.40483811, -0.00064353, 0.4, 0.3, 0.003, 0.0, 0.0, 22015, 2)
    ops.limitCurve('ThreePoint', 12015, 2015, 0.0, 56.96193524, 0.02769387, 56.96193524, 0.08308161, 39.87335467, -1282.93519435, 0.05, 2, 0, 72015, 23015, 1, 3)
    ops.uniaxialMaterial('LimitState', 32015, 14.24048381, 6.435e-05, 42.72145143, 0.00019306, 142.40483811, 0.00064353, -14.24048381, -6.435e-05, -42.72145143, -0.00019306, -142.40483811, -0.00064353, 0.4, 0.3, 0.003, 0.0, 0.0, 12015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2015, 99999, 'P', 42015, 'Vy', 32015, 'Vz', 22015, 'My', 12015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172015, 72015, 172015, 2015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123015, 123015, 23015, 2015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172016, 17.65, 7.3, 5.65)
    ops.node(123016, 17.65, 7.3, 7.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2016, 172016, 123016, 0.0625, 27078712.61291431, 11282796.92204763, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22016, 32.75113811, 0.00118452, 39.75644663, 0.01807282, 3.97564466, 0.06708141, -32.75113811, -0.00118452, -39.75644663, -0.01807282, -3.97564466, -0.06708141, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12016, 32.75113811, 0.00118452, 39.75644663, 0.01807282, 3.97564466, 0.06708141, -32.75113811, -0.00118452, -39.75644663, -0.01807282, -3.97564466, -0.06708141, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22016, 2016, 0.0, 71.85257655, 0.02369037, 71.85257655, 0.0710711, 50.29680358, -1346.20381308, 0.05, 2, 0, 72016, 23016, 2, 3)
    ops.uniaxialMaterial('LimitState', 42016, 17.96314414, 8.101e-05, 53.88943241, 0.00024302, 179.63144137, 0.00081005, -17.96314414, -8.101e-05, -53.88943241, -0.00024302, -179.63144137, -0.00081005, 0.4, 0.3, 0.003, 0.0, 0.0, 22016, 2)
    ops.limitCurve('ThreePoint', 12016, 2016, 0.0, 71.85257655, 0.02369037, 71.85257655, 0.0710711, 50.29680358, -1346.20381308, 0.05, 2, 0, 72016, 23016, 1, 3)
    ops.uniaxialMaterial('LimitState', 32016, 17.96314414, 8.101e-05, 53.88943241, 0.00024302, 179.63144137, 0.00081005, -17.96314414, -8.101e-05, -53.88943241, -0.00024302, -179.63144137, -0.00081005, 0.4, 0.3, 0.003, 0.0, 0.0, 12016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2016, 99999, 'P', 42016, 'Vy', 32016, 'Vz', 22016, 'My', 12016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172016, 72016, 172016, 2016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123016, 123016, 23016, 2016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172017, 24.95, 7.3, 5.65)
    ops.node(123017, 24.95, 7.3, 7.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2017, 172017, 123017, 0.1225, 29415860.18708752, 12256608.41128647, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22017, 89.99410412, 0.00092318, 109.10207382, 0.01909785, 10.91020738, 0.062628, -89.99410412, -0.00092318, -109.10207382, -0.01909785, -10.91020738, -0.062628, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12017, 77.03142229, 0.00092318, 93.38709468, 0.01909785, 9.33870947, 0.062628, -77.03142229, -0.00092318, -93.38709468, -0.01909785, -9.33870947, -0.062628, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22017, 2017, 0.0, 138.33162347, 0.0184636, 138.33162347, 0.0553908, 96.83213643, -2410.22176006, 0.05, 2, 0, 72017, 23017, 2, 3)
    ops.uniaxialMaterial('LimitState', 42017, 34.58290587, 7.325e-05, 103.7487176, 0.00021974, 345.82905866, 0.00073246, -34.58290587, -7.325e-05, -103.7487176, -0.00021974, -345.82905866, -0.00073246, 0.4, 0.3, 0.003, 0.0, 0.0, 22017, 2)
    ops.limitCurve('ThreePoint', 12017, 2017, 0.0, 138.33162347, 0.0184636, 138.33162347, 0.0553908, 96.83213643, -2410.22176006, 0.05, 2, 0, 72017, 23017, 1, 3)
    ops.uniaxialMaterial('LimitState', 32017, 34.58290587, 7.325e-05, 103.7487176, 0.00021974, 345.82905866, 0.00073246, -34.58290587, -7.325e-05, -103.7487176, -0.00021974, -345.82905866, -0.00073246, 0.4, 0.3, 0.003, 0.0, 0.0, 12017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2017, 99999, 'P', 42017, 'Vy', 32017, 'Vz', 22017, 'My', 12017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172017, 72017, 172017, 2017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123017, 123017, 23017, 2017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172018, 32.25, 7.3, 5.65)
    ops.node(123018, 32.25, 7.3, 7.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2018, 172018, 123018, 0.0625, 27691366.73448351, 11538069.47270146, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22018, 43.60310688, 0.00136757, 53.00738689, 0.02207728, 5.30073869, 0.06844203, -43.60310688, -0.00136757, -53.00738689, -0.02207728, -5.30073869, -0.06844203, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12018, 43.60310688, 0.00136757, 53.00738689, 0.02207728, 5.30073869, 0.06844203, -43.60310688, -0.00136757, -53.00738689, -0.02207728, -5.30073869, -0.06844203, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22018, 2018, 0.0, 60.61282606, 0.02735132, 60.61282606, 0.08205396, 42.42897824, -1251.27557628, 0.05, 2, 0, 72018, 23018, 2, 3)
    ops.uniaxialMaterial('LimitState', 42018, 15.15320651, 6.682e-05, 45.45961954, 0.00020047, 151.53206515, 0.00066822, -15.15320651, -6.682e-05, -45.45961954, -0.00020047, -151.53206515, -0.00066822, 0.4, 0.3, 0.003, 0.0, 0.0, 22018, 2)
    ops.limitCurve('ThreePoint', 12018, 2018, 0.0, 60.61282606, 0.02735132, 60.61282606, 0.08205396, 42.42897824, -1251.27557628, 0.05, 2, 0, 72018, 23018, 1, 3)
    ops.uniaxialMaterial('LimitState', 32018, 15.15320651, 6.682e-05, 45.45961954, 0.00020047, 151.53206515, 0.00066822, -15.15320651, -6.682e-05, -45.45961954, -0.00020047, -151.53206515, -0.00066822, 0.4, 0.3, 0.003, 0.0, 0.0, 12018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2018, 99999, 'P', 42018, 'Vy', 32018, 'Vz', 22018, 'My', 12018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172018, 72018, 172018, 2018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123018, 123018, 23018, 2018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173001, 0.0, 0.0, 8.3)
    ops.node(124001, 0.0, 0.0, 10.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3001, 173001, 124001, 0.0625, 31959918.2927652, 13316632.6219855, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23001, 47.63403515, 0.00117199, 57.55342056, 0.01711553, 5.75534206, 0.07306489, -47.63403515, -0.00117199, -57.55342056, -0.01711553, -5.75534206, -0.07306489, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13001, 44.04191927, 0.00117199, 53.21327689, 0.01711553, 5.32132769, 0.07306489, -44.04191927, -0.00117199, -53.21327689, -0.01711553, -5.32132769, -0.07306489, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23001, 3001, 0.0, 39.05302323, 0.02343973, 39.05302323, 0.0703192, 27.33711626, -1907.97625825, 0.05, 2, 0, 73001, 24001, 2, 3)
    ops.uniaxialMaterial('LimitState', 43001, 9.76325581, 3.73e-05, 29.28976742, 0.00011191, 97.63255807, 0.00037303, -9.76325581, -3.73e-05, -29.28976742, -0.00011191, -97.63255807, -0.00037303, 0.4, 0.3, 0.003, 0.0, 0.0, 23001, 2)
    ops.limitCurve('ThreePoint', 13001, 3001, 0.0, 39.05302323, 0.02343973, 39.05302323, 0.0703192, 27.33711626, -1907.97625825, 0.05, 2, 0, 73001, 24001, 1, 3)
    ops.uniaxialMaterial('LimitState', 33001, 9.76325581, 3.73e-05, 29.28976742, 0.00011191, 97.63255807, 0.00037303, -9.76325581, -3.73e-05, -29.28976742, -0.00011191, -97.63255807, -0.00037303, 0.4, 0.3, 0.003, 0.0, 0.0, 13001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3001, 99999, 'P', 43001, 'Vy', 33001, 'Vz', 23001, 'My', 13001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173001, 73001, 173001, 3001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124001, 124001, 24001, 3001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173002, 7.3, 0.0, 8.3)
    ops.node(124002, 7.3, 0.0, 10.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3002, 173002, 124002, 0.1225, 27745440.79391793, 11560600.33079914, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23002, 64.62581684, 0.00102462, 78.99312329, 0.01436396, 7.89931233, 0.06312886, -64.62581684, -0.00102462, -78.99312329, -0.01436396, -7.89931233, -0.06312886, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13002, 56.93608615, 0.00102462, 69.59384799, 0.01436396, 6.9593848, 0.06312886, -56.93608615, -0.00102462, -69.59384799, -0.01436396, -6.9593848, -0.06312886, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23002, 3002, 0.0, 104.15427846, 0.02049247, 104.15427846, 0.0614774, 72.90799492, -2698.71703086, 0.05, 2, 0, 73002, 24002, 2, 3)
    ops.uniaxialMaterial('LimitState', 43002, 26.03856961, 5.847e-05, 78.11570884, 0.00017541, 260.38569614, 0.00058469, -26.03856961, -5.847e-05, -78.11570884, -0.00017541, -260.38569614, -0.00058469, 0.4, 0.3, 0.003, 0.0, 0.0, 23002, 2)
    ops.limitCurve('ThreePoint', 13002, 3002, 0.0, 104.15427846, 0.02049247, 104.15427846, 0.0614774, 72.90799492, -2698.71703086, 0.05, 2, 0, 73002, 24002, 1, 3)
    ops.uniaxialMaterial('LimitState', 33002, 26.03856961, 5.847e-05, 78.11570884, 0.00017541, 260.38569614, 0.00058469, -26.03856961, -5.847e-05, -78.11570884, -0.00017541, -260.38569614, -0.00058469, 0.4, 0.3, 0.003, 0.0, 0.0, 13002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3002, 99999, 'P', 43002, 'Vy', 33002, 'Vz', 23002, 'My', 13002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173002, 73002, 173002, 3002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124002, 124002, 24002, 3002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173005, 24.95, 0.0, 8.3)
    ops.node(124005, 24.95, 0.0, 10.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3005, 173005, 124005, 0.1225, 24236924.1569918, 10098718.39874659, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23005, 69.15338989, 0.00091827, 85.06147049, 0.01881469, 8.50614705, 0.06598592, -69.15338989, -0.00091827, -85.06147049, -0.01881469, -8.50614705, -0.06598592, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13005, 57.47920906, 0.00091827, 70.70175523, 0.01881469, 7.07017552, 0.06598592, -57.47920906, -0.00091827, -70.70175523, -0.01881469, -7.07017552, -0.06598592, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23005, 3005, 0.0, 100.76439535, 0.01836549, 100.76439535, 0.05509647, 70.53507674, -3621.76453216, 0.05, 2, 0, 73005, 24005, 2, 3)
    ops.uniaxialMaterial('LimitState', 43005, 25.19109884, 6.475e-05, 75.57329651, 0.00019426, 251.91098837, 0.00064755, -25.19109884, -6.475e-05, -75.57329651, -0.00019426, -251.91098837, -0.00064755, 0.4, 0.3, 0.003, 0.0, 0.0, 23005, 2)
    ops.limitCurve('ThreePoint', 13005, 3005, 0.0, 100.76439535, 0.01836549, 100.76439535, 0.05509647, 70.53507674, -3621.76453216, 0.05, 2, 0, 73005, 24005, 1, 3)
    ops.uniaxialMaterial('LimitState', 33005, 25.19109884, 6.475e-05, 75.57329651, 0.00019426, 251.91098837, 0.00064755, -25.19109884, -6.475e-05, -75.57329651, -0.00019426, -251.91098837, -0.00064755, 0.4, 0.3, 0.003, 0.0, 0.0, 13005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3005, 99999, 'P', 43005, 'Vy', 33005, 'Vz', 23005, 'My', 13005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173005, 73005, 173005, 3005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124005, 124005, 24005, 3005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173006, 32.25, 0.0, 8.3)
    ops.node(124006, 32.25, 0.0, 10.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3006, 173006, 124006, 0.0625, 26637972.97810646, 11099155.40754436, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23006, 45.09549966, 0.00139112, 55.24753959, 0.02541648, 5.52475396, 0.07967774, -45.09549966, -0.00139112, -55.24753959, -0.02541648, -5.52475396, -0.07967774, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13006, 42.01000524, 0.00139112, 51.46742901, 0.02541648, 5.1467429, 0.07967774, -42.01000524, -0.00139112, -51.46742901, -0.02541648, -5.1467429, -0.07967774, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23006, 3006, 0.0, 58.47808303, 0.02782241, 58.47808303, 0.08346723, 40.93465812, -3393.31685578, 0.05, 2, 0, 73006, 24006, 2, 3)
    ops.uniaxialMaterial('LimitState', 43006, 14.61952076, 6.702e-05, 43.85856228, 0.00020105, 146.19520758, 0.00067018, -14.61952076, -6.702e-05, -43.85856228, -0.00020105, -146.19520758, -0.00067018, 0.4, 0.3, 0.003, 0.0, 0.0, 23006, 2)
    ops.limitCurve('ThreePoint', 13006, 3006, 0.0, 58.47808303, 0.02782241, 58.47808303, 0.08346723, 40.93465812, -3393.31685578, 0.05, 2, 0, 73006, 24006, 1, 3)
    ops.uniaxialMaterial('LimitState', 33006, 14.61952076, 6.702e-05, 43.85856228, 0.00020105, 146.19520758, 0.00067018, -14.61952076, -6.702e-05, -43.85856228, -0.00020105, -146.19520758, -0.00067018, 0.4, 0.3, 0.003, 0.0, 0.0, 13006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3006, 99999, 'P', 43006, 'Vy', 33006, 'Vz', 23006, 'My', 13006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173006, 73006, 173006, 3006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124006, 124006, 24006, 3006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173007, 0.0, 3.65, 8.3)
    ops.node(124007, 0.0, 3.65, 10.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3007, 173007, 124007, 0.1225, 30165103.66561431, 12568793.19400596, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23007, 118.709211, 0.0010377, 144.22663935, 0.04233803, 14.42266394, 0.11627689, -118.709211, -0.0010377, -144.22663935, -0.04233803, -14.42266394, -0.11627689, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13007, 108.70961258, 0.0010377, 132.07755283, 0.04233803, 13.20775528, 0.11627689, -108.70961258, -0.0010377, -132.07755283, -0.04233803, -13.20775528, -0.11627689, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23007, 3007, 0.0, 153.25570102, 0.02075403, 153.25570102, 0.06226208, 107.27899072, -8934.61374643, 0.05, 2, 0, 73007, 24007, 2, 3)
    ops.uniaxialMaterial('LimitState', 43007, 38.31392526, 7.913e-05, 114.94177577, 0.0002374, 383.13925256, 0.00079132, -38.31392526, -7.913e-05, -114.94177577, -0.0002374, -383.13925256, -0.00079132, 0.4, 0.3, 0.003, 0.0, 0.0, 23007, 2)
    ops.limitCurve('ThreePoint', 13007, 3007, 0.0, 153.25570102, 0.02075403, 153.25570102, 0.06226208, 107.27899072, -8934.61374643, 0.05, 2, 0, 73007, 24007, 1, 3)
    ops.uniaxialMaterial('LimitState', 33007, 38.31392526, 7.913e-05, 114.94177577, 0.0002374, 383.13925256, 0.00079132, -38.31392526, -7.913e-05, -114.94177577, -0.0002374, -383.13925256, -0.00079132, 0.4, 0.3, 0.003, 0.0, 0.0, 13007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3007, 99999, 'P', 43007, 'Vy', 33007, 'Vz', 23007, 'My', 13007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173007, 73007, 173007, 3007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124007, 124007, 24007, 3007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173008, 7.3, 3.65, 8.3)
    ops.node(124008, 7.3, 3.65, 10.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3008, 173008, 124008, 0.1225, 26889488.3976437, 11203953.49901821, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23008, 84.70852784, 0.00112248, 103.59673701, 0.01781711, 10.3596737, 0.05875942, -84.70852784, -0.00112248, -103.59673701, -0.01781711, -10.3596737, -0.05875942, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13008, 79.25506666, 0.00112248, 96.92726939, 0.01781711, 9.69272694, 0.05875942, -79.25506666, -0.00112248, -96.92726939, -0.01781711, -9.69272694, -0.05875942, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23008, 3008, 0.0, 102.58782369, 0.02244956, 102.58782369, 0.06734868, 71.81147659, -1979.91949384, 0.05, 2, 0, 73008, 24008, 2, 3)
    ops.uniaxialMaterial('LimitState', 43008, 25.64695592, 5.942e-05, 76.94086777, 0.00017827, 256.46955923, 0.00059423, -25.64695592, -5.942e-05, -76.94086777, -0.00017827, -256.46955923, -0.00059423, 0.4, 0.3, 0.003, 0.0, 0.0, 23008, 2)
    ops.limitCurve('ThreePoint', 13008, 3008, 0.0, 102.58782369, 0.02244956, 102.58782369, 0.06734868, 71.81147659, -1979.91949384, 0.05, 2, 0, 73008, 24008, 1, 3)
    ops.uniaxialMaterial('LimitState', 33008, 25.64695592, 5.942e-05, 76.94086777, 0.00017827, 256.46955923, 0.00059423, -25.64695592, -5.942e-05, -76.94086777, -0.00017827, -256.46955923, -0.00059423, 0.4, 0.3, 0.003, 0.0, 0.0, 13008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3008, 99999, 'P', 43008, 'Vy', 33008, 'Vz', 23008, 'My', 13008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173008, 73008, 173008, 3008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124008, 124008, 24008, 3008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173009, 14.6, 3.65, 8.3)
    ops.node(124009, 14.6, 3.65, 10.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3009, 173009, 124009, 0.1225, 23102799.87197462, 9626166.61332276, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23009, 92.51274833, 0.00107325, 113.78834648, 0.02716788, 11.37883465, 0.06619578, -92.51274833, -0.00107325, -113.78834648, -0.02716788, -11.37883465, -0.06619578, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13009, 92.51274833, 0.00107325, 113.78834648, 0.02716788, 11.37883465, 0.06619578, -92.51274833, -0.00107325, -113.78834648, -0.02716788, -11.37883465, -0.06619578, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23009, 3009, 0.0, 93.96269502, 0.02146494, 93.96269502, 0.06439483, 65.77388651, -2462.84416637, 0.05, 2, 0, 73009, 24009, 2, 3)
    ops.uniaxialMaterial('LimitState', 43009, 23.49067375, 6.335e-05, 70.47202126, 0.00019004, 234.90673755, 0.00063348, -23.49067375, -6.335e-05, -70.47202126, -0.00019004, -234.90673755, -0.00063348, 0.4, 0.3, 0.003, 0.0, 0.0, 23009, 2)
    ops.limitCurve('ThreePoint', 13009, 3009, 0.0, 93.96269502, 0.02146494, 93.96269502, 0.06439483, 65.77388651, -2462.84416637, 0.05, 2, 0, 73009, 24009, 1, 3)
    ops.uniaxialMaterial('LimitState', 33009, 23.49067375, 6.335e-05, 70.47202126, 0.00019004, 234.90673755, 0.00063348, -23.49067375, -6.335e-05, -70.47202126, -0.00019004, -234.90673755, -0.00063348, 0.4, 0.3, 0.003, 0.0, 0.0, 13009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3009, 99999, 'P', 43009, 'Vy', 33009, 'Vz', 23009, 'My', 13009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173009, 73009, 173009, 3009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124009, 124009, 24009, 3009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173010, 17.65, 3.65, 8.3)
    ops.node(124010, 17.65, 3.65, 10.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3010, 173010, 124010, 0.1225, 25830910.97060874, 10762879.57108697, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23010, 96.66321573, 0.00111775, 118.48562812, 0.0208899, 11.84856281, 0.06178602, -96.66321573, -0.00111775, -118.48562812, -0.0208899, -11.84856281, -0.06178602, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13010, 96.66321573, 0.00111775, 118.48562812, 0.0208899, 11.84856281, 0.06178602, -96.66321573, -0.00111775, -118.48562812, -0.0208899, -11.84856281, -0.06178602, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23010, 3010, 0.0, 94.01115767, 0.02235501, 94.01115767, 0.06706502, 65.80781037, -1787.94436748, 0.05, 2, 0, 73010, 24010, 2, 3)
    ops.uniaxialMaterial('LimitState', 43010, 23.50278942, 5.669e-05, 70.50836825, 0.00017006, 235.02789418, 0.00056687, -23.50278942, -5.669e-05, -70.50836825, -0.00017006, -235.02789418, -0.00056687, 0.4, 0.3, 0.003, 0.0, 0.0, 23010, 2)
    ops.limitCurve('ThreePoint', 13010, 3010, 0.0, 94.01115767, 0.02235501, 94.01115767, 0.06706502, 65.80781037, -1787.94436748, 0.05, 2, 0, 73010, 24010, 1, 3)
    ops.uniaxialMaterial('LimitState', 33010, 23.50278942, 5.669e-05, 70.50836825, 0.00017006, 235.02789418, 0.00056687, -23.50278942, -5.669e-05, -70.50836825, -0.00017006, -235.02789418, -0.00056687, 0.4, 0.3, 0.003, 0.0, 0.0, 13010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3010, 99999, 'P', 43010, 'Vy', 33010, 'Vz', 23010, 'My', 13010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173010, 73010, 173010, 3010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124010, 124010, 24010, 3010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173011, 24.95, 3.65, 8.3)
    ops.node(124011, 24.95, 3.65, 10.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3011, 173011, 124011, 0.1225, 24006188.75395412, 10002578.64748088, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23011, 81.66501374, 0.00107851, 100.29642087, 0.01699099, 10.02964209, 0.05604775, -81.66501374, -0.00107851, -100.29642087, -0.01699099, -10.02964209, -0.05604775, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13011, 75.95165132, 0.00107851, 93.2795874, 0.01699099, 9.32795874, 0.05604775, -75.95165132, -0.00107851, -93.2795874, -0.01699099, -9.32795874, -0.05604775, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23011, 3011, 0.0, 90.78940552, 0.02157013, 90.78940552, 0.06471038, 63.55258386, -1812.17187895, 0.05, 2, 0, 73011, 24011, 2, 3)
    ops.uniaxialMaterial('LimitState', 43011, 22.69735138, 5.891e-05, 68.09205414, 0.00017672, 226.97351379, 0.00058905, -22.69735138, -5.891e-05, -68.09205414, -0.00017672, -226.97351379, -0.00058905, 0.4, 0.3, 0.003, 0.0, 0.0, 23011, 2)
    ops.limitCurve('ThreePoint', 13011, 3011, 0.0, 90.78940552, 0.02157013, 90.78940552, 0.06471038, 63.55258386, -1812.17187895, 0.05, 2, 0, 73011, 24011, 1, 3)
    ops.uniaxialMaterial('LimitState', 33011, 22.69735138, 5.891e-05, 68.09205414, 0.00017672, 226.97351379, 0.00058905, -22.69735138, -5.891e-05, -68.09205414, -0.00017672, -226.97351379, -0.00058905, 0.4, 0.3, 0.003, 0.0, 0.0, 13011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3011, 99999, 'P', 43011, 'Vy', 33011, 'Vz', 23011, 'My', 13011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173011, 73011, 173011, 3011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124011, 124011, 24011, 3011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173012, 32.25, 3.65, 8.3)
    ops.node(124012, 32.25, 3.65, 10.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3012, 173012, 124012, 0.1225, 34411675.39313839, 14338198.08047433, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23012, 113.46254843, 0.00087497, 135.88395277, 0.03840705, 13.58839528, 0.11347117, -113.46254843, -0.00087497, -135.88395277, -0.03840705, -13.58839528, -0.11347117, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13012, 103.61770075, 0.00087497, 124.09365865, 0.03840705, 12.40936587, 0.11347117, -103.61770075, -0.00087497, -124.09365865, -0.03840705, -12.40936587, -0.11347117, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23012, 3012, 0.0, 162.88137363, 0.01749937, 162.88137363, 0.05249812, 114.01696154, -7716.19416995, 0.05, 2, 0, 73012, 24012, 2, 3)
    ops.uniaxialMaterial('LimitState', 43012, 40.72034341, 7.372e-05, 122.16103022, 0.00022117, 407.20343408, 0.00073724, -40.72034341, -7.372e-05, -122.16103022, -0.00022117, -407.20343408, -0.00073724, 0.4, 0.3, 0.003, 0.0, 0.0, 23012, 2)
    ops.limitCurve('ThreePoint', 13012, 3012, 0.0, 162.88137363, 0.01749937, 162.88137363, 0.05249812, 114.01696154, -7716.19416995, 0.05, 2, 0, 73012, 24012, 1, 3)
    ops.uniaxialMaterial('LimitState', 33012, 40.72034341, 7.372e-05, 122.16103022, 0.00022117, 407.20343408, 0.00073724, -40.72034341, -7.372e-05, -122.16103022, -0.00022117, -407.20343408, -0.00073724, 0.4, 0.3, 0.003, 0.0, 0.0, 13012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3012, 99999, 'P', 43012, 'Vy', 33012, 'Vz', 23012, 'My', 13012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173012, 73012, 173012, 3012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124012, 124012, 24012, 3012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173013, 0.0, 7.3, 8.3)
    ops.node(124013, 0.0, 7.3, 10.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3013, 173013, 124013, 0.0625, 32561254.49185663, 13567189.37160693, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23013, 49.21000185, 0.00137429, 59.33728084, 0.0171226, 5.93372808, 0.07319574, -49.21000185, -0.00137429, -59.33728084, -0.0171226, -5.93372808, -0.07319574, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13013, 45.99934141, 0.00137429, 55.46587558, 0.0171226, 5.54658756, 0.07319574, -45.99934141, -0.00137429, -55.46587558, -0.0171226, -5.54658756, -0.07319574, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23013, 3013, 0.0, 40.21709549, 0.02748582, 40.21709549, 0.08245747, 28.15196684, -1885.33344376, 0.05, 2, 0, 73013, 24013, 2, 3)
    ops.uniaxialMaterial('LimitState', 43013, 10.05427387, 3.771e-05, 30.16282161, 0.00011312, 100.54273872, 0.00037706, -10.05427387, -3.771e-05, -30.16282161, -0.00011312, -100.54273872, -0.00037706, 0.4, 0.3, 0.003, 0.0, 0.0, 23013, 2)
    ops.limitCurve('ThreePoint', 13013, 3013, 0.0, 40.21709549, 0.02748582, 40.21709549, 0.08245747, 28.15196684, -1885.33344376, 0.05, 2, 0, 73013, 24013, 1, 3)
    ops.uniaxialMaterial('LimitState', 33013, 10.05427387, 3.771e-05, 30.16282161, 0.00011312, 100.54273872, 0.00037706, -10.05427387, -3.771e-05, -30.16282161, -0.00011312, -100.54273872, -0.00037706, 0.4, 0.3, 0.003, 0.0, 0.0, 13013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3013, 99999, 'P', 43013, 'Vy', 33013, 'Vz', 23013, 'My', 13013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173013, 73013, 173013, 3013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124013, 124013, 24013, 3013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173014, 7.3, 7.3, 8.3)
    ops.node(124014, 7.3, 7.3, 10.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3014, 173014, 124014, 0.1225, 29633539.74791497, 12347308.2282979, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23014, 67.84584157, 0.00086806, 82.54595265, 0.01471212, 8.25459526, 0.06404103, -67.84584157, -0.00086806, -82.54595265, -0.01471212, -8.25459526, -0.06404103, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13014, 57.32480817, 0.00086806, 69.7453343, 0.01471212, 6.97453343, 0.06404103, -57.32480817, -0.00086806, -69.7453343, -0.01471212, -6.97453343, -0.06404103, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23014, 3014, 0.0, 111.41321819, 0.01736126, 111.41321819, 0.05208378, 77.98925273, -2765.17359063, 0.05, 2, 0, 73014, 24014, 2, 3)
    ops.uniaxialMaterial('LimitState', 43014, 27.85330455, 5.856e-05, 83.55991364, 0.00017568, 278.53304548, 0.00058559, -27.85330455, -5.856e-05, -83.55991364, -0.00017568, -278.53304548, -0.00058559, 0.4, 0.3, 0.003, 0.0, 0.0, 23014, 2)
    ops.limitCurve('ThreePoint', 13014, 3014, 0.0, 111.41321819, 0.01736126, 111.41321819, 0.05208378, 77.98925273, -2765.17359063, 0.05, 2, 0, 73014, 24014, 1, 3)
    ops.uniaxialMaterial('LimitState', 33014, 27.85330455, 5.856e-05, 83.55991364, 0.00017568, 278.53304548, 0.00058559, -27.85330455, -5.856e-05, -83.55991364, -0.00017568, -278.53304548, -0.00058559, 0.4, 0.3, 0.003, 0.0, 0.0, 13014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3014, 99999, 'P', 43014, 'Vy', 33014, 'Vz', 23014, 'My', 13014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173014, 73014, 173014, 3014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124014, 124014, 24014, 3014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173015, 14.6, 7.3, 8.3)
    ops.node(124015, 14.6, 7.3, 10.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3015, 173015, 124015, 0.0625, 28114982.58111627, 11714576.07546511, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23015, 21.99996841, 0.00117696, 26.85039448, 0.02252993, 2.68503945, 0.08458616, -21.99996841, -0.00117696, -26.85039448, -0.02252993, -2.68503945, -0.08458616, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13015, 21.99996841, 0.00117696, 26.85039448, 0.02252993, 2.68503945, 0.08458616, -21.99996841, -0.00117696, -26.85039448, -0.02252993, -2.68503945, -0.08458616, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23015, 3015, 0.0, 70.35386554, 0.02353918, 70.35386554, 0.07061754, 49.24770588, -2802.56205451, 0.05, 2, 0, 73015, 24015, 2, 3)
    ops.uniaxialMaterial('LimitState', 43015, 17.58846638, 7.639e-05, 52.76539915, 0.00022918, 175.88466384, 0.00076392, -17.58846638, -7.639e-05, -52.76539915, -0.00022918, -175.88466384, -0.00076392, 0.4, 0.3, 0.003, 0.0, 0.0, 23015, 2)
    ops.limitCurve('ThreePoint', 13015, 3015, 0.0, 70.35386554, 0.02353918, 70.35386554, 0.07061754, 49.24770588, -2802.56205451, 0.05, 2, 0, 73015, 24015, 1, 3)
    ops.uniaxialMaterial('LimitState', 33015, 17.58846638, 7.639e-05, 52.76539915, 0.00022918, 175.88466384, 0.00076392, -17.58846638, -7.639e-05, -52.76539915, -0.00022918, -175.88466384, -0.00076392, 0.4, 0.3, 0.003, 0.0, 0.0, 13015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3015, 99999, 'P', 43015, 'Vy', 33015, 'Vz', 23015, 'My', 13015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173015, 73015, 173015, 3015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124015, 124015, 24015, 3015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173016, 17.65, 7.3, 8.3)
    ops.node(124016, 17.65, 7.3, 10.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3016, 173016, 124016, 0.0625, 29314702.52674033, 12214459.38614181, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23016, 24.24686357, 0.00116051, 29.50810704, 0.02295924, 2.9508107, 0.08563027, -24.24686357, -0.00116051, -29.50810704, -0.02295924, -2.9508107, -0.08563027, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13016, 24.24686357, 0.00116051, 29.50810704, 0.02295924, 2.9508107, 0.08563027, -24.24686357, -0.00116051, -29.50810704, -0.02295924, -2.9508107, -0.08563027, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23016, 3016, 0.0, 77.04575955, 0.02321025, 77.04575955, 0.06963075, 53.93203169, -3415.7251857, 0.05, 2, 0, 73016, 24016, 2, 3)
    ops.uniaxialMaterial('LimitState', 43016, 19.26143989, 8.023e-05, 57.78431967, 0.0002407, 192.61439889, 0.00080235, -19.26143989, -8.023e-05, -57.78431967, -0.0002407, -192.61439889, -0.00080235, 0.4, 0.3, 0.003, 0.0, 0.0, 23016, 2)
    ops.limitCurve('ThreePoint', 13016, 3016, 0.0, 77.04575955, 0.02321025, 77.04575955, 0.06963075, 53.93203169, -3415.7251857, 0.05, 2, 0, 73016, 24016, 1, 3)
    ops.uniaxialMaterial('LimitState', 33016, 19.26143989, 8.023e-05, 57.78431967, 0.0002407, 192.61439889, 0.00080235, -19.26143989, -8.023e-05, -57.78431967, -0.0002407, -192.61439889, -0.00080235, 0.4, 0.3, 0.003, 0.0, 0.0, 13016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3016, 99999, 'P', 43016, 'Vy', 33016, 'Vz', 23016, 'My', 13016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173016, 73016, 173016, 3016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124016, 124016, 24016, 3016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173017, 24.95, 7.3, 8.3)
    ops.node(124017, 24.95, 7.3, 10.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3017, 173017, 124017, 0.1225, 25202093.65485706, 10500872.35619044, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23017, 67.27648668, 0.00088948, 82.63409183, 0.01916521, 8.26340918, 0.0668667, -67.27648668, -0.00088948, -82.63409183, -0.01916521, -8.26340918, -0.0668667, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13017, 56.17876677, 0.00088948, 69.00302915, 0.01916521, 6.90030292, 0.0668667, -56.17876677, -0.00088948, -69.00302915, -0.01916521, -6.90030292, -0.0668667, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23017, 3017, 0.0, 104.03742796, 0.0177895, 104.03742796, 0.0533685, 72.82619957, -3646.1361409, 0.05, 2, 0, 73017, 24017, 2, 3)
    ops.uniaxialMaterial('LimitState', 43017, 26.00935699, 6.43e-05, 78.02807097, 0.00019289, 260.09356989, 0.00064298, -26.00935699, -6.43e-05, -78.02807097, -0.00019289, -260.09356989, -0.00064298, 0.4, 0.3, 0.003, 0.0, 0.0, 23017, 2)
    ops.limitCurve('ThreePoint', 13017, 3017, 0.0, 104.03742796, 0.0177895, 104.03742796, 0.0533685, 72.82619957, -3646.1361409, 0.05, 2, 0, 73017, 24017, 1, 3)
    ops.uniaxialMaterial('LimitState', 33017, 26.00935699, 6.43e-05, 78.02807097, 0.00019289, 260.09356989, 0.00064298, -26.00935699, -6.43e-05, -78.02807097, -0.00019289, -260.09356989, -0.00064298, 0.4, 0.3, 0.003, 0.0, 0.0, 13017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3017, 99999, 'P', 43017, 'Vy', 33017, 'Vz', 23017, 'My', 13017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173017, 73017, 173017, 3017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124017, 124017, 24017, 3017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173018, 32.25, 7.3, 8.3)
    ops.node(124018, 32.25, 7.3, 10.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3018, 173018, 124018, 0.0625, 26155674.19322466, 10898197.58051028, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23018, 46.08162835, 0.001327, 56.50720991, 0.01917241, 5.65072099, 0.07320476, -46.08162835, -0.001327, -56.50720991, -0.01917241, -5.65072099, -0.07320476, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13018, 42.63808576, 0.001327, 52.28459471, 0.01917241, 5.22845947, 0.07320476, -42.63808576, -0.001327, -52.28459471, -0.01917241, -5.22845947, -0.07320476, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23018, 3018, 0.0, 28.57038608, 0.02654008, 28.57038608, 0.07962025, 19.99927026, -1672.30873524, 0.05, 2, 0, 73018, 24018, 2, 3)
    ops.uniaxialMaterial('LimitState', 43018, 7.14259652, 3.335e-05, 21.42778956, 0.00010004, 71.42596521, 0.00033346, -7.14259652, -3.335e-05, -21.42778956, -0.00010004, -71.42596521, -0.00033346, 0.4, 0.3, 0.003, 0.0, 0.0, 23018, 2)
    ops.limitCurve('ThreePoint', 13018, 3018, 0.0, 28.57038608, 0.02654008, 28.57038608, 0.07962025, 19.99927026, -1672.30873524, 0.05, 2, 0, 73018, 24018, 1, 3)
    ops.uniaxialMaterial('LimitState', 33018, 7.14259652, 3.335e-05, 21.42778956, 0.00010004, 71.42596521, 0.00033346, -7.14259652, -3.335e-05, -21.42778956, -0.00010004, -71.42596521, -0.00033346, 0.4, 0.3, 0.003, 0.0, 0.0, 13018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3018, 99999, 'P', 43018, 'Vy', 33018, 'Vz', 23018, 'My', 13018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173018, 73018, 173018, 3018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124018, 124018, 24018, 3018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170003, 14.6, 0.0, 0.0)
    ops.node(124019, 14.6, 0.0, 1.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4046, 170003, 124019, 0.16, 27619181.81829989, 11507992.42429162, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24046, 153.89255576, 0.000685, 186.57118421, 0.02647324, 18.65711842, 0.07712526, -153.89255576, -0.000685, -186.57118421, -0.02647324, -18.65711842, -0.07712526, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14046, 168.17461729, 0.000685, 203.8859992, 0.02647324, 20.38859992, 0.07712526, -168.17461729, -0.000685, -203.8859992, -0.02647324, -20.38859992, -0.07712526, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24046, 4046, 0.0, 278.37204962, 0.01369993, 278.37204962, 0.04109979, 194.86043473, -6192.15908334, 0.05, 2, 0, 70003, 24019, 2, 3)
    ops.uniaxialMaterial('LimitState', 44046, 69.5930124, 6.01e-05, 208.77903721, 0.00018029, 695.93012404, 0.00060096, -69.5930124, -6.01e-05, -208.77903721, -0.00018029, -695.93012404, -0.00060096, 0.4, 0.3, 0.003, 0.0, 0.0, 24046, 2)
    ops.limitCurve('ThreePoint', 14046, 4046, 0.0, 278.37204962, 0.01369993, 278.37204962, 0.04109979, 194.86043473, -6192.15908334, 0.05, 2, 0, 70003, 24019, 1, 3)
    ops.uniaxialMaterial('LimitState', 34046, 69.5930124, 6.01e-05, 208.77903721, 0.00018029, 695.93012404, 0.00060096, -69.5930124, -6.01e-05, -208.77903721, -0.00018029, -695.93012404, -0.00060096, 0.4, 0.3, 0.003, 0.0, 0.0, 14046, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4046, 99999, 'P', 44046, 'Vy', 34046, 'Vz', 24046, 'My', 14046, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170003, 70003, 170003, 4046, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124019, 124019, 24019, 4046, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174019, 14.6, 0.0, 1.525)
    ops.node(121003, 14.6, 0.0, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4047, 174019, 121003, 0.16, 26575855.65737681, 11073273.19057367, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24047, 126.46280312, 0.00073185, 153.59828275, 0.0293989, 15.35982827, 0.07916681, -126.46280312, -0.00073185, -153.59828275, -0.0293989, -15.35982827, -0.07916681, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14047, 109.33155072, 0.00073185, 132.7911293, 0.0293989, 13.27911293, 0.07916681, -109.33155072, -0.00073185, -132.7911293, -0.0293989, -13.27911293, -0.07916681, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24047, 4047, 0.0, 275.82956445, 0.01463698, 275.82956445, 0.04391095, 193.08069511, -7195.43165067, 0.05, 2, 0, 74019, 21003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44047, 68.95739111, 6.188e-05, 206.87217334, 0.00018565, 689.57391112, 0.00061885, -68.95739111, -6.188e-05, -206.87217334, -0.00018565, -689.57391112, -0.00061885, 0.4, 0.3, 0.003, 0.0, 0.0, 24047, 2)
    ops.limitCurve('ThreePoint', 14047, 4047, 0.0, 275.82956445, 0.01463698, 275.82956445, 0.04391095, 193.08069511, -7195.43165067, 0.05, 2, 0, 74019, 21003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34047, 68.95739111, 6.188e-05, 206.87217334, 0.00018565, 689.57391112, 0.00061885, -68.95739111, -6.188e-05, -206.87217334, -0.00018565, -689.57391112, -0.00061885, 0.4, 0.3, 0.003, 0.0, 0.0, 14047, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4047, 99999, 'P', 44047, 'Vy', 34047, 'Vz', 24047, 'My', 14047, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174019, 74019, 174019, 4047, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121003, 121003, 21003, 4047, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170004, 17.65, 0.0, 0.0)
    ops.node(124020, 17.65, 0.0, 1.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4048, 170004, 124020, 0.16, 23597312.5093995, 9832213.54558312, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24048, 154.99381358, 0.00080208, 188.09539888, 0.02480701, 18.80953989, 0.06566132, -154.99381358, -0.00080208, -188.09539888, -0.02480701, -18.80953989, -0.06566132, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14048, 168.60777151, 0.00080208, 204.61685085, 0.02480701, 20.46168508, 0.06566132, -168.60777151, -0.00080208, -204.61685085, -0.02480701, -20.46168508, -0.06566132, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24048, 4048, 0.0, 241.73729249, 0.01604164, 241.73729249, 0.04812493, 169.21610474, -6034.62081936, 0.05, 2, 0, 70004, 24020, 2, 3)
    ops.uniaxialMaterial('LimitState', 44048, 60.43432312, 6.108e-05, 181.30296937, 0.00018324, 604.34323123, 0.00061081, -60.43432312, -6.108e-05, -181.30296937, -0.00018324, -604.34323123, -0.00061081, 0.4, 0.3, 0.003, 0.0, 0.0, 24048, 2)
    ops.limitCurve('ThreePoint', 14048, 4048, 0.0, 241.73729249, 0.01604164, 241.73729249, 0.04812493, 169.21610474, -6034.62081936, 0.05, 2, 0, 70004, 24020, 1, 3)
    ops.uniaxialMaterial('LimitState', 34048, 60.43432312, 6.108e-05, 181.30296937, 0.00018324, 604.34323123, 0.00061081, -60.43432312, -6.108e-05, -181.30296937, -0.00018324, -604.34323123, -0.00061081, 0.4, 0.3, 0.003, 0.0, 0.0, 14048, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4048, 99999, 'P', 44048, 'Vy', 34048, 'Vz', 24048, 'My', 14048, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170004, 70004, 170004, 4048, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124020, 124020, 24020, 4048, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174020, 17.65, 0.0, 1.525)
    ops.node(121004, 17.65, 0.0, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4049, 174020, 121004, 0.16, 33255265.40187414, 13856360.58411422, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24049, 139.25447979, 0.00067027, 166.80595721, 0.02544861, 16.68059572, 0.0846348, -139.25447979, -0.00067027, -166.80595721, -0.02544861, -16.68059572, -0.0846348, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14049, 117.89352348, 0.00067027, 141.21873897, 0.02544861, 14.1218739, 0.0846348, -117.89352348, -0.00067027, -141.21873897, -0.02544861, -14.1218739, -0.0846348, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24049, 4049, 0.0, 332.99849892, 0.01340547, 332.99849892, 0.0402164, 233.09894924, -6671.64469567, 0.05, 2, 0, 74020, 21004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44049, 83.24962473, 5.97e-05, 249.74887419, 0.00017911, 832.4962473, 0.00059705, -83.24962473, -5.97e-05, -249.74887419, -0.00017911, -832.4962473, -0.00059705, 0.4, 0.3, 0.003, 0.0, 0.0, 24049, 2)
    ops.limitCurve('ThreePoint', 14049, 4049, 0.0, 332.99849892, 0.01340547, 332.99849892, 0.0402164, 233.09894924, -6671.64469567, 0.05, 2, 0, 74020, 21004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34049, 83.24962473, 5.97e-05, 249.74887419, 0.00017911, 832.4962473, 0.00059705, -83.24962473, -5.97e-05, -249.74887419, -0.00017911, -832.4962473, -0.00059705, 0.4, 0.3, 0.003, 0.0, 0.0, 14049, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4049, 99999, 'P', 44049, 'Vy', 34049, 'Vz', 24049, 'My', 14049, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174020, 74020, 174020, 4049, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121004, 121004, 21004, 4049, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171003, 14.6, 0.0, 3.0)
    ops.node(124021, 14.6, 0.0, 3.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4051, 171003, 124021, 0.16, 27107208.33806206, 11294670.14085919, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24051, 120.21237324, 0.00067499, 146.25306776, 0.03050569, 14.62530678, 0.08475736, -120.21237324, -0.00067499, -146.25306776, -0.03050569, -14.62530678, -0.08475736, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14051, 100.69465267, 0.00067499, 122.50737144, 0.03050569, 12.25073714, 0.08475736, -100.69465267, -0.00067499, -122.50737144, -0.03050569, -12.25073714, -0.08475736, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24051, 4051, 0.0, 288.66832774, 0.01349973, 288.66832774, 0.04049919, 202.06782942, -9796.75946298, 0.05, 2, 0, 71003, 24021, 2, 3)
    ops.uniaxialMaterial('LimitState', 44051, 72.16708194, 6.35e-05, 216.50124581, 0.00019049, 721.67081936, 0.00063495, -72.16708194, -6.35e-05, -216.50124581, -0.00019049, -721.67081936, -0.00063495, 0.4, 0.3, 0.003, 0.0, 0.0, 24051, 2)
    ops.limitCurve('ThreePoint', 14051, 4051, 0.0, 288.66832774, 0.01349973, 288.66832774, 0.04049919, 202.06782942, -9796.75946298, 0.05, 2, 0, 71003, 24021, 1, 3)
    ops.uniaxialMaterial('LimitState', 34051, 72.16708194, 6.35e-05, 216.50124581, 0.00019049, 721.67081936, 0.00063495, -72.16708194, -6.35e-05, -216.50124581, -0.00019049, -721.67081936, -0.00063495, 0.4, 0.3, 0.003, 0.0, 0.0, 14051, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4051, 99999, 'P', 44051, 'Vy', 34051, 'Vz', 24051, 'My', 14051, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171003, 71003, 171003, 4051, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124021, 124021, 24021, 4051, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174021, 14.6, 0.0, 4.175)
    ops.node(122003, 14.6, 0.0, 4.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4052, 174021, 122003, 0.16, 27494344.3588389, 11455976.81618288, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24052, 128.2544482, 0.00070691, 156.07031877, 0.02645131, 15.60703188, 0.08255731, -128.2544482, -0.00070691, -156.07031877, -0.02645131, -15.60703188, -0.08255731, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14052, 105.4622021, 0.00070691, 128.33488219, 0.02645131, 12.83348822, 0.08255731, -105.4622021, -0.00070691, -128.33488219, -0.02645131, -12.83348822, -0.08255731, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24052, 4052, 0.0, 264.00504476, 0.01413828, 264.00504476, 0.04241483, 184.80353133, -7184.34521977, 0.05, 2, 0, 74021, 22003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44052, 66.00126119, 5.725e-05, 198.00378357, 0.00017176, 660.0126119, 0.00057253, -66.00126119, -5.725e-05, -198.00378357, -0.00017176, -660.0126119, -0.00057253, 0.4, 0.3, 0.003, 0.0, 0.0, 24052, 2)
    ops.limitCurve('ThreePoint', 14052, 4052, 0.0, 264.00504476, 0.01413828, 264.00504476, 0.04241483, 184.80353133, -7184.34521977, 0.05, 2, 0, 74021, 22003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34052, 66.00126119, 5.725e-05, 198.00378357, 0.00017176, 660.0126119, 0.00057253, -66.00126119, -5.725e-05, -198.00378357, -0.00017176, -660.0126119, -0.00057253, 0.4, 0.3, 0.003, 0.0, 0.0, 14052, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4052, 99999, 'P', 44052, 'Vy', 34052, 'Vz', 24052, 'My', 14052, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174021, 74021, 174021, 4052, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122003, 122003, 22003, 4052, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171004, 17.65, 0.0, 3.0)
    ops.node(124022, 17.65, 0.0, 3.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4053, 171004, 124022, 0.16, 26360696.51085193, 10983623.5461883, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24053, 119.49467572, 0.00068973, 145.50874292, 0.03037748, 14.55087429, 0.08335821, -119.49467572, -0.00068973, -145.50874292, -0.03037748, -14.55087429, -0.08335821, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14053, 100.39373827, 0.00068973, 122.24951919, 0.03037748, 12.22495192, 0.08335821, -100.39373827, -0.00068973, -122.24951919, -0.03037748, -12.22495192, -0.08335821, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24053, 4053, 0.0, 273.13496561, 0.01379464, 273.13496561, 0.04138393, 191.19447593, -8690.27207456, 0.05, 2, 0, 71004, 24022, 2, 3)
    ops.uniaxialMaterial('LimitState', 44053, 68.2837414, 6.178e-05, 204.85122421, 0.00018534, 682.83741403, 0.0006178, -68.2837414, -6.178e-05, -204.85122421, -0.00018534, -682.83741403, -0.0006178, 0.4, 0.3, 0.003, 0.0, 0.0, 24053, 2)
    ops.limitCurve('ThreePoint', 14053, 4053, 0.0, 273.13496561, 0.01379464, 273.13496561, 0.04138393, 191.19447593, -8690.27207456, 0.05, 2, 0, 71004, 24022, 1, 3)
    ops.uniaxialMaterial('LimitState', 34053, 68.2837414, 6.178e-05, 204.85122421, 0.00018534, 682.83741403, 0.0006178, -68.2837414, -6.178e-05, -204.85122421, -0.00018534, -682.83741403, -0.0006178, 0.4, 0.3, 0.003, 0.0, 0.0, 14053, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4053, 99999, 'P', 44053, 'Vy', 34053, 'Vz', 24053, 'My', 14053, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171004, 71004, 171004, 4053, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124022, 124022, 24022, 4053, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174022, 17.65, 0.0, 4.175)
    ops.node(122004, 17.65, 0.0, 4.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4054, 174022, 122004, 0.16, 25922359.48376984, 10800983.11823743, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24054, 116.378157, 0.00070689, 141.90327044, 0.03012619, 14.19032704, 0.08374188, -116.378157, -0.00070689, -141.90327044, -0.03012619, -14.19032704, -0.08374188, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14054, 97.76554925, 0.00070689, 119.20837665, 0.03012619, 11.92083767, 0.08374188, -97.76554925, -0.00070689, -119.20837665, -0.03012619, -11.92083767, -0.08374188, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24054, 4054, 0.0, 257.07463702, 0.01413786, 257.07463702, 0.04241359, 179.95224592, -7961.120299, 0.05, 2, 0, 74022, 22004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44054, 64.26865926, 5.913e-05, 192.80597777, 0.00017739, 642.68659256, 0.00059131, -64.26865926, -5.913e-05, -192.80597777, -0.00017739, -642.68659256, -0.00059131, 0.4, 0.3, 0.003, 0.0, 0.0, 24054, 2)
    ops.limitCurve('ThreePoint', 14054, 4054, 0.0, 257.07463702, 0.01413786, 257.07463702, 0.04241359, 179.95224592, -7961.120299, 0.05, 2, 0, 74022, 22004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34054, 64.26865926, 5.913e-05, 192.80597777, 0.00017739, 642.68659256, 0.00059131, -64.26865926, -5.913e-05, -192.80597777, -0.00017739, -642.68659256, -0.00059131, 0.4, 0.3, 0.003, 0.0, 0.0, 14054, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4054, 99999, 'P', 44054, 'Vy', 34054, 'Vz', 24054, 'My', 14054, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174022, 74022, 174022, 4054, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122004, 122004, 22004, 4054, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172003, 14.6, 0.0, 5.65)
    ops.node(124023, 14.6, 0.0, 6.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4056, 172003, 124023, 0.1225, 26768042.52338123, 11153351.05140885, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24056, 84.8397738, 0.00076331, 103.41211652, 0.02404814, 10.34121165, 0.07366226, -84.8397738, -0.00076331, -103.41211652, -0.02404814, -10.34121165, -0.07366226, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14056, 72.50557277, 0.00076331, 88.37782569, 0.02404814, 8.83778257, 0.07366226, -72.50557277, -0.00076331, -88.37782569, -0.02404814, -8.83778257, -0.07366226, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24056, 4056, 0.0, 180.80790462, 0.01526627, 180.80790462, 0.0457988, 126.56553323, -5880.94289275, 0.05, 2, 0, 72003, 24023, 2, 3)
    ops.uniaxialMaterial('LimitState', 44056, 45.20197615, 5.26e-05, 135.60592846, 0.00015781, 452.01976154, 0.00052603, -45.20197615, -5.26e-05, -135.60592846, -0.00015781, -452.01976154, -0.00052603, 0.4, 0.3, 0.003, 0.0, 0.0, 24056, 2)
    ops.limitCurve('ThreePoint', 14056, 4056, 0.0, 180.80790462, 0.01526627, 180.80790462, 0.0457988, 126.56553323, -5880.94289275, 0.05, 2, 0, 72003, 24023, 1, 3)
    ops.uniaxialMaterial('LimitState', 34056, 45.20197615, 5.26e-05, 135.60592846, 0.00015781, 452.01976154, 0.00052603, -45.20197615, -5.26e-05, -135.60592846, -0.00015781, -452.01976154, -0.00052603, 0.4, 0.3, 0.003, 0.0, 0.0, 14056, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4056, 99999, 'P', 44056, 'Vy', 34056, 'Vz', 24056, 'My', 14056, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172003, 72003, 172003, 4056, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124023, 124023, 24023, 4056, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174023, 14.6, 0.0, 6.825)
    ops.node(123003, 14.6, 0.0, 7.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4057, 174023, 123003, 0.1225, 29954296.43260404, 12480956.84691835, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24057, 82.8019387, 0.0007501, 100.40330973, 0.02061714, 10.04033097, 0.07492849, -82.8019387, -0.0007501, -100.40330973, -0.02061714, -10.04033097, -0.07492849, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14057, 70.99644543, 0.0007501, 86.08829953, 0.02061714, 8.60882995, 0.07492849, -70.99644543, -0.0007501, -86.08829953, -0.02061714, -8.60882995, -0.07492849, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24057, 4057, 0.0, 186.4099006, 0.01500194, 186.4099006, 0.04500581, 130.48693042, -5087.9706984, 0.05, 2, 0, 74023, 23003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44057, 46.60247515, 4.846e-05, 139.80742545, 0.00014539, 466.0247515, 0.00048464, -46.60247515, -4.846e-05, -139.80742545, -0.00014539, -466.0247515, -0.00048464, 0.4, 0.3, 0.003, 0.0, 0.0, 24057, 2)
    ops.limitCurve('ThreePoint', 14057, 4057, 0.0, 186.4099006, 0.01500194, 186.4099006, 0.04500581, 130.48693042, -5087.9706984, 0.05, 2, 0, 74023, 23003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34057, 46.60247515, 4.846e-05, 139.80742545, 0.00014539, 466.0247515, 0.00048464, -46.60247515, -4.846e-05, -139.80742545, -0.00014539, -466.0247515, -0.00048464, 0.4, 0.3, 0.003, 0.0, 0.0, 14057, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4057, 99999, 'P', 44057, 'Vy', 34057, 'Vz', 24057, 'My', 14057, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174023, 74023, 174023, 4057, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123003, 123003, 23003, 4057, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172004, 17.65, 0.0, 5.65)
    ops.node(124024, 17.65, 0.0, 6.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4058, 172004, 124024, 0.1225, 29080830.63540678, 12117012.76475282, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24058, 87.77275857, 0.00080874, 106.55277155, 0.02099081, 10.65527715, 0.07318644, -87.77275857, -0.00080874, -106.55277155, -0.02099081, -10.65527715, -0.07318644, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14058, 76.03735444, 0.00080874, 92.30643982, 0.02099081, 9.23064398, 0.07318644, -76.03735444, -0.00080874, -92.30643982, -0.02099081, -9.23064398, -0.07318644, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24058, 4058, 0.0, 193.1909048, 0.01617473, 193.1909048, 0.04852418, 135.23363336, -5717.84661346, 0.05, 2, 0, 72004, 24024, 2, 3)
    ops.uniaxialMaterial('LimitState', 44058, 48.2977262, 5.174e-05, 144.8931786, 0.00015521, 482.97726201, 0.00051736, -48.2977262, -5.174e-05, -144.8931786, -0.00015521, -482.97726201, -0.00051736, 0.4, 0.3, 0.003, 0.0, 0.0, 24058, 2)
    ops.limitCurve('ThreePoint', 14058, 4058, 0.0, 193.1909048, 0.01617473, 193.1909048, 0.04852418, 135.23363336, -5717.84661346, 0.05, 2, 0, 72004, 24024, 1, 3)
    ops.uniaxialMaterial('LimitState', 34058, 48.2977262, 5.174e-05, 144.8931786, 0.00015521, 482.97726201, 0.00051736, -48.2977262, -5.174e-05, -144.8931786, -0.00015521, -482.97726201, -0.00051736, 0.4, 0.3, 0.003, 0.0, 0.0, 14058, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4058, 99999, 'P', 44058, 'Vy', 34058, 'Vz', 24058, 'My', 14058, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172004, 72004, 172004, 4058, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124024, 124024, 24024, 4058, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174024, 17.65, 0.0, 6.825)
    ops.node(123004, 17.65, 0.0, 7.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4059, 174024, 123004, 0.1225, 26719613.75397731, 11133172.39749055, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24059, 79.76950948, 0.00076303, 97.35665714, 0.02096703, 9.73566571, 0.07234658, -79.76950948, -0.00076303, -97.35665714, -0.02096703, -9.73566571, -0.07234658, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14059, 68.2467972, 0.00076303, 83.29347991, 0.02096703, 8.32934799, 0.07234658, -68.2467972, -0.00076303, -83.29347991, -0.02096703, -8.32934799, -0.07234658, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24059, 4059, 0.0, 166.09009775, 0.01526067, 166.09009775, 0.04578202, 116.26306843, -4956.90454902, 0.05, 2, 0, 74024, 23004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44059, 41.52252444, 4.841e-05, 124.56757331, 0.00014523, 415.22524438, 0.00048409, -41.52252444, -4.841e-05, -124.56757331, -0.00014523, -415.22524438, -0.00048409, 0.4, 0.3, 0.003, 0.0, 0.0, 24059, 2)
    ops.limitCurve('ThreePoint', 14059, 4059, 0.0, 166.09009775, 0.01526067, 166.09009775, 0.04578202, 116.26306843, -4956.90454902, 0.05, 2, 0, 74024, 23004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34059, 41.52252444, 4.841e-05, 124.56757331, 0.00014523, 415.22524438, 0.00048409, -41.52252444, -4.841e-05, -124.56757331, -0.00014523, -415.22524438, -0.00048409, 0.4, 0.3, 0.003, 0.0, 0.0, 14059, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4059, 99999, 'P', 44059, 'Vy', 34059, 'Vz', 24059, 'My', 14059, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174024, 74024, 174024, 4059, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123004, 123004, 23004, 4059, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173003, 14.6, 0.0, 8.3)
    ops.node(124025, 14.6, 0.0, 9.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4061, 173003, 124025, 0.1225, 22483132.19678178, 9367971.74865908, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24061, 67.86025559, 0.00080489, 83.60047892, 0.02225395, 8.36004789, 0.06758749, -67.86025559, -0.00080489, -83.60047892, -0.02225395, -8.36004789, -0.06758749, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14061, 56.99134618, 0.00080489, 70.21052004, 0.02225395, 7.021052, 0.06758749, -56.99134618, -0.00080489, -70.21052004, -0.02225395, -7.021052, -0.06758749, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24061, 4061, 0.0, 139.62566846, 0.01609783, 139.62566846, 0.04829348, 97.73796792, -9839.69929511, 0.05, 2, 0, 73003, 24025, 2, 3)
    ops.uniaxialMaterial('LimitState', 44061, 34.90641711, 4.836e-05, 104.71925134, 0.00014509, 349.06417114, 0.00048364, -34.90641711, -4.836e-05, -104.71925134, -0.00014509, -349.06417114, -0.00048364, 0.4, 0.3, 0.003, 0.0, 0.0, 24061, 2)
    ops.limitCurve('ThreePoint', 14061, 4061, 0.0, 139.62566846, 0.01609783, 139.62566846, 0.04829348, 97.73796792, -9839.69929511, 0.05, 2, 0, 73003, 24025, 1, 3)
    ops.uniaxialMaterial('LimitState', 34061, 34.90641711, 4.836e-05, 104.71925134, 0.00014509, 349.06417114, 0.00048364, -34.90641711, -4.836e-05, -104.71925134, -0.00014509, -349.06417114, -0.00048364, 0.4, 0.3, 0.003, 0.0, 0.0, 14061, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4061, 99999, 'P', 44061, 'Vy', 34061, 'Vz', 24061, 'My', 14061, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173003, 73003, 173003, 4061, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124025, 124025, 24025, 4061, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174025, 14.6, 0.0, 9.475)
    ops.node(124003, 14.6, 0.0, 10.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4062, 174025, 124003, 0.1225, 29606464.11343613, 12336026.71393172, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24062, 62.97400515, 0.00065204, 76.67624094, 0.01829897, 7.66762409, 0.06863106, -62.97400515, -0.00065204, -76.67624094, -0.01829897, -7.66762409, -0.06863106, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14062, 52.34590228, 0.00065204, 63.73561608, 0.01829897, 6.37356161, 0.06863106, -52.34590228, -0.00065204, -63.73561608, -0.01829897, -6.37356161, -0.06863106, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24062, 4062, 0.0, 163.18638602, 0.01304082, 163.18638602, 0.03912245, 114.23047022, -11429.95288718, 0.05, 2, 0, 74025, 24003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44062, 40.79659651, 4.292e-05, 122.38978952, 0.00012877, 407.96596506, 0.00042925, -40.79659651, -4.292e-05, -122.38978952, -0.00012877, -407.96596506, -0.00042925, 0.4, 0.3, 0.003, 0.0, 0.0, 24062, 2)
    ops.limitCurve('ThreePoint', 14062, 4062, 0.0, 163.18638602, 0.01304082, 163.18638602, 0.03912245, 114.23047022, -11429.95288718, 0.05, 2, 0, 74025, 24003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34062, 40.79659651, 4.292e-05, 122.38978952, 0.00012877, 407.96596506, 0.00042925, -40.79659651, -4.292e-05, -122.38978952, -0.00012877, -407.96596506, -0.00042925, 0.4, 0.3, 0.003, 0.0, 0.0, 14062, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4062, 99999, 'P', 44062, 'Vy', 34062, 'Vz', 24062, 'My', 14062, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174025, 74025, 174025, 4062, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124003, 124003, 24003, 4062, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173004, 17.65, 0.0, 8.3)
    ops.node(124026, 17.65, 0.0, 9.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4063, 173004, 124026, 0.1225, 25991204.53560818, 10829668.55650341, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24063, 67.29138374, 0.00076984, 82.51816982, 0.02153605, 8.25181698, 0.0692097, -67.29138374, -0.00076984, -82.51816982, -0.02153605, -8.25181698, -0.0692097, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14063, 57.35747682, 0.00076984, 70.33640489, 0.02153605, 7.03364049, 0.0692097, -57.35747682, -0.00076984, -70.33640489, -0.02153605, -7.03364049, -0.0692097, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24063, 4063, 0.0, 157.78871027, 0.01539682, 157.78871027, 0.04619047, 110.45209719, -9708.70820007, 0.05, 2, 0, 73004, 24026, 2, 3)
    ops.uniaxialMaterial('LimitState', 44063, 39.44717757, 4.728e-05, 118.3415327, 0.00014183, 394.47177566, 0.00047278, -39.44717757, -4.728e-05, -118.3415327, -0.00014183, -394.47177566, -0.00047278, 0.4, 0.3, 0.003, 0.0, 0.0, 24063, 2)
    ops.limitCurve('ThreePoint', 14063, 4063, 0.0, 157.78871027, 0.01539682, 157.78871027, 0.04619047, 110.45209719, -9708.70820007, 0.05, 2, 0, 73004, 24026, 1, 3)
    ops.uniaxialMaterial('LimitState', 34063, 39.44717757, 4.728e-05, 118.3415327, 0.00014183, 394.47177566, 0.00047278, -39.44717757, -4.728e-05, -118.3415327, -0.00014183, -394.47177566, -0.00047278, 0.4, 0.3, 0.003, 0.0, 0.0, 14063, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4063, 99999, 'P', 44063, 'Vy', 34063, 'Vz', 24063, 'My', 14063, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173004, 73004, 173004, 4063, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124026, 124026, 24026, 4063, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174026, 17.65, 0.0, 9.475)
    ops.node(124004, 17.65, 0.0, 10.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4064, 174026, 124004, 0.1225, 27990546.91930006, 11662727.88304169, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24064, 64.73506702, 0.00067398, 79.14791691, 0.01940759, 7.91479169, 0.06946367, -64.73506702, -0.00067398, -79.14791691, -0.01940759, -7.91479169, -0.06946367, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14064, 53.53391456, 0.00067398, 65.45289927, 0.01940759, 6.54528993, 0.06946367, -53.53391456, -0.00067398, -65.45289927, -0.01940759, -6.54528993, -0.06946367, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24064, 4064, 0.0, 148.09309513, 0.0134796, 148.09309513, 0.04043881, 103.66516659, -9314.22192132, 0.05, 2, 0, 74026, 24004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44064, 37.02327378, 4.12e-05, 111.06982135, 0.00012361, 370.23273783, 0.00041204, -37.02327378, -4.12e-05, -111.06982135, -0.00012361, -370.23273783, -0.00041204, 0.4, 0.3, 0.003, 0.0, 0.0, 24064, 2)
    ops.limitCurve('ThreePoint', 14064, 4064, 0.0, 148.09309513, 0.0134796, 148.09309513, 0.04043881, 103.66516659, -9314.22192132, 0.05, 2, 0, 74026, 24004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34064, 37.02327378, 4.12e-05, 111.06982135, 0.00012361, 370.23273783, 0.00041204, -37.02327378, -4.12e-05, -111.06982135, -0.00012361, -370.23273783, -0.00041204, 0.4, 0.3, 0.003, 0.0, 0.0, 14064, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4064, 99999, 'P', 44064, 'Vy', 34064, 'Vz', 24064, 'My', 14064, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174026, 74026, 174026, 4064, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124004, 124004, 24004, 4064, '-orient', 0, 0, 1, 0, 1, 0)
