import openseespy.opensees as ops


def add_columns() -> None:
    """Add components of all columns to ops domain (plastic hinges, column elements and nodes)
    """
    # Create elastic column element nodes
    ops.node(170003, 9.6, 0.0, 0.0)
    ops.node(121003, 9.6, 0.0, 2.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3, 170003, 121003, 0.16, 26164800.56154356, 10902000.23397648, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20003, 113.80608861, 0.00059338, 138.07257248, 0.02890818, 13.80725725, 0.07578805, -113.80608861, -0.00059338, -138.07257248, -0.02890818, -13.80725725, -0.07578805, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10003, 122.67356964, 0.00059338, 148.83083623, 0.02890818, 14.88308362, 0.07578805, -122.67356964, -0.00059338, -148.83083623, -0.02890818, -14.88308362, -0.07578805, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20003, 3, 0.0, 161.20663907, 0.01186761, 161.20663907, 0.03560284, 112.84464735, -2193.1083407, 0.05, 2, 0, 70003, 21003, 2, 3)
    ops.uniaxialMaterial('LimitState', 40003, 40.30165977, 7.902e-05, 120.9049793, 0.00023705, 403.01659767, 0.00079017, -40.30165977, -7.902e-05, -120.9049793, -0.00023705, -403.01659767, -0.00079017, 0.4, 0.3, 0.003, 0.0, 0.0, 20003, 2)
    ops.limitCurve('ThreePoint', 10003, 3, 0.0, 161.20663907, 0.01186761, 161.20663907, 0.03560284, 112.84464735, -2193.1083407, 0.05, 2, 0, 70003, 21003, 1, 3)
    ops.uniaxialMaterial('LimitState', 30003, 40.30165977, 7.902e-05, 120.9049793, 0.00023705, 403.01659767, 0.00079017, -40.30165977, -7.902e-05, -120.9049793, -0.00023705, -403.01659767, -0.00079017, 0.4, 0.3, 0.003, 0.0, 0.0, 10003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3, 99999, 'P', 40003, 'Vy', 30003, 'Vz', 20003, 'My', 10003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170003, 70003, 170003, 3, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121003, 121003, 21003, 3, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170004, 16.25, 0.0, 0.0)
    ops.node(121004, 16.25, 0.0, 2.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4, 170004, 121004, 0.09, 27840449.32158704, 11600187.21732793, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20004, 54.18078537, 0.00073296, 65.6383893, 0.02403962, 6.56383893, 0.06630966, -54.18078537, -0.00073296, -65.6383893, -0.02403962, -6.56383893, -0.06630966, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10004, 51.40018752, 0.00073296, 62.26977878, 0.02403962, 6.22697788, 0.06630966, -51.40018752, -0.00073296, -62.26977878, -0.02403962, -6.22697788, -0.06630966, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20004, 4, 0.0, 88.81329147, 0.01465928, 88.81329147, 0.04397784, 62.16930403, -1029.88624041, 0.05, 2, 0, 70004, 21004, 2, 3)
    ops.uniaxialMaterial('LimitState', 40004, 22.20332287, 7.273e-05, 66.6099686, 0.0002182, 222.03322866, 0.00072734, -22.20332287, -7.273e-05, -66.6099686, -0.0002182, -222.03322866, -0.00072734, 0.4, 0.3, 0.003, 0.0, 0.0, 20004, 2)
    ops.limitCurve('ThreePoint', 10004, 4, 0.0, 88.81329147, 0.01465928, 88.81329147, 0.04397784, 62.16930403, -1029.88624041, 0.05, 2, 0, 70004, 21004, 1, 3)
    ops.uniaxialMaterial('LimitState', 30004, 22.20332287, 7.273e-05, 66.6099686, 0.0002182, 222.03322866, 0.00072734, -22.20332287, -7.273e-05, -66.6099686, -0.0002182, -222.03322866, -0.00072734, 0.4, 0.3, 0.003, 0.0, 0.0, 10004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4, 99999, 'P', 40004, 'Vy', 30004, 'Vz', 20004, 'My', 10004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170004, 70004, 170004, 4, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121004, 121004, 21004, 4, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170005, 0.0, 3.65, 0.0)
    ops.node(121005, 0.0, 3.65, 2.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 5, 170005, 121005, 0.09, 27601235.31822017, 11500514.71592507, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20005, 45.01030114, 0.00069497, 54.5330496, 0.02522406, 5.45330496, 0.07485052, -45.01030114, -0.00069497, -54.5330496, -0.02522406, -5.45330496, -0.07485052, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10005, 50.83478238, 0.00069497, 61.58980586, 0.02522406, 6.15898059, 0.07485052, -50.83478238, -0.00069497, -61.58980586, -0.02522406, -6.15898059, -0.07485052, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20005, 5, 0.0, 95.46799343, 0.01389948, 95.46799343, 0.04169844, 66.8275954, -1259.88098516, 0.05, 2, 0, 70005, 21005, 2, 3)
    ops.uniaxialMaterial('LimitState', 40005, 23.86699836, 7.886e-05, 71.60099507, 0.00023658, 238.66998356, 0.00078861, -23.86699836, -7.886e-05, -71.60099507, -0.00023658, -238.66998356, -0.00078861, 0.4, 0.3, 0.003, 0.0, 0.0, 20005, 2)
    ops.limitCurve('ThreePoint', 10005, 5, 0.0, 95.46799343, 0.01389948, 95.46799343, 0.04169844, 66.8275954, -1259.88098516, 0.05, 2, 0, 70005, 21005, 1, 3)
    ops.uniaxialMaterial('LimitState', 30005, 23.86699836, 7.886e-05, 71.60099507, 0.00023658, 238.66998356, 0.00078861, -23.86699836, -7.886e-05, -71.60099507, -0.00023658, -238.66998356, -0.00078861, 0.4, 0.3, 0.003, 0.0, 0.0, 10005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 5, 99999, 'P', 40005, 'Vy', 30005, 'Vz', 20005, 'My', 10005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170005, 70005, 170005, 5, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121005, 121005, 21005, 5, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170006, 2.95, 3.65, 0.0)
    ops.node(121006, 2.95, 3.65, 2.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 6, 170006, 121006, 0.16, 27569694.28155567, 11487372.61731486, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20006, 159.721617, 0.00060721, 193.31277773, 0.04300216, 19.33127777, 0.11042417, -159.721617, -0.00060721, -193.31277773, -0.04300216, -19.33127777, -0.11042417, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10006, 164.45672456, 0.00060721, 199.04372895, 0.04300216, 19.90437289, 0.11042417, -164.45672456, -0.00060721, -199.04372895, -0.04300216, -19.90437289, -0.11042417, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20006, 6, 0.0, 209.86735488, 0.01214413, 209.86735488, 0.03643238, 146.90714841, -3645.54400117, 0.05, 2, 0, 70006, 21006, 2, 3)
    ops.uniaxialMaterial('LimitState', 40006, 52.46683872, 9.763e-05, 157.40051616, 0.00029288, 524.66838719, 0.00097627, -52.46683872, -9.763e-05, -157.40051616, -0.00029288, -524.66838719, -0.00097627, 0.4, 0.3, 0.003, 0.0, 0.0, 20006, 2)
    ops.limitCurve('ThreePoint', 10006, 6, 0.0, 209.86735488, 0.01214413, 209.86735488, 0.03643238, 146.90714841, -3645.54400117, 0.05, 2, 0, 70006, 21006, 1, 3)
    ops.uniaxialMaterial('LimitState', 30006, 52.46683872, 9.763e-05, 157.40051616, 0.00029288, 524.66838719, 0.00097627, -52.46683872, -9.763e-05, -157.40051616, -0.00029288, -524.66838719, -0.00097627, 0.4, 0.3, 0.003, 0.0, 0.0, 10006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 6, 99999, 'P', 40006, 'Vy', 30006, 'Vz', 20006, 'My', 10006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170006, 70006, 170006, 6, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121006, 121006, 21006, 6, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170007, 9.6, 3.65, 0.0)
    ops.node(121007, 9.6, 3.65, 2.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 7, 170007, 121007, 0.2025, 27373518.03730932, 11405632.51554555, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20007, 193.9328481, 0.0005666, 234.89301894, 0.03997152, 23.48930189, 0.10140012, -193.9328481, -0.0005666, -234.89301894, -0.03997152, -23.48930189, -0.10140012, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10007, 210.82785193, 0.0005666, 255.35638289, 0.03997152, 25.53563829, 0.10140012, -210.82785193, -0.0005666, -255.35638289, -0.03997152, -25.53563829, -0.10140012, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20007, 7, 0.0, 241.87477216, 0.01133206, 241.87477216, 0.03399617, 169.31234051, -3751.02356275, 0.05, 2, 0, 70007, 21007, 2, 3)
    ops.uniaxialMaterial('LimitState', 40007, 60.46869304, 8.954e-05, 181.40607912, 0.00026862, 604.68693041, 0.00089539, -60.46869304, -8.954e-05, -181.40607912, -0.00026862, -604.68693041, -0.00089539, 0.4, 0.3, 0.003, 0.0, 0.0, 20007, 2)
    ops.limitCurve('ThreePoint', 10007, 7, 0.0, 241.87477216, 0.01133206, 241.87477216, 0.03399617, 169.31234051, -3751.02356275, 0.05, 2, 0, 70007, 21007, 1, 3)
    ops.uniaxialMaterial('LimitState', 30007, 60.46869304, 8.954e-05, 181.40607912, 0.00026862, 604.68693041, 0.00089539, -60.46869304, -8.954e-05, -181.40607912, -0.00026862, -604.68693041, -0.00089539, 0.4, 0.3, 0.003, 0.0, 0.0, 10007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 7, 99999, 'P', 40007, 'Vy', 30007, 'Vz', 20007, 'My', 10007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170007, 70007, 170007, 7, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121007, 121007, 21007, 7, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170008, 16.25, 3.65, 0.0)
    ops.node(121008, 16.25, 3.65, 2.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 8, 170008, 121008, 0.16, 27058245.626104, 11274269.01087667, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20008, 115.95113099, 0.0006054, 140.71060206, 0.0432955, 14.07106021, 0.11369264, -115.95113099, -0.0006054, -140.71060206, -0.0432955, -14.07106021, -0.11369264, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10008, 124.00278485, 0.0006054, 150.48155515, 0.0432955, 15.04815551, 0.11369264, -124.00278485, -0.0006054, -150.48155515, -0.0432955, -15.04815551, -0.11369264, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20008, 8, 0.0, 199.03106658, 0.01210799, 199.03106658, 0.03632397, 139.32174661, -3641.5194447, 0.05, 2, 0, 70008, 21008, 2, 3)
    ops.uniaxialMaterial('LimitState', 40008, 49.75776665, 9.434e-05, 149.27329994, 0.00028301, 497.57766646, 0.00094336, -49.75776665, -9.434e-05, -149.27329994, -0.00028301, -497.57766646, -0.00094336, 0.4, 0.3, 0.003, 0.0, 0.0, 20008, 2)
    ops.limitCurve('ThreePoint', 10008, 8, 0.0, 199.03106658, 0.01210799, 199.03106658, 0.03632397, 139.32174661, -3641.5194447, 0.05, 2, 0, 70008, 21008, 1, 3)
    ops.uniaxialMaterial('LimitState', 30008, 49.75776665, 9.434e-05, 149.27329994, 0.00028301, 497.57766646, 0.00094336, -49.75776665, -9.434e-05, -149.27329994, -0.00028301, -497.57766646, -0.00094336, 0.4, 0.3, 0.003, 0.0, 0.0, 10008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 8, 99999, 'P', 40008, 'Vy', 30008, 'Vz', 20008, 'My', 10008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170008, 70008, 170008, 8, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121008, 121008, 21008, 8, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170009, 0.0, 7.3, 0.0)
    ops.node(121009, 0.0, 7.3, 2.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 9, 170009, 121009, 0.09, 27990151.46102585, 11662563.10876077, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20009, 42.07747809, 0.00069295, 51.04037678, 0.02600154, 5.10403768, 0.07890934, -42.07747809, -0.00069295, -51.04037678, -0.02600154, -5.10403768, -0.07890934, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10009, 47.5977654, 0.00069295, 57.73653722, 0.02600154, 5.77365372, 0.07890934, -47.5977654, -0.00069295, -57.73653722, -0.02600154, -5.77365372, -0.07890934, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20009, 9, 0.0, 94.11998178, 0.01385896, 94.11998178, 0.04157687, 65.88398725, -1267.62349344, 0.05, 2, 0, 70009, 21009, 2, 3)
    ops.uniaxialMaterial('LimitState', 40009, 23.52999545, 7.667e-05, 70.58998634, 0.00023, 235.29995446, 0.00076668, -23.52999545, -7.667e-05, -70.58998634, -0.00023, -235.29995446, -0.00076668, 0.4, 0.3, 0.003, 0.0, 0.0, 20009, 2)
    ops.limitCurve('ThreePoint', 10009, 9, 0.0, 94.11998178, 0.01385896, 94.11998178, 0.04157687, 65.88398725, -1267.62349344, 0.05, 2, 0, 70009, 21009, 1, 3)
    ops.uniaxialMaterial('LimitState', 30009, 23.52999545, 7.667e-05, 70.58998634, 0.00023, 235.29995446, 0.00076668, -23.52999545, -7.667e-05, -70.58998634, -0.00023, -235.29995446, -0.00076668, 0.4, 0.3, 0.003, 0.0, 0.0, 10009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 9, 99999, 'P', 40009, 'Vy', 30009, 'Vz', 20009, 'My', 10009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170009, 70009, 170009, 9, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121009, 121009, 21009, 9, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170010, 2.95, 7.3, 0.0)
    ops.node(121010, 2.95, 7.3, 2.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 10, 170010, 121010, 0.16, 27302653.53285908, 11376105.63869128, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20010, 156.22881111, 0.00061934, 189.38290598, 0.04338993, 18.9382906, 0.11271416, -156.22881111, -0.00061934, -189.38290598, -0.04338993, -18.9382906, -0.11271416, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10010, 160.88984959, 0.00061934, 195.03308667, 0.04338993, 19.50330867, 0.11271416, -160.88984959, -0.00061934, -195.03308667, -0.04338993, -19.50330867, -0.11271416, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20010, 10, 0.0, 200.77869018, 0.01238673, 200.77869018, 0.03716019, 140.54508313, -3519.9879883, 0.05, 2, 0, 70010, 21010, 2, 3)
    ops.uniaxialMaterial('LimitState', 40010, 50.19467255, 9.431e-05, 150.58401764, 0.00028294, 501.94672546, 0.00094313, -50.19467255, -9.431e-05, -150.58401764, -0.00028294, -501.94672546, -0.00094313, 0.4, 0.3, 0.003, 0.0, 0.0, 20010, 2)
    ops.limitCurve('ThreePoint', 10010, 10, 0.0, 200.77869018, 0.01238673, 200.77869018, 0.03716019, 140.54508313, -3519.9879883, 0.05, 2, 0, 70010, 21010, 1, 3)
    ops.uniaxialMaterial('LimitState', 30010, 50.19467255, 9.431e-05, 150.58401764, 0.00028294, 501.94672546, 0.00094313, -50.19467255, -9.431e-05, -150.58401764, -0.00028294, -501.94672546, -0.00094313, 0.4, 0.3, 0.003, 0.0, 0.0, 10010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 10, 99999, 'P', 40010, 'Vy', 30010, 'Vz', 20010, 'My', 10010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170010, 70010, 170010, 10, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121010, 121010, 21010, 10, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170011, 9.6, 7.3, 0.0)
    ops.node(121011, 9.6, 7.3, 2.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 11, 170011, 121011, 0.2025, 27223283.14499593, 11343034.6437483, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20011, 204.20389862, 0.00056708, 247.36636575, 0.04037039, 24.73663658, 0.10139401, -204.20389862, -0.00056708, -247.36636575, -0.04037039, -24.73663658, -0.10139401, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10011, 215.4219473, 0.00056708, 260.95556729, 0.04037039, 26.09555673, 0.10139401, -215.4219473, -0.00056708, -260.95556729, -0.04037039, -26.09555673, -0.10139401, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20011, 11, 0.0, 241.89849055, 0.01134167, 241.89849055, 0.034025, 169.32894338, -3786.43441114, 0.05, 2, 0, 70011, 21011, 2, 3)
    ops.uniaxialMaterial('LimitState', 40011, 60.47462264, 9.004e-05, 181.42386791, 0.00027013, 604.74622637, 0.00090042, -60.47462264, -9.004e-05, -181.42386791, -0.00027013, -604.74622637, -0.00090042, 0.4, 0.3, 0.003, 0.0, 0.0, 20011, 2)
    ops.limitCurve('ThreePoint', 10011, 11, 0.0, 241.89849055, 0.01134167, 241.89849055, 0.034025, 169.32894338, -3786.43441114, 0.05, 2, 0, 70011, 21011, 1, 3)
    ops.uniaxialMaterial('LimitState', 30011, 60.47462264, 9.004e-05, 181.42386791, 0.00027013, 604.74622637, 0.00090042, -60.47462264, -9.004e-05, -181.42386791, -0.00027013, -604.74622637, -0.00090042, 0.4, 0.3, 0.003, 0.0, 0.0, 10011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 11, 99999, 'P', 40011, 'Vy', 30011, 'Vz', 20011, 'My', 10011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170011, 70011, 170011, 11, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121011, 121011, 21011, 11, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170012, 16.25, 7.3, 0.0)
    ops.node(121012, 16.25, 7.3, 2.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 12, 170012, 121012, 0.16, 27994260.73399261, 11664275.30583026, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20012, 113.35942715, 0.00060881, 137.41446624, 0.04345244, 13.74144662, 0.11632252, -113.35942715, -0.00060881, -137.41446624, -0.04345244, -13.74144662, -0.11632252, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10012, 120.62998121, 0.00060881, 146.22784268, 0.04345244, 14.62278427, 0.11632252, -120.62998121, -0.00060881, -146.22784268, -0.04345244, -14.62278427, -0.11632252, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20012, 12, 0.0, 203.24279177, 0.01217616, 203.24279177, 0.03652847, 142.26995424, -3635.2675554, 0.05, 2, 0, 70012, 21012, 2, 3)
    ops.uniaxialMaterial('LimitState', 40012, 50.81069794, 9.311e-05, 152.43209383, 0.00027933, 508.10697942, 0.00093112, -50.81069794, -9.311e-05, -152.43209383, -0.00027933, -508.10697942, -0.00093112, 0.4, 0.3, 0.003, 0.0, 0.0, 20012, 2)
    ops.limitCurve('ThreePoint', 10012, 12, 0.0, 203.24279177, 0.01217616, 203.24279177, 0.03652847, 142.26995424, -3635.2675554, 0.05, 2, 0, 70012, 21012, 1, 3)
    ops.uniaxialMaterial('LimitState', 30012, 50.81069794, 9.311e-05, 152.43209383, 0.00027933, 508.10697942, 0.00093112, -50.81069794, -9.311e-05, -152.43209383, -0.00027933, -508.10697942, -0.00093112, 0.4, 0.3, 0.003, 0.0, 0.0, 10012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 12, 99999, 'P', 40012, 'Vy', 30012, 'Vz', 20012, 'My', 10012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170012, 70012, 170012, 12, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121012, 121012, 21012, 12, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170013, 0.0, 10.95, 0.0)
    ops.node(121013, 0.0, 10.95, 2.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 13, 170013, 121013, 0.09, 27797306.29059401, 11582210.95441417, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20013, 42.36204897, 0.00068494, 51.39943007, 0.02601819, 5.13994301, 0.07859636, -42.36204897, -0.00068494, -51.39943007, -0.02601819, -5.13994301, -0.07859636, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10013, 48.20492494, 0.00068494, 58.4888061, 0.02601819, 5.84888061, 0.07859636, -48.20492494, -0.00068494, -58.4888061, -0.02601819, -5.84888061, -0.07859636, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20013, 13, 0.0, 94.2321437, 0.01369882, 94.2321437, 0.04109645, 65.96250059, -1290.70474848, 0.05, 2, 0, 70013, 21013, 2, 3)
    ops.uniaxialMaterial('LimitState', 40013, 23.55803593, 7.729e-05, 70.67410778, 0.00023187, 235.58035926, 0.00077291, -23.55803593, -7.729e-05, -70.67410778, -0.00023187, -235.58035926, -0.00077291, 0.4, 0.3, 0.003, 0.0, 0.0, 20013, 2)
    ops.limitCurve('ThreePoint', 10013, 13, 0.0, 94.2321437, 0.01369882, 94.2321437, 0.04109645, 65.96250059, -1290.70474848, 0.05, 2, 0, 70013, 21013, 1, 3)
    ops.uniaxialMaterial('LimitState', 30013, 23.55803593, 7.729e-05, 70.67410778, 0.00023187, 235.58035926, 0.00077291, -23.55803593, -7.729e-05, -70.67410778, -0.00023187, -235.58035926, -0.00077291, 0.4, 0.3, 0.003, 0.0, 0.0, 10013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 13, 99999, 'P', 40013, 'Vy', 30013, 'Vz', 20013, 'My', 10013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170013, 70013, 170013, 13, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121013, 121013, 21013, 13, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170014, 2.95, 10.95, 0.0)
    ops.node(121014, 2.95, 10.95, 2.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 14, 170014, 121014, 0.16, 26832014.25445624, 11180005.93935677, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20014, 154.97071281, 0.00060532, 187.93583916, 0.04365931, 18.79358392, 0.11160127, -154.97071281, -0.00060532, -187.93583916, -0.04365931, -18.79358392, -0.11160127, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10014, 159.73375811, 0.00060532, 193.71207197, 0.04365931, 19.3712072, 0.11160127, -159.73375811, -0.00060532, -193.71207197, -0.04365931, -19.3712072, -0.11160127, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20014, 14, 0.0, 201.44463123, 0.01210632, 201.44463123, 0.03631895, 141.01124186, -3643.85039024, 0.05, 2, 0, 70014, 21014, 2, 3)
    ops.uniaxialMaterial('LimitState', 40014, 50.36115781, 9.629e-05, 151.08347342, 0.00028886, 503.61157806, 0.00096285, -50.36115781, -9.629e-05, -151.08347342, -0.00028886, -503.61157806, -0.00096285, 0.4, 0.3, 0.003, 0.0, 0.0, 20014, 2)
    ops.limitCurve('ThreePoint', 10014, 14, 0.0, 201.44463123, 0.01210632, 201.44463123, 0.03631895, 141.01124186, -3643.85039024, 0.05, 2, 0, 70014, 21014, 1, 3)
    ops.uniaxialMaterial('LimitState', 30014, 50.36115781, 9.629e-05, 151.08347342, 0.00028886, 503.61157806, 0.00096285, -50.36115781, -9.629e-05, -151.08347342, -0.00028886, -503.61157806, -0.00096285, 0.4, 0.3, 0.003, 0.0, 0.0, 10014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 14, 99999, 'P', 40014, 'Vy', 30014, 'Vz', 20014, 'My', 10014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170014, 70014, 170014, 14, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121014, 121014, 21014, 14, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170015, 9.6, 10.95, 0.0)
    ops.node(121015, 9.6, 10.95, 2.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 15, 170015, 121015, 0.2025, 27764742.8153908, 11568642.83974617, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20015, 205.05429436, 0.00057321, 248.26587757, 0.04077035, 24.82658776, 0.10322136, -205.05429436, -0.00057321, -248.26587757, -0.04077035, -24.82658776, -0.10322136, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10015, 216.06926563, 0.00057321, 261.60206015, 0.04077035, 26.16020601, 0.10322136, -216.06926563, -0.00057321, -261.60206015, -0.04077035, -26.16020601, -0.10322136, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20015, 15, 0.0, 250.00961666, 0.01146426, 250.00961666, 0.03439277, 175.00673166, -3976.12470799, 0.05, 2, 0, 70015, 21015, 2, 3)
    ops.uniaxialMaterial('LimitState', 40015, 62.50240417, 9.125e-05, 187.5072125, 0.00027374, 625.02404165, 0.00091246, -62.50240417, -9.125e-05, -187.5072125, -0.00027374, -625.02404165, -0.00091246, 0.4, 0.3, 0.003, 0.0, 0.0, 20015, 2)
    ops.limitCurve('ThreePoint', 10015, 15, 0.0, 250.00961666, 0.01146426, 250.00961666, 0.03439277, 175.00673166, -3976.12470799, 0.05, 2, 0, 70015, 21015, 1, 3)
    ops.uniaxialMaterial('LimitState', 30015, 62.50240417, 9.125e-05, 187.5072125, 0.00027374, 625.02404165, 0.00091246, -62.50240417, -9.125e-05, -187.5072125, -0.00027374, -625.02404165, -0.00091246, 0.4, 0.3, 0.003, 0.0, 0.0, 10015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 15, 99999, 'P', 40015, 'Vy', 30015, 'Vz', 20015, 'My', 10015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170015, 70015, 170015, 15, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121015, 121015, 21015, 15, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170016, 16.25, 10.95, 0.0)
    ops.node(121016, 16.25, 10.95, 2.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 16, 170016, 121016, 0.16, 26998694.20683129, 11249455.91951304, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20016, 114.91798045, 0.00060544, 139.46491387, 0.04301651, 13.94649139, 0.11324667, -114.91798045, -0.00060544, -139.46491387, -0.04301651, -13.94649139, -0.11324667, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10016, 122.77506749, 0.00060544, 149.00030565, 0.04301651, 14.90003057, 0.11324667, -122.77506749, -0.00060544, -149.00030565, -0.04301651, -14.90003057, -0.11324667, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20016, 16, 0.0, 194.53921501, 0.01210882, 194.53921501, 0.03632646, 136.1774505, -3451.58508048, 0.05, 2, 0, 70016, 21016, 2, 3)
    ops.uniaxialMaterial('LimitState', 40016, 48.63480375, 9.241e-05, 145.90441125, 0.00027723, 486.34803751, 0.00092411, -48.63480375, -9.241e-05, -145.90441125, -0.00027723, -486.34803751, -0.00092411, 0.4, 0.3, 0.003, 0.0, 0.0, 20016, 2)
    ops.limitCurve('ThreePoint', 10016, 16, 0.0, 194.53921501, 0.01210882, 194.53921501, 0.03632646, 136.1774505, -3451.58508048, 0.05, 2, 0, 70016, 21016, 1, 3)
    ops.uniaxialMaterial('LimitState', 30016, 48.63480375, 9.241e-05, 145.90441125, 0.00027723, 486.34803751, 0.00092411, -48.63480375, -9.241e-05, -145.90441125, -0.00027723, -486.34803751, -0.00092411, 0.4, 0.3, 0.003, 0.0, 0.0, 10016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 16, 99999, 'P', 40016, 'Vy', 30016, 'Vz', 20016, 'My', 10016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170016, 70016, 170016, 16, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121016, 121016, 21016, 16, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170017, 0.0, 14.6, 0.0)
    ops.node(121017, 0.0, 14.6, 2.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 17, 170017, 121017, 0.09, 28401895.65062046, 11834123.18775853, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20017, 42.70985464, 0.00067762, 51.77521405, 0.02596406, 5.17752141, 0.07955005, -42.70985464, -0.00067762, -51.77521405, -0.02596406, -5.17752141, -0.07955005, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10017, 48.73649029, 0.00067762, 59.08103033, 0.02596406, 5.90810303, 0.07955005, -48.73649029, -0.00067762, -59.08103033, -0.02596406, -5.90810303, -0.07955005, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20017, 17, 0.0, 95.26563526, 0.01355234, 95.26563526, 0.04065701, 66.68594468, -1269.83451002, 0.05, 2, 0, 70017, 21017, 2, 3)
    ops.uniaxialMaterial('LimitState', 40017, 23.81640882, 7.648e-05, 71.44922645, 0.00022943, 238.16408815, 0.00076476, -23.81640882, -7.648e-05, -71.44922645, -0.00022943, -238.16408815, -0.00076476, 0.4, 0.3, 0.003, 0.0, 0.0, 20017, 2)
    ops.limitCurve('ThreePoint', 10017, 17, 0.0, 95.26563526, 0.01355234, 95.26563526, 0.04065701, 66.68594468, -1269.83451002, 0.05, 2, 0, 70017, 21017, 1, 3)
    ops.uniaxialMaterial('LimitState', 30017, 23.81640882, 7.648e-05, 71.44922645, 0.00022943, 238.16408815, 0.00076476, -23.81640882, -7.648e-05, -71.44922645, -0.00022943, -238.16408815, -0.00076476, 0.4, 0.3, 0.003, 0.0, 0.0, 10017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 17, 99999, 'P', 40017, 'Vy', 30017, 'Vz', 20017, 'My', 10017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170017, 70017, 170017, 17, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121017, 121017, 21017, 17, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170018, 2.95, 14.6, 0.0)
    ops.node(121018, 2.95, 14.6, 2.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 18, 170018, 121018, 0.16, 28627128.22616072, 11927970.09423363, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20018, 153.08068707, 0.00059723, 185.25896892, 0.04387311, 18.52589689, 0.11670068, -153.08068707, -0.00059723, -185.25896892, -0.04387311, -18.52589689, -0.11670068, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10018, 157.58266273, 0.00059723, 190.70728108, 0.04387311, 19.07072811, 0.11670068, -157.58266273, -0.00059723, -190.70728108, -0.04387311, -19.07072811, -0.11670068, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20018, 18, 0.0, 207.70593624, 0.01194466, 207.70593624, 0.03583399, 145.39415537, -3549.74994245, 0.05, 2, 0, 70018, 21018, 2, 3)
    ops.uniaxialMaterial('LimitState', 40018, 51.92648406, 9.305e-05, 155.77945218, 0.00027916, 519.26484061, 0.00093053, -51.92648406, -9.305e-05, -155.77945218, -0.00027916, -519.26484061, -0.00093053, 0.4, 0.3, 0.003, 0.0, 0.0, 20018, 2)
    ops.limitCurve('ThreePoint', 10018, 18, 0.0, 207.70593624, 0.01194466, 207.70593624, 0.03583399, 145.39415537, -3549.74994245, 0.05, 2, 0, 70018, 21018, 1, 3)
    ops.uniaxialMaterial('LimitState', 30018, 51.92648406, 9.305e-05, 155.77945218, 0.00027916, 519.26484061, 0.00093053, -51.92648406, -9.305e-05, -155.77945218, -0.00027916, -519.26484061, -0.00093053, 0.4, 0.3, 0.003, 0.0, 0.0, 10018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 18, 99999, 'P', 40018, 'Vy', 30018, 'Vz', 20018, 'My', 10018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170018, 70018, 170018, 18, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121018, 121018, 21018, 18, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170019, 9.6, 14.6, 0.0)
    ops.node(121019, 9.6, 14.6, 2.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 19, 170019, 121019, 0.2025, 27724384.06680581, 11551826.69450242, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20019, 201.69365588, 0.00056544, 244.20767362, 0.04055401, 24.42076736, 0.10290167, -201.69365588, -0.00056544, -244.20767362, -0.04055401, -24.42076736, -0.10290167, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10019, 212.45496824, 0.00056544, 257.23731029, 0.04055401, 25.72373103, 0.10290167, -212.45496824, -0.00056544, -257.23731029, -0.04055401, -25.72373103, -0.10290167, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20019, 19, 0.0, 243.41254227, 0.01130878, 243.41254227, 0.03392633, 170.38877959, -3729.24196183, 0.05, 2, 0, 70019, 21019, 2, 3)
    ops.uniaxialMaterial('LimitState', 40019, 60.85313557, 8.897e-05, 182.5594067, 0.0002669, 608.53135568, 0.00088968, -60.85313557, -8.897e-05, -182.5594067, -0.0002669, -608.53135568, -0.00088968, 0.4, 0.3, 0.003, 0.0, 0.0, 20019, 2)
    ops.limitCurve('ThreePoint', 10019, 19, 0.0, 243.41254227, 0.01130878, 243.41254227, 0.03392633, 170.38877959, -3729.24196183, 0.05, 2, 0, 70019, 21019, 1, 3)
    ops.uniaxialMaterial('LimitState', 30019, 60.85313557, 8.897e-05, 182.5594067, 0.0002669, 608.53135568, 0.00088968, -60.85313557, -8.897e-05, -182.5594067, -0.0002669, -608.53135568, -0.00088968, 0.4, 0.3, 0.003, 0.0, 0.0, 10019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 19, 99999, 'P', 40019, 'Vy', 30019, 'Vz', 20019, 'My', 10019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170019, 70019, 170019, 19, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121019, 121019, 21019, 19, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170020, 16.25, 14.6, 0.0)
    ops.node(121020, 16.25, 14.6, 2.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 20, 170020, 121020, 0.16, 28599797.08678026, 11916582.11949178, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20020, 116.39054463, 0.00059971, 140.9629173, 0.04310454, 14.09629173, 0.11743207, -116.39054463, -0.00059971, -140.9629173, -0.04310454, -14.09629173, -0.11743207, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10020, 124.31576119, 0.00059971, 150.56130564, 0.04310454, 15.05613056, 0.11743207, -124.31576119, -0.00059971, -150.56130564, -0.04310454, -15.05613056, -0.11743207, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20020, 20, 0.0, 205.43282847, 0.01199423, 205.43282847, 0.03598269, 143.80297993, -3604.90119007, 0.05, 2, 0, 70020, 21020, 2, 3)
    ops.uniaxialMaterial('LimitState', 40020, 51.35820712, 9.212e-05, 154.07462135, 0.00027637, 513.58207117, 0.00092122, -51.35820712, -9.212e-05, -154.07462135, -0.00027637, -513.58207117, -0.00092122, 0.4, 0.3, 0.003, 0.0, 0.0, 20020, 2)
    ops.limitCurve('ThreePoint', 10020, 20, 0.0, 205.43282847, 0.01199423, 205.43282847, 0.03598269, 143.80297993, -3604.90119007, 0.05, 2, 0, 70020, 21020, 1, 3)
    ops.uniaxialMaterial('LimitState', 30020, 51.35820712, 9.212e-05, 154.07462135, 0.00027637, 513.58207117, 0.00092122, -51.35820712, -9.212e-05, -154.07462135, -0.00027637, -513.58207117, -0.00092122, 0.4, 0.3, 0.003, 0.0, 0.0, 10020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 20, 99999, 'P', 40020, 'Vy', 30020, 'Vz', 20020, 'My', 10020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170020, 70020, 170020, 20, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121020, 121020, 21020, 20, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170021, 0.0, 18.25, 0.0)
    ops.node(121021, 0.0, 18.25, 2.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 21, 170021, 121021, 0.09, 26589646.42101824, 11079019.34209093, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20021, 42.13247951, 0.00070107, 51.19054629, 0.02535863, 5.11905463, 0.07568474, -42.13247951, -0.00070107, -51.19054629, -0.02535863, -5.11905463, -0.07568474, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10021, 47.84157982, 0.00070107, 58.12704675, 0.02535863, 5.81270467, 0.07568474, -47.84157982, -0.00070107, -58.12704675, -0.02535863, -5.81270467, -0.07568474, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20021, 21, 0.0, 89.41592289, 0.01402137, 89.41592289, 0.0420641, 62.59114602, -1227.85999842, 0.05, 2, 0, 70021, 21021, 2, 3)
    ops.uniaxialMaterial('LimitState', 40021, 22.35398072, 7.667e-05, 67.06194217, 0.00023002, 223.53980722, 0.00076672, -22.35398072, -7.667e-05, -67.06194217, -0.00023002, -223.53980722, -0.00076672, 0.4, 0.3, 0.003, 0.0, 0.0, 20021, 2)
    ops.limitCurve('ThreePoint', 10021, 21, 0.0, 89.41592289, 0.01402137, 89.41592289, 0.0420641, 62.59114602, -1227.85999842, 0.05, 2, 0, 70021, 21021, 1, 3)
    ops.uniaxialMaterial('LimitState', 30021, 22.35398072, 7.667e-05, 67.06194217, 0.00023002, 223.53980722, 0.00076672, -22.35398072, -7.667e-05, -67.06194217, -0.00023002, -223.53980722, -0.00076672, 0.4, 0.3, 0.003, 0.0, 0.0, 10021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 21, 99999, 'P', 40021, 'Vy', 30021, 'Vz', 20021, 'My', 10021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170021, 70021, 170021, 21, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121021, 121021, 21021, 21, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170022, 2.95, 18.25, 0.0)
    ops.node(121022, 2.95, 18.25, 2.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 22, 170022, 121022, 0.16, 27747346.85397518, 11561394.52248966, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20022, 154.42601086, 0.00060565, 187.10802554, 0.04348342, 18.71080255, 0.11404532, -154.42601086, -0.00060565, -187.10802554, -0.04348342, -18.71080255, -0.11404532, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10022, 159.03915491, 0.00060565, 192.6974743, 0.04348342, 19.26974743, 0.11404532, -159.03915491, -0.00060565, -192.6974743, -0.04348342, -19.26974743, -0.11404532, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20022, 22, 0.0, 201.45909521, 0.01211298, 201.45909521, 0.03633893, 141.02136665, -3459.95511984, 0.05, 2, 0, 70022, 21022, 2, 3)
    ops.uniaxialMaterial('LimitState', 40022, 50.3647738, 9.312e-05, 151.09432141, 0.00027935, 503.64773803, 0.00093116, -50.3647738, -9.312e-05, -151.09432141, -0.00027935, -503.64773803, -0.00093116, 0.4, 0.3, 0.003, 0.0, 0.0, 20022, 2)
    ops.limitCurve('ThreePoint', 10022, 22, 0.0, 201.45909521, 0.01211298, 201.45909521, 0.03633893, 141.02136665, -3459.95511984, 0.05, 2, 0, 70022, 21022, 1, 3)
    ops.uniaxialMaterial('LimitState', 30022, 50.3647738, 9.312e-05, 151.09432141, 0.00027935, 503.64773803, 0.00093116, -50.3647738, -9.312e-05, -151.09432141, -0.00027935, -503.64773803, -0.00093116, 0.4, 0.3, 0.003, 0.0, 0.0, 10022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 22, 99999, 'P', 40022, 'Vy', 30022, 'Vz', 20022, 'My', 10022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170022, 70022, 170022, 22, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121022, 121022, 21022, 22, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170023, 9.6, 18.25, 0.0)
    ops.node(121023, 9.6, 18.25, 2.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 23, 170023, 121023, 0.2025, 26506509.15412935, 11044378.81422056, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20023, 210.21933083, 0.00056517, 254.77990496, 0.04054244, 25.4779905, 0.0995351, -210.21933083, -0.00056517, -254.77990496, -0.04054244, -25.4779905, -0.0995351, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10023, 215.64995883, 0.00056517, 261.36167305, 0.04054244, 26.1361673, 0.0995351, -215.64995883, -0.00056517, -261.36167305, -0.04054244, -26.1361673, -0.0995351, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20023, 23, 0.0, 236.8833012, 0.01130344, 236.8833012, 0.03391032, 165.81831084, -3756.85669664, 0.05, 2, 0, 70023, 21023, 2, 3)
    ops.uniaxialMaterial('LimitState', 40023, 59.2208253, 9.056e-05, 177.6624759, 0.00027168, 592.208253, 0.0009056, -59.2208253, -9.056e-05, -177.6624759, -0.00027168, -592.208253, -0.0009056, 0.4, 0.3, 0.003, 0.0, 0.0, 20023, 2)
    ops.limitCurve('ThreePoint', 10023, 23, 0.0, 236.8833012, 0.01130344, 236.8833012, 0.03391032, 165.81831084, -3756.85669664, 0.05, 2, 0, 70023, 21023, 1, 3)
    ops.uniaxialMaterial('LimitState', 30023, 59.2208253, 9.056e-05, 177.6624759, 0.00027168, 592.208253, 0.0009056, -59.2208253, -9.056e-05, -177.6624759, -0.00027168, -592.208253, -0.0009056, 0.4, 0.3, 0.003, 0.0, 0.0, 10023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 23, 99999, 'P', 40023, 'Vy', 30023, 'Vz', 20023, 'My', 10023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170023, 70023, 170023, 23, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121023, 121023, 21023, 23, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170024, 16.25, 18.25, 0.0)
    ops.node(121024, 16.25, 18.25, 2.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 24, 170024, 121024, 0.16, 27586072.2657209, 11494196.77738371, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20024, 114.70732029, 0.00059433, 139.12097606, 0.04336938, 13.91209761, 0.11519525, -114.70732029, -0.00059433, -139.12097606, -0.04336938, -13.91209761, -0.11519525, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10024, 122.60415267, 0.00059433, 148.69852548, 0.04336938, 14.86985255, 0.11519525, -122.60415267, -0.00059433, -148.69852548, -0.04336938, -14.86985255, -0.11519525, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20024, 24, 0.0, 202.27237534, 0.01188662, 202.27237534, 0.03565986, 141.59066274, -3678.07925064, 0.05, 2, 0, 70024, 21024, 2, 3)
    ops.uniaxialMaterial('LimitState', 40024, 50.56809384, 9.404e-05, 151.70428151, 0.00028211, 505.68093835, 0.00094038, -50.56809384, -9.404e-05, -151.70428151, -0.00028211, -505.68093835, -0.00094038, 0.4, 0.3, 0.003, 0.0, 0.0, 20024, 2)
    ops.limitCurve('ThreePoint', 10024, 24, 0.0, 202.27237534, 0.01188662, 202.27237534, 0.03565986, 141.59066274, -3678.07925064, 0.05, 2, 0, 70024, 21024, 1, 3)
    ops.uniaxialMaterial('LimitState', 30024, 50.56809384, 9.404e-05, 151.70428151, 0.00028211, 505.68093835, 0.00094038, -50.56809384, -9.404e-05, -151.70428151, -0.00028211, -505.68093835, -0.00094038, 0.4, 0.3, 0.003, 0.0, 0.0, 10024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 24, 99999, 'P', 40024, 'Vy', 30024, 'Vz', 20024, 'My', 10024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170024, 70024, 170024, 24, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121024, 121024, 21024, 24, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170025, 0.0, 21.9, 0.0)
    ops.node(121025, 0.0, 21.9, 2.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 25, 170025, 121025, 0.0625, 26674244.54409361, 11114268.560039, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20025, 21.44511623, 0.00077364, 26.08960606, 0.02186168, 2.60896061, 0.07278186, -21.44511623, -0.00077364, -26.08960606, -0.02186168, -2.60896061, -0.07278186, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10025, 21.44511623, 0.00077364, 26.08960606, 0.02186168, 2.60896061, 0.07278186, -21.44511623, -0.00077364, -26.08960606, -0.02186168, -2.60896061, -0.07278186, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20025, 25, 0.0, 60.23519649, 0.0154728, 60.23519649, 0.04641841, 42.16463755, -832.81588013, 0.05, 2, 0, 70025, 21025, 2, 3)
    ops.uniaxialMaterial('LimitState', 40025, 15.05879912, 7.414e-05, 45.17639737, 0.00022242, 150.58799123, 0.00074141, -15.05879912, -7.414e-05, -45.17639737, -0.00022242, -150.58799123, -0.00074141, 0.4, 0.3, 0.003, 0.0, 0.0, 20025, 2)
    ops.limitCurve('ThreePoint', 10025, 25, 0.0, 60.23519649, 0.0154728, 60.23519649, 0.04641841, 42.16463755, -832.81588013, 0.05, 2, 0, 70025, 21025, 1, 3)
    ops.uniaxialMaterial('LimitState', 30025, 15.05879912, 7.414e-05, 45.17639737, 0.00022242, 150.58799123, 0.00074141, -15.05879912, -7.414e-05, -45.17639737, -0.00022242, -150.58799123, -0.00074141, 0.4, 0.3, 0.003, 0.0, 0.0, 10025, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 25, 99999, 'P', 40025, 'Vy', 30025, 'Vz', 20025, 'My', 10025, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170025, 70025, 170025, 25, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121025, 121025, 21025, 25, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170026, 2.95, 21.9, 0.0)
    ops.node(121026, 2.95, 21.9, 2.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 26, 170026, 121026, 0.1225, 26803919.79636461, 11168299.91515192, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20026, 82.55614505, 0.00062567, 100.17519527, 0.03114204, 10.01751953, 0.08592636, -82.55614505, -0.00062567, -100.17519527, -0.03114204, -10.01751953, -0.08592636, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10026, 86.46797673, 0.00062567, 104.92188617, 0.03114204, 10.49218862, 0.08592636, -86.46797673, -0.00062567, -104.92188617, -0.03114204, -10.49218862, -0.08592636, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20026, 26, 0.0, 132.00728211, 0.01251348, 132.00728211, 0.03754045, 92.40509748, -1943.18030871, 0.05, 2, 0, 70026, 21026, 2, 3)
    ops.uniaxialMaterial('LimitState', 40026, 33.00182053, 8.25e-05, 99.00546158, 0.00024749, 330.01820527, 0.00082498, -33.00182053, -8.25e-05, -99.00546158, -0.00024749, -330.01820527, -0.00082498, 0.4, 0.3, 0.003, 0.0, 0.0, 20026, 2)
    ops.limitCurve('ThreePoint', 10026, 26, 0.0, 132.00728211, 0.01251348, 132.00728211, 0.03754045, 92.40509748, -1943.18030871, 0.05, 2, 0, 70026, 21026, 1, 3)
    ops.uniaxialMaterial('LimitState', 30026, 33.00182053, 8.25e-05, 99.00546158, 0.00024749, 330.01820527, 0.00082498, -33.00182053, -8.25e-05, -99.00546158, -0.00024749, -330.01820527, -0.00082498, 0.4, 0.3, 0.003, 0.0, 0.0, 10026, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 26, 99999, 'P', 40026, 'Vy', 30026, 'Vz', 20026, 'My', 10026, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170026, 70026, 170026, 26, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121026, 121026, 21026, 26, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170027, 9.6, 21.9, 0.0)
    ops.node(121027, 9.6, 21.9, 2.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 27, 170027, 121027, 0.16, 27940958.63968185, 11642066.09986744, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20027, 124.05983154, 0.00058845, 150.27990635, 0.03971127, 15.02799064, 0.11078821, -124.05983154, -0.00058845, -150.27990635, -0.03971127, -15.02799064, -0.11078821, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10027, 128.46679584, 0.00058845, 155.6182836, 0.03971127, 15.56182836, 0.11078821, -128.46679584, -0.00058845, -155.6182836, -0.03971127, -15.56182836, -0.11078821, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20027, 27, 0.0, 204.481038, 0.01176891, 204.481038, 0.03530673, 143.1367266, -3550.63017136, 0.05, 2, 0, 70027, 21027, 2, 3)
    ops.uniaxialMaterial('LimitState', 40027, 51.1202595, 9.386e-05, 153.3607785, 0.00028157, 511.202595, 0.00093858, -51.1202595, -9.386e-05, -153.3607785, -0.00028157, -511.202595, -0.00093858, 0.4, 0.3, 0.003, 0.0, 0.0, 20027, 2)
    ops.limitCurve('ThreePoint', 10027, 27, 0.0, 204.481038, 0.01176891, 204.481038, 0.03530673, 143.1367266, -3550.63017136, 0.05, 2, 0, 70027, 21027, 1, 3)
    ops.uniaxialMaterial('LimitState', 30027, 51.1202595, 9.386e-05, 153.3607785, 0.00028157, 511.202595, 0.00093858, -51.1202595, -9.386e-05, -153.3607785, -0.00028157, -511.202595, -0.00093858, 0.4, 0.3, 0.003, 0.0, 0.0, 10027, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 27, 99999, 'P', 40027, 'Vy', 30027, 'Vz', 20027, 'My', 10027, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170027, 70027, 170027, 27, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121027, 121027, 21027, 27, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170028, 16.25, 21.9, 0.0)
    ops.node(121028, 16.25, 21.9, 2.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 28, 170028, 121028, 0.09, 27117638.0203096, 11299015.84179567, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20028, 47.3585848, 0.00070983, 57.4171648, 0.0278992, 5.74171648, 0.07683566, -47.3585848, -0.00070983, -57.4171648, -0.0278992, -5.74171648, -0.07683566, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10028, 47.3585848, 0.00070983, 57.4171648, 0.0278992, 5.74171648, 0.07683566, -47.3585848, -0.00070983, -57.4171648, -0.0278992, -5.74171648, -0.07683566, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20028, 28, 0.0, 92.97360687, 0.01419661, 92.97360687, 0.04258984, 65.08152481, -1226.91687802, 0.05, 2, 0, 70028, 21028, 2, 3)
    ops.uniaxialMaterial('LimitState', 40028, 23.24340172, 7.817e-05, 69.73020515, 0.00023451, 232.43401717, 0.0007817, -23.24340172, -7.817e-05, -69.73020515, -0.00023451, -232.43401717, -0.0007817, 0.4, 0.3, 0.003, 0.0, 0.0, 20028, 2)
    ops.limitCurve('ThreePoint', 10028, 28, 0.0, 92.97360687, 0.01419661, 92.97360687, 0.04258984, 65.08152481, -1226.91687802, 0.05, 2, 0, 70028, 21028, 1, 3)
    ops.uniaxialMaterial('LimitState', 30028, 23.24340172, 7.817e-05, 69.73020515, 0.00023451, 232.43401717, 0.0007817, -23.24340172, -7.817e-05, -69.73020515, -0.00023451, -232.43401717, -0.0007817, 0.4, 0.3, 0.003, 0.0, 0.0, 10028, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 28, 99999, 'P', 40028, 'Vy', 30028, 'Vz', 20028, 'My', 10028, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170028, 70028, 170028, 28, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121028, 121028, 21028, 28, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171003, 9.6, 0.0, 3.15)
    ops.node(122003, 9.6, 0.0, 5.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1003, 171003, 122003, 0.16, 26721209.98199302, 11133837.49249709, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21003, 88.37139566, 0.00056198, 107.54428644, 0.02312614, 10.75442864, 0.06568989, -88.37139566, -0.00056198, -107.54428644, -0.02312614, -10.75442864, -0.06568989, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11003, 76.09697214, 0.00056198, 92.60682722, 0.02312614, 9.26068272, 0.06568989, -76.09697214, -0.00056198, -92.60682722, -0.02312614, -9.26068272, -0.06568989, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21003, 1003, 0.0, 139.9439921, 0.01123954, 139.9439921, 0.03371863, 97.96079447, -1635.84745904, 0.05, 2, 0, 71003, 22003, 2, 3)
    ops.uniaxialMaterial('LimitState', 41003, 34.98599802, 6.717e-05, 104.95799407, 0.0002015, 349.85998025, 0.00067167, -34.98599802, -6.717e-05, -104.95799407, -0.0002015, -349.85998025, -0.00067167, 0.4, 0.3, 0.003, 0.0, 0.0, 21003, 2)
    ops.limitCurve('ThreePoint', 11003, 1003, 0.0, 139.9439921, 0.01123954, 139.9439921, 0.03371863, 97.96079447, -1635.84745904, 0.05, 2, 0, 71003, 22003, 1, 3)
    ops.uniaxialMaterial('LimitState', 31003, 34.98599802, 6.717e-05, 104.95799407, 0.0002015, 349.85998025, 0.00067167, -34.98599802, -6.717e-05, -104.95799407, -0.0002015, -349.85998025, -0.00067167, 0.4, 0.3, 0.003, 0.0, 0.0, 11003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1003, 99999, 'P', 41003, 'Vy', 31003, 'Vz', 21003, 'My', 11003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171003, 71003, 171003, 1003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122003, 122003, 22003, 1003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171004, 16.25, 0.0, 3.15)
    ops.node(122004, 16.25, 0.0, 5.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1004, 171004, 122004, 0.09, 27102092.29440457, 11292538.4560019, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21004, 55.68750715, 0.00070252, 67.74028995, 0.03785315, 6.77402899, 0.10638069, -55.68750715, -0.00070252, -67.74028995, -0.03785315, -6.77402899, -0.10638069, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11004, 49.86949315, 0.00070252, 60.66304811, 0.03785315, 6.06630481, 0.10638069, -49.86949315, -0.00070252, -60.66304811, -0.03785315, -6.06630481, -0.10638069, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21004, 1004, 0.0, 102.9040094, 0.01405038, 102.9040094, 0.04215114, 72.03280658, -1907.15674134, 0.05, 2, 0, 71004, 22004, 2, 3)
    ops.uniaxialMaterial('LimitState', 41004, 25.72600235, 8.657e-05, 77.17800705, 0.00025971, 257.2600235, 0.00086569, -25.72600235, -8.657e-05, -77.17800705, -0.00025971, -257.2600235, -0.00086569, 0.4, 0.3, 0.003, 0.0, 0.0, 21004, 2)
    ops.limitCurve('ThreePoint', 11004, 1004, 0.0, 102.9040094, 0.01405038, 102.9040094, 0.04215114, 72.03280658, -1907.15674134, 0.05, 2, 0, 71004, 22004, 1, 3)
    ops.uniaxialMaterial('LimitState', 31004, 25.72600235, 8.657e-05, 77.17800705, 0.00025971, 257.2600235, 0.00086569, -25.72600235, -8.657e-05, -77.17800705, -0.00025971, -257.2600235, -0.00086569, 0.4, 0.3, 0.003, 0.0, 0.0, 11004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1004, 99999, 'P', 41004, 'Vy', 31004, 'Vz', 21004, 'My', 11004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171004, 71004, 171004, 1004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122004, 122004, 22004, 1004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171005, 0.0, 3.65, 3.1)
    ops.node(122005, 0.0, 3.65, 5.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1005, 171005, 122005, 0.09, 27417240.48656357, 11423850.20273482, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21005, 36.0892115, 0.00067101, 43.86512327, 0.02538076, 4.38651233, 0.07927427, -36.0892115, -0.00067101, -43.86512327, -0.02538076, -4.38651233, -0.07927427, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11005, 38.94323561, 0.00067101, 47.33408571, 0.02538076, 4.73340857, 0.07927427, -38.94323561, -0.00067101, -47.33408571, -0.02538076, -4.73340857, -0.07927427, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21005, 1005, 0.0, 90.57626469, 0.01342014, 90.57626469, 0.04026041, 63.40338529, -1275.747646, 0.05, 2, 0, 71005, 22005, 2, 3)
    ops.uniaxialMaterial('LimitState', 41005, 22.64406617, 7.532e-05, 67.93219852, 0.00022597, 226.44066173, 0.00075323, -22.64406617, -7.532e-05, -67.93219852, -0.00022597, -226.44066173, -0.00075323, 0.4, 0.3, 0.003, 0.0, 0.0, 21005, 2)
    ops.limitCurve('ThreePoint', 11005, 1005, 0.0, 90.57626469, 0.01342014, 90.57626469, 0.04026041, 63.40338529, -1275.747646, 0.05, 2, 0, 71005, 22005, 1, 3)
    ops.uniaxialMaterial('LimitState', 31005, 22.64406617, 7.532e-05, 67.93219852, 0.00022597, 226.44066173, 0.00075323, -22.64406617, -7.532e-05, -67.93219852, -0.00022597, -226.44066173, -0.00075323, 0.4, 0.3, 0.003, 0.0, 0.0, 11005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1005, 99999, 'P', 41005, 'Vy', 31005, 'Vz', 21005, 'My', 11005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171005, 71005, 171005, 1005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122005, 122005, 22005, 1005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171006, 2.95, 3.65, 3.1)
    ops.node(122006, 2.95, 3.65, 5.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1006, 171006, 122006, 0.16, 27669223.57413147, 11528843.15588811, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21006, 109.27017261, 0.00057554, 132.6596055, 0.04179688, 13.26596055, 0.11624997, -109.27017261, -0.00057554, -132.6596055, -0.04179688, -13.26596055, -0.11624997, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11006, 96.42569898, 0.00057554, 117.06575437, 0.04179688, 11.70657544, 0.11624997, -96.42569898, -0.00057554, -117.06575437, -0.04179688, -11.70657544, -0.11624997, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21006, 1006, 0.0, 196.1409253, 0.01151074, 196.1409253, 0.03453222, 137.29864771, -3616.71213124, 0.05, 2, 0, 71006, 22006, 2, 3)
    ops.uniaxialMaterial('LimitState', 41006, 49.03523132, 9.091e-05, 147.10569397, 0.00027274, 490.35231325, 0.00090914, -49.03523132, -9.091e-05, -147.10569397, -0.00027274, -490.35231325, -0.00090914, 0.4, 0.3, 0.003, 0.0, 0.0, 21006, 2)
    ops.limitCurve('ThreePoint', 11006, 1006, 0.0, 196.1409253, 0.01151074, 196.1409253, 0.03453222, 137.29864771, -3616.71213124, 0.05, 2, 0, 71006, 22006, 1, 3)
    ops.uniaxialMaterial('LimitState', 31006, 49.03523132, 9.091e-05, 147.10569397, 0.00027274, 490.35231325, 0.00090914, -49.03523132, -9.091e-05, -147.10569397, -0.00027274, -490.35231325, -0.00090914, 0.4, 0.3, 0.003, 0.0, 0.0, 11006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1006, 99999, 'P', 41006, 'Vy', 31006, 'Vz', 21006, 'My', 11006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171006, 71006, 171006, 1006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122006, 122006, 22006, 1006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171007, 9.6, 3.65, 3.1)
    ops.node(122007, 9.6, 3.65, 5.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1007, 171007, 122007, 0.2025, 27049902.24789109, 11270792.60328796, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21007, 136.09093187, 0.00055235, 165.43141488, 0.0310371, 16.54314149, 0.07901433, -136.09093187, -0.00055235, -165.43141488, -0.0310371, -16.54314149, -0.07901433, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11007, 121.28662957, 0.00055235, 147.43538353, 0.0310371, 14.74353835, 0.07901433, -121.28662957, -0.00055235, -147.43538353, -0.0310371, -14.74353835, -0.07901433, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21007, 1007, 0.0, 194.56925472, 0.01104695, 194.56925472, 0.03314086, 136.1984783, -2496.93439882, 0.05, 2, 0, 71007, 22007, 2, 3)
    ops.uniaxialMaterial('LimitState', 41007, 48.64231368, 7.289e-05, 145.92694104, 0.00021867, 486.4231368, 0.00072889, -48.64231368, -7.289e-05, -145.92694104, -0.00021867, -486.4231368, -0.00072889, 0.4, 0.3, 0.003, 0.0, 0.0, 21007, 2)
    ops.limitCurve('ThreePoint', 11007, 1007, 0.0, 194.56925472, 0.01104695, 194.56925472, 0.03314086, 136.1984783, -2496.93439882, 0.05, 2, 0, 71007, 22007, 1, 3)
    ops.uniaxialMaterial('LimitState', 31007, 48.64231368, 7.289e-05, 145.92694104, 0.00021867, 486.4231368, 0.00072889, -48.64231368, -7.289e-05, -145.92694104, -0.00021867, -486.4231368, -0.00072889, 0.4, 0.3, 0.003, 0.0, 0.0, 11007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1007, 99999, 'P', 41007, 'Vy', 31007, 'Vz', 21007, 'My', 11007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171007, 71007, 171007, 1007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122007, 122007, 22007, 1007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171008, 16.25, 3.65, 3.1)
    ops.node(122008, 16.25, 3.65, 5.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1008, 171008, 122008, 0.16, 28037197.21121729, 11682165.50467387, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21008, 110.56292019, 0.00057841, 134.37344008, 0.04501406, 13.43734401, 0.12400978, -110.56292019, -0.00057841, -134.37344008, -0.04501406, -13.43734401, -0.12400978, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11008, 102.922925, 0.00057841, 125.08811699, 0.04501406, 12.5088117, 0.12400978, -102.922925, -0.00057841, -125.08811699, -0.04501406, -12.5088117, -0.12400978, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21008, 1008, 0.0, 193.99336314, 0.01156822, 193.99336314, 0.03470465, 135.7953542, -3904.104515, 0.05, 2, 0, 71008, 22008, 2, 3)
    ops.uniaxialMaterial('LimitState', 41008, 48.49834079, 8.874e-05, 145.49502236, 0.00026621, 484.98340786, 0.00088738, -48.49834079, -8.874e-05, -145.49502236, -0.00026621, -484.98340786, -0.00088738, 0.4, 0.3, 0.003, 0.0, 0.0, 21008, 2)
    ops.limitCurve('ThreePoint', 11008, 1008, 0.0, 193.99336314, 0.01156822, 193.99336314, 0.03470465, 135.7953542, -3904.104515, 0.05, 2, 0, 71008, 22008, 1, 3)
    ops.uniaxialMaterial('LimitState', 31008, 48.49834079, 8.874e-05, 145.49502236, 0.00026621, 484.98340786, 0.00088738, -48.49834079, -8.874e-05, -145.49502236, -0.00026621, -484.98340786, -0.00088738, 0.4, 0.3, 0.003, 0.0, 0.0, 11008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1008, 99999, 'P', 41008, 'Vy', 31008, 'Vz', 21008, 'My', 11008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171008, 71008, 171008, 1008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122008, 122008, 22008, 1008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171009, 0.0, 7.3, 3.1)
    ops.node(122009, 0.0, 7.3, 5.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1009, 171009, 122009, 0.09, 27701102.23286538, 11542125.93036058, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21009, 33.52242942, 0.00065898, 40.78658257, 0.02606225, 4.07865826, 0.08275555, -33.52242942, -0.00065898, -40.78658257, -0.02606225, -4.07865826, -0.08275555, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11009, 36.33370884, 0.00065898, 44.20705304, 0.02606225, 4.4207053, 0.08275555, -36.33370884, -0.00065898, -44.20705304, -0.02606225, -4.4207053, -0.08275555, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21009, 1009, 0.0, 89.13314229, 0.01317955, 89.13314229, 0.03953864, 62.3931996, -1319.56373934, 0.05, 2, 0, 71009, 22009, 2, 3)
    ops.uniaxialMaterial('LimitState', 41009, 22.28328557, 7.336e-05, 66.84985672, 0.00022009, 222.83285572, 0.00073363, -22.28328557, -7.336e-05, -66.84985672, -0.00022009, -222.83285572, -0.00073363, 0.4, 0.3, 0.003, 0.0, 0.0, 21009, 2)
    ops.limitCurve('ThreePoint', 11009, 1009, 0.0, 89.13314229, 0.01317955, 89.13314229, 0.03953864, 62.3931996, -1319.56373934, 0.05, 2, 0, 71009, 22009, 1, 3)
    ops.uniaxialMaterial('LimitState', 31009, 22.28328557, 7.336e-05, 66.84985672, 0.00022009, 222.83285572, 0.00073363, -22.28328557, -7.336e-05, -66.84985672, -0.00022009, -222.83285572, -0.00073363, 0.4, 0.3, 0.003, 0.0, 0.0, 11009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1009, 99999, 'P', 41009, 'Vy', 31009, 'Vz', 21009, 'My', 11009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171009, 71009, 171009, 1009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122009, 122009, 22009, 1009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171010, 2.95, 7.3, 3.1)
    ops.node(122010, 2.95, 7.3, 5.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1010, 171010, 122010, 0.16, 27747327.30093216, 11561386.3753884, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21010, 96.65290138, 0.00056619, 117.44545827, 0.04201838, 11.74454583, 0.11889817, -96.65290138, -0.00056619, -117.44545827, -0.04201838, -11.74454583, -0.11889817, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11010, 87.8728305, 0.00056619, 106.77656542, 0.04201838, 10.67765654, 0.11889817, -87.8728305, -0.00056619, -106.77656542, -0.04201838, -10.67765654, -0.11889817, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21010, 1010, 0.0, 197.16547795, 0.01132386, 197.16547795, 0.03397157, 138.01583456, -3925.50822037, 0.05, 2, 0, 71010, 22010, 2, 3)
    ops.uniaxialMaterial('LimitState', 41010, 49.29136949, 9.113e-05, 147.87410846, 0.00027339, 492.91369487, 0.00091131, -49.29136949, -9.113e-05, -147.87410846, -0.00027339, -492.91369487, -0.00091131, 0.4, 0.3, 0.003, 0.0, 0.0, 21010, 2)
    ops.limitCurve('ThreePoint', 11010, 1010, 0.0, 197.16547795, 0.01132386, 197.16547795, 0.03397157, 138.01583456, -3925.50822037, 0.05, 2, 0, 71010, 22010, 1, 3)
    ops.uniaxialMaterial('LimitState', 31010, 49.29136949, 9.113e-05, 147.87410846, 0.00027339, 492.91369487, 0.00091131, -49.29136949, -9.113e-05, -147.87410846, -0.00027339, -492.91369487, -0.00091131, 0.4, 0.3, 0.003, 0.0, 0.0, 11010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1010, 99999, 'P', 41010, 'Vy', 31010, 'Vz', 21010, 'My', 11010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171010, 71010, 171010, 1010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122010, 122010, 22010, 1010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171011, 9.6, 7.3, 3.1)
    ops.node(122011, 9.6, 7.3, 5.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1011, 171011, 122011, 0.2025, 27498264.73159692, 11457610.30483205, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21011, 134.43852853, 0.00054391, 163.32947136, 0.03139899, 16.33294714, 0.08007754, -134.43852853, -0.00054391, -163.32947136, -0.03139899, -16.33294714, -0.08007754, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11011, 119.98163788, 0.00054391, 145.76578383, 0.03139899, 14.57657838, 0.08007754, -119.98163788, -0.00054391, -145.76578383, -0.03139899, -14.57657838, -0.08007754, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21011, 1011, 0.0, 200.04402008, 0.01087817, 200.04402008, 0.03263451, 140.03081405, -2602.24296836, 0.05, 2, 0, 71011, 22011, 2, 3)
    ops.uniaxialMaterial('LimitState', 41011, 50.01100502, 7.372e-05, 150.03301506, 0.00022115, 500.11005019, 0.00073718, -50.01100502, -7.372e-05, -150.03301506, -0.00022115, -500.11005019, -0.00073718, 0.4, 0.3, 0.003, 0.0, 0.0, 21011, 2)
    ops.limitCurve('ThreePoint', 11011, 1011, 0.0, 200.04402008, 0.01087817, 200.04402008, 0.03263451, 140.03081405, -2602.24296836, 0.05, 2, 0, 71011, 22011, 1, 3)
    ops.uniaxialMaterial('LimitState', 31011, 50.01100502, 7.372e-05, 150.03301506, 0.00022115, 500.11005019, 0.00073718, -50.01100502, -7.372e-05, -150.03301506, -0.00022115, -500.11005019, -0.00073718, 0.4, 0.3, 0.003, 0.0, 0.0, 11011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1011, 99999, 'P', 41011, 'Vy', 31011, 'Vz', 21011, 'My', 11011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171011, 71011, 171011, 1011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122011, 122011, 22011, 1011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171012, 16.25, 7.3, 3.1)
    ops.node(122012, 16.25, 7.3, 5.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1012, 171012, 122012, 0.16, 28426418.45423739, 11844341.02259891, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21012, 109.22805257, 0.00058665, 132.6603899, 0.04500237, 13.26603899, 0.12473569, -109.22805257, -0.00058665, -132.6603899, -0.04500237, -13.26603899, -0.12473569, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11012, 101.99712396, 0.00058665, 123.87823379, 0.04500237, 12.38782338, 0.12473569, -101.99712396, -0.00058665, -123.87823379, -0.04500237, -12.38782338, -0.12473569, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21012, 1012, 0.0, 196.68173851, 0.011733, 196.68173851, 0.03519901, 137.67721695, -3953.33059817, 0.05, 2, 0, 71012, 22012, 2, 3)
    ops.uniaxialMaterial('LimitState', 41012, 49.17043463, 8.874e-05, 147.51130388, 0.00026621, 491.70434626, 0.00088736, -49.17043463, -8.874e-05, -147.51130388, -0.00026621, -491.70434626, -0.00088736, 0.4, 0.3, 0.003, 0.0, 0.0, 21012, 2)
    ops.limitCurve('ThreePoint', 11012, 1012, 0.0, 196.68173851, 0.011733, 196.68173851, 0.03519901, 137.67721695, -3953.33059817, 0.05, 2, 0, 71012, 22012, 1, 3)
    ops.uniaxialMaterial('LimitState', 31012, 49.17043463, 8.874e-05, 147.51130388, 0.00026621, 491.70434626, 0.00088736, -49.17043463, -8.874e-05, -147.51130388, -0.00026621, -491.70434626, -0.00088736, 0.4, 0.3, 0.003, 0.0, 0.0, 11012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1012, 99999, 'P', 41012, 'Vy', 31012, 'Vz', 21012, 'My', 11012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171012, 71012, 171012, 1012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122012, 122012, 22012, 1012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171013, 0.0, 10.95, 3.1)
    ops.node(122013, 0.0, 10.95, 5.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1013, 171013, 122013, 0.09, 27904915.06573193, 11627047.94405497, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21013, 33.39006199, 0.00065472, 40.61164953, 0.02651773, 4.06116495, 0.08348399, -33.39006199, -0.00065472, -40.61164953, -0.02651773, -4.06116495, -0.08348399, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11013, 36.17949327, 0.00065472, 44.00437775, 0.02651773, 4.40043777, 0.08348399, -36.17949327, -0.00065472, -44.00437775, -0.02651773, -4.40043777, -0.08348399, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21013, 1013, 0.0, 90.93472119, 0.01309438, 90.93472119, 0.03928314, 63.65430483, -1377.38227236, 0.05, 2, 0, 71013, 22013, 2, 3)
    ops.uniaxialMaterial('LimitState', 41013, 22.7336803, 7.43e-05, 68.20104089, 0.0002229, 227.33680297, 0.00074299, -22.7336803, -7.43e-05, -68.20104089, -0.0002229, -227.33680297, -0.00074299, 0.4, 0.3, 0.003, 0.0, 0.0, 21013, 2)
    ops.limitCurve('ThreePoint', 11013, 1013, 0.0, 90.93472119, 0.01309438, 90.93472119, 0.03928314, 63.65430483, -1377.38227236, 0.05, 2, 0, 71013, 22013, 1, 3)
    ops.uniaxialMaterial('LimitState', 31013, 22.7336803, 7.43e-05, 68.20104089, 0.0002229, 227.33680297, 0.00074299, -22.7336803, -7.43e-05, -68.20104089, -0.0002229, -227.33680297, -0.00074299, 0.4, 0.3, 0.003, 0.0, 0.0, 11013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1013, 99999, 'P', 41013, 'Vy', 31013, 'Vz', 21013, 'My', 11013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171013, 71013, 171013, 1013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122013, 122013, 22013, 1013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171014, 2.95, 10.95, 3.1)
    ops.node(122014, 2.95, 10.95, 5.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1014, 171014, 122014, 0.16, 26928738.82379294, 11220307.84324706, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21014, 95.18143557, 0.0005754, 115.78680161, 0.04201614, 11.57868016, 0.11703001, -95.18143557, -0.0005754, -115.78680161, -0.04201614, -11.57868016, -0.11703001, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11014, 86.79497372, 0.0005754, 105.58479543, 0.04201614, 10.55847954, 0.11703001, -86.79497372, -0.0005754, -105.58479543, -0.04201614, -10.55847954, -0.11703001, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21014, 1014, 0.0, 190.44940899, 0.0115079, 190.44940899, 0.03452371, 133.31458629, -3768.4301149, 0.05, 2, 0, 71014, 22014, 2, 3)
    ops.uniaxialMaterial('LimitState', 41014, 47.61235225, 9.07e-05, 142.83705674, 0.00027211, 476.12352248, 0.00090703, -47.61235225, -9.07e-05, -142.83705674, -0.00027211, -476.12352248, -0.00090703, 0.4, 0.3, 0.003, 0.0, 0.0, 21014, 2)
    ops.limitCurve('ThreePoint', 11014, 1014, 0.0, 190.44940899, 0.0115079, 190.44940899, 0.03452371, 133.31458629, -3768.4301149, 0.05, 2, 0, 71014, 22014, 1, 3)
    ops.uniaxialMaterial('LimitState', 31014, 47.61235225, 9.07e-05, 142.83705674, 0.00027211, 476.12352248, 0.00090703, -47.61235225, -9.07e-05, -142.83705674, -0.00027211, -476.12352248, -0.00090703, 0.4, 0.3, 0.003, 0.0, 0.0, 11014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1014, 99999, 'P', 41014, 'Vy', 31014, 'Vz', 21014, 'My', 11014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171014, 71014, 171014, 1014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122014, 122014, 22014, 1014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171015, 9.6, 10.95, 3.1)
    ops.node(122015, 9.6, 10.95, 5.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1015, 171015, 122015, 0.2025, 28178032.43047657, 11740846.84603191, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21015, 135.1056167, 0.00053495, 163.97476007, 0.03143849, 16.39747601, 0.0811074, -135.1056167, -0.00053495, -163.97476007, -0.03143849, -16.39747601, -0.0811074, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11015, 120.3115496, 0.00053495, 146.01952133, 0.03143849, 14.60195213, 0.0811074, -120.3115496, -0.00053495, -146.01952133, -0.03143849, -14.60195213, -0.0811074, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21015, 1015, 0.0, 203.80010423, 0.01069894, 203.80010423, 0.03209683, 142.66007296, -2592.16412001, 0.05, 2, 0, 71015, 22015, 2, 3)
    ops.uniaxialMaterial('LimitState', 41015, 50.95002606, 7.329e-05, 152.85007817, 0.00021987, 509.50026057, 0.0007329, -50.95002606, -7.329e-05, -152.85007817, -0.00021987, -509.50026057, -0.0007329, 0.4, 0.3, 0.003, 0.0, 0.0, 21015, 2)
    ops.limitCurve('ThreePoint', 11015, 1015, 0.0, 203.80010423, 0.01069894, 203.80010423, 0.03209683, 142.66007296, -2592.16412001, 0.05, 2, 0, 71015, 22015, 1, 3)
    ops.uniaxialMaterial('LimitState', 31015, 50.95002606, 7.329e-05, 152.85007817, 0.00021987, 509.50026057, 0.0007329, -50.95002606, -7.329e-05, -152.85007817, -0.00021987, -509.50026057, -0.0007329, 0.4, 0.3, 0.003, 0.0, 0.0, 11015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1015, 99999, 'P', 41015, 'Vy', 31015, 'Vz', 21015, 'My', 11015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171015, 71015, 171015, 1015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122015, 122015, 22015, 1015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171016, 16.25, 10.95, 3.1)
    ops.node(122016, 16.25, 10.95, 5.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1016, 171016, 122016, 0.16, 29280730.9550745, 12200304.56461438, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21016, 110.68085753, 0.00058365, 134.19979727, 0.04467909, 13.41997973, 0.12590722, -110.68085753, -0.00058365, -134.19979727, -0.04467909, -13.41997973, -0.12590722, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11016, 103.28531282, 0.00058365, 125.23274892, 0.04467909, 12.52327489, 0.12590722, -103.28531282, -0.00058365, -125.23274892, -0.04467909, -12.52327489, -0.12590722, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21016, 1016, 0.0, 201.08669632, 0.01167297, 201.08669632, 0.0350189, 140.76068742, -3975.17720429, 0.05, 2, 0, 71016, 22016, 2, 3)
    ops.uniaxialMaterial('LimitState', 41016, 50.27167408, 8.808e-05, 150.81502224, 0.00026423, 502.7167408, 0.00088076, -50.27167408, -8.808e-05, -150.81502224, -0.00026423, -502.7167408, -0.00088076, 0.4, 0.3, 0.003, 0.0, 0.0, 21016, 2)
    ops.limitCurve('ThreePoint', 11016, 1016, 0.0, 201.08669632, 0.01167297, 201.08669632, 0.0350189, 140.76068742, -3975.17720429, 0.05, 2, 0, 71016, 22016, 1, 3)
    ops.uniaxialMaterial('LimitState', 31016, 50.27167408, 8.808e-05, 150.81502224, 0.00026423, 502.7167408, 0.00088076, -50.27167408, -8.808e-05, -150.81502224, -0.00026423, -502.7167408, -0.00088076, 0.4, 0.3, 0.003, 0.0, 0.0, 11016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1016, 99999, 'P', 41016, 'Vy', 31016, 'Vz', 21016, 'My', 11016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171016, 71016, 171016, 1016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122016, 122016, 22016, 1016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171017, 0.0, 14.6, 3.1)
    ops.node(122017, 0.0, 14.6, 5.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1017, 171017, 122017, 0.09, 27736419.81023252, 11556841.58759688, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21017, 33.36595533, 0.00067081, 40.59383703, 0.02645451, 4.0593837, 0.08319564, -33.36595533, -0.00067081, -40.59383703, -0.02645451, -4.0593837, -0.08319564, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11017, 36.03528164, 0.00067081, 43.84140468, 0.02645451, 4.38414047, 0.08319564, -36.03528164, -0.00067081, -43.84140468, -0.02645451, -4.38414047, -0.08319564, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21017, 1017, 0.0, 90.24620364, 0.01341629, 90.24620364, 0.04024886, 63.17234255, -1365.77233609, 0.05, 2, 0, 71017, 22017, 2, 3)
    ops.uniaxialMaterial('LimitState', 41017, 22.56155091, 7.418e-05, 67.68465273, 0.00022255, 225.6155091, 0.00074185, -22.56155091, -7.418e-05, -67.68465273, -0.00022255, -225.6155091, -0.00074185, 0.4, 0.3, 0.003, 0.0, 0.0, 21017, 2)
    ops.limitCurve('ThreePoint', 11017, 1017, 0.0, 90.24620364, 0.01341629, 90.24620364, 0.04024886, 63.17234255, -1365.77233609, 0.05, 2, 0, 71017, 22017, 1, 3)
    ops.uniaxialMaterial('LimitState', 31017, 22.56155091, 7.418e-05, 67.68465273, 0.00022255, 225.6155091, 0.00074185, -22.56155091, -7.418e-05, -67.68465273, -0.00022255, -225.6155091, -0.00074185, 0.4, 0.3, 0.003, 0.0, 0.0, 11017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1017, 99999, 'P', 41017, 'Vy', 31017, 'Vz', 21017, 'My', 11017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171017, 71017, 171017, 1017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122017, 122017, 22017, 1017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171018, 2.95, 14.6, 3.1)
    ops.node(122018, 2.95, 14.6, 5.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1018, 171018, 122018, 0.16, 28773795.87523847, 11989081.6146827, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21018, 94.36169337, 0.00057615, 114.46246818, 0.04184928, 11.44624682, 0.12080889, -94.36169337, -0.00057615, -114.46246818, -0.04184928, -11.44624682, -0.12080889, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11018, 86.52531115, 0.00057615, 104.95679253, 0.04184928, 10.49567925, 0.12080889, -86.52531115, -0.00057615, -104.95679253, -0.04184928, -10.49567925, -0.12080889, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21018, 1018, 0.0, 199.60967298, 0.01152306, 199.60967298, 0.03456918, 139.72677109, -3801.9229218, 0.05, 2, 0, 71018, 22018, 2, 3)
    ops.uniaxialMaterial('LimitState', 41018, 49.90241825, 8.897e-05, 149.70725474, 0.00026691, 499.02418245, 0.0008897, -49.90241825, -8.897e-05, -149.70725474, -0.00026691, -499.02418245, -0.0008897, 0.4, 0.3, 0.003, 0.0, 0.0, 21018, 2)
    ops.limitCurve('ThreePoint', 11018, 1018, 0.0, 199.60967298, 0.01152306, 199.60967298, 0.03456918, 139.72677109, -3801.9229218, 0.05, 2, 0, 71018, 22018, 1, 3)
    ops.uniaxialMaterial('LimitState', 31018, 49.90241825, 8.897e-05, 149.70725474, 0.00026691, 499.02418245, 0.0008897, -49.90241825, -8.897e-05, -149.70725474, -0.00026691, -499.02418245, -0.0008897, 0.4, 0.3, 0.003, 0.0, 0.0, 11018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1018, 99999, 'P', 41018, 'Vy', 31018, 'Vz', 21018, 'My', 11018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171018, 71018, 171018, 1018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122018, 122018, 22018, 1018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171019, 9.6, 14.6, 3.1)
    ops.node(122019, 9.6, 14.6, 5.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1019, 171019, 122019, 0.2025, 27398926.139446, 11416219.22476917, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21019, 137.95457381, 0.00054123, 167.62340765, 0.03090731, 16.76234077, 0.07943389, -137.95457381, -0.00054123, -167.62340765, -0.03090731, -16.76234077, -0.07943389, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11019, 122.26506119, 0.00054123, 148.55967169, 0.03090731, 14.85596717, 0.07943389, -122.26506119, -0.00054123, -148.55967169, -0.03090731, -14.85596717, -0.07943389, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21019, 1019, 0.0, 196.23649951, 0.01082463, 196.23649951, 0.03247388, 137.36554966, -2483.29813412, 0.05, 2, 0, 71019, 22019, 2, 3)
    ops.uniaxialMaterial('LimitState', 41019, 49.05912488, 7.258e-05, 147.17737464, 0.00021773, 490.59124878, 0.00072577, -49.05912488, -7.258e-05, -147.17737464, -0.00021773, -490.59124878, -0.00072577, 0.4, 0.3, 0.003, 0.0, 0.0, 21019, 2)
    ops.limitCurve('ThreePoint', 11019, 1019, 0.0, 196.23649951, 0.01082463, 196.23649951, 0.03247388, 137.36554966, -2483.29813412, 0.05, 2, 0, 71019, 22019, 1, 3)
    ops.uniaxialMaterial('LimitState', 31019, 49.05912488, 7.258e-05, 147.17737464, 0.00021773, 490.59124878, 0.00072577, -49.05912488, -7.258e-05, -147.17737464, -0.00021773, -490.59124878, -0.00072577, 0.4, 0.3, 0.003, 0.0, 0.0, 11019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1019, 99999, 'P', 41019, 'Vy', 31019, 'Vz', 21019, 'My', 11019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171019, 71019, 171019, 1019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122019, 122019, 22019, 1019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171020, 16.25, 14.6, 3.1)
    ops.node(122020, 16.25, 14.6, 5.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1020, 171020, 122020, 0.16, 27877473.28220074, 11615613.86758364, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21020, 109.88963099, 0.00058661, 133.59065356, 0.04534218, 13.35906536, 0.12402425, -109.88963099, -0.00058661, -133.59065356, -0.04534218, -13.35906536, -0.12402425, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11020, 102.46529889, 0.00058661, 124.5650397, 0.04534218, 12.45650397, 0.12402425, -102.46529889, -0.00058661, -124.5650397, -0.04534218, -12.45650397, -0.12402425, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21020, 1020, 0.0, 197.61290636, 0.01173223, 197.61290636, 0.0351967, 138.32903445, -4149.90200291, 0.05, 2, 0, 71020, 22020, 2, 3)
    ops.uniaxialMaterial('LimitState', 41020, 49.40322659, 9.091e-05, 148.20967977, 0.00027273, 494.0322659, 0.00090912, -49.40322659, -9.091e-05, -148.20967977, -0.00027273, -494.0322659, -0.00090912, 0.4, 0.3, 0.003, 0.0, 0.0, 21020, 2)
    ops.limitCurve('ThreePoint', 11020, 1020, 0.0, 197.61290636, 0.01173223, 197.61290636, 0.0351967, 138.32903445, -4149.90200291, 0.05, 2, 0, 71020, 22020, 1, 3)
    ops.uniaxialMaterial('LimitState', 31020, 49.40322659, 9.091e-05, 148.20967977, 0.00027273, 494.0322659, 0.00090912, -49.40322659, -9.091e-05, -148.20967977, -0.00027273, -494.0322659, -0.00090912, 0.4, 0.3, 0.003, 0.0, 0.0, 11020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1020, 99999, 'P', 41020, 'Vy', 31020, 'Vz', 21020, 'My', 11020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171020, 71020, 171020, 1020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122020, 122020, 22020, 1020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171021, 0.0, 18.25, 3.1)
    ops.node(122021, 0.0, 18.25, 5.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1021, 171021, 122021, 0.09, 27584856.71586768, 11493690.2982782, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21021, 33.28101018, 0.00067329, 40.50049332, 0.02653035, 4.05004933, 0.08306464, -33.28101018, -0.00067329, -40.50049332, -0.02653035, -4.05004933, -0.08306464, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11021, 35.91840883, 0.00067329, 43.71000967, 0.02653035, 4.37100097, 0.08306464, -35.91840883, -0.00067329, -43.71000967, -0.02653035, -4.37100097, -0.08306464, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21021, 1021, 0.0, 90.33069122, 0.0134658, 90.33069122, 0.04039741, 63.23148386, -1387.46400678, 0.05, 2, 0, 71021, 22021, 2, 3)
    ops.uniaxialMaterial('LimitState', 41021, 22.58267281, 7.466e-05, 67.74801842, 0.00022399, 225.82672806, 0.00074662, -22.58267281, -7.466e-05, -67.74801842, -0.00022399, -225.82672806, -0.00074662, 0.4, 0.3, 0.003, 0.0, 0.0, 21021, 2)
    ops.limitCurve('ThreePoint', 11021, 1021, 0.0, 90.33069122, 0.0134658, 90.33069122, 0.04039741, 63.23148386, -1387.46400678, 0.05, 2, 0, 71021, 22021, 1, 3)
    ops.uniaxialMaterial('LimitState', 31021, 22.58267281, 7.466e-05, 67.74801842, 0.00022399, 225.82672806, 0.00074662, -22.58267281, -7.466e-05, -67.74801842, -0.00022399, -225.82672806, -0.00074662, 0.4, 0.3, 0.003, 0.0, 0.0, 11021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1021, 99999, 'P', 41021, 'Vy', 31021, 'Vz', 21021, 'My', 11021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171021, 71021, 171021, 1021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122021, 122021, 22021, 1021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171022, 2.95, 18.25, 3.1)
    ops.node(122022, 2.95, 18.25, 5.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1022, 171022, 122022, 0.16, 27604231.51047998, 11501763.12936666, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21022, 106.19072031, 0.00057571, 129.06257433, 0.04238539, 12.90625743, 0.11895299, -106.19072031, -0.00057571, -129.06257433, -0.04238539, -12.90625743, -0.11895299, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11022, 93.2091502, 0.00057571, 113.28497293, 0.04238539, 11.32849729, 0.11895299, -93.2091502, -0.00057571, -113.28497293, -0.04238539, -11.32849729, -0.11895299, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21022, 1022, 0.0, 192.90720339, 0.01151423, 192.90720339, 0.0345427, 135.03504237, -3735.9696899, 0.05, 2, 0, 71022, 22022, 2, 3)
    ops.uniaxialMaterial('LimitState', 41022, 48.22680085, 8.963e-05, 144.68040254, 0.00026888, 482.26800848, 0.00089625, -48.22680085, -8.963e-05, -144.68040254, -0.00026888, -482.26800848, -0.00089625, 0.4, 0.3, 0.003, 0.0, 0.0, 21022, 2)
    ops.limitCurve('ThreePoint', 11022, 1022, 0.0, 192.90720339, 0.01151423, 192.90720339, 0.0345427, 135.03504237, -3735.9696899, 0.05, 2, 0, 71022, 22022, 1, 3)
    ops.uniaxialMaterial('LimitState', 31022, 48.22680085, 8.963e-05, 144.68040254, 0.00026888, 482.26800848, 0.00089625, -48.22680085, -8.963e-05, -144.68040254, -0.00026888, -482.26800848, -0.00089625, 0.4, 0.3, 0.003, 0.0, 0.0, 11022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1022, 99999, 'P', 41022, 'Vy', 31022, 'Vz', 21022, 'My', 11022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171022, 71022, 171022, 1022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122022, 122022, 22022, 1022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171023, 9.6, 18.25, 3.1)
    ops.node(122023, 9.6, 18.25, 5.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1023, 171023, 122023, 0.2025, 28376587.9715132, 11823578.32146383, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21023, 136.32554439, 0.0005343, 165.40154044, 0.03092027, 16.54015404, 0.08086283, -136.32554439, -0.0005343, -165.40154044, -0.03092027, -16.54015404, -0.08086283, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11023, 121.18570655, 0.0005343, 147.03262425, 0.03092027, 14.70326242, 0.08086283, -121.18570655, -0.0005343, -147.03262425, -0.03092027, -14.70326242, -0.08086283, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21023, 1023, 0.0, 201.99351879, 0.01068609, 201.99351879, 0.03205828, 141.39546315, -2481.84590279, 0.05, 2, 0, 71023, 22023, 2, 3)
    ops.uniaxialMaterial('LimitState', 41023, 50.4983797, 7.213e-05, 151.49513909, 0.0002164, 504.98379698, 0.00072132, -50.4983797, -7.213e-05, -151.49513909, -0.0002164, -504.98379698, -0.00072132, 0.4, 0.3, 0.003, 0.0, 0.0, 21023, 2)
    ops.limitCurve('ThreePoint', 11023, 1023, 0.0, 201.99351879, 0.01068609, 201.99351879, 0.03205828, 141.39546315, -2481.84590279, 0.05, 2, 0, 71023, 22023, 1, 3)
    ops.uniaxialMaterial('LimitState', 31023, 50.4983797, 7.213e-05, 151.49513909, 0.0002164, 504.98379698, 0.00072132, -50.4983797, -7.213e-05, -151.49513909, -0.0002164, -504.98379698, -0.00072132, 0.4, 0.3, 0.003, 0.0, 0.0, 11023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1023, 99999, 'P', 41023, 'Vy', 31023, 'Vz', 21023, 'My', 11023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171023, 71023, 171023, 1023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122023, 122023, 22023, 1023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171024, 16.25, 18.25, 3.1)
    ops.node(122024, 16.25, 18.25, 5.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1024, 171024, 122024, 0.16, 27810862.23994924, 11587859.26664552, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21024, 112.32596734, 0.00058867, 136.56724681, 0.04528496, 13.65672468, 0.1238343, -112.32596734, -0.00058867, -136.56724681, -0.04528496, -13.65672468, -0.1238343, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11024, 104.51803998, 0.00058867, 127.07427589, 0.04528496, 12.70742759, 0.1238343, -104.51803998, -0.00058867, -127.07427589, -0.04528496, -12.70742759, -0.1238343, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21024, 1024, 0.0, 196.22108979, 0.01177334, 196.22108979, 0.03532002, 137.35476285, -4087.95293691, 0.05, 2, 0, 71024, 22024, 2, 3)
    ops.uniaxialMaterial('LimitState', 41024, 49.05527245, 9.049e-05, 147.16581734, 0.00027146, 490.55272448, 0.00090488, -49.05527245, -9.049e-05, -147.16581734, -0.00027146, -490.55272448, -0.00090488, 0.4, 0.3, 0.003, 0.0, 0.0, 21024, 2)
    ops.limitCurve('ThreePoint', 11024, 1024, 0.0, 196.22108979, 0.01177334, 196.22108979, 0.03532002, 137.35476285, -4087.95293691, 0.05, 2, 0, 71024, 22024, 1, 3)
    ops.uniaxialMaterial('LimitState', 31024, 49.05527245, 9.049e-05, 147.16581734, 0.00027146, 490.55272448, 0.00090488, -49.05527245, -9.049e-05, -147.16581734, -0.00027146, -490.55272448, -0.00090488, 0.4, 0.3, 0.003, 0.0, 0.0, 11024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1024, 99999, 'P', 41024, 'Vy', 31024, 'Vz', 21024, 'My', 11024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171024, 71024, 171024, 1024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122024, 122024, 22024, 1024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171025, 0.0, 21.9, 3.15)
    ops.node(122025, 0.0, 21.9, 5.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1025, 171025, 122025, 0.0625, 29172134.69635449, 12155056.12348104, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21025, 19.1908948, 0.00075291, 23.30254885, 0.02228486, 2.33025489, 0.08020137, -19.1908948, -0.00075291, -23.30254885, -0.02228486, -2.33025489, -0.08020137, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11025, 19.1908948, 0.00075291, 23.30254885, 0.02228486, 2.33025489, 0.08020137, -19.1908948, -0.00075291, -23.30254885, -0.02228486, -2.33025489, -0.08020137, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21025, 1025, 0.0, 62.95740421, 0.0150581, 62.95740421, 0.0451743, 44.07018295, -921.20064998, 0.05, 2, 0, 71025, 22025, 2, 3)
    ops.uniaxialMaterial('LimitState', 41025, 15.73935105, 7.086e-05, 47.21805316, 0.00021257, 157.39351052, 0.00070856, -15.73935105, -7.086e-05, -47.21805316, -0.00021257, -157.39351052, -0.00070856, 0.4, 0.3, 0.003, 0.0, 0.0, 21025, 2)
    ops.limitCurve('ThreePoint', 11025, 1025, 0.0, 62.95740421, 0.0150581, 62.95740421, 0.0451743, 44.07018295, -921.20064998, 0.05, 2, 0, 71025, 22025, 1, 3)
    ops.uniaxialMaterial('LimitState', 31025, 15.73935105, 7.086e-05, 47.21805316, 0.00021257, 157.39351052, 0.00070856, -15.73935105, -7.086e-05, -47.21805316, -0.00021257, -157.39351052, -0.00070856, 0.4, 0.3, 0.003, 0.0, 0.0, 11025, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1025, 99999, 'P', 41025, 'Vy', 31025, 'Vz', 21025, 'My', 11025, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171025, 71025, 171025, 1025, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122025, 122025, 22025, 1025, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171026, 2.95, 21.9, 3.15)
    ops.node(122026, 2.95, 21.9, 5.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1026, 171026, 122026, 0.1225, 27828952.93729831, 11595397.05720763, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21026, 69.57370249, 0.00060613, 84.57281712, 0.03183668, 8.45728171, 0.09394962, -69.57370249, -0.00060613, -84.57281712, -0.03183668, -8.45728171, -0.09394962, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11026, 58.42735864, 0.00060613, 71.02347784, 0.03183668, 7.10234778, 0.09394962, -58.42735864, -0.00060613, -71.02347784, -0.03183668, -7.10234778, -0.09394962, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21026, 1026, 0.0, 131.50423399, 0.01212252, 131.50423399, 0.03636757, 92.0529638, -2125.16089676, 0.05, 2, 0, 71026, 22026, 2, 3)
    ops.uniaxialMaterial('LimitState', 41026, 32.8760585, 7.916e-05, 98.6281755, 0.00023747, 328.76058499, 0.00079156, -32.8760585, -7.916e-05, -98.6281755, -0.00023747, -328.76058499, -0.00079156, 0.4, 0.3, 0.003, 0.0, 0.0, 21026, 2)
    ops.limitCurve('ThreePoint', 11026, 1026, 0.0, 131.50423399, 0.01212252, 131.50423399, 0.03636757, 92.0529638, -2125.16089676, 0.05, 2, 0, 71026, 22026, 1, 3)
    ops.uniaxialMaterial('LimitState', 31026, 32.8760585, 7.916e-05, 98.6281755, 0.00023747, 328.76058499, 0.00079156, -32.8760585, -7.916e-05, -98.6281755, -0.00023747, -328.76058499, -0.00079156, 0.4, 0.3, 0.003, 0.0, 0.0, 11026, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1026, 99999, 'P', 41026, 'Vy', 31026, 'Vz', 21026, 'My', 11026, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171026, 71026, 171026, 1026, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122026, 122026, 22026, 1026, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171027, 9.6, 21.9, 3.15)
    ops.node(122027, 9.6, 21.9, 5.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1027, 171027, 122027, 0.16, 26602686.18153297, 11084452.57563874, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21027, 91.11385783, 0.00056698, 110.89665735, 0.02983176, 11.08966573, 0.08290332, -91.11385783, -0.00056698, -110.89665735, -0.02983176, -11.08966573, -0.08290332, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11027, 77.84184702, 0.00056698, 94.74300443, 0.02983176, 9.47430044, 0.08290332, -77.84184702, -0.00056698, -94.74300443, -0.02983176, -9.47430044, -0.08290332, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21027, 1027, 0.0, 157.94943243, 0.01133964, 157.94943243, 0.03401891, 110.5646027, -2342.17861635, 0.05, 2, 0, 71027, 22027, 2, 3)
    ops.uniaxialMaterial('LimitState', 41027, 39.48735811, 7.615e-05, 118.46207432, 0.00022844, 394.87358106, 0.00076147, -39.48735811, -7.615e-05, -118.46207432, -0.00022844, -394.87358106, -0.00076147, 0.4, 0.3, 0.003, 0.0, 0.0, 21027, 2)
    ops.limitCurve('ThreePoint', 11027, 1027, 0.0, 157.94943243, 0.01133964, 157.94943243, 0.03401891, 110.5646027, -2342.17861635, 0.05, 2, 0, 71027, 22027, 1, 3)
    ops.uniaxialMaterial('LimitState', 31027, 39.48735811, 7.615e-05, 118.46207432, 0.00022844, 394.87358106, 0.00076147, -39.48735811, -7.615e-05, -118.46207432, -0.00022844, -394.87358106, -0.00076147, 0.4, 0.3, 0.003, 0.0, 0.0, 11027, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1027, 99999, 'P', 41027, 'Vy', 31027, 'Vz', 21027, 'My', 11027, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171027, 71027, 171027, 1027, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122027, 122027, 22027, 1027, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171028, 16.25, 21.9, 3.15)
    ops.node(122028, 16.25, 21.9, 5.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1028, 171028, 122028, 0.09, 27453647.18005611, 11439019.65835671, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21028, 48.14605596, 0.00068573, 58.53849306, 0.03686255, 5.85384931, 0.10610824, -48.14605596, -0.00068573, -58.53849306, -0.03686255, -5.85384931, -0.10610824, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11028, 45.3539304, 0.00068573, 55.14368077, 0.03686255, 5.51436808, 0.10610824, -45.3539304, -0.00068573, -55.14368077, -0.03686255, -5.51436808, -0.10610824, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21028, 1028, 0.0, 103.00265207, 0.01371468, 103.00265207, 0.04114404, 72.10185645, -1867.19367363, 0.05, 2, 0, 71028, 22028, 2, 3)
    ops.uniaxialMaterial('LimitState', 41028, 25.75066302, 8.554e-05, 77.25198905, 0.00025663, 257.50663017, 0.00085543, -25.75066302, -8.554e-05, -77.25198905, -0.00025663, -257.50663017, -0.00085543, 0.4, 0.3, 0.003, 0.0, 0.0, 21028, 2)
    ops.limitCurve('ThreePoint', 11028, 1028, 0.0, 103.00265207, 0.01371468, 103.00265207, 0.04114404, 72.10185645, -1867.19367363, 0.05, 2, 0, 71028, 22028, 1, 3)
    ops.uniaxialMaterial('LimitState', 31028, 25.75066302, 8.554e-05, 77.25198905, 0.00025663, 257.50663017, 0.00085543, -25.75066302, -8.554e-05, -77.25198905, -0.00025663, -257.50663017, -0.00085543, 0.4, 0.3, 0.003, 0.0, 0.0, 11028, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1028, 99999, 'P', 41028, 'Vy', 31028, 'Vz', 21028, 'My', 11028, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171028, 71028, 171028, 1028, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122028, 122028, 22028, 1028, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172003, 9.6, 0.0, 6.0)
    ops.node(123003, 9.6, 0.0, 8.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2003, 172003, 123003, 0.1225, 28615495.08058058, 11923122.95024191, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22003, 56.39918268, 0.00059223, 68.53754503, 0.01995826, 6.8537545, 0.06375572, -56.39918268, -0.00059223, -68.53754503, -0.01995826, -6.8537545, -0.06375572, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12003, 49.53290924, 0.00059223, 60.19349637, 0.01995826, 6.01934964, 0.06375572, -49.53290924, -0.00059223, -60.19349637, -0.01995826, -6.01934964, -0.06375572, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22003, 2003, 0.0, 107.753547, 0.01184453, 107.753547, 0.03553359, 75.4274829, -1163.05664984, 0.05, 2, 0, 72003, 23003, 2, 3)
    ops.uniaxialMaterial('LimitState', 42003, 26.93838675, 6.308e-05, 80.81516025, 0.00018923, 269.3838675, 0.00063077, -26.93838675, -6.308e-05, -80.81516025, -0.00018923, -269.3838675, -0.00063077, 0.4, 0.3, 0.003, 0.0, 0.0, 22003, 2)
    ops.limitCurve('ThreePoint', 12003, 2003, 0.0, 107.753547, 0.01184453, 107.753547, 0.03553359, 75.4274829, -1163.05664984, 0.05, 2, 0, 72003, 23003, 1, 3)
    ops.uniaxialMaterial('LimitState', 32003, 26.93838675, 6.308e-05, 80.81516025, 0.00018923, 269.3838675, 0.00063077, -26.93838675, -6.308e-05, -80.81516025, -0.00018923, -269.3838675, -0.00063077, 0.4, 0.3, 0.003, 0.0, 0.0, 12003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2003, 99999, 'P', 42003, 'Vy', 32003, 'Vz', 22003, 'My', 12003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172003, 72003, 172003, 2003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123003, 123003, 23003, 2003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172004, 16.25, 0.0, 6.0)
    ops.node(123004, 16.25, 0.0, 8.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2004, 172004, 123004, 0.0625, 27539782.31906125, 11474909.29960885, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22004, 28.35536088, 0.00084796, 34.50812861, 0.02718932, 3.45081286, 0.08180768, -28.35536088, -0.00084796, -34.50812861, -0.02718932, -3.45081286, -0.08180768, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12004, 28.35536088, 0.00084796, 34.50812861, 0.02718932, 3.45081286, 0.08180768, -28.35536088, -0.00084796, -34.50812861, -0.02718932, -3.45081286, -0.08180768, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22004, 2004, 0.0, 61.60560399, 0.01695926, 61.60560399, 0.05087778, 43.1239228, -914.5753218, 0.05, 2, 0, 72004, 23004, 2, 3)
    ops.uniaxialMaterial('LimitState', 42004, 15.401401, 7.344e-05, 46.204203, 0.00022033, 154.01400999, 0.00073444, -15.401401, -7.344e-05, -46.204203, -0.00022033, -154.01400999, -0.00073444, 0.4, 0.3, 0.003, 0.0, 0.0, 22004, 2)
    ops.limitCurve('ThreePoint', 12004, 2004, 0.0, 61.60560399, 0.01695926, 61.60560399, 0.05087778, 43.1239228, -914.5753218, 0.05, 2, 0, 72004, 23004, 1, 3)
    ops.uniaxialMaterial('LimitState', 32004, 15.401401, 7.344e-05, 46.204203, 0.00022033, 154.01400999, 0.00073444, -15.401401, -7.344e-05, -46.204203, -0.00022033, -154.01400999, -0.00073444, 0.4, 0.3, 0.003, 0.0, 0.0, 12004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2004, 99999, 'P', 42004, 'Vy', 32004, 'Vz', 22004, 'My', 12004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172004, 72004, 172004, 2004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123004, 123004, 23004, 2004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172005, 0.0, 3.65, 5.95)
    ops.node(123005, 0.0, 3.65, 8.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2005, 172005, 123005, 0.0625, 26181098.34604938, 10908790.97752057, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22005, 20.2321582, 0.00079924, 24.64511738, 0.02227792, 2.46451174, 0.07347878, -20.2321582, -0.00079924, -24.64511738, -0.02227792, -2.46451174, -0.07347878, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12005, 20.2321582, 0.00079924, 24.64511738, 0.02227792, 2.46451174, 0.07347878, -20.2321582, -0.00079924, -24.64511738, -0.02227792, -2.46451174, -0.07347878, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22005, 2005, 0.0, 59.50575872, 0.01598482, 59.50575872, 0.04795446, 41.65403111, -874.11067743, 0.05, 2, 0, 72005, 23005, 2, 3)
    ops.uniaxialMaterial('LimitState', 42005, 14.87643968, 7.462e-05, 44.62931904, 0.00022387, 148.76439681, 0.00074622, -14.87643968, -7.462e-05, -44.62931904, -0.00022387, -148.76439681, -0.00074622, 0.4, 0.3, 0.003, 0.0, 0.0, 22005, 2)
    ops.limitCurve('ThreePoint', 12005, 2005, 0.0, 59.50575872, 0.01598482, 59.50575872, 0.04795446, 41.65403111, -874.11067743, 0.05, 2, 0, 72005, 23005, 1, 3)
    ops.uniaxialMaterial('LimitState', 32005, 14.87643968, 7.462e-05, 44.62931904, 0.00022387, 148.76439681, 0.00074622, -14.87643968, -7.462e-05, -44.62931904, -0.00022387, -148.76439681, -0.00074622, 0.4, 0.3, 0.003, 0.0, 0.0, 12005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2005, 99999, 'P', 42005, 'Vy', 32005, 'Vz', 22005, 'My', 12005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172005, 72005, 172005, 2005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123005, 123005, 23005, 2005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172006, 2.95, 3.65, 5.95)
    ops.node(123006, 2.95, 3.65, 8.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2006, 172006, 123006, 0.1225, 27173540.72653969, 11322308.6360582, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22006, 64.69887778, 0.00061562, 78.71472199, 0.03457484, 7.8714722, 0.09537514, -64.69887778, -0.00061562, -78.71472199, -0.03457484, -7.8714722, -0.09537514, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12006, 61.15029734, 0.00061562, 74.39740564, 0.03457484, 7.43974056, 0.09537514, -61.15029734, -0.00061562, -74.39740564, -0.03457484, -7.43974056, -0.09537514, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22006, 2006, 0.0, 129.25692187, 0.01231243, 129.25692187, 0.03693728, 90.47984531, -2109.44166166, 0.05, 2, 0, 72006, 23006, 2, 3)
    ops.uniaxialMaterial('LimitState', 42006, 32.31423047, 7.968e-05, 96.9426914, 0.00023904, 323.14230467, 0.0007968, -32.31423047, -7.968e-05, -96.9426914, -0.00023904, -323.14230467, -0.0007968, 0.4, 0.3, 0.003, 0.0, 0.0, 22006, 2)
    ops.limitCurve('ThreePoint', 12006, 2006, 0.0, 129.25692187, 0.01231243, 129.25692187, 0.03693728, 90.47984531, -2109.44166166, 0.05, 2, 0, 72006, 23006, 1, 3)
    ops.uniaxialMaterial('LimitState', 32006, 32.31423047, 7.968e-05, 96.9426914, 0.00023904, 323.14230467, 0.0007968, -32.31423047, -7.968e-05, -96.9426914, -0.00023904, -323.14230467, -0.0007968, 0.4, 0.3, 0.003, 0.0, 0.0, 12006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2006, 99999, 'P', 42006, 'Vy', 32006, 'Vz', 22006, 'My', 12006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172006, 72006, 172006, 2006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123006, 123006, 23006, 2006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172007, 9.6, 3.65, 5.95)
    ops.node(123007, 9.6, 3.65, 8.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2007, 172007, 123007, 0.1225, 26517997.71690856, 11049165.71537857, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22007, 68.93004193, 0.00062906, 83.80001427, 0.02258386, 8.38000143, 0.06069746, -68.93004193, -0.00062906, -83.80001427, -0.02258386, -8.38000143, -0.06069746, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12007, 65.27099364, 0.00062906, 79.35161572, 0.02258386, 7.93516157, 0.06069746, -65.27099364, -0.00062906, -79.35161572, -0.02258386, -7.93516157, -0.06069746, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22007, 2007, 0.0, 104.86276898, 0.01258121, 104.86276898, 0.03774364, 73.40393828, -1139.10728901, 0.05, 2, 0, 72007, 23007, 2, 3)
    ops.uniaxialMaterial('LimitState', 42007, 26.21569224, 6.624e-05, 78.64707673, 0.00019872, 262.15692244, 0.0006624, -26.21569224, -6.624e-05, -78.64707673, -0.00019872, -262.15692244, -0.0006624, 0.4, 0.3, 0.003, 0.0, 0.0, 22007, 2)
    ops.limitCurve('ThreePoint', 12007, 2007, 0.0, 104.86276898, 0.01258121, 104.86276898, 0.03774364, 73.40393828, -1139.10728901, 0.05, 2, 0, 72007, 23007, 1, 3)
    ops.uniaxialMaterial('LimitState', 32007, 26.21569224, 6.624e-05, 78.64707673, 0.00019872, 262.15692244, 0.0006624, -26.21569224, -6.624e-05, -78.64707673, -0.00019872, -262.15692244, -0.0006624, 0.4, 0.3, 0.003, 0.0, 0.0, 12007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2007, 99999, 'P', 42007, 'Vy', 32007, 'Vz', 22007, 'My', 12007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172007, 72007, 172007, 2007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123007, 123007, 23007, 2007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172008, 16.25, 3.65, 5.95)
    ops.node(123008, 16.25, 3.65, 8.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2008, 172008, 123008, 0.1225, 29899798.5694064, 12458249.40391933, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22008, 68.1195681, 0.00062395, 82.57184924, 0.04708133, 8.25718492, 0.14253114, -68.1195681, -0.00062395, -82.57184924, -0.04708133, -8.25718492, -0.14253114, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12008, 68.1195681, 0.00062395, 82.57184924, 0.04708133, 8.25718492, 0.14253114, -68.1195681, -0.00062395, -82.57184924, -0.04708133, -8.25718492, -0.14253114, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22008, 2008, 0.0, 163.61318848, 0.01247899, 163.61318848, 0.03743696, 114.52923193, -4051.78520533, 0.05, 2, 0, 72008, 23008, 2, 3)
    ops.uniaxialMaterial('LimitState', 42008, 40.90329712, 9.166e-05, 122.70989136, 0.00027499, 409.03297119, 0.00091662, -40.90329712, -9.166e-05, -122.70989136, -0.00027499, -409.03297119, -0.00091662, 0.4, 0.3, 0.003, 0.0, 0.0, 22008, 2)
    ops.limitCurve('ThreePoint', 12008, 2008, 0.0, 163.61318848, 0.01247899, 163.61318848, 0.03743696, 114.52923193, -4051.78520533, 0.05, 2, 0, 72008, 23008, 1, 3)
    ops.uniaxialMaterial('LimitState', 32008, 40.90329712, 9.166e-05, 122.70989136, 0.00027499, 409.03297119, 0.00091662, -40.90329712, -9.166e-05, -122.70989136, -0.00027499, -409.03297119, -0.00091662, 0.4, 0.3, 0.003, 0.0, 0.0, 12008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2008, 99999, 'P', 42008, 'Vy', 32008, 'Vz', 22008, 'My', 12008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172008, 72008, 172008, 2008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123008, 123008, 23008, 2008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172009, 0.0, 7.3, 5.95)
    ops.node(123009, 0.0, 7.3, 8.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2009, 172009, 123009, 0.0625, 29353960.10187443, 12230816.70911434, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22009, 19.02854747, 0.00074594, 23.09521679, 0.02267448, 2.30952168, 0.08070145, -19.02854747, -0.00074594, -23.09521679, -0.02267448, -2.30952168, -0.08070145, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12009, 19.02854747, 0.00074594, 23.09521679, 0.02267448, 2.30952168, 0.08070145, -19.02854747, -0.00074594, -23.09521679, -0.02267448, -2.30952168, -0.08070145, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22009, 2009, 0.0, 63.82775889, 0.01491882, 63.82775889, 0.04475645, 44.67943122, -942.88989435, 0.05, 2, 0, 72009, 23009, 2, 3)
    ops.uniaxialMaterial('LimitState', 42009, 15.95693972, 7.139e-05, 47.87081917, 0.00021417, 159.56939722, 0.0007139, -15.95693972, -7.139e-05, -47.87081917, -0.00021417, -159.56939722, -0.0007139, 0.4, 0.3, 0.003, 0.0, 0.0, 22009, 2)
    ops.limitCurve('ThreePoint', 12009, 2009, 0.0, 63.82775889, 0.01491882, 63.82775889, 0.04475645, 44.67943122, -942.88989435, 0.05, 2, 0, 72009, 23009, 1, 3)
    ops.uniaxialMaterial('LimitState', 32009, 15.95693972, 7.139e-05, 47.87081917, 0.00021417, 159.56939722, 0.0007139, -15.95693972, -7.139e-05, -47.87081917, -0.00021417, -159.56939722, -0.0007139, 0.4, 0.3, 0.003, 0.0, 0.0, 12009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2009, 99999, 'P', 42009, 'Vy', 32009, 'Vz', 22009, 'My', 12009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172009, 72009, 172009, 2009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123009, 123009, 23009, 2009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172010, 2.95, 7.3, 5.95)
    ops.node(123010, 2.95, 7.3, 8.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2010, 172010, 123010, 0.1225, 28446412.30822515, 11852671.79509382, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22010, 62.15636461, 0.00060472, 75.53449385, 0.03472136, 7.55344939, 0.09924376, -62.15636461, -0.00060472, -75.53449385, -0.03472136, -7.55344939, -0.09924376, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12010, 58.66179674, 0.00060472, 71.28777806, 0.03472136, 7.12877781, 0.09924376, -58.66179674, -0.00060472, -71.28777806, -0.03472136, -7.12877781, -0.09924376, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22010, 2010, 0.0, 131.1569263, 0.0120944, 131.1569263, 0.03628319, 91.80984841, -2158.4097605, 0.05, 2, 0, 72010, 23010, 2, 3)
    ops.uniaxialMaterial('LimitState', 42010, 32.78923158, 7.723e-05, 98.36769473, 0.0002317, 327.89231576, 0.00077233, -32.78923158, -7.723e-05, -98.36769473, -0.0002317, -327.89231576, -0.00077233, 0.4, 0.3, 0.003, 0.0, 0.0, 22010, 2)
    ops.limitCurve('ThreePoint', 12010, 2010, 0.0, 131.1569263, 0.0120944, 131.1569263, 0.03628319, 91.80984841, -2158.4097605, 0.05, 2, 0, 72010, 23010, 1, 3)
    ops.uniaxialMaterial('LimitState', 32010, 32.78923158, 7.723e-05, 98.36769473, 0.0002317, 327.89231576, 0.00077233, -32.78923158, -7.723e-05, -98.36769473, -0.0002317, -327.89231576, -0.00077233, 0.4, 0.3, 0.003, 0.0, 0.0, 12010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2010, 99999, 'P', 42010, 'Vy', 32010, 'Vz', 22010, 'My', 12010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172010, 72010, 172010, 2010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123010, 123010, 23010, 2010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172011, 9.6, 7.3, 5.95)
    ops.node(123011, 9.6, 7.3, 8.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2011, 172011, 123011, 0.1225, 27951959.79522955, 11646649.91467898, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22011, 68.29302959, 0.00063784, 82.88233828, 0.02735003, 8.28823383, 0.07475369, -68.29302959, -0.00063784, -82.88233828, -0.02735003, -8.28823383, -0.07475369, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12011, 64.91945673, 0.00063784, 78.78807553, 0.02735003, 7.87880755, 0.07475369, -64.91945673, -0.00063784, -78.78807553, -0.02735003, -7.87880755, -0.07475369, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22011, 2011, 0.0, 118.99499092, 0.01275689, 118.99499092, 0.03827066, 83.29649364, -1438.76990736, 0.05, 2, 0, 72011, 23011, 2, 3)
    ops.uniaxialMaterial('LimitState', 42011, 29.74874773, 7.131e-05, 89.24624319, 0.00021393, 297.48747729, 0.00071311, -29.74874773, -7.131e-05, -89.24624319, -0.00021393, -297.48747729, -0.00071311, 0.4, 0.3, 0.003, 0.0, 0.0, 22011, 2)
    ops.limitCurve('ThreePoint', 12011, 2011, 0.0, 118.99499092, 0.01275689, 118.99499092, 0.03827066, 83.29649364, -1438.76990736, 0.05, 2, 0, 72011, 23011, 1, 3)
    ops.uniaxialMaterial('LimitState', 32011, 29.74874773, 7.131e-05, 89.24624319, 0.00021393, 297.48747729, 0.00071311, -29.74874773, -7.131e-05, -89.24624319, -0.00021393, -297.48747729, -0.00071311, 0.4, 0.3, 0.003, 0.0, 0.0, 12011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2011, 99999, 'P', 42011, 'Vy', 32011, 'Vz', 22011, 'My', 12011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172011, 72011, 172011, 2011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123011, 123011, 23011, 2011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172012, 16.25, 7.3, 5.95)
    ops.node(123012, 16.25, 7.3, 8.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2012, 172012, 123012, 0.1225, 28344022.70482242, 11810009.46034267, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22012, 66.61161745, 0.00062303, 81.01885427, 0.04807257, 8.10188543, 0.14105065, -66.61161745, -0.00062303, -81.01885427, -0.04807257, -8.10188543, -0.14105065, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12012, 66.61161745, 0.00062303, 81.01885427, 0.04807257, 8.10188543, 0.14105065, -66.61161745, -0.00062303, -81.01885427, -0.04807257, -8.10188543, -0.14105065, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22012, 2012, 0.0, 161.52108153, 0.01246068, 161.52108153, 0.03738203, 113.06475707, -4307.89356555, 0.05, 2, 0, 72012, 23012, 2, 3)
    ops.uniaxialMaterial('LimitState', 42012, 40.38027038, 9.546e-05, 121.14081115, 0.00028637, 403.80270383, 0.00095457, -40.38027038, -9.546e-05, -121.14081115, -0.00028637, -403.80270383, -0.00095457, 0.4, 0.3, 0.003, 0.0, 0.0, 22012, 2)
    ops.limitCurve('ThreePoint', 12012, 2012, 0.0, 161.52108153, 0.01246068, 161.52108153, 0.03738203, 113.06475707, -4307.89356555, 0.05, 2, 0, 72012, 23012, 1, 3)
    ops.uniaxialMaterial('LimitState', 32012, 40.38027038, 9.546e-05, 121.14081115, 0.00028637, 403.80270383, 0.00095457, -40.38027038, -9.546e-05, -121.14081115, -0.00028637, -403.80270383, -0.00095457, 0.4, 0.3, 0.003, 0.0, 0.0, 12012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2012, 99999, 'P', 42012, 'Vy', 32012, 'Vz', 22012, 'My', 12012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172012, 72012, 172012, 2012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123012, 123012, 23012, 2012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172013, 0.0, 10.95, 5.95)
    ops.node(123013, 0.0, 10.95, 8.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2013, 172013, 123013, 0.0625, 26951226.28414627, 11229677.61839428, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22013, 19.32456363, 0.00075271, 23.56099666, 0.02262993, 2.35609967, 0.0779885, -19.32456363, -0.00075271, -23.56099666, -0.02262993, -2.35609967, -0.0779885, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12013, 19.32456363, 0.00075271, 23.56099666, 0.02262993, 2.35609967, 0.0779885, -19.32456363, -0.00075271, -23.56099666, -0.02262993, -2.35609967, -0.0779885, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22013, 2013, 0.0, 59.11827163, 0.01505413, 59.11827163, 0.04516239, 41.38279014, -923.73022684, 0.05, 2, 0, 72013, 23013, 2, 3)
    ops.uniaxialMaterial('LimitState', 42013, 14.77956791, 7.202e-05, 44.33870373, 0.00021605, 147.79567909, 0.00072018, -14.77956791, -7.202e-05, -44.33870373, -0.00021605, -147.79567909, -0.00072018, 0.4, 0.3, 0.003, 0.0, 0.0, 22013, 2)
    ops.limitCurve('ThreePoint', 12013, 2013, 0.0, 59.11827163, 0.01505413, 59.11827163, 0.04516239, 41.38279014, -923.73022684, 0.05, 2, 0, 72013, 23013, 1, 3)
    ops.uniaxialMaterial('LimitState', 32013, 14.77956791, 7.202e-05, 44.33870373, 0.00021605, 147.79567909, 0.00072018, -14.77956791, -7.202e-05, -44.33870373, -0.00021605, -147.79567909, -0.00072018, 0.4, 0.3, 0.003, 0.0, 0.0, 12013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2013, 99999, 'P', 42013, 'Vy', 32013, 'Vz', 22013, 'My', 12013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172013, 72013, 172013, 2013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123013, 123013, 23013, 2013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172014, 2.95, 10.95, 5.95)
    ops.node(123014, 2.95, 10.95, 8.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2014, 172014, 123014, 0.1225, 27286947.98524707, 11369561.66051961, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22014, 61.86953268, 0.00061468, 75.33529623, 0.0350754, 7.53352962, 0.09790449, -61.86953268, -0.00061468, -75.33529623, -0.0350754, -7.53352962, -0.09790449, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12014, 58.40870609, 0.00061468, 71.12122857, 0.0350754, 7.11212286, 0.09790449, -58.40870609, -0.00061468, -71.12122857, -0.0350754, -7.11212286, -0.09790449, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22014, 2014, 0.0, 128.61954664, 0.01229358, 128.61954664, 0.03688073, 90.03368265, -2235.09403639, 0.05, 2, 0, 72014, 23014, 2, 3)
    ops.uniaxialMaterial('LimitState', 42014, 32.15488666, 7.896e-05, 96.46465998, 0.00023687, 321.54886661, 0.00078957, -32.15488666, -7.896e-05, -96.46465998, -0.00023687, -321.54886661, -0.00078957, 0.4, 0.3, 0.003, 0.0, 0.0, 22014, 2)
    ops.limitCurve('ThreePoint', 12014, 2014, 0.0, 128.61954664, 0.01229358, 128.61954664, 0.03688073, 90.03368265, -2235.09403639, 0.05, 2, 0, 72014, 23014, 1, 3)
    ops.uniaxialMaterial('LimitState', 32014, 32.15488666, 7.896e-05, 96.46465998, 0.00023687, 321.54886661, 0.00078957, -32.15488666, -7.896e-05, -96.46465998, -0.00023687, -321.54886661, -0.00078957, 0.4, 0.3, 0.003, 0.0, 0.0, 12014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2014, 99999, 'P', 42014, 'Vy', 32014, 'Vz', 22014, 'My', 12014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172014, 72014, 172014, 2014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123014, 123014, 23014, 2014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172015, 9.6, 10.95, 5.95)
    ops.node(123015, 9.6, 10.95, 8.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2015, 172015, 123015, 0.1225, 27786675.74057118, 11577781.55857133, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22015, 69.57716705, 0.00062012, 84.46097206, 0.02772862, 8.44609721, 0.07489086, -69.57716705, -0.00062012, -84.46097206, -0.02772862, -8.44609721, -0.07489086, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12015, 65.86168372, 0.00062012, 79.95068015, 0.02772862, 7.99506802, 0.07489086, -65.86168372, -0.00062012, -79.95068015, -0.02772862, -7.99506802, -0.07489086, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22015, 2015, 0.0, 120.10776601, 0.01240249, 120.10776601, 0.03720746, 84.0754362, -1498.6541274, 0.05, 2, 0, 72015, 23015, 2, 3)
    ops.uniaxialMaterial('LimitState', 42015, 30.0269415, 7.241e-05, 90.0808245, 0.00021722, 300.26941501, 0.00072406, -30.0269415, -7.241e-05, -90.0808245, -0.00021722, -300.26941501, -0.00072406, 0.4, 0.3, 0.003, 0.0, 0.0, 22015, 2)
    ops.limitCurve('ThreePoint', 12015, 2015, 0.0, 120.10776601, 0.01240249, 120.10776601, 0.03720746, 84.0754362, -1498.6541274, 0.05, 2, 0, 72015, 23015, 1, 3)
    ops.uniaxialMaterial('LimitState', 32015, 30.0269415, 7.241e-05, 90.0808245, 0.00021722, 300.26941501, 0.00072406, -30.0269415, -7.241e-05, -90.0808245, -0.00021722, -300.26941501, -0.00072406, 0.4, 0.3, 0.003, 0.0, 0.0, 12015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2015, 99999, 'P', 42015, 'Vy', 32015, 'Vz', 22015, 'My', 12015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172015, 72015, 172015, 2015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123015, 123015, 23015, 2015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172016, 16.25, 10.95, 5.95)
    ops.node(123016, 16.25, 10.95, 8.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2016, 172016, 123016, 0.1225, 27432290.77154844, 11430121.15481185, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22016, 68.17132487, 0.00063421, 83.05240685, 0.04808693, 8.30524068, 0.13935926, -68.17132487, -0.00063421, -83.05240685, -0.04808693, -8.30524068, -0.13935926, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12016, 68.17132487, 0.00063421, 83.05240685, 0.04808693, 8.30524068, 0.13935926, -68.17132487, -0.00063421, -83.05240685, -0.04808693, -8.30524068, -0.13935926, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22016, 2016, 0.0, 155.27350747, 0.01268425, 155.27350747, 0.03805276, 108.69145523, -4083.68474788, 0.05, 2, 0, 72016, 23016, 2, 3)
    ops.uniaxialMaterial('LimitState', 42016, 38.81837687, 9.481e-05, 116.4551306, 0.00028444, 388.18376868, 0.00094815, -38.81837687, -9.481e-05, -116.4551306, -0.00028444, -388.18376868, -0.00094815, 0.4, 0.3, 0.003, 0.0, 0.0, 22016, 2)
    ops.limitCurve('ThreePoint', 12016, 2016, 0.0, 155.27350747, 0.01268425, 155.27350747, 0.03805276, 108.69145523, -4083.68474788, 0.05, 2, 0, 72016, 23016, 1, 3)
    ops.uniaxialMaterial('LimitState', 32016, 38.81837687, 9.481e-05, 116.4551306, 0.00028444, 388.18376868, 0.00094815, -38.81837687, -9.481e-05, -116.4551306, -0.00028444, -388.18376868, -0.00094815, 0.4, 0.3, 0.003, 0.0, 0.0, 12016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2016, 99999, 'P', 42016, 'Vy', 32016, 'Vz', 22016, 'My', 12016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172016, 72016, 172016, 2016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123016, 123016, 23016, 2016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172017, 0.0, 14.6, 5.95)
    ops.node(123017, 0.0, 14.6, 8.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2017, 172017, 123017, 0.0625, 26366582.23586136, 10986075.9316089, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22017, 18.85062094, 0.00075507, 23.00210946, 0.02264927, 2.30021095, 0.0772157, -18.85062094, -0.00075507, -23.00210946, -0.02264927, -2.30021095, -0.0772157, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12017, 18.85062094, 0.00075507, 23.00210946, 0.02264927, 2.30021095, 0.0772157, -18.85062094, -0.00075507, -23.00210946, -0.02264927, -2.30021095, -0.0772157, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22017, 2017, 0.0, 57.81589603, 0.01510148, 57.81589603, 0.04530443, 40.47112722, -909.93597963, 0.05, 2, 0, 72017, 23017, 2, 3)
    ops.uniaxialMaterial('LimitState', 42017, 14.45397401, 7.199e-05, 43.36192202, 0.00021598, 144.53974007, 0.00071993, -14.45397401, -7.199e-05, -43.36192202, -0.00021598, -144.53974007, -0.00071993, 0.4, 0.3, 0.003, 0.0, 0.0, 22017, 2)
    ops.limitCurve('ThreePoint', 12017, 2017, 0.0, 57.81589603, 0.01510148, 57.81589603, 0.04530443, 40.47112722, -909.93597963, 0.05, 2, 0, 72017, 23017, 1, 3)
    ops.uniaxialMaterial('LimitState', 32017, 14.45397401, 7.199e-05, 43.36192202, 0.00021598, 144.53974007, 0.00071993, -14.45397401, -7.199e-05, -43.36192202, -0.00021598, -144.53974007, -0.00071993, 0.4, 0.3, 0.003, 0.0, 0.0, 12017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2017, 99999, 'P', 42017, 'Vy', 32017, 'Vz', 22017, 'My', 12017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172017, 72017, 172017, 2017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123017, 123017, 23017, 2017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172018, 2.95, 14.6, 5.95)
    ops.node(123018, 2.95, 14.6, 8.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2018, 172018, 123018, 0.1225, 29561045.92235452, 12317102.46764771, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22018, 63.19838857, 0.00060597, 76.62320707, 0.03423245, 7.66232071, 0.10015662, -63.19838857, -0.00060597, -76.62320707, -0.03423245, -7.66232071, -0.10015662, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12018, 59.63380227, 0.00060597, 72.30141912, 0.03423245, 7.23014191, 0.10015662, -59.63380227, -0.00060597, -72.30141912, -0.03423245, -7.23014191, -0.10015662, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22018, 2018, 0.0, 135.43125603, 0.01211937, 135.43125603, 0.0363581, 94.80187922, -2171.55755987, 0.05, 2, 0, 72018, 23018, 2, 3)
    ops.uniaxialMaterial('LimitState', 42018, 33.85781401, 7.674e-05, 101.57344202, 0.00023023, 338.57814008, 0.00076743, -33.85781401, -7.674e-05, -101.57344202, -0.00023023, -338.57814008, -0.00076743, 0.4, 0.3, 0.003, 0.0, 0.0, 22018, 2)
    ops.limitCurve('ThreePoint', 12018, 2018, 0.0, 135.43125603, 0.01211937, 135.43125603, 0.0363581, 94.80187922, -2171.55755987, 0.05, 2, 0, 72018, 23018, 1, 3)
    ops.uniaxialMaterial('LimitState', 32018, 33.85781401, 7.674e-05, 101.57344202, 0.00023023, 338.57814008, 0.00076743, -33.85781401, -7.674e-05, -101.57344202, -0.00023023, -338.57814008, -0.00076743, 0.4, 0.3, 0.003, 0.0, 0.0, 12018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2018, 99999, 'P', 42018, 'Vy', 32018, 'Vz', 22018, 'My', 12018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172018, 72018, 172018, 2018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123018, 123018, 23018, 2018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172019, 9.6, 14.6, 5.95)
    ops.node(123019, 9.6, 14.6, 8.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2019, 172019, 123019, 0.1225, 27613911.03063542, 11505796.26276476, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22019, 69.86496487, 0.000623, 84.83059044, 0.02740507, 8.48305904, 0.0743096, -69.86496487, -0.000623, -84.83059044, -0.02740507, -8.48305904, -0.0743096, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12019, 66.11377343, 0.000623, 80.27586426, 0.02740507, 8.02758643, 0.0743096, -66.11377343, -0.000623, -80.27586426, -0.02740507, -8.02758643, -0.0743096, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22019, 2019, 0.0, 118.9042939, 0.01246006, 118.9042939, 0.03738019, 83.23300573, -1477.69992464, 0.05, 2, 0, 72019, 23019, 2, 3)
    ops.uniaxialMaterial('LimitState', 42019, 29.72607348, 7.213e-05, 89.17822043, 0.00021639, 297.26073476, 0.00072129, -29.72607348, -7.213e-05, -89.17822043, -0.00021639, -297.26073476, -0.00072129, 0.4, 0.3, 0.003, 0.0, 0.0, 22019, 2)
    ops.limitCurve('ThreePoint', 12019, 2019, 0.0, 118.9042939, 0.01246006, 118.9042939, 0.03738019, 83.23300573, -1477.69992464, 0.05, 2, 0, 72019, 23019, 1, 3)
    ops.uniaxialMaterial('LimitState', 32019, 29.72607348, 7.213e-05, 89.17822043, 0.00021639, 297.26073476, 0.00072129, -29.72607348, -7.213e-05, -89.17822043, -0.00021639, -297.26073476, -0.00072129, 0.4, 0.3, 0.003, 0.0, 0.0, 12019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2019, 99999, 'P', 42019, 'Vy', 32019, 'Vz', 22019, 'My', 12019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172019, 72019, 172019, 2019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123019, 123019, 23019, 2019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172020, 16.25, 14.6, 5.95)
    ops.node(123020, 16.25, 14.6, 8.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2020, 172020, 123020, 0.1225, 27744747.66448511, 11560311.5268688, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22020, 68.34662176, 0.0006232, 83.22149238, 0.04833287, 8.32214924, 0.1402136, -68.34662176, -0.0006232, -83.22149238, -0.04833287, -8.32214924, -0.1402136, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12020, 68.34662176, 0.0006232, 83.22149238, 0.04833287, 8.32214924, 0.1402136, -68.34662176, -0.0006232, -83.22149238, -0.04833287, -8.32214924, -0.1402136, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22020, 2020, 0.0, 161.29950984, 0.01246409, 161.29950984, 0.03739228, 112.90965689, -4448.91027635, 0.05, 2, 0, 72020, 23020, 2, 3)
    ops.uniaxialMaterial('LimitState', 42020, 40.32487746, 9.739e-05, 120.97463238, 0.00029216, 403.24877461, 0.00097385, -40.32487746, -9.739e-05, -120.97463238, -0.00029216, -403.24877461, -0.00097385, 0.4, 0.3, 0.003, 0.0, 0.0, 22020, 2)
    ops.limitCurve('ThreePoint', 12020, 2020, 0.0, 161.29950984, 0.01246409, 161.29950984, 0.03739228, 112.90965689, -4448.91027635, 0.05, 2, 0, 72020, 23020, 1, 3)
    ops.uniaxialMaterial('LimitState', 32020, 40.32487746, 9.739e-05, 120.97463238, 0.00029216, 403.24877461, 0.00097385, -40.32487746, -9.739e-05, -120.97463238, -0.00029216, -403.24877461, -0.00097385, 0.4, 0.3, 0.003, 0.0, 0.0, 12020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2020, 99999, 'P', 42020, 'Vy', 32020, 'Vz', 22020, 'My', 12020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172020, 72020, 172020, 2020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123020, 123020, 23020, 2020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172021, 0.0, 18.25, 5.95)
    ops.node(123021, 0.0, 18.25, 8.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2021, 172021, 123021, 0.0625, 27358059.12289379, 11399191.30120574, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22021, 18.98598346, 0.00074907, 23.13339186, 0.02245385, 2.31333919, 0.07832726, -18.98598346, -0.00074907, -23.13339186, -0.02245385, -2.31333919, -0.07832726, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12021, 18.98598346, 0.00074907, 23.13339186, 0.02245385, 2.31333919, 0.07832726, -18.98598346, -0.00074907, -23.13339186, -0.02245385, -2.31333919, -0.07832726, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22021, 2021, 0.0, 59.20696022, 0.0149813, 59.20696022, 0.0449439, 41.44487215, -893.81930239, 0.05, 2, 0, 72021, 23021, 2, 3)
    ops.uniaxialMaterial('LimitState', 42021, 14.80174005, 7.105e-05, 44.40522016, 0.00021316, 148.01740054, 0.00071053, -14.80174005, -7.105e-05, -44.40522016, -0.00021316, -148.01740054, -0.00071053, 0.4, 0.3, 0.003, 0.0, 0.0, 22021, 2)
    ops.limitCurve('ThreePoint', 12021, 2021, 0.0, 59.20696022, 0.0149813, 59.20696022, 0.0449439, 41.44487215, -893.81930239, 0.05, 2, 0, 72021, 23021, 1, 3)
    ops.uniaxialMaterial('LimitState', 32021, 14.80174005, 7.105e-05, 44.40522016, 0.00021316, 148.01740054, 0.00071053, -14.80174005, -7.105e-05, -44.40522016, -0.00021316, -148.01740054, -0.00071053, 0.4, 0.3, 0.003, 0.0, 0.0, 12021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2021, 99999, 'P', 42021, 'Vy', 32021, 'Vz', 22021, 'My', 12021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172021, 72021, 172021, 2021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123021, 123021, 23021, 2021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172022, 2.95, 18.25, 5.95)
    ops.node(123022, 2.95, 18.25, 8.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2022, 172022, 123022, 0.1225, 27205570.22213296, 11335654.25922207, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22022, 62.01659909, 0.0006017, 75.52363133, 0.0352368, 7.55236313, 0.09793695, -62.01659909, -0.0006017, -75.52363133, -0.0352368, -7.55236313, -0.09793695, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12022, 58.43062376, 0.0006017, 71.15664115, 0.0352368, 7.11566411, 0.09793695, -58.43062376, -0.0006017, -71.15664115, -0.0352368, -7.11566411, -0.09793695, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22022, 2022, 0.0, 128.25169426, 0.01203405, 128.25169426, 0.03610214, 89.77618598, -2230.75316861, 0.05, 2, 0, 72022, 23022, 2, 3)
    ops.uniaxialMaterial('LimitState', 42022, 32.06292356, 7.897e-05, 96.18877069, 0.0002369, 320.62923564, 0.00078967, -32.06292356, -7.897e-05, -96.18877069, -0.0002369, -320.62923564, -0.00078967, 0.4, 0.3, 0.003, 0.0, 0.0, 22022, 2)
    ops.limitCurve('ThreePoint', 12022, 2022, 0.0, 128.25169426, 0.01203405, 128.25169426, 0.03610214, 89.77618598, -2230.75316861, 0.05, 2, 0, 72022, 23022, 1, 3)
    ops.uniaxialMaterial('LimitState', 32022, 32.06292356, 7.897e-05, 96.18877069, 0.0002369, 320.62923564, 0.00078967, -32.06292356, -7.897e-05, -96.18877069, -0.0002369, -320.62923564, -0.00078967, 0.4, 0.3, 0.003, 0.0, 0.0, 12022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2022, 99999, 'P', 42022, 'Vy', 32022, 'Vz', 22022, 'My', 12022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172022, 72022, 172022, 2022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123022, 123022, 23022, 2022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172023, 9.6, 18.25, 5.95)
    ops.node(123023, 9.6, 18.25, 8.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2023, 172023, 123023, 0.1225, 27498258.771178, 11457607.82132417, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22023, 68.99940528, 0.00061996, 83.79249256, 0.02771521, 8.37924926, 0.07444409, -68.99940528, -0.00061996, -83.79249256, -0.02771521, -8.37924926, -0.07444409, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12023, 65.34574322, 0.00061996, 79.35550577, 0.02771521, 7.93555058, 0.07444409, -65.34574322, -0.00061996, -79.35550577, -0.02771521, -7.93555058, -0.07444409, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22023, 2023, 0.0, 118.30700402, 0.01239926, 118.30700402, 0.03719779, 82.81490281, -1471.04508991, 0.05, 2, 0, 72023, 23023, 2, 3)
    ops.uniaxialMaterial('LimitState', 42023, 29.576751, 7.207e-05, 88.73025301, 0.00021621, 295.76751005, 0.00072069, -29.576751, -7.207e-05, -88.73025301, -0.00021621, -295.76751005, -0.00072069, 0.4, 0.3, 0.003, 0.0, 0.0, 22023, 2)
    ops.limitCurve('ThreePoint', 12023, 2023, 0.0, 118.30700402, 0.01239926, 118.30700402, 0.03719779, 82.81490281, -1471.04508991, 0.05, 2, 0, 72023, 23023, 1, 3)
    ops.uniaxialMaterial('LimitState', 32023, 29.576751, 7.207e-05, 88.73025301, 0.00021621, 295.76751005, 0.00072069, -29.576751, -7.207e-05, -88.73025301, -0.00021621, -295.76751005, -0.00072069, 0.4, 0.3, 0.003, 0.0, 0.0, 12023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2023, 99999, 'P', 42023, 'Vy', 32023, 'Vz', 22023, 'My', 12023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172023, 72023, 172023, 2023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123023, 123023, 23023, 2023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172024, 16.25, 18.25, 5.95)
    ops.node(123024, 16.25, 18.25, 8.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2024, 172024, 123024, 0.1225, 28548679.90146926, 11895283.29227886, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22024, 68.86612121, 0.00062314, 83.72707573, 0.04802183, 8.37270757, 0.14135489, -68.86612121, -0.00062314, -83.72707573, -0.04802183, -8.37270757, -0.14135489, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12024, 68.86612121, 0.00062314, 83.72707573, 0.04802183, 8.37270757, 0.14135489, -68.86612121, -0.00062314, -83.72707573, -0.04802183, -8.37270757, -0.14135489, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22024, 2024, 0.0, 164.4175156, 0.01246286, 164.4175156, 0.03738857, 115.09226092, -4470.76791099, 0.05, 2, 0, 72024, 23024, 2, 3)
    ops.uniaxialMaterial('LimitState', 42024, 41.1043789, 9.647e-05, 123.3131367, 0.00028942, 411.043789, 0.00096472, -41.1043789, -9.647e-05, -123.3131367, -0.00028942, -411.043789, -0.00096472, 0.4, 0.3, 0.003, 0.0, 0.0, 22024, 2)
    ops.limitCurve('ThreePoint', 12024, 2024, 0.0, 164.4175156, 0.01246286, 164.4175156, 0.03738857, 115.09226092, -4470.76791099, 0.05, 2, 0, 72024, 23024, 1, 3)
    ops.uniaxialMaterial('LimitState', 32024, 41.1043789, 9.647e-05, 123.3131367, 0.00028942, 411.043789, 0.00096472, -41.1043789, -9.647e-05, -123.3131367, -0.00028942, -411.043789, -0.00096472, 0.4, 0.3, 0.003, 0.0, 0.0, 12024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2024, 99999, 'P', 42024, 'Vy', 32024, 'Vz', 22024, 'My', 12024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172024, 72024, 172024, 2024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123024, 123024, 23024, 2024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172025, 0.0, 21.9, 6.0)
    ops.node(123025, 0.0, 21.9, 8.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2025, 172025, 123025, 0.0625, 28268445.41777076, 11778518.92407115, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22025, 16.64065153, 0.0007322, 20.28760865, 0.023222, 2.02876086, 0.08402091, -16.64065153, -0.0007322, -20.28760865, -0.023222, -2.02876086, -0.08402091, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12025, 16.64065153, 0.0007322, 20.28760865, 0.023222, 2.02876086, 0.08402091, -16.64065153, -0.0007322, -20.28760865, -0.023222, -2.02876086, -0.08402091, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22025, 2025, 0.0, 59.16998775, 0.01464401, 59.16998775, 0.04393204, 41.41899142, -1160.5353503, 0.05, 2, 0, 72025, 23025, 2, 3)
    ops.uniaxialMaterial('LimitState', 42025, 14.79249694, 6.872e-05, 44.37749081, 0.00020617, 147.92496937, 0.00068722, -14.79249694, -6.872e-05, -44.37749081, -0.00020617, -147.92496937, -0.00068722, 0.4, 0.3, 0.003, 0.0, 0.0, 22025, 2)
    ops.limitCurve('ThreePoint', 12025, 2025, 0.0, 59.16998775, 0.01464401, 59.16998775, 0.04393204, 41.41899142, -1160.5353503, 0.05, 2, 0, 72025, 23025, 1, 3)
    ops.uniaxialMaterial('LimitState', 32025, 14.79249694, 6.872e-05, 44.37749081, 0.00020617, 147.92496937, 0.00068722, -14.79249694, -6.872e-05, -44.37749081, -0.00020617, -147.92496937, -0.00068722, 0.4, 0.3, 0.003, 0.0, 0.0, 12025, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2025, 99999, 'P', 42025, 'Vy', 32025, 'Vz', 22025, 'My', 12025, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172025, 72025, 172025, 2025, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123025, 123025, 23025, 2025, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172026, 2.95, 21.9, 6.0)
    ops.node(123026, 2.95, 21.9, 8.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2026, 172026, 123026, 0.0625, 27481665.46781997, 11450693.94492499, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22026, 22.25798511, 0.000776, 27.03173197, 0.0218272, 2.7031732, 0.07296627, -22.25798511, -0.000776, -27.03173197, -0.0218272, -2.7031732, -0.07296627, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12026, 22.25798511, 0.000776, 27.03173197, 0.0218272, 2.7031732, 0.07296627, -22.25798511, -0.000776, -27.03173197, -0.0218272, -2.7031732, -0.07296627, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22026, 2026, 0.0, 63.14753344, 0.01551994, 63.14753344, 0.04655982, 44.20327341, -855.02896645, 0.05, 2, 0, 72026, 23026, 2, 3)
    ops.uniaxialMaterial('LimitState', 42026, 15.78688336, 7.544e-05, 47.36065008, 0.00022632, 157.86883361, 0.00075442, -15.78688336, -7.544e-05, -47.36065008, -0.00022632, -157.86883361, -0.00075442, 0.4, 0.3, 0.003, 0.0, 0.0, 22026, 2)
    ops.limitCurve('ThreePoint', 12026, 2026, 0.0, 63.14753344, 0.01551994, 63.14753344, 0.04655982, 44.20327341, -855.02896645, 0.05, 2, 0, 72026, 23026, 1, 3)
    ops.uniaxialMaterial('LimitState', 32026, 15.78688336, 7.544e-05, 47.36065008, 0.00022632, 157.86883361, 0.00075442, -15.78688336, -7.544e-05, -47.36065008, -0.00022632, -157.86883361, -0.00075442, 0.4, 0.3, 0.003, 0.0, 0.0, 12026, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2026, 99999, 'P', 42026, 'Vy', 32026, 'Vz', 22026, 'My', 12026, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172026, 72026, 172026, 2026, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123026, 123026, 23026, 2026, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172027, 9.6, 21.9, 6.0)
    ops.node(123027, 9.6, 21.9, 8.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2027, 172027, 123027, 0.1225, 25944895.63551983, 10810373.1814666, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22027, 56.10678688, 0.00059698, 68.46670331, 0.02500689, 6.84667033, 0.07365425, -56.10678688, -0.00059698, -68.46670331, -0.02500689, -6.84667033, -0.07365425, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12027, 49.03620482, 0.00059698, 59.83852353, 0.02500689, 5.98385235, 0.07365425, -49.03620482, -0.00059698, -59.83852353, -0.02500689, -5.98385235, -0.07365425, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22027, 2027, 0.0, 107.46876528, 0.01193969, 107.46876528, 0.03581908, 75.2281357, -1522.19670586, 0.05, 2, 0, 72027, 23027, 2, 3)
    ops.uniaxialMaterial('LimitState', 42027, 26.86719132, 6.939e-05, 80.60157396, 0.00020816, 268.67191321, 0.00069386, -26.86719132, -6.939e-05, -80.60157396, -0.00020816, -268.67191321, -0.00069386, 0.4, 0.3, 0.003, 0.0, 0.0, 22027, 2)
    ops.limitCurve('ThreePoint', 12027, 2027, 0.0, 107.46876528, 0.01193969, 107.46876528, 0.03581908, 75.2281357, -1522.19670586, 0.05, 2, 0, 72027, 23027, 1, 3)
    ops.uniaxialMaterial('LimitState', 32027, 26.86719132, 6.939e-05, 80.60157396, 0.00020816, 268.67191321, 0.00069386, -26.86719132, -6.939e-05, -80.60157396, -0.00020816, -268.67191321, -0.00069386, 0.4, 0.3, 0.003, 0.0, 0.0, 12027, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2027, 99999, 'P', 42027, 'Vy', 32027, 'Vz', 22027, 'My', 12027, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172027, 72027, 172027, 2027, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123027, 123027, 23027, 2027, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172028, 16.25, 21.9, 6.0)
    ops.node(123028, 16.25, 21.9, 8.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2028, 172028, 123028, 0.0625, 28437746.00914134, 11849060.83714222, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22028, 28.48021309, 0.00080781, 34.6061058, 0.02717697, 3.46061058, 0.0829344, -28.48021309, -0.00080781, -34.6061058, -0.02717697, -3.46061058, -0.0829344, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12028, 28.48021309, 0.00080781, 34.6061058, 0.02717697, 3.46061058, 0.0829344, -28.48021309, -0.00080781, -34.6061058, -0.02717697, -3.46061058, -0.0829344, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22028, 2028, 0.0, 63.03019848, 0.01615622, 63.03019848, 0.04846865, 44.12113893, -906.13667549, 0.05, 2, 0, 72028, 23028, 2, 3)
    ops.uniaxialMaterial('LimitState', 42028, 15.75754962, 7.277e-05, 47.27264886, 0.00021831, 157.57549619, 0.0007277, -15.75754962, -7.277e-05, -47.27264886, -0.00021831, -157.57549619, -0.0007277, 0.4, 0.3, 0.003, 0.0, 0.0, 22028, 2)
    ops.limitCurve('ThreePoint', 12028, 2028, 0.0, 63.03019848, 0.01615622, 63.03019848, 0.04846865, 44.12113893, -906.13667549, 0.05, 2, 0, 72028, 23028, 1, 3)
    ops.uniaxialMaterial('LimitState', 32028, 15.75754962, 7.277e-05, 47.27264886, 0.00021831, 157.57549619, 0.0007277, -15.75754962, -7.277e-05, -47.27264886, -0.00021831, -157.57549619, -0.0007277, 0.4, 0.3, 0.003, 0.0, 0.0, 12028, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2028, 99999, 'P', 42028, 'Vy', 32028, 'Vz', 22028, 'My', 12028, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172028, 72028, 172028, 2028, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123028, 123028, 23028, 2028, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173003, 9.6, 0.0, 8.85)
    ops.node(124003, 9.6, 0.0, 11.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3003, 173003, 124003, 0.1225, 27229633.27405487, 11345680.5308562, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23003, 42.51747447, 0.0005837, 52.04248825, 0.0219605, 5.20424882, 0.07095729, -42.51747447, -0.0005837, -52.04248825, -0.0219605, -5.20424882, -0.07095729, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13003, 36.23218403, 0.0005837, 44.34913021, 0.0219605, 4.43491302, 0.07095729, -36.23218403, -0.0005837, -44.34913021, -0.0219605, -4.43491302, -0.07095729, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23003, 3003, 0.0, 95.34162143, 0.01167407, 95.34162143, 0.03502222, 66.739135, -2106.00122253, 0.05, 2, 0, 73003, 24003, 2, 3)
    ops.uniaxialMaterial('LimitState', 43003, 23.83540536, 5.865e-05, 71.50621607, 0.00017596, 238.35405357, 0.00058652, -23.83540536, -5.865e-05, -71.50621607, -0.00017596, -238.35405357, -0.00058652, 0.4, 0.3, 0.003, 0.0, 0.0, 23003, 2)
    ops.limitCurve('ThreePoint', 13003, 3003, 0.0, 95.34162143, 0.01167407, 95.34162143, 0.03502222, 66.739135, -2106.00122253, 0.05, 2, 0, 73003, 24003, 1, 3)
    ops.uniaxialMaterial('LimitState', 33003, 23.83540536, 5.865e-05, 71.50621607, 0.00017596, 238.35405357, 0.00058652, -23.83540536, -5.865e-05, -71.50621607, -0.00017596, -238.35405357, -0.00058652, 0.4, 0.3, 0.003, 0.0, 0.0, 13003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3003, 99999, 'P', 43003, 'Vy', 33003, 'Vz', 23003, 'My', 13003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173003, 73003, 173003, 3003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124003, 124003, 24003, 3003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173004, 16.25, 0.0, 8.85)
    ops.node(124004, 16.25, 0.0, 11.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3004, 173004, 124004, 0.0625, 27910660.76253617, 11629441.98439007, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23004, 23.28615263, 0.00075525, 28.45943076, 0.03457607, 2.84594308, 0.1110062, -23.28615263, -0.00075525, -28.45943076, -0.03457607, -2.84594308, -0.1110062, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13004, 23.28615263, 0.00075525, 28.45943076, 0.03457607, 2.84594308, 0.1110062, -23.28615263, -0.00075525, -28.45943076, -0.03457607, -2.84594308, -0.1110062, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23004, 3004, 0.0, 62.21543706, 0.01510496, 62.21543706, 0.04531488, 43.55080594, -2570.03539699, 0.05, 2, 0, 73004, 24004, 2, 3)
    ops.uniaxialMaterial('LimitState', 43004, 15.55385926, 7.319e-05, 46.66157779, 0.00021956, 155.53859264, 0.00073186, -15.55385926, -7.319e-05, -46.66157779, -0.00021956, -155.53859264, -0.00073186, 0.4, 0.3, 0.003, 0.0, 0.0, 23004, 2)
    ops.limitCurve('ThreePoint', 13004, 3004, 0.0, 62.21543706, 0.01510496, 62.21543706, 0.04531488, 43.55080594, -2570.03539699, 0.05, 2, 0, 73004, 24004, 1, 3)
    ops.uniaxialMaterial('LimitState', 33004, 15.55385926, 7.319e-05, 46.66157779, 0.00021956, 155.53859264, 0.00073186, -15.55385926, -7.319e-05, -46.66157779, -0.00021956, -155.53859264, -0.00073186, 0.4, 0.3, 0.003, 0.0, 0.0, 13004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3004, 99999, 'P', 43004, 'Vy', 33004, 'Vz', 23004, 'My', 13004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173004, 73004, 173004, 3004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124004, 124004, 24004, 3004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173005, 0.0, 3.65, 8.8)
    ops.node(124005, 0.0, 3.65, 11.175)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3005, 173005, 124005, 0.0625, 26159882.08283219, 10899950.86784675, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23005, 15.12318242, 0.00075726, 18.52640577, 0.02452891, 1.85264058, 0.08506277, -15.12318242, -0.00075726, -18.52640577, -0.02452891, -1.85264058, -0.08506277, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13005, 15.12318242, 0.00075726, 18.52640577, 0.02452891, 1.85264058, 0.08506277, -15.12318242, -0.00075726, -18.52640577, -0.02452891, -1.85264058, -0.08506277, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23005, 3005, 0.0, 55.38812425, 0.01514517, 55.38812425, 0.04543552, 38.77168697, -1358.65120322, 0.05, 2, 0, 73005, 24005, 2, 3)
    ops.uniaxialMaterial('LimitState', 43005, 13.84703106, 6.951e-05, 41.54109318, 0.00020854, 138.47031062, 0.00069515, -13.84703106, -6.951e-05, -41.54109318, -0.00020854, -138.47031062, -0.00069515, 0.4, 0.3, 0.003, 0.0, 0.0, 23005, 2)
    ops.limitCurve('ThreePoint', 13005, 3005, 0.0, 55.38812425, 0.01514517, 55.38812425, 0.04543552, 38.77168697, -1358.65120322, 0.05, 2, 0, 73005, 24005, 1, 3)
    ops.uniaxialMaterial('LimitState', 33005, 13.84703106, 6.951e-05, 41.54109318, 0.00020854, 138.47031062, 0.00069515, -13.84703106, -6.951e-05, -41.54109318, -0.00020854, -138.47031062, -0.00069515, 0.4, 0.3, 0.003, 0.0, 0.0, 13005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3005, 99999, 'P', 43005, 'Vy', 33005, 'Vz', 23005, 'My', 13005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173005, 73005, 173005, 3005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124005, 124005, 24005, 3005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173006, 2.95, 3.65, 8.8)
    ops.node(124006, 2.95, 3.65, 11.175)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3006, 173006, 124006, 0.1225, 28086811.52729093, 11702838.13637122, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23006, 50.69321979, 0.00058918, 61.87207485, 0.03699554, 6.18720749, 0.1084393, -50.69321979, -0.00058918, -61.87207485, -0.03699554, -6.18720749, -0.1084393, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13006, 47.36579956, 0.00058918, 57.81089281, 0.03699554, 5.78108928, 0.1084393, -47.36579956, -0.00058918, -57.81089281, -0.03699554, -5.78108928, -0.1084393, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23006, 3006, 0.0, 124.33574152, 0.01178364, 124.33574152, 0.03535092, 87.03501906, -3596.7406003, 0.05, 2, 0, 73006, 24006, 2, 3)
    ops.uniaxialMaterial('LimitState', 43006, 31.08393538, 7.415e-05, 93.25180614, 0.00022246, 310.83935379, 0.00074154, -31.08393538, -7.415e-05, -93.25180614, -0.00022246, -310.83935379, -0.00074154, 0.4, 0.3, 0.003, 0.0, 0.0, 23006, 2)
    ops.limitCurve('ThreePoint', 13006, 3006, 0.0, 124.33574152, 0.01178364, 124.33574152, 0.03535092, 87.03501906, -3596.7406003, 0.05, 2, 0, 73006, 24006, 1, 3)
    ops.uniaxialMaterial('LimitState', 33006, 31.08393538, 7.415e-05, 93.25180614, 0.00022246, 310.83935379, 0.00074154, -31.08393538, -7.415e-05, -93.25180614, -0.00022246, -310.83935379, -0.00074154, 0.4, 0.3, 0.003, 0.0, 0.0, 13006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3006, 99999, 'P', 43006, 'Vy', 33006, 'Vz', 23006, 'My', 13006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173006, 73006, 173006, 3006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124006, 124006, 24006, 3006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173007, 9.6, 3.65, 8.8)
    ops.node(124007, 9.6, 3.65, 11.175)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3007, 173007, 124007, 0.1225, 27499623.79075484, 11458176.57948118, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23007, 50.34185127, 0.0005897, 61.50687977, 0.02176539, 6.15068798, 0.06326372, -50.34185127, -0.0005897, -61.50687977, -0.02176539, -6.15068798, -0.06326372, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13007, 47.11712369, 0.0005897, 57.56695847, 0.02176539, 5.75669585, 0.06326372, -47.11712369, -0.0005897, -57.56695847, -0.02176539, -5.75669585, -0.06326372, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23007, 3007, 0.0, 93.1163138, 0.0117941, 93.1163138, 0.0353823, 65.18141966, -1206.91661194, 0.05, 2, 0, 73007, 24007, 2, 3)
    ops.uniaxialMaterial('LimitState', 43007, 23.27907845, 5.672e-05, 69.83723535, 0.00017016, 232.79078451, 0.00056721, -23.27907845, -5.672e-05, -69.83723535, -0.00017016, -232.79078451, -0.00056721, 0.4, 0.3, 0.003, 0.0, 0.0, 23007, 2)
    ops.limitCurve('ThreePoint', 13007, 3007, 0.0, 93.1163138, 0.0117941, 93.1163138, 0.0353823, 65.18141966, -1206.91661194, 0.05, 2, 0, 73007, 24007, 1, 3)
    ops.uniaxialMaterial('LimitState', 33007, 23.27907845, 5.672e-05, 69.83723535, 0.00017016, 232.79078451, 0.00056721, -23.27907845, -5.672e-05, -69.83723535, -0.00017016, -232.79078451, -0.00056721, 0.4, 0.3, 0.003, 0.0, 0.0, 13007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3007, 99999, 'P', 43007, 'Vy', 33007, 'Vz', 23007, 'My', 13007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173007, 73007, 173007, 3007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124007, 124007, 24007, 3007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173008, 16.25, 3.65, 8.8)
    ops.node(124008, 16.25, 3.65, 11.175)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3008, 173008, 124008, 0.1225, 27730299.67653756, 11554291.53189065, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23008, 70.81273849, 0.00061356, 86.57442415, 0.05247272, 8.65744242, 0.15247272, -70.81273849, -0.00061356, -86.57442415, -0.05247272, -8.65744242, -0.15247272, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13008, 64.8916802, 0.00061356, 79.33544113, 0.05247272, 7.93354411, 0.15247272, -64.8916802, -0.00061356, -79.33544113, -0.05247272, -7.93354411, -0.15247272, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23008, 3008, 0.0, 147.73287529, 0.01227128, 147.73287529, 0.03681385, 103.4130127, -9379.78751925, 0.05, 2, 0, 73008, 24008, 2, 3)
    ops.uniaxialMaterial('LimitState', 43008, 36.93321882, 8.924e-05, 110.79965647, 0.00026772, 369.33218822, 0.00089241, -36.93321882, -8.924e-05, -110.79965647, -0.00026772, -369.33218822, -0.00089241, 0.4, 0.3, 0.003, 0.0, 0.0, 23008, 2)
    ops.limitCurve('ThreePoint', 13008, 3008, 0.0, 147.73287529, 0.01227128, 147.73287529, 0.03681385, 103.4130127, -9379.78751925, 0.05, 2, 0, 73008, 24008, 1, 3)
    ops.uniaxialMaterial('LimitState', 33008, 36.93321882, 8.924e-05, 110.79965647, 0.00026772, 369.33218822, 0.00089241, -36.93321882, -8.924e-05, -110.79965647, -0.00026772, -369.33218822, -0.00089241, 0.4, 0.3, 0.003, 0.0, 0.0, 13008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3008, 99999, 'P', 43008, 'Vy', 33008, 'Vz', 23008, 'My', 13008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173008, 73008, 173008, 3008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124008, 124008, 24008, 3008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173009, 0.0, 7.3, 8.8)
    ops.node(124009, 0.0, 7.3, 11.175)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3009, 173009, 124009, 0.0625, 27558125.32389544, 11482552.21828977, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23009, 14.41943914, 0.00072554, 17.63853714, 0.02383278, 1.76385371, 0.08756013, -14.41943914, -0.00072554, -17.63853714, -0.02383278, -1.76385371, -0.08756013, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13009, 14.41943914, 0.00072554, 17.63853714, 0.02383278, 1.76385371, 0.08756013, -14.41943914, -0.00072554, -17.63853714, -0.02383278, -1.76385371, -0.08756013, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23009, 3009, 0.0, 55.35790063, 0.0145108, 55.35790063, 0.0435324, 38.75053044, -1816.22472426, 0.05, 2, 0, 73009, 24009, 2, 3)
    ops.uniaxialMaterial('LimitState', 43009, 13.83947516, 6.595e-05, 41.51842547, 0.00019786, 138.39475158, 0.00065952, -13.83947516, -6.595e-05, -41.51842547, -0.00019786, -138.39475158, -0.00065952, 0.4, 0.3, 0.003, 0.0, 0.0, 23009, 2)
    ops.limitCurve('ThreePoint', 13009, 3009, 0.0, 55.35790063, 0.0145108, 55.35790063, 0.0435324, 38.75053044, -1816.22472426, 0.05, 2, 0, 73009, 24009, 1, 3)
    ops.uniaxialMaterial('LimitState', 33009, 13.83947516, 6.595e-05, 41.51842547, 0.00019786, 138.39475158, 0.00065952, -13.83947516, -6.595e-05, -41.51842547, -0.00019786, -138.39475158, -0.00065952, 0.4, 0.3, 0.003, 0.0, 0.0, 13009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3009, 99999, 'P', 43009, 'Vy', 33009, 'Vz', 23009, 'My', 13009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173009, 73009, 173009, 3009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124009, 124009, 24009, 3009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173010, 2.95, 7.3, 8.8)
    ops.node(124010, 2.95, 7.3, 11.175)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3010, 173010, 124010, 0.1225, 27419561.66541083, 11424817.36058785, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23010, 47.8931641, 0.00059208, 58.56912621, 0.03749141, 5.85691262, 0.1096167, -47.8931641, -0.00059208, -58.56912621, -0.03749141, -5.85691262, -0.1096167, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13010, 44.77891078, 0.00059208, 54.76066838, 0.03749141, 5.47606684, 0.1096167, -44.77891078, -0.00059208, -54.76066838, -0.03749141, -5.47606684, -0.1096167, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23010, 3010, 0.0, 120.07559181, 0.01184157, 120.07559181, 0.0355247, 84.05291427, -4065.98540542, 0.05, 2, 0, 73010, 24010, 2, 3)
    ops.uniaxialMaterial('LimitState', 43010, 30.01889795, 7.336e-05, 90.05669386, 0.00022007, 300.18897954, 0.00073356, -30.01889795, -7.336e-05, -90.05669386, -0.00022007, -300.18897954, -0.00073356, 0.4, 0.3, 0.003, 0.0, 0.0, 23010, 2)
    ops.limitCurve('ThreePoint', 13010, 3010, 0.0, 120.07559181, 0.01184157, 120.07559181, 0.0355247, 84.05291427, -4065.98540542, 0.05, 2, 0, 73010, 24010, 1, 3)
    ops.uniaxialMaterial('LimitState', 33010, 30.01889795, 7.336e-05, 90.05669386, 0.00022007, 300.18897954, 0.00073356, -30.01889795, -7.336e-05, -90.05669386, -0.00022007, -300.18897954, -0.00073356, 0.4, 0.3, 0.003, 0.0, 0.0, 13010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3010, 99999, 'P', 43010, 'Vy', 33010, 'Vz', 23010, 'My', 13010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173010, 73010, 173010, 3010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124010, 124010, 24010, 3010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173011, 9.6, 7.3, 8.8)
    ops.node(124011, 9.6, 7.3, 11.175)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3011, 173011, 124011, 0.1225, 27843225.51297492, 11601343.96373955, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23011, 50.64259216, 0.0005969, 61.8299554, 0.02150784, 6.18299554, 0.06315639, -50.64259216, -0.0005969, -61.8299554, -0.02150784, -6.18299554, -0.06315639, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13011, 47.44709892, 0.0005969, 57.92855155, 0.02150784, 5.79285515, 0.06315639, -47.44709892, -0.0005969, -57.92855155, -0.02150784, -5.79285515, -0.06315639, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23011, 3011, 0.0, 93.73054703, 0.01193794, 93.73054703, 0.03581381, 65.61138292, -1175.60797512, 0.05, 2, 0, 73011, 24011, 2, 3)
    ops.uniaxialMaterial('LimitState', 43011, 23.43263676, 5.639e-05, 70.29791027, 0.00016917, 234.32636757, 0.0005639, -23.43263676, -5.639e-05, -70.29791027, -0.00016917, -234.32636757, -0.0005639, 0.4, 0.3, 0.003, 0.0, 0.0, 23011, 2)
    ops.limitCurve('ThreePoint', 13011, 3011, 0.0, 93.73054703, 0.01193794, 93.73054703, 0.03581381, 65.61138292, -1175.60797512, 0.05, 2, 0, 73011, 24011, 1, 3)
    ops.uniaxialMaterial('LimitState', 33011, 23.43263676, 5.639e-05, 70.29791027, 0.00016917, 234.32636757, 0.0005639, -23.43263676, -5.639e-05, -70.29791027, -0.00016917, -234.32636757, -0.0005639, 0.4, 0.3, 0.003, 0.0, 0.0, 13011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3011, 99999, 'P', 43011, 'Vy', 33011, 'Vz', 23011, 'My', 13011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173011, 73011, 173011, 3011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124011, 124011, 24011, 3011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173012, 16.25, 7.3, 8.8)
    ops.node(124012, 16.25, 7.3, 11.175)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3012, 173012, 124012, 0.1225, 29385691.93850982, 12244038.30771242, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23012, 70.98828048, 0.00061306, 86.43930932, 0.0512662, 8.64393093, 0.1512662, -70.98828048, -0.00061306, -86.43930932, -0.0512662, -8.64393093, -0.1512662, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13012, 65.19725075, 0.00061306, 79.38782692, 0.0512662, 7.93878269, 0.1512662, -65.19725075, -0.00061306, -79.38782692, -0.0512662, -7.93878269, -0.1512662, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23012, 3012, 0.0, 153.56842107, 0.01226125, 153.56842107, 0.03678375, 107.49789475, -9388.34352173, 0.05, 2, 0, 73012, 24012, 2, 3)
    ops.uniaxialMaterial('LimitState', 43012, 38.39210527, 8.754e-05, 115.1763158, 0.00026262, 383.92105268, 0.0008754, -38.39210527, -8.754e-05, -115.1763158, -0.00026262, -383.92105268, -0.0008754, 0.4, 0.3, 0.003, 0.0, 0.0, 23012, 2)
    ops.limitCurve('ThreePoint', 13012, 3012, 0.0, 153.56842107, 0.01226125, 153.56842107, 0.03678375, 107.49789475, -9388.34352173, 0.05, 2, 0, 73012, 24012, 1, 3)
    ops.uniaxialMaterial('LimitState', 33012, 38.39210527, 8.754e-05, 115.1763158, 0.00026262, 383.92105268, 0.0008754, -38.39210527, -8.754e-05, -115.1763158, -0.00026262, -383.92105268, -0.0008754, 0.4, 0.3, 0.003, 0.0, 0.0, 13012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3012, 99999, 'P', 43012, 'Vy', 33012, 'Vz', 23012, 'My', 13012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173012, 73012, 173012, 3012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124012, 124012, 24012, 3012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173013, 0.0, 10.95, 8.8)
    ops.node(124013, 0.0, 10.95, 11.175)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3013, 173013, 124013, 0.0625, 26746104.96671351, 11144210.40279729, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23013, 14.26591898, 0.00071812, 17.48083551, 0.0248614, 1.74808355, 0.08826058, -14.26591898, -0.00071812, -17.48083551, -0.0248614, -1.74808355, -0.08826058, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13013, 14.26591898, 0.00071812, 17.48083551, 0.0248614, 1.74808355, 0.08826058, -14.26591898, -0.00071812, -17.48083551, -0.0248614, -1.74808355, -0.08826058, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23013, 3013, 0.0, 55.22580555, 0.01436241, 55.22580555, 0.04308723, 38.65806388, -1982.25543325, 0.05, 2, 0, 73013, 24013, 2, 3)
    ops.uniaxialMaterial('LimitState', 43013, 13.80645139, 6.779e-05, 41.41935416, 0.00020338, 138.06451387, 0.00067792, -13.80645139, -6.779e-05, -41.41935416, -0.00020338, -138.06451387, -0.00067792, 0.4, 0.3, 0.003, 0.0, 0.0, 23013, 2)
    ops.limitCurve('ThreePoint', 13013, 3013, 0.0, 55.22580555, 0.01436241, 55.22580555, 0.04308723, 38.65806388, -1982.25543325, 0.05, 2, 0, 73013, 24013, 1, 3)
    ops.uniaxialMaterial('LimitState', 33013, 13.80645139, 6.779e-05, 41.41935416, 0.00020338, 138.06451387, 0.00067792, -13.80645139, -6.779e-05, -41.41935416, -0.00020338, -138.06451387, -0.00067792, 0.4, 0.3, 0.003, 0.0, 0.0, 13013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3013, 99999, 'P', 43013, 'Vy', 33013, 'Vz', 23013, 'My', 13013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173013, 73013, 173013, 3013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124013, 124013, 24013, 3013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173014, 2.95, 10.95, 8.8)
    ops.node(124014, 2.95, 10.95, 11.175)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3014, 173014, 124014, 0.1225, 27334418.72312696, 11389341.13463623, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23014, 48.79318997, 0.00058139, 59.68046703, 0.03760577, 5.9680467, 0.10968047, -48.79318997, -0.00058139, -59.68046703, -0.03760577, -5.9680467, -0.10968047, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13014, 45.45946091, 0.00058139, 55.60287941, 0.03760577, 5.56028794, 0.10968047, -45.45946091, -0.00058139, -55.60287941, -0.03760577, -5.56028794, -0.10968047, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23014, 3014, 0.0, 119.097475, 0.01162785, 119.097475, 0.03488355, 83.3682325, -3985.2676828, 0.05, 2, 0, 73014, 24014, 2, 3)
    ops.uniaxialMaterial('LimitState', 43014, 29.77436875, 7.299e-05, 89.32310625, 0.00021896, 297.74368749, 0.00072985, -29.77436875, -7.299e-05, -89.32310625, -0.00021896, -297.74368749, -0.00072985, 0.4, 0.3, 0.003, 0.0, 0.0, 23014, 2)
    ops.limitCurve('ThreePoint', 13014, 3014, 0.0, 119.097475, 0.01162785, 119.097475, 0.03488355, 83.3682325, -3985.2676828, 0.05, 2, 0, 73014, 24014, 1, 3)
    ops.uniaxialMaterial('LimitState', 33014, 29.77436875, 7.299e-05, 89.32310625, 0.00021896, 297.74368749, 0.00072985, -29.77436875, -7.299e-05, -89.32310625, -0.00021896, -297.74368749, -0.00072985, 0.4, 0.3, 0.003, 0.0, 0.0, 13014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3014, 99999, 'P', 43014, 'Vy', 33014, 'Vz', 23014, 'My', 13014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173014, 73014, 173014, 3014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124014, 124014, 24014, 3014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173015, 9.6, 10.95, 8.8)
    ops.node(124015, 9.6, 10.95, 11.175)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3015, 173015, 124015, 0.1225, 26333446.51420285, 10972269.38091785, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23015, 50.14187447, 0.00060074, 61.39772144, 0.02174683, 6.13977214, 0.06267441, -50.14187447, -0.00060074, -61.39772144, -0.02174683, -6.13977214, -0.06267441, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13015, 46.95582576, 0.00060074, 57.49646857, 0.02174683, 5.74964686, 0.06267441, -46.95582576, -0.00060074, -57.49646857, -0.02174683, -5.74964686, -0.06267441, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23015, 3015, 0.0, 88.05190138, 0.01201486, 88.05190138, 0.03604457, 61.63633097, -1145.15158739, 0.05, 2, 0, 73015, 24015, 2, 3)
    ops.uniaxialMaterial('LimitState', 43015, 22.01297535, 5.601e-05, 66.03892604, 0.00016803, 220.12975346, 0.00056011, -22.01297535, -5.601e-05, -66.03892604, -0.00016803, -220.12975346, -0.00056011, 0.4, 0.3, 0.003, 0.0, 0.0, 23015, 2)
    ops.limitCurve('ThreePoint', 13015, 3015, 0.0, 88.05190138, 0.01201486, 88.05190138, 0.03604457, 61.63633097, -1145.15158739, 0.05, 2, 0, 73015, 24015, 1, 3)
    ops.uniaxialMaterial('LimitState', 33015, 22.01297535, 5.601e-05, 66.03892604, 0.00016803, 220.12975346, 0.00056011, -22.01297535, -5.601e-05, -66.03892604, -0.00016803, -220.12975346, -0.00056011, 0.4, 0.3, 0.003, 0.0, 0.0, 13015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3015, 99999, 'P', 43015, 'Vy', 33015, 'Vz', 23015, 'My', 13015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173015, 73015, 173015, 3015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124015, 124015, 24015, 3015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173016, 16.25, 10.95, 8.8)
    ops.node(124016, 16.25, 10.95, 11.175)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3016, 173016, 124016, 0.1225, 28272746.168736, 11780310.90364, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23016, 69.91360956, 0.00063523, 85.36840113, 0.0519891, 8.53684011, 0.1519891, -69.91360956, -0.00063523, -85.36840113, -0.0519891, -8.53684011, -0.1519891, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13016, 64.43844766, 0.00063523, 78.6829243, 0.0519891, 7.86829243, 0.1519891, -64.43844766, -0.00063523, -78.6829243, -0.0519891, -7.86829243, -0.1519891, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23016, 3016, 0.0, 147.68785509, 0.01270468, 147.68785509, 0.03811404, 103.38149856, -9003.39598177, 0.05, 2, 0, 73016, 24016, 2, 3)
    ops.uniaxialMaterial('LimitState', 43016, 36.92196377, 8.75e-05, 110.76589132, 0.00026251, 369.21963772, 0.00087502, -36.92196377, -8.75e-05, -110.76589132, -0.00026251, -369.21963772, -0.00087502, 0.4, 0.3, 0.003, 0.0, 0.0, 23016, 2)
    ops.limitCurve('ThreePoint', 13016, 3016, 0.0, 147.68785509, 0.01270468, 147.68785509, 0.03811404, 103.38149856, -9003.39598177, 0.05, 2, 0, 73016, 24016, 1, 3)
    ops.uniaxialMaterial('LimitState', 33016, 36.92196377, 8.75e-05, 110.76589132, 0.00026251, 369.21963772, 0.00087502, -36.92196377, -8.75e-05, -110.76589132, -0.00026251, -369.21963772, -0.00087502, 0.4, 0.3, 0.003, 0.0, 0.0, 13016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3016, 99999, 'P', 43016, 'Vy', 33016, 'Vz', 23016, 'My', 13016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173016, 73016, 173016, 3016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124016, 124016, 24016, 3016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173017, 0.0, 14.6, 8.8)
    ops.node(124017, 0.0, 14.6, 11.175)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3017, 173017, 124017, 0.0625, 28076030.86234329, 11698346.19264304, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23017, 14.09203016, 0.00070509, 17.2177054, 0.02380402, 1.72177054, 0.08772051, -14.09203016, -0.00070509, -17.2177054, -0.02380402, -1.72177054, -0.08772051, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13017, 14.09203016, 0.00070509, 17.2177054, 0.02380402, 1.72177054, 0.08772051, -14.09203016, -0.00070509, -17.2177054, -0.02380402, -1.72177054, -0.08772051, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23017, 3017, 0.0, 56.13834706, 0.01410185, 56.13834706, 0.04230556, 39.29684294, -1799.89494965, 0.05, 2, 0, 73017, 24017, 2, 3)
    ops.uniaxialMaterial('LimitState', 43017, 14.03458677, 6.565e-05, 42.1037603, 0.00019694, 140.34586765, 0.00065648, -14.03458677, -6.565e-05, -42.1037603, -0.00019694, -140.34586765, -0.00065648, 0.4, 0.3, 0.003, 0.0, 0.0, 23017, 2)
    ops.limitCurve('ThreePoint', 13017, 3017, 0.0, 56.13834706, 0.01410185, 56.13834706, 0.04230556, 39.29684294, -1799.89494965, 0.05, 2, 0, 73017, 24017, 1, 3)
    ops.uniaxialMaterial('LimitState', 33017, 14.03458677, 6.565e-05, 42.1037603, 0.00019694, 140.34586765, 0.00065648, -14.03458677, -6.565e-05, -42.1037603, -0.00019694, -140.34586765, -0.00065648, 0.4, 0.3, 0.003, 0.0, 0.0, 13017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3017, 99999, 'P', 43017, 'Vy', 33017, 'Vz', 23017, 'My', 13017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173017, 73017, 173017, 3017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124017, 124017, 24017, 3017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173018, 2.95, 14.6, 8.8)
    ops.node(124018, 2.95, 14.6, 11.175)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3018, 173018, 124018, 0.1225, 27086421.4415645, 11286008.93398521, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23018, 47.94748949, 0.00058554, 58.67607033, 0.03752309, 5.86760703, 0.10944668, -47.94748949, -0.00058554, -58.67607033, -0.03752309, -5.86760703, -0.10944668, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13018, 44.75712562, 0.00058554, 54.77184058, 0.03752309, 5.47718406, 0.10944668, -44.75712562, -0.00058554, -54.77184058, -0.03752309, -5.47718406, -0.10944668, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23018, 3018, 0.0, 117.87494859, 0.01171075, 117.87494859, 0.03513226, 82.51246402, -3940.91091711, 0.05, 2, 0, 73018, 24018, 2, 3)
    ops.uniaxialMaterial('LimitState', 43018, 29.46873715, 7.29e-05, 88.40621145, 0.00021869, 294.68737149, 0.00072897, -29.46873715, -7.29e-05, -88.40621145, -0.00021869, -294.68737149, -0.00072897, 0.4, 0.3, 0.003, 0.0, 0.0, 23018, 2)
    ops.limitCurve('ThreePoint', 13018, 3018, 0.0, 117.87494859, 0.01171075, 117.87494859, 0.03513226, 82.51246402, -3940.91091711, 0.05, 2, 0, 73018, 24018, 1, 3)
    ops.uniaxialMaterial('LimitState', 33018, 29.46873715, 7.29e-05, 88.40621145, 0.00021869, 294.68737149, 0.00072897, -29.46873715, -7.29e-05, -88.40621145, -0.00021869, -294.68737149, -0.00072897, 0.4, 0.3, 0.003, 0.0, 0.0, 13018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3018, 99999, 'P', 43018, 'Vy', 33018, 'Vz', 23018, 'My', 13018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173018, 73018, 173018, 3018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124018, 124018, 24018, 3018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173019, 9.6, 14.6, 8.8)
    ops.node(124019, 9.6, 14.6, 11.175)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3019, 173019, 124019, 0.1225, 27562041.95944459, 11484184.14976858, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23019, 51.21799935, 0.00058606, 62.56933379, 0.02140263, 6.25693338, 0.06292881, -51.21799935, -0.00058606, -62.56933379, -0.02140263, -6.25693338, -0.06292881, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13019, 47.8382824, 0.00058606, 58.44057748, 0.02140263, 5.84405775, 0.06292881, -47.8382824, -0.00058606, -58.44057748, -0.02140263, -5.84405775, -0.06292881, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23019, 3019, 0.0, 92.10348421, 0.01172112, 92.10348421, 0.03516336, 64.47243895, -1139.71674429, 0.05, 2, 0, 73019, 24019, 2, 3)
    ops.uniaxialMaterial('LimitState', 43019, 23.02587105, 5.598e-05, 69.07761316, 0.00016793, 230.25871052, 0.00055977, -23.02587105, -5.598e-05, -69.07761316, -0.00016793, -230.25871052, -0.00055977, 0.4, 0.3, 0.003, 0.0, 0.0, 23019, 2)
    ops.limitCurve('ThreePoint', 13019, 3019, 0.0, 92.10348421, 0.01172112, 92.10348421, 0.03516336, 64.47243895, -1139.71674429, 0.05, 2, 0, 73019, 24019, 1, 3)
    ops.uniaxialMaterial('LimitState', 33019, 23.02587105, 5.598e-05, 69.07761316, 0.00016793, 230.25871052, 0.00055977, -23.02587105, -5.598e-05, -69.07761316, -0.00016793, -230.25871052, -0.00055977, 0.4, 0.3, 0.003, 0.0, 0.0, 13019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3019, 99999, 'P', 43019, 'Vy', 33019, 'Vz', 23019, 'My', 13019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173019, 73019, 173019, 3019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124019, 124019, 24019, 3019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173020, 16.25, 14.6, 8.8)
    ops.node(124020, 16.25, 14.6, 11.175)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3020, 173020, 124020, 0.1225, 28044937.45338374, 11685390.60557656, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23020, 70.92449751, 0.00061007, 86.64896806, 0.05243825, 8.66489681, 0.15243825, -70.92449751, -0.00061007, -86.64896806, -0.05243825, -8.66489681, -0.15243825, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13020, 64.97836305, 0.00061007, 79.38453287, 0.05243825, 7.93845329, 0.15243825, -64.97836305, -0.00061007, -79.38453287, -0.05243825, -7.93845329, -0.15243825, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23020, 3020, 0.0, 149.618941, 0.01220137, 149.618941, 0.03660411, 104.7332587, -9539.44807772, 0.05, 2, 0, 73020, 24020, 2, 3)
    ops.uniaxialMaterial('LimitState', 43020, 37.40473525, 8.937e-05, 112.21420575, 0.0002681, 374.04735251, 0.00089366, -37.40473525, -8.937e-05, -112.21420575, -0.0002681, -374.04735251, -0.00089366, 0.4, 0.3, 0.003, 0.0, 0.0, 23020, 2)
    ops.limitCurve('ThreePoint', 13020, 3020, 0.0, 149.618941, 0.01220137, 149.618941, 0.03660411, 104.7332587, -9539.44807772, 0.05, 2, 0, 73020, 24020, 1, 3)
    ops.uniaxialMaterial('LimitState', 33020, 37.40473525, 8.937e-05, 112.21420575, 0.0002681, 374.04735251, 0.00089366, -37.40473525, -8.937e-05, -112.21420575, -0.0002681, -374.04735251, -0.00089366, 0.4, 0.3, 0.003, 0.0, 0.0, 13020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3020, 99999, 'P', 43020, 'Vy', 33020, 'Vz', 23020, 'My', 13020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173020, 73020, 173020, 3020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124020, 124020, 24020, 3020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173021, 0.0, 18.25, 8.8)
    ops.node(124021, 0.0, 18.25, 11.175)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3021, 173021, 124021, 0.0625, 28085150.79333648, 11702146.1638902, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23021, 14.48980385, 0.00071066, 17.7033291, 0.02397087, 1.77033291, 0.08789057, -14.48980385, -0.00071066, -17.7033291, -0.02397087, -1.77033291, -0.08789057, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13021, 14.48980385, 0.00071066, 17.7033291, 0.02397087, 1.77033291, 0.08789057, -14.48980385, -0.00071066, -17.7033291, -0.02397087, -1.77033291, -0.08789057, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23021, 3021, 0.0, 56.86685238, 0.01421321, 56.86685238, 0.04263964, 39.80679667, -1891.75682652, 0.05, 2, 0, 73021, 24021, 2, 3)
    ops.uniaxialMaterial('LimitState', 43021, 14.21671309, 6.648e-05, 42.65013928, 0.00019943, 142.16713095, 0.00066478, -14.21671309, -6.648e-05, -42.65013928, -0.00019943, -142.16713095, -0.00066478, 0.4, 0.3, 0.003, 0.0, 0.0, 23021, 2)
    ops.limitCurve('ThreePoint', 13021, 3021, 0.0, 56.86685238, 0.01421321, 56.86685238, 0.04263964, 39.80679667, -1891.75682652, 0.05, 2, 0, 73021, 24021, 1, 3)
    ops.uniaxialMaterial('LimitState', 33021, 14.21671309, 6.648e-05, 42.65013928, 0.00019943, 142.16713095, 0.00066478, -14.21671309, -6.648e-05, -42.65013928, -0.00019943, -142.16713095, -0.00066478, 0.4, 0.3, 0.003, 0.0, 0.0, 13021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3021, 99999, 'P', 43021, 'Vy', 33021, 'Vz', 23021, 'My', 13021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173021, 73021, 173021, 3021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124021, 124021, 24021, 3021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173022, 2.95, 18.25, 8.8)
    ops.node(124022, 2.95, 18.25, 11.175)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3022, 173022, 124022, 0.1225, 26955228.12887306, 11231345.05369711, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23022, 49.02533582, 0.00058694, 60.01096106, 0.0486459, 6.00109611, 0.1486459, -49.02533582, -0.00058694, -60.01096106, -0.0486459, -6.00109611, -0.1486459, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13022, 45.67580701, 0.00058694, 55.91086793, 0.0486459, 5.59108679, 0.1486459, -45.67580701, -0.00058694, -55.91086793, -0.0486459, -5.59108679, -0.1486459, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23022, 3022, 0.0, 148.96961039, 0.01173877, 148.96961039, 0.03521631, 104.27872727, -8451.57976345, 0.05, 2, 0, 73022, 24022, 2, 3)
    ops.uniaxialMaterial('LimitState', 43022, 37.2424026, 9.258e-05, 111.72720779, 0.00027773, 372.42402596, 0.00092575, -37.2424026, -9.258e-05, -111.72720779, -0.00027773, -372.42402596, -0.00092575, 0.4, 0.3, 0.003, 0.0, 0.0, 23022, 2)
    ops.limitCurve('ThreePoint', 13022, 3022, 0.0, 148.96961039, 0.01173877, 148.96961039, 0.03521631, 104.27872727, -8451.57976345, 0.05, 2, 0, 73022, 24022, 1, 3)
    ops.uniaxialMaterial('LimitState', 33022, 37.2424026, 9.258e-05, 111.72720779, 0.00027773, 372.42402596, 0.00092575, -37.2424026, -9.258e-05, -111.72720779, -0.00027773, -372.42402596, -0.00092575, 0.4, 0.3, 0.003, 0.0, 0.0, 13022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3022, 99999, 'P', 43022, 'Vy', 33022, 'Vz', 23022, 'My', 13022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173022, 73022, 173022, 3022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124022, 124022, 24022, 3022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173023, 9.6, 18.25, 8.8)
    ops.node(124023, 9.6, 18.25, 11.175)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3023, 173023, 124023, 0.1225, 28738690.54415097, 11974454.39339624, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23023, 49.80589796, 0.00060142, 60.68607875, 0.02129526, 6.06860787, 0.06330197, -49.80589796, -0.00060142, -60.68607875, -0.02129526, -6.06860787, -0.06330197, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13023, 46.82325771, 0.00060142, 57.05187579, 0.02129526, 5.70518758, 0.06330197, -46.82325771, -0.00060142, -57.05187579, -0.02129526, -5.70518758, -0.06330197, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23023, 3023, 0.0, 96.20498765, 0.01202834, 96.20498765, 0.03608503, 67.34349135, -1140.28176118, 0.05, 2, 0, 73023, 24023, 2, 3)
    ops.uniaxialMaterial('LimitState', 43023, 24.05124691, 5.608e-05, 72.15374074, 0.00016823, 240.51246912, 0.00056075, -24.05124691, -5.608e-05, -72.15374074, -0.00016823, -240.51246912, -0.00056075, 0.4, 0.3, 0.003, 0.0, 0.0, 23023, 2)
    ops.limitCurve('ThreePoint', 13023, 3023, 0.0, 96.20498765, 0.01202834, 96.20498765, 0.03608503, 67.34349135, -1140.28176118, 0.05, 2, 0, 73023, 24023, 1, 3)
    ops.uniaxialMaterial('LimitState', 33023, 24.05124691, 5.608e-05, 72.15374074, 0.00016823, 240.51246912, 0.00056075, -24.05124691, -5.608e-05, -72.15374074, -0.00016823, -240.51246912, -0.00056075, 0.4, 0.3, 0.003, 0.0, 0.0, 13023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3023, 99999, 'P', 43023, 'Vy', 33023, 'Vz', 23023, 'My', 13023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173023, 73023, 173023, 3023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124023, 124023, 24023, 3023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173024, 16.25, 18.25, 8.8)
    ops.node(124024, 16.25, 18.25, 11.175)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3024, 173024, 124024, 0.1225, 28380725.09280906, 11825302.12200378, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23024, 69.48300982, 0.00062162, 84.82079079, 0.05233951, 8.48207908, 0.15233951, -69.48300982, -0.00062162, -84.82079079, -0.05233951, -8.48207908, -0.15233951, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13024, 63.93896342, 0.00062162, 78.05294349, 0.05233951, 7.80529435, 0.15233951, -63.93896342, -0.00062162, -78.05294349, -0.05233951, -7.80529435, -0.15233951, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23024, 3024, 0.0, 152.75311706, 0.01243241, 152.75311706, 0.03729723, 106.92718194, -9936.95438732, 0.05, 2, 0, 73024, 24024, 2, 3)
    ops.uniaxialMaterial('LimitState', 43024, 38.18827927, 9.016e-05, 114.5648378, 0.00027048, 381.88279266, 0.00090159, -38.18827927, -9.016e-05, -114.5648378, -0.00027048, -381.88279266, -0.00090159, 0.4, 0.3, 0.003, 0.0, 0.0, 23024, 2)
    ops.limitCurve('ThreePoint', 13024, 3024, 0.0, 152.75311706, 0.01243241, 152.75311706, 0.03729723, 106.92718194, -9936.95438732, 0.05, 2, 0, 73024, 24024, 1, 3)
    ops.uniaxialMaterial('LimitState', 33024, 38.18827927, 9.016e-05, 114.5648378, 0.00027048, 381.88279266, 0.00090159, -38.18827927, -9.016e-05, -114.5648378, -0.00027048, -381.88279266, -0.00090159, 0.4, 0.3, 0.003, 0.0, 0.0, 13024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3024, 99999, 'P', 43024, 'Vy', 33024, 'Vz', 23024, 'My', 13024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173024, 73024, 173024, 3024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124024, 124024, 24024, 3024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173025, 0.0, 21.9, 8.85)
    ops.node(124025, 0.0, 21.9, 11.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3025, 173025, 124025, 0.0625, 26829685.76651913, 11179035.73604964, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23025, 13.55108378, 0.00070892, 16.61631318, 0.02453253, 1.66163132, 0.08960852, -13.55108378, -0.00070892, -16.61631318, -0.02453253, -1.66163132, -0.08960852, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13025, 13.55108378, 0.00070892, 16.61631318, 0.02453253, 1.66163132, 0.08960852, -13.55108378, -0.00070892, -16.61631318, -0.02453253, -1.66163132, -0.08960852, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23025, 3025, 0.0, 53.97815689, 0.01417832, 53.97815689, 0.04253496, 37.78470982, -3217.34608659, 0.05, 2, 0, 73025, 24025, 2, 3)
    ops.uniaxialMaterial('LimitState', 43025, 13.49453922, 6.605e-05, 40.48361767, 0.00019816, 134.94539223, 0.00066054, -13.49453922, -6.605e-05, -40.48361767, -0.00019816, -134.94539223, -0.00066054, 0.4, 0.3, 0.003, 0.0, 0.0, 23025, 2)
    ops.limitCurve('ThreePoint', 13025, 3025, 0.0, 53.97815689, 0.01417832, 53.97815689, 0.04253496, 37.78470982, -3217.34608659, 0.05, 2, 0, 73025, 24025, 1, 3)
    ops.uniaxialMaterial('LimitState', 33025, 13.49453922, 6.605e-05, 40.48361767, 0.00019816, 134.94539223, 0.00066054, -13.49453922, -6.605e-05, -40.48361767, -0.00019816, -134.94539223, -0.00066054, 0.4, 0.3, 0.003, 0.0, 0.0, 13025, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3025, 99999, 'P', 43025, 'Vy', 33025, 'Vz', 23025, 'My', 13025, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173025, 73025, 173025, 3025, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124025, 124025, 24025, 3025, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173026, 2.95, 21.9, 8.85)
    ops.node(124026, 2.95, 21.9, 11.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3026, 173026, 124026, 0.0625, 28685284.4072923, 11952201.83637179, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23026, 15.603594, 0.00071216, 19.02322624, 0.02322276, 1.90232262, 0.08602089, -15.603594, -0.00071216, -19.02322624, -0.02322276, -1.90232262, -0.08602089, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13026, 15.603594, 0.00071216, 19.02322624, 0.02322276, 1.90232262, 0.08602089, -15.603594, -0.00071216, -19.02322624, -0.02322276, -1.90232262, -0.08602089, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23026, 3026, 0.0, 58.51254945, 0.01424316, 58.51254945, 0.04272949, 40.95878462, -1409.14251197, 0.05, 2, 0, 73026, 24026, 2, 3)
    ops.uniaxialMaterial('LimitState', 43026, 14.62813736, 6.697e-05, 43.88441209, 0.00020091, 146.28137364, 0.00066971, -14.62813736, -6.697e-05, -43.88441209, -0.00020091, -146.28137364, -0.00066971, 0.4, 0.3, 0.003, 0.0, 0.0, 23026, 2)
    ops.limitCurve('ThreePoint', 13026, 3026, 0.0, 58.51254945, 0.01424316, 58.51254945, 0.04272949, 40.95878462, -1409.14251197, 0.05, 2, 0, 73026, 24026, 1, 3)
    ops.uniaxialMaterial('LimitState', 33026, 14.62813736, 6.697e-05, 43.88441209, 0.00020091, 146.28137364, 0.00066971, -14.62813736, -6.697e-05, -43.88441209, -0.00020091, -146.28137364, -0.00066971, 0.4, 0.3, 0.003, 0.0, 0.0, 13026, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3026, 99999, 'P', 43026, 'Vy', 33026, 'Vz', 23026, 'My', 13026, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173026, 73026, 173026, 3026, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124026, 124026, 24026, 3026, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173027, 9.6, 21.9, 8.85)
    ops.node(124027, 9.6, 21.9, 11.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3027, 173027, 124027, 0.1225, 28300095.56479199, 11791706.48532999, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23027, 43.00412547, 0.00056748, 52.5111201, 0.02099974, 5.25111201, 0.07031442, -43.00412547, -0.00056748, -52.5111201, -0.02099974, -5.25111201, -0.07031442, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13027, 36.40326624, 0.00056748, 44.45099777, 0.02099974, 4.44509978, 0.07031442, -36.40326624, -0.00056748, -44.45099777, -0.02099974, -4.44509978, -0.07031442, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23027, 3027, 0.0, 97.81628623, 0.01134953, 97.81628623, 0.0340486, 68.47140036, -1992.01789415, 0.05, 2, 0, 73027, 24027, 2, 3)
    ops.uniaxialMaterial('LimitState', 43027, 24.45407156, 5.79e-05, 73.36221467, 0.00017369, 244.54071556, 0.00057898, -24.45407156, -5.79e-05, -73.36221467, -0.00017369, -244.54071556, -0.00057898, 0.4, 0.3, 0.003, 0.0, 0.0, 23027, 2)
    ops.limitCurve('ThreePoint', 13027, 3027, 0.0, 97.81628623, 0.01134953, 97.81628623, 0.0340486, 68.47140036, -1992.01789415, 0.05, 2, 0, 73027, 24027, 1, 3)
    ops.uniaxialMaterial('LimitState', 33027, 24.45407156, 5.79e-05, 73.36221467, 0.00017369, 244.54071556, 0.00057898, -24.45407156, -5.79e-05, -73.36221467, -0.00017369, -244.54071556, -0.00057898, 0.4, 0.3, 0.003, 0.0, 0.0, 13027, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3027, 99999, 'P', 43027, 'Vy', 33027, 'Vz', 23027, 'My', 13027, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173027, 73027, 173027, 3027, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124027, 124027, 24027, 3027, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173028, 16.25, 21.9, 8.85)
    ops.node(124028, 16.25, 21.9, 11.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3028, 173028, 124028, 0.0625, 28441322.78929318, 11850551.16220549, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23028, 23.68633986, 0.00075794, 28.91239465, 0.02852141, 2.89123947, 0.09239836, -23.68633986, -0.00075794, -28.91239465, -0.02852141, -2.89123947, -0.09239836, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13028, 23.68633986, 0.00075794, 28.91239465, 0.02852141, 2.89123947, 0.09239836, -23.68633986, -0.00075794, -28.91239465, -0.02852141, -2.89123947, -0.09239836, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23028, 3028, 0.0, 57.6876369, 0.01515883, 57.6876369, 0.0454765, 40.38134583, -1824.93954461, 0.05, 2, 0, 73028, 24028, 2, 3)
    ops.uniaxialMaterial('LimitState', 43028, 14.42190923, 6.659e-05, 43.26572768, 0.00019978, 144.21909226, 0.00066593, -14.42190923, -6.659e-05, -43.26572768, -0.00019978, -144.21909226, -0.00066593, 0.4, 0.3, 0.003, 0.0, 0.0, 23028, 2)
    ops.limitCurve('ThreePoint', 13028, 3028, 0.0, 57.6876369, 0.01515883, 57.6876369, 0.0454765, 40.38134583, -1824.93954461, 0.05, 2, 0, 73028, 24028, 1, 3)
    ops.uniaxialMaterial('LimitState', 33028, 14.42190923, 6.659e-05, 43.26572768, 0.00019978, 144.21909226, 0.00066593, -14.42190923, -6.659e-05, -43.26572768, -0.00019978, -144.21909226, -0.00066593, 0.4, 0.3, 0.003, 0.0, 0.0, 13028, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3028, 99999, 'P', 43028, 'Vy', 33028, 'Vz', 23028, 'My', 13028, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173028, 73028, 173028, 3028, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124028, 124028, 24028, 3028, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170001, 0.0, 0.0, 0.0)
    ops.node(124029, 0.0, 0.0, 1.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4074, 170001, 124029, 0.0625, 27827136.18986971, 11594640.07911238, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24074, 29.96786886, 0.00059212, 36.3152633, 0.02683445, 3.63152633, 0.08577758, -29.96786886, -0.00059212, -36.3152633, -0.02683445, -3.63152633, -0.08577758, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14074, 27.74702815, 0.00059212, 33.62403372, 0.02683445, 3.36240337, 0.08577758, -27.74702815, -0.00059212, -33.62403372, -0.02683445, -3.36240337, -0.08577758, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24074, 4074, 0.0, 75.91024719, 0.01184232, 75.91024719, 0.03552695, 53.13717303, -2098.73585952, 0.05, 2, 0, 70001, 24029, 2, 3)
    ops.uniaxialMaterial('LimitState', 44074, 18.9775618, 4.478e-05, 56.93268539, 0.00013434, 189.77561796, 0.00044782, -18.9775618, -4.478e-05, -56.93268539, -0.00013434, -189.77561796, -0.00044782, 0.4, 0.3, 0.003, 0.0, 0.0, 24074, 2)
    ops.limitCurve('ThreePoint', 14074, 4074, 0.0, 75.91024719, 0.01184232, 75.91024719, 0.03552695, 53.13717303, -2098.73585952, 0.05, 2, 0, 70001, 24029, 1, 3)
    ops.uniaxialMaterial('LimitState', 34074, 18.9775618, 4.478e-05, 56.93268539, 0.00013434, 189.77561796, 0.00044782, -18.9775618, -4.478e-05, -56.93268539, -0.00013434, -189.77561796, -0.00044782, 0.4, 0.3, 0.003, 0.0, 0.0, 14074, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4074, 99999, 'P', 44074, 'Vy', 34074, 'Vz', 24074, 'My', 14074, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170001, 70001, 170001, 4074, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124029, 124029, 24029, 4074, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174029, 0.0, 0.0, 1.6)
    ops.node(121001, 0.0, 0.0, 2.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4075, 174029, 121001, 0.0625, 27103550.21355891, 11293145.92231621, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24075, 22.26616511, 0.00056212, 27.05366094, 0.03485837, 2.70536609, 0.11232023, -22.26616511, -0.00056212, -27.05366094, -0.03485837, -2.70536609, -0.11232023, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14075, 22.26616511, 0.00056212, 27.05366094, 0.03485837, 2.70536609, 0.11232023, -22.26616511, -0.00056212, -27.05366094, -0.03485837, -2.70536609, -0.11232023, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24075, 4075, 0.0, 84.83354658, 0.01124241, 84.83354658, 0.03372723, 59.3834826, -3315.56485953, 0.05, 2, 0, 74029, 21001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44075, 21.20838664, 5.138e-05, 63.62515993, 0.00015415, 212.08386644, 0.00051382, -21.20838664, -5.138e-05, -63.62515993, -0.00015415, -212.08386644, -0.00051382, 0.4, 0.3, 0.003, 0.0, 0.0, 24075, 2)
    ops.limitCurve('ThreePoint', 14075, 4075, 0.0, 84.83354658, 0.01124241, 84.83354658, 0.03372723, 59.3834826, -3315.56485953, 0.05, 2, 0, 74029, 21001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34075, 21.20838664, 5.138e-05, 63.62515993, 0.00015415, 212.08386644, 0.00051382, -21.20838664, -5.138e-05, -63.62515993, -0.00015415, -212.08386644, -0.00051382, 0.4, 0.3, 0.003, 0.0, 0.0, 14075, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4075, 99999, 'P', 44075, 'Vy', 34075, 'Vz', 24075, 'My', 14075, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174029, 74029, 174029, 4075, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121001, 121001, 21001, 4075, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170002, 2.95, 0.0, 0.0)
    ops.node(124030, 2.95, 0.0, 1.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4076, 170002, 124030, 0.16, 28921609.93262925, 12050670.80526219, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24076, 135.75410242, 0.00048809, 164.39695149, 0.0415205, 16.43969515, 0.11753427, -135.75410242, -0.00048809, -164.39695149, -0.0415205, -16.43969515, -0.11753427, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14076, 140.47888271, 0.00048809, 170.11861634, 0.0415205, 17.01186163, 0.11753427, -140.47888271, -0.00048809, -170.11861634, -0.0415205, -17.01186163, -0.11753427, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24076, 4076, 0.0, 290.3595798, 0.00976174, 290.3595798, 0.02928523, 203.25170586, -7455.97359011, 0.05, 2, 0, 70002, 24030, 2, 3)
    ops.uniaxialMaterial('LimitState', 44076, 72.58989495, 6.438e-05, 217.76968485, 0.00019314, 725.89894949, 0.00064379, -72.58989495, -6.438e-05, -217.76968485, -0.00019314, -725.89894949, -0.00064379, 0.4, 0.3, 0.003, 0.0, 0.0, 24076, 2)
    ops.limitCurve('ThreePoint', 14076, 4076, 0.0, 290.3595798, 0.00976174, 290.3595798, 0.02928523, 203.25170586, -7455.97359011, 0.05, 2, 0, 70002, 24030, 1, 3)
    ops.uniaxialMaterial('LimitState', 34076, 72.58989495, 6.438e-05, 217.76968485, 0.00019314, 725.89894949, 0.00064379, -72.58989495, -6.438e-05, -217.76968485, -0.00019314, -725.89894949, -0.00064379, 0.4, 0.3, 0.003, 0.0, 0.0, 14076, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4076, 99999, 'P', 44076, 'Vy', 34076, 'Vz', 24076, 'My', 14076, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170002, 70002, 170002, 4076, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124030, 124030, 24030, 4076, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174030, 2.95, 0.0, 1.6)
    ops.node(121002, 2.95, 0.0, 2.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4077, 174030, 121002, 0.16, 27930884.07718916, 11637868.36549548, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24077, 95.01213423, 0.00048605, 115.31806105, 0.03907925, 11.53180611, 0.11436231, -95.01213423, -0.00048605, -115.31806105, -0.03907925, -11.53180611, -0.11436231, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14077, 82.00257479, 0.00048605, 99.52810767, 0.03907925, 9.95281077, 0.11436231, -82.00257479, -0.00048605, -99.52810767, -0.03907925, -9.95281077, -0.11436231, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24077, 4077, 0.0, 281.0104185, 0.009721, 281.0104185, 0.02916301, 196.70729295, -7840.59244699, 0.05, 2, 0, 74030, 21002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44077, 70.25260462, 6.452e-05, 210.75781387, 0.00019355, 702.52604625, 0.00064516, -70.25260462, -6.452e-05, -210.75781387, -0.00019355, -702.52604625, -0.00064516, 0.4, 0.3, 0.003, 0.0, 0.0, 24077, 2)
    ops.limitCurve('ThreePoint', 14077, 4077, 0.0, 281.0104185, 0.009721, 281.0104185, 0.02916301, 196.70729295, -7840.59244699, 0.05, 2, 0, 74030, 21002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34077, 70.25260462, 6.452e-05, 210.75781387, 0.00019355, 702.52604625, 0.00064516, -70.25260462, -6.452e-05, -210.75781387, -0.00019355, -702.52604625, -0.00064516, 0.4, 0.3, 0.003, 0.0, 0.0, 14077, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4077, 99999, 'P', 44077, 'Vy', 34077, 'Vz', 24077, 'My', 14077, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174030, 74030, 174030, 4077, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121002, 121002, 21002, 4077, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171001, 0.0, 0.0, 3.15)
    ops.node(124031, 0.0, 0.0, 4.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4079, 171001, 124031, 0.0625, 27409256.71326834, 11420523.63052847, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24079, 21.3965734, 0.00056564, 26.01175626, 0.02708408, 2.60117563, 0.09000399, -21.3965734, -0.00056564, -26.01175626, -0.02708408, -2.60117563, -0.09000399, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14079, 21.3965734, 0.00056564, 26.01175626, 0.02708408, 2.60117563, 0.09000399, -21.3965734, -0.00056564, -26.01175626, -0.02708408, -2.60117563, -0.09000399, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24079, 4079, 0.0, 73.02692273, 0.01131271, 73.02692273, 0.03393813, 51.11884591, -2281.72352678, 0.05, 2, 0, 71001, 24031, 2, 3)
    ops.uniaxialMaterial('LimitState', 44079, 18.25673068, 4.374e-05, 54.77019205, 0.00013121, 182.56730683, 0.00043737, -18.25673068, -4.374e-05, -54.77019205, -0.00013121, -182.56730683, -0.00043737, 0.4, 0.3, 0.003, 0.0, 0.0, 24079, 2)
    ops.limitCurve('ThreePoint', 14079, 4079, 0.0, 73.02692273, 0.01131271, 73.02692273, 0.03393813, 51.11884591, -2281.72352678, 0.05, 2, 0, 71001, 24031, 1, 3)
    ops.uniaxialMaterial('LimitState', 34079, 18.25673068, 4.374e-05, 54.77019205, 0.00013121, 182.56730683, 0.00043737, -18.25673068, -4.374e-05, -54.77019205, -0.00013121, -182.56730683, -0.00043737, 0.4, 0.3, 0.003, 0.0, 0.0, 14079, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4079, 99999, 'P', 44079, 'Vy', 34079, 'Vz', 24079, 'My', 14079, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171001, 71001, 171001, 4079, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124031, 124031, 24031, 4079, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174031, 0.0, 0.0, 4.45)
    ops.node(122001, 0.0, 0.0, 5.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4080, 174031, 122001, 0.0625, 27215686.80873668, 11339869.50364028, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24080, 19.33957258, 0.00056271, 23.56041818, 0.02263191, 2.35604182, 0.07768257, -19.33957258, -0.00056271, -23.56041818, -0.02263191, -2.35604182, -0.07768257, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14080, 19.33957258, 0.00056271, 23.56041818, 0.02263191, 2.35604182, 0.07768257, -19.33957258, -0.00056271, -23.56041818, -0.02263191, -2.35604182, -0.07768257, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24080, 4080, 0.0, 64.29131464, 0.0112541, 64.29131464, 0.03376231, 45.00392024, -1823.15878597, 0.05, 2, 0, 74031, 22001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44080, 16.07282866, 3.878e-05, 48.21848598, 0.00011634, 160.72828659, 0.00038779, -16.07282866, -3.878e-05, -48.21848598, -0.00011634, -160.72828659, -0.00038779, 0.4, 0.3, 0.003, 0.0, 0.0, 24080, 2)
    ops.limitCurve('ThreePoint', 14080, 4080, 0.0, 64.29131464, 0.0112541, 64.29131464, 0.03376231, 45.00392024, -1823.15878597, 0.05, 2, 0, 74031, 22001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34080, 16.07282866, 3.878e-05, 48.21848598, 0.00011634, 160.72828659, 0.00038779, -16.07282866, -3.878e-05, -48.21848598, -0.00011634, -160.72828659, -0.00038779, 0.4, 0.3, 0.003, 0.0, 0.0, 14080, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4080, 99999, 'P', 44080, 'Vy', 34080, 'Vz', 24080, 'My', 14080, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174031, 74031, 174031, 4080, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122001, 122001, 22001, 4080, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171002, 2.95, 0.0, 3.15)
    ops.node(124032, 2.95, 0.0, 4.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4081, 171002, 124032, 0.16, 28896016.12061324, 12040006.71692218, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24081, 86.8389331, 0.00047643, 105.3983345, 0.03984183, 10.53983345, 0.1209686, -86.8389331, -0.00047643, -105.3983345, -0.03984183, -10.53983345, -0.1209686, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14081, 74.17503448, 0.00047643, 90.02788055, 0.03984183, 9.00278805, 0.1209686, -74.17503448, -0.00047643, -90.02788055, -0.03984183, -9.00278805, -0.1209686, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24081, 4081, 0.0, 279.34366063, 0.00952865, 279.34366063, 0.02858596, 195.54056244, -8368.56202616, 0.05, 2, 0, 71002, 24032, 2, 3)
    ops.uniaxialMaterial('LimitState', 44081, 69.83591516, 6.199e-05, 209.50774547, 0.00018597, 698.35915157, 0.00061991, -69.83591516, -6.199e-05, -209.50774547, -0.00018597, -698.35915157, -0.00061991, 0.4, 0.3, 0.003, 0.0, 0.0, 24081, 2)
    ops.limitCurve('ThreePoint', 14081, 4081, 0.0, 279.34366063, 0.00952865, 279.34366063, 0.02858596, 195.54056244, -8368.56202616, 0.05, 2, 0, 71002, 24032, 1, 3)
    ops.uniaxialMaterial('LimitState', 34081, 69.83591516, 6.199e-05, 209.50774547, 0.00018597, 698.35915157, 0.00061991, -69.83591516, -6.199e-05, -209.50774547, -0.00018597, -698.35915157, -0.00061991, 0.4, 0.3, 0.003, 0.0, 0.0, 14081, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4081, 99999, 'P', 44081, 'Vy', 34081, 'Vz', 24081, 'My', 14081, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171002, 71002, 171002, 4081, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124032, 124032, 24032, 4081, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174032, 2.95, 0.0, 4.45)
    ops.node(122002, 2.95, 0.0, 5.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4082, 174032, 122002, 0.16, 27568356.38233837, 11486815.15930765, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24082, 82.99321681, 0.00047732, 101.04247888, 0.04072291, 10.10424789, 0.12111368, -82.99321681, -0.00047732, -101.04247888, -0.04072291, -10.10424789, -0.12111368, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14082, 70.51633621, 0.00047732, 85.85214174, 0.04072291, 8.58521417, 0.12111368, -70.51633621, -0.00047732, -85.85214174, -0.04072291, -8.58521417, -0.12111368, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24082, 4082, 0.0, 263.99424177, 0.00954634, 263.99424177, 0.02863903, 184.79596924, -8637.81880334, 0.05, 2, 0, 74032, 22002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44082, 65.99856044, 6.141e-05, 197.99568133, 0.00018422, 659.98560442, 0.00061406, -65.99856044, -6.141e-05, -197.99568133, -0.00018422, -659.98560442, -0.00061406, 0.4, 0.3, 0.003, 0.0, 0.0, 24082, 2)
    ops.limitCurve('ThreePoint', 14082, 4082, 0.0, 263.99424177, 0.00954634, 263.99424177, 0.02863903, 184.79596924, -8637.81880334, 0.05, 2, 0, 74032, 22002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34082, 65.99856044, 6.141e-05, 197.99568133, 0.00018422, 659.98560442, 0.00061406, -65.99856044, -6.141e-05, -197.99568133, -0.00018422, -659.98560442, -0.00061406, 0.4, 0.3, 0.003, 0.0, 0.0, 14082, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4082, 99999, 'P', 44082, 'Vy', 34082, 'Vz', 24082, 'My', 14082, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174032, 74032, 174032, 4082, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122002, 122002, 22002, 4082, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172001, 0.0, 0.0, 6.0)
    ops.node(124033, 0.0, 0.0, 6.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4084, 172001, 124033, 0.0625, 27820501.19566289, 11591875.49819287, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24084, 18.77531193, 0.00055577, 22.87065526, 0.02841848, 2.28706553, 0.09720972, -18.77531193, -0.00055577, -22.87065526, -0.02841848, -2.28706553, -0.09720972, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14084, 18.77531193, 0.00055577, 22.87065526, 0.02841848, 2.28706553, 0.09720972, -18.77531193, -0.00055577, -22.87065526, -0.02841848, -2.28706553, -0.09720972, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24084, 4084, 0.0, 71.34913468, 0.01111543, 71.34913468, 0.03334628, 49.94439428, -2689.68883236, 0.05, 2, 0, 72001, 24033, 2, 3)
    ops.uniaxialMaterial('LimitState', 44084, 17.83728367, 4.21e-05, 53.51185101, 0.0001263, 178.3728367, 0.00042101, -17.83728367, -4.21e-05, -53.51185101, -0.0001263, -178.3728367, -0.00042101, 0.4, 0.3, 0.003, 0.0, 0.0, 24084, 2)
    ops.limitCurve('ThreePoint', 14084, 4084, 0.0, 71.34913468, 0.01111543, 71.34913468, 0.03334628, 49.94439428, -2689.68883236, 0.05, 2, 0, 72001, 24033, 1, 3)
    ops.uniaxialMaterial('LimitState', 34084, 17.83728367, 4.21e-05, 53.51185101, 0.0001263, 178.3728367, 0.00042101, -17.83728367, -4.21e-05, -53.51185101, -0.0001263, -178.3728367, -0.00042101, 0.4, 0.3, 0.003, 0.0, 0.0, 14084, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4084, 99999, 'P', 44084, 'Vy', 34084, 'Vz', 24084, 'My', 14084, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172001, 72001, 172001, 4084, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124033, 124033, 24033, 4084, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174033, 0.0, 0.0, 7.3)
    ops.node(123001, 0.0, 0.0, 8.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4085, 174033, 123001, 0.0625, 27966393.21640042, 11652663.84016684, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24085, 16.2329391, 0.00054327, 19.80643319, 0.02344442, 1.98064332, 0.08431137, -16.2329391, -0.00054327, -19.80643319, -0.02344442, -1.98064332, -0.08431137, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14085, 16.2329391, 0.00054327, 19.80643319, 0.02344442, 1.98064332, 0.08431137, -16.2329391, -0.00054327, -19.80643319, -0.02344442, -1.98064332, -0.08431137, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24085, 4085, 0.0, 62.70789125, 0.01086544, 62.70789125, 0.03259632, 43.89552387, -2407.45777063, 0.05, 2, 0, 74033, 23001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44085, 15.67697281, 3.681e-05, 47.03091844, 0.00011043, 156.76972812, 0.00036809, -15.67697281, -3.681e-05, -47.03091844, -0.00011043, -156.76972812, -0.00036809, 0.4, 0.3, 0.003, 0.0, 0.0, 24085, 2)
    ops.limitCurve('ThreePoint', 14085, 4085, 0.0, 62.70789125, 0.01086544, 62.70789125, 0.03259632, 43.89552387, -2407.45777063, 0.05, 2, 0, 74033, 23001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34085, 15.67697281, 3.681e-05, 47.03091844, 0.00011043, 156.76972812, 0.00036809, -15.67697281, -3.681e-05, -47.03091844, -0.00011043, -156.76972812, -0.00036809, 0.4, 0.3, 0.003, 0.0, 0.0, 14085, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4085, 99999, 'P', 44085, 'Vy', 34085, 'Vz', 24085, 'My', 14085, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174033, 74033, 174033, 4085, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123001, 123001, 23001, 4085, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172002, 2.95, 0.0, 6.0)
    ops.node(124034, 2.95, 0.0, 6.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4086, 172002, 124034, 0.1225, 28529230.14750068, 11887179.22812529, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24086, 55.65151153, 0.00048909, 67.66591052, 0.04257838, 6.76659105, 0.13597881, -55.65151153, -0.00048909, -67.66591052, -0.04257838, -6.76659105, -0.13597881, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14086, 48.6820453, 0.00048909, 59.191832, 0.04257838, 5.9191832, 0.13597881, -48.6820453, -0.00048909, -59.191832, -0.04257838, -5.9191832, -0.13597881, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24086, 4086, 0.0, 201.3469349, 0.00978172, 201.3469349, 0.02934517, 140.94285443, -8391.67839232, 0.05, 2, 0, 72002, 24034, 2, 3)
    ops.uniaxialMaterial('LimitState', 44086, 50.33673372, 5.911e-05, 151.01020117, 0.00017733, 503.36733724, 0.00059111, -50.33673372, -5.911e-05, -151.01020117, -0.00017733, -503.36733724, -0.00059111, 0.4, 0.3, 0.003, 0.0, 0.0, 24086, 2)
    ops.limitCurve('ThreePoint', 14086, 4086, 0.0, 201.3469349, 0.00978172, 201.3469349, 0.02934517, 140.94285443, -8391.67839232, 0.05, 2, 0, 72002, 24034, 1, 3)
    ops.uniaxialMaterial('LimitState', 34086, 50.33673372, 5.911e-05, 151.01020117, 0.00017733, 503.36733724, 0.00059111, -50.33673372, -5.911e-05, -151.01020117, -0.00017733, -503.36733724, -0.00059111, 0.4, 0.3, 0.003, 0.0, 0.0, 14086, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4086, 99999, 'P', 44086, 'Vy', 34086, 'Vz', 24086, 'My', 14086, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172002, 72002, 172002, 4086, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124034, 124034, 24034, 4086, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174034, 2.95, 0.0, 7.3)
    ops.node(123002, 2.95, 0.0, 8.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4087, 174034, 123002, 0.1225, 27999629.86923208, 11666512.44551337, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24087, 52.03508577, 0.00048595, 63.39697566, 0.03211688, 6.33969757, 0.09942916, -52.03508577, -0.00048595, -63.39697566, -0.03211688, -6.33969757, -0.09942916, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14087, 45.25305959, 0.00048595, 55.1340903, 0.03211688, 5.51340903, 0.09942916, -45.25305959, -0.00048595, -55.1340903, -0.03211688, -5.51340903, -0.09942916, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24087, 4087, 0.0, 164.95615574, 0.00971897, 164.95615574, 0.0291569, 115.46930902, -4929.42408027, 0.05, 2, 0, 74034, 23002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44087, 41.23903894, 4.934e-05, 123.71711681, 0.00014803, 412.39038935, 0.00049343, -41.23903894, -4.934e-05, -123.71711681, -0.00014803, -412.39038935, -0.00049343, 0.4, 0.3, 0.003, 0.0, 0.0, 24087, 2)
    ops.limitCurve('ThreePoint', 14087, 4087, 0.0, 164.95615574, 0.00971897, 164.95615574, 0.0291569, 115.46930902, -4929.42408027, 0.05, 2, 0, 74034, 23002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34087, 41.23903894, 4.934e-05, 123.71711681, 0.00014803, 412.39038935, 0.00049343, -41.23903894, -4.934e-05, -123.71711681, -0.00014803, -412.39038935, -0.00049343, 0.4, 0.3, 0.003, 0.0, 0.0, 14087, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4087, 99999, 'P', 44087, 'Vy', 34087, 'Vz', 24087, 'My', 14087, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174034, 74034, 174034, 4087, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123002, 123002, 23002, 4087, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173001, 0.0, 0.0, 8.85)
    ops.node(124035, 0.0, 0.0, 9.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4089, 173001, 124035, 0.0625, 26974896.77281971, 11239540.32200821, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24089, 15.74187038, 0.000534, 19.26573961, 0.02410413, 1.92657396, 0.08618193, -15.74187038, -0.000534, -19.26573961, -0.02410413, -1.92657396, -0.08618193, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14089, 15.74187038, 0.000534, 19.26573961, 0.02410413, 1.92657396, 0.08618193, -15.74187038, -0.000534, -19.26573961, -0.02410413, -1.92657396, -0.08618193, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24089, 4089, 0.0, 60.23256851, 0.01068004, 60.23256851, 0.03204011, 42.16279795, -3105.04040491, 0.05, 2, 0, 73001, 24035, 2, 3)
    ops.uniaxialMaterial('LimitState', 44089, 15.05814213, 3.666e-05, 45.17442638, 0.00010997, 150.58142126, 0.00036655, -15.05814213, -3.666e-05, -45.17442638, -0.00010997, -150.58142126, -0.00036655, 0.4, 0.3, 0.003, 0.0, 0.0, 24089, 2)
    ops.limitCurve('ThreePoint', 14089, 4089, 0.0, 60.23256851, 0.01068004, 60.23256851, 0.03204011, 42.16279795, -3105.04040491, 0.05, 2, 0, 73001, 24035, 1, 3)
    ops.uniaxialMaterial('LimitState', 34089, 15.05814213, 3.666e-05, 45.17442638, 0.00010997, 150.58142126, 0.00036655, -15.05814213, -3.666e-05, -45.17442638, -0.00010997, -150.58142126, -0.00036655, 0.4, 0.3, 0.003, 0.0, 0.0, 14089, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4089, 99999, 'P', 44089, 'Vy', 34089, 'Vz', 24089, 'My', 14089, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173001, 73001, 173001, 4089, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124035, 124035, 24035, 4089, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174035, 0.0, 0.0, 10.15)
    ops.node(124001, 0.0, 0.0, 11.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4090, 174035, 124001, 0.0625, 27929099.32506092, 11637124.71877538, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24090, 12.58796434, 0.00053821, 15.40466277, 0.02455801, 1.54046628, 0.09086469, -12.58796434, -0.00053821, -15.40466277, -0.02455801, -1.54046628, -0.09086469, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14090, 12.58796434, 0.00053821, 15.40466277, 0.02455801, 1.54046628, 0.09086469, -12.58796434, -0.00053821, -15.40466277, -0.02455801, -1.54046628, -0.09086469, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24090, 4090, 0.0, 59.13863324, 0.01076428, 59.13863324, 0.03229284, 41.39704327, -15473.36840944, 0.05, 2, 0, 74035, 24001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44090, 14.78465831, 3.476e-05, 44.35397493, 0.00010428, 147.84658309, 0.0003476, -14.78465831, -3.476e-05, -44.35397493, -0.00010428, -147.84658309, -0.0003476, 0.4, 0.3, 0.003, 0.0, 0.0, 24090, 2)
    ops.limitCurve('ThreePoint', 14090, 4090, 0.0, 59.13863324, 0.01076428, 59.13863324, 0.03229284, 41.39704327, -15473.36840944, 0.05, 2, 0, 74035, 24001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34090, 14.78465831, 3.476e-05, 44.35397493, 0.00010428, 147.84658309, 0.0003476, -14.78465831, -3.476e-05, -44.35397493, -0.00010428, -147.84658309, -0.0003476, 0.4, 0.3, 0.003, 0.0, 0.0, 14090, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4090, 99999, 'P', 44090, 'Vy', 34090, 'Vz', 24090, 'My', 14090, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174035, 74035, 174035, 4090, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124001, 124001, 24001, 4090, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173002, 2.95, 0.0, 8.85)
    ops.node(124036, 2.95, 0.0, 9.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4091, 173002, 124036, 0.1225, 27714020.66030947, 11547508.60846228, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24091, 44.5220934, 0.00047762, 54.4204447, 0.03342757, 5.44204447, 0.10605271, -44.5220934, -0.00047762, -54.4204447, -0.03342757, -5.44204447, -0.10605271, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14091, 37.71768066, 0.00047762, 46.10324443, 0.03342757, 4.61032444, 0.10605271, -37.71768066, -0.00047762, -46.10324443, -0.03342757, -4.61032444, -0.10605271, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24091, 4091, 0.0, 153.51801153, 0.00955243, 153.51801153, 0.02865728, 107.46260807, -7999.89172948, 0.05, 2, 0, 73002, 24036, 2, 3)
    ops.uniaxialMaterial('LimitState', 44091, 38.37950288, 4.639e-05, 115.13850865, 0.00013918, 383.79502882, 0.00046395, -38.37950288, -4.639e-05, -115.13850865, -0.00013918, -383.79502882, -0.00046395, 0.4, 0.3, 0.003, 0.0, 0.0, 24091, 2)
    ops.limitCurve('ThreePoint', 14091, 4091, 0.0, 153.51801153, 0.00955243, 153.51801153, 0.02865728, 107.46260807, -7999.89172948, 0.05, 2, 0, 73002, 24036, 1, 3)
    ops.uniaxialMaterial('LimitState', 34091, 38.37950288, 4.639e-05, 115.13850865, 0.00013918, 383.79502882, 0.00046395, -38.37950288, -4.639e-05, -115.13850865, -0.00013918, -383.79502882, -0.00046395, 0.4, 0.3, 0.003, 0.0, 0.0, 14091, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4091, 99999, 'P', 44091, 'Vy', 34091, 'Vz', 24091, 'My', 14091, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173002, 73002, 173002, 4091, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124036, 124036, 24036, 4091, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174036, 2.95, 0.0, 10.15)
    ops.node(124002, 2.95, 0.0, 11.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4092, 174036, 124002, 0.1225, 27836748.27333391, 11598645.11388913, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24092, 40.89782946, 0.00046749, 50.02801627, 0.03410605, 5.00280163, 0.10904909, -40.89782946, -0.00046749, -50.02801627, -0.03410605, -5.00280163, -0.10904909, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14092, 34.18408949, 0.00046749, 41.81547549, 0.03410605, 4.18154755, 0.10904909, -34.18408949, -0.00046749, -41.81547549, -0.03410605, -4.18154755, -0.10904909, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24092, 4092, 0.0, 152.6231259, 0.00934976, 152.6231259, 0.02804929, 106.83618813, -15144.19808461, 0.05, 2, 0, 74036, 24002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44092, 38.15578147, 4.592e-05, 114.46734442, 0.00013776, 381.55781474, 0.00045921, -38.15578147, -4.592e-05, -114.46734442, -0.00013776, -381.55781474, -0.00045921, 0.4, 0.3, 0.003, 0.0, 0.0, 24092, 2)
    ops.limitCurve('ThreePoint', 14092, 4092, 0.0, 152.6231259, 0.00934976, 152.6231259, 0.02804929, 106.83618813, -15144.19808461, 0.05, 2, 0, 74036, 24002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34092, 38.15578147, 4.592e-05, 114.46734442, 0.00013776, 381.55781474, 0.00045921, -38.15578147, -4.592e-05, -114.46734442, -0.00013776, -381.55781474, -0.00045921, 0.4, 0.3, 0.003, 0.0, 0.0, 14092, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4092, 99999, 'P', 44092, 'Vy', 34092, 'Vz', 24092, 'My', 14092, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174036, 74036, 174036, 4092, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124002, 124002, 24002, 4092, '-orient', 0, 0, 1, 0, 1, 0)
