import openseespy.opensees as ops


def add_columns() -> None:
    """Add components of all columns to ops domain (plastic hinges, column elements and nodes)
    """
    # Create elastic column element nodes
    ops.node(170001, 0.0, 0.0, 0.0)
    ops.node(121001, 0.0, 0.0, 3.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1, 170001, 121001, 0.16, 24563224.2069678, 10234676.75290325, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20001, 115.00549707, 0.0009805, 140.01042544, 0.01515757, 14.00104254, 0.04722368, -115.00549707, -0.0009805, -140.01042544, -0.01515757, -14.00104254, -0.04722368, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10001, 122.21958465, 0.0009805, 148.79302711, 0.01515757, 14.87930271, 0.04722368, -122.21958465, -0.0009805, -148.79302711, -0.01515757, -14.87930271, -0.04722368, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20001, 1, 0.0, 136.18716686, 0.01960997, 136.18716686, 0.05882991, 95.33101681, -1416.15929826, 0.05, 2, 0, 70001, 21001, 2, 3)
    ops.uniaxialMaterial('LimitState', 40001, 34.04679172, 8.857e-05, 102.14037515, 0.00026571, 340.46791716, 0.00088571, -34.04679172, -8.857e-05, -102.14037515, -0.00026571, -340.46791716, -0.00088571, 0.4, 0.3, 0.003, 0.0, 0.0, 20001, 2)
    ops.limitCurve('ThreePoint', 10001, 1, 0.0, 136.18716686, 0.01960997, 136.18716686, 0.05882991, 95.33101681, -1416.15929826, 0.05, 2, 0, 70001, 21001, 1, 3)
    ops.uniaxialMaterial('LimitState', 30001, 34.04679172, 8.857e-05, 102.14037515, 0.00026571, 340.46791716, 0.00088571, -34.04679172, -8.857e-05, -102.14037515, -0.00026571, -340.46791716, -0.00088571, 0.4, 0.3, 0.003, 0.0, 0.0, 10001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1, 99999, 'P', 40001, 'Vy', 30001, 'Vz', 20001, 'My', 10001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170001, 70001, 170001, 1, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121001, 121001, 21001, 1, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170004, 14.45, 0.0, 0.0)
    ops.node(121004, 14.45, 0.0, 3.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4, 170004, 121004, 0.16, 27810128.47716095, 11587553.5321504, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20004, 113.65716288, 0.0009502, 138.00322639, 0.01893003, 13.80032264, 0.05541838, -113.65716288, -0.0009502, -138.00322639, -0.01893003, -13.80032264, -0.05541838, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10004, 120.15221181, 0.0009502, 145.88955477, 0.01893003, 14.58895548, 0.05541838, -120.15221181, -0.0009502, -145.88955477, -0.01893003, -14.58895548, -0.05541838, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20004, 4, 0.0, 163.45398227, 0.01900393, 163.45398227, 0.05701179, 114.41778759, -1788.70555714, 0.05, 2, 0, 70004, 21004, 2, 3)
    ops.uniaxialMaterial('LimitState', 40004, 40.86349557, 9.389e-05, 122.5904867, 0.00028168, 408.63495567, 0.00093893, -40.86349557, -9.389e-05, -122.5904867, -0.00028168, -408.63495567, -0.00093893, 0.4, 0.3, 0.003, 0.0, 0.0, 20004, 2)
    ops.limitCurve('ThreePoint', 10004, 4, 0.0, 163.45398227, 0.01900393, 163.45398227, 0.05701179, 114.41778759, -1788.70555714, 0.05, 2, 0, 70004, 21004, 1, 3)
    ops.uniaxialMaterial('LimitState', 30004, 40.86349557, 9.389e-05, 122.5904867, 0.00028168, 408.63495567, 0.00093893, -40.86349557, -9.389e-05, -122.5904867, -0.00028168, -408.63495567, -0.00093893, 0.4, 0.3, 0.003, 0.0, 0.0, 10004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4, 99999, 'P', 40004, 'Vy', 30004, 'Vz', 20004, 'My', 10004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170004, 70004, 170004, 4, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121004, 121004, 21004, 4, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170005, 0.0, 4.15, 0.0)
    ops.node(121005, 0.0, 4.15, 3.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 5, 170005, 121005, 0.25, 27334274.68746622, 11389281.11977759, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20005, 250.887633, 0.00089841, 304.56208353, 0.02709273, 30.45620835, 0.06211861, -250.887633, -0.00089841, -304.56208353, -0.02709273, -30.45620835, -0.06211861, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10005, 277.01612565, 0.00089841, 336.28045907, 0.02709273, 33.62804591, 0.06211861, -277.01612565, -0.00089841, -336.28045907, -0.02709273, -33.62804591, -0.06211861, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20005, 5, 0.0, 237.06483819, 0.01796829, 237.06483819, 0.05390487, 165.94538674, -2262.48354195, 0.05, 2, 0, 70005, 21005, 2, 3)
    ops.uniaxialMaterial('LimitState', 40005, 59.26620955, 8.867e-05, 177.79862865, 0.00026601, 592.66209549, 0.00088671, -59.26620955, -8.867e-05, -177.79862865, -0.00026601, -592.66209549, -0.00088671, 0.4, 0.3, 0.003, 0.0, 0.0, 20005, 2)
    ops.limitCurve('ThreePoint', 10005, 5, 0.0, 237.06483819, 0.01796829, 237.06483819, 0.05390487, 165.94538674, -2262.48354195, 0.05, 2, 0, 70005, 21005, 1, 3)
    ops.uniaxialMaterial('LimitState', 30005, 59.26620955, 8.867e-05, 177.79862865, 0.00026601, 592.66209549, 0.00088671, -59.26620955, -8.867e-05, -177.79862865, -0.00026601, -592.66209549, -0.00088671, 0.4, 0.3, 0.003, 0.0, 0.0, 10005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 5, 99999, 'P', 40005, 'Vy', 30005, 'Vz', 20005, 'My', 10005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170005, 70005, 170005, 5, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121005, 121005, 21005, 5, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170006, 5.8, 4.15, 0.0)
    ops.node(121006, 5.8, 4.15, 3.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 6, 170006, 121006, 0.25, 27271838.44193284, 11363266.01747202, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20006, 329.74495996, 0.00092841, 399.67328135, 0.0351316, 39.96732813, 0.0763064, -329.74495996, -0.00092841, -399.67328135, -0.0351316, -39.96732813, -0.0763064, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10006, 363.8717162, 0.00092841, 441.03722713, 0.0351316, 44.10372271, 0.0763064, -363.8717162, -0.00092841, -441.03722713, -0.0351316, -44.10372271, -0.0763064, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20006, 6, 0.0, 285.25524566, 0.01856817, 285.25524566, 0.0557045, 199.67867196, -3469.35218114, 0.05, 2, 0, 70006, 21006, 2, 3)
    ops.uniaxialMaterial('LimitState', 40006, 71.31381141, 0.00010694, 213.94143424, 0.00032082, 713.13811414, 0.0010694, -71.31381141, -0.00010694, -213.94143424, -0.00032082, -713.13811414, -0.0010694, 0.4, 0.3, 0.003, 0.0, 0.0, 20006, 2)
    ops.limitCurve('ThreePoint', 10006, 6, 0.0, 285.25524566, 0.01856817, 285.25524566, 0.0557045, 199.67867196, -3469.35218114, 0.05, 2, 0, 70006, 21006, 1, 3)
    ops.uniaxialMaterial('LimitState', 30006, 71.31381141, 0.00010694, 213.94143424, 0.00032082, 713.13811414, 0.0010694, -71.31381141, -0.00010694, -213.94143424, -0.00032082, -713.13811414, -0.0010694, 0.4, 0.3, 0.003, 0.0, 0.0, 10006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 6, 99999, 'P', 40006, 'Vy', 30006, 'Vz', 20006, 'My', 10006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170006, 70006, 170006, 6, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121006, 121006, 21006, 6, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170007, 8.65, 4.15, 0.0)
    ops.node(121007, 8.65, 4.15, 3.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 7, 170007, 121007, 0.25, 26885105.66811134, 11202127.36171306, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20007, 326.16361305, 0.00095957, 395.46518213, 0.03601938, 39.54651821, 0.07651069, -326.16361305, -0.00095957, -395.46518213, -0.03601938, -39.54651821, -0.07651069, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10007, 358.44376799, 0.00095957, 434.60405857, 0.03601938, 43.46040586, 0.07651069, -358.44376799, -0.00095957, -434.60405857, -0.03601938, -43.46040586, -0.07651069, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20007, 7, 0.0, 287.10993374, 0.01919134, 287.10993374, 0.05757403, 200.97695362, -3612.87622059, 0.05, 2, 0, 70007, 21007, 2, 3)
    ops.uniaxialMaterial('LimitState', 40007, 71.77748343, 0.00010918, 215.3324503, 0.00032755, 717.77483435, 0.00109184, -71.77748343, -0.00010918, -215.3324503, -0.00032755, -717.77483435, -0.00109184, 0.4, 0.3, 0.003, 0.0, 0.0, 20007, 2)
    ops.limitCurve('ThreePoint', 10007, 7, 0.0, 287.10993374, 0.01919134, 287.10993374, 0.05757403, 200.97695362, -3612.87622059, 0.05, 2, 0, 70007, 21007, 1, 3)
    ops.uniaxialMaterial('LimitState', 30007, 71.77748343, 0.00010918, 215.3324503, 0.00032755, 717.77483435, 0.00109184, -71.77748343, -0.00010918, -215.3324503, -0.00032755, -717.77483435, -0.00109184, 0.4, 0.3, 0.003, 0.0, 0.0, 10007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 7, 99999, 'P', 40007, 'Vy', 30007, 'Vz', 20007, 'My', 10007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170007, 70007, 170007, 7, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121007, 121007, 21007, 7, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170008, 14.45, 4.15, 0.0)
    ops.node(121008, 14.45, 4.15, 3.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 8, 170008, 121008, 0.25, 26269377.68789311, 10945574.03662213, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20008, 251.3350436, 0.00093168, 305.41679905, 0.02885782, 30.54167991, 0.06246023, -251.3350436, -0.00093168, -305.41679905, -0.02885782, -30.54167991, -0.06246023, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10008, 277.40274599, 0.00093168, 337.09369579, 0.02885782, 33.70936958, 0.06246023, -277.40274599, -0.00093168, -337.09369579, -0.02885782, -33.70936958, -0.06246023, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20008, 8, 0.0, 244.14299995, 0.0186336, 244.14299995, 0.0559008, 170.90009997, -2669.12149317, 0.05, 2, 0, 70008, 21008, 2, 3)
    ops.uniaxialMaterial('LimitState', 40008, 61.03574999, 9.502e-05, 183.10724996, 0.00028506, 610.35749988, 0.0009502, -61.03574999, -9.502e-05, -183.10724996, -0.00028506, -610.35749988, -0.0009502, 0.4, 0.3, 0.003, 0.0, 0.0, 20008, 2)
    ops.limitCurve('ThreePoint', 10008, 8, 0.0, 244.14299995, 0.0186336, 244.14299995, 0.0559008, 170.90009997, -2669.12149317, 0.05, 2, 0, 70008, 21008, 1, 3)
    ops.uniaxialMaterial('LimitState', 30008, 61.03574999, 9.502e-05, 183.10724996, 0.00028506, 610.35749988, 0.0009502, -61.03574999, -9.502e-05, -183.10724996, -0.00028506, -610.35749988, -0.0009502, 0.4, 0.3, 0.003, 0.0, 0.0, 10008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 8, 99999, 'P', 40008, 'Vy', 30008, 'Vz', 20008, 'My', 10008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170008, 70008, 170008, 8, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121008, 121008, 21008, 8, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170009, 0.0, 8.3, 0.0)
    ops.node(121009, 0.0, 8.3, 3.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 9, 170009, 121009, 0.16, 28110010.77032863, 11712504.48763693, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20009, 116.79876833, 0.00097243, 141.75358201, 0.01570828, 14.1753582, 0.05252103, -116.79876833, -0.00097243, -141.75358201, -0.01570828, -14.1753582, -0.05252103, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10009, 123.60882762, 0.00097243, 150.0186546, 0.01570828, 15.00186546, 0.05252103, -123.60882762, -0.00097243, -150.0186546, -0.01570828, -15.00186546, -0.05252103, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20009, 9, 0.0, 153.76018456, 0.01944866, 153.76018456, 0.05834599, 107.63212919, -1461.99856911, 0.05, 2, 0, 70009, 21009, 2, 3)
    ops.uniaxialMaterial('LimitState', 40009, 38.44004614, 8.738e-05, 115.32013842, 0.00026215, 384.4004614, 0.00087382, -38.44004614, -8.738e-05, -115.32013842, -0.00026215, -384.4004614, -0.00087382, 0.4, 0.3, 0.003, 0.0, 0.0, 20009, 2)
    ops.limitCurve('ThreePoint', 10009, 9, 0.0, 153.76018456, 0.01944866, 153.76018456, 0.05834599, 107.63212919, -1461.99856911, 0.05, 2, 0, 70009, 21009, 1, 3)
    ops.uniaxialMaterial('LimitState', 30009, 38.44004614, 8.738e-05, 115.32013842, 0.00026215, 384.4004614, 0.00087382, -38.44004614, -8.738e-05, -115.32013842, -0.00026215, -384.4004614, -0.00087382, 0.4, 0.3, 0.003, 0.0, 0.0, 10009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 9, 99999, 'P', 40009, 'Vy', 30009, 'Vz', 20009, 'My', 10009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170009, 70009, 170009, 9, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121009, 121009, 21009, 9, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170010, 5.8, 8.3, 0.0)
    ops.node(121010, 5.8, 8.3, 3.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 10, 170010, 121010, 0.16, 26746085.64158459, 11144202.35066025, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20010, 157.42649697, 0.00104792, 190.79873184, 0.0163, 19.07987318, 0.04835869, -157.42649697, -0.00104792, -190.79873184, -0.0163, -19.07987318, -0.04835869, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10010, 164.7830055, 0.00104792, 199.7147182, 0.0163, 19.97147182, 0.04835869, -164.7830055, -0.00104792, -199.7147182, -0.0163, -19.97147182, -0.04835869, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20010, 10, 0.0, 158.00905258, 0.02095837, 158.00905258, 0.06287512, 110.60633681, -1573.73224494, 0.05, 2, 0, 70010, 21010, 2, 3)
    ops.uniaxialMaterial('LimitState', 40010, 39.50226315, 9.438e-05, 118.50678944, 0.00028313, 395.02263145, 0.00094376, -39.50226315, -9.438e-05, -118.50678944, -0.00028313, -395.02263145, -0.00094376, 0.4, 0.3, 0.003, 0.0, 0.0, 20010, 2)
    ops.limitCurve('ThreePoint', 10010, 10, 0.0, 158.00905258, 0.02095837, 158.00905258, 0.06287512, 110.60633681, -1573.73224494, 0.05, 2, 0, 70010, 21010, 1, 3)
    ops.uniaxialMaterial('LimitState', 30010, 39.50226315, 9.438e-05, 118.50678944, 0.00028313, 395.02263145, 0.00094376, -39.50226315, -9.438e-05, -118.50678944, -0.00028313, -395.02263145, -0.00094376, 0.4, 0.3, 0.003, 0.0, 0.0, 10010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 10, 99999, 'P', 40010, 'Vy', 30010, 'Vz', 20010, 'My', 10010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170010, 70010, 170010, 10, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121010, 121010, 21010, 10, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170011, 8.65, 8.3, 0.0)
    ops.node(121011, 8.65, 8.3, 3.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 11, 170011, 121011, 0.16, 26590806.84649917, 11079502.85270799, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20011, 162.13149196, 0.00106604, 196.52015381, 0.01699488, 19.65201538, 0.04881479, -162.13149196, -0.00106604, -196.52015381, -0.01699488, -19.65201538, -0.04881479, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10011, 170.03086933, 0.00106604, 206.095017, 0.01699488, 20.6095017, 0.04881479, -170.03086933, -0.00106604, -206.095017, -0.01699488, -20.6095017, -0.04881479, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20011, 11, 0.0, 163.28599832, 0.02132078, 163.28599832, 0.06396234, 114.30019882, -1728.26769047, 0.05, 2, 0, 70011, 21011, 2, 3)
    ops.uniaxialMaterial('LimitState', 40011, 40.82149958, 9.81e-05, 122.46449874, 0.00029429, 408.2149958, 0.00098098, -40.82149958, -9.81e-05, -122.46449874, -0.00029429, -408.2149958, -0.00098098, 0.4, 0.3, 0.003, 0.0, 0.0, 20011, 2)
    ops.limitCurve('ThreePoint', 10011, 11, 0.0, 163.28599832, 0.02132078, 163.28599832, 0.06396234, 114.30019882, -1728.26769047, 0.05, 2, 0, 70011, 21011, 1, 3)
    ops.uniaxialMaterial('LimitState', 30011, 40.82149958, 9.81e-05, 122.46449874, 0.00029429, 408.2149958, 0.00098098, -40.82149958, -9.81e-05, -122.46449874, -0.00029429, -408.2149958, -0.00098098, 0.4, 0.3, 0.003, 0.0, 0.0, 10011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 11, 99999, 'P', 40011, 'Vy', 30011, 'Vz', 20011, 'My', 10011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170011, 70011, 170011, 11, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121011, 121011, 21011, 11, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170012, 14.45, 8.3, 0.0)
    ops.node(121012, 14.45, 8.3, 3.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 12, 170012, 121012, 0.16, 28118265.11555659, 11715943.79814858, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20012, 114.30990684, 0.00092104, 138.73116634, 0.01815285, 13.87311663, 0.05497436, -114.30990684, -0.00092104, -138.73116634, -0.01815285, -13.87311663, -0.05497436, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10012, 121.16780251, 0.00092104, 147.0541883, 0.01815285, 14.70541883, 0.05497436, -121.16780251, -0.00092104, -147.0541883, -0.01815285, -14.70541883, -0.05497436, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20012, 12, 0.0, 165.11719683, 0.01842074, 165.11719683, 0.05526223, 115.58203778, -1795.87063141, 0.05, 2, 0, 70012, 21012, 2, 3)
    ops.uniaxialMaterial('LimitState', 40012, 41.27929921, 9.381e-05, 123.83789762, 0.00028143, 412.79299208, 0.00093809, -41.27929921, -9.381e-05, -123.83789762, -0.00028143, -412.79299208, -0.00093809, 0.4, 0.3, 0.003, 0.0, 0.0, 20012, 2)
    ops.limitCurve('ThreePoint', 10012, 12, 0.0, 165.11719683, 0.01842074, 165.11719683, 0.05526223, 115.58203778, -1795.87063141, 0.05, 2, 0, 70012, 21012, 1, 3)
    ops.uniaxialMaterial('LimitState', 30012, 41.27929921, 9.381e-05, 123.83789762, 0.00028143, 412.79299208, 0.00093809, -41.27929921, -9.381e-05, -123.83789762, -0.00028143, -412.79299208, -0.00093809, 0.4, 0.3, 0.003, 0.0, 0.0, 10012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 12, 99999, 'P', 40012, 'Vy', 30012, 'Vz', 20012, 'My', 10012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170012, 70012, 170012, 12, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121012, 121012, 21012, 12, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171001, 0.0, 0.0, 3.85)
    ops.node(122001, 0.0, 0.0, 5.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1001, 171001, 122001, 0.16, 27724003.17264619, 11551667.98860258, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21001, 118.59234209, 0.00080271, 144.36275773, 0.02967442, 14.43627577, 0.08731351, -118.59234209, -0.00080271, -144.36275773, -0.02967442, -14.43627577, -0.08731351, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11001, 98.12233568, 0.00080271, 119.44456719, 0.02967442, 11.94445672, 0.08731351, -98.12233568, -0.00080271, -119.44456719, -0.02967442, -11.94445672, -0.08731351, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21001, 1001, 0.0, 192.20954109, 0.0160542, 192.20954109, 0.04816261, 134.54667877, -4826.71983147, 0.05, 2, 0, 71001, 22001, 2, 3)
    ops.uniaxialMaterial('LimitState', 41001, 48.05238527, 7.956e-05, 144.15715582, 0.00023867, 480.52385273, 0.00079556, -48.05238527, -7.956e-05, -144.15715582, -0.00023867, -480.52385273, -0.00079556, 0.4, 0.3, 0.003, 0.0, 0.0, 21001, 2)
    ops.limitCurve('ThreePoint', 11001, 1001, 0.0, 192.20954109, 0.0160542, 192.20954109, 0.04816261, 134.54667877, -4826.71983147, 0.05, 2, 0, 71001, 22001, 1, 3)
    ops.uniaxialMaterial('LimitState', 31001, 48.05238527, 7.956e-05, 144.15715582, 0.00023867, 480.52385273, 0.00079556, -48.05238527, -7.956e-05, -144.15715582, -0.00023867, -480.52385273, -0.00079556, 0.4, 0.3, 0.003, 0.0, 0.0, 11001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1001, 99999, 'P', 41001, 'Vy', 31001, 'Vz', 21001, 'My', 11001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171001, 71001, 171001, 1001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122001, 122001, 22001, 1001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171004, 14.45, 0.0, 3.85)
    ops.node(122004, 14.45, 0.0, 5.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1004, 171004, 122004, 0.16, 25831942.59450376, 10763309.41437657, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21004, 117.42505671, 0.00087095, 143.3216158, 0.02976443, 14.33216158, 0.08467634, -117.42505671, -0.00087095, -143.3216158, -0.02976443, -14.33216158, -0.08467634, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11004, 98.27238333, 0.00087095, 119.94507103, 0.02976443, 11.9945071, 0.08467634, -98.27238333, -0.00087095, -119.94507103, -0.02976443, -11.9945071, -0.08467634, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21004, 1004, 0.0, 180.55288253, 0.0174189, 180.55288253, 0.05225671, 126.38701777, -4604.26272831, 0.05, 2, 0, 71004, 22004, 2, 3)
    ops.uniaxialMaterial('LimitState', 41004, 45.13822063, 8.02e-05, 135.4146619, 0.00024061, 451.38220633, 0.00080205, -45.13822063, -8.02e-05, -135.4146619, -0.00024061, -451.38220633, -0.00080205, 0.4, 0.3, 0.003, 0.0, 0.0, 21004, 2)
    ops.limitCurve('ThreePoint', 11004, 1004, 0.0, 180.55288253, 0.0174189, 180.55288253, 0.05225671, 126.38701777, -4604.26272831, 0.05, 2, 0, 71004, 22004, 1, 3)
    ops.uniaxialMaterial('LimitState', 31004, 45.13822063, 8.02e-05, 135.4146619, 0.00024061, 451.38220633, 0.00080205, -45.13822063, -8.02e-05, -135.4146619, -0.00024061, -451.38220633, -0.00080205, 0.4, 0.3, 0.003, 0.0, 0.0, 11004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1004, 99999, 'P', 41004, 'Vy', 31004, 'Vz', 21004, 'My', 11004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171004, 71004, 171004, 1004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122004, 122004, 22004, 1004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171005, 0.0, 4.15, 3.9)
    ops.node(122005, 0.0, 4.15, 5.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1005, 171005, 122005, 0.25, 27659086.01206975, 11524619.17169573, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21005, 253.90380587, 0.0007719, 308.91404262, 0.04880852, 30.89140426, 0.11439494, -253.90380587, -0.0007719, -308.91404262, -0.04880852, -30.89140426, -0.11439494, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11005, 227.91287023, 0.0007719, 277.29196837, 0.04880852, 27.72919684, 0.11439494, -227.91287023, -0.0007719, -277.29196837, -0.04880852, -27.72919684, -0.11439494, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21005, 1005, 0.0, 393.13324047, 0.01543791, 393.13324047, 0.04631374, 275.19326833, -11268.15613475, 0.05, 2, 0, 71005, 22005, 2, 3)
    ops.uniaxialMaterial('LimitState', 41005, 98.28331012, 0.00010438, 294.84993036, 0.00031315, 982.83310118, 0.00104384, -98.28331012, -0.00010438, -294.84993036, -0.00031315, -982.83310118, -0.00104384, 0.4, 0.3, 0.003, 0.0, 0.0, 21005, 2)
    ops.limitCurve('ThreePoint', 11005, 1005, 0.0, 393.13324047, 0.01543791, 393.13324047, 0.04631374, 275.19326833, -11268.15613475, 0.05, 2, 0, 71005, 22005, 1, 3)
    ops.uniaxialMaterial('LimitState', 31005, 98.28331012, 0.00010438, 294.84993036, 0.00031315, 982.83310118, 0.00104384, -98.28331012, -0.00010438, -294.84993036, -0.00031315, -982.83310118, -0.00104384, 0.4, 0.3, 0.003, 0.0, 0.0, 11005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1005, 99999, 'P', 41005, 'Vy', 31005, 'Vz', 21005, 'My', 11005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171005, 71005, 171005, 1005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122005, 122005, 22005, 1005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171006, 5.8, 4.15, 3.9)
    ops.node(122006, 5.8, 4.15, 5.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1006, 171006, 122006, 0.25, 26153874.46889042, 10897447.69537101, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21006, 250.09064281, 0.00083955, 304.44899684, 0.03357545, 30.44489968, 0.07707039, -250.09064281, -0.00083955, -304.44899684, -0.03357545, -30.44489968, -0.07707039, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11006, 232.8084557, 0.00083955, 283.4104467, 0.03357545, 28.34104467, 0.07707039, -232.8084557, -0.00083955, -283.4104467, -0.03357545, -28.34104467, -0.07707039, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21006, 1006, 0.0, 285.12311234, 0.01679097, 285.12311234, 0.05037292, 199.58617864, -4326.38229242, 0.05, 2, 0, 71006, 22006, 2, 3)
    ops.uniaxialMaterial('LimitState', 41006, 71.28077808, 8.006e-05, 213.84233425, 0.00024019, 712.80778085, 0.00080062, -71.28077808, -8.006e-05, -213.84233425, -0.00024019, -712.80778085, -0.00080062, 0.4, 0.3, 0.003, 0.0, 0.0, 21006, 2)
    ops.limitCurve('ThreePoint', 11006, 1006, 0.0, 285.12311234, 0.01679097, 285.12311234, 0.05037292, 199.58617864, -4326.38229242, 0.05, 2, 0, 71006, 22006, 1, 3)
    ops.uniaxialMaterial('LimitState', 31006, 71.28077808, 8.006e-05, 213.84233425, 0.00024019, 712.80778085, 0.00080062, -71.28077808, -8.006e-05, -213.84233425, -0.00024019, -712.80778085, -0.00080062, 0.4, 0.3, 0.003, 0.0, 0.0, 11006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1006, 99999, 'P', 41006, 'Vy', 31006, 'Vz', 21006, 'My', 11006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171006, 71006, 171006, 1006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122006, 122006, 22006, 1006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171007, 8.65, 4.15, 3.9)
    ops.node(122007, 8.65, 4.15, 5.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1007, 171007, 122007, 0.25, 28943108.3151231, 12059628.46463462, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21007, 240.69115381, 0.00077291, 291.84527423, 0.03616061, 29.18452742, 0.08340523, -240.69115381, -0.00077291, -291.84527423, -0.03616061, -29.18452742, -0.08340523, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11007, 224.89159834, 0.00077291, 272.68783729, 0.03616061, 27.26878373, 0.08340523, -224.89159834, -0.00077291, -272.68783729, -0.03616061, -27.26878373, -0.08340523, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21007, 1007, 0.0, 337.1509723, 0.0154581, 337.1509723, 0.04637431, 236.00568061, -5685.56018227, 0.05, 2, 0, 71007, 22007, 2, 3)
    ops.uniaxialMaterial('LimitState', 41007, 84.28774308, 8.555e-05, 252.86322923, 0.00025665, 842.87743076, 0.00085548, -84.28774308, -8.555e-05, -252.86322923, -0.00025665, -842.87743076, -0.00085548, 0.4, 0.3, 0.003, 0.0, 0.0, 21007, 2)
    ops.limitCurve('ThreePoint', 11007, 1007, 0.0, 337.1509723, 0.0154581, 337.1509723, 0.04637431, 236.00568061, -5685.56018227, 0.05, 2, 0, 71007, 22007, 1, 3)
    ops.uniaxialMaterial('LimitState', 31007, 84.28774308, 8.555e-05, 252.86322923, 0.00025665, 842.87743076, 0.00085548, -84.28774308, -8.555e-05, -252.86322923, -0.00025665, -842.87743076, -0.00085548, 0.4, 0.3, 0.003, 0.0, 0.0, 11007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1007, 99999, 'P', 41007, 'Vy', 31007, 'Vz', 21007, 'My', 11007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171007, 71007, 171007, 1007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122007, 122007, 22007, 1007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171008, 14.45, 4.15, 3.9)
    ops.node(122008, 14.45, 4.15, 5.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1008, 171008, 122008, 0.25, 29403977.48437407, 12251657.28515586, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21008, 259.30180674, 0.00078757, 314.43605349, 0.04754274, 31.44360535, 0.11563117, -259.30180674, -0.00078757, -314.43605349, -0.04754274, -31.44360535, -0.11563117, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11008, 233.55324074, 0.00078757, 283.21267878, 0.04754274, 28.32126788, 0.11563117, -233.55324074, -0.00078757, -283.21267878, -0.04754274, -28.32126788, -0.11563117, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21008, 1008, 0.0, 394.27162745, 0.01575133, 394.27162745, 0.047254, 275.99013922, -10081.27379287, 0.05, 2, 0, 71008, 22008, 2, 3)
    ops.uniaxialMaterial('LimitState', 41008, 98.56790686, 9.847e-05, 295.70372059, 0.00029542, 985.67906863, 0.00098474, -98.56790686, -9.847e-05, -295.70372059, -0.00029542, -985.67906863, -0.00098474, 0.4, 0.3, 0.003, 0.0, 0.0, 21008, 2)
    ops.limitCurve('ThreePoint', 11008, 1008, 0.0, 394.27162745, 0.01575133, 394.27162745, 0.047254, 275.99013922, -10081.27379287, 0.05, 2, 0, 71008, 22008, 1, 3)
    ops.uniaxialMaterial('LimitState', 31008, 98.56790686, 9.847e-05, 295.70372059, 0.00029542, 985.67906863, 0.00098474, -98.56790686, -9.847e-05, -295.70372059, -0.00029542, -985.67906863, -0.00098474, 0.4, 0.3, 0.003, 0.0, 0.0, 11008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1008, 99999, 'P', 41008, 'Vy', 31008, 'Vz', 21008, 'My', 11008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171008, 71008, 171008, 1008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122008, 122008, 22008, 1008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171009, 0.0, 8.3, 3.85)
    ops.node(122009, 0.0, 8.3, 5.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1009, 171009, 122009, 0.16, 27578734.12184899, 11491139.21743708, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21009, 137.05978547, 0.00084194, 166.88423534, 0.03336445, 16.68842353, 0.09081808, -137.05978547, -0.00084194, -166.88423534, -0.03336445, -16.68842353, -0.09081808, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11009, 109.66656717, 0.00084194, 133.53020466, 0.03336445, 13.35302047, 0.09081808, -109.66656717, -0.00084194, -133.53020466, -0.03336445, -13.35302047, -0.09081808, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21009, 1009, 0.0, 205.87893843, 0.01683885, 205.87893843, 0.05051656, 144.1152569, -5896.09583374, 0.05, 2, 0, 71009, 22009, 2, 3)
    ops.uniaxialMaterial('LimitState', 41009, 51.46973461, 8.566e-05, 154.40920382, 0.00025699, 514.69734607, 0.00085662, -51.46973461, -8.566e-05, -154.40920382, -0.00025699, -514.69734607, -0.00085662, 0.4, 0.3, 0.003, 0.0, 0.0, 21009, 2)
    ops.limitCurve('ThreePoint', 11009, 1009, 0.0, 205.87893843, 0.01683885, 205.87893843, 0.05051656, 144.1152569, -5896.09583374, 0.05, 2, 0, 71009, 22009, 1, 3)
    ops.uniaxialMaterial('LimitState', 31009, 51.46973461, 8.566e-05, 154.40920382, 0.00025699, 514.69734607, 0.00085662, -51.46973461, -8.566e-05, -154.40920382, -0.00025699, -514.69734607, -0.00085662, 0.4, 0.3, 0.003, 0.0, 0.0, 11009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1009, 99999, 'P', 41009, 'Vy', 31009, 'Vz', 21009, 'My', 11009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171009, 71009, 171009, 1009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122009, 122009, 22009, 1009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171010, 5.8, 8.3, 3.85)
    ops.node(122010, 5.8, 8.3, 5.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1010, 171010, 122010, 0.16, 29347858.64705681, 12228274.43627367, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21010, 130.83220713, 0.00083251, 158.48578341, 0.02149824, 15.84857834, 0.06669031, -130.83220713, -0.00083251, -158.48578341, -0.02149824, -15.84857834, -0.06669031, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11010, 110.07906232, 0.00083251, 133.34611416, 0.02149824, 13.33461142, 0.06669031, -110.07906232, -0.00083251, -133.34611416, -0.02149824, -13.33461142, -0.06669031, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21010, 1010, 0.0, 179.53728004, 0.01665025, 179.53728004, 0.04995075, 125.67609603, -2939.38111836, 0.05, 2, 0, 71010, 22010, 2, 3)
    ops.uniaxialMaterial('LimitState', 41010, 44.88432001, 7.02e-05, 134.65296003, 0.0002106, 448.8432001, 0.00070199, -44.88432001, -7.02e-05, -134.65296003, -0.0002106, -448.8432001, -0.00070199, 0.4, 0.3, 0.003, 0.0, 0.0, 21010, 2)
    ops.limitCurve('ThreePoint', 11010, 1010, 0.0, 179.53728004, 0.01665025, 179.53728004, 0.04995075, 125.67609603, -2939.38111836, 0.05, 2, 0, 71010, 22010, 1, 3)
    ops.uniaxialMaterial('LimitState', 31010, 44.88432001, 7.02e-05, 134.65296003, 0.0002106, 448.8432001, 0.00070199, -44.88432001, -7.02e-05, -134.65296003, -0.0002106, -448.8432001, -0.00070199, 0.4, 0.3, 0.003, 0.0, 0.0, 11010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1010, 99999, 'P', 41010, 'Vy', 31010, 'Vz', 21010, 'My', 11010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171010, 71010, 171010, 1010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122010, 122010, 22010, 1010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171011, 8.65, 8.3, 3.85)
    ops.node(122011, 8.65, 8.3, 5.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1011, 171011, 122011, 0.16, 25367381.45314012, 10569742.27214172, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21011, 124.08771639, 0.00082965, 151.10887105, 0.02045309, 15.1108871, 0.06030129, -124.08771639, -0.00082965, -151.10887105, -0.02045309, -15.1108871, -0.06030129, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11011, 104.06874967, 0.00082965, 126.73060422, 0.02045309, 12.67306042, 0.06030129, -104.06874967, -0.00082965, -126.73060422, -0.02045309, -12.67306042, -0.06030129, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21011, 1011, 0.0, 156.20441759, 0.01659302, 156.20441759, 0.04977907, 109.34309232, -2702.82818748, 0.05, 2, 0, 71011, 22011, 2, 3)
    ops.uniaxialMaterial('LimitState', 41011, 39.0511044, 7.066e-05, 117.1533132, 0.00021198, 390.51104399, 0.00070659, -39.0511044, -7.066e-05, -117.1533132, -0.00021198, -390.51104399, -0.00070659, 0.4, 0.3, 0.003, 0.0, 0.0, 21011, 2)
    ops.limitCurve('ThreePoint', 11011, 1011, 0.0, 156.20441759, 0.01659302, 156.20441759, 0.04977907, 109.34309232, -2702.82818748, 0.05, 2, 0, 71011, 22011, 1, 3)
    ops.uniaxialMaterial('LimitState', 31011, 39.0511044, 7.066e-05, 117.1533132, 0.00021198, 390.51104399, 0.00070659, -39.0511044, -7.066e-05, -117.1533132, -0.00021198, -390.51104399, -0.00070659, 0.4, 0.3, 0.003, 0.0, 0.0, 11011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1011, 99999, 'P', 41011, 'Vy', 31011, 'Vz', 21011, 'My', 11011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171011, 71011, 171011, 1011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122011, 122011, 22011, 1011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171012, 14.45, 8.3, 3.85)
    ops.node(122012, 14.45, 8.3, 5.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1012, 171012, 122012, 0.16, 27624437.34542678, 11510182.22726116, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21012, 135.47070192, 0.00081208, 164.93673103, 0.02888884, 16.4936731, 0.08640121, -135.47070192, -0.00081208, -164.93673103, -0.02888884, -16.4936731, -0.08640121, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11012, 107.84389545, 0.00081208, 131.30085934, 0.02888884, 13.13008593, 0.08640121, -107.84389545, -0.00081208, -131.30085934, -0.02888884, -13.13008593, -0.08640121, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21012, 1012, 0.0, 180.17783008, 0.01624161, 180.17783008, 0.04872484, 126.12448106, -4041.08750131, 0.05, 2, 0, 71012, 22012, 2, 3)
    ops.uniaxialMaterial('LimitState', 41012, 45.04445752, 7.484e-05, 135.13337256, 0.00022453, 450.4445752, 0.00074845, -45.04445752, -7.484e-05, -135.13337256, -0.00022453, -450.4445752, -0.00074845, 0.4, 0.3, 0.003, 0.0, 0.0, 21012, 2)
    ops.limitCurve('ThreePoint', 11012, 1012, 0.0, 180.17783008, 0.01624161, 180.17783008, 0.04872484, 126.12448106, -4041.08750131, 0.05, 2, 0, 71012, 22012, 1, 3)
    ops.uniaxialMaterial('LimitState', 31012, 45.04445752, 7.484e-05, 135.13337256, 0.00022453, 450.4445752, 0.00074845, -45.04445752, -7.484e-05, -135.13337256, -0.00022453, -450.4445752, -0.00074845, 0.4, 0.3, 0.003, 0.0, 0.0, 11012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1012, 99999, 'P', 41012, 'Vy', 31012, 'Vz', 21012, 'My', 11012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171012, 71012, 171012, 1012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122012, 122012, 22012, 1012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172001, 0.0, 0.0, 6.4)
    ops.node(123001, 0.0, 0.0, 8.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2001, 172001, 123001, 0.1225, 25208998.17220958, 10503749.23842066, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22001, 77.87456543, 0.00094643, 95.26674118, 0.02432732, 9.52667412, 0.07444059, -77.87456543, -0.00094643, -95.26674118, -0.02432732, -9.52667412, -0.07444059, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12001, 66.54619455, 0.00094643, 81.40833991, 0.02432732, 8.14083399, 0.07444059, -66.54619455, -0.00094643, -81.40833991, -0.02432732, -8.14083399, -0.07444059, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22001, 2001, 0.0, 129.32567018, 0.0189285, 129.32567018, 0.05678551, 90.52796913, -3609.47704195, 0.05, 2, 0, 72001, 23001, 2, 3)
    ops.uniaxialMaterial('LimitState', 42001, 32.33141754, 7.689e-05, 96.99425263, 0.00023067, 323.31417545, 0.00076889, -32.33141754, -7.689e-05, -96.99425263, -0.00023067, -323.31417545, -0.00076889, 0.4, 0.3, 0.003, 0.0, 0.0, 22001, 2)
    ops.limitCurve('ThreePoint', 12001, 2001, 0.0, 129.32567018, 0.0189285, 129.32567018, 0.05678551, 90.52796913, -3609.47704195, 0.05, 2, 0, 72001, 23001, 1, 3)
    ops.uniaxialMaterial('LimitState', 32001, 32.33141754, 7.689e-05, 96.99425263, 0.00023067, 323.31417545, 0.00076889, -32.33141754, -7.689e-05, -96.99425263, -0.00023067, -323.31417545, -0.00076889, 0.4, 0.3, 0.003, 0.0, 0.0, 12001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2001, 99999, 'P', 42001, 'Vy', 32001, 'Vz', 22001, 'My', 12001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172001, 72001, 172001, 2001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123001, 123001, 23001, 2001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172004, 14.45, 0.0, 6.4)
    ops.node(123004, 14.45, 0.0, 8.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2004, 172004, 123004, 0.1225, 27304250.14761152, 11376770.89483813, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22004, 74.1514966, 0.00088976, 90.44419853, 0.02662959, 9.04441985, 0.07914214, -74.1514966, -0.00088976, -90.44419853, -0.02662959, -9.04441985, -0.07914214, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12004, 64.01431537, 0.00088976, 78.07965737, 0.02662959, 7.80796574, 0.07914214, -64.01431537, -0.00088976, -78.07965737, -0.02662959, -7.80796574, -0.07914214, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22004, 2004, 0.0, 144.32893205, 0.01779517, 144.32893205, 0.0533855, 101.03025244, -4261.49431716, 0.05, 2, 0, 72004, 23004, 2, 3)
    ops.uniaxialMaterial('LimitState', 42004, 36.08223301, 7.922e-05, 108.24669904, 0.00023767, 360.82233013, 0.00079225, -36.08223301, -7.922e-05, -108.24669904, -0.00023767, -360.82233013, -0.00079225, 0.4, 0.3, 0.003, 0.0, 0.0, 22004, 2)
    ops.limitCurve('ThreePoint', 12004, 2004, 0.0, 144.32893205, 0.01779517, 144.32893205, 0.0533855, 101.03025244, -4261.49431716, 0.05, 2, 0, 72004, 23004, 1, 3)
    ops.uniaxialMaterial('LimitState', 32004, 36.08223301, 7.922e-05, 108.24669904, 0.00023767, 360.82233013, 0.00079225, -36.08223301, -7.922e-05, -108.24669904, -0.00023767, -360.82233013, -0.00079225, 0.4, 0.3, 0.003, 0.0, 0.0, 12004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2004, 99999, 'P', 42004, 'Vy', 32004, 'Vz', 22004, 'My', 12004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172004, 72004, 172004, 2004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123004, 123004, 23004, 2004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172005, 0.0, 4.15, 6.45)
    ops.node(123005, 0.0, 4.15, 8.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2005, 172005, 123005, 0.16, 25529056.92288116, 10637107.05120048, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22005, 122.54800985, 0.00094762, 149.53800107, 0.03989648, 14.95380011, 0.093412, -122.54800985, -0.00094762, -149.53800107, -0.03989648, -14.95380011, -0.093412, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12005, 122.54800985, 0.00094762, 149.53800107, 0.03989648, 14.95380011, 0.093412, -122.54800985, -0.00094762, -149.53800107, -0.03989648, -14.95380011, -0.093412, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22005, 2005, 0.0, 186.0940406, 0.01895248, 186.0940406, 0.05685744, 130.26582842, -4861.24811286, 0.05, 2, 0, 72005, 23005, 2, 3)
    ops.uniaxialMaterial('LimitState', 42005, 46.52351015, 8.365e-05, 139.57053045, 0.00025094, 465.2351015, 0.00083647, -46.52351015, -8.365e-05, -139.57053045, -0.00025094, -465.2351015, -0.00083647, 0.4, 0.3, 0.003, 0.0, 0.0, 22005, 2)
    ops.limitCurve('ThreePoint', 12005, 2005, 0.0, 186.0940406, 0.01895248, 186.0940406, 0.05685744, 130.26582842, -4861.24811286, 0.05, 2, 0, 72005, 23005, 1, 3)
    ops.uniaxialMaterial('LimitState', 32005, 46.52351015, 8.365e-05, 139.57053045, 0.00025094, 465.2351015, 0.00083647, -46.52351015, -8.365e-05, -139.57053045, -0.00025094, -465.2351015, -0.00083647, 0.4, 0.3, 0.003, 0.0, 0.0, 12005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2005, 99999, 'P', 42005, 'Vy', 32005, 'Vz', 22005, 'My', 12005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172005, 72005, 172005, 2005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123005, 123005, 23005, 2005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172006, 5.8, 4.15, 6.45)
    ops.node(123006, 5.8, 4.15, 8.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2006, 172006, 123006, 0.16, 25777876.2481099, 10740781.77004579, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22006, 134.42182285, 0.00097409, 163.69013539, 0.02583361, 16.36901354, 0.06051737, -134.42182285, -0.00097409, -163.69013539, -0.02583361, -16.36901354, -0.06051737, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12006, 134.42182285, 0.00097409, 163.69013539, 0.02583361, 16.36901354, 0.06051737, -134.42182285, -0.00097409, -163.69013539, -0.02583361, -16.36901354, -0.06051737, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22006, 2006, 0.0, 151.43361521, 0.01948187, 151.43361521, 0.05844562, 106.00353065, -2437.08538661, 0.05, 2, 0, 72006, 23006, 2, 3)
    ops.uniaxialMaterial('LimitState', 42006, 37.8584038, 6.741e-05, 113.57521141, 0.00020223, 378.58403803, 0.00067411, -37.8584038, -6.741e-05, -113.57521141, -0.00020223, -378.58403803, -0.00067411, 0.4, 0.3, 0.003, 0.0, 0.0, 22006, 2)
    ops.limitCurve('ThreePoint', 12006, 2006, 0.0, 151.43361521, 0.01948187, 151.43361521, 0.05844562, 106.00353065, -2437.08538661, 0.05, 2, 0, 72006, 23006, 1, 3)
    ops.uniaxialMaterial('LimitState', 32006, 37.8584038, 6.741e-05, 113.57521141, 0.00020223, 378.58403803, 0.00067411, -37.8584038, -6.741e-05, -113.57521141, -0.00020223, -378.58403803, -0.00067411, 0.4, 0.3, 0.003, 0.0, 0.0, 12006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2006, 99999, 'P', 42006, 'Vy', 32006, 'Vz', 22006, 'My', 12006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172006, 72006, 172006, 2006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123006, 123006, 23006, 2006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172007, 8.65, 4.15, 6.45)
    ops.node(123007, 8.65, 4.15, 8.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2007, 172007, 123007, 0.16, 28011290.64789016, 11671371.10328757, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22007, 134.734286, 0.00095815, 163.63686883, 0.02575476, 16.36368688, 0.06307421, -134.734286, -0.00095815, -163.63686883, -0.02575476, -16.36368688, -0.06307421, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12007, 134.734286, 0.00095815, 163.63686883, 0.02575476, 16.36368688, 0.06307421, -134.734286, -0.00095815, -163.63686883, -0.02575476, -16.36368688, -0.06307421, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22007, 2007, 0.0, 161.4343043, 0.01916305, 161.4343043, 0.05748915, 113.00401301, -2430.51078595, 0.05, 2, 0, 72007, 23007, 2, 3)
    ops.uniaxialMaterial('LimitState', 42007, 40.35857608, 6.613e-05, 121.07572823, 0.0001984, 403.58576075, 0.00066133, -40.35857608, -6.613e-05, -121.07572823, -0.0001984, -403.58576075, -0.00066133, 0.4, 0.3, 0.003, 0.0, 0.0, 22007, 2)
    ops.limitCurve('ThreePoint', 12007, 2007, 0.0, 161.4343043, 0.01916305, 161.4343043, 0.05748915, 113.00401301, -2430.51078595, 0.05, 2, 0, 72007, 23007, 1, 3)
    ops.uniaxialMaterial('LimitState', 32007, 40.35857608, 6.613e-05, 121.07572823, 0.0001984, 403.58576075, 0.00066133, -40.35857608, -6.613e-05, -121.07572823, -0.0001984, -403.58576075, -0.00066133, 0.4, 0.3, 0.003, 0.0, 0.0, 12007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2007, 99999, 'P', 42007, 'Vy', 32007, 'Vz', 22007, 'My', 12007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172007, 72007, 172007, 2007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123007, 123007, 23007, 2007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172008, 14.45, 4.15, 6.45)
    ops.node(123008, 14.45, 4.15, 8.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2008, 172008, 123008, 0.16, 26384825.93716229, 10993677.47381762, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22008, 128.20132675, 0.00089784, 156.29522424, 0.04080755, 15.62952242, 0.09577191, -128.20132675, -0.00089784, -156.29522424, -0.04080755, -15.62952242, -0.09577191, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12008, 128.20132675, 0.00089784, 156.29522424, 0.04080755, 15.62952242, 0.09577191, -128.20132675, -0.00089784, -156.29522424, -0.04080755, -15.62952242, -0.09577191, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22008, 2008, 0.0, 197.17141966, 0.01795682, 197.17141966, 0.05387045, 138.01999376, -5376.7376692, 0.05, 2, 0, 72008, 23008, 2, 3)
    ops.uniaxialMaterial('LimitState', 42008, 49.29285491, 8.575e-05, 147.87856474, 0.00025725, 492.92854915, 0.00085752, -49.29285491, -8.575e-05, -147.87856474, -0.00025725, -492.92854915, -0.00085752, 0.4, 0.3, 0.003, 0.0, 0.0, 22008, 2)
    ops.limitCurve('ThreePoint', 12008, 2008, 0.0, 197.17141966, 0.01795682, 197.17141966, 0.05387045, 138.01999376, -5376.7376692, 0.05, 2, 0, 72008, 23008, 1, 3)
    ops.uniaxialMaterial('LimitState', 32008, 49.29285491, 8.575e-05, 147.87856474, 0.00025725, 492.92854915, 0.00085752, -49.29285491, -8.575e-05, -147.87856474, -0.00025725, -492.92854915, -0.00085752, 0.4, 0.3, 0.003, 0.0, 0.0, 12008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2008, 99999, 'P', 42008, 'Vy', 32008, 'Vz', 22008, 'My', 12008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172008, 72008, 172008, 2008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123008, 123008, 23008, 2008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172009, 0.0, 8.3, 6.4)
    ops.node(123009, 0.0, 8.3, 8.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2009, 172009, 123009, 0.1225, 25619034.26883273, 10674597.61201364, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22009, 76.11652458, 0.00087927, 93.0724183, 0.02230388, 9.30724183, 0.07294508, -76.11652458, -0.00087927, -93.0724183, -0.02230388, -9.30724183, -0.07294508, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12009, 64.67474901, 0.00087927, 79.08184623, 0.02230388, 7.90818462, 0.07294508, -64.67474901, -0.00087927, -79.08184623, -0.02230388, -7.90818462, -0.07294508, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22009, 2009, 0.0, 121.62042192, 0.01758535, 121.62042192, 0.05275605, 85.13429535, -2934.9145556, 0.05, 2, 0, 72009, 23009, 2, 3)
    ops.uniaxialMaterial('LimitState', 42009, 30.40510548, 7.115e-05, 91.21531644, 0.00021345, 304.05105481, 0.00071151, -30.40510548, -7.115e-05, -91.21531644, -0.00021345, -304.05105481, -0.00071151, 0.4, 0.3, 0.003, 0.0, 0.0, 22009, 2)
    ops.limitCurve('ThreePoint', 12009, 2009, 0.0, 121.62042192, 0.01758535, 121.62042192, 0.05275605, 85.13429535, -2934.9145556, 0.05, 2, 0, 72009, 23009, 1, 3)
    ops.uniaxialMaterial('LimitState', 32009, 30.40510548, 7.115e-05, 91.21531644, 0.00021345, 304.05105481, 0.00071151, -30.40510548, -7.115e-05, -91.21531644, -0.00021345, -304.05105481, -0.00071151, 0.4, 0.3, 0.003, 0.0, 0.0, 12009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2009, 99999, 'P', 42009, 'Vy', 32009, 'Vz', 22009, 'My', 12009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172009, 72009, 172009, 2009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123009, 123009, 23009, 2009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172010, 5.8, 8.3, 6.4)
    ops.node(123010, 5.8, 8.3, 8.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2010, 172010, 123010, 0.1225, 26354583.35465271, 10981076.39777196, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22010, 78.8726268, 0.00090456, 96.15718285, 0.01871, 9.61571828, 0.05971177, -78.8726268, -0.00090456, -96.15718285, -0.01871, -9.61571828, -0.05971177, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12010, 68.49967847, 0.00090456, 83.51105289, 0.01871, 8.35110529, 0.05971177, -68.49967847, -0.00090456, -83.51105289, -0.01871, -8.35110529, -0.05971177, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22010, 2010, 0.0, 121.352555, 0.0180911, 121.352555, 0.05427331, 84.9467885, -2266.72462807, 0.05, 2, 0, 72010, 23010, 2, 3)
    ops.uniaxialMaterial('LimitState', 42010, 30.33813875, 6.901e-05, 91.01441625, 0.00020704, 303.3813875, 0.00069013, -30.33813875, -6.901e-05, -91.01441625, -0.00020704, -303.3813875, -0.00069013, 0.4, 0.3, 0.003, 0.0, 0.0, 22010, 2)
    ops.limitCurve('ThreePoint', 12010, 2010, 0.0, 121.352555, 0.0180911, 121.352555, 0.05427331, 84.9467885, -2266.72462807, 0.05, 2, 0, 72010, 23010, 1, 3)
    ops.uniaxialMaterial('LimitState', 32010, 30.33813875, 6.901e-05, 91.01441625, 0.00020704, 303.3813875, 0.00069013, -30.33813875, -6.901e-05, -91.01441625, -0.00020704, -303.3813875, -0.00069013, 0.4, 0.3, 0.003, 0.0, 0.0, 12010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2010, 99999, 'P', 42010, 'Vy', 32010, 'Vz', 22010, 'My', 12010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172010, 72010, 172010, 2010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123010, 123010, 23010, 2010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172011, 8.65, 8.3, 6.4)
    ops.node(123011, 8.65, 8.3, 8.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2011, 172011, 123011, 0.1225, 26971058.91961571, 11237941.21650655, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22011, 82.51176118, 0.00090818, 100.51308189, 0.02044472, 10.05130819, 0.06215746, -82.51176118, -0.00090818, -100.51308189, -0.02044472, -10.05130819, -0.06215746, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12011, 71.0845099, 0.00090818, 86.59278462, 0.02044472, 8.65927846, 0.06215746, -71.0845099, -0.00090818, -86.59278462, -0.02044472, -8.65927846, -0.06215746, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22011, 2011, 0.0, 128.98260556, 0.01816358, 128.98260556, 0.05449075, 90.28782389, -2572.33133474, 0.05, 2, 0, 72011, 23011, 2, 3)
    ops.uniaxialMaterial('LimitState', 42011, 32.24565139, 7.168e-05, 96.73695417, 0.00021503, 322.4565139, 0.00071675, -32.24565139, -7.168e-05, -96.73695417, -0.00021503, -322.4565139, -0.00071675, 0.4, 0.3, 0.003, 0.0, 0.0, 22011, 2)
    ops.limitCurve('ThreePoint', 12011, 2011, 0.0, 128.98260556, 0.01816358, 128.98260556, 0.05449075, 90.28782389, -2572.33133474, 0.05, 2, 0, 72011, 23011, 1, 3)
    ops.uniaxialMaterial('LimitState', 32011, 32.24565139, 7.168e-05, 96.73695417, 0.00021503, 322.4565139, 0.00071675, -32.24565139, -7.168e-05, -96.73695417, -0.00021503, -322.4565139, -0.00071675, 0.4, 0.3, 0.003, 0.0, 0.0, 12011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2011, 99999, 'P', 42011, 'Vy', 32011, 'Vz', 22011, 'My', 12011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172011, 72011, 172011, 2011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123011, 123011, 23011, 2011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172012, 14.45, 8.3, 6.4)
    ops.node(123012, 14.45, 8.3, 8.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2012, 172012, 123012, 0.1225, 27469101.87824628, 11445459.11593595, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22012, 78.69271608, 0.00090182, 95.95534566, 0.02400224, 9.59553457, 0.07667502, -78.69271608, -0.00090182, -95.95534566, -0.02400224, -9.59553457, -0.07667502, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12012, 67.1629787, 0.00090182, 81.89635786, 0.02400224, 8.18963579, 0.07667502, -67.1629787, -0.00090182, -81.89635786, -0.02400224, -8.18963579, -0.07667502, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22012, 2012, 0.0, 130.0845382, 0.01803637, 130.0845382, 0.05410912, 91.05917674, -3093.60837501, 0.05, 2, 0, 72012, 23012, 2, 3)
    ops.uniaxialMaterial('LimitState', 42012, 32.52113455, 7.098e-05, 97.56340365, 0.00021293, 325.2113455, 0.00070977, -32.52113455, -7.098e-05, -97.56340365, -0.00021293, -325.2113455, -0.00070977, 0.4, 0.3, 0.003, 0.0, 0.0, 22012, 2)
    ops.limitCurve('ThreePoint', 12012, 2012, 0.0, 130.0845382, 0.01803637, 130.0845382, 0.05410912, 91.05917674, -3093.60837501, 0.05, 2, 0, 72012, 23012, 1, 3)
    ops.uniaxialMaterial('LimitState', 32012, 32.52113455, 7.098e-05, 97.56340365, 0.00021293, 325.2113455, 0.00070977, -32.52113455, -7.098e-05, -97.56340365, -0.00021293, -325.2113455, -0.00070977, 0.4, 0.3, 0.003, 0.0, 0.0, 12012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2012, 99999, 'P', 42012, 'Vy', 32012, 'Vz', 22012, 'My', 12012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172012, 72012, 172012, 2012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123012, 123012, 23012, 2012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173001, 0.0, 0.0, 8.95)
    ops.node(124001, 0.0, 0.0, 10.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3001, 173001, 124001, 0.1225, 26253179.92213515, 10938824.96755631, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23001, 78.96373516, 0.00089183, 96.88056092, 0.03463451, 9.68805609, 0.10807178, -78.96373516, -0.00089183, -96.88056092, -0.03463451, -9.68805609, -0.10807178, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13001, 63.02611595, 0.00089183, 77.32670515, 0.03463451, 7.73267052, 0.10807178, -63.02611595, -0.00089183, -77.32670515, -0.03463451, -7.73267052, -0.10807178, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23001, 3001, 0.0, 139.45784343, 0.01783669, 139.45784343, 0.05351007, 97.6204904, -12338.45315337, 0.05, 2, 0, 73001, 24001, 2, 3)
    ops.uniaxialMaterial('LimitState', 43001, 34.86446086, 7.962e-05, 104.59338257, 0.00023885, 348.64460858, 0.00079615, -34.86446086, -7.962e-05, -104.59338257, -0.00023885, -348.64460858, -0.00079615, 0.4, 0.3, 0.003, 0.0, 0.0, 23001, 2)
    ops.limitCurve('ThreePoint', 13001, 3001, 0.0, 139.45784343, 0.01783669, 139.45784343, 0.05351007, 97.6204904, -12338.45315337, 0.05, 2, 0, 73001, 24001, 1, 3)
    ops.uniaxialMaterial('LimitState', 33001, 34.86446086, 7.962e-05, 104.59338257, 0.00023885, 348.64460858, 0.00079615, -34.86446086, -7.962e-05, -104.59338257, -0.00023885, -348.64460858, -0.00079615, 0.4, 0.3, 0.003, 0.0, 0.0, 13001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3001, 99999, 'P', 43001, 'Vy', 33001, 'Vz', 23001, 'My', 13001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173001, 73001, 173001, 3001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124001, 124001, 24001, 3001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173004, 14.45, 0.0, 8.95)
    ops.node(124004, 14.45, 0.0, 10.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3004, 173004, 124004, 0.1225, 28204584.60188689, 11751910.25078621, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23004, 83.9204782, 0.00090025, 102.52660485, 0.03262482, 10.25266048, 0.10683597, -83.9204782, -0.00090025, -102.52660485, -0.03262482, -10.25266048, -0.10683597, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13004, 66.76927517, 0.00090025, 81.5727846, 0.03262482, 8.15727846, 0.10683597, -66.76927517, -0.00090025, -81.5727846, -0.03262482, -8.15727846, -0.10683597, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23004, 3004, 0.0, 142.32190311, 0.01800498, 142.32190311, 0.05401493, 99.62533217, -11337.54995648, 0.05, 2, 0, 73004, 24004, 2, 3)
    ops.uniaxialMaterial('LimitState', 43004, 35.58047578, 7.563e-05, 106.74142733, 0.00022689, 355.80475777, 0.00075629, -35.58047578, -7.563e-05, -106.74142733, -0.00022689, -355.80475777, -0.00075629, 0.4, 0.3, 0.003, 0.0, 0.0, 23004, 2)
    ops.limitCurve('ThreePoint', 13004, 3004, 0.0, 142.32190311, 0.01800498, 142.32190311, 0.05401493, 99.62533217, -11337.54995648, 0.05, 2, 0, 73004, 24004, 1, 3)
    ops.uniaxialMaterial('LimitState', 33004, 35.58047578, 7.563e-05, 106.74142733, 0.00022689, 355.80475777, 0.00075629, -35.58047578, -7.563e-05, -106.74142733, -0.00022689, -355.80475777, -0.00075629, 0.4, 0.3, 0.003, 0.0, 0.0, 13004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3004, 99999, 'P', 43004, 'Vy', 33004, 'Vz', 23004, 'My', 13004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173004, 73004, 173004, 3004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124004, 124004, 24004, 3004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173005, 0.0, 4.15, 9.0)
    ops.node(124005, 0.0, 4.15, 10.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3005, 173005, 124005, 0.16, 27532434.52446334, 11471847.71852639, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23005, 149.97346524, 0.00095646, 183.39032049, 0.05633003, 18.33903205, 0.14768617, -149.97346524, -0.00095646, -183.39032049, -0.05633003, -18.33903205, -0.14768617, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13005, 133.34848044, 0.00095646, 163.06098233, 0.05633003, 16.30609823, 0.14768617, -133.34848044, -0.00095646, -163.06098233, -0.05633003, -16.30609823, -0.14768617, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23005, 3005, 0.0, 217.88773989, 0.01912925, 217.88773989, 0.05738776, 152.52141792, -17723.96908532, 0.05, 2, 0, 73005, 24005, 2, 3)
    ops.uniaxialMaterial('LimitState', 43005, 54.47193497, 9.081e-05, 163.41580492, 0.00027243, 544.71934972, 0.00090812, -54.47193497, -9.081e-05, -163.41580492, -0.00027243, -544.71934972, -0.00090812, 0.4, 0.3, 0.003, 0.0, 0.0, 23005, 2)
    ops.limitCurve('ThreePoint', 13005, 3005, 0.0, 217.88773989, 0.01912925, 217.88773989, 0.05738776, 152.52141792, -17723.96908532, 0.05, 2, 0, 73005, 24005, 1, 3)
    ops.uniaxialMaterial('LimitState', 33005, 54.47193497, 9.081e-05, 163.41580492, 0.00027243, 544.71934972, 0.00090812, -54.47193497, -9.081e-05, -163.41580492, -0.00027243, -544.71934972, -0.00090812, 0.4, 0.3, 0.003, 0.0, 0.0, 13005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3005, 99999, 'P', 43005, 'Vy', 33005, 'Vz', 23005, 'My', 13005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173005, 73005, 173005, 3005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124005, 124005, 24005, 3005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173006, 5.8, 4.15, 9.0)
    ops.node(124006, 5.8, 4.15, 10.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3006, 173006, 124006, 0.16, 27624398.41257858, 11510166.00524108, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23006, 113.06902127, 0.00091198, 138.12979346, 0.03188296, 13.81297935, 0.0827125, -113.06902127, -0.00091198, -138.12979346, -0.03188296, -13.81297935, -0.0827125, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13006, 113.06902127, 0.00091198, 138.12979346, 0.03188296, 13.81297935, 0.0827125, -113.06902127, -0.00091198, -138.12979346, -0.03188296, -13.81297935, -0.0827125, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23006, 3006, 0.0, 156.08881083, 0.01823951, 156.08881083, 0.05471854, 109.26216758, -4644.07329342, 0.05, 2, 0, 73006, 24006, 2, 3)
    ops.uniaxialMaterial('LimitState', 43006, 39.02220271, 6.484e-05, 117.06660812, 0.00019451, 390.22202706, 0.00064838, -39.02220271, -6.484e-05, -117.06660812, -0.00019451, -390.22202706, -0.00064838, 0.4, 0.3, 0.003, 0.0, 0.0, 23006, 2)
    ops.limitCurve('ThreePoint', 13006, 3006, 0.0, 156.08881083, 0.01823951, 156.08881083, 0.05471854, 109.26216758, -4644.07329342, 0.05, 2, 0, 73006, 24006, 1, 3)
    ops.uniaxialMaterial('LimitState', 33006, 39.02220271, 6.484e-05, 117.06660812, 0.00019451, 390.22202706, 0.00064838, -39.02220271, -6.484e-05, -117.06660812, -0.00019451, -390.22202706, -0.00064838, 0.4, 0.3, 0.003, 0.0, 0.0, 13006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3006, 99999, 'P', 43006, 'Vy', 33006, 'Vz', 23006, 'My', 13006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173006, 73006, 173006, 3006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124006, 124006, 24006, 3006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173007, 8.65, 4.15, 9.0)
    ops.node(124007, 8.65, 4.15, 10.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3007, 173007, 124007, 0.16, 27130705.82017782, 11304460.75840742, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23007, 108.3152509, 0.0009218, 132.45496037, 0.03444526, 13.24549604, 0.08501217, -108.3152509, -0.0009218, -132.45496037, -0.03444526, -13.24549604, -0.08501217, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13007, 108.3152509, 0.0009218, 132.45496037, 0.03444526, 13.24549604, 0.08501217, -108.3152509, -0.0009218, -132.45496037, -0.03444526, -13.24549604, -0.08501217, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23007, 3007, 0.0, 163.79199596, 0.01843594, 163.79199596, 0.05530783, 114.65439717, -5724.58234678, 0.05, 2, 0, 73007, 24007, 2, 3)
    ops.uniaxialMaterial('LimitState', 43007, 40.94799899, 6.928e-05, 122.84399697, 0.00020783, 409.4799899, 0.00069276, -40.94799899, -6.928e-05, -122.84399697, -0.00020783, -409.4799899, -0.00069276, 0.4, 0.3, 0.003, 0.0, 0.0, 23007, 2)
    ops.limitCurve('ThreePoint', 13007, 3007, 0.0, 163.79199596, 0.01843594, 163.79199596, 0.05530783, 114.65439717, -5724.58234678, 0.05, 2, 0, 73007, 24007, 1, 3)
    ops.uniaxialMaterial('LimitState', 33007, 40.94799899, 6.928e-05, 122.84399697, 0.00020783, 409.4799899, 0.00069276, -40.94799899, -6.928e-05, -122.84399697, -0.00020783, -409.4799899, -0.00069276, 0.4, 0.3, 0.003, 0.0, 0.0, 13007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3007, 99999, 'P', 43007, 'Vy', 33007, 'Vz', 23007, 'My', 13007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173007, 73007, 173007, 3007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124007, 124007, 24007, 3007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173008, 14.45, 4.15, 9.0)
    ops.node(124008, 14.45, 4.15, 10.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3008, 173008, 124008, 0.16, 28993110.08850084, 12080462.53687535, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23008, 155.68586154, 0.00092115, 189.72572052, 0.05666599, 18.97257205, 0.14891643, -155.68586154, -0.00092115, -189.72572052, -0.05666599, -18.97257205, -0.14891643, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13008, 137.70924349, 0.00092115, 167.81861362, 0.05666599, 16.78186136, 0.14891643, -137.70924349, -0.00092115, -167.81861362, -0.05666599, -16.78186136, -0.14891643, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23008, 3008, 0.0, 243.73556535, 0.01842294, 243.73556535, 0.05526881, 170.61489575, -22553.61365996, 0.05, 2, 0, 73008, 24008, 2, 3)
    ops.uniaxialMaterial('LimitState', 43008, 60.93389134, 9.647e-05, 182.80167401, 0.0002894, 609.33891338, 0.00096467, -60.93389134, -9.647e-05, -182.80167401, -0.0002894, -609.33891338, -0.00096467, 0.4, 0.3, 0.003, 0.0, 0.0, 23008, 2)
    ops.limitCurve('ThreePoint', 13008, 3008, 0.0, 243.73556535, 0.01842294, 243.73556535, 0.05526881, 170.61489575, -22553.61365996, 0.05, 2, 0, 73008, 24008, 1, 3)
    ops.uniaxialMaterial('LimitState', 33008, 60.93389134, 9.647e-05, 182.80167401, 0.0002894, 609.33891338, 0.00096467, -60.93389134, -9.647e-05, -182.80167401, -0.0002894, -609.33891338, -0.00096467, 0.4, 0.3, 0.003, 0.0, 0.0, 13008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3008, 99999, 'P', 43008, 'Vy', 33008, 'Vz', 23008, 'My', 13008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173008, 73008, 173008, 3008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124008, 124008, 24008, 3008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173009, 0.0, 8.3, 8.95)
    ops.node(124009, 0.0, 8.3, 10.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3009, 173009, 124009, 0.1225, 27939068.65764095, 11641278.60735039, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23009, 81.67320434, 0.00095013, 99.84379704, 0.0346706, 9.9843797, 0.10878951, -81.67320434, -0.00095013, -99.84379704, -0.0346706, -9.9843797, -0.10878951, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13009, 66.33506452, 0.00095013, 81.09323947, 0.0346706, 8.10932395, 0.10878951, -66.33506452, -0.00095013, -81.09323947, -0.0346706, -8.10932395, -0.10878951, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23009, 3009, 0.0, 149.60109494, 0.01900267, 149.60109494, 0.05700801, 104.72076646, -13582.31236288, 0.05, 2, 0, 73009, 24009, 2, 3)
    ops.uniaxialMaterial('LimitState', 43009, 37.40027374, 8.025e-05, 112.20082121, 0.00024076, 374.00273736, 0.00080253, -37.40027374, -8.025e-05, -112.20082121, -0.00024076, -374.00273736, -0.00080253, 0.4, 0.3, 0.003, 0.0, 0.0, 23009, 2)
    ops.limitCurve('ThreePoint', 13009, 3009, 0.0, 149.60109494, 0.01900267, 149.60109494, 0.05700801, 104.72076646, -13582.31236288, 0.05, 2, 0, 73009, 24009, 1, 3)
    ops.uniaxialMaterial('LimitState', 33009, 37.40027374, 8.025e-05, 112.20082121, 0.00024076, 374.00273736, 0.00080253, -37.40027374, -8.025e-05, -112.20082121, -0.00024076, -374.00273736, -0.00080253, 0.4, 0.3, 0.003, 0.0, 0.0, 13009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3009, 99999, 'P', 43009, 'Vy', 33009, 'Vz', 23009, 'My', 13009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173009, 73009, 173009, 3009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124009, 124009, 24009, 3009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173010, 5.8, 8.3, 8.95)
    ops.node(124010, 5.8, 8.3, 10.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3010, 173010, 124010, 0.1225, 26018517.25641327, 10841048.85683887, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23010, 67.66038932, 0.00089509, 82.99543805, 0.02143954, 8.2995438, 0.06962191, -67.66038932, -0.00089509, -82.99543805, -0.02143954, -8.2995438, -0.06962191, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13010, 56.85370986, 0.00089509, 69.7394532, 0.02143954, 6.97394532, 0.06962191, -56.85370986, -0.00089509, -69.7394532, -0.02143954, -6.97394532, -0.06962191, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23010, 3010, 0.0, 113.76933311, 0.01790186, 113.76933311, 0.05370559, 79.63853317, -4850.3727014, 0.05, 2, 0, 73010, 24010, 2, 3)
    ops.uniaxialMaterial('LimitState', 43010, 28.44233328, 6.554e-05, 85.32699983, 0.00019661, 284.42333276, 0.00065536, -28.44233328, -6.554e-05, -85.32699983, -0.00019661, -284.42333276, -0.00065536, 0.4, 0.3, 0.003, 0.0, 0.0, 23010, 2)
    ops.limitCurve('ThreePoint', 13010, 3010, 0.0, 113.76933311, 0.01790186, 113.76933311, 0.05370559, 79.63853317, -4850.3727014, 0.05, 2, 0, 73010, 24010, 1, 3)
    ops.uniaxialMaterial('LimitState', 33010, 28.44233328, 6.554e-05, 85.32699983, 0.00019661, 284.42333276, 0.00065536, -28.44233328, -6.554e-05, -85.32699983, -0.00019661, -284.42333276, -0.00065536, 0.4, 0.3, 0.003, 0.0, 0.0, 13010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3010, 99999, 'P', 43010, 'Vy', 33010, 'Vz', 23010, 'My', 13010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173010, 73010, 173010, 3010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124010, 124010, 24010, 3010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173011, 8.65, 8.3, 8.95)
    ops.node(124011, 8.65, 8.3, 10.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3011, 173011, 124011, 0.1225, 28488648.32723416, 11870270.13634757, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23011, 64.20710374, 0.00088605, 78.35038119, 0.01944337, 7.83503812, 0.06851863, -64.20710374, -0.00088605, -78.35038119, -0.01944337, -7.83503812, -0.06851863, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13011, 55.12368934, 0.00088605, 67.26610953, 0.01944337, 6.72661095, 0.06851863, -55.12368934, -0.00088605, -67.26610953, -0.01944337, -6.72661095, -0.06851863, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23011, 3011, 0.0, 116.82471719, 0.017721, 116.82471719, 0.05316299, 81.77730203, -4107.01708629, 0.05, 2, 0, 73011, 24011, 2, 3)
    ops.uniaxialMaterial('LimitState', 43011, 29.2061793, 6.146e-05, 87.61853789, 0.00018438, 292.06179297, 0.00061461, -29.2061793, -6.146e-05, -87.61853789, -0.00018438, -292.06179297, -0.00061461, 0.4, 0.3, 0.003, 0.0, 0.0, 23011, 2)
    ops.limitCurve('ThreePoint', 13011, 3011, 0.0, 116.82471719, 0.017721, 116.82471719, 0.05316299, 81.77730203, -4107.01708629, 0.05, 2, 0, 73011, 24011, 1, 3)
    ops.uniaxialMaterial('LimitState', 33011, 29.2061793, 6.146e-05, 87.61853789, 0.00018438, 292.06179297, 0.00061461, -29.2061793, -6.146e-05, -87.61853789, -0.00018438, -292.06179297, -0.00061461, 0.4, 0.3, 0.003, 0.0, 0.0, 13011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3011, 99999, 'P', 43011, 'Vy', 33011, 'Vz', 23011, 'My', 13011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173011, 73011, 173011, 3011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124011, 124011, 24011, 3011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173012, 14.45, 8.3, 8.95)
    ops.node(124012, 14.45, 8.3, 10.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3012, 173012, 124012, 0.1225, 30761984.08654795, 12817493.36939498, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23012, 80.67676685, 0.00085373, 97.88441739, 0.03561273, 9.78844174, 0.11055136, -80.67676685, -0.00085373, -97.88441739, -0.03561273, -9.78844174, -0.11055136, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13012, 64.78685561, 0.00085373, 78.60532671, 0.03561273, 7.86053267, 0.11055136, -64.78685561, -0.00085373, -78.60532671, -0.03561273, -7.86053267, -0.11055136, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23012, 3012, 0.0, 168.53316548, 0.01707459, 168.53316548, 0.05122378, 117.97321583, -16243.28038644, 0.05, 2, 0, 73012, 24012, 2, 3)
    ops.uniaxialMaterial('LimitState', 43012, 42.13329137, 8.211e-05, 126.39987411, 0.00024634, 421.33291369, 0.00082112, -42.13329137, -8.211e-05, -126.39987411, -0.00024634, -421.33291369, -0.00082112, 0.4, 0.3, 0.003, 0.0, 0.0, 23012, 2)
    ops.limitCurve('ThreePoint', 13012, 3012, 0.0, 168.53316548, 0.01707459, 168.53316548, 0.05122378, 117.97321583, -16243.28038644, 0.05, 2, 0, 73012, 24012, 1, 3)
    ops.uniaxialMaterial('LimitState', 33012, 42.13329137, 8.211e-05, 126.39987411, 0.00024634, 421.33291369, 0.00082112, -42.13329137, -8.211e-05, -126.39987411, -0.00024634, -421.33291369, -0.00082112, 0.4, 0.3, 0.003, 0.0, 0.0, 13012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3012, 99999, 'P', 43012, 'Vy', 33012, 'Vz', 23012, 'My', 13012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173012, 73012, 173012, 3012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124012, 124012, 24012, 3012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170002, 5.8, 0.0, 0.0)
    ops.node(124013, 5.8, 0.0, 1.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4030, 170002, 124013, 0.2025, 27602684.34676113, 11501118.47781714, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24030, 226.32017687, 0.00070884, 274.60228417, 0.03070567, 27.46022842, 0.07790239, -226.32017687, -0.00070884, -274.60228417, -0.03070567, -27.46022842, -0.07790239, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14030, 244.3713985, 0.00070884, 296.50447055, 0.03070567, 29.65044705, 0.07790239, -244.3713985, -0.00070884, -296.50447055, -0.03070567, -29.65044705, -0.07790239, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24030, 4030, 0.0, 328.02879216, 0.01417681, 328.02879216, 0.04253044, 229.62015451, -7256.78993054, 0.05, 2, 0, 70002, 24013, 2, 3)
    ops.uniaxialMaterial('LimitState', 44030, 82.00719804, 7.5e-05, 246.02159412, 0.000225, 820.0719804, 0.00075001, -82.00719804, -7.5e-05, -246.02159412, -0.000225, -820.0719804, -0.00075001, 0.4, 0.3, 0.003, 0.0, 0.0, 24030, 2)
    ops.limitCurve('ThreePoint', 14030, 4030, 0.0, 328.02879216, 0.01417681, 328.02879216, 0.04253044, 229.62015451, -7256.78993054, 0.05, 2, 0, 70002, 24013, 1, 3)
    ops.uniaxialMaterial('LimitState', 34030, 82.00719804, 7.5e-05, 246.02159412, 0.000225, 820.0719804, 0.00075001, -82.00719804, -7.5e-05, -246.02159412, -0.000225, -820.0719804, -0.00075001, 0.4, 0.3, 0.003, 0.0, 0.0, 14030, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4030, 99999, 'P', 44030, 'Vy', 34030, 'Vz', 24030, 'My', 14030, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170002, 70002, 170002, 4030, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124013, 124013, 24013, 4030, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174013, 5.8, 0.0, 1.975)
    ops.node(121002, 5.8, 0.0, 3.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4031, 174013, 121002, 0.2025, 29706044.79564267, 12377518.66485111, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24031, 182.99264035, 0.00069309, 221.37392163, 0.0262274, 22.13739216, 0.07723722, -182.99264035, -0.00069309, -221.37392163, -0.0262274, -22.13739216, -0.07723722, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14031, 151.94532565, 0.00069309, 183.81467445, 0.0262274, 18.38146744, 0.07723722, -151.94532565, -0.00069309, -183.81467445, -0.0262274, -18.38146744, -0.07723722, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24031, 4031, 0.0, 317.70009465, 0.01386175, 317.70009465, 0.04158526, 222.39006626, -5412.78467982, 0.05, 2, 0, 74013, 21002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44031, 79.42502366, 6.75e-05, 238.27507099, 0.00020249, 794.25023663, 0.00067496, -79.42502366, -6.75e-05, -238.27507099, -0.00020249, -794.25023663, -0.00067496, 0.4, 0.3, 0.003, 0.0, 0.0, 24031, 2)
    ops.limitCurve('ThreePoint', 14031, 4031, 0.0, 317.70009465, 0.01386175, 317.70009465, 0.04158526, 222.39006626, -5412.78467982, 0.05, 2, 0, 74013, 21002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34031, 79.42502366, 6.75e-05, 238.27507099, 0.00020249, 794.25023663, 0.00067496, -79.42502366, -6.75e-05, -238.27507099, -0.00020249, -794.25023663, -0.00067496, 0.4, 0.3, 0.003, 0.0, 0.0, 14031, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4031, 99999, 'P', 44031, 'Vy', 34031, 'Vz', 24031, 'My', 14031, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174013, 74013, 174013, 4031, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121002, 121002, 21002, 4031, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170003, 8.65, 0.0, 0.0)
    ops.node(124014, 8.65, 0.0, 1.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4032, 170003, 124014, 0.2025, 26935038.34657495, 11222932.64440623, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24032, 220.86289231, 0.00074502, 268.18220443, 0.03020377, 26.81822044, 0.07625645, -220.86289231, -0.00074502, -268.18220443, -0.03020377, -26.81822044, -0.07625645, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14032, 236.86892345, 0.00074502, 287.61748697, 0.03020377, 28.7617487, 0.07625645, -236.86892345, -0.00074502, -287.61748697, -0.03020377, -28.7617487, -0.07625645, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24032, 4032, 0.0, 323.16448089, 0.01490035, 323.16448089, 0.04470105, 226.21513662, -7365.06859401, 0.05, 2, 0, 70003, 24014, 2, 3)
    ops.uniaxialMaterial('LimitState', 44032, 80.79112022, 7.572e-05, 242.37336067, 0.00022716, 807.91120222, 0.0007572, -80.79112022, -7.572e-05, -242.37336067, -0.00022716, -807.91120222, -0.0007572, 0.4, 0.3, 0.003, 0.0, 0.0, 24032, 2)
    ops.limitCurve('ThreePoint', 14032, 4032, 0.0, 323.16448089, 0.01490035, 323.16448089, 0.04470105, 226.21513662, -7365.06859401, 0.05, 2, 0, 70003, 24014, 1, 3)
    ops.uniaxialMaterial('LimitState', 34032, 80.79112022, 7.572e-05, 242.37336067, 0.00022716, 807.91120222, 0.0007572, -80.79112022, -7.572e-05, -242.37336067, -0.00022716, -807.91120222, -0.0007572, 0.4, 0.3, 0.003, 0.0, 0.0, 14032, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4032, 99999, 'P', 44032, 'Vy', 34032, 'Vz', 24032, 'My', 14032, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170003, 70003, 170003, 4032, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124014, 124014, 24014, 4032, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174014, 8.65, 0.0, 1.975)
    ops.node(121003, 8.65, 0.0, 3.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4033, 174014, 121003, 0.2025, 27884144.93644137, 11618393.72351724, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24033, 181.12131755, 0.00067173, 219.81671151, 0.02838236, 21.98167115, 0.07692737, -181.12131755, -0.00067173, -219.81671151, -0.02838236, -21.98167115, -0.07692737, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14033, 148.36074305, 0.00067173, 180.0570529, 0.02838236, 18.00570529, 0.07692737, -148.36074305, -0.00067173, -180.0570529, -0.02838236, -18.00570529, -0.07692737, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24033, 4033, 0.0, 310.14151802, 0.01343469, 310.14151802, 0.04030406, 217.09906262, -6107.56236096, 0.05, 2, 0, 74014, 21003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44033, 77.53537951, 7.02e-05, 232.60613852, 0.00021059, 775.35379506, 0.00070195, -77.53537951, -7.02e-05, -232.60613852, -0.00021059, -775.35379506, -0.00070195, 0.4, 0.3, 0.003, 0.0, 0.0, 24033, 2)
    ops.limitCurve('ThreePoint', 14033, 4033, 0.0, 310.14151802, 0.01343469, 310.14151802, 0.04030406, 217.09906262, -6107.56236096, 0.05, 2, 0, 74014, 21003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34033, 77.53537951, 7.02e-05, 232.60613852, 0.00021059, 775.35379506, 0.00070195, -77.53537951, -7.02e-05, -232.60613852, -0.00021059, -775.35379506, -0.00070195, 0.4, 0.3, 0.003, 0.0, 0.0, 14033, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4033, 99999, 'P', 44033, 'Vy', 34033, 'Vz', 24033, 'My', 14033, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174014, 74014, 174014, 4033, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121003, 121003, 21003, 4033, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171002, 5.8, 0.0, 3.85)
    ops.node(124015, 5.8, 0.0, 4.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4035, 171002, 124015, 0.2025, 27301843.93728144, 11375768.3072006, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24035, 163.2093726, 0.00068076, 198.64266967, 0.02839665, 19.86426697, 0.07906334, -163.2093726, -0.00068076, -198.64266967, -0.02839665, -19.86426697, -0.07906334, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14035, 135.20393374, 0.00068076, 164.55715698, 0.02839665, 16.4557157, 0.07906334, -135.20393374, -0.00068076, -164.55715698, -0.02839665, -16.4557157, -0.07906334, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24035, 4035, 0.0, 338.64930087, 0.01361512, 338.64930087, 0.04084537, 237.05451061, -9192.30299424, 0.05, 2, 0, 71002, 24015, 2, 3)
    ops.uniaxialMaterial('LimitState', 44035, 84.66232522, 5.623e-05, 253.98697566, 0.00016869, 846.62325219, 0.00056231, -84.66232522, -5.623e-05, -253.98697566, -0.00016869, -846.62325219, -0.00056231, 0.4, 0.3, 0.003, 0.0, 0.0, 24035, 2)
    ops.limitCurve('ThreePoint', 14035, 4035, 0.0, 338.64930087, 0.01361512, 338.64930087, 0.04084537, 237.05451061, -9192.30299424, 0.05, 2, 0, 71002, 24015, 1, 3)
    ops.uniaxialMaterial('LimitState', 34035, 84.66232522, 5.623e-05, 253.98697566, 0.00016869, 846.62325219, 0.00056231, -84.66232522, -5.623e-05, -253.98697566, -0.00016869, -846.62325219, -0.00056231, 0.4, 0.3, 0.003, 0.0, 0.0, 14035, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4035, 99999, 'P', 44035, 'Vy', 34035, 'Vz', 24035, 'My', 14035, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171002, 71002, 171002, 4035, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124015, 124015, 24015, 4035, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174015, 5.8, 0.0, 5.0)
    ops.node(122002, 5.8, 0.0, 5.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4036, 174015, 122002, 0.2025, 27340209.43542022, 11391753.93142509, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24036, 166.012416, 0.00067392, 202.17089214, 0.02701822, 20.21708921, 0.07870382, -166.012416, -0.00067392, -202.17089214, -0.02701822, -20.21708921, -0.07870382, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14036, 134.67906498, 0.00067392, 164.01295382, 0.02701822, 16.40129538, 0.07870382, -134.67906498, -0.00067392, -164.01295382, -0.02701822, -16.40129538, -0.07870382, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24036, 4036, 0.0, 324.98566855, 0.01347831, 324.98566855, 0.04043493, 227.48996798, -8281.08452223, 0.05, 2, 0, 74015, 22002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44036, 81.24641714, 5.389e-05, 243.73925141, 0.00016166, 812.46417136, 0.00053887, -81.24641714, -5.389e-05, -243.73925141, -0.00016166, -812.46417136, -0.00053887, 0.4, 0.3, 0.003, 0.0, 0.0, 24036, 2)
    ops.limitCurve('ThreePoint', 14036, 4036, 0.0, 324.98566855, 0.01347831, 324.98566855, 0.04043493, 227.48996798, -8281.08452223, 0.05, 2, 0, 74015, 22002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34036, 81.24641714, 5.389e-05, 243.73925141, 0.00016166, 812.46417136, 0.00053887, -81.24641714, -5.389e-05, -243.73925141, -0.00016166, -812.46417136, -0.00053887, 0.4, 0.3, 0.003, 0.0, 0.0, 14036, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4036, 99999, 'P', 44036, 'Vy', 34036, 'Vz', 24036, 'My', 14036, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174015, 74015, 174015, 4036, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122002, 122002, 22002, 4036, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171003, 8.65, 0.0, 3.85)
    ops.node(124016, 8.65, 0.0, 4.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4037, 171003, 124016, 0.2025, 28891551.43561214, 12038146.43150506, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24037, 171.37150415, 0.00067413, 208.00060248, 0.02938814, 20.80006025, 0.08198627, -171.37150415, -0.00067413, -208.00060248, -0.02938814, -20.80006025, -0.08198627, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14037, 140.37941713, 0.00067413, 170.3842391, 0.02938814, 17.03842391, 0.08198627, -140.37941713, -0.00067413, -170.3842391, -0.02938814, -17.03842391, -0.08198627, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24037, 4037, 0.0, 365.20492788, 0.01348257, 365.20492788, 0.0404477, 255.64344951, -10136.28286938, 0.05, 2, 0, 71003, 24016, 2, 3)
    ops.uniaxialMaterial('LimitState', 44037, 91.30123197, 5.73e-05, 273.90369591, 0.00017191, 913.01231969, 0.00057304, -91.30123197, -5.73e-05, -273.90369591, -0.00017191, -913.01231969, -0.00057304, 0.4, 0.3, 0.003, 0.0, 0.0, 24037, 2)
    ops.limitCurve('ThreePoint', 14037, 4037, 0.0, 365.20492788, 0.01348257, 365.20492788, 0.0404477, 255.64344951, -10136.28286938, 0.05, 2, 0, 71003, 24016, 1, 3)
    ops.uniaxialMaterial('LimitState', 34037, 91.30123197, 5.73e-05, 273.90369591, 0.00017191, 913.01231969, 0.00057304, -91.30123197, -5.73e-05, -273.90369591, -0.00017191, -913.01231969, -0.00057304, 0.4, 0.3, 0.003, 0.0, 0.0, 14037, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4037, 99999, 'P', 44037, 'Vy', 34037, 'Vz', 24037, 'My', 14037, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171003, 71003, 171003, 4037, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124016, 124016, 24016, 4037, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174016, 8.65, 0.0, 5.0)
    ops.node(122003, 8.65, 0.0, 5.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4038, 174016, 122003, 0.2025, 27751050.16911313, 11562937.57046381, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24038, 170.88171399, 0.0006748, 207.96130444, 0.03040878, 20.79613044, 0.08259236, -170.88171399, -0.0006748, -207.96130444, -0.03040878, -20.79613044, -0.08259236, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14038, 137.62925981, 0.0006748, 167.49340659, 0.03040878, 16.74934066, 0.08259236, -137.62925981, -0.0006748, -167.49340659, -0.03040878, -16.74934066, -0.08259236, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24038, 4038, 0.0, 359.86352428, 0.01349604, 359.86352428, 0.04048813, 251.904467, -12101.64895787, 0.05, 2, 0, 74016, 22003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44038, 89.96588107, 5.879e-05, 269.89764321, 0.00017636, 899.6588107, 0.00058786, -89.96588107, -5.879e-05, -269.89764321, -0.00017636, -899.6588107, -0.00058786, 0.4, 0.3, 0.003, 0.0, 0.0, 24038, 2)
    ops.limitCurve('ThreePoint', 14038, 4038, 0.0, 359.86352428, 0.01349604, 359.86352428, 0.04048813, 251.904467, -12101.64895787, 0.05, 2, 0, 74016, 22003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34038, 89.96588107, 5.879e-05, 269.89764321, 0.00017636, 899.6588107, 0.00058786, -89.96588107, -5.879e-05, -269.89764321, -0.00017636, -899.6588107, -0.00058786, 0.4, 0.3, 0.003, 0.0, 0.0, 14038, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4038, 99999, 'P', 44038, 'Vy', 34038, 'Vz', 24038, 'My', 14038, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174016, 74016, 174016, 4038, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122003, 122003, 22003, 4038, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172002, 5.8, 0.0, 6.4)
    ops.node(124017, 5.8, 0.0, 7.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4040, 172002, 124017, 0.1225, 30534227.3739001, 12722594.73912504, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24040, 83.94751253, 0.00074803, 101.48749715, 0.01529898, 10.14874971, 0.05947441, -83.94751253, -0.00074803, -101.48749715, -0.01529898, -10.14874971, -0.05947441, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14040, 73.92895895, 0.00074803, 89.37566802, 0.01529898, 8.9375668, 0.05947441, -73.92895895, -0.00074803, -89.37566802, -0.01529898, -8.9375668, -0.05947441, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24040, 4040, 0.0, 191.42938363, 0.01496067, 191.42938363, 0.04488201, 134.00056854, -3632.3012589, 0.05, 2, 0, 72002, 24017, 2, 3)
    ops.uniaxialMaterial('LimitState', 44040, 47.85734591, 4.698e-05, 143.57203772, 0.00014094, 478.57345908, 0.00046982, -47.85734591, -4.698e-05, -143.57203772, -0.00014094, -478.57345908, -0.00046982, 0.4, 0.3, 0.003, 0.0, 0.0, 24040, 2)
    ops.limitCurve('ThreePoint', 14040, 4040, 0.0, 191.42938363, 0.01496067, 191.42938363, 0.04488201, 134.00056854, -3632.3012589, 0.05, 2, 0, 72002, 24017, 1, 3)
    ops.uniaxialMaterial('LimitState', 34040, 47.85734591, 4.698e-05, 143.57203772, 0.00014094, 478.57345908, 0.00046982, -47.85734591, -4.698e-05, -143.57203772, -0.00014094, -478.57345908, -0.00046982, 0.4, 0.3, 0.003, 0.0, 0.0, 14040, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4040, 99999, 'P', 44040, 'Vy', 34040, 'Vz', 24040, 'My', 14040, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172002, 72002, 172002, 4040, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124017, 124017, 24017, 4040, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174017, 5.8, 0.0, 7.55)
    ops.node(123002, 5.8, 0.0, 8.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4041, 174017, 123002, 0.1225, 27787165.49197738, 11577985.62165724, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24041, 80.87900643, 0.00074427, 98.43891986, 0.0187008, 9.84389199, 0.06177561, -80.87900643, -0.00074427, -98.43891986, -0.0187008, -9.84389199, -0.06177561, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14041, 69.95486097, 0.00074427, 85.14299641, 0.0187008, 8.51429964, 0.06177561, -69.95486097, -0.00074427, -85.14299641, -0.0187008, -8.51429964, -0.06177561, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24041, 4041, 0.0, 179.19348961, 0.01488536, 179.19348961, 0.04465609, 125.43544272, -4721.02296626, 0.05, 2, 0, 74017, 23002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44041, 44.7983724, 4.833e-05, 134.3951172, 0.00014498, 447.98372401, 0.00048326, -44.7983724, -4.833e-05, -134.3951172, -0.00014498, -447.98372401, -0.00048326, 0.4, 0.3, 0.003, 0.0, 0.0, 24041, 2)
    ops.limitCurve('ThreePoint', 14041, 4041, 0.0, 179.19348961, 0.01488536, 179.19348961, 0.04465609, 125.43544272, -4721.02296626, 0.05, 2, 0, 74017, 23002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34041, 44.7983724, 4.833e-05, 134.3951172, 0.00014498, 447.98372401, 0.00048326, -44.7983724, -4.833e-05, -134.3951172, -0.00014498, -447.98372401, -0.00048326, 0.4, 0.3, 0.003, 0.0, 0.0, 14041, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4041, 99999, 'P', 44041, 'Vy', 34041, 'Vz', 24041, 'My', 14041, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174017, 74017, 174017, 4041, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123002, 123002, 23002, 4041, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172003, 8.65, 0.0, 6.4)
    ops.node(124018, 8.65, 0.0, 7.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4042, 172003, 124018, 0.1225, 25392268.25933572, 10580111.77472322, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24042, 87.02175872, 0.00080916, 106.09547871, 0.01811244, 10.60954787, 0.05676811, -87.02175872, -0.00080916, -106.09547871, -0.01811244, -10.60954787, -0.05676811, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14042, 75.18043887, 0.00080916, 91.6587388, 0.01811244, 9.16587388, 0.05676811, -75.18043887, -0.00080916, -91.6587388, -0.01811244, -9.16587388, -0.05676811, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24042, 4042, 0.0, 166.30720941, 0.0161833, 166.30720941, 0.04854989, 116.41504659, -4276.70464271, 0.05, 2, 0, 72003, 24018, 2, 3)
    ops.uniaxialMaterial('LimitState', 44042, 41.57680235, 4.908e-05, 124.73040706, 0.00014724, 415.76802352, 0.00049081, -41.57680235, -4.908e-05, -124.73040706, -0.00014724, -415.76802352, -0.00049081, 0.4, 0.3, 0.003, 0.0, 0.0, 24042, 2)
    ops.limitCurve('ThreePoint', 14042, 4042, 0.0, 166.30720941, 0.0161833, 166.30720941, 0.04854989, 116.41504659, -4276.70464271, 0.05, 2, 0, 72003, 24018, 1, 3)
    ops.uniaxialMaterial('LimitState', 34042, 41.57680235, 4.908e-05, 124.73040706, 0.00014724, 415.76802352, 0.00049081, -41.57680235, -4.908e-05, -124.73040706, -0.00014724, -415.76802352, -0.00049081, 0.4, 0.3, 0.003, 0.0, 0.0, 14042, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4042, 99999, 'P', 44042, 'Vy', 34042, 'Vz', 24042, 'My', 14042, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172003, 72003, 172003, 4042, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124018, 124018, 24018, 4042, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174018, 8.65, 0.0, 7.55)
    ops.node(123003, 8.65, 0.0, 8.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4043, 174018, 123003, 0.1225, 27042734.91592156, 11267806.21496732, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24043, 77.83140803, 0.00076899, 94.84319209, 0.01967666, 9.48431921, 0.06201335, -77.83140803, -0.00076899, -94.84319209, -0.01967666, -9.48431921, -0.06201335, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14043, 68.22529127, 0.00076899, 83.137445, 0.01967666, 8.3137445, 0.06201335, -68.22529127, -0.00076899, -83.137445, -0.01967666, -8.3137445, -0.06201335, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24043, 4043, 0.0, 175.2886332, 0.01537976, 175.2886332, 0.04613929, 122.70204324, -4792.59937755, 0.05, 2, 0, 74018, 23003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44043, 43.8221583, 4.857e-05, 131.4664749, 0.00014572, 438.22158301, 0.00048575, -43.8221583, -4.857e-05, -131.4664749, -0.00014572, -438.22158301, -0.00048575, 0.4, 0.3, 0.003, 0.0, 0.0, 24043, 2)
    ops.limitCurve('ThreePoint', 14043, 4043, 0.0, 175.2886332, 0.01537976, 175.2886332, 0.04613929, 122.70204324, -4792.59937755, 0.05, 2, 0, 74018, 23003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34043, 43.8221583, 4.857e-05, 131.4664749, 0.00014572, 438.22158301, 0.00048575, -43.8221583, -4.857e-05, -131.4664749, -0.00014572, -438.22158301, -0.00048575, 0.4, 0.3, 0.003, 0.0, 0.0, 14043, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4043, 99999, 'P', 44043, 'Vy', 34043, 'Vz', 24043, 'My', 14043, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174018, 74018, 174018, 4043, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123003, 123003, 23003, 4043, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173002, 5.8, 0.0, 8.95)
    ops.node(124019, 5.8, 0.0, 9.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4045, 173002, 124019, 0.1225, 29380084.67565384, 12241701.9481891, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24045, 69.88766688, 0.00070663, 85.04670231, 0.01859949, 8.50467023, 0.0671636, -69.88766688, -0.00070663, -85.04670231, -0.01859949, -8.50467023, -0.0671636, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14045, 59.26535013, 0.00070663, 72.12034419, 0.01859949, 7.21203442, 0.0671636, -59.26535013, -0.00070663, -72.12034419, -0.01859949, -7.21203442, -0.0671636, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24045, 4045, 0.0, 175.19660716, 0.01413259, 175.19660716, 0.04239778, 122.63762501, -7214.98256266, 0.05, 2, 0, 73002, 24019, 2, 3)
    ops.uniaxialMaterial('LimitState', 44045, 43.79915179, 4.469e-05, 131.39745537, 0.00013406, 437.9915179, 0.00044687, -43.79915179, -4.469e-05, -131.39745537, -0.00013406, -437.9915179, -0.00044687, 0.4, 0.3, 0.003, 0.0, 0.0, 24045, 2)
    ops.limitCurve('ThreePoint', 14045, 4045, 0.0, 175.19660716, 0.01413259, 175.19660716, 0.04239778, 122.63762501, -7214.98256266, 0.05, 2, 0, 73002, 24019, 1, 3)
    ops.uniaxialMaterial('LimitState', 34045, 43.79915179, 4.469e-05, 131.39745537, 0.00013406, 437.9915179, 0.00044687, -43.79915179, -4.469e-05, -131.39745537, -0.00013406, -437.9915179, -0.00044687, 0.4, 0.3, 0.003, 0.0, 0.0, 14045, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4045, 99999, 'P', 44045, 'Vy', 34045, 'Vz', 24045, 'My', 14045, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173002, 73002, 173002, 4045, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124019, 124019, 24019, 4045, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174019, 5.8, 0.0, 10.1)
    ops.node(124002, 5.8, 0.0, 10.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4046, 174019, 124002, 0.1225, 27212692.94175111, 11338622.05906296, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24046, 67.33557071, 0.00073489, 82.44622544, 0.02670916, 8.24462254, 0.08520373, -67.33557071, -0.00073489, -82.44622544, -0.02670916, -8.24462254, -0.08520373, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14046, 56.5135214, 0.00073489, 69.19561944, 0.02670916, 6.91956194, 0.08520373, -56.5135214, -0.00073489, -69.19561944, -0.02670916, -6.91956194, -0.08520373, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24046, 4046, 0.0, 175.98505702, 0.01469783, 175.98505702, 0.0440935, 123.18953992, -18427.6934213, 0.05, 2, 0, 74019, 24002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44046, 43.99626426, 4.846e-05, 131.98879277, 0.00014539, 439.96264256, 0.00048463, -43.99626426, -4.846e-05, -131.98879277, -0.00014539, -439.96264256, -0.00048463, 0.4, 0.3, 0.003, 0.0, 0.0, 24046, 2)
    ops.limitCurve('ThreePoint', 14046, 4046, 0.0, 175.98505702, 0.01469783, 175.98505702, 0.0440935, 123.18953992, -18427.6934213, 0.05, 2, 0, 74019, 24002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34046, 43.99626426, 4.846e-05, 131.98879277, 0.00014539, 439.96264256, 0.00048463, -43.99626426, -4.846e-05, -131.98879277, -0.00014539, -439.96264256, -0.00048463, 0.4, 0.3, 0.003, 0.0, 0.0, 14046, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4046, 99999, 'P', 44046, 'Vy', 34046, 'Vz', 24046, 'My', 14046, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174019, 74019, 174019, 4046, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124002, 124002, 24002, 4046, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173003, 8.65, 0.0, 8.95)
    ops.node(124020, 8.65, 0.0, 9.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4047, 173003, 124020, 0.1225, 24593834.09550582, 10247430.87312743, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24047, 73.44177604, 0.0007655, 90.21269744, 0.01967464, 9.02126974, 0.06584495, -73.44177604, -0.0007655, -90.21269744, -0.01967464, -9.02126974, -0.06584495, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14047, 61.12406702, 0.0007655, 75.08215708, 0.01967464, 7.50821571, 0.06584495, -61.12406702, -0.0007655, -75.08215708, -0.01967464, -7.50821571, -0.06584495, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24047, 4047, 0.0, 145.67003034, 0.01531, 145.67003034, 0.04593, 101.96902124, -6972.77923796, 0.05, 2, 0, 73003, 24020, 2, 3)
    ops.uniaxialMaterial('LimitState', 44047, 36.41750758, 4.439e-05, 109.25252275, 0.00013316, 364.17507584, 0.00044386, -36.41750758, -4.439e-05, -109.25252275, -0.00013316, -364.17507584, -0.00044386, 0.4, 0.3, 0.003, 0.0, 0.0, 24047, 2)
    ops.limitCurve('ThreePoint', 14047, 4047, 0.0, 145.67003034, 0.01531, 145.67003034, 0.04593, 101.96902124, -6972.77923796, 0.05, 2, 0, 73003, 24020, 1, 3)
    ops.uniaxialMaterial('LimitState', 34047, 36.41750758, 4.439e-05, 109.25252275, 0.00013316, 364.17507584, 0.00044386, -36.41750758, -4.439e-05, -109.25252275, -0.00013316, -364.17507584, -0.00044386, 0.4, 0.3, 0.003, 0.0, 0.0, 14047, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4047, 99999, 'P', 44047, 'Vy', 34047, 'Vz', 24047, 'My', 14047, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173003, 73003, 173003, 4047, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124020, 124020, 24020, 4047, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174020, 8.65, 0.0, 10.1)
    ops.node(124003, 8.65, 0.0, 10.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4048, 174020, 124003, 0.1225, 26493722.11040679, 11039050.87933616, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24048, 65.84414446, 0.00073011, 80.74060591, 0.0265558, 8.07406059, 0.08480246, -65.84414446, -0.00073011, -80.74060591, -0.0265558, -8.07406059, -0.08480246, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14048, 55.25005631, 0.00073011, 67.74973021, 0.0265558, 6.77497302, 0.08480246, -55.25005631, -0.00073011, -67.74973021, -0.0265558, -6.77497302, -0.08480246, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24048, 4048, 0.0, 170.66783698, 0.01460217, 170.66783698, 0.04380651, 119.46748588, -17933.2850909, 0.05, 2, 0, 74020, 24003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44048, 42.66695924, 4.827e-05, 128.00087773, 0.00014482, 426.66959244, 0.00048274, -42.66695924, -4.827e-05, -128.00087773, -0.00014482, -426.66959244, -0.00048274, 0.4, 0.3, 0.003, 0.0, 0.0, 24048, 2)
    ops.limitCurve('ThreePoint', 14048, 4048, 0.0, 170.66783698, 0.01460217, 170.66783698, 0.04380651, 119.46748588, -17933.2850909, 0.05, 2, 0, 74020, 24003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34048, 42.66695924, 4.827e-05, 128.00087773, 0.00014482, 426.66959244, 0.00048274, -42.66695924, -4.827e-05, -128.00087773, -0.00014482, -426.66959244, -0.00048274, 0.4, 0.3, 0.003, 0.0, 0.0, 14048, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4048, 99999, 'P', 44048, 'Vy', 34048, 'Vz', 24048, 'My', 14048, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174020, 74020, 174020, 4048, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124003, 124003, 24003, 4048, '-orient', 0, 0, 1, 0, 1, 0)
