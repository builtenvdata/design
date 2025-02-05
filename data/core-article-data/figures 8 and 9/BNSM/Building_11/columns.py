import openseespy.opensees as ops


def add_columns() -> None:
    """Add components of all columns to ops domain (plastic hinges, column elements and nodes)
    """
    # Create elastic column element nodes
    ops.node(170003, 9.0, 0.0, 0.0)
    ops.node(121003, 9.0, 0.0, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3, 170003, 121003, 0.25, 26164800.56154356, 10902000.23397648, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20003, 241.59127119, 0.00078685, 293.46644628, 0.0236528, 29.34664463, 0.05666001, -241.59127119, -0.00078685, -293.46644628, -0.0236528, -29.34664463, -0.05666001, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10003, 258.08470074, 0.00078685, 313.50139263, 0.0236528, 31.35013926, 0.05666001, -258.08470074, -0.00078685, -313.50139263, -0.0236528, -31.35013926, -0.05666001, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20003, 3, 0.0, 252.47828394, 0.01573699, 252.47828394, 0.04721096, 176.73479876, -3177.09795747, 0.05, 2, 0, 70003, 21003, 2, 3)
    ops.uniaxialMaterial('LimitState', 40003, 63.11957098, 8.754e-05, 189.35871295, 0.00026262, 631.19570984, 0.00087541, -63.11957098, -8.754e-05, -189.35871295, -0.00026262, -631.19570984, -0.00087541, 0.4, 0.3, 0.003, 0.0, 0.0, 20003, 2)
    ops.limitCurve('ThreePoint', 10003, 3, 0.0, 252.47828394, 0.01573699, 252.47828394, 0.04721096, 176.73479876, -3177.09795747, 0.05, 2, 0, 70003, 21003, 1, 3)
    ops.uniaxialMaterial('LimitState', 30003, 63.11957098, 8.754e-05, 189.35871295, 0.00026262, 631.19570984, 0.00087541, -63.11957098, -8.754e-05, -189.35871295, -0.00026262, -631.19570984, -0.00087541, 0.4, 0.3, 0.003, 0.0, 0.0, 10003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3, 99999, 'P', 40003, 'Vy', 30003, 'Vz', 20003, 'My', 10003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170003, 70003, 170003, 3, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121003, 121003, 21003, 3, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170004, 14.95, 0.0, 0.0)
    ops.node(121004, 14.95, 0.0, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4, 170004, 121004, 0.1225, 27840449.32158704, 11600187.21732793, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20004, 95.84437391, 0.00094792, 116.11036776, 0.01580675, 11.61103678, 0.05343502, -95.84437391, -0.00094792, -116.11036776, -0.01580675, -11.61103678, -0.05343502, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10004, 84.10673408, 0.00094792, 101.89084062, 0.01580675, 10.18908406, 0.05343502, -84.10673408, -0.00094792, -101.89084062, -0.01580675, -10.18908406, -0.05343502, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20004, 4, 0.0, 138.68489435, 0.01895847, 138.68489435, 0.05687541, 97.07942604, -1817.1904297, 0.05, 2, 0, 70004, 21004, 2, 3)
    ops.uniaxialMaterial('LimitState', 40004, 34.67122359, 9.223e-05, 104.01367076, 0.00027668, 346.71223587, 0.00092227, -34.67122359, -9.223e-05, -104.01367076, -0.00027668, -346.71223587, -0.00092227, 0.4, 0.3, 0.003, 0.0, 0.0, 20004, 2)
    ops.limitCurve('ThreePoint', 10004, 4, 0.0, 138.68489435, 0.01895847, 138.68489435, 0.05687541, 97.07942604, -1817.1904297, 0.05, 2, 0, 70004, 21004, 1, 3)
    ops.uniaxialMaterial('LimitState', 30004, 34.67122359, 9.223e-05, 104.01367076, 0.00027668, 346.71223587, 0.00092227, -34.67122359, -9.223e-05, -104.01367076, -0.00027668, -346.71223587, -0.00092227, 0.4, 0.3, 0.003, 0.0, 0.0, 10004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4, 99999, 'P', 40004, 'Vy', 30004, 'Vz', 20004, 'My', 10004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170004, 70004, 170004, 4, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121004, 121004, 21004, 4, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170005, 0.0, 3.95, 0.0)
    ops.node(121005, 0.0, 3.95, 2.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 5, 170005, 121005, 0.1225, 27601235.31822017, 11500514.71592507, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20005, 93.29239513, 0.00095606, 113.14464609, 0.01541833, 11.31446461, 0.05364222, -93.29239513, -0.00095606, -113.14464609, -0.01541833, -11.31446461, -0.05364222, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10005, 81.77899532, 0.00095606, 99.18124055, 0.01541833, 9.91812406, 0.05364222, -81.77899532, -0.00095606, -99.18124055, -0.01541833, -9.91812406, -0.05364222, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20005, 5, 0.0, 134.10907283, 0.01912127, 134.10907283, 0.05736382, 93.87635098, -1756.42907715, 0.05, 2, 0, 70005, 21005, 2, 3)
    ops.uniaxialMaterial('LimitState', 40005, 33.52726821, 8.996e-05, 100.58180463, 0.00026987, 335.27268208, 0.00089957, -33.52726821, -8.996e-05, -100.58180463, -0.00026987, -335.27268208, -0.00089957, 0.4, 0.3, 0.003, 0.0, 0.0, 20005, 2)
    ops.limitCurve('ThreePoint', 10005, 5, 0.0, 134.10907283, 0.01912127, 134.10907283, 0.05736382, 93.87635098, -1756.42907715, 0.05, 2, 0, 70005, 21005, 1, 3)
    ops.uniaxialMaterial('LimitState', 30005, 33.52726821, 8.996e-05, 100.58180463, 0.00026987, 335.27268208, 0.00089957, -33.52726821, -8.996e-05, -100.58180463, -0.00026987, -335.27268208, -0.00089957, 0.4, 0.3, 0.003, 0.0, 0.0, 10005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 5, 99999, 'P', 40005, 'Vy', 30005, 'Vz', 20005, 'My', 10005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170005, 70005, 170005, 5, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121005, 121005, 21005, 5, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170006, 3.05, 3.95, 0.0)
    ops.node(121006, 3.05, 3.95, 2.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 6, 170006, 121006, 0.25, 27569694.28155567, 11487372.61731486, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20006, 313.07064081, 0.00080479, 379.40437086, 0.02976326, 37.94043709, 0.07162792, -313.07064081, -0.00080479, -379.40437086, -0.02976326, -37.94043709, -0.07162792, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10006, 330.00285199, 0.00080479, 399.92419639, 0.02976326, 39.99241964, 0.07162792, -330.00285199, -0.00080479, -399.92419639, -0.02976326, -39.99241964, -0.07162792, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20006, 6, 0.0, 307.15027855, 0.01609579, 307.15027855, 0.04828738, 215.00519498, -4555.76710067, 0.05, 2, 0, 70006, 21006, 2, 3)
    ops.uniaxialMaterial('LimitState', 40006, 76.78756964, 0.00010107, 230.36270891, 0.00030321, 767.87569637, 0.0010107, -76.78756964, -0.00010107, -230.36270891, -0.00030321, -767.87569637, -0.0010107, 0.4, 0.3, 0.003, 0.0, 0.0, 20006, 2)
    ops.limitCurve('ThreePoint', 10006, 6, 0.0, 307.15027855, 0.01609579, 307.15027855, 0.04828738, 215.00519498, -4555.76710067, 0.05, 2, 0, 70006, 21006, 1, 3)
    ops.uniaxialMaterial('LimitState', 30006, 76.78756964, 0.00010107, 230.36270891, 0.00030321, 767.87569637, 0.0010107, -76.78756964, -0.00010107, -230.36270891, -0.00030321, -767.87569637, -0.0010107, 0.4, 0.3, 0.003, 0.0, 0.0, 10006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 6, 99999, 'P', 40006, 'Vy', 30006, 'Vz', 20006, 'My', 10006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170006, 70006, 170006, 6, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121006, 121006, 21006, 6, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170007, 9.0, 3.95, 0.0)
    ops.node(121007, 9.0, 3.95, 2.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 7, 170007, 121007, 0.3025, 27373518.03730932, 11405632.51554555, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20007, 422.80479968, 0.000759, 512.05023046, 0.02869816, 51.20502305, 0.06635673, -422.80479968, -0.000759, -512.05023046, -0.02869816, -51.20502305, -0.06635673, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10007, 479.84432172, 0.000759, 581.12962698, 0.02869816, 58.1129627, 0.06635673, -479.84432172, -0.000759, -581.12962698, -0.02869816, -58.1129627, -0.06635673, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20007, 7, 0.0, 372.11480648, 0.01517997, 372.11480648, 0.04553991, 260.48036453, -4718.91966663, 0.05, 2, 0, 70007, 21007, 2, 3)
    ops.uniaxialMaterial('LimitState', 40007, 93.02870162, 0.00010192, 279.08610486, 0.00030576, 930.28701619, 0.00101921, -93.02870162, -0.00010192, -279.08610486, -0.00030576, -930.28701619, -0.00101921, 0.4, 0.3, 0.003, 0.0, 0.0, 20007, 2)
    ops.limitCurve('ThreePoint', 10007, 7, 0.0, 372.11480648, 0.01517997, 372.11480648, 0.04553991, 260.48036453, -4718.91966663, 0.05, 2, 0, 70007, 21007, 1, 3)
    ops.uniaxialMaterial('LimitState', 30007, 93.02870162, 0.00010192, 279.08610486, 0.00030576, 930.28701619, 0.00101921, -93.02870162, -0.00010192, -279.08610486, -0.00030576, -930.28701619, -0.00101921, 0.4, 0.3, 0.003, 0.0, 0.0, 10007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 7, 99999, 'P', 40007, 'Vy', 30007, 'Vz', 20007, 'My', 10007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170007, 70007, 170007, 7, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121007, 121007, 21007, 7, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170008, 14.95, 3.95, 0.0)
    ops.node(121008, 14.95, 3.95, 2.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 8, 170008, 121008, 0.2025, 27058245.626104, 11274269.01087667, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20008, 232.40024198, 0.00083529, 281.64508488, 0.02224921, 28.16450849, 0.05749474, -232.40024198, -0.00083529, -281.64508488, -0.02224921, -28.16450849, -0.05749474, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10008, 223.85400663, 0.00083529, 271.28793051, 0.02224921, 27.12879305, 0.05749474, -223.85400663, -0.00083529, -271.28793051, -0.02224921, -27.12879305, -0.05749474, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20008, 8, 0.0, 222.78118058, 0.01670573, 222.78118058, 0.0501172, 155.94682641, -2894.76469778, 0.05, 2, 0, 70008, 21008, 2, 3)
    ops.uniaxialMaterial('LimitState', 40008, 55.69529515, 9.221e-05, 167.08588544, 0.00027664, 556.95295145, 0.00092214, -55.69529515, -9.221e-05, -167.08588544, -0.00027664, -556.95295145, -0.00092214, 0.4, 0.3, 0.003, 0.0, 0.0, 20008, 2)
    ops.limitCurve('ThreePoint', 10008, 8, 0.0, 222.78118058, 0.01670573, 222.78118058, 0.0501172, 155.94682641, -2894.76469778, 0.05, 2, 0, 70008, 21008, 1, 3)
    ops.uniaxialMaterial('LimitState', 30008, 55.69529515, 9.221e-05, 167.08588544, 0.00027664, 556.95295145, 0.00092214, -55.69529515, -9.221e-05, -167.08588544, -0.00027664, -556.95295145, -0.00092214, 0.4, 0.3, 0.003, 0.0, 0.0, 10008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 8, 99999, 'P', 40008, 'Vy', 30008, 'Vz', 20008, 'My', 10008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170008, 70008, 170008, 8, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121008, 121008, 21008, 8, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170009, 0.0, 7.9, 0.0)
    ops.node(121009, 0.0, 7.9, 2.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 9, 170009, 121009, 0.1225, 27990151.46102585, 11662563.10876077, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20009, 92.65685779, 0.00095532, 112.33302645, 0.01586227, 11.23330264, 0.05477079, -92.65685779, -0.00095532, -112.33302645, -0.01586227, -11.23330264, -0.05477079, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10009, 81.33122022, 0.00095532, 98.60233048, 0.01586227, 9.86023305, 0.05477079, -81.33122022, -0.00095532, -98.60233048, -0.01586227, -9.86023305, -0.05477079, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20009, 9, 0.0, 135.82495372, 0.0191065, 135.82495372, 0.05731949, 95.07746761, -1779.48094649, 0.05, 2, 0, 70009, 21009, 2, 3)
    ops.uniaxialMaterial('LimitState', 40009, 33.95623843, 8.984e-05, 101.86871529, 0.00026953, 339.56238431, 0.00089842, -33.95623843, -8.984e-05, -101.86871529, -0.00026953, -339.56238431, -0.00089842, 0.4, 0.3, 0.003, 0.0, 0.0, 20009, 2)
    ops.limitCurve('ThreePoint', 10009, 9, 0.0, 135.82495372, 0.0191065, 135.82495372, 0.05731949, 95.07746761, -1779.48094649, 0.05, 2, 0, 70009, 21009, 1, 3)
    ops.uniaxialMaterial('LimitState', 30009, 33.95623843, 8.984e-05, 101.86871529, 0.00026953, 339.56238431, 0.00089842, -33.95623843, -8.984e-05, -101.86871529, -0.00026953, -339.56238431, -0.00089842, 0.4, 0.3, 0.003, 0.0, 0.0, 10009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 9, 99999, 'P', 40009, 'Vy', 30009, 'Vz', 20009, 'My', 10009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170009, 70009, 170009, 9, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121009, 121009, 21009, 9, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170010, 3.05, 7.9, 0.0)
    ops.node(121010, 3.05, 7.9, 2.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 10, 170010, 121010, 0.25, 27302653.53285908, 11376105.63869128, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20010, 305.32636575, 0.00078337, 370.26764669, 0.02993885, 37.02676467, 0.07184387, -305.32636575, -0.00078337, -370.26764669, -0.02993885, -37.02676467, -0.07184387, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10010, 322.17053841, 0.00078337, 390.69448458, 0.02993885, 39.06944846, 0.07184387, -322.17053841, -0.00078337, -390.69448458, -0.02993885, -39.06944846, -0.07184387, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20010, 10, 0.0, 300.421478, 0.01566731, 300.421478, 0.04700194, 210.2950346, -4459.66165601, 0.05, 2, 0, 70010, 21010, 2, 3)
    ops.uniaxialMaterial('LimitState', 40010, 75.1053695, 9.982e-05, 225.3161085, 0.00029947, 751.05369501, 0.00099823, -75.1053695, -9.982e-05, -225.3161085, -0.00029947, -751.05369501, -0.00099823, 0.4, 0.3, 0.003, 0.0, 0.0, 20010, 2)
    ops.limitCurve('ThreePoint', 10010, 10, 0.0, 300.421478, 0.01566731, 300.421478, 0.04700194, 210.2950346, -4459.66165601, 0.05, 2, 0, 70010, 21010, 1, 3)
    ops.uniaxialMaterial('LimitState', 30010, 75.1053695, 9.982e-05, 225.3161085, 0.00029947, 751.05369501, 0.00099823, -75.1053695, -9.982e-05, -225.3161085, -0.00029947, -751.05369501, -0.00099823, 0.4, 0.3, 0.003, 0.0, 0.0, 10010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 10, 99999, 'P', 40010, 'Vy', 30010, 'Vz', 20010, 'My', 10010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170010, 70010, 170010, 10, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121010, 121010, 21010, 10, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170011, 9.0, 7.9, 0.0)
    ops.node(121011, 9.0, 7.9, 2.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 11, 170011, 121011, 0.3025, 27223283.14499593, 11343034.6437483, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20011, 463.23424848, 0.00076155, 561.08718541, 0.02897519, 56.10871854, 0.06638329, -463.23424848, -0.00076155, -561.08718541, -0.02897519, -56.10871854, -0.06638329, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10011, 501.6093408, 0.00076155, 607.56857708, 0.02897519, 60.75685771, 0.06638329, -501.6093408, -0.00076155, -607.56857708, -0.02897519, -60.75685771, -0.06638329, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20011, 11, 0.0, 371.14559887, 0.01523104, 371.14559887, 0.04569313, 259.80191921, -4736.08242454, 0.05, 2, 0, 70011, 21011, 2, 3)
    ops.uniaxialMaterial('LimitState', 40011, 92.78639972, 0.00010222, 278.35919915, 0.00030665, 927.86399718, 0.00102217, -92.78639972, -0.00010222, -278.35919915, -0.00030665, -927.86399718, -0.00102217, 0.4, 0.3, 0.003, 0.0, 0.0, 20011, 2)
    ops.limitCurve('ThreePoint', 10011, 11, 0.0, 371.14559887, 0.01523104, 371.14559887, 0.04569313, 259.80191921, -4736.08242454, 0.05, 2, 0, 70011, 21011, 1, 3)
    ops.uniaxialMaterial('LimitState', 30011, 92.78639972, 0.00010222, 278.35919915, 0.00030665, 927.86399718, 0.00102217, -92.78639972, -0.00010222, -278.35919915, -0.00030665, -927.86399718, -0.00102217, 0.4, 0.3, 0.003, 0.0, 0.0, 10011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 11, 99999, 'P', 40011, 'Vy', 30011, 'Vz', 20011, 'My', 10011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170011, 70011, 170011, 11, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121011, 121011, 21011, 11, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170012, 14.95, 7.9, 0.0)
    ops.node(121012, 14.95, 7.9, 2.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 12, 170012, 121012, 0.2025, 27994260.73399261, 11664275.30583026, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20012, 231.23242002, 0.00082361, 279.96267341, 0.02224803, 27.99626734, 0.05888936, -231.23242002, -0.00082361, -279.96267341, -0.02224803, -27.99626734, -0.05888936, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10012, 222.84734528, 0.00082361, 269.81051594, 0.02224803, 26.98105159, 0.05888936, -222.84734528, -0.00082361, -269.81051594, -0.02224803, -26.98105159, -0.05888936, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20012, 12, 0.0, 226.67837925, 0.01647215, 226.67837925, 0.04941646, 158.67486547, -2841.44570754, 0.05, 2, 0, 70012, 21012, 2, 3)
    ops.uniaxialMaterial('LimitState', 40012, 56.66959481, 9.069e-05, 170.00878443, 0.00027207, 566.69594811, 0.0009069, -56.66959481, -9.069e-05, -170.00878443, -0.00027207, -566.69594811, -0.0009069, 0.4, 0.3, 0.003, 0.0, 0.0, 20012, 2)
    ops.limitCurve('ThreePoint', 10012, 12, 0.0, 226.67837925, 0.01647215, 226.67837925, 0.04941646, 158.67486547, -2841.44570754, 0.05, 2, 0, 70012, 21012, 1, 3)
    ops.uniaxialMaterial('LimitState', 30012, 56.66959481, 9.069e-05, 170.00878443, 0.00027207, 566.69594811, 0.0009069, -56.66959481, -9.069e-05, -170.00878443, -0.00027207, -566.69594811, -0.0009069, 0.4, 0.3, 0.003, 0.0, 0.0, 10012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 12, 99999, 'P', 40012, 'Vy', 30012, 'Vz', 20012, 'My', 10012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170012, 70012, 170012, 12, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121012, 121012, 21012, 12, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170013, 0.0, 11.85, 0.0)
    ops.node(121013, 0.0, 11.85, 2.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 13, 170013, 121013, 0.1225, 27797306.29059401, 11582210.95441417, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20013, 93.06358753, 0.00092547, 112.85515367, 0.01585078, 11.28551537, 0.0545024, -93.06358753, -0.00092547, -112.85515367, -0.01585078, -11.28551537, -0.0545024, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10013, 81.12866603, 0.00092547, 98.38206666, 0.01585078, 9.83820667, 0.0545024, -81.12866603, -0.00092547, -98.38206666, -0.01585078, -9.83820667, -0.0545024, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20013, 13, 0.0, 136.0326623, 0.0185094, 136.0326623, 0.05552819, 95.22286361, -1810.96595782, 0.05, 2, 0, 70013, 21013, 2, 3)
    ops.uniaxialMaterial('LimitState', 40013, 34.00816557, 9.06e-05, 102.02449672, 0.00027181, 340.08165574, 0.00090604, -34.00816557, -9.06e-05, -102.02449672, -0.00027181, -340.08165574, -0.00090604, 0.4, 0.3, 0.003, 0.0, 0.0, 20013, 2)
    ops.limitCurve('ThreePoint', 10013, 13, 0.0, 136.0326623, 0.0185094, 136.0326623, 0.05552819, 95.22286361, -1810.96595782, 0.05, 2, 0, 70013, 21013, 1, 3)
    ops.uniaxialMaterial('LimitState', 30013, 34.00816557, 9.06e-05, 102.02449672, 0.00027181, 340.08165574, 0.00090604, -34.00816557, -9.06e-05, -102.02449672, -0.00027181, -340.08165574, -0.00090604, 0.4, 0.3, 0.003, 0.0, 0.0, 10013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 13, 99999, 'P', 40013, 'Vy', 30013, 'Vz', 20013, 'My', 10013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170013, 70013, 170013, 13, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121013, 121013, 21013, 13, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170014, 3.05, 11.85, 0.0)
    ops.node(121014, 3.05, 11.85, 2.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 14, 170014, 121014, 0.25, 26832014.25445624, 11180005.93935677, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20014, 307.92471152, 0.00081819, 373.58254939, 0.02967815, 37.35825494, 0.07077653, -307.92471152, -0.00081819, -373.58254939, -0.02967815, -37.35825494, -0.07077653, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10014, 324.4678195, 0.00081819, 393.65309333, 0.02967815, 39.36530933, 0.07077653, -324.4678195, -0.00081819, -393.65309333, -0.02967815, -39.36530933, -0.07077653, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20014, 14, 0.0, 296.17269891, 0.01636382, 296.17269891, 0.04909145, 207.32088923, -4429.56502233, 0.05, 2, 0, 70014, 21014, 2, 3)
    ops.uniaxialMaterial('LimitState', 40014, 74.04317473, 0.00010014, 222.12952418, 0.00030041, 740.43174726, 0.00100137, -74.04317473, -0.00010014, -222.12952418, -0.00030041, -740.43174726, -0.00100137, 0.4, 0.3, 0.003, 0.0, 0.0, 20014, 2)
    ops.limitCurve('ThreePoint', 10014, 14, 0.0, 296.17269891, 0.01636382, 296.17269891, 0.04909145, 207.32088923, -4429.56502233, 0.05, 2, 0, 70014, 21014, 1, 3)
    ops.uniaxialMaterial('LimitState', 30014, 74.04317473, 0.00010014, 222.12952418, 0.00030041, 740.43174726, 0.00100137, -74.04317473, -0.00010014, -222.12952418, -0.00030041, -740.43174726, -0.00100137, 0.4, 0.3, 0.003, 0.0, 0.0, 10014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 14, 99999, 'P', 40014, 'Vy', 30014, 'Vz', 20014, 'My', 10014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170014, 70014, 170014, 14, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121014, 121014, 21014, 14, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170015, 9.0, 11.85, 0.0)
    ops.node(121015, 9.0, 11.85, 2.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 15, 170015, 121015, 0.3025, 27764742.8153908, 11568642.83974617, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20015, 471.55172223, 0.0007646, 570.86517633, 0.0290998, 57.08651763, 0.06739075, -471.55172223, -0.0007646, -570.86517633, -0.0290998, -57.08651763, -0.06739075, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10015, 510.97773583, 0.0007646, 618.59469813, 0.0290998, 61.85946981, 0.06739075, -510.97773583, -0.0007646, -618.59469813, -0.0290998, -61.85946981, -0.06739075, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20015, 15, 0.0, 375.86143579, 0.01529202, 375.86143579, 0.04587607, 263.10300505, -4714.32928192, 0.05, 2, 0, 70015, 21015, 2, 3)
    ops.uniaxialMaterial('LimitState', 40015, 93.96535895, 0.0001015, 281.89607684, 0.00030449, 939.65358947, 0.00101497, -93.96535895, -0.0001015, -281.89607684, -0.00030449, -939.65358947, -0.00101497, 0.4, 0.3, 0.003, 0.0, 0.0, 20015, 2)
    ops.limitCurve('ThreePoint', 10015, 15, 0.0, 375.86143579, 0.01529202, 375.86143579, 0.04587607, 263.10300505, -4714.32928192, 0.05, 2, 0, 70015, 21015, 1, 3)
    ops.uniaxialMaterial('LimitState', 30015, 93.96535895, 0.0001015, 281.89607684, 0.00030449, 939.65358947, 0.00101497, -93.96535895, -0.0001015, -281.89607684, -0.00030449, -939.65358947, -0.00101497, 0.4, 0.3, 0.003, 0.0, 0.0, 10015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 15, 99999, 'P', 40015, 'Vy', 30015, 'Vz', 20015, 'My', 10015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170015, 70015, 170015, 15, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121015, 121015, 21015, 15, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170016, 14.95, 11.85, 0.0)
    ops.node(121016, 14.95, 11.85, 2.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 16, 170016, 121016, 0.2025, 26998694.20683129, 11249455.91951304, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20016, 231.29749038, 0.00084006, 280.32210493, 0.0220013, 28.03221049, 0.05715281, -231.29749038, -0.00084006, -280.32210493, -0.0220013, -28.03221049, -0.05715281, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10016, 222.90001054, 0.00084006, 270.14473889, 0.0220013, 27.01447389, 0.05715281, -222.90001054, -0.00084006, -270.14473889, -0.0220013, -27.01447389, -0.05715281, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20016, 16, 0.0, 220.56002325, 0.01680118, 220.56002325, 0.05040355, 154.39201628, -2834.37958818, 0.05, 2, 0, 70016, 21016, 2, 3)
    ops.uniaxialMaterial('LimitState', 40016, 55.14000581, 9.15e-05, 165.42001744, 0.00027449, 551.40005813, 0.00091496, -55.14000581, -9.15e-05, -165.42001744, -0.00027449, -551.40005813, -0.00091496, 0.4, 0.3, 0.003, 0.0, 0.0, 20016, 2)
    ops.limitCurve('ThreePoint', 10016, 16, 0.0, 220.56002325, 0.01680118, 220.56002325, 0.05040355, 154.39201628, -2834.37958818, 0.05, 2, 0, 70016, 21016, 1, 3)
    ops.uniaxialMaterial('LimitState', 30016, 55.14000581, 9.15e-05, 165.42001744, 0.00027449, 551.40005813, 0.00091496, -55.14000581, -9.15e-05, -165.42001744, -0.00027449, -551.40005813, -0.00091496, 0.4, 0.3, 0.003, 0.0, 0.0, 10016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 16, 99999, 'P', 40016, 'Vy', 30016, 'Vz', 20016, 'My', 10016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170016, 70016, 170016, 16, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121016, 121016, 21016, 16, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170017, 0.0, 15.8, 0.0)
    ops.node(121017, 0.0, 15.8, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 17, 170017, 121017, 0.09, 28401895.65062046, 11834123.18775853, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20017, 54.57729683, 0.00106094, 66.24596243, 0.01697081, 6.62459624, 0.06367268, -54.57729683, -0.00106094, -66.24596243, -0.01697081, -6.62459624, -0.06367268, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10017, 50.09939351, 0.00106094, 60.81068014, 0.01697081, 6.08106801, 0.06367268, -50.09939351, -0.00106094, -60.81068014, -0.01697081, -6.08106801, -0.06367268, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20017, 17, 0.0, 105.68621428, 0.02121885, 105.68621428, 0.06365656, 73.98034999, -1674.03655221, 0.05, 2, 0, 70017, 21017, 2, 3)
    ops.uniaxialMaterial('LimitState', 40017, 26.42155357, 9.377e-05, 79.26466071, 0.00028131, 264.2155357, 0.00093772, -26.42155357, -9.377e-05, -79.26466071, -0.00028131, -264.2155357, -0.00093772, 0.4, 0.3, 0.003, 0.0, 0.0, 20017, 2)
    ops.limitCurve('ThreePoint', 10017, 17, 0.0, 105.68621428, 0.02121885, 105.68621428, 0.06365656, 73.98034999, -1674.03655221, 0.05, 2, 0, 70017, 21017, 1, 3)
    ops.uniaxialMaterial('LimitState', 30017, 26.42155357, 9.377e-05, 79.26466071, 0.00028131, 264.2155357, 0.00093772, -26.42155357, -9.377e-05, -79.26466071, -0.00028131, -264.2155357, -0.00093772, 0.4, 0.3, 0.003, 0.0, 0.0, 10017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 17, 99999, 'P', 40017, 'Vy', 30017, 'Vz', 20017, 'My', 10017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170017, 70017, 170017, 17, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121017, 121017, 21017, 17, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170018, 3.05, 15.8, 0.0)
    ops.node(121018, 3.05, 15.8, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 18, 170018, 121018, 0.16, 28627128.22616072, 11927970.09423363, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20018, 155.46520518, 0.00085969, 188.057083, 0.01505572, 18.8057083, 0.04976201, -155.46520518, -0.00085969, -188.057083, -0.01505572, -18.8057083, -0.04976201, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10018, 162.73212615, 0.00085969, 196.84744839, 0.01505572, 19.68474484, 0.04976201, -162.73212615, -0.00085969, -196.84744839, -0.01505572, -19.68474484, -0.04976201, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20018, 18, 0.0, 173.8201903, 0.01719371, 173.8201903, 0.05158114, 121.67413321, -1981.88065587, 0.05, 2, 0, 70018, 21018, 2, 3)
    ops.uniaxialMaterial('LimitState', 40018, 43.45504757, 8.607e-05, 130.36514272, 0.00025821, 434.55047574, 0.00086069, -43.45504757, -8.607e-05, -130.36514272, -0.00025821, -434.55047574, -0.00086069, 0.4, 0.3, 0.003, 0.0, 0.0, 20018, 2)
    ops.limitCurve('ThreePoint', 10018, 18, 0.0, 173.8201903, 0.01719371, 173.8201903, 0.05158114, 121.67413321, -1981.88065587, 0.05, 2, 0, 70018, 21018, 1, 3)
    ops.uniaxialMaterial('LimitState', 30018, 43.45504757, 8.607e-05, 130.36514272, 0.00025821, 434.55047574, 0.00086069, -43.45504757, -8.607e-05, -130.36514272, -0.00025821, -434.55047574, -0.00086069, 0.4, 0.3, 0.003, 0.0, 0.0, 10018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 18, 99999, 'P', 40018, 'Vy', 30018, 'Vz', 20018, 'My', 10018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170018, 70018, 170018, 18, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121018, 121018, 21018, 18, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170019, 9.0, 15.8, 0.0)
    ops.node(121019, 9.0, 15.8, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 19, 170019, 121019, 0.25, 27724384.06680581, 11551826.69450242, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20019, 241.17006963, 0.00077367, 292.51455948, 0.02424202, 29.25145595, 0.05935457, -241.17006963, -0.00077367, -292.51455948, -0.02424202, -29.25145595, -0.05935457, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10019, 257.24745389, 0.00077367, 312.01477765, 0.02424202, 31.20147776, 0.05935457, -257.24745389, -0.00077367, -312.01477765, -0.02424202, -31.20147776, -0.05935457, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20019, 19, 0.0, 266.30422068, 0.01547336, 266.30422068, 0.04642009, 186.41295448, -3258.88216825, 0.05, 2, 0, 70019, 21019, 2, 3)
    ops.uniaxialMaterial('LimitState', 40019, 66.57605517, 8.714e-05, 199.72816551, 0.00026142, 665.76055171, 0.0008714, -66.57605517, -8.714e-05, -199.72816551, -0.00026142, -665.76055171, -0.0008714, 0.4, 0.3, 0.003, 0.0, 0.0, 20019, 2)
    ops.limitCurve('ThreePoint', 10019, 19, 0.0, 266.30422068, 0.01547336, 266.30422068, 0.04642009, 186.41295448, -3258.88216825, 0.05, 2, 0, 70019, 21019, 1, 3)
    ops.uniaxialMaterial('LimitState', 30019, 66.57605517, 8.714e-05, 199.72816551, 0.00026142, 665.76055171, 0.0008714, -66.57605517, -8.714e-05, -199.72816551, -0.00026142, -665.76055171, -0.0008714, 0.4, 0.3, 0.003, 0.0, 0.0, 10019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 19, 99999, 'P', 40019, 'Vy', 30019, 'Vz', 20019, 'My', 10019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170019, 70019, 170019, 19, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121019, 121019, 21019, 19, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170020, 14.95, 15.8, 0.0)
    ops.node(121020, 14.95, 15.8, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 20, 170020, 121020, 0.1225, 28599797.08678026, 11916582.11949178, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20020, 95.9161638, 0.00094438, 116.07818777, 0.01585493, 11.60781878, 0.05452264, -95.9161638, -0.00094438, -116.07818777, -0.01585493, -11.60781878, -0.05452264, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10020, 84.29463973, 0.00094438, 102.01376527, 0.01585493, 10.20137653, 0.05452264, -84.29463973, -0.00094438, -102.01376527, -0.01585493, -10.20137653, -0.05452264, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20020, 20, 0.0, 140.44578034, 0.01888769, 140.44578034, 0.05666308, 98.31204623, -1783.94071789, 0.05, 2, 0, 70020, 21020, 2, 3)
    ops.uniaxialMaterial('LimitState', 40020, 35.11144508, 9.092e-05, 105.33433525, 0.00027276, 351.11445084, 0.00090919, -35.11144508, -9.092e-05, -105.33433525, -0.00027276, -351.11445084, -0.00090919, 0.4, 0.3, 0.003, 0.0, 0.0, 20020, 2)
    ops.limitCurve('ThreePoint', 10020, 20, 0.0, 140.44578034, 0.01888769, 140.44578034, 0.05666308, 98.31204623, -1783.94071789, 0.05, 2, 0, 70020, 21020, 1, 3)
    ops.uniaxialMaterial('LimitState', 30020, 35.11144508, 9.092e-05, 105.33433525, 0.00027276, 351.11445084, 0.00090919, -35.11144508, -9.092e-05, -105.33433525, -0.00027276, -351.11445084, -0.00090919, 0.4, 0.3, 0.003, 0.0, 0.0, 10020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 20, 99999, 'P', 40020, 'Vy', 30020, 'Vz', 20020, 'My', 10020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170020, 70020, 170020, 20, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121020, 121020, 21020, 20, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171003, 9.0, 0.0, 3.45)
    ops.node(122003, 9.0, 0.0, 6.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1003, 171003, 122003, 0.25, 26589646.42101824, 11079019.34209093, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21003, 233.33004537, 0.0007723, 284.23015053, 0.01781101, 28.42301505, 0.0460343, -233.33004537, -0.0007723, -284.23015053, -0.01781101, -28.42301505, -0.0460343, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11003, 217.45130465, 0.0007723, 264.88751997, 0.01781101, 26.488752, 0.0460343, -217.45130465, -0.0007723, -264.88751997, -0.01781101, -26.488752, -0.0460343, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21003, 1003, 0.0, 209.17705643, 0.01544596, 209.17705643, 0.04633787, 146.4239395, -2070.03263796, 0.05, 2, 0, 71003, 22003, 2, 3)
    ops.uniaxialMaterial('LimitState', 41003, 52.29426411, 7.137e-05, 156.88279232, 0.0002141, 522.94264107, 0.00071368, -52.29426411, -7.137e-05, -156.88279232, -0.0002141, -522.94264107, -0.00071368, 0.4, 0.3, 0.003, 0.0, 0.0, 21003, 2)
    ops.limitCurve('ThreePoint', 11003, 1003, 0.0, 209.17705643, 0.01544596, 209.17705643, 0.04633787, 146.4239395, -2070.03263796, 0.05, 2, 0, 71003, 22003, 1, 3)
    ops.uniaxialMaterial('LimitState', 31003, 52.29426411, 7.137e-05, 156.88279232, 0.0002141, 522.94264107, 0.00071368, -52.29426411, -7.137e-05, -156.88279232, -0.0002141, -522.94264107, -0.00071368, 0.4, 0.3, 0.003, 0.0, 0.0, 11003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1003, 99999, 'P', 41003, 'Vy', 31003, 'Vz', 21003, 'My', 11003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171003, 71003, 171003, 1003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122003, 122003, 22003, 1003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171004, 14.95, 0.0, 3.45)
    ops.node(122004, 14.95, 0.0, 6.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1004, 171004, 122004, 0.1225, 27747346.85397518, 11561394.52248966, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21004, 102.30157071, 0.00095034, 124.32517644, 0.01671029, 12.43251764, 0.05777348, -102.30157071, -0.00095034, -124.32517644, -0.01671029, -12.43251764, -0.05777348, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11004, 84.5187117, 0.00095034, 102.71400206, 0.01671029, 10.27140021, 0.05777348, -84.5187117, -0.00095034, -102.71400206, -0.01671029, -10.27140021, -0.05777348, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21004, 1004, 0.0, 132.92094041, 0.01900675, 132.92094041, 0.05702026, 93.04465828, -1937.07435449, 0.05, 2, 0, 71004, 22004, 2, 3)
    ops.uniaxialMaterial('LimitState', 41004, 33.2302351, 8.869e-05, 99.6907053, 0.00026607, 332.30235101, 0.00088691, -33.2302351, -8.869e-05, -99.6907053, -0.00026607, -332.30235101, -0.00088691, 0.4, 0.3, 0.003, 0.0, 0.0, 21004, 2)
    ops.limitCurve('ThreePoint', 11004, 1004, 0.0, 132.92094041, 0.01900675, 132.92094041, 0.05702026, 93.04465828, -1937.07435449, 0.05, 2, 0, 71004, 22004, 1, 3)
    ops.uniaxialMaterial('LimitState', 31004, 33.2302351, 8.869e-05, 99.6907053, 0.00026607, 332.30235101, 0.00088691, -33.2302351, -8.869e-05, -99.6907053, -0.00026607, -332.30235101, -0.00088691, 0.4, 0.3, 0.003, 0.0, 0.0, 11004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1004, 99999, 'P', 41004, 'Vy', 31004, 'Vz', 21004, 'My', 11004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171004, 71004, 171004, 1004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122004, 122004, 22004, 1004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171005, 0.0, 3.95, 3.5)
    ops.node(122005, 0.0, 3.95, 5.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1005, 171005, 122005, 0.1225, 26506509.15412935, 11044378.81422056, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21005, 85.44704577, 0.00093436, 104.06243768, 0.0166767, 10.40624377, 0.05680474, -85.44704577, -0.00093436, -104.06243768, -0.0166767, -10.40624377, -0.05680474, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11005, 73.7758819, 0.00093436, 89.84860792, 0.0166767, 8.98486079, 0.05680474, -73.7758819, -0.00093436, -89.84860792, -0.0166767, -8.98486079, -0.05680474, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21005, 1005, 0.0, 129.23942714, 0.0186873, 129.23942714, 0.05606189, 90.467599, -2029.64009519, 0.05, 2, 0, 71005, 22005, 2, 3)
    ops.uniaxialMaterial('LimitState', 41005, 32.30985679, 9.027e-05, 96.92957036, 0.00027081, 323.09856785, 0.00090271, -32.30985679, -9.027e-05, -96.92957036, -0.00027081, -323.09856785, -0.00090271, 0.4, 0.3, 0.003, 0.0, 0.0, 21005, 2)
    ops.limitCurve('ThreePoint', 11005, 1005, 0.0, 129.23942714, 0.0186873, 129.23942714, 0.05606189, 90.467599, -2029.64009519, 0.05, 2, 0, 71005, 22005, 1, 3)
    ops.uniaxialMaterial('LimitState', 31005, 32.30985679, 9.027e-05, 96.92957036, 0.00027081, 323.09856785, 0.00090271, -32.30985679, -9.027e-05, -96.92957036, -0.00027081, -323.09856785, -0.00090271, 0.4, 0.3, 0.003, 0.0, 0.0, 11005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1005, 99999, 'P', 41005, 'Vy', 31005, 'Vz', 21005, 'My', 11005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171005, 71005, 171005, 1005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122005, 122005, 22005, 1005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171006, 3.05, 3.95, 3.5)
    ops.node(122006, 3.05, 3.95, 5.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1006, 171006, 122006, 0.25, 27586072.2657209, 11494196.77738371, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21006, 239.26215322, 0.00077507, 290.79982614, 0.03014476, 29.07998261, 0.07584567, -239.26215322, -0.00077507, -290.79982614, -0.03014476, -29.07998261, -0.07584567, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11006, 223.86123405, 0.00077507, 272.08151004, 0.03014476, 27.208151, 0.07584567, -223.86123405, -0.00077507, -272.08151004, -0.03014476, -27.208151, -0.07584567, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21006, 1006, 0.0, 292.01386485, 0.01550143, 292.01386485, 0.04650428, 204.40970539, -4745.06651085, 0.05, 2, 0, 71006, 22006, 2, 3)
    ops.uniaxialMaterial('LimitState', 41006, 73.00346621, 9.603e-05, 219.01039863, 0.0002881, 730.03466211, 0.00096032, -73.00346621, -9.603e-05, -219.01039863, -0.0002881, -730.03466211, -0.00096032, 0.4, 0.3, 0.003, 0.0, 0.0, 21006, 2)
    ops.limitCurve('ThreePoint', 11006, 1006, 0.0, 292.01386485, 0.01550143, 292.01386485, 0.04650428, 204.40970539, -4745.06651085, 0.05, 2, 0, 71006, 22006, 1, 3)
    ops.uniaxialMaterial('LimitState', 31006, 73.00346621, 9.603e-05, 219.01039863, 0.0002881, 730.03466211, 0.00096032, -73.00346621, -9.603e-05, -219.01039863, -0.0002881, -730.03466211, -0.00096032, 0.4, 0.3, 0.003, 0.0, 0.0, 11006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1006, 99999, 'P', 41006, 'Vy', 31006, 'Vz', 21006, 'My', 11006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171006, 71006, 171006, 1006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122006, 122006, 22006, 1006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171007, 9.0, 3.95, 3.5)
    ops.node(122007, 9.0, 3.95, 5.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1007, 171007, 122007, 0.3025, 26674244.54409361, 11114268.560039, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21007, 339.05188611, 0.00074553, 412.2928311, 0.02002459, 41.22928311, 0.04846764, -339.05188611, -0.00074553, -412.2928311, -0.02002459, -41.22928311, -0.04846764, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11007, 302.24508397, 0.00074553, 367.53513684, 0.02002459, 36.75351368, 0.04846764, -302.24508397, -0.00074553, -367.53513684, -0.02002459, -36.75351368, -0.04846764, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21007, 1007, 0.0, 287.47055076, 0.01491058, 287.47055076, 0.04473175, 201.22938554, -2784.10822784, 0.05, 2, 0, 71007, 22007, 2, 3)
    ops.uniaxialMaterial('LimitState', 41007, 71.86763769, 8.08e-05, 215.60291307, 0.0002424, 718.67637691, 0.00080801, -71.86763769, -8.08e-05, -215.60291307, -0.0002424, -718.67637691, -0.00080801, 0.4, 0.3, 0.003, 0.0, 0.0, 21007, 2)
    ops.limitCurve('ThreePoint', 11007, 1007, 0.0, 287.47055076, 0.01491058, 287.47055076, 0.04473175, 201.22938554, -2784.10822784, 0.05, 2, 0, 71007, 22007, 1, 3)
    ops.uniaxialMaterial('LimitState', 31007, 71.86763769, 8.08e-05, 215.60291307, 0.0002424, 718.67637691, 0.00080801, -71.86763769, -8.08e-05, -215.60291307, -0.0002424, -718.67637691, -0.00080801, 0.4, 0.3, 0.003, 0.0, 0.0, 11007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1007, 99999, 'P', 41007, 'Vy', 31007, 'Vz', 21007, 'My', 11007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171007, 71007, 171007, 1007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122007, 122007, 22007, 1007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171008, 14.95, 3.95, 3.5)
    ops.node(122008, 14.95, 3.95, 5.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1008, 171008, 122008, 0.2025, 26803919.79636461, 11168299.91515192, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21008, 187.22730647, 0.00081227, 227.73607345, 0.02859376, 22.77360735, 0.07666731, -187.22730647, -0.00081227, -227.73607345, -0.02859376, -22.77360735, -0.07666731, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11008, 163.63170985, 0.00081227, 199.0352999, 0.02859376, 19.90352999, 0.07666731, -163.63170985, -0.00081227, -199.0352999, -0.02859376, -19.90352999, -0.07666731, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21008, 1008, 0.0, 240.25459914, 0.01624543, 240.25459914, 0.0487363, 168.17821939, -4237.62079347, 0.05, 2, 0, 71008, 22008, 2, 3)
    ops.uniaxialMaterial('LimitState', 41008, 60.06364978, 0.00010039, 180.19094935, 0.00030117, 600.63649784, 0.0010039, -60.06364978, -0.00010039, -180.19094935, -0.00030117, -600.63649784, -0.0010039, 0.4, 0.3, 0.003, 0.0, 0.0, 21008, 2)
    ops.limitCurve('ThreePoint', 11008, 1008, 0.0, 240.25459914, 0.01624543, 240.25459914, 0.0487363, 168.17821939, -4237.62079347, 0.05, 2, 0, 71008, 22008, 1, 3)
    ops.uniaxialMaterial('LimitState', 31008, 60.06364978, 0.00010039, 180.19094935, 0.00030117, 600.63649784, 0.0010039, -60.06364978, -0.00010039, -180.19094935, -0.00030117, -600.63649784, -0.0010039, 0.4, 0.3, 0.003, 0.0, 0.0, 11008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1008, 99999, 'P', 41008, 'Vy', 31008, 'Vz', 21008, 'My', 11008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171008, 71008, 171008, 1008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122008, 122008, 22008, 1008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171009, 0.0, 7.9, 3.5)
    ops.node(122009, 0.0, 7.9, 5.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1009, 171009, 122009, 0.1225, 27940958.63968185, 11642066.09986744, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21009, 83.55886489, 0.00091649, 101.58463966, 0.01682926, 10.15846397, 0.05893975, -83.55886489, -0.00091649, -101.58463966, -0.01682926, -10.15846397, -0.05893975, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11009, 72.40142431, 0.00091649, 88.02025505, 0.01682926, 8.8020255, 0.05893975, -72.40142431, -0.00091649, -88.02025505, -0.01682926, -8.8020255, -0.05893975, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21009, 1009, 0.0, 132.55603663, 0.01832988, 132.55603663, 0.05498963, 92.78922564, -2000.03289045, 0.05, 2, 0, 71009, 22009, 2, 3)
    ops.uniaxialMaterial('LimitState', 41009, 33.13900916, 8.783e-05, 99.41702747, 0.0002635, 331.39009157, 0.00087835, -33.13900916, -8.783e-05, -99.41702747, -0.0002635, -331.39009157, -0.00087835, 0.4, 0.3, 0.003, 0.0, 0.0, 21009, 2)
    ops.limitCurve('ThreePoint', 11009, 1009, 0.0, 132.55603663, 0.01832988, 132.55603663, 0.05498963, 92.78922564, -2000.03289045, 0.05, 2, 0, 71009, 22009, 1, 3)
    ops.uniaxialMaterial('LimitState', 31009, 33.13900916, 8.783e-05, 99.41702747, 0.0002635, 331.39009157, 0.00087835, -33.13900916, -8.783e-05, -99.41702747, -0.0002635, -331.39009157, -0.00087835, 0.4, 0.3, 0.003, 0.0, 0.0, 11009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1009, 99999, 'P', 41009, 'Vy', 31009, 'Vz', 21009, 'My', 11009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171009, 71009, 171009, 1009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122009, 122009, 22009, 1009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171010, 3.05, 7.9, 3.5)
    ops.node(122010, 3.05, 7.9, 5.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1010, 171010, 122010, 0.25, 27117638.0203096, 11299015.84179567, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21010, 240.64550724, 0.00077478, 292.77101194, 0.03036164, 29.27710119, 0.07589657, -240.64550724, -0.00077478, -292.77101194, -0.03036164, -29.27710119, -0.07589657, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11010, 224.44063428, 0.00077478, 273.05604983, 0.03036164, 27.30560498, 0.07589657, -224.44063428, -0.00077478, -273.05604983, -0.03036164, -27.30560498, -0.07589657, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21010, 1010, 0.0, 287.80144755, 0.01549558, 287.80144755, 0.04648675, 201.46101328, -4831.76198683, 0.05, 2, 0, 71010, 22010, 2, 3)
    ops.uniaxialMaterial('LimitState', 41010, 71.95036189, 9.628e-05, 215.85108566, 0.00028885, 719.50361887, 0.00096282, -71.95036189, -9.628e-05, -215.85108566, -0.00028885, -719.50361887, -0.00096282, 0.4, 0.3, 0.003, 0.0, 0.0, 21010, 2)
    ops.limitCurve('ThreePoint', 11010, 1010, 0.0, 287.80144755, 0.01549558, 287.80144755, 0.04648675, 201.46101328, -4831.76198683, 0.05, 2, 0, 71010, 22010, 1, 3)
    ops.uniaxialMaterial('LimitState', 31010, 71.95036189, 9.628e-05, 215.85108566, 0.00028885, 719.50361887, 0.00096282, -71.95036189, -9.628e-05, -215.85108566, -0.00028885, -719.50361887, -0.00096282, 0.4, 0.3, 0.003, 0.0, 0.0, 11010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1010, 99999, 'P', 41010, 'Vy', 31010, 'Vz', 21010, 'My', 11010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171010, 71010, 171010, 1010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122010, 122010, 22010, 1010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171011, 9.0, 7.9, 3.5)
    ops.node(122011, 9.0, 7.9, 5.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1011, 171011, 122011, 0.3025, 26721209.98199302, 11133837.49249709, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21011, 336.54742995, 0.00073831, 409.22728928, 0.02012829, 40.92272893, 0.04861915, -336.54742995, -0.00073831, -409.22728928, -0.02012829, -40.92272893, -0.04861915, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11011, 300.07829263, 0.00073831, 364.88237716, 0.02012829, 36.48823772, 0.04861915, -300.07829263, -0.00073831, -364.88237716, -0.02012829, -36.48823772, -0.04861915, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21011, 1011, 0.0, 289.46511146, 0.0147662, 289.46511146, 0.0442986, 202.62557802, -2830.57307901, 0.05, 2, 0, 71011, 22011, 2, 3)
    ops.uniaxialMaterial('LimitState', 41011, 72.36627786, 8.122e-05, 217.09883359, 0.00024366, 723.66277865, 0.00081219, -72.36627786, -8.122e-05, -217.09883359, -0.00024366, -723.66277865, -0.00081219, 0.4, 0.3, 0.003, 0.0, 0.0, 21011, 2)
    ops.limitCurve('ThreePoint', 11011, 1011, 0.0, 289.46511146, 0.0147662, 289.46511146, 0.0442986, 202.62557802, -2830.57307901, 0.05, 2, 0, 71011, 22011, 1, 3)
    ops.uniaxialMaterial('LimitState', 31011, 72.36627786, 8.122e-05, 217.09883359, 0.00024366, 723.66277865, 0.00081219, -72.36627786, -8.122e-05, -217.09883359, -0.00024366, -723.66277865, -0.00081219, 0.4, 0.3, 0.003, 0.0, 0.0, 11011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1011, 99999, 'P', 41011, 'Vy', 31011, 'Vz', 21011, 'My', 11011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171011, 71011, 171011, 1011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122011, 122011, 22011, 1011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171012, 14.95, 7.9, 3.5)
    ops.node(122012, 14.95, 7.9, 5.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1012, 171012, 122012, 0.2025, 27102092.29440457, 11292538.4560019, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21012, 186.34358296, 0.00080996, 226.58042098, 0.02294498, 22.6580421, 0.06197654, -186.34358296, -0.00080996, -226.58042098, -0.02294498, -22.6580421, -0.06197654, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11012, 163.10120931, 0.00080996, 198.31936297, 0.02294498, 19.8319363, 0.06197654, -163.10120931, -0.00080996, -198.31936297, -0.02294498, -19.8319363, -0.06197654, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21012, 1012, 0.0, 213.22853306, 0.01619921, 213.22853306, 0.04859764, 149.25997314, -3014.59060386, 0.05, 2, 0, 71012, 22012, 2, 3)
    ops.uniaxialMaterial('LimitState', 41012, 53.30713326, 8.812e-05, 159.92139979, 0.00026435, 533.07133264, 0.00088117, -53.30713326, -8.812e-05, -159.92139979, -0.00026435, -533.07133264, -0.00088117, 0.4, 0.3, 0.003, 0.0, 0.0, 21012, 2)
    ops.limitCurve('ThreePoint', 11012, 1012, 0.0, 213.22853306, 0.01619921, 213.22853306, 0.04859764, 149.25997314, -3014.59060386, 0.05, 2, 0, 71012, 22012, 1, 3)
    ops.uniaxialMaterial('LimitState', 31012, 53.30713326, 8.812e-05, 159.92139979, 0.00026435, 533.07133264, 0.00088117, -53.30713326, -8.812e-05, -159.92139979, -0.00026435, -533.07133264, -0.00088117, 0.4, 0.3, 0.003, 0.0, 0.0, 11012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1012, 99999, 'P', 41012, 'Vy', 31012, 'Vz', 21012, 'My', 11012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171012, 71012, 171012, 1012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122012, 122012, 22012, 1012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171013, 0.0, 11.85, 3.5)
    ops.node(122013, 0.0, 11.85, 5.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1013, 171013, 122013, 0.1225, 27417240.48656357, 11423850.20273482, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21013, 83.57351053, 0.00094267, 101.68691263, 0.01679335, 10.16869126, 0.05834536, -83.57351053, -0.00094267, -101.68691263, -0.01679335, -10.16869126, -0.05834536, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11013, 72.65889753, 0.00094267, 88.40670827, 0.01679335, 8.84067083, 0.05834536, -72.65889753, -0.00094267, -88.40670827, -0.01679335, -8.84067083, -0.05834536, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21013, 1013, 0.0, 131.56379168, 0.01885335, 131.56379168, 0.05656005, 92.09465418, -2037.06866684, 0.05, 2, 0, 71013, 22013, 2, 3)
    ops.uniaxialMaterial('LimitState', 41013, 32.89094792, 8.884e-05, 98.67284376, 0.00026653, 328.9094792, 0.00088842, -32.89094792, -8.884e-05, -98.67284376, -0.00026653, -328.9094792, -0.00088842, 0.4, 0.3, 0.003, 0.0, 0.0, 21013, 2)
    ops.limitCurve('ThreePoint', 11013, 1013, 0.0, 131.56379168, 0.01885335, 131.56379168, 0.05656005, 92.09465418, -2037.06866684, 0.05, 2, 0, 71013, 22013, 1, 3)
    ops.uniaxialMaterial('LimitState', 31013, 32.89094792, 8.884e-05, 98.67284376, 0.00026653, 328.9094792, 0.00088842, -32.89094792, -8.884e-05, -98.67284376, -0.00026653, -328.9094792, -0.00088842, 0.4, 0.3, 0.003, 0.0, 0.0, 11013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1013, 99999, 'P', 41013, 'Vy', 31013, 'Vz', 21013, 'My', 11013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171013, 71013, 171013, 1013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122013, 122013, 22013, 1013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171014, 3.05, 11.85, 3.5)
    ops.node(122014, 3.05, 11.85, 5.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1014, 171014, 122014, 0.25, 27669223.57413147, 11528843.15588811, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21014, 239.9698207, 0.00078881, 291.71949665, 0.0301361, 29.17194966, 0.07639399, -239.9698207, -0.00078881, -291.71949665, -0.0301361, -29.17194966, -0.07639399, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11014, 224.37756895, 0.00078881, 272.76476384, 0.0301361, 27.27647638, 0.07639399, -224.37756895, -0.00078881, -272.76476384, -0.0301361, -27.27647638, -0.07639399, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21014, 1014, 0.0, 290.55736993, 0.01577626, 290.55736993, 0.04732878, 203.39015895, -4774.9651596, 0.05, 2, 0, 71014, 22014, 2, 3)
    ops.uniaxialMaterial('LimitState', 41014, 72.63934248, 9.527e-05, 217.91802744, 0.0002858, 726.39342481, 0.00095266, -72.63934248, -9.527e-05, -217.91802744, -0.0002858, -726.39342481, -0.00095266, 0.4, 0.3, 0.003, 0.0, 0.0, 21014, 2)
    ops.limitCurve('ThreePoint', 11014, 1014, 0.0, 290.55736993, 0.01577626, 290.55736993, 0.04732878, 203.39015895, -4774.9651596, 0.05, 2, 0, 71014, 22014, 1, 3)
    ops.uniaxialMaterial('LimitState', 31014, 72.63934248, 9.527e-05, 217.91802744, 0.0002858, 726.39342481, 0.00095266, -72.63934248, -9.527e-05, -217.91802744, -0.0002858, -726.39342481, -0.00095266, 0.4, 0.3, 0.003, 0.0, 0.0, 11014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1014, 99999, 'P', 41014, 'Vy', 31014, 'Vz', 21014, 'My', 11014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171014, 71014, 171014, 1014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122014, 122014, 22014, 1014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171015, 9.0, 11.85, 3.5)
    ops.node(122015, 9.0, 11.85, 5.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1015, 171015, 122015, 0.3025, 27049902.24789109, 11270792.60328796, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21015, 336.51577461, 0.00072943, 409.0385134, 0.02032622, 40.90385134, 0.0491439, -336.51577461, -0.00072943, -409.0385134, -0.02032622, -40.90385134, -0.0491439, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11015, 299.83813206, 0.00072943, 364.45644766, 0.02032622, 36.44564477, 0.0491439, -299.83813206, -0.00072943, -364.45644766, -0.02032622, -36.44564477, -0.0491439, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21015, 1015, 0.0, 293.5451839, 0.0145887, 293.5451839, 0.0437661, 205.48162873, -2858.62100692, 0.05, 2, 0, 71015, 22015, 2, 3)
    ops.uniaxialMaterial('LimitState', 41015, 73.38629598, 8.136e-05, 220.15888793, 0.00024409, 733.86295976, 0.00081363, -73.38629598, -8.136e-05, -220.15888793, -0.00024409, -733.86295976, -0.00081363, 0.4, 0.3, 0.003, 0.0, 0.0, 21015, 2)
    ops.limitCurve('ThreePoint', 11015, 1015, 0.0, 293.5451839, 0.0145887, 293.5451839, 0.0437661, 205.48162873, -2858.62100692, 0.05, 2, 0, 71015, 22015, 1, 3)
    ops.uniaxialMaterial('LimitState', 31015, 73.38629598, 8.136e-05, 220.15888793, 0.00024409, 733.86295976, 0.00081363, -73.38629598, -8.136e-05, -220.15888793, -0.00024409, -733.86295976, -0.00081363, 0.4, 0.3, 0.003, 0.0, 0.0, 11015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1015, 99999, 'P', 41015, 'Vy', 31015, 'Vz', 21015, 'My', 11015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171015, 71015, 171015, 1015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122015, 122015, 22015, 1015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171016, 14.95, 11.85, 3.5)
    ops.node(122016, 14.95, 11.85, 5.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1016, 171016, 122016, 0.2025, 28037197.21121729, 11682165.50467387, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21016, 190.26664028, 0.00080401, 231.04334042, 0.02285963, 23.10433404, 0.06299294, -190.26664028, -0.00080401, -231.04334042, -0.02285963, -23.10433404, -0.06299294, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11016, 166.04152074, 0.00080401, 201.62645193, 0.02285963, 20.16264519, 0.06299294, -166.04152074, -0.00080401, -201.62645193, -0.02285963, -20.16264519, -0.06299294, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21016, 1016, 0.0, 216.32288326, 0.01608011, 216.32288326, 0.04824032, 151.42601828, -2923.93644658, 0.05, 2, 0, 71016, 22016, 2, 3)
    ops.uniaxialMaterial('LimitState', 41016, 54.08072081, 8.641e-05, 162.24216244, 0.00025924, 540.80720814, 0.00086414, -54.08072081, -8.641e-05, -162.24216244, -0.00025924, -540.80720814, -0.00086414, 0.4, 0.3, 0.003, 0.0, 0.0, 21016, 2)
    ops.limitCurve('ThreePoint', 11016, 1016, 0.0, 216.32288326, 0.01608011, 216.32288326, 0.04824032, 151.42601828, -2923.93644658, 0.05, 2, 0, 71016, 22016, 1, 3)
    ops.uniaxialMaterial('LimitState', 31016, 54.08072081, 8.641e-05, 162.24216244, 0.00025924, 540.80720814, 0.00086414, -54.08072081, -8.641e-05, -162.24216244, -0.00025924, -540.80720814, -0.00086414, 0.4, 0.3, 0.003, 0.0, 0.0, 11016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1016, 99999, 'P', 41016, 'Vy', 31016, 'Vz', 21016, 'My', 11016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171016, 71016, 171016, 1016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122016, 122016, 22016, 1016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171017, 0.0, 15.8, 3.45)
    ops.node(122017, 0.0, 15.8, 6.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1017, 171017, 122017, 0.09, 27701102.23286538, 11542125.93036058, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21017, 50.824261, 0.00103202, 61.9002611, 0.01733015, 6.19002611, 0.06635501, -50.824261, -0.00103202, -61.9002611, -0.01733015, -6.19002611, -0.06635501, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11017, 46.16779309, 0.00103202, 56.22902114, 0.01733015, 5.62290211, 0.06635501, -46.16779309, -0.00103202, -56.22902114, -0.01733015, -5.62290211, -0.06635501, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21017, 1017, 0.0, 100.908206, 0.02064039, 100.908206, 0.06192118, 70.6357442, -1920.16160402, 0.05, 2, 0, 71017, 22017, 2, 3)
    ops.uniaxialMaterial('LimitState', 41017, 25.2270515, 9.18e-05, 75.6811545, 0.00027539, 252.270515, 0.00091797, -25.2270515, -9.18e-05, -75.6811545, -0.00027539, -252.270515, -0.00091797, 0.4, 0.3, 0.003, 0.0, 0.0, 21017, 2)
    ops.limitCurve('ThreePoint', 11017, 1017, 0.0, 100.908206, 0.02064039, 100.908206, 0.06192118, 70.6357442, -1920.16160402, 0.05, 2, 0, 71017, 22017, 1, 3)
    ops.uniaxialMaterial('LimitState', 31017, 25.2270515, 9.18e-05, 75.6811545, 0.00027539, 252.270515, 0.00091797, -25.2270515, -9.18e-05, -75.6811545, -0.00027539, -252.270515, -0.00091797, 0.4, 0.3, 0.003, 0.0, 0.0, 11017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1017, 99999, 'P', 41017, 'Vy', 31017, 'Vz', 21017, 'My', 11017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171017, 71017, 171017, 1017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122017, 122017, 22017, 1017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171018, 3.05, 15.8, 3.45)
    ops.node(122018, 3.05, 15.8, 6.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1018, 171018, 122018, 0.16, 27747327.30093216, 11561386.3753884, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21018, 125.28024128, 0.00085157, 152.19322937, 0.0157827, 15.21932294, 0.05265666, -125.28024128, -0.00085157, -152.19322937, -0.0157827, -15.21932294, -0.05265666, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11018, 106.29760472, 0.00085157, 129.13269938, 0.0157827, 12.91326994, 0.05265666, -106.29760472, -0.00085157, -129.13269938, -0.0157827, -12.91326994, -0.05265666, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21018, 1018, 0.0, 165.70725449, 0.01703135, 165.70725449, 0.05109404, 115.99507814, -2160.37366138, 0.05, 2, 0, 71018, 22018, 2, 3)
    ops.uniaxialMaterial('LimitState', 41018, 41.42681362, 8.465e-05, 124.28044087, 0.00025396, 414.26813623, 0.00084653, -41.42681362, -8.465e-05, -124.28044087, -0.00025396, -414.26813623, -0.00084653, 0.4, 0.3, 0.003, 0.0, 0.0, 21018, 2)
    ops.limitCurve('ThreePoint', 11018, 1018, 0.0, 165.70725449, 0.01703135, 165.70725449, 0.05109404, 115.99507814, -2160.37366138, 0.05, 2, 0, 71018, 22018, 1, 3)
    ops.uniaxialMaterial('LimitState', 31018, 41.42681362, 8.465e-05, 124.28044087, 0.00025396, 414.26813623, 0.00084653, -41.42681362, -8.465e-05, -124.28044087, -0.00025396, -414.26813623, -0.00084653, 0.4, 0.3, 0.003, 0.0, 0.0, 11018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1018, 99999, 'P', 41018, 'Vy', 31018, 'Vz', 21018, 'My', 11018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171018, 71018, 171018, 1018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122018, 122018, 22018, 1018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171019, 9.0, 15.8, 3.45)
    ops.node(122019, 9.0, 15.8, 6.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1019, 171019, 122019, 0.25, 27498264.73159692, 11457610.30483205, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21019, 235.06348255, 0.00077418, 285.98511298, 0.01775316, 28.5985113, 0.04670573, -235.06348255, -0.00077418, -285.98511298, -0.01775316, -28.5985113, -0.04670573, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11019, 219.23685053, 0.00077418, 266.72996923, 0.01775316, 26.67299692, 0.04670573, -219.23685053, -0.00077418, -266.72996923, -0.01775316, -26.67299692, -0.04670573, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21019, 1019, 0.0, 215.30927523, 0.01548367, 215.30927523, 0.04645101, 150.71649266, -2058.19275821, 0.05, 2, 0, 71019, 22019, 2, 3)
    ops.uniaxialMaterial('LimitState', 41019, 53.82731881, 7.103e-05, 161.48195643, 0.0002131, 538.27318808, 0.00071033, -53.82731881, -7.103e-05, -161.48195643, -0.0002131, -538.27318808, -0.00071033, 0.4, 0.3, 0.003, 0.0, 0.0, 21019, 2)
    ops.limitCurve('ThreePoint', 11019, 1019, 0.0, 215.30927523, 0.01548367, 215.30927523, 0.04645101, 150.71649266, -2058.19275821, 0.05, 2, 0, 71019, 22019, 1, 3)
    ops.uniaxialMaterial('LimitState', 31019, 53.82731881, 7.103e-05, 161.48195643, 0.0002131, 538.27318808, 0.00071033, -53.82731881, -7.103e-05, -161.48195643, -0.0002131, -538.27318808, -0.00071033, 0.4, 0.3, 0.003, 0.0, 0.0, 11019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1019, 99999, 'P', 41019, 'Vy', 31019, 'Vz', 21019, 'My', 11019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171019, 71019, 171019, 1019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122019, 122019, 22019, 1019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171020, 14.95, 15.8, 3.45)
    ops.node(122020, 14.95, 15.8, 6.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1020, 171020, 122020, 0.1225, 28426418.45423739, 11844341.02259891, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21020, 100.33799154, 0.00094009, 121.80265464, 0.01653059, 12.18026546, 0.05833249, -100.33799154, -0.00094009, -121.80265464, -0.01653059, -12.18026546, -0.05833249, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11020, 83.38646066, 0.00094009, 101.22479147, 0.01653059, 10.12247915, 0.05833249, -83.38646066, -0.00094009, -101.22479147, -0.01653059, -10.12247915, -0.05833249, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21020, 1020, 0.0, 133.49571929, 0.01880185, 133.49571929, 0.05640554, 93.4470035, -1862.443803, 0.05, 2, 0, 71020, 22020, 2, 3)
    ops.uniaxialMaterial('LimitState', 41020, 33.37392982, 8.695e-05, 100.12178946, 0.00026084, 333.73929822, 0.00086947, -33.37392982, -8.695e-05, -100.12178946, -0.00026084, -333.73929822, -0.00086947, 0.4, 0.3, 0.003, 0.0, 0.0, 21020, 2)
    ops.limitCurve('ThreePoint', 11020, 1020, 0.0, 133.49571929, 0.01880185, 133.49571929, 0.05640554, 93.4470035, -1862.443803, 0.05, 2, 0, 71020, 22020, 1, 3)
    ops.uniaxialMaterial('LimitState', 31020, 33.37392982, 8.695e-05, 100.12178946, 0.00026084, 333.73929822, 0.00086947, -33.37392982, -8.695e-05, -100.12178946, -0.00026084, -333.73929822, -0.00086947, 0.4, 0.3, 0.003, 0.0, 0.0, 11020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1020, 99999, 'P', 41020, 'Vy', 31020, 'Vz', 21020, 'My', 11020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171020, 71020, 171020, 1020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122020, 122020, 22020, 1020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172003, 9.0, 0.0, 6.6)
    ops.node(123003, 9.0, 0.0, 9.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2003, 172003, 123003, 0.16, 27904915.06573193, 11627047.94405497, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22003, 129.40417714, 0.00088342, 157.37861361, 0.01410063, 15.73786136, 0.04246705, -129.40417714, -0.00088342, -157.37861361, -0.01410063, -15.73786136, -0.04246705, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12003, 129.40417714, 0.00088342, 157.37861361, 0.01410063, 15.73786136, 0.04246705, -129.40417714, -0.00088342, -157.37861361, -0.01410063, -15.73786136, -0.04246705, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22003, 2003, 0.0, 134.39384631, 0.01766835, 134.39384631, 0.05300504, 94.07569242, -1223.02481543, 0.05, 2, 0, 72003, 23003, 2, 3)
    ops.uniaxialMaterial('LimitState', 42003, 33.59846158, 6.827e-05, 100.79538473, 0.00020481, 335.98461578, 0.00068269, -33.59846158, -6.827e-05, -100.79538473, -0.00020481, -335.98461578, -0.00068269, 0.4, 0.3, 0.003, 0.0, 0.0, 22003, 2)
    ops.limitCurve('ThreePoint', 12003, 2003, 0.0, 134.39384631, 0.01766835, 134.39384631, 0.05300504, 94.07569242, -1223.02481543, 0.05, 2, 0, 72003, 23003, 1, 3)
    ops.uniaxialMaterial('LimitState', 32003, 33.59846158, 6.827e-05, 100.79538473, 0.00020481, 335.98461578, 0.00068269, -33.59846158, -6.827e-05, -100.79538473, -0.00020481, -335.98461578, -0.00068269, 0.4, 0.3, 0.003, 0.0, 0.0, 12003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2003, 99999, 'P', 42003, 'Vy', 32003, 'Vz', 22003, 'My', 12003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172003, 72003, 172003, 2003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123003, 123003, 23003, 2003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172004, 14.95, 0.0, 6.6)
    ops.node(123004, 14.95, 0.0, 9.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2004, 172004, 123004, 0.0625, 26928738.82379294, 11220307.84324706, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22004, 41.15568358, 0.00129414, 49.99179191, 0.0184995, 4.99917919, 0.0679731, -41.15568358, -0.00129414, -49.99179191, -0.0184995, -4.99917919, -0.0679731, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12004, 37.53018994, 0.00129414, 45.58790627, 0.0184995, 4.55879063, 0.0679731, -37.53018994, -0.00129414, -45.58790627, -0.0184995, -4.55879063, -0.0679731, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22004, 2004, 0.0, 79.42637103, 0.0258828, 79.42637103, 0.07764841, 55.59845972, -1432.11516181, 0.05, 2, 0, 72004, 23004, 2, 3)
    ops.uniaxialMaterial('LimitState', 42004, 19.85659276, 0.00010703, 59.56977827, 0.00032109, 198.56592757, 0.00107032, -19.85659276, -0.00010703, -59.56977827, -0.00032109, -198.56592757, -0.00107032, 0.4, 0.3, 0.003, 0.0, 0.0, 22004, 2)
    ops.limitCurve('ThreePoint', 12004, 2004, 0.0, 79.42637103, 0.0258828, 79.42637103, 0.07764841, 55.59845972, -1432.11516181, 0.05, 2, 0, 72004, 23004, 1, 3)
    ops.uniaxialMaterial('LimitState', 32004, 19.85659276, 0.00010703, 59.56977827, 0.00032109, 198.56592757, 0.00107032, -19.85659276, -0.00010703, -59.56977827, -0.00032109, -198.56592757, -0.00107032, 0.4, 0.3, 0.003, 0.0, 0.0, 12004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2004, 99999, 'P', 42004, 'Vy', 32004, 'Vz', 22004, 'My', 12004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172004, 72004, 172004, 2004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123004, 123004, 23004, 2004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172005, 0.0, 3.95, 6.65)
    ops.node(123005, 0.0, 3.95, 9.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2005, 172005, 123005, 0.0625, 28178032.43047657, 11740846.84603191, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22005, 31.23677692, 0.00124113, 37.88597548, 0.01825134, 3.78859755, 0.06999841, -31.23677692, -0.00124113, -37.88597548, -0.01825134, -3.78859755, -0.06999841, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12005, 31.23677692, 0.00124113, 37.88597548, 0.01825134, 3.78859755, 0.06999841, -31.23677692, -0.00124113, -37.88597548, -0.01825134, -3.78859755, -0.06999841, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22005, 2005, 0.0, 82.04032162, 0.02482255, 82.04032162, 0.07446765, 57.42822514, -1456.86025579, 0.05, 2, 0, 72005, 23005, 2, 3)
    ops.uniaxialMaterial('LimitState', 42005, 20.51008041, 0.00010565, 61.53024122, 0.00031696, 205.10080406, 0.00105652, -20.51008041, -0.00010565, -61.53024122, -0.00031696, -205.10080406, -0.00105652, 0.4, 0.3, 0.003, 0.0, 0.0, 22005, 2)
    ops.limitCurve('ThreePoint', 12005, 2005, 0.0, 82.04032162, 0.02482255, 82.04032162, 0.07446765, 57.42822514, -1456.86025579, 0.05, 2, 0, 72005, 23005, 1, 3)
    ops.uniaxialMaterial('LimitState', 32005, 20.51008041, 0.00010565, 61.53024122, 0.00031696, 205.10080406, 0.00105652, -20.51008041, -0.00010565, -61.53024122, -0.00031696, -205.10080406, -0.00105652, 0.4, 0.3, 0.003, 0.0, 0.0, 12005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2005, 99999, 'P', 42005, 'Vy', 32005, 'Vz', 22005, 'My', 12005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172005, 72005, 172005, 2005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123005, 123005, 23005, 2005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172006, 3.05, 3.95, 6.65)
    ops.node(123006, 3.05, 3.95, 9.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2006, 172006, 123006, 0.16, 29280730.9550745, 12200304.56461438, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22006, 135.44193412, 0.00087573, 164.1327853, 0.0184916, 16.41327853, 0.05256197, -135.44193412, -0.00087573, -164.1327853, -0.0184916, -16.41327853, -0.05256197, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12006, 135.44193412, 0.00087573, 164.1327853, 0.0184916, 16.41327853, 0.05256197, -135.44193412, -0.00087573, -164.1327853, -0.0184916, -16.41327853, -0.05256197, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22006, 2006, 0.0, 157.25171246, 0.01751459, 157.25171246, 0.05254376, 110.07619872, -1644.83961443, 0.05, 2, 0, 72006, 23006, 2, 3)
    ops.uniaxialMaterial('LimitState', 42006, 39.31292812, 7.613e-05, 117.93878435, 0.00022838, 393.12928116, 0.00076127, -39.31292812, -7.613e-05, -117.93878435, -0.00022838, -393.12928116, -0.00076127, 0.4, 0.3, 0.003, 0.0, 0.0, 22006, 2)
    ops.limitCurve('ThreePoint', 12006, 2006, 0.0, 157.25171246, 0.01751459, 157.25171246, 0.05254376, 110.07619872, -1644.83961443, 0.05, 2, 0, 72006, 23006, 1, 3)
    ops.uniaxialMaterial('LimitState', 32006, 39.31292812, 7.613e-05, 117.93878435, 0.00022838, 393.12928116, 0.00076127, -39.31292812, -7.613e-05, -117.93878435, -0.00022838, -393.12928116, -0.00076127, 0.4, 0.3, 0.003, 0.0, 0.0, 12006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2006, 99999, 'P', 42006, 'Vy', 32006, 'Vz', 22006, 'My', 12006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172006, 72006, 172006, 2006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123006, 123006, 23006, 2006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172007, 9.0, 3.95, 6.65)
    ops.node(123007, 9.0, 3.95, 9.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2007, 172007, 123007, 0.25, 27736419.81023252, 11556841.58759688, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22007, 226.56957108, 0.00075352, 275.69516351, 0.02106653, 27.56951635, 0.05429768, -226.56957108, -0.00075352, -275.69516351, -0.02106653, -27.56951635, -0.05429768, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12007, 211.10541405, 0.00075352, 256.87801485, 0.02106653, 25.68780148, 0.05429768, -211.10541405, -0.00075352, -256.87801485, -0.02106653, -25.68780148, -0.05429768, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22007, 2007, 0.0, 230.54431057, 0.01507033, 230.54431057, 0.04521098, 161.3810174, -2603.87521282, 0.05, 2, 0, 72007, 23007, 2, 3)
    ops.uniaxialMaterial('LimitState', 42007, 57.63607764, 7.541e-05, 172.90823293, 0.00022622, 576.36077644, 0.00075406, -57.63607764, -7.541e-05, -172.90823293, -0.00022622, -576.36077644, -0.00075406, 0.4, 0.3, 0.003, 0.0, 0.0, 22007, 2)
    ops.limitCurve('ThreePoint', 12007, 2007, 0.0, 230.54431057, 0.01507033, 230.54431057, 0.04521098, 161.3810174, -2603.87521282, 0.05, 2, 0, 72007, 23007, 1, 3)
    ops.uniaxialMaterial('LimitState', 32007, 57.63607764, 7.541e-05, 172.90823293, 0.00022622, 576.36077644, 0.00075406, -57.63607764, -7.541e-05, -172.90823293, -0.00022622, -576.36077644, -0.00075406, 0.4, 0.3, 0.003, 0.0, 0.0, 12007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2007, 99999, 'P', 42007, 'Vy', 32007, 'Vz', 22007, 'My', 12007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172007, 72007, 172007, 2007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123007, 123007, 23007, 2007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172008, 14.95, 3.95, 6.65)
    ops.node(123008, 14.95, 3.95, 9.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2008, 172008, 123008, 0.1225, 28773795.87523847, 11989081.6146827, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22008, 94.22047281, 0.00096542, 114.25208137, 0.01687208, 11.42520814, 0.05336822, -94.22047281, -0.00096542, -114.25208137, -0.01687208, -11.42520814, -0.05336822, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12008, 88.82964387, 0.00096542, 107.71514297, 0.01687208, 10.7715143, 0.05336822, -88.82964387, -0.00096542, -107.71514297, -0.01687208, -10.7715143, -0.05336822, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22008, 2008, 0.0, 127.54382978, 0.01930832, 127.54382978, 0.05792496, 89.28068085, -1532.12525349, 0.05, 2, 0, 72008, 23008, 2, 3)
    ops.uniaxialMaterial('LimitState', 42008, 31.88595744, 8.207e-05, 95.65787233, 0.0002462, 318.85957445, 0.00082067, -31.88595744, -8.207e-05, -95.65787233, -0.0002462, -318.85957445, -0.00082067, 0.4, 0.3, 0.003, 0.0, 0.0, 22008, 2)
    ops.limitCurve('ThreePoint', 12008, 2008, 0.0, 127.54382978, 0.01930832, 127.54382978, 0.05792496, 89.28068085, -1532.12525349, 0.05, 2, 0, 72008, 23008, 1, 3)
    ops.uniaxialMaterial('LimitState', 32008, 31.88595744, 8.207e-05, 95.65787233, 0.0002462, 318.85957445, 0.00082067, -31.88595744, -8.207e-05, -95.65787233, -0.0002462, -318.85957445, -0.00082067, 0.4, 0.3, 0.003, 0.0, 0.0, 12008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2008, 99999, 'P', 42008, 'Vy', 32008, 'Vz', 22008, 'My', 12008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172008, 72008, 172008, 2008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123008, 123008, 23008, 2008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172009, 0.0, 7.9, 6.65)
    ops.node(123009, 0.0, 7.9, 9.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2009, 172009, 123009, 0.0625, 27398926.139446, 11416219.22476917, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22009, 30.06933023, 0.00127479, 36.53691278, 0.01818387, 3.65369128, 0.06979574, -30.06933023, -0.00127479, -36.53691278, -0.01818387, -3.65369128, -0.06979574, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12009, 30.06933023, 0.00127479, 36.53691278, 0.01818387, 3.65369128, 0.06979574, -30.06933023, -0.00127479, -36.53691278, -0.01818387, -3.65369128, -0.06979574, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22009, 2009, 0.0, 79.91490002, 0.02549581, 79.91490002, 0.07648742, 55.94043002, -1499.83059596, 0.05, 2, 0, 72009, 23009, 2, 3)
    ops.uniaxialMaterial('LimitState', 42009, 19.97872501, 0.00010584, 59.93617502, 0.00031753, 199.78725006, 0.00105842, -19.97872501, -0.00010584, -59.93617502, -0.00031753, -199.78725006, -0.00105842, 0.4, 0.3, 0.003, 0.0, 0.0, 22009, 2)
    ops.limitCurve('ThreePoint', 12009, 2009, 0.0, 79.91490002, 0.02549581, 79.91490002, 0.07648742, 55.94043002, -1499.83059596, 0.05, 2, 0, 72009, 23009, 1, 3)
    ops.uniaxialMaterial('LimitState', 32009, 19.97872501, 0.00010584, 59.93617502, 0.00031753, 199.78725006, 0.00105842, -19.97872501, -0.00010584, -59.93617502, -0.00031753, -199.78725006, -0.00105842, 0.4, 0.3, 0.003, 0.0, 0.0, 12009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2009, 99999, 'P', 42009, 'Vy', 32009, 'Vz', 22009, 'My', 12009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172009, 72009, 172009, 2009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123009, 123009, 23009, 2009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172010, 3.05, 7.9, 6.65)
    ops.node(123010, 3.05, 7.9, 9.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2010, 172010, 123010, 0.16, 27877473.28220074, 11615613.86758364, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22010, 134.46047869, 0.0008968, 163.42459106, 0.02241112, 16.34245911, 0.06018054, -134.46047869, -0.0008968, -163.42459106, -0.02241112, -16.34245911, -0.06018054, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12010, 134.46047869, 0.0008968, 163.42459106, 0.02241112, 16.34245911, 0.06018054, -134.46047869, -0.0008968, -163.42459106, -0.02241112, -16.34245911, -0.06018054, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22010, 2010, 0.0, 163.16881293, 0.01793598, 163.16881293, 0.05380793, 114.21816905, -2144.45718678, 0.05, 2, 0, 72010, 23010, 2, 3)
    ops.uniaxialMaterial('LimitState', 42010, 40.79220323, 8.297e-05, 122.3766097, 0.0002489, 407.92203232, 0.00082967, -40.79220323, -8.297e-05, -122.3766097, -0.0002489, -407.92203232, -0.00082967, 0.4, 0.3, 0.003, 0.0, 0.0, 22010, 2)
    ops.limitCurve('ThreePoint', 12010, 2010, 0.0, 163.16881293, 0.01793598, 163.16881293, 0.05380793, 114.21816905, -2144.45718678, 0.05, 2, 0, 72010, 23010, 1, 3)
    ops.uniaxialMaterial('LimitState', 32010, 40.79220323, 8.297e-05, 122.3766097, 0.0002489, 407.92203232, 0.00082967, -40.79220323, -8.297e-05, -122.3766097, -0.0002489, -407.92203232, -0.00082967, 0.4, 0.3, 0.003, 0.0, 0.0, 12010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2010, 99999, 'P', 42010, 'Vy', 32010, 'Vz', 22010, 'My', 12010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172010, 72010, 172010, 2010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123010, 123010, 23010, 2010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172011, 9.0, 7.9, 6.65)
    ops.node(123011, 9.0, 7.9, 9.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2011, 172011, 123011, 0.25, 27584856.71586768, 11493690.2982782, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22011, 227.91386312, 0.0007507, 277.40027669, 0.02098092, 27.74002767, 0.05409391, -227.91386312, -0.0007507, -277.40027669, -0.02098092, -27.74002767, -0.05409391, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12011, 212.11399971, 0.0007507, 258.16982522, 0.02098092, 25.81698252, 0.05409391, -212.11399971, -0.0007507, -258.16982522, -0.02098092, -25.81698252, -0.05409391, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22011, 2011, 0.0, 226.92484145, 0.01501396, 226.92484145, 0.04504188, 158.84738901, -2512.9484869, 0.05, 2, 0, 72011, 23011, 2, 3)
    ops.uniaxialMaterial('LimitState', 42011, 56.73121036, 7.463e-05, 170.19363109, 0.00022389, 567.31210362, 0.0007463, -56.73121036, -7.463e-05, -170.19363109, -0.00022389, -567.31210362, -0.0007463, 0.4, 0.3, 0.003, 0.0, 0.0, 22011, 2)
    ops.limitCurve('ThreePoint', 12011, 2011, 0.0, 226.92484145, 0.01501396, 226.92484145, 0.04504188, 158.84738901, -2512.9484869, 0.05, 2, 0, 72011, 23011, 1, 3)
    ops.uniaxialMaterial('LimitState', 32011, 56.73121036, 7.463e-05, 170.19363109, 0.00022389, 567.31210362, 0.0007463, -56.73121036, -7.463e-05, -170.19363109, -0.00022389, -567.31210362, -0.0007463, 0.4, 0.3, 0.003, 0.0, 0.0, 12011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2011, 99999, 'P', 42011, 'Vy', 32011, 'Vz', 22011, 'My', 12011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172011, 72011, 172011, 2011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123011, 123011, 23011, 2011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172012, 14.95, 7.9, 6.65)
    ops.node(123012, 14.95, 7.9, 9.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2012, 172012, 123012, 0.1225, 27604231.51047998, 11501763.12936666, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22012, 95.26495008, 0.00098638, 115.73809424, 0.01681424, 11.57380942, 0.05215127, -95.26495008, -0.00098638, -115.73809424, -0.01681424, -11.57380942, -0.05215127, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12012, 89.70733643, 0.00098638, 108.98610819, 0.01681424, 10.89861082, 0.05215127, -89.70733643, -0.00098638, -108.98610819, -0.01681424, -10.89861082, -0.05215127, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22012, 2012, 0.0, 124.26896484, 0.01972756, 124.26896484, 0.05918268, 86.98827539, -1564.0642062, 0.05, 2, 0, 72012, 23012, 2, 3)
    ops.uniaxialMaterial('LimitState', 42012, 31.06724121, 8.335e-05, 93.20172363, 0.00025004, 310.6724121, 0.00083348, -31.06724121, -8.335e-05, -93.20172363, -0.00025004, -310.6724121, -0.00083348, 0.4, 0.3, 0.003, 0.0, 0.0, 22012, 2)
    ops.limitCurve('ThreePoint', 12012, 2012, 0.0, 124.26896484, 0.01972756, 124.26896484, 0.05918268, 86.98827539, -1564.0642062, 0.05, 2, 0, 72012, 23012, 1, 3)
    ops.uniaxialMaterial('LimitState', 32012, 31.06724121, 8.335e-05, 93.20172363, 0.00025004, 310.6724121, 0.00083348, -31.06724121, -8.335e-05, -93.20172363, -0.00025004, -310.6724121, -0.00083348, 0.4, 0.3, 0.003, 0.0, 0.0, 12012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2012, 99999, 'P', 42012, 'Vy', 32012, 'Vz', 22012, 'My', 12012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172012, 72012, 172012, 2012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123012, 123012, 23012, 2012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172013, 0.0, 11.85, 6.65)
    ops.node(123013, 0.0, 11.85, 9.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2013, 172013, 123013, 0.0625, 28376587.9715132, 11823578.32146383, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22013, 30.26184137, 0.00122519, 36.71691135, 0.0181193, 3.67169113, 0.07123335, -30.26184137, -0.00122519, -36.71691135, -0.0181193, -3.67169113, -0.07123335, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12013, 30.26184137, 0.00122519, 36.71691135, 0.0181193, 3.67169113, 0.07123335, -30.26184137, -0.00122519, -36.71691135, -0.0181193, -3.67169113, -0.07123335, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22013, 2013, 0.0, 82.0731432, 0.02450378, 82.0731432, 0.07351134, 57.45120024, -1518.73572254, 0.05, 2, 0, 72013, 23013, 2, 3)
    ops.uniaxialMaterial('LimitState', 42013, 20.5182858, 0.00010496, 61.5548574, 0.00031487, 205.18285799, 0.00104955, -20.5182858, -0.00010496, -61.5548574, -0.00031487, -205.18285799, -0.00104955, 0.4, 0.3, 0.003, 0.0, 0.0, 22013, 2)
    ops.limitCurve('ThreePoint', 12013, 2013, 0.0, 82.0731432, 0.02450378, 82.0731432, 0.07351134, 57.45120024, -1518.73572254, 0.05, 2, 0, 72013, 23013, 1, 3)
    ops.uniaxialMaterial('LimitState', 32013, 20.5182858, 0.00010496, 61.5548574, 0.00031487, 205.18285799, 0.00104955, -20.5182858, -0.00010496, -61.5548574, -0.00031487, -205.18285799, -0.00104955, 0.4, 0.3, 0.003, 0.0, 0.0, 12013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2013, 99999, 'P', 42013, 'Vy', 32013, 'Vz', 22013, 'My', 12013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172013, 72013, 172013, 2013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123013, 123013, 23013, 2013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172014, 3.05, 11.85, 6.65)
    ops.node(123014, 3.05, 11.85, 9.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2014, 172014, 123014, 0.16, 27810862.23994924, 11587859.26664552, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22014, 133.47611213, 0.00088514, 162.24546099, 0.02208875, 16.2245461, 0.05979245, -133.47611213, -0.00088514, -162.24546099, -0.02208875, -16.2245461, -0.05979245, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12014, 133.47611213, 0.00088514, 162.24546099, 0.02208875, 16.2245461, 0.05979245, -133.47611213, -0.00088514, -162.24546099, -0.02208875, -16.2245461, -0.05979245, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22014, 2014, 0.0, 160.5142915, 0.01770285, 160.5142915, 0.05310855, 112.36000405, -2054.86075267, 0.05, 2, 0, 72014, 23014, 2, 3)
    ops.uniaxialMaterial('LimitState', 42014, 40.12857288, 8.181e-05, 120.38571863, 0.00024544, 401.28572876, 0.00081813, -40.12857288, -8.181e-05, -120.38571863, -0.00024544, -401.28572876, -0.00081813, 0.4, 0.3, 0.003, 0.0, 0.0, 22014, 2)
    ops.limitCurve('ThreePoint', 12014, 2014, 0.0, 160.5142915, 0.01770285, 160.5142915, 0.05310855, 112.36000405, -2054.86075267, 0.05, 2, 0, 72014, 23014, 1, 3)
    ops.uniaxialMaterial('LimitState', 32014, 40.12857288, 8.181e-05, 120.38571863, 0.00024544, 401.28572876, 0.00081813, -40.12857288, -8.181e-05, -120.38571863, -0.00024544, -401.28572876, -0.00081813, 0.4, 0.3, 0.003, 0.0, 0.0, 12014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2014, 99999, 'P', 42014, 'Vy', 32014, 'Vz', 22014, 'My', 12014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172014, 72014, 172014, 2014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123014, 123014, 23014, 2014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172015, 9.0, 11.85, 6.65)
    ops.node(123015, 9.0, 11.85, 9.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2015, 172015, 123015, 0.25, 29172134.69635449, 12155056.12348104, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22015, 230.13321247, 0.00075545, 279.26620027, 0.02067158, 27.92662003, 0.05491212, -230.13321247, -0.00075545, -279.26620027, -0.02067158, -27.92662003, -0.05491212, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12015, 214.54258725, 0.00075545, 260.34700726, 0.02067158, 26.03470073, 0.05491212, -214.54258725, -0.00075545, -260.34700726, -0.02067158, -26.03470073, -0.05491212, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22015, 2015, 0.0, 239.83338902, 0.01510891, 239.83338902, 0.04532673, 167.88337231, -2557.10797096, 0.05, 2, 0, 72015, 23015, 2, 3)
    ops.uniaxialMaterial('LimitState', 42015, 59.95834726, 7.458e-05, 179.87504177, 0.00022375, 599.58347255, 0.00074584, -59.95834726, -7.458e-05, -179.87504177, -0.00022375, -599.58347255, -0.00074584, 0.4, 0.3, 0.003, 0.0, 0.0, 22015, 2)
    ops.limitCurve('ThreePoint', 12015, 2015, 0.0, 239.83338902, 0.01510891, 239.83338902, 0.04532673, 167.88337231, -2557.10797096, 0.05, 2, 0, 72015, 23015, 1, 3)
    ops.uniaxialMaterial('LimitState', 32015, 59.95834726, 7.458e-05, 179.87504177, 0.00022375, 599.58347255, 0.00074584, -59.95834726, -7.458e-05, -179.87504177, -0.00022375, -599.58347255, -0.00074584, 0.4, 0.3, 0.003, 0.0, 0.0, 12015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2015, 99999, 'P', 42015, 'Vy', 32015, 'Vz', 22015, 'My', 12015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172015, 72015, 172015, 2015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123015, 123015, 23015, 2015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172016, 14.95, 11.85, 6.65)
    ops.node(123016, 14.95, 11.85, 9.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2016, 172016, 123016, 0.1225, 27828952.93729831, 11595397.05720763, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22016, 97.19053203, 0.00097176, 118.03889419, 0.01626197, 11.80388942, 0.05183521, -97.19053203, -0.00097176, -118.03889419, -0.01626197, -11.80388942, -0.05183521, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12016, 91.27520311, 0.00097176, 110.85466678, 0.01626197, 11.08546668, 0.05183521, -91.27520311, -0.00097176, -110.85466678, -0.01626197, -11.08546668, -0.05183521, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22016, 2016, 0.0, 122.3881761, 0.01943519, 122.3881761, 0.05830556, 85.67172327, -1470.00898774, 0.05, 2, 0, 72016, 23016, 2, 3)
    ops.uniaxialMaterial('LimitState', 42016, 30.59704403, 8.142e-05, 91.79113208, 0.00024427, 305.97044025, 0.00081423, -30.59704403, -8.142e-05, -91.79113208, -0.00024427, -305.97044025, -0.00081423, 0.4, 0.3, 0.003, 0.0, 0.0, 22016, 2)
    ops.limitCurve('ThreePoint', 12016, 2016, 0.0, 122.3881761, 0.01943519, 122.3881761, 0.05830556, 85.67172327, -1470.00898774, 0.05, 2, 0, 72016, 23016, 1, 3)
    ops.uniaxialMaterial('LimitState', 32016, 30.59704403, 8.142e-05, 91.79113208, 0.00024427, 305.97044025, 0.00081423, -30.59704403, -8.142e-05, -91.79113208, -0.00024427, -305.97044025, -0.00081423, 0.4, 0.3, 0.003, 0.0, 0.0, 12016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2016, 99999, 'P', 42016, 'Vy', 32016, 'Vz', 22016, 'My', 12016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172016, 72016, 172016, 2016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123016, 123016, 23016, 2016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172017, 0.0, 15.8, 6.6)
    ops.node(123017, 0.0, 15.8, 9.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2017, 172017, 123017, 0.0625, 26602686.18153297, 11084452.57563874, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22017, 27.2613323, 0.00123147, 33.2895311, 0.01888939, 3.32895311, 0.07553371, -27.2613323, -0.00123147, -33.2895311, -0.01888939, -3.32895311, -0.07553371, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12017, 27.2613323, 0.00123147, 33.2895311, 0.01888939, 3.32895311, 0.07553371, -27.2613323, -0.00123147, -33.2895311, -0.01888939, -3.32895311, -0.07553371, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22017, 2017, 0.0, 73.95548514, 0.02462946, 73.95548514, 0.07388837, 51.76883959, -1869.51928929, 0.05, 2, 0, 72017, 23017, 2, 3)
    ops.uniaxialMaterial('LimitState', 42017, 18.48887128, 0.00010088, 55.46661385, 0.00030264, 184.88871284, 0.00100881, -18.48887128, -0.00010088, -55.46661385, -0.00030264, -184.88871284, -0.00100881, 0.4, 0.3, 0.003, 0.0, 0.0, 22017, 2)
    ops.limitCurve('ThreePoint', 12017, 2017, 0.0, 73.95548514, 0.02462946, 73.95548514, 0.07388837, 51.76883959, -1869.51928929, 0.05, 2, 0, 72017, 23017, 1, 3)
    ops.uniaxialMaterial('LimitState', 32017, 18.48887128, 0.00010088, 55.46661385, 0.00030264, 184.88871284, 0.00100881, -18.48887128, -0.00010088, -55.46661385, -0.00030264, -184.88871284, -0.00100881, 0.4, 0.3, 0.003, 0.0, 0.0, 12017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2017, 99999, 'P', 42017, 'Vy', 32017, 'Vz', 22017, 'My', 12017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172017, 72017, 172017, 2017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123017, 123017, 23017, 2017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172018, 3.05, 15.8, 6.6)
    ops.node(123018, 3.05, 15.8, 9.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2018, 172018, 123018, 0.1225, 27453647.18005611, 11439019.65835671, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22018, 84.13403692, 0.00090824, 102.42106569, 0.01668474, 10.24210657, 0.05898193, -84.13403692, -0.00090824, -102.42106569, -0.01668474, -10.24210657, -0.05898193, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12018, 72.08522173, 0.00090824, 87.75336951, 0.01668474, 8.77533695, 0.05898193, -72.08522173, -0.00090824, -87.75336951, -0.01668474, -8.77533695, -0.05898193, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22018, 2018, 0.0, 129.28432832, 0.01816477, 129.28432832, 0.05449432, 90.49902983, -2029.61031822, 0.05, 2, 0, 72018, 23018, 2, 3)
    ops.uniaxialMaterial('LimitState', 42018, 32.32108208, 8.719e-05, 96.96324624, 0.00026156, 323.2108208, 0.00087187, -32.32108208, -8.719e-05, -96.96324624, -0.00026156, -323.2108208, -0.00087187, 0.4, 0.3, 0.003, 0.0, 0.0, 22018, 2)
    ops.limitCurve('ThreePoint', 12018, 2018, 0.0, 129.28432832, 0.01816477, 129.28432832, 0.05449432, 90.49902983, -2029.61031822, 0.05, 2, 0, 72018, 23018, 1, 3)
    ops.uniaxialMaterial('LimitState', 32018, 32.32108208, 8.719e-05, 96.96324624, 0.00026156, 323.2108208, 0.00087187, -32.32108208, -8.719e-05, -96.96324624, -0.00026156, -323.2108208, -0.00087187, 0.4, 0.3, 0.003, 0.0, 0.0, 12018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2018, 99999, 'P', 42018, 'Vy', 32018, 'Vz', 22018, 'My', 12018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172018, 72018, 172018, 2018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123018, 123018, 23018, 2018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172019, 9.0, 15.8, 6.6)
    ops.node(123019, 9.0, 15.8, 9.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2019, 172019, 123019, 0.16, 28615495.08058058, 11923122.95024191, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22019, 131.2428178, 0.00088012, 159.40878584, 0.01449907, 15.94087858, 0.04331753, -131.2428178, -0.00088012, -159.40878584, -0.01449907, -15.94087858, -0.04331753, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12019, 131.2428178, 0.00088012, 159.40878584, 0.01449907, 15.94087858, 0.04331753, -131.2428178, -0.00088012, -159.40878584, -0.01449907, -15.94087858, -0.04331753, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22019, 2019, 0.0, 139.8099114, 0.01760249, 139.8099114, 0.05280747, 97.86693798, -1288.92988488, 0.05, 2, 0, 72019, 23019, 2, 3)
    ops.uniaxialMaterial('LimitState', 42019, 34.95247785, 6.926e-05, 104.85743355, 0.00020777, 349.5247785, 0.00069256, -34.95247785, -6.926e-05, -104.85743355, -0.00020777, -349.5247785, -0.00069256, 0.4, 0.3, 0.003, 0.0, 0.0, 22019, 2)
    ops.limitCurve('ThreePoint', 12019, 2019, 0.0, 139.8099114, 0.01760249, 139.8099114, 0.05280747, 97.86693798, -1288.92988488, 0.05, 2, 0, 72019, 23019, 1, 3)
    ops.uniaxialMaterial('LimitState', 32019, 34.95247785, 6.926e-05, 104.85743355, 0.00020777, 349.5247785, 0.00069256, -34.95247785, -6.926e-05, -104.85743355, -0.00020777, -349.5247785, -0.00069256, 0.4, 0.3, 0.003, 0.0, 0.0, 12019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2019, 99999, 'P', 42019, 'Vy', 32019, 'Vz', 22019, 'My', 12019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172019, 72019, 172019, 2019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123019, 123019, 23019, 2019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172020, 14.95, 15.8, 6.6)
    ops.node(123020, 14.95, 15.8, 9.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2020, 172020, 123020, 0.0625, 27539782.31906125, 11474909.29960885, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22020, 40.46011317, 0.00128168, 49.11221162, 0.01886543, 4.91122116, 0.06942907, -40.46011317, -0.00128168, -49.11221162, -0.01886543, -4.91122116, -0.06942907, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12020, 37.00873918, 0.00128168, 44.92278661, 0.01886543, 4.49227866, 0.06942907, -37.00873918, -0.00128168, -44.92278661, -0.01886543, -4.49227866, -0.06942907, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22020, 2020, 0.0, 81.0999569, 0.02563361, 81.0999569, 0.07690084, 56.76996983, -1458.36254665, 0.05, 2, 0, 72020, 23020, 2, 3)
    ops.uniaxialMaterial('LimitState', 42020, 20.27498923, 0.00010686, 60.82496768, 0.00032059, 202.74989226, 0.00106862, -20.27498923, -0.00010686, -60.82496768, -0.00032059, -202.74989226, -0.00106862, 0.4, 0.3, 0.003, 0.0, 0.0, 22020, 2)
    ops.limitCurve('ThreePoint', 12020, 2020, 0.0, 81.0999569, 0.02563361, 81.0999569, 0.07690084, 56.76996983, -1458.36254665, 0.05, 2, 0, 72020, 23020, 1, 3)
    ops.uniaxialMaterial('LimitState', 32020, 20.27498923, 0.00010686, 60.82496768, 0.00032059, 202.74989226, 0.00106862, -20.27498923, -0.00010686, -60.82496768, -0.00032059, -202.74989226, -0.00106862, 0.4, 0.3, 0.003, 0.0, 0.0, 12020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2020, 99999, 'P', 42020, 'Vy', 32020, 'Vz', 22020, 'My', 12020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172020, 72020, 172020, 2020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123020, 123020, 23020, 2020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173003, 9.0, 0.0, 9.75)
    ops.node(124003, 9.0, 0.0, 12.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3003, 173003, 124003, 0.16, 26181098.34604938, 10908790.97752057, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23003, 108.75274875, 0.00087369, 133.35397179, 0.01530407, 13.33539718, 0.04747985, -108.75274875, -0.00087369, -133.35397179, -0.01530407, -13.33539718, -0.04747985, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13003, 108.75274875, 0.00087369, 133.35397179, 0.01530407, 13.33539718, 0.04747985, -108.75274875, -0.00087369, -133.35397179, -0.01530407, -13.33539718, -0.04747985, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23003, 3003, 0.0, 114.81335276, 0.01747386, 114.81335276, 0.05242157, 80.36934693, -1838.6287066, 0.05, 2, 0, 73003, 24003, 2, 3)
    ops.uniaxialMaterial('LimitState', 43003, 28.70333819, 6.216e-05, 86.11001457, 0.00018649, 287.03338191, 0.00062162, -28.70333819, -6.216e-05, -86.11001457, -0.00018649, -287.03338191, -0.00062162, 0.4, 0.3, 0.003, 0.0, 0.0, 23003, 2)
    ops.limitCurve('ThreePoint', 13003, 3003, 0.0, 114.81335276, 0.01747386, 114.81335276, 0.05242157, 80.36934693, -1838.6287066, 0.05, 2, 0, 73003, 24003, 1, 3)
    ops.uniaxialMaterial('LimitState', 33003, 28.70333819, 6.216e-05, 86.11001457, 0.00018649, 287.03338191, 0.00062162, -28.70333819, -6.216e-05, -86.11001457, -0.00018649, -287.03338191, -0.00062162, 0.4, 0.3, 0.003, 0.0, 0.0, 13003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3003, 99999, 'P', 43003, 'Vy', 33003, 'Vz', 23003, 'My', 13003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173003, 73003, 173003, 3003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124003, 124003, 24003, 3003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173004, 14.95, 0.0, 9.75)
    ops.node(124004, 14.95, 0.0, 12.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3004, 173004, 124004, 0.0625, 27173540.72653969, 11322308.6360582, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23004, 33.88428605, 0.00120451, 41.44326127, 0.02032598, 4.14432613, 0.08209058, -33.88428605, -0.00120451, -41.44326127, -0.02032598, -4.14432613, -0.08209058, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13004, 30.3691494, 0.00120451, 37.14396081, 0.02032598, 3.71439608, 0.08209058, -30.3691494, -0.00120451, -37.14396081, -0.02032598, -3.71439608, -0.08209058, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23004, 3004, 0.0, 72.9362118, 0.02409021, 72.9362118, 0.07227062, 51.05534826, -2971.83582672, 0.05, 2, 0, 73004, 24004, 2, 3)
    ops.uniaxialMaterial('LimitState', 43004, 18.23405295, 9.74e-05, 54.70215885, 0.0002922, 182.34052949, 0.000974, -18.23405295, -9.74e-05, -54.70215885, -0.0002922, -182.34052949, -0.000974, 0.4, 0.3, 0.003, 0.0, 0.0, 23004, 2)
    ops.limitCurve('ThreePoint', 13004, 3004, 0.0, 72.9362118, 0.02409021, 72.9362118, 0.07227062, 51.05534826, -2971.83582672, 0.05, 2, 0, 73004, 24004, 1, 3)
    ops.uniaxialMaterial('LimitState', 33004, 18.23405295, 9.74e-05, 54.70215885, 0.0002922, 182.34052949, 0.000974, -18.23405295, -9.74e-05, -54.70215885, -0.0002922, -182.34052949, -0.000974, 0.4, 0.3, 0.003, 0.0, 0.0, 13004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3004, 99999, 'P', 43004, 'Vy', 33004, 'Vz', 23004, 'My', 13004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173004, 73004, 173004, 3004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124004, 124004, 24004, 3004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173005, 0.0, 3.95, 9.8)
    ops.node(124005, 0.0, 3.95, 12.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3005, 173005, 124005, 0.0625, 26517997.71690856, 11049165.71537857, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23005, 24.63802697, 0.00121506, 30.14548834, 0.02007889, 3.01454883, 0.07981479, -24.63802697, -0.00121506, -30.14548834, -0.02007889, -3.01454883, -0.07981479, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13005, 24.63802697, 0.00121506, 30.14548834, 0.02007889, 3.01454883, 0.07981479, -24.63802697, -0.00121506, -30.14548834, -0.02007889, -3.01454883, -0.07981479, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23005, 3005, 0.0, 74.00711797, 0.0243011, 74.00711797, 0.07290331, 51.80498258, -2586.82506491, 0.05, 2, 0, 73005, 24005, 2, 3)
    ops.uniaxialMaterial('LimitState', 43005, 18.50177949, 0.00010127, 55.50533848, 0.00030382, 185.01779492, 0.00101273, -18.50177949, -0.00010127, -55.50533848, -0.00030382, -185.01779492, -0.00101273, 0.4, 0.3, 0.003, 0.0, 0.0, 23005, 2)
    ops.limitCurve('ThreePoint', 13005, 3005, 0.0, 74.00711797, 0.0243011, 74.00711797, 0.07290331, 51.80498258, -2586.82506491, 0.05, 2, 0, 73005, 24005, 1, 3)
    ops.uniaxialMaterial('LimitState', 33005, 18.50177949, 0.00010127, 55.50533848, 0.00030382, 185.01779492, 0.00101273, -18.50177949, -0.00010127, -55.50533848, -0.00030382, -185.01779492, -0.00101273, 0.4, 0.3, 0.003, 0.0, 0.0, 13005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3005, 99999, 'P', 43005, 'Vy', 33005, 'Vz', 23005, 'My', 13005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173005, 73005, 173005, 3005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124005, 124005, 24005, 3005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173006, 3.05, 3.95, 9.8)
    ops.node(124006, 3.05, 3.95, 12.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3006, 173006, 124006, 0.16, 29899798.5694064, 12458249.40391933, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23006, 110.85548449, 0.00086156, 134.69701959, 0.01443088, 13.46970196, 0.0468486, -110.85548449, -0.00086156, -134.69701959, -0.01443088, -13.46970196, -0.0468486, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13006, 110.85548449, 0.00086156, 134.69701959, 0.01443088, 13.46970196, 0.0468486, -110.85548449, -0.00086156, -134.69701959, -0.01443088, -13.46970196, -0.0468486, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23006, 3006, 0.0, 133.82901585, 0.0172312, 133.82901585, 0.0516936, 93.6803111, -1556.09330755, 0.05, 2, 0, 73006, 24006, 2, 3)
    ops.uniaxialMaterial('LimitState', 43006, 33.45725396, 6.345e-05, 100.37176189, 0.00019034, 334.57253963, 0.00063446, -33.45725396, -6.345e-05, -100.37176189, -0.00019034, -334.57253963, -0.00063446, 0.4, 0.3, 0.003, 0.0, 0.0, 23006, 2)
    ops.limitCurve('ThreePoint', 13006, 3006, 0.0, 133.82901585, 0.0172312, 133.82901585, 0.0516936, 93.6803111, -1556.09330755, 0.05, 2, 0, 73006, 24006, 1, 3)
    ops.uniaxialMaterial('LimitState', 33006, 33.45725396, 6.345e-05, 100.37176189, 0.00019034, 334.57253963, 0.00063446, -33.45725396, -6.345e-05, -100.37176189, -0.00019034, -334.57253963, -0.00063446, 0.4, 0.3, 0.003, 0.0, 0.0, 13006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3006, 99999, 'P', 43006, 'Vy', 33006, 'Vz', 23006, 'My', 13006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173006, 73006, 173006, 3006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124006, 124006, 24006, 3006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173007, 9.0, 3.95, 9.8)
    ops.node(124007, 9.0, 3.95, 12.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3007, 173007, 124007, 0.25, 29353960.10187443, 12230816.70911434, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23007, 193.09140893, 0.00072332, 235.07393135, 0.01400658, 23.50739313, 0.04287546, -193.09140893, -0.00072332, -235.07393135, -0.01400658, -23.50739313, -0.04287546, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13007, 177.38387291, 0.00072332, 215.95121499, 0.01400658, 21.5951215, 0.04287546, -177.38387291, -0.00072332, -215.95121499, -0.01400658, -21.5951215, -0.04287546, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23007, 3007, 0.0, 191.69018996, 0.01446636, 191.69018996, 0.04339907, 134.18313297, -1978.44138863, 0.05, 2, 0, 73007, 24007, 2, 3)
    ops.uniaxialMaterial('LimitState', 43007, 47.92254749, 5.924e-05, 143.76764247, 0.00017773, 479.22547491, 0.00059243, -47.92254749, -5.924e-05, -143.76764247, -0.00017773, -479.22547491, -0.00059243, 0.4, 0.3, 0.003, 0.0, 0.0, 23007, 2)
    ops.limitCurve('ThreePoint', 13007, 3007, 0.0, 191.69018996, 0.01446636, 191.69018996, 0.04339907, 134.18313297, -1978.44138863, 0.05, 2, 0, 73007, 24007, 1, 3)
    ops.uniaxialMaterial('LimitState', 33007, 47.92254749, 5.924e-05, 143.76764247, 0.00017773, 479.22547491, 0.00059243, -47.92254749, -5.924e-05, -143.76764247, -0.00017773, -479.22547491, -0.00059243, 0.4, 0.3, 0.003, 0.0, 0.0, 13007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3007, 99999, 'P', 43007, 'Vy', 33007, 'Vz', 23007, 'My', 13007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173007, 73007, 173007, 3007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124007, 124007, 24007, 3007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173008, 14.95, 3.95, 9.8)
    ops.node(124008, 14.95, 3.95, 12.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3008, 173008, 124008, 0.1225, 28446412.30822515, 11852671.79509382, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23008, 92.53791211, 0.00093071, 112.87016088, 0.02737583, 11.28701609, 0.08451541, -92.53791211, -0.00093071, -112.87016088, -0.02737583, -11.28701609, -0.08451541, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13008, 81.45478862, 0.00093071, 99.35187521, 0.02737583, 9.93518752, 0.08451541, -81.45478862, -0.00093071, -99.35187521, -0.02737583, -9.93518752, -0.08451541, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23008, 3008, 0.0, 141.30971633, 0.01861423, 141.30971633, 0.0558427, 98.91680143, -5110.76092433, 0.05, 2, 0, 73008, 24008, 2, 3)
    ops.uniaxialMaterial('LimitState', 43008, 35.32742908, 9.197e-05, 105.98228725, 0.00027591, 353.27429082, 0.00091971, -35.32742908, -9.197e-05, -105.98228725, -0.00027591, -353.27429082, -0.00091971, 0.4, 0.3, 0.003, 0.0, 0.0, 23008, 2)
    ops.limitCurve('ThreePoint', 13008, 3008, 0.0, 141.30971633, 0.01861423, 141.30971633, 0.0558427, 98.91680143, -5110.76092433, 0.05, 2, 0, 73008, 24008, 1, 3)
    ops.uniaxialMaterial('LimitState', 33008, 35.32742908, 9.197e-05, 105.98228725, 0.00027591, 353.27429082, 0.00091971, -35.32742908, -9.197e-05, -105.98228725, -0.00027591, -353.27429082, -0.00091971, 0.4, 0.3, 0.003, 0.0, 0.0, 13008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3008, 99999, 'P', 43008, 'Vy', 33008, 'Vz', 23008, 'My', 13008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173008, 73008, 173008, 3008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124008, 124008, 24008, 3008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173009, 0.0, 7.9, 9.8)
    ops.node(124009, 0.0, 7.9, 12.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3009, 173009, 124009, 0.0625, 27951959.79522955, 11646649.91467898, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23009, 23.64528461, 0.00123927, 28.87906798, 0.01962011, 2.8879068, 0.0822408, -23.64528461, -0.00123927, -28.87906798, -0.01962011, -2.8879068, -0.0822408, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13009, 23.64528461, 0.00123927, 28.87906798, 0.01962011, 2.8879068, 0.0822408, -23.64528461, -0.00123927, -28.87906798, -0.01962011, -2.8879068, -0.0822408, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23009, 3009, 0.0, 74.37365451, 0.02478544, 74.37365451, 0.07435632, 52.06155816, -3236.82154299, 0.05, 2, 0, 73009, 24009, 2, 3)
    ops.uniaxialMaterial('LimitState', 43009, 18.59341363, 9.655e-05, 55.78024089, 0.00028966, 185.93413629, 0.00096554, -18.59341363, -9.655e-05, -55.78024089, -0.00028966, -185.93413629, -0.00096554, 0.4, 0.3, 0.003, 0.0, 0.0, 23009, 2)
    ops.limitCurve('ThreePoint', 13009, 3009, 0.0, 74.37365451, 0.02478544, 74.37365451, 0.07435632, 52.06155816, -3236.82154299, 0.05, 2, 0, 73009, 24009, 1, 3)
    ops.uniaxialMaterial('LimitState', 33009, 18.59341363, 9.655e-05, 55.78024089, 0.00028966, 185.93413629, 0.00096554, -18.59341363, -9.655e-05, -55.78024089, -0.00028966, -185.93413629, -0.00096554, 0.4, 0.3, 0.003, 0.0, 0.0, 13009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3009, 99999, 'P', 43009, 'Vy', 33009, 'Vz', 23009, 'My', 13009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173009, 73009, 173009, 3009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124009, 124009, 24009, 3009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173010, 3.05, 7.9, 9.8)
    ops.node(124010, 3.05, 7.9, 12.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3010, 173010, 124010, 0.16, 28344022.70482242, 11810009.46034267, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23010, 112.29233919, 0.00088323, 137.01418131, 0.02020791, 13.70141813, 0.05897678, -112.29233919, -0.00088323, -137.01418131, -0.02020791, -13.70141813, -0.05897678, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13010, 112.29233919, 0.00088323, 137.01418131, 0.02020791, 13.70141813, 0.05897678, -112.29233919, -0.00088323, -137.01418131, -0.02020791, -13.70141813, -0.05897678, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23010, 3010, 0.0, 141.0379362, 0.01766451, 141.0379362, 0.05299353, 98.72655534, -2702.5946121, 0.05, 2, 0, 73010, 24010, 2, 3)
    ops.uniaxialMaterial('LimitState', 43010, 35.25948405, 7.053e-05, 105.77845215, 0.0002116, 352.5948405, 0.00070534, -35.25948405, -7.053e-05, -105.77845215, -0.0002116, -352.5948405, -0.00070534, 0.4, 0.3, 0.003, 0.0, 0.0, 23010, 2)
    ops.limitCurve('ThreePoint', 13010, 3010, 0.0, 141.0379362, 0.01766451, 141.0379362, 0.05299353, 98.72655534, -2702.5946121, 0.05, 2, 0, 73010, 24010, 1, 3)
    ops.uniaxialMaterial('LimitState', 33010, 35.25948405, 7.053e-05, 105.77845215, 0.0002116, 352.5948405, 0.00070534, -35.25948405, -7.053e-05, -105.77845215, -0.0002116, -352.5948405, -0.00070534, 0.4, 0.3, 0.003, 0.0, 0.0, 13010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3010, 99999, 'P', 43010, 'Vy', 33010, 'Vz', 23010, 'My', 13010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173010, 73010, 173010, 3010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124010, 124010, 24010, 3010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173011, 9.0, 7.9, 9.8)
    ops.node(124011, 9.0, 7.9, 12.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3011, 173011, 124011, 0.25, 26951226.28414627, 11229677.61839428, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23011, 188.46737303, 0.00075334, 230.71808045, 0.01464177, 23.07180805, 0.0430205, -188.46737303, -0.00075334, -230.71808045, -0.01464177, -23.07180805, -0.0430205, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13011, 173.60260669, 0.00075334, 212.52092355, 0.01464177, 21.25209236, 0.0430205, -173.60260669, -0.00075334, -212.52092355, -0.01464177, -21.25209236, -0.0430205, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23011, 3011, 0.0, 175.74072085, 0.01506671, 175.74072085, 0.04520013, 123.0185046, -2053.11890263, 0.05, 2, 0, 73011, 24011, 2, 3)
    ops.uniaxialMaterial('LimitState', 43011, 43.93518021, 5.916e-05, 131.80554064, 0.00017747, 439.35180213, 0.00059156, -43.93518021, -5.916e-05, -131.80554064, -0.00017747, -439.35180213, -0.00059156, 0.4, 0.3, 0.003, 0.0, 0.0, 23011, 2)
    ops.limitCurve('ThreePoint', 13011, 3011, 0.0, 175.74072085, 0.01506671, 175.74072085, 0.04520013, 123.0185046, -2053.11890263, 0.05, 2, 0, 73011, 24011, 1, 3)
    ops.uniaxialMaterial('LimitState', 33011, 43.93518021, 5.916e-05, 131.80554064, 0.00017747, 439.35180213, 0.00059156, -43.93518021, -5.916e-05, -131.80554064, -0.00017747, -439.35180213, -0.00059156, 0.4, 0.3, 0.003, 0.0, 0.0, 13011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3011, 99999, 'P', 43011, 'Vy', 33011, 'Vz', 23011, 'My', 13011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173011, 73011, 173011, 3011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124011, 124011, 24011, 3011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173012, 14.95, 7.9, 9.8)
    ops.node(124012, 14.95, 7.9, 12.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3012, 173012, 124012, 0.1225, 27286947.98524707, 11369561.66051961, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23012, 91.12062569, 0.00097173, 111.42332555, 0.02734989, 11.14233255, 0.08390642, -91.12062569, -0.00097173, -111.42332555, -0.02734989, -11.14233255, -0.08390642, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13012, 80.64904921, 0.00097173, 98.6185641, 0.02734989, 9.86185641, 0.08390642, -80.64904921, -0.00097173, -98.6185641, -0.02734989, -9.86185641, -0.08390642, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23012, 3012, 0.0, 133.39744447, 0.01943462, 133.39744447, 0.05830387, 93.37821113, -4663.69430435, 0.05, 2, 0, 73012, 24012, 2, 3)
    ops.uniaxialMaterial('LimitState', 43012, 33.34936112, 9.051e-05, 100.04808335, 0.00027153, 333.49361117, 0.00090511, -33.34936112, -9.051e-05, -100.04808335, -0.00027153, -333.49361117, -0.00090511, 0.4, 0.3, 0.003, 0.0, 0.0, 23012, 2)
    ops.limitCurve('ThreePoint', 13012, 3012, 0.0, 133.39744447, 0.01943462, 133.39744447, 0.05830387, 93.37821113, -4663.69430435, 0.05, 2, 0, 73012, 24012, 1, 3)
    ops.uniaxialMaterial('LimitState', 33012, 33.34936112, 9.051e-05, 100.04808335, 0.00027153, 333.49361117, 0.00090511, -33.34936112, -9.051e-05, -100.04808335, -0.00027153, -333.49361117, -0.00090511, 0.4, 0.3, 0.003, 0.0, 0.0, 13012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3012, 99999, 'P', 43012, 'Vy', 33012, 'Vz', 23012, 'My', 13012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173012, 73012, 173012, 3012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124012, 124012, 24012, 3012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173013, 0.0, 11.85, 9.8)
    ops.node(124013, 0.0, 11.85, 12.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3013, 173013, 124013, 0.0625, 27786675.74057118, 11577781.55857133, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23013, 23.89517745, 0.0011815, 29.19493891, 0.01970797, 2.91949389, 0.08224524, -23.89517745, -0.0011815, -29.19493891, -0.01970797, -2.91949389, -0.08224524, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13013, 23.89517745, 0.0011815, 29.19493891, 0.01970797, 2.91949389, 0.08224524, -23.89517745, -0.0011815, -29.19493891, -0.01970797, -2.91949389, -0.08224524, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23013, 3013, 0.0, 74.21963714, 0.02363008, 74.21963714, 0.07089025, 51.953746, -3255.47761034, 0.05, 2, 0, 73013, 24013, 2, 3)
    ops.uniaxialMaterial('LimitState', 43013, 18.55490929, 9.693e-05, 55.66472786, 0.00029078, 185.54909286, 0.00096927, -18.55490929, -9.693e-05, -55.66472786, -0.00029078, -185.54909286, -0.00096927, 0.4, 0.3, 0.003, 0.0, 0.0, 23013, 2)
    ops.limitCurve('ThreePoint', 13013, 3013, 0.0, 74.21963714, 0.02363008, 74.21963714, 0.07089025, 51.953746, -3255.47761034, 0.05, 2, 0, 73013, 24013, 1, 3)
    ops.uniaxialMaterial('LimitState', 33013, 18.55490929, 9.693e-05, 55.66472786, 0.00029078, 185.54909286, 0.00096927, -18.55490929, -9.693e-05, -55.66472786, -0.00029078, -185.54909286, -0.00096927, 0.4, 0.3, 0.003, 0.0, 0.0, 13013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3013, 99999, 'P', 43013, 'Vy', 33013, 'Vz', 23013, 'My', 13013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173013, 73013, 173013, 3013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124013, 124013, 24013, 3013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173014, 3.05, 11.85, 9.8)
    ops.node(124014, 3.05, 11.85, 12.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3014, 173014, 124014, 0.16, 27432290.77154844, 11430121.15481185, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23014, 110.42451077, 0.00088336, 135.00630833, 0.02059992, 13.50063083, 0.05907468, -110.42451077, -0.00088336, -135.00630833, -0.02059992, -13.50063083, -0.05907468, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13014, 110.42451077, 0.00088336, 135.00630833, 0.02059992, 13.50063083, 0.05907468, -110.42451077, -0.00088336, -135.00630833, -0.02059992, -13.50063083, -0.05907468, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23014, 3014, 0.0, 136.79077013, 0.01766729, 136.79077013, 0.05300187, 95.75353909, -2692.02128323, 0.05, 2, 0, 73014, 24014, 2, 3)
    ops.uniaxialMaterial('LimitState', 43014, 34.19769253, 7.068e-05, 102.5930776, 0.00021205, 341.97692533, 0.00070683, -34.19769253, -7.068e-05, -102.5930776, -0.00021205, -341.97692533, -0.00070683, 0.4, 0.3, 0.003, 0.0, 0.0, 23014, 2)
    ops.limitCurve('ThreePoint', 13014, 3014, 0.0, 136.79077013, 0.01766729, 136.79077013, 0.05300187, 95.75353909, -2692.02128323, 0.05, 2, 0, 73014, 24014, 1, 3)
    ops.uniaxialMaterial('LimitState', 33014, 34.19769253, 7.068e-05, 102.5930776, 0.00021205, 341.97692533, 0.00070683, -34.19769253, -7.068e-05, -102.5930776, -0.00021205, -341.97692533, -0.00070683, 0.4, 0.3, 0.003, 0.0, 0.0, 13014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3014, 99999, 'P', 43014, 'Vy', 33014, 'Vz', 23014, 'My', 13014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173014, 73014, 173014, 3014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124014, 124014, 24014, 3014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173015, 9.0, 11.85, 9.8)
    ops.node(124015, 9.0, 11.85, 12.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3015, 173015, 124015, 0.25, 26366582.23586136, 10986075.9316089, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23015, 191.72184738, 0.00075533, 234.96798817, 0.01430648, 23.49679882, 0.04253682, -191.72184738, -0.00075533, -234.96798817, -0.01430648, -23.49679882, -0.04253682, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13015, 176.19005674, 0.00075533, 215.93273659, 0.01430648, 21.59327366, 0.04253682, -176.19005674, -0.00075533, -215.93273659, -0.01430648, -21.59327366, -0.04253682, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23015, 3015, 0.0, 170.38576769, 0.01510669, 170.38576769, 0.04532008, 119.27003739, -1980.22666359, 0.05, 2, 0, 73015, 24015, 2, 3)
    ops.uniaxialMaterial('LimitState', 43015, 42.59644192, 5.862e-05, 127.78932577, 0.00017587, 425.96441923, 0.00058625, -42.59644192, -5.862e-05, -127.78932577, -0.00017587, -425.96441923, -0.00058625, 0.4, 0.3, 0.003, 0.0, 0.0, 23015, 2)
    ops.limitCurve('ThreePoint', 13015, 3015, 0.0, 170.38576769, 0.01510669, 170.38576769, 0.04532008, 119.27003739, -1980.22666359, 0.05, 2, 0, 73015, 24015, 1, 3)
    ops.uniaxialMaterial('LimitState', 33015, 42.59644192, 5.862e-05, 127.78932577, 0.00017587, 425.96441923, 0.00058625, -42.59644192, -5.862e-05, -127.78932577, -0.00017587, -425.96441923, -0.00058625, 0.4, 0.3, 0.003, 0.0, 0.0, 13015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3015, 99999, 'P', 43015, 'Vy', 33015, 'Vz', 23015, 'My', 13015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173015, 73015, 173015, 3015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124015, 124015, 24015, 3015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173016, 14.95, 11.85, 9.8)
    ops.node(124016, 14.95, 11.85, 12.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3016, 173016, 124016, 0.1225, 29561045.92235452, 12317102.46764771, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23016, 91.67340043, 0.00095647, 111.50774237, 0.02661286, 11.15077424, 0.08422804, -91.67340043, -0.00095647, -111.50774237, -0.02661286, -11.15077424, -0.08422804, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13016, 81.33798549, 0.00095647, 98.93617001, 0.02661286, 9.893617, 0.08422804, -81.33798549, -0.00095647, -98.93617001, -0.02661286, -9.893617, -0.08422804, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23016, 3016, 0.0, 142.41692892, 0.01912944, 142.41692892, 0.05738833, 99.69185025, -4784.19650774, 0.05, 2, 0, 73016, 24016, 2, 3)
    ops.uniaxialMaterial('LimitState', 43016, 35.60423223, 8.92e-05, 106.81269669, 0.00026759, 356.04232231, 0.00089197, -35.60423223, -8.92e-05, -106.81269669, -0.00026759, -356.04232231, -0.00089197, 0.4, 0.3, 0.003, 0.0, 0.0, 23016, 2)
    ops.limitCurve('ThreePoint', 13016, 3016, 0.0, 142.41692892, 0.01912944, 142.41692892, 0.05738833, 99.69185025, -4784.19650774, 0.05, 2, 0, 73016, 24016, 1, 3)
    ops.uniaxialMaterial('LimitState', 33016, 35.60423223, 8.92e-05, 106.81269669, 0.00026759, 356.04232231, 0.00089197, -35.60423223, -8.92e-05, -106.81269669, -0.00026759, -356.04232231, -0.00089197, 0.4, 0.3, 0.003, 0.0, 0.0, 13016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3016, 99999, 'P', 43016, 'Vy', 33016, 'Vz', 23016, 'My', 13016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173016, 73016, 173016, 3016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124016, 124016, 24016, 3016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173017, 0.0, 15.8, 9.75)
    ops.node(124017, 0.0, 15.8, 12.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3017, 173017, 124017, 0.0625, 27613911.03063542, 11505796.26276476, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23017, 21.87721824, 0.00121884, 26.76820184, 0.02029175, 2.67682018, 0.08477413, -21.87721824, -0.00121884, -26.76820184, -0.02029175, -2.67682018, -0.08477413, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13017, 21.87721824, 0.00121884, 26.76820184, 0.02029175, 2.67682018, 0.08477413, -21.87721824, -0.00121884, -26.76820184, -0.02029175, -2.67682018, -0.08477413, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23017, 3017, 0.0, 72.62260308, 0.02437672, 72.62260308, 0.07313016, 50.83582216, -5418.76450495, 0.05, 2, 0, 73017, 24017, 2, 3)
    ops.uniaxialMaterial('LimitState', 43017, 18.15565077, 9.543e-05, 54.46695231, 0.0002863, 181.5565077, 0.00095435, -18.15565077, -9.543e-05, -54.46695231, -0.0002863, -181.5565077, -0.00095435, 0.4, 0.3, 0.003, 0.0, 0.0, 23017, 2)
    ops.limitCurve('ThreePoint', 13017, 3017, 0.0, 72.62260308, 0.02437672, 72.62260308, 0.07313016, 50.83582216, -5418.76450495, 0.05, 2, 0, 73017, 24017, 1, 3)
    ops.uniaxialMaterial('LimitState', 33017, 18.15565077, 9.543e-05, 54.46695231, 0.0002863, 181.5565077, 0.00095435, -18.15565077, -9.543e-05, -54.46695231, -0.0002863, -181.5565077, -0.00095435, 0.4, 0.3, 0.003, 0.0, 0.0, 13017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3017, 99999, 'P', 43017, 'Vy', 33017, 'Vz', 23017, 'My', 13017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173017, 73017, 173017, 3017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124017, 124017, 24017, 3017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173018, 3.05, 15.8, 9.75)
    ops.node(124018, 3.05, 15.8, 12.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3018, 173018, 124018, 0.1225, 27744747.66448511, 11560311.5268688, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23018, 67.60011152, 0.00086851, 82.63621153, 0.0180885, 8.26362115, 0.06698414, -67.60011152, -0.00086851, -82.63621153, -0.0180885, -8.26362115, -0.06698414, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13018, 56.69231737, 0.00086851, 69.30222783, 0.0180885, 6.93022278, 0.06698414, -56.69231737, -0.00086851, -69.30222783, -0.0180885, -6.93022278, -0.06698414, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23018, 3018, 0.0, 121.13548579, 0.01737011, 121.13548579, 0.05211034, 84.79484006, -4184.99331611, 0.05, 2, 0, 73018, 24018, 2, 3)
    ops.uniaxialMaterial('LimitState', 43018, 30.28387145, 8.083e-05, 90.85161435, 0.0002425, 302.83871449, 0.00080835, -30.28387145, -8.083e-05, -90.85161435, -0.0002425, -302.83871449, -0.00080835, 0.4, 0.3, 0.003, 0.0, 0.0, 23018, 2)
    ops.limitCurve('ThreePoint', 13018, 3018, 0.0, 121.13548579, 0.01737011, 121.13548579, 0.05211034, 84.79484006, -4184.99331611, 0.05, 2, 0, 73018, 24018, 1, 3)
    ops.uniaxialMaterial('LimitState', 33018, 30.28387145, 8.083e-05, 90.85161435, 0.0002425, 302.83871449, 0.00080835, -30.28387145, -8.083e-05, -90.85161435, -0.0002425, -302.83871449, -0.00080835, 0.4, 0.3, 0.003, 0.0, 0.0, 13018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3018, 99999, 'P', 43018, 'Vy', 33018, 'Vz', 23018, 'My', 13018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173018, 73018, 173018, 3018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124018, 124018, 24018, 3018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173019, 9.0, 15.8, 9.75)
    ops.node(124019, 9.0, 15.8, 12.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3019, 173019, 124019, 0.16, 27358059.12289379, 11399191.30120574, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23019, 107.29496302, 0.00087639, 131.2594333, 0.01537742, 13.12594333, 0.04786456, -107.29496302, -0.00087639, -131.2594333, -0.01537742, -13.12594333, -0.04786456, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13019, 107.29496302, 0.00087639, 131.2594333, 0.01537742, 13.12594333, 0.04786456, -107.29496302, -0.00087639, -131.2594333, -0.01537742, -13.12594333, -0.04786456, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23019, 3019, 0.0, 121.15296784, 0.01752776, 121.15296784, 0.05258328, 84.80707749, -1921.85404488, 0.05, 2, 0, 73019, 24019, 2, 3)
    ops.uniaxialMaterial('LimitState', 43019, 30.28824196, 6.277e-05, 90.86472588, 0.00018832, 302.8824196, 0.00062773, -30.28824196, -6.277e-05, -90.86472588, -0.00018832, -302.8824196, -0.00062773, 0.4, 0.3, 0.003, 0.0, 0.0, 23019, 2)
    ops.limitCurve('ThreePoint', 13019, 3019, 0.0, 121.15296784, 0.01752776, 121.15296784, 0.05258328, 84.80707749, -1921.85404488, 0.05, 2, 0, 73019, 24019, 1, 3)
    ops.uniaxialMaterial('LimitState', 33019, 30.28824196, 6.277e-05, 90.86472588, 0.00018832, 302.8824196, 0.00062773, -30.28824196, -6.277e-05, -90.86472588, -0.00018832, -302.8824196, -0.00062773, 0.4, 0.3, 0.003, 0.0, 0.0, 13019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3019, 99999, 'P', 43019, 'Vy', 33019, 'Vz', 23019, 'My', 13019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173019, 73019, 173019, 3019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124019, 124019, 24019, 3019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173020, 14.95, 15.8, 9.75)
    ops.node(124020, 14.95, 15.8, 12.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3020, 173020, 124020, 0.0625, 27205570.22213296, 11335654.25922207, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23020, 34.13144812, 0.00120703, 41.74287101, 0.02077881, 4.1742871, 0.0825629, -34.13144812, -0.00120703, -41.74287101, -0.02077881, -4.1742871, -0.0825629, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13020, 30.57016536, 0.00120703, 37.38741073, 0.02077881, 3.73874107, 0.0825629, -30.57016536, -0.00120703, -37.38741073, -0.02077881, -3.73874107, -0.0825629, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23020, 3020, 0.0, 74.66884863, 0.02414051, 74.66884863, 0.07242154, 52.26819404, -3184.47838481, 0.05, 2, 0, 73020, 24020, 2, 3)
    ops.uniaxialMaterial('LimitState', 43020, 18.66721216, 9.96e-05, 56.00163647, 0.00029879, 186.67212156, 0.00099597, -18.66721216, -9.96e-05, -56.00163647, -0.00029879, -186.67212156, -0.00099597, 0.4, 0.3, 0.003, 0.0, 0.0, 23020, 2)
    ops.limitCurve('ThreePoint', 13020, 3020, 0.0, 74.66884863, 0.02414051, 74.66884863, 0.07242154, 52.26819404, -3184.47838481, 0.05, 2, 0, 73020, 24020, 1, 3)
    ops.uniaxialMaterial('LimitState', 33020, 18.66721216, 9.96e-05, 56.00163647, 0.00029879, 186.67212156, 0.00099597, -18.66721216, -9.96e-05, -56.00163647, -0.00029879, -186.67212156, -0.00099597, 0.4, 0.3, 0.003, 0.0, 0.0, 13020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3020, 99999, 'P', 43020, 'Vy', 33020, 'Vz', 23020, 'My', 13020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173020, 73020, 173020, 3020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124020, 124020, 24020, 3020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170001, 0.0, 0.0, 0.0)
    ops.node(124021, 0.0, 0.0, 1.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4052, 170001, 124021, 0.0625, 27498258.771178, 11457607.82132417, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24052, 33.670309, 0.00087961, 40.77187482, 0.01670339, 4.07718748, 0.06361485, -33.670309, -0.00087961, -40.77187482, -0.01670339, -4.07718748, -0.06361485, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14052, 33.670309, 0.00087961, 40.77187482, 0.01670339, 4.07718748, 0.06361485, -33.670309, -0.00087961, -40.77187482, -0.01670339, -4.07718748, -0.06361485, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24052, 4052, 0.0, 82.92675446, 0.01759216, 82.92675446, 0.05277647, 58.04872812, -2658.74754207, 0.05, 2, 0, 70001, 24021, 2, 3)
    ops.uniaxialMaterial('LimitState', 44052, 20.73168861, 5.472e-05, 62.19506584, 0.00016415, 207.31688614, 0.00054717, -20.73168861, -5.472e-05, -62.19506584, -0.00016415, -207.31688614, -0.00054717, 0.4, 0.3, 0.003, 0.0, 0.0, 24052, 2)
    ops.limitCurve('ThreePoint', 14052, 4052, 0.0, 82.92675446, 0.01759216, 82.92675446, 0.05277647, 58.04872812, -2658.74754207, 0.05, 2, 0, 70001, 24021, 1, 3)
    ops.uniaxialMaterial('LimitState', 34052, 20.73168861, 5.472e-05, 62.19506584, 0.00016415, 207.31688614, 0.00054717, -20.73168861, -5.472e-05, -62.19506584, -0.00016415, -207.31688614, -0.00054717, 0.4, 0.3, 0.003, 0.0, 0.0, 14052, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4052, 99999, 'P', 44052, 'Vy', 34052, 'Vz', 24052, 'My', 14052, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170001, 70001, 170001, 4052, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124021, 124021, 24021, 4052, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174021, 0.0, 0.0, 1.775)
    ops.node(121001, 0.0, 0.0, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4053, 174021, 121001, 0.0625, 28548679.90146926, 11895283.29227886, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24053, 32.20035928, 0.00086954, 39.01146406, 0.01735929, 3.90114641, 0.06887741, -32.20035928, -0.00086954, -39.01146406, -0.01735929, -3.90114641, -0.06887741, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14053, 32.20035928, 0.00086954, 39.01146406, 0.01735929, 3.90114641, 0.06887741, -32.20035928, -0.00086954, -39.01146406, -0.01735929, -3.90114641, -0.06887741, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24053, 4053, 0.0, 83.13311962, 0.01739075, 83.13311962, 0.05217225, 58.19318374, -2789.71679239, 0.05, 2, 0, 74021, 21001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44053, 20.78327991, 5.283e-05, 62.34983972, 0.0001585, 207.83279905, 0.00052835, -20.78327991, -5.283e-05, -62.34983972, -0.0001585, -207.83279905, -0.00052835, 0.4, 0.3, 0.003, 0.0, 0.0, 24053, 2)
    ops.limitCurve('ThreePoint', 14053, 4053, 0.0, 83.13311962, 0.01739075, 83.13311962, 0.05217225, 58.19318374, -2789.71679239, 0.05, 2, 0, 74021, 21001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34053, 20.78327991, 5.283e-05, 62.34983972, 0.0001585, 207.83279905, 0.00052835, -20.78327991, -5.283e-05, -62.34983972, -0.0001585, -207.83279905, -0.00052835, 0.4, 0.3, 0.003, 0.0, 0.0, 14053, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4053, 99999, 'P', 44053, 'Vy', 34053, 'Vz', 24053, 'My', 14053, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174021, 74021, 174021, 4053, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121001, 121001, 21001, 4053, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170002, 3.05, 0.0, 0.0)
    ops.node(124022, 3.05, 0.0, 1.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4054, 170002, 124022, 0.2025, 28268445.41777076, 11778518.92407115, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24054, 214.23387734, 0.00064351, 259.70313705, 0.02475851, 25.9703137, 0.07303517, -214.23387734, -0.00064351, -259.70313705, -0.02475851, -25.9703137, -0.07303517, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14054, 222.59005961, 0.00064351, 269.83284565, 0.02475851, 26.98328456, 0.07303517, -222.59005961, -0.00064351, -269.83284565, -0.02475851, -26.98328456, -0.07303517, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24054, 4054, 0.0, 359.7937204, 0.0128701, 359.7937204, 0.03861031, 251.85560428, -8106.69951565, 0.05, 2, 0, 70002, 24022, 2, 3)
    ops.uniaxialMaterial('LimitState', 44054, 89.9484301, 7.128e-05, 269.8452903, 0.00021383, 899.48430099, 0.00071275, -89.9484301, -7.128e-05, -269.8452903, -0.00021383, -899.48430099, -0.00071275, 0.4, 0.3, 0.003, 0.0, 0.0, 24054, 2)
    ops.limitCurve('ThreePoint', 14054, 4054, 0.0, 359.7937204, 0.0128701, 359.7937204, 0.03861031, 251.85560428, -8106.69951565, 0.05, 2, 0, 70002, 24022, 1, 3)
    ops.uniaxialMaterial('LimitState', 34054, 89.9484301, 7.128e-05, 269.8452903, 0.00021383, 899.48430099, 0.00071275, -89.9484301, -7.128e-05, -269.8452903, -0.00021383, -899.48430099, -0.00071275, 0.4, 0.3, 0.003, 0.0, 0.0, 14054, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4054, 99999, 'P', 44054, 'Vy', 34054, 'Vz', 24054, 'My', 14054, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170002, 70002, 170002, 4054, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124022, 124022, 24022, 4054, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174022, 3.05, 0.0, 1.775)
    ops.node(121002, 3.05, 0.0, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4055, 174022, 121002, 0.2025, 27481665.46781997, 11450693.94492499, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24055, 182.9089499, 0.0006338, 222.11297975, 0.01879533, 22.21129798, 0.05734913, -182.9089499, -0.0006338, -222.11297975, -0.01879533, -22.21129798, -0.05734913, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14055, 151.04364814, 0.0006338, 183.41778671, 0.01879533, 18.34177867, 0.05734913, -151.04364814, -0.0006338, -183.41778671, -0.01879533, -18.34177867, -0.05734913, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24055, 4055, 0.0, 317.71511136, 0.01267607, 317.71511136, 0.03802821, 222.40057795, -5850.96367161, 0.05, 2, 0, 74022, 21002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44055, 79.42877784, 6.474e-05, 238.28633352, 0.00019422, 794.28777839, 0.00064742, -79.42877784, -6.474e-05, -238.28633352, -0.00019422, -794.28777839, -0.00064742, 0.4, 0.3, 0.003, 0.0, 0.0, 24055, 2)
    ops.limitCurve('ThreePoint', 14055, 4055, 0.0, 317.71511136, 0.01267607, 317.71511136, 0.03802821, 222.40057795, -5850.96367161, 0.05, 2, 0, 74022, 21002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34055, 79.42877784, 6.474e-05, 238.28633352, 0.00019422, 794.28777839, 0.00064742, -79.42877784, -6.474e-05, -238.28633352, -0.00019422, -794.28777839, -0.00064742, 0.4, 0.3, 0.003, 0.0, 0.0, 14055, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4055, 99999, 'P', 44055, 'Vy', 34055, 'Vz', 24055, 'My', 14055, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174022, 74022, 174022, 4055, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121002, 121002, 21002, 4055, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171001, 0.0, 0.0, 3.45)
    ops.node(124023, 0.0, 0.0, 4.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4057, 171001, 124023, 0.0625, 25944895.63551983, 10810373.1814666, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24057, 30.29865835, 0.00090074, 36.85609459, 0.01764426, 3.68560946, 0.06604148, -30.29865835, -0.00090074, -36.85609459, -0.01764426, -3.68560946, -0.06604148, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14057, 30.29865835, 0.00090074, 36.85609459, 0.01764426, 3.68560946, 0.06604148, -30.29865835, -0.00090074, -36.85609459, -0.01764426, -3.68560946, -0.06604148, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24057, 4057, 0.0, 77.96997724, 0.01801477, 77.96997724, 0.05404431, 54.57898406, -2934.00666378, 0.05, 2, 0, 71001, 24023, 2, 3)
    ops.uniaxialMaterial('LimitState', 44057, 19.49249431, 5.453e-05, 58.47748293, 0.00016358, 194.92494309, 0.00054527, -19.49249431, -5.453e-05, -58.47748293, -0.00016358, -194.92494309, -0.00054527, 0.4, 0.3, 0.003, 0.0, 0.0, 24057, 2)
    ops.limitCurve('ThreePoint', 14057, 4057, 0.0, 77.96997724, 0.01801477, 77.96997724, 0.05404431, 54.57898406, -2934.00666378, 0.05, 2, 0, 71001, 24023, 1, 3)
    ops.uniaxialMaterial('LimitState', 34057, 19.49249431, 5.453e-05, 58.47748293, 0.00016358, 194.92494309, 0.00054527, -19.49249431, -5.453e-05, -58.47748293, -0.00016358, -194.92494309, -0.00054527, 0.4, 0.3, 0.003, 0.0, 0.0, 14057, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4057, 99999, 'P', 44057, 'Vy', 34057, 'Vz', 24057, 'My', 14057, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171001, 71001, 171001, 4057, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124023, 124023, 24023, 4057, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174023, 0.0, 0.0, 4.925)
    ops.node(122001, 0.0, 0.0, 6.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4058, 174023, 122001, 0.0625, 28437746.00914134, 11849060.83714222, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24058, 28.69038196, 0.00084554, 34.85737026, 0.01812353, 3.48573703, 0.07368533, -28.69038196, -0.00084554, -34.85737026, -0.01812353, -3.48573703, -0.07368533, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14058, 28.69038196, 0.00084554, 34.85737026, 0.01812353, 3.48573703, 0.07368533, -28.69038196, -0.00084554, -34.85737026, -0.01812353, -3.48573703, -0.07368533, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24058, 4058, 0.0, 80.21983812, 0.01691087, 80.21983812, 0.0507326, 56.15388669, -3205.60494752, 0.05, 2, 0, 74023, 22001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44058, 20.05495953, 5.118e-05, 60.16487859, 0.00015355, 200.54959531, 0.00051182, -20.05495953, -5.118e-05, -60.16487859, -0.00015355, -200.54959531, -0.00051182, 0.4, 0.3, 0.003, 0.0, 0.0, 24058, 2)
    ops.limitCurve('ThreePoint', 14058, 4058, 0.0, 80.21983812, 0.01691087, 80.21983812, 0.0507326, 56.15388669, -3205.60494752, 0.05, 2, 0, 74023, 22001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34058, 20.05495953, 5.118e-05, 60.16487859, 0.00015355, 200.54959531, 0.00051182, -20.05495953, -5.118e-05, -60.16487859, -0.00015355, -200.54959531, -0.00051182, 0.4, 0.3, 0.003, 0.0, 0.0, 14058, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4058, 99999, 'P', 44058, 'Vy', 34058, 'Vz', 24058, 'My', 14058, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174023, 74023, 174023, 4058, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122001, 122001, 22001, 4058, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171002, 3.05, 0.0, 3.45)
    ops.node(124024, 3.05, 0.0, 4.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4059, 171002, 124024, 0.2025, 27229633.27405487, 11345680.5308562, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24059, 171.589828, 0.00061886, 208.86058721, 0.01900881, 20.88605872, 0.05964367, -171.589828, -0.00061886, -208.86058721, -0.01900881, -20.88605872, -0.05964367, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14059, 138.89608403, 0.00061886, 169.06548604, 0.01900881, 16.9065486, 0.05964367, -138.89608403, -0.00061886, -169.06548604, -0.01900881, -16.9065486, -0.05964367, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24059, 4059, 0.0, 303.9248861, 0.01237719, 303.9248861, 0.03713156, 212.74742027, -6153.87997176, 0.05, 2, 0, 71002, 24024, 2, 3)
    ops.uniaxialMaterial('LimitState', 44059, 75.98122153, 6.25e-05, 227.94366458, 0.00018751, 759.81221526, 0.00062505, -75.98122153, -6.25e-05, -227.94366458, -0.00018751, -759.81221526, -0.00062505, 0.4, 0.3, 0.003, 0.0, 0.0, 24059, 2)
    ops.limitCurve('ThreePoint', 14059, 4059, 0.0, 303.9248861, 0.01237719, 303.9248861, 0.03713156, 212.74742027, -6153.87997176, 0.05, 2, 0, 71002, 24024, 1, 3)
    ops.uniaxialMaterial('LimitState', 34059, 75.98122153, 6.25e-05, 227.94366458, 0.00018751, 759.81221526, 0.00062505, -75.98122153, -6.25e-05, -227.94366458, -0.00018751, -759.81221526, -0.00062505, 0.4, 0.3, 0.003, 0.0, 0.0, 14059, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4059, 99999, 'P', 44059, 'Vy', 34059, 'Vz', 24059, 'My', 14059, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171002, 71002, 171002, 4059, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124024, 124024, 24024, 4059, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174024, 3.05, 0.0, 4.925)
    ops.node(122002, 3.05, 0.0, 6.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4060, 174024, 122002, 0.2025, 27910660.76253617, 11629441.98439007, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24060, 164.9181467, 0.00062393, 200.65076058, 0.01968488, 20.06507606, 0.06180512, -164.9181467, -0.00062393, -200.65076058, -0.01968488, -20.06507606, -0.06180512, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14060, 134.49419481, 0.00062393, 163.63488811, 0.01968488, 16.36348881, 0.06180512, -134.49419481, -0.00062393, -163.63488811, -0.01968488, -16.36348881, -0.06180512, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24060, 4060, 0.0, 309.39844998, 0.01247859, 309.39844998, 0.03743578, 216.57891499, -6513.10598394, 0.05, 2, 0, 74024, 22002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44060, 77.3496125, 6.208e-05, 232.04883749, 0.00018623, 773.49612495, 0.00062078, -77.3496125, -6.208e-05, -232.04883749, -0.00018623, -773.49612495, -0.00062078, 0.4, 0.3, 0.003, 0.0, 0.0, 24060, 2)
    ops.limitCurve('ThreePoint', 14060, 4060, 0.0, 309.39844998, 0.01247859, 309.39844998, 0.03743578, 216.57891499, -6513.10598394, 0.05, 2, 0, 74024, 22002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34060, 77.3496125, 6.208e-05, 232.04883749, 0.00018623, 773.49612495, 0.00062078, -77.3496125, -6.208e-05, -232.04883749, -0.00018623, -773.49612495, -0.00062078, 0.4, 0.3, 0.003, 0.0, 0.0, 14060, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4060, 99999, 'P', 44060, 'Vy', 34060, 'Vz', 24060, 'My', 14060, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174024, 74024, 174024, 4060, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122002, 122002, 22002, 4060, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172001, 0.0, 0.0, 6.6)
    ops.node(124025, 0.0, 0.0, 7.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4062, 172001, 124025, 0.0625, 26159882.08283219, 10899950.86784675, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24062, 27.89138323, 0.00084653, 34.04130854, 0.01862456, 3.40413085, 0.07281871, -27.89138323, -0.00084653, -34.04130854, -0.01862456, -3.40413085, -0.07281871, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14062, 27.89138323, 0.00084653, 34.04130854, 0.01862456, 3.40413085, 0.07281871, -27.89138323, -0.00084653, -34.04130854, -0.01862456, -3.40413085, -0.07281871, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24062, 4062, 0.0, 75.93542872, 0.01693055, 75.93542872, 0.05079165, 53.1548001, -3550.69951331, 0.05, 2, 0, 72001, 24025, 2, 3)
    ops.uniaxialMaterial('LimitState', 44062, 18.98385718, 5.267e-05, 56.95157154, 0.000158, 189.8385718, 0.00052667, -18.98385718, -5.267e-05, -56.95157154, -0.000158, -189.8385718, -0.00052667, 0.4, 0.3, 0.003, 0.0, 0.0, 24062, 2)
    ops.limitCurve('ThreePoint', 14062, 4062, 0.0, 75.93542872, 0.01693055, 75.93542872, 0.05079165, 53.1548001, -3550.69951331, 0.05, 2, 0, 72001, 24025, 1, 3)
    ops.uniaxialMaterial('LimitState', 34062, 18.98385718, 5.267e-05, 56.95157154, 0.000158, 189.8385718, 0.00052667, -18.98385718, -5.267e-05, -56.95157154, -0.000158, -189.8385718, -0.00052667, 0.4, 0.3, 0.003, 0.0, 0.0, 14062, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4062, 99999, 'P', 44062, 'Vy', 34062, 'Vz', 24062, 'My', 14062, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172001, 72001, 172001, 4062, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124025, 124025, 24025, 4062, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174025, 0.0, 0.0, 8.075)
    ops.node(123001, 0.0, 0.0, 9.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4063, 174025, 123001, 0.0625, 28086811.52729093, 11702838.13637122, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24063, 24.40052122, 0.00082413, 29.7544308, 0.01954708, 2.97544308, 0.07989364, -24.40052122, -0.00082413, -29.7544308, -0.01954708, -2.97544308, -0.07989364, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14063, 24.40052122, 0.00082413, 29.7544308, 0.01954708, 2.97544308, 0.07989364, -24.40052122, -0.00082413, -29.7544308, -0.01954708, -2.97544308, -0.07989364, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24063, 4063, 0.0, 76.80067422, 0.0164826, 76.80067422, 0.0494478, 53.76047195, -4679.07629255, 0.05, 2, 0, 74025, 23001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44063, 19.20016855, 4.961e-05, 57.60050566, 0.00014884, 192.00168555, 0.00049613, -19.20016855, -4.961e-05, -57.60050566, -0.00014884, -192.00168555, -0.00049613, 0.4, 0.3, 0.003, 0.0, 0.0, 24063, 2)
    ops.limitCurve('ThreePoint', 14063, 4063, 0.0, 76.80067422, 0.0164826, 76.80067422, 0.0494478, 53.76047195, -4679.07629255, 0.05, 2, 0, 74025, 23001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34063, 19.20016855, 4.961e-05, 57.60050566, 0.00014884, 192.00168555, 0.00049613, -19.20016855, -4.961e-05, -57.60050566, -0.00014884, -192.00168555, -0.00049613, 0.4, 0.3, 0.003, 0.0, 0.0, 14063, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4063, 99999, 'P', 44063, 'Vy', 34063, 'Vz', 24063, 'My', 14063, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174025, 74025, 174025, 4063, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123001, 123001, 23001, 4063, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172002, 3.05, 0.0, 6.6)
    ops.node(124026, 3.05, 0.0, 7.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4064, 172002, 124026, 0.1225, 27499623.79075484, 11458176.57948118, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24064, 86.37091855, 0.000696, 105.05421589, 0.01576761, 10.50542159, 0.05713544, -86.37091855, -0.000696, -105.05421589, -0.01576761, -10.50542159, -0.05713544, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14064, 74.49082912, 0.000696, 90.60428875, 0.01576761, 9.06042887, 0.05713544, -74.49082912, -0.000696, -90.60428875, -0.01576761, -9.06042887, -0.05713544, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24064, 4064, 0.0, 159.45794005, 0.01392003, 159.45794005, 0.0417601, 111.62055804, -3806.06534147, 0.05, 2, 0, 72002, 24026, 2, 3)
    ops.uniaxialMaterial('LimitState', 44064, 39.86448501, 5.368e-05, 119.59345504, 0.00016103, 398.64485013, 0.00053678, -39.86448501, -5.368e-05, -119.59345504, -0.00016103, -398.64485013, -0.00053678, 0.4, 0.3, 0.003, 0.0, 0.0, 24064, 2)
    ops.limitCurve('ThreePoint', 14064, 4064, 0.0, 159.45794005, 0.01392003, 159.45794005, 0.0417601, 111.62055804, -3806.06534147, 0.05, 2, 0, 72002, 24026, 1, 3)
    ops.uniaxialMaterial('LimitState', 34064, 39.86448501, 5.368e-05, 119.59345504, 0.00016103, 398.64485013, 0.00053678, -39.86448501, -5.368e-05, -119.59345504, -0.00016103, -398.64485013, -0.00053678, 0.4, 0.3, 0.003, 0.0, 0.0, 14064, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4064, 99999, 'P', 44064, 'Vy', 34064, 'Vz', 24064, 'My', 14064, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172002, 72002, 172002, 4064, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124026, 124026, 24026, 4064, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174026, 3.05, 0.0, 8.075)
    ops.node(123002, 3.05, 0.0, 9.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4065, 174026, 123002, 0.1225, 27730299.67653756, 11554291.53189065, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24065, 79.14615637, 0.00068753, 96.3436285, 0.01634032, 9.63436285, 0.05941935, -79.14615637, -0.00068753, -96.3436285, -0.01634032, -9.63436285, -0.05941935, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14065, 68.64108095, 0.00068753, 83.55593128, 0.01634032, 8.35559313, 0.05941935, -68.64108095, -0.00068753, -83.55593128, -0.01634032, -8.35559313, -0.05941935, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24065, 4065, 0.0, 157.15825512, 0.01375053, 157.15825512, 0.0412516, 110.01077859, -3991.50222565, 0.05, 2, 0, 74026, 23002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44065, 39.28956378, 5.246e-05, 117.86869134, 0.00015739, 392.89563781, 0.00052464, -39.28956378, -5.246e-05, -117.86869134, -0.00015739, -392.89563781, -0.00052464, 0.4, 0.3, 0.003, 0.0, 0.0, 24065, 2)
    ops.limitCurve('ThreePoint', 14065, 4065, 0.0, 157.15825512, 0.01375053, 157.15825512, 0.0412516, 110.01077859, -3991.50222565, 0.05, 2, 0, 74026, 23002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34065, 39.28956378, 5.246e-05, 117.86869134, 0.00015739, 392.89563781, 0.00052464, -39.28956378, -5.246e-05, -117.86869134, -0.00015739, -392.89563781, -0.00052464, 0.4, 0.3, 0.003, 0.0, 0.0, 14065, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4065, 99999, 'P', 44065, 'Vy', 34065, 'Vz', 24065, 'My', 14065, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174026, 74026, 174026, 4065, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123002, 123002, 23002, 4065, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173001, 0.0, 0.0, 9.75)
    ops.node(124027, 0.0, 0.0, 10.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4067, 173001, 124027, 0.0625, 27558125.32389544, 11482552.21828977, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24067, 23.65868478, 0.00082951, 28.91281189, 0.0195261, 2.89128119, 0.08146608, -23.65868478, -0.00082951, -28.91281189, -0.0195261, -2.89128119, -0.08146608, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14067, 23.65868478, 0.00082951, 28.91281189, 0.0195261, 2.89128119, 0.08146608, -23.65868478, -0.00082951, -28.91281189, -0.0195261, -2.89128119, -0.08146608, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24067, 4067, 0.0, 74.21438863, 0.01659012, 74.21438863, 0.04977035, 51.95007204, -5913.42573952, 0.05, 2, 0, 73001, 24027, 2, 3)
    ops.uniaxialMaterial('LimitState', 44067, 18.55359716, 4.886e-05, 55.66079147, 0.00014659, 185.53597158, 0.00048862, -18.55359716, -4.886e-05, -55.66079147, -0.00014659, -185.53597158, -0.00048862, 0.4, 0.3, 0.003, 0.0, 0.0, 24067, 2)
    ops.limitCurve('ThreePoint', 14067, 4067, 0.0, 74.21438863, 0.01659012, 74.21438863, 0.04977035, 51.95007204, -5913.42573952, 0.05, 2, 0, 73001, 24027, 1, 3)
    ops.uniaxialMaterial('LimitState', 34067, 18.55359716, 4.886e-05, 55.66079147, 0.00014659, 185.53597158, 0.00048862, -18.55359716, -4.886e-05, -55.66079147, -0.00014659, -185.53597158, -0.00048862, 0.4, 0.3, 0.003, 0.0, 0.0, 14067, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4067, 99999, 'P', 44067, 'Vy', 34067, 'Vz', 24067, 'My', 14067, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173001, 73001, 173001, 4067, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124027, 124027, 24027, 4067, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174027, 0.0, 0.0, 11.225)
    ops.node(124001, 0.0, 0.0, 12.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4068, 174027, 124001, 0.0625, 27419561.66541083, 11424817.36058785, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24068, 21.13372457, 0.0007993, 25.89375561, 0.02005676, 2.58937556, 0.08628224, -21.13372457, -0.0007993, -25.89375561, -0.02005676, -2.58937556, -0.08628224, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14068, 21.13372457, 0.0007993, 25.89375561, 0.02005676, 2.58937556, 0.08628224, -21.13372457, -0.0007993, -25.89375561, -0.02005676, -2.58937556, -0.08628224, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24068, 4068, 0.0, 71.20073903, 0.01598608, 71.20073903, 0.04795824, 49.84051732, -34298.21790338, 0.05, 2, 0, 74027, 24001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44068, 17.80018476, 4.711e-05, 53.40055427, 0.00014134, 178.00184758, 0.00047115, -17.80018476, -4.711e-05, -53.40055427, -0.00014134, -178.00184758, -0.00047115, 0.4, 0.3, 0.003, 0.0, 0.0, 24068, 2)
    ops.limitCurve('ThreePoint', 14068, 4068, 0.0, 71.20073903, 0.01598608, 71.20073903, 0.04795824, 49.84051732, -34298.21790338, 0.05, 2, 0, 74027, 24001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34068, 17.80018476, 4.711e-05, 53.40055427, 0.00014134, 178.00184758, 0.00047115, -17.80018476, -4.711e-05, -53.40055427, -0.00014134, -178.00184758, -0.00047115, 0.4, 0.3, 0.003, 0.0, 0.0, 14068, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4068, 99999, 'P', 44068, 'Vy', 34068, 'Vz', 24068, 'My', 14068, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174027, 74027, 174027, 4068, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124001, 124001, 24001, 4068, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173002, 3.05, 0.0, 9.75)
    ops.node(124028, 3.05, 0.0, 10.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4069, 173002, 124028, 0.1225, 27843225.51297492, 11601343.96373955, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24069, 68.70504722, 0.00067469, 83.91287451, 0.01734129, 8.39128745, 0.06531415, -68.70504722, -0.00067469, -83.91287451, -0.01734129, -8.39128745, -0.06531415, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14069, 58.39980695, 0.00067469, 71.32657454, 0.01734129, 7.13265745, 0.06531415, -58.39980695, -0.00067469, -71.32657454, -0.01734129, -7.13265745, -0.06531415, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24069, 4069, 0.0, 148.94620392, 0.01349376, 148.94620392, 0.04048129, 104.26234274, -6615.96829637, 0.05, 2, 0, 73002, 24028, 2, 3)
    ops.uniaxialMaterial('LimitState', 44069, 37.23655098, 4.952e-05, 111.70965294, 0.00014856, 372.36550979, 0.00049521, -37.23655098, -4.952e-05, -111.70965294, -0.00014856, -372.36550979, -0.00049521, 0.4, 0.3, 0.003, 0.0, 0.0, 24069, 2)
    ops.limitCurve('ThreePoint', 14069, 4069, 0.0, 148.94620392, 0.01349376, 148.94620392, 0.04048129, 104.26234274, -6615.96829637, 0.05, 2, 0, 73002, 24028, 1, 3)
    ops.uniaxialMaterial('LimitState', 34069, 37.23655098, 4.952e-05, 111.70965294, 0.00014856, 372.36550979, 0.00049521, -37.23655098, -4.952e-05, -111.70965294, -0.00014856, -372.36550979, -0.00049521, 0.4, 0.3, 0.003, 0.0, 0.0, 14069, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4069, 99999, 'P', 44069, 'Vy', 34069, 'Vz', 24069, 'My', 14069, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173002, 73002, 173002, 4069, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124028, 124028, 24028, 4069, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174028, 3.05, 0.0, 11.225)
    ops.node(124002, 3.05, 0.0, 12.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4070, 174028, 124002, 0.1225, 29385691.93850982, 12244038.30771242, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24070, 68.02436271, 0.00066128, 82.85686406, 0.01699321, 8.28568641, 0.06695682, -68.02436271, -0.00066128, -82.85686406, -0.01699321, -8.28568641, -0.06695682, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14070, 56.94153805, 0.00066128, 69.35746384, 0.01699321, 6.93574638, 0.06695682, -56.94153805, -0.00066128, -69.35746384, -0.01699321, -6.93574638, -0.06695682, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24070, 4070, 0.0, 152.54853563, 0.01322557, 152.54853563, 0.03967671, 106.78397494, -10253.85960167, 0.05, 2, 0, 74028, 24002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44070, 38.13713391, 4.806e-05, 114.41140172, 0.00014417, 381.37133907, 0.00048056, -38.13713391, -4.806e-05, -114.41140172, -0.00014417, -381.37133907, -0.00048056, 0.4, 0.3, 0.003, 0.0, 0.0, 24070, 2)
    ops.limitCurve('ThreePoint', 14070, 4070, 0.0, 152.54853563, 0.01322557, 152.54853563, 0.03967671, 106.78397494, -10253.85960167, 0.05, 2, 0, 74028, 24002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34070, 38.13713391, 4.806e-05, 114.41140172, 0.00014417, 381.37133907, 0.00048056, -38.13713391, -4.806e-05, -114.41140172, -0.00014417, -381.37133907, -0.00048056, 0.4, 0.3, 0.003, 0.0, 0.0, 14070, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4070, 99999, 'P', 44070, 'Vy', 34070, 'Vz', 24070, 'My', 14070, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174028, 74028, 174028, 4070, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124002, 124002, 24002, 4070, '-orient', 0, 0, 1, 0, 1, 0)
