import openseespy.opensees as ops


def add_columns() -> None:
    """Add components of all columns to ops domain (plastic hinges, column elements and nodes)
    """
    # Create elastic column element nodes
    ops.node(170001, 0.0, 0.0, 0.0)
    ops.node(121001, 0.0, 0.0, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1, 170001, 121001, 0.09, 26119670.70288791, 10883196.1262033, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20001, 59.84539419, 0.00119843, 72.5826198, 0.01535515, 7.25826198, 0.05420107, -59.84539419, -0.00119843, -72.5826198, -0.01535515, -7.25826198, -0.05420107, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10001, 55.35242325, 0.00119843, 67.13338505, 0.01535515, 6.71333851, 0.05420107, -55.35242325, -0.00119843, -67.13338505, -0.01535515, -6.71333851, -0.05420107, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20001, 1, 0.0, 93.74144078, 0.02396864, 93.74144078, 0.07190593, 65.61900855, -1284.87250931, 0.05, 2, 0, 70001, 21001, 2, 3)
    ops.uniaxialMaterial('LimitState', 40001, 23.43536019, 8.47e-05, 70.30608058, 0.0002541, 234.35360195, 0.00084699, -23.43536019, -8.47e-05, -70.30608058, -0.0002541, -234.35360195, -0.00084699, 0.4, 0.3, 0.003, 0.0, 0.0, 20001, 2)
    ops.limitCurve('ThreePoint', 10001, 1, 0.0, 93.74144078, 0.02396864, 93.74144078, 0.07190593, 65.61900855, -1284.87250931, 0.05, 2, 0, 70001, 21001, 1, 3)
    ops.uniaxialMaterial('LimitState', 30001, 23.43536019, 8.47e-05, 70.30608058, 0.0002541, 234.35360195, 0.00084699, -23.43536019, -8.47e-05, -70.30608058, -0.0002541, -234.35360195, -0.00084699, 0.4, 0.3, 0.003, 0.0, 0.0, 10001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1, 99999, 'P', 40001, 'Vy', 30001, 'Vz', 20001, 'My', 10001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170001, 70001, 170001, 1, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121001, 121001, 21001, 1, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170002, 3.85, 0.0, 0.0)
    ops.node(121002, 3.85, 0.0, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2, 170002, 121002, 0.16, 29572314.77056647, 12321797.82106936, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20002, 126.28271384, 0.00089245, 152.58835171, 0.02130806, 15.25883517, 0.06401847, -126.28271384, -0.00089245, -152.58835171, -0.02130806, -15.25883517, -0.06401847, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10002, 132.96320032, 0.00089245, 160.66043371, 0.02130806, 16.06604337, 0.06401847, -132.96320032, -0.00089245, -160.66043371, -0.02130806, -16.06604337, -0.06401847, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20002, 2, 0.0, 184.42000407, 0.01784891, 184.42000407, 0.05354673, 129.09400285, -2366.37919774, 0.05, 2, 0, 70002, 21002, 2, 3)
    ops.uniaxialMaterial('LimitState', 40002, 46.10500102, 8.279e-05, 138.31500305, 0.00024836, 461.05001018, 0.00082786, -46.10500102, -8.279e-05, -138.31500305, -0.00024836, -461.05001018, -0.00082786, 0.4, 0.3, 0.003, 0.0, 0.0, 20002, 2)
    ops.limitCurve('ThreePoint', 10002, 2, 0.0, 184.42000407, 0.01784891, 184.42000407, 0.05354673, 129.09400285, -2366.37919774, 0.05, 2, 0, 70002, 21002, 1, 3)
    ops.uniaxialMaterial('LimitState', 30002, 46.10500102, 8.279e-05, 138.31500305, 0.00024836, 461.05001018, 0.00082786, -46.10500102, -8.279e-05, -138.31500305, -0.00024836, -461.05001018, -0.00082786, 0.4, 0.3, 0.003, 0.0, 0.0, 10002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2, 99999, 'P', 40002, 'Vy', 30002, 'Vz', 20002, 'My', 10002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170002, 70002, 170002, 2, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121002, 121002, 21002, 2, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170003, 7.7, 0.0, 0.0)
    ops.node(121003, 7.7, 0.0, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3, 170003, 121003, 0.16, 29066308.54822284, 12110961.89509285, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20003, 126.79941026, 0.00086568, 153.35085593, 0.02014661, 15.33508559, 0.06221033, -126.79941026, -0.00086568, -153.35085593, -0.02014661, -15.33508559, -0.06221033, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10003, 134.01279932, 0.00086568, 162.0747087, 0.02014661, 16.20747087, 0.06221033, -134.01279932, -0.00086568, -162.0747087, -0.02014661, -16.20747087, -0.06221033, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20003, 3, 0.0, 176.65256142, 0.01731366, 176.65256142, 0.05194097, 123.65679299, -2184.51276865, 0.05, 2, 0, 70003, 21003, 2, 3)
    ops.uniaxialMaterial('LimitState', 40003, 44.16314035, 8.068e-05, 132.48942106, 0.00024204, 441.63140354, 0.0008068, -44.16314035, -8.068e-05, -132.48942106, -0.00024204, -441.63140354, -0.0008068, 0.4, 0.3, 0.003, 0.0, 0.0, 20003, 2)
    ops.limitCurve('ThreePoint', 10003, 3, 0.0, 176.65256142, 0.01731366, 176.65256142, 0.05194097, 123.65679299, -2184.51276865, 0.05, 2, 0, 70003, 21003, 1, 3)
    ops.uniaxialMaterial('LimitState', 30003, 44.16314035, 8.068e-05, 132.48942106, 0.00024204, 441.63140354, 0.0008068, -44.16314035, -8.068e-05, -132.48942106, -0.00024204, -441.63140354, -0.0008068, 0.4, 0.3, 0.003, 0.0, 0.0, 10003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3, 99999, 'P', 40003, 'Vy', 30003, 'Vz', 20003, 'My', 10003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170003, 70003, 170003, 3, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121003, 121003, 21003, 3, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170006, 18.45, 0.0, 0.0)
    ops.node(121006, 18.45, 0.0, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 6, 170006, 121006, 0.16, 28999916.03559846, 12083298.34816602, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20006, 129.25551443, 0.00092219, 156.33864211, 0.02257938, 15.63386421, 0.06455535, -129.25551443, -0.00092219, -156.33864211, -0.02257938, -15.63386421, -0.06455535, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10006, 136.29466314, 0.00092219, 164.85271562, 0.02257938, 16.48527156, 0.06455535, -136.29466314, -0.00092219, -164.85271562, -0.02257938, -16.48527156, -0.06455535, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20006, 6, 0.0, 186.33130261, 0.01844388, 186.33130261, 0.05533164, 130.43191182, -2532.27572341, 0.05, 2, 0, 70006, 21006, 2, 3)
    ops.uniaxialMaterial('LimitState', 40006, 46.58282565, 8.53e-05, 139.74847695, 0.00025589, 465.82825651, 0.00085295, -46.58282565, -8.53e-05, -139.74847695, -0.00025589, -465.82825651, -0.00085295, 0.4, 0.3, 0.003, 0.0, 0.0, 20006, 2)
    ops.limitCurve('ThreePoint', 10006, 6, 0.0, 186.33130261, 0.01844388, 186.33130261, 0.05533164, 130.43191182, -2532.27572341, 0.05, 2, 0, 70006, 21006, 1, 3)
    ops.uniaxialMaterial('LimitState', 30006, 46.58282565, 8.53e-05, 139.74847695, 0.00025589, 465.82825651, 0.00085295, -46.58282565, -8.53e-05, -139.74847695, -0.00025589, -465.82825651, -0.00085295, 0.4, 0.3, 0.003, 0.0, 0.0, 10006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 6, 99999, 'P', 40006, 'Vy', 30006, 'Vz', 20006, 'My', 10006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170006, 70006, 170006, 6, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121006, 121006, 21006, 6, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170007, 22.3, 0.0, 0.0)
    ops.node(121007, 22.3, 0.0, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 7, 170007, 121007, 0.16, 28588677.97429515, 11911949.15595631, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20007, 128.98558851, 0.00090761, 156.11380982, 0.0208669, 15.61138098, 0.06228379, -128.98558851, -0.00090761, -156.11380982, -0.0208669, -15.61138098, -0.06228379, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10007, 136.240507, 0.00090761, 164.89458121, 0.0208669, 16.48945812, 0.06228379, -136.240507, -0.00090761, -164.89458121, -0.0208669, -16.48945812, -0.06228379, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20007, 7, 0.0, 179.28294466, 0.0181523, 179.28294466, 0.0544569, 125.49806126, -2352.37672598, 0.05, 2, 0, 70007, 21007, 2, 3)
    ops.uniaxialMaterial('LimitState', 40007, 44.82073616, 8.325e-05, 134.46220849, 0.00024975, 448.20736164, 0.00083249, -44.82073616, -8.325e-05, -134.46220849, -0.00024975, -448.20736164, -0.00083249, 0.4, 0.3, 0.003, 0.0, 0.0, 20007, 2)
    ops.limitCurve('ThreePoint', 10007, 7, 0.0, 179.28294466, 0.0181523, 179.28294466, 0.0544569, 125.49806126, -2352.37672598, 0.05, 2, 0, 70007, 21007, 1, 3)
    ops.uniaxialMaterial('LimitState', 30007, 44.82073616, 8.325e-05, 134.46220849, 0.00024975, 448.20736164, 0.00083249, -44.82073616, -8.325e-05, -134.46220849, -0.00024975, -448.20736164, -0.00083249, 0.4, 0.3, 0.003, 0.0, 0.0, 10007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 7, 99999, 'P', 40007, 'Vy', 30007, 'Vz', 20007, 'My', 10007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170007, 70007, 170007, 7, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121007, 121007, 21007, 7, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170008, 26.15, 0.0, 0.0)
    ops.node(121008, 26.15, 0.0, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 8, 170008, 121008, 0.09, 27933934.44590719, 11639139.35246133, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20008, 62.75505796, 0.0011299, 75.99814485, 0.01948376, 7.59981449, 0.06158736, -62.75505796, -0.0011299, -75.99814485, -0.01948376, -7.59981449, -0.06158736, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10008, 57.52579026, 0.0011299, 69.66535421, 0.01948376, 6.96653542, 0.06158736, -57.52579026, -0.0011299, -69.66535421, -0.01948376, -6.96653542, -0.06158736, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20008, 8, 0.0, 108.55735174, 0.02259803, 108.55735174, 0.06779409, 75.99014622, -1647.8894168, 0.05, 2, 0, 70008, 21008, 2, 3)
    ops.uniaxialMaterial('LimitState', 40008, 27.13933793, 9.171e-05, 81.4180138, 0.00027514, 271.39337934, 0.00091715, -27.13933793, -9.171e-05, -81.4180138, -0.00027514, -271.39337934, -0.00091715, 0.4, 0.3, 0.003, 0.0, 0.0, 20008, 2)
    ops.limitCurve('ThreePoint', 10008, 8, 0.0, 108.55735174, 0.02259803, 108.55735174, 0.06779409, 75.99014622, -1647.8894168, 0.05, 2, 0, 70008, 21008, 1, 3)
    ops.uniaxialMaterial('LimitState', 30008, 27.13933793, 9.171e-05, 81.4180138, 0.00027514, 271.39337934, 0.00091715, -27.13933793, -9.171e-05, -81.4180138, -0.00027514, -271.39337934, -0.00091715, 0.4, 0.3, 0.003, 0.0, 0.0, 10008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 8, 99999, 'P', 40008, 'Vy', 30008, 'Vz', 20008, 'My', 10008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170008, 70008, 170008, 8, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121008, 121008, 21008, 8, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170009, 0.0, 4.8, 0.0)
    ops.node(121009, 0.0, 4.8, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 9, 170009, 121009, 0.16, 29891199.07830913, 12454666.28262881, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20009, 149.85791134, 0.0009203, 180.90256024, 0.02085712, 18.09025602, 0.06352995, -149.85791134, -0.0009203, -180.90256024, -0.02085712, -18.09025602, -0.06352995, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10009, 149.85791134, 0.0009203, 180.90256024, 0.02085712, 18.09025602, 0.06352995, -149.85791134, -0.0009203, -180.90256024, -0.02085712, -18.09025602, -0.06352995, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20009, 9, 0.0, 186.42124321, 0.01840606, 186.42124321, 0.05521818, 130.49487025, -2341.23520879, 0.05, 2, 0, 70009, 21009, 2, 3)
    ops.uniaxialMaterial('LimitState', 40009, 46.6053108, 8.279e-05, 139.81593241, 0.00024837, 466.05310804, 0.00082792, -46.6053108, -8.279e-05, -139.81593241, -0.00024837, -466.05310804, -0.00082792, 0.4, 0.3, 0.003, 0.0, 0.0, 20009, 2)
    ops.limitCurve('ThreePoint', 10009, 9, 0.0, 186.42124321, 0.01840606, 186.42124321, 0.05521818, 130.49487025, -2341.23520879, 0.05, 2, 0, 70009, 21009, 1, 3)
    ops.uniaxialMaterial('LimitState', 30009, 46.6053108, 8.279e-05, 139.81593241, 0.00024837, 466.05310804, 0.00082792, -46.6053108, -8.279e-05, -139.81593241, -0.00024837, -466.05310804, -0.00082792, 0.4, 0.3, 0.003, 0.0, 0.0, 10009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 9, 99999, 'P', 40009, 'Vy', 30009, 'Vz', 20009, 'My', 10009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170009, 70009, 170009, 9, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121009, 121009, 21009, 9, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170010, 3.85, 4.8, 0.0)
    ops.node(121010, 3.85, 4.8, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 10, 170010, 121010, 0.2025, 28440848.95627252, 11850353.73178022, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20010, 228.97055578, 0.00083713, 276.70231193, 0.03393039, 27.67023119, 0.0785047, -228.97055578, -0.00083713, -276.70231193, -0.03393039, -27.67023119, -0.0785047, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10010, 221.11890058, 0.00083713, 267.21388169, 0.03393039, 26.72138817, 0.0785047, -221.11890058, -0.00083713, -267.21388169, -0.03393039, -26.72138817, -0.0785047, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20010, 10, 0.0, 262.90397437, 0.01674263, 262.90397437, 0.0502279, 184.03278206, -4049.08921322, 0.05, 2, 0, 70010, 21010, 2, 3)
    ops.uniaxialMaterial('LimitState', 40010, 65.72599359, 9.696e-05, 197.17798078, 0.00029087, 657.25993594, 0.00096958, -65.72599359, -9.696e-05, -197.17798078, -0.00029087, -657.25993594, -0.00096958, 0.4, 0.3, 0.003, 0.0, 0.0, 20010, 2)
    ops.limitCurve('ThreePoint', 10010, 10, 0.0, 262.90397437, 0.01674263, 262.90397437, 0.0502279, 184.03278206, -4049.08921322, 0.05, 2, 0, 70010, 21010, 1, 3)
    ops.uniaxialMaterial('LimitState', 30010, 65.72599359, 9.696e-05, 197.17798078, 0.00029087, 657.25993594, 0.00096958, -65.72599359, -9.696e-05, -197.17798078, -0.00029087, -657.25993594, -0.00096958, 0.4, 0.3, 0.003, 0.0, 0.0, 10010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 10, 99999, 'P', 40010, 'Vy', 30010, 'Vz', 20010, 'My', 10010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170010, 70010, 170010, 10, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121010, 121010, 21010, 10, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170011, 7.7, 4.8, 0.0)
    ops.node(121011, 7.7, 4.8, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 11, 170011, 121011, 0.2025, 28275730.93428167, 11781554.55595069, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20011, 236.3262473, 0.00091031, 285.64833095, 0.03336319, 28.5648331, 0.07763651, -236.3262473, -0.00091031, -285.64833095, -0.03336319, -28.5648331, -0.07763651, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10011, 228.4857584, 0.00091031, 276.17150562, 0.03336319, 27.61715056, 0.07763651, -228.4857584, -0.00091031, -276.17150562, -0.03336319, -27.61715056, -0.07763651, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20011, 11, 0.0, 265.34579732, 0.01820629, 265.34579732, 0.05461887, 185.74205812, -4178.80169632, 0.05, 2, 0, 70011, 21011, 2, 3)
    ops.uniaxialMaterial('LimitState', 40011, 66.33644933, 9.843e-05, 199.00934799, 0.00029529, 663.3644933, 0.0009843, -66.33644933, -9.843e-05, -199.00934799, -0.00029529, -663.3644933, -0.0009843, 0.4, 0.3, 0.003, 0.0, 0.0, 20011, 2)
    ops.limitCurve('ThreePoint', 10011, 11, 0.0, 265.34579732, 0.01820629, 265.34579732, 0.05461887, 185.74205812, -4178.80169632, 0.05, 2, 0, 70011, 21011, 1, 3)
    ops.uniaxialMaterial('LimitState', 30011, 66.33644933, 9.843e-05, 199.00934799, 0.00029529, 663.3644933, 0.0009843, -66.33644933, -9.843e-05, -199.00934799, -0.00029529, -663.3644933, -0.0009843, 0.4, 0.3, 0.003, 0.0, 0.0, 10011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 11, 99999, 'P', 40011, 'Vy', 30011, 'Vz', 20011, 'My', 10011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170011, 70011, 170011, 11, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121011, 121011, 21011, 11, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170012, 11.55, 4.8, 0.0)
    ops.node(121012, 11.55, 4.8, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 12, 170012, 121012, 0.2025, 29899976.45938116, 12458323.52474215, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20012, 262.2012188, 0.00086164, 316.35657708, 0.02571437, 31.63565771, 0.07364776, -262.2012188, -0.00086164, -316.35657708, -0.02571437, -31.63565771, -0.07364776, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10012, 244.78599806, 0.00086164, 295.34439549, 0.02571437, 29.53443955, 0.07364776, -244.78599806, -0.00086164, -295.34439549, -0.02571437, -29.53443955, -0.07364776, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20012, 12, 0.0, 250.04280198, 0.01723283, 250.04280198, 0.05169848, 175.02996139, -3372.5455931, 0.05, 2, 0, 70012, 21012, 2, 3)
    ops.uniaxialMaterial('LimitState', 40012, 62.5107005, 8.771e-05, 187.53210149, 0.00026314, 625.10700496, 0.00087715, -62.5107005, -8.771e-05, -187.53210149, -0.00026314, -625.10700496, -0.00087715, 0.4, 0.3, 0.003, 0.0, 0.0, 20012, 2)
    ops.limitCurve('ThreePoint', 10012, 12, 0.0, 250.04280198, 0.01723283, 250.04280198, 0.05169848, 175.02996139, -3372.5455931, 0.05, 2, 0, 70012, 21012, 1, 3)
    ops.uniaxialMaterial('LimitState', 30012, 62.5107005, 8.771e-05, 187.53210149, 0.00026314, 625.10700496, 0.00087715, -62.5107005, -8.771e-05, -187.53210149, -0.00026314, -625.10700496, -0.00087715, 0.4, 0.3, 0.003, 0.0, 0.0, 10012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 12, 99999, 'P', 40012, 'Vy', 30012, 'Vz', 20012, 'My', 10012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170012, 70012, 170012, 12, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121012, 121012, 21012, 12, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170013, 14.6, 4.8, 0.0)
    ops.node(121013, 14.6, 4.8, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 13, 170013, 121013, 0.2025, 29480732.14386581, 12283638.39327742, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20013, 247.31359326, 0.00083088, 298.62220044, 0.02641683, 29.86222004, 0.07372353, -247.31359326, -0.00083088, -298.62220044, -0.02641683, -29.86222004, -0.07372353, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10013, 231.61083287, 0.00083088, 279.66168639, 0.02641683, 27.96616864, 0.07372353, -231.61083287, -0.00083088, -279.66168639, -0.02641683, -27.96616864, -0.07372353, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20013, 13, 0.0, 238.97667298, 0.0166176, 238.97667298, 0.04985281, 167.28367109, -3080.42902846, 0.05, 2, 0, 70013, 21013, 2, 3)
    ops.uniaxialMaterial('LimitState', 40013, 59.74416825, 8.503e-05, 179.23250474, 0.00025508, 597.44168246, 0.00085025, -59.74416825, -8.503e-05, -179.23250474, -0.00025508, -597.44168246, -0.00085025, 0.4, 0.3, 0.003, 0.0, 0.0, 20013, 2)
    ops.limitCurve('ThreePoint', 10013, 13, 0.0, 238.97667298, 0.0166176, 238.97667298, 0.04985281, 167.28367109, -3080.42902846, 0.05, 2, 0, 70013, 21013, 1, 3)
    ops.uniaxialMaterial('LimitState', 30013, 59.74416825, 8.503e-05, 179.23250474, 0.00025508, 597.44168246, 0.00085025, -59.74416825, -8.503e-05, -179.23250474, -0.00025508, -597.44168246, -0.00085025, 0.4, 0.3, 0.003, 0.0, 0.0, 10013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 13, 99999, 'P', 40013, 'Vy', 30013, 'Vz', 20013, 'My', 10013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170013, 70013, 170013, 13, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121013, 121013, 21013, 13, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170014, 18.45, 4.8, 0.0)
    ops.node(121014, 18.45, 4.8, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 14, 170014, 121014, 0.2025, 27468781.31711004, 11445325.54879585, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20014, 236.89538407, 0.00088873, 286.5667695, 0.03040346, 28.65667695, 0.07312343, -236.89538407, -0.00088873, -286.5667695, -0.03040346, -28.65667695, -0.07312343, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10014, 228.5745971, 0.00088873, 276.50130937, 0.03040346, 27.65013094, 0.07312343, -228.5745971, -0.00088873, -276.50130937, -0.03040346, -27.65013094, -0.07312343, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20014, 14, 0.0, 235.69083388, 0.01777461, 235.69083388, 0.05332384, 164.98358372, -3291.01140834, 0.05, 2, 0, 70014, 21014, 2, 3)
    ops.uniaxialMaterial('LimitState', 40014, 58.92270847, 9e-05, 176.76812541, 0.00026999, 589.22708471, 0.00089998, -58.92270847, -9e-05, -176.76812541, -0.00026999, -589.22708471, -0.00089998, 0.4, 0.3, 0.003, 0.0, 0.0, 20014, 2)
    ops.limitCurve('ThreePoint', 10014, 14, 0.0, 235.69083388, 0.01777461, 235.69083388, 0.05332384, 164.98358372, -3291.01140834, 0.05, 2, 0, 70014, 21014, 1, 3)
    ops.uniaxialMaterial('LimitState', 30014, 58.92270847, 9e-05, 176.76812541, 0.00026999, 589.22708471, 0.00089998, -58.92270847, -9e-05, -176.76812541, -0.00026999, -589.22708471, -0.00089998, 0.4, 0.3, 0.003, 0.0, 0.0, 10014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 14, 99999, 'P', 40014, 'Vy', 30014, 'Vz', 20014, 'My', 10014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170014, 70014, 170014, 14, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121014, 121014, 21014, 14, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170015, 22.3, 4.8, 0.0)
    ops.node(121015, 22.3, 4.8, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 15, 170015, 121015, 0.2025, 29411701.51323947, 12254875.63051645, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20015, 238.88933235, 0.00088577, 288.28485668, 0.03145783, 28.82848567, 0.0776936, -238.88933235, -0.00088577, -288.28485668, -0.03145783, -28.82848567, -0.0776936, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10015, 230.80677009, 0.00088577, 278.53105026, 0.03145783, 27.85310503, 0.0776936, -230.80677009, -0.00088577, -278.53105026, -0.03145783, -27.85310503, -0.0776936, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20015, 15, 0.0, 259.81006125, 0.01771539, 259.81006125, 0.05314618, 181.86704287, -3717.81245131, 0.05, 2, 0, 70015, 21015, 2, 3)
    ops.uniaxialMaterial('LimitState', 40015, 64.95251531, 9.265e-05, 194.85754594, 0.00027796, 649.52515312, 0.00092654, -64.95251531, -9.265e-05, -194.85754594, -0.00027796, -649.52515312, -0.00092654, 0.4, 0.3, 0.003, 0.0, 0.0, 20015, 2)
    ops.limitCurve('ThreePoint', 10015, 15, 0.0, 259.81006125, 0.01771539, 259.81006125, 0.05314618, 181.86704287, -3717.81245131, 0.05, 2, 0, 70015, 21015, 1, 3)
    ops.uniaxialMaterial('LimitState', 30015, 64.95251531, 9.265e-05, 194.85754594, 0.00027796, 649.52515312, 0.00092654, -64.95251531, -9.265e-05, -194.85754594, -0.00027796, -649.52515312, -0.00092654, 0.4, 0.3, 0.003, 0.0, 0.0, 10015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 15, 99999, 'P', 40015, 'Vy', 30015, 'Vz', 20015, 'My', 10015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170015, 70015, 170015, 15, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121015, 121015, 21015, 15, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170016, 26.15, 4.8, 0.0)
    ops.node(121016, 26.15, 4.8, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 16, 170016, 121016, 0.16, 27811112.37580542, 11587963.48991892, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20016, 142.89137573, 0.0009575, 173.05294049, 0.02273973, 17.30529405, 0.06251698, -142.89137573, -0.0009575, -173.05294049, -0.02273973, -17.30529405, -0.06251698, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10016, 142.89137573, 0.0009575, 173.05294049, 0.02273973, 17.30529405, 0.06251698, -142.89137573, -0.0009575, -173.05294049, -0.02273973, -17.30529405, -0.06251698, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20016, 16, 0.0, 186.10378341, 0.01914992, 186.10378341, 0.05744976, 130.27264838, -2681.86407322, 0.05, 2, 0, 70016, 21016, 2, 3)
    ops.uniaxialMaterial('LimitState', 40016, 46.52594585, 8.883e-05, 139.57783755, 0.0002665, 465.25945851, 0.00088832, -46.52594585, -8.883e-05, -139.57783755, -0.0002665, -465.25945851, -0.00088832, 0.4, 0.3, 0.003, 0.0, 0.0, 20016, 2)
    ops.limitCurve('ThreePoint', 10016, 16, 0.0, 186.10378341, 0.01914992, 186.10378341, 0.05744976, 130.27264838, -2681.86407322, 0.05, 2, 0, 70016, 21016, 1, 3)
    ops.uniaxialMaterial('LimitState', 30016, 46.52594585, 8.883e-05, 139.57783755, 0.0002665, 465.25945851, 0.00088832, -46.52594585, -8.883e-05, -139.57783755, -0.0002665, -465.25945851, -0.00088832, 0.4, 0.3, 0.003, 0.0, 0.0, 10016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 16, 99999, 'P', 40016, 'Vy', 30016, 'Vz', 20016, 'My', 10016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170016, 70016, 170016, 16, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121016, 121016, 21016, 16, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170017, 0.0, 9.6, 0.0)
    ops.node(121017, 0.0, 9.6, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 17, 170017, 121017, 0.16, 30777085.77421134, 12823785.73925472, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20017, 129.88582237, 0.00083938, 156.5082212, 0.01985951, 15.65082212, 0.06364142, -129.88582237, -0.00083938, -156.5082212, -0.01985951, -15.65082212, -0.06364142, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10017, 137.39489328, 0.00083938, 165.55640913, 0.01985951, 16.55564091, 0.06364142, -137.39489328, -0.00083938, -165.55640913, -0.01985951, -16.55564091, -0.06364142, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20017, 17, 0.0, 189.68408528, 0.01678756, 189.68408528, 0.05036268, 132.7788597, -2310.62439214, 0.05, 2, 0, 70017, 21017, 2, 3)
    ops.uniaxialMaterial('LimitState', 40017, 47.42102132, 8.182e-05, 142.26306396, 0.00024545, 474.2102132, 0.00081816, -47.42102132, -8.182e-05, -142.26306396, -0.00024545, -474.2102132, -0.00081816, 0.4, 0.3, 0.003, 0.0, 0.0, 20017, 2)
    ops.limitCurve('ThreePoint', 10017, 17, 0.0, 189.68408528, 0.01678756, 189.68408528, 0.05036268, 132.7788597, -2310.62439214, 0.05, 2, 0, 70017, 21017, 1, 3)
    ops.uniaxialMaterial('LimitState', 30017, 47.42102132, 8.182e-05, 142.26306396, 0.00024545, 474.2102132, 0.00081816, -47.42102132, -8.182e-05, -142.26306396, -0.00024545, -474.2102132, -0.00081816, 0.4, 0.3, 0.003, 0.0, 0.0, 10017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 17, 99999, 'P', 40017, 'Vy', 30017, 'Vz', 20017, 'My', 10017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170017, 70017, 170017, 17, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121017, 121017, 21017, 17, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170018, 3.85, 9.6, 0.0)
    ops.node(121018, 3.85, 9.6, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 18, 170018, 121018, 0.2025, 31267157.87698254, 13027982.44874272, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20018, 201.00424287, 0.00083512, 241.68718112, 0.03201033, 24.16871811, 0.08106433, -201.00424287, -0.00083512, -241.68718112, -0.03201033, -24.16871811, -0.08106433, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10018, 209.06195516, 0.00083512, 251.37576152, 0.03201033, 25.13757615, 0.08106433, -209.06195516, -0.00083512, -251.37576152, -0.03201033, -25.13757615, -0.08106433, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20018, 18, 0.0, 281.68576084, 0.0167024, 281.68576084, 0.0501072, 197.18003259, -4107.81126039, 0.05, 2, 0, 70018, 21018, 2, 3)
    ops.uniaxialMaterial('LimitState', 40018, 70.42144021, 9.449e-05, 211.26432063, 0.00028348, 704.21440211, 0.00094494, -70.42144021, -9.449e-05, -211.26432063, -0.00028348, -704.21440211, -0.00094494, 0.4, 0.3, 0.003, 0.0, 0.0, 20018, 2)
    ops.limitCurve('ThreePoint', 10018, 18, 0.0, 281.68576084, 0.0167024, 281.68576084, 0.0501072, 197.18003259, -4107.81126039, 0.05, 2, 0, 70018, 21018, 1, 3)
    ops.uniaxialMaterial('LimitState', 30018, 70.42144021, 9.449e-05, 211.26432063, 0.00028348, 704.21440211, 0.00094494, -70.42144021, -9.449e-05, -211.26432063, -0.00028348, -704.21440211, -0.00094494, 0.4, 0.3, 0.003, 0.0, 0.0, 10018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 18, 99999, 'P', 40018, 'Vy', 30018, 'Vz', 20018, 'My', 10018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170018, 70018, 170018, 18, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121018, 121018, 21018, 18, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170019, 7.7, 9.6, 0.0)
    ops.node(121019, 7.7, 9.6, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 19, 170019, 121019, 0.2025, 29326258.13271105, 12219274.22196294, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20019, 204.12528653, 0.00087984, 246.38865647, 0.03267955, 24.63886565, 0.07889876, -204.12528653, -0.00087984, -246.38865647, -0.03267955, -24.63886565, -0.07889876, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10019, 212.51756214, 0.00087984, 256.51852105, 0.03267955, 25.65185211, 0.07889876, -212.51756214, -0.00087984, -256.51852105, -0.03267955, -25.65185211, -0.07889876, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20019, 19, 0.0, 268.47681156, 0.01759671, 268.47681156, 0.05279014, 187.93376809, -4070.60844166, 0.05, 2, 0, 70019, 21019, 2, 3)
    ops.uniaxialMaterial('LimitState', 40019, 67.11920289, 9.602e-05, 201.35760867, 0.00028807, 671.19202889, 0.00096024, -67.11920289, -9.602e-05, -201.35760867, -0.00028807, -671.19202889, -0.00096024, 0.4, 0.3, 0.003, 0.0, 0.0, 20019, 2)
    ops.limitCurve('ThreePoint', 10019, 19, 0.0, 268.47681156, 0.01759671, 268.47681156, 0.05279014, 187.93376809, -4070.60844166, 0.05, 2, 0, 70019, 21019, 1, 3)
    ops.uniaxialMaterial('LimitState', 30019, 67.11920289, 9.602e-05, 201.35760867, 0.00028807, 671.19202889, 0.00096024, -67.11920289, -9.602e-05, -201.35760867, -0.00028807, -671.19202889, -0.00096024, 0.4, 0.3, 0.003, 0.0, 0.0, 10019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 19, 99999, 'P', 40019, 'Vy', 30019, 'Vz', 20019, 'My', 10019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170019, 70019, 170019, 19, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121019, 121019, 21019, 19, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170020, 11.55, 9.6, 0.0)
    ops.node(121020, 11.55, 9.6, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 20, 170020, 121020, 0.16, 31207483.07457853, 13003117.94774106, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20020, 153.82254173, 0.00086702, 184.78077691, 0.02159012, 18.47807769, 0.06319129, -153.82254173, -0.00086702, -184.78077691, -0.02159012, -18.47807769, -0.06319129, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10020, 153.82254173, 0.00086702, 184.78077691, 0.02159012, 18.47807769, 0.06319129, -153.82254173, -0.00086702, -184.78077691, -0.02159012, -18.47807769, -0.06319129, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20020, 20, 0.0, 206.37416864, 0.01734039, 206.37416864, 0.05202117, 144.46191805, -2545.95175629, 0.05, 2, 0, 70020, 21020, 2, 3)
    ops.uniaxialMaterial('LimitState', 40020, 51.59354216, 8.779e-05, 154.78062648, 0.00026336, 515.93542161, 0.00087787, -51.59354216, -8.779e-05, -154.78062648, -0.00026336, -515.93542161, -0.00087787, 0.4, 0.3, 0.003, 0.0, 0.0, 20020, 2)
    ops.limitCurve('ThreePoint', 10020, 20, 0.0, 206.37416864, 0.01734039, 206.37416864, 0.05202117, 144.46191805, -2545.95175629, 0.05, 2, 0, 70020, 21020, 1, 3)
    ops.uniaxialMaterial('LimitState', 30020, 51.59354216, 8.779e-05, 154.78062648, 0.00026336, 515.93542161, 0.00087787, -51.59354216, -8.779e-05, -154.78062648, -0.00026336, -515.93542161, -0.00087787, 0.4, 0.3, 0.003, 0.0, 0.0, 10020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 20, 99999, 'P', 40020, 'Vy', 30020, 'Vz', 20020, 'My', 10020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170020, 70020, 170020, 20, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121020, 121020, 21020, 20, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170021, 14.6, 9.6, 0.0)
    ops.node(121021, 14.6, 9.6, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 21, 170021, 121021, 0.16, 26974783.30074484, 11239493.04197701, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20021, 162.41896586, 0.00092803, 196.21880889, 0.01955133, 19.62188089, 0.05438177, -162.41896586, -0.00092803, -196.21880889, -0.01955133, -19.62188089, -0.05438177, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10021, 162.41896586, 0.00092803, 196.21880889, 0.01955133, 19.62188089, 0.05438177, -162.41896586, -0.00092803, -196.21880889, -0.01955133, -19.62188089, -0.05438177, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20021, 21, 0.0, 177.65100658, 0.01856062, 177.65100658, 0.05568185, 124.3557046, -2302.6339297, 0.05, 2, 0, 70021, 21021, 2, 3)
    ops.uniaxialMaterial('LimitState', 40021, 44.41275164, 8.743e-05, 133.23825493, 0.00026228, 444.12751645, 0.00087427, -44.41275164, -8.743e-05, -133.23825493, -0.00026228, -444.12751645, -0.00087427, 0.4, 0.3, 0.003, 0.0, 0.0, 20021, 2)
    ops.limitCurve('ThreePoint', 10021, 21, 0.0, 177.65100658, 0.01856062, 177.65100658, 0.05568185, 124.3557046, -2302.6339297, 0.05, 2, 0, 70021, 21021, 1, 3)
    ops.uniaxialMaterial('LimitState', 30021, 44.41275164, 8.743e-05, 133.23825493, 0.00026228, 444.12751645, 0.00087427, -44.41275164, -8.743e-05, -133.23825493, -0.00026228, -444.12751645, -0.00087427, 0.4, 0.3, 0.003, 0.0, 0.0, 10021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 21, 99999, 'P', 40021, 'Vy', 30021, 'Vz', 20021, 'My', 10021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170021, 70021, 170021, 21, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121021, 121021, 21021, 21, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170022, 18.45, 9.6, 0.0)
    ops.node(121022, 18.45, 9.6, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 22, 170022, 121022, 0.2025, 29374857.33694636, 12239523.89039432, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20022, 200.60027604, 0.0008661, 242.11469603, 0.03076048, 24.2114696, 0.07705849, -200.60027604, -0.0008661, -242.11469603, -0.03076048, -24.2114696, -0.07705849, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10022, 208.66739443, 0.0008661, 251.85131232, 0.03076048, 25.18513123, 0.07705849, -208.66739443, -0.0008661, -251.85131232, -0.03076048, -25.18513123, -0.07705849, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20022, 22, 0.0, 258.46516894, 0.01732201, 258.46516894, 0.05196602, 180.92561826, -3692.01733808, 0.05, 2, 0, 70022, 21022, 2, 3)
    ops.uniaxialMaterial('LimitState', 40022, 64.61629224, 9.229e-05, 193.84887671, 0.00027687, 646.16292235, 0.0009229, -64.61629224, -9.229e-05, -193.84887671, -0.00027687, -646.16292235, -0.0009229, 0.4, 0.3, 0.003, 0.0, 0.0, 20022, 2)
    ops.limitCurve('ThreePoint', 10022, 22, 0.0, 258.46516894, 0.01732201, 258.46516894, 0.05196602, 180.92561826, -3692.01733808, 0.05, 2, 0, 70022, 21022, 1, 3)
    ops.uniaxialMaterial('LimitState', 30022, 64.61629224, 9.229e-05, 193.84887671, 0.00027687, 646.16292235, 0.0009229, -64.61629224, -9.229e-05, -193.84887671, -0.00027687, -646.16292235, -0.0009229, 0.4, 0.3, 0.003, 0.0, 0.0, 10022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 22, 99999, 'P', 40022, 'Vy', 30022, 'Vz', 20022, 'My', 10022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170022, 70022, 170022, 22, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121022, 121022, 21022, 22, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170023, 22.3, 9.6, 0.0)
    ops.node(121023, 22.3, 9.6, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 23, 170023, 121023, 0.2025, 26806364.07744209, 11169318.36560087, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20023, 202.23688262, 0.00090173, 244.77845153, 0.02931821, 24.47784515, 0.07080347, -202.23688262, -0.00090173, -244.77845153, -0.02931821, -24.47784515, -0.07080347, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10023, 210.81459833, 0.00090173, 255.16053388, 0.02931821, 25.51605339, 0.07080347, -210.81459833, -0.00090173, -255.16053388, -0.02931821, -25.51605339, -0.07080347, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20023, 23, 0.0, 236.51496005, 0.01803458, 236.51496005, 0.05410374, 165.56047204, -3465.50016901, 0.05, 2, 0, 70023, 21023, 2, 3)
    ops.uniaxialMaterial('LimitState', 40023, 59.12874001, 9.254e-05, 177.38622004, 0.00027763, 591.28740013, 0.00092544, -59.12874001, -9.254e-05, -177.38622004, -0.00027763, -591.28740013, -0.00092544, 0.4, 0.3, 0.003, 0.0, 0.0, 20023, 2)
    ops.limitCurve('ThreePoint', 10023, 23, 0.0, 236.51496005, 0.01803458, 236.51496005, 0.05410374, 165.56047204, -3465.50016901, 0.05, 2, 0, 70023, 21023, 1, 3)
    ops.uniaxialMaterial('LimitState', 30023, 59.12874001, 9.254e-05, 177.38622004, 0.00027763, 591.28740013, 0.00092544, -59.12874001, -9.254e-05, -177.38622004, -0.00027763, -591.28740013, -0.00092544, 0.4, 0.3, 0.003, 0.0, 0.0, 10023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 23, 99999, 'P', 40023, 'Vy', 30023, 'Vz', 20023, 'My', 10023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170023, 70023, 170023, 23, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121023, 121023, 21023, 23, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170024, 26.15, 9.6, 0.0)
    ops.node(121024, 26.15, 9.6, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 24, 170024, 121024, 0.16, 29034381.50609666, 12097658.96087361, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20024, 129.49383464, 0.00089744, 156.57111041, 0.02139969, 15.65711104, 0.06304875, -129.49383464, -0.00089744, -156.57111041, -0.02139969, -15.65711104, -0.06304875, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10024, 136.60432421, 0.00089744, 165.16840965, 0.02139969, 16.51684097, 0.06304875, -136.60432421, -0.00089744, -165.16840965, -0.02139969, -16.51684097, -0.06304875, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20024, 24, 0.0, 184.12791485, 0.01794871, 184.12791485, 0.05384613, 128.88954039, -2412.86296996, 0.05, 2, 0, 70024, 21024, 2, 3)
    ops.uniaxialMaterial('LimitState', 40024, 46.03197871, 8.419e-05, 138.09593614, 0.00025256, 460.31978712, 0.00084186, -46.03197871, -8.419e-05, -138.09593614, -0.00025256, -460.31978712, -0.00084186, 0.4, 0.3, 0.003, 0.0, 0.0, 20024, 2)
    ops.limitCurve('ThreePoint', 10024, 24, 0.0, 184.12791485, 0.01794871, 184.12791485, 0.05384613, 128.88954039, -2412.86296996, 0.05, 2, 0, 70024, 21024, 1, 3)
    ops.uniaxialMaterial('LimitState', 30024, 46.03197871, 8.419e-05, 138.09593614, 0.00025256, 460.31978712, 0.00084186, -46.03197871, -8.419e-05, -138.09593614, -0.00025256, -460.31978712, -0.00084186, 0.4, 0.3, 0.003, 0.0, 0.0, 10024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 24, 99999, 'P', 40024, 'Vy', 30024, 'Vz', 20024, 'My', 10024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170024, 70024, 170024, 24, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121024, 121024, 21024, 24, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170025, 0.0, 14.4, 0.0)
    ops.node(121025, 0.0, 14.4, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 25, 170025, 121025, 0.09, 27146703.3221064, 11311126.384211, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20025, 58.44895786, 0.00113552, 70.84165043, 0.01963544, 7.08416504, 0.06040931, -58.44895786, -0.00113552, -70.84165043, -0.01963544, -7.08416504, -0.06040931, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10025, 54.15095562, 0.00113552, 65.63236041, 0.01963544, 6.56323604, 0.06040931, -54.15095562, -0.00113552, -65.63236041, -0.01963544, -6.56323604, -0.06040931, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20025, 25, 0.0, 106.8677732, 0.02271042, 106.8677732, 0.06813126, 74.80744124, -1662.55267235, 0.05, 2, 0, 70025, 21025, 2, 3)
    ops.uniaxialMaterial('LimitState', 40025, 26.7169433, 9.291e-05, 80.1508299, 0.00027872, 267.16943299, 0.00092906, -26.7169433, -9.291e-05, -80.1508299, -0.00027872, -267.16943299, -0.00092906, 0.4, 0.3, 0.003, 0.0, 0.0, 20025, 2)
    ops.limitCurve('ThreePoint', 10025, 25, 0.0, 106.8677732, 0.02271042, 106.8677732, 0.06813126, 74.80744124, -1662.55267235, 0.05, 2, 0, 70025, 21025, 1, 3)
    ops.uniaxialMaterial('LimitState', 30025, 26.7169433, 9.291e-05, 80.1508299, 0.00027872, 267.16943299, 0.00092906, -26.7169433, -9.291e-05, -80.1508299, -0.00027872, -267.16943299, -0.00092906, 0.4, 0.3, 0.003, 0.0, 0.0, 10025, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 25, 99999, 'P', 40025, 'Vy', 30025, 'Vz', 20025, 'My', 10025, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170025, 70025, 170025, 25, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121025, 121025, 21025, 25, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170026, 3.85, 14.4, 0.0)
    ops.node(121026, 3.85, 14.4, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 26, 170026, 121026, 0.16, 27411289.06153249, 11421370.4423052, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20026, 145.67525964, 0.00094581, 176.57797821, 0.02329249, 17.65779782, 0.06295028, -145.67525964, -0.00094581, -176.57797821, -0.02329249, -17.65779782, -0.06295028, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10026, 145.67525964, 0.00094581, 176.57797821, 0.02329249, 17.65779782, 0.06295028, -145.67525964, -0.00094581, -176.57797821, -0.02329249, -17.65779782, -0.06295028, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20026, 26, 0.0, 182.18023567, 0.0189161, 182.18023567, 0.05674831, 127.52616497, -2655.15006636, 0.05, 2, 0, 70026, 21026, 2, 3)
    ops.uniaxialMaterial('LimitState', 40026, 45.54505892, 8.823e-05, 136.63517675, 0.00026468, 455.45058917, 0.00088228, -45.54505892, -8.823e-05, -136.63517675, -0.00026468, -455.45058917, -0.00088228, 0.4, 0.3, 0.003, 0.0, 0.0, 20026, 2)
    ops.limitCurve('ThreePoint', 10026, 26, 0.0, 182.18023567, 0.0189161, 182.18023567, 0.05674831, 127.52616497, -2655.15006636, 0.05, 2, 0, 70026, 21026, 1, 3)
    ops.uniaxialMaterial('LimitState', 30026, 45.54505892, 8.823e-05, 136.63517675, 0.00026468, 455.45058917, 0.00088228, -45.54505892, -8.823e-05, -136.63517675, -0.00026468, -455.45058917, -0.00088228, 0.4, 0.3, 0.003, 0.0, 0.0, 10026, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 26, 99999, 'P', 40026, 'Vy', 30026, 'Vz', 20026, 'My', 10026, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170026, 70026, 170026, 26, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121026, 121026, 21026, 26, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170027, 7.7, 14.4, 0.0)
    ops.node(121027, 7.7, 14.4, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 27, 170027, 121027, 0.16, 29786223.56417813, 12410926.48507422, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20027, 147.08489307, 0.0008938, 177.65101688, 0.02255126, 17.76510169, 0.0655237, -147.08489307, -0.0008938, -177.65101688, -0.02255126, -17.76510169, -0.0655237, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10027, 147.08489307, 0.0008938, 177.65101688, 0.02255126, 17.76510169, 0.0655237, -147.08489307, -0.0008938, -177.65101688, -0.02255126, -17.76510169, -0.0655237, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20027, 27, 0.0, 193.69301892, 0.01787593, 193.69301892, 0.05362779, 135.58511324, -2662.07487922, 0.05, 2, 0, 70027, 21027, 2, 3)
    ops.uniaxialMaterial('LimitState', 40027, 48.42325473, 8.632e-05, 145.26976419, 0.00025897, 484.23254729, 0.00086324, -48.42325473, -8.632e-05, -145.26976419, -0.00025897, -484.23254729, -0.00086324, 0.4, 0.3, 0.003, 0.0, 0.0, 20027, 2)
    ops.limitCurve('ThreePoint', 10027, 27, 0.0, 193.69301892, 0.01787593, 193.69301892, 0.05362779, 135.58511324, -2662.07487922, 0.05, 2, 0, 70027, 21027, 1, 3)
    ops.uniaxialMaterial('LimitState', 30027, 48.42325473, 8.632e-05, 145.26976419, 0.00025897, 484.23254729, 0.00086324, -48.42325473, -8.632e-05, -145.26976419, -0.00025897, -484.23254729, -0.00086324, 0.4, 0.3, 0.003, 0.0, 0.0, 10027, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 27, 99999, 'P', 40027, 'Vy', 30027, 'Vz', 20027, 'My', 10027, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170027, 70027, 170027, 27, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121027, 121027, 21027, 27, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170028, 11.55, 14.4, 0.0)
    ops.node(121028, 11.55, 14.4, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 28, 170028, 121028, 0.1225, 28056698.06312323, 11690290.85963468, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20028, 94.87091262, 0.00098378, 114.72673621, 0.01469557, 11.47267362, 0.05095906, -94.87091262, -0.00098378, -114.72673621, -0.01469557, -11.47267362, -0.05095906, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10028, 94.87091262, 0.00098378, 114.72673621, 0.01469557, 11.47267362, 0.05095906, -94.87091262, -0.00098378, -114.72673621, -0.01469557, -11.47267362, -0.05095906, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20028, 28, 0.0, 128.94301366, 0.0196756, 128.94301366, 0.05902681, 90.26010956, -1504.82353726, 0.05, 2, 0, 70028, 21028, 2, 3)
    ops.uniaxialMaterial('LimitState', 40028, 32.23575342, 7.969e-05, 96.70726025, 0.00023906, 322.35753415, 0.00079686, -32.23575342, -7.969e-05, -96.70726025, -0.00023906, -322.35753415, -0.00079686, 0.4, 0.3, 0.003, 0.0, 0.0, 20028, 2)
    ops.limitCurve('ThreePoint', 10028, 28, 0.0, 128.94301366, 0.0196756, 128.94301366, 0.05902681, 90.26010956, -1504.82353726, 0.05, 2, 0, 70028, 21028, 1, 3)
    ops.uniaxialMaterial('LimitState', 30028, 32.23575342, 7.969e-05, 96.70726025, 0.00023906, 322.35753415, 0.00079686, -32.23575342, -7.969e-05, -96.70726025, -0.00023906, -322.35753415, -0.00079686, 0.4, 0.3, 0.003, 0.0, 0.0, 10028, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 28, 99999, 'P', 40028, 'Vy', 30028, 'Vz', 20028, 'My', 10028, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170028, 70028, 170028, 28, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121028, 121028, 21028, 28, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170029, 14.6, 14.4, 0.0)
    ops.node(121029, 14.6, 14.4, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 29, 170029, 121029, 0.1225, 27242382.07450357, 11350992.53104316, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20029, 91.92492644, 0.00102272, 111.24832444, 0.01870475, 11.12483244, 0.05366583, -91.92492644, -0.00102272, -111.24832444, -0.01870475, -11.12483244, -0.05366583, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10029, 91.92492644, 0.00102272, 111.24832444, 0.01870475, 11.12483244, 0.05366583, -91.92492644, -0.00102272, -111.24832444, -0.01870475, -11.12483244, -0.05366583, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20029, 29, 0.0, 139.06590211, 0.02045434, 139.06590211, 0.06136302, 97.34613147, -1916.20526352, 0.05, 2, 0, 70029, 21029, 2, 3)
    ops.uniaxialMaterial('LimitState', 40029, 34.76647553, 8.851e-05, 104.29942658, 0.00026553, 347.66475527, 0.0008851, -34.76647553, -8.851e-05, -104.29942658, -0.00026553, -347.66475527, -0.0008851, 0.4, 0.3, 0.003, 0.0, 0.0, 20029, 2)
    ops.limitCurve('ThreePoint', 10029, 29, 0.0, 139.06590211, 0.02045434, 139.06590211, 0.06136302, 97.34613147, -1916.20526352, 0.05, 2, 0, 70029, 21029, 1, 3)
    ops.uniaxialMaterial('LimitState', 30029, 34.76647553, 8.851e-05, 104.29942658, 0.00026553, 347.66475527, 0.0008851, -34.76647553, -8.851e-05, -104.29942658, -0.00026553, -347.66475527, -0.0008851, 0.4, 0.3, 0.003, 0.0, 0.0, 10029, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 29, 99999, 'P', 40029, 'Vy', 30029, 'Vz', 20029, 'My', 10029, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170029, 70029, 170029, 29, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121029, 121029, 21029, 29, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170030, 18.45, 14.4, 0.0)
    ops.node(121030, 18.45, 14.4, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 30, 170030, 121030, 0.16, 28024539.16208893, 11676891.31753705, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20030, 139.60393803, 0.00087638, 169.0984374, 0.02101915, 16.90984374, 0.06162362, -139.60393803, -0.00087638, -169.0984374, -0.02101915, -16.90984374, -0.06162362, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10030, 139.60393803, 0.00087638, 169.0984374, 0.02101915, 16.90984374, 0.06162362, -139.60393803, -0.00087638, -169.0984374, -0.02101915, -16.90984374, -0.06162362, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20030, 30, 0.0, 176.93379623, 0.01752764, 176.93379623, 0.05258291, 123.85365736, -2363.71340061, 0.05, 2, 0, 70030, 21030, 2, 3)
    ops.uniaxialMaterial('LimitState', 40030, 44.23344906, 8.381e-05, 132.70034717, 0.00025144, 442.33449057, 0.00083812, -44.23344906, -8.381e-05, -132.70034717, -0.00025144, -442.33449057, -0.00083812, 0.4, 0.3, 0.003, 0.0, 0.0, 20030, 2)
    ops.limitCurve('ThreePoint', 10030, 30, 0.0, 176.93379623, 0.01752764, 176.93379623, 0.05258291, 123.85365736, -2363.71340061, 0.05, 2, 0, 70030, 21030, 1, 3)
    ops.uniaxialMaterial('LimitState', 30030, 44.23344906, 8.381e-05, 132.70034717, 0.00025144, 442.33449057, 0.00083812, -44.23344906, -8.381e-05, -132.70034717, -0.00025144, -442.33449057, -0.00083812, 0.4, 0.3, 0.003, 0.0, 0.0, 10030, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 30, 99999, 'P', 40030, 'Vy', 30030, 'Vz', 20030, 'My', 10030, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170030, 70030, 170030, 30, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121030, 121030, 21030, 30, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170031, 22.3, 14.4, 0.0)
    ops.node(121031, 22.3, 14.4, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 31, 170031, 121031, 0.16, 28680077.64586187, 11950032.35244245, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20031, 138.78671066, 0.00092788, 167.95292508, 0.0217908, 16.79529251, 0.06333431, -138.78671066, -0.00092788, -167.95292508, -0.0217908, -16.79529251, -0.06333431, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10031, 138.78671066, 0.00092788, 167.95292508, 0.0217908, 16.79529251, 0.06333431, -138.78671066, -0.00092788, -167.95292508, -0.0217908, -16.79529251, -0.06333431, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20031, 31, 0.0, 184.84272079, 0.01855767, 184.84272079, 0.05567301, 129.38990456, -2533.85699104, 0.05, 2, 0, 70031, 21031, 2, 3)
    ops.uniaxialMaterial('LimitState', 40031, 46.2106802, 8.556e-05, 138.63204059, 0.00025667, 462.10680198, 0.00085557, -46.2106802, -8.556e-05, -138.63204059, -0.00025667, -462.10680198, -0.00085557, 0.4, 0.3, 0.003, 0.0, 0.0, 20031, 2)
    ops.limitCurve('ThreePoint', 10031, 31, 0.0, 184.84272079, 0.01855767, 184.84272079, 0.05567301, 129.38990456, -2533.85699104, 0.05, 2, 0, 70031, 21031, 1, 3)
    ops.uniaxialMaterial('LimitState', 30031, 46.2106802, 8.556e-05, 138.63204059, 0.00025667, 462.10680198, 0.00085557, -46.2106802, -8.556e-05, -138.63204059, -0.00025667, -462.10680198, -0.00085557, 0.4, 0.3, 0.003, 0.0, 0.0, 10031, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 31, 99999, 'P', 40031, 'Vy', 30031, 'Vz', 20031, 'My', 10031, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170031, 70031, 170031, 31, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121031, 121031, 21031, 31, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170032, 26.15, 14.4, 0.0)
    ops.node(121032, 26.15, 14.4, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 32, 170032, 121032, 0.09, 29209679.05183822, 12170699.60493259, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20032, 60.66492519, 0.00114486, 73.32996209, 0.01914196, 7.33299621, 0.06315695, -60.66492519, -0.00114486, -73.32996209, -0.01914196, -7.33299621, -0.06315695, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10032, 56.17025991, 0.00114486, 67.89694403, 0.01914196, 6.7896944, 0.06315695, -56.17025991, -0.00114486, -67.89694403, -0.01914196, -6.7896944, -0.06315695, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20032, 32, 0.0, 110.72889978, 0.02289728, 110.72889978, 0.06869185, 77.51022984, -1600.25546492, 0.05, 2, 0, 70032, 21032, 2, 3)
    ops.uniaxialMaterial('LimitState', 40032, 27.68222494, 8.946e-05, 83.04667483, 0.00026839, 276.82224944, 0.00089464, -27.68222494, -8.946e-05, -83.04667483, -0.00026839, -276.82224944, -0.00089464, 0.4, 0.3, 0.003, 0.0, 0.0, 20032, 2)
    ops.limitCurve('ThreePoint', 10032, 32, 0.0, 110.72889978, 0.02289728, 110.72889978, 0.06869185, 77.51022984, -1600.25546492, 0.05, 2, 0, 70032, 21032, 1, 3)
    ops.uniaxialMaterial('LimitState', 30032, 27.68222494, 8.946e-05, 83.04667483, 0.00026839, 276.82224944, 0.00089464, -27.68222494, -8.946e-05, -83.04667483, -0.00026839, -276.82224944, -0.00089464, 0.4, 0.3, 0.003, 0.0, 0.0, 10032, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 32, 99999, 'P', 40032, 'Vy', 30032, 'Vz', 20032, 'My', 10032, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170032, 70032, 170032, 32, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121032, 121032, 21032, 32, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171001, 0.0, 0.0, 3.2)
    ops.node(122001, 0.0, 0.0, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1001, 171001, 122001, 0.09, 27916710.31017665, 11631962.62924027, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21001, 56.05048352, 0.00111819, 68.08675448, 0.01743703, 6.80867545, 0.06350299, -56.05048352, -0.00111819, -68.08675448, -0.01743703, -6.80867545, -0.06350299, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11001, 51.18013748, 0.00111819, 62.1705512, 0.01743703, 6.21705512, 0.06350299, -51.18013748, -0.00111819, -62.1705512, -0.01743703, -6.21705512, -0.06350299, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21001, 1001, 0.0, 95.78193043, 0.02236379, 95.78193043, 0.06709136, 67.0473513, -1401.40982347, 0.05, 2, 0, 71001, 22001, 2, 3)
    ops.uniaxialMaterial('LimitState', 41001, 23.94548261, 8.097e-05, 71.83644782, 0.00024291, 239.45482607, 0.00080971, -23.94548261, -8.097e-05, -71.83644782, -0.00024291, -239.45482607, -0.00080971, 0.4, 0.3, 0.003, 0.0, 0.0, 21001, 2)
    ops.limitCurve('ThreePoint', 11001, 1001, 0.0, 95.78193043, 0.02236379, 95.78193043, 0.06709136, 67.0473513, -1401.40982347, 0.05, 2, 0, 71001, 22001, 1, 3)
    ops.uniaxialMaterial('LimitState', 31001, 23.94548261, 8.097e-05, 71.83644782, 0.00024291, 239.45482607, 0.00080971, -23.94548261, -8.097e-05, -71.83644782, -0.00024291, -239.45482607, -0.00080971, 0.4, 0.3, 0.003, 0.0, 0.0, 11001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1001, 99999, 'P', 41001, 'Vy', 31001, 'Vz', 21001, 'My', 11001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171001, 71001, 171001, 1001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122001, 122001, 22001, 1001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171002, 3.85, 0.0, 3.2)
    ops.node(122002, 3.85, 0.0, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1002, 171002, 122002, 0.16, 29991765.57221067, 12496568.98842111, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21002, 127.88097632, 0.0008391, 154.74604264, 0.01619959, 15.47460426, 0.05550096, -127.88097632, -0.0008391, -154.74604264, -0.01619959, -15.47460426, -0.05550096, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11002, 106.79192341, 0.0008391, 129.2266294, 0.01619959, 12.92266294, 0.05550096, -106.79192341, -0.0008391, -129.2266294, -0.01619959, -12.92266294, -0.05550096, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21002, 1002, 0.0, 166.33477937, 0.01678195, 166.33477937, 0.05034584, 116.43434556, -1975.20917755, 0.05, 2, 0, 71002, 22002, 2, 3)
    ops.uniaxialMaterial('LimitState', 41002, 41.58369484, 7.362e-05, 124.75108453, 0.00022087, 415.83694843, 0.00073623, -41.58369484, -7.362e-05, -124.75108453, -0.00022087, -415.83694843, -0.00073623, 0.4, 0.3, 0.003, 0.0, 0.0, 21002, 2)
    ops.limitCurve('ThreePoint', 11002, 1002, 0.0, 166.33477937, 0.01678195, 166.33477937, 0.05034584, 116.43434556, -1975.20917755, 0.05, 2, 0, 71002, 22002, 1, 3)
    ops.uniaxialMaterial('LimitState', 31002, 41.58369484, 7.362e-05, 124.75108453, 0.00022087, 415.83694843, 0.00073623, -41.58369484, -7.362e-05, -124.75108453, -0.00022087, -415.83694843, -0.00073623, 0.4, 0.3, 0.003, 0.0, 0.0, 11002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1002, 99999, 'P', 41002, 'Vy', 31002, 'Vz', 21002, 'My', 11002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171002, 71002, 171002, 1002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122002, 122002, 22002, 1002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171003, 7.7, 0.0, 3.2)
    ops.node(122003, 7.7, 0.0, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1003, 171003, 122003, 0.16, 29277024.7654951, 12198760.31895629, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21003, 126.21865529, 0.00084599, 152.97104463, 0.01884907, 15.29710446, 0.05756986, -126.21865529, -0.00084599, -152.97104463, -0.01884907, -15.29710446, -0.05756986, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11003, 105.7022325, 0.00084599, 128.1061099, 0.01884907, 12.81061099, 0.05756986, -105.7022325, -0.00084599, -128.1061099, -0.01884907, -12.81061099, -0.05756986, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21003, 1003, 0.0, 167.43578476, 0.01691983, 167.43578476, 0.05075948, 117.20504934, -2148.30481073, 0.05, 2, 0, 71003, 22003, 2, 3)
    ops.uniaxialMaterial('LimitState', 41003, 41.85894619, 7.592e-05, 125.57683857, 0.00022776, 418.58946191, 0.0007592, -41.85894619, -7.592e-05, -125.57683857, -0.00022776, -418.58946191, -0.0007592, 0.4, 0.3, 0.003, 0.0, 0.0, 21003, 2)
    ops.limitCurve('ThreePoint', 11003, 1003, 0.0, 167.43578476, 0.01691983, 167.43578476, 0.05075948, 117.20504934, -2148.30481073, 0.05, 2, 0, 71003, 22003, 1, 3)
    ops.uniaxialMaterial('LimitState', 31003, 41.85894619, 7.592e-05, 125.57683857, 0.00022776, 418.58946191, 0.0007592, -41.85894619, -7.592e-05, -125.57683857, -0.00022776, -418.58946191, -0.0007592, 0.4, 0.3, 0.003, 0.0, 0.0, 11003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1003, 99999, 'P', 41003, 'Vy', 31003, 'Vz', 21003, 'My', 11003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171003, 71003, 171003, 1003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122003, 122003, 22003, 1003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171006, 18.45, 0.0, 3.2)
    ops.node(122006, 18.45, 0.0, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1006, 171006, 122006, 0.16, 29374815.93712174, 12239506.64046739, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21006, 124.81977351, 0.00086782, 151.24513761, 0.01600392, 15.12451376, 0.05480726, -124.81977351, -0.00086782, -151.24513761, -0.01600392, -15.12451376, -0.05480726, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11006, 105.49346927, 0.00086782, 127.82729714, 0.01600392, 12.78272971, 0.05480726, -105.49346927, -0.00086782, -127.82729714, -0.01600392, -12.78272971, -0.05480726, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21006, 1006, 0.0, 161.51547456, 0.01735633, 161.51547456, 0.05206899, 113.06083219, -1906.08259254, 0.05, 2, 0, 71006, 22006, 2, 3)
    ops.uniaxialMaterial('LimitState', 41006, 40.37886864, 7.299e-05, 121.13660592, 0.00021898, 403.7886864, 0.00072992, -40.37886864, -7.299e-05, -121.13660592, -0.00021898, -403.7886864, -0.00072992, 0.4, 0.3, 0.003, 0.0, 0.0, 21006, 2)
    ops.limitCurve('ThreePoint', 11006, 1006, 0.0, 161.51547456, 0.01735633, 161.51547456, 0.05206899, 113.06083219, -1906.08259254, 0.05, 2, 0, 71006, 22006, 1, 3)
    ops.uniaxialMaterial('LimitState', 31006, 40.37886864, 7.299e-05, 121.13660592, 0.00021898, 403.7886864, 0.00072992, -40.37886864, -7.299e-05, -121.13660592, -0.00021898, -403.7886864, -0.00072992, 0.4, 0.3, 0.003, 0.0, 0.0, 11006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1006, 99999, 'P', 41006, 'Vy', 31006, 'Vz', 21006, 'My', 11006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171006, 71006, 171006, 1006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122006, 122006, 22006, 1006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171007, 22.3, 0.0, 3.2)
    ops.node(122007, 22.3, 0.0, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1007, 171007, 122007, 0.16, 28849840.55794065, 12020766.89914194, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21007, 131.48528025, 0.00090451, 159.48856574, 0.01834787, 15.94885657, 0.05669589, -131.48528025, -0.00090451, -159.48856574, -0.01834787, -15.94885657, -0.05669589, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11007, 110.0526587, 0.00090451, 133.49129772, 0.01834787, 13.34912977, 0.05669589, -110.0526587, -0.00090451, -133.49129772, -0.01834787, -13.34912977, -0.05669589, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21007, 1007, 0.0, 165.85299933, 0.01809019, 165.85299933, 0.05427058, 116.09709953, -2165.49750377, 0.05, 2, 0, 71007, 22007, 2, 3)
    ops.uniaxialMaterial('LimitState', 41007, 41.46324983, 7.632e-05, 124.3897495, 0.00022895, 414.63249834, 0.00076316, -41.46324983, -7.632e-05, -124.3897495, -0.00022895, -414.63249834, -0.00076316, 0.4, 0.3, 0.003, 0.0, 0.0, 21007, 2)
    ops.limitCurve('ThreePoint', 11007, 1007, 0.0, 165.85299933, 0.01809019, 165.85299933, 0.05427058, 116.09709953, -2165.49750377, 0.05, 2, 0, 71007, 22007, 1, 3)
    ops.uniaxialMaterial('LimitState', 31007, 41.46324983, 7.632e-05, 124.3897495, 0.00022895, 414.63249834, 0.00076316, -41.46324983, -7.632e-05, -124.3897495, -0.00022895, -414.63249834, -0.00076316, 0.4, 0.3, 0.003, 0.0, 0.0, 11007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1007, 99999, 'P', 41007, 'Vy', 31007, 'Vz', 21007, 'My', 11007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171007, 71007, 171007, 1007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122007, 122007, 22007, 1007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171008, 26.15, 0.0, 3.2)
    ops.node(122008, 26.15, 0.0, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1008, 171008, 122008, 0.09, 30830255.90546865, 12845939.96061194, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21008, 53.30174768, 0.00104399, 64.36048976, 0.01977748, 6.43604898, 0.06894181, -53.30174768, -0.00104399, -64.36048976, -0.01977748, -6.43604898, -0.06894181, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11008, 49.04614105, 0.00104399, 59.22195418, 0.01977748, 5.92219542, 0.06894181, -49.04614105, -0.00104399, -59.22195418, -0.01977748, -5.92219542, -0.06894181, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21008, 1008, 0.0, 112.23135004, 0.02087971, 112.23135004, 0.06263913, 78.56194503, -1783.52530436, 0.05, 2, 0, 71008, 22008, 2, 3)
    ops.uniaxialMaterial('LimitState', 41008, 28.05783751, 8.591e-05, 84.17351253, 0.00025773, 280.5783751, 0.00085911, -28.05783751, -8.591e-05, -84.17351253, -0.00025773, -280.5783751, -0.00085911, 0.4, 0.3, 0.003, 0.0, 0.0, 21008, 2)
    ops.limitCurve('ThreePoint', 11008, 1008, 0.0, 112.23135004, 0.02087971, 112.23135004, 0.06263913, 78.56194503, -1783.52530436, 0.05, 2, 0, 71008, 22008, 1, 3)
    ops.uniaxialMaterial('LimitState', 31008, 28.05783751, 8.591e-05, 84.17351253, 0.00025773, 280.5783751, 0.00085911, -28.05783751, -8.591e-05, -84.17351253, -0.00025773, -280.5783751, -0.00085911, 0.4, 0.3, 0.003, 0.0, 0.0, 11008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1008, 99999, 'P', 41008, 'Vy', 31008, 'Vz', 21008, 'My', 11008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171008, 71008, 171008, 1008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122008, 122008, 22008, 1008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171009, 0.0, 4.8, 3.2)
    ops.node(122009, 0.0, 4.8, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1009, 171009, 122009, 0.16, 29709425.23400282, 12378927.18083451, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21009, 125.93467381, 0.00084885, 152.4524388, 0.01641494, 15.24524388, 0.05522927, -125.93467381, -0.00084885, -152.4524388, -0.01641494, -15.24524388, -0.05522927, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11009, 106.2568724, 0.00084885, 128.63112951, 0.01641494, 12.86311295, 0.05522927, -106.2568724, -0.00084885, -128.63112951, -0.01641494, -12.86311295, -0.05522927, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21009, 1009, 0.0, 164.50341376, 0.01697694, 164.50341376, 0.05093081, 115.15238963, -1922.54096165, 0.05, 2, 0, 71009, 22009, 2, 3)
    ops.uniaxialMaterial('LimitState', 41009, 41.12585344, 7.35e-05, 123.37756032, 0.00022051, 411.2585344, 0.00073505, -41.12585344, -7.35e-05, -123.37756032, -0.00022051, -411.2585344, -0.00073505, 0.4, 0.3, 0.003, 0.0, 0.0, 21009, 2)
    ops.limitCurve('ThreePoint', 11009, 1009, 0.0, 164.50341376, 0.01697694, 164.50341376, 0.05093081, 115.15238963, -1922.54096165, 0.05, 2, 0, 71009, 22009, 1, 3)
    ops.uniaxialMaterial('LimitState', 31009, 41.12585344, 7.35e-05, 123.37756032, 0.00022051, 411.2585344, 0.00073505, -41.12585344, -7.35e-05, -123.37756032, -0.00022051, -411.2585344, -0.00073505, 0.4, 0.3, 0.003, 0.0, 0.0, 11009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1009, 99999, 'P', 41009, 'Vy', 31009, 'Vz', 21009, 'My', 11009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171009, 71009, 171009, 1009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122009, 122009, 22009, 1009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171010, 3.85, 4.8, 3.2)
    ops.node(122010, 3.85, 4.8, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1010, 171010, 122010, 0.2025, 27667178.2657157, 11527990.94404821, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21010, 199.67627299, 0.00087034, 242.33722151, 0.02434864, 24.23372215, 0.06276952, -199.67627299, -0.00087034, -242.33722151, -0.02434864, -24.23372215, -0.06276952, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11010, 174.30200744, 0.00087034, 211.5417298, 0.02434864, 21.15417298, 0.06276952, -174.30200744, -0.00087034, -211.5417298, -0.02434864, -21.15417298, -0.06276952, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21010, 1010, 0.0, 203.08848103, 0.01740682, 203.08848103, 0.05222047, 142.16193672, -2527.4275225, 0.05, 2, 0, 71010, 22010, 2, 3)
    ops.uniaxialMaterial('LimitState', 41010, 50.77212026, 7.699e-05, 152.31636078, 0.00023098, 507.72120259, 0.00076993, -50.77212026, -7.699e-05, -152.31636078, -0.00023098, -507.72120259, -0.00076993, 0.4, 0.3, 0.003, 0.0, 0.0, 21010, 2)
    ops.limitCurve('ThreePoint', 11010, 1010, 0.0, 203.08848103, 0.01740682, 203.08848103, 0.05222047, 142.16193672, -2527.4275225, 0.05, 2, 0, 71010, 22010, 1, 3)
    ops.uniaxialMaterial('LimitState', 31010, 50.77212026, 7.699e-05, 152.31636078, 0.00023098, 507.72120259, 0.00076993, -50.77212026, -7.699e-05, -152.31636078, -0.00023098, -507.72120259, -0.00076993, 0.4, 0.3, 0.003, 0.0, 0.0, 11010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1010, 99999, 'P', 41010, 'Vy', 31010, 'Vz', 21010, 'My', 11010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171010, 71010, 171010, 1010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122010, 122010, 22010, 1010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171011, 7.7, 4.8, 3.2)
    ops.node(122011, 7.7, 4.8, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1011, 171011, 122011, 0.2025, 30293828.9700036, 12622428.7375015, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21011, 193.89232572, 0.00081545, 234.20699589, 0.01998334, 23.42069959, 0.05525762, -193.89232572, -0.00081545, -234.20699589, -0.01998334, -23.42069959, -0.05525762, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11011, 170.25542777, 0.00081545, 205.65544368, 0.01998334, 20.56554437, 0.05525762, -170.25542777, -0.00081545, -205.65544368, -0.01998334, -20.56554437, -0.05525762, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21011, 1011, 0.0, 207.95827822, 0.01630897, 207.95827822, 0.04892691, 145.57079475, -2162.65834566, 0.05, 2, 0, 71011, 22011, 2, 3)
    ops.uniaxialMaterial('LimitState', 41011, 51.98956955, 7.2e-05, 155.96870866, 0.00021601, 519.89569554, 0.00072003, -51.98956955, -7.2e-05, -155.96870866, -0.00021601, -519.89569554, -0.00072003, 0.4, 0.3, 0.003, 0.0, 0.0, 21011, 2)
    ops.limitCurve('ThreePoint', 11011, 1011, 0.0, 207.95827822, 0.01630897, 207.95827822, 0.04892691, 145.57079475, -2162.65834566, 0.05, 2, 0, 71011, 22011, 1, 3)
    ops.uniaxialMaterial('LimitState', 31011, 51.98956955, 7.2e-05, 155.96870866, 0.00021601, 519.89569554, 0.00072003, -51.98956955, -7.2e-05, -155.96870866, -0.00021601, -519.89569554, -0.00072003, 0.4, 0.3, 0.003, 0.0, 0.0, 11011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1011, 99999, 'P', 41011, 'Vy', 31011, 'Vz', 21011, 'My', 11011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171011, 71011, 171011, 1011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122011, 122011, 22011, 1011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171012, 11.55, 4.8, 3.2)
    ops.node(122012, 11.55, 4.8, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1012, 171012, 122012, 0.2025, 32711214.44554438, 13629672.68564349, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21012, 182.7243366, 0.00076067, 219.36894637, 0.01846545, 21.93689464, 0.0621149, -182.7243366, -0.00076067, -219.36894637, -0.01846545, -21.93689464, -0.0621149, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11012, 150.82933681, 0.00076067, 181.07753632, 0.01846545, 18.10775363, 0.0621149, -150.82933681, -0.00076067, -181.07753632, -0.01846545, -18.10775363, -0.0621149, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21012, 1012, 0.0, 228.36088583, 0.01521333, 228.36088583, 0.04563999, 159.85262008, -2395.50756013, 0.05, 2, 0, 71012, 22012, 2, 3)
    ops.uniaxialMaterial('LimitState', 41012, 57.09022146, 7.322e-05, 171.27066437, 0.00021967, 570.90221458, 0.00073224, -57.09022146, -7.322e-05, -171.27066437, -0.00021967, -570.90221458, -0.00073224, 0.4, 0.3, 0.003, 0.0, 0.0, 21012, 2)
    ops.limitCurve('ThreePoint', 11012, 1012, 0.0, 228.36088583, 0.01521333, 228.36088583, 0.04563999, 159.85262008, -2395.50756013, 0.05, 2, 0, 71012, 22012, 1, 3)
    ops.uniaxialMaterial('LimitState', 31012, 57.09022146, 7.322e-05, 171.27066437, 0.00021967, 570.90221458, 0.00073224, -57.09022146, -7.322e-05, -171.27066437, -0.00021967, -570.90221458, -0.00073224, 0.4, 0.3, 0.003, 0.0, 0.0, 11012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1012, 99999, 'P', 41012, 'Vy', 31012, 'Vz', 21012, 'My', 11012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171012, 71012, 171012, 1012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122012, 122012, 22012, 1012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171013, 14.6, 4.8, 3.2)
    ops.node(122013, 14.6, 4.8, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1013, 171013, 122013, 0.2025, 29351725.96147385, 12229885.81728077, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21013, 181.41675423, 0.00083719, 219.67138656, 0.01970428, 21.96713866, 0.06062195, -181.41675423, -0.00083719, -219.67138656, -0.01970428, -21.96713866, -0.06062195, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11013, 151.46167916, 0.00083719, 183.39980347, 0.01970428, 18.33998035, 0.06062195, -151.46167916, -0.00083719, -183.39980347, -0.01970428, -18.33998035, -0.06062195, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21013, 1013, 0.0, 211.26783065, 0.01674382, 211.26783065, 0.05023147, 147.88748146, -2533.88449435, 0.05, 2, 0, 71013, 22013, 2, 3)
    ops.uniaxialMaterial('LimitState', 41013, 52.81695766, 7.55e-05, 158.45087299, 0.00022649, 528.16957663, 0.00075497, -52.81695766, -7.55e-05, -158.45087299, -0.00022649, -528.16957663, -0.00075497, 0.4, 0.3, 0.003, 0.0, 0.0, 21013, 2)
    ops.limitCurve('ThreePoint', 11013, 1013, 0.0, 211.26783065, 0.01674382, 211.26783065, 0.05023147, 147.88748146, -2533.88449435, 0.05, 2, 0, 71013, 22013, 1, 3)
    ops.uniaxialMaterial('LimitState', 31013, 52.81695766, 7.55e-05, 158.45087299, 0.00022649, 528.16957663, 0.00075497, -52.81695766, -7.55e-05, -158.45087299, -0.00022649, -528.16957663, -0.00075497, 0.4, 0.3, 0.003, 0.0, 0.0, 11013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1013, 99999, 'P', 41013, 'Vy', 31013, 'Vz', 21013, 'My', 11013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171013, 71013, 171013, 1013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122013, 122013, 22013, 1013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171014, 18.45, 4.8, 3.2)
    ops.node(122014, 18.45, 4.8, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1014, 171014, 122014, 0.2025, 31588365.65630184, 13161819.0234591, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21014, 199.94961646, 0.00079582, 240.74991971, 0.01811235, 24.07499197, 0.05433645, -199.94961646, -0.00079582, -240.74991971, -0.01811235, -24.07499197, -0.05433645, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11014, 174.40738945, 0.00079582, 209.99572668, 0.01811235, 20.99957267, 0.05433645, -174.40738945, -0.00079582, -209.99572668, -0.01811235, -20.99957267, -0.05433645, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21014, 1014, 0.0, 207.46025687, 0.01591641, 207.46025687, 0.04774924, 145.22217981, -1896.19025231, 0.05, 2, 0, 71014, 22014, 2, 3)
    ops.uniaxialMaterial('LimitState', 41014, 51.86506422, 6.889e-05, 155.59519266, 0.00020666, 518.65064219, 0.00068887, -51.86506422, -6.889e-05, -155.59519266, -0.00020666, -518.65064219, -0.00068887, 0.4, 0.3, 0.003, 0.0, 0.0, 21014, 2)
    ops.limitCurve('ThreePoint', 11014, 1014, 0.0, 207.46025687, 0.01591641, 207.46025687, 0.04774924, 145.22217981, -1896.19025231, 0.05, 2, 0, 71014, 22014, 1, 3)
    ops.uniaxialMaterial('LimitState', 31014, 51.86506422, 6.889e-05, 155.59519266, 0.00020666, 518.65064219, 0.00068887, -51.86506422, -6.889e-05, -155.59519266, -0.00020666, -518.65064219, -0.00068887, 0.4, 0.3, 0.003, 0.0, 0.0, 11014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1014, 99999, 'P', 41014, 'Vy', 31014, 'Vz', 21014, 'My', 11014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171014, 71014, 171014, 1014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122014, 122014, 22014, 1014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171015, 22.3, 4.8, 3.2)
    ops.node(122015, 22.3, 4.8, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1015, 171015, 122015, 0.2025, 28641774.63244529, 11934072.76351887, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21015, 192.0587958, 0.00088901, 232.75055697, 0.026263, 23.2750557, 0.06585775, -192.0587958, -0.00088901, -232.75055697, -0.026263, -23.2750557, -0.06585775, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11015, 170.26149502, 0.00088901, 206.33503211, 0.026263, 20.63350321, 0.06585775, -170.26149502, -0.00088901, -206.33503211, -0.026263, -20.63350321, -0.06585775, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21015, 1015, 0.0, 219.21965228, 0.01778011, 219.21965228, 0.05334034, 153.45375659, -2898.03815757, 0.05, 2, 0, 71015, 22015, 2, 3)
    ops.uniaxialMaterial('LimitState', 41015, 54.80491307, 8.028e-05, 164.41473921, 0.00024084, 548.0491307, 0.0008028, -54.80491307, -8.028e-05, -164.41473921, -0.00024084, -548.0491307, -0.0008028, 0.4, 0.3, 0.003, 0.0, 0.0, 21015, 2)
    ops.limitCurve('ThreePoint', 11015, 1015, 0.0, 219.21965228, 0.01778011, 219.21965228, 0.05334034, 153.45375659, -2898.03815757, 0.05, 2, 0, 71015, 22015, 1, 3)
    ops.uniaxialMaterial('LimitState', 31015, 54.80491307, 8.028e-05, 164.41473921, 0.00024084, 548.0491307, 0.0008028, -54.80491307, -8.028e-05, -164.41473921, -0.00024084, -548.0491307, -0.0008028, 0.4, 0.3, 0.003, 0.0, 0.0, 11015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1015, 99999, 'P', 41015, 'Vy', 31015, 'Vz', 21015, 'My', 11015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171015, 71015, 171015, 1015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122015, 122015, 22015, 1015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171016, 26.15, 4.8, 3.2)
    ops.node(122016, 26.15, 4.8, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1016, 171016, 122016, 0.16, 29651021.27614199, 12354592.1983925, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21016, 130.79450073, 0.00085418, 158.35551459, 0.01446681, 15.83555146, 0.05323258, -130.79450073, -0.00085418, -158.35551459, -0.01446681, -15.83555146, -0.05323258, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11016, 109.19691306, 0.00085418, 132.2068838, 0.01446681, 13.22068838, 0.05323258, -109.19691306, -0.00085418, -132.2068838, -0.01446681, -13.22068838, -0.05323258, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21016, 1016, 0.0, 156.97339326, 0.01708355, 156.97339326, 0.05125064, 109.88137529, -1668.43564763, 0.05, 2, 0, 71016, 22016, 2, 3)
    ops.uniaxialMaterial('LimitState', 41016, 39.24334832, 7.028e-05, 117.73004495, 0.00021083, 392.43348316, 0.00070278, -39.24334832, -7.028e-05, -117.73004495, -0.00021083, -392.43348316, -0.00070278, 0.4, 0.3, 0.003, 0.0, 0.0, 21016, 2)
    ops.limitCurve('ThreePoint', 11016, 1016, 0.0, 156.97339326, 0.01708355, 156.97339326, 0.05125064, 109.88137529, -1668.43564763, 0.05, 2, 0, 71016, 22016, 1, 3)
    ops.uniaxialMaterial('LimitState', 31016, 39.24334832, 7.028e-05, 117.73004495, 0.00021083, 392.43348316, 0.00070278, -39.24334832, -7.028e-05, -117.73004495, -0.00021083, -392.43348316, -0.00070278, 0.4, 0.3, 0.003, 0.0, 0.0, 11016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1016, 99999, 'P', 41016, 'Vy', 31016, 'Vz', 21016, 'My', 11016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171016, 71016, 171016, 1016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122016, 122016, 22016, 1016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171017, 0.0, 9.6, 3.2)
    ops.node(122017, 0.0, 9.6, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1017, 171017, 122017, 0.16, 29031822.8264651, 12096592.84436046, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21017, 126.62256905, 0.00086007, 153.50451111, 0.01816602, 15.35045111, 0.05643976, -126.62256905, -0.00086007, -153.50451111, -0.01816602, -15.35045111, -0.05643976, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11017, 106.57707627, 0.00086007, 129.20336485, 0.01816602, 12.92033648, 0.05643976, -106.57707627, -0.00086007, -129.20336485, -0.01816602, -12.92033648, -0.05643976, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21017, 1017, 0.0, 169.30360473, 0.01720144, 169.30360473, 0.05160433, 118.51252331, -2231.84846398, 0.05, 2, 0, 71017, 22017, 2, 3)
    ops.uniaxialMaterial('LimitState', 41017, 42.32590118, 7.742e-05, 126.97770354, 0.00023225, 423.25901181, 0.00077415, -42.32590118, -7.742e-05, -126.97770354, -0.00023225, -423.25901181, -0.00077415, 0.4, 0.3, 0.003, 0.0, 0.0, 21017, 2)
    ops.limitCurve('ThreePoint', 11017, 1017, 0.0, 169.30360473, 0.01720144, 169.30360473, 0.05160433, 118.51252331, -2231.84846398, 0.05, 2, 0, 71017, 22017, 1, 3)
    ops.uniaxialMaterial('LimitState', 31017, 42.32590118, 7.742e-05, 126.97770354, 0.00023225, 423.25901181, 0.00077415, -42.32590118, -7.742e-05, -126.97770354, -0.00023225, -423.25901181, -0.00077415, 0.4, 0.3, 0.003, 0.0, 0.0, 11017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1017, 99999, 'P', 41017, 'Vy', 31017, 'Vz', 21017, 'My', 11017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171017, 71017, 171017, 1017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122017, 122017, 22017, 1017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171018, 3.85, 9.6, 3.2)
    ops.node(122018, 3.85, 9.6, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1018, 171018, 122018, 0.2025, 29072619.35094796, 12113591.39622832, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21018, 194.98033965, 0.00083311, 236.12449817, 0.02170965, 23.61244982, 0.05599599, -194.98033965, -0.00083311, -236.12449817, -0.02170965, -23.61244982, -0.05599599, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11018, 170.76382501, 0.00083311, 206.79788822, 0.02170965, 20.67978882, 0.05599599, -170.76382501, -0.00083311, -206.79788822, -0.02170965, -20.67978882, -0.05599599, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21018, 1018, 0.0, 205.45785813, 0.01666223, 205.45785813, 0.04998668, 143.82050069, -2331.15903508, 0.05, 2, 0, 71018, 22018, 2, 3)
    ops.uniaxialMaterial('LimitState', 41018, 51.36446453, 7.413e-05, 154.0933936, 0.00022238, 513.64464533, 0.00074126, -51.36446453, -7.413e-05, -154.0933936, -0.00022238, -513.64464533, -0.00074126, 0.4, 0.3, 0.003, 0.0, 0.0, 21018, 2)
    ops.limitCurve('ThreePoint', 11018, 1018, 0.0, 205.45785813, 0.01666223, 205.45785813, 0.04998668, 143.82050069, -2331.15903508, 0.05, 2, 0, 71018, 22018, 1, 3)
    ops.uniaxialMaterial('LimitState', 31018, 51.36446453, 7.413e-05, 154.0933936, 0.00022238, 513.64464533, 0.00074126, -51.36446453, -7.413e-05, -154.0933936, -0.00022238, -513.64464533, -0.00074126, 0.4, 0.3, 0.003, 0.0, 0.0, 11018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1018, 99999, 'P', 41018, 'Vy', 31018, 'Vz', 21018, 'My', 11018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171018, 71018, 171018, 1018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122018, 122018, 22018, 1018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171019, 7.7, 9.6, 3.2)
    ops.node(122019, 7.7, 9.6, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1019, 171019, 122019, 0.2025, 30722261.99766035, 12800942.49902515, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21019, 195.6143853, 0.00081892, 236.06151256, 0.02642585, 23.60615126, 0.06815943, -195.6143853, -0.00081892, -236.06151256, -0.02642585, -23.60615126, -0.06815943, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11019, 171.6359013, 0.00081892, 207.12500468, 0.02642585, 20.71250047, 0.06815943, -171.6359013, -0.00081892, -207.12500468, -0.02642585, -20.71250047, -0.06815943, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21019, 1019, 0.0, 238.33181277, 0.01637846, 238.33181277, 0.04913538, 166.83226894, -3150.71683804, 0.05, 2, 0, 71019, 22019, 2, 3)
    ops.uniaxialMaterial('LimitState', 41019, 59.58295319, 8.137e-05, 178.74885958, 0.00024411, 595.82953192, 0.00081369, -59.58295319, -8.137e-05, -178.74885958, -0.00024411, -595.82953192, -0.00081369, 0.4, 0.3, 0.003, 0.0, 0.0, 21019, 2)
    ops.limitCurve('ThreePoint', 11019, 1019, 0.0, 238.33181277, 0.01637846, 238.33181277, 0.04913538, 166.83226894, -3150.71683804, 0.05, 2, 0, 71019, 22019, 1, 3)
    ops.uniaxialMaterial('LimitState', 31019, 59.58295319, 8.137e-05, 178.74885958, 0.00024411, 595.82953192, 0.00081369, -59.58295319, -8.137e-05, -178.74885958, -0.00024411, -595.82953192, -0.00081369, 0.4, 0.3, 0.003, 0.0, 0.0, 11019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1019, 99999, 'P', 41019, 'Vy', 31019, 'Vz', 21019, 'My', 11019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171019, 71019, 171019, 1019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122019, 122019, 22019, 1019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171020, 11.55, 9.6, 3.2)
    ops.node(122020, 11.55, 9.6, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1020, 171020, 122020, 0.16, 29509492.97083487, 12295622.07118119, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21020, 140.28539106, 0.00091225, 169.58376856, 0.01765705, 16.95837686, 0.05423306, -140.28539106, -0.00091225, -169.58376856, -0.01765705, -16.95837686, -0.05423306, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11020, 119.79988337, 0.00091225, 144.81989564, 0.01765705, 14.48198956, 0.05423306, -119.79988337, -0.00091225, -144.81989564, -0.01765705, -14.48198956, -0.05423306, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21020, 1020, 0.0, 174.93388611, 0.01824508, 174.93388611, 0.05473525, 122.45372028, -2090.48823016, 0.05, 2, 0, 71020, 22020, 2, 3)
    ops.uniaxialMaterial('LimitState', 41020, 43.73347153, 7.869e-05, 131.20041458, 0.00023608, 437.33471527, 0.00078695, -43.73347153, -7.869e-05, -131.20041458, -0.00023608, -437.33471527, -0.00078695, 0.4, 0.3, 0.003, 0.0, 0.0, 21020, 2)
    ops.limitCurve('ThreePoint', 11020, 1020, 0.0, 174.93388611, 0.01824508, 174.93388611, 0.05473525, 122.45372028, -2090.48823016, 0.05, 2, 0, 71020, 22020, 1, 3)
    ops.uniaxialMaterial('LimitState', 31020, 43.73347153, 7.869e-05, 131.20041458, 0.00023608, 437.33471527, 0.00078695, -43.73347153, -7.869e-05, -131.20041458, -0.00023608, -437.33471527, -0.00078695, 0.4, 0.3, 0.003, 0.0, 0.0, 11020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1020, 99999, 'P', 41020, 'Vy', 31020, 'Vz', 21020, 'My', 11020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171020, 71020, 171020, 1020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122020, 122020, 22020, 1020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171021, 14.6, 9.6, 3.2)
    ops.node(122021, 14.6, 9.6, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1021, 171021, 122021, 0.16, 32469025.9492538, 13528760.81218908, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21021, 134.11996135, 0.00082187, 160.97840021, 0.0155727, 16.09784002, 0.05472651, -134.11996135, -0.00082187, -160.97840021, -0.0155727, -16.09784002, -0.05472651, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11021, 115.09485838, 0.00082187, 138.14339035, 0.0155727, 13.81433903, 0.05472651, -115.09485838, -0.00082187, -138.14339035, -0.0155727, -13.81433903, -0.05472651, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21021, 1021, 0.0, 182.0616993, 0.01643733, 182.0616993, 0.049312, 127.44318951, -1843.87724014, 0.05, 2, 0, 71021, 22021, 2, 3)
    ops.uniaxialMaterial('LimitState', 41021, 45.51542482, 7.444e-05, 136.54627447, 0.00022331, 455.15424824, 0.00074436, -45.51542482, -7.444e-05, -136.54627447, -0.00022331, -455.15424824, -0.00074436, 0.4, 0.3, 0.003, 0.0, 0.0, 21021, 2)
    ops.limitCurve('ThreePoint', 11021, 1021, 0.0, 182.0616993, 0.01643733, 182.0616993, 0.049312, 127.44318951, -1843.87724014, 0.05, 2, 0, 71021, 22021, 1, 3)
    ops.uniaxialMaterial('LimitState', 31021, 45.51542482, 7.444e-05, 136.54627447, 0.00022331, 455.15424824, 0.00074436, -45.51542482, -7.444e-05, -136.54627447, -0.00022331, -455.15424824, -0.00074436, 0.4, 0.3, 0.003, 0.0, 0.0, 11021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1021, 99999, 'P', 41021, 'Vy', 31021, 'Vz', 21021, 'My', 11021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171021, 71021, 171021, 1021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122021, 122021, 22021, 1021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171022, 18.45, 9.6, 3.2)
    ops.node(122022, 18.45, 9.6, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1022, 171022, 122022, 0.2025, 29547896.73788899, 12311623.64078708, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21022, 189.68372001, 0.00083208, 229.49986047, 0.02763268, 22.94998605, 0.06826124, -189.68372001, -0.00083208, -229.49986047, -0.02763268, -22.94998605, -0.06826124, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11022, 167.39927616, 0.00083208, 202.53773239, 0.02763268, 20.25377324, 0.06826124, -167.39927616, -0.00083208, -202.53773239, -0.02763268, -20.25377324, -0.06826124, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21022, 1022, 0.0, 234.38807115, 0.01664159, 234.38807115, 0.04992477, 164.07164981, -3279.66827265, 0.05, 2, 0, 71022, 22022, 2, 3)
    ops.uniaxialMaterial('LimitState', 41022, 58.59701779, 8.32e-05, 175.79105337, 0.00024961, 585.97017789, 0.00083203, -58.59701779, -8.32e-05, -175.79105337, -0.00024961, -585.97017789, -0.00083203, 0.4, 0.3, 0.003, 0.0, 0.0, 21022, 2)
    ops.limitCurve('ThreePoint', 11022, 1022, 0.0, 234.38807115, 0.01664159, 234.38807115, 0.04992477, 164.07164981, -3279.66827265, 0.05, 2, 0, 71022, 22022, 1, 3)
    ops.uniaxialMaterial('LimitState', 31022, 58.59701779, 8.32e-05, 175.79105337, 0.00024961, 585.97017789, 0.00083203, -58.59701779, -8.32e-05, -175.79105337, -0.00024961, -585.97017789, -0.00083203, 0.4, 0.3, 0.003, 0.0, 0.0, 11022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1022, 99999, 'P', 41022, 'Vy', 31022, 'Vz', 21022, 'My', 11022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171022, 71022, 171022, 1022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122022, 122022, 22022, 1022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171023, 22.3, 9.6, 3.2)
    ops.node(122023, 22.3, 9.6, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1023, 171023, 122023, 0.2025, 27001247.05718, 11250519.60715833, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21023, 195.77453822, 0.00086184, 237.80729028, 0.01913415, 23.78072903, 0.05126418, -195.77453822, -0.00086184, -237.80729028, -0.01913415, -23.78072903, -0.05126418, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11023, 170.91078641, 0.00086184, 207.6052962, 0.01913415, 20.76052962, 0.05126418, -170.91078641, -0.00086184, -207.6052962, -0.01913415, -20.76052962, -0.05126418, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21023, 1023, 0.0, 186.24335476, 0.01723688, 186.24335476, 0.05171064, 130.37034833, -2104.73713908, 0.05, 2, 0, 71023, 22023, 2, 3)
    ops.uniaxialMaterial('LimitState', 41023, 46.56083869, 7.235e-05, 139.68251607, 0.00021704, 465.6083869, 0.00072348, -46.56083869, -7.235e-05, -139.68251607, -0.00021704, -465.6083869, -0.00072348, 0.4, 0.3, 0.003, 0.0, 0.0, 21023, 2)
    ops.limitCurve('ThreePoint', 11023, 1023, 0.0, 186.24335476, 0.01723688, 186.24335476, 0.05171064, 130.37034833, -2104.73713908, 0.05, 2, 0, 71023, 22023, 1, 3)
    ops.uniaxialMaterial('LimitState', 31023, 46.56083869, 7.235e-05, 139.68251607, 0.00021704, 465.6083869, 0.00072348, -46.56083869, -7.235e-05, -139.68251607, -0.00021704, -465.6083869, -0.00072348, 0.4, 0.3, 0.003, 0.0, 0.0, 11023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1023, 99999, 'P', 41023, 'Vy', 31023, 'Vz', 21023, 'My', 11023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171023, 71023, 171023, 1023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122023, 122023, 22023, 1023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171024, 26.15, 9.6, 3.2)
    ops.node(122024, 26.15, 9.6, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1024, 171024, 122024, 0.16, 28756295.38523661, 11981789.74384859, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21024, 127.83325048, 0.00084818, 155.05320338, 0.01633923, 15.50532034, 0.0543613, -127.83325048, -0.00084818, -155.05320338, -0.01633923, -15.50532034, -0.0543613, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11024, 106.85571323, 0.00084818, 129.60885039, 0.01633923, 12.96088504, 0.0543613, -106.85571323, -0.00084818, -129.60885039, -0.01633923, -12.96088504, -0.0543613, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21024, 1024, 0.0, 158.71950075, 0.01696355, 158.71950075, 0.05089065, 111.10365053, -1882.65799864, 0.05, 2, 0, 71024, 22024, 2, 3)
    ops.uniaxialMaterial('LimitState', 41024, 39.67987519, 7.327e-05, 119.03962556, 0.00021981, 396.79875188, 0.00073271, -39.67987519, -7.327e-05, -119.03962556, -0.00021981, -396.79875188, -0.00073271, 0.4, 0.3, 0.003, 0.0, 0.0, 21024, 2)
    ops.limitCurve('ThreePoint', 11024, 1024, 0.0, 158.71950075, 0.01696355, 158.71950075, 0.05089065, 111.10365053, -1882.65799864, 0.05, 2, 0, 71024, 22024, 1, 3)
    ops.uniaxialMaterial('LimitState', 31024, 39.67987519, 7.327e-05, 119.03962556, 0.00021981, 396.79875188, 0.00073271, -39.67987519, -7.327e-05, -119.03962556, -0.00021981, -396.79875188, -0.00073271, 0.4, 0.3, 0.003, 0.0, 0.0, 11024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1024, 99999, 'P', 41024, 'Vy', 31024, 'Vz', 21024, 'My', 11024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171024, 71024, 171024, 1024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122024, 122024, 22024, 1024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171025, 0.0, 14.4, 3.2)
    ops.node(122025, 0.0, 14.4, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1025, 171025, 122025, 0.09, 31241751.10258349, 13017396.29274312, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21025, 54.20100548, 0.00109002, 65.37621414, 0.01898645, 6.53762141, 0.06850481, -54.20100548, -0.00109002, -65.37621414, -0.01898645, -6.53762141, -0.06850481, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11025, 50.0140211, 0.00109002, 60.32595382, 0.01898645, 6.03259538, 0.06850481, -50.0140211, -0.00109002, -60.32595382, -0.01898645, -6.03259538, -0.06850481, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21025, 1025, 0.0, 110.61055486, 0.02180032, 110.61055486, 0.06540096, 77.4273884, -1656.31921733, 0.05, 2, 0, 71025, 22025, 2, 3)
    ops.uniaxialMaterial('LimitState', 41025, 27.65263872, 8.356e-05, 82.95791615, 0.00025067, 276.52638715, 0.00083555, -27.65263872, -8.356e-05, -82.95791615, -0.00025067, -276.52638715, -0.00083555, 0.4, 0.3, 0.003, 0.0, 0.0, 21025, 2)
    ops.limitCurve('ThreePoint', 11025, 1025, 0.0, 110.61055486, 0.02180032, 110.61055486, 0.06540096, 77.4273884, -1656.31921733, 0.05, 2, 0, 71025, 22025, 1, 3)
    ops.uniaxialMaterial('LimitState', 31025, 27.65263872, 8.356e-05, 82.95791615, 0.00025067, 276.52638715, 0.00083555, -27.65263872, -8.356e-05, -82.95791615, -0.00025067, -276.52638715, -0.00083555, 0.4, 0.3, 0.003, 0.0, 0.0, 11025, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1025, 99999, 'P', 41025, 'Vy', 31025, 'Vz', 21025, 'My', 11025, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171025, 71025, 171025, 1025, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122025, 122025, 22025, 1025, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171026, 3.85, 14.4, 3.2)
    ops.node(122026, 3.85, 14.4, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1026, 171026, 122026, 0.16, 28937022.7861094, 12057092.82754558, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21026, 129.2721417, 0.0008572, 156.77783443, 0.01497475, 15.67778344, 0.05340049, -129.2721417, -0.0008572, -156.77783443, -0.01497475, -15.67778344, -0.05340049, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11026, 107.61647643, 0.0008572, 130.51441635, 0.01497475, 13.05144163, 0.05340049, -107.61647643, -0.0008572, -130.51441635, -0.01497475, -13.05144163, -0.05340049, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21026, 1026, 0.0, 157.30424474, 0.01714391, 157.30424474, 0.05143172, 110.11297132, -1828.32630575, 0.05, 2, 0, 71026, 22026, 2, 3)
    ops.uniaxialMaterial('LimitState', 41026, 39.32606119, 7.216e-05, 117.97818356, 0.00021649, 393.26061185, 0.00072164, -39.32606119, -7.216e-05, -117.97818356, -0.00021649, -393.26061185, -0.00072164, 0.4, 0.3, 0.003, 0.0, 0.0, 21026, 2)
    ops.limitCurve('ThreePoint', 11026, 1026, 0.0, 157.30424474, 0.01714391, 157.30424474, 0.05143172, 110.11297132, -1828.32630575, 0.05, 2, 0, 71026, 22026, 1, 3)
    ops.uniaxialMaterial('LimitState', 31026, 39.32606119, 7.216e-05, 117.97818356, 0.00021649, 393.26061185, 0.00072164, -39.32606119, -7.216e-05, -117.97818356, -0.00021649, -393.26061185, -0.00072164, 0.4, 0.3, 0.003, 0.0, 0.0, 11026, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1026, 99999, 'P', 41026, 'Vy', 31026, 'Vz', 21026, 'My', 11026, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171026, 71026, 171026, 1026, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122026, 122026, 22026, 1026, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171027, 7.7, 14.4, 3.2)
    ops.node(122027, 7.7, 14.4, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1027, 171027, 122027, 0.16, 26152220.18426416, 10896758.41011007, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21027, 123.77508574, 0.00092678, 150.7183243, 0.01528529, 15.07183243, 0.05074434, -123.77508574, -0.00092678, -150.7183243, -0.01528529, -15.07183243, -0.05074434, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11027, 104.76710808, 0.00092678, 127.57270881, 0.01528529, 12.75727088, 0.05074434, -104.76710808, -0.00092678, -127.57270881, -0.01528529, -12.75727088, -0.05074434, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21027, 1027, 0.0, 142.75057852, 0.0185356, 142.75057852, 0.05560679, 99.92540497, -1764.49519601, 0.05, 2, 0, 71027, 22027, 2, 3)
    ops.uniaxialMaterial('LimitState', 41027, 35.68764463, 7.246e-05, 107.06293389, 0.00021738, 356.8764463, 0.00072461, -35.68764463, -7.246e-05, -107.06293389, -0.00021738, -356.8764463, -0.00072461, 0.4, 0.3, 0.003, 0.0, 0.0, 21027, 2)
    ops.limitCurve('ThreePoint', 11027, 1027, 0.0, 142.75057852, 0.0185356, 142.75057852, 0.05560679, 99.92540497, -1764.49519601, 0.05, 2, 0, 71027, 22027, 1, 3)
    ops.uniaxialMaterial('LimitState', 31027, 35.68764463, 7.246e-05, 107.06293389, 0.00021738, 356.8764463, 0.00072461, -35.68764463, -7.246e-05, -107.06293389, -0.00021738, -356.8764463, -0.00072461, 0.4, 0.3, 0.003, 0.0, 0.0, 11027, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1027, 99999, 'P', 41027, 'Vy', 31027, 'Vz', 21027, 'My', 11027, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171027, 71027, 171027, 1027, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122027, 122027, 22027, 1027, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171028, 11.55, 14.4, 3.2)
    ops.node(122028, 11.55, 14.4, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1028, 171028, 122028, 0.1225, 28172494.4326057, 11738539.34691904, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21028, 81.86125747, 0.00100318, 99.30596757, 0.01678686, 9.93059676, 0.05696285, -81.86125747, -0.00100318, -99.30596757, -0.01678686, -9.93059676, -0.05696285, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11028, 81.86125747, 0.00100318, 99.30596757, 0.01678686, 9.93059676, 0.05696285, -81.86125747, -0.00100318, -99.30596757, -0.01678686, -9.93059676, -0.05696285, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21028, 1028, 0.0, 127.040586, 0.02006364, 127.040586, 0.06019092, 88.9284102, -1635.77096396, 0.05, 2, 0, 71028, 22028, 2, 3)
    ops.uniaxialMaterial('LimitState', 41028, 31.7601465, 7.819e-05, 95.2804395, 0.00023456, 317.60146499, 0.00078187, -31.7601465, -7.819e-05, -95.2804395, -0.00023456, -317.60146499, -0.00078187, 0.4, 0.3, 0.003, 0.0, 0.0, 21028, 2)
    ops.limitCurve('ThreePoint', 11028, 1028, 0.0, 127.040586, 0.02006364, 127.040586, 0.06019092, 88.9284102, -1635.77096396, 0.05, 2, 0, 71028, 22028, 1, 3)
    ops.uniaxialMaterial('LimitState', 31028, 31.7601465, 7.819e-05, 95.2804395, 0.00023456, 317.60146499, 0.00078187, -31.7601465, -7.819e-05, -95.2804395, -0.00023456, -317.60146499, -0.00078187, 0.4, 0.3, 0.003, 0.0, 0.0, 11028, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1028, 99999, 'P', 41028, 'Vy', 31028, 'Vz', 21028, 'My', 11028, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171028, 71028, 171028, 1028, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122028, 122028, 22028, 1028, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171029, 14.6, 14.4, 3.2)
    ops.node(122029, 14.6, 14.4, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1029, 171029, 122029, 0.1225, 26829606.16751771, 11179002.56979905, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21029, 83.98828044, 0.00100172, 102.06327571, 0.01930496, 10.20632757, 0.05772955, -83.98828044, -0.00100172, -102.06327571, -0.01930496, -10.20632757, -0.05772955, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11029, 83.98828044, 0.00100172, 102.06327571, 0.01930496, 10.20632757, 0.05772955, -83.98828044, -0.00100172, -102.06327571, -0.01930496, -10.20632757, -0.05772955, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21029, 1029, 0.0, 133.37071105, 0.02003442, 133.37071105, 0.06010327, 93.35949773, -2062.54948766, 0.05, 2, 0, 71029, 22029, 2, 3)
    ops.uniaxialMaterial('LimitState', 41029, 33.34267776, 8.619e-05, 100.02803329, 0.00025857, 333.42677762, 0.00086192, -33.34267776, -8.619e-05, -100.02803329, -0.00025857, -333.42677762, -0.00086192, 0.4, 0.3, 0.003, 0.0, 0.0, 21029, 2)
    ops.limitCurve('ThreePoint', 11029, 1029, 0.0, 133.37071105, 0.02003442, 133.37071105, 0.06010327, 93.35949773, -2062.54948766, 0.05, 2, 0, 71029, 22029, 1, 3)
    ops.uniaxialMaterial('LimitState', 31029, 33.34267776, 8.619e-05, 100.02803329, 0.00025857, 333.42677762, 0.00086192, -33.34267776, -8.619e-05, -100.02803329, -0.00025857, -333.42677762, -0.00086192, 0.4, 0.3, 0.003, 0.0, 0.0, 11029, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1029, 99999, 'P', 41029, 'Vy', 31029, 'Vz', 21029, 'My', 11029, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171029, 71029, 171029, 1029, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122029, 122029, 22029, 1029, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171030, 18.45, 14.4, 3.2)
    ops.node(122030, 18.45, 14.4, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1030, 171030, 122030, 0.16, 34109029.68749252, 14212095.70312188, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21030, 128.89057793, 0.00084629, 154.09097647, 0.01362921, 15.40909765, 0.05544391, -128.89057793, -0.00084629, -154.09097647, -0.01362921, -15.40909765, -0.05544391, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11030, 109.14925969, 0.00084629, 130.48987969, 0.01362921, 13.04898797, 0.05544391, -109.14925969, -0.00084629, -130.48987969, -0.01362921, -13.04898797, -0.05544391, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21030, 1030, 0.0, 179.88070215, 0.01692588, 179.88070215, 0.05077765, 125.91649151, -1717.06941592, 0.05, 2, 0, 71030, 22030, 2, 3)
    ops.uniaxialMaterial('LimitState', 41030, 44.97017554, 7.001e-05, 134.91052661, 0.00021003, 449.70175538, 0.00070008, -44.97017554, -7.001e-05, -134.91052661, -0.00021003, -449.70175538, -0.00070008, 0.4, 0.3, 0.003, 0.0, 0.0, 21030, 2)
    ops.limitCurve('ThreePoint', 11030, 1030, 0.0, 179.88070215, 0.01692588, 179.88070215, 0.05077765, 125.91649151, -1717.06941592, 0.05, 2, 0, 71030, 22030, 1, 3)
    ops.uniaxialMaterial('LimitState', 31030, 44.97017554, 7.001e-05, 134.91052661, 0.00021003, 449.70175538, 0.00070008, -44.97017554, -7.001e-05, -134.91052661, -0.00021003, -449.70175538, -0.00070008, 0.4, 0.3, 0.003, 0.0, 0.0, 11030, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1030, 99999, 'P', 41030, 'Vy', 31030, 'Vz', 21030, 'My', 11030, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171030, 71030, 171030, 1030, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122030, 122030, 22030, 1030, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171031, 22.3, 14.4, 3.2)
    ops.node(122031, 22.3, 14.4, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1031, 171031, 122031, 0.16, 32875036.15571297, 13697931.73154707, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21031, 130.65200468, 0.0008443, 156.85332296, 0.01526965, 15.6853323, 0.05645641, -130.65200468, -0.0008443, -156.85332296, -0.01526965, -15.6853323, -0.05645641, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11031, 109.67393687, 0.0008443, 131.66825479, 0.01526965, 13.16682548, 0.05645641, -109.67393687, -0.0008443, -131.66825479, -0.01526965, -13.16682548, -0.05645641, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21031, 1031, 0.0, 176.5906581, 0.0168859, 176.5906581, 0.05065771, 123.61346067, -1826.26287017, 0.05, 2, 0, 71031, 22031, 2, 3)
    ops.uniaxialMaterial('LimitState', 41031, 44.14766453, 7.131e-05, 132.44299358, 0.00021392, 441.47664526, 0.00071308, -44.14766453, -7.131e-05, -132.44299358, -0.00021392, -441.47664526, -0.00071308, 0.4, 0.3, 0.003, 0.0, 0.0, 21031, 2)
    ops.limitCurve('ThreePoint', 11031, 1031, 0.0, 176.5906581, 0.0168859, 176.5906581, 0.05065771, 123.61346067, -1826.26287017, 0.05, 2, 0, 71031, 22031, 1, 3)
    ops.uniaxialMaterial('LimitState', 31031, 44.14766453, 7.131e-05, 132.44299358, 0.00021392, 441.47664526, 0.00071308, -44.14766453, -7.131e-05, -132.44299358, -0.00021392, -441.47664526, -0.00071308, 0.4, 0.3, 0.003, 0.0, 0.0, 11031, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1031, 99999, 'P', 41031, 'Vy', 31031, 'Vz', 21031, 'My', 11031, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171031, 71031, 171031, 1031, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122031, 122031, 22031, 1031, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171032, 26.15, 14.4, 3.2)
    ops.node(122032, 26.15, 14.4, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1032, 171032, 122032, 0.09, 30873640.36597519, 12864016.81915633, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21032, 54.45938143, 0.00108237, 65.75104144, 0.01628631, 6.57510414, 0.06548881, -54.45938143, -0.00108237, -65.75104144, -0.01628631, -6.57510414, -0.06548881, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11032, 50.13309524, 0.00108237, 60.52773896, 0.01628631, 6.0527739, 0.06548881, -50.13309524, -0.00108237, -60.52773896, -0.01628631, -6.0527739, -0.06548881, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21032, 1032, 0.0, 104.64082753, 0.0216474, 104.64082753, 0.0649422, 73.24857927, -1440.14760292, 0.05, 2, 0, 71032, 22032, 2, 3)
    ops.uniaxialMaterial('LimitState', 41032, 26.16020688, 7.999e-05, 78.48062064, 0.00023996, 261.60206882, 0.00079988, -26.16020688, -7.999e-05, -78.48062064, -0.00023996, -261.60206882, -0.00079988, 0.4, 0.3, 0.003, 0.0, 0.0, 21032, 2)
    ops.limitCurve('ThreePoint', 11032, 1032, 0.0, 104.64082753, 0.0216474, 104.64082753, 0.0649422, 73.24857927, -1440.14760292, 0.05, 2, 0, 71032, 22032, 1, 3)
    ops.uniaxialMaterial('LimitState', 31032, 26.16020688, 7.999e-05, 78.48062064, 0.00023996, 261.60206882, 0.00079988, -26.16020688, -7.999e-05, -78.48062064, -0.00023996, -261.60206882, -0.00079988, 0.4, 0.3, 0.003, 0.0, 0.0, 11032, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1032, 99999, 'P', 41032, 'Vy', 31032, 'Vz', 21032, 'My', 11032, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171032, 71032, 171032, 1032, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122032, 122032, 22032, 1032, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172001, 0.0, 0.0, 6.15)
    ops.node(123001, 0.0, 0.0, 8.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2001, 172001, 123001, 0.0625, 29809683.56008601, 12420701.48336917, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22001, 30.44006106, 0.00123453, 36.87333409, 0.02132173, 3.68733341, 0.07822417, -30.44006106, -0.00123453, -36.87333409, -0.02132173, -3.68733341, -0.07822417, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12001, 30.44006106, 0.00123453, 36.87333409, 0.02132173, 3.68733341, 0.07822417, -30.44006106, -0.00123453, -36.87333409, -0.02132173, -3.68733341, -0.07822417, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22001, 2001, 0.0, 81.4494955, 0.02469052, 81.4494955, 0.07407155, 57.01464685, -1646.7515054, 0.05, 2, 0, 72001, 23001, 2, 3)
    ops.uniaxialMaterial('LimitState', 42001, 20.36237387, 9.286e-05, 61.08712162, 0.00027857, 203.62373874, 0.00092855, -20.36237387, -9.286e-05, -61.08712162, -0.00027857, -203.62373874, -0.00092855, 0.4, 0.3, 0.003, 0.0, 0.0, 22001, 2)
    ops.limitCurve('ThreePoint', 12001, 2001, 0.0, 81.4494955, 0.02469052, 81.4494955, 0.07407155, 57.01464685, -1646.7515054, 0.05, 2, 0, 72001, 23001, 1, 3)
    ops.uniaxialMaterial('LimitState', 32001, 20.36237387, 9.286e-05, 61.08712162, 0.00027857, 203.62373874, 0.00092855, -20.36237387, -9.286e-05, -61.08712162, -0.00027857, -203.62373874, -0.00092855, 0.4, 0.3, 0.003, 0.0, 0.0, 12001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2001, 99999, 'P', 42001, 'Vy', 32001, 'Vz', 22001, 'My', 12001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172001, 72001, 172001, 2001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123001, 123001, 23001, 2001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172002, 3.85, 0.0, 6.15)
    ops.node(123002, 3.85, 0.0, 8.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2002, 172002, 123002, 0.1225, 30651788.08610618, 12771578.36921091, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22002, 69.0939669, 0.00088443, 83.56729172, 0.02022533, 8.35672917, 0.06547161, -69.0939669, -0.00088443, -83.56729172, -0.02022533, -8.35672917, -0.06547161, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12002, 80.19811823, 0.00088443, 96.99746364, 0.02022533, 9.69974636, 0.06547161, -80.19811823, -0.00088443, -96.99746364, -0.02022533, -9.69974636, -0.06547161, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22002, 2002, 0.0, 140.05076886, 0.01768856, 140.05076886, 0.05306568, 98.0355382, -2188.55657285, 0.05, 2, 0, 72002, 23002, 2, 3)
    ops.uniaxialMaterial('LimitState', 42002, 35.01269221, 7.922e-05, 105.03807664, 0.00023767, 350.12692215, 0.00079222, -35.01269221, -7.922e-05, -105.03807664, -0.00023767, -350.12692215, -0.00079222, 0.4, 0.3, 0.003, 0.0, 0.0, 22002, 2)
    ops.limitCurve('ThreePoint', 12002, 2002, 0.0, 140.05076886, 0.01768856, 140.05076886, 0.05306568, 98.0355382, -2188.55657285, 0.05, 2, 0, 72002, 23002, 1, 3)
    ops.uniaxialMaterial('LimitState', 32002, 35.01269221, 7.922e-05, 105.03807664, 0.00023767, 350.12692215, 0.00079222, -35.01269221, -7.922e-05, -105.03807664, -0.00023767, -350.12692215, -0.00079222, 0.4, 0.3, 0.003, 0.0, 0.0, 12002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2002, 99999, 'P', 42002, 'Vy', 32002, 'Vz', 22002, 'My', 12002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172002, 72002, 172002, 2002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123002, 123002, 23002, 2002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172003, 7.7, 0.0, 6.15)
    ops.node(123003, 7.7, 0.0, 8.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2003, 172003, 123003, 0.1225, 27713405.78159033, 11547252.40899597, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22003, 69.19677433, 0.00094414, 84.22423637, 0.01914441, 8.42242364, 0.06204664, -69.19677433, -0.00094414, -84.22423637, -0.01914441, -8.42242364, -0.06204664, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12003, 80.22728456, 0.00094414, 97.65024226, 0.01914441, 9.76502423, 0.06204664, -80.22728456, -0.00094414, -97.65024226, -0.01914441, -9.76502423, -0.06204664, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22003, 2003, 0.0, 127.29640207, 0.01888284, 127.29640207, 0.05664851, 89.10748145, -2081.52474513, 0.05, 2, 0, 72003, 23003, 2, 3)
    ops.uniaxialMaterial('LimitState', 42003, 31.82410052, 7.964e-05, 95.47230155, 0.00023893, 318.24100517, 0.00079642, -31.82410052, -7.964e-05, -95.47230155, -0.00023893, -318.24100517, -0.00079642, 0.4, 0.3, 0.003, 0.0, 0.0, 22003, 2)
    ops.limitCurve('ThreePoint', 12003, 2003, 0.0, 127.29640207, 0.01888284, 127.29640207, 0.05664851, 89.10748145, -2081.52474513, 0.05, 2, 0, 72003, 23003, 1, 3)
    ops.uniaxialMaterial('LimitState', 32003, 31.82410052, 7.964e-05, 95.47230155, 0.00023893, 318.24100517, 0.00079642, -31.82410052, -7.964e-05, -95.47230155, -0.00023893, -318.24100517, -0.00079642, 0.4, 0.3, 0.003, 0.0, 0.0, 12003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2003, 99999, 'P', 42003, 'Vy', 32003, 'Vz', 22003, 'My', 12003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172003, 72003, 172003, 2003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123003, 123003, 23003, 2003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172006, 18.45, 0.0, 6.15)
    ops.node(123006, 18.45, 0.0, 8.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2006, 172006, 123006, 0.1225, 28408137.80361635, 11836724.08484015, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22006, 71.44118372, 0.00097405, 86.84690111, 0.01641525, 8.68469011, 0.05995585, -71.44118372, -0.00097405, -86.84690111, -0.01641525, -8.68469011, -0.05995585, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12006, 82.81393592, 0.00097405, 100.67209596, 0.01641525, 10.0672096, 0.05995585, -82.81393592, -0.00097405, -100.67209596, -0.01641525, -10.0672096, -0.05995585, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22006, 2006, 0.0, 118.81661849, 0.01948103, 118.81661849, 0.05844309, 83.17163294, -1581.06728733, 0.05, 2, 0, 72006, 23006, 2, 3)
    ops.uniaxialMaterial('LimitState', 42006, 29.70415462, 7.252e-05, 89.11246386, 0.00021756, 297.04154621, 0.00072519, -29.70415462, -7.252e-05, -89.11246386, -0.00021756, -297.04154621, -0.00072519, 0.4, 0.3, 0.003, 0.0, 0.0, 22006, 2)
    ops.limitCurve('ThreePoint', 12006, 2006, 0.0, 118.81661849, 0.01948103, 118.81661849, 0.05844309, 83.17163294, -1581.06728733, 0.05, 2, 0, 72006, 23006, 1, 3)
    ops.uniaxialMaterial('LimitState', 32006, 29.70415462, 7.252e-05, 89.11246386, 0.00021756, 297.04154621, 0.00072519, -29.70415462, -7.252e-05, -89.11246386, -0.00021756, -297.04154621, -0.00072519, 0.4, 0.3, 0.003, 0.0, 0.0, 12006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2006, 99999, 'P', 42006, 'Vy', 32006, 'Vz', 22006, 'My', 12006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172006, 72006, 172006, 2006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123006, 123006, 23006, 2006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172007, 22.3, 0.0, 6.15)
    ops.node(123007, 22.3, 0.0, 8.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2007, 172007, 123007, 0.1225, 29458187.76720933, 12274244.90300389, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22007, 68.80819704, 0.000995, 83.46335234, 0.01635313, 8.34633523, 0.06075392, -68.80819704, -0.000995, -83.46335234, -0.01635313, -8.34633523, -0.06075392, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12007, 77.90065051, 0.000995, 94.49236748, 0.01635313, 9.44923675, 0.06075392, -77.90065051, -0.000995, -94.49236748, -0.01635313, -9.44923675, -0.06075392, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22007, 2007, 0.0, 126.66863428, 0.0198999, 126.66863428, 0.0596997, 88.668044, -1760.17437394, 0.05, 2, 0, 72007, 23007, 2, 3)
    ops.uniaxialMaterial('LimitState', 42007, 31.66715857, 7.456e-05, 95.00147571, 0.00022367, 316.67158571, 0.00074556, -31.66715857, -7.456e-05, -95.00147571, -0.00022367, -316.67158571, -0.00074556, 0.4, 0.3, 0.003, 0.0, 0.0, 22007, 2)
    ops.limitCurve('ThreePoint', 12007, 2007, 0.0, 126.66863428, 0.0198999, 126.66863428, 0.0596997, 88.668044, -1760.17437394, 0.05, 2, 0, 72007, 23007, 1, 3)
    ops.uniaxialMaterial('LimitState', 32007, 31.66715857, 7.456e-05, 95.00147571, 0.00022367, 316.67158571, 0.00074556, -31.66715857, -7.456e-05, -95.00147571, -0.00022367, -316.67158571, -0.00074556, 0.4, 0.3, 0.003, 0.0, 0.0, 12007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2007, 99999, 'P', 42007, 'Vy', 32007, 'Vz', 22007, 'My', 12007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172007, 72007, 172007, 2007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123007, 123007, 23007, 2007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172008, 26.15, 0.0, 6.15)
    ops.node(123008, 26.15, 0.0, 8.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2008, 172008, 123008, 0.0625, 28711573.28921484, 11963155.53717285, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22008, 26.76371715, 0.00147899, 32.4955376, 0.01825307, 3.24955376, 0.07393625, -26.76371715, -0.00147899, -32.4955376, -0.01825307, -3.24955376, -0.07393625, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12008, 26.76371715, 0.00147899, 32.4955376, 0.01825307, 3.24955376, 0.07393625, -26.76371715, -0.00147899, -32.4955376, -0.01825307, -3.24955376, -0.07393625, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22008, 2008, 0.0, 65.61237834, 0.02957973, 65.61237834, 0.08873919, 45.92866484, -1203.3201632, 0.05, 2, 0, 72008, 23008, 2, 3)
    ops.uniaxialMaterial('LimitState', 42008, 16.40309459, 7.766e-05, 49.20928376, 0.00023298, 164.03094585, 0.00077661, -16.40309459, -7.766e-05, -49.20928376, -0.00023298, -164.03094585, -0.00077661, 0.4, 0.3, 0.003, 0.0, 0.0, 22008, 2)
    ops.limitCurve('ThreePoint', 12008, 2008, 0.0, 65.61237834, 0.02957973, 65.61237834, 0.08873919, 45.92866484, -1203.3201632, 0.05, 2, 0, 72008, 23008, 1, 3)
    ops.uniaxialMaterial('LimitState', 32008, 16.40309459, 7.766e-05, 49.20928376, 0.00023298, 164.03094585, 0.00077661, -16.40309459, -7.766e-05, -49.20928376, -0.00023298, -164.03094585, -0.00077661, 0.4, 0.3, 0.003, 0.0, 0.0, 12008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2008, 99999, 'P', 42008, 'Vy', 32008, 'Vz', 22008, 'My', 12008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172008, 72008, 172008, 2008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123008, 123008, 23008, 2008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172009, 0.0, 4.8, 6.15)
    ops.node(123009, 0.0, 4.8, 8.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2009, 172009, 123009, 0.1225, 26524091.41939091, 11051704.75807955, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22009, 83.90004829, 0.00097144, 102.27833005, 0.01860147, 10.22783301, 0.05996371, -83.90004829, -0.00097144, -102.27833005, -0.01860147, -10.22783301, -0.05996371, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12009, 71.77682847, 0.00097144, 87.49952237, 0.01860147, 8.74995224, 0.05996371, -71.77682847, -0.00097144, -87.49952237, -0.01860147, -8.74995224, -0.05996371, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22009, 2009, 0.0, 119.00853695, 0.01942878, 119.00853695, 0.05828634, 83.30597586, -1844.95191701, 0.05, 2, 0, 72009, 23009, 2, 3)
    ops.uniaxialMaterial('LimitState', 42009, 29.75213424, 7.78e-05, 89.25640271, 0.00023339, 297.52134237, 0.00077796, -29.75213424, -7.78e-05, -89.25640271, -0.00023339, -297.52134237, -0.00077796, 0.4, 0.3, 0.003, 0.0, 0.0, 22009, 2)
    ops.limitCurve('ThreePoint', 12009, 2009, 0.0, 119.00853695, 0.01942878, 119.00853695, 0.05828634, 83.30597586, -1844.95191701, 0.05, 2, 0, 72009, 23009, 1, 3)
    ops.uniaxialMaterial('LimitState', 32009, 29.75213424, 7.78e-05, 89.25640271, 0.00023339, 297.52134237, 0.00077796, -29.75213424, -7.78e-05, -89.25640271, -0.00023339, -297.52134237, -0.00077796, 0.4, 0.3, 0.003, 0.0, 0.0, 12009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2009, 99999, 'P', 42009, 'Vy', 32009, 'Vz', 22009, 'My', 12009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172009, 72009, 172009, 2009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123009, 123009, 23009, 2009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172010, 3.85, 4.8, 6.15)
    ops.node(123010, 3.85, 4.8, 8.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2010, 172010, 123010, 0.1225, 33340524.8414375, 13891885.35059896, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22010, 100.63118773, 0.00096319, 120.50889857, 0.0157921, 12.05088986, 0.05467033, -100.63118773, -0.00096319, -120.50889857, -0.0157921, -12.05088986, -0.05467033, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12010, 94.9160884, 0.00096319, 113.66489383, 0.0157921, 11.36648938, 0.05467033, -94.9160884, -0.00096319, -113.66489383, -0.0157921, -11.36648938, -0.05467033, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22010, 2010, 0.0, 139.11510015, 0.0192637, 139.11510015, 0.05779111, 97.38057011, -1336.18034054, 0.05, 2, 0, 72010, 23010, 2, 3)
    ops.uniaxialMaterial('LimitState', 42010, 34.77877504, 7.235e-05, 104.33632512, 0.00021704, 347.78775038, 0.00072347, -34.77877504, -7.235e-05, -104.33632512, -0.00021704, -347.78775038, -0.00072347, 0.4, 0.3, 0.003, 0.0, 0.0, 22010, 2)
    ops.limitCurve('ThreePoint', 12010, 2010, 0.0, 139.11510015, 0.0192637, 139.11510015, 0.05779111, 97.38057011, -1336.18034054, 0.05, 2, 0, 72010, 23010, 1, 3)
    ops.uniaxialMaterial('LimitState', 32010, 34.77877504, 7.235e-05, 104.33632512, 0.00021704, 347.78775038, 0.00072347, -34.77877504, -7.235e-05, -104.33632512, -0.00021704, -347.78775038, -0.00072347, 0.4, 0.3, 0.003, 0.0, 0.0, 12010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2010, 99999, 'P', 42010, 'Vy', 32010, 'Vz', 22010, 'My', 12010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172010, 72010, 172010, 2010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123010, 123010, 23010, 2010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172011, 7.7, 4.8, 6.15)
    ops.node(123011, 7.7, 4.8, 8.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2011, 172011, 123011, 0.1225, 29093011.75661206, 12122088.23192169, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22011, 104.09434453, 0.00104699, 126.00819579, 0.01904199, 12.60081958, 0.05461861, -104.09434453, -0.00104699, -126.00819579, -0.01904199, -12.60081958, -0.05461861, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12011, 97.78358828, 0.00104699, 118.3689046, 0.01904199, 11.83689046, 0.05461861, -97.78358828, -0.00104699, -118.3689046, -0.01904199, -11.83689046, -0.05461861, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22011, 2011, 0.0, 128.94098753, 0.02093985, 128.94098753, 0.06281954, 90.25869127, -1534.14031791, 0.05, 2, 0, 72011, 23011, 2, 3)
    ops.uniaxialMaterial('LimitState', 42011, 32.23524688, 7.685e-05, 96.70574065, 0.00023054, 322.35246883, 0.00076846, -32.23524688, -7.685e-05, -96.70574065, -0.00023054, -322.35246883, -0.00076846, 0.4, 0.3, 0.003, 0.0, 0.0, 22011, 2)
    ops.limitCurve('ThreePoint', 12011, 2011, 0.0, 128.94098753, 0.02093985, 128.94098753, 0.06281954, 90.25869127, -1534.14031791, 0.05, 2, 0, 72011, 23011, 1, 3)
    ops.uniaxialMaterial('LimitState', 32011, 32.23524688, 7.685e-05, 96.70574065, 0.00023054, 322.35246883, 0.00076846, -32.23524688, -7.685e-05, -96.70574065, -0.00023054, -322.35246883, -0.00076846, 0.4, 0.3, 0.003, 0.0, 0.0, 12011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2011, 99999, 'P', 42011, 'Vy', 32011, 'Vz', 22011, 'My', 12011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172011, 72011, 172011, 2011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123011, 123011, 23011, 2011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172012, 11.55, 4.8, 6.15)
    ops.node(123012, 11.55, 4.8, 8.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2012, 172012, 123012, 0.1225, 29369354.30670407, 12237230.96112669, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22012, 90.93652315, 0.00095374, 110.06301231, 0.01695049, 11.00630123, 0.05823228, -90.93652315, -0.00095374, -110.06301231, -0.01695049, -11.00630123, -0.05823228, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12012, 79.30597473, 0.00095374, 95.98623492, 0.01695049, 9.59862349, 0.05823228, -79.30597473, -0.00095374, -95.98623492, -0.01695049, -9.59862349, -0.05823228, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22012, 2012, 0.0, 131.86438333, 0.01907486, 131.86438333, 0.05722457, 92.30506833, -1633.98089829, 0.05, 2, 0, 72012, 23012, 2, 3)
    ops.uniaxialMaterial('LimitState', 42012, 32.96609583, 7.785e-05, 98.8982875, 0.00023355, 329.66095832, 0.00077849, -32.96609583, -7.785e-05, -98.8982875, -0.00023355, -329.66095832, -0.00077849, 0.4, 0.3, 0.003, 0.0, 0.0, 22012, 2)
    ops.limitCurve('ThreePoint', 12012, 2012, 0.0, 131.86438333, 0.01907486, 131.86438333, 0.05722457, 92.30506833, -1633.98089829, 0.05, 2, 0, 72012, 23012, 1, 3)
    ops.uniaxialMaterial('LimitState', 32012, 32.96609583, 7.785e-05, 98.8982875, 0.00023355, 329.66095832, 0.00077849, -32.96609583, -7.785e-05, -98.8982875, -0.00023355, -329.66095832, -0.00077849, 0.4, 0.3, 0.003, 0.0, 0.0, 12012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2012, 99999, 'P', 42012, 'Vy', 32012, 'Vz', 22012, 'My', 12012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172012, 72012, 172012, 2012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123012, 123012, 23012, 2012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172013, 14.6, 4.8, 6.15)
    ops.node(123013, 14.6, 4.8, 8.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2013, 172013, 123013, 0.1225, 28556396.76498147, 11898498.65207561, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22013, 89.58506632, 0.00104042, 108.58644851, 0.01923798, 10.85864485, 0.05961888, -89.58506632, -0.00104042, -108.58644851, -0.01923798, -10.85864485, -0.05961888, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12013, 79.32838639, 0.00104042, 96.15428215, 0.01923798, 9.61542822, 0.05961888, -79.32838639, -0.00104042, -96.15428215, -0.01923798, -9.61542822, -0.05961888, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22013, 2013, 0.0, 141.0129226, 0.02080833, 141.0129226, 0.062425, 98.70904582, -2096.93089907, 0.05, 2, 0, 72013, 23013, 2, 3)
    ops.uniaxialMaterial('LimitState', 42013, 35.25323065, 8.562e-05, 105.75969195, 0.00025686, 352.5323065, 0.0008562, -35.25323065, -8.562e-05, -105.75969195, -0.00025686, -352.5323065, -0.0008562, 0.4, 0.3, 0.003, 0.0, 0.0, 22013, 2)
    ops.limitCurve('ThreePoint', 12013, 2013, 0.0, 141.0129226, 0.02080833, 141.0129226, 0.062425, 98.70904582, -2096.93089907, 0.05, 2, 0, 72013, 23013, 1, 3)
    ops.uniaxialMaterial('LimitState', 32013, 35.25323065, 8.562e-05, 105.75969195, 0.00025686, 352.5323065, 0.0008562, -35.25323065, -8.562e-05, -105.75969195, -0.00025686, -352.5323065, -0.0008562, 0.4, 0.3, 0.003, 0.0, 0.0, 12013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2013, 99999, 'P', 42013, 'Vy', 32013, 'Vz', 22013, 'My', 12013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172013, 72013, 172013, 2013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123013, 123013, 23013, 2013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172014, 18.45, 4.8, 6.15)
    ops.node(123014, 18.45, 4.8, 8.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2014, 172014, 123014, 0.1225, 28238947.50153174, 11766228.12563823, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22014, 99.62845655, 0.00106419, 120.77254878, 0.01684106, 12.07725488, 0.05152601, -99.62845655, -0.00106419, -120.77254878, -0.01684106, -12.07725488, -0.05152601, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12014, 93.97724446, 0.00106419, 113.92198308, 0.01684106, 11.39219831, 0.05152601, -93.97724446, -0.00106419, -113.92198308, -0.01684106, -11.39219831, -0.05152601, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22014, 2014, 0.0, 118.71694199, 0.02128384, 118.71694199, 0.06385151, 83.10185939, -1301.90259138, 0.05, 2, 0, 72014, 23014, 2, 3)
    ops.uniaxialMaterial('LimitState', 42014, 29.6792355, 7.289e-05, 89.03770649, 0.00021868, 296.79235496, 0.00072892, -29.6792355, -7.289e-05, -89.03770649, -0.00021868, -296.79235496, -0.00072892, 0.4, 0.3, 0.003, 0.0, 0.0, 22014, 2)
    ops.limitCurve('ThreePoint', 12014, 2014, 0.0, 118.71694199, 0.02128384, 118.71694199, 0.06385151, 83.10185939, -1301.90259138, 0.05, 2, 0, 72014, 23014, 1, 3)
    ops.uniaxialMaterial('LimitState', 32014, 29.6792355, 7.289e-05, 89.03770649, 0.00021868, 296.79235496, 0.00072892, -29.6792355, -7.289e-05, -89.03770649, -0.00021868, -296.79235496, -0.00072892, 0.4, 0.3, 0.003, 0.0, 0.0, 12014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2014, 99999, 'P', 42014, 'Vy', 32014, 'Vz', 22014, 'My', 12014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172014, 72014, 172014, 2014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123014, 123014, 23014, 2014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172015, 22.3, 4.8, 6.15)
    ops.node(123015, 22.3, 4.8, 8.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2015, 172015, 123015, 0.1225, 28849828.05117931, 12020761.68799138, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22015, 104.55381232, 0.00104589, 126.61871671, 0.01810518, 12.66187167, 0.05343725, -104.55381232, -0.00104589, -126.61871671, -0.01810518, -12.66187167, -0.05343725, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12015, 98.12853653, 0.00104589, 118.83745884, 0.01810518, 11.88374588, 0.05343725, -98.12853653, -0.00104589, -118.83745884, -0.01810518, -11.88374588, -0.05343725, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22015, 2015, 0.0, 127.23236109, 0.02091773, 127.23236109, 0.0627532, 89.06265277, -1506.42818286, 0.05, 2, 0, 72015, 23015, 2, 3)
    ops.uniaxialMaterial('LimitState', 42015, 31.80809027, 7.647e-05, 95.42427082, 0.0002294, 318.08090274, 0.00076467, -31.80809027, -7.647e-05, -95.42427082, -0.0002294, -318.08090274, -0.00076467, 0.4, 0.3, 0.003, 0.0, 0.0, 22015, 2)
    ops.limitCurve('ThreePoint', 12015, 2015, 0.0, 127.23236109, 0.02091773, 127.23236109, 0.0627532, 89.06265277, -1506.42818286, 0.05, 2, 0, 72015, 23015, 1, 3)
    ops.uniaxialMaterial('LimitState', 32015, 31.80809027, 7.647e-05, 95.42427082, 0.0002294, 318.08090274, 0.00076467, -31.80809027, -7.647e-05, -95.42427082, -0.0002294, -318.08090274, -0.00076467, 0.4, 0.3, 0.003, 0.0, 0.0, 12015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2015, 99999, 'P', 42015, 'Vy', 32015, 'Vz', 22015, 'My', 12015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172015, 72015, 172015, 2015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123015, 123015, 23015, 2015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172016, 26.15, 4.8, 6.15)
    ops.node(123016, 26.15, 4.8, 8.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2016, 172016, 123016, 0.1225, 31096026.82304648, 12956677.84293604, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22016, 82.59001559, 0.0009306, 99.7573784, 0.01929001, 9.97573784, 0.06462697, -82.59001559, -0.0009306, -99.7573784, -0.01929001, -9.97573784, -0.06462697, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12016, 71.57113479, 0.0009306, 86.44808606, 0.01929001, 8.64480861, 0.06462697, -71.57113479, -0.0009306, -86.44808606, -0.01929001, -8.64480861, -0.06462697, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22016, 2016, 0.0, 141.07863608, 0.01861199, 141.07863608, 0.05583598, 98.75504526, -2112.37227868, 0.05, 2, 0, 72016, 23016, 2, 3)
    ops.uniaxialMaterial('LimitState', 42016, 35.26965902, 7.866e-05, 105.80897706, 0.00023599, 352.69659021, 0.00078664, -35.26965902, -7.866e-05, -105.80897706, -0.00023599, -352.69659021, -0.00078664, 0.4, 0.3, 0.003, 0.0, 0.0, 22016, 2)
    ops.limitCurve('ThreePoint', 12016, 2016, 0.0, 141.07863608, 0.01861199, 141.07863608, 0.05583598, 98.75504526, -2112.37227868, 0.05, 2, 0, 72016, 23016, 1, 3)
    ops.uniaxialMaterial('LimitState', 32016, 35.26965902, 7.866e-05, 105.80897706, 0.00023599, 352.69659021, 0.00078664, -35.26965902, -7.866e-05, -105.80897706, -0.00023599, -352.69659021, -0.00078664, 0.4, 0.3, 0.003, 0.0, 0.0, 12016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2016, 99999, 'P', 42016, 'Vy', 32016, 'Vz', 22016, 'My', 12016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172016, 72016, 172016, 2016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123016, 123016, 23016, 2016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172017, 0.0, 9.6, 6.15)
    ops.node(123017, 0.0, 9.6, 8.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2017, 172017, 123017, 0.1225, 30488544.4621688, 12703560.19257033, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22017, 82.89729687, 0.00100919, 100.29184363, 0.0164097, 10.02918436, 0.0613797, -82.89729687, -0.00100919, -100.29184363, -0.0164097, -10.02918436, -0.0613797, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12017, 72.6546446, 0.00100919, 87.89995005, 0.0164097, 8.78999501, 0.0613797, -72.6546446, -0.00100919, -87.89995005, -0.0164097, -8.78999501, -0.0613797, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22017, 2017, 0.0, 130.2607938, 0.0201837, 130.2607938, 0.0605511, 91.18255566, -1723.70154331, 0.05, 2, 0, 72017, 23017, 2, 3)
    ops.uniaxialMaterial('LimitState', 42017, 32.56519845, 7.408e-05, 97.69559535, 0.00022224, 325.65198451, 0.00074079, -32.56519845, -7.408e-05, -97.69559535, -0.00022224, -325.65198451, -0.00074079, 0.4, 0.3, 0.003, 0.0, 0.0, 22017, 2)
    ops.limitCurve('ThreePoint', 12017, 2017, 0.0, 130.2607938, 0.0201837, 130.2607938, 0.0605511, 91.18255566, -1723.70154331, 0.05, 2, 0, 72017, 23017, 1, 3)
    ops.uniaxialMaterial('LimitState', 32017, 32.56519845, 7.408e-05, 97.69559535, 0.00022224, 325.65198451, 0.00074079, -32.56519845, -7.408e-05, -97.69559535, -0.00022224, -325.65198451, -0.00074079, 0.4, 0.3, 0.003, 0.0, 0.0, 12017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2017, 99999, 'P', 42017, 'Vy', 32017, 'Vz', 22017, 'My', 12017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172017, 72017, 172017, 2017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123017, 123017, 23017, 2017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172018, 3.85, 9.6, 6.15)
    ops.node(123018, 3.85, 9.6, 8.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2018, 172018, 123018, 0.1225, 28815020.79176477, 12006258.66323532, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22018, 96.13922181, 0.00110226, 116.44176418, 0.01813396, 11.64417642, 0.05348918, -96.13922181, -0.00110226, -116.44176418, -0.01813396, -11.64417642, -0.05348918, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12018, 91.32046691, 0.00110226, 110.60539156, 0.01813396, 11.06053916, 0.05348918, -91.32046691, -0.00110226, -110.60539156, -0.01813396, -11.06053916, -0.05348918, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22018, 2018, 0.0, 124.60061422, 0.02204523, 124.60061422, 0.06613568, 87.22042995, -1427.30749589, 0.05, 2, 0, 72018, 23018, 2, 3)
    ops.uniaxialMaterial('LimitState', 42018, 31.15015356, 7.498e-05, 93.45046067, 0.00022493, 311.50153555, 0.00074976, -31.15015356, -7.498e-05, -93.45046067, -0.00022493, -311.50153555, -0.00074976, 0.4, 0.3, 0.003, 0.0, 0.0, 22018, 2)
    ops.limitCurve('ThreePoint', 12018, 2018, 0.0, 124.60061422, 0.02204523, 124.60061422, 0.06613568, 87.22042995, -1427.30749589, 0.05, 2, 0, 72018, 23018, 1, 3)
    ops.uniaxialMaterial('LimitState', 32018, 31.15015356, 7.498e-05, 93.45046067, 0.00022493, 311.50153555, 0.00074976, -31.15015356, -7.498e-05, -93.45046067, -0.00022493, -311.50153555, -0.00074976, 0.4, 0.3, 0.003, 0.0, 0.0, 12018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2018, 99999, 'P', 42018, 'Vy', 32018, 'Vz', 22018, 'My', 12018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172018, 72018, 172018, 2018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123018, 123018, 23018, 2018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172019, 7.7, 9.6, 6.15)
    ops.node(123019, 7.7, 9.6, 8.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2019, 172019, 123019, 0.1225, 25682464.47562659, 10701026.86484441, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22019, 93.13939784, 0.00108867, 113.20125981, 0.01878953, 11.32012598, 0.05025401, -93.13939784, -0.00108867, -113.20125981, -0.01878953, -11.32012598, -0.05025401, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12019, 88.18253377, 0.00108867, 107.17670662, 0.01878953, 10.71767066, 0.05025401, -88.18253377, -0.00108867, -107.17670662, -0.01878953, -10.71767066, -0.05025401, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22019, 2019, 0.0, 116.23799274, 0.02177335, 116.23799274, 0.06532006, 81.36659492, -1516.85238802, 0.05, 2, 0, 72019, 23019, 2, 3)
    ops.uniaxialMaterial('LimitState', 42019, 29.05949819, 7.847e-05, 87.17849456, 0.00023542, 290.59498186, 0.00078475, -29.05949819, -7.847e-05, -87.17849456, -0.00023542, -290.59498186, -0.00078475, 0.4, 0.3, 0.003, 0.0, 0.0, 22019, 2)
    ops.limitCurve('ThreePoint', 12019, 2019, 0.0, 116.23799274, 0.02177335, 116.23799274, 0.06532006, 81.36659492, -1516.85238802, 0.05, 2, 0, 72019, 23019, 1, 3)
    ops.uniaxialMaterial('LimitState', 32019, 29.05949819, 7.847e-05, 87.17849456, 0.00023542, 290.59498186, 0.00078475, -29.05949819, -7.847e-05, -87.17849456, -0.00023542, -290.59498186, -0.00078475, 0.4, 0.3, 0.003, 0.0, 0.0, 12019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2019, 99999, 'P', 42019, 'Vy', 32019, 'Vz', 22019, 'My', 12019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172019, 72019, 172019, 2019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123019, 123019, 23019, 2019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172020, 11.55, 9.6, 6.15)
    ops.node(123020, 11.55, 9.6, 8.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2020, 172020, 123020, 0.1225, 30854831.70625789, 12856179.87760746, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22020, 88.94593637, 0.00097407, 107.35244422, 0.01756759, 10.73524442, 0.06088398, -88.94593637, -0.00097407, -107.35244422, -0.01756759, -10.73524442, -0.06088398, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12020, 78.07041372, 0.00097407, 94.22633654, 0.01756759, 9.42263365, 0.06088398, -78.07041372, -0.00097407, -94.22633654, -0.01756759, -9.42263365, -0.06088398, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22020, 2020, 0.0, 142.86991614, 0.01948145, 142.86991614, 0.05844434, 100.0089413, -1910.61555946, 0.05, 2, 0, 72020, 23020, 2, 3)
    ops.uniaxialMaterial('LimitState', 42020, 35.71747904, 8.029e-05, 107.15243711, 0.00024086, 357.17479036, 0.00080285, -35.71747904, -8.029e-05, -107.15243711, -0.00024086, -357.17479036, -0.00080285, 0.4, 0.3, 0.003, 0.0, 0.0, 22020, 2)
    ops.limitCurve('ThreePoint', 12020, 2020, 0.0, 142.86991614, 0.01948145, 142.86991614, 0.05844434, 100.0089413, -1910.61555946, 0.05, 2, 0, 72020, 23020, 1, 3)
    ops.uniaxialMaterial('LimitState', 32020, 35.71747904, 8.029e-05, 107.15243711, 0.00024086, 357.17479036, 0.00080285, -35.71747904, -8.029e-05, -107.15243711, -0.00024086, -357.17479036, -0.00080285, 0.4, 0.3, 0.003, 0.0, 0.0, 12020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2020, 99999, 'P', 42020, 'Vy', 32020, 'Vz', 22020, 'My', 12020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172020, 72020, 172020, 2020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123020, 123020, 23020, 2020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172021, 14.6, 9.6, 6.15)
    ops.node(123021, 14.6, 9.6, 8.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2021, 172021, 123021, 0.1225, 28288923.7208566, 11787051.55035692, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22021, 91.24790783, 0.00098892, 110.71903867, 0.01593182, 11.07190387, 0.05675199, -91.24790783, -0.00098892, -110.71903867, -0.01593182, -11.07190387, -0.05675199, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12021, 79.06608249, 0.00098892, 95.93776837, 0.01593182, 9.59377684, 0.05675199, -79.06608249, -0.00098892, -95.93776837, -0.01593182, -9.59377684, -0.05675199, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22021, 2021, 0.0, 125.83864686, 0.01977832, 125.83864686, 0.05933495, 88.0870528, -1616.83192446, 0.05, 2, 0, 72021, 23021, 2, 3)
    ops.uniaxialMaterial('LimitState', 42021, 31.45966172, 7.713e-05, 94.37898515, 0.00023139, 314.59661716, 0.00077129, -31.45966172, -7.713e-05, -94.37898515, -0.00023139, -314.59661716, -0.00077129, 0.4, 0.3, 0.003, 0.0, 0.0, 22021, 2)
    ops.limitCurve('ThreePoint', 12021, 2021, 0.0, 125.83864686, 0.01977832, 125.83864686, 0.05933495, 88.0870528, -1616.83192446, 0.05, 2, 0, 72021, 23021, 1, 3)
    ops.uniaxialMaterial('LimitState', 32021, 31.45966172, 7.713e-05, 94.37898515, 0.00023139, 314.59661716, 0.00077129, -31.45966172, -7.713e-05, -94.37898515, -0.00023139, -314.59661716, -0.00077129, 0.4, 0.3, 0.003, 0.0, 0.0, 12021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2021, 99999, 'P', 42021, 'Vy', 32021, 'Vz', 22021, 'My', 12021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172021, 72021, 172021, 2021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123021, 123021, 23021, 2021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172022, 18.45, 9.6, 6.15)
    ops.node(123022, 18.45, 9.6, 8.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2022, 172022, 123022, 0.1225, 29721660.9941299, 12384025.41422079, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22022, 95.09656819, 0.00102904, 114.98310408, 0.01838238, 11.49831041, 0.05461312, -95.09656819, -0.00102904, -114.98310408, -0.01838238, -11.49831041, -0.05461312, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12022, 90.15002462, 0.00102904, 109.00214236, 0.01838238, 10.90021424, 0.05461312, -90.15002462, -0.00102904, -109.00214236, -0.01838238, -10.90021424, -0.05461312, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22022, 2022, 0.0, 127.56242712, 0.02058087, 127.56242712, 0.0617426, 89.29369898, -1415.21473919, 0.05, 2, 0, 72022, 23022, 2, 3)
    ops.uniaxialMaterial('LimitState', 42022, 31.89060678, 7.442e-05, 95.67182034, 0.00022325, 318.90606779, 0.00074416, -31.89060678, -7.442e-05, -95.67182034, -0.00022325, -318.90606779, -0.00074416, 0.4, 0.3, 0.003, 0.0, 0.0, 22022, 2)
    ops.limitCurve('ThreePoint', 12022, 2022, 0.0, 127.56242712, 0.02058087, 127.56242712, 0.0617426, 89.29369898, -1415.21473919, 0.05, 2, 0, 72022, 23022, 1, 3)
    ops.uniaxialMaterial('LimitState', 32022, 31.89060678, 7.442e-05, 95.67182034, 0.00022325, 318.90606779, 0.00074416, -31.89060678, -7.442e-05, -95.67182034, -0.00022325, -318.90606779, -0.00074416, 0.4, 0.3, 0.003, 0.0, 0.0, 12022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2022, 99999, 'P', 42022, 'Vy', 32022, 'Vz', 22022, 'My', 12022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172022, 72022, 172022, 2022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123022, 123022, 23022, 2022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172023, 22.3, 9.6, 6.15)
    ops.node(123023, 22.3, 9.6, 8.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2023, 172023, 123023, 0.1225, 26109851.63553866, 10879104.84814111, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22023, 102.96331625, 0.00113258, 125.11163201, 0.01583171, 12.5111632, 0.04791856, -102.96331625, -0.00113258, -125.11163201, -0.01583171, -12.5111632, -0.04791856, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12023, 96.77072768, 0.00113258, 117.58696312, 0.01583171, 11.75869631, 0.04791856, -96.77072768, -0.00113258, -117.58696312, -0.01583171, -11.75869631, -0.04791856, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22023, 2023, 0.0, 111.07624314, 0.02265164, 111.07624314, 0.06795491, 77.7533702, -1300.75046298, 0.05, 2, 0, 72023, 23023, 2, 3)
    ops.uniaxialMaterial('LimitState', 42023, 27.76906079, 7.376e-05, 83.30718236, 0.00022129, 277.69060786, 0.00073762, -27.76906079, -7.376e-05, -83.30718236, -0.00022129, -277.69060786, -0.00073762, 0.4, 0.3, 0.003, 0.0, 0.0, 22023, 2)
    ops.limitCurve('ThreePoint', 12023, 2023, 0.0, 111.07624314, 0.02265164, 111.07624314, 0.06795491, 77.7533702, -1300.75046298, 0.05, 2, 0, 72023, 23023, 1, 3)
    ops.uniaxialMaterial('LimitState', 32023, 27.76906079, 7.376e-05, 83.30718236, 0.00022129, 277.69060786, 0.00073762, -27.76906079, -7.376e-05, -83.30718236, -0.00022129, -277.69060786, -0.00073762, 0.4, 0.3, 0.003, 0.0, 0.0, 12023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2023, 99999, 'P', 42023, 'Vy', 32023, 'Vz', 22023, 'My', 12023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172023, 72023, 172023, 2023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123023, 123023, 23023, 2023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172024, 26.15, 9.6, 6.15)
    ops.node(123024, 26.15, 9.6, 8.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2024, 172024, 123024, 0.1225, 30098005.68731456, 12540835.70304773, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22024, 80.97702062, 0.00096925, 98.06389085, 0.01928074, 9.80638908, 0.06397636, -80.97702062, -0.00096925, -98.06389085, -0.01928074, -9.80638908, -0.06397636, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12024, 70.77604493, 0.00096925, 85.71041873, 0.01928074, 8.57104187, 0.06397636, -70.77604493, -0.00096925, -85.71041873, -0.01928074, -8.57104187, -0.06397636, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22024, 2024, 0.0, 138.81585031, 0.01938499, 138.81585031, 0.05815497, 97.17109522, -2191.03770213, 0.05, 2, 0, 72024, 23024, 2, 3)
    ops.uniaxialMaterial('LimitState', 42024, 34.70396258, 7.997e-05, 104.11188773, 0.00023991, 347.03962577, 0.00079969, -34.70396258, -7.997e-05, -104.11188773, -0.00023991, -347.03962577, -0.00079969, 0.4, 0.3, 0.003, 0.0, 0.0, 22024, 2)
    ops.limitCurve('ThreePoint', 12024, 2024, 0.0, 138.81585031, 0.01938499, 138.81585031, 0.05815497, 97.17109522, -2191.03770213, 0.05, 2, 0, 72024, 23024, 1, 3)
    ops.uniaxialMaterial('LimitState', 32024, 34.70396258, 7.997e-05, 104.11188773, 0.00023991, 347.03962577, 0.00079969, -34.70396258, -7.997e-05, -104.11188773, -0.00023991, -347.03962577, -0.00079969, 0.4, 0.3, 0.003, 0.0, 0.0, 12024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2024, 99999, 'P', 42024, 'Vy', 32024, 'Vz', 22024, 'My', 12024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172024, 72024, 172024, 2024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123024, 123024, 23024, 2024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172025, 0.0, 14.4, 6.15)
    ops.node(123025, 0.0, 14.4, 8.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2025, 172025, 123025, 0.0625, 28852692.34581239, 12021955.1440885, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22025, 30.16190793, 0.00125017, 36.61134321, 0.02028406, 3.66113432, 0.07613375, -30.16190793, -0.00125017, -36.61134321, -0.02028406, -3.66113432, -0.07613375, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12025, 30.16190793, 0.00125017, 36.61134321, 0.02028406, 3.66113432, 0.07613375, -30.16190793, -0.00125017, -36.61134321, -0.02028406, -3.66113432, -0.07613375, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22025, 2025, 0.0, 77.28566617, 0.02500335, 77.28566617, 0.07501006, 54.09996632, -1511.36733589, 0.05, 2, 0, 72025, 23025, 2, 3)
    ops.uniaxialMaterial('LimitState', 42025, 19.32141654, 9.103e-05, 57.96424963, 0.00027309, 193.21416542, 0.00091031, -19.32141654, -9.103e-05, -57.96424963, -0.00027309, -193.21416542, -0.00091031, 0.4, 0.3, 0.003, 0.0, 0.0, 22025, 2)
    ops.limitCurve('ThreePoint', 12025, 2025, 0.0, 77.28566617, 0.02500335, 77.28566617, 0.07501006, 54.09996632, -1511.36733589, 0.05, 2, 0, 72025, 23025, 1, 3)
    ops.uniaxialMaterial('LimitState', 32025, 19.32141654, 9.103e-05, 57.96424963, 0.00027309, 193.21416542, 0.00091031, -19.32141654, -9.103e-05, -57.96424963, -0.00027309, -193.21416542, -0.00091031, 0.4, 0.3, 0.003, 0.0, 0.0, 12025, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2025, 99999, 'P', 42025, 'Vy', 32025, 'Vz', 22025, 'My', 12025, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172025, 72025, 172025, 2025, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123025, 123025, 23025, 2025, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172026, 3.85, 14.4, 6.15)
    ops.node(123026, 3.85, 14.4, 8.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2026, 172026, 123026, 0.1225, 29338774.27776011, 12224489.28240005, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22026, 70.67325551, 0.0009081, 85.74845209, 0.01619042, 8.57484521, 0.06049923, -70.67325551, -0.0009081, -85.74845209, -0.01619042, -8.57484521, -0.06049923, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12026, 82.58894422, 0.0009081, 100.20585688, 0.01619042, 10.02058569, 0.06049923, -82.58894422, -0.0009081, -100.20585688, -0.01619042, -10.02058569, -0.06049923, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22026, 2026, 0.0, 124.36459763, 0.01816206, 124.36459763, 0.05448619, 87.05521834, -1676.93888382, 0.05, 2, 0, 72026, 23026, 2, 3)
    ops.uniaxialMaterial('LimitState', 42026, 31.09114941, 7.35e-05, 93.27344822, 0.00022049, 310.91149408, 0.00073498, -31.09114941, -7.35e-05, -93.27344822, -0.00022049, -310.91149408, -0.00073498, 0.4, 0.3, 0.003, 0.0, 0.0, 22026, 2)
    ops.limitCurve('ThreePoint', 12026, 2026, 0.0, 124.36459763, 0.01816206, 124.36459763, 0.05448619, 87.05521834, -1676.93888382, 0.05, 2, 0, 72026, 23026, 1, 3)
    ops.uniaxialMaterial('LimitState', 32026, 31.09114941, 7.35e-05, 93.27344822, 0.00022049, 310.91149408, 0.00073498, -31.09114941, -7.35e-05, -93.27344822, -0.00022049, -310.91149408, -0.00073498, 0.4, 0.3, 0.003, 0.0, 0.0, 12026, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2026, 99999, 'P', 42026, 'Vy', 32026, 'Vz', 22026, 'My', 12026, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172026, 72026, 172026, 2026, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123026, 123026, 23026, 2026, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172027, 7.7, 14.4, 6.15)
    ops.node(123027, 7.7, 14.4, 8.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2027, 172027, 123027, 0.1225, 28975582.9105846, 12073159.54607692, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22027, 72.11310578, 0.00100619, 87.5638867, 0.01702527, 8.75638867, 0.06104539, -72.11310578, -0.00100619, -87.5638867, -0.01702527, -8.75638867, -0.06104539, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12027, 82.9788343, 0.00100619, 100.75768013, 0.01702527, 10.07576801, 0.06104539, -82.9788343, -0.00100619, -100.75768013, -0.01702527, -10.07576801, -0.06104539, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22027, 2027, 0.0, 127.19697864, 0.02012383, 127.19697864, 0.0603715, 89.03788505, -1863.83521144, 0.05, 2, 0, 72027, 23027, 2, 3)
    ops.uniaxialMaterial('LimitState', 42027, 31.79924466, 7.611e-05, 95.39773398, 0.00022834, 317.9924466, 0.00076114, -31.79924466, -7.611e-05, -95.39773398, -0.00022834, -317.9924466, -0.00076114, 0.4, 0.3, 0.003, 0.0, 0.0, 22027, 2)
    ops.limitCurve('ThreePoint', 12027, 2027, 0.0, 127.19697864, 0.02012383, 127.19697864, 0.0603715, 89.03788505, -1863.83521144, 0.05, 2, 0, 72027, 23027, 1, 3)
    ops.uniaxialMaterial('LimitState', 32027, 31.79924466, 7.611e-05, 95.39773398, 0.00022834, 317.9924466, 0.00076114, -31.79924466, -7.611e-05, -95.39773398, -0.00022834, -317.9924466, -0.00076114, 0.4, 0.3, 0.003, 0.0, 0.0, 12027, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2027, 99999, 'P', 42027, 'Vy', 32027, 'Vz', 22027, 'My', 12027, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172027, 72027, 172027, 2027, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123027, 123027, 23027, 2027, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172028, 11.55, 14.4, 6.15)
    ops.node(123028, 11.55, 14.4, 8.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2028, 172028, 123028, 0.0625, 28684934.03595847, 11952055.84831603, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22028, 33.96767467, 0.00129423, 41.10581597, 0.01776293, 4.1105816, 0.06809995, -33.96767467, -0.00129423, -41.10581597, -0.01776293, -4.1105816, -0.06809995, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12028, 33.96767467, 0.00129423, 41.10581597, 0.01776293, 4.1105816, 0.06809995, -33.96767467, -0.00129423, -41.10581597, -0.01776293, -4.1105816, -0.06809995, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22028, 2028, 0.0, 75.8800026, 0.02588464, 75.8800026, 0.07765392, 53.11600182, -1188.1264696, 0.05, 2, 0, 72028, 23028, 2, 3)
    ops.uniaxialMaterial('LimitState', 42028, 18.97000065, 8.99e-05, 56.91000195, 0.00026969, 189.7000065, 0.00089898, -18.97000065, -8.99e-05, -56.91000195, -0.00026969, -189.7000065, -0.00089898, 0.4, 0.3, 0.003, 0.0, 0.0, 22028, 2)
    ops.limitCurve('ThreePoint', 12028, 2028, 0.0, 75.8800026, 0.02588464, 75.8800026, 0.07765392, 53.11600182, -1188.1264696, 0.05, 2, 0, 72028, 23028, 1, 3)
    ops.uniaxialMaterial('LimitState', 32028, 18.97000065, 8.99e-05, 56.91000195, 0.00026969, 189.7000065, 0.00089898, -18.97000065, -8.99e-05, -56.91000195, -0.00026969, -189.7000065, -0.00089898, 0.4, 0.3, 0.003, 0.0, 0.0, 12028, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2028, 99999, 'P', 42028, 'Vy', 32028, 'Vz', 22028, 'My', 12028, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172028, 72028, 172028, 2028, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123028, 123028, 23028, 2028, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172029, 14.6, 14.4, 6.15)
    ops.node(123029, 14.6, 14.4, 8.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2029, 172029, 123029, 0.0625, 29578212.84340128, 12324255.3514172, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22029, 33.27837099, 0.00130793, 40.21014573, 0.01727962, 4.02101457, 0.06903072, -33.27837099, -0.00130793, -40.21014573, -0.01727962, -4.02101457, -0.06903072, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12029, 33.27837099, 0.00130793, 40.21014573, 0.01727962, 4.02101457, 0.06903072, -33.27837099, -0.00130793, -40.21014573, -0.01727962, -4.02101457, -0.06903072, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22029, 2029, 0.0, 73.48877291, 0.02615852, 73.48877291, 0.07847556, 51.44214104, -1145.71886408, 0.05, 2, 0, 72029, 23029, 2, 3)
    ops.uniaxialMaterial('LimitState', 42029, 18.37219323, 8.444e-05, 55.11657968, 0.00025331, 183.72193228, 0.00084435, -18.37219323, -8.444e-05, -55.11657968, -0.00025331, -183.72193228, -0.00084435, 0.4, 0.3, 0.003, 0.0, 0.0, 22029, 2)
    ops.limitCurve('ThreePoint', 12029, 2029, 0.0, 73.48877291, 0.02615852, 73.48877291, 0.07847556, 51.44214104, -1145.71886408, 0.05, 2, 0, 72029, 23029, 1, 3)
    ops.uniaxialMaterial('LimitState', 32029, 18.37219323, 8.444e-05, 55.11657968, 0.00025331, 183.72193228, 0.00084435, -18.37219323, -8.444e-05, -55.11657968, -0.00025331, -183.72193228, -0.00084435, 0.4, 0.3, 0.003, 0.0, 0.0, 12029, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2029, 99999, 'P', 42029, 'Vy', 32029, 'Vz', 22029, 'My', 12029, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172029, 72029, 172029, 2029, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123029, 123029, 23029, 2029, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172030, 18.45, 14.4, 6.15)
    ops.node(123030, 18.45, 14.4, 8.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2030, 172030, 123030, 0.1225, 32946150.86175956, 13727562.85906648, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22030, 73.93891825, 0.00094107, 88.82164722, 0.0164116, 8.88216472, 0.06296578, -73.93891825, -0.00094107, -88.82164722, -0.0164116, -8.88216472, -0.06296578, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12030, 85.66729905, 0.00094107, 102.91076466, 0.0164116, 10.29107647, 0.06296578, -85.66729905, -0.00094107, -102.91076466, -0.0164116, -10.29107647, -0.06296578, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22030, 2030, 0.0, 141.13374971, 0.01882142, 141.13374971, 0.05646425, 98.7936248, -1821.65192944, 0.05, 2, 0, 72030, 23030, 2, 3)
    ops.uniaxialMaterial('LimitState', 42030, 35.28343743, 7.428e-05, 105.85031228, 0.00022283, 352.83437428, 0.00074275, -35.28343743, -7.428e-05, -105.85031228, -0.00022283, -352.83437428, -0.00074275, 0.4, 0.3, 0.003, 0.0, 0.0, 22030, 2)
    ops.limitCurve('ThreePoint', 12030, 2030, 0.0, 141.13374971, 0.01882142, 141.13374971, 0.05646425, 98.7936248, -1821.65192944, 0.05, 2, 0, 72030, 23030, 1, 3)
    ops.uniaxialMaterial('LimitState', 32030, 35.28343743, 7.428e-05, 105.85031228, 0.00022283, 352.83437428, 0.00074275, -35.28343743, -7.428e-05, -105.85031228, -0.00022283, -352.83437428, -0.00074275, 0.4, 0.3, 0.003, 0.0, 0.0, 12030, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2030, 99999, 'P', 42030, 'Vy', 32030, 'Vz', 22030, 'My', 12030, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172030, 72030, 172030, 2030, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123030, 123030, 23030, 2030, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172031, 22.3, 14.4, 6.15)
    ops.node(123031, 22.3, 14.4, 8.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2031, 172031, 123031, 0.1225, 27293166.79645327, 11372152.83185553, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22031, 70.90778979, 0.00096709, 86.36590617, 0.01984731, 8.63659062, 0.0623336, -70.90778979, -0.00096709, -86.36590617, -0.01984731, -8.63659062, -0.0623336, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12031, 82.59376273, 0.00096709, 100.59945717, 0.01984731, 10.05994572, 0.0623336, -82.59376273, -0.00096709, -100.59945717, -0.01984731, -10.05994572, -0.0623336, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22031, 2031, 0.0, 127.22719448, 0.01934177, 127.22719448, 0.05802532, 89.05903613, -2150.22329844, 0.05, 2, 0, 72031, 23031, 2, 3)
    ops.uniaxialMaterial('LimitState', 42031, 31.80679862, 8.082e-05, 95.42039586, 0.00024247, 318.06798619, 0.00080825, -31.80679862, -8.082e-05, -95.42039586, -0.00024247, -318.06798619, -0.00080825, 0.4, 0.3, 0.003, 0.0, 0.0, 22031, 2)
    ops.limitCurve('ThreePoint', 12031, 2031, 0.0, 127.22719448, 0.01934177, 127.22719448, 0.05802532, 89.05903613, -2150.22329844, 0.05, 2, 0, 72031, 23031, 1, 3)
    ops.uniaxialMaterial('LimitState', 32031, 31.80679862, 8.082e-05, 95.42039586, 0.00024247, 318.06798619, 0.00080825, -31.80679862, -8.082e-05, -95.42039586, -0.00024247, -318.06798619, -0.00080825, 0.4, 0.3, 0.003, 0.0, 0.0, 12031, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2031, 99999, 'P', 42031, 'Vy', 32031, 'Vz', 22031, 'My', 12031, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172031, 72031, 172031, 2031, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123031, 123031, 23031, 2031, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172032, 26.15, 14.4, 6.15)
    ops.node(123032, 26.15, 14.4, 8.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2032, 172032, 123032, 0.0625, 28507066.29469013, 11877944.28945422, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22032, 29.10568965, 0.00128282, 35.35287588, 0.02085229, 3.53528759, 0.07628872, -29.10568965, -0.00128282, -35.35287588, -0.02085229, -3.53528759, -0.07628872, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12032, 29.10568965, 0.00128282, 35.35287588, 0.02085229, 3.53528759, 0.07628872, -29.10568965, -0.00128282, -35.35287588, -0.02085229, -3.53528759, -0.07628872, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22032, 2032, 0.0, 76.54476086, 0.02565647, 76.54476086, 0.07696942, 53.5813326, -1505.30251248, 0.05, 2, 0, 72032, 23032, 2, 3)
    ops.uniaxialMaterial('LimitState', 42032, 19.13619021, 9.125e-05, 57.40857064, 0.00027375, 191.36190214, 0.00091251, -19.13619021, -9.125e-05, -57.40857064, -0.00027375, -191.36190214, -0.00091251, 0.4, 0.3, 0.003, 0.0, 0.0, 22032, 2)
    ops.limitCurve('ThreePoint', 12032, 2032, 0.0, 76.54476086, 0.02565647, 76.54476086, 0.07696942, 53.5813326, -1505.30251248, 0.05, 2, 0, 72032, 23032, 1, 3)
    ops.uniaxialMaterial('LimitState', 32032, 19.13619021, 9.125e-05, 57.40857064, 0.00027375, 191.36190214, 0.00091251, -19.13619021, -9.125e-05, -57.40857064, -0.00027375, -191.36190214, -0.00091251, 0.4, 0.3, 0.003, 0.0, 0.0, 12032, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2032, 99999, 'P', 42032, 'Vy', 32032, 'Vz', 22032, 'My', 12032, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172032, 72032, 172032, 2032, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123032, 123032, 23032, 2032, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173001, 0.0, 0.0, 9.1)
    ops.node(124001, 0.0, 0.0, 11.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3001, 173001, 124001, 0.0625, 26457465.97396301, 11023944.15581792, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23001, 22.14336975, 0.00122197, 27.14121289, 0.02365194, 2.71412129, 0.08637627, -22.14336975, -0.00122197, -27.14121289, -0.02365194, -2.71412129, -0.08637627, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13001, 22.14336975, 0.00122197, 27.14121289, 0.02365194, 2.71412129, 0.08637627, -22.14336975, -0.00122197, -27.14121289, -0.02365194, -2.71412129, -0.08637627, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23001, 3001, 0.0, 68.03096171, 0.02443935, 68.03096171, 0.07331804, 47.6216732, -3527.00044841, 0.05, 2, 0, 73001, 24001, 2, 3)
    ops.uniaxialMaterial('LimitState', 43001, 17.00774043, 8.738e-05, 51.02322128, 0.00026215, 170.07740427, 0.00087384, -17.00774043, -8.738e-05, -51.02322128, -0.00026215, -170.07740427, -0.00087384, 0.4, 0.3, 0.003, 0.0, 0.0, 23001, 2)
    ops.limitCurve('ThreePoint', 13001, 3001, 0.0, 68.03096171, 0.02443935, 68.03096171, 0.07331804, 47.6216732, -3527.00044841, 0.05, 2, 0, 73001, 24001, 1, 3)
    ops.uniaxialMaterial('LimitState', 33001, 17.00774043, 8.738e-05, 51.02322128, 0.00026215, 170.07740427, 0.00087384, -17.00774043, -8.738e-05, -51.02322128, -0.00026215, -170.07740427, -0.00087384, 0.4, 0.3, 0.003, 0.0, 0.0, 13001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3001, 99999, 'P', 43001, 'Vy', 33001, 'Vz', 23001, 'My', 13001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173001, 73001, 173001, 3001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124001, 124001, 24001, 3001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173002, 3.85, 0.0, 9.1)
    ops.node(124002, 3.85, 0.0, 11.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3002, 173002, 124002, 0.1225, 30497822.19991756, 12707425.91663232, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23002, 56.91260057, 0.00092638, 69.08234193, 0.02608163, 6.90823419, 0.08488983, -56.91260057, -0.00092638, -69.08234193, -0.02608163, -6.90823419, -0.08488983, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13002, 66.80598968, 0.00092638, 81.09125529, 0.02608163, 8.10912553, 0.08488983, -66.80598968, -0.00092638, -81.09125529, -0.02608163, -8.10912553, -0.08488983, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23002, 3002, 0.0, 142.29623976, 0.01852758, 142.29623976, 0.05558274, 99.60736783, -6151.66895784, 0.05, 2, 0, 73002, 24002, 2, 3)
    ops.uniaxialMaterial('LimitState', 43002, 35.57405994, 8.09e-05, 106.72217982, 0.0002427, 355.74059939, 0.00080899, -35.57405994, -8.09e-05, -106.72217982, -0.0002427, -355.74059939, -0.00080899, 0.4, 0.3, 0.003, 0.0, 0.0, 23002, 2)
    ops.limitCurve('ThreePoint', 13002, 3002, 0.0, 142.29623976, 0.01852758, 142.29623976, 0.05558274, 99.60736783, -6151.66895784, 0.05, 2, 0, 73002, 24002, 1, 3)
    ops.uniaxialMaterial('LimitState', 33002, 35.57405994, 8.09e-05, 106.72217982, 0.0002427, 355.74059939, 0.00080899, -35.57405994, -8.09e-05, -106.72217982, -0.0002427, -355.74059939, -0.00080899, 0.4, 0.3, 0.003, 0.0, 0.0, 13002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3002, 99999, 'P', 43002, 'Vy', 33002, 'Vz', 23002, 'My', 13002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173002, 73002, 173002, 3002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124002, 124002, 24002, 3002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173003, 7.7, 0.0, 9.1)
    ops.node(124003, 7.7, 0.0, 11.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3003, 173003, 124003, 0.1225, 30074904.86349335, 12531210.3597889, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23003, 58.02071413, 0.00092816, 70.51267029, 0.02365884, 7.05126703, 0.08235466, -58.02071413, -0.00092816, -70.51267029, -0.02365884, -7.05126703, -0.08235466, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13003, 68.60772261, 0.00092816, 83.37907929, 0.02365884, 8.33790793, 0.08235466, -68.60772261, -0.00092816, -83.37907929, -0.02365884, -8.33790793, -0.08235466, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23003, 3003, 0.0, 133.40914379, 0.01856321, 133.40914379, 0.05568964, 93.38640065, -5067.99532784, 0.05, 2, 0, 73003, 24003, 2, 3)
    ops.uniaxialMaterial('LimitState', 43003, 33.35228595, 7.691e-05, 100.05685784, 0.00023074, 333.52285946, 0.00076913, -33.35228595, -7.691e-05, -100.05685784, -0.00023074, -333.52285946, -0.00076913, 0.4, 0.3, 0.003, 0.0, 0.0, 23003, 2)
    ops.limitCurve('ThreePoint', 13003, 3003, 0.0, 133.40914379, 0.01856321, 133.40914379, 0.05568964, 93.38640065, -5067.99532784, 0.05, 2, 0, 73003, 24003, 1, 3)
    ops.uniaxialMaterial('LimitState', 33003, 33.35228595, 7.691e-05, 100.05685784, 0.00023074, 333.52285946, 0.00076913, -33.35228595, -7.691e-05, -100.05685784, -0.00023074, -333.52285946, -0.00076913, 0.4, 0.3, 0.003, 0.0, 0.0, 13003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3003, 99999, 'P', 43003, 'Vy', 33003, 'Vz', 23003, 'My', 13003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173003, 73003, 173003, 3003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124003, 124003, 24003, 3003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173006, 18.45, 0.0, 9.1)
    ops.node(124006, 18.45, 0.0, 11.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3006, 173006, 124006, 0.1225, 27992140.07958784, 11663391.69982827, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23006, 55.75839459, 0.00095277, 68.12391266, 0.02686732, 6.81239127, 0.08489972, -55.75839459, -0.00095277, -68.12391266, -0.02686732, -6.81239127, -0.08489972, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13006, 65.34010364, 0.00095277, 79.83055371, 0.02686732, 7.98305537, 0.08489972, -65.34010364, -0.00095277, -79.83055371, -0.02686732, -7.98305537, -0.08489972, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23006, 3006, 0.0, 132.64893242, 0.01905547, 132.64893242, 0.05716641, 92.85425269, -6037.8049683, 0.05, 2, 0, 73006, 24006, 2, 3)
    ops.uniaxialMaterial('LimitState', 43006, 33.1622331, 8.216e-05, 99.48669931, 0.00024649, 331.62233105, 0.00082165, -33.1622331, -8.216e-05, -99.48669931, -0.00024649, -331.62233105, -0.00082165, 0.4, 0.3, 0.003, 0.0, 0.0, 23006, 2)
    ops.limitCurve('ThreePoint', 13006, 3006, 0.0, 132.64893242, 0.01905547, 132.64893242, 0.05716641, 92.85425269, -6037.8049683, 0.05, 2, 0, 73006, 24006, 1, 3)
    ops.uniaxialMaterial('LimitState', 33006, 33.1622331, 8.216e-05, 99.48669931, 0.00024649, 331.62233105, 0.00082165, -33.1622331, -8.216e-05, -99.48669931, -0.00024649, -331.62233105, -0.00082165, 0.4, 0.3, 0.003, 0.0, 0.0, 13006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3006, 99999, 'P', 43006, 'Vy', 33006, 'Vz', 23006, 'My', 13006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173006, 73006, 173006, 3006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124006, 124006, 24006, 3006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173007, 22.3, 0.0, 9.1)
    ops.node(124007, 22.3, 0.0, 11.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3007, 173007, 124007, 0.1225, 28983819.67279368, 12076591.5303307, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23007, 57.15959159, 0.0009505, 69.66887153, 0.02280775, 6.96688715, 0.08118085, -57.15959159, -0.0009505, -69.66887153, -0.02280775, -6.96688715, -0.08118085, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13007, 67.19414728, 0.0009505, 81.89947276, 0.02280775, 8.18994728, 0.08118085, -67.19414728, -0.0009505, -81.89947276, -0.02280775, -8.18994728, -0.08118085, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23007, 3007, 0.0, 126.59795264, 0.01901001, 126.59795264, 0.05703003, 88.61856685, -4668.20055417, 0.05, 2, 0, 73007, 24007, 2, 3)
    ops.uniaxialMaterial('LimitState', 43007, 31.64948816, 7.573e-05, 94.94846448, 0.0002272, 316.49488161, 0.00075734, -31.64948816, -7.573e-05, -94.94846448, -0.0002272, -316.49488161, -0.00075734, 0.4, 0.3, 0.003, 0.0, 0.0, 23007, 2)
    ops.limitCurve('ThreePoint', 13007, 3007, 0.0, 126.59795264, 0.01901001, 126.59795264, 0.05703003, 88.61856685, -4668.20055417, 0.05, 2, 0, 73007, 24007, 1, 3)
    ops.uniaxialMaterial('LimitState', 33007, 31.64948816, 7.573e-05, 94.94846448, 0.0002272, 316.49488161, 0.00075734, -31.64948816, -7.573e-05, -94.94846448, -0.0002272, -316.49488161, -0.00075734, 0.4, 0.3, 0.003, 0.0, 0.0, 13007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3007, 99999, 'P', 43007, 'Vy', 33007, 'Vz', 23007, 'My', 13007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173007, 73007, 173007, 3007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124007, 124007, 24007, 3007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173008, 26.15, 0.0, 9.1)
    ops.node(124008, 26.15, 0.0, 11.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3008, 173008, 124008, 0.0625, 30008327.53956894, 12503469.80815372, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23008, 23.77958245, 0.00118448, 28.90434395, 0.02097061, 2.8904344, 0.08511079, -23.77958245, -0.00118448, -28.90434395, -0.02097061, -2.8904344, -0.08511079, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13008, 23.77958245, 0.00118448, 28.90434395, 0.02097061, 2.8904344, 0.08511079, -23.77958245, -0.00118448, -28.90434395, -0.02097061, -2.8904344, -0.08511079, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23008, 3008, 0.0, 73.18553251, 0.02368952, 73.18553251, 0.07106855, 51.22987276, -3343.92578727, 0.05, 2, 0, 73008, 24008, 2, 3)
    ops.uniaxialMaterial('LimitState', 43008, 18.29638313, 8.288e-05, 54.88914938, 0.00024864, 182.96383128, 0.00082882, -18.29638313, -8.288e-05, -54.88914938, -0.00024864, -182.96383128, -0.00082882, 0.4, 0.3, 0.003, 0.0, 0.0, 23008, 2)
    ops.limitCurve('ThreePoint', 13008, 3008, 0.0, 73.18553251, 0.02368952, 73.18553251, 0.07106855, 51.22987276, -3343.92578727, 0.05, 2, 0, 73008, 24008, 1, 3)
    ops.uniaxialMaterial('LimitState', 33008, 18.29638313, 8.288e-05, 54.88914938, 0.00024864, 182.96383128, 0.00082882, -18.29638313, -8.288e-05, -54.88914938, -0.00024864, -182.96383128, -0.00082882, 0.4, 0.3, 0.003, 0.0, 0.0, 13008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3008, 99999, 'P', 43008, 'Vy', 33008, 'Vz', 23008, 'My', 13008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173008, 73008, 173008, 3008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124008, 124008, 24008, 3008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173009, 0.0, 4.8, 9.1)
    ops.node(124009, 0.0, 4.8, 11.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3009, 173009, 124009, 0.1225, 30094446.48642823, 12539352.70267843, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23009, 67.05363832, 0.00088851, 81.48483353, 0.01718614, 8.14848335, 0.06673729, -67.05363832, -0.00088851, -81.48483353, -0.01718614, -8.14848335, -0.06673729, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13009, 56.49880973, 0.00088851, 68.65840871, 0.01718614, 6.86584087, 0.06673729, -56.49880973, -0.00088851, -68.65840871, -0.01718614, -6.86584087, -0.06673729, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23009, 3009, 0.0, 118.43303499, 0.01777023, 118.43303499, 0.0533107, 82.90312449, -3150.84361588, 0.05, 2, 0, 73009, 24009, 2, 3)
    ops.uniaxialMaterial('LimitState', 43009, 29.60825875, 6.823e-05, 88.82477624, 0.0002047, 296.08258748, 0.00068235, -29.60825875, -6.823e-05, -88.82477624, -0.0002047, -296.08258748, -0.00068235, 0.4, 0.3, 0.003, 0.0, 0.0, 23009, 2)
    ops.limitCurve('ThreePoint', 13009, 3009, 0.0, 118.43303499, 0.01777023, 118.43303499, 0.0533107, 82.90312449, -3150.84361588, 0.05, 2, 0, 73009, 24009, 1, 3)
    ops.uniaxialMaterial('LimitState', 33009, 29.60825875, 6.823e-05, 88.82477624, 0.0002047, 296.08258748, 0.00068235, -29.60825875, -6.823e-05, -88.82477624, -0.0002047, -296.08258748, -0.00068235, 0.4, 0.3, 0.003, 0.0, 0.0, 13009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3009, 99999, 'P', 43009, 'Vy', 33009, 'Vz', 23009, 'My', 13009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173009, 73009, 173009, 3009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124009, 124009, 24009, 3009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173010, 3.85, 4.8, 9.1)
    ops.node(124010, 3.85, 4.8, 11.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3010, 173010, 124010, 0.1225, 27721636.42604771, 11550681.84418655, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23010, 79.36716843, 0.00101817, 96.91036808, 0.01796239, 9.69103681, 0.05937231, -79.36716843, -0.00101817, -96.91036808, -0.01796239, -9.69103681, -0.05937231, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13010, 74.00409421, 0.00101817, 90.361848, 0.01796239, 9.0361848, 0.05937231, -74.00409421, -0.00101817, -90.361848, -0.01796239, -9.0361848, -0.05937231, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23010, 3010, 0.0, 103.37578404, 0.02036345, 103.37578404, 0.06109036, 72.36304883, -1668.42705951, 0.05, 2, 0, 73010, 24010, 2, 3)
    ops.uniaxialMaterial('LimitState', 43010, 25.84394601, 6.466e-05, 77.53183803, 0.00019397, 258.4394601, 0.00064657, -25.84394601, -6.466e-05, -77.53183803, -0.00019397, -258.4394601, -0.00064657, 0.4, 0.3, 0.003, 0.0, 0.0, 23010, 2)
    ops.limitCurve('ThreePoint', 13010, 3010, 0.0, 103.37578404, 0.02036345, 103.37578404, 0.06109036, 72.36304883, -1668.42705951, 0.05, 2, 0, 73010, 24010, 1, 3)
    ops.uniaxialMaterial('LimitState', 33010, 25.84394601, 6.466e-05, 77.53183803, 0.00019397, 258.4394601, 0.00064657, -25.84394601, -6.466e-05, -77.53183803, -0.00019397, -258.4394601, -0.00064657, 0.4, 0.3, 0.003, 0.0, 0.0, 13010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3010, 99999, 'P', 43010, 'Vy', 33010, 'Vz', 23010, 'My', 13010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173010, 73010, 173010, 3010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124010, 124010, 24010, 3010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173011, 7.7, 4.8, 9.1)
    ops.node(124011, 7.7, 4.8, 11.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3011, 173011, 124011, 0.1225, 31511334.20911921, 13129722.58713301, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23011, 80.56209935, 0.00094728, 97.41058738, 0.01782024, 9.74105874, 0.06056479, -80.56209935, -0.00094728, -97.41058738, -0.01782024, -9.74105874, -0.06056479, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13011, 75.05627726, 0.00094728, 90.75329607, 0.01782024, 9.07532961, 0.06056479, -75.05627726, -0.00094728, -90.75329607, -0.01782024, -9.07532961, -0.06056479, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23011, 3011, 0.0, 118.0356823, 0.0189456, 118.0356823, 0.0568368, 82.62497761, -1733.91336336, 0.05, 2, 0, 73011, 24011, 2, 3)
    ops.uniaxialMaterial('LimitState', 43011, 29.50892058, 6.495e-05, 88.52676173, 0.00019484, 295.08920575, 0.00064948, -29.50892058, -6.495e-05, -88.52676173, -0.00019484, -295.08920575, -0.00064948, 0.4, 0.3, 0.003, 0.0, 0.0, 23011, 2)
    ops.limitCurve('ThreePoint', 13011, 3011, 0.0, 118.0356823, 0.0189456, 118.0356823, 0.0568368, 82.62497761, -1733.91336336, 0.05, 2, 0, 73011, 24011, 1, 3)
    ops.uniaxialMaterial('LimitState', 33011, 29.50892058, 6.495e-05, 88.52676173, 0.00019484, 295.08920575, 0.00064948, -29.50892058, -6.495e-05, -88.52676173, -0.00019484, -295.08920575, -0.00064948, 0.4, 0.3, 0.003, 0.0, 0.0, 13011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3011, 99999, 'P', 43011, 'Vy', 33011, 'Vz', 23011, 'My', 13011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173011, 73011, 173011, 3011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124011, 124011, 24011, 3011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173012, 11.55, 4.8, 9.1)
    ops.node(124012, 11.55, 4.8, 11.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3012, 173012, 124012, 0.1225, 30731220.86119926, 12804675.35883303, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23012, 71.48974507, 0.0009063, 86.63433469, 0.01662222, 8.66343347, 0.06494134, -71.48974507, -0.0009063, -86.63433469, -0.01662222, -8.66343347, -0.06494134, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13012, 60.96482188, 0.0009063, 73.87978204, 0.01662222, 7.3879782, 0.06494134, -60.96482188, -0.0009063, -73.87978204, -0.01662222, -7.3879782, -0.06494134, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23012, 3012, 0.0, 124.03743024, 0.01812598, 124.03743024, 0.05437795, 86.82620117, -2272.47030125, 0.05, 2, 0, 73012, 24012, 2, 3)
    ops.uniaxialMaterial('LimitState', 43012, 31.00935756, 6.998e-05, 93.02807268, 0.00020995, 310.0935756, 0.00069983, -31.00935756, -6.998e-05, -93.02807268, -0.00020995, -310.0935756, -0.00069983, 0.4, 0.3, 0.003, 0.0, 0.0, 23012, 2)
    ops.limitCurve('ThreePoint', 13012, 3012, 0.0, 124.03743024, 0.01812598, 124.03743024, 0.05437795, 86.82620117, -2272.47030125, 0.05, 2, 0, 73012, 24012, 1, 3)
    ops.uniaxialMaterial('LimitState', 33012, 31.00935756, 6.998e-05, 93.02807268, 0.00020995, 310.0935756, 0.00069983, -31.00935756, -6.998e-05, -93.02807268, -0.00020995, -310.0935756, -0.00069983, 0.4, 0.3, 0.003, 0.0, 0.0, 13012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3012, 99999, 'P', 43012, 'Vy', 33012, 'Vz', 23012, 'My', 13012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173012, 73012, 173012, 3012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124012, 124012, 24012, 3012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173013, 14.6, 4.8, 9.1)
    ops.node(124013, 14.6, 4.8, 11.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3013, 173013, 124013, 0.1225, 27464014.03053401, 11443339.17938917, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23013, 69.59292544, 0.00100637, 85.00879173, 0.01733942, 8.50087917, 0.06419767, -69.59292544, -0.00100637, -85.00879173, -0.01733942, -8.50087917, -0.06419767, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13013, 60.27689599, 0.00100637, 73.62912344, 0.01733942, 7.36291234, 0.06419767, -60.27689599, -0.00100637, -73.62912344, -0.01733942, -7.36291234, -0.06419767, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23013, 3013, 0.0, 111.14187139, 0.02012739, 111.14187139, 0.06038218, 77.79930998, -2181.8899259, 0.05, 2, 0, 73013, 24013, 2, 3)
    ops.uniaxialMaterial('LimitState', 43013, 27.78546785, 7.017e-05, 83.35640355, 0.0002105, 277.85467849, 0.00070167, -27.78546785, -7.017e-05, -83.35640355, -0.0002105, -277.85467849, -0.00070167, 0.4, 0.3, 0.003, 0.0, 0.0, 23013, 2)
    ops.limitCurve('ThreePoint', 13013, 3013, 0.0, 111.14187139, 0.02012739, 111.14187139, 0.06038218, 77.79930998, -2181.8899259, 0.05, 2, 0, 73013, 24013, 1, 3)
    ops.uniaxialMaterial('LimitState', 33013, 27.78546785, 7.017e-05, 83.35640355, 0.0002105, 277.85467849, 0.00070167, -27.78546785, -7.017e-05, -83.35640355, -0.0002105, -277.85467849, -0.00070167, 0.4, 0.3, 0.003, 0.0, 0.0, 13013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3013, 99999, 'P', 43013, 'Vy', 33013, 'Vz', 23013, 'My', 13013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173013, 73013, 173013, 3013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124013, 124013, 24013, 3013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173014, 18.45, 4.8, 9.1)
    ops.node(124014, 18.45, 4.8, 11.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3014, 173014, 124014, 0.1225, 31394325.75117134, 13080969.06298806, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23014, 78.09898286, 0.00091434, 94.46635176, 0.01849772, 9.44663518, 0.06121053, -78.09898286, -0.00091434, -94.46635176, -0.01849772, -9.44663518, -0.06121053, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13014, 72.75654698, 0.00091434, 88.00429031, 0.01849772, 8.80042903, 0.06121053, -72.75654698, -0.00091434, -88.00429031, -0.01849772, -8.80042903, -0.06121053, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23014, 3014, 0.0, 119.77978603, 0.01828671, 119.77978603, 0.05486014, 83.84585022, -1875.96515775, 0.05, 2, 0, 73014, 24014, 2, 3)
    ops.uniaxialMaterial('LimitState', 43014, 29.94494651, 6.615e-05, 89.83483952, 0.00019846, 299.44946507, 0.00066153, -29.94494651, -6.615e-05, -89.83483952, -0.00019846, -299.44946507, -0.00066153, 0.4, 0.3, 0.003, 0.0, 0.0, 23014, 2)
    ops.limitCurve('ThreePoint', 13014, 3014, 0.0, 119.77978603, 0.01828671, 119.77978603, 0.05486014, 83.84585022, -1875.96515775, 0.05, 2, 0, 73014, 24014, 1, 3)
    ops.uniaxialMaterial('LimitState', 33014, 29.94494651, 6.615e-05, 89.83483952, 0.00019846, 299.44946507, 0.00066153, -29.94494651, -6.615e-05, -89.83483952, -0.00019846, -299.44946507, -0.00066153, 0.4, 0.3, 0.003, 0.0, 0.0, 13014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3014, 99999, 'P', 43014, 'Vy', 33014, 'Vz', 23014, 'My', 13014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173014, 73014, 173014, 3014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124014, 124014, 24014, 3014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173015, 22.3, 4.8, 9.1)
    ops.node(124015, 22.3, 4.8, 11.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3015, 173015, 124015, 0.1225, 30556854.34638626, 12732022.64432761, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23015, 77.78190081, 0.00098131, 94.31534929, 0.01971806, 9.43153493, 0.06218874, -77.78190081, -0.00098131, -94.31534929, -0.01971806, -9.43153493, -0.06218874, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13015, 72.80702008, 0.00098131, 88.28299974, 0.01971806, 8.82829997, 0.06218874, -72.80702008, -0.00098131, -88.28299974, -0.01971806, -8.82829997, -0.06218874, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23015, 3015, 0.0, 120.0195732, 0.01962613, 120.0195732, 0.05887838, 84.01370124, -2104.29915734, 0.05, 2, 0, 73015, 24015, 2, 3)
    ops.uniaxialMaterial('LimitState', 43015, 30.0048933, 6.81e-05, 90.0146799, 0.00020431, 300.048933, 0.00068102, -30.0048933, -6.81e-05, -90.0146799, -0.00020431, -300.048933, -0.00068102, 0.4, 0.3, 0.003, 0.0, 0.0, 23015, 2)
    ops.limitCurve('ThreePoint', 13015, 3015, 0.0, 120.0195732, 0.01962613, 120.0195732, 0.05887838, 84.01370124, -2104.29915734, 0.05, 2, 0, 73015, 24015, 1, 3)
    ops.uniaxialMaterial('LimitState', 33015, 30.0048933, 6.81e-05, 90.0146799, 0.00020431, 300.048933, 0.00068102, -30.0048933, -6.81e-05, -90.0146799, -0.00020431, -300.048933, -0.00068102, 0.4, 0.3, 0.003, 0.0, 0.0, 13015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3015, 99999, 'P', 43015, 'Vy', 33015, 'Vz', 23015, 'My', 13015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173015, 73015, 173015, 3015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124015, 124015, 24015, 3015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173016, 26.15, 4.8, 9.1)
    ops.node(124016, 26.15, 4.8, 11.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3016, 173016, 124016, 0.1225, 30862593.77642816, 12859414.07351173, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23016, 63.8094468, 0.00096092, 77.36938062, 0.01875387, 7.73693806, 0.06847447, -63.8094468, -0.00096092, -77.36938062, -0.01875387, -7.73693806, -0.06847447, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13016, 55.53163251, 0.00096092, 67.33247548, 0.01875387, 6.73324755, 0.06847447, -55.53163251, -0.00096092, -67.33247548, -0.01875387, -6.73324755, -0.06847447, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23016, 3016, 0.0, 126.93861863, 0.01921831, 126.93861863, 0.05765492, 88.85703304, -3809.72770966, 0.05, 2, 0, 73016, 24016, 2, 3)
    ops.uniaxialMaterial('LimitState', 43016, 31.73465466, 7.131e-05, 95.20396397, 0.00021394, 317.34654657, 0.00071315, -31.73465466, -7.131e-05, -95.20396397, -0.00021394, -317.34654657, -0.00071315, 0.4, 0.3, 0.003, 0.0, 0.0, 23016, 2)
    ops.limitCurve('ThreePoint', 13016, 3016, 0.0, 126.93861863, 0.01921831, 126.93861863, 0.05765492, 88.85703304, -3809.72770966, 0.05, 2, 0, 73016, 24016, 1, 3)
    ops.uniaxialMaterial('LimitState', 33016, 31.73465466, 7.131e-05, 95.20396397, 0.00021394, 317.34654657, 0.00071315, -31.73465466, -7.131e-05, -95.20396397, -0.00021394, -317.34654657, -0.00071315, 0.4, 0.3, 0.003, 0.0, 0.0, 13016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3016, 99999, 'P', 43016, 'Vy', 33016, 'Vz', 23016, 'My', 13016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173016, 73016, 173016, 3016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124016, 124016, 24016, 3016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173017, 0.0, 9.6, 9.1)
    ops.node(124017, 0.0, 9.6, 11.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3017, 173017, 124017, 0.1225, 29544038.93459187, 12310016.22274661, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23017, 71.90898776, 0.00094525, 87.5184015, 0.01920893, 8.75184015, 0.06864885, -71.90898776, -0.00094525, -87.5184015, -0.01920893, -8.75184015, -0.06864885, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13017, 60.27959489, 0.00094525, 73.36459532, 0.01920893, 7.33645953, 0.06864885, -60.27959489, -0.00094525, -73.36459532, -0.01920893, -7.33645953, -0.06864885, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23017, 3017, 0.0, 122.82059118, 0.0189049, 122.82059118, 0.0567147, 85.97441382, -3924.75447068, 0.05, 2, 0, 73017, 24017, 2, 3)
    ops.uniaxialMaterial('LimitState', 43017, 30.70514779, 7.208e-05, 92.11544338, 0.00021624, 307.05147794, 0.00072081, -30.70514779, -7.208e-05, -92.11544338, -0.00021624, -307.05147794, -0.00072081, 0.4, 0.3, 0.003, 0.0, 0.0, 23017, 2)
    ops.limitCurve('ThreePoint', 13017, 3017, 0.0, 122.82059118, 0.0189049, 122.82059118, 0.0567147, 85.97441382, -3924.75447068, 0.05, 2, 0, 73017, 24017, 1, 3)
    ops.uniaxialMaterial('LimitState', 33017, 30.70514779, 7.208e-05, 92.11544338, 0.00021624, 307.05147794, 0.00072081, -30.70514779, -7.208e-05, -92.11544338, -0.00021624, -307.05147794, -0.00072081, 0.4, 0.3, 0.003, 0.0, 0.0, 13017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3017, 99999, 'P', 43017, 'Vy', 33017, 'Vz', 23017, 'My', 13017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173017, 73017, 173017, 3017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124017, 124017, 24017, 3017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173018, 3.85, 9.6, 9.1)
    ops.node(124018, 3.85, 9.6, 11.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3018, 173018, 124018, 0.1225, 28027554.32497219, 11678147.63540508, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23018, 78.33260953, 0.00104689, 95.58796088, 0.01949897, 9.55879609, 0.06108276, -78.33260953, -0.00104689, -95.58796088, -0.01949897, -9.55879609, -0.06108276, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13018, 73.32023341, 0.00104689, 89.47144293, 0.01949897, 8.94714429, 0.06108276, -73.32023341, -0.00104689, -89.47144293, -0.01949897, -8.94714429, -0.06108276, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23018, 3018, 0.0, 108.11452058, 0.02093789, 108.11452058, 0.06281366, 75.68016441, -1921.82177491, 0.05, 2, 0, 73018, 24018, 2, 3)
    ops.uniaxialMaterial('LimitState', 43018, 27.02863015, 6.688e-05, 81.08589044, 0.00020065, 270.28630145, 0.00066883, -27.02863015, -6.688e-05, -81.08589044, -0.00020065, -270.28630145, -0.00066883, 0.4, 0.3, 0.003, 0.0, 0.0, 23018, 2)
    ops.limitCurve('ThreePoint', 13018, 3018, 0.0, 108.11452058, 0.02093789, 108.11452058, 0.06281366, 75.68016441, -1921.82177491, 0.05, 2, 0, 73018, 24018, 1, 3)
    ops.uniaxialMaterial('LimitState', 33018, 27.02863015, 6.688e-05, 81.08589044, 0.00020065, 270.28630145, 0.00066883, -27.02863015, -6.688e-05, -81.08589044, -0.00020065, -270.28630145, -0.00066883, 0.4, 0.3, 0.003, 0.0, 0.0, 13018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3018, 99999, 'P', 43018, 'Vy', 33018, 'Vz', 23018, 'My', 13018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173018, 73018, 173018, 3018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124018, 124018, 24018, 3018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173019, 7.7, 9.6, 9.1)
    ops.node(124019, 7.7, 9.6, 11.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3019, 173019, 124019, 0.1225, 31913744.87390431, 13297393.69746013, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23019, 81.56103522, 0.00094658, 98.49551932, 0.01875768, 9.84955193, 0.06163311, -81.56103522, -0.00094658, -98.49551932, -0.01875768, -9.84955193, -0.06163311, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13019, 75.92728642, 0.00094658, 91.69203758, 0.01875768, 9.16920376, 0.06163311, -75.92728642, -0.00094658, -91.69203758, -0.01875768, -9.16920376, -0.06163311, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23019, 3019, 0.0, 125.22263505, 0.01893154, 125.22263505, 0.05679462, 87.65584453, -2131.93039867, 0.05, 2, 0, 73019, 24019, 2, 3)
    ops.uniaxialMaterial('LimitState', 43019, 31.30565876, 6.803e-05, 93.91697628, 0.0002041, 313.05658762, 0.00068034, -31.30565876, -6.803e-05, -93.91697628, -0.0002041, -313.05658762, -0.00068034, 0.4, 0.3, 0.003, 0.0, 0.0, 23019, 2)
    ops.limitCurve('ThreePoint', 13019, 3019, 0.0, 125.22263505, 0.01893154, 125.22263505, 0.05679462, 87.65584453, -2131.93039867, 0.05, 2, 0, 73019, 24019, 1, 3)
    ops.uniaxialMaterial('LimitState', 33019, 31.30565876, 6.803e-05, 93.91697628, 0.0002041, 313.05658762, 0.00068034, -31.30565876, -6.803e-05, -93.91697628, -0.0002041, -313.05658762, -0.00068034, 0.4, 0.3, 0.003, 0.0, 0.0, 13019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3019, 99999, 'P', 43019, 'Vy', 33019, 'Vz', 23019, 'My', 13019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173019, 73019, 173019, 3019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124019, 124019, 24019, 3019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173020, 11.55, 9.6, 9.1)
    ops.node(124020, 11.55, 9.6, 11.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3020, 173020, 124020, 0.1225, 29764747.63168217, 12401978.17986757, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23020, 66.92076794, 0.00092635, 81.34741784, 0.01949914, 8.13474178, 0.06806977, -66.92076794, -0.00092635, -81.34741784, -0.01949914, -8.13474178, -0.06806977, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13020, 57.56580855, 0.00092635, 69.97573438, 0.01949914, 6.99757344, 0.06806977, -57.56580855, -0.00092635, -69.97573438, -0.01949914, -6.99757344, -0.06806977, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23020, 3020, 0.0, 125.67480644, 0.01852709, 125.67480644, 0.05558127, 87.9723645, -3084.81237373, 0.05, 2, 0, 73020, 24020, 2, 3)
    ops.uniaxialMaterial('LimitState', 43020, 31.41870161, 7.321e-05, 94.25610483, 0.00021963, 314.18701609, 0.00073209, -31.41870161, -7.321e-05, -94.25610483, -0.00021963, -314.18701609, -0.00073209, 0.4, 0.3, 0.003, 0.0, 0.0, 23020, 2)
    ops.limitCurve('ThreePoint', 13020, 3020, 0.0, 125.67480644, 0.01852709, 125.67480644, 0.05558127, 87.9723645, -3084.81237373, 0.05, 2, 0, 73020, 24020, 1, 3)
    ops.uniaxialMaterial('LimitState', 33020, 31.41870161, 7.321e-05, 94.25610483, 0.00021963, 314.18701609, 0.00073209, -31.41870161, -7.321e-05, -94.25610483, -0.00021963, -314.18701609, -0.00073209, 0.4, 0.3, 0.003, 0.0, 0.0, 13020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3020, 99999, 'P', 43020, 'Vy', 33020, 'Vz', 23020, 'My', 13020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173020, 73020, 173020, 3020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124020, 124020, 24020, 3020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173021, 14.6, 9.6, 9.1)
    ops.node(124021, 14.6, 9.6, 11.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3021, 173021, 124021, 0.1225, 28663377.06654114, 11943073.77772548, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23021, 70.83834609, 0.00091775, 86.34845913, 0.02078179, 8.63484591, 0.06894854, -70.83834609, -0.00091775, -86.34845913, -0.02078179, -8.63484591, -0.06894854, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13021, 59.75772262, 0.00091775, 72.84172421, 0.02078179, 7.28417242, 0.06894854, -59.75772262, -0.00091775, -72.84172421, -0.02078179, -7.28417242, -0.06894854, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23021, 3021, 0.0, 123.790044, 0.01835507, 123.790044, 0.0550652, 86.6530308, -3273.83424496, 0.05, 2, 0, 73021, 24021, 2, 3)
    ops.uniaxialMaterial('LimitState', 43021, 30.947511, 7.488e-05, 92.842533, 0.00022465, 309.47510999, 0.00074882, -30.947511, -7.488e-05, -92.842533, -0.00022465, -309.47510999, -0.00074882, 0.4, 0.3, 0.003, 0.0, 0.0, 23021, 2)
    ops.limitCurve('ThreePoint', 13021, 3021, 0.0, 123.790044, 0.01835507, 123.790044, 0.0550652, 86.6530308, -3273.83424496, 0.05, 2, 0, 73021, 24021, 1, 3)
    ops.uniaxialMaterial('LimitState', 33021, 30.947511, 7.488e-05, 92.842533, 0.00022465, 309.47510999, 0.00074882, -30.947511, -7.488e-05, -92.842533, -0.00022465, -309.47510999, -0.00074882, 0.4, 0.3, 0.003, 0.0, 0.0, 13021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3021, 99999, 'P', 43021, 'Vy', 33021, 'Vz', 23021, 'My', 13021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173021, 73021, 173021, 3021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124021, 124021, 24021, 3021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173022, 18.45, 9.6, 9.1)
    ops.node(124022, 18.45, 9.6, 11.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3022, 173022, 124022, 0.1225, 28259953.11707816, 11774980.46544923, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23022, 79.55187818, 0.00098525, 97.02625314, 0.01991854, 9.70262531, 0.06160073, -79.55187818, -0.00098525, -97.02625314, -0.01991854, -9.70262531, -0.06160073, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13022, 74.0340382, 0.00098525, 90.29636378, 0.01991854, 9.02963638, 0.06160073, -74.0340382, -0.00098525, -90.29636378, -0.01991854, -9.02963638, -0.06160073, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23022, 3022, 0.0, 111.2316159, 0.01970491, 111.2316159, 0.05911473, 77.86213113, -2080.95257437, 0.05, 2, 0, 73022, 24022, 2, 3)
    ops.uniaxialMaterial('LimitState', 43022, 27.80790398, 6.825e-05, 83.42371193, 0.00020474, 278.07903976, 0.00068246, -27.80790398, -6.825e-05, -83.42371193, -0.00020474, -278.07903976, -0.00068246, 0.4, 0.3, 0.003, 0.0, 0.0, 23022, 2)
    ops.limitCurve('ThreePoint', 13022, 3022, 0.0, 111.2316159, 0.01970491, 111.2316159, 0.05911473, 77.86213113, -2080.95257437, 0.05, 2, 0, 73022, 24022, 1, 3)
    ops.uniaxialMaterial('LimitState', 33022, 27.80790398, 6.825e-05, 83.42371193, 0.00020474, 278.07903976, 0.00068246, -27.80790398, -6.825e-05, -83.42371193, -0.00020474, -278.07903976, -0.00068246, 0.4, 0.3, 0.003, 0.0, 0.0, 13022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3022, 99999, 'P', 43022, 'Vy', 33022, 'Vz', 23022, 'My', 13022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173022, 73022, 173022, 3022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124022, 124022, 24022, 3022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173023, 22.3, 9.6, 9.1)
    ops.node(124023, 22.3, 9.6, 11.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3023, 173023, 124023, 0.1225, 31857286.53821601, 13273869.39092334, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23023, 80.16063191, 0.00102341, 96.82183216, 0.01983721, 9.68218322, 0.06269831, -80.16063191, -0.00102341, -96.82183216, -0.01983721, -9.68218322, -0.06269831, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13023, 75.21234619, 0.00102341, 90.84505679, 0.01983721, 9.08450568, 0.06269831, -75.21234619, -0.00102341, -90.84505679, -0.01983721, -9.08450568, -0.06269831, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23023, 3023, 0.0, 127.1203617, 0.02046821, 127.1203617, 0.06140462, 88.98425319, -2284.7488755, 0.05, 2, 0, 73023, 24023, 2, 3)
    ops.uniaxialMaterial('LimitState', 43023, 31.78009042, 6.919e-05, 95.34027127, 0.00020756, 317.80090424, 0.00069187, -31.78009042, -6.919e-05, -95.34027127, -0.00020756, -317.80090424, -0.00069187, 0.4, 0.3, 0.003, 0.0, 0.0, 23023, 2)
    ops.limitCurve('ThreePoint', 13023, 3023, 0.0, 127.1203617, 0.02046821, 127.1203617, 0.06140462, 88.98425319, -2284.7488755, 0.05, 2, 0, 73023, 24023, 1, 3)
    ops.uniaxialMaterial('LimitState', 33023, 31.78009042, 6.919e-05, 95.34027127, 0.00020756, 317.80090424, 0.00069187, -31.78009042, -6.919e-05, -95.34027127, -0.00020756, -317.80090424, -0.00069187, 0.4, 0.3, 0.003, 0.0, 0.0, 13023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3023, 99999, 'P', 43023, 'Vy', 33023, 'Vz', 23023, 'My', 13023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173023, 73023, 173023, 3023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124023, 124023, 24023, 3023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173024, 26.15, 9.6, 9.1)
    ops.node(124024, 26.15, 9.6, 11.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3024, 173024, 124024, 0.1225, 28997101.49415643, 12082125.62256518, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23024, 68.41786645, 0.00090832, 83.38824209, 0.01950816, 8.33882421, 0.06880653, -68.41786645, -0.00090832, -83.38824209, -0.01950816, -8.33882421, -0.06880653, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13024, 57.40856032, 0.00090832, 69.97001185, 0.01950816, 6.99700119, 0.06880653, -57.40856032, -0.00090832, -69.97001185, -0.01950816, -6.99700119, -0.06880653, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23024, 3024, 0.0, 119.98843387, 0.01816646, 119.98843387, 0.05449938, 83.99190371, -3816.00517838, 0.05, 2, 0, 73024, 24024, 2, 3)
    ops.uniaxialMaterial('LimitState', 43024, 29.99710847, 7.175e-05, 89.99132541, 0.00021524, 299.97108468, 0.00071747, -29.99710847, -7.175e-05, -89.99132541, -0.00021524, -299.97108468, -0.00071747, 0.4, 0.3, 0.003, 0.0, 0.0, 23024, 2)
    ops.limitCurve('ThreePoint', 13024, 3024, 0.0, 119.98843387, 0.01816646, 119.98843387, 0.05449938, 83.99190371, -3816.00517838, 0.05, 2, 0, 73024, 24024, 1, 3)
    ops.uniaxialMaterial('LimitState', 33024, 29.99710847, 7.175e-05, 89.99132541, 0.00021524, 299.97108468, 0.00071747, -29.99710847, -7.175e-05, -89.99132541, -0.00021524, -299.97108468, -0.00071747, 0.4, 0.3, 0.003, 0.0, 0.0, 13024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3024, 99999, 'P', 43024, 'Vy', 33024, 'Vz', 23024, 'My', 13024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173024, 73024, 173024, 3024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124024, 124024, 24024, 3024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173025, 0.0, 14.4, 9.1)
    ops.node(124025, 0.0, 14.4, 11.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3025, 173025, 124025, 0.0625, 29529951.88257354, 12304146.61773898, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23025, 24.1021514, 0.00122795, 29.33469952, 0.02300331, 2.93346995, 0.08699263, -24.1021514, -0.00122795, -29.33469952, -0.02300331, -2.93346995, -0.08699263, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13025, 24.1021514, 0.00122795, 29.33469952, 0.02300331, 2.93346995, 0.08699263, -24.1021514, -0.00122795, -29.33469952, -0.02300331, -2.93346995, -0.08699263, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23025, 3025, 0.0, 75.10918197, 0.02455893, 75.10918197, 0.07367679, 52.57642738, -3803.61771644, 0.05, 2, 0, 73025, 24025, 2, 3)
    ops.uniaxialMaterial('LimitState', 43025, 18.77729549, 8.644e-05, 56.33188648, 0.00025931, 187.77295492, 0.00086438, -18.77729549, -8.644e-05, -56.33188648, -0.00025931, -187.77295492, -0.00086438, 0.4, 0.3, 0.003, 0.0, 0.0, 23025, 2)
    ops.limitCurve('ThreePoint', 13025, 3025, 0.0, 75.10918197, 0.02455893, 75.10918197, 0.07367679, 52.57642738, -3803.61771644, 0.05, 2, 0, 73025, 24025, 1, 3)
    ops.uniaxialMaterial('LimitState', 33025, 18.77729549, 8.644e-05, 56.33188648, 0.00025931, 187.77295492, 0.00086438, -18.77729549, -8.644e-05, -56.33188648, -0.00025931, -187.77295492, -0.00086438, 0.4, 0.3, 0.003, 0.0, 0.0, 13025, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3025, 99999, 'P', 43025, 'Vy', 33025, 'Vz', 23025, 'My', 13025, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173025, 73025, 173025, 3025, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124025, 124025, 24025, 3025, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173026, 3.85, 14.4, 9.1)
    ops.node(124026, 3.85, 14.4, 11.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3026, 173026, 124026, 0.1225, 29840476.87872986, 12433532.03280411, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23026, 58.15349074, 0.0009111, 70.72007187, 0.02499136, 7.07200719, 0.08362197, -58.15349074, -0.0009111, -70.72007187, -0.02499136, -7.07200719, -0.08362197, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13026, 69.23430274, 0.0009111, 84.19537337, 0.02499136, 8.41953734, 0.08362197, -69.23430274, -0.0009111, -84.19537337, -0.02499136, -8.41953734, -0.08362197, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23026, 3026, 0.0, 135.33309758, 0.01822201, 135.33309758, 0.05466604, 94.7331683, -5464.27467979, 0.05, 2, 0, 73026, 24026, 2, 3)
    ops.uniaxialMaterial('LimitState', 43026, 33.83327439, 7.864e-05, 101.49982318, 0.00023591, 338.33274394, 0.00078635, -33.83327439, -7.864e-05, -101.49982318, -0.00023591, -338.33274394, -0.00078635, 0.4, 0.3, 0.003, 0.0, 0.0, 23026, 2)
    ops.limitCurve('ThreePoint', 13026, 3026, 0.0, 135.33309758, 0.01822201, 135.33309758, 0.05466604, 94.7331683, -5464.27467979, 0.05, 2, 0, 73026, 24026, 1, 3)
    ops.uniaxialMaterial('LimitState', 33026, 33.83327439, 7.864e-05, 101.49982318, 0.00023591, 338.33274394, 0.00078635, -33.83327439, -7.864e-05, -101.49982318, -0.00023591, -338.33274394, -0.00078635, 0.4, 0.3, 0.003, 0.0, 0.0, 13026, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3026, 99999, 'P', 43026, 'Vy', 33026, 'Vz', 23026, 'My', 13026, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173026, 73026, 173026, 3026, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124026, 124026, 24026, 3026, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173027, 7.7, 14.4, 9.1)
    ops.node(124027, 7.7, 14.4, 11.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3027, 173027, 124027, 0.1225, 31053670.81572603, 12939029.50655251, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23027, 58.71931491, 0.00093229, 71.15718883, 0.02349018, 7.11571888, 0.08243649, -58.71931491, -0.00093229, -71.15718883, -0.02349018, -7.11571888, -0.08243649, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13027, 69.28692664, 0.00093229, 83.96322282, 0.02349018, 8.39632228, 0.08243649, -69.28692664, -0.00093229, -83.96322282, -0.02349018, -8.39632228, -0.08243649, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23027, 3027, 0.0, 136.31825769, 0.01864585, 136.31825769, 0.05593756, 95.42278039, -4973.93387668, 0.05, 2, 0, 73027, 24027, 2, 3)
    ops.uniaxialMaterial('LimitState', 43027, 34.07956442, 7.611e-05, 102.23869327, 0.00022834, 340.79564423, 0.00076113, -34.07956442, -7.611e-05, -102.23869327, -0.00022834, -340.79564423, -0.00076113, 0.4, 0.3, 0.003, 0.0, 0.0, 23027, 2)
    ops.limitCurve('ThreePoint', 13027, 3027, 0.0, 136.31825769, 0.01864585, 136.31825769, 0.05593756, 95.42278039, -4973.93387668, 0.05, 2, 0, 73027, 24027, 1, 3)
    ops.uniaxialMaterial('LimitState', 33027, 34.07956442, 7.611e-05, 102.23869327, 0.00022834, 340.79564423, 0.00076113, -34.07956442, -7.611e-05, -102.23869327, -0.00022834, -340.79564423, -0.00076113, 0.4, 0.3, 0.003, 0.0, 0.0, 13027, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3027, 99999, 'P', 43027, 'Vy', 33027, 'Vz', 23027, 'My', 13027, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173027, 73027, 173027, 3027, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124027, 124027, 24027, 3027, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173028, 11.55, 14.4, 9.1)
    ops.node(124028, 11.55, 14.4, 11.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3028, 173028, 124028, 0.0625, 29911446.83995828, 12463102.84998262, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23028, 30.18083346, 0.00112855, 36.66056513, 0.02433119, 3.66605651, 0.08667203, -30.18083346, -0.00112855, -36.66056513, -0.02433119, -3.66605651, -0.08667203, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13028, 33.79901077, 0.00112855, 41.05555393, 0.02433119, 4.10555539, 0.08667203, -33.79901077, -0.00112855, -41.05555393, -0.02433119, -4.10555539, -0.08667203, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23028, 3028, 0.0, 79.40516663, 0.02257093, 79.40516663, 0.0677128, 55.58361664, -2853.35762375, 0.05, 2, 0, 73028, 24028, 2, 3)
    ops.uniaxialMaterial('LimitState', 43028, 19.85129166, 9.022e-05, 59.55387497, 0.00027065, 198.51291658, 0.00090216, -19.85129166, -9.022e-05, -59.55387497, -0.00027065, -198.51291658, -0.00090216, 0.4, 0.3, 0.003, 0.0, 0.0, 23028, 2)
    ops.limitCurve('ThreePoint', 13028, 3028, 0.0, 79.40516663, 0.02257093, 79.40516663, 0.0677128, 55.58361664, -2853.35762375, 0.05, 2, 0, 73028, 24028, 1, 3)
    ops.uniaxialMaterial('LimitState', 33028, 19.85129166, 9.022e-05, 59.55387497, 0.00027065, 198.51291658, 0.00090216, -19.85129166, -9.022e-05, -59.55387497, -0.00027065, -198.51291658, -0.00090216, 0.4, 0.3, 0.003, 0.0, 0.0, 13028, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3028, 99999, 'P', 43028, 'Vy', 33028, 'Vz', 23028, 'My', 13028, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173028, 73028, 173028, 3028, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124028, 124028, 24028, 3028, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173029, 14.6, 14.4, 9.1)
    ops.node(124029, 14.6, 14.4, 11.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3029, 173029, 124029, 0.0625, 27762106.93672669, 11567544.55696946, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23029, 32.44246527, 0.0013215, 39.60943867, 0.02283534, 3.96094387, 0.08393538, -32.44246527, -0.0013215, -39.60943867, -0.02283534, -3.96094387, -0.08393538, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13029, 36.20856924, 0.0013215, 44.20752527, 0.02283534, 4.42075253, 0.08393538, -36.20856924, -0.0013215, -44.20752527, -0.02283534, -4.42075253, -0.08393538, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23029, 3029, 0.0, 73.49881264, 0.02642996, 73.49881264, 0.07928989, 51.44916885, -2625.89544639, 0.05, 2, 0, 73029, 24029, 2, 3)
    ops.uniaxialMaterial('LimitState', 43029, 18.37470316, 8.997e-05, 55.12410948, 0.00026991, 183.7470316, 0.00089971, -18.37470316, -8.997e-05, -55.12410948, -0.00026991, -183.7470316, -0.00089971, 0.4, 0.3, 0.003, 0.0, 0.0, 23029, 2)
    ops.limitCurve('ThreePoint', 13029, 3029, 0.0, 73.49881264, 0.02642996, 73.49881264, 0.07928989, 51.44916885, -2625.89544639, 0.05, 2, 0, 73029, 24029, 1, 3)
    ops.uniaxialMaterial('LimitState', 33029, 18.37470316, 8.997e-05, 55.12410948, 0.00026991, 183.7470316, 0.00089971, -18.37470316, -8.997e-05, -55.12410948, -0.00026991, -183.7470316, -0.00089971, 0.4, 0.3, 0.003, 0.0, 0.0, 13029, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3029, 99999, 'P', 43029, 'Vy', 33029, 'Vz', 23029, 'My', 13029, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173029, 73029, 173029, 3029, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124029, 124029, 24029, 3029, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173030, 18.45, 14.4, 9.1)
    ops.node(124030, 18.45, 14.4, 11.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3030, 173030, 124030, 0.1225, 29760943.88531344, 12400393.28554727, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23030, 60.2533019, 0.00092832, 73.28959825, 0.02447802, 7.32895983, 0.08308602, -60.2533019, -0.00092832, -73.28959825, -0.02447802, -7.32895983, -0.08308602, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13030, 72.13502764, 0.00092832, 87.74203287, 0.02447802, 8.77420329, 0.08308602, -72.13502764, -0.00092832, -87.74203287, -0.02447802, -8.77420329, -0.08308602, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23030, 3030, 0.0, 135.28082068, 0.01856631, 135.28082068, 0.05569892, 94.69657448, -5498.42648845, 0.05, 2, 0, 73030, 24030, 2, 3)
    ops.uniaxialMaterial('LimitState', 43030, 33.82020517, 7.881e-05, 101.46061551, 0.00023644, 338.20205171, 0.00078815, -33.82020517, -7.881e-05, -101.46061551, -0.00023644, -338.20205171, -0.00078815, 0.4, 0.3, 0.003, 0.0, 0.0, 23030, 2)
    ops.limitCurve('ThreePoint', 13030, 3030, 0.0, 135.28082068, 0.01856631, 135.28082068, 0.05569892, 94.69657448, -5498.42648845, 0.05, 2, 0, 73030, 24030, 1, 3)
    ops.uniaxialMaterial('LimitState', 33030, 33.82020517, 7.881e-05, 101.46061551, 0.00023644, 338.20205171, 0.00078815, -33.82020517, -7.881e-05, -101.46061551, -0.00023644, -338.20205171, -0.00078815, 0.4, 0.3, 0.003, 0.0, 0.0, 13030, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3030, 99999, 'P', 43030, 'Vy', 33030, 'Vz', 23030, 'My', 13030, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173030, 73030, 173030, 3030, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124030, 124030, 24030, 3030, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173031, 22.3, 14.4, 9.1)
    ops.node(124031, 22.3, 14.4, 11.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3031, 173031, 124031, 0.1225, 29304337.85267856, 12210140.7719494, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23031, 55.93578222, 0.0008964, 68.12098929, 0.0261676, 6.81209893, 0.08464075, -55.93578222, -0.0008964, -68.12098929, -0.0261676, -6.81209893, -0.08464075, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13031, 66.2960476, 0.0008964, 80.73816383, 0.0261676, 8.07381638, 0.08464075, -66.2960476, -0.0008964, -80.73816383, -0.0261676, -8.07381638, -0.08464075, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23031, 3031, 0.0, 134.03233005, 0.01792806, 134.03233005, 0.05378419, 93.82263104, -5554.89228492, 0.05, 2, 0, 73031, 24031, 2, 3)
    ops.uniaxialMaterial('LimitState', 43031, 33.50808251, 7.93e-05, 100.52424754, 0.00023791, 335.08082513, 0.00079304, -33.50808251, -7.93e-05, -100.52424754, -0.00023791, -335.08082513, -0.00079304, 0.4, 0.3, 0.003, 0.0, 0.0, 23031, 2)
    ops.limitCurve('ThreePoint', 13031, 3031, 0.0, 134.03233005, 0.01792806, 134.03233005, 0.05378419, 93.82263104, -5554.89228492, 0.05, 2, 0, 73031, 24031, 1, 3)
    ops.uniaxialMaterial('LimitState', 33031, 33.50808251, 7.93e-05, 100.52424754, 0.00023791, 335.08082513, 0.00079304, -33.50808251, -7.93e-05, -100.52424754, -0.00023791, -335.08082513, -0.00079304, 0.4, 0.3, 0.003, 0.0, 0.0, 13031, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3031, 99999, 'P', 43031, 'Vy', 33031, 'Vz', 23031, 'My', 13031, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173031, 73031, 173031, 3031, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124031, 124031, 24031, 3031, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173032, 26.15, 14.4, 9.1)
    ops.node(124032, 26.15, 14.4, 11.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3032, 173032, 124032, 0.0625, 29564452.73588933, 12318521.97328722, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23032, 23.14943604, 0.00112752, 28.1725523, 0.02090182, 2.81725523, 0.08490237, -23.14943604, -0.00112752, -28.1725523, -0.02090182, -2.81725523, -0.08490237, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13032, 23.14943604, 0.00112752, 28.1725523, 0.02090182, 2.81725523, 0.08490237, -23.14943604, -0.00112752, -28.1725523, -0.02090182, -2.81725523, -0.08490237, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23032, 3032, 0.0, 70.7194851, 0.02255032, 70.7194851, 0.06765097, 49.50363957, -3086.87298068, 0.05, 2, 0, 73032, 24032, 2, 3)
    ops.uniaxialMaterial('LimitState', 43032, 17.67987127, 8.129e-05, 53.03961382, 0.00024387, 176.79871275, 0.00081291, -17.67987127, -8.129e-05, -53.03961382, -0.00024387, -176.79871275, -0.00081291, 0.4, 0.3, 0.003, 0.0, 0.0, 23032, 2)
    ops.limitCurve('ThreePoint', 13032, 3032, 0.0, 70.7194851, 0.02255032, 70.7194851, 0.06765097, 49.50363957, -3086.87298068, 0.05, 2, 0, 73032, 24032, 1, 3)
    ops.uniaxialMaterial('LimitState', 33032, 17.67987127, 8.129e-05, 53.03961382, 0.00024387, 176.79871275, 0.00081291, -17.67987127, -8.129e-05, -53.03961382, -0.00024387, -176.79871275, -0.00081291, 0.4, 0.3, 0.003, 0.0, 0.0, 13032, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3032, 99999, 'P', 43032, 'Vy', 33032, 'Vz', 23032, 'My', 13032, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173032, 73032, 173032, 3032, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124032, 124032, 24032, 3032, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170004, 11.55, 0.0, 0.0)
    ops.node(124033, 11.55, 0.0, 1.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4085, 170004, 124033, 0.1225, 30287389.23523812, 12619745.51468255, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24085, 109.14959425, 0.00078352, 131.43874494, 0.02785697, 13.14387449, 0.08521089, -109.14959425, -0.00078352, -131.43874494, -0.02785697, -13.14387449, -0.08521089, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14085, 103.87681863, 0.00078352, 125.08922973, 0.02785697, 12.50892297, 0.08521089, -103.87681863, -0.00078352, -125.08922973, -0.02785697, -12.50892297, -0.08521089, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24085, 4085, 0.0, 223.69335901, 0.0156703, 223.69335901, 0.04701091, 156.58535131, -5541.21644195, 0.05, 2, 0, 70004, 24033, 2, 3)
    ops.uniaxialMaterial('LimitState', 44085, 55.92333975, 6.403e-05, 167.77001926, 0.00019209, 559.23339753, 0.00064029, -55.92333975, -6.403e-05, -167.77001926, -0.00019209, -559.23339753, -0.00064029, 0.4, 0.3, 0.003, 0.0, 0.0, 24085, 2)
    ops.limitCurve('ThreePoint', 14085, 4085, 0.0, 223.69335901, 0.0156703, 223.69335901, 0.04701091, 156.58535131, -5541.21644195, 0.05, 2, 0, 70004, 24033, 1, 3)
    ops.uniaxialMaterial('LimitState', 34085, 55.92333975, 6.403e-05, 167.77001926, 0.00019209, 559.23339753, 0.00064029, -55.92333975, -6.403e-05, -167.77001926, -0.00019209, -559.23339753, -0.00064029, 0.4, 0.3, 0.003, 0.0, 0.0, 14085, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4085, 99999, 'P', 44085, 'Vy', 34085, 'Vz', 24085, 'My', 14085, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170004, 70004, 170004, 4085, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124033, 124033, 24033, 4085, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174033, 11.55, 0.0, 1.675)
    ops.node(121004, 11.55, 0.0, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4086, 174033, 121004, 0.1225, 28165173.87929891, 11735489.11637455, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24086, 100.25394632, 0.00078408, 121.24589213, 0.02777776, 12.12458921, 0.08246903, -100.25394632, -0.00078408, -121.24589213, -0.02777776, -12.12458921, -0.08246903, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14086, 88.3630851, 0.00078408, 106.86523052, 0.02777776, 10.68652305, 0.08246903, -88.3630851, -0.00078408, -106.86523052, -0.02777776, -10.68652305, -0.08246903, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24086, 4086, 0.0, 208.50430368, 0.01568152, 208.50430368, 0.04704456, 145.95301257, -5633.95916503, 0.05, 2, 0, 74033, 21004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44086, 52.12607592, 6.418e-05, 156.37822776, 0.00019254, 521.26075919, 0.00064179, -52.12607592, -6.418e-05, -156.37822776, -0.00019254, -521.26075919, -0.00064179, 0.4, 0.3, 0.003, 0.0, 0.0, 24086, 2)
    ops.limitCurve('ThreePoint', 14086, 4086, 0.0, 208.50430368, 0.01568152, 208.50430368, 0.04704456, 145.95301257, -5633.95916503, 0.05, 2, 0, 74033, 21004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34086, 52.12607592, 6.418e-05, 156.37822776, 0.00019254, 521.26075919, 0.00064179, -52.12607592, -6.418e-05, -156.37822776, -0.00019254, -521.26075919, -0.00064179, 0.4, 0.3, 0.003, 0.0, 0.0, 14086, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4086, 99999, 'P', 44086, 'Vy', 34086, 'Vz', 24086, 'My', 14086, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174033, 74033, 174033, 4086, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121004, 121004, 21004, 4086, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170005, 14.6, 0.0, 0.0)
    ops.node(124034, 14.6, 0.0, 1.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4087, 170005, 124034, 0.1225, 27824764.82519826, 11593652.01049927, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24087, 111.28351374, 0.00080417, 134.4771309, 0.03046134, 13.44771309, 0.08252036, -111.28351374, -0.00080417, -134.4771309, -0.03046134, -13.44771309, -0.08252036, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14087, 105.35794699, 0.00080417, 127.31656248, 0.03046134, 12.73165625, 0.08252036, -105.35794699, -0.00080417, -127.31656248, -0.03046134, -12.73165625, -0.08252036, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24087, 4087, 0.0, 219.62978923, 0.01608337, 219.62978923, 0.0482501, 153.74085246, -6335.04282061, 0.05, 2, 0, 70005, 24034, 2, 3)
    ops.uniaxialMaterial('LimitState', 44087, 54.90744731, 6.843e-05, 164.72234193, 0.00020529, 549.07447309, 0.0006843, -54.90744731, -6.843e-05, -164.72234193, -0.00020529, -549.07447309, -0.0006843, 0.4, 0.3, 0.003, 0.0, 0.0, 24087, 2)
    ops.limitCurve('ThreePoint', 14087, 4087, 0.0, 219.62978923, 0.01608337, 219.62978923, 0.0482501, 153.74085246, -6335.04282061, 0.05, 2, 0, 70005, 24034, 1, 3)
    ops.uniaxialMaterial('LimitState', 34087, 54.90744731, 6.843e-05, 164.72234193, 0.00020529, 549.07447309, 0.0006843, -54.90744731, -6.843e-05, -164.72234193, -0.00020529, -549.07447309, -0.0006843, 0.4, 0.3, 0.003, 0.0, 0.0, 14087, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4087, 99999, 'P', 44087, 'Vy', 34087, 'Vz', 24087, 'My', 14087, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170005, 70005, 170005, 4087, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124034, 124034, 24034, 4087, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174034, 14.6, 0.0, 1.675)
    ops.node(121005, 14.6, 0.0, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4088, 174034, 121005, 0.1225, 27274279.87850375, 11364283.2827099, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24088, 100.49977275, 0.00078034, 121.64994706, 0.03050941, 12.16499471, 0.08311364, -100.49977275, -0.00078034, -121.64994706, -0.03050941, -12.16499471, -0.08311364, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14088, 88.11457424, 0.00078034, 106.65828387, 0.03050941, 10.66582839, 0.08311364, -88.11457424, -0.00078034, -106.65828387, -0.03050941, -10.66582839, -0.08311364, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24088, 4088, 0.0, 212.05861671, 0.01560682, 212.05861671, 0.04682047, 148.4410317, -6345.16670389, 0.05, 2, 0, 74034, 21005, 2, 3)
    ops.uniaxialMaterial('LimitState', 44088, 53.01465418, 6.74e-05, 159.04396253, 0.00020221, 530.14654177, 0.00067405, -53.01465418, -6.74e-05, -159.04396253, -0.00020221, -530.14654177, -0.00067405, 0.4, 0.3, 0.003, 0.0, 0.0, 24088, 2)
    ops.limitCurve('ThreePoint', 14088, 4088, 0.0, 212.05861671, 0.01560682, 212.05861671, 0.04682047, 148.4410317, -6345.16670389, 0.05, 2, 0, 74034, 21005, 1, 3)
    ops.uniaxialMaterial('LimitState', 34088, 53.01465418, 6.74e-05, 159.04396253, 0.00020221, 530.14654177, 0.00067405, -53.01465418, -6.74e-05, -159.04396253, -0.00020221, -530.14654177, -0.00067405, 0.4, 0.3, 0.003, 0.0, 0.0, 14088, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4088, 99999, 'P', 44088, 'Vy', 34088, 'Vz', 24088, 'My', 14088, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174034, 74034, 174034, 4088, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121005, 121005, 21005, 4088, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171004, 11.55, 0.0, 3.2)
    ops.node(124035, 11.55, 0.0, 4.175)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4090, 171004, 124035, 0.1225, 28312833.43157547, 11797013.92982311, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24090, 94.13999866, 0.00079953, 114.07935071, 0.04251953, 11.40793507, 0.12560937, -94.13999866, -0.00079953, -114.07935071, -0.04251953, -11.40793507, -0.12560937, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14090, 82.65298818, 0.00079953, 100.15933037, 0.04251953, 10.01593304, 0.12560937, -82.65298818, -0.00079953, -100.15933037, -0.04251953, -10.01593304, -0.12560937, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24090, 4090, 0.0, 248.49376323, 0.0159907, 248.49376323, 0.04797209, 173.94563426, -10934.39030257, 0.05, 2, 0, 71004, 24035, 2, 3)
    ops.uniaxialMaterial('LimitState', 44090, 62.12344081, 7.609e-05, 186.37032242, 0.00022827, 621.23440807, 0.00076089, -62.12344081, -7.609e-05, -186.37032242, -0.00022827, -621.23440807, -0.00076089, 0.4, 0.3, 0.003, 0.0, 0.0, 24090, 2)
    ops.limitCurve('ThreePoint', 14090, 4090, 0.0, 248.49376323, 0.0159907, 248.49376323, 0.04797209, 173.94563426, -10934.39030257, 0.05, 2, 0, 71004, 24035, 1, 3)
    ops.uniaxialMaterial('LimitState', 34090, 62.12344081, 7.609e-05, 186.37032242, 0.00022827, 621.23440807, 0.00076089, -62.12344081, -7.609e-05, -186.37032242, -0.00022827, -621.23440807, -0.00076089, 0.4, 0.3, 0.003, 0.0, 0.0, 14090, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4090, 99999, 'P', 44090, 'Vy', 34090, 'Vz', 24090, 'My', 14090, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171004, 71004, 171004, 4090, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124035, 124035, 24035, 4090, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174035, 11.55, 0.0, 4.675)
    ops.node(122004, 11.55, 0.0, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4091, 174035, 122004, 0.1225, 25542048.86927399, 10642520.3621975, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24091, 84.88737251, 0.0007833, 103.29844685, 0.04402585, 10.32984468, 0.12191617, -84.88737251, -0.0007833, -103.29844685, -0.04402585, -10.32984468, -0.12191617, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14091, 84.88737251, 0.0007833, 103.29844685, 0.04402585, 10.32984468, 0.12191617, -84.88737251, -0.0007833, -103.29844685, -0.04402585, -10.32984468, -0.12191617, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24091, 4091, 0.0, 237.27711144, 0.01566591, 237.27711144, 0.04699772, 166.09397801, -12656.49178914, 0.05, 2, 0, 74035, 22004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44091, 59.31927786, 8.054e-05, 177.95783358, 0.00024161, 593.19277861, 0.00080536, -59.31927786, -8.054e-05, -177.95783358, -0.00024161, -593.19277861, -0.00080536, 0.4, 0.3, 0.003, 0.0, 0.0, 24091, 2)
    ops.limitCurve('ThreePoint', 14091, 4091, 0.0, 237.27711144, 0.01566591, 237.27711144, 0.04699772, 166.09397801, -12656.49178914, 0.05, 2, 0, 74035, 22004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34091, 59.31927786, 8.054e-05, 177.95783358, 0.00024161, 593.19277861, 0.00080536, -59.31927786, -8.054e-05, -177.95783358, -0.00024161, -593.19277861, -0.00080536, 0.4, 0.3, 0.003, 0.0, 0.0, 14091, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4091, 99999, 'P', 44091, 'Vy', 34091, 'Vz', 24091, 'My', 14091, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174035, 74035, 174035, 4091, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122004, 122004, 22004, 4091, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171005, 14.6, 0.0, 3.2)
    ops.node(124036, 14.6, 0.0, 4.175)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4092, 171005, 124036, 0.1225, 29938928.05613865, 12474553.35672444, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24092, 97.29672845, 0.00075905, 117.56129102, 0.04478028, 11.7561291, 0.1318173, -97.29672845, -0.00075905, -117.56129102, -0.04478028, -11.7561291, -0.1318173, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14092, 84.48017304, 0.00075905, 102.07535614, 0.04478028, 10.20753561, 0.1318173, -84.48017304, -0.00075905, -102.07535614, -0.04478028, -10.20753561, -0.1318173, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24092, 4092, 0.0, 270.1747857, 0.01518092, 270.1747857, 0.04554276, 189.12234999, -12588.49682608, 0.05, 2, 0, 71005, 24036, 2, 3)
    ops.uniaxialMaterial('LimitState', 44092, 67.54369643, 7.823e-05, 202.63108928, 0.0002347, 675.43696425, 0.00078234, -67.54369643, -7.823e-05, -202.63108928, -0.0002347, -675.43696425, -0.00078234, 0.4, 0.3, 0.003, 0.0, 0.0, 24092, 2)
    ops.limitCurve('ThreePoint', 14092, 4092, 0.0, 270.1747857, 0.01518092, 270.1747857, 0.04554276, 189.12234999, -12588.49682608, 0.05, 2, 0, 71005, 24036, 1, 3)
    ops.uniaxialMaterial('LimitState', 34092, 67.54369643, 7.823e-05, 202.63108928, 0.0002347, 675.43696425, 0.00078234, -67.54369643, -7.823e-05, -202.63108928, -0.0002347, -675.43696425, -0.00078234, 0.4, 0.3, 0.003, 0.0, 0.0, 14092, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4092, 99999, 'P', 44092, 'Vy', 34092, 'Vz', 24092, 'My', 14092, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171005, 71005, 171005, 4092, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124036, 124036, 24036, 4092, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174036, 14.6, 0.0, 4.675)
    ops.node(122005, 14.6, 0.0, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4093, 174036, 122005, 0.1225, 28418771.36843697, 11841154.73684874, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24093, 82.09850771, 0.00078703, 99.58208873, 0.04514125, 9.95820887, 0.13132165, -82.09850771, -0.00078703, -99.58208873, -0.04514125, -9.95820887, -0.13132165, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14093, 82.09850771, 0.00078703, 99.58208873, 0.04514125, 9.95820887, 0.13132165, -82.09850771, -0.00078703, -99.58208873, -0.04514125, -9.95820887, -0.13132165, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24093, 4093, 0.0, 260.34607666, 0.01574058, 260.34607666, 0.04722175, 182.24225366, -13820.60042852, 0.05, 2, 0, 74036, 22005, 2, 3)
    ops.uniaxialMaterial('LimitState', 44093, 65.08651917, 7.942e-05, 195.2595575, 0.00023826, 650.86519165, 0.00079421, -65.08651917, -7.942e-05, -195.2595575, -0.00023826, -650.86519165, -0.00079421, 0.4, 0.3, 0.003, 0.0, 0.0, 24093, 2)
    ops.limitCurve('ThreePoint', 14093, 4093, 0.0, 260.34607666, 0.01574058, 260.34607666, 0.04722175, 182.24225366, -13820.60042852, 0.05, 2, 0, 74036, 22005, 1, 3)
    ops.uniaxialMaterial('LimitState', 34093, 65.08651917, 7.942e-05, 195.2595575, 0.00023826, 650.86519165, 0.00079421, -65.08651917, -7.942e-05, -195.2595575, -0.00023826, -650.86519165, -0.00079421, 0.4, 0.3, 0.003, 0.0, 0.0, 14093, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4093, 99999, 'P', 44093, 'Vy', 34093, 'Vz', 24093, 'My', 14093, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174036, 74036, 174036, 4093, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122005, 122005, 22005, 4093, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172004, 11.55, 0.0, 6.15)
    ops.node(124037, 11.55, 0.0, 7.175)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4095, 172004, 124037, 0.0625, 27828862.46290033, 11595359.3595418, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24095, 34.74861022, 0.00094734, 42.03329804, 0.02194085, 4.2033298, 0.07782872, -34.74861022, -0.00094734, -42.03329804, -0.02194085, -4.2033298, -0.07782872, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14095, 34.74861022, 0.00094734, 42.03329804, 0.02194085, 4.2033298, 0.07782872, -34.74861022, -0.00094734, -42.03329804, -0.02194085, -4.2033298, -0.07782872, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24095, 4095, 0.0, 87.14109297, 0.01894687, 87.14109297, 0.05684062, 60.99876508, -2813.10704863, 0.05, 2, 0, 72004, 24037, 2, 3)
    ops.uniaxialMaterial('LimitState', 44095, 21.78527324, 5.321e-05, 65.35581972, 0.00015962, 217.85273241, 0.00053207, -21.78527324, -5.321e-05, -65.35581972, -0.00015962, -217.85273241, -0.00053207, 0.4, 0.3, 0.003, 0.0, 0.0, 24095, 2)
    ops.limitCurve('ThreePoint', 14095, 4095, 0.0, 87.14109297, 0.01894687, 87.14109297, 0.05684062, 60.99876508, -2813.10704863, 0.05, 2, 0, 72004, 24037, 1, 3)
    ops.uniaxialMaterial('LimitState', 34095, 21.78527324, 5.321e-05, 65.35581972, 0.00015962, 217.85273241, 0.00053207, -21.78527324, -5.321e-05, -65.35581972, -0.00015962, -217.85273241, -0.00053207, 0.4, 0.3, 0.003, 0.0, 0.0, 14095, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4095, 99999, 'P', 44095, 'Vy', 34095, 'Vz', 24095, 'My', 14095, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172004, 72004, 172004, 4095, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124037, 124037, 24037, 4095, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174037, 11.55, 0.0, 7.575)
    ops.node(123004, 11.55, 0.0, 8.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4096, 174037, 123004, 0.0625, 27134812.25109316, 11306171.77128882, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24096, 43.07298781, 0.00106563, 52.27942212, 0.02268489, 5.22794221, 0.08150835, -43.07298781, -0.00106563, -52.27942212, -0.02268489, -5.22794221, -0.08150835, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14096, 39.38069681, 0.00106563, 47.79793965, 0.02268489, 4.77979397, 0.08150835, -39.38069681, -0.00106563, -47.79793965, -0.02268489, -4.77979397, -0.08150835, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24096, 4096, 0.0, 83.14142516, 0.02131267, 83.14142516, 0.06393802, 58.19899761, -2973.3277014, 0.05, 2, 0, 74037, 23004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44096, 20.78535629, 5.206e-05, 62.35606887, 0.00015619, 207.85356289, 0.00052064, -20.78535629, -5.206e-05, -62.35606887, -0.00015619, -207.85356289, -0.00052064, 0.4, 0.3, 0.003, 0.0, 0.0, 24096, 2)
    ops.limitCurve('ThreePoint', 14096, 4096, 0.0, 83.14142516, 0.02131267, 83.14142516, 0.06393802, 58.19899761, -2973.3277014, 0.05, 2, 0, 74037, 23004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34096, 20.78535629, 5.206e-05, 62.35606887, 0.00015619, 207.85356289, 0.00052064, -20.78535629, -5.206e-05, -62.35606887, -0.00015619, -207.85356289, -0.00052064, 0.4, 0.3, 0.003, 0.0, 0.0, 14096, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4096, 99999, 'P', 44096, 'Vy', 34096, 'Vz', 24096, 'My', 14096, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174037, 74037, 174037, 4096, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123004, 123004, 23004, 4096, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172005, 14.6, 0.0, 6.15)
    ops.node(124038, 14.6, 0.0, 7.175)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4097, 172005, 124038, 0.0625, 28361905.44655066, 11817460.60272944, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24097, 36.41613003, 0.00105351, 44.02390514, 0.02422247, 4.40239051, 0.08136749, -36.41613003, -0.00105351, -44.02390514, -0.02422247, -4.40239051, -0.08136749, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14097, 36.41613003, 0.00105351, 44.02390514, 0.02422247, 4.40239051, 0.08136749, -36.41613003, -0.00105351, -44.02390514, -0.02422247, -4.40239051, -0.08136749, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24097, 4097, 0.0, 95.79780153, 0.02107029, 95.79780153, 0.06321086, 67.05846107, -3453.75075408, 0.05, 2, 0, 72005, 24038, 2, 3)
    ops.uniaxialMaterial('LimitState', 44097, 23.94945038, 5.739e-05, 71.84835115, 0.00017218, 239.49450383, 0.00057394, -23.94945038, -5.739e-05, -71.84835115, -0.00017218, -239.49450383, -0.00057394, 0.4, 0.3, 0.003, 0.0, 0.0, 24097, 2)
    ops.limitCurve('ThreePoint', 14097, 4097, 0.0, 95.79780153, 0.02107029, 95.79780153, 0.06321086, 67.05846107, -3453.75075408, 0.05, 2, 0, 72005, 24038, 1, 3)
    ops.uniaxialMaterial('LimitState', 34097, 23.94945038, 5.739e-05, 71.84835115, 0.00017218, 239.49450383, 0.00057394, -23.94945038, -5.739e-05, -71.84835115, -0.00017218, -239.49450383, -0.00057394, 0.4, 0.3, 0.003, 0.0, 0.0, 14097, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4097, 99999, 'P', 44097, 'Vy', 34097, 'Vz', 24097, 'My', 14097, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172005, 72005, 172005, 4097, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124038, 124038, 24038, 4097, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174038, 14.6, 0.0, 7.575)
    ops.node(123005, 14.6, 0.0, 8.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4098, 174038, 123005, 0.0625, 27993800.22407941, 11664083.42669975, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24098, 42.18040742, 0.00096616, 51.14256294, 0.02848401, 5.11425629, 0.08914522, -42.18040742, -0.00096616, -51.14256294, -0.02848401, -5.11425629, -0.08914522, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14098, 38.3972018, 0.00096616, 46.55553205, 0.02848401, 4.6555532, 0.08914522, -38.3972018, -0.00096616, -46.55553205, -0.02848401, -4.6555532, -0.08914522, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24098, 4098, 0.0, 97.41153625, 0.01932325, 97.41153625, 0.05796976, 68.18807538, -4255.11334333, 0.05, 2, 0, 74038, 23005, 2, 3)
    ops.uniaxialMaterial('LimitState', 44098, 24.35288406, 5.913e-05, 73.05865219, 0.00017738, 243.52884063, 0.00059128, -24.35288406, -5.913e-05, -73.05865219, -0.00017738, -243.52884063, -0.00059128, 0.4, 0.3, 0.003, 0.0, 0.0, 24098, 2)
    ops.limitCurve('ThreePoint', 14098, 4098, 0.0, 97.41153625, 0.01932325, 97.41153625, 0.05796976, 68.18807538, -4255.11334333, 0.05, 2, 0, 74038, 23005, 1, 3)
    ops.uniaxialMaterial('LimitState', 34098, 24.35288406, 5.913e-05, 73.05865219, 0.00017738, 243.52884063, 0.00059128, -24.35288406, -5.913e-05, -73.05865219, -0.00017738, -243.52884063, -0.00059128, 0.4, 0.3, 0.003, 0.0, 0.0, 14098, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4098, 99999, 'P', 44098, 'Vy', 34098, 'Vz', 24098, 'My', 14098, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174038, 74038, 174038, 4098, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123005, 123005, 23005, 4098, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173004, 11.55, 0.0, 9.1)
    ops.node(124039, 11.55, 0.0, 10.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4100, 173004, 124039, 0.0625, 28371174.50627796, 11821322.71094915, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24100, 26.40304629, 0.00094965, 32.14897548, 0.01848507, 3.21489755, 0.07750558, -26.40304629, -0.00094965, -32.14897548, -0.01848507, -3.21489755, -0.07750558, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14100, 26.40304629, 0.00094965, 32.14897548, 0.01848507, 3.21489755, 0.07750558, -26.40304629, -0.00094965, -32.14897548, -0.01848507, -3.21489755, -0.07750558, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24100, 4100, 0.0, 68.97335188, 0.01899299, 68.97335188, 0.05697898, 48.28134632, -3066.38938234, 0.05, 2, 0, 73004, 24039, 2, 3)
    ops.uniaxialMaterial('LimitState', 44100, 17.24333797, 4.131e-05, 51.73001391, 0.00012393, 172.4333797, 0.00041309, -17.24333797, -4.131e-05, -51.73001391, -0.00012393, -172.4333797, -0.00041309, 0.4, 0.3, 0.003, 0.0, 0.0, 24100, 2)
    ops.limitCurve('ThreePoint', 14100, 4100, 0.0, 68.97335188, 0.01899299, 68.97335188, 0.05697898, 48.28134632, -3066.38938234, 0.05, 2, 0, 73004, 24039, 1, 3)
    ops.uniaxialMaterial('LimitState', 34100, 17.24333797, 4.131e-05, 51.73001391, 0.00012393, 172.4333797, 0.00041309, -17.24333797, -4.131e-05, -51.73001391, -0.00012393, -172.4333797, -0.00041309, 0.4, 0.3, 0.003, 0.0, 0.0, 14100, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4100, 99999, 'P', 44100, 'Vy', 34100, 'Vz', 24100, 'My', 14100, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173004, 73004, 173004, 4100, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124039, 124039, 24039, 4100, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174039, 11.55, 0.0, 10.525)
    ops.node(124004, 11.55, 0.0, 11.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4101, 174039, 124004, 0.0625, 29225643.16337052, 12177351.31807105, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24101, 23.75654755, 0.00088745, 28.93478265, 0.02186597, 2.89347826, 0.08559331, -23.75654755, -0.00088745, -28.93478265, -0.02186597, -2.89347826, -0.08559331, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14101, 23.75654755, 0.00088745, 28.93478265, 0.02186597, 2.89347826, 0.08559331, -23.75654755, -0.00088745, -28.93478265, -0.02186597, -2.89347826, -0.08559331, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24101, 4101, 0.0, 75.41871595, 0.01774896, 75.41871595, 0.05324689, 52.79310116, -6621.82139307, 0.05, 2, 0, 74039, 24004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44101, 18.85467899, 4.385e-05, 56.56403696, 0.00013155, 188.54678986, 0.00043849, -18.85467899, -4.385e-05, -56.56403696, -0.00013155, -188.54678986, -0.00043849, 0.4, 0.3, 0.003, 0.0, 0.0, 24101, 2)
    ops.limitCurve('ThreePoint', 14101, 4101, 0.0, 75.41871595, 0.01774896, 75.41871595, 0.05324689, 52.79310116, -6621.82139307, 0.05, 2, 0, 74039, 24004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34101, 18.85467899, 4.385e-05, 56.56403696, 0.00013155, 188.54678986, 0.00043849, -18.85467899, -4.385e-05, -56.56403696, -0.00013155, -188.54678986, -0.00043849, 0.4, 0.3, 0.003, 0.0, 0.0, 14101, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4101, 99999, 'P', 44101, 'Vy', 34101, 'Vz', 24101, 'My', 14101, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174039, 74039, 174039, 4101, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124004, 124004, 24004, 4101, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173005, 14.6, 0.0, 9.1)
    ops.node(124040, 14.6, 0.0, 10.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4102, 173005, 124040, 0.0625, 29571572.26192649, 12321488.44246937, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24102, 25.52309339, 0.00089882, 30.99323256, 0.02277858, 3.09932326, 0.0827662, -25.52309339, -0.00089882, -30.99323256, -0.02277858, -3.09932326, -0.0827662, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14102, 25.52309339, 0.00089882, 30.99323256, 0.02277858, 3.09932326, 0.0827662, -25.52309339, -0.00089882, -30.99323256, -0.02277858, -3.09932326, -0.0827662, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24102, 4102, 0.0, 82.84096246, 0.01797632, 82.84096246, 0.05392896, 57.98867372, -4277.52372531, 0.05, 2, 0, 73005, 24040, 2, 3)
    ops.uniaxialMaterial('LimitState', 44102, 20.71024061, 4.76e-05, 62.13072184, 0.0001428, 207.10240615, 0.00047601, -20.71024061, -4.76e-05, -62.13072184, -0.0001428, -207.10240615, -0.00047601, 0.4, 0.3, 0.003, 0.0, 0.0, 24102, 2)
    ops.limitCurve('ThreePoint', 14102, 4102, 0.0, 82.84096246, 0.01797632, 82.84096246, 0.05392896, 57.98867372, -4277.52372531, 0.05, 2, 0, 73005, 24040, 1, 3)
    ops.uniaxialMaterial('LimitState', 34102, 20.71024061, 4.76e-05, 62.13072184, 0.0001428, 207.10240615, 0.00047601, -20.71024061, -4.76e-05, -62.13072184, -0.0001428, -207.10240615, -0.00047601, 0.4, 0.3, 0.003, 0.0, 0.0, 14102, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4102, 99999, 'P', 44102, 'Vy', 34102, 'Vz', 24102, 'My', 14102, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173005, 73005, 173005, 4102, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124040, 124040, 24040, 4102, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174040, 14.6, 0.0, 10.525)
    ops.node(124005, 14.6, 0.0, 11.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4103, 174040, 124005, 0.0625, 31196063.10076448, 12998359.62531853, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24103, 23.75324927, 0.00085745, 28.7697258, 0.02139449, 2.87697258, 0.08573824, -23.75324927, -0.00085745, -28.7697258, -0.02139449, -2.87697258, -0.08573824, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14103, 23.75324927, 0.00085745, 28.7697258, 0.02139449, 2.87697258, 0.08573824, -23.75324927, -0.00085745, -28.7697258, -0.02139449, -2.87697258, -0.08573824, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24103, 4103, 0.0, 82.44706277, 0.01714895, 82.44706277, 0.05144684, 57.71294394, -7599.50618519, 0.05, 2, 0, 74040, 24005, 2, 3)
    ops.uniaxialMaterial('LimitState', 44103, 20.61176569, 4.491e-05, 61.83529708, 0.00013472, 206.11765693, 0.00044908, -20.61176569, -4.491e-05, -61.83529708, -0.00013472, -206.11765693, -0.00044908, 0.4, 0.3, 0.003, 0.0, 0.0, 24103, 2)
    ops.limitCurve('ThreePoint', 14103, 4103, 0.0, 82.44706277, 0.01714895, 82.44706277, 0.05144684, 57.71294394, -7599.50618519, 0.05, 2, 0, 74040, 24005, 1, 3)
    ops.uniaxialMaterial('LimitState', 34103, 20.61176569, 4.491e-05, 61.83529708, 0.00013472, 206.11765693, 0.00044908, -20.61176569, -4.491e-05, -61.83529708, -0.00013472, -206.11765693, -0.00044908, 0.4, 0.3, 0.003, 0.0, 0.0, 14103, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4103, 99999, 'P', 44103, 'Vy', 34103, 'Vz', 24103, 'My', 14103, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174040, 74040, 174040, 4103, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124005, 124005, 24005, 4103, '-orient', 0, 0, 1, 0, 1, 0)
