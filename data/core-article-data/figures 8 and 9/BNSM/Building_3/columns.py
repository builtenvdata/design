import openseespy.opensees as ops


def add_columns() -> None:
    """Add components of all columns to ops domain (plastic hinges, column elements and nodes)
    """
    # Create elastic column element nodes
    ops.node(170001, 0.0, 0.0, 0.0)
    ops.node(121001, 0.0, 0.0, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1, 170001, 121001, 0.09, 26119670.70288791, 10883196.1262033, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20001, 65.26091738, 0.00125275, 79.10871277, 0.0196092, 7.91087128, 0.05784468, -65.26091738, -0.00125275, -79.10871277, -0.0196092, -7.91087128, -0.05784468, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10001, 65.26091738, 0.00125275, 79.10871277, 0.0196092, 7.91087128, 0.05784468, -65.26091738, -0.00125275, -79.10871277, -0.0196092, -7.91087128, -0.05784468, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20001, 1, 0.0, 102.19976842, 0.02505502, 102.19976842, 0.07516506, 71.5398379, -1436.51748171, 0.05, 2, 0, 70001, 21001, 2, 3)
    ops.uniaxialMaterial('LimitState', 40001, 25.54994211, 0.00010017, 76.64982632, 0.0003005, 255.49942105, 0.00100166, -25.54994211, -0.00010017, -76.64982632, -0.0003005, -255.49942105, -0.00100166, 0.4, 0.3, 0.003, 0.0, 0.0, 20001, 2)
    ops.limitCurve('ThreePoint', 10001, 1, 0.0, 102.19976842, 0.02505502, 102.19976842, 0.07516506, 71.5398379, -1436.51748171, 0.05, 2, 0, 70001, 21001, 1, 3)
    ops.uniaxialMaterial('LimitState', 30001, 25.54994211, 0.00010017, 76.64982632, 0.0003005, 255.49942105, 0.00100166, -25.54994211, -0.00010017, -76.64982632, -0.0003005, -255.49942105, -0.00100166, 0.4, 0.3, 0.003, 0.0, 0.0, 10001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1, 99999, 'P', 40001, 'Vy', 30001, 'Vz', 20001, 'My', 10001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170001, 70001, 170001, 1, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121001, 121001, 21001, 1, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170002, 7.4, 0.0, 0.0)
    ops.node(121002, 7.4, 0.0, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2, 170002, 121002, 0.16, 29572314.77056647, 12321797.82106936, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20002, 180.88286571, 0.00107142, 218.38713713, 0.02920158, 21.83871371, 0.07090433, -180.88286571, -0.00107142, -218.38713713, -0.02920158, -21.83871371, -0.07090433, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10002, 200.03230094, 0.00107142, 241.50701817, 0.02920158, 24.15070182, 0.07090433, -200.03230094, -0.00107142, -241.50701817, -0.02920158, -24.15070182, -0.07090433, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20002, 2, 0.0, 181.35919261, 0.02142833, 181.35919261, 0.06428498, 126.95143483, -2009.4671587, 0.05, 2, 0, 70002, 21002, 2, 3)
    ops.uniaxialMaterial('LimitState', 40002, 45.33979815, 8.831e-05, 136.01939446, 0.00026493, 453.39798153, 0.00088311, -45.33979815, -8.831e-05, -136.01939446, -0.00026493, -453.39798153, -0.00088311, 0.4, 0.3, 0.003, 0.0, 0.0, 20002, 2)
    ops.limitCurve('ThreePoint', 10002, 2, 0.0, 181.35919261, 0.02142833, 181.35919261, 0.06428498, 126.95143483, -2009.4671587, 0.05, 2, 0, 70002, 21002, 1, 3)
    ops.uniaxialMaterial('LimitState', 30002, 45.33979815, 8.831e-05, 136.01939446, 0.00026493, 453.39798153, 0.00088311, -45.33979815, -8.831e-05, -136.01939446, -0.00026493, -453.39798153, -0.00088311, 0.4, 0.3, 0.003, 0.0, 0.0, 10002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2, 99999, 'P', 40002, 'Vy', 30002, 'Vz', 20002, 'My', 10002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170002, 70002, 170002, 2, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121002, 121002, 21002, 2, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170005, 25.2, 0.0, 0.0)
    ops.node(121005, 25.2, 0.0, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 5, 170005, 121005, 0.16, 29066308.54822284, 12110961.89509285, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20005, 174.99519036, 0.00103149, 211.45922422, 0.02978382, 21.14592242, 0.07079711, -174.99519036, -0.00103149, -211.45922422, -0.02978382, -21.14592242, -0.07079711, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10005, 193.50871304, 0.00103149, 233.83043989, 0.02978382, 23.38304399, 0.07079711, -193.50871304, -0.00103149, -233.83043989, -0.02978382, -23.38304399, -0.07079711, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20005, 5, 0.0, 182.14079535, 0.0206298, 182.14079535, 0.0618894, 127.49855675, -2106.30300022, 0.05, 2, 0, 70005, 21005, 2, 3)
    ops.uniaxialMaterial('LimitState', 40005, 45.53519884, 9.024e-05, 136.60559651, 0.00027071, 455.35198838, 0.00090236, -45.53519884, -9.024e-05, -136.60559651, -0.00027071, -455.35198838, -0.00090236, 0.4, 0.3, 0.003, 0.0, 0.0, 20005, 2)
    ops.limitCurve('ThreePoint', 10005, 5, 0.0, 182.14079535, 0.0206298, 182.14079535, 0.0618894, 127.49855675, -2106.30300022, 0.05, 2, 0, 70005, 21005, 1, 3)
    ops.uniaxialMaterial('LimitState', 30005, 45.53519884, 9.024e-05, 136.60559651, 0.00027071, 455.35198838, 0.00090236, -45.53519884, -9.024e-05, -136.60559651, -0.00027071, -455.35198838, -0.00090236, 0.4, 0.3, 0.003, 0.0, 0.0, 10005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 5, 99999, 'P', 40005, 'Vy', 30005, 'Vz', 20005, 'My', 10005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170005, 70005, 170005, 5, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121005, 121005, 21005, 5, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170006, 32.6, 0.0, 0.0)
    ops.node(121006, 32.6, 0.0, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 6, 170006, 121006, 0.09, 28999916.03559846, 12083298.34816602, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20006, 67.79096131, 0.00116098, 81.94168314, 0.02006786, 8.19416831, 0.06330192, -67.79096131, -0.00116098, -81.94168314, -0.02006786, -8.19416831, -0.06330192, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10006, 67.79096131, 0.00116098, 81.94168314, 0.02006786, 8.19416831, 0.06330192, -67.79096131, -0.00116098, -81.94168314, -0.02006786, -8.19416831, -0.06330192, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20006, 6, 0.0, 111.96140231, 0.02321957, 111.96140231, 0.0696587, 78.37298162, -1509.83575431, 0.05, 2, 0, 70006, 21006, 2, 3)
    ops.uniaxialMaterial('LimitState', 40006, 27.99035058, 9.884e-05, 83.97105173, 0.00029651, 279.90350577, 0.00098835, -27.99035058, -9.884e-05, -83.97105173, -0.00029651, -279.90350577, -0.00098835, 0.4, 0.3, 0.003, 0.0, 0.0, 20006, 2)
    ops.limitCurve('ThreePoint', 10006, 6, 0.0, 111.96140231, 0.02321957, 111.96140231, 0.0696587, 78.37298162, -1509.83575431, 0.05, 2, 0, 70006, 21006, 1, 3)
    ops.uniaxialMaterial('LimitState', 30006, 27.99035058, 9.884e-05, 83.97105173, 0.00029651, 279.90350577, 0.00098835, -27.99035058, -9.884e-05, -83.97105173, -0.00029651, -279.90350577, -0.00098835, 0.4, 0.3, 0.003, 0.0, 0.0, 10006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 6, 99999, 'P', 40006, 'Vy', 30006, 'Vz', 20006, 'My', 10006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170006, 70006, 170006, 6, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121006, 121006, 21006, 6, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170007, 0.0, 3.5, 0.0)
    ops.node(121007, 0.0, 3.5, 2.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 7, 170007, 121007, 0.1225, 28588677.97429515, 11911949.15595631, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20007, 126.40957574, 0.00115876, 152.71284898, 0.02608702, 15.2712849, 0.06950187, -126.40957574, -0.00115876, -152.71284898, -0.02608702, -15.2712849, -0.06950187, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10007, 132.35458878, 0.00115876, 159.89489887, 0.02608702, 15.98948989, 0.06950187, -132.35458878, -0.00115876, -159.89489887, -0.02608702, -15.98948989, -0.06950187, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20007, 7, 0.0, 144.44072449, 0.02317511, 144.44072449, 0.06952534, 101.10850714, -1758.92760868, 0.05, 2, 0, 70007, 21007, 2, 3)
    ops.uniaxialMaterial('LimitState', 40007, 36.11018112, 9.503e-05, 108.33054337, 0.00028508, 361.10181122, 0.00095026, -36.11018112, -9.503e-05, -108.33054337, -0.00028508, -361.10181122, -0.00095026, 0.4, 0.3, 0.003, 0.0, 0.0, 20007, 2)
    ops.limitCurve('ThreePoint', 10007, 7, 0.0, 144.44072449, 0.02317511, 144.44072449, 0.06952534, 101.10850714, -1758.92760868, 0.05, 2, 0, 70007, 21007, 1, 3)
    ops.uniaxialMaterial('LimitState', 30007, 36.11018112, 9.503e-05, 108.33054337, 0.00028508, 361.10181122, 0.00095026, -36.11018112, -9.503e-05, -108.33054337, -0.00028508, -361.10181122, -0.00095026, 0.4, 0.3, 0.003, 0.0, 0.0, 10007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 7, 99999, 'P', 40007, 'Vy', 30007, 'Vz', 20007, 'My', 10007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170007, 70007, 170007, 7, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121007, 121007, 21007, 7, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170008, 7.4, 3.5, 0.0)
    ops.node(121008, 7.4, 3.5, 2.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 8, 170008, 121008, 0.16, 27933934.44590719, 11639139.35246133, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20008, 251.11237771, 0.00114616, 303.02750296, 0.03601345, 30.3027503, 0.08115976, -251.11237771, -0.00114616, -303.02750296, -0.03601345, -30.3027503, -0.08115976, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10008, 279.31681941, 0.00114616, 337.06294803, 0.03601345, 33.7062948, 0.08115976, -279.31681941, -0.00114616, -337.06294803, -0.03601345, -33.7062948, -0.08115976, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20008, 8, 0.0, 207.01027489, 0.02292312, 207.01027489, 0.06876936, 144.90719242, -2818.48809835, 0.05, 2, 0, 70008, 21008, 2, 3)
    ops.uniaxialMaterial('LimitState', 40008, 51.75256872, 0.00010671, 155.25770617, 0.00032014, 517.52568722, 0.00106714, -51.75256872, -0.00010671, -155.25770617, -0.00032014, -517.52568722, -0.00106714, 0.4, 0.3, 0.003, 0.0, 0.0, 20008, 2)
    ops.limitCurve('ThreePoint', 10008, 8, 0.0, 207.01027489, 0.02292312, 207.01027489, 0.06876936, 144.90719242, -2818.48809835, 0.05, 2, 0, 70008, 21008, 1, 3)
    ops.uniaxialMaterial('LimitState', 30008, 51.75256872, 0.00010671, 155.25770617, 0.00032014, 517.52568722, 0.00106714, -51.75256872, -0.00010671, -155.25770617, -0.00032014, -517.52568722, -0.00106714, 0.4, 0.3, 0.003, 0.0, 0.0, 10008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 8, 99999, 'P', 40008, 'Vy', 30008, 'Vz', 20008, 'My', 10008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170008, 70008, 170008, 8, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121008, 121008, 21008, 8, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170009, 14.8, 3.5, 0.0)
    ops.node(121009, 14.8, 3.5, 2.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 9, 170009, 121009, 0.1225, 29891199.07830913, 12454666.28262881, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20009, 163.53827445, 0.00111693, 196.81855491, 0.02378949, 19.68185549, 0.0669706, -163.53827445, -0.00111693, -196.81855491, -0.02378949, -19.68185549, -0.0669706, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10009, 170.59537168, 0.00111693, 205.31178185, 0.02378949, 20.53117818, 0.0669706, -170.59537168, -0.00111693, -205.31178185, -0.02378949, -20.53117818, -0.0669706, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20009, 9, 0.0, 162.62156777, 0.02233855, 162.62156777, 0.06701565, 113.83509744, -2038.49681674, 0.05, 2, 0, 70009, 21009, 2, 3)
    ops.uniaxialMaterial('LimitState', 40009, 40.65539194, 0.00010232, 121.96617583, 0.00030697, 406.55391942, 0.00102325, -40.65539194, -0.00010232, -121.96617583, -0.00030697, -406.55391942, -0.00102325, 0.4, 0.3, 0.003, 0.0, 0.0, 20009, 2)
    ops.limitCurve('ThreePoint', 10009, 9, 0.0, 162.62156777, 0.02233855, 162.62156777, 0.06701565, 113.83509744, -2038.49681674, 0.05, 2, 0, 70009, 21009, 1, 3)
    ops.uniaxialMaterial('LimitState', 30009, 40.65539194, 0.00010232, 121.96617583, 0.00030697, 406.55391942, 0.00102325, -40.65539194, -0.00010232, -121.96617583, -0.00030697, -406.55391942, -0.00102325, 0.4, 0.3, 0.003, 0.0, 0.0, 10009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 9, 99999, 'P', 40009, 'Vy', 30009, 'Vz', 20009, 'My', 10009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170009, 70009, 170009, 9, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121009, 121009, 21009, 9, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170010, 17.8, 3.5, 0.0)
    ops.node(121010, 17.8, 3.5, 2.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 10, 170010, 121010, 0.1225, 28440848.95627252, 11850353.73178022, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20010, 156.78436228, 0.00110582, 189.04742615, 0.0216378, 18.90474262, 0.0621849, -156.78436228, -0.00110582, -189.04742615, -0.0216378, -18.90474262, -0.0621849, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10010, 163.44521533, 0.00110582, 197.07894861, 0.0216378, 19.70789486, 0.0621849, -163.44521533, -0.00110582, -197.07894861, -0.0216378, -19.70789486, -0.0621849, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20010, 10, 0.0, 149.32074526, 0.02211643, 149.32074526, 0.06634929, 104.52452168, -1811.29847795, 0.05, 2, 0, 70010, 21010, 2, 3)
    ops.uniaxialMaterial('LimitState', 40010, 37.33018632, 9.875e-05, 111.99055895, 0.00029624, 373.30186315, 0.00098747, -37.33018632, -9.875e-05, -111.99055895, -0.00029624, -373.30186315, -0.00098747, 0.4, 0.3, 0.003, 0.0, 0.0, 20010, 2)
    ops.limitCurve('ThreePoint', 10010, 10, 0.0, 149.32074526, 0.02211643, 149.32074526, 0.06634929, 104.52452168, -1811.29847795, 0.05, 2, 0, 70010, 21010, 1, 3)
    ops.uniaxialMaterial('LimitState', 30010, 37.33018632, 9.875e-05, 111.99055895, 0.00029624, 373.30186315, 0.00098747, -37.33018632, -9.875e-05, -111.99055895, -0.00029624, -373.30186315, -0.00098747, 0.4, 0.3, 0.003, 0.0, 0.0, 10010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 10, 99999, 'P', 40010, 'Vy', 30010, 'Vz', 20010, 'My', 10010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170010, 70010, 170010, 10, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121010, 121010, 21010, 10, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170011, 25.2, 3.5, 0.0)
    ops.node(121011, 25.2, 3.5, 2.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 11, 170011, 121011, 0.16, 28275730.93428167, 11781554.55595069, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20011, 243.77058412, 0.00111478, 294.08074855, 0.03763748, 29.40807486, 0.08355567, -243.77058412, -0.00111478, -294.08074855, -0.03763748, -29.40807486, -0.08355567, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10011, 270.37643867, 0.00111478, 326.17760572, 0.03763748, 32.61776057, 0.08355567, -270.37643867, -0.00111478, -326.17760572, -0.03763748, -32.61776057, -0.08355567, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20011, 11, 0.0, 210.00701944, 0.02229552, 210.00701944, 0.06688656, 147.00491361, -2860.49394838, 0.05, 2, 0, 70011, 21011, 2, 3)
    ops.uniaxialMaterial('LimitState', 40011, 52.50175486, 0.00010695, 157.50526458, 0.00032085, 525.01754861, 0.0010695, -52.50175486, -0.00010695, -157.50526458, -0.00032085, -525.01754861, -0.0010695, 0.4, 0.3, 0.003, 0.0, 0.0, 20011, 2)
    ops.limitCurve('ThreePoint', 10011, 11, 0.0, 210.00701944, 0.02229552, 210.00701944, 0.06688656, 147.00491361, -2860.49394838, 0.05, 2, 0, 70011, 21011, 1, 3)
    ops.uniaxialMaterial('LimitState', 30011, 52.50175486, 0.00010695, 157.50526458, 0.00032085, 525.01754861, 0.0010695, -52.50175486, -0.00010695, -157.50526458, -0.00032085, -525.01754861, -0.0010695, 0.4, 0.3, 0.003, 0.0, 0.0, 10011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 11, 99999, 'P', 40011, 'Vy', 30011, 'Vz', 20011, 'My', 10011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170011, 70011, 170011, 11, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121011, 121011, 21011, 11, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170012, 32.6, 3.5, 0.0)
    ops.node(121012, 32.6, 3.5, 2.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 12, 170012, 121012, 0.1225, 29899976.45938116, 12458323.52474215, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20012, 123.67096932, 0.00106947, 149.0997956, 0.02929869, 14.90997956, 0.07483523, -123.67096932, -0.00106947, -149.0997956, -0.02929869, -14.90997956, -0.07483523, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10012, 129.56192235, 0.00106947, 156.20202741, 0.02929869, 15.62020274, 0.07483523, -129.56192235, -0.00106947, -156.20202741, -0.02929869, -15.62020274, -0.07483523, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20012, 12, 0.0, 163.39716484, 0.02138931, 163.39716484, 0.06416792, 114.37801539, -2209.09235168, 0.05, 2, 0, 70012, 21012, 2, 3)
    ops.uniaxialMaterial('LimitState', 40012, 40.84929121, 0.00010278, 122.54787363, 0.00030835, 408.49291209, 0.00102783, -40.84929121, -0.00010278, -122.54787363, -0.00030835, -408.49291209, -0.00102783, 0.4, 0.3, 0.003, 0.0, 0.0, 20012, 2)
    ops.limitCurve('ThreePoint', 10012, 12, 0.0, 163.39716484, 0.02138931, 163.39716484, 0.06416792, 114.37801539, -2209.09235168, 0.05, 2, 0, 70012, 21012, 1, 3)
    ops.uniaxialMaterial('LimitState', 30012, 40.84929121, 0.00010278, 122.54787363, 0.00030835, 408.49291209, 0.00102783, -40.84929121, -0.00010278, -122.54787363, -0.00030835, -408.49291209, -0.00102783, 0.4, 0.3, 0.003, 0.0, 0.0, 10012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 12, 99999, 'P', 40012, 'Vy', 30012, 'Vz', 20012, 'My', 10012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170012, 70012, 170012, 12, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121012, 121012, 21012, 12, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170013, 0.0, 7.0, 0.0)
    ops.node(121013, 0.0, 7.0, 2.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 13, 170013, 121013, 0.1225, 29480732.14386581, 12283638.39327742, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20013, 125.27045861, 0.00113843, 151.13806224, 0.02703048, 15.11380622, 0.0719222, -125.27045861, -0.00113843, -151.13806224, -0.02703048, -15.11380622, -0.0719222, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10013, 131.01399333, 0.00113843, 158.06760267, 0.02703048, 15.80676027, 0.0719222, -131.01399333, -0.00113843, -158.06760267, -0.02703048, -15.80676027, -0.0719222, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20013, 13, 0.0, 154.94482707, 0.02276865, 154.94482707, 0.06830596, 108.46137895, -1982.54709821, 0.05, 2, 0, 70013, 21013, 2, 3)
    ops.uniaxialMaterial('LimitState', 40013, 38.73620677, 9.885e-05, 116.2086203, 0.00029656, 387.36206768, 0.00098852, -38.73620677, -9.885e-05, -116.2086203, -0.00029656, -387.36206768, -0.00098852, 0.4, 0.3, 0.003, 0.0, 0.0, 20013, 2)
    ops.limitCurve('ThreePoint', 10013, 13, 0.0, 154.94482707, 0.02276865, 154.94482707, 0.06830596, 108.46137895, -1982.54709821, 0.05, 2, 0, 70013, 21013, 1, 3)
    ops.uniaxialMaterial('LimitState', 30013, 38.73620677, 9.885e-05, 116.2086203, 0.00029656, 387.36206768, 0.00098852, -38.73620677, -9.885e-05, -116.2086203, -0.00029656, -387.36206768, -0.00098852, 0.4, 0.3, 0.003, 0.0, 0.0, 10013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 13, 99999, 'P', 40013, 'Vy', 30013, 'Vz', 20013, 'My', 10013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170013, 70013, 170013, 13, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121013, 121013, 21013, 13, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170014, 7.4, 7.0, 0.0)
    ops.node(121014, 7.4, 7.0, 2.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 14, 170014, 121014, 0.16, 27468781.31711004, 11445325.54879585, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20014, 239.81243944, 0.00110502, 289.48225936, 0.03713602, 28.94822594, 0.08118676, -239.81243944, -0.00110502, -289.48225936, -0.03713602, -28.94822594, -0.08118676, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10014, 266.25589109, 0.00110502, 321.4026641, 0.03713602, 32.14026641, 0.08118676, -266.25589109, -0.00110502, -321.4026641, -0.03713602, -32.14026641, -0.08118676, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20014, 14, 0.0, 213.07885166, 0.02210036, 213.07885166, 0.06630108, 149.15519616, -3083.74838213, 0.05, 2, 0, 70014, 21014, 2, 3)
    ops.uniaxialMaterial('LimitState', 40014, 53.26971291, 0.0001117, 159.80913874, 0.00033511, 532.69712915, 0.00111703, -53.26971291, -0.0001117, -159.80913874, -0.00033511, -532.69712915, -0.00111703, 0.4, 0.3, 0.003, 0.0, 0.0, 20014, 2)
    ops.limitCurve('ThreePoint', 10014, 14, 0.0, 213.07885166, 0.02210036, 213.07885166, 0.06630108, 149.15519616, -3083.74838213, 0.05, 2, 0, 70014, 21014, 1, 3)
    ops.uniaxialMaterial('LimitState', 30014, 53.26971291, 0.0001117, 159.80913874, 0.00033511, 532.69712915, 0.00111703, -53.26971291, -0.0001117, -159.80913874, -0.00033511, -532.69712915, -0.00111703, 0.4, 0.3, 0.003, 0.0, 0.0, 10014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 14, 99999, 'P', 40014, 'Vy', 30014, 'Vz', 20014, 'My', 10014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170014, 70014, 170014, 14, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121014, 121014, 21014, 14, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170015, 14.8, 7.0, 0.0)
    ops.node(121015, 14.8, 7.0, 2.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 15, 170015, 121015, 0.1225, 29411701.51323947, 12254875.63051645, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20015, 150.46227085, 0.00108864, 181.45278323, 0.02126655, 18.14527832, 0.06532268, -150.46227085, -0.00108864, -181.45278323, -0.02126655, -18.14527832, -0.06532268, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10015, 156.72350116, 0.00108864, 189.00363076, 0.02126655, 18.90036308, 0.06532268, -156.72350116, -0.00108864, -189.00363076, -0.02126655, -18.90036308, -0.06532268, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20015, 15, 0.0, 148.21340083, 0.0217727, 148.21340083, 0.06531811, 103.74938058, -1745.57641936, 0.05, 2, 0, 70015, 21015, 2, 3)
    ops.uniaxialMaterial('LimitState', 40015, 37.05335021, 9.478e-05, 111.16005062, 0.00028434, 370.53350208, 0.00094779, -37.05335021, -9.478e-05, -111.16005062, -0.00028434, -370.53350208, -0.00094779, 0.4, 0.3, 0.003, 0.0, 0.0, 20015, 2)
    ops.limitCurve('ThreePoint', 10015, 15, 0.0, 148.21340083, 0.0217727, 148.21340083, 0.06531811, 103.74938058, -1745.57641936, 0.05, 2, 0, 70015, 21015, 1, 3)
    ops.uniaxialMaterial('LimitState', 30015, 37.05335021, 9.478e-05, 111.16005062, 0.00028434, 370.53350208, 0.00094779, -37.05335021, -9.478e-05, -111.16005062, -0.00028434, -370.53350208, -0.00094779, 0.4, 0.3, 0.003, 0.0, 0.0, 10015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 15, 99999, 'P', 40015, 'Vy', 30015, 'Vz', 20015, 'My', 10015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170015, 70015, 170015, 15, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121015, 121015, 21015, 15, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170016, 17.8, 7.0, 0.0)
    ops.node(121016, 17.8, 7.0, 2.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 16, 170016, 121016, 0.1225, 27811112.37580542, 11587963.48991892, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20016, 151.57617095, 0.00110641, 183.15498504, 0.02258778, 18.3154985, 0.06377014, -151.57617095, -0.00110641, -183.15498504, -0.02258778, -18.3154985, -0.06377014, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10016, 158.14673112, 0.00110641, 191.09443121, 0.02258778, 19.10944312, 0.06377014, -158.14673112, -0.00110641, -191.09443121, -0.02258778, -19.10944312, -0.06377014, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20016, 16, 0.0, 145.34578568, 0.02212828, 145.34578568, 0.06638483, 101.74204997, -1837.04169935, 0.05, 2, 0, 70016, 21016, 2, 3)
    ops.uniaxialMaterial('LimitState', 40016, 36.33644642, 9.829e-05, 109.00933926, 0.00029488, 363.36446419, 0.00098295, -36.33644642, -9.829e-05, -109.00933926, -0.00029488, -363.36446419, -0.00098295, 0.4, 0.3, 0.003, 0.0, 0.0, 20016, 2)
    ops.limitCurve('ThreePoint', 10016, 16, 0.0, 145.34578568, 0.02212828, 145.34578568, 0.06638483, 101.74204997, -1837.04169935, 0.05, 2, 0, 70016, 21016, 1, 3)
    ops.uniaxialMaterial('LimitState', 30016, 36.33644642, 9.829e-05, 109.00933926, 0.00029488, 363.36446419, 0.00098295, -36.33644642, -9.829e-05, -109.00933926, -0.00029488, -363.36446419, -0.00098295, 0.4, 0.3, 0.003, 0.0, 0.0, 10016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 16, 99999, 'P', 40016, 'Vy', 30016, 'Vz', 20016, 'My', 10016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170016, 70016, 170016, 16, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121016, 121016, 21016, 16, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170017, 25.2, 7.0, 0.0)
    ops.node(121017, 25.2, 7.0, 2.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 17, 170017, 121017, 0.16, 30777085.77421134, 12823785.73925472, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20017, 253.60435178, 0.00107302, 304.80660265, 0.03605112, 30.48066026, 0.08684234, -253.60435178, -0.00107302, -304.80660265, -0.03605112, -30.48066026, -0.08684234, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10017, 281.97777681, 0.00107302, 338.90856987, 0.03605112, 33.89085699, 0.08684234, -281.97777681, -0.00107302, -338.90856987, -0.03605112, -33.89085699, -0.08684234, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20017, 17, 0.0, 217.06103765, 0.02146042, 217.06103765, 0.06438126, 151.94272636, -2693.91473489, 0.05, 2, 0, 70017, 21017, 2, 3)
    ops.uniaxialMaterial('LimitState', 40017, 54.26525941, 0.00010156, 162.79577824, 0.00030468, 542.65259413, 0.00101559, -54.26525941, -0.00010156, -162.79577824, -0.00030468, -542.65259413, -0.00101559, 0.4, 0.3, 0.003, 0.0, 0.0, 20017, 2)
    ops.limitCurve('ThreePoint', 10017, 17, 0.0, 217.06103765, 0.02146042, 217.06103765, 0.06438126, 151.94272636, -2693.91473489, 0.05, 2, 0, 70017, 21017, 1, 3)
    ops.uniaxialMaterial('LimitState', 30017, 54.26525941, 0.00010156, 162.79577824, 0.00030468, 542.65259413, 0.00101559, -54.26525941, -0.00010156, -162.79577824, -0.00030468, -542.65259413, -0.00101559, 0.4, 0.3, 0.003, 0.0, 0.0, 10017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 17, 99999, 'P', 40017, 'Vy', 30017, 'Vz', 20017, 'My', 10017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170017, 70017, 170017, 17, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121017, 121017, 21017, 17, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170018, 32.6, 7.0, 0.0)
    ops.node(121018, 32.6, 7.0, 2.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 18, 170018, 121018, 0.1225, 31267157.87698254, 13027982.44874272, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20018, 124.4067707, 0.00109462, 149.56148851, 0.027236, 14.95614885, 0.07467702, -124.4067707, -0.00109462, -149.56148851, -0.027236, -14.95614885, -0.07467702, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10018, 129.99862863, 0.00109462, 156.28400521, 0.027236, 15.62840052, 0.07467702, -129.99862863, -0.00109462, -156.28400521, -0.027236, -15.62840052, -0.07467702, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20018, 18, 0.0, 160.23362228, 0.02189234, 160.23362228, 0.06567701, 112.1635356, -1933.59820181, 0.05, 2, 0, 70018, 21018, 2, 3)
    ops.uniaxialMaterial('LimitState', 40018, 40.05840557, 9.639e-05, 120.17521671, 0.00028916, 400.5840557, 0.00096385, -40.05840557, -9.639e-05, -120.17521671, -0.00028916, -400.5840557, -0.00096385, 0.4, 0.3, 0.003, 0.0, 0.0, 20018, 2)
    ops.limitCurve('ThreePoint', 10018, 18, 0.0, 160.23362228, 0.02189234, 160.23362228, 0.06567701, 112.1635356, -1933.59820181, 0.05, 2, 0, 70018, 21018, 1, 3)
    ops.uniaxialMaterial('LimitState', 30018, 40.05840557, 9.639e-05, 120.17521671, 0.00028916, 400.5840557, 0.00096385, -40.05840557, -9.639e-05, -120.17521671, -0.00028916, -400.5840557, -0.00096385, 0.4, 0.3, 0.003, 0.0, 0.0, 10018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 18, 99999, 'P', 40018, 'Vy', 30018, 'Vz', 20018, 'My', 10018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170018, 70018, 170018, 18, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121018, 121018, 21018, 18, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170019, 0.0, 10.5, 0.0)
    ops.node(121019, 0.0, 10.5, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 19, 170019, 121019, 0.09, 29326258.13271105, 12219274.22196294, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20019, 85.03047247, 0.00125257, 102.72445388, 0.01687772, 10.27244539, 0.06058048, -85.03047247, -0.00125257, -102.72445388, -0.01687772, -10.27244539, -0.06058048, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10019, 79.69263729, 0.00125257, 96.27586918, 0.01687772, 9.62758692, 0.06058048, -79.69263729, -0.00125257, -96.27586918, -0.01687772, -9.62758692, -0.06058048, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20019, 19, 0.0, 104.60482087, 0.02505142, 104.60482087, 0.07515425, 73.22337461, -1239.12119388, 0.05, 2, 0, 70019, 21019, 2, 3)
    ops.uniaxialMaterial('LimitState', 40019, 26.15120522, 9.131e-05, 78.45361565, 0.00027394, 261.51205217, 0.00091314, -26.15120522, -9.131e-05, -78.45361565, -0.00027394, -261.51205217, -0.00091314, 0.4, 0.3, 0.003, 0.0, 0.0, 20019, 2)
    ops.limitCurve('ThreePoint', 10019, 19, 0.0, 104.60482087, 0.02505142, 104.60482087, 0.07515425, 73.22337461, -1239.12119388, 0.05, 2, 0, 70019, 21019, 1, 3)
    ops.uniaxialMaterial('LimitState', 30019, 26.15120522, 9.131e-05, 78.45361565, 0.00027394, 261.51205217, 0.00091314, -26.15120522, -9.131e-05, -78.45361565, -0.00027394, -261.51205217, -0.00091314, 0.4, 0.3, 0.003, 0.0, 0.0, 10019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 19, 99999, 'P', 40019, 'Vy', 30019, 'Vz', 20019, 'My', 10019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170019, 70019, 170019, 19, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121019, 121019, 21019, 19, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170020, 7.4, 10.5, 0.0)
    ops.node(121020, 7.4, 10.5, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 20, 170020, 121020, 0.16, 31207483.07457853, 13003117.94774106, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20020, 189.60561455, 0.00108387, 228.1377327, 0.02789284, 22.81377327, 0.07156894, -189.60561455, -0.00108387, -228.1377327, -0.02789284, -22.81377327, -0.07156894, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10020, 210.16229918, 0.00108387, 252.87199722, 0.02789284, 25.28719972, 0.07156894, -210.16229918, -0.00108387, -252.87199722, -0.02789284, -25.28719972, -0.07156894, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20020, 20, 0.0, 186.57416881, 0.02167744, 186.57416881, 0.06503232, 130.60191817, -1924.84163387, 0.05, 2, 0, 70020, 21020, 2, 3)
    ops.uniaxialMaterial('LimitState', 40020, 46.6435422, 8.609e-05, 139.93062661, 0.00025827, 466.43542203, 0.00086091, -46.6435422, -8.609e-05, -139.93062661, -0.00025827, -466.43542203, -0.00086091, 0.4, 0.3, 0.003, 0.0, 0.0, 20020, 2)
    ops.limitCurve('ThreePoint', 10020, 20, 0.0, 186.57416881, 0.02167744, 186.57416881, 0.06503232, 130.60191817, -1924.84163387, 0.05, 2, 0, 70020, 21020, 1, 3)
    ops.uniaxialMaterial('LimitState', 30020, 46.6435422, 8.609e-05, 139.93062661, 0.00025827, 466.43542203, 0.00086091, -46.6435422, -8.609e-05, -139.93062661, -0.00025827, -466.43542203, -0.00086091, 0.4, 0.3, 0.003, 0.0, 0.0, 10020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 20, 99999, 'P', 40020, 'Vy', 30020, 'Vz', 20020, 'My', 10020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170020, 70020, 170020, 20, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121020, 121020, 21020, 20, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170021, 14.8, 10.5, 0.0)
    ops.node(121021, 14.8, 10.5, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 21, 170021, 121021, 0.1225, 26974783.30074484, 11239493.04197701, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20021, 136.02376862, 0.00113155, 164.94702697, 0.02581903, 16.4947027, 0.06895757, -136.02376862, -0.00113155, -164.94702697, -0.02581903, -16.4947027, -0.06895757, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10021, 136.02376862, 0.00113155, 164.94702697, 0.02581903, 16.4947027, 0.06895757, -136.02376862, -0.00113155, -164.94702697, -0.02581903, -16.4947027, -0.06895757, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20021, 21, 0.0, 153.67087981, 0.02263109, 153.67087981, 0.06789328, 107.56961587, -2448.32306459, 0.05, 2, 0, 70021, 21021, 2, 3)
    ops.uniaxialMaterial('LimitState', 40021, 38.41771995, 0.00010715, 115.25315986, 0.00032144, 384.17719952, 0.00107147, -38.41771995, -0.00010715, -115.25315986, -0.00032144, -384.17719952, -0.00107147, 0.4, 0.3, 0.003, 0.0, 0.0, 20021, 2)
    ops.limitCurve('ThreePoint', 10021, 21, 0.0, 153.67087981, 0.02263109, 153.67087981, 0.06789328, 107.56961587, -2448.32306459, 0.05, 2, 0, 70021, 21021, 1, 3)
    ops.uniaxialMaterial('LimitState', 30021, 38.41771995, 0.00010715, 115.25315986, 0.00032144, 384.17719952, 0.00107147, -38.41771995, -0.00010715, -115.25315986, -0.00032144, -384.17719952, -0.00107147, 0.4, 0.3, 0.003, 0.0, 0.0, 10021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 21, 99999, 'P', 40021, 'Vy', 30021, 'Vz', 20021, 'My', 10021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170021, 70021, 170021, 21, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121021, 121021, 21021, 21, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170022, 17.8, 10.5, 0.0)
    ops.node(121022, 17.8, 10.5, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 22, 170022, 121022, 0.1225, 29374857.33694636, 12239523.89039432, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20022, 135.32411345, 0.00108734, 163.57266088, 0.02368038, 16.35726609, 0.07071967, -135.32411345, -0.00108734, -163.57266088, -0.02368038, -16.35726609, -0.07071967, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10022, 135.32411345, 0.00108734, 163.57266088, 0.02368038, 16.35726609, 0.07071967, -135.32411345, -0.00108734, -163.57266088, -0.02368038, -16.35726609, -0.07071967, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20022, 22, 0.0, 150.09975556, 0.02174689, 150.09975556, 0.06524066, 105.06982889, -1994.40132203, 0.05, 2, 0, 70022, 21022, 2, 3)
    ops.uniaxialMaterial('LimitState', 40022, 37.52493889, 9.611e-05, 112.57481667, 0.00028832, 375.24938891, 0.00096106, -37.52493889, -9.611e-05, -112.57481667, -0.00028832, -375.24938891, -0.00096106, 0.4, 0.3, 0.003, 0.0, 0.0, 20022, 2)
    ops.limitCurve('ThreePoint', 10022, 22, 0.0, 150.09975556, 0.02174689, 150.09975556, 0.06524066, 105.06982889, -1994.40132203, 0.05, 2, 0, 70022, 21022, 1, 3)
    ops.uniaxialMaterial('LimitState', 30022, 37.52493889, 9.611e-05, 112.57481667, 0.00028832, 375.24938891, 0.00096106, -37.52493889, -9.611e-05, -112.57481667, -0.00028832, -375.24938891, -0.00096106, 0.4, 0.3, 0.003, 0.0, 0.0, 10022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 22, 99999, 'P', 40022, 'Vy', 30022, 'Vz', 20022, 'My', 10022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170022, 70022, 170022, 22, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121022, 121022, 21022, 22, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170023, 25.2, 10.5, 0.0)
    ops.node(121023, 25.2, 10.5, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 23, 170023, 121023, 0.16, 26806364.07744209, 11169318.36560087, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20023, 181.33426761, 0.00111438, 219.67766069, 0.03031849, 21.96776607, 0.06771372, -181.33426761, -0.00111438, -219.67766069, -0.03031849, -21.96776607, -0.06771372, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10023, 201.60184086, 0.00111438, 244.23084161, 0.03031849, 24.42308416, 0.06771372, -201.60184086, -0.00111438, -244.23084161, -0.03031849, -24.42308416, -0.06771372, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20023, 23, 0.0, 171.10726715, 0.02228758, 171.10726715, 0.06686273, 119.775087, -2096.40311755, 0.05, 2, 0, 70023, 21023, 2, 3)
    ops.uniaxialMaterial('LimitState', 40023, 42.77681679, 9.192e-05, 128.33045036, 0.00027575, 427.76816787, 0.00091916, -42.77681679, -9.192e-05, -128.33045036, -0.00027575, -427.76816787, -0.00091916, 0.4, 0.3, 0.003, 0.0, 0.0, 20023, 2)
    ops.limitCurve('ThreePoint', 10023, 23, 0.0, 171.10726715, 0.02228758, 171.10726715, 0.06686273, 119.775087, -2096.40311755, 0.05, 2, 0, 70023, 21023, 1, 3)
    ops.uniaxialMaterial('LimitState', 30023, 42.77681679, 9.192e-05, 128.33045036, 0.00027575, 427.76816787, 0.00091916, -42.77681679, -9.192e-05, -128.33045036, -0.00027575, -427.76816787, -0.00091916, 0.4, 0.3, 0.003, 0.0, 0.0, 10023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 23, 99999, 'P', 40023, 'Vy', 30023, 'Vz', 20023, 'My', 10023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170023, 70023, 170023, 23, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121023, 121023, 21023, 23, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170024, 32.6, 10.5, 0.0)
    ops.node(121024, 32.6, 10.5, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 24, 170024, 121024, 0.09, 29034381.50609666, 12097658.96087361, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20024, 82.9557996, 0.00122897, 100.26653096, 0.01682681, 10.0266531, 0.0601112, -82.9557996, -0.00122897, -100.26653096, -0.01682681, -10.0266531, -0.0601112, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10024, 77.80770612, 0.00122897, 94.04416343, 0.01682681, 9.40441634, 0.0601112, -77.80770612, -0.00122897, -94.04416343, -0.01682681, -9.40441634, -0.0601112, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20024, 24, 0.0, 103.65423316, 0.02457934, 103.65423316, 0.07373801, 72.55796321, -1234.28088031, 0.05, 2, 0, 70024, 21024, 2, 3)
    ops.uniaxialMaterial('LimitState', 40024, 25.91355829, 9.139e-05, 77.74067487, 0.00027418, 259.13558291, 0.00091393, -25.91355829, -9.139e-05, -77.74067487, -0.00027418, -259.13558291, -0.00091393, 0.4, 0.3, 0.003, 0.0, 0.0, 20024, 2)
    ops.limitCurve('ThreePoint', 10024, 24, 0.0, 103.65423316, 0.02457934, 103.65423316, 0.07373801, 72.55796321, -1234.28088031, 0.05, 2, 0, 70024, 21024, 1, 3)
    ops.uniaxialMaterial('LimitState', 30024, 25.91355829, 9.139e-05, 77.74067487, 0.00027418, 259.13558291, 0.00091393, -25.91355829, -9.139e-05, -77.74067487, -0.00027418, -259.13558291, -0.00091393, 0.4, 0.3, 0.003, 0.0, 0.0, 10024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 24, 99999, 'P', 40024, 'Vy', 30024, 'Vz', 20024, 'My', 10024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170024, 70024, 170024, 24, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121024, 121024, 21024, 24, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171001, 0.0, 0.0, 3.5)
    ops.node(122001, 0.0, 0.0, 6.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1001, 171001, 122001, 0.09, 27146703.3221064, 11311126.384211, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21001, 78.95482932, 0.00132565, 95.98696792, 0.02157819, 9.59869679, 0.06622391, -78.95482932, -0.00132565, -95.98696792, -0.02157819, -9.59869679, -0.06622391, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11001, 65.80461884, 0.00132565, 79.99999357, 0.02157819, 7.99999936, 0.06622391, -65.80461884, -0.00132565, -79.99999357, -0.02157819, -7.99999936, -0.06622391, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21001, 1001, 0.0, 104.84887028, 0.026513, 104.84887028, 0.07953901, 73.39420919, -1715.02095695, 0.05, 2, 0, 71001, 22001, 2, 3)
    ops.uniaxialMaterial('LimitState', 41001, 26.21221757, 9.888e-05, 78.63665271, 0.00029663, 262.12217569, 0.00098875, -26.21221757, -9.888e-05, -78.63665271, -0.00029663, -262.12217569, -0.00098875, 0.4, 0.3, 0.003, 0.0, 0.0, 21001, 2)
    ops.limitCurve('ThreePoint', 11001, 1001, 0.0, 104.84887028, 0.026513, 104.84887028, 0.07953901, 73.39420919, -1715.02095695, 0.05, 2, 0, 71001, 22001, 1, 3)
    ops.uniaxialMaterial('LimitState', 31001, 26.21221757, 9.888e-05, 78.63665271, 0.00029663, 262.12217569, 0.00098875, -26.21221757, -9.888e-05, -78.63665271, -0.00029663, -262.12217569, -0.00098875, 0.4, 0.3, 0.003, 0.0, 0.0, 11001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1001, 99999, 'P', 41001, 'Vy', 31001, 'Vz', 21001, 'My', 11001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171001, 71001, 171001, 1001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122001, 122001, 22001, 1001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171002, 7.4, 0.0, 3.5)
    ops.node(122002, 7.4, 0.0, 6.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1002, 171002, 122002, 0.16, 27411289.06153249, 11421370.4423052, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21002, 139.78300597, 0.00107431, 169.84148032, 0.02087627, 16.98414803, 0.0527965, -139.78300597, -0.00107431, -169.84148032, -0.02087627, -16.98414803, -0.0527965, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11002, 139.78300597, 0.00107431, 169.84148032, 0.02087627, 16.98414803, 0.0527965, -139.78300597, -0.00107431, -169.84148032, -0.02087627, -16.98414803, -0.0527965, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21002, 1002, 0.0, 145.17870727, 0.02148615, 145.17870727, 0.06445845, 101.62509509, -1469.13047017, 0.05, 2, 0, 71002, 22002, 2, 3)
    ops.uniaxialMaterial('LimitState', 41002, 36.29467682, 7.627e-05, 108.88403045, 0.0002288, 362.94676817, 0.00076267, -36.29467682, -7.627e-05, -108.88403045, -0.0002288, -362.94676817, -0.00076267, 0.4, 0.3, 0.003, 0.0, 0.0, 21002, 2)
    ops.limitCurve('ThreePoint', 11002, 1002, 0.0, 145.17870727, 0.02148615, 145.17870727, 0.06445845, 101.62509509, -1469.13047017, 0.05, 2, 0, 71002, 22002, 1, 3)
    ops.uniaxialMaterial('LimitState', 31002, 36.29467682, 7.627e-05, 108.88403045, 0.0002288, 362.94676817, 0.00076267, -36.29467682, -7.627e-05, -108.88403045, -0.0002288, -362.94676817, -0.00076267, 0.4, 0.3, 0.003, 0.0, 0.0, 11002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1002, 99999, 'P', 41002, 'Vy', 31002, 'Vz', 21002, 'My', 11002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171002, 71002, 171002, 1002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122002, 122002, 22002, 1002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171005, 25.2, 0.0, 3.5)
    ops.node(122005, 25.2, 0.0, 6.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1005, 171005, 122005, 0.16, 29786223.56417813, 12410926.48507422, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21005, 140.68772253, 0.00099584, 170.23278572, 0.02204719, 17.02327857, 0.05604392, -140.68772253, -0.00099584, -170.23278572, -0.02204719, -17.02327857, -0.05604392, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11005, 140.68772253, 0.00099584, 170.23278572, 0.02204719, 17.02327857, 0.05604392, -140.68772253, -0.00099584, -170.23278572, -0.02204719, -17.02327857, -0.05604392, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21005, 1005, 0.0, 160.26750549, 0.01991683, 160.26750549, 0.05975049, 112.18725384, -1587.97228624, 0.05, 2, 0, 71005, 22005, 2, 3)
    ops.uniaxialMaterial('LimitState', 41005, 40.06687637, 7.748e-05, 120.20062912, 0.00023244, 400.66876373, 0.00077481, -40.06687637, -7.748e-05, -120.20062912, -0.00023244, -400.66876373, -0.00077481, 0.4, 0.3, 0.003, 0.0, 0.0, 21005, 2)
    ops.limitCurve('ThreePoint', 11005, 1005, 0.0, 160.26750549, 0.01991683, 160.26750549, 0.05975049, 112.18725384, -1587.97228624, 0.05, 2, 0, 71005, 22005, 1, 3)
    ops.uniaxialMaterial('LimitState', 31005, 40.06687637, 7.748e-05, 120.20062912, 0.00023244, 400.66876373, 0.00077481, -40.06687637, -7.748e-05, -120.20062912, -0.00023244, -400.66876373, -0.00077481, 0.4, 0.3, 0.003, 0.0, 0.0, 11005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1005, 99999, 'P', 41005, 'Vy', 31005, 'Vz', 21005, 'My', 11005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171005, 71005, 171005, 1005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122005, 122005, 22005, 1005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171006, 32.6, 0.0, 3.5)
    ops.node(122006, 32.6, 0.0, 6.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1006, 171006, 122006, 0.09, 28056698.06312323, 11690290.85963468, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21006, 75.3381675, 0.00119043, 91.47187862, 0.01968386, 9.14718786, 0.06556557, -75.3381675, -0.00119043, -91.47187862, -0.01968386, -9.14718786, -0.06556557, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11006, 62.51500441, 0.00119043, 75.90262791, 0.01968386, 7.59026279, 0.06556557, -62.51500441, -0.00119043, -75.90262791, -0.01968386, -7.59026279, -0.06556557, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21006, 1006, 0.0, 100.89823095, 0.02380854, 100.89823095, 0.07142562, 70.62876166, -1452.0724654, 0.05, 2, 0, 71006, 22006, 2, 3)
    ops.uniaxialMaterial('LimitState', 41006, 25.22455774, 9.206e-05, 75.67367321, 0.00027619, 252.24557737, 0.00092063, -25.22455774, -9.206e-05, -75.67367321, -0.00027619, -252.24557737, -0.00092063, 0.4, 0.3, 0.003, 0.0, 0.0, 21006, 2)
    ops.limitCurve('ThreePoint', 11006, 1006, 0.0, 100.89823095, 0.02380854, 100.89823095, 0.07142562, 70.62876166, -1452.0724654, 0.05, 2, 0, 71006, 22006, 1, 3)
    ops.uniaxialMaterial('LimitState', 31006, 25.22455774, 9.206e-05, 75.67367321, 0.00027619, 252.24557737, 0.00092063, -25.22455774, -9.206e-05, -75.67367321, -0.00027619, -252.24557737, -0.00092063, 0.4, 0.3, 0.003, 0.0, 0.0, 11006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1006, 99999, 'P', 41006, 'Vy', 31006, 'Vz', 21006, 'My', 11006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171006, 71006, 171006, 1006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122006, 122006, 22006, 1006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171007, 0.0, 3.5, 3.525)
    ops.node(122007, 0.0, 3.5, 6.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1007, 171007, 122007, 0.1225, 27242382.07450357, 11350992.53104316, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21007, 141.48941679, 0.00116259, 171.80899109, 0.03606512, 17.18089911, 0.09374678, -141.48941679, -0.00116259, -171.80899109, -0.03606512, -17.18089911, -0.09374678, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11007, 117.68408392, 0.00116259, 142.90244587, 0.03606512, 14.29024459, 0.09374678, -117.68408392, -0.00116259, -142.90244587, -0.03606512, -14.29024459, -0.09374678, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21007, 1007, 0.0, 154.94139798, 0.02325174, 154.94139798, 0.06975523, 108.45897858, -2682.78594426, 0.05, 2, 0, 71007, 22007, 2, 3)
    ops.uniaxialMaterial('LimitState', 41007, 38.73534949, 0.00010697, 116.20604848, 0.00032092, 387.35349494, 0.00106972, -38.73534949, -0.00010697, -116.20604848, -0.00032092, -387.35349494, -0.00106972, 0.4, 0.3, 0.003, 0.0, 0.0, 21007, 2)
    ops.limitCurve('ThreePoint', 11007, 1007, 0.0, 154.94139798, 0.02325174, 154.94139798, 0.06975523, 108.45897858, -2682.78594426, 0.05, 2, 0, 71007, 22007, 1, 3)
    ops.uniaxialMaterial('LimitState', 31007, 38.73534949, 0.00010697, 116.20604848, 0.00032092, 387.35349494, 0.00106972, -38.73534949, -0.00010697, -116.20604848, -0.00032092, -387.35349494, -0.00106972, 0.4, 0.3, 0.003, 0.0, 0.0, 11007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1007, 99999, 'P', 41007, 'Vy', 31007, 'Vz', 21007, 'My', 11007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171007, 71007, 171007, 1007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122007, 122007, 22007, 1007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171008, 7.4, 3.5, 3.525)
    ops.node(122008, 7.4, 3.5, 6.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1008, 171008, 122008, 0.16, 28024539.16208893, 11676891.31753705, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21008, 148.01861464, 0.00103097, 179.29059607, 0.02876294, 17.92905961, 0.06936532, -148.01861464, -0.00103097, -179.29059607, -0.02876294, -17.92905961, -0.06936532, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11008, 148.01861464, 0.00103097, 179.29059607, 0.02876294, 17.92905961, 0.06936532, -148.01861464, -0.00103097, -179.29059607, -0.02876294, -17.92905961, -0.06936532, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21008, 1008, 0.0, 175.09357578, 0.02061935, 175.09357578, 0.06185806, 122.56550305, -2120.18179407, 0.05, 2, 0, 71008, 22008, 2, 3)
    ops.uniaxialMaterial('LimitState', 41008, 43.77339395, 8.997e-05, 131.32018184, 0.00026991, 437.73393946, 0.00089969, -43.77339395, -8.997e-05, -131.32018184, -0.00026991, -437.73393946, -0.00089969, 0.4, 0.3, 0.003, 0.0, 0.0, 21008, 2)
    ops.limitCurve('ThreePoint', 11008, 1008, 0.0, 175.09357578, 0.02061935, 175.09357578, 0.06185806, 122.56550305, -2120.18179407, 0.05, 2, 0, 71008, 22008, 1, 3)
    ops.uniaxialMaterial('LimitState', 31008, 43.77339395, 8.997e-05, 131.32018184, 0.00026991, 437.73393946, 0.00089969, -43.77339395, -8.997e-05, -131.32018184, -0.00026991, -437.73393946, -0.00089969, 0.4, 0.3, 0.003, 0.0, 0.0, 11008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1008, 99999, 'P', 41008, 'Vy', 31008, 'Vz', 21008, 'My', 11008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171008, 71008, 171008, 1008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122008, 122008, 22008, 1008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171009, 14.8, 3.5, 3.525)
    ops.node(122009, 14.8, 3.5, 6.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1009, 171009, 122009, 0.1225, 28680077.64586187, 11950032.35244245, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21009, 119.42074772, 0.00100692, 144.4744666, 0.02424006, 14.44744666, 0.06985629, -119.42074772, -0.00100692, -144.4744666, -0.02424006, -14.44744666, -0.06985629, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11009, 106.85286074, 0.00100692, 129.26991628, 0.02424006, 12.92699163, 0.06985629, -106.85286074, -0.00100692, -129.26991628, -0.02424006, -12.92699163, -0.06985629, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21009, 1009, 0.0, 152.19049386, 0.02013843, 152.19049386, 0.06041529, 106.5333457, -2128.08377047, 0.05, 2, 0, 71009, 22009, 2, 3)
    ops.uniaxialMaterial('LimitState', 41009, 38.04762347, 9.981e-05, 114.1428704, 0.00029942, 380.47623465, 0.00099805, -38.04762347, -9.981e-05, -114.1428704, -0.00029942, -380.47623465, -0.00099805, 0.4, 0.3, 0.003, 0.0, 0.0, 21009, 2)
    ops.limitCurve('ThreePoint', 11009, 1009, 0.0, 152.19049386, 0.02013843, 152.19049386, 0.06041529, 106.5333457, -2128.08377047, 0.05, 2, 0, 71009, 22009, 1, 3)
    ops.uniaxialMaterial('LimitState', 31009, 38.04762347, 9.981e-05, 114.1428704, 0.00029942, 380.47623465, 0.00099805, -38.04762347, -9.981e-05, -114.1428704, -0.00029942, -380.47623465, -0.00099805, 0.4, 0.3, 0.003, 0.0, 0.0, 11009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1009, 99999, 'P', 41009, 'Vy', 31009, 'Vz', 21009, 'My', 11009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171009, 71009, 171009, 1009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122009, 122009, 22009, 1009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171010, 17.8, 3.5, 3.525)
    ops.node(122010, 17.8, 3.5, 6.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1010, 171010, 122010, 0.1225, 29209679.05183822, 12170699.60493259, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21010, 123.62535535, 0.00106108, 149.43386276, 0.023985, 14.94338628, 0.07040214, -123.62535535, -0.00106108, -149.43386276, -0.023985, -14.94338628, -0.07040214, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11010, 110.78155429, 0.00106108, 133.9087401, 0.023985, 13.39087401, 0.07040214, -110.78155429, -0.00106108, -133.9087401, -0.023985, -13.39087401, -0.07040214, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21010, 1010, 0.0, 153.20504895, 0.0212215, 153.20504895, 0.06366451, 107.24353427, -2094.77070032, 0.05, 2, 0, 71010, 22010, 2, 3)
    ops.uniaxialMaterial('LimitState', 41010, 38.30126224, 9.865e-05, 114.90378672, 0.00029595, 383.01262238, 0.00098649, -38.30126224, -9.865e-05, -114.90378672, -0.00029595, -383.01262238, -0.00098649, 0.4, 0.3, 0.003, 0.0, 0.0, 21010, 2)
    ops.limitCurve('ThreePoint', 11010, 1010, 0.0, 153.20504895, 0.0212215, 153.20504895, 0.06366451, 107.24353427, -2094.77070032, 0.05, 2, 0, 71010, 22010, 1, 3)
    ops.uniaxialMaterial('LimitState', 31010, 38.30126224, 9.865e-05, 114.90378672, 0.00029595, 383.01262238, 0.00098649, -38.30126224, -9.865e-05, -114.90378672, -0.00029595, -383.01262238, -0.00098649, 0.4, 0.3, 0.003, 0.0, 0.0, 11010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1010, 99999, 'P', 41010, 'Vy', 31010, 'Vz', 21010, 'My', 11010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171010, 71010, 171010, 1010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122010, 122010, 22010, 1010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171011, 25.2, 3.5, 3.525)
    ops.node(122011, 25.2, 3.5, 6.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1011, 171011, 122011, 0.16, 27916710.31017665, 11631962.62924027, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21011, 153.24828173, 0.00104982, 185.65039811, 0.02770137, 18.56503981, 0.06814221, -153.24828173, -0.00104982, -185.65039811, -0.02770137, -18.56503981, -0.06814221, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11011, 153.24828173, 0.00104982, 185.65039811, 0.02770137, 18.56503981, 0.06814221, -153.24828173, -0.00104982, -185.65039811, -0.02770137, -18.56503981, -0.06814221, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21011, 1011, 0.0, 171.11500243, 0.0209964, 171.11500243, 0.06298919, 119.7805017, -2011.64226586, 0.05, 2, 0, 71011, 22011, 2, 3)
    ops.uniaxialMaterial('LimitState', 41011, 42.77875061, 8.826e-05, 128.33625182, 0.00026479, 427.78750608, 0.00088265, -42.77875061, -8.826e-05, -128.33625182, -0.00026479, -427.78750608, -0.00088265, 0.4, 0.3, 0.003, 0.0, 0.0, 21011, 2)
    ops.limitCurve('ThreePoint', 11011, 1011, 0.0, 171.11500243, 0.0209964, 171.11500243, 0.06298919, 119.7805017, -2011.64226586, 0.05, 2, 0, 71011, 22011, 1, 3)
    ops.uniaxialMaterial('LimitState', 31011, 42.77875061, 8.826e-05, 128.33625182, 0.00026479, 427.78750608, 0.00088265, -42.77875061, -8.826e-05, -128.33625182, -0.00026479, -427.78750608, -0.00088265, 0.4, 0.3, 0.003, 0.0, 0.0, 11011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1011, 99999, 'P', 41011, 'Vy', 31011, 'Vz', 21011, 'My', 11011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171011, 71011, 171011, 1011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122011, 122011, 22011, 1011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171012, 32.6, 3.5, 3.525)
    ops.node(122012, 32.6, 3.5, 6.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1012, 171012, 122012, 0.1225, 29991765.57221067, 12496568.98842111, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21012, 140.16201319, 0.00111628, 169.41771689, 0.0368337, 16.94177169, 0.09930339, -140.16201319, -0.00111628, -169.41771689, -0.0368337, -16.94177169, -0.09930339, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11012, 117.53334017, 0.00111628, 142.06581153, 0.0368337, 14.20658115, 0.09930339, -117.53334017, -0.00111628, -142.06581153, -0.0368337, -14.20658115, -0.09930339, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21012, 1012, 0.0, 168.44205329, 0.02232553, 168.44205329, 0.0669766, 117.9094373, -2841.05828957, 0.05, 2, 0, 71012, 22012, 2, 3)
    ops.uniaxialMaterial('LimitState', 41012, 42.11051332, 0.00010563, 126.33153997, 0.0003169, 421.10513322, 0.00105632, -42.11051332, -0.00010563, -126.33153997, -0.0003169, -421.10513322, -0.00105632, 0.4, 0.3, 0.003, 0.0, 0.0, 21012, 2)
    ops.limitCurve('ThreePoint', 11012, 1012, 0.0, 168.44205329, 0.02232553, 168.44205329, 0.0669766, 117.9094373, -2841.05828957, 0.05, 2, 0, 71012, 22012, 1, 3)
    ops.uniaxialMaterial('LimitState', 31012, 42.11051332, 0.00010563, 126.33153997, 0.0003169, 421.10513322, 0.00105632, -42.11051332, -0.00010563, -126.33153997, -0.0003169, -421.10513322, -0.00105632, 0.4, 0.3, 0.003, 0.0, 0.0, 11012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1012, 99999, 'P', 41012, 'Vy', 31012, 'Vz', 21012, 'My', 11012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171012, 71012, 171012, 1012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122012, 122012, 22012, 1012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171013, 0.0, 7.0, 3.525)
    ops.node(122013, 0.0, 7.0, 6.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1013, 171013, 122013, 0.1225, 29277024.7654951, 12198760.31895629, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21013, 139.07634801, 0.00112834, 168.35004549, 0.0349231, 16.83500455, 0.09629863, -139.07634801, -0.00112834, -168.35004549, -0.0349231, -16.83500455, -0.09629863, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11013, 116.70294883, 0.00112834, 141.26734722, 0.0349231, 14.12673472, 0.09629863, -116.70294883, -0.00112834, -141.26734722, -0.0349231, -14.12673472, -0.09629863, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21013, 1013, 0.0, 156.31758102, 0.02256681, 156.31758102, 0.06770042, 109.42230671, -2428.18127773, 0.05, 2, 0, 71013, 22013, 2, 3)
    ops.uniaxialMaterial('LimitState', 41013, 39.07939525, 0.00010042, 117.23818576, 0.00030126, 390.79395255, 0.00100422, -39.07939525, -0.00010042, -117.23818576, -0.00030126, -390.79395255, -0.00100422, 0.4, 0.3, 0.003, 0.0, 0.0, 21013, 2)
    ops.limitCurve('ThreePoint', 11013, 1013, 0.0, 156.31758102, 0.02256681, 156.31758102, 0.06770042, 109.42230671, -2428.18127773, 0.05, 2, 0, 71013, 22013, 1, 3)
    ops.uniaxialMaterial('LimitState', 31013, 39.07939525, 0.00010042, 117.23818576, 0.00030126, 390.79395255, 0.00100422, -39.07939525, -0.00010042, -117.23818576, -0.00030126, -390.79395255, -0.00100422, 0.4, 0.3, 0.003, 0.0, 0.0, 11013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1013, 99999, 'P', 41013, 'Vy', 31013, 'Vz', 21013, 'My', 11013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171013, 71013, 171013, 1013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122013, 122013, 22013, 1013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171014, 7.4, 7.0, 3.525)
    ops.node(122014, 7.4, 7.0, 6.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1014, 171014, 122014, 0.16, 29374815.93712174, 12239506.64046739, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21014, 149.17164083, 0.00101657, 180.31041808, 0.02856088, 18.03104181, 0.07102159, -149.17164083, -0.00101657, -180.31041808, -0.02856088, -18.03104181, -0.07102159, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11014, 149.17164083, 0.00101657, 180.31041808, 0.02856088, 18.03104181, 0.07102159, -149.17164083, -0.00101657, -180.31041808, -0.02856088, -18.03104181, -0.07102159, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21014, 1014, 0.0, 183.42535271, 0.02033141, 183.42535271, 0.06099422, 128.3977469, -2180.16296037, 0.05, 2, 0, 71014, 22014, 2, 3)
    ops.uniaxialMaterial('LimitState', 41014, 45.85633818, 8.992e-05, 137.56901454, 0.00026975, 458.56338179, 0.00089918, -45.85633818, -8.992e-05, -137.56901454, -0.00026975, -458.56338179, -0.00089918, 0.4, 0.3, 0.003, 0.0, 0.0, 21014, 2)
    ops.limitCurve('ThreePoint', 11014, 1014, 0.0, 183.42535271, 0.02033141, 183.42535271, 0.06099422, 128.3977469, -2180.16296037, 0.05, 2, 0, 71014, 22014, 1, 3)
    ops.uniaxialMaterial('LimitState', 31014, 45.85633818, 8.992e-05, 137.56901454, 0.00026975, 458.56338179, 0.00089918, -45.85633818, -8.992e-05, -137.56901454, -0.00026975, -458.56338179, -0.00089918, 0.4, 0.3, 0.003, 0.0, 0.0, 11014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1014, 99999, 'P', 41014, 'Vy', 31014, 'Vz', 21014, 'My', 11014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171014, 71014, 171014, 1014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122014, 122014, 22014, 1014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171015, 14.8, 7.0, 3.525)
    ops.node(122015, 14.8, 7.0, 6.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1015, 171015, 122015, 0.1225, 28849840.55794065, 12020766.89914194, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21015, 116.91176751, 0.00099999, 141.55841886, 0.02467157, 14.15584189, 0.0720854, -116.91176751, -0.00099999, -141.55841886, -0.02467157, -14.15584189, -0.0720854, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11015, 104.19877865, 0.00099999, 126.16535244, 0.02467157, 12.61653524, 0.0720854, -104.19877865, -0.00099999, -126.16535244, -0.02467157, -12.61653524, -0.0720854, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21015, 1015, 0.0, 149.56720016, 0.01999985, 149.56720016, 0.05999955, 104.69704011, -2142.10633883, 0.05, 2, 0, 71015, 22015, 2, 3)
    ops.uniaxialMaterial('LimitState', 41015, 37.39180004, 9.751e-05, 112.17540012, 0.00029252, 373.91800039, 0.00097508, -37.39180004, -9.751e-05, -112.17540012, -0.00029252, -373.91800039, -0.00097508, 0.4, 0.3, 0.003, 0.0, 0.0, 21015, 2)
    ops.limitCurve('ThreePoint', 11015, 1015, 0.0, 149.56720016, 0.01999985, 149.56720016, 0.05999955, 104.69704011, -2142.10633883, 0.05, 2, 0, 71015, 22015, 1, 3)
    ops.uniaxialMaterial('LimitState', 31015, 37.39180004, 9.751e-05, 112.17540012, 0.00029252, 373.91800039, 0.00097508, -37.39180004, -9.751e-05, -112.17540012, -0.00029252, -373.91800039, -0.00097508, 0.4, 0.3, 0.003, 0.0, 0.0, 11015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1015, 99999, 'P', 41015, 'Vy', 31015, 'Vz', 21015, 'My', 11015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171015, 71015, 171015, 1015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122015, 122015, 22015, 1015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171016, 17.8, 7.0, 3.525)
    ops.node(122016, 17.8, 7.0, 6.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1016, 171016, 122016, 0.1225, 30830255.90546865, 12845939.96061194, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21016, 117.22354918, 0.00099512, 141.36018389, 0.02461678, 14.13601839, 0.07449782, -117.22354918, -0.00099512, -141.36018389, -0.02461678, -14.13601839, -0.07449782, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11016, 104.90297066, 0.00099512, 126.5027661, 0.02461678, 12.65027661, 0.07449782, -104.90297066, -0.00099512, -126.5027661, -0.02461678, -12.65027661, -0.07449782, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21016, 1016, 0.0, 159.6421481, 0.0199025, 159.6421481, 0.05970749, 111.74950367, -2246.43971703, 0.05, 2, 0, 71016, 22016, 2, 3)
    ops.uniaxialMaterial('LimitState', 41016, 39.91053702, 9.739e-05, 119.73161107, 0.00029217, 399.10537024, 0.00097391, -39.91053702, -9.739e-05, -119.73161107, -0.00029217, -399.10537024, -0.00097391, 0.4, 0.3, 0.003, 0.0, 0.0, 21016, 2)
    ops.limitCurve('ThreePoint', 11016, 1016, 0.0, 159.6421481, 0.0199025, 159.6421481, 0.05970749, 111.74950367, -2246.43971703, 0.05, 2, 0, 71016, 22016, 1, 3)
    ops.uniaxialMaterial('LimitState', 31016, 39.91053702, 9.739e-05, 119.73161107, 0.00029217, 399.10537024, 0.00097391, -39.91053702, -9.739e-05, -119.73161107, -0.00029217, -399.10537024, -0.00097391, 0.4, 0.3, 0.003, 0.0, 0.0, 11016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1016, 99999, 'P', 41016, 'Vy', 31016, 'Vz', 21016, 'My', 11016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171016, 71016, 171016, 1016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122016, 122016, 22016, 1016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171017, 25.2, 7.0, 3.525)
    ops.node(122017, 25.2, 7.0, 6.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1017, 171017, 122017, 0.16, 29709425.23400282, 12378927.18083451, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21017, 144.976333, 0.00104533, 175.13010583, 0.0298884, 17.51301058, 0.07276571, -144.976333, -0.00104533, -175.13010583, -0.0298884, -17.51301058, -0.07276571, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11017, 144.976333, 0.00104533, 175.13010583, 0.0298884, 17.51301058, 0.07276571, -144.976333, -0.00104533, -175.13010583, -0.0298884, -17.51301058, -0.07276571, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21017, 1017, 0.0, 190.60748329, 0.02090661, 190.60748329, 0.06271983, 133.42523831, -2362.3622566, 0.05, 2, 0, 71017, 22017, 2, 3)
    ops.uniaxialMaterial('LimitState', 41017, 47.65187082, 9.239e-05, 142.95561247, 0.00027716, 476.51870824, 0.00092386, -47.65187082, -9.239e-05, -142.95561247, -0.00027716, -476.51870824, -0.00092386, 0.4, 0.3, 0.003, 0.0, 0.0, 21017, 2)
    ops.limitCurve('ThreePoint', 11017, 1017, 0.0, 190.60748329, 0.02090661, 190.60748329, 0.06271983, 133.42523831, -2362.3622566, 0.05, 2, 0, 71017, 22017, 1, 3)
    ops.uniaxialMaterial('LimitState', 31017, 47.65187082, 9.239e-05, 142.95561247, 0.00027716, 476.51870824, 0.00092386, -47.65187082, -9.239e-05, -142.95561247, -0.00027716, -476.51870824, -0.00092386, 0.4, 0.3, 0.003, 0.0, 0.0, 11017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1017, 99999, 'P', 41017, 'Vy', 31017, 'Vz', 21017, 'My', 11017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171017, 71017, 171017, 1017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122017, 122017, 22017, 1017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171018, 32.6, 7.0, 3.525)
    ops.node(122018, 32.6, 7.0, 6.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1018, 171018, 122018, 0.1225, 27667178.2657157, 11527990.94404821, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21018, 131.22188605, 0.00111843, 159.25722947, 0.0364136, 15.92572295, 0.09494467, -131.22188605, -0.00111843, -159.25722947, -0.0364136, -15.92572295, -0.09494467, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11018, 110.71030802, 0.00111843, 134.36338601, 0.0364136, 13.4363386, 0.09494467, -110.71030802, -0.00111843, -134.36338601, -0.0364136, -13.4363386, -0.09494467, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21018, 1018, 0.0, 160.49736242, 0.02236863, 160.49736242, 0.0671059, 112.34815369, -2863.99401077, 0.05, 2, 0, 71018, 22018, 2, 3)
    ops.uniaxialMaterial('LimitState', 41018, 40.1243406, 0.00010911, 120.37302181, 0.00032732, 401.24340605, 0.00109106, -40.1243406, -0.00010911, -120.37302181, -0.00032732, -401.24340605, -0.00109106, 0.4, 0.3, 0.003, 0.0, 0.0, 21018, 2)
    ops.limitCurve('ThreePoint', 11018, 1018, 0.0, 160.49736242, 0.02236863, 160.49736242, 0.0671059, 112.34815369, -2863.99401077, 0.05, 2, 0, 71018, 22018, 1, 3)
    ops.uniaxialMaterial('LimitState', 31018, 40.1243406, 0.00010911, 120.37302181, 0.00032732, 401.24340605, 0.00109106, -40.1243406, -0.00010911, -120.37302181, -0.00032732, -401.24340605, -0.00109106, 0.4, 0.3, 0.003, 0.0, 0.0, 11018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1018, 99999, 'P', 41018, 'Vy', 31018, 'Vz', 21018, 'My', 11018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171018, 71018, 171018, 1018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122018, 122018, 22018, 1018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171019, 0.0, 10.5, 3.5)
    ops.node(122019, 0.0, 10.5, 6.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1019, 171019, 122019, 0.09, 30293828.9700036, 12622428.7375015, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21019, 81.7256449, 0.00119776, 98.79139169, 0.01889298, 9.87913917, 0.06727396, -81.7256449, -0.00119776, -98.79139169, -0.01889298, -9.87913917, -0.06727396, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11019, 67.03483876, 0.00119776, 81.03288779, 0.01889298, 8.10328878, 0.06727396, -67.03483876, -0.00119776, -81.03288779, -0.01889298, -8.10328878, -0.06727396, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21019, 1019, 0.0, 105.89373034, 0.02395512, 105.89373034, 0.07186536, 74.12561124, -1412.83213595, 0.05, 2, 0, 71019, 22019, 2, 3)
    ops.uniaxialMaterial('LimitState', 41019, 26.47343258, 8.949e-05, 79.42029775, 0.00026846, 264.73432584, 0.00089486, -26.47343258, -8.949e-05, -79.42029775, -0.00026846, -264.73432584, -0.00089486, 0.4, 0.3, 0.003, 0.0, 0.0, 21019, 2)
    ops.limitCurve('ThreePoint', 11019, 1019, 0.0, 105.89373034, 0.02395512, 105.89373034, 0.07186536, 74.12561124, -1412.83213595, 0.05, 2, 0, 71019, 22019, 1, 3)
    ops.uniaxialMaterial('LimitState', 31019, 26.47343258, 8.949e-05, 79.42029775, 0.00026846, 264.73432584, 0.00089486, -26.47343258, -8.949e-05, -79.42029775, -0.00026846, -264.73432584, -0.00089486, 0.4, 0.3, 0.003, 0.0, 0.0, 11019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1019, 99999, 'P', 41019, 'Vy', 31019, 'Vz', 21019, 'My', 11019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171019, 71019, 171019, 1019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122019, 122019, 22019, 1019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171020, 7.4, 10.5, 3.5)
    ops.node(122020, 7.4, 10.5, 6.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1020, 171020, 122020, 0.16, 32711214.44554438, 13629672.68564349, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21020, 136.32641178, 0.00090207, 163.68817793, 0.02050589, 16.36881779, 0.05635182, -136.32641178, -0.00090207, -163.68817793, -0.02050589, -16.36881779, -0.05635182, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11020, 136.32641178, 0.00090207, 163.68817793, 0.02050589, 16.36881779, 0.05635182, -136.32641178, -0.00090207, -163.68817793, -0.02050589, -16.36881779, -0.05635182, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21020, 1020, 0.0, 168.7782224, 0.01804146, 168.7782224, 0.05412437, 118.14475568, -1407.78773174, 0.05, 2, 0, 71020, 22020, 2, 3)
    ops.uniaxialMaterial('LimitState', 41020, 42.1945556, 7.43e-05, 126.5836668, 0.0002229, 421.94555599, 0.00074299, -42.1945556, -7.43e-05, -126.5836668, -0.0002229, -421.94555599, -0.00074299, 0.4, 0.3, 0.003, 0.0, 0.0, 21020, 2)
    ops.limitCurve('ThreePoint', 11020, 1020, 0.0, 168.7782224, 0.01804146, 168.7782224, 0.05412437, 118.14475568, -1407.78773174, 0.05, 2, 0, 71020, 22020, 1, 3)
    ops.uniaxialMaterial('LimitState', 31020, 42.1945556, 7.43e-05, 126.5836668, 0.0002229, 421.94555599, 0.00074299, -42.1945556, -7.43e-05, -126.5836668, -0.0002229, -421.94555599, -0.00074299, 0.4, 0.3, 0.003, 0.0, 0.0, 11020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1020, 99999, 'P', 41020, 'Vy', 31020, 'Vz', 21020, 'My', 11020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171020, 71020, 171020, 1020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122020, 122020, 22020, 1020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171021, 14.8, 10.5, 3.5)
    ops.node(122021, 14.8, 10.5, 6.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1021, 171021, 122021, 0.1225, 29351725.96147385, 12229885.81728077, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21021, 100.48153685, 0.00100113, 121.76740011, 0.02293756, 12.17674001, 0.07360008, -100.48153685, -0.00100113, -121.76740011, -0.02293756, -12.17674001, -0.07360008, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11021, 83.2670539, 0.00100113, 100.90622602, 0.02293756, 10.0906226, 0.07360008, -83.2670539, -0.00100113, -100.90622602, -0.02293756, -10.0906226, -0.07360008, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21021, 1021, 0.0, 144.53035415, 0.02002252, 144.53035415, 0.06006755, 101.17124791, -2162.24477305, 0.05, 2, 0, 71021, 22021, 2, 3)
    ops.uniaxialMaterial('LimitState', 41021, 36.13258854, 9.261e-05, 108.39776561, 0.00027784, 361.32588538, 0.00092613, -36.13258854, -9.261e-05, -108.39776561, -0.00027784, -361.32588538, -0.00092613, 0.4, 0.3, 0.003, 0.0, 0.0, 21021, 2)
    ops.limitCurve('ThreePoint', 11021, 1021, 0.0, 144.53035415, 0.02002252, 144.53035415, 0.06006755, 101.17124791, -2162.24477305, 0.05, 2, 0, 71021, 22021, 1, 3)
    ops.uniaxialMaterial('LimitState', 31021, 36.13258854, 9.261e-05, 108.39776561, 0.00027784, 361.32588538, 0.00092613, -36.13258854, -9.261e-05, -108.39776561, -0.00027784, -361.32588538, -0.00092613, 0.4, 0.3, 0.003, 0.0, 0.0, 11021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1021, 99999, 'P', 41021, 'Vy', 31021, 'Vz', 21021, 'My', 11021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171021, 71021, 171021, 1021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122021, 122021, 22021, 1021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171022, 17.8, 10.5, 3.5)
    ops.node(122022, 17.8, 10.5, 6.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1022, 171022, 122022, 0.1225, 31588365.65630184, 13161819.0234591, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21022, 98.99825529, 0.00095441, 119.31663352, 0.02476628, 11.93166335, 0.0775539, -98.99825529, -0.00095441, -119.31663352, -0.02476628, -11.93166335, -0.0775539, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11022, 82.31985987, 0.00095441, 99.21516821, 0.02476628, 9.92151682, 0.0775539, -82.31985987, -0.00095441, -99.21516821, -0.02476628, -9.92151682, -0.0775539, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21022, 1022, 0.0, 157.79276242, 0.01908824, 157.79276242, 0.05726473, 110.4549337, -2380.30752173, 0.05, 2, 0, 71022, 22022, 2, 3)
    ops.uniaxialMaterial('LimitState', 41022, 39.44819061, 9.395e-05, 118.34457182, 0.00028186, 394.48190605, 0.00093952, -39.44819061, -9.395e-05, -118.34457182, -0.00028186, -394.48190605, -0.00093952, 0.4, 0.3, 0.003, 0.0, 0.0, 21022, 2)
    ops.limitCurve('ThreePoint', 11022, 1022, 0.0, 157.79276242, 0.01908824, 157.79276242, 0.05726473, 110.4549337, -2380.30752173, 0.05, 2, 0, 71022, 22022, 1, 3)
    ops.uniaxialMaterial('LimitState', 31022, 39.44819061, 9.395e-05, 118.34457182, 0.00028186, 394.48190605, 0.00093952, -39.44819061, -9.395e-05, -118.34457182, -0.00028186, -394.48190605, -0.00093952, 0.4, 0.3, 0.003, 0.0, 0.0, 11022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1022, 99999, 'P', 41022, 'Vy', 31022, 'Vz', 21022, 'My', 11022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171022, 71022, 171022, 1022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122022, 122022, 22022, 1022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171023, 25.2, 10.5, 3.5)
    ops.node(122023, 25.2, 10.5, 6.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1023, 171023, 122023, 0.16, 28641774.63244529, 11934072.76351887, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21023, 139.55513505, 0.00096775, 169.24203416, 0.02211037, 16.92420342, 0.05518321, -139.55513505, -0.00096775, -169.24203416, -0.02211037, -16.92420342, -0.05518321, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11023, 139.55513505, 0.00096775, 169.24203416, 0.02211037, 16.92420342, 0.05518321, -139.55513505, -0.00096775, -169.24203416, -0.02211037, -16.92420342, -0.05518321, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21023, 1023, 0.0, 152.18777406, 0.01935491, 152.18777406, 0.05806474, 106.53144184, -1507.71346171, 0.05, 2, 0, 71023, 22023, 2, 3)
    ops.uniaxialMaterial('LimitState', 41023, 38.04694352, 7.651e-05, 114.14083055, 0.00022954, 380.46943516, 0.00076514, -38.04694352, -7.651e-05, -114.14083055, -0.00022954, -380.46943516, -0.00076514, 0.4, 0.3, 0.003, 0.0, 0.0, 21023, 2)
    ops.limitCurve('ThreePoint', 11023, 1023, 0.0, 152.18777406, 0.01935491, 152.18777406, 0.05806474, 106.53144184, -1507.71346171, 0.05, 2, 0, 71023, 22023, 1, 3)
    ops.uniaxialMaterial('LimitState', 31023, 38.04694352, 7.651e-05, 114.14083055, 0.00022954, 380.46943516, 0.00076514, -38.04694352, -7.651e-05, -114.14083055, -0.00022954, -380.46943516, -0.00076514, 0.4, 0.3, 0.003, 0.0, 0.0, 11023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1023, 99999, 'P', 41023, 'Vy', 31023, 'Vz', 21023, 'My', 11023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171023, 71023, 171023, 1023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122023, 122023, 22023, 1023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171024, 32.6, 10.5, 3.5)
    ops.node(122024, 32.6, 10.5, 6.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1024, 171024, 122024, 0.09, 29651021.27614199, 12354592.1983925, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21024, 80.60976413, 0.00124627, 97.5826783, 0.0198255, 9.75826783, 0.06755822, -80.60976413, -0.00124627, -97.5826783, -0.0198255, -9.75826783, -0.06755822, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11024, 66.7594933, 0.00124627, 80.81614217, 0.0198255, 8.08161422, 0.06755822, -66.7594933, -0.00124627, -80.81614217, -0.0198255, -8.08161422, -0.06755822, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21024, 1024, 0.0, 105.59039976, 0.02492549, 105.59039976, 0.07477647, 73.91327983, -1470.32516951, 0.05, 2, 0, 71024, 22024, 2, 3)
    ops.uniaxialMaterial('LimitState', 41024, 26.39759994, 9.116e-05, 79.19279982, 0.00027349, 263.97599939, 0.00091164, -26.39759994, -9.116e-05, -79.19279982, -0.00027349, -263.97599939, -0.00091164, 0.4, 0.3, 0.003, 0.0, 0.0, 21024, 2)
    ops.limitCurve('ThreePoint', 11024, 1024, 0.0, 105.59039976, 0.02492549, 105.59039976, 0.07477647, 73.91327983, -1470.32516951, 0.05, 2, 0, 71024, 22024, 1, 3)
    ops.uniaxialMaterial('LimitState', 31024, 26.39759994, 9.116e-05, 79.19279982, 0.00027349, 263.97599939, 0.00091164, -26.39759994, -9.116e-05, -79.19279982, -0.00027349, -263.97599939, -0.00091164, 0.4, 0.3, 0.003, 0.0, 0.0, 11024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1024, 99999, 'P', 41024, 'Vy', 31024, 'Vz', 21024, 'My', 11024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171024, 71024, 171024, 1024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122024, 122024, 22024, 1024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172001, 0.0, 0.0, 6.7)
    ops.node(123001, 0.0, 0.0, 9.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2001, 172001, 123001, 0.0625, 29031822.8264651, 12096592.84436046, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22001, 38.07769387, 0.00139994, 46.19559514, 0.01833558, 4.61955951, 0.07412354, -38.07769387, -0.00139994, -46.19559514, -0.01833558, -4.61955951, -0.07412354, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12001, 34.8528902, 0.00139994, 42.28328561, 0.01833558, 4.22832856, 0.07412354, -34.8528902, -0.00139994, -42.28328561, -0.01833558, -4.22832856, -0.07412354, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22001, 2001, 0.0, 65.73029948, 0.02799883, 65.73029948, 0.08399648, 46.01120964, -1128.06902643, 0.05, 2, 0, 72001, 23001, 2, 3)
    ops.uniaxialMaterial('LimitState', 42001, 16.43257487, 8.346e-05, 49.29772461, 0.00025039, 164.32574871, 0.00083463, -16.43257487, -8.346e-05, -49.29772461, -0.00025039, -164.32574871, -0.00083463, 0.4, 0.3, 0.003, 0.0, 0.0, 22001, 2)
    ops.limitCurve('ThreePoint', 12001, 2001, 0.0, 65.73029948, 0.02799883, 65.73029948, 0.08399648, 46.01120964, -1128.06902643, 0.05, 2, 0, 72001, 23001, 1, 3)
    ops.uniaxialMaterial('LimitState', 32001, 16.43257487, 8.346e-05, 49.29772461, 0.00025039, 164.32574871, 0.00083463, -16.43257487, -8.346e-05, -49.29772461, -0.00025039, -164.32574871, -0.00083463, 0.4, 0.3, 0.003, 0.0, 0.0, 12001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2001, 99999, 'P', 42001, 'Vy', 32001, 'Vz', 22001, 'My', 12001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172001, 72001, 172001, 2001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123001, 123001, 23001, 2001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172002, 7.4, 0.0, 6.7)
    ops.node(123002, 7.4, 0.0, 9.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2002, 172002, 123002, 0.1225, 29072619.35094796, 12113591.39622832, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22002, 105.38923373, 0.00115783, 127.89449389, 0.02535348, 12.78944939, 0.06361415, -105.38923373, -0.00115783, -127.89449389, -0.02535348, -12.78944939, -0.06361415, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12002, 105.38923373, 0.00115783, 127.89449389, 0.02535348, 12.78944939, 0.06361415, -105.38923373, -0.00115783, -127.89449389, -0.02535348, -12.78944939, -0.06361415, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22002, 2002, 0.0, 124.97253844, 0.02315668, 124.97253844, 0.06947004, 87.48077691, -1546.18081914, 0.05, 2, 0, 72002, 23002, 2, 3)
    ops.uniaxialMaterial('LimitState', 42002, 31.24313461, 8.085e-05, 93.72940383, 0.00024255, 312.4313461, 0.00080849, -31.24313461, -8.085e-05, -93.72940383, -0.00024255, -312.4313461, -0.00080849, 0.4, 0.3, 0.003, 0.0, 0.0, 22002, 2)
    ops.limitCurve('ThreePoint', 12002, 2002, 0.0, 124.97253844, 0.02315668, 124.97253844, 0.06947004, 87.48077691, -1546.18081914, 0.05, 2, 0, 72002, 23002, 1, 3)
    ops.uniaxialMaterial('LimitState', 32002, 31.24313461, 8.085e-05, 93.72940383, 0.00024255, 312.4313461, 0.00080849, -31.24313461, -8.085e-05, -93.72940383, -0.00024255, -312.4313461, -0.00080849, 0.4, 0.3, 0.003, 0.0, 0.0, 12002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2002, 99999, 'P', 42002, 'Vy', 32002, 'Vz', 22002, 'My', 12002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172002, 72002, 172002, 2002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123002, 123002, 23002, 2002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172005, 25.2, 0.0, 6.7)
    ops.node(123005, 25.2, 0.0, 9.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2005, 172005, 123005, 0.1225, 30722261.99766035, 12800942.49902515, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22005, 100.69705086, 0.00109538, 121.72909277, 0.0210442, 12.17290928, 0.06041595, -100.69705086, -0.00109538, -121.72909277, -0.0210442, -12.17290928, -0.06041595, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12005, 100.69705086, 0.00109538, 121.72909277, 0.0210442, 12.17290928, 0.06041595, -100.69705086, -0.00109538, -121.72909277, -0.0210442, -12.17290928, -0.06041595, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22005, 2005, 0.0, 120.40822042, 0.02190759, 120.40822042, 0.06572277, 84.28575429, -1158.73418759, 0.05, 2, 0, 72005, 23005, 2, 3)
    ops.uniaxialMaterial('LimitState', 42005, 30.1020551, 7.371e-05, 90.30616531, 0.00022114, 301.02055104, 0.00073714, -30.1020551, -7.371e-05, -90.30616531, -0.00022114, -301.02055104, -0.00073714, 0.4, 0.3, 0.003, 0.0, 0.0, 22005, 2)
    ops.limitCurve('ThreePoint', 12005, 2005, 0.0, 120.40822042, 0.02190759, 120.40822042, 0.06572277, 84.28575429, -1158.73418759, 0.05, 2, 0, 72005, 23005, 1, 3)
    ops.uniaxialMaterial('LimitState', 32005, 30.1020551, 7.371e-05, 90.30616531, 0.00022114, 301.02055104, 0.00073714, -30.1020551, -7.371e-05, -90.30616531, -0.00022114, -301.02055104, -0.00073714, 0.4, 0.3, 0.003, 0.0, 0.0, 12005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2005, 99999, 'P', 42005, 'Vy', 32005, 'Vz', 22005, 'My', 12005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172005, 72005, 172005, 2005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123005, 123005, 23005, 2005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172006, 32.6, 0.0, 6.7)
    ops.node(123006, 32.6, 0.0, 9.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2006, 172006, 123006, 0.0625, 29509492.97083487, 12295622.07118119, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22006, 37.35035311, 0.00140722, 45.26766549, 0.02263465, 4.52676655, 0.07896369, -37.35035311, -0.00140722, -45.26766549, -0.02263465, -4.52676655, -0.07896369, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12006, 34.36358411, 0.00140722, 41.64777843, 0.02263465, 4.16477784, 0.07896369, -34.36358411, -0.00140722, -41.64777843, -0.02263465, -4.16477784, -0.07896369, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22006, 2006, 0.0, 80.87806534, 0.02814443, 80.87806534, 0.0844333, 56.61464574, -1490.13228137, 0.05, 2, 0, 72006, 23006, 2, 3)
    ops.uniaxialMaterial('LimitState', 42006, 20.21951634, 0.00010103, 60.65854901, 0.0003031, 202.19516336, 0.00101035, -20.21951634, -0.00010103, -60.65854901, -0.0003031, -202.19516336, -0.00101035, 0.4, 0.3, 0.003, 0.0, 0.0, 22006, 2)
    ops.limitCurve('ThreePoint', 12006, 2006, 0.0, 80.87806534, 0.02814443, 80.87806534, 0.0844333, 56.61464574, -1490.13228137, 0.05, 2, 0, 72006, 23006, 1, 3)
    ops.uniaxialMaterial('LimitState', 32006, 20.21951634, 0.00010103, 60.65854901, 0.0003031, 202.19516336, 0.00101035, -20.21951634, -0.00010103, -60.65854901, -0.0003031, -202.19516336, -0.00101035, 0.4, 0.3, 0.003, 0.0, 0.0, 12006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2006, 99999, 'P', 42006, 'Vy', 32006, 'Vz', 22006, 'My', 12006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172006, 72006, 172006, 2006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123006, 123006, 23006, 2006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172007, 0.0, 3.5, 6.725)
    ops.node(123007, 0.0, 3.5, 9.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2007, 172007, 123007, 0.0625, 32469025.9492538, 13528760.81218908, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22007, 50.18117858, 0.00147305, 60.20228446, 0.0190148, 6.02022845, 0.06675297, -50.18117858, -0.00147305, -60.20228446, -0.0190148, -6.02022845, -0.06675297, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12007, 50.18117858, 0.00147305, 60.20228446, 0.0190148, 6.02022845, 0.06675297, -50.18117858, -0.00147305, -60.20228446, -0.0190148, -6.02022845, -0.06675297, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22007, 2007, 0.0, 65.02103779, 0.02946093, 65.02103779, 0.08838278, 45.51472645, -925.2511834, 0.05, 2, 0, 72007, 23007, 2, 3)
    ops.uniaxialMaterial('LimitState', 42007, 16.25525945, 7.382e-05, 48.76577834, 0.00022147, 162.55259448, 0.00073822, -16.25525945, -7.382e-05, -48.76577834, -0.00022147, -162.55259448, -0.00073822, 0.4, 0.3, 0.003, 0.0, 0.0, 22007, 2)
    ops.limitCurve('ThreePoint', 12007, 2007, 0.0, 65.02103779, 0.02946093, 65.02103779, 0.08838278, 45.51472645, -925.2511834, 0.05, 2, 0, 72007, 23007, 1, 3)
    ops.uniaxialMaterial('LimitState', 32007, 16.25525945, 7.382e-05, 48.76577834, 0.00022147, 162.55259448, 0.00073822, -16.25525945, -7.382e-05, -48.76577834, -0.00022147, -162.55259448, -0.00073822, 0.4, 0.3, 0.003, 0.0, 0.0, 12007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2007, 99999, 'P', 42007, 'Vy', 32007, 'Vz', 22007, 'My', 12007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172007, 72007, 172007, 2007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123007, 123007, 23007, 2007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172008, 7.4, 3.5, 6.725)
    ops.node(123008, 7.4, 3.5, 9.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2008, 172008, 123008, 0.1225, 29547896.73788899, 12311623.64078708, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22008, 116.61961425, 0.00114753, 141.13244465, 0.02681911, 14.11324447, 0.06858881, -116.61961425, -0.00114753, -141.13244465, -0.02681911, -14.11324447, -0.06858881, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12008, 116.61961425, 0.00114753, 141.13244465, 0.02681911, 14.11324447, 0.06858881, -116.61961425, -0.00114753, -141.13244465, -0.02681911, -14.11324447, -0.06858881, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22008, 2008, 0.0, 137.14501491, 0.02295063, 137.14501491, 0.06885188, 96.00151044, -1691.37014306, 0.05, 2, 0, 72008, 23008, 2, 3)
    ops.uniaxialMaterial('LimitState', 42008, 34.28625373, 8.73e-05, 102.85876118, 0.00026189, 342.86253728, 0.00087297, -34.28625373, -8.73e-05, -102.85876118, -0.00026189, -342.86253728, -0.00087297, 0.4, 0.3, 0.003, 0.0, 0.0, 22008, 2)
    ops.limitCurve('ThreePoint', 12008, 2008, 0.0, 137.14501491, 0.02295063, 137.14501491, 0.06885188, 96.00151044, -1691.37014306, 0.05, 2, 0, 72008, 23008, 1, 3)
    ops.uniaxialMaterial('LimitState', 32008, 34.28625373, 8.73e-05, 102.85876118, 0.00026189, 342.86253728, 0.00087297, -34.28625373, -8.73e-05, -102.85876118, -0.00026189, -342.86253728, -0.00087297, 0.4, 0.3, 0.003, 0.0, 0.0, 12008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2008, 99999, 'P', 42008, 'Vy', 32008, 'Vz', 22008, 'My', 12008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172008, 72008, 172008, 2008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123008, 123008, 23008, 2008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172009, 14.8, 3.5, 6.725)
    ops.node(123009, 14.8, 3.5, 9.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2009, 172009, 123009, 0.0625, 27001247.05718, 11250519.60715833, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22009, 45.66235757, 0.00146464, 55.18034641, 0.01968989, 5.51803464, 0.06231587, -45.66235757, -0.00146464, -55.18034641, -0.01968989, -5.51803464, -0.06231587, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12009, 41.96537574, 0.00146464, 50.7127554, 0.01968989, 5.07127554, 0.06231587, -41.96537574, -0.00146464, -50.7127554, -0.01968989, -5.07127554, -0.06231587, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22009, 2009, 0.0, 81.0892557, 0.02929276, 81.0892557, 0.08787829, 56.76247899, -1191.66300644, 0.05, 2, 0, 72009, 23009, 2, 3)
    ops.uniaxialMaterial('LimitState', 42009, 20.27231392, 0.00011071, 60.81694177, 0.00033213, 202.72313924, 0.00110709, -20.27231392, -0.00011071, -60.81694177, -0.00033213, -202.72313924, -0.00110709, 0.4, 0.3, 0.003, 0.0, 0.0, 22009, 2)
    ops.limitCurve('ThreePoint', 12009, 2009, 0.0, 81.0892557, 0.02929276, 81.0892557, 0.08787829, 56.76247899, -1191.66300644, 0.05, 2, 0, 72009, 23009, 1, 3)
    ops.uniaxialMaterial('LimitState', 32009, 20.27231392, 0.00011071, 60.81694177, 0.00033213, 202.72313924, 0.00110709, -20.27231392, -0.00011071, -60.81694177, -0.00033213, -202.72313924, -0.00110709, 0.4, 0.3, 0.003, 0.0, 0.0, 12009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2009, 99999, 'P', 42009, 'Vy', 32009, 'Vz', 22009, 'My', 12009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172009, 72009, 172009, 2009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123009, 123009, 23009, 2009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172010, 17.8, 3.5, 6.725)
    ops.node(123010, 17.8, 3.5, 9.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2010, 172010, 123010, 0.0625, 28756295.38523661, 11981789.74384859, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22010, 46.1478517, 0.00160013, 55.68383781, 0.01731664, 5.56838378, 0.06374608, -46.1478517, -0.00160013, -55.68383781, -0.01731664, -5.56838378, -0.06374608, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12010, 42.93360725, 0.00160013, 51.80540231, 0.01731664, 5.18054023, 0.06374608, -42.93360725, -0.00160013, -51.80540231, -0.01731664, -5.18054023, -0.06374608, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22010, 2010, 0.0, 76.49542273, 0.03200258, 76.49542273, 0.09600774, 53.54679591, -1018.89228425, 0.05, 2, 0, 72010, 23010, 2, 3)
    ops.uniaxialMaterial('LimitState', 42010, 19.12385568, 9.806e-05, 57.37156705, 0.00029419, 191.23855683, 0.00098063, -19.12385568, -9.806e-05, -57.37156705, -0.00029419, -191.23855683, -0.00098063, 0.4, 0.3, 0.003, 0.0, 0.0, 22010, 2)
    ops.limitCurve('ThreePoint', 12010, 2010, 0.0, 76.49542273, 0.03200258, 76.49542273, 0.09600774, 53.54679591, -1018.89228425, 0.05, 2, 0, 72010, 23010, 1, 3)
    ops.uniaxialMaterial('LimitState', 32010, 19.12385568, 9.806e-05, 57.37156705, 0.00029419, 191.23855683, 0.00098063, -19.12385568, -9.806e-05, -57.37156705, -0.00029419, -191.23855683, -0.00098063, 0.4, 0.3, 0.003, 0.0, 0.0, 12010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2010, 99999, 'P', 42010, 'Vy', 32010, 'Vz', 22010, 'My', 12010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172010, 72010, 172010, 2010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123010, 123010, 23010, 2010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172011, 25.2, 3.5, 6.725)
    ops.node(123011, 25.2, 3.5, 9.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2011, 172011, 123011, 0.1225, 31241751.10258349, 13017396.29274312, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22011, 110.80462799, 0.00114274, 133.56856117, 0.02480781, 13.35685612, 0.06811521, -110.80462799, -0.00114274, -133.56856117, -0.02480781, -13.35685612, -0.06811521, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12011, 110.80462799, 0.00114274, 133.56856117, 0.02480781, 13.35685612, 0.06811521, -110.80462799, -0.00114274, -133.56856117, -0.02480781, -13.35685612, -0.06811521, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22011, 2011, 0.0, 137.09854721, 0.02285484, 137.09854721, 0.06856453, 95.96898304, -1471.62493385, 0.05, 2, 0, 72011, 23011, 2, 3)
    ops.uniaxialMaterial('LimitState', 42011, 34.2746368, 8.254e-05, 102.8239104, 0.00024761, 342.74636801, 0.00082536, -34.2746368, -8.254e-05, -102.8239104, -0.00024761, -342.74636801, -0.00082536, 0.4, 0.3, 0.003, 0.0, 0.0, 22011, 2)
    ops.limitCurve('ThreePoint', 12011, 2011, 0.0, 137.09854721, 0.02285484, 137.09854721, 0.06856453, 95.96898304, -1471.62493385, 0.05, 2, 0, 72011, 23011, 1, 3)
    ops.uniaxialMaterial('LimitState', 32011, 34.2746368, 8.254e-05, 102.8239104, 0.00024761, 342.74636801, 0.00082536, -34.2746368, -8.254e-05, -102.8239104, -0.00024761, -342.74636801, -0.00082536, 0.4, 0.3, 0.003, 0.0, 0.0, 12011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2011, 99999, 'P', 42011, 'Vy', 32011, 'Vz', 22011, 'My', 12011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172011, 72011, 172011, 2011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123011, 123011, 23011, 2011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172012, 32.6, 3.5, 6.725)
    ops.node(123012, 32.6, 3.5, 9.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2012, 172012, 123012, 0.0625, 28937022.7861094, 12057092.82754558, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22012, 48.60275001, 0.00151694, 58.77325328, 0.01874013, 5.87732533, 0.06230671, -48.60275001, -0.00151694, -58.77325328, -0.01874013, -5.87732533, -0.06230671, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12012, 48.60275001, 0.00151694, 58.77325328, 0.01874013, 5.87732533, 0.06230671, -48.60275001, -0.00151694, -58.77325328, -0.01874013, -5.87732533, -0.06230671, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22012, 2012, 0.0, 52.00787, 0.03033879, 52.00787, 0.09101637, 36.405509, -935.31755424, 0.05, 2, 0, 72012, 23012, 2, 3)
    ops.uniaxialMaterial('LimitState', 42012, 13.0019675, 6.625e-05, 39.0059025, 0.00019876, 130.01967499, 0.00066255, -13.0019675, -6.625e-05, -39.0059025, -0.00019876, -130.01967499, -0.00066255, 0.4, 0.3, 0.003, 0.0, 0.0, 22012, 2)
    ops.limitCurve('ThreePoint', 12012, 2012, 0.0, 52.00787, 0.03033879, 52.00787, 0.09101637, 36.405509, -935.31755424, 0.05, 2, 0, 72012, 23012, 1, 3)
    ops.uniaxialMaterial('LimitState', 32012, 13.0019675, 6.625e-05, 39.0059025, 0.00019876, 130.01967499, 0.00066255, -13.0019675, -6.625e-05, -39.0059025, -0.00019876, -130.01967499, -0.00066255, 0.4, 0.3, 0.003, 0.0, 0.0, 12012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2012, 99999, 'P', 42012, 'Vy', 32012, 'Vz', 22012, 'My', 12012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172012, 72012, 172012, 2012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123012, 123012, 23012, 2012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172013, 0.0, 7.0, 6.725)
    ops.node(123013, 0.0, 7.0, 9.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2013, 172013, 123013, 0.0625, 26152220.18426416, 10896758.41011007, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22013, 46.52485342, 0.00166334, 56.42235707, 0.02136495, 5.64223571, 0.06019619, -46.52485342, -0.00166334, -56.42235707, -0.02136495, -5.64223571, -0.06019619, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12013, 46.52485342, 0.00166334, 56.42235707, 0.02136495, 5.64223571, 0.06019619, -46.52485342, -0.00166334, -56.42235707, -0.02136495, -5.64223571, -0.06019619, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22013, 2013, 0.0, 64.9821678, 0.03326684, 64.9821678, 0.09980051, 45.48751746, -1001.9382713, 0.05, 2, 0, 72013, 23013, 2, 3)
    ops.uniaxialMaterial('LimitState', 42013, 16.24554195, 9.16e-05, 48.73662585, 0.0002748, 162.4554195, 0.00091598, -16.24554195, -9.16e-05, -48.73662585, -0.0002748, -162.4554195, -0.00091598, 0.4, 0.3, 0.003, 0.0, 0.0, 22013, 2)
    ops.limitCurve('ThreePoint', 12013, 2013, 0.0, 64.9821678, 0.03326684, 64.9821678, 0.09980051, 45.48751746, -1001.9382713, 0.05, 2, 0, 72013, 23013, 1, 3)
    ops.uniaxialMaterial('LimitState', 32013, 16.24554195, 9.16e-05, 48.73662585, 0.0002748, 162.4554195, 0.00091598, -16.24554195, -9.16e-05, -48.73662585, -0.0002748, -162.4554195, -0.00091598, 0.4, 0.3, 0.003, 0.0, 0.0, 12013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2013, 99999, 'P', 42013, 'Vy', 32013, 'Vz', 22013, 'My', 12013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172013, 72013, 172013, 2013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123013, 123013, 23013, 2013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172014, 7.4, 7.0, 6.725)
    ops.node(123014, 7.4, 7.0, 9.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2014, 172014, 123014, 0.1225, 28172494.4326057, 11738539.34691904, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22014, 109.66288202, 0.00116129, 133.04190498, 0.02756851, 13.3041905, 0.06783247, -109.66288202, -0.00116129, -133.04190498, -0.02756851, -13.3041905, -0.06783247, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12014, 109.66288202, 0.00116129, 133.04190498, 0.02756851, 13.3041905, 0.06783247, -109.66288202, -0.00116129, -133.04190498, -0.02756851, -13.3041905, -0.06783247, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22014, 2014, 0.0, 134.33151345, 0.0232258, 134.33151345, 0.06967739, 94.03205942, -1769.86811924, 0.05, 2, 0, 72014, 23014, 2, 3)
    ops.uniaxialMaterial('LimitState', 42014, 33.58287836, 8.968e-05, 100.74863509, 0.00026904, 335.82878364, 0.00089681, -33.58287836, -8.968e-05, -100.74863509, -0.00026904, -335.82878364, -0.00089681, 0.4, 0.3, 0.003, 0.0, 0.0, 22014, 2)
    ops.limitCurve('ThreePoint', 12014, 2014, 0.0, 134.33151345, 0.0232258, 134.33151345, 0.06967739, 94.03205942, -1769.86811924, 0.05, 2, 0, 72014, 23014, 1, 3)
    ops.uniaxialMaterial('LimitState', 32014, 33.58287836, 8.968e-05, 100.74863509, 0.00026904, 335.82878364, 0.00089681, -33.58287836, -8.968e-05, -100.74863509, -0.00026904, -335.82878364, -0.00089681, 0.4, 0.3, 0.003, 0.0, 0.0, 12014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2014, 99999, 'P', 42014, 'Vy', 32014, 'Vz', 22014, 'My', 12014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172014, 72014, 172014, 2014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123014, 123014, 23014, 2014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172015, 14.8, 7.0, 6.725)
    ops.node(123015, 14.8, 7.0, 9.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2015, 172015, 123015, 0.0625, 26829606.16751771, 11179002.56979905, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22015, 45.76446755, 0.00152267, 55.41796927, 0.01749722, 5.54179693, 0.06229983, -45.76446755, -0.00152267, -55.41796927, -0.01749722, -5.54179693, -0.06229983, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12015, 41.82849563, 0.00152267, 50.65174817, 0.01749722, 5.06517482, 0.06229983, -41.82849563, -0.00152267, -50.65174817, -0.01749722, -5.06517482, -0.06229983, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22015, 2015, 0.0, 72.48519923, 0.03045341, 72.48519923, 0.09136022, 50.73963946, -1064.42623514, 0.05, 2, 0, 72015, 23015, 2, 3)
    ops.uniaxialMaterial('LimitState', 42015, 18.12129981, 9.959e-05, 54.36389942, 0.00029878, 181.21299807, 0.00099595, -18.12129981, -9.959e-05, -54.36389942, -0.00029878, -181.21299807, -0.00099595, 0.4, 0.3, 0.003, 0.0, 0.0, 22015, 2)
    ops.limitCurve('ThreePoint', 12015, 2015, 0.0, 72.48519923, 0.03045341, 72.48519923, 0.09136022, 50.73963946, -1064.42623514, 0.05, 2, 0, 72015, 23015, 1, 3)
    ops.uniaxialMaterial('LimitState', 32015, 18.12129981, 9.959e-05, 54.36389942, 0.00029878, 181.21299807, 0.00099595, -18.12129981, -9.959e-05, -54.36389942, -0.00029878, -181.21299807, -0.00099595, 0.4, 0.3, 0.003, 0.0, 0.0, 12015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2015, 99999, 'P', 42015, 'Vy', 32015, 'Vz', 22015, 'My', 12015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172015, 72015, 172015, 2015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123015, 123015, 23015, 2015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172016, 17.8, 7.0, 6.725)
    ops.node(123016, 17.8, 7.0, 9.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2016, 172016, 123016, 0.0625, 34109029.68749252, 14212095.70312188, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22016, 44.35563008, 0.00139309, 52.91308442, 0.02032019, 5.29130844, 0.07621364, -44.35563008, -0.00139309, -52.91308442, -0.02032019, -5.29130844, -0.07621364, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12016, 41.1062995, 0.00139309, 49.03686616, 0.02032019, 4.90368662, 0.07621364, -41.1062995, -0.00139309, -49.03686616, -0.02032019, -4.90368662, -0.07621364, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22016, 2016, 0.0, 95.543141, 0.02786182, 95.543141, 0.08358547, 66.8801987, -1293.98400144, 0.05, 2, 0, 72016, 23016, 2, 3)
    ops.uniaxialMaterial('LimitState', 42016, 23.88578525, 0.00010326, 71.65735575, 0.00030978, 238.8578525, 0.0010326, -23.88578525, -0.00010326, -71.65735575, -0.00030978, -238.8578525, -0.0010326, 0.4, 0.3, 0.003, 0.0, 0.0, 22016, 2)
    ops.limitCurve('ThreePoint', 12016, 2016, 0.0, 95.543141, 0.02786182, 95.543141, 0.08358547, 66.8801987, -1293.98400144, 0.05, 2, 0, 72016, 23016, 1, 3)
    ops.uniaxialMaterial('LimitState', 32016, 23.88578525, 0.00010326, 71.65735575, 0.00030978, 238.8578525, 0.0010326, -23.88578525, -0.00010326, -71.65735575, -0.00030978, -238.8578525, -0.0010326, 0.4, 0.3, 0.003, 0.0, 0.0, 12016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2016, 99999, 'P', 42016, 'Vy', 32016, 'Vz', 22016, 'My', 12016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172016, 72016, 172016, 2016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123016, 123016, 23016, 2016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172017, 25.2, 7.0, 6.725)
    ops.node(123017, 25.2, 7.0, 9.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2017, 172017, 123017, 0.1225, 32875036.15571297, 13697931.73154707, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22017, 112.99467064, 0.00107494, 135.57085746, 0.02344992, 13.55708575, 0.06797184, -112.99467064, -0.00107494, -135.57085746, -0.02344992, -13.55708575, -0.06797184, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12017, 112.99467064, 0.00107494, 135.57085746, 0.02344992, 13.55708575, 0.06797184, -112.99467064, -0.00107494, -135.57085746, -0.02344992, -13.55708575, -0.06797184, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22017, 2017, 0.0, 140.04525814, 0.02149881, 140.04525814, 0.06449644, 98.0316807, -1362.00955677, 0.05, 2, 0, 72017, 23017, 2, 3)
    ops.uniaxialMaterial('LimitState', 42017, 35.01131454, 8.012e-05, 105.03394361, 0.00024036, 350.11314536, 0.00080121, -35.01131454, -8.012e-05, -105.03394361, -0.00024036, -350.11314536, -0.00080121, 0.4, 0.3, 0.003, 0.0, 0.0, 22017, 2)
    ops.limitCurve('ThreePoint', 12017, 2017, 0.0, 140.04525814, 0.02149881, 140.04525814, 0.06449644, 98.0316807, -1362.00955677, 0.05, 2, 0, 72017, 23017, 1, 3)
    ops.uniaxialMaterial('LimitState', 32017, 35.01131454, 8.012e-05, 105.03394361, 0.00024036, 350.11314536, 0.00080121, -35.01131454, -8.012e-05, -105.03394361, -0.00024036, -350.11314536, -0.00080121, 0.4, 0.3, 0.003, 0.0, 0.0, 12017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2017, 99999, 'P', 42017, 'Vy', 32017, 'Vz', 22017, 'My', 12017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172017, 72017, 172017, 2017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123017, 123017, 23017, 2017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172018, 32.6, 7.0, 6.725)
    ops.node(123018, 32.6, 7.0, 9.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2018, 172018, 123018, 0.0625, 30873640.36597519, 12864016.81915633, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22018, 46.9853249, 0.0014182, 56.60194861, 0.01821601, 5.66019486, 0.06427846, -46.9853249, -0.0014182, -56.60194861, -0.01821601, -5.66019486, -0.06427846, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12018, 46.9853249, 0.0014182, 56.60194861, 0.01821601, 5.66019486, 0.06427846, -46.9853249, -0.0014182, -56.60194861, -0.01821601, -5.66019486, -0.06427846, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22018, 2018, 0.0, 50.34774963, 0.02836407, 50.34774963, 0.08509221, 35.24342474, -775.06590958, 0.05, 2, 0, 72018, 23018, 2, 3)
    ops.uniaxialMaterial('LimitState', 42018, 12.58693741, 6.012e-05, 37.76081222, 0.00018035, 125.86937407, 0.00060117, -12.58693741, -6.012e-05, -37.76081222, -0.00018035, -125.86937407, -0.00060117, 0.4, 0.3, 0.003, 0.0, 0.0, 22018, 2)
    ops.limitCurve('ThreePoint', 12018, 2018, 0.0, 50.34774963, 0.02836407, 50.34774963, 0.08509221, 35.24342474, -775.06590958, 0.05, 2, 0, 72018, 23018, 1, 3)
    ops.uniaxialMaterial('LimitState', 32018, 12.58693741, 6.012e-05, 37.76081222, 0.00018035, 125.86937407, 0.00060117, -12.58693741, -6.012e-05, -37.76081222, -0.00018035, -125.86937407, -0.00060117, 0.4, 0.3, 0.003, 0.0, 0.0, 12018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2018, 99999, 'P', 42018, 'Vy', 32018, 'Vz', 22018, 'My', 12018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172018, 72018, 172018, 2018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123018, 123018, 23018, 2018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172019, 0.0, 10.5, 6.7)
    ops.node(123019, 0.0, 10.5, 9.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2019, 172019, 123019, 0.0625, 29809683.56008601, 12420701.48336917, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22019, 38.99194999, 0.00131945, 47.22562704, 0.02042866, 4.7225627, 0.07708126, -38.99194999, -0.00131945, -47.22562704, -0.02042866, -4.7225627, -0.07708126, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12019, 35.38475097, 0.00131945, 42.85671921, 0.02042866, 4.28567192, 0.07708126, -35.38475097, -0.00131945, -42.85671921, -0.02042866, -4.28567192, -0.07708126, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22019, 2019, 0.0, 78.56093868, 0.02638907, 78.56093868, 0.07916721, 54.99265708, -1343.97763885, 0.05, 2, 0, 72019, 23019, 2, 3)
    ops.uniaxialMaterial('LimitState', 42019, 19.64023467, 9.715e-05, 58.92070401, 0.00029146, 196.4023467, 0.00097152, -19.64023467, -9.715e-05, -58.92070401, -0.00029146, -196.4023467, -0.00097152, 0.4, 0.3, 0.003, 0.0, 0.0, 22019, 2)
    ops.limitCurve('ThreePoint', 12019, 2019, 0.0, 78.56093868, 0.02638907, 78.56093868, 0.07916721, 54.99265708, -1343.97763885, 0.05, 2, 0, 72019, 23019, 1, 3)
    ops.uniaxialMaterial('LimitState', 32019, 19.64023467, 9.715e-05, 58.92070401, 0.00029146, 196.4023467, 0.00097152, -19.64023467, -9.715e-05, -58.92070401, -0.00029146, -196.4023467, -0.00097152, 0.4, 0.3, 0.003, 0.0, 0.0, 12019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2019, 99999, 'P', 42019, 'Vy', 32019, 'Vz', 22019, 'My', 12019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172019, 72019, 172019, 2019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123019, 123019, 23019, 2019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172020, 7.4, 10.5, 6.7)
    ops.node(123020, 7.4, 10.5, 9.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2020, 172020, 123020, 0.1225, 30651788.08610618, 12771578.36921091, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22020, 107.90854, 0.00115423, 130.47059988, 0.02158064, 13.04705999, 0.06090952, -107.90854, -0.00115423, -130.47059988, -0.02158064, -13.04705999, -0.06090952, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12020, 107.90854, 0.00115423, 130.47059988, 0.02158064, 13.04705999, 0.06090952, -107.90854, -0.00115423, -130.47059988, -0.02158064, -13.04705999, -0.06090952, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22020, 2020, 0.0, 121.54251514, 0.02308459, 121.54251514, 0.06925377, 85.0797606, -1206.536743, 0.05, 2, 0, 72020, 23020, 2, 3)
    ops.uniaxialMaterial('LimitState', 42020, 30.38562879, 7.458e-05, 91.15688636, 0.00022374, 303.85628786, 0.00074579, -30.38562879, -7.458e-05, -91.15688636, -0.00022374, -303.85628786, -0.00074579, 0.4, 0.3, 0.003, 0.0, 0.0, 22020, 2)
    ops.limitCurve('ThreePoint', 12020, 2020, 0.0, 121.54251514, 0.02308459, 121.54251514, 0.06925377, 85.0797606, -1206.536743, 0.05, 2, 0, 72020, 23020, 1, 3)
    ops.uniaxialMaterial('LimitState', 32020, 30.38562879, 7.458e-05, 91.15688636, 0.00022374, 303.85628786, 0.00074579, -30.38562879, -7.458e-05, -91.15688636, -0.00022374, -303.85628786, -0.00074579, 0.4, 0.3, 0.003, 0.0, 0.0, 12020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2020, 99999, 'P', 42020, 'Vy', 32020, 'Vz', 22020, 'My', 12020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172020, 72020, 172020, 2020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123020, 123020, 23020, 2020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172021, 14.8, 10.5, 6.7)
    ops.node(123021, 14.8, 10.5, 9.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2021, 172021, 123021, 0.0625, 27713405.78159033, 11547252.40899597, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22021, 31.38928773, 0.00139648, 38.09628714, 0.02029244, 3.80962871, 0.07128163, -31.38928773, -0.00139648, -38.09628714, -0.02029244, -3.80962871, -0.07128163, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12021, 31.38928773, 0.00139648, 38.09628714, 0.02029244, 3.80962871, 0.07128163, -31.38928773, -0.00139648, -38.09628714, -0.02029244, -3.80962871, -0.07128163, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22021, 2021, 0.0, 76.96339237, 0.0279296, 76.96339237, 0.08378879, 53.87437466, -1248.99784805, 0.05, 2, 0, 72021, 23021, 2, 3)
    ops.uniaxialMaterial('LimitState', 42021, 19.24084809, 0.00010238, 57.72254428, 0.00030713, 192.40848092, 0.00102376, -19.24084809, -0.00010238, -57.72254428, -0.00030713, -192.40848092, -0.00102376, 0.4, 0.3, 0.003, 0.0, 0.0, 22021, 2)
    ops.limitCurve('ThreePoint', 12021, 2021, 0.0, 76.96339237, 0.0279296, 76.96339237, 0.08378879, 53.87437466, -1248.99784805, 0.05, 2, 0, 72021, 23021, 1, 3)
    ops.uniaxialMaterial('LimitState', 32021, 19.24084809, 0.00010238, 57.72254428, 0.00030713, 192.40848092, 0.00102376, -19.24084809, -0.00010238, -57.72254428, -0.00030713, -192.40848092, -0.00102376, 0.4, 0.3, 0.003, 0.0, 0.0, 12021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2021, 99999, 'P', 42021, 'Vy', 32021, 'Vz', 22021, 'My', 12021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172021, 72021, 172021, 2021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123021, 123021, 23021, 2021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172022, 17.8, 10.5, 6.7)
    ops.node(123022, 17.8, 10.5, 9.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2022, 172022, 123022, 0.0625, 28408137.80361635, 11836724.08484015, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22022, 30.88617637, 0.00138616, 37.44715384, 0.01884586, 3.74471538, 0.07094667, -30.88617637, -0.00138616, -37.44715384, -0.01884586, -3.74471538, -0.07094667, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12022, 30.88617637, 0.00138616, 37.44715384, 0.01884586, 3.74471538, 0.07094667, -30.88617637, -0.00138616, -37.44715384, -0.01884586, -3.74471538, -0.07094667, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22022, 2022, 0.0, 78.06507114, 0.02772316, 78.06507114, 0.08316947, 54.6455498, -1241.99121673, 0.05, 2, 0, 72022, 23022, 2, 3)
    ops.uniaxialMaterial('LimitState', 42022, 19.51626779, 0.0001013, 58.54880336, 0.0003039, 195.16267786, 0.00101302, -19.51626779, -0.0001013, -58.54880336, -0.0003039, -195.16267786, -0.00101302, 0.4, 0.3, 0.003, 0.0, 0.0, 22022, 2)
    ops.limitCurve('ThreePoint', 12022, 2022, 0.0, 78.06507114, 0.02772316, 78.06507114, 0.08316947, 54.6455498, -1241.99121673, 0.05, 2, 0, 72022, 23022, 1, 3)
    ops.uniaxialMaterial('LimitState', 32022, 19.51626779, 0.0001013, 58.54880336, 0.0003039, 195.16267786, 0.00101302, -19.51626779, -0.0001013, -58.54880336, -0.0003039, -195.16267786, -0.00101302, 0.4, 0.3, 0.003, 0.0, 0.0, 12022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2022, 99999, 'P', 42022, 'Vy', 32022, 'Vz', 22022, 'My', 12022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172022, 72022, 172022, 2022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123022, 123022, 23022, 2022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172023, 25.2, 10.5, 6.7)
    ops.node(123023, 25.2, 10.5, 9.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2023, 172023, 123023, 0.1225, 29458187.76720933, 12274244.90300389, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22023, 103.36584937, 0.00102241, 125.33536743, 0.02566753, 12.53353674, 0.06420927, -103.36584937, -0.00102241, -125.33536743, -0.02566753, -12.53353674, -0.06420927, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12023, 103.36584937, 0.00102241, 125.33536743, 0.02566753, 12.53353674, 0.06420927, -103.36584937, -0.00102241, -125.33536743, -0.02566753, -12.53353674, -0.06420927, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22023, 2023, 0.0, 129.37420014, 0.02044823, 129.37420014, 0.06134468, 90.5619401, -1666.03330185, 0.05, 2, 0, 72023, 23023, 2, 3)
    ops.uniaxialMaterial('LimitState', 42023, 32.34355004, 8.26e-05, 97.03065011, 0.0002478, 323.43550036, 0.00082602, -32.34355004, -8.26e-05, -97.03065011, -0.0002478, -323.43550036, -0.00082602, 0.4, 0.3, 0.003, 0.0, 0.0, 22023, 2)
    ops.limitCurve('ThreePoint', 12023, 2023, 0.0, 129.37420014, 0.02044823, 129.37420014, 0.06134468, 90.5619401, -1666.03330185, 0.05, 2, 0, 72023, 23023, 1, 3)
    ops.uniaxialMaterial('LimitState', 32023, 32.34355004, 8.26e-05, 97.03065011, 0.0002478, 323.43550036, 0.00082602, -32.34355004, -8.26e-05, -97.03065011, -0.0002478, -323.43550036, -0.00082602, 0.4, 0.3, 0.003, 0.0, 0.0, 12023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2023, 99999, 'P', 42023, 'Vy', 32023, 'Vz', 22023, 'My', 12023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172023, 72023, 172023, 2023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123023, 123023, 23023, 2023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172024, 32.6, 10.5, 6.7)
    ops.node(123024, 32.6, 10.5, 9.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2024, 172024, 123024, 0.0625, 28711573.28921484, 11963155.53717285, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22024, 38.40678886, 0.00136404, 46.62433361, 0.02224378, 4.66243336, 0.07764997, -38.40678886, -0.00136404, -46.62433361, -0.02224378, -4.66243336, -0.07764997, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12024, 34.96961657, 0.00136404, 42.45174141, 0.02224378, 4.24517414, 0.07764997, -34.96961657, -0.00136404, -42.45174141, -0.02224378, -4.24517414, -0.07764997, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22024, 2024, 0.0, 80.40167557, 0.02728079, 80.40167557, 0.08184237, 56.2811729, -1542.46633754, 0.05, 2, 0, 72024, 23024, 2, 3)
    ops.uniaxialMaterial('LimitState', 42024, 20.10041889, 0.00010323, 60.30125667, 0.00030969, 201.00418891, 0.00103231, -20.10041889, -0.00010323, -60.30125667, -0.00030969, -201.00418891, -0.00103231, 0.4, 0.3, 0.003, 0.0, 0.0, 22024, 2)
    ops.limitCurve('ThreePoint', 12024, 2024, 0.0, 80.40167557, 0.02728079, 80.40167557, 0.08184237, 56.2811729, -1542.46633754, 0.05, 2, 0, 72024, 23024, 1, 3)
    ops.uniaxialMaterial('LimitState', 32024, 20.10041889, 0.00010323, 60.30125667, 0.00030969, 201.00418891, 0.00103231, -20.10041889, -0.00010323, -60.30125667, -0.00030969, -201.00418891, -0.00103231, 0.4, 0.3, 0.003, 0.0, 0.0, 12024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2024, 99999, 'P', 42024, 'Vy', 32024, 'Vz', 22024, 'My', 12024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172024, 72024, 172024, 2024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123024, 123024, 23024, 2024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173001, 0.0, 0.0, 9.9)
    ops.node(124001, 0.0, 0.0, 12.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3001, 173001, 124001, 0.0625, 26524091.41939091, 11051704.75807955, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23001, 33.65382834, 0.00130002, 41.24566071, 0.02291966, 4.12456607, 0.0857389, -33.65382834, -0.00130002, -41.24566071, -0.02291966, -4.12456607, -0.0857389, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13001, 29.89281176, 0.00130002, 36.63621146, 0.02291966, 3.66362115, 0.0857389, -29.89281176, -0.00130002, -36.63621146, -0.02291966, -3.66362115, -0.0857389, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23001, 3001, 0.0, 67.4763068, 0.02600041, 67.4763068, 0.07800124, 47.23341476, -3194.90708454, 0.05, 2, 0, 73001, 24001, 2, 3)
    ops.uniaxialMaterial('LimitState', 43001, 16.8690767, 9.378e-05, 50.6072301, 0.00028134, 168.69076699, 0.00093781, -16.8690767, -9.378e-05, -50.6072301, -0.00028134, -168.69076699, -0.00093781, 0.4, 0.3, 0.003, 0.0, 0.0, 23001, 2)
    ops.limitCurve('ThreePoint', 13001, 3001, 0.0, 67.4763068, 0.02600041, 67.4763068, 0.07800124, 47.23341476, -3194.90708454, 0.05, 2, 0, 73001, 24001, 1, 3)
    ops.uniaxialMaterial('LimitState', 33001, 16.8690767, 9.378e-05, 50.6072301, 0.00028134, 168.69076699, 0.00093781, -16.8690767, -9.378e-05, -50.6072301, -0.00028134, -168.69076699, -0.00093781, 0.4, 0.3, 0.003, 0.0, 0.0, 13001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3001, 99999, 'P', 43001, 'Vy', 33001, 'Vz', 23001, 'My', 13001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173001, 73001, 173001, 3001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124001, 124001, 24001, 3001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173002, 7.4, 0.0, 9.9)
    ops.node(124002, 7.4, 0.0, 12.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3002, 173002, 124002, 0.1225, 33340524.8414375, 13891885.35059896, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23002, 88.91452379, 0.00099657, 106.92494654, 0.01659811, 10.69249465, 0.05299107, -88.91452379, -0.00099657, -106.92494654, -0.01659811, -10.69249465, -0.05299107, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13002, 88.91452379, 0.00099657, 106.92494654, 0.01659811, 10.69249465, 0.05299107, -88.91452379, -0.00099657, -106.92494654, -0.01659811, -10.69249465, -0.05299107, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23002, 3002, 0.0, 105.37485893, 0.01993135, 105.37485893, 0.05979405, 73.76240125, -1529.81311309, 0.05, 2, 0, 73002, 24002, 2, 3)
    ops.uniaxialMaterial('LimitState', 43002, 26.34371473, 5.944e-05, 79.0311442, 0.00017833, 263.43714732, 0.00059444, -26.34371473, -5.944e-05, -79.0311442, -0.00017833, -263.43714732, -0.00059444, 0.4, 0.3, 0.003, 0.0, 0.0, 23002, 2)
    ops.limitCurve('ThreePoint', 13002, 3002, 0.0, 105.37485893, 0.01993135, 105.37485893, 0.05979405, 73.76240125, -1529.81311309, 0.05, 2, 0, 73002, 24002, 1, 3)
    ops.uniaxialMaterial('LimitState', 33002, 26.34371473, 5.944e-05, 79.0311442, 0.00017833, 263.43714732, 0.00059444, -26.34371473, -5.944e-05, -79.0311442, -0.00017833, -263.43714732, -0.00059444, 0.4, 0.3, 0.003, 0.0, 0.0, 13002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3002, 99999, 'P', 43002, 'Vy', 33002, 'Vz', 23002, 'My', 13002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173002, 73002, 173002, 3002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124002, 124002, 24002, 3002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173005, 25.2, 0.0, 9.9)
    ops.node(124005, 25.2, 0.0, 12.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3005, 173005, 124005, 0.1225, 29093011.75661206, 12122088.23192169, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23005, 90.96950842, 0.00105711, 110.84949223, 0.01573836, 11.08494922, 0.05152059, -90.96950842, -0.00105711, -110.84949223, -0.01573836, -11.08494922, -0.05152059, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13005, 90.96950842, 0.00105711, 110.84949223, 0.01573836, 11.08494922, 0.05152059, -90.96950842, -0.00105711, -110.84949223, -0.01573836, -11.08494922, -0.05152059, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23005, 3005, 0.0, 74.45428431, 0.02114224, 74.45428431, 0.06342672, 52.11799902, -1261.14731853, 0.05, 2, 0, 73005, 24005, 2, 3)
    ops.uniaxialMaterial('LimitState', 43005, 18.61357108, 4.813e-05, 55.84071323, 0.0001444, 186.13571077, 0.00048133, -18.61357108, -4.813e-05, -55.84071323, -0.0001444, -186.13571077, -0.00048133, 0.4, 0.3, 0.003, 0.0, 0.0, 23005, 2)
    ops.limitCurve('ThreePoint', 13005, 3005, 0.0, 74.45428431, 0.02114224, 74.45428431, 0.06342672, 52.11799902, -1261.14731853, 0.05, 2, 0, 73005, 24005, 1, 3)
    ops.uniaxialMaterial('LimitState', 33005, 18.61357108, 4.813e-05, 55.84071323, 0.0001444, 186.13571077, 0.00048133, -18.61357108, -4.813e-05, -55.84071323, -0.0001444, -186.13571077, -0.00048133, 0.4, 0.3, 0.003, 0.0, 0.0, 13005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3005, 99999, 'P', 43005, 'Vy', 33005, 'Vz', 23005, 'My', 13005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173005, 73005, 173005, 3005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124005, 124005, 24005, 3005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173006, 32.6, 0.0, 9.9)
    ops.node(124006, 32.6, 0.0, 12.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3006, 173006, 124006, 0.0625, 29369354.30670407, 12237230.96112669, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23006, 32.13904849, 0.0013097, 39.13394698, 0.0192234, 3.9133947, 0.08320386, -32.13904849, -0.0013097, -39.13394698, -0.0192234, -3.9133947, -0.08320386, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13006, 28.99431227, 0.0013097, 35.30477512, 0.0192234, 3.53047751, 0.08320386, -28.99431227, -0.0013097, -35.30477512, -0.0192234, -3.53047751, -0.08320386, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23006, 3006, 0.0, 58.88793305, 0.02619407, 58.88793305, 0.07858222, 41.22155314, -2441.31464526, 0.05, 2, 0, 73006, 24006, 2, 3)
    ops.uniaxialMaterial('LimitState', 43006, 14.72198326, 7.392e-05, 44.16594979, 0.00022175, 147.21983263, 0.00073915, -14.72198326, -7.392e-05, -44.16594979, -0.00022175, -147.21983263, -0.00073915, 0.4, 0.3, 0.003, 0.0, 0.0, 23006, 2)
    ops.limitCurve('ThreePoint', 13006, 3006, 0.0, 58.88793305, 0.02619407, 58.88793305, 0.07858222, 41.22155314, -2441.31464526, 0.05, 2, 0, 73006, 24006, 1, 3)
    ops.uniaxialMaterial('LimitState', 33006, 14.72198326, 7.392e-05, 44.16594979, 0.00022175, 147.21983263, 0.00073915, -14.72198326, -7.392e-05, -44.16594979, -0.00022175, -147.21983263, -0.00073915, 0.4, 0.3, 0.003, 0.0, 0.0, 13006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3006, 99999, 'P', 43006, 'Vy', 33006, 'Vz', 23006, 'My', 13006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173006, 73006, 173006, 3006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124006, 124006, 24006, 3006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173007, 0.0, 3.5, 9.925)
    ops.node(124007, 0.0, 3.5, 12.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3007, 173007, 124007, 0.0625, 28556396.76498147, 11898498.65207561, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23007, 36.51597372, 0.00151014, 44.49555079, 0.02457423, 4.44955508, 0.07764087, -36.51597372, -0.00151014, -44.49555079, -0.02457423, -4.44955508, -0.07764087, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13007, 36.51597372, 0.00151014, 44.49555079, 0.02457423, 4.44955508, 0.07764087, -36.51597372, -0.00151014, -44.49555079, -0.02457423, -4.44955508, -0.07764087, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23007, 3007, 0.0, 66.65517048, 0.03020278, 66.65517048, 0.09060834, 46.65861933, -1894.35362304, 0.05, 2, 0, 73007, 24007, 2, 3)
    ops.uniaxialMaterial('LimitState', 43007, 16.66379262, 8.605e-05, 49.99137786, 0.00025814, 166.63792619, 0.00086046, -16.66379262, -8.605e-05, -49.99137786, -0.00025814, -166.63792619, -0.00086046, 0.4, 0.3, 0.003, 0.0, 0.0, 23007, 2)
    ops.limitCurve('ThreePoint', 13007, 3007, 0.0, 66.65517048, 0.03020278, 66.65517048, 0.09060834, 46.65861933, -1894.35362304, 0.05, 2, 0, 73007, 24007, 1, 3)
    ops.uniaxialMaterial('LimitState', 33007, 16.66379262, 8.605e-05, 49.99137786, 0.00025814, 166.63792619, 0.00086046, -16.66379262, -8.605e-05, -49.99137786, -0.00025814, -166.63792619, -0.00086046, 0.4, 0.3, 0.003, 0.0, 0.0, 13007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3007, 99999, 'P', 43007, 'Vy', 33007, 'Vz', 23007, 'My', 13007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173007, 73007, 173007, 3007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124007, 124007, 24007, 3007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173008, 7.4, 3.5, 9.925)
    ops.node(124008, 7.4, 3.5, 12.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3008, 173008, 124008, 0.1225, 28238947.50153174, 11766228.12563823, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23008, 87.84138283, 0.00111119, 107.15855396, 0.01851966, 10.7158554, 0.05311095, -87.84138283, -0.00111119, -107.15855396, -0.01851966, -10.7158554, -0.05311095, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13008, 87.84138283, 0.00111119, 107.15855396, 0.01851966, 10.7158554, 0.05311095, -87.84138283, -0.00111119, -107.15855396, -0.01851966, -10.7158554, -0.05311095, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23008, 3008, 0.0, 97.42773535, 0.0222237, 97.42773535, 0.06667111, 68.19941475, -1360.11868917, 0.05, 2, 0, 73008, 24008, 2, 3)
    ops.uniaxialMaterial('LimitState', 43008, 24.35693384, 6.489e-05, 73.07080151, 0.00019467, 243.56933838, 0.0006489, -24.35693384, -6.489e-05, -73.07080151, -0.00019467, -243.56933838, -0.0006489, 0.4, 0.3, 0.003, 0.0, 0.0, 23008, 2)
    ops.limitCurve('ThreePoint', 13008, 3008, 0.0, 97.42773535, 0.0222237, 97.42773535, 0.06667111, 68.19941475, -1360.11868917, 0.05, 2, 0, 73008, 24008, 1, 3)
    ops.uniaxialMaterial('LimitState', 33008, 24.35693384, 6.489e-05, 73.07080151, 0.00019467, 243.56933838, 0.0006489, -24.35693384, -6.489e-05, -73.07080151, -0.00019467, -243.56933838, -0.0006489, 0.4, 0.3, 0.003, 0.0, 0.0, 13008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3008, 99999, 'P', 43008, 'Vy', 33008, 'Vz', 23008, 'My', 13008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173008, 73008, 173008, 3008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124008, 124008, 24008, 3008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173009, 14.8, 3.5, 9.925)
    ops.node(124009, 14.8, 3.5, 12.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3009, 173009, 124009, 0.0625, 28849828.05117931, 12020761.68799138, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23009, 26.55425764, 0.00132691, 32.29072984, 0.02286692, 3.22907298, 0.0818023, -26.55425764, -0.00132691, -32.29072984, -0.02286692, -3.22907298, -0.0818023, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13009, 26.55425764, 0.00132691, 32.29072984, 0.02286692, 3.22907298, 0.0818023, -26.55425764, -0.00132691, -32.29072984, -0.02286692, -3.22907298, -0.0818023, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23009, 3009, 0.0, 81.27756682, 0.02653827, 81.27756682, 0.0796148, 56.89429677, -2082.68274746, 0.05, 2, 0, 73009, 24009, 2, 3)
    ops.uniaxialMaterial('LimitState', 43009, 20.31939171, 0.00010386, 60.95817512, 0.00031157, 203.19391705, 0.00103856, -20.31939171, -0.00010386, -60.95817512, -0.00031157, -203.19391705, -0.00103856, 0.4, 0.3, 0.003, 0.0, 0.0, 23009, 2)
    ops.limitCurve('ThreePoint', 13009, 3009, 0.0, 81.27756682, 0.02653827, 81.27756682, 0.0796148, 56.89429677, -2082.68274746, 0.05, 2, 0, 73009, 24009, 1, 3)
    ops.uniaxialMaterial('LimitState', 33009, 20.31939171, 0.00010386, 60.95817512, 0.00031157, 203.19391705, 0.00103856, -20.31939171, -0.00010386, -60.95817512, -0.00031157, -203.19391705, -0.00103856, 0.4, 0.3, 0.003, 0.0, 0.0, 13009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3009, 99999, 'P', 43009, 'Vy', 33009, 'Vz', 23009, 'My', 13009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173009, 73009, 173009, 3009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124009, 124009, 24009, 3009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173010, 17.8, 3.5, 9.925)
    ops.node(124010, 17.8, 3.5, 12.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3010, 173010, 124010, 0.0625, 31096026.82304648, 12956677.84293604, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23010, 26.10702047, 0.00123028, 31.56756589, 0.02105643, 3.15675659, 0.08167607, -26.10702047, -0.00123028, -31.56756589, -0.02105643, -3.15675659, -0.08167607, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13010, 26.10702047, 0.00123028, 31.56756589, 0.02105643, 3.15675659, 0.08167607, -26.10702047, -0.00123028, -31.56756589, -0.02105643, -3.15675659, -0.08167607, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23010, 3010, 0.0, 79.33303615, 0.02460562, 79.33303615, 0.07381685, 55.53312531, -1651.75345875, 0.05, 2, 0, 73010, 24010, 2, 3)
    ops.uniaxialMaterial('LimitState', 43010, 19.83325904, 9.405e-05, 59.49977711, 0.00028215, 198.33259038, 0.00094048, -19.83325904, -9.405e-05, -59.49977711, -0.00028215, -198.33259038, -0.00094048, 0.4, 0.3, 0.003, 0.0, 0.0, 23010, 2)
    ops.limitCurve('ThreePoint', 13010, 3010, 0.0, 79.33303615, 0.02460562, 79.33303615, 0.07381685, 55.53312531, -1651.75345875, 0.05, 2, 0, 73010, 24010, 1, 3)
    ops.uniaxialMaterial('LimitState', 33010, 19.83325904, 9.405e-05, 59.49977711, 0.00028215, 198.33259038, 0.00094048, -19.83325904, -9.405e-05, -59.49977711, -0.00028215, -198.33259038, -0.00094048, 0.4, 0.3, 0.003, 0.0, 0.0, 13010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3010, 99999, 'P', 43010, 'Vy', 33010, 'Vz', 23010, 'My', 13010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173010, 73010, 173010, 3010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124010, 124010, 24010, 3010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173011, 25.2, 3.5, 9.925)
    ops.node(124011, 25.2, 3.5, 12.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3011, 173011, 124011, 0.1225, 30488544.4621688, 12703560.19257033, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23011, 100.63195857, 0.00107304, 122.06374738, 0.01458217, 12.20637474, 0.04980469, -100.63195857, -0.00107304, -122.06374738, -0.01458217, -12.20637474, -0.04980469, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13011, 100.63195857, 0.00107304, 122.06374738, 0.01458217, 12.20637474, 0.04980469, -100.63195857, -0.00107304, -122.06374738, -0.01458217, -12.20637474, -0.04980469, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23011, 3011, 0.0, 82.7382057, 0.02146084, 82.7382057, 0.06438251, 57.91674399, -1036.14540612, 0.05, 2, 0, 73011, 24011, 2, 3)
    ops.uniaxialMaterial('LimitState', 43011, 20.68455143, 5.104e-05, 62.05365428, 0.00015312, 206.84551426, 0.00051041, -20.68455143, -5.104e-05, -62.05365428, -0.00015312, -206.84551426, -0.00051041, 0.4, 0.3, 0.003, 0.0, 0.0, 23011, 2)
    ops.limitCurve('ThreePoint', 13011, 3011, 0.0, 82.7382057, 0.02146084, 82.7382057, 0.06438251, 57.91674399, -1036.14540612, 0.05, 2, 0, 73011, 24011, 1, 3)
    ops.uniaxialMaterial('LimitState', 33011, 20.68455143, 5.104e-05, 62.05365428, 0.00015312, 206.84551426, 0.00051041, -20.68455143, -5.104e-05, -62.05365428, -0.00015312, -206.84551426, -0.00051041, 0.4, 0.3, 0.003, 0.0, 0.0, 13011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3011, 99999, 'P', 43011, 'Vy', 33011, 'Vz', 23011, 'My', 13011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173011, 73011, 173011, 3011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124011, 124011, 24011, 3011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173012, 32.6, 3.5, 9.925)
    ops.node(124012, 32.6, 3.5, 12.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3012, 173012, 124012, 0.0625, 28815020.79176477, 12006258.66323532, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23012, 38.32827167, 0.001464, 46.67598241, 0.02183764, 4.66759824, 0.0750452, -38.32827167, -0.001464, -46.67598241, -0.02183764, -4.66759824, -0.0750452, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13012, 38.32827167, 0.001464, 46.67598241, 0.02183764, 4.66759824, 0.0750452, -38.32827167, -0.001464, -46.67598241, -0.02183764, -4.66759824, -0.0750452, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23012, 3012, 0.0, 49.85861451, 0.02928006, 49.85861451, 0.08784018, 34.90103016, -1467.37597191, 0.05, 2, 0, 73012, 24012, 2, 3)
    ops.uniaxialMaterial('LimitState', 43012, 12.46465363, 6.379e-05, 37.39396088, 0.00019136, 124.64653627, 0.00063786, -12.46465363, -6.379e-05, -37.39396088, -0.00019136, -124.64653627, -0.00063786, 0.4, 0.3, 0.003, 0.0, 0.0, 23012, 2)
    ops.limitCurve('ThreePoint', 13012, 3012, 0.0, 49.85861451, 0.02928006, 49.85861451, 0.08784018, 34.90103016, -1467.37597191, 0.05, 2, 0, 73012, 24012, 1, 3)
    ops.uniaxialMaterial('LimitState', 33012, 12.46465363, 6.379e-05, 37.39396088, 0.00019136, 124.64653627, 0.00063786, -12.46465363, -6.379e-05, -37.39396088, -0.00019136, -124.64653627, -0.00063786, 0.4, 0.3, 0.003, 0.0, 0.0, 13012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3012, 99999, 'P', 43012, 'Vy', 33012, 'Vz', 23012, 'My', 13012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173012, 73012, 173012, 3012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124012, 124012, 24012, 3012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173013, 0.0, 7.0, 9.925)
    ops.node(124013, 0.0, 7.0, 12.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3013, 173013, 124013, 0.0625, 25682464.47562659, 10701026.86484441, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23013, 39.62798556, 0.00153845, 48.55033758, 0.0252864, 4.85503376, 0.07637456, -39.62798556, -0.00153845, -48.55033758, -0.0252864, -4.85503376, -0.07637456, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13013, 39.62798556, 0.00153845, 48.55033758, 0.0252864, 4.85503376, 0.07637456, -39.62798556, -0.00153845, -48.55033758, -0.0252864, -4.85503376, -0.07637456, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23013, 3013, 0.0, 63.39525849, 0.03076906, 63.39525849, 0.09230718, 44.37668094, -1805.03184979, 0.05, 2, 0, 73013, 24013, 2, 3)
    ops.uniaxialMaterial('LimitState', 43013, 15.84881462, 9.1e-05, 47.54644387, 0.00027299, 158.48814622, 0.00090996, -15.84881462, -9.1e-05, -47.54644387, -0.00027299, -158.48814622, -0.00090996, 0.4, 0.3, 0.003, 0.0, 0.0, 23013, 2)
    ops.limitCurve('ThreePoint', 13013, 3013, 0.0, 63.39525849, 0.03076906, 63.39525849, 0.09230718, 44.37668094, -1805.03184979, 0.05, 2, 0, 73013, 24013, 1, 3)
    ops.uniaxialMaterial('LimitState', 33013, 15.84881462, 9.1e-05, 47.54644387, 0.00027299, 158.48814622, 0.00090996, -15.84881462, -9.1e-05, -47.54644387, -0.00027299, -158.48814622, -0.00090996, 0.4, 0.3, 0.003, 0.0, 0.0, 13013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3013, 99999, 'P', 43013, 'Vy', 33013, 'Vz', 23013, 'My', 13013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173013, 73013, 173013, 3013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124013, 124013, 24013, 3013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173014, 7.4, 7.0, 9.925)
    ops.node(124014, 7.4, 7.0, 12.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3014, 173014, 124014, 0.1225, 30854831.70625789, 12856179.87760746, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23014, 93.02592019, 0.00106175, 112.71883191, 0.01653915, 11.27188319, 0.05184717, -93.02592019, -0.00106175, -112.71883191, -0.01653915, -11.27188319, -0.05184717, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13014, 93.02592019, 0.00106175, 112.71883191, 0.01653915, 11.27188319, 0.05184717, -93.02592019, -0.00106175, -112.71883191, -0.01653915, -11.27188319, -0.05184717, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23014, 3014, 0.0, 97.30649592, 0.02123495, 97.30649592, 0.06370484, 68.11454714, -1204.83999822, 0.05, 2, 0, 73014, 24014, 2, 3)
    ops.uniaxialMaterial('LimitState', 43014, 24.32662398, 5.932e-05, 72.97987194, 0.00017795, 243.2662398, 0.00059315, -24.32662398, -5.932e-05, -72.97987194, -0.00017795, -243.2662398, -0.00059315, 0.4, 0.3, 0.003, 0.0, 0.0, 23014, 2)
    ops.limitCurve('ThreePoint', 13014, 3014, 0.0, 97.30649592, 0.02123495, 97.30649592, 0.06370484, 68.11454714, -1204.83999822, 0.05, 2, 0, 73014, 24014, 1, 3)
    ops.uniaxialMaterial('LimitState', 33014, 24.32662398, 5.932e-05, 72.97987194, 0.00017795, 243.2662398, 0.00059315, -24.32662398, -5.932e-05, -72.97987194, -0.00017795, -243.2662398, -0.00059315, 0.4, 0.3, 0.003, 0.0, 0.0, 13014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3014, 99999, 'P', 43014, 'Vy', 33014, 'Vz', 23014, 'My', 13014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173014, 73014, 173014, 3014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124014, 124014, 24014, 3014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173015, 14.8, 7.0, 9.925)
    ops.node(124015, 14.8, 7.0, 12.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3015, 173015, 124015, 0.0625, 28288923.7208566, 11787051.55035692, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23015, 24.93116737, 0.00132265, 30.38088085, 0.01870934, 3.03808808, 0.0787619, -24.93116737, -0.00132265, -30.38088085, -0.01870934, -3.03808808, -0.0787619, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13015, 24.93116737, 0.00132265, 30.38088085, 0.01870934, 3.03808808, 0.0787619, -24.93116737, -0.00132265, -30.38088085, -0.01870934, -3.03808808, -0.0787619, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23015, 3015, 0.0, 60.85148883, 0.02645303, 60.85148883, 0.07935908, 42.59604218, -1466.31188121, 0.05, 2, 0, 73015, 24015, 2, 3)
    ops.uniaxialMaterial('LimitState', 43015, 15.21287221, 7.93e-05, 45.63861662, 0.00023789, 152.12872208, 0.00079297, -15.21287221, -7.93e-05, -45.63861662, -0.00023789, -152.12872208, -0.00079297, 0.4, 0.3, 0.003, 0.0, 0.0, 23015, 2)
    ops.limitCurve('ThreePoint', 13015, 3015, 0.0, 60.85148883, 0.02645303, 60.85148883, 0.07935908, 42.59604218, -1466.31188121, 0.05, 2, 0, 73015, 24015, 1, 3)
    ops.uniaxialMaterial('LimitState', 33015, 15.21287221, 7.93e-05, 45.63861662, 0.00023789, 152.12872208, 0.00079297, -15.21287221, -7.93e-05, -45.63861662, -0.00023789, -152.12872208, -0.00079297, 0.4, 0.3, 0.003, 0.0, 0.0, 13015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3015, 99999, 'P', 43015, 'Vy', 33015, 'Vz', 23015, 'My', 13015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173015, 73015, 173015, 3015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124015, 124015, 24015, 3015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173016, 17.8, 7.0, 9.925)
    ops.node(124016, 17.8, 7.0, 12.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3016, 173016, 124016, 0.0625, 29721660.9941299, 12384025.41422079, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23016, 25.71162023, 0.00125452, 31.22714522, 0.0181373, 3.12271452, 0.07918871, -25.71162023, -0.00125452, -31.22714522, -0.0181373, -3.12271452, -0.07918871, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13016, 25.71162023, 0.00125452, 31.22714522, 0.0181373, 3.12271452, 0.07918871, -25.71162023, -0.00125452, -31.22714522, -0.0181373, -3.12271452, -0.07918871, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23016, 3016, 0.0, 62.46186741, 0.02509035, 62.46186741, 0.07527106, 43.72330719, -1466.23974857, 0.05, 2, 0, 73016, 24016, 2, 3)
    ops.uniaxialMaterial('LimitState', 43016, 15.61546685, 7.747e-05, 46.84640056, 0.00023242, 156.15466853, 0.00077472, -15.61546685, -7.747e-05, -46.84640056, -0.00023242, -156.15466853, -0.00077472, 0.4, 0.3, 0.003, 0.0, 0.0, 23016, 2)
    ops.limitCurve('ThreePoint', 13016, 3016, 0.0, 62.46186741, 0.02509035, 62.46186741, 0.07527106, 43.72330719, -1466.23974857, 0.05, 2, 0, 73016, 24016, 1, 3)
    ops.uniaxialMaterial('LimitState', 33016, 15.61546685, 7.747e-05, 46.84640056, 0.00023242, 156.15466853, 0.00077472, -15.61546685, -7.747e-05, -46.84640056, -0.00023242, -156.15466853, -0.00077472, 0.4, 0.3, 0.003, 0.0, 0.0, 13016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3016, 99999, 'P', 43016, 'Vy', 33016, 'Vz', 23016, 'My', 13016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173016, 73016, 173016, 3016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124016, 124016, 24016, 3016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173017, 25.2, 7.0, 9.925)
    ops.node(124017, 25.2, 7.0, 12.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3017, 173017, 124017, 0.1225, 26109851.63553866, 10879104.84814111, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23017, 90.35410828, 0.00114629, 110.6856527, 0.01601138, 11.06856527, 0.04978402, -90.35410828, -0.00114629, -110.6856527, -0.01601138, -11.06856527, -0.04978402, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13017, 90.35410828, 0.00114629, 110.6856527, 0.01601138, 11.06856527, 0.04978402, -90.35410828, -0.00114629, -110.6856527, -0.01601138, -11.06856527, -0.04978402, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23017, 3017, 0.0, 68.1571312, 0.02292582, 68.1571312, 0.06877746, 47.70999184, -1001.98731528, 0.05, 2, 0, 73017, 24017, 2, 3)
    ops.uniaxialMaterial('LimitState', 43017, 17.0392828, 4.91e-05, 51.1178484, 0.00014729, 170.39282799, 0.00049097, -17.0392828, -4.91e-05, -51.1178484, -0.00014729, -170.39282799, -0.00049097, 0.4, 0.3, 0.003, 0.0, 0.0, 23017, 2)
    ops.limitCurve('ThreePoint', 13017, 3017, 0.0, 68.1571312, 0.02292582, 68.1571312, 0.06877746, 47.70999184, -1001.98731528, 0.05, 2, 0, 73017, 24017, 1, 3)
    ops.uniaxialMaterial('LimitState', 33017, 17.0392828, 4.91e-05, 51.1178484, 0.00014729, 170.39282799, 0.00049097, -17.0392828, -4.91e-05, -51.1178484, -0.00014729, -170.39282799, -0.00049097, 0.4, 0.3, 0.003, 0.0, 0.0, 13017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3017, 99999, 'P', 43017, 'Vy', 33017, 'Vz', 23017, 'My', 13017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173017, 73017, 173017, 3017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124017, 124017, 24017, 3017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173018, 32.6, 7.0, 9.925)
    ops.node(124018, 32.6, 7.0, 12.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3018, 173018, 124018, 0.0625, 30098005.68731456, 12540835.70304773, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23018, 39.17367397, 0.00141772, 47.55170456, 0.02044089, 4.75517046, 0.07427726, -39.17367397, -0.00141772, -47.55170456, -0.02044089, -4.75517046, -0.07427726, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13018, 39.17367397, 0.00141772, 47.55170456, 0.02044089, 4.75517046, 0.07427726, -39.17367397, -0.00141772, -47.55170456, -0.02044089, -4.75517046, -0.07427726, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23018, 3018, 0.0, 46.38818751, 0.02835448, 46.38818751, 0.08506345, 32.47173126, -1353.79636497, 0.05, 2, 0, 73018, 24018, 2, 3)
    ops.uniaxialMaterial('LimitState', 43018, 11.59704688, 5.682e-05, 34.79114063, 0.00017045, 115.97046877, 0.00056816, -11.59704688, -5.682e-05, -34.79114063, -0.00017045, -115.97046877, -0.00056816, 0.4, 0.3, 0.003, 0.0, 0.0, 23018, 2)
    ops.limitCurve('ThreePoint', 13018, 3018, 0.0, 46.38818751, 0.02835448, 46.38818751, 0.08506345, 32.47173126, -1353.79636497, 0.05, 2, 0, 73018, 24018, 1, 3)
    ops.uniaxialMaterial('LimitState', 33018, 11.59704688, 5.682e-05, 34.79114063, 0.00017045, 115.97046877, 0.00056816, -11.59704688, -5.682e-05, -34.79114063, -0.00017045, -115.97046877, -0.00056816, 0.4, 0.3, 0.003, 0.0, 0.0, 13018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3018, 99999, 'P', 43018, 'Vy', 33018, 'Vz', 23018, 'My', 13018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173018, 73018, 173018, 3018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124018, 124018, 24018, 3018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173019, 0.0, 10.5, 9.9)
    ops.node(124019, 0.0, 10.5, 12.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3019, 173019, 124019, 0.0625, 28852692.34581239, 12021955.1440885, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23019, 32.21794281, 0.00128862, 39.28209139, 0.02367128, 3.92820914, 0.0874754, -32.21794281, -0.00128862, -39.28209139, -0.02367128, -3.92820914, -0.0874754, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13019, 28.95206464, 0.00128862, 35.30013246, 0.02367128, 3.53001325, 0.0874754, -28.95206464, -0.00128862, -35.30013246, -0.02367128, -3.53001325, -0.0874754, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23019, 3019, 0.0, 73.07369509, 0.02577244, 73.07369509, 0.07731731, 51.15158657, -3427.81793782, 0.05, 2, 0, 73019, 24019, 2, 3)
    ops.uniaxialMaterial('LimitState', 43019, 18.26842377, 9.336e-05, 54.80527132, 0.00028009, 182.68423774, 0.00093364, -18.26842377, -9.336e-05, -54.80527132, -0.00028009, -182.68423774, -0.00093364, 0.4, 0.3, 0.003, 0.0, 0.0, 23019, 2)
    ops.limitCurve('ThreePoint', 13019, 3019, 0.0, 73.07369509, 0.02577244, 73.07369509, 0.07731731, 51.15158657, -3427.81793782, 0.05, 2, 0, 73019, 24019, 1, 3)
    ops.uniaxialMaterial('LimitState', 33019, 18.26842377, 9.336e-05, 54.80527132, 0.00028009, 182.68423774, 0.00093364, -18.26842377, -9.336e-05, -54.80527132, -0.00028009, -182.68423774, -0.00093364, 0.4, 0.3, 0.003, 0.0, 0.0, 13019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3019, 99999, 'P', 43019, 'Vy', 33019, 'Vz', 23019, 'My', 13019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173019, 73019, 173019, 3019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124019, 124019, 24019, 3019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173020, 7.4, 10.5, 9.9)
    ops.node(124020, 7.4, 10.5, 12.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3020, 173020, 124020, 0.1225, 29338774.27776011, 12224489.28240005, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23020, 88.56215447, 0.00113159, 107.84724541, 0.01590806, 10.78472454, 0.05173619, -88.56215447, -0.00113159, -107.84724541, -0.01590806, -10.78472454, -0.05173619, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13020, 88.56215447, 0.00113159, 107.84724541, 0.01590806, 10.78472454, 0.05173619, -88.56215447, -0.00113159, -107.84724541, -0.01590806, -10.78472454, -0.05173619, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23020, 3020, 0.0, 77.65559008, 0.02263178, 77.65559008, 0.06789534, 54.35891306, -1296.42831267, 0.05, 2, 0, 73020, 24020, 2, 3)
    ops.uniaxialMaterial('LimitState', 43020, 19.41389752, 4.978e-05, 58.24169256, 0.00014935, 194.1389752, 0.00049783, -19.41389752, -4.978e-05, -58.24169256, -0.00014935, -194.1389752, -0.00049783, 0.4, 0.3, 0.003, 0.0, 0.0, 23020, 2)
    ops.limitCurve('ThreePoint', 13020, 3020, 0.0, 77.65559008, 0.02263178, 77.65559008, 0.06789534, 54.35891306, -1296.42831267, 0.05, 2, 0, 73020, 24020, 1, 3)
    ops.uniaxialMaterial('LimitState', 33020, 19.41389752, 4.978e-05, 58.24169256, 0.00014935, 194.1389752, 0.00049783, -19.41389752, -4.978e-05, -58.24169256, -0.00014935, -194.1389752, -0.00049783, 0.4, 0.3, 0.003, 0.0, 0.0, 13020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3020, 99999, 'P', 43020, 'Vy', 33020, 'Vz', 23020, 'My', 13020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173020, 73020, 173020, 3020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124020, 124020, 24020, 3020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173021, 14.8, 10.5, 9.9)
    ops.node(124021, 14.8, 10.5, 12.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3021, 173021, 124021, 0.0625, 28975582.9105846, 12073159.54607692, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23021, 23.61927631, 0.00133847, 28.77350648, 0.0221484, 2.87735065, 0.08496914, -23.61927631, -0.00133847, -28.77350648, -0.0221484, -2.87735065, -0.08496914, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13021, 23.61927631, 0.00133847, 28.77350648, 0.0221484, 2.87735065, 0.08496914, -23.61927631, -0.00133847, -28.77350648, -0.0221484, -2.87735065, -0.08496914, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23021, 3021, 0.0, 73.59420448, 0.02676933, 73.59420448, 0.08030798, 51.51594314, -2674.9699785, 0.05, 2, 0, 73021, 24021, 2, 3)
    ops.uniaxialMaterial('LimitState', 43021, 18.39855112, 9.363e-05, 55.19565336, 0.00028089, 183.9855112, 0.0009363, -18.39855112, -9.363e-05, -55.19565336, -0.00028089, -183.9855112, -0.0009363, 0.4, 0.3, 0.003, 0.0, 0.0, 23021, 2)
    ops.limitCurve('ThreePoint', 13021, 3021, 0.0, 73.59420448, 0.02676933, 73.59420448, 0.08030798, 51.51594314, -2674.9699785, 0.05, 2, 0, 73021, 24021, 1, 3)
    ops.uniaxialMaterial('LimitState', 33021, 18.39855112, 9.363e-05, 55.19565336, 0.00028089, 183.9855112, 0.0009363, -18.39855112, -9.363e-05, -55.19565336, -0.00028089, -183.9855112, -0.0009363, 0.4, 0.3, 0.003, 0.0, 0.0, 13021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3021, 99999, 'P', 43021, 'Vy', 33021, 'Vz', 23021, 'My', 13021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173021, 73021, 173021, 3021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124021, 124021, 24021, 3021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173022, 17.8, 10.5, 9.9)
    ops.node(124022, 17.8, 10.5, 12.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3022, 173022, 124022, 0.0625, 28684934.03595847, 11952055.84831603, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23022, 24.05728416, 0.00125098, 29.32784296, 0.01917937, 2.9327843, 0.08186377, -24.05728416, -0.00125098, -29.32784296, -0.01917937, -2.9327843, -0.08186377, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13022, 24.05728416, 0.00125098, 29.32784296, 0.01917937, 2.9327843, 0.08186377, -24.05728416, -0.00125098, -29.32784296, -0.01917937, -2.9327843, -0.08186377, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23022, 3022, 0.0, 61.28950996, 0.02501958, 61.28950996, 0.07505875, 42.90265697, -1953.70951157, 0.05, 2, 0, 73022, 24022, 2, 3)
    ops.uniaxialMaterial('LimitState', 43022, 15.32237749, 7.877e-05, 45.96713247, 0.0002363, 153.22377489, 0.00078765, -15.32237749, -7.877e-05, -45.96713247, -0.0002363, -153.22377489, -0.00078765, 0.4, 0.3, 0.003, 0.0, 0.0, 23022, 2)
    ops.limitCurve('ThreePoint', 13022, 3022, 0.0, 61.28950996, 0.02501958, 61.28950996, 0.07505875, 42.90265697, -1953.70951157, 0.05, 2, 0, 73022, 24022, 1, 3)
    ops.uniaxialMaterial('LimitState', 33022, 15.32237749, 7.877e-05, 45.96713247, 0.0002363, 153.22377489, 0.00078765, -15.32237749, -7.877e-05, -45.96713247, -0.0002363, -153.22377489, -0.00078765, 0.4, 0.3, 0.003, 0.0, 0.0, 13022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3022, 99999, 'P', 43022, 'Vy', 33022, 'Vz', 23022, 'My', 13022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173022, 73022, 173022, 3022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124022, 124022, 24022, 3022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173023, 25.2, 10.5, 9.9)
    ops.node(124023, 25.2, 10.5, 12.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3023, 173023, 124023, 0.1225, 29578212.84340128, 12324255.3514172, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23023, 89.19007534, 0.00115947, 108.54287314, 0.01965259, 10.85428731, 0.0555239, -89.19007534, -0.00115947, -108.54287314, -0.01965259, -10.85428731, -0.0555239, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13023, 89.19007534, 0.00115947, 108.54287314, 0.01965259, 10.85428731, 0.0555239, -89.19007534, -0.00115947, -108.54287314, -0.01965259, -10.85428731, -0.0555239, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23023, 3023, 0.0, 106.19926489, 0.02318948, 106.19926489, 0.06956843, 74.33948543, -1983.76940262, 0.05, 2, 0, 73023, 24023, 2, 3)
    ops.uniaxialMaterial('LimitState', 43023, 26.54981622, 6.753e-05, 79.64944867, 0.00020259, 265.49816224, 0.0006753, -26.54981622, -6.753e-05, -79.64944867, -0.00020259, -265.49816224, -0.0006753, 0.4, 0.3, 0.003, 0.0, 0.0, 23023, 2)
    ops.limitCurve('ThreePoint', 13023, 3023, 0.0, 106.19926489, 0.02318948, 106.19926489, 0.06956843, 74.33948543, -1983.76940262, 0.05, 2, 0, 73023, 24023, 1, 3)
    ops.uniaxialMaterial('LimitState', 33023, 26.54981622, 6.753e-05, 79.64944867, 0.00020259, 265.49816224, 0.0006753, -26.54981622, -6.753e-05, -79.64944867, -0.00020259, -265.49816224, -0.0006753, 0.4, 0.3, 0.003, 0.0, 0.0, 13023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3023, 99999, 'P', 43023, 'Vy', 33023, 'Vz', 23023, 'My', 13023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173023, 73023, 173023, 3023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124023, 124023, 24023, 3023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173024, 32.6, 10.5, 9.9)
    ops.node(124024, 32.6, 10.5, 12.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3024, 173024, 124024, 0.0625, 32946150.86175956, 13727562.85906648, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23024, 34.96866786, 0.00118448, 42.1115493, 0.02287043, 4.21115493, 0.0877796, -34.96866786, -0.00118448, -42.1115493, -0.02287043, -4.21115493, -0.0877796, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13024, 31.02827173, 0.00118448, 37.36626742, 0.02287043, 3.73662674, 0.0877796, -31.02827173, -0.00118448, -37.36626742, -0.02287043, -3.73662674, -0.0877796, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23024, 3024, 0.0, 84.17841022, 0.0236896, 84.17841022, 0.0710688, 58.92488716, -3978.0927232, 0.05, 2, 0, 73024, 24024, 2, 3)
    ops.uniaxialMaterial('LimitState', 43024, 21.04460256, 9.419e-05, 63.13380767, 0.00028257, 210.44602556, 0.00094189, -21.04460256, -9.419e-05, -63.13380767, -0.00028257, -210.44602556, -0.00094189, 0.4, 0.3, 0.003, 0.0, 0.0, 23024, 2)
    ops.limitCurve('ThreePoint', 13024, 3024, 0.0, 84.17841022, 0.0236896, 84.17841022, 0.0710688, 58.92488716, -3978.0927232, 0.05, 2, 0, 73024, 24024, 1, 3)
    ops.uniaxialMaterial('LimitState', 33024, 21.04460256, 9.419e-05, 63.13380767, 0.00028257, 210.44602556, 0.00094189, -21.04460256, -9.419e-05, -63.13380767, -0.00028257, -210.44602556, -0.00094189, 0.4, 0.3, 0.003, 0.0, 0.0, 13024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3024, 99999, 'P', 43024, 'Vy', 33024, 'Vz', 23024, 'My', 13024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173024, 73024, 173024, 3024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124024, 124024, 24024, 3024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170003, 14.8, 0.0, 0.0)
    ops.node(124025, 14.8, 0.0, 1.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4063, 170003, 124025, 0.1225, 27293166.79645327, 11372152.83185553, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24063, 169.62045433, 0.00091379, 205.21441572, 0.04739527, 20.52144157, 0.12084815, -169.62045433, -0.00091379, -205.21441572, -0.04739527, -20.52144157, -0.12084815, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14063, 156.59411658, 0.00091379, 189.45456941, 0.04739527, 18.94545694, 0.12084815, -156.59411658, -0.00091379, -189.45456941, -0.04739527, -18.94545694, -0.12084815, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24063, 4063, 0.0, 231.88940641, 0.01827572, 231.88940641, 0.05482715, 162.32258449, -8182.22294405, 0.05, 2, 0, 70003, 24025, 2, 3)
    ops.uniaxialMaterial('LimitState', 44063, 57.9723516, 7.99e-05, 173.91705481, 0.0002397, 579.72351604, 0.00079899, -57.9723516, -7.99e-05, -173.91705481, -0.0002397, -579.72351604, -0.00079899, 0.4, 0.3, 0.003, 0.0, 0.0, 24063, 2)
    ops.limitCurve('ThreePoint', 14063, 4063, 0.0, 231.88940641, 0.01827572, 231.88940641, 0.05482715, 162.32258449, -8182.22294405, 0.05, 2, 0, 70003, 24025, 1, 3)
    ops.uniaxialMaterial('LimitState', 34063, 57.9723516, 7.99e-05, 173.91705481, 0.0002397, 579.72351604, 0.00079899, -57.9723516, -7.99e-05, -173.91705481, -0.0002397, -579.72351604, -0.00079899, 0.4, 0.3, 0.003, 0.0, 0.0, 14063, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4063, 99999, 'P', 44063, 'Vy', 34063, 'Vz', 24063, 'My', 14063, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170003, 70003, 170003, 4063, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124025, 124025, 24025, 4063, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174025, 14.8, 0.0, 1.825)
    ops.node(121003, 14.8, 0.0, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4064, 174025, 121003, 0.1225, 28507066.29469013, 11877944.28945422, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24064, 151.62665871, 0.00086378, 183.37470374, 0.04982428, 18.33747037, 0.12928804, -151.62665871, -0.00086378, -183.37470374, -0.04982428, -18.33747037, -0.12928804, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14064, 126.05122102, 0.00086378, 152.44420412, 0.04982428, 15.24442041, 0.12928804, -126.05122102, -0.00086378, -152.44420412, -0.04982428, -15.24442041, -0.12928804, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24064, 4064, 0.0, 266.92202026, 0.01727564, 266.92202026, 0.05182693, 186.84541418, -11723.8485859, 0.05, 2, 0, 74025, 21003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44064, 66.73050506, 8.805e-05, 200.19151519, 0.00026416, 667.30505064, 0.00088054, -66.73050506, -8.805e-05, -200.19151519, -0.00026416, -667.30505064, -0.00088054, 0.4, 0.3, 0.003, 0.0, 0.0, 24064, 2)
    ops.limitCurve('ThreePoint', 14064, 4064, 0.0, 266.92202026, 0.01727564, 266.92202026, 0.05182693, 186.84541418, -11723.8485859, 0.05, 2, 0, 74025, 21003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34064, 66.73050506, 8.805e-05, 200.19151519, 0.00026416, 667.30505064, 0.00088054, -66.73050506, -8.805e-05, -200.19151519, -0.00026416, -667.30505064, -0.00088054, 0.4, 0.3, 0.003, 0.0, 0.0, 14064, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4064, 99999, 'P', 44064, 'Vy', 34064, 'Vz', 24064, 'My', 14064, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174025, 74025, 174025, 4064, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121003, 121003, 21003, 4064, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170004, 17.8, 0.0, 0.0)
    ops.node(124026, 17.8, 0.0, 1.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4065, 170004, 124026, 0.1225, 26457465.97396301, 11023944.15581792, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24065, 166.05700774, 0.00091921, 200.99410347, 0.04851687, 20.09941035, 0.11885641, -166.05700774, -0.00091921, -200.99410347, -0.04851687, -20.09941035, -0.11885641, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14065, 153.38599432, 0.00091921, 185.65720792, 0.04851687, 18.56572079, 0.11885641, -153.38599432, -0.00091921, -185.65720792, -0.04851687, -18.56572079, -0.11885641, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24065, 4065, 0.0, 242.451353, 0.01838416, 242.451353, 0.05515248, 169.7159471, -9606.11948121, 0.05, 2, 0, 70004, 24026, 2, 3)
    ops.uniaxialMaterial('LimitState', 44065, 60.61283825, 8.618e-05, 181.83851475, 0.00025853, 606.1283825, 0.00086177, -60.61283825, -8.618e-05, -181.83851475, -0.00025853, -606.1283825, -0.00086177, 0.4, 0.3, 0.003, 0.0, 0.0, 24065, 2)
    ops.limitCurve('ThreePoint', 14065, 4065, 0.0, 242.451353, 0.01838416, 242.451353, 0.05515248, 169.7159471, -9606.11948121, 0.05, 2, 0, 70004, 24026, 1, 3)
    ops.uniaxialMaterial('LimitState', 34065, 60.61283825, 8.618e-05, 181.83851475, 0.00025853, 606.1283825, 0.00086177, -60.61283825, -8.618e-05, -181.83851475, -0.00025853, -606.1283825, -0.00086177, 0.4, 0.3, 0.003, 0.0, 0.0, 14065, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4065, 99999, 'P', 44065, 'Vy', 34065, 'Vz', 24065, 'My', 14065, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170004, 70004, 170004, 4065, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124026, 124026, 24026, 4065, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174026, 17.8, 0.0, 1.825)
    ops.node(121004, 17.8, 0.0, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4066, 174026, 121004, 0.1225, 30497822.19991756, 12707425.91663232, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24066, 156.1935469, 0.00086158, 188.23857346, 0.04842768, 18.82385735, 0.1331475, -156.1935469, -0.00086158, -188.23857346, -0.04842768, -18.82385735, -0.1331475, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14066, 130.11060333, 0.00086158, 156.80439333, 0.04842768, 15.68043933, 0.1331475, -130.11060333, -0.00086158, -156.80439333, -0.04842768, -15.68043933, -0.1331475, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24066, 4066, 0.0, 271.59658644, 0.0172316, 271.59658644, 0.0516948, 190.11761051, -11071.68630466, 0.05, 2, 0, 74026, 21004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44066, 67.89914661, 8.375e-05, 203.69743983, 0.00025124, 678.9914661, 0.00083748, -67.89914661, -8.375e-05, -203.69743983, -0.00025124, -678.9914661, -0.00083748, 0.4, 0.3, 0.003, 0.0, 0.0, 24066, 2)
    ops.limitCurve('ThreePoint', 14066, 4066, 0.0, 271.59658644, 0.0172316, 271.59658644, 0.0516948, 190.11761051, -11071.68630466, 0.05, 2, 0, 74026, 21004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34066, 67.89914661, 8.375e-05, 203.69743983, 0.00025124, 678.9914661, 0.00083748, -67.89914661, -8.375e-05, -203.69743983, -0.00025124, -678.9914661, -0.00083748, 0.4, 0.3, 0.003, 0.0, 0.0, 14066, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4066, 99999, 'P', 44066, 'Vy', 34066, 'Vz', 24066, 'My', 14066, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174026, 74026, 174026, 4066, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121004, 121004, 21004, 4066, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171003, 14.8, 0.0, 3.5)
    ops.node(124027, 14.8, 0.0, 4.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4068, 171003, 124027, 0.1225, 30074904.86349335, 12531210.3597889, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24068, 101.37544895, 0.00083052, 122.51376429, 0.03576737, 12.25137643, 0.09836696, -101.37544895, -0.00083052, -122.51376429, -0.03576737, -12.25137643, -0.09836696, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14068, 95.41451068, 0.00083052, 115.30988018, 0.03576737, 11.53098802, 0.09836696, -95.41451068, -0.00083052, -115.30988018, -0.03576737, -11.53098802, -0.09836696, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24068, 4068, 0.0, 210.2927048, 0.01661041, 210.2927048, 0.04983122, 147.20489336, -6443.38791329, 0.05, 2, 0, 71003, 24027, 2, 3)
    ops.uniaxialMaterial('LimitState', 44068, 52.5731762, 6.576e-05, 157.7195286, 0.00019727, 525.731762, 0.00065756, -52.5731762, -6.576e-05, -157.7195286, -0.00019727, -525.731762, -0.00065756, 0.4, 0.3, 0.003, 0.0, 0.0, 24068, 2)
    ops.limitCurve('ThreePoint', 14068, 4068, 0.0, 210.2927048, 0.01661041, 210.2927048, 0.04983122, 147.20489336, -6443.38791329, 0.05, 2, 0, 71003, 24027, 1, 3)
    ops.uniaxialMaterial('LimitState', 34068, 52.5731762, 6.576e-05, 157.7195286, 0.00019727, 525.731762, 0.00065756, -52.5731762, -6.576e-05, -157.7195286, -0.00019727, -525.731762, -0.00065756, 0.4, 0.3, 0.003, 0.0, 0.0, 14068, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4068, 99999, 'P', 44068, 'Vy', 34068, 'Vz', 24068, 'My', 14068, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171003, 71003, 171003, 4068, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124027, 124027, 24027, 4068, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174027, 14.8, 0.0, 4.975)
    ops.node(122003, 14.8, 0.0, 6.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4069, 174027, 122003, 0.1225, 27992140.07958784, 11663391.69982827, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24069, 97.7186627, 0.00086229, 118.64661965, 0.03616162, 11.86466196, 0.09687775, -97.7186627, -0.00086229, -118.64661965, -0.03616162, -11.86466196, -0.09687775, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14069, 91.85967963, 0.00086229, 111.5328451, 0.03616162, 11.15328451, 0.09687775, -91.85967963, -0.00086229, -111.5328451, -0.03616162, -11.15328451, -0.09687775, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24069, 4069, 0.0, 192.76995357, 0.01724576, 192.76995357, 0.05173728, 134.9389675, -6249.49659493, 0.05, 2, 0, 74027, 22003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44069, 48.19248839, 6.476e-05, 144.57746517, 0.00019429, 481.92488392, 0.00064762, -48.19248839, -6.476e-05, -144.57746517, -0.00019429, -481.92488392, -0.00064762, 0.4, 0.3, 0.003, 0.0, 0.0, 24069, 2)
    ops.limitCurve('ThreePoint', 14069, 4069, 0.0, 192.76995357, 0.01724576, 192.76995357, 0.05173728, 134.9389675, -6249.49659493, 0.05, 2, 0, 74027, 22003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34069, 48.19248839, 6.476e-05, 144.57746517, 0.00019429, 481.92488392, 0.00064762, -48.19248839, -6.476e-05, -144.57746517, -0.00019429, -481.92488392, -0.00064762, 0.4, 0.3, 0.003, 0.0, 0.0, 14069, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4069, 99999, 'P', 44069, 'Vy', 34069, 'Vz', 24069, 'My', 14069, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174027, 74027, 174027, 4069, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122003, 122003, 22003, 4069, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171004, 17.8, 0.0, 3.5)
    ops.node(124028, 17.8, 0.0, 4.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4070, 171004, 124028, 0.1225, 28983819.67279368, 12076591.5303307, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24070, 101.58859231, 0.00086737, 123.03928627, 0.03493337, 12.30392863, 0.09584131, -101.58859231, -0.00086737, -123.03928627, -0.03493337, -12.30392863, -0.09584131, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14070, 95.69186538, 0.00086737, 115.89745021, 0.03493337, 11.58974502, 0.09584131, -95.69186538, -0.00086737, -115.89745021, -0.03493337, -11.58974502, -0.09584131, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24070, 4070, 0.0, 197.2457167, 0.01734732, 197.2457167, 0.05204197, 138.07200169, -5748.41081356, 0.05, 2, 0, 71004, 24028, 2, 3)
    ops.uniaxialMaterial('LimitState', 44070, 49.31142917, 6.4e-05, 147.93428752, 0.00019199, 493.11429174, 0.00063998, -49.31142917, -6.4e-05, -147.93428752, -0.00019199, -493.11429174, -0.00063998, 0.4, 0.3, 0.003, 0.0, 0.0, 24070, 2)
    ops.limitCurve('ThreePoint', 14070, 4070, 0.0, 197.2457167, 0.01734732, 197.2457167, 0.05204197, 138.07200169, -5748.41081356, 0.05, 2, 0, 71004, 24028, 1, 3)
    ops.uniaxialMaterial('LimitState', 34070, 49.31142917, 6.4e-05, 147.93428752, 0.00019199, 493.11429174, 0.00063998, -49.31142917, -6.4e-05, -147.93428752, -0.00019199, -493.11429174, -0.00063998, 0.4, 0.3, 0.003, 0.0, 0.0, 14070, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4070, 99999, 'P', 44070, 'Vy', 34070, 'Vz', 24070, 'My', 14070, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171004, 71004, 171004, 4070, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124028, 124028, 24028, 4070, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174028, 17.8, 0.0, 4.975)
    ops.node(122004, 17.8, 0.0, 6.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4071, 174028, 122004, 0.1225, 30008327.53956894, 12503469.80815372, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24071, 91.96210281, 0.00075903, 111.23040449, 0.03446795, 11.12304045, 0.09826935, -91.96210281, -0.00075903, -111.23040449, -0.03446795, -11.12304045, -0.09826935, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14071, 86.53696739, 0.00075903, 104.66857098, 0.03446795, 10.4668571, 0.09826935, -86.53696739, -0.00075903, -104.66857098, -0.03446795, -10.4668571, -0.09826935, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24071, 4071, 0.0, 196.73606633, 0.01518057, 196.73606633, 0.04554171, 137.71524643, -5637.74295926, 0.05, 2, 0, 74028, 22004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44071, 49.18401658, 6.165e-05, 147.55204974, 0.00018496, 491.84016582, 0.00061654, -49.18401658, -6.165e-05, -147.55204974, -0.00018496, -491.84016582, -0.00061654, 0.4, 0.3, 0.003, 0.0, 0.0, 24071, 2)
    ops.limitCurve('ThreePoint', 14071, 4071, 0.0, 196.73606633, 0.01518057, 196.73606633, 0.04554171, 137.71524643, -5637.74295926, 0.05, 2, 0, 74028, 22004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34071, 49.18401658, 6.165e-05, 147.55204974, 0.00018496, 491.84016582, 0.00061654, -49.18401658, -6.165e-05, -147.55204974, -0.00018496, -491.84016582, -0.00061654, 0.4, 0.3, 0.003, 0.0, 0.0, 14071, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4071, 99999, 'P', 44071, 'Vy', 34071, 'Vz', 24071, 'My', 14071, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174028, 74028, 174028, 4071, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122004, 122004, 22004, 4071, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172003, 14.8, 0.0, 6.7)
    ops.node(124029, 14.8, 0.0, 7.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4073, 172003, 124029, 0.0625, 30094446.48642823, 12539352.70267843, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24073, 49.82712532, 0.00105028, 60.11421728, 0.02962214, 6.01142173, 0.09168943, -49.82712532, -0.00105028, -60.11421728, -0.02962214, -6.01142173, -0.09168943, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14073, 49.82712532, 0.00105028, 60.11421728, 0.02962214, 6.01142173, 0.09168943, -49.82712532, -0.00105028, -60.11421728, -0.02962214, -6.01142173, -0.09168943, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24073, 4073, 0.0, 90.63382739, 0.02100562, 90.63382739, 0.06301685, 63.44367917, -2920.75021946, 0.05, 2, 0, 72003, 24029, 2, 3)
    ops.uniaxialMaterial('LimitState', 44073, 22.65845685, 5.551e-05, 67.97537054, 0.00016653, 226.58456846, 0.00055511, -22.65845685, -5.551e-05, -67.97537054, -0.00016653, -226.58456846, -0.00055511, 0.4, 0.3, 0.003, 0.0, 0.0, 24073, 2)
    ops.limitCurve('ThreePoint', 14073, 4073, 0.0, 90.63382739, 0.02100562, 90.63382739, 0.06301685, 63.44367917, -2920.75021946, 0.05, 2, 0, 72003, 24029, 1, 3)
    ops.uniaxialMaterial('LimitState', 34073, 22.65845685, 5.551e-05, 67.97537054, 0.00016653, 226.58456846, 0.00055511, -22.65845685, -5.551e-05, -67.97537054, -0.00016653, -226.58456846, -0.00055511, 0.4, 0.3, 0.003, 0.0, 0.0, 14073, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4073, 99999, 'P', 44073, 'Vy', 34073, 'Vz', 24073, 'My', 14073, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172003, 72003, 172003, 4073, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124029, 124029, 24029, 4073, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174029, 14.8, 0.0, 8.175)
    ops.node(123003, 14.8, 0.0, 9.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4074, 174029, 123003, 0.0625, 27721636.42604771, 11550681.84418655, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24074, 47.24719817, 0.00119294, 57.32433359, 0.022458, 5.73243336, 0.07299605, -47.24719817, -0.00119294, -57.32433359, -0.022458, -5.73243336, -0.07299605, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14074, 47.24719817, 0.00119294, 57.32433359, 0.022458, 5.73243336, 0.07299605, -47.24719817, -0.00119294, -57.32433359, -0.022458, -5.73243336, -0.07299605, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24074, 4074, 0.0, 65.89376034, 0.02385887, 65.89376034, 0.07157661, 46.12563223, -2054.03450658, 0.05, 2, 0, 74029, 23003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44074, 16.47344008, 4.381e-05, 49.42032025, 0.00013144, 164.73440084, 0.00043812, -16.47344008, -4.381e-05, -49.42032025, -0.00013144, -164.73440084, -0.00043812, 0.4, 0.3, 0.003, 0.0, 0.0, 24074, 2)
    ops.limitCurve('ThreePoint', 14074, 4074, 0.0, 65.89376034, 0.02385887, 65.89376034, 0.07157661, 46.12563223, -2054.03450658, 0.05, 2, 0, 74029, 23003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34074, 16.47344008, 4.381e-05, 49.42032025, 0.00013144, 164.73440084, 0.00043812, -16.47344008, -4.381e-05, -49.42032025, -0.00013144, -164.73440084, -0.00043812, 0.4, 0.3, 0.003, 0.0, 0.0, 14074, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4074, 99999, 'P', 44074, 'Vy', 34074, 'Vz', 24074, 'My', 14074, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174029, 74029, 174029, 4074, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123003, 123003, 23003, 4074, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172004, 17.8, 0.0, 6.7)
    ops.node(124030, 17.8, 0.0, 7.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4075, 172004, 124030, 0.0625, 31511334.20911921, 13129722.58713301, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24075, 47.06497623, 0.00104717, 56.59980083, 0.02856666, 5.65998008, 0.09295385, -47.06497623, -0.00104717, -56.59980083, -0.02856666, -5.65998008, -0.09295385, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14075, 47.06497623, 0.00104717, 56.59980083, 0.02856666, 5.65998008, 0.09295385, -47.06497623, -0.00104717, -56.59980083, -0.02856666, -5.65998008, -0.09295385, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24075, 4075, 0.0, 90.88663232, 0.02094343, 90.88663232, 0.06283029, 63.62064263, -2719.40844605, 0.05, 2, 0, 72004, 24030, 2, 3)
    ops.uniaxialMaterial('LimitState', 44075, 22.72165808, 5.316e-05, 68.16497424, 0.00015949, 227.21658081, 0.00053163, -22.72165808, -5.316e-05, -68.16497424, -0.00015949, -227.21658081, -0.00053163, 0.4, 0.3, 0.003, 0.0, 0.0, 24075, 2)
    ops.limitCurve('ThreePoint', 14075, 4075, 0.0, 90.88663232, 0.02094343, 90.88663232, 0.06283029, 63.62064263, -2719.40844605, 0.05, 2, 0, 72004, 24030, 1, 3)
    ops.uniaxialMaterial('LimitState', 34075, 22.72165808, 5.316e-05, 68.16497424, 0.00015949, 227.21658081, 0.00053163, -22.72165808, -5.316e-05, -68.16497424, -0.00015949, -227.21658081, -0.00053163, 0.4, 0.3, 0.003, 0.0, 0.0, 14075, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4075, 99999, 'P', 44075, 'Vy', 34075, 'Vz', 24075, 'My', 14075, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172004, 72004, 172004, 4075, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124030, 124030, 24030, 4075, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174030, 17.8, 0.0, 8.175)
    ops.node(123004, 17.8, 0.0, 9.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4076, 174030, 123004, 0.0625, 30731220.86119926, 12804675.35883303, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24076, 45.1908952, 0.00106456, 54.52256723, 0.0263937, 5.45225672, 0.08123633, -45.1908952, -0.00106456, -54.52256723, -0.0263937, -5.45225672, -0.08123633, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14076, 45.1908952, 0.00106456, 54.52256723, 0.0263937, 5.45225672, 0.08123633, -45.1908952, -0.00106456, -54.52256723, -0.0263937, -5.45225672, -0.08123633, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24076, 4076, 0.0, 85.77856015, 0.02129111, 85.77856015, 0.06387334, 60.04499211, -2718.05894712, 0.05, 2, 0, 74030, 23004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44076, 21.44464004, 5.145e-05, 64.33392012, 0.00015435, 214.44640039, 0.00051448, -21.44464004, -5.145e-05, -64.33392012, -0.00015435, -214.44640039, -0.00051448, 0.4, 0.3, 0.003, 0.0, 0.0, 24076, 2)
    ops.limitCurve('ThreePoint', 14076, 4076, 0.0, 85.77856015, 0.02129111, 85.77856015, 0.06387334, 60.04499211, -2718.05894712, 0.05, 2, 0, 74030, 23004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34076, 21.44464004, 5.145e-05, 64.33392012, 0.00015435, 214.44640039, 0.00051448, -21.44464004, -5.145e-05, -64.33392012, -0.00015435, -214.44640039, -0.00051448, 0.4, 0.3, 0.003, 0.0, 0.0, 14076, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4076, 99999, 'P', 44076, 'Vy', 34076, 'Vz', 24076, 'My', 14076, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174030, 74030, 174030, 4076, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123004, 123004, 23004, 4076, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173003, 14.8, 0.0, 9.9)
    ops.node(124031, 14.8, 0.0, 11.025)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4078, 173003, 124031, 0.0625, 27464014.03053401, 11443339.17938917, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24078, 41.88720695, 0.00105497, 51.12821896, 0.0220946, 5.1128219, 0.07356233, -41.88720695, -0.00105497, -51.12821896, -0.0220946, -5.1128219, -0.07356233, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14078, 41.88720695, 0.00105497, 51.12821896, 0.0220946, 5.1128219, 0.07356233, -41.88720695, -0.00105497, -51.12821896, -0.0220946, -5.1128219, -0.07356233, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24078, 4078, 0.0, 53.26062486, 0.02109932, 53.26062486, 0.06329796, 37.2824374, -2897.41293948, 0.05, 2, 0, 73003, 24031, 2, 3)
    ops.uniaxialMaterial('LimitState', 44078, 13.31515622, 3.574e-05, 39.94546865, 0.00010723, 133.15156215, 0.00035745, -13.31515622, -3.574e-05, -39.94546865, -0.00010723, -133.15156215, -0.00035745, 0.4, 0.3, 0.003, 0.0, 0.0, 24078, 2)
    ops.limitCurve('ThreePoint', 14078, 4078, 0.0, 53.26062486, 0.02109932, 53.26062486, 0.06329796, 37.2824374, -2897.41293948, 0.05, 2, 0, 73003, 24031, 1, 3)
    ops.uniaxialMaterial('LimitState', 34078, 13.31515622, 3.574e-05, 39.94546865, 0.00010723, 133.15156215, 0.00035745, -13.31515622, -3.574e-05, -39.94546865, -0.00010723, -133.15156215, -0.00035745, 0.4, 0.3, 0.003, 0.0, 0.0, 14078, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4078, 99999, 'P', 44078, 'Vy', 34078, 'Vz', 24078, 'My', 14078, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173003, 73003, 173003, 4078, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124031, 124031, 24031, 4078, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174031, 14.8, 0.0, 11.375)
    ops.node(124003, 14.8, 0.0, 12.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4079, 174031, 124003, 0.0625, 31394325.75117134, 13080969.06298806, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24079, 39.81122485, 0.00098889, 48.18977667, 0.02073917, 4.81897767, 0.0765882, -39.81122485, -0.00098889, -48.18977667, -0.02073917, -4.81897767, -0.0765882, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14079, 39.81122485, 0.00098889, 48.18977667, 0.02073917, 4.81897767, 0.0765882, -39.81122485, -0.00098889, -48.18977667, -0.02073917, -4.81897767, -0.0765882, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24079, 4079, 0.0, 53.53735298, 0.01977787, 53.53735298, 0.0593336, 37.47614708, -3922.40617049, 0.05, 2, 0, 74031, 24003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44079, 13.38433824, 3.143e-05, 40.15301473, 9.43e-05, 133.84338244, 0.00031432, -13.38433824, -3.143e-05, -40.15301473, -9.43e-05, -133.84338244, -0.00031432, 0.4, 0.3, 0.003, 0.0, 0.0, 24079, 2)
    ops.limitCurve('ThreePoint', 14079, 4079, 0.0, 53.53735298, 0.01977787, 53.53735298, 0.0593336, 37.47614708, -3922.40617049, 0.05, 2, 0, 74031, 24003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34079, 13.38433824, 3.143e-05, 40.15301473, 9.43e-05, 133.84338244, 0.00031432, -13.38433824, -3.143e-05, -40.15301473, -9.43e-05, -133.84338244, -0.00031432, 0.4, 0.3, 0.003, 0.0, 0.0, 14079, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4079, 99999, 'P', 44079, 'Vy', 34079, 'Vz', 24079, 'My', 14079, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174031, 74031, 174031, 4079, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124003, 124003, 24003, 4079, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173004, 17.8, 0.0, 9.9)
    ops.node(124032, 17.8, 0.0, 11.025)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4080, 173004, 124032, 0.0625, 30556854.34638626, 12732022.64432761, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24080, 39.37693629, 0.00104203, 47.71775335, 0.02232928, 4.77177534, 0.07568205, -39.37693629, -0.00104203, -47.71775335, -0.02232928, -4.77177534, -0.07568205, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14080, 39.37693629, 0.00104203, 47.71775335, 0.02232928, 4.77177534, 0.07568205, -39.37693629, -0.00104203, -47.71775335, -0.02232928, -4.77177534, -0.07568205, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24080, 4080, 0.0, 63.54082505, 0.02084067, 63.54082505, 0.062522, 44.47857754, -2845.10674049, 0.05, 2, 0, 73004, 24032, 2, 3)
    ops.uniaxialMaterial('LimitState', 44080, 15.88520626, 3.833e-05, 47.65561879, 0.00011498, 158.85206263, 0.00038328, -15.88520626, -3.833e-05, -47.65561879, -0.00011498, -158.85206263, -0.00038328, 0.4, 0.3, 0.003, 0.0, 0.0, 24080, 2)
    ops.limitCurve('ThreePoint', 14080, 4080, 0.0, 63.54082505, 0.02084067, 63.54082505, 0.062522, 44.47857754, -2845.10674049, 0.05, 2, 0, 73004, 24032, 1, 3)
    ops.uniaxialMaterial('LimitState', 34080, 15.88520626, 3.833e-05, 47.65561879, 0.00011498, 158.85206263, 0.00038328, -15.88520626, -3.833e-05, -47.65561879, -0.00011498, -158.85206263, -0.00038328, 0.4, 0.3, 0.003, 0.0, 0.0, 14080, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4080, 99999, 'P', 44080, 'Vy', 34080, 'Vz', 24080, 'My', 14080, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173004, 73004, 173004, 4080, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124032, 124032, 24032, 4080, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174032, 17.8, 0.0, 11.375)
    ops.node(124004, 17.8, 0.0, 12.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4081, 174032, 124004, 0.0625, 30862593.77642816, 12859414.07351173, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24081, 38.89585684, 0.00097282, 47.15867192, 0.02099147, 4.71586719, 0.07671473, -38.89585684, -0.00097282, -47.15867192, -0.02099147, -4.71586719, -0.07671473, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14081, 38.89585684, 0.00097282, 47.15867192, 0.02099147, 4.71586719, 0.07671473, -38.89585684, -0.00097282, -47.15867192, -0.02099147, -4.71586719, -0.07671473, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24081, 4081, 0.0, 52.05520299, 0.01945639, 52.05520299, 0.05836918, 36.4386421, -4120.7355937, 0.05, 2, 0, 74032, 24004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44081, 13.01380075, 3.109e-05, 39.04140224, 9.327e-05, 130.13800748, 0.00031089, -13.01380075, -3.109e-05, -39.04140224, -9.327e-05, -130.13800748, -0.00031089, 0.4, 0.3, 0.003, 0.0, 0.0, 24081, 2)
    ops.limitCurve('ThreePoint', 14081, 4081, 0.0, 52.05520299, 0.01945639, 52.05520299, 0.05836918, 36.4386421, -4120.7355937, 0.05, 2, 0, 74032, 24004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34081, 13.01380075, 3.109e-05, 39.04140224, 9.327e-05, 130.13800748, 0.00031089, -13.01380075, -3.109e-05, -39.04140224, -9.327e-05, -130.13800748, -0.00031089, 0.4, 0.3, 0.003, 0.0, 0.0, 14081, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4081, 99999, 'P', 44081, 'Vy', 34081, 'Vz', 24081, 'My', 14081, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174032, 74032, 174032, 4081, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124004, 124004, 24004, 4081, '-orient', 0, 0, 1, 0, 1, 0)
